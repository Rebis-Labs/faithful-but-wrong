# fbw-eval report

Generated 2026-11-06 23:05 UTC · 38 questions (33 answerable, 5 refusable) · stratifiable 32/38 (84%)
- **gold:** docs/paper_v2/reports/v2_admin_anchor59/gold.jsonl
- **outputs:** eval/reports/fbw/v2/v2_vanilla_admin/outputs.jsonl
- **judge:** openai/gpt-4o-mini
- **judge calls:** 198
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 6 | 33.3 [0.0, 66.7] | 100.0 [100.0, 100.0] | 75.0 [58.3, 91.7] | 83.3 [66.7, 100.0] | 0 |
| partial_recall | 2 | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 75.0 [50.0, 100.0] | 75.0 [50.0, 100.0] | 0 |
| zero_recall | 24 | 12.5 [0.0, 29.2] | 91.7 [79.2, 100.0] | 50.0 [39.6, 62.5] | 27.1 [10.4, 43.8] | 0 |
| no_gold_articles | 6 | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 50.0 [50.0, 50.0] | 50.0 [50.0, 50.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 13.2 [2.6, 23.7] |
| pass rate, refusal-driven passes excluded | 13.2 [2.6, 23.7] |
| faithfulness (answerable) | 93.9 [84.8, 100.0] |
| correctness (answerable) | 56.1 [45.5, 66.7] |
| answer relevancy (answerable) | 85.8 [73.0, 96.4] |
| context relevancy (answerable) | 83.8 [72.7, 91.9] |
| citation accuracy (answerable) | 40.9 [25.8, 56.1] |
| refusal accuracy | 86.8 [76.3, 97.4] |
| false refusals (FP) / missed refusals (FN) | 0 / 5 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| ADM001 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM002 | zero_recall | — | 1.00 | 0.50 | 1.00 | 0.67 | 1.00 | ❌ |
| ADM003 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM004 | zero_recall | — | 0.00 | 0.00 | 0.00 | 0.33 | 0.00 | ❌ |
| ADM005 | zero_recall | — | 1.00 | 0.50 | 1.00 | 0.33 | 0.00 | ❌ |
| ADM006 | zero_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM007 | no_gold_articles | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.50 | ❌ |
| ADM008 | partial_recall | — | 1.00 | 0.50 | 1.00 | 0.67 | 1.00 | ❌ |
| ADM009 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.50 | ❌ |
| ADM010 | zero_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM011 | full_recall | — | 1.00 | 0.50 | 1.00 | 0.67 | 1.00 | ❌ |
| ADM012 | zero_recall | — | 1.00 | 0.50 | 1.00 | 0.67 | 0.00 | ❌ |
| ADM013 | zero_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM014 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM015 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM016 | zero_recall | — | 0.00 | 0.00 | 0.00 | 0.00 | 0.00 | ❌ |
| ADM017 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM018 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM019 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM020 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM021 | zero_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM022 | zero_recall | — | 1.00 | 0.00 | 0.00 | 0.33 | 0.00 | ❌ |
| ADM023 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.50 | ❌ |
| ADM024 | zero_recall | — | 1.00 | 0.50 | 1.00 | 0.33 | 0.50 | ❌ |
| ADM025 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM026 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| ADM027 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM028 | zero_recall | — | 1.00 | 0.00 | 0.00 | 1.00 | 0.00 | ❌ |
| ADM029 | partial_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.50 | ❌ |
| ADM030 | zero_recall | — | 1.00 | 0.50 | 0.50 | 1.00 | 1.00 | ❌ |
| ADM031 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM032 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.00 | ❌ |
| ADM033 | zero_recall | — | 1.00 | 0.50 | 0.80 | 1.00 | 1.00 | ❌ |
| ADM_REF001 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF003 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF004 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF005 | no_gold_articles | — | — | — | — | — | — | ❌ |
