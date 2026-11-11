# fbw-eval report

Generated 2026-11-06 22:35 UTC · 78 questions (73 answerable, 5 refusable) · stratifiable 71/78 (91%)
- **gold:** docs/paper_v2/reports/v2_labor_v3_anchor59/gold.jsonl
- **outputs:** eval/reports/fbw/v2/v2_vanillaj_labor_v3/outputs.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 438
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold', '|anchor_2026-10-28:provisional|anchor_2026-10-28:confirmed']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 48 | 27.1 [14.6, 39.6] | 90.2 [85.4, 94.5] | 80.2 [71.5, 87.7] | 89.6 [81.2, 96.9] | 0 |
| partial_recall | 4 | 0.0 [0.0, 0.0] | 77.0 [60.0, 94.0] | 52.5 [32.5, 70.0] | 100.0 [100.0, 100.0] | 0 |
| zero_recall | 19 | 5.3 [0.0, 15.8] | 71.0 [57.0, 83.4] | 25.8 [13.2, 38.9] | 68.4 [47.4, 86.8] | 0 |
| no_gold_articles | 7 | 0.0 [0.0, 0.0] | 80.5 [71.0, 90.0] | 60.0 [50.0, 70.0] | 25.0 [0.0, 50.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 17.9 [10.3, 26.9] |
| pass rate, refusal-driven passes excluded | 17.9 [10.3, 26.9] |
| faithfulness (answerable) | 84.2 [78.7, 88.9] |
| correctness (answerable) | 64.0 [55.3, 72.5] |
| answer relevancy (answerable) | 73.9 [67.6, 79.8] |
| context relevancy (answerable) | 69.4 [62.1, 76.3] |
| citation accuracy (answerable) | 82.9 [74.7, 90.4] |
| refusal accuracy | 93.6 [87.2, 98.7] |
| false refusals (FP) / missed refusals (FN) | 0 / 5 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| LAB001 | zero_recall | — | 1.00 | 0.00 | 0.70 | 0.00 | 1.00 | ❌ |
| LAB002 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB003 | full_recall | — | 1.00 | 1.00 | 0.90 | 1.00 | 1.00 | ✅ |
| LAB004 | full_recall | — | 1.00 | 1.00 | 0.90 | 1.00 | 0.50 | ❌ |
| LAB005 | full_recall | — | 0.75 | 1.00 | 0.90 | 1.00 | 1.00 | ❌ |
| LAB006 | full_recall | — | 1.00 | 0.80 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB007 | full_recall | — | 1.00 | 1.00 | 0.90 | 1.00 | 1.00 | ✅ |
| LAB008 | full_recall | — | 1.00 | 1.00 | 0.85 | 0.67 | 0.50 | ❌ |
| LAB009 | full_recall | — | 1.00 | 1.00 | 0.70 | 1.00 | 1.00 | ❌ |
| LAB010 | full_recall | — | 1.00 | 0.90 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB011 | zero_recall | — | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | ❌ |
| LAB012 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB013 | zero_recall | — | 0.75 | 0.00 | 0.10 | 0.00 | 1.00 | ❌ |
| LAB014 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.33 | 1.00 | ❌ |
| LAB015 | zero_recall | — | 0.25 | 0.00 | 0.30 | 0.67 | 0.00 | ❌ |
| LAB016 | zero_recall | — | 0.67 | 0.50 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB017 | full_recall | — | 0.75 | 1.00 | 0.90 | 1.00 | 1.00 | ❌ |
| LAB018 | full_recall | — | 1.00 | 1.00 | 0.95 | 1.00 | 1.00 | ✅ |
| LAB019 | full_recall | — | 0.83 | 1.00 | 0.85 | 0.67 | 1.00 | ❌ |
| LAB020 | full_recall | — | 0.83 | 1.00 | 0.95 | 0.67 | 1.00 | ❌ |
| LAB021 | zero_recall | — | 0.40 | 0.00 | 0.30 | 0.00 | 0.00 | ❌ |
| LAB022 | full_recall | — | 0.50 | 0.00 | 0.30 | 0.33 | 1.00 | ❌ |
| LAB023 | full_recall | — | 1.00 | 0.50 | 0.90 | 1.00 | 1.00 | ✅ |
| LAB024 | full_recall | — | 0.33 | 0.50 | 0.90 | 0.33 | 1.00 | ❌ |
| LAB025 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB026 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB027 | no_gold_articles | — | 0.90 | 0.50 | 0.70 | 1.00 | 0.50 | ❌ |
| LAB028 | full_recall | — | 0.50 | 1.00 | 0.40 | 0.67 | 1.00 | ❌ |
| LAB029 | full_recall | — | 1.00 | 0.50 | 0.85 | 0.33 | 1.00 | ❌ |
| LAB030 | full_recall | — | 1.00 | 1.00 | 0.70 | 1.00 | 0.50 | ❌ |
| LAB031 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB032 | full_recall | — | 1.00 | 0.50 | 0.95 | 0.33 | 1.00 | ❌ |
| LAB033 | zero_recall | — | 0.80 | 0.50 | 0.60 | 0.33 | 0.50 | ❌ |
| LAB034 | zero_recall | — | 1.00 | 0.90 | 0.85 | 1.00 | 1.00 | ✅ |
| LAB035 | partial_recall | — | 0.60 | 0.20 | 0.70 | 1.00 | 1.00 | ❌ |
| LAB036 | zero_recall | — | 1.00 | 0.50 | 0.30 | 0.67 | 1.00 | ❌ |
| LAB037 | full_recall | — | 0.82 | 0.90 | 0.85 | 1.00 | 1.00 | ❌ |
| LAB038 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.33 | 1.00 | ❌ |
| LAB039 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB040 | full_recall | — | 0.80 | 0.10 | 0.20 | 0.33 | 0.00 | ❌ |
| LAB041 | full_recall | — | 1.00 | 0.50 | 0.90 | 1.00 | 1.00 | ✅ |
| LAB042 | full_recall | — | 1.00 | 0.00 | 0.90 | 1.00 | 1.00 | ✅ |
| LAB043 | zero_recall | — | 0.86 | 0.50 | 0.70 | 0.67 | 1.00 | ❌ |
| LAB044 | full_recall | — | 0.83 | 0.50 | 0.70 | 1.00 | 1.00 | ❌ |
| LAB045 | full_recall | — | 0.86 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB046 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB047 | full_recall | — | 1.00 | 1.00 | 0.90 | 1.00 | 1.00 | ✅ |
| LAB048 | zero_recall | — | 1.00 | 0.50 | 0.70 | 0.67 | 1.00 | ❌ |
| LAB049 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB050 | zero_recall | — | 0.60 | 0.00 | 0.70 | 1.00 | 1.00 | ❌ |
| LAB051 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.00 | ❌ |
| LAB052 | zero_recall | — | 0.67 | 0.50 | 0.30 | 0.33 | 1.00 | ❌ |
| LAB053 | zero_recall | — | 1.00 | 0.50 | 0.70 | 0.33 | 0.00 | ❌ |
| LAB054 | full_recall | — | 0.75 | 1.00 | 0.85 | 0.67 | 1.00 | ❌ |
| LAB055 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB056 | full_recall | — | 1.00 | 0.70 | 0.70 | 0.67 | 1.00 | ❌ |
| LAB057 | full_recall | — | 0.75 | 0.50 | 1.00 | 1.00 | 1.00 | ❌ |
| LAB058 | full_recall | — | 1.00 | 0.50 | 0.85 | 1.00 | 0.00 | ❌ |
| LAB059 | partial_recall | — | 0.88 | 0.70 | 0.75 | 1.00 | 1.00 | ❌ |
| LAB060 | zero_recall | — | 0.50 | 0.00 | 0.30 | 0.33 | 1.00 | ❌ |
| LAB061 | full_recall | — | 1.00 | 1.00 | 0.90 | 1.00 | 1.00 | ✅ |
| LAB062 | full_recall | — | 0.75 | 0.50 | 0.30 | 0.67 | 1.00 | ❌ |
| LAB063 | full_recall | — | 0.91 | 0.80 | 0.95 | 0.33 | 1.00 | ❌ |
| LAB064 | full_recall | — | 1.00 | 1.00 | 0.85 | 0.33 | 1.00 | ❌ |
| LAB065 | partial_recall | — | 0.60 | 0.50 | 0.30 | 1.00 | 1.00 | ❌ |
| LAB066 | zero_recall | — | 1.00 | 0.00 | 0.70 | 0.33 | 1.00 | ❌ |
| LAB067 | full_recall | — | 1.00 | 0.80 | 0.90 | 0.67 | 1.00 | ❌ |
| LAB068 | zero_recall | — | 1.00 | 0.00 | 0.20 | 0.33 | 0.00 | ❌ |
| LAB069 | full_recall | — | 1.00 | 0.50 | 0.70 | 1.00 | 0.50 | ❌ |
| LAB070 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB073 | zero_recall | — | 0.20 | 0.50 | 0.30 | 1.00 | 0.50 | ❌ |
| LAB074 | no_gold_articles | — | 0.71 | 0.70 | 0.30 | 0.33 | 0.00 | ❌ |
| LAB075 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB077 | full_recall | — | 0.75 | 1.00 | 0.70 | 0.67 | 1.00 | ❌ |
| LAB078 | zero_recall | — | 0.80 | 0.00 | 0.30 | 0.33 | 1.00 | ❌ |
| LAB079 | full_recall | — | 0.60 | 1.00 | 1.00 | 1.00 | 1.00 | ❌ |
| LAB080 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB081 | partial_recall | — | 1.00 | 0.70 | 1.00 | 0.33 | 1.00 | ❌ |
