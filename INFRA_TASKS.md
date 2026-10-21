# CommunityMech infrastructure tasks

This versioned ledger collects repository requirements and upgrades discovered
during every goal. The workflow profile and its parent govern intake, stage 6
implementation, closure and cycle restart.

## Intake protocol

- Give each actionable task a stable ID such as `communitymech-infra-0001` and retain it
  across cycles. Record the originating run, cycle and goal, observation,
  desired outcome, evidence paths, priority, dependencies and status.
- Link each task to an actual issue in https://github.com/CultureBotAI/CommunityMech/issues.
  Search existing open and closed issues before creating one. If access fails,
  retain an explicit pending-link blocker; never invent an issue number or URL.
- Preserve resolved and deferred entries with their issue, implementation PR,
  validation and disposition. Do not overwrite previous cycle evidence.
- At stage 6, freeze a bounded snapshot, write a dependency-aware plan and
  acceptance criteria, implement selected work, validate, and complete the
  commit sequence, write the closure receipt and stop; only the supervisor
  dispatches another goal. New arrivals after the cutoff enter the next cycle;
  never expand the frozen task-ID scope. A new blocking prerequisite requires
  an explicit deferred disposition for the selected task. Carry unfinished work
  forward explicitly.

## Machine-readable task inventory

This fenced mapping is the inventory stage 6 freezes and reconciles. Each task
uses `task_id`, `summary`, `status` (`note`, `open`, `deferred`, or `resolved`),
optional `issue_url`, and optional `disposition`. Status `note` may have a
pending issue link; all other statuses require a real issue URL. Keep richer
notes below keyed by the same stable task ID.

<!-- mech-infra-tasks:start -->
```yaml
schema_version: '1.0.0'
tasks:
  - task_id: communitymech-infra-0001
    summary: Evaluate optional edge-level evidence on InteractionDownstream and decouple scope-credit tests from hardcoded corpus counts
    status: note
    disposition: Captured during run mech-goal-sequence-20261019 cycle 1 stage 2 (causal_graphs); pending issue linkage and Stage 6 evaluation.
```
<!-- mech-infra-tasks:end -->

## Tasks

### `communitymech-infra-0001` — Edge-level causal evidence slot and corpus-count test decoupling

- **Origin**: `mech-goal-sequence-20261019`, cycle 1, stage 2 (`causal_graphs`)
- **Observation**:
  1. `InteractionDownstream` in `src/communitymech/schema/communitymech.yaml` defines only `target` and `description`; edge-specific supporting snippets must currently be stored on the parent `EcologicalInteraction.evidence` list and mirrored in `reports/causal_graph_review/decisions/*.yaml`.
  2. `tests/test_community_level_connectivity_credit.py`, `tests/test_causal_review_batch109.py`, and `tests/test_participating_taxa.py` assert exact corpus-wide `COMMUNITY_LEVEL` / `PAIRWISE` node-scope partition integers (`records: 477, with_community_level: 422, mixed: 140, community_level_only: 282, taxa: 1607, credited_solely_by_the_rule: 1310`) and an exact `USERS` filename set, requiring synchronized test updates whenever corpus records or node scopes change.
- **Desired outcome**: Evaluate adding an optional `evidence` slot on `InteractionDownstream` (or formalizing the decision-ledger contract) and refactoring `test_community_level_connectivity_credit.py` / `test_participating_taxa.py` to test the connectivity-credit invariant without brittle hardcoded corpus totals.
- **Evidence paths**:
  - `src/communitymech/schema/communitymech.yaml`
  - `tests/test_community_level_connectivity_credit.py`
  - `tests/test_causal_review_batch109.py`
  - `tests/test_participating_taxa.py`
  - `reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml`
- **Priority**: P2
- **Dependencies**: None
- **Status**: `note` (pending issue linkage at Stage 6)

