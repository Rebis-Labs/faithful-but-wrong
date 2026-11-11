from fbw.citations import extract_articles, normalize_article, parse_citations
from fbw.judge import MockJudge, parse_json, parse_score
from fbw.metrics import Thresholds, citation_accuracy, passed
from fbw.refusal import RefusalDetector, refusal_outcome
from fbw.report import bootstrap_ci, render_markdown
from fbw.run import evaluate
from fbw.schema import GoldItem, RetrievedChunk, SystemOutput
from fbw.stratify import Bucket, classify, gold_articles, retrieved_articles
from fbw.verify import simple_lookup_from_dict, verify_answer


def test_normalize_article():
    assert normalize_article("Art. 29 bis") == "29-bis"
    assert normalize_article("29-bis") == "29-bis"
    assert normalize_article("29bis") == "29-bis"
    assert normalize_article("18, comma 1 e 2") == "18"
    assert normalize_article("2103") == "2103"


def test_parse_citations_forms():
    c = parse_citations("x [Source: Codice Civile, art. 2103] y [Source: art. 575 c.p.] z [Source: Circolari AdE, circolare n. 23]")
    assert (c[0].source, c[0].article) == ("Codice Civile", "2103")
    assert c[1].article == "575" and "c.p." in c[1].source
    assert c[2].article == "circolare-23"


def test_extract_gold_articles_regex():
    assert extract_articles("ai sensi dell'art. 2103 c.c. e dell'articolo 18 bis") == {"2103", "18-bis"}


def test_classify_buckets():
    assert classify(set(), {"1"}) == Bucket.NO_GOLD
    assert classify({"1", "2"}, {"1", "2", "3"}) == Bucket.FULL
    assert classify({"1", "2"}, {"1"}) == Bucket.PARTIAL
    assert classify({"1"}, {"2"}) == Bucket.ZERO


def test_gold_articles_explicit_wins():
    g = GoldItem(question_id="q", question="?", expected_answer="art. 99", gold_articles=["Art. 2103"])
    assert gold_articles(g) == {"2103"}


def test_retrieved_articles_metadata_then_text():
    chunks = [RetrievedChunk(text="…", source="s", article="2103"), RetrievedChunk(text="vedi art. 18 bis", source="s")]
    assert retrieved_articles(chunks) == {"2103", "18-bis"}
    assert retrieved_articles(chunks, fallback_to_text=False) == {"2103"}


def test_refusal_detector():
    d = RefusalDetector()
    assert d("Non ho trovato informazioni sufficienti nei documenti.")
    assert d("La documentazione disponibile non copre il caso.")
    # paraphrase after the first 250 chars = trailing caveat, not a refusal
    assert not d("Il periodo di prova per gli operatori è di due mesi, prorogabile una sola volta. " * 4 + "La documentazione disponibile non copre altri casi.")
    assert d("anything", explicit=True)
    assert not d("Non ho trovato informazioni sufficienti", explicit=False)
    assert refusal_outcome(True, True) == (True, "TP")
    assert refusal_outcome(True, False) == (False, "FP")


def test_citation_accuracy_tagged_and_inline():
    chunks = [RetrievedChunk(text="Art. 2103. Il lavoratore…", source="Codice Civile", article="2103")]
    assert citation_accuracy("… [Source: Codice Civile, art. 2103]", chunks) == 1.0
    assert citation_accuracy("… [Source: Codice Civile, art. 2104]", chunks) == 0.0
    assert citation_accuracy("ai sensi dell'art. 2103 c.c.", chunks) == 1.0
    assert citation_accuracy("nessun riferimento", chunks) == 0.0


def test_passed_gate():
    t = Thresholds()
    assert passed(should_refuse=False, refusal_correct=True, faith=0.95, ans_rel=0.9, ctx_rel=0.85, cit_acc=1.0, corr=None, t=t)
    assert not passed(should_refuse=False, refusal_correct=True, faith=0.5, ans_rel=0.9, ctx_rel=0.85, cit_acc=1.0, corr=None, t=t)
    assert passed(should_refuse=True, refusal_correct=True, faith=None, ans_rel=None, ctx_rel=None, cit_acc=None, corr=None, t=t)
    tc = Thresholds(correctness=0.5)
    assert not passed(should_refuse=False, refusal_correct=True, faith=0.95, ans_rel=0.9, ctx_rel=0.85, cit_acc=1.0, corr=0.0, t=tc)


def test_parse_json_fences():
    assert parse_json('```json\n{"score": 0.5}\n```') == {"score": 0.5}
    assert parse_score('prose {"score": 2.0}') == 1.0
    assert parse_score("garbage") == 0.0


def test_bootstrap_ci_basic():
    m, lo, hi = bootstrap_ci([1, 0, 1, 1, 0, 1, 1, 1], n_boot=500)
    assert abs(m - 0.75) < 1e-9 and lo <= m <= hi
    assert bootstrap_ci([]) == (None, None, None)


def test_evaluate_end_to_end_mock():
    gold = [
        GoldItem(question_id="q1", question="Durata periodo di prova operatori?", expected_answer="Il periodo di prova è di due mesi (art. 20 CCNL).", gold_articles=["20"]),
        GoldItem(question_id="q2", question="Domanda impossibile", expected_answer="", should_refuse=True),
    ]
    outs = [
        SystemOutput(question_id="q1", answer="Il periodo di prova per gli operatori è di due mesi. [Source: CCNL Funzioni Locali, art. 20]",
                     retrieved=[RetrievedChunk(text="Art. 20 Periodo di prova. Il periodo di prova per gli operatori è di due mesi.", source="CCNL Funzioni Locali", article="20")]),
        SystemOutput(question_id="q2", answer="Non ho trovato informazioni sufficienti."),
    ]
    recs = evaluate(gold, outs, MockJudge())
    assert [r.bucket for r in recs] == ["full_recall", "no_gold_articles"]
    assert recs[0].citation_accuracy == 1.0 and recs[0].correctness is not None
    assert recs[1].refusal_type == "TP" and recs[1].passed
    md = render_markdown(recs, n_boot=100)
    assert "full_recall" in md and "refusal-driven" in md


def test_citations_for_explicit_and_custom_parser():
    from fbw.citations import citations_for, load_parser
    from fbw.schema import CitationRef

    chunks = [RetrievedChunk(text="Art. 2103. Il lavoratore…", source="Codice Civile", article="2103")]
    # explicit citations on the record win over the (absent) tags in the text
    explicit = [CitationRef(source="Codice Civile", article="Art. 2103")]
    cits = citations_for("risposta senza tag", explicit)
    assert [(c.source, c.article) for c in cits] == [("Codice Civile", "2103")]
    assert citation_accuracy("risposta senza tag", chunks, cits) == 1.0
    # a user parser for another citation style
    parse = load_parser("examples.paren_parser:parse")
    cits = citations_for("come previsto (Codice Civile, art. 2103) e (TUIR, art. 51)", parser=parse)
    assert [(c.source, c.article) for c in cits] == [("Codice Civile", "2103"), ("TUIR", "51")]
    assert citation_accuracy("…", chunks, cits) == 0.5
    # no explicit, no parser → built-in tags
    assert citations_for("[Source: TUIR, art. 51]")[0].article == "51"


def test_verify_many_accepts_resolved_citations():
    from fbw.citations import Citation
    from fbw.verify import verify_many

    lookup, known = simple_lookup_from_dict({("codice civile", "2103"): "Art. 2103. Il lavoratore deve essere adibito alle mansioni…"})
    rows = [("q1", "sys", "Il lavoratore deve essere adibito alle mansioni", [Citation("Codice Civile", "2103", "(c.c. 2103)")])]
    per = verify_many(MockJudge(threshold=0.0), lookup, rows, known)
    assert per["sys"].cited == 1 and per["sys"].supported == 1
    assert per["sys"].verdicts[0].raw == "(c.c. 2103)"


def test_verify_against_lookup():
    lookup, known = simple_lookup_from_dict({("codice civile", "2103"): "Art. 2103. Il lavoratore deve essere adibito alle mansioni…"})
    st = verify_answer(MockJudge(threshold=0.0), lookup, "q", "sys",
                       "Il lavoratore deve essere adibito alle mansioni [Source: Codice Civile, art. 2103] e [Source: Codice Civile, art. 9999] e [Source: TUIR, art. 1]", known)
    assert (st.cited, st.supported, st.not_found, st.unverifiable) == (3, 1, 1, 1)
    assert st.checkable == 2 and st.precision_checkable == 0.5


def test_parse_composite_and_prassi():
    c = parse_citations("[Source: art. 9, Tariffa, parte I, DPR 131/1986; Agenzia delle Entrate, risposta n. 3/E del 13 gennaio 2026]")
    assert [(x.source, x.article) for x in c] == [("Tariffa, parte I, DPR 131/1986", "9"), ("Agenzia delle Entrate", "risposta-3/e/2026")]
    c = parse_citations("[Source: Art. 10, comma 1, lett. e), TUIR]")
    assert (c[0].source, c[0].article) == ("TUIR", "10")
    c = parse_citations("[Source: TUIR, artt. 49 e 51]")
    assert (c[0].source, c[0].article) == ("TUIR", "49,51")
    c = parse_citations("[Source: Agenzia delle Entrate, Risoluzione n. 89/E del 2002]")
    assert c[0].article == "risoluzione-89/e/2002"


def test_prassi_year_is_part_of_the_id():
    # practice numbering restarts every year: 1/2019 and 1/2024 are different documents
    a = parse_citations("[Source: Ministero del Lavoro, interpello n. 1/2019]")[0]
    b = parse_citations("[Source: Ministero del Lavoro, interpello n. 1 del 2024]")[0]
    c = parse_citations("[Source: INPS, circolare n. 23 del 19/11/2024]")[0]
    d = parse_citations("[Source: Agenzia delle Entrate, circolare n. 23/E]")[0]
    assert (a.article, b.article, c.article, d.article) == ("interpello-1/2019", "interpello-1/2024", "circolare-23/2024", "circolare-23/e")
    assert a.article != b.article
