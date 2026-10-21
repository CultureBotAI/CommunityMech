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
  - task_id: communitymech-infra-0002
    summary: Fix build_sequence_map.py CommonTaxon.genes key mismatch and evaluate optional gene/protein linkage on EcologicalInteraction
    status: note
    disposition: Captured during run mech-goal-sequence-20261019 cycle 1 stage 3 (protein_examples); pending issue linkage and Stage 6 evaluation.
  - task_id: communitymech-infra-0003
    summary: Align audit_completeness.py scoring with proportional Completeness Score rubric and include data/isolates in completeness and network audits
    status: note
    disposition: Captured during run mech-goal-sequence-20261019 cycle 1 stage 4 (record_review); pending issue linkage and Stage 6 evaluation.
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

### `communitymech-infra-0002` — `build_sequence_map.py` `CommonTaxon.genes` projection and interaction-node protein linkage

- **Origin**: `mech-goal-sequence-20261019`, cycle 1, stage 3 (`protein_examples`)
- **Observation**:
  1. `scripts/build_sequence_map.py` (`load_curated_genes()`, lines 626–634) reads `doc.get("functional_genes")`, `fg.get("function")`, and `fg.get("phenotype")` instead of the schema-canonical `CommonTaxon` slots `doc.get("genes")`, `fg.get("product")`, and `fg.get("supports_interaction")`. As a result, `data/embeddings/sequence_map.json` reports `"curated_in_taxa_kb": false` and `"source_taxon_yaml": ""` even for UniProtKB proteins curated in `kb/taxa/*.yaml`.
  2. `EcologicalInteraction` in `src/communitymech/schema/communitymech.yaml` provides `metabolites` and `biological_processes` slots on interaction nodes, whereas gene/protein mediation is represented at the reusable taxon level via `CommonTaxon.genes[].supports_interaction` and `TaxonomicComposition.common_taxon` rather than a direct gene/protein reference slot on `EcologicalInteraction`.
- **Desired outcome**: Update `scripts/build_sequence_map.py` to read `CommonTaxon.genes` (`gene_id`, `gene_symbol`, `locus_tag`, `product`, `supports_interaction`) and evaluate whether `EcologicalInteraction` should optionally reference `CommonTaxon.genes` entries directly.
- **Evidence paths**:
  - `scripts/build_sequence_map.py`
  - `kb/taxa/Shewanella_oneidensis_MR1.yaml`
  - `kb/taxa/Geobacter_sulfurreducens.yaml`
  - `src/communitymech/schema/communitymech.yaml`
- **Priority**: P2
- **Dependencies**: None
- **Status**: `note` (pending issue linkage at Stage 6)

### `communitymech-infra-0003` — Completeness audit rubric alignment and `data/isolates/` scanner coverage

- **Origin**: `mech-goal-sequence-20261019`, cycle 1, stage 4 (`record_review`)
- **Observation**:
  1. `scripts/audit_completeness.py` scans only `kb/communities/*.yaml` (omitting `data/isolates/*.yaml`) and uses a binary presence check (e.g., `has_interactions`, `has_taxon_roles`) rather than the proportional 0–100 Completeness Score rubric defined in `.claude/skills/review-yaml-record/SKILL.md`.
  2. `scripts/record_review.py` calls `Path(__file__).resolve()` at module import time (`REPO_ROOT = Path(__file__).resolve().parents[1]`), which raises `PermissionError` under macOS Seatbelt sandboxes that restrict `stat()` on parent `/Users` directories.
- **Desired outcome**: Extend `scripts/audit_completeness.py` to optionally include `data/isolates/*.yaml` and compute the proportional 0–100 Completeness Score alongside the binary checklist, and wrap `Path(__file__).resolve()` in `scripts/record_review.py` with a fallback to `Path(__file__).absolute()` when parent directory traversal is sandbox-restricted.
- **Evidence paths**:
  - `scripts/audit_completeness.py`
  - `scripts/record_review.py`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/review_report.md`
- **Priority**: P3
- **Dependencies**: None
- **Status**: `note` (pending issue linkage at Stage 6)

