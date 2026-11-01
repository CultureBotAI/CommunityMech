# Cycle 4 Stage 6 Implementation Plan — CommunityMech Infrastructure (`mech-goal-sequence-20261019`)

- **Run**: `mech-goal-sequence-20261019`
- **Cycle**: `4`
- **Stage**: `6` (`infrastructure`)
- **Source Revision**: `fb5cbe66b8e19daed26b32ab96316af75c3ec961`
- **Scope Frozen At**: `2026-11-01T01:43:10Z`
- **Frozen Snapshot**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md` (SHA-256: `ea5df4865a121d43a16f45577c248f285e5e2a81e094ef8e6a7043a209f8069f`)

## 1. Frozen Intake Scope & Issue Reconciliation

At the supervisor-frozen cutoff (`2026-11-01T01:43:10Z`), `INFRA_TASKS.md` contains four machine-readable tasks, all of which are `resolved` (`0` pending `open`, `note`, or `deferred` tasks at freeze):

| Task ID | GitHub Issue | Status at Freeze | Priority | Dependencies | Disposition Plan |
| --- | --- | --- | --- | --- | --- |
| `communitymech-infra-0001` | [CultureBotAI/CommunityMech#2055](https://github.com/CultureBotAI/CommunityMech/issues/2055) | `resolved` | P2 | None | Already resolved in Cycle 1 Stage 6 (`#2059`). Verify regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0001_downstream_edge_contract_and_decision_provenance` and `tests/test_community_level_connectivity_credit.py` on the Cycle 4 corpus (`490` community/isolate records). |
| `communitymech-infra-0002` | [CultureBotAI/CommunityMech#2056](https://github.com/CultureBotAI/CommunityMech/issues/2056) | `resolved` | P2 | None | Already resolved in Cycle 1 Stage 6 (`#2059`). Verify regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0002_build_sequence_map_projects_commontaxon_genes` across all `9` curated UniProtKB accessions (`32` `EvidenceItem` entries) in `kb/taxa/` (`kb/taxa/Geobacter_sulfurreducens.yaml` [`4` genes, `13` evidence entries] and `kb/taxa/Shewanella_oneidensis_MR1.yaml` [`5` genes, `19` evidence entries]). |
| `communitymech-infra-0003` | [CultureBotAI/CommunityMech#2057](https://github.com/CultureBotAI/CommunityMech/issues/2057) | `resolved` | P3 | None | Already resolved in Cycle 1 Stage 6 (`#2059`). Verify regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0003_audit_completeness_and_seatbelt_safe_root` across `kb/communities/` (`481`), `data/isolates/` (`9`), and `kb/taxa/` (`2`). |
| `communitymech-infra-0004` | [CultureBotAI/CommunityMech#2063](https://github.com/CultureBotAI/CommunityMech/issues/2063) | `resolved` | P2 | None | Already resolved in Cycle 2 Stage 6 (`#2076`). Verify regression coverage in `tests/test_stage6_infrastructure.py::test_infra_0004_corpus_count_decoupling_preserves_invariants`, `tests/test_causal_review_batch109.py`, `tests/test_participating_taxa.py`, `tests/test_okeke_participant_census.py`, `tests/test_gtdb_coherence_validator.py`, `tests/test_is_reclassified_semantics.py`, and `tests/test_transwell_participants.py` on the expanded Cycle 4 corpus (`490` community/isolate records). |

## 2. Explicit Empty Pending-Task Plan (`explicit_empty_plan: true`)

Per `effective-workflow.json` (`infrastructure_planning.explicit_empty_plan: true`) and `.claude/skills/communitymech-evolve-workflow/SKILL.md` (*"An empty intake is a real no-op with evidence, not a reason to invent upgrades"*):

1. **Pending Scope**: `pending_tasks = {t["task_id"]: t for t in notebook["tasks"] if t["status"] != "resolved"} == {}` (`0` pending tasks).
2. **Code & Schema Modifications**: None required. During Cycle 4 Stages 1–5 (`PR #2087`, `PR #2089`, `PR #2091`, `PR #2093`, `PR #2096`), no new infrastructure blockers or count-pinned test breakages occurred because the Cycle 1 Stage 6 (`#2055`, `#2056`, `#2057`) and Cycle 2 Stage 6 (`#2063`) infrastructure upgrades absorbed the `1` new Cycle 4 Stage 1 community record (`CommunityMech:000496` `Synechococcus_Escherichia_Sucrose_Consortium` in `PR #2087`, expanding the corpus from `489 -> 490` community/isolate records: `480 -> 481` in `kb/communities/` and `9` in `data/isolates/`), the `1` Cycle 4 Stage 2 causal graph expansion (`CommunityMech:000496`, Batch 136 in `PR #2089`), the `3` new Cycle 4 Stage 3 `IN_VITRO` coculture `EvidenceItem` annotations on `pilA` and `omcS` in `kb/taxa/Geobacter_sulfurreducens.yaml` (`29 -> 32` evidence entries across the `9` curated UniProtKB proteins in `kb/taxa/` in `PR #2091`), and the `3` Cycle 4 Stage 5 category review remediations (`CommunityMech:000083`, `000357`, `000397` in `#2095` / `PR #2096`) without manual test-count bumps.
3. **Evidence & Index Synchronization**:
   - Synchronize `reviews/workflow/latest.yaml` with the supervisor's `verified-evidence-index.json` (adding the verified Cycle 4 Stage 5 closure entry for `PR #2096`, `merge_commit_sha: fb5cbe66b8e19daed26b32ab96316af75c3ec961`).
   - Freeze `reviews/workflow/mech-goal-sequence-20261019/cycle-000004/stage-06/revision-0001/infra_snapshot.md` byte-identical to `INFRA_TASKS.md` (`sha256: ea5df4865a121d43a16f45577c248f285e5e2a81e094ef8e6a7043a209f8069f`).
   - Execute the full Stage 6 regression test suite and repository CI gates on `fb5cbe66b8e19daed26b32ab96316af75c3ec961` and record the results in `validation.md` and `evidence.yaml` (`outcome: no_findings`, `infra_tasks: []`, `carry_forward_ids: []`).
