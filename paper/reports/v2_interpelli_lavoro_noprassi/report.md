# fbw-eval report

Generated 2026-10-20 10:11 UTC · 23 questions (23 answerable, 0 refusable) · stratifiable 23/23 (100%)
- **gold:** eval/reports/fbw/v2/interpelli_lavoro_noprassi/gold.jsonl
- **outputs:** eval/reports/fbw/v2/interpelli_lavoro_noprassi/outputs.jsonl
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
| partial_recall | 16 | 0.0 [0.0, 0.0] | 77.2 [68.8, 85.8] | 43.6 [29.3, 57.9] | 93.8 [81.2, 100.0] | 2 |
| zero_recall | 7 | 0.0 [0.0, 0.0] | 68.1 [51.7, 87.9] | 16.0 [2.0, 34.0] | 78.6 [50.0, 100.0] | 2 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 0.0 [0.0, 0.0] |
| pass rate, refusal-driven passes excluded | 0.0 [0.0, 0.0] |
| faithfulness (answerable) | 74.5 [66.5, 82.7] |
| correctness (answerable) | 36.3 [24.2, 48.9] |
| answer relevancy (answerable) | 56.5 [47.8, 67.0] |
| context relevancy (answerable) | 52.0 [36.8, 68.2] |
| citation accuracy (answerable) | 89.1 [76.1, 100.0] |
| refusal accuracy | 82.6 [65.2, 95.7] |
| false refusals (FP) / missed refusals (FN) | 4 / 0 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| INT001 | zero_recall | ⛔ | 1.00 | — | 1.00 | — | 1.00 | ❌ |
| INT002 | partial_recall | — | 0.83 | 0.50 | 0.50 | 1.00 | 1.00 | ❌ |
| INT003 | partial_recall | ⛔ | 1.00 | — | 1.00 | — | 1.00 | ❌ |
| INT004 | partial_recall | — | 0.67 | 0.50 | 0.60 | 1.00 | 1.00 | ❌ |
| INT005 | zero_recall | ⛔ | 1.00 | — | 1.00 | — | 1.00 | ❌ |
| INT006 | zero_recall | — | 0.86 | 0.00 | 0.30 | 0.33 | 0.00 | ❌ |
| INT007 | partial_recall | ⛔ | 1.00 | — | 1.00 | — | 1.00 | ❌ |
| INT008 | zero_recall | — | 0.44 | 0.20 | 0.60 | 0.60 | 0.50 | ❌ |
| INT010 | partial_recall | — | 0.75 | 0.50 | 0.60 | 0.33 | 1.00 | ❌ |
| INT011 | partial_recall | — | 0.80 | 0.20 | 0.60 | 1.00 | 1.00 | ❌ |
| INT012 | zero_recall | — | 0.43 | 0.50 | 0.40 | 0.50 | 1.00 | ❌ |
| INT013 | partial_recall | — | 1.00 | 0.50 | 0.30 | 0.25 | 0.00 | ❌ |
| INT014 | partial_recall | — | 0.78 | 0.50 | 0.60 | 1.00 | 1.00 | ❌ |
| INT015 | partial_recall | — | 0.75 | 0.50 | 0.60 | 0.33 | 1.00 | ❌ |
| INT016 | partial_recall | — | 1.00 | 0.50 | 0.30 | 0.33 | 1.00 | ❌ |
| INT017 | partial_recall | — | 0.40 | 0.50 | 0.40 | 0.33 | 1.00 | ❌ |
| INT018 | partial_recall | — | 0.86 | 0.80 | 0.50 | 1.00 | 1.00 | ❌ |
| INT019 | partial_recall | — | 0.75 | 1.00 | 0.60 | 1.00 | 1.00 | ❌ |
| INT020 | partial_recall | — | 0.50 | 0.00 | 0.40 | 0.00 | 1.00 | ❌ |
| INT021 | partial_recall | — | 0.67 | 0.00 | 0.70 | 0.20 | 1.00 | ❌ |
| INT022 | zero_recall | — | 0.44 | 0.00 | 0.30 | 0.00 | 1.00 | ❌ |
| INT023 | zero_recall | — | 0.60 | 0.10 | 0.40 | 0.33 | 1.00 | ❌ |
| INT024 | partial_recall | — | 0.60 | 0.10 | 0.30 | 0.33 | 1.00 | ❌ |
