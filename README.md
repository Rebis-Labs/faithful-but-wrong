# faithful-but-wrong — recall-based evaluation for retrieval-augmented legal QA

> Package `fbw-eval`, command `fbw`. Companion code for *Faithful yet Wrong: Recall-Based Evaluation of
> Legal RAG on Italian Law* (A. Esposito Brescia, preprint, arXiv November 2026 [id to be added at
> announcement]). `paper/` holds the per-item records of every table in the paper and the script that
> regenerates them without API access.

## The failure mode this measures

A retrieval-augmented system can be **faithful but wrong**: every sentence it writes is supported
by the passages it was given, and the passages were the wrong ones. Standard RAG metrics do not
see it. Faithfulness is computed against the retrieved context, so it saturates; aggregate pass
rates are dominated by the questions the retriever had already solved.

In the paper's labour benchmark (78 questions, one frozen configuration, judge Claude Sonnet 4.6), the
questions where the retriever returned **all** of the gold articles score 94.6 faithfulness and 83.0
correctness; the questions where it returned **none** of them score 67.5 faithfulness and 33.0
correctness. The aggregate hides the second group.

The protocol is simple: classify every question by **retrieval recall of the gold articles**
(full / partial / zero), then report **faithfulness and correctness separately per bucket**.
Correctness is judged against the gold reference, not the context, so it is the axis faithfulness
cannot see.

The harness also **verifies citations against a corpus**: a judge reading the answer alone rewards
a plausible "art. 2110 c.c." cited from memory; here the cited article's actual text is fetched
from *your* corpus and a judge says whether it supports the claim. Citations to acts you do not
hold are reported as *unverifiable*, never as wrong.

## What it evaluates

Outputs, not systems. Any pipeline that can dump, per question, its answer and the contexts it
handed to the generator can be evaluated — a bi-encoder, a web search, a human. The harness never
calls your retriever or generator.

```
gold.jsonl       {question_id, question, expected_answer, gold_articles, should_refuse, domain}
outputs.jsonl    {question_id, answer, retrieved: [{text, source, article}], refused?, system}
```

`gold_articles` are the article identifiers a correct answer **must** cite ("2103", "29-bis").
If omitted they are extracted from `expected_answer` by regex (a documented, weaker option).
`retrieved[].article` is the article metadata of each chunk when your corpus is article-segmented;
otherwise article mentions in the chunk text are used.

**Composite tags and administrative practice.** A tag may cite several sources separated by `;`; each becomes its own citation. References to practice (`circolare n. 23/E`, `risposta n. 3/E del 13 gennaio 2026`, `risoluzione 89/E`) are parsed as `kind-number[/year]` identifiers (e.g. `("Agenzia delle Entrate", "risposta-3/e/2026")`; the year is kept because practice numbering restarts every year) so a lookup over a practice corpus can resolve them instead of counting them as missing articles. Article lists (`artt. 49 e 51`) are reported as range/list, not checked.

**Citations in another format.** The built-in parser reads `[Source: act, art. N]` tags, the
reference system's convention. Two ways out for other systems, in order of precedence:

1. put the citations on the output record — `"citations": [{"source": "Codice Civile", "article": "2103"}]` —
   and they are used as-is (for systems whose citations are metadata or footnotes, not text);
2. pass your own parser: `--citation-parser mypkg.cites:parse`, a function `answer text → [(source, article), …]`
   (see `examples/paren_parser.py`). The report records which parser was used.

**Gold you built yourself is not comparable to anyone else's numbers.** The harness measures;
it does not certify. A gold set written to match a system's output will score that system
perfectly. For comparability use a gold set whose ground truth is external (official answers,
published cases) and state its provenance — the report prints it.

## Run

```bash
pip install -e ".[judge,dev]"
python -m pytest -q

# recall buckets only — no judge, no key
python -m fbw buckets --gold examples/gold.jsonl --outputs examples/outputs.jsonl

# full report with an LLM judge (OpenAI-compatible endpoint; OpenRouter by default)
export JUDGE_API_KEY=...            # or OPENROUTER_API_KEY / OPENAI_API_KEY
python -m fbw run --gold examples/gold.jsonl --outputs examples/outputs.jsonl \
    --out reports/demo --judge-model openai/gpt-4o-mini

# verify every citation against your corpus (you supply the lookup)
python -m fbw verify --outputs examples/outputs.jsonl \
    --lookup examples.corpus_lookup:lookup --out reports/demo

# pipeline smoke test without a key (lexical mock judge — numbers are meaningless)
python -m fbw run --gold examples/gold.jsonl --outputs examples/outputs.jsonl --out /tmp/x --mock
```

Judges that reason before answering (Claude, Gemini) need `JUDGE_SYSTEM="Return only the JSON object
requested, no analysis before or after it."` and/or `JUDGE_MAX_TOKENS=1024`, otherwise the JSON is
truncated and the score falls back to 0. Both are part of the cache key.

Every judge call is cached on disk (`<out>/judge_cache.jsonl`): re-bucketing, re-reporting and
bootstrapping are free. Delete the cache to re-judge.

## What the report contains

- **Recall-based table**: per bucket, n, pass rate, faithfulness, correctness, citation
  accuracy, refusals — each with a seeded percentile-bootstrap 95% CI (questions resampled).
  Small buckets get wide intervals; that is the information.
- **End-task metrics** over all questions, with pass rate reported **with and without
  refusal-driven passes** (refusing well on hard questions raises the headline; the report says
  how much).
- **Coverage**: how many questions were stratifiable (gold without articles — principle questions,
  refusals — are kept for end-task metrics and excluded from the recall table).
- **Citation verification**: per system, cited / checkable / supported / unsupported /
  not found (act in corpus, article absent) / unverifiable (act not in corpus) / range-or-list.
  Two ratios: precision on checkable citations and the checkable share of all citations.

## Metrics (per question)

| metric | computed against | judge |
|---|---|---|
| faithfulness | the retrieved contexts | yes |
| correctness | the gold reference answer | yes |
| answer relevancy | the question | yes |
| context relevancy | the question, per chunk | yes |
| citation accuracy | the retrieved chunks (source + article match); parser replaceable | no |
| refusal accuracy | `should_refuse` | no (marker/paraphrase detector, overridable) |

`pass` = refusal correct **and** faithfulness ≥ .90, answer relevancy ≥ .85, context relevancy
≥ .80, citation accuracy ≥ .90 (the reference implementation's production gate). Add
`--correctness-gate 0.5` to make correctness a requirement as well. Thresholds are reported in
the output so they can be changed and compared.

## What to report with your numbers

The judge is a parameter of the protocol, not an implementation detail. Report: the judge model
(a judge from the generator's own model family is a known bias source), the gold set and how it was
annotated, the recall granularity (article), the coverage, and the CI method. The harness writes
all of these into `report.json`.

## Limitations

- Recall is measured at **article** granularity. Chunk-level would be too strict (long articles span
  chunks), document-level too loose (a code has hundreds of articles). It assumes the gold answer can
  be pinned to articles; questions of principle fall out of the recall table.
- Regex extraction of gold articles from free text misses multi-sentence references; give
  `gold_articles` explicitly where you can.
- Citation verification checks against **your** corpus: a missing act or corrupt metadata penalises a
  correct citation. Keep the unverifiable column visible.
- LLM judges carry position, verbosity and self-enhancement biases. Validate against human
  verdicts on a sample (the companion paper reports Cohen's kappa against two human annotators).

## Layout

```
fbw/
  schema.py     GoldItem / SystemOutput / EvalRecord, JSONL IO
  stratify.py   recall buckets
  metrics.py    judge prompts + citation accuracy + pass gate
  refusal.py    refusal detector (markers + paraphrases, overridable)
  citations.py  [Source: …] parsing, article normalisation
  verify.py     citation verification against a corpus via lookup(source, article)
  report.py     stratified tables, bootstrap CIs, markdown/json
  judge.py      OpenAI-compatible judge with disk cache; MockJudge for tests
  run.py        join + score
examples/       synthetic gold/outputs/corpus (invented texts — not a benchmark); paren_parser.py (custom citation parser)
tests/
```

## Paper package

`paper/reports/<set>/` — one folder per evaluation set of the paper (records, cached judge verdicts,
citation verdicts, system outputs; gold for the authority-answered sets). `python paper/make_tables.py`
rewrites every table of the paper from them. Which sets exist, what each contains and which gold is
withheld: `paper/README.md`.

## License

Apache License 2.0. The reference system this harness was extracted from is separate and not
included.
