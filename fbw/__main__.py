"""CLI.

  python -m fbw run    --gold gold.jsonl --outputs sys.jsonl --out reports/run1 [--judge-model …] [--mock]
  python -m fbw verify --outputs sys.jsonl --lookup pkg.module:function --out reports/run1 [--mock]
  python -m fbw buckets --gold gold.jsonl --outputs sys.jsonl        (no judge: recall buckets only)
"""

from __future__ import annotations

import argparse
import importlib
import json
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path

from . import __version__
from .citations import citations_for, load_parser
from .judge import MockJudge, OpenAICompatibleJudge
from .metrics import Thresholds
from .refusal import RefusalDetector
from .report import write_reports
from .run import evaluate
from .schema import GoldItem, SystemOutput, read_jsonl, write_jsonl
from .stratify import classify, gold_articles, retrieved_articles
from .verify import verification_table, verify_many


def _judge(args):
    if args.mock:
        return MockJudge()
    return OpenAICompatibleJudge(model=args.judge_model, cache_path=Path(args.out) / "judge_cache.jsonl")


def cmd_run(args) -> int:
    gold = list(read_jsonl(args.gold, GoldItem))
    outputs = list(read_jsonl(args.outputs, SystemOutput))
    if args.max:
        gold = gold[: args.max]
    judge = _judge(args)
    det = RefusalDetector(markers=args.refusal_marker or None)
    t = Thresholds(correctness=args.correctness_gate)
    parser = load_parser(args.citation_parser) if args.citation_parser else None
    records = evaluate(
        gold, outputs, judge, thresholds=t, detector=det,
        with_correctness=not args.no_correctness, with_context_relevancy=not args.no_context_relevancy,
        progress=(lambda i, qid: print(f"  [{i}/{len(gold)}] {qid}", file=sys.stderr)) if args.verbose else None,
        citation_parser=parser,
    )
    meta = {
        "gold": args.gold, "outputs": args.outputs, "judge": judge.model,
        "judge calls": getattr(judge, "calls", "n/a"), "harness": f"fbw-eval {__version__}",
        "thresholds": vars(t), "seed": args.seed,
        "citation parser": args.citation_parser or "built-in [Source: …] tags",
        "gold provenance": sorted({g.provenance for g in gold if g.provenance}) or ["not stated"],
    }
    md, js = write_reports(records, args.out, meta=meta, n_boot=args.n_boot, seed=args.seed)
    write_jsonl(Path(args.out) / "records.jsonl", records)
    print(md.read_text(encoding="utf-8").split("## Per-question")[0])
    print(f"→ {md}\n→ {js}")
    return 0


def cmd_buckets(args) -> int:
    gold = list(read_jsonl(args.gold, GoldItem))
    outs = {o.question_id: o for o in read_jsonl(args.outputs, SystemOutput)}
    c: Counter = Counter()
    for g in gold:
        o = outs.get(g.question_id)
        b = classify(gold_articles(g), retrieved_articles(o.retrieved) if o else set())
        c[b.value] += 1
        if args.verbose:
            print(g.question_id, b.value, sorted(gold_articles(g)), file=sys.stderr)
    for k, v in c.most_common():
        print(f"{k:<18} {v}")
    strat = sum(v for k, v in c.items() if k != "no_gold_articles")
    print(f"stratifiable {strat}/{len(gold)}")
    return 0


def cmd_verify(args) -> int:
    mod, _, fn = args.lookup.partition(":")
    factory = getattr(importlib.import_module(mod), fn or "lookup")
    built = factory()
    lookup, known = built if isinstance(built, tuple) else (built, None)
    outputs = list(read_jsonl(args.outputs, SystemOutput))
    judge = _judge(args)
    parser = load_parser(args.citation_parser) if args.citation_parser else None
    per_system = verify_many(
        judge, lookup,
        ((o.question_id, o.system or "system", o.answer, citations_for(o.answer, o.citations, parser)) for o in outputs),
        known,
    )
    table = verification_table(per_system)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    lines = [f"# Citation verification — {args.outputs}", "", f"Judge: {judge.model}", "", table, "", "## Not supported / not found", ""]
    for s, st in per_system.items():
        for v in st.verdicts:
            if v.outcome in ("unsupported", "not_found"):
                lines.append(f"- {v.question_id} · **{s}** · `{v.raw}` → {v.outcome} — {v.reason}")
    (out / "citations.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    with (out / "citation_verdicts.jsonl").open("w", encoding="utf-8") as f:
        for s, st in per_system.items():
            for v in st.verdicts:
                f.write(json.dumps(asdict(v), ensure_ascii=False) + "\n")
    print(table)
    print(f"→ {out / 'citations.md'}  · {out / 'citation_verdicts.jsonl'} (one verdict per line, with claim + provision text)")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="fbw", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--version", action="version", version=__version__)
    sub = p.add_subparsers(dest="cmd", required=True)

    def common(sp):
        sp.add_argument("--out", default="reports/latest")
        sp.add_argument("--citation-parser", default=None, metavar="MODULE:FUNC",
                        help="replace the built-in [Source: …] parser (answer text → citations); "
                             "explicit `citations` on an output record always win")
        sp.add_argument("--judge-model", default=None, help="OpenAI-compatible model id (default env JUDGE_MODEL)")
        sp.add_argument("--mock", action="store_true", help="deterministic lexical judge: pipeline smoke test only")
        sp.add_argument("-v", "--verbose", action="store_true")

    r = sub.add_parser("run", help="score + stratify a system's outputs against a gold set")
    r.add_argument("--gold", required=True)
    r.add_argument("--outputs", required=True)
    r.add_argument("--max", type=int, default=0)
    r.add_argument("--n-boot", type=int, default=2000)
    r.add_argument("--seed", type=int, default=2026)
    r.add_argument("--refusal-marker", action="append", help="override refusal markers (repeatable)")
    r.add_argument("--correctness-gate", type=float, default=None, help="if set, correctness ≥ this is required to pass")
    r.add_argument("--no-correctness", action="store_true")
    r.add_argument("--no-context-relevancy", action="store_true")
    common(r)
    r.set_defaults(func=cmd_run)

    b = sub.add_parser("buckets", help="recall buckets only (no judge, no key)")
    b.add_argument("--gold", required=True)
    b.add_argument("--outputs", required=True)
    b.add_argument("-v", "--verbose", action="store_true")
    b.set_defaults(func=cmd_buckets)

    v = sub.add_parser("verify", help="verify every citation against your corpus")
    v.add_argument("--outputs", required=True)
    v.add_argument("--lookup", required=True, help="module:factory returning lookup or (lookup, known_source)")
    common(v)
    v.set_defaults(func=cmd_verify)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
