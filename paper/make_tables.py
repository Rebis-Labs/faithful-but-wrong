"""Regenerate the paper's tables from the released per-item records (no API access needed).

Reads <reports>/<set>/{records,citation_verdicts}.jsonl and report.json (bucket figures),
recomputes set-level means with a percentile bootstrap CI (seed 2026, 2000 resamples, the
harness protocol) and writes <out>/<prefix>{numbers.json, tab_main.tex, tab_fc.tex, tab_practice.tex,
tab_verify.tex, tab_judge.tex}. The .tex files define macros (\\vtabmain, \\vtabfc, \\vtabpractice,
\\vtabverify, \\vtabjudge) to \\input in the preamble.

Bucket figures for the benchmark sets come from the post-anchoring re-bucket (`<set>_anchor59/`, same
cached judge verdicts, gold articles anchored to the source text) when that folder exists; set-level
means are identical in both folders and are recomputed from `<set>/records.jsonl`. If the anchored
folder also holds `citation_verdicts.jsonl`, those verdicts are used: they were re-run with the
corrected act lookup (exact display-name match first; 29 Oct), which changed three labour verdicts.

The vanilla baseline (`v2_vanilla_*`: cosine top-3, minimal prompt, same generator, same tag, judge and gold)
shares the rows of tab_main and tab_fc with the grounded system; the case-law variant (`v2_vanillaj_*`) and the
gpt-4o-mini re-judge of the same outputs (`*_judge4omini`) are kept in numbers.json; the latter feeds tab_judge.

Run from the repository root:  python paper/make_tables.py
Paper repo wrapper:            python3 nllp_paper/tools/v2_tables.py  (same code, other paths)
"""

from __future__ import annotations

import argparse
import json
import random
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TAG = "paper-v2-config-2026-10-17"
JUDGE = "anthropic/claude-sonnet-4.6"
JUDGE_4OMINI = "openai/gpt-4o-mini"
ANCHOR_SUFFIX = "_anchor59"
GROUNDED_LABEL = "grounded"
VANILLA_LABEL = "vanilla"

# (folder, label, ground truth, n expected, vanilla folder or None, show in tab_main)
SETS = [
    ("v2_labor_v3", "Labour benchmark", "LLM-drafted, anchored", 78, "v2_vanilla_labor_v3", True),
    ("v2_criminal", "Criminal benchmark", "LLM-drafted, anchored", 30, "v2_vanilla_criminal", True),
    ("v2_admin", "Admin/tax benchmark", "LLM-drafted, anchored", 38, "v2_vanilla_admin", True),
    ("v2_interpelli_lavoro_prassi", "Labour interpelli, practice in corpus", "official reply", 23, "v2_vanilla_interpelli_lavoro", True),
    ("v2_interpelli_lavoro_noprassi", "Labour interpelli, practice removed", "official reply", 23, None, True),
    ("v2_trib2026_prassi", "Tax interpelli 2026, practice in corpus", "official reply", 111, None, True),
    ("v2_trib2026_noprassi", "Tax interpelli 2026, practice removed", "official reply", 111, None, True),
    ("v2_expert", "Expert set, non-circular items", "expert", 5, None, False),  # human verdicts in the paper, not a rate
]
# case-law variant of the vanilla retriever (sensitivity row, numbers.json only)
VANILLAJ = {"v2_labor_v3": "v2_vanillaj_labor_v3", "v2_criminal": "v2_vanillaj_criminal",
            "v2_admin": "v2_vanillaj_admin", "v2_interpelli_lavoro_prassi": "v2_vanillaj_interpelli_lavoro"}
# buckets table: benchmark sets, both systems
FC_SETS = [("v2_labor_v3", "Labour"), ("v2_criminal", "Criminal"), ("v2_admin", "Admin/tax")]

# frontier comparison: (grounded set folder, frontier folder, group label, n). Frontier answers were collected
# once (tax 2026: 17 Oct 2026; benchmark sets: 6-7 Oct 2026) and judged/verified with the same judge, gold
# and corpus as the grounded set. Benchmark rows are a memory test as much as a retrieval test (statutes in training data).
FRONTIER_SETS = [
    ("v2_trib2026_prassi", "v2_frontier_trib2026", "Tax interpelli 2026 (authority-answered, $n{=}111$, ground truth post-dates training)", 111),
    ("v2_admin", "v2_frontier_admin", "Admin/tax benchmark ($n{=}38$)", 38),
    ("v2_labor_v3", "v2_frontier_labor_v3", "Labour benchmark ($n{=}78$)", 78),
    ("v2_criminal", "v2_frontier_criminal", "Criminal benchmark ($n{=}30$)", 30),
]
FRONTIER_MODELS = [  # subfolder, label, model id
    ("chatgpt", "GPT-5.1", "openai/gpt-5.1"),
    ("claude", "Claude Sonnet 4.6", "anthropic/claude-sonnet-4.6"),
    ("gemini", "Gemini 2.5 Pro", "google/gemini-2.5-pro"),
    ("perplexity", "Perplexity sonar-pro (web)", "perplexity/sonar-pro"),
]

# the same outputs.jsonl judged twice: Sonnet 4.6 (paper judge) and gpt-4o-mini (the generator's family);
# `metis/` holds the literal June evaluator on the same outputs (kept in numbers.json, not printed)
JUDGE_SWAP_SETS = [  # sonnet folder, gpt-4o-mini folder, set label, system label
    ("v2_labor_v3", "v2_labor_v3_judge4omini", "Labour benchmark", GROUNDED_LABEL),
    ("v2_vanilla_labor_v3", "v2_vanilla_labor_v3_judge4omini", "", VANILLA_LABEL),
    ("v2_criminal", "v2_criminal_judge4omini", "Criminal benchmark", GROUNDED_LABEL),
    ("v2_vanilla_criminal", "v2_vanilla_criminal_judge4omini", "", VANILLA_LABEL),
    ("v2_admin", "v2_admin_judge4omini", "Admin/tax benchmark", GROUNDED_LABEL),
    ("v2_vanilla_admin", "v2_vanilla_admin_judge4omini", "", VANILLA_LABEL),
]


def jsonl(p: Path) -> list[dict]:
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]


def boot(values: list[float], seed: int = 2026, n: int = 2000) -> tuple[float, float, float]:
    """(mean, lo, hi): percentile bootstrap over items, the harness protocol."""
    if not values:
        return (float("nan"),) * 3
    rng = random.Random(seed)
    m = sum(values) / len(values)
    means = sorted(sum(rng.choice(values) for _ in values) / len(values) for _ in range(n))
    return m, means[int(0.025 * n)], means[int(0.975 * n) - 1]


def pct(x: float) -> str:
    return "--" if x != x else f"{100 * x:.1f}"


def ci(t: tuple[float, float, float]) -> str:
    m, lo, hi = t
    return "--" if m != m else f"{100 * m:.1f} [{100 * lo:.0f}--{100 * hi:.0f}]"


def set_numbers(reports: Path, folder: str) -> dict:
    d = reports / folder
    recs = jsonl(d / "records.jsonl")
    verdicts = jsonl(d / "citation_verdicts.jsonl") if (d / "citation_verdicts.jsonl").exists() else []
    report = json.loads((d / "report.json").read_text(encoding="utf-8"))
    # post-anchoring re-bucket: same judge verdicts, gold anchored to the source text
    bucket_src = folder
    verdicts_src = folder
    anchored = reports / f"{folder}{ANCHOR_SUFFIX}"
    if anchored.is_dir():
        if (anchored / "citation_verdicts.jsonl").exists():  # re-verified with the corrected act lookup
            verdicts = jsonl(anchored / "citation_verdicts.jsonl")
            verdicts_src = f"{folder}{ANCHOR_SUFFIX}"
        a_recs = jsonl(anchored / "records.jsonl")
        for x, y in zip(recs, a_recs):
            assert x["question_id"] == y["question_id"], (folder, x["question_id"], y["question_id"])
            for k in ("correctness", "faithfulness", "passed", "refusal_type"):
                assert x.get(k) == y.get(k), (folder, x["question_id"], k)  # VERIFIED 29 Oct: judge from cache
        report = json.loads((anchored / "report.json").read_text(encoding="utf-8"))
        bucket_src = f"{folder}{ANCHOR_SUFFIX}"
    corr = [r["correctness"] for r in recs if r.get("correctness") is not None]
    faith = [r["faithfulness"] for r in recs if r.get("faithfulness") is not None]
    passed = [1.0 if r.get("passed") else 0.0 for r in recs]
    # passes that are correct refusals (TP): the gate credits them; the "without refusal credit" rate removes them
    passed_no_ref = [1.0 if (r.get("passed") and r.get("refusal_type") != "TP") else 0.0 for r in recs]
    ref = Counter(r.get("refusal_type") for r in recs)
    out = Counter(v.get("outcome") for v in verdicts)
    checkable = out["supported"] + out["unsupported"]
    return {
        "n": len(recs), "n_judged_correctness": len(corr),
        "correctness": boot(corr), "faithfulness": boot(faith), "pass_rate": boot(passed),
        "pass_rate_no_refusal_credit": boot(passed_no_ref), "passes": int(sum(passed)), "passes_from_refusals": int(sum(passed) - sum(passed_no_ref)),
        "refusal_FP": ref["FP"], "refusal_FN": ref["FN"], "refusal_TP": ref["TP"],
        "cited": sum(out.values()), "checkable": checkable, "supported": out["supported"], "unsupported": out["unsupported"],
        "not_found": out["not_found"], "unverifiable": out["unverifiable"], "range_or_list": out["range_or_list"],
        "precision_checkable": (out["supported"] / checkable) if checkable else float("nan"),
        "buckets": {b["bucket"]: b for b in report.get("buckets", [])},
        "coverage": report.get("coverage"), "buckets_from": bucket_src, "verdicts_from": verdicts_src,
        "judge": report["meta"].get("judge"), "harness": report["meta"].get("harness"), "generated": report.get("generated"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--reports", type=Path, default=HERE / "reports")
    ap.add_argument("--out", type=Path, default=HERE / "tables")
    ap.add_argument("--prefix", default="", help="file-name prefix, e.g. v2_")
    ap.add_argument("--self", default="paper/make_tables.py", help="name printed in the generated-by header")
    args = ap.parse_args()
    reports, out, pre = args.reports, args.out, args.prefix
    out.mkdir(exist_ok=True)
    head = f"% generated by {args.self}, do not edit; \\input this file in the preamble and use the macro inside the tabular\n"

    nums = {"tag": TAG, "judge": JUDGE, "sets": {}, "vanilla": {}, "vanilla_caselaw": {}, "frontier": {}, "judge_swap": {}}

    def load(folder: str, n_exp: int, judge: str = JUDGE) -> dict:
        s = set_numbers(reports, folder)
        assert s["judge"] == judge, (folder, s["judge"])
        assert s["n"] == n_exp, (folder, s["n"], n_exp)
        return s

    for folder, label, gt, n_exp, v_folder, _ in SETS:
        s = load(folder, n_exp)
        s["label"], s["ground_truth"] = label, gt
        nums["sets"][folder] = s
        if v_folder and (reports / v_folder).is_dir():
            v = load(v_folder, n_exp)
            v["label"], v["ground_truth"], v["grounded_set"] = label, gt, folder
            nums["vanilla"][v_folder] = v
        vj = VANILLAJ.get(folder)
        if vj and (reports / vj).is_dir():
            j = load(vj, n_exp)
            j["label"], j["grounded_set"] = label, folder
            nums["vanilla_caselaw"][vj] = j

    def vanilla_of(folder: str) -> dict | None:
        for v_folder, v in nums["vanilla"].items():
            if v["grounded_set"] == folder:
                return v
        return None

    # --- main table: set & ground truth & system & n & correctness & faithfulness & pass & pass without refusal credit & FP/FN
    rows = []
    for folder, label, gt, _, _, show in SETS:
        if not show:
            continue
        s = nums["sets"][folder]
        v = vanilla_of(folder)
        if rows:
            rows.append("\\addlinespace[2pt]")
        rows.append(f"{label} & {gt} & {GROUNDED_LABEL} & {s['n']} & {ci(s['correctness'])} & {ci(s['faithfulness'])} & "
                    f"{pct(s['pass_rate'][0])} & {pct(s['pass_rate_no_refusal_credit'][0])} & {s['refusal_FP']}/{s['refusal_FN']} \\\\")
        if v:
            rows.append(f" & & {VANILLA_LABEL} & {v['n']} & {ci(v['correctness'])} & {ci(v['faithfulness'])} & "
                        f"{pct(v['pass_rate'][0])} & {pct(v['pass_rate_no_refusal_credit'][0])} & {v['refusal_FP']}/{v['refusal_FN']} \\\\")
    (out / f"{pre}tab_main.tex").write_text(head + "\\newcommand{\\vtabmain}{%\n" + "\n".join(rows) + "}\n", encoding="utf-8")

    # --- faithful vs correct by bucket (benchmark sets, both systems): domain & system & bucket & n & faithfulness & correctness
    rows = []
    for folder, dom in FC_SETS:
        for s, sys_label in ((nums["sets"][folder], GROUNDED_LABEL), (vanilla_of(folder), VANILLA_LABEL)):
            if s is None:
                continue
            if rows:
                rows.append("\\addlinespace[2pt]")
            first = True
            for bk, name in (("full_recall", "full"), ("zero_recall", "zero")):  # partial-recall buckets (n 1-4) stay in numbers.json
                x = s["buckets"].get(bk)
                if not x:
                    continue
                d_lab = dom if first else ""
                s_lab = sys_label if first else ""
                first = False
                rows.append(f"{d_lab} & {s_lab} & {name} & {x['n']} & {ci(tuple(x['faithfulness']))} & {ci(tuple(x['correctness']))} \\\\")
    (out / f"{pre}tab_fc.tex").write_text(head + "\\newcommand{\\vtabfc}{%\n" + "\n".join(rows) + "}\n", encoding="utf-8")

    # --- practice in/out: set & condition & correctness & faithfulness & refusals (FP) & unverifiable citations & supported/checkable
    rows = []
    for a, b_, label in (("v2_interpelli_lavoro_prassi", "v2_interpelli_lavoro_noprassi", "Labour interpelli ($n{=}23$)"),
                         ("v2_trib2026_prassi", "v2_trib2026_noprassi", "Tax interpelli 2026 ($n{=}111$)")):
        for folder, cond in ((a, "practice in"), (b_, "practice out")):
            s = nums["sets"][folder]
            lab = label if cond == "practice in" else ""
            rows.append(f"{lab} & {cond} & {ci(s['correctness'])} & {ci(s['faithfulness'])} & {s['refusal_FP']} & "
                        f"{s['unverifiable']} & {s['supported']}/{s['checkable']} \\\\")
    (out / f"{pre}tab_practice.tex").write_text(head + "\\newcommand{\\vtabpractice}{%\n" + "\n".join(rows) + "}\n", encoding="utf-8")

    # --- frontier vs grounded, one group per set: system & correctness & FP/FN & cited & checkable (%) & supported & unsupported & not found & unverifiable & supported/cited %
    rows = []
    for g_folder, f_dir, g_label, n_exp in FRONTIER_SETS:
        if not (reports / f_dir).is_dir():
            continue
        group = {"label": g_label, "n": n_exp, "systems": {}}
        if rows:
            rows.append("\\midrule")
        rows.append(f"\\multicolumn{{10}}{{l}}{{\\emph{{{g_label}}}}} \\\\")
        for folder, label, model in [(g_folder, GROUNDED_LABEL, "gpt-4o-mini + retrieval")] + \
                [(f"{f_dir}/{sub}", lab, mid) for sub, lab, mid in FRONTIER_MODELS]:
            s = dict(nums["sets"][folder]) if folder in nums["sets"] else load(folder, n_exp)
            s["label"], s["model"] = label, model
            group["systems"][folder] = s
            chk = f"{s['checkable']} ({100 * s['checkable'] / s['cited']:.0f}\\%)" if s["cited"] else "0"
            sup_all = f"{100 * s['supported'] / s['cited']:.0f}" if s["cited"] else "--"
            rows.append(f"\\quad {label} & {ci(s['correctness'])} & {s['refusal_FP']}/{s['refusal_FN']} & {s['cited']} & {chk} & {s['supported']} & "
                        f"{s['unsupported']} & {s['not_found']} & {s['unverifiable']} & {sup_all} \\\\")
        nums["frontier"][f_dir] = group
    if rows:
        (out / f"{pre}tab_verify.tex").write_text(head + "\\newcommand{\\vtabverify}{%\n" + "\n".join(rows) + "}\n", encoding="utf-8")

    # --- the same outputs under two judges: set & system & n & pass Sonnet & pass gpt-4o-mini & correctness Sonnet & correctness gpt-4o-mini
    rows = []
    for s_folder, j_folder, set_label, sys_label in JUDGE_SWAP_SETS:
        if not (reports / j_folder).is_dir():
            continue
        a = nums["sets"].get(s_folder) or nums["vanilla"].get(s_folder) or load(s_folder, set_numbers(reports, j_folder)["n"])
        b = set_numbers(reports, j_folder)
        assert a["judge"] == JUDGE and b["judge"] == JUDGE_4OMINI and a["n"] == b["n"], (s_folder, j_folder)
        metis = sorted((reports / j_folder / "metis").glob("*.json"))
        metis_pass = json.loads(metis[0].read_text(encoding="utf-8"))["summary"]["overall_pass_rate"] if metis else None
        nums["judge_swap"][s_folder] = {"set": set_label or None, "system": sys_label, "n": a["n"],
                                        "sonnet": {"pass_rate": a["pass_rate"], "correctness": a["correctness"], "faithfulness": a["faithfulness"]},
                                        "gpt4omini": {"pass_rate": b["pass_rate"], "correctness": b["correctness"], "faithfulness": b["faithfulness"]},
                                        "metis_literal_pass": metis_pass, "metis_file": metis[0].name if metis else None}
        rows.append(f"{set_label} & {sys_label} & {a['n']} & {pct(a['pass_rate'][0])} & {pct(b['pass_rate'][0])} & "
                    f"{ci(a['correctness'])} & {ci(b['correctness'])} \\\\")
    if rows:
        (out / f"{pre}tab_judge.tex").write_text(head + "\\newcommand{\\vtabjudge}{%\n" + "\n".join(rows) + "}\n", encoding="utf-8")

    (out / f"{pre}numbers.json").write_text(json.dumps(nums, ensure_ascii=False, indent=1), encoding="utf-8")
    for key in ("sets", "vanilla"):
        for folder, s in nums[key].items():
            print(f"{folder:36s} n={s['n']:3d} corr {ci(s['correctness']):16s} faith {ci(s['faithfulness']):16s} pass {ci(s['pass_rate']):16s} "
                  f"no-ref {pct(s['pass_rate_no_refusal_credit'][0]):5s} FP/FN {s['refusal_FP']}/{s['refusal_FN']} cit {s['cited']}/{s['checkable']}/{s['supported']}"
                  f"  buckets<-{s['buckets_from']} verdicts<-{s['verdicts_from']}")
    for f_dir, g in nums["frontier"].items():
        print(f"frontier group {g['label']}")
        for folder, s in g["systems"].items():
            print(f"  {s['label']:28s} corr {ci(s['correctness']):16s} FP/FN {s['refusal_FP']}/{s['refusal_FN']} cit {s['cited']}/{s['checkable']}/{s['supported']} "
                  f"unsup {s['unsupported']} nf {s['not_found']} unv {s['unverifiable']}  verdicts<-{s['verdicts_from']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
