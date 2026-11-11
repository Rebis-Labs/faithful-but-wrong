# fbw-eval report

Generated 2026-10-26 16:58 UTC · 111 questions (111 answerable, 0 refusable) · stratifiable 111/111 (100%)
- **gold:** docs/paper_v2/reports/v2_trib2026_prassi/gold.jsonl
- **outputs:** eval/reports/fbw/v2/frontier_trib2026/outputs_chatgpt.jsonl
- **judge:** anthropic/claude-sonnet-4.6
- **judge calls:** 333
- **harness:** fbw-eval 0.1.0.dev0
- **thresholds:** {'faithfulness': 0.9, 'answer_relevancy': 0.85, 'context_relevancy': 0.8, 'citation_accuracy': 0.9, 'correctness': None}
- **seed:** 2026
- **citation parser:** built-in [Source: …] tags
- **gold provenance:** ['Agenzia delle Entrate, Risposta a interpello n. 1/2026 del 12/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 100/2026 del 2/04/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 101/2026 del 2/04/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 102/2026 del 2/04/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 103/2026 del 2/04/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 106/2026 del 25/05/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 109/2026 del 26/05/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 11/2026 del 20/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 110/2026 del 27/05/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 113/2026 del 29/05/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 115/2026 del 4/06/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 116/2026 del 4/06/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 117/2026 del 4/06/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 118/2026 del 8/06/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 119/2026 del 8/06/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 12/2026 del 20/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 124/2026 del 18/06/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 127/2026 del 22/06/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 128/2026 del 25/06/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 13/2026 del 20/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 130/2026 del 25/06/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 131/2026 del 25/06/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 134/2026 del 6/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 136/2026 del 8/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 138/2026 del 8/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 139/2026 del 10/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 14/2026 del 21/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 141/2026 del 10/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 143/2026 del 13/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 144/2026 del 13/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 145/2026 del 13/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 147/2026 del 16/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 15/2026 del 22/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 152/2026 del 31/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 153/2026 del 31/07/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 155/2026 del 7/08/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 156/2026 del 7/08/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 157/2026 del 10/08/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 158/2026 del 10/08/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 159/2026 del 10/08/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 163/2026 del 14/08/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 169/2026 del 3/09/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 173/2026 del 15/09/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 176/2026 del 21/09/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 178/2026 del 30/09/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 179/2026 del 1/10/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 2/2026 del 12/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 20/2026 del 27/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 21/2026 del 28/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 22/2026 del 9/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 23/2026 del 9/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 24/2026 del 9/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 25/2026 del 9/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 26/2026 del 10/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 27/2026 del 10/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 29/2026 del 10/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 3/2026 del 13/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 30/2026 del 10/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 31/2026 del 11/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 32/2026 del 11/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 33/2026 del 11/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 34/2026 del 11/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 35/2026 del 11/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 36/2026 del 11/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 38/2026 del 12/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 39/2026 del 12/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 4/2026 del 14/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 40/2026 del 16/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 41/2026 del 16/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 42/2026 del 18/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 44/2026 del 20/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 45/2026 del 24/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 46/2026 del 24/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 47/2026 del 24/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 48/2026 del 24/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 49/2026 del 24/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 5/2026 del 15/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 50/2026 del 25/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 51/2026 del 25/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 52/2026 del 25/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 54/2026 del 27/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 55/2026 del 27/02/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 58/2026 del 2/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 6/2026 del 16/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 60/2026 del 2/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 61/2026 del 3/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 62/2026 del 3/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 63/2026 del 3/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 64/2026 del 3/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 65/2026 del 4/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 67/2026 del 6/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 68/2026 del 6/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 7/2026 del 16/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 71/2026 del 9/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 74/2026 del 10/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 76/2026 del 11/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 77/2026 del 12/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 79/2026 del 12/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 8/2026 del 16/01/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 80/2026 del 18/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 82/2026 del 20/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 85/2026 del 26/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 86/2026 del 27/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 87/2026 del 30/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 88/2026 del 30/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 90/2026 del 31/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 91/2026 del 31/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 92/2026 del 31/03/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 96/2026 del 1/04/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 97/2026 del 1/04/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana', 'Agenzia delle Entrate, Risposta a interpello n. 98/2026 del 1/04/2026 (parere ufficiale = ground truth); estratto LLM 6 ott 2026 dal raw del crawler, selezione umana']

## Recall-conditional table (95% bootstrap CI, questions resampled)

| Bucket | n | pass rate | faithfulness | correctness | citation acc. | refusals |
|---|--:|--:|--:|--:|--:|--:|
| zero_recall | 111 | 0.0 [0.0, 0.0] | 2.0 [1.1, 3.1] | 38.1 [31.9, 44.0] | 0.0 [0.0, 0.0] | 0 |

Read across a row: faithfulness that stays high while correctness falls in `zero_recall` is the failure mode this protocol exists to show. Read down a column: how much of the aggregate comes from questions the retriever had already solved.

## End-task metrics (all questions)

| Metric | value |
|---|--:|
| pass rate | 0.0 [0.0, 0.0] |
| pass rate, refusal-driven passes excluded | 0.0 [0.0, 0.0] |
| faithfulness (answerable) | 2.0 [1.1, 3.1] |
| correctness (answerable) | 38.1 [31.9, 44.0] |
| answer relevancy (answerable) | 80.5 [78.2, 82.5] |
| context relevancy (answerable) | — |
| citation accuracy (answerable) | 0.0 [0.0, 0.0] |
| refusal accuracy | 100.0 [100.0, 100.0] |
| false refusals (FP) / missed refusals (FN) | 0 / 0 |

## Per-question

| id | bucket | refused | faith | corr | ansrel | ctxrel | cit | pass |
|---|---|---|--:|--:|--:|--:|--:|---|
| INTT001 | zero_recall | — | 0.00 | 0.50 | 0.90 | — | 0.00 | ❌ |
| INTT002 | zero_recall | — | 0.00 | 0.50 | 0.90 | — | 0.00 | ❌ |
| INTT003 | zero_recall | — | 0.00 | 0.10 | 0.82 | — | 0.00 | ❌ |
| INTT004 | zero_recall | — | 0.00 | 0.50 | 0.70 | — | 0.00 | ❌ |
| INTT005 | zero_recall | — | 0.00 | 1.00 | 0.90 | — | 0.00 | ❌ |
| INTT006 | zero_recall | — | 0.03 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT007 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT008 | zero_recall | — | 0.00 | 0.50 | 0.95 | — | 0.00 | ❌ |
| INTT011 | zero_recall | — | 0.09 | 1.00 | 0.82 | — | 0.00 | ❌ |
| INTT012 | zero_recall | — | 0.00 | 0.10 | 0.85 | — | 0.00 | ❌ |
| INTT013 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT014 | zero_recall | — | 0.00 | 0.80 | 0.95 | — | 0.00 | ❌ |
| INTT015 | zero_recall | — | 0.09 | 0.20 | 0.85 | — | 0.00 | ❌ |
| INTT020 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT021 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT022 | zero_recall | — | 0.00 | 0.00 | 0.82 | — | 0.00 | ❌ |
| INTT023 | zero_recall | — | 0.00 | 0.00 | 0.82 | — | 0.00 | ❌ |
| INTT024 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT025 | zero_recall | — | 0.00 | 0.80 | 0.70 | — | 0.00 | ❌ |
| INTT026 | zero_recall | — | 0.00 | 0.10 | 0.82 | — | 0.00 | ❌ |
| INTT027 | zero_recall | — | 0.09 | 0.50 | 0.70 | — | 0.00 | ❌ |
| INTT029 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT030 | zero_recall | — | 0.00 | 0.10 | 0.70 | — | 0.00 | ❌ |
| INTT031 | zero_recall | — | 0.00 | 0.70 | 0.85 | — | 0.00 | ❌ |
| INTT032 | zero_recall | — | 0.00 | 0.80 | 0.90 | — | 0.00 | ❌ |
| INTT033 | zero_recall | — | 0.00 | 0.00 | 0.45 | — | 0.00 | ❌ |
| INTT034 | zero_recall | — | 0.00 | 0.00 | 0.70 | — | 0.00 | ❌ |
| INTT035 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT036 | zero_recall | — | 0.00 | 0.20 | 0.82 | — | 0.00 | ❌ |
| INTT038 | zero_recall | — | 0.00 | 0.10 | 0.82 | — | 0.00 | ❌ |
| INTT039 | zero_recall | — | 0.00 | 0.80 | 0.82 | — | 0.00 | ❌ |
| INTT040 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT041 | zero_recall | — | 0.00 | 0.20 | 0.90 | — | 0.00 | ❌ |
| INTT042 | zero_recall | — | 0.00 | 0.50 | 0.95 | — | 0.00 | ❌ |
| INTT044 | zero_recall | — | 0.00 | 0.20 | 0.90 | — | 0.00 | ❌ |
| INTT045 | zero_recall | — | 0.00 | 0.10 | 0.70 | — | 0.00 | ❌ |
| INTT046 | zero_recall | — | 0.00 | 0.10 | 0.72 | — | 0.00 | ❌ |
| INTT047 | zero_recall | — | 0.00 | 0.10 | 0.70 | — | 0.00 | ❌ |
| INTT048 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT049 | zero_recall | — | 0.00 | 0.10 | 0.60 | — | 0.00 | ❌ |
| INTT050 | zero_recall | — | 0.00 | 1.00 | 0.00 | — | 0.00 | ❌ |
| INTT051 | zero_recall | — | 0.00 | 0.50 | 0.60 | — | 0.00 | ❌ |
| INTT052 | zero_recall | — | 0.00 | 0.70 | 0.85 | — | 0.00 | ❌ |
| INTT054 | zero_recall | — | 0.25 | 0.00 | 0.82 | — | 0.00 | ❌ |
| INTT055 | zero_recall | — | 0.00 | 0.10 | 0.82 | — | 0.00 | ❌ |
| INTT058 | zero_recall | — | 0.00 | 0.00 | 0.82 | — | 0.00 | ❌ |
| INTT060 | zero_recall | — | 0.00 | 0.00 | 0.60 | — | 0.00 | ❌ |
| INTT061 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT062 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT063 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT064 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT065 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT067 | zero_recall | — | 0.17 | 0.00 | 0.70 | — | 0.00 | ❌ |
| INTT068 | zero_recall | — | 0.00 | 1.00 | 0.82 | — | 0.00 | ❌ |
| INTT071 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT074 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT076 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT077 | zero_recall | — | 0.00 | 1.00 | 0.72 | — | 0.00 | ❌ |
| INTT079 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT080 | zero_recall | — | 0.00 | 0.50 | 0.70 | — | 0.00 | ❌ |
| INTT082 | zero_recall | — | 0.00 | 0.00 | 0.82 | — | 0.00 | ❌ |
| INTT085 | zero_recall | — | 0.00 | 0.20 | 0.85 | — | 0.00 | ❌ |
| INTT086 | zero_recall | — | 0.10 | 0.10 | 0.82 | — | 0.00 | ❌ |
| INTT087 | zero_recall | — | 0.00 | 0.90 | 0.85 | — | 0.00 | ❌ |
| INTT088 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT090 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT091 | zero_recall | — | 0.00 | 0.80 | 0.85 | — | 0.00 | ❌ |
| INTT092 | zero_recall | — | 0.00 | 0.50 | 0.90 | — | 0.00 | ❌ |
| INTT096 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| INTT097 | zero_recall | — | 0.00 | 0.80 | 0.85 | — | 0.00 | ❌ |
| INTT098 | zero_recall | — | 0.00 | 0.10 | 0.82 | — | 0.00 | ❌ |
| INTT100 | zero_recall | — | 0.00 | 0.10 | 0.82 | — | 0.00 | ❌ |
| INTT101 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT102 | zero_recall | — | 0.08 | 0.50 | 0.72 | — | 0.00 | ❌ |
| INTT103 | zero_recall | — | 0.00 | 0.50 | 0.60 | — | 0.00 | ❌ |
| INTT106 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT109 | zero_recall | — | 0.12 | 0.00 | 0.90 | — | 0.00 | ❌ |
| INTT110 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| INTT113 | zero_recall | — | 0.17 | 0.20 | 0.82 | — | 0.00 | ❌ |
| INTT115 | zero_recall | — | 0.15 | 0.50 | 0.95 | — | 0.00 | ❌ |
| INTT116 | zero_recall | — | 0.25 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT117 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT118 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT119 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT124 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT127 | zero_recall | — | 0.00 | 0.00 | 0.40 | — | 0.00 | ❌ |
| INTT128 | zero_recall | — | 0.00 | 0.10 | 0.82 | — | 0.00 | ❌ |
| INTT130 | zero_recall | — | 0.00 | 0.80 | 0.82 | — | 0.00 | ❌ |
| INTT131 | zero_recall | — | 0.00 | 1.00 | 0.95 | — | 0.00 | ❌ |
| INTT134 | zero_recall | — | 0.00 | 0.50 | 0.90 | — | 0.00 | ❌ |
| INTT136 | zero_recall | — | 0.22 | 1.00 | 0.70 | — | 0.00 | ❌ |
| INTT138 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT139 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT141 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT143 | zero_recall | — | 0.13 | 0.20 | 0.82 | — | 0.00 | ❌ |
| INTT144 | zero_recall | — | 0.00 | 1.00 | 0.85 | — | 0.00 | ❌ |
| INTT145 | zero_recall | — | 0.00 | 0.00 | 0.90 | — | 0.00 | ❌ |
| INTT147 | zero_recall | — | 0.00 | 0.10 | 0.82 | — | 0.00 | ❌ |
| INTT152 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT153 | zero_recall | — | 0.00 | 0.50 | 0.60 | — | 0.00 | ❌ |
| INTT155 | zero_recall | — | 0.00 | 0.50 | 0.92 | — | 0.00 | ❌ |
| INTT156 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT157 | zero_recall | — | 0.22 | 1.00 | 0.90 | — | 0.00 | ❌ |
| INTT158 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT159 | zero_recall | — | 0.11 | 0.00 | 0.70 | — | 0.00 | ❌ |
| INTT163 | zero_recall | — | 0.00 | 0.00 | 0.85 | — | 0.00 | ❌ |
| INTT169 | zero_recall | — | 0.00 | 0.50 | 0.82 | — | 0.00 | ❌ |
| INTT173 | zero_recall | — | 0.00 | 0.00 | 0.82 | — | 0.00 | ❌ |
| INTT176 | zero_recall | — | 0.00 | 0.50 | 0.85 | — | 0.00 | ❌ |
| INTT178 | zero_recall | — | 0.00 | 0.50 | 0.70 | — | 0.00 | ❌ |
| INTT179 | zero_recall | — | 0.00 | 0.00 | 0.95 | — | 0.00 | ❌ |
