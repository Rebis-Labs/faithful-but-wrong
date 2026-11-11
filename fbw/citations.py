"""Citation parsing and article-identifier normalisation.

Two citation forms are recognised:
  - tagged:  [Source: Codice Civile, art. 2103]   (also "circolare n. 23", "p. 4")
  - inline:  "ai sensi dell'art. 2103 c.c."       (used only if no tag exists)

Normalisation maps "Art. 29 bis", "29-bis", "29bis" → "29-bis" so that gold,
retrieved metadata and cited identifiers compare as strings. Comma/paragraph
suffixes ("18, comma 1") are dropped: the unit of recall is the article.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any, Callable, Optional, Sequence

_SUFFIX = r"(?:bis|ter|quater|quinquies|sexies|septies|octies|novies|decies)"

TAG_RE = re.compile(r"\[Source:\s*(?P<body>[^\]]+?)\s*\]", re.IGNORECASE)
"""One [Source: …] tag. Its body may hold several citations separated by ';' (frontier models do
this: "art. 9, Tariffa, DPR 131/1986; Agenzia delle Entrate, risposta n. 3/E del 13 gennaio 2026")."""

_KINDS = r"(?:circolare|risoluzione|interpello|risposta(?:\s+a(?:d)?\s+interpello)?|messaggio|nota|provvedimento)"
PRASSI_RE = re.compile(
    rf"(?P<kind>{_KINDS})\s*(?:n\.?|n°|numero)?\s*(?P<num>\d+(?:/[A-Z]+)?)"
    r"(?:\s*(?:del|dell'|/)\s*(?P<date>\d{1,2}\s+\w+\s+\d{4}|\d{1,2}/\d{1,2}/\d{4}|\d{4}))?",
    re.IGNORECASE,
)
"""Administrative-practice citation inside a tag body: 'circolare n. 23/E del 19/11/2024',
'risposta n. 3/E del 13 gennaio 2026', 'risoluzione 89/E del 2002', 'interpello n. 1/2019'. The year, when
given, is kept in the identifier (`risposta-3/e/2026`, `interpello-1/2019`): practice numbering restarts every
year, so the number alone is ambiguous."""

PAGE_RE = re.compile(r"\bp\.?\s*(?P<page>\d+)\b", re.IGNORECASE)

# kept for backward compatibility with callers that import it (tests, docs)
CITATION_RE = TAG_RE

INLINE_ART_RE = re.compile(
    rf"\b(?:artt?\.?|articolo|article)\s*(\d+(?:\s*-?\s*{_SUFFIX})?)", re.IGNORECASE
)

RANGE_OR_LIST_RE = re.compile(r"artt\.|\d\s*[-–]\s*\d|\d\s*,\s*\d")


@dataclass(frozen=True)
class Citation:
    source: str
    article: str  # normalised, "" if absent
    raw: str


def normalize_article(raw: str) -> str:
    v = (raw or "").strip().lower()
    v = re.split(r"[,;]|\s+comma\b|\s+co\.|\s+par(?:agrafo)?\.?\s", v)[0]
    v = re.sub(r"^(?:art(?:icolo|icle)?\.?|artt\.?)\s*", "", v)
    v = re.sub(rf"\s*-?\s*({_SUFFIX})\b", r"-\1", v)
    v = re.sub(r"[\s._]+", "-", v).strip("-")
    return v


LIST_RE = re.compile(
    rf"\b(?:artt\.?|articoli)\s*(?P<list>\d+(?:\s*-?\s*{_SUFFIX})?(?:\s*(?:,|e|ed|–|-)\s*\d+(?:\s*-?\s*{_SUFFIX})?)+)",
    re.IGNORECASE,
)
"""'artt. 49 e 51', 'artt. 1-3': a list/range of articles — kept as 'a,b' so verify() reports it
as range_or_list instead of checking a single article."""

_TAIL_RE = re.compile(
    r"^[\s,]*(?:(?:comma|co\.)\s*[\w-]+|c\.\s*\d+|lett(?:era)?\.?\s*[a-z]\)?|par(?:agrafo)?\.?\s*\w+|n\.?\s*\d+\))",
    re.IGNORECASE,
)
"""Comma/letter/paragraph details that follow an article number ('art. 10, comma 1, lett. e)')."""


def _strip_tail(after: str) -> str:
    while True:
        m = _TAIL_RE.match(after)
        if not m:
            return after
        after = after[m.end():]


def _parse_segment(seg: str) -> Optional[Citation]:
    """One citation inside a tag body. Detection order: administrative practice (kind + number)
    → article list → single article → page → bare source."""
    raw = seg.strip(" ,;")
    if not raw:
        return None
    pm = PRASSI_RE.search(raw)
    if pm:
        kind = pm.group("kind").lower().split()[0]           # "risposta a interpello" → "risposta"
        art = f"{kind}-{pm.group('num').strip().lower()}"
        ym = re.search(r"\d{4}", pm.group("date") or "")
        if ym:                                               # the year is part of the identifier:
            art += "/" + ym.group(0)                         # "interpello n. 1/2019" ≠ "interpello n. 1/2024"
        source = (raw[: pm.start()] + " " + raw[pm.end():]).strip(" ,;")
        return Citation(source=source or kind, article=art, raw=raw)
    lm = LIST_RE.search(raw)
    if lm:
        nums = [normalize_article(x) for x in re.split(r"\s*(?:,|\be\b|\bed\b|–|-)\s*", lm.group("list")) if x.strip()]
        source = (raw[: lm.start()] + " " + _strip_tail(raw[lm.end():])).strip(" ,;")
        return Citation(source=re.sub(r"\s{2,}", " ", source), article=",".join(nums), raw=raw)
    am = INLINE_ART_RE.search(raw)
    if am:
        art = normalize_article(am.group(1))
        source = (raw[: am.start()] + " " + _strip_tail(raw[am.end():])).strip(" ,;")
        return Citation(source=re.sub(r"\s{2,}", " ", source), article=art, raw=raw)
    pg = PAGE_RE.search(raw)
    if pg:
        source = (raw[: pg.start()] + " " + raw[pg.end():]).strip(" ,;")
        return Citation(source=source, article="", raw=raw)
    return Citation(source=raw, article="", raw=raw)


def parse_citations(text: str) -> list[Citation]:
    """All citations in `[Source: …]` tags. A tag body is split on ';' into segments, each
    parsed on its own, so a composite tag yields several citations (one per source cited) and
    administrative-practice references are recognised as `kind-number` identifiers that a
    corpus lookup can resolve (e.g. ("Agenzia delle Entrate", "risposta-3/e"))."""
    out: list[Citation] = []
    seen: set[tuple[str, str]] = set()
    for m in TAG_RE.finditer(text or ""):
        body = m.group("body")
        for seg in re.split(r"\s*;\s*", body):
            cit = _parse_segment(seg)
            if cit is None:
                continue
            key = (cit.source.lower(), cit.article)
            if key in seen:
                continue
            seen.add(key)
            out.append(Citation(source=cit.source, article=cit.article, raw=m.group(0) if ";" not in body else cit.raw))
    return out


Parser = Callable[[str], Sequence[Any]]
"""A citation parser: answer text → sequence of Citation, (source, article) tuples or
{"source","article"} dicts. Replaceable so systems with other citation formats can be evaluated."""


def _coerce(items: Sequence[Any]) -> list[Citation]:
    out: list[Citation] = []
    for it in items or ():
        if isinstance(it, Citation):
            out.append(it)
            continue
        if isinstance(it, dict):
            src, art, raw = it.get("source", ""), it.get("article", ""), it.get("raw", "")
        elif isinstance(it, (tuple, list)) and len(it) >= 2:
            src, art = it[0], it[1]
            raw = it[2] if len(it) > 2 else ""
        else:  # pydantic CitationRef or any object with the attributes
            src, art, raw = getattr(it, "source", ""), getattr(it, "article", ""), getattr(it, "raw", "")
        src, art = str(src or "").strip(), normalize_article(str(art or ""))
        out.append(Citation(source=src, article=art, raw=str(raw or "") or f"{src}, art. {art}".strip(", .")))
    return out


def citations_for(answer: str, explicit: Optional[Sequence[Any]] = None, parser: Optional[Parser] = None) -> list[Citation]:
    """Resolution order: explicit citations on the output record → user parser → built-in
    `[Source: …]` parser. Explicit citations are the fallback for systems whose answers carry
    no parseable tags (citations as metadata, UI footnotes, ...)."""
    if explicit is not None:
        return _coerce(explicit)
    return _coerce((parser or parse_citations)(answer or ""))


def load_parser(spec: str) -> Parser:
    """'package.module:function' → callable. The function takes the answer text and returns
    citations in any of the forms accepted by `citations_for`."""
    import importlib

    mod, _, fn = spec.partition(":")
    obj = getattr(importlib.import_module(mod), fn or "parse_citations")
    if not callable(obj):
        raise TypeError(f"{spec} is not callable")
    return obj


def inline_articles(text: str) -> set[str]:
    return {normalize_article(m) for m in INLINE_ART_RE.findall(text or "")}


def extract_articles(text: str) -> set[str]:
    """Article identifiers mentioned anywhere in free text (used for gold answers
    when `gold_articles` is not given — a documented regex limitation)."""
    return {a for a in inline_articles(text) if a}
