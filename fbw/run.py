"""Join gold + outputs, score, stratify."""

from __future__ import annotations

from typing import Iterable, Optional

from . import metrics as M
from .citations import Parser, citations_for
from .judge import Judge
from .refusal import RefusalDetector, refusal_outcome
from .schema import EvalRecord, GoldItem, SystemOutput
from .stratify import classify, gold_articles, retrieved_articles


def evaluate(
    gold: Iterable[GoldItem],
    outputs: Iterable[SystemOutput],
    judge: Judge,
    thresholds: Optional[M.Thresholds] = None,
    detector: Optional[RefusalDetector] = None,
    with_correctness: bool = True,
    with_context_relevancy: bool = True,
    articles_from_text: bool = True,
    progress: Optional[callable] = None,
    citation_parser: Optional[Parser] = None,
) -> list[EvalRecord]:
    t = thresholds or M.Thresholds()
    det = detector or RefusalDetector()
    outs = {o.question_id: o for o in outputs}
    records: list[EvalRecord] = []
    for i, g in enumerate(gold, 1):
        o = outs.get(g.question_id)
        errors: list[str] = []
        if o is None:
            errors.append("no system output for this question")
            o = SystemOutput(question_id=g.question_id, answer="")
        refused = det(o.answer, o.refused)
        ok, rtype = refusal_outcome(refused, g.should_refuse)
        gset = gold_articles(g)
        rset = retrieved_articles(o.retrieved, fallback_to_text=articles_from_text)
        bucket = classify(gset, rset)

        faith = ans_rel = ctx_rel = cit = corr = None
        if not g.should_refuse and not refused:
            for name, fn in (
                ("faithfulness", lambda: M.faithfulness(judge, o.answer, o.retrieved)),
                ("answer_relevancy", lambda: M.answer_relevancy(judge, g.question, o.answer)),
                ("citation_accuracy", lambda: M.citation_accuracy(
                    o.answer, o.retrieved, citations_for(o.answer, o.citations, citation_parser))),
                ("context_relevancy", (lambda: M.context_relevancy(judge, g.question, o.retrieved)) if with_context_relevancy else None),
                ("correctness", (lambda: M.correctness(judge, g.question, o.answer, g.expected_answer)) if with_correctness and g.expected_answer else None),
            ):
                if fn is None:
                    continue
                try:
                    val = fn()
                except Exception as exc:  # noqa: BLE001
                    errors.append(f"{name}: {exc}")
                    continue
                if name == "faithfulness":
                    faith = val
                elif name == "answer_relevancy":
                    ans_rel = val
                elif name == "citation_accuracy":
                    cit = val
                elif name == "context_relevancy":
                    ctx_rel = val
                else:
                    corr = val
        elif refused and not g.should_refuse:
            # A false refusal is scored as faithful/relevant by convention in the
            # reference implementation; here it simply fails the refusal gate.
            faith, ans_rel, cit = 1.0, 1.0, 1.0

        records.append(
            EvalRecord(
                question_id=g.question_id,
                system=o.system,
                domain=g.domain,
                should_refuse=g.should_refuse,
                refused=refused,
                refusal_type=rtype,
                bucket=bucket.value,
                gold_articles=sorted(gset),
                retrieved_articles=sorted(rset),
                context_relevancy=ctx_rel,
                faithfulness=faith,
                answer_relevancy=ans_rel,
                citation_accuracy=cit,
                correctness=corr,
                passed=M.passed(
                    should_refuse=g.should_refuse, refusal_correct=ok, faith=faith, ans_rel=ans_rel,
                    ctx_rel=ctx_rel if with_context_relevancy else 1.0, cit_acc=cit, corr=corr, t=t,
                ),
                errors=errors,
            )
        )
        if progress:
            progress(i, g.question_id)
    return records
