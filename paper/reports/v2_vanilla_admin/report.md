# fbw-eval report

Generated 2026-11-06 22:13 UTC · 38 questions (33 answerable, 5 refusable) · stratifiable 32/38 (84%)
- **gold:** docs/paper_v2/reports/v2_admin_anchor59/gold.jsonl
- **outputs:** eval/reports/fbw/v2/v2_vanilla_admin/outputs.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 198
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 6 | 0.0 [0.0, 0.0] | 93.8 [85.4, 100.0] | 70.8 [54.2, 87.5] | 83.3 [66.7, 100.0] | 0 |
| partial_recall | 2 | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 50.0 [50.0, 50.0] | 75.0 [50.0, 100.0] | 0 |
| zero_recall | 24 | 0.0 [0.0, 0.0] | 82.2 [69.9, 92.9] | 39.2 [25.4, 54.2] | 27.1 [10.4, 43.8] | 0 |
| no_gold_articles | 6 | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 50.0 [50.0, 50.0] | 50.0 [50.0, 50.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 0.0 [0.0, 0.0] |
| pass rate, refusal-driven passes excluded | 0.0 [0.0, 0.0] |
| faithfulness (answerable) | 85.9 [76.2, 93.5] |
| correctness (answerable) | 45.9 [34.4, 57.4] |
| answer relevancy (answerable) | 49.0 [39.8, 58.2] |
| context relevancy (answerable) | 66.7 [54.5, 78.8] |
| citation accuracy (answerable) | 40.9 [25.8, 56.1] |
| refusal accuracy | 86.8 [76.3, 97.4] |
| false refusals (FP) / missed refusals (FN) | 0 / 5 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| ADM001 | zero_recall | — | 1.00 | 0.00 | 0.50 | 1.00 | 1.00 | ❌ |
| ADM002 | zero_recall | — | 0.78 | 0.20 | 0.30 | 0.67 | 1.00 | ❌ |
| ADM003 | zero_recall | — | 1.00 | 0.50 | 0.35 | 0.67 | 0.00 | ❌ |
| ADM004 | zero_recall | — | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | ❌ |
| ADM005 | zero_recall | — | 1.00 | 0.50 | 0.30 | 0.33 | 0.00 | ❌ |
| ADM006 | zero_recall | — | 0.93 | 1.00 | 0.70 | 1.00 | 0.00 | ❌ |
| ADM007 | no_gold_articles | — | 1.00 | 0.50 | 0.20 | 1.00 | 0.50 | ❌ |
| ADM008 | partial_recall | — | 1.00 | 0.50 | 0.70 | 0.67 | 1.00 | ❌ |
| ADM009 | full_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 0.50 | ❌ |
| ADM010 | zero_recall | — | 1.00 | 1.00 | 0.70 | 1.00 | 0.00 | ❌ |
| ADM011 | full_recall | — | 1.00 | 0.50 | 0.60 | 1.00 | 1.00 | ❌ |
| ADM012 | zero_recall | — | 0.83 | 0.50 | 0.50 | 0.67 | 0.00 | ❌ |
| ADM013 | zero_recall | — | 1.00 | 1.00 | 0.70 | 1.00 | 0.00 | ❌ |
| ADM014 | zero_recall | — | 0.75 | 0.00 | 0.10 | 0.00 | 0.00 | ❌ |
| ADM015 | zero_recall | — | 1.00 | 0.50 | 0.40 | 1.00 | 1.00 | ❌ |
| ADM016 | zero_recall | — | 0.50 | 0.00 | 0.10 | 0.00 | 0.00 | ❌ |
| ADM017 | zero_recall | — | 0.86 | 0.50 | 0.60 | 0.67 | 1.00 | ❌ |
| ADM018 | zero_recall | — | 1.00 | 0.50 | 0.40 | 0.67 | 0.00 | ❌ |
| ADM019 | zero_recall | — | 1.00 | 0.50 | 0.30 | 1.00 | 0.00 | ❌ |
| ADM020 | zero_recall | — | 0.83 | 0.50 | 0.20 | 1.00 | 0.00 | ❌ |
| ADM021 | zero_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 0.00 | ❌ |
| ADM022 | zero_recall | — | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | ❌ |
| ADM023 | full_recall | — | 1.00 | 0.50 | 0.90 | 0.33 | 0.50 | ❌ |
| ADM024 | zero_recall | — | 1.00 | 0.00 | 0.20 | 0.33 | 0.50 | ❌ |
| ADM025 | full_recall | — | 1.00 | 0.50 | 0.85 | 0.67 | 1.00 | ❌ |
| ADM026 | full_recall | — | 0.88 | 0.75 | 0.85 | 0.33 | 1.00 | ❌ |
| ADM027 | full_recall | — | 0.75 | 1.00 | 0.85 | 1.00 | 1.00 | ❌ |
| ADM028 | zero_recall | — | 0.50 | 0.00 | 0.10 | 0.67 | 0.00 | ❌ |
| ADM029 | partial_recall | — | 1.00 | 0.50 | 0.82 | 0.67 | 0.50 | ❌ |
| ADM030 | zero_recall | — | 0.75 | 0.10 | 0.20 | 0.67 | 1.00 | ❌ |
| ADM031 | zero_recall | — | 1.00 | 0.50 | 0.85 | 0.67 | 0.00 | ❌ |
| ADM032 | zero_recall | — | 1.00 | 0.50 | 0.60 | 1.00 | 0.00 | ❌ |
| ADM033 | zero_recall | — | 1.00 | 0.10 | 0.30 | 0.33 | 1.00 | ❌ |
| ADM_REF001 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF003 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF004 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF005 | no_gold_articles | — | — | — | — | — | — | ❌ |
