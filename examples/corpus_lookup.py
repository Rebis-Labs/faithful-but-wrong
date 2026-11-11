"""Example `lookup` factory for `python -m fbw verify --lookup examples.corpus_lookup:lookup`.

Replace with your own corpus access (SQL, vector store metadata, files…).
Contract: lookup(source_as_cited, normalised_article) -> article text or None;
optionally also return known_source(source) -> bool so that "act in corpus but
article absent" (likely invented) is told apart from "act not in corpus".
"""

from fbw.verify import simple_lookup_from_dict

_ARTICLES = {
    ("ccnl esempio", "19"): "Art. 19 Assunzione. L'assunzione avviene con contratto scritto.",
    ("ccnl esempio", "20"): "Art. 20 Periodo di prova. Il periodo di prova per gli operatori è di due mesi; per i funzionari di quattro mesi.",
    ("ccnl esempio", "21"): "Art. 21 Orario di lavoro. L'orario ordinario di lavoro è di 36 ore settimanali, articolato su cinque giorni.",
    ("ccnl esempio", "22"): "Art. 22 Durata massima. La durata media dell'orario non può superare le 48 ore settimanali, straordinario incluso, su sei mesi.",
    ("ccnl esempio", "41"): "Art. 41 Preavviso. Il preavviso di dimissioni è di 60 giorni per i quadri e di 30 giorni per gli operatori.",
    ("codice esempio", "1375"): "Art. 1375 Esecuzione di buona fede. Il contratto deve essere eseguito secondo buona fede.",
}


def lookup():
    return simple_lookup_from_dict(_ARTICLES)
