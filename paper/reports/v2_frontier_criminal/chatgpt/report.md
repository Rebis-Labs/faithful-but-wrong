# fbw-eval report

Generated 2026-10-30 18:07 UTC · 30 questions (25 answerable, 5 refusable) · stratifiable 24/30 (80%)
- **gold:** docs/paper_v2/reports/v2_criminal_anchor59/gold.jsonl
- **outputs:** eval/reports/fbw/v2/frontier_criminal/outputs_chatgpt.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 75
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| zero_recall | 24 | 0.0 [0.0, 0.0] | 1.6 [0.0, 4.7] | 90.4 [83.3, 96.7] | 0.0 [0.0, 0.0] | 0 |
| no_gold_articles | 6 | 0.0 [0.0, 0.0] | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 0.0 [0.0, 0.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 0.0 [0.0, 0.0] |
| pass rate, refusal-driven passes excluded | 0.0 [0.0, 0.0] |
| faithfulness (answerable) | 1.5 [0.0, 4.5] |
| correctness (answerable) | 90.8 [84.0, 96.8] |
| answer relevancy (answerable) | 90.6 [87.0, 93.6] |
| context relevancy (answerable) | — |
| citation accuracy (answerable) | 0.0 [0.0, 0.0] |
| refusal accuracy | 83.3 [70.0, 96.7] |
| false refusals (FP) / missed refusals (FN) | 0 / 5 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| CRIM001 | zero_recall | — | 0.00 | 1.00 | 1.00 | — | 0.00 | ❌ |
| CRIM002 | zero_recall | — | 0.00 | 0.50 | 0.95 | — | 0.00 | ❌ |
| CRIM003 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM004 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| CRIM005 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM006 | no_gold_articles | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM007 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM008 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM009 | zero_recall | — | 0.00 | 1.00 | 0.60 | — | 0.00 | ❌ |
| CRIM010 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM011 | zero_recall | — | 0.38 | 1.00 | 1.00 | — | 0.00 | ❌ |
| CRIM012 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| CRIM013 | zero_recall | — | 0.00 | 0.50 | 0.80 | — | 0.00 | ❌ |
| CRIM014 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| CRIM015 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM016 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM017 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM018 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM019 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM020 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| CRIM021 | zero_recall | — | 0.00 | 0.80 | 0.85 | — | 0.00 | ❌ |
| CRIM022 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| CRIM023 | zero_recall | — | 0.00 | 0.80 | 0.85 | — | 0.00 | ❌ |
| CRIM024 | zero_recall | — | 0.00 | 0.80 | 0.85 | — | 0.00 | ❌ |
| CRIM025 | zero_recall | — | 0.00 | 0.80 | 0.95 | — | 0.00 | ❌ |
| CRIM_REF001 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF003 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF004 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF005 | no_gold_articles | — | — | — | — | — | — | ❌ |
