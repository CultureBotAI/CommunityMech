# Cycle 3 Stage 5 Remediation Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `3` (`cycle-000003`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`

## 1. Executed Validation Gates

| Validation Gate | Command | Exit Code | Result Summary |
|---|---|---|---|
| Strict Corpus & Schema Validation | `PYTHONPATH=src ./.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | All 480 `kb/communities/` YAML records and 9 `data/isolates/` YAML records (`489` total files) validate cleanly against `src/communitymech/schema/communitymech.yaml` with `0` errors. |
| Writer Bypass & History Sidecar Validation | `PYTHONPATH=src ./.venv/bin/python scripts/audit_writers.py` & `./.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Pinus_armandii_Endophytic_Biocontrol_SynCom/2026-10-31T080000Z-antigravity-2084.yaml history/records/Acidic_Nitrification_Minimal_Consortium/2026-10-31T080000Z-antigravity-2084.yaml history/records/Soymilk_Mixed_Starter_Metabolic_Division_SynCom/2026-10-31T080000Z-antigravity-2084.yaml` | `0` | All 3 modified community YAML records were written through `record_curation_event(..., llm_assisted=True)` + `write_validated_community` and carry schema-valid `HistoryRecord` sidecars (`No issues found`). |
| Causal Review Inventory, Batch Regression & Structured Review Suite | `./.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_record_review_contract.py tests/test_record_review_routes.py tests/test_causal_review_inventory.py tests/test_causal_review_batch85.py tests/test_causal_review_batch104.py tests/test_participating_taxa.py -v` | `0` | `65 passed` across structured review contract/immutability checks, causal review inventory integrity (`489` records, `435` reviewed, `54` `needs_research`, `0` stale, `0` structural defects), batch 85 and batch 104 regression suites, and participating-taxa checks. |
| HTML Community Site Currency Gate | `PYTHONPATH=src ./.venv/bin/python -m communitymech.render` | `0` | Updated `docs/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.html`, `docs/communities/Acidic_Nitrification_Minimal_Consortium.html`, and `docs/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.html` (`480` communities rendered cleanly). |
| Lint & Static Typing Gate | `./.venv/bin/black --check src/ tests/ scripts/ && ./.venv/bin/ruff check --cache-dir /tmp/ruff_cache src/ tests/ scripts/ && ./.venv/bin/mypy --cache-dir /tmp/mypy_cache src/` | `0` | `408 files would be left unchanged`, `All checks passed!`, and `Success: no issues found in 49 source files`. |
| Workflow Evidence Contract Validation | `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src ./.venv/bin/python -m kg_microbe_workflows validate-evidence --evidence reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-05/revision-0001/evidence.yaml --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-04/revision-0001/evidence.yaml --required-output issue_map --required-output validation` | `0` | Validated `FindingGroupResolution` schema and ancestor evidence graph (`stage: 5`, `10` findings, `8` groups, `7` `carry_forward_ids`). |

## 2. Remediated Record Metrics

- **`CommunityMech:000280` (`kb/communities/Pinus_armandii_Endophytic_Biocontrol_SynCom.yaml`, `#2084`)**:
  - Added `functional_role: [PATHOGEN_ANTAGONIST]` on `Paenibacillus terrae RE7`, `Bacillus velezensis NA3`, and `Bacillus subtilis NA11`, and `abundance_level: ABUNDANT` across all 5 equal-part SynCom members (`PMID:42322490`).
  - Preserved `ecological_interactions[2]` (`Pinus Seedling Growth Promotion`) without `biological_processes` per `tests/test_causal_review_batch85.py` (`#1705`).
  - `calculate_completeness` score: `5` -> `15`.
- **`CommunityMech:000434` (`kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml`, `#2084`)**:
  - Added `functional_role: [PRIMARY_PRODUCER]` and `abundance_level: DOMINANT` on `"Candidatus Nitrosoglobus kelleri"` and `abundance_level: DOMINANT` on `Mycobacterium species` (`PMID:42762737`, `doi:10.1016/j.watres.2026.126966`).
  - `calculate_completeness` score: `0` -> `10`.
- **`CommunityMech:000448` (`kb/communities/Soymilk_Mixed_Starter_Metabolic_Division_SynCom.yaml`, `#2084`)**:
  - Added `functional_role: [PRIMARY_DEGRADER]` and `abundance_level: DOMINANT` on `Streptococcus salivarius subsp. thermophilus`, `abundance_level: ABUNDANT` on `Lactobacillus delbrueckii subsp. bulgaricus`, `abundance_level: DOMINANT` on `Lactiplantibacillus plantarum`, and explicit 3-member `participating_taxa` + `biological_processes` (`GO:0006113` `fermentation`) on `Inferred Soymilk Nutrient Cross-Feeding` (`PMID:42637460`, `doi:10.1016/j.foodres.2026.120134`).
  - Eliminated the `DISCONNECTED_TAXON` warning on `Lactobacillus delbrueckii subsp. bulgaricus` (reducing corpus-wide network warnings from `45` to `44` with `0` errors).
  - `calculate_completeness` score: `5` -> `20`.
