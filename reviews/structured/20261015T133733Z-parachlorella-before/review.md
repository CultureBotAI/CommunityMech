# Parachlorella assay scope before

- Review: 20261015T133733Z-parachlorella-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-15T13:37:33.174651Z
- Finished UTC: 2026-10-15T13:37:33.174651Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Correct existing assay attribution while preserving unresolved mechanistic scope.

## Scope And Provenance

Four existing graph nodes and two edges; full record read but non-graph metadata not certified.

Selection: Source follow-up to issue1681 and new bounded correction2020
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a6feb9194b199d255148557d6c5b3c3e129631f0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | Parachlorella-Saccharomyces coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Separate supplementary assays | unavailable | True | CommunityMech:000295 | S1/S2/S3 and TableS1 were not inspected; issue1681 remains open. |

## Scientific And Domain Assessments

### Proposed Reciprocal Oxygen and Carbon Dioxide Exchange

graph: unknown. Targets: CommunityMech:000295.

Retain gas exchange as proposed mediation; main text does not isolate it with direct flux/perturbation assays.

ecological_interactions[0]; PMID42217804. Methods2.1-2.4; Results3.2-3.5. No strain identity replacement or taxonomic recertification.

### Yeast support of microalgal growth and lipid accumulation

graph: concern. Targets: CommunityMech:000295.

Retain observed yeast-associated algal growth; nutrient competition remains the authors' interpretation of lipid response.

ecological_interactions[1]; PMID42217804. Methods2.1-2.4; Results3.2-3.5. No strain identity replacement or taxonomic recertification.

### Proposed EPS-Derived Metabolic Support of Yeast

graph: unknown. Targets: CommunityMech:000295.

Retain viable yeast and physical observations without inferring EPS uptake or necessity.

ecological_interactions[2]; PMID42217804. Methods2.1-2.4; Results3.2-3.5. No strain identity replacement or taxonomic recertification.

### Fourfold Coculture Biomass and Lipid Increase

graph: concern. Targets: CommunityMech:000295.

Distinguish day12 algal cell counts from day14 normalized bulk lipid fluorescence, with matched-medium control and conflicting source numbers.

ecological_interactions[3]; PMID42217804. Methods2.1-2.4; Results3.2-3.5. No strain identity replacement or taxonomic recertification.

### Retained incoming link 0

graph: unknown. Targets: CommunityMech:000295.

Retain proposed gas mediation.

ecological_interactions[0].downstream[0] -&gt; Fourfold Coculture Biomass and Lipid Increase. HYPOTHESIZED - Photosynthetic oxygen and respiratory carbon dioxide exchange could support coculture productivity. The accessible abstract does not isolate the contribution of gas exchange to the observed fourfold biomass/lipid increase.

### Retained incoming link 1

graph: supported. Targets: CommunityMech:000295.

Retain partial physiological contribution; total fold change includes medium enrichment.

ecological_interactions[1].downstream[0] -&gt; Fourfold Coculture Biomass and Lipid Increase. PARTIAL - Yeast-associated maintenance of algal growth and nutrient-competition-associated lipid accumulation provide the reported physiological contribution to higher coculture biomass/lipid production. This does not apportion the fourfold endpoint among growth support, gas exchange and other mechanisms.

## Findings

### assay-scope: Growth and lipid endpoint conflation

major / open / confirmed; issue key: parachlorella-assay-scope.

Existing endpoint conflates algal cell counts with bulk fluorescence and obscures the matched-medium comparator. Correct wording/evidence without adding topology.

### remaining-research: Supplement and physical-adhesion structure review remains incomplete

major / open / confirmed; issue key: parachlorella-remaining-research.

Main article access resolves the prior main-text barrier, but not separate supplements, dye/fold reporting conflicts, mediator specificity or provider-required new structure.

## Recommended Actions And Acceptance Checks

### follow-assay-scope

Existing endpoint conflates algal cell counts with bulk fluorescence and obscures the matched-medium comparator. Correct wording/evidence without adding topology.

- Attach exact primary evidence at the affected claims.
- Preserve source conflicts and remaining research limits.
- Run required provider workflow before any new topology.

### follow-remaining-research

Main article access resolves the prior main-text barrier, but not separate supplements, dye/fold reporting conflicts, mediator specificity or provider-required new structure.

- Attach exact primary evidence at the affected claims.
- Preserve source conflicts and remaining research limits.
- Run required provider workflow before any new topology.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | doi:10.1016/j.biortech.2026.135004; HAL PDF; Methods2.1-2.4, Results3.1-3.5, Fig3,4,6; source-access.md gives PDF hash and inspection scope | supports | Species-resolved algal counts differ from bulk relative Nile Red signal; medium control and source reporting conflicts must be retained. |
| record | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml; Whole record read; four graph nodes and two downstream links assessed | context_only | Existing topology retained; no new physical-adhesion node or independent approval. |
| access | reports/causal_graph_review/20261015-parachlorella-assays/source-access.md; Dated public access, figure scope and search exclusions | context_only | Primary main article available; separate supplements and raw data uninspected. |

## Limits And Additional Notes

- Separate supplements and raw data uninspected; no independent approval.
- No new topology or provider report; remaining research is not completed by structural validation.
- Whole-record native completeness/validation-quality scores not assessed by this graph-only review; node/edge coverage denominators are 4 and 2.
- Non-graph metadata issue1683 is outside this correction, preserved and not disposed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T133733Z-parachlorella-before
kind: record
repository: CultureBotAI/CommunityMech
title: Parachlorella assay scope before
started_at: '2026-10-15T13:37:33.174651Z'
finished_at: '2026-10-15T13:37:33.174651Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Source-based adversarial review by the implementing agent; not
    independent approval.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
native_verdict: needs_research
scientific_review: true
source:
  git_revision: a6feb9194b199d255148557d6c5b3c3e129631f0
  state: working_tree
  inputs:
  - path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    sha256: ee3166c701c928154cb1f46337d3d43a5ee56946d75f93fcd6d4ac8ecb3f8b82
    role: target
  - path: references_cache/PMID_42217804.md
    sha256: 74b5d91bfe086e1436de49647950ad27677571093e914e94e25964191d7ac937
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/source-access.md
    sha256: 4458e44a9d057ceb26d85a81a96178c7a02e2f99339f3ddc99a01abafe8d8aa1
    role: context
  - path: reports/causal_graph_review/decisions/20261007-four-records-batch82.yaml
    sha256: 287d391e90ad2e832c8cf57a63e6db79adfd6a73fa59a670dc6441c1466cea58
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
targets:
- target_id: CommunityMech:000295
  path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  label: Parachlorella-Saccharomyces coculture
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
summary: Correct existing assay attribution while preserving unresolved mechanistic
  scope.
scope:
  description: Four existing graph nodes and two edges; full record read but non-graph
    metadata not certified.
  selection: Source follow-up to issue1681 and new bounded correction2020
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000295
checks:
- check_id: supplements
  name: Separate supplementary assays
  status: unavailable
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - access
  summary: S1/S2/S3 and TableS1 were not inspected; issue1681 remains open.
evidence:
- evidence_id: primary
  kind: primary_source
  reference: doi:10.1016/j.biortech.2026.135004
  locator: HAL PDF; Methods2.1-2.4, Results3.1-3.5, Fig3,4,6; source-access.md gives
    PDF hash and inspection scope
  accessed_at: '2026-10-15T13:37:33.174651Z'
  support: supports
  summary: Species-resolved algal counts differ from bulk relative Nile Red signal;
    medium control and source reporting conflicts must be retained.
- evidence_id: record
  kind: record_content
  reference: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  locator: Whole record read; four graph nodes and two downstream links assessed
  accessed_at: '2026-10-15T13:37:33.174651Z'
  support: context_only
  summary: Existing topology retained; no new physical-adhesion node or independent
    approval.
- evidence_id: access
  kind: search
  reference: reports/causal_graph_review/20261015-parachlorella-assays/source-access.md
  locator: Dated public access, figure scope and search exclusions
  accessed_at: '2026-10-15T13:37:33.174651Z'
  support: context_only
  summary: Primary main article available; separate supplements and raw data uninspected.
  search_scope: Ignored/hidden-inclusive scoped local search; GitHub all-state Parachlorella
    title/body search.
assessments:
- assessment_id: node-0
  area: graph
  topic: Proposed Reciprocal Oxygen and Carbon Dioxide Exchange
  outcome: unknown
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  - access
  summary: Retain gas exchange as proposed mediation; main text does not isolate it
    with direct flux/perturbation assays.
  details: ecological_interactions[0]; PMID42217804. Methods2.1-2.4; Results3.2-3.5.
    No strain identity replacement or taxonomic recertification.
  dimensions:
  - name: experimental-system
    value: P. kessleri UTEX2229 + S. cerevisiae BY4741; engineered coculture in glucose/peptone-supplemented
      BBM
    definition: Primary-source assay scope, not natural-community generalization
    evidence_ids:
    - primary
- assessment_id: node-1
  area: graph
  topic: Yeast support of microalgal growth and lipid accumulation
  outcome: concern
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  - access
  summary: Retain observed yeast-associated algal growth; nutrient competition remains
    the authors' interpretation of lipid response.
  details: ecological_interactions[1]; PMID42217804. Methods2.1-2.4; Results3.2-3.5.
    No strain identity replacement or taxonomic recertification.
  dimensions:
  - name: experimental-system
    value: P. kessleri UTEX2229 + S. cerevisiae BY4741; engineered coculture in glucose/peptone-supplemented
      BBM
    definition: Primary-source assay scope, not natural-community generalization
    evidence_ids:
    - primary
- assessment_id: node-2
  area: graph
  topic: Proposed EPS-Derived Metabolic Support of Yeast
  outcome: unknown
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  - access
  summary: Retain viable yeast and physical observations without inferring EPS uptake
    or necessity.
  details: ecological_interactions[2]; PMID42217804. Methods2.1-2.4; Results3.2-3.5.
    No strain identity replacement or taxonomic recertification.
  dimensions:
  - name: experimental-system
    value: P. kessleri UTEX2229 + S. cerevisiae BY4741; engineered coculture in glucose/peptone-supplemented
      BBM
    definition: Primary-source assay scope, not natural-community generalization
    evidence_ids:
    - primary
- assessment_id: node-3
  area: graph
  topic: Fourfold Coculture Biomass and Lipid Increase
  outcome: concern
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  - access
  summary: Distinguish day12 algal cell counts from day14 normalized bulk lipid fluorescence,
    with matched-medium control and conflicting source numbers.
  details: ecological_interactions[3]; PMID42217804. Methods2.1-2.4; Results3.2-3.5.
    No strain identity replacement or taxonomic recertification.
  dimensions:
  - name: experimental-system
    value: P. kessleri UTEX2229 + S. cerevisiae BY4741; engineered coculture in glucose/peptone-supplemented
      BBM
    definition: Primary-source assay scope, not natural-community generalization
    evidence_ids:
    - primary
- assessment_id: edge-0
  area: graph
  topic: Retained incoming link 0
  outcome: unknown
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  summary: Retain proposed gas mediation.
  details: ecological_interactions[0].downstream[0] -> Fourfold Coculture Biomass
    and Lipid Increase. HYPOTHESIZED - Photosynthetic oxygen and respiratory carbon
    dioxide exchange could support coculture productivity. The accessible abstract
    does not isolate the contribution of gas exchange to the observed fourfold biomass/lipid
    increase.
- assessment_id: edge-1
  area: graph
  topic: Retained incoming link 1
  outcome: supported
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  summary: Retain partial physiological contribution; total fold change includes medium
    enrichment.
  details: ecological_interactions[1].downstream[0] -> Fourfold Coculture Biomass
    and Lipid Increase. PARTIAL - Yeast-associated maintenance of algal growth and
    nutrient-competition-associated lipid accumulation provide the reported physiological
    contribution to higher coculture biomass/lipid production. This does not apportion
    the fourfold endpoint among growth support, gas exchange and other mechanisms.
findings:
- finding_id: assay-scope
  issue_key: parachlorella-assay-scope
  title: Growth and lipid endpoint conflation
  description: Existing endpoint conflates algal cell counts with bulk fluorescence
    and obscures the matched-medium comparator. Correct wording/evidence without adding
    topology.
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  target_ids:
  - CommunityMech:000295
  field_paths:
  - ecological_interactions
  - discussions
  evidence_ids:
  - primary
  - record
  - access
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  rule_id: CLAUDE.claim-level-evidence
  native_severity: P2
  normalization_reason: Assay attribution and mediator certainty affect scientific
    interpretation.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2020
- finding_id: remaining-research
  issue_key: parachlorella-remaining-research
  title: Supplement and physical-adhesion structure review remains incomplete
  description: Main article access resolves the prior main-text barrier, but not separate
    supplements, dye/fold reporting conflicts, mediator specificity or provider-required
    new structure.
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  target_ids:
  - CommunityMech:000295
  field_paths:
  - ecological_interactions
  - discussions
  evidence_ids:
  - primary
  - record
  - access
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  rule_id: CLAUDE.claim-level-evidence
  native_severity: P2
  normalization_reason: Assay attribution and mediator certainty affect scientific
    interpretation.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
actions:
- action_id: follow-assay-scope
  finding_ids:
  - assay-scope
  target_ids:
  - CommunityMech:000295
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  description: Existing endpoint conflates algal cell counts with bulk fluorescence
    and obscures the matched-medium comparator. Correct wording/evidence without adding
    topology.
  acceptance_checks:
  - Attach exact primary evidence at the affected claims.
  - Preserve source conflicts and remaining research limits.
  - Run required provider workflow before any new topology.
- action_id: follow-remaining-research
  finding_ids:
  - remaining-research
  target_ids:
  - CommunityMech:000295
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  description: Main article access resolves the prior main-text barrier, but not separate
    supplements, dye/fold reporting conflicts, mediator specificity or provider-required
    new structure.
  acceptance_checks:
  - Attach exact primary evidence at the affected claims.
  - Preserve source conflicts and remaining research limits.
  - Run required provider workflow before any new topology.
limitations:
- Separate supplements and raw data uninspected; no independent approval.
- No new topology or provider report; remaining research is not completed by structural
  validation.
- Whole-record native completeness/validation-quality scores not assessed by this
  graph-only review; node/edge coverage denominators are 4 and 2.
- Non-graph metadata issue1683 is outside this correction, preserved and not disposed.
```
