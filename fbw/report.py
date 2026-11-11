"""Stratified report with bootstrap confidence intervals.

The headline table is per recall bucket: n, pass rate, faithfulness,
correctness, citation accuracy — each with a percentile-bootstrap 95% CI
(seeded, resampling questions). Small buckets get wide intervals; that is the
information, not a nuisance. A second table gives end-task metrics over all
questions, with and without refusal-driven passes.
"""

from __future__ import annotations

import json
import random
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean
from typing import Callable, Optional, Sequence

from .schema import EvalRecord
from .stratify import RECALL_BUCKETS, Bucket


def bootstrap_ci(
    values: Sequence[float], n_boot: int = 2000, seed: int = 2026, alpha: float = 0.05
) -> tuple[Optional[float], Optional[float], Optional[float]]:
    """(mean, lo, hi). Percentile bootstrap over the sample. None if empty."""
    vals = [float(v) for v in values if v is not None]
    if not vals:
        return None, None, None
    if len(vals) == 1:
        return vals[0], vals[0], vals[0]
    rng = random.Random(seed)
    n = len(vals)
    means = sorted(mean(rng.choices(vals, k=n)) for _ in range(n_boot))
    lo = means[int((alpha / 2) * n_boot)]
    hi = means[min(n_boot - 1, int((1 - alpha / 2) * n_boot))]
    return mean(vals), lo, hi


def _fmt(triple: tuple[Optional[float], Optional[float], Optional[float]], pct: bool = True) -> str:
    m, lo, hi = triple
    if m is None:
        return "—"
    if pct:
        return f"{m*100:.1f} [{lo*100:.1f}, {hi*100:.1f}]"
    return f"{m:.3f} [{lo:.3f}, {hi:.3f}]"


def _col(records: Sequence[EvalRecord], get: Callable[[EvalRecord], Optional[float]]) -> list[float]:
    return [v for v in (get(r) for r in records) if v is not None]


def stratified_rows(records: Sequence[EvalRecord], n_boot: int = 2000, seed: int = 2026) -> list[dict]:
    rows = []
    for b in list(RECALL_BUCKETS) + [Bucket.NO_GOLD]:
        rs = [r for r in records if r.bucket == b.value]
        if not rs:
            continue
        rows.append(
            {
                "bucket": b.value,
                "n": len(rs),
                "pass_rate": bootstrap_ci([float(r.passed) for r in rs], n_boot, seed),
                "faithfulness": bootstrap_ci(_col(rs, lambda r: r.faithfulness), n_boot, seed),
                "correctness": bootstrap_ci(_col(rs, lambda r: r.correctness), n_boot, seed),
                "citation_accuracy": bootstrap_ci(_col(rs, lambda r: r.citation_accuracy), n_boot, seed),
                "refusals": sum(r.refused for r in rs),
            }
        )
    return rows


def coverage(records: Sequence[EvalRecord]) -> tuple[int, int]:
    strat = sum(1 for r in records if r.bucket != Bucket.NO_GOLD.value)
    return strat, len(records)


def render_markdown(
    records: Sequence[EvalRecord],
    title: str = "fbw-eval report",
    meta: Optional[dict] = None,
    n_boot: int = 2000,
    seed: int = 2026,
) -> str:
    meta = meta or {}
    strat, total = coverage(records)
    answerable = [r for r in records if not r.should_refuse]
    refusable = [r for r in records if r.should_refuse]
    pass_all = bootstrap_ci([float(r.passed) for r in records], n_boot, seed)
    pass_no_refusal_credit = bootstrap_ci(
        [float(r.passed and not r.refused) for r in records], n_boot, seed
    )
    lines = [
        f"# {title}",
        "",
        f"Generated {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC · "
        f"{total} questions ({len(answerable)} answerable, {len(refusable)} refusable) · "
        f"stratifiable {strat}/{total} ({strat/total*100:.0f}%)" if total else "No records.",
    ]
    for k, v in meta.items():
        lines.append(f"- **{k}:** {v}")
    lines += [
        "",
        "## Recall-conditional table (95% bootstrap CI, questions resampled)",
        "",
        "| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |",
        "|---|--:|--:|--:|--:|--:|--:|",
    ]
    for row in stratified_rows(records, n_boot, seed):
        lines.append(
            f"| {row['bucket']} | {row['n']} | {_fmt(row['pass_rate'])} | {_fmt(row['faithfulness'])} | "
            f"{_fmt(row['correctness'])} | {_fmt(row['citation_accuracy'])} | {row['refusals']} |"
        )
    lines += [
        "",
        "Read across a row: faithfulness that stays high while correctness falls in `zero_recall` "
        "is the failure mode this protocol exists to show. Read down a column: how much of the "
        "aggregate comes from questions the retriever had already solved.",
        "",
        "## End-task metrics (all questions)",
        "",
        "| Metric | value |",
        "|---|--:|",
        f"| pass rate | {_fmt(pass_all)} |",
        f"| pass rate, refusal-driven passes excluded | {_fmt(pass_no_refusal_credit)} |",
        f"| faithfulness (answerable) | {_fmt(bootstrap_ci(_col(answerable, lambda r: r.faithfulness), n_boot, seed))} |",
        f"| correctness (answerable) | {_fmt(bootstrap_ci(_col(answerable, lambda r: r.correctness), n_boot, seed))} |",
        f"| answer relevancy (answerable) | {_fmt(bootstrap_ci(_col(answerable, lambda r: r.answer_relevancy), n_boot, seed))} |",
        f"| context relevancy (answerable) | {_fmt(bootstrap_ci(_col(answerable, lambda r: r.context_relevancy), n_boot, seed))} |",
        f"| citation accuracy (answerable) | {_fmt(bootstrap_ci(_col(answerable, lambda r: r.citation_accuracy), n_boot, seed))} |",
        f"| refusal accuracy | {_fmt(bootstrap_ci([float(r.refusal_type in ('TP', 'TN')) for r in records], n_boot, seed))} |",
        f"| false refusals (FP) / missed refusals (FN) | {sum(r.refusal_type == 'FP' for r in records)} / {sum(r.refusal_type == 'FN' for r in records)} |",
        "",
        "## Per-question",
        "",
        "| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |",
        "|---|---|---|--:|--:|--:|--:|--:|---|",
    ]

    def f(v: Optional[float]) -> str:
        return "—" if v is None else f"{v:.2f}"

    for r in records:
        lines.append(
            f"| {r.question_id} | {r.bucket} | {'⛔' if r.refused else '—'} | {f(r.faithfulness)} | {f(r.correctness)} | "
            f"{f(r.answer_relevancy)} | {f(r.context_relevancy)} | {f(r.citation_accuracy)} | {'✅' if r.passed else '❌'} |"
        )
    errs = [r for r in records if r.errors]
    if errs:
        lines += ["", f"## Errors ({len(errs)})", ""]
        for r in errs:
            lines.append(f"- {r.question_id}: {'; '.join(r.errors)}")
    return "\n".join(lines) + "\n"


def write_reports(records: Sequence[EvalRecord], out_dir: str | Path, meta: Optional[dict] = None, **kw) -> tuple[Path, Path]:
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    md = out / "report.md"
    js = out / "report.json"
    md.write_text(render_markdown(records, meta=meta, **kw), encoding="utf-8")
    rows = stratified_rows(records, kw.get("n_boot", 2000), kw.get("seed", 2026))
    js.write_text(
        json.dumps(
            {
                "generated": datetime.now(timezone.utc).isoformat(),
                "meta": meta or {},
                "coverage": dict(zip(("stratifiable", "total"), coverage(records))),
                "buckets": [
                    {k: (list(v) if isinstance(v, tuple) else v) for k, v in row.items()} for row in rows
                ],
                "records": [r.model_dump() for r in records],
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    return md, js
