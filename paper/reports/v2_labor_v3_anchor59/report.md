# fbw-eval report

Generated 2026-10-29 00:01 UTC · 78 questions (73 answerable, 5 refusable) · stratifiable 71/78 (91%)
- **gold:** eval/reports/fbw/v2/labor_v3/gold.jsonl
- **outputs:** eval/reports/fbw/v2/labor_v3/outputs.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 0
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold', '|anchor_2026-10-28:provisional|anchor_2026-10-28:confirmed']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 58 | 44.8 [32.8, 58.6] | 94.6 [91.8, 97.2] | 83.0 [76.1, 89.2] | 95.1 [89.9, 99.1] | 0 |
| partial_recall | 2 | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 72.5 [70.0, 75.0] | 100.0 [100.0, 100.0] | 0 |
| zero_recall | 11 | 0.0 [0.0, 0.0] | 67.5 [51.6, 83.0] | 33.0 [13.0, 56.0] | 100.0 [100.0, 100.0] | 1 |
| no_gold_articles | 7 | 28.6 [0.0, 71.4] | 67.0 [43.0, 91.0] | 40.0 [30.0, 50.0] | 100.0 [100.0, 100.0] | 2 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 35.9 [25.6, 47.4] |
| pass rate, refusal-driven passes excluded | 33.3 [23.1, 44.9] |
| faithfulness (answerable) | 89.9 [85.9, 93.8] |
| correctness (answerable) | 74.6 [66.9, 82.0] |
| answer relevancy (answerable) | 84.3 [79.5, 88.8] |
| context relevancy (answerable) | 83.8 [77.4, 89.2] |
| citation accuracy (answerable) | 96.1 [92.0, 99.3] |
| refusal accuracy | 94.9 [89.7, 98.7] |
| false refusals (FP) / missed refusals (FN) | 1 / 3 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| LAB001 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB002 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB003 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB004 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB005 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB006 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB007 | full_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| LAB008 | full_recall | — | 1.00 | 1.00 | 0.85 | 0.67 | 1.00 | ❌ |
| LAB009 | full_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| LAB010 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB011 | zero_recall | — | 0.60 | 0.10 | 0.20 | 0.00 | 1.00 | ❌ |
| LAB012 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB013 | zero_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB014 | full_recall | — | 1.00 | 1.00 | 0.95 | 1.00 | 1.00 | ✅ |
| LAB015 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB016 | zero_recall | — | 0.67 | 0.00 | 0.30 | 0.67 | 1.00 | ❌ |
| LAB017 | full_recall | — | 0.88 | 0.75 | 0.85 | 1.00 | 1.00 | ❌ |
| LAB018 | full_recall | — | 1.00 | 1.00 | 0.95 | 0.33 | 1.00 | ❌ |
| LAB019 | full_recall | — | 1.00 | 1.00 | 0.70 | 0.67 | 1.00 | ❌ |
| LAB020 | full_recall | — | 1.00 | 1.00 | 0.85 | 0.67 | 1.00 | ❌ |
| LAB021 | zero_recall | — | 0.33 | 0.00 | 1.00 | 0.00 | 1.00 | ❌ |
| LAB022 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.33 | 1.00 | ❌ |
| LAB023 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB024 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB025 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| LAB026 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| LAB027 | no_gold_articles | — | 0.91 | 0.50 | 0.50 | 1.00 | 1.00 | ❌ |
| LAB028 | full_recall | — | 0.86 | 1.00 | 0.60 | 0.67 | 0.50 | ❌ |
| LAB029 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB030 | full_recall | — | 1.00 | 1.00 | 0.70 | 0.67 | 1.00 | ❌ |
| LAB031 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB032 | full_recall | — | 1.00 | 0.50 | 0.85 | 0.67 | 1.00 | ❌ |
| LAB033 | full_recall | — | 1.00 | 0.75 | 0.70 | 0.33 | 1.00 | ❌ |
| LAB034 | full_recall | — | 1.00 | 0.90 | 0.85 | 1.00 | 1.00 | ✅ |
| LAB035 | zero_recall | — | 0.38 | 0.50 | 0.70 | 1.00 | 1.00 | ❌ |
| LAB036 | zero_recall | ⛔ | 1.00 | — | 1.00 | — | 1.00 | ❌ |
| LAB037 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB038 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.75 | 1.00 | ❌ |
| LAB039 | full_recall | — | 1.00 | 0.75 | 0.70 | 0.67 | 0.50 | ❌ |
| LAB040 | full_recall | — | 1.00 | 0.50 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB041 | full_recall | — | 0.60 | 0.50 | 0.60 | 1.00 | 1.00 | ❌ |
| LAB042 | full_recall | — | 1.00 | 0.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB043 | zero_recall | — | 0.86 | 0.50 | 0.70 | 1.00 | 1.00 | ❌ |
| LAB044 | full_recall | — | 1.00 | 0.50 | 0.85 | 1.00 | 1.00 | ✅ |
| LAB045 | full_recall | — | 0.88 | 1.00 | 1.00 | 1.00 | 1.00 | ❌ |
| LAB046 | full_recall | — | 0.91 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB047 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB048 | zero_recall | — | 1.00 | 0.00 | 0.70 | 1.00 | 1.00 | ❌ |
| LAB049 | full_recall | — | 1.00 | 1.00 | 0.95 | 1.00 | 1.00 | ✅ |
| LAB050 | zero_recall | — | 0.25 | 0.00 | 0.85 | 1.00 | 1.00 | ❌ |
| LAB051 | full_recall | — | 1.00 | 1.00 | 0.90 | 1.00 | 0.50 | ❌ |
| LAB052 | full_recall | — | 0.83 | 0.50 | 1.00 | 1.00 | 1.00 | ❌ |
| LAB053 | full_recall | — | 0.67 | 1.00 | 1.00 | 1.00 | 1.00 | ❌ |
| LAB054 | full_recall | — | 1.00 | 1.00 | 0.90 | 1.00 | 1.00 | ✅ |
| LAB055 | full_recall | — | 0.67 | 1.00 | 1.00 | 1.00 | 1.00 | ❌ |
| LAB056 | full_recall | — | 0.71 | 0.50 | 0.85 | 1.00 | 1.00 | ❌ |
| LAB057 | full_recall | — | 1.00 | 0.50 | 0.90 | 1.00 | 1.00 | ✅ |
| LAB058 | full_recall | — | 0.75 | 0.80 | 0.95 | 1.00 | 1.00 | ❌ |
| LAB059 | partial_recall | — | 1.00 | 0.70 | 0.70 | 1.00 | 1.00 | ❌ |
| LAB060 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB061 | full_recall | — | 0.80 | 0.90 | 0.70 | 1.00 | 1.00 | ❌ |
| LAB062 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.00 | ❌ |
| LAB063 | full_recall | — | 0.94 | 0.50 | 0.95 | 0.50 | 1.00 | ❌ |
| LAB064 | full_recall | — | 1.00 | 1.00 | 0.85 | 0.67 | 1.00 | ❌ |
| LAB065 | zero_recall | — | 0.56 | 0.50 | 0.40 | 1.00 | 1.00 | ❌ |
| LAB066 | full_recall | — | 0.86 | 0.00 | 0.30 | 0.50 | 1.00 | ❌ |
| LAB067 | full_recall | — | 0.80 | 0.90 | 0.85 | 0.50 | 1.00 | ❌ |
| LAB068 | full_recall | — | 1.00 | 0.50 | 0.40 | 1.00 | 1.00 | ❌ |
| LAB069 | full_recall | — | 0.90 | 0.50 | 0.70 | 0.75 | 0.67 | ❌ |
| LAB070 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB073 | zero_recall | — | 0.79 | 0.70 | 0.40 | 1.00 | 1.00 | ❌ |
| LAB074 | no_gold_articles | — | 0.43 | 0.30 | 0.40 | 0.33 | 1.00 | ❌ |
| LAB075 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB077 | full_recall | — | 0.83 | 1.00 | 0.95 | 1.00 | 1.00 | ❌ |
| LAB078 | full_recall | — | 1.00 | 0.90 | 0.85 | 0.33 | 1.00 | ❌ |
| LAB079 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB080 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB081 | partial_recall | — | 1.00 | 0.75 | 1.00 | 0.67 | 1.00 | ❌ |
