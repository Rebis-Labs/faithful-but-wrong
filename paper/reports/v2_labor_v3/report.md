# fbw-eval report

Generated 2026-10-20 10:11 UTC · 78 questions (73 answerable, 5 refusable) · stratifiable 45/78 (58%)
- **gold:** eval/reports/fbw/v2/labor_v3/gold.jsonl
- **outputs:** eval/reports/fbw/v2/labor_v3/outputs.jsonl
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
| full_recall | 37 | 32.4 [18.9, 48.6] | 91.9 [87.8, 95.5] | 75.9 [65.9, 84.6] | 92.3 [84.7, 97.7] | 0 |
| zero_recall | 8 | 0.0 [0.0, 0.0] | 71.4 [52.5, 90.4] | 35.7 [14.3, 64.3] | 100.0 [100.0, 100.0] | 1 |
| no_gold_articles | 33 | 48.5 [30.3, 66.7] | 92.6 [85.9, 98.6] | 82.5 [71.2, 92.7] | 100.0 [100.0, 100.0] | 2 |

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
| LAB001 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB002 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB003 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB004 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB005 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB006 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB007 | no_gold_articles | — | 1.00 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| LAB008 | no_gold_articles | — | 1.00 | 1.00 | 0.85 | 0.67 | 1.00 | ❌ |
| LAB009 | no_gold_articles | — | 1.00 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| LAB010 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB011 | no_gold_articles | — | 0.60 | 0.10 | 0.20 | 0.00 | 1.00 | ❌ |
| LAB012 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB013 | zero_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB014 | no_gold_articles | — | 1.00 | 1.00 | 0.95 | 1.00 | 1.00 | ✅ |
| LAB015 | no_gold_articles | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB016 | zero_recall | — | 0.67 | 0.00 | 0.30 | 0.67 | 1.00 | ❌ |
| LAB017 | no_gold_articles | — | 0.88 | 0.75 | 0.85 | 1.00 | 1.00 | ❌ |
| LAB018 | no_gold_articles | — | 1.00 | 1.00 | 0.95 | 0.33 | 1.00 | ❌ |
| LAB019 | no_gold_articles | — | 1.00 | 1.00 | 0.70 | 0.67 | 1.00 | ❌ |
| LAB020 | no_gold_articles | — | 1.00 | 1.00 | 0.85 | 0.67 | 1.00 | ❌ |
| LAB021 | no_gold_articles | — | 0.33 | 0.00 | 1.00 | 0.00 | 1.00 | ❌ |
| LAB022 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 0.33 | 1.00 | ❌ |
| LAB023 | no_gold_articles | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB024 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB025 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| LAB026 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| LAB027 | no_gold_articles | — | 0.91 | 0.50 | 0.50 | 1.00 | 1.00 | ❌ |
| LAB028 | full_recall | — | 0.86 | 1.00 | 0.60 | 0.67 | 0.50 | ❌ |
| LAB029 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB030 | no_gold_articles | — | 1.00 | 1.00 | 0.70 | 0.67 | 1.00 | ❌ |
| LAB031 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB032 | full_recall | — | 1.00 | 0.50 | 0.85 | 0.67 | 1.00 | ❌ |
| LAB033 | no_gold_articles | — | 1.00 | 0.75 | 0.70 | 0.33 | 1.00 | ❌ |
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
| LAB059 | full_recall | — | 1.00 | 0.70 | 0.70 | 1.00 | 1.00 | ❌ |
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
| LAB073 | no_gold_articles | — | 0.79 | 0.70 | 0.40 | 1.00 | 1.00 | ❌ |
| LAB074 | no_gold_articles | — | 0.43 | 0.30 | 0.40 | 0.33 | 1.00 | ❌ |
| LAB075 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB077 | full_recall | — | 0.83 | 1.00 | 0.95 | 1.00 | 1.00 | ❌ |
| LAB078 | full_recall | — | 1.00 | 0.90 | 0.85 | 0.33 | 1.00 | ❌ |
| LAB079 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB080 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB081 | full_recall | — | 1.00 | 0.75 | 1.00 | 0.67 | 1.00 | ❌ |
