# Cycle 8 Stage 5 Remediation Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `8` (`cycle-000008`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`

## 1. Executed Validation Gates

| Validation Gate | Command | Exit Code | Result Summary |
|---|---|---|---|
| Strict Corpus & Schema Validation | `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv kb/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml kb/communities/PPHET_Hybrid_Photosynthetic_PHB_Microbiome.yaml kb/communities/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture.yaml` | `0` | All 3 remediated `kb/communities/` YAML records validate cleanly against `src/communitymech/schema/communitymech.yaml` with `0` errors, `0` GTDB coherence errors, `0` scalar errors, and `0` ontology term label errors. |
| Reference & Snippet Verification | `.venv/bin/linkml-reference-validator validate data kb/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml -s src/communitymech/schema/communitymech.yaml --config conf/reference_validator.yaml` (and `000359`, `000454`) | `0` | All 3 modified community YAML records pass `linkml-reference-validator` with `0` snippet mismatches against `references_cache/`. |
| Writer Bypass & History Sidecar Validation | `.venv/bin/linkml-validate --schema src/communitymech/schema/history.yaml --target-class HistoryRecord history/records/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism/2026-11-06T113500Z-antigravity-2514a1.yaml history/records/PPHET_Hybrid_Photosynthetic_PHB_Microbiome/2026-11-06T113500Z-antigravity-2514a2.yaml history/records/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture/2026-11-06T113500Z-antigravity-2514a3.yaml` | `0` | All 3 modified community YAML records were written through `record_curation_event(..., llm_assisted=True)` + `write_validated_community` and carry schema-valid `HistoryRecord` sidecars (`No issues found`). |
| Causal Review Inventory, GTDB Demoted Clades & Participating Taxa Suite | `.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_causal_review_inventory.py tests/test_gtdb_demoted_clades.py tests/test_participating_taxa.py -v` | `0` | All `32` causal review inventory integrity checks pass (`508` records, `454` reviewed, `54` `needs_research`, `0` stale, `0` structural defects) alongside GTDB demoted clades and participating-taxa checks. |
| HTML Community Site & Browser Data Currency Gate | `.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_docs_do_not_contradict_the_kb.py tests/test_published_pages_name_real_records.py -v` | `0` | Updated `docs/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.html`, `docs/communities/PPHET_Hybrid_Photosynthetic_PHB_Microbiome.html`, and `docs/communities/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture.html`; `1014` passed in `test_docs_do_not_contradict_the_kb.py` and `test_published_pages_name_real_records.py` (`501` communities rendered cleanly). |
| Lint & Static Typing Gate | `.venv/bin/black --check src/ tests/ scripts/ && .venv/bin/ruff check --cache-dir /tmp/ruff_cache src/ tests/ scripts/ && .venv/bin/mypy --cache-dir /tmp/mypy_cache src/` | `0` | All formatting, lint, and static typing checks pass with `0` issues. |
| Workflow Evidence Contract Validation | `PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/python -m kg_microbe_workflows validate-evidence --root . --previous reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/evidence.yaml --required-output issue_map --required-output validation reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-05/revision-0001/evidence.yaml` | `0` | Validated `FindingGroupResolution` schema and ancestor evidence graph (`stage: 5`, `10` findings, `8` groups, `7` `carry_forward_ids`). |

## 2. Remediated Record Metrics

- **`CommunityMech:000210` (`kb/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml`, `#2514`)**:
  - Added `abundance_level: DOMINANT` and verbatim flow-cytometry coculture evidence (`PMID:26885935`, `doi:10.1021/acssynbio.5b00236`) on `Zymomonas mobilis` (`NCBITaxon:542`, `taxonomy[0]`) and `Escherichia coli` (`NCBITaxon:562`, `taxonomy[1]`).
  - `review-communities` `s_ab` rubric component: `0/5` -> `5/5` (`0/2` -> `2/2` taxa with `abundance_level`); proportional Completeness Score: `98/100`; `scripts/audit_completeness.py` score: `85/100`.
- **`CommunityMech:000359` (`kb/communities/PPHET_Hybrid_Photosynthetic_PHB_Microbiome.yaml`, `#2514`)**:
  - Added `abundance_level: ABUNDANT` and verbatim 16S community-composition evidence (`PMID:41559821`, `PMC12819161`, `doi:10.1111/1751-7915.70302`) on `non-cyanobacterial WCRM heterotrophs` (`NCBITaxon:2`, `taxonomy[1]`).
  - `review-communities` `s_ab` rubric component: `2.5/5` -> `5/5` (`1/2` -> `2/2` taxa with `abundance_level`); proportional Completeness Score: `94/100`; `scripts/audit_completeness.py` score: `90/100`.
- **`CommunityMech:000454` (`kb/communities/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture.yaml`, `#2514`)**:
  - Added `abundance_level: DOMINANT` and verbatim mutualistic co-culture evidence (`PMID:42468699`, `doi:10.1016/j.biortech.2026.135440`) on `Chelatococcus sp. XZ-Ab1` (`NCBITaxon:3034027`, `taxonomy[1]`).
  - `review-communities` `s_ab` rubric component: `2.5/5` -> `5/5` (`1/2` -> `2/2` taxa with `abundance_level`); proportional Completeness Score: `90/100`; `scripts/audit_completeness.py` score: `60/100`.
