# PR 937 historical schema integration review: after

- Review: 20261010T054622Z-pr937-provenance-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-10T05:46:22Z
- Finished UTC: 2026-10-10T05:46:22Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Issue 1984 is repaired without modifying review history, scientific records, or gate policy. Fresh exact-head and merge-group CI remain required.

## Scope And Provenance

Historical schema hash guard, current semantic assertions, and retention of recorded source revision.

Selection: The single failing integration-test surface from exact-head CI.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 296619a9896dd09566158f9937ae3f09f49bc8a2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| guard | tests/test_causal_review_batch91.py | maintained | Historical schema provenance guard |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused evidence and causal integration regressions | passed | True | guard | 152 passed in 23.56s, including 14 batch91 tests. Controls, mutated historical and live-evidence hashes, missing base/tree, and immediate restore checks all pass. Black, Ruff and git diff --check pass. Historical ledgers, current records, caches and shared schema are unchanged. |
| Historical base retained remotely | passed | True | guard | Annotated tag review-provenance/20261010-batch91-schema retains exact c12b1dc7 base; ledger bytes and all scientific records remain unchanged. |

## Scientific And Domain Assessments

### Historical input versus live semantic invariants

provenance: supported. Targets: guard.

Historical byte identity and current scientific semantics are now separate, both enforced; the permitted additive vocabulary extension passes.

## Findings

### historical-schema: Historical schema digest is incorrectly compared with the live schema

major / resolved / confirmed; issue key: pr937-historical-schema-guard.

Batch91 primary_artifacts includes a schema digest at recorded base c12b1dc71b78f968854875181b0e3b1f8d9ef3df. The test freezes the entire live schema instead, so the additive enum extension fails despite unchanged reviewed scientific semantics.

Disposition: The test now checks the immutable schema blob at the ledger base commit, fails closed if unavailable, and retains live cache/prior-review hashes and the existing current SYNTROPHY assertion. Control/mutation/restore tests pass.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| failure | https://github.com/CultureBotAI/CommunityMech/actions/runs/38026533178 | supports | Full suite on 0e52bb53: 1 failed, 4799 passed, 86 skipped, 8 deselected. The only failure hashes current schema bytes against the historical digest. |
| historical | reports/causal_graph_review/decisions/20261007-five-records-batch91.yaml | supports | Recorded base and tree match GitHub commit c12b1dc71b78f968854875181b0e3b1f8d9ef3df; its schema blob still hashes to 99079e7712d0c6b5eef0f278822a6b04fdb9a3a55b446e1f73f0752e4e626d04. |
| regressions | tests/test_causal_review_batch91.py | supports | 152 passed in 23.56s, including 14 batch91 tests. Controls, mutated historical and live-evidence hashes, missing base/tree, and immediate restore checks all pass. Black, Ruff and git diff --check pass. Historical ledgers, current records, caches and shared schema are unchanged. |

## Limits And Additional Notes

- Self-review, not independent approval.
- No record-level science is re-reviewed; legacy review ledgers remain immutable.
- Auto-merge was disabled after the failure; no failed gate has been bypassed.
- Prior full CI failed before this fix; new full CI and protected merge-group results are not yet claimed passed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T054622Z-pr937-provenance-after
kind: repository
repository: CultureBotAI/CommunityMech
title: 'PR 937 historical schema integration review: after'
started_at: '2026-10-10T05:46:22Z'
finished_at: '2026-10-10T05:46:22Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Same agent implementing and reviewing the integration fix; not
    independent approval.
skill: pr-adversarial-review
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Issue 1984 is repaired without modifying review history, scientific records,
  or gate policy. Fresh exact-head and merge-group CI remain required.
source:
  git_revision: 296619a9896dd09566158f9937ae3f09f49bc8a2
  state: git_commit
  inputs:
  - path: reports/causal_graph_review/decisions/20261007-five-records-batch91.yaml
    sha256: 55c2dafc3c10346c37f864ef5acc1fdadefd37967c51f21696eef562a0296bbe
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e086ff2361e608dea1064d7eebab4f305efda2b0cd8ff25c8a532a1c34277e2a
    role: context
  - path: tests/test_causal_review_batch91.py
    sha256: 43e1dfce5356c250f6932ee600631afe695bc45054dd5a1cb5224b67d56007f6
    role: target
targets:
- target_id: guard
  path: tests/test_causal_review_batch91.py
  label: Historical schema provenance guard
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_causal_review_batch91.py
    role: test owner
scope:
  description: Historical schema hash guard, current semantic assertions, and retention
    of recorded source revision.
  selection: The single failing integration-test surface from exact-head CI.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - guard
checks:
- check_id: focused-regressions
  name: Focused evidence and causal integration regressions
  status: passed
  required: true
  command: PYTHONPATH=src UV_PROJECT_ENVIRONMENT=/Users/marcin/.cache/uv/archive-v0/ehbrYhRifONitMW5eqG2U
    UV_NO_SYNC=1 /Users/marcin/.cache/uv/archive-v0/ehbrYhRifONitMW5eqG2U/bin/python
    -m pytest tests/test_evidence_assessment.py tests/test_causal_review_batch90.py
    tests/test_causal_review_batch91.py tests/test_causal_review_batch92.py tests/test_record_review_contract.py
    -q
  exit_code: 0
  expected_exit_code: 0
  summary: 152 passed in 23.56s, including 14 batch91 tests. Controls, mutated historical
    and live-evidence hashes, missing base/tree, and immediate restore checks all
    pass. Black, Ruff and git diff --check pass. Historical ledgers, current records,
    caches and shared schema are unchanged.
  target_ids:
  - guard
  evidence_ids:
  - regressions
- check_id: source-retention
  name: Historical base retained remotely
  status: passed
  required: true
  summary: Annotated tag review-provenance/20261010-batch91-schema retains exact c12b1dc7
    base; ledger bytes and all scientific records remain unchanged.
  target_ids:
  - guard
  evidence_ids:
  - historical
evidence:
- evidence_id: failure
  kind: validation
  reference: https://github.com/CultureBotAI/CommunityMech/actions/runs/38026533178
  accessed_at: '2026-10-10T05:46:22Z'
  support: supports
  summary: 'Full suite on 0e52bb53: 1 failed, 4799 passed, 86 skipped, 8 deselected.
    The only failure hashes current schema bytes against the historical digest.'
- evidence_id: historical
  kind: record_content
  reference: reports/causal_graph_review/decisions/20261007-five-records-batch91.yaml
  accessed_at: '2026-10-10T05:46:22Z'
  support: supports
  summary: Recorded base and tree match GitHub commit c12b1dc71b78f968854875181b0e3b1f8d9ef3df;
    its schema blob still hashes to 99079e7712d0c6b5eef0f278822a6b04fdb9a3a55b446e1f73f0752e4e626d04.
- evidence_id: regressions
  kind: validation
  reference: tests/test_causal_review_batch91.py
  accessed_at: '2026-10-10T05:46:22Z'
  support: supports
  summary: 152 passed in 23.56s, including 14 batch91 tests. Controls, mutated historical
    and live-evidence hashes, missing base/tree, and immediate restore checks all
    pass. Black, Ruff and git diff --check pass. Historical ledgers, current records,
    caches and shared schema are unchanged.
assessments:
- assessment_id: provenance-boundary
  area: provenance
  topic: Historical input versus live semantic invariants
  outcome: supported
  summary: Historical byte identity and current scientific semantics are now separate,
    both enforced; the permitted additive vocabulary extension passes.
  target_ids:
  - guard
  evidence_ids:
  - historical
  - regressions
findings:
- finding_id: historical-schema
  issue_key: pr937-historical-schema-guard
  category: provenance
  severity: major
  status: resolved
  certainty: confirmed
  title: Historical schema digest is incorrectly compared with the live schema
  description: Batch91 primary_artifacts includes a schema digest at recorded base
    c12b1dc71b78f968854875181b0e3b1f8d9ef3df. The test freezes the entire live schema
    instead, so the additive enum extension fails despite unchanged reviewed scientific
    semantics.
  target_ids:
  - guard
  field_paths:
  - primary_artifacts
  evidence_ids:
  - failure
  - historical
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_causal_review_batch91.py
    role: test owner
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1984
  disposition_reason: The test now checks the immutable schema blob at the ledger
    base commit, fails closed if unavailable, and retains live cache/prior-review
    hashes and the existing current SYNTROPHY assertion. Control/mutation/restore
    tests pass.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261010T054430Z-pr937-provenance-before
    finding_id: historical-schema
actions: []
limitations:
- Self-review, not independent approval.
- No record-level science is re-reviewed; legacy review ledgers remain immutable.
- Auto-merge was disabled after the failure; no failed gate has been bypassed.
- Prior full CI failed before this fix; new full CI and protected merge-group results
  are not yet claimed passed.
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261010T050841Z-pr937-after
  relationship: Later integration failure outside the earlier focused-test scope
- repository: CultureBotAI/CommunityMech
  review_id: 20261010T054430Z-pr937-provenance-before
  relationship: Explicit resolution of historical-schema finding
links:
- https://github.com/CultureBotAI/CommunityMech/pull/937
- https://github.com/CultureBotAI/CommunityMech/issues/1984
```
