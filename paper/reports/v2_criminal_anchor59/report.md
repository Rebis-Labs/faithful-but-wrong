# fbw-eval report

Generated 2026-10-29 00:01 UTC · 30 questions (25 answerable, 5 refusable) · stratifiable 24/30 (80%)
- **gold:** eval/reports/fbw/v2/criminal/gold.jsonl
- **outputs:** eval/reports/fbw/v2/criminal/outputs.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 0
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 21 | 19.0 [4.8, 38.1] | 80.4 [69.0, 89.9] | 75.2 [64.3, 85.7] | 95.2 [86.9, 100.0] | 0 |
| partial_recall | 1 | 0.0 [0.0, 0.0] | 55.0 [55.0, 55.0] | 70.0 [70.0, 70.0] | 50.0 [50.0, 50.0] | 0 |
| zero_recall | 2 | 0.0 [0.0, 0.0] | 96.5 [93.0, 100.0] | 50.0 [50.0, 50.0] | 50.0 [0.0, 100.0] | 0 |
| no_gold_articles | 6 | 66.7 [33.3, 100.0] | 100.0 [100.0, 100.0] | 50.0 [50.0, 50.0] | 0.0 [0.0, 0.0] | 4 |

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
| CRIM001 | full_recall | — | 1.00 | 0.50 | 0.70 | 0.40 | 1.00 | ❌ |
| CRIM002 | full_recall | — | 0.80 | 0.50 | 0.95 | 0.80 | 1.00 | ❌ |
| CRIM003 | partial_recall | — | 0.55 | 0.70 | 0.70 | 0.75 | 0.50 | ❌ |
| CRIM004 | full_recall | — | 1.00 | 0.50 | 0.40 | 0.57 | 1.00 | ❌ |
| CRIM005 | full_recall | — | 1.00 | 0.50 | 0.80 | 1.00 | 1.00 | ❌ |
| CRIM006 | no_gold_articles | — | 1.00 | 0.50 | 0.30 | 1.00 | 0.00 | ❌ |
| CRIM007 | full_recall | — | 1.00 | 1.00 | 0.95 | 1.00 | 1.00 | ✅ |
| CRIM008 | full_recall | — | 0.85 | 1.00 | 0.85 | 1.00 | 1.00 | ❌ |
| CRIM009 | full_recall | — | 0.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| CRIM010 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM011 | full_recall | — | 0.50 | 1.00 | 1.00 | 0.83 | 1.00 | ❌ |
| CRIM012 | full_recall | — | 0.75 | 0.50 | 0.85 | 1.00 | 1.00 | ❌ |
| CRIM013 | full_recall | — | 0.60 | 1.00 | 0.70 | 0.75 | 1.00 | ❌ |
| CRIM014 | full_recall | — | 1.00 | 1.00 | 0.70 | 0.67 | 1.00 | ❌ |
| CRIM015 | full_recall | — | 0.43 | 0.50 | 0.60 | 0.71 | 0.25 | ❌ |
| CRIM016 | full_recall | — | 0.62 | 0.50 | 0.85 | 1.00 | 1.00 | ❌ |
| CRIM017 | full_recall | — | 0.92 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| CRIM018 | full_recall | — | 1.00 | 0.50 | 0.82 | 1.00 | 1.00 | ❌ |
| CRIM019 | full_recall | — | 0.93 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| CRIM020 | full_recall | — | 0.90 | 0.50 | 0.85 | 0.29 | 1.00 | ❌ |
| CRIM021 | zero_recall | — | 1.00 | 0.50 | 0.30 | 0.50 | 0.00 | ❌ |
| CRIM022 | full_recall | — | 0.70 | 0.50 | 0.70 | 1.00 | 0.75 | ❌ |
| CRIM023 | full_recall | — | 1.00 | 1.00 | 0.85 | 0.20 | 1.00 | ❌ |
| CRIM024 | zero_recall | — | 0.93 | 0.50 | 0.70 | 0.86 | 1.00 | ❌ |
| CRIM025 | full_recall | — | 0.88 | 0.80 | 0.85 | 1.00 | 1.00 | ❌ |
| CRIM_REF001 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| CRIM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF003 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| CRIM_REF004 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| CRIM_REF005 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
