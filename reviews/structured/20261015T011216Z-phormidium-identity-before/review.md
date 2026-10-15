# Phormidium graph participant identity before repair

- Review: 20261015T011216Z-phormidium-identity-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-15T01:09:00.508795Z
- Finished UTC: 2026-10-15T01:12:16.472646Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Confirmed wrong-organism ID in the cyanobacterial member and four graph references, hidden by two stale exact-pair waivers. Species-level replacement is supported; graph extension and broader non-graph claims remain unresolved.

## Scope And Provenance

One member identity, its four graph references, and two exact-pair policy exceptions.

Selection: Confirmed issue #2009 during Phormidium graph research.
Coverage: partial; 2 reviewed / 462 in the declared population.
Source: git_commit at Git base faba89b8c65aec6a0436fe2d4b0c960ceda84372.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | Phormidium alkaline consortium |
| id-label-policy | conf/id_label_targets.yaml | maintained | ID-label correspondence policy |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Source/ontology identity reconciliation | passed | True | CommunityMech:000054, id-label-policy | Read primary identity context and live/local taxonomy statements; legacy ID denotes another organism. |

## Scientific And Domain Assessments

### Cyanobacterial participant identity and source-population scope

identity: concern. Targets: CommunityMech:000054.

Wrong organism is attached to four graph references. Preserve source wording and population scope while selecting the canonical species ID.

### Exact-pair exceptions hide the wrong organism

grounding: concern. Targets: id-label-policy.

The two exceptions must be removed together with the supported identity repair, not replaced by a broader waiver.

## Findings

### wrong-cyanobacterial-id: Cyanobacterial graph references point to an unrelated organism

blocker / open / confirmed; issue key: communitymech-2009-phormidium-identity.

1807132 is an alternative ID for Syntrophocurvum, not Phormidium/Sodalinema. Five maintained fields and two policy waivers require coordinated repair.

## Recommended Actions And Acceptance Checks

### repair-identity

Correct the five species references and remove the two stale waivers; retain graph structure and source evidence.

- Canonical species label resolves without an exception.
- No unsupported single-strain assertion or new graph topology.
- Guarded write, history, derived artifacts, native validators and current-hash review lineage verified.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ncbi | reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/ncbi-taxonomy.xml; Taxon 2293317/AkaTaxIds, 3723519/name and synonym, 2839084/parent and rank | refutes | Legacy 1807132 resolves to a Bacillota/Clostridia species, not the cyanobacterium. The source name is a synonym of cyanobacterial species 3723519; PBR-2020 is its child strain 2839084. |
| oak | reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/oak-taxonomy.json; Selected statements; ontology version 2026-07-12 | supports | The installed ontology independently represents the same legacy alias, species canonical label and source-name synonym; neither replacement candidate needs a missing-term waiver in this snapshot. |
| paper2022 | doi:10.3389/fmicb.2022.780346; Results, community composition; five metagenomes from different cultures/time points; distinct OSCR comparison | supports | The named Phormidium population is the only cyanobacterium and the most abundant member. The combined record spans multiple conditions and sampling times, not one isolated strain. |
| paper2021 | PMID:34877483; https://pmc.ncbi.nlm.nih.gov/articles/PMC8633866/ ; identity/strain Results p0085-p0110, conclusion p0205, limitations p0215, data availability p0255 | supports | Species naming, persistent strain diversity and the PBR-2020 reference-genome accession support species-level grounding while retaining the publication name; one reference strain must not absorb all conditions. |
| canonical | kb/communities/Phormidium_Alkaline_Consortium.yaml; taxonomy[0] and all four cyanobacterial graph participant references | supports | Five term objects use the unrelated legacy ID. The two policy exceptions explicitly permit that wrong ID/name pair. |

## Limits And Additional Notes

- Scoped identity review, not whole-record certification or corpus completion.
- The 2021 raw article remains an attributed local read-only copy; its hash/read scope is in the source manifest, not republished.
- Existing non-graph claims and other member groundings are not recertified. No native whole-record completeness/quality score is assigned.
- GTDB assignment remains unresolved; no lineage is invented. No Edison submission, paid research or new graph structure.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T011216Z-phormidium-identity-before
kind: repository
repository: CultureBotAI/CommunityMech
title: Phormidium graph participant identity before repair
started_at: '2026-10-15T01:09:00.508795Z'
finished_at: '2026-10-15T01:12:16.472646Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Implementing-agent scientific source review, not independent
    approval.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
scientific_review: true
source:
  git_revision: faba89b8c65aec6a0436fe2d4b0c960ceda84372
  state: git_commit
  inputs:
  - path: conf/id_label_targets.yaml
    sha256: 1821ee1958c36068c2f6aa19ddea8a7d3d0be756577c22a8091ed6278f4d259f
    role: target
  - path: conf/record_review.yaml
    sha256: 8cbd8f9d209f78de47a8c35091e43bf1dadbe41ee07492c7860b6d4be30112a8
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    sha256: 5bd6ec7333293e123e4b68212ddd64a6db8a8efd69f446912d154b260d79f2f5
    role: target
  - path: references_cache/doi_10.3389_fmicb.2022.780346.md
    sha256: a3ba7f3dfd3bd6b6ae6338a05beead53f2cb15c89f70f0a89700cbfa0dc2b929
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-network.json
    sha256: 1cfcd0081f37d8b7d1fe31e7476a69da6e019c73dc37e372fa84c571627d28e9
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-rank.json
    sha256: 9fd1107144f6aa87d8305c001760974e1720e1527f6b0100c8293487cfdce956
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-references.json
    sha256: 3baff05486b40e489c6e58fe6dd5077096b2cdb336988da5afb1ae216db2506d
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-strict.json
    sha256: 83316e3f11375b5ddb2caed362f859a9d6cf4fef81b0032d9e0e361ddb643303
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-terms.json
    sha256: 65ca6849b04e1531363ba07160d9245dcb334c84519cd83c23f1db6c6e457fe4
    role: context
  - path: reports/causal_graph_review/20261015-batch132/baseline-validate.json
    sha256: ccdd0d74e25129a29b742b5892d742ffc9d90df9996c1d8803961710af7f73a0
    role: context
  - path: reports/causal_graph_review/20261015-batch132/before-regression.json
    sha256: 56cfbfbd6c7ce807992bfd71e328ea121efa5f73353235554f8059b9ca7de95b
    role: context
  - path: reports/causal_graph_review/20261015-batch132/gtdb-lookup.json
    sha256: 9aaae6e4ed46288d512adfdf82eef8b5b58e21a021e9e295914be4bfd07c76d2
    role: context
  - path: reports/causal_graph_review/sources/20261014-phormidium-batch131/article.xml
    sha256: 3c62edb9012494e345827fe35d4a76c11a96f9c2decc36ffabfdfef43d0e14f5
    role: context
  - path: reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/manifest.json
    sha256: 18b6fd51c762c339a957efb4664c0f33612048c3b41e972e7c4659bb1f47aa10
    role: context
  - path: reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/ncbi-taxonomy.xml
    sha256: cfee5fecfe1e5362eb32f516f341c16d6cf0eab8992c1f665021fc2d931258c3
    role: context
  - path: reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/oak-taxonomy.json
    sha256: f9a6a4e2c0aab63008c54e77db6cd2b1382260dc24881aa8928786609121b5b6
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: tests/test_phormidium_identity.py
    sha256: 5b46d5c7117ebac6c0508fa9b0fca6e9f6ad378e24ca5ac717ad27995b0538c1
    role: context
  snapshot_id: review-provenance/20261015-batch132-before-inputs
targets:
- target_id: CommunityMech:000054
  path: kb/communities/Phormidium_Alkaline_Consortium.yaml
  label: Phormidium alkaline consortium
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical member and graph participants
- target_id: id-label-policy
  path: conf/id_label_targets.yaml
  label: ID-label correspondence policy
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: conf/id_label_targets.yaml
    role: canonical and export exact-pair exceptions
summary: Confirmed wrong-organism ID in the cyanobacterial member and four graph references,
  hidden by two stale exact-pair waivers. Species-level replacement is supported;
  graph extension and broader non-graph claims remain unresolved.
scope:
  description: One member identity, its four graph references, and two exact-pair
    policy exceptions.
  selection: 'Confirmed issue #2009 during Phormidium graph research.'
  coverage: partial
  population_size: 462
  reviewed_target_ids:
  - CommunityMech:000054
  - id-label-policy
  exclusions:
  - target: Other 461 records and other Phormidium member identities
    reason: Not newly assessed.
  - target: Whole-record scores and completion of graph research
    reason: 'Existing #1699 and #1701 remain open; no whole-record metric is inferred.'
checks:
- check_id: identity-source
  name: Source/ontology identity reconciliation
  status: passed
  required: true
  summary: Read primary identity context and live/local taxonomy statements; legacy
    ID denotes another organism.
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  evidence_ids:
  - ncbi
  - oak
  - paper2022
  - paper2021
  - canonical
evidence:
- evidence_id: ncbi
  kind: database
  reference: reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/ncbi-taxonomy.xml
  locator: Taxon 2293317/AkaTaxIds, 3723519/name and synonym, 2839084/parent and rank
  accessed_at: '2026-10-15T01:09:00.508795Z'
  support: refutes
  summary: Legacy 1807132 resolves to a Bacillota/Clostridia species, not the cyanobacterium.
    The source name is a synonym of cyanobacterial species 3723519; PBR-2020 is its
    child strain 2839084.
- evidence_id: oak
  kind: database
  reference: reports/causal_graph_review/sources/20261015-phormidium-identity-batch132/oak-taxonomy.json
  locator: Selected statements; ontology version 2026-07-12
  accessed_at: '2026-10-15T01:12:16.472646Z'
  support: supports
  summary: The installed ontology independently represents the same legacy alias,
    species canonical label and source-name synonym; neither replacement candidate
    needs a missing-term waiver in this snapshot.
- evidence_id: paper2022
  kind: primary_source
  reference: doi:10.3389/fmicb.2022.780346
  locator: Results, community composition; five metagenomes from different cultures/time
    points; distinct OSCR comparison
  accessed_at: '2026-10-15T01:12:16.472646Z'
  support: supports
  summary: The named Phormidium population is the only cyanobacterium and the most
    abundant member. The combined record spans multiple conditions and sampling times,
    not one isolated strain.
- evidence_id: paper2021
  kind: primary_source
  reference: PMID:34877483
  locator: https://pmc.ncbi.nlm.nih.gov/articles/PMC8633866/ ; identity/strain Results
    p0085-p0110, conclusion p0205, limitations p0215, data availability p0255
  accessed_at: '2026-10-15T01:12:16.472646Z'
  support: supports
  summary: Species naming, persistent strain diversity and the PBR-2020 reference-genome
    accession support species-level grounding while retaining the publication name;
    one reference strain must not absorb all conditions.
- evidence_id: canonical
  kind: record_content
  reference: kb/communities/Phormidium_Alkaline_Consortium.yaml
  locator: taxonomy[0] and all four cyanobacterial graph participant references
  accessed_at: '2026-10-15T01:12:16.472646Z'
  support: supports
  summary: Five term objects use the unrelated legacy ID. The two policy exceptions
    explicitly permit that wrong ID/name pair.
assessments:
- assessment_id: identity
  area: identity
  topic: Cyanobacterial participant identity and source-population scope
  outcome: concern
  summary: Wrong organism is attached to four graph references. Preserve source wording
    and population scope while selecting the canonical species ID.
  target_ids:
  - CommunityMech:000054
  evidence_ids:
  - ncbi
  - oak
  - paper2022
  - paper2021
  - canonical
- assessment_id: waivers
  area: grounding
  topic: Exact-pair exceptions hide the wrong organism
  outcome: concern
  summary: The two exceptions must be removed together with the supported identity
    repair, not replaced by a broader waiver.
  target_ids:
  - id-label-policy
  evidence_ids:
  - ncbi
  - oak
  - canonical
findings:
- finding_id: wrong-cyanobacterial-id
  issue_key: communitymech-2009-phormidium-identity
  category: identity
  severity: blocker
  status: open
  certainty: confirmed
  title: Cyanobacterial graph references point to an unrelated organism
  description: 1807132 is an alternative ID for Syntrophocurvum, not Phormidium/Sodalinema.
    Five maintained fields and two policy waivers require coordinated repair.
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  field_paths:
  - taxonomy[0].taxon_term.term
  - ecological_interactions[0,2,3].source_taxon.term
  - ecological_interactions[1].participating_taxa[0].term
  - targets[communities_yaml,kgx_nodes].exceptions
  evidence_ids:
  - ncbi
  - oak
  - paper2022
  - paper2021
  - canonical
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical member and graph participants
  - repository: CultureBotAI/CommunityMech
    path: conf/id_label_targets.yaml
    role: canonical and export exact-pair exceptions
  rule_id: causal-participant-identity
  native_severity: P1
  normalization_reason: The identifier makes the graph denote the wrong organism,
    not merely a stale label.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2009
actions:
- action_id: repair-identity
  description: Correct the five species references and remove the two stale waivers;
    retain graph structure and source evidence.
  finding_ids:
  - wrong-cyanobacterial-id
  target_ids:
  - CommunityMech:000054
  - id-label-policy
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical member and graph participants
  - repository: CultureBotAI/CommunityMech
    path: conf/id_label_targets.yaml
    role: canonical and export exact-pair exceptions
  acceptance_checks:
  - Canonical species label resolves without an exception.
  - No unsupported single-strain assertion or new graph topology.
  - Guarded write, history, derived artifacts, native validators and current-hash
    review lineage verified.
limitations:
- Scoped identity review, not whole-record certification or corpus completion.
- The 2021 raw article remains an attributed local read-only copy; its hash/read scope
  is in the source manifest, not republished.
- Existing non-graph claims and other member groundings are not recertified. No native
  whole-record completeness/quality score is assigned.
- GTDB assignment remains unresolved; no lineage is invented. No Edison submission,
  paid research or new graph structure.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2009
- https://github.com/CultureBotAI/CommunityMech/issues/1699
- https://github.com/CultureBotAI/CommunityMech/issues/1701
tags:
- batch132
- causal-graphs
- self-review
```
