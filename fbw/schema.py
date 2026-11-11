"""Input/output schema. Two JSONL files in, one record per question out.

gold.jsonl      — one GoldItem per line (what a correct answer must say/cite)
outputs.jsonl   — one SystemOutput per line (what the system under test produced)

The two are joined on `question_id`. Nothing here depends on how the system
retrieved or generated: a bi-encoder, a web search, a human — any pipeline
that can dump its answer and the contexts it saw can be evaluated.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Optional

from pydantic import BaseModel, Field


class GoldItem(BaseModel):
    question_id: str
    question: str
    expected_answer: str = ""
    gold_articles: list[str] = Field(default_factory=list)
    """Article identifiers a correct answer MUST cite (e.g. "2103", "29-bis").
    Empty → derived by regex from `expected_answer` (documented limitation)."""
    expected_sources: list[str] = Field(default_factory=list)
    should_refuse: bool = False
    domain: str = ""
    difficulty: str = ""
    provenance: str = ""


class RetrievedChunk(BaseModel):
    text: str
    source: str = ""
    """Citable name of the act/document the chunk belongs to."""
    article: str = ""
    """Article identifier of the chunk, if the corpus is article-segmented."""


class CitationRef(BaseModel):
    source: str
    article: str = ""
    raw: str = ""
    """How the citation appeared in the answer (for the verification log). Optional."""


class SystemOutput(BaseModel):
    question_id: str
    answer: str = ""
    retrieved: list[RetrievedChunk] = Field(default_factory=list)
    """Exactly the contexts handed to the generator, in rank order."""
    refused: Optional[bool] = None
    """Set it if the system knows it refused; otherwise the refusal detector decides."""
    citations: Optional[list[CitationRef]] = None
    """Explicit citations, if the system does not emit `[Source: act, art. N]` tags in the
    answer text. When given, they replace citation parsing for this output."""
    system: str = ""
    latency_ms: float = 0.0


class EvalRecord(BaseModel):
    """One evaluated question. Scores are 0-1 floats; None = not computed."""

    question_id: str
    system: str = ""
    domain: str = ""
    should_refuse: bool
    refused: bool
    refusal_type: str  # TP | TN | FP | FN
    bucket: str  # full_recall | partial_recall | zero_recall | no_gold_articles
    gold_articles: list[str] = Field(default_factory=list)
    retrieved_articles: list[str] = Field(default_factory=list)

    context_relevancy: Optional[float] = None
    faithfulness: Optional[float] = None
    answer_relevancy: Optional[float] = None
    citation_accuracy: Optional[float] = None
    correctness: Optional[float] = None

    passed: bool = False
    errors: list[str] = Field(default_factory=list)


def read_jsonl(path: str | Path, model):
    """Yield `model` instances from a JSONL file; `#` lines are comments."""
    with open(path, encoding="utf-8") as f:
        for n, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                yield model(**json.loads(line))
            except Exception as exc:  # noqa: BLE001 — surface the line, keep going
                raise ValueError(f"{path}:{n}: {exc}") from exc


def write_jsonl(path: str | Path, rows: Iterable[BaseModel]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(r.model_dump_json() + "\n")
