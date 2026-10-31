# Cycle 3 Stage 6 Implementation Plan — CommunityMech Infrastructure (`mech-goal-sequence-20261019`)

- **Run**: `mech-goal-sequence-20261019`
- **Cycle**: `3`
- **Stage**: `6` (`infrastructure`)
- **Source Revision**: `369e6a3571a328652cd503170502f5893ebd1324`
- **Scope Frozen At**: `2026-10-31T10:07:00Z`
- **Frozen Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md` (SHA-256: `ea5df4865a121d43a16f45577c248f285e5e2a81e094ef8e6a7043a209f8069f`)

## 1. Frozen Intake Scope & Issue Reconciliation

At the supervisor-frozen cutoff (`2026-10-31T10:07:00Z`), `INFRA_TASKS.md` contains four machine-readable tasks, all of which are `resolved` (`0` pending `open`, `note`, or `deferred` tasks at freeze):

| Task ID | GitHub Issue | Status at Freeze | Priority | Dependencies | Disposition Plan |
| --- | --- | --- | --- | --- | --- |
| `communitymech-infra-0001` | [CultureBotAI/CommunityMech#2055](https://github.com/CultureBotAI/CommunityMech/issues/2055) | `resolved` | P2 | None | Already resolved in Cycle 1 Stage 6 (`#2059`). Verify regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0001_downstream_edge_contract_and_decision_provenance` and `tests/test_community_level_connectivity_credit.py` on the Cycle 3 corpus (`489` community/isolate records). |
| `communitymech-infra-0002` | [CultureBotAI/CommunityMech#2056](https://github.com/CultureBotAI/CommunityMech/issues/2056) | `resolved` | P2 | None | Already resolved in Cycle 1 Stage 6 (`#2059`). Verify regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0002_build_sequence_map_projects_commontaxon_genes` across all `9` curated UniProtKB accessions (`29` `EvidenceItem` entries) in `kb/taxa/`. |
| `communitymech-infra-0003` | [CultureBotAI/CommunityMech#2057](https://github.com/CultureBotAI/CommunityMech/issues/2057) | `resolved` | P3 | None | Already resolved in Cycle 1 Stage 6 (`#2059`). Verify regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0003_audit_completeness_and_seatbelt_safe_root` across `kb/communities/` (`480`), `data/isolates/` (`9`), and `kb/taxa/` (`2`). |
| `communitymech-infra-0004` | [CultureBotAI/CommunityMech#2063](https://github.com/CultureBotAI/CommunityMech/issues/2063) | `resolved` | P2 | None | Already resolved in Cycle 2 Stage 6 (`#2076`). Verify regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0004_corpus_count_decoupling_preserves_invariants`, `tests/test_causal_review_batch109.py`, `tests/test_participating_taxa.py`, `tests/test_okeke_participant_census.py`, `tests/test_gtdb_coherence_validator.py`, `tests/test_is_reclassified_semantics.py`, and `tests/test_transwell_participants.py` on the expanded Cycle 3 corpus (`489` community/isolate records). |

## 2. Explicit Empty Pending-Task Plan (`explicit_empty_plan: true`)

Per `effective-workflow.json` (`infrastructure_planning.explicit_empty_plan: true`) and `.claude/skills/communitymech-evolve-workflow/SKILL.md` (*"An empty intake is a real no-op with evidence, not a reason to invent upgrades"*):

1. **Pending Scope**: `pending_tasks = {t["task_id"]: t for t in notebook["tasks"] if t["status"] != "resolved"} == {}` (`0` pending tasks).
2. **Code & Schema Modifications**: None required. During Cycle 3 Stages 1–5 (`PR #2077`, `PR #2078`, `PR #2080`, `PR #2081`, `PR #2085`), no new infrastructure blockers or count-pinned test breakages occurred because the Cycle 1 Stage 6 (`#2055`, `#2056`, `#2057`) and Cycle 2 Stage 6 (`#2063`) infrastructure upgrades absorbed the `5` new Cycle 3 Stage 1 community/isolate records (`484 -> 489` community/isolate records: `477 -> 480` in `kb/communities/` and `7 -> 9` in `data/isolates/` in `PR #2077`), the `5` Cycle 3 Stage 2 causal graph expansions (`CommunityMech:000491`–`000495`, Batch 135 in `PR #2078`), the `10` new Cycle 3 Stage 3 `IN_VITRO` coculture `EvidenceItem` annotations (`19 -> 29` evidence entries across the `9` curated UniProtKB proteins in `kb/taxa/` in `PR #2080`), and the `3` Cycle 3 Stage 5 category review remediations (`CommunityMech:000280`, `000434`, `000448` in `#2084` / `PR #2085`) without manual test-count bumps.
3. **Evidence & Index Synchronization**:
   - Synchronize `reviews/workflow/latest.yaml` with the supervisor's `verified-evidence-index.json` (adding the verified Cycle 3 Stage 5 closure entry for `PR #2085`, `merge_commit_sha: 369e6a3571a328652cd503170502f5893ebd1324`).
   - Freeze `reviews/workflow/mech-goal-sequence-20261019/cycle-000003/stage-06/revision-0001/infra_snapshot.md` byte-identical to `INFRA_TASKS.md` (`sha256: ea5df4865a121d43a16f45577c248f285e5e2a81e094ef8e6a7043a209f8069f`).
   - Execute the full Stage 6 regression test suite and repository CI gates on `369e6a3571a328652cd503170502f5893ebd1324` and record the results in `validation.md` and `evidence.yaml` (`outcome: no_findings`, `infra_tasks: []`, `carry_forward_ids: []`).
