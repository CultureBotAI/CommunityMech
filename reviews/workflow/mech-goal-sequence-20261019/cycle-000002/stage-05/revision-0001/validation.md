# Cycle 2 Stage 5 Remediation Validation Report

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `2` (`cycle-000002`)
- **Stage**: `5` (`resolve_review_findings`, `revision-0001`)
- **Repository**: `CultureBotAI/CommunityMech`

## 1. Executed Validation Gates

| Validation Gate | Command | Exit Code | Result Summary |
|---|---|---|---|
| Strict Corpus & Schema Validation | `PYTHONPATH=src .venv/bin/python scripts/validate_strict.py` | `0` | All 477 `kb/communities/` YAML records, 7 `data/isolates/` YAML records, and 2 `kb/taxa/` records validate cleanly against `src/communitymech/schema/communitymech.yaml` with `0` errors. |
| Writer Bypass & History Sidecar Audit | `PYTHONPATH=src .venv/bin/python scripts/audit_writers.py` | `0` | All 10 modified community YAML records have valid append-only `curation_history` entries and matching `history/records/` sidecars. |
| Causal Review Inventory & Taxon Linkage Suite | `.venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_taxon_records.py tests/test_causal_review_inventory.py tests/test_causal_review_batch19.py tests/test_causal_review_batch24.py tests/test_causal_review_batch45.py tests/test_causal_review_batch78.py tests/test_causal_review_batch91.py tests/test_causal_review_batch94.py tests/test_causal_review_batch101.py` | `0` | `173 passed` across reusable taxon linkage checks (`6/6` `Geobacter sulfurreducens`, `9/9` `Shewanella oneidensis`), causal review inventory integrity (`423` reviewed, `54` `needs_research`, `0` stale, `0` structural defects), and all batch regression suites. |
| HTML & Browser Site Currency Gate | `PYTHONPATH=src .venv/bin/python -m communitymech.render` | `0` | Updated `docs/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.html`, `BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.html`, `BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.html`, and `BioModels_MODEL2407300002_Sponge_Holobiont_Network.html` (`0` diffs against `communitymech.render`). |
| Structured Review Validation | `PYTHONPATH=src .venv/bin/python -c 'from pathlib import Path; from scripts.record_review import parse_review_bundle; parse_review_bundle(Path("reviews/structured/20261025T161500Z-c2s5-remediation-verification"))'` | `0` | Structured review bundle `20261025T161500Z-c2s5-remediation-verification` (`review.yaml` sha256 `c8b7bd9b8e462081a734db496e8314848c4474a56deadbec891cf4af6f9ea644`) passes schema validation and Markdown parity while preserving immutable Stage 4 bundles `20261025T113500Z-c2s4-record-deep-audit` and `20261025T113600Z-c2s4-frozen-cohort-review`. |
| Workflow Evidence Contract Validation | `.venv/bin/python -c 'import sys; sys.path.insert(0, "/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/src"); from pathlib import Path; from kg_microbe_workflows import read_goal_evidence; read_goal_evidence("reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-05/revision-0001/evidence.yaml", repository_root=Path("."))'` | `0` | Validated `FindingGroupResolution` schema and ancestor evidence graph (`stage: 5`, `10` findings, `9` groups, `7` `carry_forward_ids`). |

## 2. Remediated Record Metrics

- **BioModels Host-Associated `environment_term` Grounding (`#2072`)**:
  - `CommunityMech:000006` (`BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml`): `environment_term` (`ENVO:01001002` `animal-associated environment`) added (`PMID:30254121`); `calculate_completeness` score `75.0` -> `80.0`.
  - `CommunityMech:000007` (`BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml`): `environment_term` (`ENVO:01001002` `animal-associated environment`) added (`PMID:30254121`); `calculate_completeness` score `75.0` -> `80.0`.
  - `CommunityMech:000008` (`BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml`): `environment_term` (`ENVO:01001002` `animal-associated environment`) added (`PMID:30254121`); `calculate_completeness` score `75.0` -> `80.0`.
  - `CommunityMech:000013` (`BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml`): `environment_term` (`ENVO:01001002` `animal-associated environment`) added (`PMID:39738126`); `calculate_completeness` score `75.0` -> `80.0`.
  - Corpus-wide `environment_term` coverage across all 484 `MicrobialCommunity` records: `480/484` (`99.17%`) -> `484/484` (`100.0%`).
- **Reusable `CommonTaxon` Linkage (`#2073`)**:
  - `CommunityMech:000031`, `000175`, `000176`, and `000268`: linked `Geobacter sulfurreducens` (`NCBITaxon:35554`) to `common_taxon: CommunityMech:taxon:000002` (`kb/taxa/Geobacter_sulfurreducens.yaml`), bringing corpus-wide linkage to `6/6` (`100%`).
  - `CommunityMech:000288` and `000294`: linked `Shewanella oneidensis` (`NCBITaxon:211586` / `NCBITaxon:70863`) to `common_taxon: CommunityMech:taxon:000001` (`kb/taxa/Shewanella_oneidensis_MR1.yaml`), bringing corpus-wide linkage to `9/9` (`100%`).
