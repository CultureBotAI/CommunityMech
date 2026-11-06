# Cycle 7 Stage 5 Remediation Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `7` (`cycle-000007`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`

## 1. Executed Validation Gates

| Validation Gate | Command | Exit Code | Result Summary |
|---|---|---|---|
| Strict Corpus & Schema Validation | `PYTHONPATH=src ./.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | All 3 remediated `kb/communities/` YAML records validate cleanly against `src/communitymech/schema/communitymech.yaml` with `0` errors, `0` GTDB coherence errors, `0` scalar errors, and `0` ontology term label errors. |
| Reference & Snippet Verification | `./.venv/bin/linkml-reference-validator validate data kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity --cache-dir references_cache --no-Repair` (and `000190`, `000451`) | `0` | All 3 modified community YAML records pass `linkml-reference-validator` with `0` snippet mismatches against `references_cache/`. |
| Writer Bypass & History Sidecar Validation | `./.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Anammox_Granule_Metabolic_Interaction_Community/2026-11-05T165000Z-antigravity-2120a1.yaml history/records/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture/2026-11-05T165000Z-antigravity-2120a2.yaml history/records/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture/2026-11-05T165000Z-antigravity-2120a3.yaml` | `0` | All 3 modified community YAML records were written through `record_curation_event(..., llm_assisted=True)` + `write_validated_community` and carry schema-valid `HistoryRecord` sidecars (`No issues found`). |
| Causal Review Inventory, GTDB Demoted Clades & Participating Taxa Suite | `./.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_causal_review_inventory.py tests/test_gtdb_demoted_clades.py tests/test_participating_taxa.py -v` | `0` | All 54 passed (`9` skipped, `0` failed) across causal review inventory integrity (`503` records, `449` reviewed, `54` `needs_research`, `0` stale, `0` structural defects), GTDB demoted clades, and participating-taxa checks. |
| HTML Community Site & Browser Data Currency Gate | `./.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_docs_do_not_contradict_the_kb.py tests/test_published_pages_name_real_records.py -v` | `0` | Updated `docs/communities/Anammox_Granule_Metabolic_Interaction_Community.html`, `docs/communities/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.html`, and `docs/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.html`; `1000` passed in `test_docs_do_not_contradict_the_kb.py` and `test_published_pages_name_real_records.py` (`494` communities rendered cleanly). |
| Lint & Static Typing Gate | `./.venv/bin/black --check src/ tests/ scripts/ && ./.venv/bin/ruff check --cache-dir /tmp/ruff_cache src/ tests/ scripts/ && ./.venv/bin/mypy --cache-dir /tmp/mypy_cache src/` | `0` | All formatting, lint, and static typing checks pass with `0` issues. |
| Workflow Evidence Contract Validation | `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-04/revision-0001/evidence.yaml --required-output issue_map --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-05/revision-0001/evidence.yaml` | `0` | Validated `FindingGroupResolution` schema and ancestor evidence graph (`stage: 5`, `10` findings, `8` groups, `7` `carry_forward_ids`). |

## 2. Remediated Record Metrics

- **`CommunityMech:000146` (`kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml`, `#2120`)**:
  - Added `abundance_level: DOMINANT` on `Brocadia-affiliated anammox bacterium AMX1` (`NCBITaxon:795830`, `taxonomy[0]`), `abundance_level: ABUNDANT` on `Chlorobi-affiliated heterotrophic bacteria` (`NCBITaxon:1090`, `taxonomy[1]`), and `abundance_level: COMMON` on `anammox-granule heterotrophic flanking bacteria` (`NCBITaxon:2`, `taxonomy[2]`) (`doi:10.1038/ncomms15416`, `PMID:28561030`, `PMC5460018`).
  - Proportional `review-communities` Completeness Score: `95/100` -> `100/100` (`s_ab` rubric component `0/5` -> `5/5`); `scripts/audit_completeness.py` score: `95/100`.
- **`CommunityMech:000190` (`kb/communities/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.yaml`, `#2120`)**:
  - Added `abundance_level: DOMINANT` and verbatim RNA-Seq read-mapping evidence (`PMID:30038609`, `PMC6046458`, `doi:10.3389/fmicb.2018.01551`) on `Pelotomaculum thermopropionicum` (`NCBITaxon:110500`, `taxonomy[0]`) and `Methanocella conradii` (`NCBITaxon:1175444`, `taxonomy[1]`).
  - Proportional `review-communities` Completeness Score: `97/100` -> `100/100` (`s_ab` rubric component `0/5` -> `5/5`); `scripts/audit_completeness.py` score: `100/100`.
- **`CommunityMech:000451` (`kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml`, `#2120`)**:
  - Added `abundance_level: DOMINANT` and verbatim defined-coculture selection evidence (`PMID:41724996`, `PMC13037320`, `doi:10.1186/s40168-026-02335-7`) on `Pseudomonas sp. Pseudomonas_sp1` (`NCBITaxon:306`, `taxonomy[1]`).
  - Proportional `review-communities` Completeness Score: `90/100` -> `92.5/100` (`s_ab` rubric component `2.5/5` -> `5/5`); `scripts/audit_completeness.py` score: `65/100`.
