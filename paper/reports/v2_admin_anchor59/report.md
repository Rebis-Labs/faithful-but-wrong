# fbw-eval report

Generated 2026-10-29 00:01 UTC · 38 questions (33 answerable, 5 refusable) · stratifiable 32/38 (84%)
- **gold:** eval/reports/fbw/v2/admin/gold.jsonl
- **outputs:** eval/reports/fbw/v2/admin/outputs.jsonl
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
| full_recall | 23 | 17.4 [4.3, 34.8] | 92.9 [90.0, 95.8] | 81.7 [72.2, 90.4] | 93.3 [86.2, 99.1] | 0 |
| partial_recall | 4 | 50.0 [0.0, 100.0] | 97.8 [93.2, 100.0] | 61.3 [50.0, 72.5] | 100.0 [100.0, 100.0] | 0 |
| zero_recall | 5 | 0.0 [0.0, 0.0] | 94.6 [87.8, 100.0] | 76.0 [56.0, 96.0] | 90.0 [70.0, 100.0] | 0 |
| no_gold_articles | 6 | 50.0 [16.7, 83.3] | 100.0 [100.0, 100.0] | 70.0 [70.0, 70.0] | 100.0 [100.0, 100.0] | 3 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 23.7 [10.5, 36.8] |
| pass rate, refusal-driven passes excluded | 15.8 [5.3, 28.9] |
| faithfulness (answerable) | 94.0 [91.7, 96.2] |
| correctness (answerable) | 78.0 [70.3, 85.5] |
| answer relevancy (answerable) | 69.9 [64.1, 75.5] |
| context relevancy (answerable) | 85.2 [79.1, 91.1] |
| citation accuracy (answerable) | 93.8 [88.1, 98.5] |
| refusal accuracy | 94.7 [86.8, 100.0] |
| false refusals (FP) / missed refusals (FN) | 0 / 2 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| ADM001 | zero_recall | — | 0.90 | 0.50 | 0.70 | 1.00 | 1.00 | ❌ |
| ADM002 | full_recall | — | 0.92 | 0.80 | 0.40 | 0.60 | 1.00 | ❌ |
| ADM003 | full_recall | — | 1.00 | 0.50 | 0.60 | 1.00 | 1.00 | ❌ |
| ADM004 | full_recall | — | 1.00 | 1.00 | 0.90 | 1.00 | 1.00 | ✅ |
| ADM005 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM006 | full_recall | — | 0.82 | 1.00 | 0.70 | 1.00 | 1.00 | ❌ |
| ADM007 | no_gold_articles | — | 1.00 | 0.70 | 0.50 | 1.00 | 1.00 | ❌ |
| ADM008 | partial_recall | — | 1.00 | 0.50 | 0.85 | 1.00 | 1.00 | ✅ |
| ADM009 | full_recall | — | 1.00 | 1.00 | 0.82 | 1.00 | 1.00 | ❌ |
| ADM010 | full_recall | — | 0.93 | 1.00 | 0.82 | 0.60 | 1.00 | ❌ |
| ADM011 | full_recall | — | 0.83 | 1.00 | 1.00 | 1.00 | 1.00 | ❌ |
| ADM012 | full_recall | — | 1.00 | 0.50 | 0.60 | 0.67 | 1.00 | ❌ |
| ADM013 | full_recall | — | 0.90 | 0.50 | 0.55 | 0.75 | 1.00 | ❌ |
| ADM014 | full_recall | — | 0.88 | 1.00 | 0.70 | 1.00 | 1.00 | ❌ |
| ADM015 | partial_recall | — | 0.91 | 0.75 | 0.70 | 1.00 | 1.00 | ❌ |
| ADM016 | full_recall | — | 0.88 | 0.50 | 0.55 | 0.67 | 1.00 | ❌ |
| ADM017 | partial_recall | — | 1.00 | 0.50 | 0.50 | 0.75 | 1.00 | ❌ |
| ADM018 | zero_recall | — | 1.00 | 0.80 | 0.85 | 0.40 | 1.00 | ❌ |
| ADM019 | full_recall | — | 0.94 | 0.80 | 0.60 | 0.75 | 1.00 | ❌ |
| ADM020 | full_recall | — | 1.00 | 0.50 | 0.30 | 1.00 | 0.67 | ❌ |
| ADM021 | zero_recall | — | 1.00 | 1.00 | 0.70 | 0.80 | 1.00 | ❌ |
| ADM022 | full_recall | — | 0.88 | 1.00 | 0.90 | 1.00 | 1.00 | ❌ |
| ADM023 | full_recall | — | 0.80 | 0.50 | 0.60 | 0.57 | 0.50 | ❌ |
| ADM024 | full_recall | — | 1.00 | 1.00 | 0.95 | 0.83 | 1.00 | ✅ |
| ADM025 | full_recall | — | 0.92 | 0.50 | 0.70 | 1.00 | 0.80 | ❌ |
| ADM026 | full_recall | — | 1.00 | 1.00 | 0.82 | 0.67 | 0.50 | ❌ |
| ADM027 | full_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| ADM028 | full_recall | — | 0.82 | 0.70 | 0.60 | 0.67 | 1.00 | ❌ |
| ADM029 | partial_recall | — | 1.00 | 0.70 | 0.85 | 1.00 | 1.00 | ✅ |
| ADM030 | full_recall | — | 0.87 | 1.00 | 0.70 | 1.00 | 1.00 | ❌ |
| ADM031 | zero_recall | — | 0.83 | 1.00 | 0.50 | 0.80 | 1.00 | ❌ |
| ADM032 | zero_recall | — | 1.00 | 0.50 | 0.55 | 1.00 | 0.50 | ❌ |
| ADM033 | full_recall | — | 1.00 | 1.00 | 0.70 | 0.60 | 1.00 | ❌ |
| ADM_REF001 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF003 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| ADM_REF004 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| ADM_REF005 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
