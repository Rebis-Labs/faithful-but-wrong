"""Recall-conditional stratification — the protocol's key.

Each question is classified by whether the contexts the generator saw contained
the gold articles. Metrics are then reported per bucket. The point: a generator
can only be *correct* if the answer was in its context; a generator can be
*faithful* regardless. Aggregating over buckets hides the second case.

  full_recall     all gold articles in the retrieved set
  partial_recall  some, not all
  zero_recall     none — the generator cannot be correct without confabulating
  no_gold_articles  gold has no article (principle questions, refusals): excluded
                    from recall-conditional tables, kept for end-task metrics

Granularity is the article, by design: a chunk-level match would be too strict
(long articles span chunks) and a document-level match too loose (a code has
hundreds of articles). Retrieved identifiers come from chunk metadata when the
corpus is article-segmented, else from article mentions in the chunk text.
"""

from __future__ import annotations

from enum import Enum
from typing import Iterable

from .citations import extract_articles, normalize_article
from .schema import GoldItem, RetrievedChunk


class Bucket(str, Enum):
    FULL = "full_recall"
    PARTIAL = "partial_recall"
    ZERO = "zero_recall"
    NO_GOLD = "no_gold_articles"


RECALL_BUCKETS = (Bucket.FULL, Bucket.PARTIAL, Bucket.ZERO)


def gold_articles(item: GoldItem) -> set[str]:
    if item.gold_articles:
        return {normalize_article(a) for a in item.gold_articles if normalize_article(a)}
    return extract_articles(item.expected_answer)


def retrieved_articles(chunks: Iterable[RetrievedChunk], fallback_to_text: bool = True) -> set[str]:
    out: set[str] = set()
    for c in chunks:
        a = normalize_article(c.article)
        if a and a not in ("?",):
            out.add(a)
        elif fallback_to_text:
            out |= extract_articles(c.text)
    return out


def classify(gold: set[str], retrieved: set[str]) -> Bucket:
    if not gold:
        return Bucket.NO_GOLD
    overlap = gold & retrieved
    if not overlap:
        return Bucket.ZERO
    if gold <= retrieved:
        return Bucket.FULL
    return Bucket.PARTIAL
