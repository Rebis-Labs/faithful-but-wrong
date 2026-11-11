# fbw-eval report

Generated 2026-11-06 22:52 UTC · 38 questions (33 answerable, 5 refusable) · stratifiable 32/38 (84%)
- **gold:** docs/paper_v2/reports/v2_admin_anchor59/gold.jsonl
- **outputs:** eval/reports/fbw/v2/v2_vanillaj_admin/outputs.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 197
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 7 | 14.3 [0.0, 42.9] | 86.6 [71.6, 98.4] | 61.4 [35.7, 82.9] | 92.9 [78.6, 100.0] | 0 |
| partial_recall | 1 | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 50.0 [50.0, 50.0] | 50.0 [50.0, 50.0] | 0 |
| zero_recall | 24 | 0.0 [0.0, 0.0] | 81.6 [67.6, 93.4] | 36.7 [24.6, 49.6] | 28.5 [12.5, 46.5] | 0 |
| no_gold_articles | 6 | 0.0 [0.0, 0.0] | 85.7 [85.7, 85.7] | 50.0 [50.0, 50.0] | 100.0 [100.0, 100.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 2.6 [0.0, 7.9] |
| pass rate, refusal-driven passes excluded | 2.6 [0.0, 7.9] |
| faithfulness (answerable) | 83.3 [72.0, 92.2] |
| correctness (answerable) | 42.7 [31.8, 53.9] |
| answer relevancy (answerable) | 45.6 [37.3, 53.9] |
| context relevancy (answerable) | 71.7 [60.6, 82.8] |
| citation accuracy (answerable) | 44.9 [29.8, 61.1] |
| refusal accuracy | 86.8 [76.3, 97.4] |
| false refusals (FP) / missed refusals (FN) | 0 / 5 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| ADM001 | zero_recall | — | 1.00 | 0.10 | 0.30 | 0.33 | 0.33 | ❌ |
| ADM002 | zero_recall | — | 0.71 | 0.10 | 0.30 | 0.33 | 0.50 | ❌ |
| ADM003 | zero_recall | — | 1.00 | 0.10 | 0.20 | 0.67 | 0.00 | ❌ |
| ADM004 | zero_recall | — | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | ❌ |
| ADM005 | zero_recall | — | 1.00 | 0.50 | 0.30 | 0.33 | 0.00 | ❌ |
| ADM006 | zero_recall | — | 1.00 | 0.50 | 0.60 | 1.00 | 0.00 | ❌ |
| ADM007 | no_gold_articles | — | 0.86 | 0.50 | 0.30 | 1.00 | 1.00 | ❌ |
| ADM008 | zero_recall | — | 0.00 | 0.50 | 0.70 | 0.67 | 0.00 | ❌ |
| ADM009 | full_recall | — | 1.00 | 1.00 | 0.90 | 1.00 | 0.50 | ❌ |
| ADM010 | zero_recall | — | 1.00 | 1.00 | 0.70 | 1.00 | 0.00 | ❌ |
| ADM011 | zero_recall | — | 1.00 | 0.20 | 0.20 | 1.00 | 1.00 | ❌ |
| ADM012 | full_recall | — | 0.50 | 0.50 | 0.20 | 1.00 | 1.00 | ❌ |
| ADM013 | zero_recall | — | 1.00 | 1.00 | 0.70 | 1.00 | 0.00 | ❌ |
| ADM014 | zero_recall | — | 1.00 | 0.00 | 0.20 | 0.33 | 1.00 | ❌ |
| ADM015 | zero_recall | — | 1.00 | 0.50 | 0.40 | 1.00 | 1.00 | ❌ |
| ADM016 | zero_recall | — | 0.50 | 0.00 | 0.10 | 0.00 | 0.00 | ❌ |
| ADM017 | zero_recall | — | 0.80 | 0.50 | 0.50 | 0.67 | 1.00 | ❌ |
| ADM018 | zero_recall | — | 1.00 | 0.20 | 0.35 | 0.67 | 0.00 | ❌ |
| ADM019 | zero_recall | — | 0.86 | 0.50 | 0.30 | 1.00 | 0.00 | ❌ |
| ADM020 | zero_recall | — | 0.83 | 0.50 | 0.30 | 1.00 | 0.00 | ❌ |
| ADM021 | zero_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 0.00 | ❌ |
| ADM022 | zero_recall | — | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | ❌ |
| ADM023 | full_recall | — | 1.00 | 0.00 | 0.50 | 0.67 | 1.00 | ❌ |
| ADM024 | full_recall | — | 1.00 | 0.50 | 0.60 | 1.00 | 1.00 | ❌ |
| ADM025 | full_recall | — | 0.89 | 0.50 | 0.85 | 1.00 | 1.00 | ❌ |
| ADM026 | full_recall | — | 1.00 | 0.80 | 0.85 | 1.00 | 1.00 | ✅ |
| ADM027 | full_recall | — | 0.67 | 1.00 | 0.85 | 1.00 | 1.00 | ❌ |
| ADM028 | zero_recall | — | 1.00 | 0.00 | 0.10 | 0.67 | 0.00 | ❌ |
| ADM029 | partial_recall | — | 1.00 | 0.50 | 0.70 | 0.67 | 0.50 | ❌ |
| ADM030 | zero_recall | — | 1.00 | 0.10 | 0.10 | 0.67 | 1.00 | ❌ |
| ADM031 | zero_recall | — | 1.00 | 0.50 | 0.60 | 0.67 | 0.00 | ❌ |
| ADM032 | zero_recall | — | 1.00 | 0.50 | 0.50 | 1.00 | 0.00 | ❌ |
| ADM033 | zero_recall | — | 0.88 | 0.50 | 0.60 | 0.33 | 1.00 | ❌ |
| ADM_REF001 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF003 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF004 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF005 | no_gold_articles | — | — | — | — | — | — | ❌ |
