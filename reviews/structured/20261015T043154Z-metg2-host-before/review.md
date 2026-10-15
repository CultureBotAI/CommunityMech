# MetG2 host and expression attribution before repair

- Review: 20261015T043154Z-metg2-host-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-15T04:25:47.462501Z
- Finished UTC: 2026-10-15T04:31:54.034072Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Confirmed unsupported host species and implicit cross-kingdom expression attribution; unresolved membership remains separately open.

## Scope And Provenance

Whole target read; scoped host identity and participants of two existing expression nodes assessed against abstract and taxonomy.

Selection: One record selected under existing #1847 from the 462-record corpus and 54 needs_research records.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 5ccf8a6f2996cd8daa3a5181abc84707f10b5a9c.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | MetG2 sugarcane rhizosphere |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Source/record/participant reconciliation | passed | True | CommunityMech:000302 | Compared complete committed abstract, record, taxonomy ranks and community-level schema semantics. |

## Scientific And Domain Assessments

### Host rank and response attribution

grounding: concern. Targets: CommunityMech:000302.

Correct unsupported species precision and separate the documented bacterial and plant expression participants.

### Unresolved experimental identity

completeness: concern. Targets: CommunityMech:000302.

Do not equate responding native taxa with the inoculant or silently resolve the conflicting strain spelling.

## Findings

### host-scope: Unsupported host species and implicit expression participants

major / open / confirmed; issue key: communitymech-1847-metg2-host-scope.

The species assignment exceeds the inspected host evidence; unspecified participants also credit bacteria with plant transcription and the plant with bacterial colonization-associated expression. Correct the parent-rank anchor and explicitly name participants without changing topology.

### membership: Exact MetG2 membership and host identity remain unresolved

major / open / confirmed; issue key: communitymech-1847-metg2-membership.

The responding phylum is not the defined inoculant; primary methods and conflicting strain designation still require reconciliation. A parent-only host anchor does not finish this identity work.

## Recommended Actions And Acceptance Checks

### repair-host

Use an explicitly parent-only host anchor and narrow the two existing expression participants.

- Parent genus and canonical label verified; species/cultivar uncertainty explicit.
- Host and bacterial expression participants separated; native auditor regression checks attribution.
- Unchanged topology/snippets, guarded write, append-only history, native gates and current products verified.

### resolve-membership

Retrieve primary experimental methods/member evidence and reconcile the inoculant, spelling conflict and exact host without attributing native-community observations to all inoculants.

- Exact source-backed inoculant roster and spelling disposition retained.
- Host experimental identity and native-versus-inoculant graph attribution verified.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| abstract | doi:10.1016/j.rhisph.2025.101142; references_cache/doi_10.1016_j.rhisph.2025.101142.md: complete abstract; sugarcane host and separate microbial/host expression sentences | supports | The inspected abstract supports generic sugarcane and separates bacterial colonization-associated transcription from host hormone/nutrient-transporter transcription. It does not verify the experimental cultivar or species. |
| taxonomy | reports/causal_graph_review/sources/20261015-metg2-host/ncbi-taxonomy.xml; Taxa 4546 and 4547: names, ranks and lineage | supports | NCBI distinguishes Saccharum genus from S. officinarum species. The genus can provide an explicitly broader anchor, not an exact experimental identity. |
| record | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml; taxonomy[0], ecological_interactions[0,2], discussions[0] | refutes | Host notes explicitly infer S. officinarum from generic sugarcane. Both existing expression nodes lack named participants and therefore inherit all roster members under the schema's community-level semantics. |
| limits | https://github.com/CultureBotAI/CommunityMech/issues/1847; Live issue body/comment and source manifest | context_only | Issue remains open for inoculant identity, Chiliseed2/Chileseed2 discrepancy and exact host. Bounded searches did not retrieve complete primary methods; search previews were not accepted as new membership evidence. |

## Limits And Additional Notes

- Scoped partial scientific self-review, not independent approval, whole-record certification or corpus completion.
- No native whole-record completeness/quality score is assigned to this focused identity correction.
- No full methods, all figures/supplements, or raw experimental data inspected. Search previews are leads only.
- No new topology or paid provider submission; source caches and historical reviews remain unchanged.
- Historical pre-fix observation at the declared commit. Initial schema-validation attempts published no bundle; this historical bundle was saved after the guarded correction, with all input digests verified against the pre-fix tree.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T043154Z-metg2-host-before
kind: record
repository: CultureBotAI/CommunityMech
title: MetG2 host and expression attribution before repair
started_at: '2026-10-15T04:25:47.462501Z'
finished_at: '2026-10-15T04:31:54.034072Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Implementing-agent source-based review, not independent approval.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
scientific_review: true
source:
  git_revision: 5ccf8a6f2996cd8daa3a5181abc84707f10b5a9c
  state: git_commit
  inputs:
  - path: conf/record_review.yaml
    sha256: 8cbd8f9d209f78de47a8c35091e43bf1dadbe41ee07492c7860b6d4be30112a8
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: a1fe9ffb3e47c18fa4d8ac5abb97a451dc8bffd7940b3b741d682729bb47bfb7
    role: target
  - path: references_cache/doi_10.1016_j.rhisph.2025.101142.md
    sha256: 2651ef5f596a41fc8a30d3f77b706f806b9867e7aa5ff132911e396968be3c60
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/baseline-audit.json
    sha256: 4658e938edd1478ef7a96a55e17214c037b2560b695711b3ba987843809b5519
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/baseline-inventory.json
    sha256: 83d9fd39975d8df851f72c056928f94f88a2a6db251a2d6e652487ab84bcbf49
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/baseline-rank.json
    sha256: 59cca0dce736f7fe40e09f3644f7c26c36efc09d1f4d87313e8c5ba88456863d
    role: context
  - path: reports/causal_graph_review/20261015-metg2-host/before-regression.json
    sha256: 72bcb759110186ccc2d2a497972b7950d705b9b144adbbbae7e3aa10e6ccf724
    role: context
  - path: reports/causal_graph_review/decisions/20261008-four-records-batch108.yaml
    sha256: 4004aaf9719161201cb0135d82c2f0ba2e7231ef9f7473ec99760465993bdaeb
    role: context
  - path: reports/causal_graph_review/sources/20261015-metg2-host/manifest.json
    sha256: 72902dae1b78c6b1b6eea6a325d682d819862cea05ecf7f772643e5e0f9478e2
    role: context
  - path: reports/causal_graph_review/sources/20261015-metg2-host/ncbi-taxonomy.xml
    sha256: 4d93c64556be377014f2deb493de13b74a43fd4a087b7479f106d1bb20bda2aa
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
  snapshot_id: review-provenance/20261015-metg2-host-before-inputs
targets:
- target_id: CommunityMech:000302
  path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  label: MetG2 sugarcane rhizosphere
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical host and graph participants
summary: Confirmed unsupported host species and implicit cross-kingdom expression
  attribution; unresolved membership remains separately open.
scope:
  description: Whole target read; scoped host identity and participants of two existing
    expression nodes assessed against abstract and taxonomy.
  selection: 'One record selected under existing #1847 from the 462-record corpus
    and 54 needs_research records.'
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000302
  exclusions:
  - target: Other 461 records and complete MetG2 source/strain reconciliation
    reason: Not newly certified; methods access remains incomplete.
checks:
- check_id: source-scope
  name: Source/record/participant reconciliation
  status: passed
  required: true
  summary: Compared complete committed abstract, record, taxonomy ranks and community-level
    schema semantics.
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - abstract
  - taxonomy
  - record
evidence:
- evidence_id: abstract
  kind: primary_source
  reference: doi:10.1016/j.rhisph.2025.101142
  locator: 'references_cache/doi_10.1016_j.rhisph.2025.101142.md: complete abstract;
    sugarcane host and separate microbial/host expression sentences'
  accessed_at: '2026-10-15T04:31:54.034072Z'
  support: supports
  summary: The inspected abstract supports generic sugarcane and separates bacterial
    colonization-associated transcription from host hormone/nutrient-transporter transcription.
    It does not verify the experimental cultivar or species.
- evidence_id: taxonomy
  kind: database
  reference: reports/causal_graph_review/sources/20261015-metg2-host/ncbi-taxonomy.xml
  locator: 'Taxa 4546 and 4547: names, ranks and lineage'
  accessed_at: '2026-10-15T04:25:47.462501Z'
  support: supports
  summary: NCBI distinguishes Saccharum genus from S. officinarum species. The genus
    can provide an explicitly broader anchor, not an exact experimental identity.
- evidence_id: record
  kind: record_content
  reference: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  locator: taxonomy[0], ecological_interactions[0,2], discussions[0]
  accessed_at: '2026-10-15T04:31:54.034072Z'
  support: refutes
  summary: Host notes explicitly infer S. officinarum from generic sugarcane. Both
    existing expression nodes lack named participants and therefore inherit all roster
    members under the schema's community-level semantics.
- evidence_id: limits
  kind: prior_review
  reference: https://github.com/CultureBotAI/CommunityMech/issues/1847
  locator: Live issue body/comment and source manifest
  accessed_at: '2026-10-15T04:31:54.034072Z'
  support: context_only
  summary: Issue remains open for inoculant identity, Chiliseed2/Chileseed2 discrepancy
    and exact host. Bounded searches did not retrieve complete primary methods; search
    previews were not accepted as new membership evidence.
assessments:
- assessment_id: host
  area: grounding
  topic: Host rank and response attribution
  outcome: concern
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - abstract
  - taxonomy
  - record
  summary: Correct unsupported species precision and separate the documented bacterial
    and plant expression participants.
- assessment_id: coverage
  area: completeness
  topic: Unresolved experimental identity
  outcome: concern
  target_ids:
  - CommunityMech:000302
  evidence_ids:
  - abstract
  - limits
  summary: Do not equate responding native taxa with the inoculant or silently resolve
    the conflicting strain spelling.
findings:
- finding_id: host-scope
  issue_key: communitymech-1847-metg2-host-scope
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Unsupported host species and implicit expression participants
  description: The species assignment exceeds the inspected host evidence; unspecified
    participants also credit bacteria with plant transcription and the plant with
    bacterial colonization-associated expression. Correct the parent-rank anchor and
    explicitly name participants without changing topology.
  target_ids:
  - CommunityMech:000302
  field_paths:
  - taxonomy[0].taxon_term
  - ecological_interactions[0].participating_taxa
  - ecological_interactions[2].participating_taxa
  evidence_ids:
  - abstract
  - taxonomy
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical host and graph participants
  rule_id: causal-participant-scope
  native_severity: P2
  normalization_reason: Unsupported rank precision and cross-kingdom attribution affect
    graph meaning.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1847
- finding_id: membership
  issue_key: communitymech-1847-metg2-membership
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Exact MetG2 membership and host identity remain unresolved
  description: The responding phylum is not the defined inoculant; primary methods
    and conflicting strain designation still require reconciliation. A parent-only
    host anchor does not finish this identity work.
  target_ids:
  - CommunityMech:000302
  field_paths:
  - taxonomy
  - discussions[0]
  evidence_ids:
  - abstract
  - record
  - limits
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical host and graph participants
  rule_id: causal-community-identity
  native_severity: P2
  normalization_reason: Unresolved inoculant/host identity prevents complete graph
    participant certification.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1847
actions:
- action_id: repair-host
  description: Use an explicitly parent-only host anchor and narrow the two existing
    expression participants.
  finding_ids:
  - host-scope
  target_ids:
  - CommunityMech:000302
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical host and graph participants
  acceptance_checks:
  - Parent genus and canonical label verified; species/cultivar uncertainty explicit.
  - Host and bacterial expression participants separated; native auditor regression
    checks attribution.
  - Unchanged topology/snippets, guarded write, append-only history, native gates
    and current products verified.
- action_id: resolve-membership
  description: Retrieve primary experimental methods/member evidence and reconcile
    the inoculant, spelling conflict and exact host without attributing native-community
    observations to all inoculants.
  finding_ids:
  - membership
  target_ids:
  - CommunityMech:000302
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical host and graph participants
  acceptance_checks:
  - Exact source-backed inoculant roster and spelling disposition retained.
  - Host experimental identity and native-versus-inoculant graph attribution verified.
limitations:
- Scoped partial scientific self-review, not independent approval, whole-record certification
  or corpus completion.
- No native whole-record completeness/quality score is assigned to this focused identity
  correction.
- No full methods, all figures/supplements, or raw experimental data inspected. Search
  previews are leads only.
- No new topology or paid provider submission; source caches and historical reviews
  remain unchanged.
notes:
- Historical pre-fix observation at the declared commit. Initial schema-validation
  attempts published no bundle; this historical bundle was saved after the guarded
  correction, with all input digests verified against the pre-fix tree.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/1847
```
