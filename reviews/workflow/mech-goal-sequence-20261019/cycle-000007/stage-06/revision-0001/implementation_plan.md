# Cycle 7 Stage 6 Infrastructure Implementation Plan (`mech-goal-sequence-20261019`)

## 1. Frozen Intake Cutoff and Ledger Snapshot

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: `cycle=7`, `stage=6` (`infrastructure`), `revision=1`
- **Repository**: `CultureBotAI/CommunityMech`
- **Source Revision (`HEAD` at freeze)**: `4205fe49c6045efa847b885baf89699486704a50`
- **Frozen Cutoff Timestamp (`status.json` `infra_scope.frozen_at`)**: `2026-11-05T19:18:03Z`
- **Ledger Path**: `INFRA_TASKS.md`
- **Ledger SHA-256 (`INFRA_TASKS.md`)**: `ea5df4865a121d43a16f45577c248f285e5e2a81e094ef8e6a7043a209f8069f`
- **Snapshot Path**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000007/stage-06/revision-0001/infra_snapshot.md`
- **Snapshot SHA-256 (`infra_snapshot.md`)**: `ea5df4865a121d43a16f45577c248f285e5e2a81e094ef8e6a7043a209f8069f`

## 2. Reconciled Task Inventory at Freeze Cutoff

At the documented freeze cutoff (`2026-11-05T19:18:03Z`), the fenced `mech-infra-tasks` inventory in `INFRA_TASKS.md` contains four tracked tasks, all of which are in `resolved` status from prior Stage 6 implementations, with zero `note`, `open`, or `deferred` tasks queued during Cycle 7 Stages 1–5:

| Task ID | GitHub Issue | Originating Cycle/Stage | Status at Cutoff | Cycle 7 Stage 6 Disposition |
|---|---|---|---|---|
| `communitymech-infra-0001` | [#2055](https://github.com/CultureBotAI/CommunityMech/issues/2055) | Cycle 1, Stage 2 (`causal_graphs`) | `resolved` | Retained as `resolved`; re-verified across the expanded 503-record (`494` community + `9` isolate) Cycle 7 corpus (`586` directed `InteractionDownstream` edges). |
| `communitymech-infra-0002` | [#2056](https://github.com/CultureBotAI/CommunityMech/issues/2056) | Cycle 1, Stage 3 (`protein_examples`) | `resolved` | Retained as `resolved`; re-verified `CommonTaxon.genes` projection across `9` curated UniProtKB entries (`43` `EvidenceItem` entries after Cycle 7 Stage 3 enrichment in PR `#2118`). |
| `communitymech-infra-0003` | [#2057](https://github.com/CultureBotAI/CommunityMech/issues/2057) | Cycle 1, Stage 4 (`record_review`) | `resolved` | Retained as `resolved`; re-verified proportional 0–100 completeness/validation scoring and multi-root scanning (`494` communities, `9` isolates, `2` taxa; `505` total records, `366/505` required-complete, average `67.42/100`) plus Seatbelt-safe `_repo_root()`. |
| `communitymech-infra-0004` | [#2063](https://github.com/CultureBotAI/CommunityMech/issues/2063) | Cycle 2, Stage 1 (`add_records`) | `resolved` | Retained as `resolved`; re-verified dynamic corpus-count decoupling across all five refactored test suites after Cycle 7 Stage 1 (`+5` community records in PR `#2116`), Stage 2 (causal graph enrichment in PR `#2117`), Stage 3 (UniProt protein enrichment in PR `#2118`), Stage 4 (cohort review in PR `#2119`), and Stage 5 (grouped remediation in PR `#2121`). |

## 3. Explicit Empty Pending-Task Plan (`explicit_empty_plan: true`)

Per `effective-workflow.json` (`stages[5].requirements.explicit_empty_plan: true`) and `.claude/skills/communitymech-evolve-workflow/SKILL.md` (*"An empty intake is a real no-op with evidence, not a reason to invent upgrades"*):

1. **Selected New Implementation Tasks**: `0` (`infra_tasks: []` for newly selected pending work in `evidence.yaml`; all 4 ledger tasks in `INFRA_TASKS.md` remain `resolved` and are preserved unchanged).
2. **New GitHub Issues Created**: `0` (all 4 existing tasks are already linked to closed issues `#2055`, `#2056`, `#2057`, and `#2063`; no unlinked notes or open tasks exist).
3. **Carry-Forward / Deferred Tasks**: `0` (`carry_forward_ids: []`).
4. **Tracked Workflow Latest Index Update**:
   - Update `reviews/workflow/latest.yaml` from `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/workspace/session-orchestration/20261019/communitymech/verified-evidence-index.json` so that the verified Cycle 7 Stage 5 closure (`PR #2121`, `head_sha: 40fdbd6a5976f0f1ca04d1c8eaa52fc3adfbc44b`, `merge_commit_sha: 4205fe49c6045efa847b885baf89699486704a50`, `receipt_sha256: 8468c9c981b51ac3a369be4ae08f1cbc80afb55463f08faf0baa57fa6de99d19`) is recorded in the tracked repository index.
5. **Regression & Gate Verification Scope**:
   - Execute `tests/test_stage6_infrastructure.py` and the decoupled corpus-invariant suites (`tests/test_community_level_connectivity_credit.py`, `tests/test_causal_review_batch109.py`, `tests/test_participating_taxa.py`, `tests/test_okeke_participant_census.py`, `tests/test_gtdb_coherence_validator.py`, `tests/test_is_reclassified_semantics.py`, `tests/test_transwell_participants.py`, `tests/test_record_review_contract.py`) to confirm that all resolved Stage 6 infrastructure upgrades continue to hold across the 503-record (`494` communities + `9` isolates) + 2-taxon (`505` total) Cycle 7 corpus.
   - Execute `scripts/validate_strict.py`, `communitymech audit-network`, `scripts/audit_completeness.py --include-taxa`, `ruff`, `black`, `mypy`, and `kg_microbe_workflows validate-evidence`.
