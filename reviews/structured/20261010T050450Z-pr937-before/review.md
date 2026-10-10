# PR 937 evidence vocabulary self-adversarial review: before

- Review: 20261010T050450Z-pr937-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-10T05:04:50Z
- Finished UTC: 2026-10-10T05:04:50Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

One confirmed documentation compatibility defect requires correction before merge.

## Scope And Provenance

Bounded review of PR 937 guide, additive source vocabulary and regression coverage against current main.

Selection: All three maintained PR surfaces; generated model and protected CI verified in follow-up.
Coverage: full; 3 reviewed / 3 in the declared population.
Source: working_tree at Git base 89247d7f22fe20db63cd088ad16dae0d004a4739.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| guide | docs/EVIDENCE_ASSESSMENT.md | maintained | guide |
| schema | src/communitymech/schema/communitymech.yaml | maintained | schema |
| tests | tests/test_evidence_assessment.py | maintained | tests |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Guide versus canonical schema | failed | True | guide, schema | WRONG_STATEMENT guidance contradicts the established schema meaning. |

## Scientific And Domain Assessments

### Citation attribution versus claim truth

consistency: concern. Targets: guide.

Guide contradicts local semantics and must be corrected.

### Compatibility and regression coverage

schema: supported. Targets: schema, tests.

Eight source values are added without removing existing schema definitions. Existing tests cover all thirteen source labels and five support labels; omission, citation, and generated-model checks should be expanded during the fix.

## Findings

### citation-semantics: Guide conflates a misattributed citation with an incorrect claim

major / open / confirmed; issue key: pr937-evidence-guide-semantics.

The guide defines WRONG_STATEMENT as an incorrect claim, but EvidenceItemSupportEnum reserves it for citation misattribution. It also narrows legacy source categories and uses optional-field migration language despite required existing fields.

## Recommended Actions And Acceptance Checks

### repair-guide

Align guidance with local semantics and strengthen compatibility tests.

- Correct citation-misattribution meaning and required-field guidance.
- Preserve legacy source classifications and shared quotation locations.
- Pass focused tests and protected PR/merge-group checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| contract | src/communitymech/schema/communitymech.yaml; EvidenceItemSupportEnum, EvidenceSourceEnum and EvidenceItem required slots | supports | Schema inspected alongside the guide: citation relationship is distinct from claim truth; both assessments remain required. Legacy IN_VIVO includes field studies and REVIEW includes meta-analysis. |

## Limits And Additional Notes

- Self-review, not independent approval.
- No scientific record or cited literature is reassessed.
- This initial semantic review does not claim successful CI, merge, or branch cleanup.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T050450Z-pr937-before
kind: repository
repository: CultureBotAI/CommunityMech
title: 'PR 937 evidence vocabulary self-adversarial review: before'
started_at: '2026-10-10T05:04:50Z'
finished_at: '2026-10-10T05:04:50Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The same agent integrates, fixes, and reviews this PR; no independent
    approval claimed.
skill: pr-adversarial-review
completion: completed
verdict: needs_curation
scientific_review: false
summary: One confirmed documentation compatibility defect requires correction before
  merge.
source:
  git_revision: 89247d7f22fe20db63cd088ad16dae0d004a4739
  state: working_tree
  inputs:
  - path: docs/EVIDENCE_ASSESSMENT.md
    sha256: 8a71142172815c118fe6f81819edc6bf5b374f407f4ab20bd5262b9df047e06b
    role: target
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e086ff2361e608dea1064d7eebab4f305efda2b0cd8ff25c8a532a1c34277e2a
    role: target
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_evidence_assessment.py
    sha256: b7cabe30621b4c78dc82246705240f60766f4dab1b7e645c47bcedad4b2150dc
    role: target
targets:
- target_id: guide
  path: docs/EVIDENCE_ASSESSMENT.md
  kind: maintained
  label: guide
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: docs/EVIDENCE_ASSESSMENT.md
    role: maintained evidence contract
- target_id: schema
  path: src/communitymech/schema/communitymech.yaml
  kind: maintained
  label: schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/schema/communitymech.yaml
    role: maintained evidence contract
- target_id: tests
  path: tests/test_evidence_assessment.py
  kind: maintained
  label: tests
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_evidence_assessment.py
    role: maintained evidence contract
scope:
  description: Bounded review of PR 937 guide, additive source vocabulary and regression
    coverage against current main.
  selection: All three maintained PR surfaces; generated model and protected CI verified
    in follow-up.
  coverage: full
  population_size: 3
  reviewed_target_ids:
  - guide
  - schema
  - tests
checks:
- check_id: semantic-comparison
  name: Guide versus canonical schema
  status: failed
  required: true
  summary: WRONG_STATEMENT guidance contradicts the established schema meaning.
  target_ids:
  - guide
  - schema
  evidence_ids:
  - contract
evidence:
- evidence_id: contract
  kind: record_content
  reference: src/communitymech/schema/communitymech.yaml
  locator: EvidenceItemSupportEnum, EvidenceSourceEnum and EvidenceItem required slots
  accessed_at: '2026-10-10T05:04:50Z'
  support: supports
  summary: 'Schema inspected alongside the guide: citation relationship is distinct
    from claim truth; both assessments remain required. Legacy IN_VIVO includes field
    studies and REVIEW includes meta-analysis.'
assessments:
- assessment_id: guide-semantics
  area: consistency
  topic: Citation attribution versus claim truth
  outcome: concern
  summary: Guide contradicts local semantics and must be corrected.
  target_ids:
  - guide
  evidence_ids:
  - contract
- assessment_id: additive-scope
  area: schema
  topic: Compatibility and regression coverage
  outcome: supported
  summary: Eight source values are added without removing existing schema definitions.
    Existing tests cover all thirteen source labels and five support labels; omission,
    citation, and generated-model checks should be expanded during the fix.
  target_ids:
  - schema
  - tests
  evidence_ids:
  - contract
findings:
- finding_id: citation-semantics
  issue_key: pr937-evidence-guide-semantics
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  title: Guide conflates a misattributed citation with an incorrect claim
  description: The guide defines WRONG_STATEMENT as an incorrect claim, but EvidenceItemSupportEnum
    reserves it for citation misattribution. It also narrows legacy source categories
    and uses optional-field migration language despite required existing fields.
  target_ids:
  - guide
  field_paths:
  - Support values
  - Compatibility and curation
  evidence_ids:
  - contract
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: docs/EVIDENCE_ASSESSMENT.md
    role: maintained evidence contract
  native_severity: P2
  normalization_reason: Materially misleading curation guidance can invert interpretation
    of evidence; the scoped code change itself is additive.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1982
actions:
- action_id: repair-guide
  description: Align guidance with local semantics and strengthen compatibility tests.
  finding_ids:
  - citation-semantics
  target_ids:
  - guide
  - tests
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: docs/EVIDENCE_ASSESSMENT.md
    role: maintained evidence contract
  - repository: CultureBotAI/CommunityMech
    path: tests/test_evidence_assessment.py
    role: maintained evidence contract
  acceptance_checks:
  - Correct citation-misattribution meaning and required-field guidance.
  - Preserve legacy source classifications and shared quotation locations.
  - Pass focused tests and protected PR/merge-group checks.
limitations:
- Self-review, not independent approval.
- No scientific record or cited literature is reassessed.
- This initial semantic review does not claim successful CI, merge, or branch cleanup.
links:
- https://github.com/CultureBotAI/CommunityMech/pull/937
- https://github.com/CultureBotAI/CommunityMech/issues/1982
```
