# Paper package — "Faithful yet Wrong" (v2)

Per-item records of every evaluation set reported in the paper, under one frozen configuration of
the system under test (tag `paper-v2-config-2026-10-17`) and one judge (`anthropic/claude-sonnet-4.6`).
Every table in the paper regenerates from these files without API access:

```bash
python paper/make_tables.py        # -> paper/tables/{numbers.json, tab_main.tex, tab_fc.tex, tab_practice.tex, tab_verify.tex, tab_judge.tex}
```

## Sets

| folder | tier | n | what |
|---|---|---|---|
| `v2_labor_v3` | C | 78 | v1 labour benchmark (re-baselined) |
| `v2_criminal` | C | 30 | v1 criminal benchmark |
| `v2_admin` | C | 38 | v1 administrative/tax benchmark |
| `v2_interpelli_lavoro_prassi` / `_noprassi` | A | 23 | Ministry of Labour interpelli 2019–2024, practice indexed / removed |
| `v2_trib2026_prassi` / `_noprassi` | A | 111 | Revenue Agency interpelli 2026, practice indexed / removed |
| `v2_expert` | B | 5 | expert-authored questions, non-circular subset |
| `v2_labor_v3_anchor59` / `v2_criminal_anchor59` / `v2_admin_anchor59` | C | 78/30/38 | the same records re-bucketed after the gold articles of 59 items were anchored to the source text (28–29 Oct); judge verdicts identical, only `bucket` changes. `make_tables.py` takes the bucket figures from here. `v2_labor_v3_anchor59/citation_verdicts.jsonl` is the labour verification re-run with the corrected act lookup (exact display-name match first, 29 Oct): three citations to "CCNL Funzioni Centrali, art. 38" go from supported to unsupported (the chunk labelled art. 38 held most of the agreement, an ingestion defect); `make_tables.py` uses it in place of `v2_labor_v3/citation_verdicts.jsonl`. A second lookup correction (2 Nov: candidate acts ranked across all collections, so a code is not resolved against a homonymous code of another branch) changed 13 of 4,585 resolutions and five frontier verdicts (`v2_frontier_admin/chatgpt`, `v2_frontier_labor_v3/{chatgpt,claude,perplexity}`); grounded rows unchanged |
| `v2_vanilla_{labor_v3,criminal,admin,interpelli_lavoro}` | C / A | 78/30/38/23 | the v1 vanilla baseline (cosine top-3 over the statute and practice collection, minimal prompt, same gpt-4o-mini generator, no fusion, reranking, rewriting or refusal policy) run on the same tag, corpus, judge and anchored gold as the grounded rows (6 Nov 2026). Its prompt produces no `[Source:]` tags, so `citation_verdicts.jsonl` is empty by construction and it has no row in the verification table; refusals come from the harness marker detector, so every refusal-required item counts as FN. Tier C gold withheld |
| `v2_vanillaj_{labor_v3,criminal,admin,interpelli_lavoro}` | C / A | 78/30/38/23 | the same vanilla retriever with the case-law collection added (score merge). A sensitivity row: it does not change the vanilla result |
| `v2_{labor_v3,criminal,admin}_judge4omini`, `v2_vanilla_{labor_v3,criminal,admin,interpelli_lavoro}_judge4omini` | C / A | as above | **the same `outputs.jsonl`** judged by `openai/gpt-4o-mini` (the generator's family and the June judge) instead of Sonnet 4.6: same harness, prompts, thresholds, gold. `metis/` holds the literal June evaluator (`eval/metrics.py`, gpt-4o-mini: pass with thresholds, no correctness) on the same outputs. `make_tables.py` reads these for `tab_judge.tex` and prints the vanilla rows next to the grounded rows in `tab_main.tex` and `tab_fc.tex`; nothing else in the paper uses the gpt-4o-mini verdicts |
| `v2_frontier_trib2026/{chatgpt,claude,gemini,perplexity}` | A | 111 | GPT-5.1, Claude Sonnet 4.6, Gemini 2.5 Pro, Perplexity sonar-pro on the 2026 tax interpelli (answers collected 17 Oct 2026 via OpenRouter), judged and citation-verified with the same judge, gold and corpus as `v2_trib2026_prassi`. `retrieved` is empty for these, so faithfulness, context relevancy and the pass flag are not meaningful; read correctness, refusals and citation verdicts |
| `v2_frontier_labor_v3/…` / `v2_frontier_admin/…` | C | 78 / 38 | the same four assistants on the labour and administrative/tax v1 benchmark sets (answers collected 6–7 Oct 2026 via OpenRouter, re-judged 29 Oct with the same judge, anchored gold and corpus as the grounded sets). Statutes and collective agreements are plausibly in the models' training data: read these rows for the citation-verification pattern, not as a recency test. Gold withheld with the rest of Tier C |
| `v2_frontier_criminal/…` | C | 30 | the same four assistants on the criminal v1 set (answers collected 6 Oct 2026, re-judged 30 Oct with the same judge and the anchored gold; lookup after the exact-match correction). Gold withheld |

## Files per set

- `records.jsonl` — one line per question: bucket, gold articles, retrieved articles, judge scores
  (faithfulness, correctness, relevancies, citation accuracy), refusal type (TN/TP/FP/FN), pass flag.
  These are the cached judge verdicts the tables are built from.
- `citation_verdicts.jsonl` — one line per citation: resolved id, outcome
  (`supported` / `unsupported` / `not_found` / `unverifiable` / `range_or_list`), judge rationale.
- `report.json`, `report.md`, `citations.md` — the harness report for the set (bucket figures with CIs).
- `outputs.jsonl` — the system's answers (Tiers A and C).
- `gold.jsonl` — reference answers and gold articles. **Released now for Tier A only** (transcribed from
  official replies of the Ministry of Labour and the Revenue Agency). Tier B and Tier C gold, and the
  Tier B outputs, are withheld until acceptance, as stated in the paper's data-availability section.

The system under test is a production service and is not released; it appears in the records as
`grounded`. The frontier comparison (Section "What the judge rewards and what a professional can
verify") is in `v2_frontier_trib2026/`, `v2_frontier_labor_v3/`, `v2_frontier_admin/` and `v2_frontier_criminal/`: the frontier
answers (`outputs_<model>.jsonl`) are released in full, so the citation verdicts can be re-annotated by hand.
`tab_verify.tex` has one block per set, grounded system first.
