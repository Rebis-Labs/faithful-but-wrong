# fbw-eval report

Generated 2026-11-06 22:04 UTC · 30 questions (25 answerable, 5 refusable) · stratifiable 24/30 (80%)
- **gold:** docs/paper_v2/reports/v2_criminal_anchor59/gold.jsonl
- **outputs:** eval/reports/fbw/v2/v2_vanilla_criminal/outputs.jsonl
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
| full_recall | 14 | 0.0 [0.0, 0.0] | 95.1 [91.1, 98.4] | 63.9 [50.7, 76.1] | 85.7 [75.0, 96.4] | 0 |
| partial_recall | 2 | 0.0 [0.0, 0.0] | 96.0 [92.0, 100.0] | 50.0 [50.0, 50.0] | 70.8 [66.7, 75.0] | 0 |
| zero_recall | 8 | 12.5 [0.0, 37.5] | 75.0 [50.0, 100.0] | 35.0 [12.5, 63.7] | 54.2 [25.0, 81.2] | 0 |
| no_gold_articles | 6 | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 50.0 [50.0, 50.0] | 100.0 [100.0, 100.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 3.3 [0.0, 10.0] |
| pass rate, refusal-driven passes excluded | 3.3 [0.0, 10.0] |
| faithfulness (answerable) | 88.9 [77.5, 97.8] |
| correctness (answerable) | 53.0 [41.6, 64.4] |
| answer relevancy (answerable) | 63.8 [53.9, 72.7] |
| context relevancy (answerable) | 58.7 [46.7, 72.0] |
| citation accuracy (answerable) | 75.0 [63.3, 86.7] |
| refusal accuracy | 83.3 [70.0, 96.7] |
| false refusals (FP) / missed refusals (FN) | 0 / 5 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| CRIM001 | zero_recall | — | 1.00 | 0.00 | 0.30 | 0.33 | 0.50 | ❌ |
| CRIM002 | full_recall | — | 1.00 | 0.50 | 0.85 | 0.33 | 1.00 | ❌ |
| CRIM003 | zero_recall | — | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | ❌ |
| CRIM004 | full_recall | — | 1.00 | 0.50 | 0.40 | 1.00 | 1.00 | ❌ |
| CRIM005 | partial_recall | — | 0.92 | 0.50 | 0.70 | 1.00 | 0.75 | ❌ |
| CRIM006 | no_gold_articles | — | 1.00 | 0.50 | 0.30 | 0.67 | 1.00 | ❌ |
| CRIM007 | full_recall | — | 1.00 | 1.00 | 0.85 | 0.67 | 0.50 | ❌ |
| CRIM008 | zero_recall | — | 1.00 | 0.50 | 0.70 | 1.00 | 1.00 | ❌ |
| CRIM009 | full_recall | — | 0.95 | 1.00 | 0.82 | 0.33 | 1.00 | ❌ |
| CRIM010 | full_recall | — | 0.91 | 0.80 | 0.85 | 0.33 | 0.50 | ❌ |
| CRIM011 | zero_recall | — | 1.00 | 1.00 | 0.85 | 0.67 | 0.50 | ❌ |
| CRIM012 | full_recall | — | 0.93 | 0.50 | 0.60 | 1.00 | 1.00 | ❌ |
| CRIM013 | full_recall | — | 1.00 | 0.10 | 0.80 | 0.33 | 1.00 | ❌ |
| CRIM014 | full_recall | — | 0.85 | 1.00 | 0.85 | 0.33 | 0.50 | ❌ |
| CRIM015 | zero_recall | — | 0.00 | 0.00 | 0.10 | 0.00 | 0.00 | ❌ |
| CRIM016 | full_recall | — | 1.00 | 0.50 | 0.70 | 0.67 | 1.00 | ❌ |
| CRIM017 | full_recall | — | 1.00 | 0.50 | 0.40 | 1.00 | 1.00 | ❌ |
| CRIM018 | full_recall | — | 1.00 | 0.50 | 0.70 | 1.00 | 0.75 | ❌ |
| CRIM019 | zero_recall | — | 1.00 | 0.70 | 0.70 | 0.67 | 1.00 | ❌ |
| CRIM020 | full_recall | — | 0.75 | 0.50 | 0.85 | 0.33 | 1.00 | ❌ |
| CRIM021 | zero_recall | — | 1.00 | 0.10 | 0.30 | 0.00 | 0.33 | ❌ |
| CRIM022 | partial_recall | — | 1.00 | 0.50 | 0.70 | 0.67 | 0.67 | ❌ |
| CRIM023 | full_recall | — | 1.00 | 0.80 | 0.85 | 0.33 | 1.00 | ❌ |
| CRIM024 | zero_recall | — | 1.00 | 0.50 | 0.85 | 1.00 | 1.00 | ✅ |
| CRIM025 | full_recall | — | 0.92 | 0.75 | 0.82 | 1.00 | 0.75 | ❌ |
| CRIM_REF001 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF003 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF004 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF005 | no_gold_articles | — | — | — | — | — | — | ❌ |
