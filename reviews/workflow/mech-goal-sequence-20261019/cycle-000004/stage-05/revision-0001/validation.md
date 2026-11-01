# Cycle 4 Stage 5 Remediation Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `4` (`cycle-000004`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`

## 1. Executed Validation Gates

| Validation Gate | Command | Exit Code | Result Summary |
|---|---|---|---|
| Strict Corpus & Schema Validation | `PYTHONPATH=src ./.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | All 3 remediated `kb/communities/` YAML records validate cleanly against `src/communitymech/schema/communitymech.yaml` with `0` errors, `0` GTDB coherence errors, `0` scalar errors, and `0` ontology term label errors. |
| Writer Bypass & History Sidecar Validation | `./.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/SMutans_CAlbicans_ECC_Biofilm/2026-10-31T234500Z-antigravity-2095.yaml history/records/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom/2026-10-31T234500Z-antigravity-2095.yaml history/records/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community/2026-10-31T234500Z-antigravity-2095.yaml` | `0` | All 3 modified community YAML records were written through `record_curation_event(..., llm_assisted=True)` + `write_validated_community` and carry schema-valid `HistoryRecord` sidecars (`No issues found`). |
| Causal Review Inventory, Batch Regression & Structured Review Suite | `./.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_record_review_contract.py tests/test_record_review_routes.py tests/test_causal_review_inventory.py tests/test_causal_review_batch27.py tests/test_causal_review_batch36.py tests/test_causal_review_batch97.py tests/test_participating_taxa.py -v` | `0` | All tests pass across structured review contract/immutability checks, causal review inventory integrity (`490` records, `436` reviewed, `54` `needs_research`, `0` stale, `0` structural defects), batch 27/36/97 regression suites, and participating-taxa checks. |
| HTML Community Site & Browser Data Currency Gate | `PYTHONPATH=src ./.venv/bin/python -m communitymech.render && PYTHONPATH=src ./.venv/bin/python -m communitymech.export.browser_export` | `0` | Updated `docs/communities/SMutans_CAlbicans_ECC_Biofilm.html`, `docs/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.html`, `docs/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.html`, and `docs/data.js` (`481` communities rendered cleanly). |
| Lint & Static Typing Gate | `./.venv/bin/black --check src/ tests/ scripts/ && ./.venv/bin/ruff check --cache-dir /tmp/ruff_cache src/ tests/ scripts/ && ./.venv/bin/mypy --cache-dir /tmp/mypy_cache src/` | `0` | All formatting, lint, and static typing checks pass with `0` issues. |
| Workflow Evidence Contract Validation | `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src ./.venv/bin/python -m kg_microbe_workflows validate-evidence --evidence reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-05/revision-0001/evidence.yaml --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-04/revision-0001/evidence.yaml --required-output issue_map --required-output validation` | `0` | Validated `FindingGroupResolution` schema and ancestor evidence graph (`stage: 5`, `10` findings, `8` groups, `7` `carry_forward_ids`). |

## 2. Remediated Record Metrics

- **`CommunityMech:000083` (`kb/communities/SMutans_CAlbicans_ECC_Biofilm.yaml`, `#2095`)**:
  - Added `functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER]` and `abundance_level: DOMINANT` on `Streptococcus mutans`, `functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]` and `abundance_level: ABUNDANT` on `Candida albicans`, `metabolites: [exopolysaccharide (CHEBI:72813)]` on `ecological_interactions[1]`, and `environmental_factors` for `Sucrose availability` (`1% (30 mM) sucrose`) (`PMID:24566629`).
  - Proportional `review-communities` Completeness Score: `80/100` -> `95/100`; `scripts/audit_completeness.py` score: `25/100` -> `90/100`.
- **`CommunityMech:000357` (`kb/communities/Ecoli_GL10_XL12_D_Lactate_Mixed_Sugar_SynCom.yaml`, `#2095`)**:
  - Added `functional_role: [PRIMARY_DEGRADER]` and `abundance_level: DOMINANT` on both `Escherichia coli GL10` and `Escherichia coli XL12` (`PMID:42038008`, `doi:10.1016/j.bidere.2026.100072`).
  - Proportional `review-communities` Completeness Score: `90/100` -> `98/100`; `scripts/audit_completeness.py` score: `35/100` -> `85/100`.
- **`CommunityMech:000397` (`kb/communities/Defined_ThreeStrain_Organic_Nitrogen_Nitrifying_Community.yaml`, `#2095`)**:
  - Added `functional_role: [PRIMARY_DEGRADER]` and `abundance_level: ABUNDANT` on `Bacillus badius NBRC 15713` (`NCBITaxon:1455`, `Pseudobacillus badius`) and `functional_role: [PRIMARY_PRODUCER, CROSS_FEEDER]` and `abundance_level: ABUNDANT` on `Nitrosomonas europaea NBRC 14298` and `Nitrobacter winogradskyi NBRC 14297` (`PMID:42668143`, `doi:10.1093/bbb/zbag131`).
  - Proportional `review-communities` Completeness Score: `85/100` -> `95/100`; `scripts/audit_completeness.py` score: `15/100` -> `65/100`.
