# fbw-eval report

Generated 2026-11-06 22:46 UTC · 30 questions (25 answerable, 5 refusable) · stratifiable 24/30 (80%)
- **gold:** docs/paper_v2/reports/v2_criminal_anchor59/gold.jsonl
- **outputs:** docs/paper_v2/reports/v2_criminal/outputs.jsonl
- **judge:** openai/gpt-4o-mini
- **judge calls:** 204
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['|anchor_2026-10-28:confirmed|anchor_2026-10-28:confirmed', '|anchor_2026-10-28:fixed|anchor_2026-10-28:fixed', '|anchor_2026-10-28:no_gold|anchor_2026-10-28:no_gold']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 21 | 66.7 [47.6, 85.7] | 97.1 [94.3, 100.0] | 90.5 [81.0, 97.6] | 95.2 [86.9, 100.0] | 0 |
| partial_recall | 1 | 0.0 [0.0, 0.0] | 100.0 [100.0, 100.0] | 50.0 [50.0, 50.0] | 50.0 [50.0, 50.0] | 0 |
| zero_recall | 2 | 50.0 [0.0, 100.0] | 100.0 [100.0, 100.0] | 100.0 [100.0, 100.0] | 50.0 [0.0, 100.0] | 0 |
| no_gold_articles | 6 | 66.7 [33.3, 100.0] | 100.0 [100.0, 100.0] | 50.0 [50.0, 50.0] | 0.0 [0.0, 0.0] | 4 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 63.3 [46.7, 80.0] |
| pass rate, refusal-driven passes excluded | 50.0 [33.3, 66.7] |
| faithfulness (answerable) | 97.6 [95.2, 100.0] |
| correctness (answerable) | 88.0 [80.0, 96.0] |
| answer relevancy (answerable) | 100.0 [100.0, 100.0] |
| context relevancy (answerable) | 91.3 [84.7, 96.9] |
| citation accuracy (answerable) | 86.0 [74.0, 96.0] |
| refusal accuracy | 96.7 [90.0, 100.0] |
| false refusals (FP) / missed refusals (FN) | 0 / 1 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| CRIM001 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.60 | 1.00 | ❌ |
| CRIM002 | full_recall | — | 0.80 | 0.50 | 1.00 | 1.00 | 1.00 | ❌ |
| CRIM003 | partial_recall | — | 1.00 | 0.50 | 1.00 | 0.75 | 0.50 | ❌ |
| CRIM004 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM005 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM006 | no_gold_articles | — | 1.00 | 0.50 | 1.00 | 0.83 | 0.00 | ❌ |
| CRIM007 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM008 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM009 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM010 | full_recall | — | 0.80 | 1.00 | 1.00 | 1.00 | 1.00 | ❌ |
| CRIM011 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM012 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM013 | full_recall | — | 0.80 | 1.00 | 1.00 | 0.50 | 1.00 | ❌ |
| CRIM014 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM015 | full_recall | — | 1.00 | 0.50 | 1.00 | 0.71 | 0.25 | ❌ |
| CRIM016 | full_recall | — | 1.00 | 0.50 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM017 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM018 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM019 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM020 | full_recall | — | 1.00 | 1.00 | 1.00 | 0.57 | 1.00 | ❌ |
| CRIM021 | zero_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.00 | ❌ |
| CRIM022 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 0.75 | ❌ |
| CRIM023 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM024 | zero_recall | — | 1.00 | 1.00 | 1.00 | 0.86 | 1.00 | ✅ |
| CRIM025 | full_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| CRIM_REF001 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| CRIM_REF002 | no_gold_articles | — | — | — | — | — | — | ❌ |
| CRIM_REF003 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| CRIM_REF004 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
| CRIM_REF005 | no_gold_articles | ⛔ | — | — | — | — | — | ✅ |
