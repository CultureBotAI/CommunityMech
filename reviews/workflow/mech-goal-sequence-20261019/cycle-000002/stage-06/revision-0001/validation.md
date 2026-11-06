# Cycle 2 Stage 6 Validation Report — CommunityMech Infrastructure (`mech-goal-sequence-20261019`)

- **Run**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `6` (`infrastructure`)
- **Source Revision**: `a57df1b23d29c57de67f190e8b3bf36446388442`
- **Scope Frozen At**: `2026-10-25T19:44:13Z`
- **Frozen Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md` (SHA-256: `716e172f38c4212b5c70d7c32df76fb1fbe6f6179f03f12fedab97114eabf87d`)

## 1. Task-by-Task Validation Summary

| Task ID | GitHub Issue | Status | Validation Evidence |
| --- | --- | --- | --- |
| `communitymech-infra-0001` | [CultureBotAI/CommunityMech#2055](https://github.com/CultureBotAI/CommunityMech/issues/2055) | `resolved` | `tests/test_stage6_infrastructure.py::test_infra_0001_downstream_edge_contract_and_decision_provenance` and `tests/test_community_level_connectivity_credit.py` passed (`0` failures). |
| `communitymech-infra-0002` | [CultureBotAI/CommunityMech#2056](https://github.com/CultureBotAI/CommunityMech/issues/2056) | `resolved` | `tests/test_stage6_infrastructure.py::test_infra_0002_build_sequence_map_projects_commontaxon_genes` passed (`0` failures). |
| `communitymech-infra-0003` | [CultureBotAI/CommunityMech#2057](https://github.com/CultureBotAI/CommunityMech/issues/2057) | `resolved` | `tests/test_stage6_infrastructure.py::test_infra_0003_audit_completeness_and_seatbelt_safe_root` passed (`0` failures). |
| `communitymech-infra-0004` | [CultureBotAI/CommunityMech#2063](https://github.com/CultureBotAI/CommunityMech/issues/2063) | `resolved` | `tests/test_stage6_infrastructure.py::test_infra_0004_corpus_count_decoupling_preserves_invariants`, `tests/test_causal_review_batch109.py`, `tests/test_participating_taxa.py`, `tests/test_okeke_participant_census.py`, `tests/test_gtdb_coherence_validator.py`, `tests/test_is_reclassified_semantics.py`, and `tests/test_transwell_participants.py` passed (`0` failures). |

## 2. Detailed Validation Results for `communitymech-infra-0004` (`#2063`)

1. **`tests/test_causal_review_batch109.py`**:
   - 12/12 tests passed, including `test_current_scope_census_tracks_later_source_bounded_repairs`, which enforces post-`#2014` non-vacuous floors (`records >= 484`, `with_community_level >= 429`, `mixed >= 141`, `community_level_only >= 288`, `taxa >= 1623`, `credited_solely_by_the_rule >= 1324`), the partition identity `mixed + community_level_only == with_community_level`, and the exact `#2014` Transwell predecessor delta when substituting `kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml` with `616a2806e363f01a3727ea57dcf3bcd019999943`.
2. **`tests/test_participating_taxa.py` & `tests/test_okeke_participant_census.py`**:
   - 9/9 tests in `tests/test_participating_taxa.py` and 1/1 test in `tests/test_okeke_participant_census.py` passed.
   - `BASELINE_USERS` preserves all 314 historical records (`users >= BASELINE_USERS`), `len(all_files) - len(users) >= 100` guards against schema-wide `ifabsent` defaults, and `_is_legitimate_participating_taxa_user` verifies that any `participating_taxa` user populates the slot only on `COMMUNITY_LEVEL` interactions with resolved in-record `taxonomy` participants.
3. **`tests/test_gtdb_coherence_validator.py`**:
   - `test_the_status_distribution_is_what_was_measured` and `test_the_committed_kb_is_coherent` passed (`GROUNDED == 942 > 700`, `UNRESOLVED == 512 < total_taxa * 0.35`, `GROUNDED > UNRESOLVED * 1.6`, `WITHHELD == 6`, `NOT_ATTEMPTED == 0`, `NO_GTDB_EQUIVALENT > 50`, `0` coherence errors across all 486 community/isolate records).
4. **`tests/test_is_reclassified_semantics.py`**:
   - 42/42 tests passed, enforcing `strain_dropped == 0`, `identical_after_normalisation == 0`, non-vacuous post-`#480` bucket floors, ratio bands (`0.30 < not_reclassified / total_true < 0.45`, `0.15 <= len(above) / len(blocks) <= 0.45`), and 100% agreement between stored `is_reclassified` flags and `gtdb_ground.name_differs`.
5. **`tests/test_transwell_participants.py`**:
   - 8/8 tests passed, including `test_only_transwell_accounts_for_gtdb_distribution_change` (`current_counts["UNRESOLVED"] >= 494`, `current_counts["GROUNDED"] > 700`, and exact `-5 UNRESOLVED` / `+1 GROUNDED` predecessor delta).
6. **`tests/test_stage6_infrastructure.py`**:
   - 4/4 tests passed (`test_infra_0001_downstream_edge_contract_and_decision_provenance`, `test_infra_0002_build_sequence_map_projects_commontaxon_genes`, `test_infra_0003_audit_completeness_and_seatbelt_safe_root`, `test_infra_0004_corpus_count_decoupling_preserves_invariants`).

## 3. Repository Gate Verification

- **Lint (`ruff check`)**: `0` errors across all modified files.
- **Strict Instance Validation (`scripts/validate_strict.py`)**: `0` errors across all corpus records.
- **Network Quality Audit (`scripts/audit_network_quality.py --check`)**: `0` errors.
- **Curation History (`scripts/check_curation_history.py`)**: `0` errors.
- **Docs Currency (`scripts/check_docs_current.py`)**: `0` errors.
- **Vendored Sync (`tests/test_record_review_contract.py`)**: `6/6` passed.
