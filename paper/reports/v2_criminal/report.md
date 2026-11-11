# fbw-eval report

Generated 2026-10-20 10:11 UTC · 30 questions (25 answerable, 5 refusable) · stratifiable 12/30 (40%)
- **gold:** eval/reports/fbw/v2/criminal/gold.jsonl
- **outputs:** eval/reports/fbw/v2/criminal/outputs.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 0
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['not stated']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 9 | 0.0 [0.0, 0.0] | 73.1 [49.8, 90.8] | 64.4 [53.3, 78.9] | 91.7 [75.0, 100.0] | 0 |
| partial_recall | 1 | 0.0 [0.0, 0.0] | 55.0 [55.0, 55.0] | 70.0 [70.0, 70.0] | 50.0 [50.0, 50.0] | 0 |
| zero_recall | 2 | 0.0 [0.0, 0.0] | 96.5 [93.0, 100.0] | 50.0 [50.0, 50.0] | 50.0 [0.0, 100.0] | 0 |
| no_gold_articles | 18 | 44.4 [22.2, 66.7] | 86.9 [77.7, 95.2] | 80.8 [69.2, 92.3] | 90.4 [73.1, 100.0] | 4 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 26.7 [13.3, 43.3] |
| pass rate, refusal-driven passes excluded | 13.3 [3.3, 26.7] |
| faithfulness (answerable) | 81.4 [71.2, 89.7] |
| correctness (answerable) | 72.0 [62.8, 81.2] |
| answer relevancy (answerable) | 76.5 [68.7, 83.3] |
| context relevancy (answerable) | 80.0 [69.8, 88.9] |
| citation accuracy (answerable) | 86.0 [74.0, 96.0] |
| refusal accuracy | 96.7 [90.0, 100.0] |
| false refusals (FP) / missed refusals (FN) | 0 / 1 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| CRIM001 | no_gold_articles | — | 1.00 | 0.50 | 0.70 | 0.40 | 1.00 | ❌ |
| CRIM002 | no_gold_articles | — | 0.80 | 0.50 | 0.95 | 0.80 | 1.00 | ❌ |
| CRIM003 | partial_recall | — | 0.55 | 0.70 | 0.70 | 0.75 | 0.50 | ❌ |
| CRIM004 | full_recall | — | 1.00 | 0.50 | 0.40 | 0.57 | 1.00 | ❌ |
| CRIM005 | no_gold_articles | — | 1.00 | 0.50 | 0.80 | 1.00 | 1.00 | ❌ |
| CRIM006 | no_gold_articles | — | 1.00 | 0.50 | 0.30 | 1.00 | 0.00 | ❌ |
| CRIM007 | no_gold_articles | — | 1.00 | 1.00 | 0.95 | 1.00 | 1.00 | ✅ |
| CRIM008 | no_gold_articles | — | 0.85 | 1.00 | 0.85 | 1.00 | 1.00 | ❌ |
| CRIM009 | full_recall | — | 0.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| CRIM010 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM011 | no_gold_articles | — | 0.50 | 1.00 | 1.00 | 0.83 | 1.00 | ❌ |
| CRIM012 | full_recall | — | 0.75 | 0.50 | 0.85 | 1.00 | 1.00 | ❌ |
| CRIM013 | no_gold_articles | — | 0.60 | 1.00 | 0.70 | 0.75 | 1.00 | ❌ |
| CRIM014 | full_recall | — | 1.00 | 1.00 | 0.70 | 0.67 | 1.00 | ❌ |
| CRIM015 | full_recall | — | 0.43 | 0.50 | 0.60 | 0.71 | 0.25 | ❌ |
| CRIM016 | full_recall | — | 0.62 | 0.50 | 0.85 | 1.00 | 1.00 | ❌ |
| CRIM017 | no_gold_articles | — | 0.92 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| CRIM018 | full_recall | — | 1.00 | 0.50 | 0.82 | 1.00 | 1.00 | ❌ |
| CRIM019 | no_gold_articles | — | 0.93 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| CRIM020 | full_recall | — | 0.90 | 0.50 | 0.85 | 0.29 | 1.00 | ❌ |
| CRIM021 | zero_recall | — | 1.00 | 0.50 | 0.30 | 0.50 | 0.00 | ❌ |
| CRIM022 | no_gold_articles | — | 0.70 | 0.50 | 0.70 | 1.00 | 0.75 | ❌ |
| CRIM023 | no_gold_articles | — | 1.00 | 1.00 | 0.85 | 0.20 | 1.00 | ❌ |
| CRIM024 | zero_recall | — | 0.93 | 0.50 | 0.70 | 0.86 | 1.00 | ❌ |
| CRIM025 | full_recall | — | 0.88 | 0.80 | 0.85 | 1.00 | 1.00 | ❌ |
| CRIM_REF001 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| CRIM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF003 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| CRIM_REF004 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| CRIM_REF005 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
