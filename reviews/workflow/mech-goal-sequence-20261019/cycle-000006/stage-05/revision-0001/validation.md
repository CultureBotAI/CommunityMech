# Cycle 6 Stage 5 Remediation Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `6` (`cycle-000006`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`

## 1. Executed Validation Gates

| Validation Gate | Command | Exit Code | Result Summary |
|---|---|---|---|
| Strict Corpus & Schema Validation | `PYTHONPATH=src ./.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | All 3 remediated `kb/communities/` YAML records validate cleanly against `src/communitymech/schema/communitymech.yaml` with `0` errors, `0` GTDB coherence errors, `0` scalar errors, and `0` ontology term label errors. |
| Writer Bypass & History Sidecar Validation | `./.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-11-04T202200Z-antigravity-2113a1.yaml history/records/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium/2026-11-04T202200Z-antigravity-2113a2.yaml history/records/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium/2026-11-04T202200Z-antigravity-2113a4.yaml` | `0` | All 3 modified community YAML records were written through `record_curation_event(..., llm_assisted=True)` + `write_validated_community` and carry schema-valid `HistoryRecord` sidecars (`No issues found`). |
| Causal Review Inventory, Batch Regression & Structured Review Suite | `./.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_causal_review_inventory.py tests/test_causal_review_batch6.py tests/test_causal_review_batch100.py tests/test_causal_review_batch123.py tests/test_participating_taxa.py -v` | `0` | All 69 tests pass across causal review inventory integrity (`498` records, `444` reviewed, `54` `needs_research`, `0` stale, `0` structural defects), batch 6/100/123 regression suites, and participating-taxa checks. |
| HTML Community Site & Browser Data Currency Gate | `PYTHONPATH=src ./.venv/bin/python -m communitymech.render && PYTHONPATH=src ./.venv/bin/python -m communitymech.export.browser_export` | `0` | Updated `docs/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.html`, `docs/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.html`, and `docs/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.html`; verified `docs/data.js` is current (`489` communities rendered cleanly). |
| Lint & Static Typing Gate | `./.venv/bin/black --check src/ tests/ scripts/ && ./.venv/bin/ruff check --cache-dir /tmp/ruff_cache src/ tests/ scripts/ && ./.venv/bin/mypy --cache-dir /tmp/mypy_cache src/` | `0` | All formatting, lint, and static typing checks pass with `0` issues. |
| Workflow Evidence Contract Validation | `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-04/revision-0001/evidence.yaml --required-output issue_map --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000006/stage-05/revision-0001/evidence.yaml` | `0` | Validated `FindingGroupResolution` schema and ancestor evidence graph (`stage: 5`, `10` findings, `8` groups, `7` `carry_forward_ids`). |

## 2. Remediated Record Metrics

- **`CommunityMech:000401` (`kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml`, `#2113`)**:
  - Added `abundance_level: DOMINANT` and verbatim abundance-shift evidence (`PMID:42655156`, `PMC13515949`, `doi:10.3390/microorganisms14081812`) on `Bifidobacterium bifidum JCM1254` (`NCBITaxon:1681`, `taxonomy[0]`) and `Faecalibacterium prausnitzii A2-165` (`NCBITaxon:853`, `taxonomy[1]`).
  - Proportional `review-communities` Completeness Score: `100/100` (`s_ab` rubric component `0/5` -> `5/5`); `scripts/audit_completeness.py` score: `75/100`.
- **`CommunityMech:000402` (`kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml`, `#2113`)**:
  - Added `functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER]` and `abundance_level: ABUNDANT` on `Delta nrfA Shewanella oneidensis MR-1` (`NCBITaxon:211586`, `taxonomy[0]`), and `functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]` and `abundance_level: DOMINANT` on `Candidatus Brocadia anammox bacteria` (`NCBITaxon:203682`, `taxonomy[1]`) (`PMID:42655905`, `PMC13519132`, `doi:10.1002/wer.70526`).
  - Proportional `review-communities` Completeness Score: `90/100` -> `95/100`; `scripts/audit_completeness.py` score: `25/100` (`taxonomy[2]` `NCBITaxon:2` preserved without an unverified `functional_role` per `shewanella_anammox_sludge_membership_and_flux_unresolved`).
- **`CommunityMech:000404` (`kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml`, `#2113`)**:
  - Added `functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER]` and `abundance_level: ABUNDANT` on `Ramichloridium apiculatum CMS-1` (`NCBITaxon:470080`, `taxonomy[0]`), and `functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER, SYNTROPHIC_PARTNER]` and `abundance_level: DOMINANT` on `Talaromyces pseudofuniculosus hzt-3'` (`NCBITaxon:2015341`, `taxonomy[1]`) (`PMID:42478817`, `PMC13488302`, `doi:10.1128/aem.02519-25`).
  - Proportional `review-communities` Completeness Score: `90/100` -> `98/100`; `scripts/audit_completeness.py` score: `40/100` -> `90/100`.
