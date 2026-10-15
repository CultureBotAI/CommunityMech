# Transwell assay participants: before correction

- Review: 20261015T062338Z-transwell-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-15T06:17:58Z
- Finished UTC: 2026-10-15T06:23:38.588134Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Scoped participant correction; graph expansion and source discrepancy remain under #1467.

## Scope And Provenance

Full target read; taxonomy and both existing node scopes assessed. No new causal structure.

Selection: One outstanding record selected from the 462-record causal graph corpus.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 616a2806e363f01a3727ea57dcf3bcd019999943.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000091 | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml | maintained | GLBRC Transwell demonstrations |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Assay and identity source reconciliation | passed | True | CommunityMech:000091 | Read complete record, source scientific body/table, reclassification body and NCBI XML; distinguish source names, current labels and unresolved stock discrepancy. |

## Scientific And Domain Assessments

### Assay-specific strain identity

grounding: concern. Targets: CommunityMech:000091.

Source supports correcting the umbrella roster with explicit qualified strain identities.

### Source discrepancy and graph expansion

completeness: concern. Targets: CommunityMech:000091.

SC discrepancy, independent stock verification, proposed antagonism structure and cultivation repair remain open; preserve needs_research.

## Findings

### participants: Generic roster hides two disjoint assay memberships

major / open / confirmed; issue key: communitymech-1467-assay-participants.

The Bacteria umbrella is not an assay roster or a supported cross-feeder assignment. Resolve current anchors and explicit strain-specific participants without merging the reporter assay and time series.

### remaining: Source stock discrepancy and graph extension remain open

major / open / confirmed; issue key: communitymech-1467-source-discrepancy-and-extension.

SC11,368 in Results conflicts with Table 1 SC11,378/ATCC31532. The table supports a qualified roster, not independent resolution of the actual stock. A new antagonism node requires the skill's separate provider-assisted extension workflow; no bactobolin causal arrow follows from accumulation. Cultivation metadata still confounds test tubes and plate assays and is not certified here.

## Recommended Actions And Acceptance Checks

### finish-source-context

Reconcile source stock discrepancy and separately review cultivation metadata; complete authorized provider-assisted research before new graph structure.

- Exact experimental stock and separate assay conditions verified.
- New node/edge direction has inspected primary support and the required Edison report, without presumed bactobolin mediation.

### repair-participants

Replace the umbrella roster and qualify existing node participants against the inspected primary sources.

- Five distinct strain labels with verified taxonomic anchors and claim-level evidence.
- Reporter direction and three-member subset distinguished by mutation/restoration tests; topology unchanged.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | PMID:29152587; reports/causal_graph_review/sources/20261015-transwell/transwell.xml: Results, Table 1, Discussion, Methods | supports | Main scientific sections, embedded captions and Table 1 read. Two separate demonstrations: Cv017/Cv026 reporter pair; E264/DC3000/SC11,378 table-defined community. Prose says SC11,368; no erratum or original stock verification resolves that disagreement. |
| classification | PMID:33159606; reports/causal_graph_review/sources/20261015-transwell/reclassification.xml: full scientific body and Tables 1-2 | supports | Genomic and phenotypic reclassification supports C. subtsugae for ATCC 31532 and CV026; Introduction identifies CV017 as its derivative with that species assignment. This is taxonomic evidence, not new Transwell interaction evidence. |
| taxonomy | reports/causal_graph_review/sources/20261015-transwell/taxonomy.xml; Taxa 251747, 271848, 223283: exact names and ranks | supports | Current NCBI species anchor for C. subtsugae and strain anchors for E264/DC3000. Shared species CURIE does not collapse the three Chromobacterium strains. |
| record | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml; taxonomy, ecological_interactions[0,1], discussions[0] | refutes | Bacteria-only roster and unnamed assay participants. |

## Limits And Additional Notes

- Partial scientific self-review, not independent approval or whole-record/corpus completion.
- No whole-record completeness/quality score assigned to this focused causal-graph repair.
- Main scientific bodies and embedded tables/captions read; no independent image, supplement, raw spectra or original stock audit.
- No new interaction node or downstream arrow; no provider submission or credit spend in this correction.
- Protected PR/queue checks are pending at this immutable local snapshot.
- Ignored/hidden-inclusive local searches covered kb/taxa, both canonical record roots and references_cache; no reusable matching Chromobacterium record or prior reclassification cache was found in that bounded scope.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T062338Z-transwell-before
kind: record
repository: CultureBotAI/CommunityMech
title: 'Transwell assay participants: before correction'
started_at: '2026-10-15T06:17:58Z'
finished_at: '2026-10-15T06:23:38.588134Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Implementing-agent adversarial source review, not independent
    approval.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
scientific_review: true
source:
  git_revision: 616a2806e363f01a3727ea57dcf3bcd019999943
  state: working_tree
  inputs:
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    sha256: 8d1ef9c4d9c8b8b0f2c203a984747b02cfa32e10fe648d3fd5bf0a9548c8208f
    role: target
  - path: references_cache/PMID_29152587.txt
    sha256: 2e773cfbd68cb0dde8b53d5f97ed3576433fc0bea771e916ab08836828c75f73
    role: context
  - path: references_cache/PMID_33159606.txt
    sha256: fb50e1811b956b9a6c0e77b6f0f5b4a985baf1501772935f7abe91b2276db9cc
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch42.yaml
    sha256: c0b2c349054635e9d6993082265669faede9e45656a6ae48549c87df053df645
    role: context
  - path: reports/causal_graph_review/sources/20261015-transwell/manifest.json
    sha256: cff61b0302655881f9bb5bc76e77a6f14a02663db8d087d515172ea1fd43aa7b
    role: context
  - path: reports/causal_graph_review/sources/20261015-transwell/reclassification.xml
    sha256: 3d228474c16ad1bda56060122abb5d8f2ccc1b975dd31ff755b06c6594dc9841
    role: context
  - path: reports/causal_graph_review/sources/20261015-transwell/taxonomy.xml
    sha256: 560dcbce4af198f5e8e779c0827c1747c354d42790dfec670823126d5963732e
    role: context
  - path: reports/causal_graph_review/sources/20261015-transwell/transwell.xml
    sha256: 45093e19ddf5c80b94ad776a1569d78272c0931912d6314babe960061c8a2920
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
targets:
- target_id: CommunityMech:000091
  path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
  label: GLBRC Transwell demonstrations
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical assay participants and graph
summary: 'Scoped participant correction; graph expansion and source discrepancy remain
  under #1467.'
scope:
  description: Full target read; taxonomy and both existing node scopes assessed.
    No new causal structure.
  selection: One outstanding record selected from the 462-record causal graph corpus.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000091
  exclusions:
  - target: Other 461 records; cultivation repair, figure images, separate supplements
      and raw data
    reason: Not assessed or certified by this scoped participant repair.
checks:
- check_id: source-review
  name: Assay and identity source reconciliation
  status: passed
  required: true
  summary: Read complete record, source scientific body/table, reclassification body
    and NCBI XML; distinguish source names, current labels and unresolved stock discrepancy.
  target_ids:
  - CommunityMech:000091
  evidence_ids:
  - primary
  - classification
  - taxonomy
  - record
evidence:
- evidence_id: primary
  kind: primary_source
  reference: PMID:29152587
  locator: 'reports/causal_graph_review/sources/20261015-transwell/transwell.xml:
    Results, Table 1, Discussion, Methods'
  accessed_at: '2026-10-15T06:17:58Z'
  support: supports
  summary: 'Main scientific sections, embedded captions and Table 1 read. Two separate
    demonstrations: Cv017/Cv026 reporter pair; E264/DC3000/SC11,378 table-defined
    community. Prose says SC11,368; no erratum or original stock verification resolves
    that disagreement.'
- evidence_id: classification
  kind: primary_source
  reference: PMID:33159606
  locator: 'reports/causal_graph_review/sources/20261015-transwell/reclassification.xml:
    full scientific body and Tables 1-2'
  accessed_at: '2026-10-15T06:17:59Z'
  support: supports
  summary: Genomic and phenotypic reclassification supports C. subtsugae for ATCC
    31532 and CV026; Introduction identifies CV017 as its derivative with that species
    assignment. This is taxonomic evidence, not new Transwell interaction evidence.
- evidence_id: taxonomy
  kind: database
  reference: reports/causal_graph_review/sources/20261015-transwell/taxonomy.xml
  locator: 'Taxa 251747, 271848, 223283: exact names and ranks'
  accessed_at: '2026-10-15T06:17:59Z'
  support: supports
  summary: Current NCBI species anchor for C. subtsugae and strain anchors for E264/DC3000.
    Shared species CURIE does not collapse the three Chromobacterium strains.
- evidence_id: record
  kind: record_content
  reference: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
  locator: taxonomy, ecological_interactions[0,1], discussions[0]
  accessed_at: '2026-10-15T06:23:38.588134Z'
  support: refutes
  summary: Bacteria-only roster and unnamed assay participants.
assessments:
- assessment_id: participants
  area: grounding
  topic: Assay-specific strain identity
  outcome: concern
  target_ids:
  - CommunityMech:000091
  evidence_ids:
  - primary
  - classification
  - taxonomy
  - record
  summary: Source supports correcting the umbrella roster with explicit qualified
    strain identities.
- assessment_id: limits
  area: completeness
  topic: Source discrepancy and graph expansion
  outcome: concern
  target_ids:
  - CommunityMech:000091
  evidence_ids:
  - primary
  - record
  summary: SC discrepancy, independent stock verification, proposed antagonism structure
    and cultivation repair remain open; preserve needs_research.
findings:
- target_ids:
  - CommunityMech:000091
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical assay participants and graph
  certainty: confirmed
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1467
  finding_id: participants
  issue_key: communitymech-1467-assay-participants
  category: grounding
  severity: major
  status: open
  title: Generic roster hides two disjoint assay memberships
  description: The Bacteria umbrella is not an assay roster or a supported cross-feeder
    assignment. Resolve current anchors and explicit strain-specific participants
    without merging the reporter assay and time series.
  field_paths:
  - taxonomy
  - ecological_interactions[0]
  - ecological_interactions[1].participating_taxa
  evidence_ids:
  - primary
  - classification
  - taxonomy
  - record
  rule_id: causal-participant-scope
  native_severity: P2
  normalization_reason: Missing and conflated participants change graph meaning.
- target_ids:
  - CommunityMech:000091
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical assay participants and graph
  certainty: confirmed
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1467
  finding_id: remaining
  issue_key: communitymech-1467-source-discrepancy-and-extension
  category: completeness
  severity: major
  status: open
  title: Source stock discrepancy and graph extension remain open
  description: SC11,368 in Results conflicts with Table 1 SC11,378/ATCC31532. The
    table supports a qualified roster, not independent resolution of the actual stock.
    A new antagonism node requires the skill's separate provider-assisted extension
    workflow; no bactobolin causal arrow follows from accumulation. Cultivation metadata
    still confounds test tubes and plate assays and is not certified here.
  field_paths:
  - discussions[0]
  - growth_media
  - ecological_interactions
  evidence_ids:
  - primary
  - record
  rule_id: causal-source-context
  native_severity: P2
  normalization_reason: Unresolved experimental identity and context prevent complete
    graph/record certification.
actions:
- action_id: finish-source-context
  description: Reconcile source stock discrepancy and separately review cultivation
    metadata; complete authorized provider-assisted research before new graph structure.
  finding_ids:
  - remaining
  target_ids:
  - CommunityMech:000091
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical assay participants and graph
  acceptance_checks:
  - Exact experimental stock and separate assay conditions verified.
  - New node/edge direction has inspected primary support and the required Edison
    report, without presumed bactobolin mediation.
- action_id: repair-participants
  description: Replace the umbrella roster and qualify existing node participants
    against the inspected primary sources.
  finding_ids:
  - participants
  target_ids:
  - CommunityMech:000091
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical assay participants and graph
  acceptance_checks:
  - Five distinct strain labels with verified taxonomic anchors and claim-level evidence.
  - Reporter direction and three-member subset distinguished by mutation/restoration
    tests; topology unchanged.
limitations:
- Partial scientific self-review, not independent approval or whole-record/corpus
  completion.
- No whole-record completeness/quality score assigned to this focused causal-graph
  repair.
- Main scientific bodies and embedded tables/captions read; no independent image,
  supplement, raw spectra or original stock audit.
- No new interaction node or downstream arrow; no provider submission or credit spend
  in this correction.
- Protected PR/queue checks are pending at this immutable local snapshot.
- Ignored/hidden-inclusive local searches covered kb/taxa, both canonical record roots
  and references_cache; no reusable matching Chromobacterium record or prior reclassification
  cache was found in that bounded scope.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/1467
```
