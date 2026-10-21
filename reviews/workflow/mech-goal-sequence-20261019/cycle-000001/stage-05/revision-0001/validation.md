# Stage 5 Remediation Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1` (`cycle-000001`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`

## 1. Executed Validation Gates

| Validation Gate | Command | Exit Code | Result Summary |
|---|---|---|---|
| Causal Review Inventory & Batch Regression Suite | `.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_causal_review_batch78.py tests/test_causal_review_batch88.py tests/test_causal_review_batch99.py tests/test_causal_review_batch105.py tests/test_causal_review_batch123.py tests/test_causal_review_inventory.py tests/test_participating_taxa.py tests/test_community_level_connectivity_credit.py` | `0` | `96 passed` across all causal batch regression tests, `participating_taxa` checks, and full 477-record causal review inventory (`423` reviewed, `54` `needs_research`, `0` stale, `0` structural defects). |
| Causal Graph Inventory Rebuild | `.venv/bin/python reports/causal_graph_review/build_inventory.py` | `0` | Rebuilt `reports/causal_graph_review/inventory.tsv` and `reports/causal_graph_review/summary.json` incorporating successor ledger `reports/causal_graph_review/decisions/20261021-stage5-review-remediation.yaml`. |
| HTML & Browser Site Currency Gate | `.venv/bin/python -m communitymech.render` | `0` | Regenerated all 473 HTML community pages, `docs/browser.html`, `docs/index.html`, `docs/communities.json`, and `docs/communities.tsv` so `just check-docs-current` passes with zero diff. |
| Structured Review Save & Append-Only Check | `.venv/bin/python scripts/record_review.py check --require-reviews --base main` | `0` | All retained structured review bundles in `reviews/structured/` (including immutable Stage 4 bundles `20261021T101000Z-stage4-record-deep-audit` and `20261021T101100Z-stage4-frozen-cohort-review` and new Stage 5 bundle `20261021T193000Z-stage5-remediation-verification`) pass LinkML schema validation, Markdown parity, and append-only provenance checks. |
| Workflow Evidence Contract Validation | `.venv/bin/python -c 'import sys; sys.path.insert(0, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src"); from pathlib import Path; from kg_microbe_workflows import read_goal_evidence; read_goal_evidence("reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-05/revision-0001/evidence.yaml", repository_root=Path("."))'` | `0` | Validated `FindingGroupResolution` schema and ancestor evidence graph (`stage: 5`, `13` findings, `11` groups, `7` `carry_forward_ids`). |

## 2. Remediated Record Metrics

- **Core Metadata Completeness (`#2047`)**:
  - `CommunityMech:000434` (`Acidic_Nitrification_Minimal_Consortium.yaml`): `community_origin: ENGINEERED` added; Completeness Score `85.0` → `100.0`.
  - `CommunityMech:000360` (`Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml`): `ecological_state: STABLE` added; Completeness Score `85.0` → `100.0`.
- **Network Participant Connectivity (`#2048`)**:
  - `CommunityMech:000339` (`Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml`): `DISCONNECTED_TAXON` warnings `6` → `0`.
  - `CommunityMech:000415` (`Algal_Methanotroph_Biogas_Valorization_Coculture.yaml`): `DISCONNECTED_TAXON` warnings `1` → `0`.
  - `CommunityMech:000447` (`Brocadia_Low_Nitrogen_Anammox_Consortium.yaml`): `DISCONNECTED_TAXON` warnings `1` → `0`.
  - `CommunityMech:000399` (`#1729`) and `CommunityMech:000433` (`#1648`): Preserved causal-batch-locked participant scope enforced by `tests/test_causal_review_batch88.py` and `tests/test_causal_review_batch78.py`.
- **External Non-Member Host/Pathogen Target Removal (`#2049`)**:
  - `CommunityMech:000347` (`Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml`): `UNKNOWN_TARGET` warnings `3` → `0`.
  - `CommunityMech:000373` (`Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml`): `UNKNOWN_TARGET` warnings `2` → `0`.
  - `CommunityMech:000364` (`#1787`): Preserved causal-batch-locked sclerotia challenge scope enforced by `tests/test_causal_review_batch99.py`.
- **Isolate Primary-Source Alignment & Taxon Metadata (`#2050`)**:
  - `CommunityMech:000273` (`Chromobacterium_Gold_Biocyanidation.yaml`): Unverified refractory arsenopyrite ore recovery claims and un-evidenced `environmental_factors` replaced with waste-PCB bioleaching claims from `doi:10.1007/s10163-014-0276-4`; Completeness Score `100.0`.
  - `CommunityMech:000321` (`BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml`): `functional_role: [CROSS_FEEDER]` and `abundance_level: RARE` added (`PMID:33398099`, `PMID:28963201`); Completeness Score `80.0` → `100.0`.
