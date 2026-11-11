# fbw-eval report

Generated 2026-10-29 01:50 UTC · 78 questions (73 answerable, 5 refusable) · stratifiable 71/78 (91%)
- **gold:** eval/reports/fbw/v2/labor_v3/gold.jsonl
- **outputs:** eval/reports/fbw/v2/frontier_labor_v3/outputs_claude.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 219
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold', '|anchor_2026-10-28:provisional|anchor_2026-10-28:confirmed']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| zero_recall | 71 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 64.6 [56.8, 72.5] | 0.0 [0.0, 0.0] | 0 |
| no_gold_articles | 7 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 0.0 [0.0, 0.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 0.0 [0.0, 0.0] |
| pass rate, refusal-driven passes excluded | 0.0 [0.0, 0.0] |
| faithfulness (answerable) | 0.0 [0.0, 0.0] |
| correctness (answerable) | 65.5 [57.5, 72.8] |
| answer relevancy (answerable) | 78.8 [74.5, 83.1] |
| context relevancy (answerable) | — |
| citation accuracy (answerable) | 0.0 [0.0, 0.0] |
| refusal accuracy | 93.6 [87.2, 98.7] |
| false refusals (FP) / missed refusals (FN) | 0 / 5 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| LAB001 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| LAB002 | zero_recall | — | 0.00 | 0.00 | 1.00 | — | 0.00 | ❌ |
| LAB003 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| LAB004 | zero_recall | — | 0.00 | 0.00 | 0.95 | — | 0.00 | ❌ |
| LAB005 | zero_recall | — | 0.00 | 1.00 | 0.60 | — | 0.00 | ❌ |
| LAB006 | zero_recall | — | 0.00 | 0.00 | 0.40 | — | 0.00 | ❌ |
| LAB007 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| LAB008 | zero_recall | — | 0.00 | 0.50 | 0.50 | — | 0.00 | ❌ |
| LAB009 | zero_recall | — | 0.00 | 0.50 | 0.60 | — | 0.00 | ❌ |
| LAB010 | zero_recall | — | 0.00 | 0.70 | 0.40 | — | 0.00 | ❌ |
| LAB011 | zero_recall | — | 0.00 | 0.50 | 0.70 | — | 0.00 | ❌ |
| LAB012 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| LAB013 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| LAB014 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| LAB015 | zero_recall | — | 0.00 | 0.30 | 0.85 | — | 0.00 | ❌ |
| LAB016 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| LAB017 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| LAB018 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| LAB019 | zero_recall | — | 0.00 | 1.00 | 0.70 | — | 0.00 | ❌ |
| LAB020 | zero_recall | — | 0.00 | 1.00 | 0.70 | — | 0.00 | ❌ |
| LAB021 | zero_recall | — | 0.00 | 1.00 | 0.70 | — | 0.00 | ❌ |
| LAB022 | zero_recall | — | 0.00 | 1.00 | 0.30 | — | 0.00 | ❌ |
| LAB023 | zero_recall | — | 0.00 | 0.50 | 1.00 | — | 0.00 | ❌ |
| LAB024 | zero_recall | — | 0.00 | 1.00 | 0.70 | — | 0.00 | ❌ |
| LAB025 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB026 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB027 | no_gold_articles | — | 0.00 | 1.00 | 0.82 | — | 0.00 | ❌ |
| LAB028 | zero_recall | — | 0.00 | 0.50 | 0.95 | — | 0.00 | ❌ |
| LAB029 | zero_recall | — | 0.00 | 0.75 | 0.70 | — | 0.00 | ❌ |
| LAB030 | zero_recall | — | 0.00 | 0.00 | 0.30 | — | 0.00 | ❌ |
| LAB031 | zero_recall | — | 0.00 | 1.00 | 1.00 | — | 0.00 | ❌ |
| LAB032 | zero_recall | — | 0.00 | 0.80 | 0.70 | — | 0.00 | ❌ |
| LAB033 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| LAB034 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| LAB035 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| LAB036 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| LAB037 | zero_recall | — | 0.00 | 0.90 | 0.70 | — | 0.00 | ❌ |
| LAB038 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| LAB039 | zero_recall | — | 0.00 | 1.00 | 0.70 | — | 0.00 | ❌ |
| LAB040 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| LAB041 | zero_recall | — | 0.00 | 0.00 | 0.90 | — | 0.00 | ❌ |
| LAB042 | zero_recall | — | 0.00 | 0.00 | 0.95 | — | 0.00 | ❌ |
| LAB043 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| LAB044 | zero_recall | — | 0.00 | 1.00 | 0.90 | — | 0.00 | ❌ |
| LAB045 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| LAB046 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| LAB047 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| LAB048 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| LAB049 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| LAB050 | zero_recall | — | 0.00 | 1.00 | 0.90 | — | 0.00 | ❌ |
| LAB051 | zero_recall | — | 0.00 | 0.50 | 0.95 | — | 0.00 | ❌ |
| LAB052 | zero_recall | — | 0.00 | 0.50 | 0.90 | — | 0.00 | ❌ |
| LAB053 | zero_recall | — | 0.00 | 0.80 | 1.00 | — | 0.00 | ❌ |
| LAB054 | zero_recall | — | 0.00 | 0.00 | 0.40 | — | 0.00 | ❌ |
| LAB055 | zero_recall | — | 0.00 | 0.80 | 1.00 | — | 0.00 | ❌ |
| LAB056 | zero_recall | — | 0.00 | 0.80 | 1.00 | — | 0.00 | ❌ |
| LAB057 | zero_recall | — | 0.00 | 0.50 | 0.50 | — | 0.00 | ❌ |
| LAB058 | zero_recall | — | 0.00 | 0.50 | 0.60 | — | 0.00 | ❌ |
| LAB059 | zero_recall | — | 0.00 | 0.50 | 0.42 | — | 0.00 | ❌ |
| LAB060 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| LAB061 | zero_recall | — | 0.00 | 0.20 | 0.90 | — | 0.00 | ❌ |
| LAB062 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| LAB063 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| LAB064 | zero_recall | — | 0.00 | 0.70 | 0.82 | — | 0.00 | ❌ |
| LAB065 | zero_recall | — | 0.00 | 0.70 | 0.35 | — | 0.00 | ❌ |
| LAB066 | zero_recall | — | 0.00 | 0.10 | 0.30 | — | 0.00 | ❌ |
| LAB067 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| LAB068 | zero_recall | — | 0.00 | 0.50 | 0.60 | — | 0.00 | ❌ |
| LAB069 | zero_recall | — | 0.00 | 0.30 | 0.85 | — | 0.00 | ❌ |
| LAB070 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB073 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| LAB074 | no_gold_articles | — | 0.00 | 1.00 | 0.90 | — | 0.00 | ❌ |
| LAB075 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB077 | zero_recall | — | 0.00 | 0.50 | 0.90 | — | 0.00 | ❌ |
| LAB078 | zero_recall | — | 0.00 | 0.80 | 0.82 | — | 0.00 | ❌ |
| LAB079 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| LAB080 | no_gold_articles | — | — | — | — | — | — | ❌ |
| LAB081 | zero_recall | — | 0.00 | 0.70 | 0.90 | — | 0.00 | ❌ |
