"""Citation verification against a corpus of article texts.

A judge scoring "citation quality" from the answer alone rewards a plausible
"art. 2110 c.c." cited from memory. This module checks each citation against
the real text: the caller supplies `lookup(source, article) -> text | None`
over its own corpus; a judge then reads the article and says whether it
supports the claim made around the citation.

Outcomes per citation:
  supported / unsupported   — article found, judge verdict
  not_found                 — act in corpus, article absent (likely invented)
  unverifiable              — act not in corpus: NOT counted as wrong
  range_or_list             — "artt. 17-20": not a single article, not checked

Two ratios matter: precision on checkable citations (supported / (supported +
unsupported + not_found)) and the checkable share (checkable / cited). A system
that cites a lot from memory looks good on the first only if you ignore the
second.
"""

from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Callable, Iterable, Optional

from .citations import RANGE_OR_LIST_RE, Citation, parse_citations
from .judge import Judge, parse_json
from .metrics import SEP

Lookup = Callable[[str, str], Optional[str]]
"""(source name as cited, normalised article) -> full article text, or None.
Return None both when the act is unknown and when the article is absent; use
`known_source(source) -> bool` to distinguish the two if you can."""


@dataclass
class CitationVerdict:
    question_id: str
    system: str
    raw: str
    outcome: str  # supported | unsupported | not_found | unverifiable | range_or_list
    reason: str = ""
    source: str = ""
    article: str = ""
    claim: str = ""
    """Text around the citation that was shown to the judge (for human re-annotation)."""
    text: str = ""
    """Head of the provision text that was shown to the judge."""


@dataclass
class VerificationStats:
    answers: int = 0
    cited: int = 0
    supported: int = 0
    unsupported: int = 0
    not_found: int = 0
    unverifiable: int = 0
    range_or_list: int = 0
    verdicts: list[CitationVerdict] = field(default_factory=list)

    @property
    def checkable(self) -> int:
        return self.supported + self.unsupported + self.not_found

    @property
    def precision_checkable(self) -> Optional[float]:
        return self.supported / self.checkable if self.checkable else None

    @property
    def checkable_share(self) -> Optional[float]:
        return self.checkable / self.cited if self.cited else None

    @property
    def supported_share(self) -> Optional[float]:
        return self.supported / self.cited if self.cited else None


def _claim_context(answer: str, raw: str, width: int = 350) -> str:
    i = answer.find(raw)
    return answer[:width] if i < 0 else answer[max(0, i - width): i].strip()


def verify_answer(
    judge: Judge,
    lookup: Lookup,
    question_id: str,
    system: str,
    answer: str,
    known_source: Optional[Callable[[str], bool]] = None,
    stats: Optional[VerificationStats] = None,
    citations: Optional[list[Citation]] = None,
) -> VerificationStats:
    st = stats or VerificationStats()
    st.answers += 1
    for cit in (parse_citations(answer or "") if citations is None else citations):
        st.cited += 1
        if RANGE_OR_LIST_RE.search(cit.article or ""):
            st.range_or_list += 1
            st.verdicts.append(CitationVerdict(question_id, system, cit.raw, "range_or_list"))
            continue
        if not cit.article:
            st.unverifiable += 1
            st.verdicts.append(CitationVerdict(question_id, system, cit.raw, "unverifiable", "no article"))
            continue
        text = lookup(cit.source, cit.article)
        if text is None:
            if known_source is not None and known_source(cit.source):
                st.not_found += 1
                st.verdicts.append(CitationVerdict(question_id, system, cit.raw, "not_found", "act in corpus, article absent"))
            else:
                st.unverifiable += 1
                st.verdicts.append(CitationVerdict(question_id, system, cit.raw, "unverifiable", "act not in corpus"))
            continue
        claim = _claim_context(answer, cit.raw)
        prompt = (
            "You are a rigorous legal evaluator. An AI answer cites a provision in support of a claim.\n\n"
            f"CLAIM (text around the citation):\n{claim}{SEP}"
            f"ACTUAL TEXT OF THE CITED PROVISION ({cit.source}, art. {cit.article}):\n{text[:12000]}\n\n"
            'Does the provision, in its actual text, SUPPORT the claim? Return ONLY JSON: {"supported": true/false, "reason": "one sentence"}'
        )
        try:
            j = parse_json(judge.ask(prompt))
            ok = bool(j.get("supported"))
            reason = str(j.get("reason", ""))
        except Exception as exc:  # noqa: BLE001
            ok, reason = False, f"judge error: {exc}"
        if ok:
            st.supported += 1
        else:
            st.unsupported += 1
        st.verdicts.append(CitationVerdict(
            question_id, system, cit.raw, "supported" if ok else "unsupported", reason,
            source=cit.source, article=cit.article, claim=claim, text=text[:4000],
        ))
    return st


def verify_many(
    judge: Judge,
    lookup: Lookup,
    answers: Iterable[tuple],
    known_source: Optional[Callable[[str], bool]] = None,
) -> dict[str, VerificationStats]:
    """answers = iterable of (question_id, system, answer[, citations]). Stats per system.
    The optional 4th element is a pre-resolved citation list (see `citations_for`)."""
    per_system: dict[str, VerificationStats] = defaultdict(VerificationStats)
    for row in answers:
        qid, system, answer = row[0], row[1], row[2]
        cits = row[3] if len(row) > 3 else None
        verify_answer(judge, lookup, qid, system, answer, known_source, per_system[system], citations=cits)
    return dict(per_system)


def verification_table(per_system: dict[str, VerificationStats]) -> str:
    def pct(v: Optional[float]) -> str:
        return "—" if v is None else f"{v*100:.0f}%"

    lines = [
        "| System | answers | cited | checkable | supported | unsupported | not found | range/list | unverifiable | precision (checkable) | supported / cited |",
        "|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|",
    ]
    for s, st in per_system.items():
        lines.append(
            f"| {s} | {st.answers} | {st.cited} | {st.checkable} ({pct(st.checkable_share)}) | {st.supported} | "
            f"**{st.unsupported}** | {st.not_found} | {st.range_or_list} | {st.unverifiable} | "
            f"{pct(st.precision_checkable)} | {pct(st.supported_share)} |"
        )
    return "\n".join(lines)


def simple_lookup_from_dict(articles: dict[tuple[str, str], str]) -> tuple[Lookup, Callable[[str], bool]]:
    """Build (lookup, known_source) from {(source_substring_lower, article): text}.
    Source matching is substring-based both ways, as in the reference implementation."""
    sources = {k[0] for k in articles}

    def _match(source: str) -> list[str]:
        s = source.lower()
        return [src for src in sources if src in s or s in src]

    def lookup(source: str, article: str) -> Optional[str]:
        for src in _match(source):
            if (src, article) in articles:
                return articles[(src, article)]
        return None

    def known(source: str) -> bool:
        return bool(_match(source))

    return lookup, known


_ = re  # keep re imported for callers that extend aliases
