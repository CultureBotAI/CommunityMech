# Cycle 2 Stage 6 Implementation Plan — CommunityMech Infrastructure (`mech-goal-sequence-20261019`)

- **Run**: `mech-goal-sequence-20261019`
- **Cycle**: `2`
- **Stage**: `6` (`infrastructure`)
- **Source Revision**: `a57df1b23d29c57de67f190e8b3bf36446388442`
- **Scope Frozen At**: `2026-10-25T19:44:13Z`
- **Frozen Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-06/revision-0001/infra_snapshot.md` (SHA-256: `716e172f38c4212b5c70d7c32df76fb1fbe6f6179f03f12fedab97114eabf87d`)

## 1. Frozen Intake Scope & Issue Reconciliation

At the supervisor-frozen cutoff (`2026-10-25T19:44:13Z`), `INFRA_TASKS.md` contains four machine-readable tasks:

| Task ID | GitHub Issue | Status at Freeze | Priority | Dependencies | Disposition Plan |
| --- | --- | --- | --- | --- | --- |
| `communitymech-infra-0001` | [CultureBotAI/CommunityMech#2055](https://github.com/CultureBotAI/CommunityMech/issues/2055) | `resolved` | P2 | None | Preserve Cycle 1 Stage 6 resolution (`#2059`) and regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0001_downstream_edge_contract_and_decision_provenance`. |
| `communitymech-infra-0002` | [CultureBotAI/CommunityMech#2056](https://github.com/CultureBotAI/CommunityMech/issues/2056) | `resolved` | P2 | None | Preserve Cycle 1 Stage 6 resolution (`#2059`) and regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0002_build_sequence_map_projects_commontaxon_genes`. |
| `communitymech-infra-0003` | [CultureBotAI/CommunityMech#2057](https://github.com/CultureBotAI/CommunityMech/issues/2057) | `resolved` | P3 | None | Preserve Cycle 1 Stage 6 resolution (`#2059`) and regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0003_audit_completeness_and_seatbelt_safe_root`. |
| `communitymech-infra-0004` | [CultureBotAI/CommunityMech#2063](https://github.com/CultureBotAI/CommunityMech/issues/2063) | `open` | P2 | None | Implement and resolve in Cycle 2 Stage 6 (`#2063`). |

## 2. Dependency Analysis & Execution Order

- `communitymech-infra-0004` (`#2063`) has no upstream blockers and extends the corpus-count decoupling pattern established by `communitymech-infra-0001` (`#2055`) across the remaining five count-pinned test suites identified during Cycle 2 Stage 1 (`add_records`).
- Execution order:
  1. Refactor `tests/test_causal_review_batch109.py` (`test_current_scope_census_tracks_later_source_bounded_repairs`).
  2. Refactor `tests/test_participating_taxa.py` (`BASELINE_USERS`, `_is_legitimate_participating_taxa_user`, `_legitimate_users`, `USERS`, `test_the_corpus_is_unchanged_by_this_feature`) while maintaining full compatibility with `tests/test_okeke_participant_census.py`.
  3. Refactor `tests/test_gtdb_coherence_validator.py` (`test_the_status_distribution_is_what_was_measured`).
  4. Refactor `tests/test_is_reclassified_semantics.py` (bucket partition, non-vacuous floors, `strain_dropped == 0` invariant, and ratio bands).
  5. Refactor `tests/test_transwell_participants.py` (`test_only_transwell_accounts_for_gtdb_distribution_change`).
  6. Add dedicated regression tests in `tests/test_stage6_infrastructure.py::test_infra_0004_corpus_count_decoupling_preserves_invariants`.
  7. Update `INFRA_TASKS.md` with the resolved disposition for `communitymech-infra-0004` (`#2063`).

## 3. Detailed Design & Acceptance Criteria for `communitymech-infra-0004` (`#2063`)

### 3.1 `tests/test_causal_review_batch109.py`
- **Design**: Replace hardcoded `previous` / `expected` corpus totals with dynamic `expected = survey_fn()` backed by post-`#2014` non-vacuous floors (`records >= 484`, `with_community_level >= 429`, `mixed >= 141`, `community_level_only >= 288`, `taxa >= 1623`, `credited_solely_by_the_rule >= 1324`), the partition identity `mixed + community_level_only == with_community_level`, and the exact `#2014` Transwell predecessor delta (`mixed - 1`, `community_level_only + 1`, `taxa - 4`, `credited_solely_by_the_rule - 2`) when `GLBRC_Exometabolite_Transwell_SynCom.yaml` is substituted with its hash-pinned predecessor (`616a2806e363f01a3727ea57dcf3bcd019999943`).

### 3.2 `tests/test_participating_taxa.py` & `tests/test_okeke_participant_census.py`
- **Design**: Preserve the 314 historical records in `BASELINE_USERS` and dynamically discover legitimate `participating_taxa` users via `_is_legitimate_participating_taxa_user(doc)` (requiring every `participating_taxa` list to appear on a `COMMUNITY_LEVEL` interaction and every participant entry to resolve to an in-record `taxonomy` member via `_participant_terms`). Enforce `len(all_files) - len(users) >= 100` (catching any silent schema `ifabsent` default), `BASELINE_USERS <= users` (preventing silent removal of historical participant lists), and `users == USERS` (preserving `tests/test_okeke_participant_census.py` monkeypatch verification and rejecting any `PAIRWISE` or dangling `participating_taxa`).

### 3.3 `tests/test_gtdb_coherence_validator.py`
- **Design**: Replace the brittle 1-taxon integer ceiling (`assert counts["UNRESOLVED"] < 513` at `UNRESOLVED == 512`) with corpus-proportional bounds (`counts["UNRESOLVED"] < total_taxa * 0.35` and `counts["GROUNDED"] > counts["UNRESOLVED"] * 1.6`), while retaining all exact invariants (`counts["WITHHELD"] == 6`, `counts["NOT_ATTEMPTED"] == 0`, `counts["NO_GTDB_EQUIVALENT"] > 50`, `counts["GROUNDED"] > 700`, and zero coherence findings).

### 3.4 `tests/test_is_reclassified_semantics.py`
- **Design**: Preserve the `#480` exact invariant `strain_dropped == 0` (and `identical_after_normalisation == 0`), enforce non-vacuous post-`#480` floors (`total >= TOTAL_TRUE`, `actual >= EXPECTED[bucket]` for positive buckets, `not_reclassified >= NOT_A_RECLASSIFICATION`, `len(above) >= ABOVE_SPECIES`), enforce ratio bands (`0.30 < not_reclassified / total_true < 0.45`, `0.15 <= len(above) / len(blocks) <= 0.45`), and preserve `test_the_corpus_agrees_with_the_tool` (which verifies 100% of stored `is_reclassified` flags against `gtdb_ground.name_differs`).

### 3.5 `tests/test_transwell_participants.py`
- **Design**: Replace `assert current_counts["UNRESOLVED"] == 512` with non-vacuous post-`#2014` floors (`current_counts["UNRESOLVED"] >= 494`, `current_counts["GROUNDED"] > 700`) while retaining the exact dynamic predecessor delta (`expected_previous["UNRESOLVED"] == current_counts["UNRESOLVED"] - 5`, `expected_previous["GROUNDED"] == current_counts["GROUNDED"] + 1`).
