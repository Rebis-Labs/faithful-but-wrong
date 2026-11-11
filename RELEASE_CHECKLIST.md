# Release checklist (first public version)

Repository: `github.com/Rebis-Labs/faithful-but-wrong` (org exists; repository to be created by the owner).
Making the repository public is the owner's call; nothing below pushes anything.

## Before `git push`
- [x] `paper/reports/v2_expert/` (renamed 9 Nov from the expert's surname): `records.jsonl` has no question text and no
      expert verdicts (`correctness` null); `citation_verdicts.jsonl` reduced to ids, source, article, outcome (answer fragments
      removed); `report.json` meta paths replaced. Folder kept for the n=5 line. Tables unchanged after `make_tables.py`.
- [ ] Tier C folders (`v2_labor_v3`, `v2_criminal`, `v2_admin`, `*_anchor59`, `*_judge4omini`, `v2_vanilla*`,
      `v2_frontier_{labor_v3,admin,criminal}`): no `gold.jsonl` (checked 9 Nov: only Tier A folders have one).
      `records.jsonl` carries `gold_articles` ids only. OK as is.
- [ ] `grep -rn "sk-\|OPENROUTER_API_KEY=\|ANTHROPIC_API_KEY=" .` returns nothing (checked 9 Nov: clean).
- [ ] README: arXiv id inserted after announcement.
- [ ] `pyproject.toml` version `0.1.0`; `git tag v0.1.0`.
- [x] `python -m pytest -q` green (17 passed, 9 Nov); `python paper/make_tables.py` reproduces `paper/tables/` (float deltas 2e-16 only, 9 Nov).

## After push
- [ ] Repository public; URL in the paper switches to "is available" (`\harnesspublictrue` in
      `nllp_paper_v2.tex`), arXiv v2 or journal version.
- [ ] Add the paper's citation (BibTeX) to the README once the arXiv id exists.
