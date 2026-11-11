# fbw-eval report

Generated 2026-11-06 22:55 UTC · 38 questions (33 answerable, 5 refusable) · stratifiable 32/38 (84%)
- **gold:** docs/paper_v2/reports/v2_admin_anchor59/gold.jsonl
- **outputs:** docs/paper_v2/reports/v2_admin/outputs.jsonl
- **judge:** openai/gpt-4o-mini
- **judge calls:** 240
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 23 | 60.9 [39.1, 78.3] | 100.0 [100.0, 100.0] | 91.3 [82.6, 97.8] | 93.3 [86.2, 99.1] | 0 |
| partial_recall | 4 | 75.0 [25.0, 100.0] | 100.0 [100.0, 100.0] | 87.5 [62.5, 100.0] | 100.0 [100.0, 100.0] | 0 |
| zero_recall | 5 | 60.0 [20.0, 100.0] | 100.0 [100.0, 100.0] | 80.0 [60.0, 100.0] | 90.0 [70.0, 100.0] | 0 |
| no_gold_articles | 6 | 66.7 [33.3, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 3 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 63.2 [47.4, 78.9] |
| pass rate, refusal-driven passes excluded | 55.3 [39.5, 71.1] |
| faithfulness (answerable) | 100.0 [100.0, 100.0] |
| correctness (answerable) | 89.4 [81.8, 95.5] |
| answer relevancy (answerable) | 100.0 [100.0, 100.0] |
| context relevancy (answerable) | 90.8 [84.7, 96.6] |
| citation accuracy (answerable) | 93.8 [88.1, 98.5] |
| refusal accuracy | 94.7 [86.8, 100.0] |
| false refusals (FP) / missed refusals (FN) | 0 / 2 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| ADM001 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM002 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.40 | 1.00 | ❌ |
| ADM003 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM004 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM005 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM006 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM007 | no_gold_articles | — | 1.00 | 1.00 | 1.00 | 0.80 | 1.00 | ✅ |
| ADM008 | partial_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM009 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM010 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.60 | 1.00 | ❌ |
| ADM011 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM012 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM013 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM014 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM015 | partial_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM016 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM017 | partial_recall | — | 1.00 | 0.50 | 1.00 | 0.75 | 1.00 | ❌ |
| ADM018 | zero_recall | — | 1.00 | 1.00 | 1.00 | 0.40 | 1.00 | ❌ |
| ADM019 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.75 | 1.00 | ❌ |
| ADM020 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.67 | ❌ |
| ADM021 | zero_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM022 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM023 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.50 | ❌ |
| ADM024 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM025 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.80 | ❌ |
| ADM026 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.50 | ❌ |
| ADM027 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM028 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.67 | 1.00 | ❌ |
| ADM029 | partial_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM030 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM031 | zero_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| ADM032 | zero_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 0.50 | ❌ |
| ADM033 | full_recall | — | 1.00 | 0.50 | 1.00 | 0.60 | 1.00 | ❌ |
| ADM_REF001 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF003 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| ADM_REF004 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| ADM_REF005 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
