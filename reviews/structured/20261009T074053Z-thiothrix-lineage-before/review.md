# Thiothrix active-lineage nomenclature before repair

- Review: 20261009T074053Z-thiothrix-lineage-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-09T07:40:53Z
- Finished UTC: 2026-10-09T07:40:53Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

Scoped adversarial integration review of active nomenclature and source-preservation boundaries; not a completed scientific review of the community.

## Scope And Provenance

One active-lineage field and its provenance/evidence boundary, with corpus hierarchy validation.

Selection: Exact record identified by the failing CI assertion.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 57b17a7c3116feae7b6d7deefa9c54680c0ae816.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml # taxonomy[0].taxon_term.gtdb_classification | maintained | Thiothrix active GTDB lineage |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Original full-suite hierarchy regression | failed | True | CommunityMech:000222 | Exact-head CI failed one corpus hierarchy test: 1 failed, 4667 passed, 87 skipped, 8 deselected. Locally reproduced before editing. |

## Scientific And Domain Assessments

### Active hierarchy versus verbatim evidence

nomenclature: concern. Targets: CommunityMech:000222.

Historical source spelling must remain verbatim; normalized active taxonomy must remain coherent without claiming a reclassified genome.

## Findings

### lineage-phylum: Historical phylum spelling conflicts with the active corpus hierarchy

major / open / confirmed; issue key: communitymech-1978-lineage-phylum.

Batch127 copied historical source nomenclature into the active GTDB lineage, causing a corpus-level hierarchy conflict.

## Recommended Actions And Acceptance Checks

### normalize-active-name

Normalize only the active phylum name; preserve source quotations, genus identity and all unresolved biological boundaries.

- Reproduce the original failure.
- Pass the unchanged corpus hierarchy validator.
- Retain original source rows, quotations, caches and graph; test mutation failures.
- Append history and a successor ledger, regenerate the page and review the exact pushed head.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ci | https://github.com/CultureBotAI/CommunityMech/actions/runs/37845443207; tests/test_gtdb_lineage_tree.py::test_the_committed_kb_is_a_consistent_hierarchy | supports | Original CI detects Gammaproteobacteria under both Proteobacteria and Pseudomonadota; focused predecessor validation omitted this corpus test. |
| record | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml; taxonomy[0].taxon_term.gtdb_classification.gtdb_lineage | supports | The active lineage and three historical source quotations have distinct roles. Only the active phylum spelling requires normalization. |
| source-row | PMID:38273328; Table S4, row104, ALUMROCK_MS4_Thiothrix_nivea-related_50_537_curated | supports | The retained manifest uses Proteobacteria, identifies Thiothrix genus and leaves species blank; neither source values nor participant identity should be rewritten. |
| gtdb | https://forum.gtdb.ecogenomic.org/t/announcing-gtdb-r08-rs214/456; Release changes: phylum names | supports | The GTDB maintainer announcement documents adoption of published phylum names including Pseudomonadota. The resource paper doi:10.1093/nar/gkaf1040 discusses the Proteobacteria rename. This supports nomenclature, not a fresh genome placement. |

## Limits And Additional Notes

- No new biological identities, participants, nodes, arrows, mechanistic claims, or genome-count votes are certified.
- Issue1841 remains open; the record stays needs_research. Complete source-body and study-genome reclassification were not repeated.
- A completed scoped diagnostic review is not independent approval, whole-record scientific certification, a passing new CI result, or a merged PR.
- Saved using the canonical record-review helper and schema at main commit4bad95490b1d03a2dc9bbdd7854e124d00daac57. Legacy ledgers are not migrated or rewritten.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T074053Z-thiothrix-lineage-before
kind: record
repository: CultureBotAI/CommunityMech
title: Thiothrix active-lineage nomenclature before repair
started_at: '2026-10-09T07:40:53Z'
finished_at: '2026-10-09T07:40:53Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Same agent assessed and repaired the change; not independent
    approval.
skill: communitymech-causal-graphs
completion: completed
verdict: needs_curation
scientific_review: false
summary: Scoped adversarial integration review of active nomenclature and source-preservation
  boundaries; not a completed scientific review of the community.
source:
  git_revision: 57b17a7c3116feae7b6d7deefa9c54680c0ae816
  state: git_commit
  inputs:
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 94a4a5855730de3a7f9aea67e694040d9ae7337e6c0d8072438a2d46a8670c87
    role: target
  - path: reports/causal_graph_review/decisions/20261008-spring-identity-batch127.yaml
    sha256: 9166b3bb643162691aeee39ebb7b98b9ad22ef63505fa3e9cc5654be228519ef
    role: context
  - path: reports/causal_graph_review/sources/20261008-spring-supplements-batch127.json
    sha256: e95387a98bd9afe49b2c51830fa02f05002d8936985d739efda40f5e7ccd7505
    role: context
  - path: src/communitymech/validators/gtdb_lineage_tree.py
    sha256: 1bf2f371b064f83bcba1589d05151fe3443fe826538e5a4ab6b7c3c3bde8fef0
    role: context
  - path: tests/test_gtdb_lineage_tree.py
    sha256: 091ca38968ebc844ab02491c767e4b1cd42a90f1bd71be2e931ac4ba0c845d57
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: 99079e7712d0c6b5eef0f278822a6b04fdb9a3a55b446e1f73f0752e4e626d04
    role: context
scope:
  description: One active-lineage field and its provenance/evidence boundary, with
    corpus hierarchy validation.
  selection: Exact record identified by the failing CI assertion.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000222
targets:
- target_id: CommunityMech:000222
  path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  selector: taxonomy[0].taxon_term.gtdb_classification
  label: Thiothrix active GTDB lineage
  record_class: MicrobialCommunity
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    role: maintained taxon grounding
checks:
- check_id: ci-hierarchy
  name: Original full-suite hierarchy regression
  status: failed
  required: true
  summary: 'Exact-head CI failed one corpus hierarchy test: 1 failed, 4667 passed,
    87 skipped, 8 deselected. Locally reproduced before editing.'
  target_ids:
  - CommunityMech:000222
  evidence_ids:
  - ci
  - record
  scope_note: Failed historical commit, not a pending new CI run.
evidence:
- evidence_id: ci
  kind: validation
  reference: https://github.com/CultureBotAI/CommunityMech/actions/runs/37845443207
  locator: tests/test_gtdb_lineage_tree.py::test_the_committed_kb_is_a_consistent_hierarchy
  accessed_at: '2026-10-09T07:40:53Z'
  support: supports
  summary: Original CI detects Gammaproteobacteria under both Proteobacteria and Pseudomonadota;
    focused predecessor validation omitted this corpus test.
  snapshot_sha256: 94d8ebd1c08357a0218be412a56a780321b1d232d125b855adfe432433c6c733
- evidence_id: record
  kind: record_content
  reference: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  locator: taxonomy[0].taxon_term.gtdb_classification.gtdb_lineage
  accessed_at: '2026-10-09T07:40:53Z'
  support: supports
  summary: The active lineage and three historical source quotations have distinct
    roles. Only the active phylum spelling requires normalization.
- evidence_id: source-row
  kind: primary_source
  reference: PMID:38273328
  locator: Table S4, row104, ALUMROCK_MS4_Thiothrix_nivea-related_50_537_curated
  accessed_at: '2026-10-09T07:40:53Z'
  support: supports
  summary: The retained manifest uses Proteobacteria, identifies Thiothrix genus and
    leaves species blank; neither source values nor participant identity should be
    rewritten.
  snapshot_sha256: e95387a98bd9afe49b2c51830fa02f05002d8936985d739efda40f5e7ccd7505
- evidence_id: gtdb
  kind: authority
  reference: https://forum.gtdb.ecogenomic.org/t/announcing-gtdb-r08-rs214/456
  locator: 'Release changes: phylum names'
  accessed_at: '2026-10-09T07:40:53Z'
  support: supports
  summary: The GTDB maintainer announcement documents adoption of published phylum
    names including Pseudomonadota. The resource paper doi:10.1093/nar/gkaf1040 discusses
    the Proteobacteria rename. This supports nomenclature, not a fresh genome placement.
assessments:
- assessment_id: active-vs-source
  area: nomenclature
  topic: Active hierarchy versus verbatim evidence
  outcome: concern
  summary: Historical source spelling must remain verbatim; normalized active taxonomy
    must remain coherent without claiming a reclassified genome.
  target_ids:
  - CommunityMech:000222
  evidence_ids:
  - record
  - source-row
  - gtdb
  - ci
findings:
- finding_id: lineage-phylum
  issue_key: communitymech-1978-lineage-phylum
  category: nomenclature
  severity: major
  status: open
  certainty: confirmed
  title: Historical phylum spelling conflicts with the active corpus hierarchy
  description: Batch127 copied historical source nomenclature into the active GTDB
    lineage, causing a corpus-level hierarchy conflict.
  target_ids:
  - CommunityMech:000222
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.gtdb_lineage
  evidence_ids:
  - ci
  - record
  - source-row
  - gtdb
  rule_id: gtdb-single-parent-hierarchy
  native_severity: P2
  normalization_reason: Major integration defect blocks required CI while the supported
    genus identity remains intact.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    role: maintained taxon grounding
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1978
actions:
- action_id: normalize-active-name
  description: Normalize only the active phylum name; preserve source quotations,
    genus identity and all unresolved biological boundaries.
  finding_ids:
  - lineage-phylum
  target_ids:
  - CommunityMech:000222
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    role: maintained taxon grounding
  acceptance_checks:
  - Reproduce the original failure.
  - Pass the unchanged corpus hierarchy validator.
  - Retain original source rows, quotations, caches and graph; test mutation failures.
  - Append history and a successor ledger, regenerate the page and review the exact
    pushed head.
limitations:
- No new biological identities, participants, nodes, arrows, mechanistic claims, or
  genome-count votes are certified.
- Issue1841 remains open; the record stays needs_research. Complete source-body and
  study-genome reclassification were not repeated.
- A completed scoped diagnostic review is not independent approval, whole-record scientific
  certification, a passing new CI result, or a merged PR.
notes:
- Saved using the canonical record-review helper and schema at main commit4bad95490b1d03a2dc9bbdd7854e124d00daac57.
  Legacy ledgers are not migrated or rewritten.
links:
- https://github.com/CultureBotAI/CommunityMech/pull/1975
- https://github.com/CultureBotAI/CommunityMech/issues/1841
tags:
- causal-graphs
- batch128
- self-review
```
