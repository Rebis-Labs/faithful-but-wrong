"""faithful-but-wrong (fbw-eval) — recall-conditional evaluation for retrieval-augmented legal QA.

Working name. The package evaluates the *outputs* of any RAG system (answers +
retrieved contexts) against a gold set, and reports faithfulness and
correctness separately per retrieval-recall bucket, so that "faithful but
wrong" answers — faithful to a context that did not contain the answer — are
visible instead of being averaged away.
"""

__version__ = "0.1.0.dev0"
