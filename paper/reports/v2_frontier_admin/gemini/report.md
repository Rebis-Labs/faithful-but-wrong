# fbw-eval report

Generated 2026-10-29 21:39 UTC · 38 questions (33 answerable, 5 refusable) · stratifiable 32/38 (84%)
- **gold:** eval/reports/fbw/v2/admin/gold.jsonl
- **outputs:** eval/reports/fbw/v2/frontier_admin/outputs_gemini.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 99
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| zero_recall | 32 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 90.6 [81.2, 98.4] | 0.0 [0.0, 0.0] | 0 |
| no_gold_articles | 6 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 0.0 [0.0, 0.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 0.0 [0.0, 0.0] |
| pass rate, refusal-driven passes excluded | 0.0 [0.0, 0.0] |
| faithfulness (answerable) | 0.0 [0.0, 0.0] |
| correctness (answerable) | 90.9 [81.8, 98.5] |
| answer relevancy (answerable) | 86.3 [79.3, 90.9] |
| context relevancy (answerable) | — |
| citation accuracy (answerable) | 0.0 [0.0, 0.0] |
| refusal accuracy | 86.8 [76.3, 97.4] |
| false refusals (FP) / missed refusals (FN) | 0 / 5 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| ADM001 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM002 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| ADM003 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM004 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| ADM005 | zero_recall | — | 0.00 | 1.00 | 0.90 | — | 0.00 | ❌ |
| ADM006 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM007 | no_gold_articles | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| ADM008 | zero_recall | — | 0.00 | 1.00 | 1.00 | — | 0.00 | ❌ |
| ADM009 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM010 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM011 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM012 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| ADM013 | zero_recall | — | 0.00 | 1.00 | 0.90 | — | 0.00 | ❌ |
| ADM014 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM015 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| ADM016 | zero_recall | — | 0.00 | 0.50 | 0.90 | — | 0.00 | ❌ |
| ADM017 | zero_recall | — | 0.00 | 1.00 | 0.60 | — | 0.00 | ❌ |
| ADM018 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM019 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| ADM020 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| ADM021 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| ADM022 | zero_recall | — | 0.00 | 1.00 | 0.70 | — | 0.00 | ❌ |
| ADM023 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM024 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM025 | zero_recall | — | 0.00 | 1.00 | 0.90 | — | 0.00 | ❌ |
| ADM026 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| ADM027 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM028 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| ADM029 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM030 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| ADM031 | zero_recall | — | 0.00 | 0.00 | 0.00 | — | 0.00 | ❌ |
| ADM032 | zero_recall | — | 0.00 | 1.00 | 0.90 | — | 0.00 | ❌ |
| ADM033 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| ADM_REF001 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF003 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF004 | no_gold_articles | — | — | — | — | — | — | ❌ |
| ADM_REF005 | no_gold_articles | — | — | — | — | — | — | ❌ |
