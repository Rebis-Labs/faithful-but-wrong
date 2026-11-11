"""Per-question metrics. All judge prompts end with the JSON they expect.

Two axes are kept deliberately separate:
  faithfulness  — is the answer supported by the contexts the generator saw?
  correctness   — does the answer say what the gold reference says?
A faithful answer to the wrong context scores high on the first and low on
the second; the stratified report makes that visible per recall bucket.

Prompts separate the "subject" (question/answer) from the "evidence" (context/
gold) with a `\\n\\n---\\n\\n` line; MockJudge keys on that.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .citations import Citation, inline_articles, normalize_article, parse_citations
from .judge import Judge, parse_json, parse_score
from .schema import RetrievedChunk

SEP = "\n\n---\n\n"


@dataclass
class Thresholds:
    faithfulness: float = 0.90
    answer_relevancy: float = 0.85
    context_relevancy: float = 0.80
    citation_accuracy: float = 0.90
    correctness: Optional[float] = None
    """None = correctness does not gate `passed` (reference-implementation
    behaviour, where pass = production-grade gate on the four RAG metrics)."""


def context_relevancy(judge: Judge, question: str, chunks: list[RetrievedChunk]) -> float:
    """Share of retrieved chunks that are on the question's topic (retrieval
    quality, not answer completeness)."""
    if not chunks:
        return 0.0
    relevant = 0
    for c in chunks:
        prompt = (
            f"Question: {question}{SEP}Retrieved passage:\n{c.text[:3000]}\n\n"
            "Is this passage RELEVANT to the question? Relevant = it is about the "
            "question's subject or gives useful context on it, even if it does not "
            "fully answer it alone. Not relevant only if its subject is substantially "
            'different.\nReturn ONLY JSON: {"relevant": true or false}'
        )
        try:
            if parse_json(judge.ask(prompt)).get("relevant"):
                relevant += 1
        except Exception:  # noqa: BLE001
            relevant += 1  # permissive on judge error, as in the reference implementation
    return relevant / len(chunks)


def faithfulness(judge: Judge, answer: str, chunks: list[RetrievedChunk], max_chunks: int = 5) -> float:
    """Share of the answer's factual claims explicitly supported by the context."""
    context = "\n\n".join(c.text for c in chunks[:max_chunks])
    prompt = (
        f"Answer:\n{answer}{SEP}Context:\n{context[:12000]}\n\n"
        "Break the answer into individual factual claims. For each claim, check "
        "whether it is EXPLICITLY supported by the context above. A claim is supported "
        "if the context contains the same information, even if worded differently "
        "(e.g. an act's acronym and its full title refer to the same law). Inline "
        "citations like [Source: ...] are formatting, not claims — ignore them. Claims "
        "that add general legal knowledge, doctrine or details not in the context count "
        'as unsupported.\nReturn ONLY JSON: {"total_claims": N, "supported_claims": M, "score": float_0_to_1}'
    )
    return parse_score(judge.ask(prompt))


def answer_relevancy(judge: Judge, question: str, answer: str) -> float:
    prompt = (
        f"Question: {question}{SEP}Answer:\n{answer}\n\n"
        "On a scale from 0.0 to 1.0, how well does the answer address the question? "
        '1.0 = fully addresses, 0.0 = completely off-topic.\nReturn ONLY JSON: {"score": float}'
    )
    return parse_score(judge.ask(prompt))


def correctness(judge: Judge, question: str, answer: str, expected_answer: str) -> float:
    """Agreement with the gold reference, independent of the retrieved context.
    This is the axis faithfulness cannot see."""
    prompt = (
        f"Question: {question}\n\nAI answer:\n{answer}{SEP}Reference answer (gold):\n{expected_answer}\n\n"
        "Does the AI answer provide the same legal information as the reference? "
        "Score 1.0 = same conclusion and same operative elements (articles, amounts, "
        "deadlines, conditions); 0.5 = partially correct or incomplete; 0.0 = wrong, "
        "contradicts the reference, or missing. Extra correct detail is not penalised; "
        'invented specifics are.\nReturn ONLY JSON: {"score": float, "rationale": "one sentence"}'
    )
    return parse_score(judge.ask(prompt))


def citation_accuracy(
    answer: str, chunks: list[RetrievedChunk], citations: Optional[list[Citation]] = None
) -> float:
    """Share of the answer's references that point to a retrieved chunk:
    source name matches a retrieved source AND the article (if any) matches
    that chunk's article metadata or appears in its text. No judge.
    No reference at all in a non-refusal → 0.0 (ungrounded by construction).
    `citations` (from `citations_for`) overrides the built-in tag parser."""
    sources_low = [c.source.lower() for c in chunks]
    arts = [normalize_article(c.article) for c in chunks]

    def _art_ok(art: str, idxs: list[int]) -> bool:
        if not art:
            return True
        for i in idxs:
            if arts[i]:
                if arts[i] == art:
                    return True
            elif art in inline_articles(chunks[i].text):
                return True
        return False

    tags = parse_citations(answer) if citations is None else citations
    if tags:
        ok = 0
        for cit in tags:
            name = cit.source.strip().lower()
            idxs = [i for i, s in enumerate(sources_low) if name and s and (name in s or s in name)]
            if idxs and _art_ok(cit.article, idxs):
                ok += 1
        return ok / len(tags)
    inline = {a for a in inline_articles(answer) if a}
    if not inline:
        return 0.0
    all_idx = list(range(len(chunks)))
    return sum(1 for a in inline if _art_ok(a, all_idx)) / len(inline)


def passed(
    *,
    should_refuse: bool,
    refusal_correct: bool,
    faith: Optional[float],
    ans_rel: Optional[float],
    ctx_rel: Optional[float],
    cit_acc: Optional[float],
    corr: Optional[float],
    t: Thresholds,
) -> bool:
    if should_refuse:
        return refusal_correct
    if not refusal_correct:
        return False
    gates = [
        (faith, t.faithfulness),
        (ans_rel, t.answer_relevancy),
        (ctx_rel, t.context_relevancy),
        (cit_acc, t.citation_accuracy),
    ]
    if t.correctness is not None:
        gates.append((corr, t.correctness))
    return all(v is not None and v >= th for v, th in gates)
