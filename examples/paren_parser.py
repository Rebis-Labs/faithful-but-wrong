"""Example of a replaceable citation parser.

The built-in parser reads `[Source: act, art. N]` tags. A system that cites in another
style supplies its own function and passes it with `--citation-parser examples.paren_parser:parse`.
The function receives the answer text and returns citations as (source, article[, raw])
tuples, dicts with "source"/"article", or `fbw.citations.Citation` objects.

This one reads the parenthetical style "(Codice Civile, art. 2103)" / "(TUIR, art. 51)".
"""

from __future__ import annotations

import re

PAREN_RE = re.compile(r"\((?P<source>[^(),]+?),\s*artt?\.?\s*(?P<art>[\w\s-]+?)\)", re.IGNORECASE)


def parse(answer: str):
    return [(m.group("source").strip(), m.group("art").strip(), m.group(0)) for m in PAREN_RE.finditer(answer or "")]
