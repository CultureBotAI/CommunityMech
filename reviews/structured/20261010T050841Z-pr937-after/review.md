# PR 937 evidence vocabulary self-adversarial review: after

- Review: 20261010T050841Z-pr937-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-10T05:08:41Z
- Finished UTC: 2026-10-10T05:08:41Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Issue 1982 is repaired. The eight added source values preserve every existing schema definition, citation format, required assessment, and shared quotation-location field. Focused tests pass; protected CI remains required before merge.

## Scope And Provenance

Bounded review of PR 937 guide, additive source vocabulary and regression coverage against current main.

Selection: All four changed PR surfaces: guide, canonical schema, generated model, and tests.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: git_commit at Git base 293b4518fa378ea9746db82fe630ce2b86e2f367.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| guide | docs/EVIDENCE_ASSESSMENT.md | maintained | guide |
| schema | src/communitymech/schema/communitymech.yaml | maintained | schema |
| tests | tests/test_evidence_assessment.py | maintained | tests |
| model | src/communitymech/datamodel/communitymech.py | generated | Generated Python model |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Guide versus canonical schema | passed | True | guide, schema | Guide preserves local support semantics, requiredness, legacy classifications, and separate shared quote-location provenance. |
| Focused regression suite | passed | True | guide, schema, tests, model | 152 passed in 24.34s using Python 3.13, LinkML 1.9.3 and runtime 1.9.5. Earlier subprocess cache access error was resolved by using this existing environment with UV_NO_SYNC=1. |
| Structured compatibility comparison against main | passed | True | schema, model | Removing exactly the eight new permissible values yields a parsed YAML document identical to main 42959bef. Scientific records, shared schema, history and cached references have no diff against main. |
| Local strict corpus validation | passed | True | schema, model | 460 files, zero error rows. Ontology-dependent shared-id and prokaryotic-domain checks unavailable locally and explicitly not counted as passed. |
| Formatting and diff checks | passed | True | guide, schema, tests, model | Black check for changed Python, Ruff check for the test file, and git diff --check against main pass. |

## Scientific And Domain Assessments

### Citation attribution versus claim truth

consistency: supported. Targets: guide.

Issue 1982 acceptance criteria are satisfied without changing established enum meanings.

### Backward-compatible vocabulary extension

schema: supported. Targets: schema, tests, model.

Eight source values are additive; no required fields, citation rules, shared fields, or scientific records are changed.

## Findings

### citation-semantics: Guide conflates a misattributed citation with an incorrect claim

major / resolved / confirmed; issue key: pr937-evidence-guide-semantics.

The guide defines WRONG_STATEMENT as an incorrect claim, but EvidenceItemSupportEnum reserves it for citation misattribution. It also narrows legacy source categories and uses optional-field migration language despite required existing fields.

Disposition: The guide now describes citation misattribution, contrasts it with REFUTE, states requiredness/no new fields, and explicitly retains legacy IN_VIVO and REVIEW meanings. Expanded tests and additive-schema comparison pass.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| contract | src/communitymech/schema/communitymech.yaml; EvidenceItemSupportEnum, EvidenceSourceEnum and EvidenceItem required slots | supports | Schema inspected alongside the guide: citation relationship is distinct from claim truth; both assessments remain required. Legacy IN_VIVO includes field studies and REVIEW includes meta-analysis. |
| regressions | tests/test_evidence_assessment.py | supports | All 65 support/source combinations round-trip, assessment omissions/null/empty values are rejected, existing references remain accepted, shared locations retain free text and no support default, and model enum descriptions match the schema. Related validator, review-contract and cultivation tests also pass. |

## Limits And Additional Notes

- Self-review, not independent approval.
- No scientific record or literature is reassessed.
- Pre-existing LinkML null required text-field acceptance is tracked separately in issue 1983; generated models reject those nulls. No claim that this unrelated validator gap is fixed.
- Local taxonomy-backed checks were unavailable; protected PR and merge-group checks remain mandatory.
- This pre-publication review does not assert full-suite CI, merge, or branch cleanup has completed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T050841Z-pr937-after
kind: repository
repository: CultureBotAI/CommunityMech
title: 'PR 937 evidence vocabulary self-adversarial review: after'
started_at: '2026-10-10T05:08:41Z'
finished_at: '2026-10-10T05:08:41Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The same agent integrates, fixes, and reviews this PR; no independent
    approval claimed.
skill: pr-adversarial-review
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Issue 1982 is repaired. The eight added source values preserve every existing
  schema definition, citation format, required assessment, and shared quotation-location
  field. Focused tests pass; protected CI remains required before merge.
source:
  git_revision: 293b4518fa378ea9746db82fe630ce2b86e2f367
  state: git_commit
  inputs:
  - path: docs/EVIDENCE_ASSESSMENT.md
    sha256: fa1b56f46cfea7ccfa87cadf24a61835342fe9ca07d112ba1b5712877cd26269
    role: target
  - path: src/communitymech/datamodel/communitymech.py
    sha256: 0e32cf9d89d58aac7bc348f1ba7f5df09ccb8b407b45f0d2bc3f5c07f1663dd9
    role: target
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e086ff2361e608dea1064d7eebab4f305efda2b0cd8ff25c8a532a1c34277e2a
    role: target
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_evidence_assessment.py
    sha256: 735912c84d9df8685fd889e94dca5028ec41fc2d2247013deac8b4cc2ba5e651
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
- target_id: model
  path: src/communitymech/datamodel/communitymech.py
  kind: generated
  label: Generated Python model
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/schema/communitymech.yaml
    role: canonical model schema
scope:
  description: Bounded review of PR 937 guide, additive source vocabulary and regression
    coverage against current main.
  selection: 'All four changed PR surfaces: guide, canonical schema, generated model,
    and tests.'
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - guide
  - schema
  - tests
  - model
checks:
- check_id: semantic-comparison
  name: Guide versus canonical schema
  status: passed
  required: true
  summary: Guide preserves local support semantics, requiredness, legacy classifications,
    and separate shared quote-location provenance.
  target_ids:
  - guide
  - schema
  evidence_ids:
  - contract
- check_id: compatibility-tests
  name: Focused regression suite
  status: passed
  required: true
  summary: 152 passed in 24.34s using Python 3.13, LinkML 1.9.3 and runtime 1.9.5.
    Earlier subprocess cache access error was resolved by using this existing environment
    with UV_NO_SYNC=1.
  target_ids:
  - guide
  - schema
  - tests
  - model
  evidence_ids:
  - regressions
  command: PYTHONPATH=src UV_NO_SYNC=1 UV_PROJECT_ENVIRONMENT=<verified-env> python
    -m pytest tests/test_evidence_assessment.py tests/test_github_evidence_references.py
    tests/test_datamodel.py tests/test_record_review_contract.py tests/test_validators.py
    tests/test_cultivation_vocab_sync.py tests/test_record_review_routes.py -q
  exit_code: 0
  expected_exit_code: 0
- check_id: additive-schema
  name: Structured compatibility comparison against main
  status: passed
  required: true
  summary: Removing exactly the eight new permissible values yields a parsed YAML
    document identical to main 42959bef. Scientific records, shared schema, history
    and cached references have no diff against main.
  target_ids:
  - schema
  - model
  evidence_ids:
  - contract
- check_id: strict-corpus
  name: Local strict corpus validation
  status: passed
  required: true
  summary: 460 files, zero error rows. Ontology-dependent shared-id and prokaryotic-domain
    checks unavailable locally and explicitly not counted as passed.
  target_ids:
  - schema
  - model
  evidence_ids:
  - regressions
  command: PYTHONPATH=src python scripts/validate_strict.py --out /private/tmp/communitymech-pr937-strict.tsv
    --workers 4
  exit_code: 0
  expected_exit_code: 0
  scope_note: Local schema/cross-field checks only; real required CI must supply ontology
    checks.
- check_id: format
  name: Formatting and diff checks
  status: passed
  required: true
  summary: Black check for changed Python, Ruff check for the test file, and git diff
    --check against main pass.
  target_ids:
  - guide
  - schema
  - tests
  - model
  evidence_ids:
  - regressions
evidence:
- evidence_id: contract
  kind: record_content
  reference: src/communitymech/schema/communitymech.yaml
  locator: EvidenceItemSupportEnum, EvidenceSourceEnum and EvidenceItem required slots
  accessed_at: '2026-10-10T05:08:41Z'
  support: supports
  summary: 'Schema inspected alongside the guide: citation relationship is distinct
    from claim truth; both assessments remain required. Legacy IN_VIVO includes field
    studies and REVIEW includes meta-analysis.'
- evidence_id: regressions
  kind: validation
  reference: tests/test_evidence_assessment.py
  accessed_at: '2026-10-10T05:08:41Z'
  support: supports
  summary: All 65 support/source combinations round-trip, assessment omissions/null/empty
    values are rejected, existing references remain accepted, shared locations retain
    free text and no support default, and model enum descriptions match the schema.
    Related validator, review-contract and cultivation tests also pass.
assessments:
- assessment_id: guide-semantics
  area: consistency
  topic: Citation attribution versus claim truth
  outcome: supported
  summary: Issue 1982 acceptance criteria are satisfied without changing established
    enum meanings.
  target_ids:
  - guide
  evidence_ids:
  - contract
  - regressions
- assessment_id: additive-scope
  area: schema
  topic: Backward-compatible vocabulary extension
  outcome: supported
  summary: Eight source values are additive; no required fields, citation rules, shared
    fields, or scientific records are changed.
  target_ids:
  - schema
  - tests
  - model
  evidence_ids:
  - contract
  - regressions
findings:
- finding_id: citation-semantics
  issue_key: pr937-evidence-guide-semantics
  category: consistency
  severity: major
  status: resolved
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
  disposition_reason: The guide now describes citation misattribution, contrasts it
    with REFUTE, states requiredness/no new fields, and explicitly retains legacy
    IN_VIVO and REVIEW meanings. Expanded tests and additive-schema comparison pass.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261010T050450Z-pr937-before
    finding_id: citation-semantics
actions: []
limitations:
- Self-review, not independent approval.
- No scientific record or literature is reassessed.
- Pre-existing LinkML null required text-field acceptance is tracked separately in
  issue 1983; generated models reject those nulls. No claim that this unrelated validator
  gap is fixed.
- Local taxonomy-backed checks were unavailable; protected PR and merge-group checks
  remain mandatory.
- This pre-publication review does not assert full-suite CI, merge, or branch cleanup
  has completed.
links:
- https://github.com/CultureBotAI/CommunityMech/pull/937
- https://github.com/CultureBotAI/CommunityMech/issues/1982
- https://github.com/CultureBotAI/CommunityMech/issues/1983
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261010T050450Z-pr937-before
  relationship: Explicit resolution of citation-semantics finding
```
