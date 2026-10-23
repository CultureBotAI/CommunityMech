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
    status: resolved
    issue_url: https://github.com/CultureBotAI/CommunityMech/issues/2055
    disposition: Resolved in Stage 6 (#2055). Decoupled test_community_level_connectivity_credit.py upper bounds from hardcoded corpus counts (bounding with_community_level by survey['records'] and mixed by survey['with_community_level'] while retaining non-vacuous floors and share ratio guards) and added automated contract tests in tests/test_stage6_infrastructure.py verifying that all InteractionDownstream edges resolve to in-record targets backed by parent EcologicalInteraction EvidenceItem citations and decision-ledger provenance.
  - task_id: communitymech-infra-0002
    summary: Fix build_sequence_map.py CommonTaxon.genes key mismatch and evaluate optional gene/protein linkage on EcologicalInteraction
    status: resolved
    issue_url: https://github.com/CultureBotAI/CommunityMech/issues/2056
    disposition: Resolved in Stage 6 (#2056). Updated scripts/build_sequence_map.py (load_curated_genes and _enrich_from_taxa_yaml) to read both canonical CommonTaxon.genes (product, supports_interaction, gene_symbol, locus_tag, supports_roles, go_terms, evidence/references) and legacy functional_genes (function, phenotype), projecting all 9 curated UniProtKB accessions across kb/taxa/Shewanella_oneidensis_MR1.yaml and kb/taxa/Geobacter_sulfurreducens.yaml, with regression tests in tests/test_stage6_infrastructure.py.
  - task_id: communitymech-infra-0003
    summary: Align audit_completeness.py scoring with proportional Completeness Score rubric and include data/isolates in completeness and network audits
    status: resolved
    issue_url: https://github.com/CultureBotAI/CommunityMech/issues/2057
    disposition: Resolved in Stage 6 (#2057). Implemented scripts/audit_completeness.py (and updated scripts/generate_validation_report.py) with Seatbelt-safe _repo_root() path resolution, proportional 0-100 calculate_completeness and calculate_validation_score metrics matching .claude/skills/review-communities/reference/metrics-and-reports.md, and multi-root scanning across kb/communities/*.yaml, data/isolates/*.yaml, and kb/taxa/*.yaml while preserving scripts/record_review.py byte-identical to its governed CLAW payload.
  - task_id: communitymech-infra-0004
    summary: Decouple remaining count-pinned test suites (test_causal_review_batch109, test_gtdb_coherence_validator, test_is_reclassified_semantics, test_transwell_participants) from hardcoded corpus totals
    status: open
    issue_url: https://github.com/CultureBotAI/CommunityMech/issues/2063
    disposition: Captured during Cycle 2 Stage 1 (add_records); scheduled for Cycle 2 Stage 6 (infrastructure).
```
<!-- mech-infra-tasks:end -->

## Tasks

### `communitymech-infra-0001` — Edge-level causal evidence slot and corpus-count test decoupling

- **Origin**: `mech-goal-sequence-20261019`, cycle 1, stage 2 (`causal_graphs`)
- **Issue**: https://github.com/CultureBotAI/CommunityMech/issues/2055
- **Observation**:
  1. `InteractionDownstream` in `src/communitymech/schema/communitymech.yaml` defines only `target` and `description`; edge-specific supporting snippets must currently be stored on the parent `EcologicalInteraction.evidence` list and mirrored in `reports/causal_graph_review/decisions/*.yaml`.
  2. `tests/test_community_level_connectivity_credit.py`, `tests/test_causal_review_batch109.py`, and `tests/test_participating_taxa.py` assert exact corpus-wide `COMMUNITY_LEVEL` / `PAIRWISE` node-scope partition integers (`records: 477, with_community_level: 422, mixed: 140, community_level_only: 282, taxa: 1607, credited_solely_by_the_rule: 1310`) and an exact `USERS` filename set, requiring synchronized test updates whenever corpus records or node scopes change.
- **Desired outcome**: Evaluate adding an optional `evidence` slot on `InteractionDownstream` (or formalizing the decision-ledger contract) and refactoring `test_community_level_connectivity_credit.py` / `test_participating_taxa.py` to test the connectivity-credit invariant without brittle hardcoded corpus totals.
- **Resolution**:
  - Formalized the canonical two-tier edge-provenance contract (`EcologicalInteraction.evidence` holds verbatim `EvidenceItem` citations for the source interaction node and its outgoing `InteractionDownstream` edges, while `reports/causal_graph_review/decisions/*.yaml` records edge-specific causal rationale) and enforced it via `tests/test_stage6_infrastructure.py::test_infra_0001_downstream_edge_contract_and_decision_provenance` across all `>= 100` directed `InteractionDownstream` edges in the corpus without introducing redundant duplicate `EvidenceItem` blocks on `InteractionDownstream`.
  - Refactored `tests/test_community_level_connectivity_credit.py` to bound `survey["with_community_level"]` by `survey["records"]` (`0.70 <= with_community_level / records <= 0.98`) and `survey["mixed"]` by `survey["with_community_level"]` (`0.15 <= mixed / with_community_level <= 0.60`), eliminating false-positive ceiling failures when new records are curated while preserving non-vacuous floors and the `0.65 <= share <= 0.90` connectivity-credit guard.
- **Evidence paths**:
  - `src/communitymech/schema/communitymech.yaml`
  - `tests/test_community_level_connectivity_credit.py`
  - `tests/test_stage6_infrastructure.py`
  - `reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml`
- **Priority**: P2
- **Dependencies**: None
- **Status**: `resolved` (`#2055`)

### `communitymech-infra-0002` — `build_sequence_map.py` `CommonTaxon.genes` projection and interaction-node protein linkage

- **Origin**: `mech-goal-sequence-20261019`, cycle 1, stage 3 (`protein_examples`)
- **Issue**: https://github.com/CultureBotAI/CommunityMech/issues/2056
- **Observation**:
  1. `scripts/build_sequence_map.py` (`load_curated_genes()`, lines 626–634) reads `doc.get("functional_genes")`, `fg.get("function")`, and `fg.get("phenotype")` instead of the schema-canonical `CommonTaxon` slots `doc.get("genes")`, `fg.get("product")`, and `fg.get("supports_interaction")`. As a result, `data/embeddings/sequence_map.json` reports `"curated_in_taxa_kb": false` and `"source_taxon_yaml": ""` even for UniProtKB proteins curated in `kb/taxa/*.yaml`.
  2. `EcologicalInteraction` in `src/communitymech/schema/communitymech.yaml` provides `metabolites` and `biological_processes` slots on interaction nodes, whereas gene/protein mediation is represented at the reusable taxon level via `CommonTaxon.genes[].supports_interaction` and `TaxonomicComposition.common_taxon` rather than a direct gene/protein reference slot on `EcologicalInteraction`.
- **Desired outcome**: Update `scripts/build_sequence_map.py` to read `CommonTaxon.genes` (`gene_id`, `gene_symbol`, `locus_tag`, `product`, `supports_interaction`) and evaluate whether `EcologicalInteraction` should optionally reference `CommonTaxon.genes` entries directly.
- **Resolution**:
  - Added `load_curated_genes(taxa_dir=TAXA_DIR)` and updated `_enrich_from_taxa_yaml(proteins, taxa_dir=TAXA_DIR)` in `scripts/build_sequence_map.py` to read both `CommonTaxon.genes` (`gene_id`/`uniprot_id`, `gene_symbol`, `locus_tag`, `product` -> `function`, `supports_interaction` -> `phenotype`, `supports_roles`, `go_terms`, `evidence`/`references`) and legacy `functional_genes`.
  - Evaluated `EcologicalInteraction` protein linkage: `TaxonomicComposition.common_taxon` + `CommonTaxon.genes[].supports_interaction` + `CommonTaxon.genes[].supports_roles` already provides normalized reusable taxon-to-interaction mediation without duplicating UniProtKB annotations across every community record that shares a model strain. Verified projection of all 9 curated UniProtKB entries across `kb/taxa/Shewanella_oneidensis_MR1.yaml` and `kb/taxa/Geobacter_sulfurreducens.yaml` in `tests/test_stage6_infrastructure.py::test_infra_0002_build_sequence_map_projects_commontaxon_genes`.
- **Evidence paths**:
  - `scripts/build_sequence_map.py`
  - `kb/taxa/Shewanella_oneidensis_MR1.yaml`
  - `kb/taxa/Geobacter_sulfurreducens.yaml`
  - `tests/test_stage6_infrastructure.py`
- **Priority**: P2
- **Dependencies**: None
- **Status**: `resolved` (`#2056`)

### `communitymech-infra-0003` — Completeness audit rubric alignment and `data/isolates/` scanner coverage

- **Origin**: `mech-goal-sequence-20261019`, cycle 1, stage 4 (`record_review`)
- **Issue**: https://github.com/CultureBotAI/CommunityMech/issues/2057
- **Observation**:
  1. `scripts/audit_completeness.py` scans only `kb/communities/*.yaml` (omitting `data/isolates/*.yaml`) and uses a binary presence check (e.g., `has_interactions`, `has_taxon_roles`) rather than the proportional 0–100 Completeness Score rubric defined in `.claude/skills/review-yaml-record/SKILL.md`.
  2. `scripts/record_review.py` calls `Path(__file__).resolve()` at module import time (`REPO_ROOT = Path(__file__).resolve().parents[1]`), which raises `PermissionError` under macOS Seatbelt sandboxes that restrict `stat()` on parent `/Users` directories.
- **Desired outcome**: Extend `scripts/audit_completeness.py` to optionally include `data/isolates/*.yaml` and compute the proportional 0–100 Completeness Score alongside the binary checklist, and wrap `Path(__file__).resolve()` in `scripts/record_review.py` with a fallback to `Path(__file__).absolute()` when parent directory traversal is sandbox-restricted.
- **Resolution**:
  - Implemented `scripts/audit_completeness.py` (and updated `scripts/generate_validation_report.py` and `scripts/build_sequence_map.py`) with a Seatbelt-safe `_repo_root()` helper (`Path(__file__).resolve()` falling back to `Path(__file__).absolute()` on `PermissionError`), proportional 0–100 `calculate_completeness(doc)` and `calculate_validation_score(summary)` functions matching `.claude/skills/review-communities/reference/metrics-and-reports.md`, and multi-root auditing across `kb/communities/*.yaml` (473), `data/isolates/*.yaml` (4), and `kb/taxa/*.yaml` (2).
  - Preserved `scripts/record_review.py` byte-identical to its governed CLAW payload as required by `docs/record-review-profile.md` and `tests/test_record_review_contract.py`.
- **Evidence paths**:
  - `scripts/audit_completeness.py`
  - `scripts/generate_validation_report.py`
  - `tests/test_stage6_infrastructure.py`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/review_report.md`
- **Priority**: P3
- **Dependencies**: None
- **Status**: `resolved` (`#2057`)

### `communitymech-infra-0004` — Decouple remaining count-pinned test suites from hardcoded corpus totals

- **Origin**: `mech-goal-sequence-20261019`, cycle 2, stage 1 (`add_records`)
- **Issue**: https://github.com/CultureBotAI/CommunityMech/issues/2063
- **Observation**:
  1. While `communitymech-infra-0001` (`#2055`) decoupled `tests/test_community_level_connectivity_credit.py` from hardcoded corpus counts, four additional test suites still assert exact corpus-wide record and classification counts:
     - `tests/test_causal_review_batch109.py` (`test_corpus_community_level_credit_survey_captures_batch_contribution`): pins exact integers (`records: 477, with_community_level: 424, mixed: 141, community_level_only: 283, taxa: 1623, credited_solely_by_the_rule: 1320`) and an exact `USERS` filename set.
     - `tests/test_gtdb_coherence_validator.py` (`test_corpus_has_zero_incoherent_gtdb_classifications`): pins `report.files_checked == 486`.
     - `tests/test_is_reclassified_semantics.py` (`_CORPUS_TOTAL = 79`): pins the exact corpus-wide count of `is_reclassified` occurrences across `kb/communities/*.yaml`, `kb/taxa/*.yaml`, and `data/isolates/*.yaml`.
     - `tests/test_transwell_participants.py` (`EXPECTED_COMMUNITY_FILES = 477`): pins the exact count of `kb/communities/*.yaml` files.
  2. Every Stage 1 (`add_records`) or Stage 2 (`causal_graphs`) curation batch that adds community/isolate records or `COMMUNITY_LEVEL` interactions must manually bump these four test files.
- **Desired outcome**: Refactor `tests/test_causal_review_batch109.py`, `tests/test_gtdb_coherence_validator.py`, `tests/test_is_reclassified_semantics.py`, and `tests/test_transwell_participants.py` in Stage 6 (`infrastructure`) to derive corpus denominators dynamically from the repository record roots while retaining non-vacuous floors, exact invariant checks (`0` incoherent GTDB blocks, `0` semantic mismatches on `is_reclassified`, exact batch-109 record membership), and ratio guards.
- **Evidence paths**:
  - `tests/test_causal_review_batch109.py`
  - `tests/test_gtdb_coherence_validator.py`
  - `tests/test_is_reclassified_semantics.py`
  - `tests/test_transwell_participants.py`
  - `reports/c2s1_bounded_frontier_discovery_20261023.md`
- **Priority**: P2
- **Dependencies**: None
- **Status**: `open` (`#2063`)


