# fbw-eval report

Generated 2026-10-20 10:11 UTC · 23 questions (23 answerable, 0 refusable) · stratifiable 23/23 (100%)
- **gold:** eval/reports/fbw/v2/interpelli_lavoro_prassi/gold.jsonl
- **outputs:** eval/reports/fbw/v2/interpelli_lavoro_prassi/outputs.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 0
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['Ministero del Lavoro, interpello-1/2019 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-1/2020 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-1/2021 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-1/2022 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-1/2023 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-1/2024 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-2/2019 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-2/2021 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-2/2022 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-2/2023 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-2/2024 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-3/2019 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-3/2021 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-3/2022 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-3/2023 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-3/2024 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-4/2019 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-4/2023 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-4/2024 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-5/2019 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-5/2023 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-6/2019 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione', 'Ministero del Lavoro, interpello-8/2019 (risposta ufficiale = ground truth); estratto LLM 17 set 2026, revisione umana della selezione']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| full_recall | 3 | 0.0 [0.0, 0.0] | 84.7 [66.7, 100.0] | 83.3 [50.0, 100.0] | 100.0 [100.0, 100.0] | 0 |
| partial_recall | 20 | 45.0 [25.0, 65.0] | 90.2 [82.4, 96.4] | 79.0 [63.0, 92.5] | 100.0 [100.0, 100.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 39.1 [21.7, 60.9] |
| pass rate, refusal-driven passes excluded | 39.1 [21.7, 60.9] |
| faithfulness (answerable) | 89.5 [83.0, 95.2] |
| correctness (answerable) | 79.6 [66.5, 91.3] |
| answer relevancy (answerable) | 77.6 [70.0, 84.6] |
| context relevancy (answerable) | 91.4 [85.0, 97.1] |
| citation accuracy (answerable) | 100.0 [100.0, 100.0] |
| refusal accuracy | 100.0 [100.0, 100.0] |
| false refusals (FP) / missed refusals (FN) | 0 / 0 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| INT001 | full_recall | — | 1.00 | 1.00 | 0.85 | 0.67 | 1.00 | ❌ |
| INT002 | partial_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| INT003 | partial_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| INT004 | partial_recall | — | 1.00 | 1.00 | 0.90 | 0.67 | 1.00 | ❌ |
| INT005 | partial_recall | — | 0.71 | 1.00 | 0.60 | 0.67 | 1.00 | ❌ |
| INT006 | partial_recall | — | 1.00 | 0.80 | 0.85 | 1.00 | 1.00 | ✅ |
| INT007 | partial_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| INT008 | partial_recall | — | 0.90 | 1.00 | 0.85 | 0.75 | 1.00 | ❌ |
| INT010 | partial_recall | — | 0.83 | 1.00 | 0.85 | 1.00 | 1.00 | ❌ |
| INT011 | partial_recall | — | 1.00 | 0.50 | 0.85 | 1.00 | 1.00 | ✅ |
| INT012 | partial_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
| INT013 | partial_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| INT014 | partial_recall | — | 1.00 | 0.50 | 0.60 | 1.00 | 1.00 | ❌ |
| INT015 | partial_recall | — | 0.71 | 0.50 | 0.30 | 1.00 | 1.00 | ❌ |
| INT016 | partial_recall | — | 1.00 | 1.00 | 0.70 | 1.00 | 1.00 | ❌ |
| INT017 | partial_recall | — | 0.40 | 0.00 | 0.95 | 1.00 | 1.00 | ❌ |
| INT018 | full_recall | — | 0.67 | 1.00 | 0.40 | 1.00 | 1.00 | ❌ |
| INT019 | full_recall | — | 0.88 | 0.50 | 0.60 | 1.00 | 1.00 | ❌ |
| INT020 | partial_recall | — | 1.00 | 1.00 | 0.85 | 1.00 | 1.00 | ✅ |
| INT021 | partial_recall | — | 1.00 | 1.00 | 0.85 | 0.60 | 1.00 | ❌ |
| INT022 | partial_recall | — | 0.78 | 0.00 | 0.60 | 1.00 | 1.00 | ❌ |
| INT023 | partial_recall | — | 0.71 | 0.50 | 0.70 | 0.67 | 1.00 | ❌ |
| INT024 | partial_recall | — | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | ✅ |
