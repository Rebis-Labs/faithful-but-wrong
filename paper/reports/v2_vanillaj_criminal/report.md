# fbw-eval report

Generated 2026-11-06 22:43 UTC · 30 questions (25 answerable, 5 refusable) · stratifiable 24/30 (80%)
- **gold:** docs/paper_v2/reports/v2_criminal_anchor59/gold.jsonl
- **outputs:** eval/reports/fbw/v2/v2_vanillaj_criminal/outputs.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 150
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 16 | 12.5 [0.0, 31.2] | 96.9 [92.8, 100.0] | 62.5 [51.9, 73.8] | 98.4 [95.3, 100.0] | 0 |
| partial_recall | 2 | 0.0 [0.0, 0.0] | 96.0 [92.0, 100.0] | 50.0 [50.0, 50.0] | 70.8 [66.7, 75.0] | 0 |
| zero_recall | 6 | 16.7 [0.0, 50.0] | 75.8 [42.5, 96.7] | 28.3 [8.3, 51.7] | 63.9 [30.6, 91.7] | 0 |
| no_gold_articles | 6 | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 50.0 [50.0, 50.0] | 100.0 [100.0, 100.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 10.0 [0.0, 23.3] |
| pass rate, refusal-driven passes excluded | 10.0 [0.0, 23.3] |
| faithfulness (answerable) | 91.9 [83.2, 98.0] |
| correctness (answerable) | 52.8 [42.8, 63.2] |
| answer relevancy (answerable) | 60.1 [51.7, 68.5] |
| context relevancy (answerable) | 72.0 [60.0, 84.0] |
| citation accuracy (answerable) | 88.0 [77.7, 96.7] |
| refusal accuracy | 83.3 [70.0, 96.7] |
| false refusals (FP) / missed refusals (FN) | 0 / 5 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| CRIM001 | zero_recall | — | 0.80 | 0.00 | 0.30 | 0.33 | 0.50 | ❌ |
| CRIM002 | full_recall | — | 1.00 | 0.50 | 0.40 | 0.67 | 1.00 | ❌ |
| CRIM003 | zero_recall | — | 0.00 | 0.00 | 0.20 | 0.00 | 0.00 | ❌ |
| CRIM004 | full_recall | — | 1.00 | 0.50 | 0.40 | 1.00 | 1.00 | ❌ |
| CRIM005 | partial_recall | — | 0.92 | 0.50 | 0.60 | 1.00 | 0.75 | ❌ |
| CRIM006 | no_gold_articles | — | 1.00 | 0.50 | 0.20 | 0.67 | 1.00 | ❌ |
| CRIM007 | full_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| CRIM008 | zero_recall | — | 1.00 | 0.50 | 0.40 | 1.00 | 1.00 | ❌ |
| CRIM009 | full_recall | — | 1.00 | 1.00 | 0.70 | 0.33 | 1.00 | ❌ |
| CRIM010 | full_recall | — | 1.00 | 0.50 | 0.70 | 0.67 | 1.00 | ❌ |
| CRIM011 | full_recall | — | 1.00 | 1.00 | 0.90 | 1.00 | 1.00 | ✅ |
| CRIM012 | full_recall | — | 0.91 | 0.50 | 0.70 | 1.00 | 1.00 | ❌ |
| CRIM013 | full_recall | — | 1.00 | 0.20 | 0.70 | 0.33 | 1.00 | ❌ |
| CRIM014 | full_recall | — | 1.00 | 0.50 | 0.70 | 0.67 | 1.00 | ❌ |
| CRIM015 | full_recall | — | 1.00 | 0.50 | 0.40 | 1.00 | 1.00 | ❌ |
| CRIM016 | full_recall | — | 1.00 | 0.80 | 0.70 | 1.00 | 1.00 | ❌ |
| CRIM017 | full_recall | — | 1.00 | 0.50 | 0.40 | 1.00 | 1.00 | ❌ |
| CRIM018 | full_recall | — | 1.00 | 0.80 | 0.70 | 1.00 | 1.00 | ❌ |
| CRIM019 | zero_recall | — | 1.00 | 0.70 | 0.70 | 0.67 | 1.00 | ❌ |
| CRIM020 | full_recall | — | 0.83 | 0.70 | 0.85 | 0.33 | 1.00 | ❌ |
| CRIM021 | zero_recall | — | 0.75 | 0.00 | 0.30 | 0.00 | 0.33 | ❌ |
| CRIM022 | partial_recall | — | 1.00 | 0.50 | 0.70 | 0.67 | 0.67 | ❌ |
| CRIM023 | full_recall | — | 0.76 | 0.50 | 0.85 | 0.67 | 1.00 | ❌ |
| CRIM024 | zero_recall | — | 1.00 | 0.50 | 0.85 | 1.00 | 1.00 | ✅ |
| CRIM025 | full_recall | — | 1.00 | 0.50 | 0.82 | 1.00 | 0.75 | ❌ |
| CRIM_REF001 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF003 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF004 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF005 | no_gold_articles | — | — | — | — | — | — | ❌ |
