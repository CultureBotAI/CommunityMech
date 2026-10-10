# PR 1228: additional historical vocabulary finding

- Review: 20261010T082822Z-pr1228-vocabulary
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-10T08:28:22Z
- Finished UTC: 2026-10-10T08:28:22Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Historical observation of the original PR head: the phage-versus-grazer definition overstates a population-density distinction.

## Scope And Provenance

Bounded definition review of original PR head 3d5c4da.

Selection: New lytic-infection definition and matching guide paragraph.
Coverage: partial; 2 reviewed / 20 in the declared population.
Source: git_commit at Git base 3d5c4da574530392b63d0d3a852426878af1dc95.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| schema | src/communitymech/schema/communitymech.yaml | maintained | schema |
| guide | docs/PHAGE_BACTERIA_GUIDE.md | maintained | guide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Primary-backed definition audit | failed | True | schema, guide | Original definition makes an unsupported categorical contrast. |

## Scientific And Domain Assessments

### Viral replication versus grazing

consistency: concern. Targets: schema, guide.

The proposed vocabulary is useful but its density-dependence rationale needs correction.

## Findings

### pr1228-density-distinction: Do not define lytic infection by unique prey-density dependence

major / open / confirmed; issue key: pr1228-density-distinction.

The original schema and guide incorrectly distinguish phages from grazers by population dependence on host/prey density. Use intracellular viral replication and host lysis instead.

## Recommended Actions And Acceptance Checks

### definition-fix

Narrow definition, regenerate model, and add regression.

- Remove the unsupported categorical distinction without changing the infection/lifestyle contract.
- Regenerate the model and pass the definition regression.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| density-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2211389/ | supports | Primary experimental/model study includes prey-density-dependent protozoan feeding and growth; density dependence is not unique to phage populations. |
| replication-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC4425896/ | supports | Primary study distinguishes protist consumption before reproduction from multiple phage progeny produced through infection of a host bacterium. |

## Limits And Additional Notes

- Historical observation saved after the fix: source inputs bind the original reviewed commit, not current working-tree bytes.
- Bounded vocabulary review, not a full per-record scientific certification.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T082822Z-pr1228-vocabulary
kind: repository
repository: CultureBotAI/CommunityMech
title: 'PR 1228: additional historical vocabulary finding'
started_at: '2026-10-10T08:28:22Z'
finished_at: '2026-10-10T08:28:22Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Read-only agent review of an existing PR. No independent human
    approval or separation from all historical authorship is claimed.
skill: pr-adversarial-review
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'Historical observation of the original PR head: the phage-versus-grazer
  definition overstates a population-density distinction.'
source:
  git_revision: 3d5c4da574530392b63d0d3a852426878af1dc95
  state: git_commit
  inputs:
  - path: docs/PHAGE_BACTERIA_GUIDE.md
    sha256: 3eec8fc80282c42a5dfa2ed436b3bd18abff557a924c99d0c4144d476a714883
    role: target
  - path: src/communitymech/schema/communitymech.yaml
    sha256: 61c178f8f846d19a347d3e79ae8180e518687e8d8724095159af569c0d807201
    role: target
targets:
- target_id: schema
  path: src/communitymech/schema/communitymech.yaml
  kind: maintained
  label: schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/schema/communitymech.yaml
    role: maintained source owner
- target_id: guide
  path: docs/PHAGE_BACTERIA_GUIDE.md
  kind: maintained
  label: guide
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: docs/PHAGE_BACTERIA_GUIDE.md
    role: maintained source owner
scope:
  description: Bounded definition review of original PR head 3d5c4da.
  selection: New lytic-infection definition and matching guide paragraph.
  coverage: partial
  population_size: 20
  reviewed_target_ids:
  - schema
  - guide
checks:
- check_id: definition
  name: Primary-backed definition audit
  status: failed
  required: true
  target_ids:
  - schema
  - guide
  evidence_ids:
  - density-primary
  - replication-primary
  summary: Original definition makes an unsupported categorical contrast.
evidence:
- evidence_id: density-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2211389/
  support: supports
  accessed_at: '2026-10-10T08:28:22Z'
  summary: Primary experimental/model study includes prey-density-dependent protozoan
    feeding and growth; density dependence is not unique to phage populations.
- evidence_id: replication-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4425896/
  support: supports
  accessed_at: '2026-10-10T08:28:22Z'
  summary: Primary study distinguishes protist consumption before reproduction from
    multiple phage progeny produced through infection of a host bacterium.
assessments:
- assessment_id: definition
  area: consistency
  topic: Viral replication versus grazing
  outcome: concern
  target_ids:
  - schema
  - guide
  evidence_ids:
  - density-primary
  - replication-primary
  summary: The proposed vocabulary is useful but its density-dependence rationale
    needs correction.
findings:
- finding_id: pr1228-density-distinction
  issue_key: pr1228-density-distinction
  title: Do not define lytic infection by unique prey-density dependence
  description: The original schema and guide incorrectly distinguish phages from grazers
    by population dependence on host/prey density. Use intracellular viral replication
    and host lysis instead.
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  target_ids:
  - schema
  - guide
  evidence_ids:
  - density-primary
  - replication-primary
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/schema/communitymech.yaml
    role: maintained source owner
  - repository: CultureBotAI/CommunityMech
    path: docs/PHAGE_BACTERIA_GUIDE.md
    role: maintained source owner
actions:
- action_id: definition-fix
  description: Narrow definition, regenerate model, and add regression.
  target_ids:
  - schema
  - guide
  finding_ids:
  - pr1228-density-distinction
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/schema/communitymech.yaml
    role: maintained source owner
  - repository: CultureBotAI/CommunityMech
    path: docs/PHAGE_BACTERIA_GUIDE.md
    role: maintained source owner
  acceptance_checks:
  - Remove the unsupported categorical distinction without changing the infection/lifestyle
    contract.
  - Regenerate the model and pass the definition regression.
limitations:
- 'Historical observation saved after the fix: source inputs bind the original reviewed
  commit, not current working-tree bytes.'
- Bounded vocabulary review, not a full per-record scientific certification.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/1989
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261010T074445Z-pr1228-final
  relationship: Additional finding in the same original PR snapshot.
```
