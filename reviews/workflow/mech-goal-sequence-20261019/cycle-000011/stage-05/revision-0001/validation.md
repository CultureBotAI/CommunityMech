# Cycle 11 Stage 5 Remediation Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `11` (`cycle-000011`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`

## 1. Executed Validation Gates

| Validation Gate | Command | Exit Code | Result Summary |
|---|---|---|---|
| Strict Corpus & Schema Validation | `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py --out .temp/instance_validation_failures.tsv kb/communities/Syntrophobacter_Methanospirillum_Syntrophy.yaml kb/communities/Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture.yaml kb/communities/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm.yaml` | `0` | All 3 remediated `kb/communities/` YAML records validate cleanly against `src/communitymech/schema/communitymech.yaml` with `0` errors, `0` GTDB coherence errors, `0` scalar errors, and `0` ontology term label errors. |
| Reference & Snippet Verification | `.venv/bin/linkml-reference-validator validate data kb/communities/Syntrophobacter_Methanospirillum_Syntrophy.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` (and `000181`, `000213`) | `0` | All 3 modified community YAML records pass `linkml-reference-validator` with `0` snippet mismatches against `references_cache/`. |
| Bracketed Snippet Guard | `.venv/bin/pytest tests/test_no_new_bracketed_snippets.py -v` | `0` | `4 passed` (`0` new bracketed snippets introduced). |
| Writer Bypass & History Sidecar Validation | `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Syntrophobacter_Methanospirillum_Syntrophy/2026-11-08T150000Z-antigravity-2732a1.yaml history/records/Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture/2026-11-08T150000Z-antigravity-2732a2.yaml history/records/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm/2026-11-08T150000Z-antigravity-2732a3.yaml` | `0` | All 3 modified community YAML records were written through `record_curation_event(..., llm_assisted=True)` + `write_validated_community` and carry schema-valid `HistoryRecord` sidecars (`No issues found`). |
| Causal Review Inventory, Batch Successor Ledgers, GTDB Demoted Clades & Participating Taxa Suite | `.venv/bin/pytest tests/test_causal_review_inventory.py tests/test_causal_review_batch112.py tests/test_causal_review_batch90.py tests/test_causal_review_batch117.py tests/test_gtdb_demoted_clades.py tests/test_participating_taxa.py -v` | `0` | All `32` causal review inventory integrity checks (`524` records, `470` reviewed, `54` `needs_research`, `0` stale, `0` structural defects) and all `34` batch `112`/`90`/`117` successor-ledger checks pass alongside GTDB demoted clades and participating-taxa checks. |
| HTML Community Site & Browser Data Currency Gate | `.venv/bin/pytest tests/test_docs_do_not_contradict_the_kb.py tests/test_published_pages_name_real_records.py -v` | `0` | Updated `docs/communities/Syntrophobacter_Methanospirillum_Syntrophy.html`, `docs/communities/Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture.html`, and `docs/communities/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm.html`; `1032` passed in `test_docs_do_not_contradict_the_kb.py` and `test_published_pages_name_real_records.py` (`510` communities rendered cleanly). |
| Lint & Static Typing Gate | `.venv/bin/black --check src/ tests/ scripts/ && .venv/bin/ruff check src/ tests/ scripts/ && .venv/bin/mypy src/` | `0` | All formatting, lint, and static typing checks pass with `0` issues. |
| Workflow Evidence Contract Validation | `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/evidence.yaml --required-output issue_map --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-05/revision-0001/evidence.yaml` | `0` | Validated `FindingGroupResolution` schema and ancestor evidence graph (`stage: 5`, `10` findings, `8` groups, `7` `carry_forward_ids`). |

## 2. Remediated Record Metrics

- **`CommunityMech:000069` (`kb/communities/Syntrophobacter_Methanospirillum_Syntrophy.yaml`, `#2732`)**:
  - Added `abundance_level: DOMINANT` and verbatim two-member syntrophic co-culture evidence (`PMID:9828440`, `doi:10.1099/00207713-48-4-1383`) on `Syntrophobacter fumaroxidans` (`NCBITaxon:119484`, `taxonomy[0]`) and `Methanospirillum hungatei` (`NCBITaxon:2203`, `taxonomy[1]`).
  - `review-communities` `s_ab` rubric component: `0/5` -> `5/5` (`0/2` -> `2/2` taxa with `abundance_level`); proportional Completeness Score: `100/100`; `scripts/audit_completeness.py` score: `90/100`.
- **`CommunityMech:000181` (`kb/communities/Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture.yaml`, `#2732`)**:
  - Added `abundance_level: DOMINANT` and verbatim two-strain chloronitrobenzene-degrading coculture evidence (`PMID:10049867`, `doi:10.1128/AEM.65.3.1083-1091.1999`) on `Pseudomonas putida` (`NCBITaxon:303`, `taxonomy[0]`) and `Rhodococcus` (`NCBITaxon:1827`, `taxonomy[1]`).
  - `review-communities` `s_ab` rubric component: `0/5` -> `5/5` (`0/2` -> `2/2` taxa with `abundance_level`); proportional Completeness Score: `97/100`; `scripts/audit_completeness.py` score: `95/100`.
- **`CommunityMech:000213` (`kb/communities/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm.yaml`, `#2732`)**:
  - Added `abundance_level: DOMINANT` and verbatim two-member vitamin cross-feeding mutualism evidence (`PMID:37553333`, `doi:10.1038/s41467-023-40360-4`) on `Variovorax` (`NCBITaxon:34072`, `taxonomy[0]`) and `Cryptococcus` (`NCBITaxon:5206`, `taxonomy[1]`).
  - `review-communities` `s_ab` rubric component: `0/5` -> `5/5` (`0/2` -> `2/2` taxa with `abundance_level`); proportional Completeness Score: `100/100`; `scripts/audit_completeness.py` score: `85/100`.
