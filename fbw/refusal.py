"""Refusal detection.

A refusal is a *correct* behaviour when the corpus cannot answer, and the
single biggest confound in aggregate pass rates (refusing well on hard
questions raises the headline). The protocol therefore (a) scores refusals as
their own binary metric and (b) reports pass rates with and without
refusal-driven passes.

Detection: explicit `refused` from the system wins. Otherwise canonical
markers (configurable) anywhere in the answer, or a refusal paraphrase in
the opening of the answer. The defaults are the Italian markers of the
reference implementation; pass your own for another system or language.
"""

from __future__ import annotations

import re
from typing import Iterable, Optional

DEFAULT_MARKERS: tuple[str, ...] = (
    "non ho trovato informazioni sufficienti",
    "risposta non certa",
)

# Paraphrases such as "La documentazione disponibile non copre…" — only in the
# first 250 characters, so a partial answer with a trailing caveat is not a refusal.
DEFAULT_PARAPHRASE_RE = re.compile(
    r"(documentazione|documenti|fonti)\s+(disponibil[ie]|fornit[ie]|a disposizione)\s+non\s+"
    r"(?:(?:copr|fornisc|contien|includ)(?:e|ono)|tratta(?:no)?|disciplina(?:no)?)"
    r"|non (?:posso|sono in grado di) rispondere .{0,60}(documenti|documentazione|fonti)"
    r"|the (?:provided|available) (?:documents?|context|sources?) (?:do(?:es)? not|don't) (?:cover|contain|address)"
    r"|i (?:cannot|can't|am unable to) answer .{0,60}(?:documents?|context|sources?)",
    re.IGNORECASE,
)


class RefusalDetector:
    def __init__(
        self,
        markers: Optional[Iterable[str]] = None,
        paraphrase_re: Optional[re.Pattern[str]] = DEFAULT_PARAPHRASE_RE,
        head_chars: int = 250,
    ):
        self.markers = tuple(m.lower() for m in (markers or DEFAULT_MARKERS))
        self.paraphrase_re = paraphrase_re
        self.head_chars = head_chars

    def __call__(self, answer: str, explicit: Optional[bool] = None) -> bool:
        if explicit is not None:
            return bool(explicit)
        if not answer or not answer.strip():
            return True
        low = answer.lower()
        if any(m in low for m in self.markers):
            return True
        if self.paraphrase_re and self.paraphrase_re.search(answer[: self.head_chars]):
            return True
        return False


def refusal_outcome(refused: bool, should_refuse: bool) -> tuple[bool, str]:
    """(correct, type) with type in TP/TN/FP/FN. FP = false refusal."""
    if should_refuse and refused:
        return True, "TP"
    if not should_refuse and not refused:
        return True, "TN"
    if not should_refuse and refused:
        return False, "FP"
    return False, "FN"
