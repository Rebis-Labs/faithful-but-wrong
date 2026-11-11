# fbw-eval report

Generated 2026-11-06 22:51 UTC · 78 questions (73 answerable, 5 refusable) · stratifiable 71/78 (91%)
- **gold:** docs/paper_v2/reports/v2_labor_v3_anchor59/gold.jsonl
- **outputs:** eval/reports/fbw/v2/v2_vanilla_labor_v3/outputs.jsonl
- **judge:** openai/gpt-4o-mini
- **judge calls:** 437
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold', '|anchor_2026-10-28:provisional|anchor_2026-10-28:confirmed']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 49 | 53.1 [38.8, 67.3] | 99.4 [98.4, 100.0] | 89.8 [82.7, 95.9] | 86.1 [76.9, 94.2] | 0 |
| partial_recall | 4 | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 87.5 [62.5, 100.0] | 100.0 [100.0, 100.0] | 0 |
| zero_recall | 18 | 27.8 [11.1, 50.0] | 93.3 [81.1, 100.0] | 38.9 [19.4, 58.3] | 61.1 [38.9, 83.3] | 0 |
| no_gold_articles | 7 | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 25.0 [0.0, 50.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 44.9 [33.3, 55.1] |
| pass rate, refusal-driven passes excluded | 44.9 [33.3, 55.1] |
| faithfulness (answerable) | 97.9 [94.9, 99.8] |
| correctness (answerable) | 77.4 [68.5, 86.3] |
| answer relevancy (answerable) | 93.7 [88.4, 98.1] |
| context relevancy (answerable) | 84.0 [78.5, 89.0] |
| citation accuracy (answerable) | 79.0 [69.9, 87.7] |
| refusal accuracy | 93.6 [87.2, 98.7] |
| false refusals (FP) / missed refusals (FN) | 0 / 5 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| LAB001 | zero_recall | — | 1.00 | 0.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB002 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB003 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB004 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.50 | ❌ |
| LAB005 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB006 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB007 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB008 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.50 | ❌ |
| LAB009 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB010 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB011 | zero_recall | — | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | ❌ |
| LAB012 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB013 | zero_recall | — | 1.00 | 0.00 | 0.00 | 1.00 | 1.00 | ❌ |
| LAB014 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB015 | zero_recall | — | 1.00 | 0.00 | 0.70 | 1.00 | 0.00 | ❌ |
| LAB016 | zero_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB017 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB018 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB019 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.33 | 1.00 | ❌ |
| LAB020 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB021 | zero_recall | — | 1.00 | 0.00 | 0.50 | 0.33 | 0.00 | ❌ |
| LAB022 | full_recall | — | 1.00 | 0.50 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB023 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB024 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.33 | 1.00 | ❌ |
| LAB025 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB026 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB027 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.50 | ❌ |
| LAB028 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 0.17 | ❌ |
| LAB029 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB030 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.50 | ❌ |
| LAB031 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB032 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB033 | zero_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 0.50 | ❌ |
| LAB034 | zero_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB035 | partial_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB036 | zero_recall | — | 1.00 | 0.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB037 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB038 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB039 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB040 | full_recall | — | 0.86 | 0.50 | 1.00 | 0.67 | 0.00 | ❌ |
| LAB041 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB042 | full_recall | — | 1.00 | 0.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB043 | zero_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 0.00 | ❌ |
| LAB044 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB045 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB046 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | ❌ |
| LAB047 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB048 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB049 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB050 | zero_recall | — | 1.00 | 0.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB051 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.00 | ❌ |
| LAB052 | zero_recall | — | 0.80 | 0.50 | 0.50 | 0.67 | 1.00 | ❌ |
| LAB053 | zero_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 0.00 | ❌ |
| LAB054 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB055 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB056 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB057 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB058 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | ❌ |
| LAB059 | partial_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB060 | zero_recall | — | 1.00 | 0.00 | 0.70 | 0.33 | 1.00 | ❌ |
| LAB061 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB062 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB063 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.33 | 1.00 | ❌ |
| LAB064 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB065 | partial_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB066 | zero_recall | — | 1.00 | 0.50 | 1.00 | 0.33 | 1.00 | ❌ |
| LAB067 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB068 | zero_recall | — | 1.00 | 0.00 | 0.00 | 0.33 | 0.00 | ❌ |
| LAB069 | full_recall | — | 1.00 | 0.00 | 1.00 | 1.00 | 0.50 | ❌ |
| LAB070 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB073 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.50 | ❌ |
| LAB074 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | ❌ |
| LAB075 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB077 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB078 | full_recall | — | 0.83 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| LAB079 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| LAB080 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB081 | partial_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
