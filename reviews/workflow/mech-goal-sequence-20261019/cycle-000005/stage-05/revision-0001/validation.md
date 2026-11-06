# Cycle 5 Stage 5 Remediation Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `5` (`cycle-000005`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`

## 1. Executed Validation Gates

| Validation Gate | Command | Exit Code | Result Summary |
|---|---|---|---|
| Strict Corpus & Schema Validation | `PYTHONPATH=src ./.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | All 3 remediated `kb/communities/` YAML records validate cleanly against `src/communitymech/schema/communitymech.yaml` with `0` errors, `0` GTDB coherence errors, `0` scalar errors, and `0` ontology term label errors. |
| Writer Bypass & History Sidecar Validation | `./.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/SMutans_SSputigena_ECC_Pathobiont/2026-11-04T054500Z-antigravity-2105.yaml history/records/SMutans_VParvula_ASC_Biofilm/2026-11-04T054500Z-antigravity-2105.yaml history/records/SO3_BS3_Lithium_Battery_Bioleaching_Consortium/2026-11-04T054500Z-antigravity-2105.yaml` | `0` | All 3 modified community YAML records were written through `record_curation_event(..., llm_assisted=True)` + `write_validated_community` and carry schema-valid `HistoryRecord` sidecars (`No issues found`). |
| Causal Review Inventory, Batch Regression & Structured Review Suite | `./.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_causal_review_inventory.py tests/test_causal_review_batch27.py tests/test_causal_review_batch97.py tests/test_participating_taxa.py -v` | `0` | All tests pass across causal review inventory integrity (`490` records, `436` reviewed, `54` `needs_research`, `0` stale, `0` structural defects), batch 27/97 regression suites, and participating-taxa checks. |
| HTML Community Site & Browser Data Currency Gate | `PYTHONPATH=src ./.venv/bin/python -m communitymech.render && PYTHONPATH=src ./.venv/bin/python -m communitymech.export.browser_export` | `0` | Updated `docs/communities/SMutans_SSputigena_ECC_Pathobiont.html`, `docs/communities/SMutans_VParvula_ASC_Biofilm.html`, `docs/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.html`, and `docs/data.js` (`485` communities rendered cleanly). |
| Lint & Static Typing Gate | `./.venv/bin/black --check src/ tests/ scripts/ && ./.venv/bin/ruff check --cache-dir /tmp/ruff_cache src/ tests/ scripts/ && ./.venv/bin/mypy --cache-dir /tmp/mypy_cache src/` | `0` | All formatting, lint, and static typing checks pass with `0` issues. |
| Workflow Evidence Contract Validation | `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src ./.venv/bin/python -m kg_microbe_workflows validate-evidence --evidence reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-05/revision-0001/evidence.yaml --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/evidence.yaml --required-output issue_map --required-output validation` | `0` | Validated `FindingGroupResolution` schema and ancestor evidence graph (`stage: 5`, `10` findings, `8` groups, `7` `carry_forward_ids`). |

## 2. Remediated Record Metrics

- **`CommunityMech:000084` (`kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml`, `#2105`)**:
  - Added `functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER]` and `abundance_level: ABUNDANT` on `Streptococcus mutans` (`NCBITaxon:1309`), `functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]` on `Selenomonas sputigena` (`NCBITaxon:69823`), and `environmental_factors` for `1% (w/v) sucrose supplementation in BHIS medium` (`value: 1% (w/v)`) (`PMID:37217495`, `doi:10.1038/s41467-023-38346-3`).
  - Proportional `review-communities` Completeness Score: `80/100` -> `95/100`; `scripts/audit_completeness.py` score: `15/100` -> `80/100`.
- **`CommunityMech:000085` (`kb/communities/SMutans_VParvula_ASC_Biofilm.yaml`, `#2105`)**:
  - Added `functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER]` and `abundance_level: ABUNDANT` on `Streptococcus mutans` (`NCBITaxon:1309`), `functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]` on `Veillonella parvula` (`NCBITaxon:29466`), and `environmental_factors` for `1% (w/v) sucrose supplementation in BHI broth` (`value: 1% (w/v)`) (`PMID:39345197`).
  - Proportional `review-communities` Completeness Score: `80/100` -> `95/100`; `scripts/audit_completeness.py` score: `15/100` -> `80/100`.
- **`CommunityMech:000385` (`kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml`, `#2105`)**:
  - Added `functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]` on `Bacillus subtilis 168 BS3` (`NCBITaxon:1423`, `Bacillus subtilis`) (`PMID:42733304`, `doi:10.1002/advs.77699`).
  - Proportional `review-communities` Completeness Score: `90/100` -> `98/100`; `scripts/audit_completeness.py` score: `20/100` -> `70/100`.
