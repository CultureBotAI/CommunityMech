# Stage 6 (`infrastructure`) — Dependency-Aware Implementation Plan

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `1` (`cycle-000001`)
- **Stage**: `6` (`infrastructure`)
- **Revision**: `1` (`revision-0001`)
- **Source Revision (`main`)**: `e117e3d37c65bfad2e04af53ab34e1325d8d7f98`
- **Frozen Scope Timestamp (`scope_frozen_at`)**: `2026-10-22T01:34:25Z`
- **Frozen `INFRA_TASKS.md` Digest (`sha256`)**: `364efb1bac9f8140bffebe2923c871e30dd6a2186765083f11f371d2698b7246`

---

## 1. Frozen Intake Scope & Issue Mapping

At `2026-10-22T01:34:25Z`, `INFRA_TASKS.md` was frozen at exact SHA-256 `364efb1bac9f8140bffebe2923c871e30dd6a2186765083f11f371d2698b7246` (`reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-06/revision-0001/infra_snapshot.md`). It contains 3 tasks accumulated across Stages 2, 3, and 4 of Cycle 1:

| Task ID | Originating Stage | Priority | Dependencies | GitHub Issue | Planned Disposition |
|---|---|---|---|---|---|
| `communitymech-infra-0001` | Stage 2 (`causal_graphs`) | P2 | None | [#2055](https://github.com/CultureBotAI/CommunityMech/issues/2055) | `resolved` |
| `communitymech-infra-0002` | Stage 3 (`protein_examples`) | P2 | None | [#2056](https://github.com/CultureBotAI/CommunityMech/issues/2056) | `resolved` |
| `communitymech-infra-0003` | Stage 4 (`record_review`) | P3 | None | [#2057](https://github.com/CultureBotAI/CommunityMech/issues/2057) | `resolved` |

All three tasks are orthogonal and have no blocking upstream dependencies, allowing all 3 to be implemented, validated, and resolved in Stage 6 (`carry_forward_ids: []`).

---

## 2. Dependency-Ordered Implementation Design & Acceptance Criteria

### 2.1 `communitymech-infra-0001` ([#2055](https://github.com/CultureBotAI/CommunityMech/issues/2055))
- **Problem Statement**:
  1. `tests/test_community_level_connectivity_credit.py` enforced hardcoded corpus-count upper bounds (`130 <= survey["with_community_level"] <= 422` and `35 <= survey["mixed"] <= 140`) that sat at the exact current corpus ceiling (`422` and `140`), causing any newly curated `COMMUNITY_LEVEL` or mixed-scope record to fail CI even when the underlying connectivity-credit share invariant (`0.65 <= share <= 0.90`) and `0` mixed-scope miscredits held.
  2. `InteractionDownstream` in `src/communitymech/schema/communitymech.yaml` defines `target` and `description` while primary literature `EvidenceItem` blocks live on the parent `EcologicalInteraction.evidence` slot and edge-level rationale is recorded in `reports/causal_graph_review/decisions/*.yaml`.
- **Design Decision & Implementation**:
  1. Retain `InteractionDownstream` (`target`, `description`) in `src/communitymech/schema/communitymech.yaml` without duplicating `EvidenceItem` arrays on downstream edges; instead, codify and enforce the two-tier edge-provenance contract (every `EcologicalInteraction` with `downstream` edges must carry primary `EvidenceItem` entries on the parent node, and every `InteractionDownstream.target` must resolve to an in-record `EcologicalInteraction.name`) in `tests/test_stage6_infrastructure.py::test_infra_0001_downstream_edge_contract_and_decision_provenance`.
  2. Refactor `tests/test_community_level_connectivity_credit.py` so `survey["with_community_level"]` is bounded above by `survey["records"]` (with proportion guard `0.70 <= with_community_level / records <= 0.98`) and `survey["mixed"]` is bounded above by `survey["with_community_level"]` (with proportion guard `0.15 <= mixed / with_community_level <= 0.60`), preserving the non-vacuous floors (`>= 130` and `>= 35`) and the headline share invariant (`0.65 <= share <= 0.90`).
- **Acceptance Criteria**:
  - `pytest tests/test_community_level_connectivity_credit.py tests/test_causal_review_batch109.py tests/test_participating_taxa.py tests/test_stage6_infrastructure.py` passes with 0 failures.

### 2.2 `communitymech-infra-0002` ([#2056](https://github.com/CultureBotAI/CommunityMech/issues/2056))
- **Problem Statement**:
  1. `scripts/build_sequence_map.py::_enrich_from_taxa_yaml` read only the legacy `doc.get("functional_genes")` key (`function`, `phenotype`) and skipped the schema-canonical `CommonTaxon.genes` slot (`product`, `supports_interaction`, `gene_symbol`, `locus_tag`, `supports_roles`, `go_terms`, `evidence`, `references`) populated in `kb/taxa/Shewanella_oneidensis_MR1.yaml` and `kb/taxa/Geobacter_sulfurreducens.yaml`.
  2. Evaluated whether `EcologicalInteraction` needs a direct gene/protein slot vs. taxon-level `TaxonomicComposition.common_taxon` + `CommonTaxon.genes[].supports_interaction`.
- **Design Decision & Implementation**:
  1. Add `load_curated_genes(taxa_dir=TAXA_DIR)` and update `_enrich_from_taxa_yaml(proteins, taxa_dir=TAXA_DIR)` in `scripts/build_sequence_map.py` to support both canonical `CommonTaxon.genes` and legacy `functional_genes`, mapping `product -> function`, `supports_interaction -> phenotype`, and preserving `gene_symbol`, `locus_tag`, `supports_roles`, `go_terms`, `references`, and `source_taxon_yaml`.
  2. Keep gene/protein mediation normalized on `CommonTaxon.genes` (`supports_roles` and `supports_interaction`) linked via `TaxonomicComposition.common_taxon`, avoiding redundant per-community duplication of UniProtKB accessions across communities sharing the same model organism.
- **Acceptance Criteria**:
  - `load_curated_genes()` and `_enrich_from_taxa_yaml()` project all 9 curated UniProtKB accessions across `kb/taxa/Shewanella_oneidensis_MR1.yaml` (`Q8EG33`, `Q8EG34`, `Q8EG35`, `Q8EG32`, `Q8E945`) and `kb/taxa/Geobacter_sulfurreducens.yaml` (`Q74A86`, `Q749X9`, `Q74A90`, `Q74BW5`), verified by `tests/test_stage6_infrastructure.py::test_infra_0002_build_sequence_map_projects_commontaxon_genes`.

### 2.3 `communitymech-infra-0003` ([#2057](https://github.com/CultureBotAI/CommunityMech/issues/2057))
- **Problem Statement**:
  1. `.claude/skills/review-communities/SKILL.md` and `.claude/skills/review-communities/reference/metrics-and-reports.md` reference `scripts/audit_completeness.py` and the proportional 0–100 `calculate_completeness` / `calculate_validation_score` functions, which were not implemented as a standalone script, and `scripts/generate_validation_report.py` scanned only `kb/communities/*.yaml` with binary field presence.
  2. Under macOS Seatbelt sandboxes where `stat` on parent directories above the workspace root is restricted, `Path(__file__).resolve()` can raise `PermissionError` unless guarded by a fallback to `Path(__file__).absolute()`.
- **Design Decision & Implementation**:
  1. Create `scripts/audit_completeness.py` with Seatbelt-safe `_repo_root()`, `all_required_fields_present(doc)`, `calculate_completeness(doc)`, `calculate_validation_score(summary)`, `audit_record(path)`, `audit_corpus(...)`, and CLI options (`--format summary|tsv|json`, `--communities-only`, `--include-taxa`, `--out`) scanning `kb/communities/*.yaml` (473), `data/isolates/*.yaml` (4), and optionally `kb/taxa/*.yaml` (2).
  2. Update `scripts/generate_validation_report.py` (`count_community_stats` and `main`) to compute `completeness_score` via `calculate_completeness` and use Seatbelt-safe `repo_root` resolution.
  3. Preserve `scripts/record_review.py` byte-identical to its governed CLAW payload as required by `docs/record-review-profile.md` (line 98: *"The shared schema, helper, documentation and contract test remain byte-identical CLAW payloads"*) and enforced by `tests/test_record_review_contract.py`.
- **Acceptance Criteria**:
  - `python scripts/audit_completeness.py --include-taxa` audits all `479` eligible records (`473` communities + `4` isolates + `2` taxa) with `0` errors.
  - `pytest tests/test_stage6_infrastructure.py tests/test_writers_leave_a_trace.py tests/test_record_review_contract.py` passes with 0 failures.
