# PR 937 historical schema integration review: before

- Review: 20261010T054430Z-pr937-provenance-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-10T05:44:30Z
- Finished UTC: 2026-10-10T05:44:30Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

A reproduced merge-blocking test defect requires a provenance-preserving correction.

## Scope And Provenance

Historical schema hash guard, current semantic assertions, and retention of recorded source revision.

Selection: The single failing integration-test surface from exact-head CI.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 0e52bb53c1d7bba3805307c377d4fdab3683573b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| guard | tests/test_causal_review_batch91.py | maintained | Historical schema provenance guard |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Batch91 regression reproduction | failed | True | guard | One failed, seven passed locally; identical to the sole full-CI failure. |

## Scientific And Domain Assessments

### Historical input versus live semantic invariants

provenance: concern. Targets: guard.

The guard must verify historical schema bytes at the recorded revision while preserving live semantic and evidence checks.

## Findings

### historical-schema: Historical schema digest is incorrectly compared with the live schema

major / open / confirmed; issue key: pr937-historical-schema-guard.

Batch91 primary_artifacts includes a schema digest at recorded base c12b1dc71b78f968854875181b0e3b1f8d9ef3df. The test freezes the entire live schema instead, so the additive enum extension fails despite unchanged reviewed scientific semantics.

## Recommended Actions And Acceptance Checks

### repair-guard

Verify historical schema at recorded base without changing the immutable ledger.

- Fail closed for wrong hashes or unavailable revisions.
- Keep current SYNTROPHY and evidence-byte guards.
- Add mutation/control/restore tests and rerun protected CI.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| failure | https://github.com/CultureBotAI/CommunityMech/actions/runs/38026533178 | supports | Full suite on 0e52bb53: 1 failed, 4799 passed, 86 skipped, 8 deselected. The only failure hashes current schema bytes against the historical digest. |
| historical | reports/causal_graph_review/decisions/20261007-five-records-batch91.yaml | supports | Recorded base and tree match GitHub commit c12b1dc71b78f968854875181b0e3b1f8d9ef3df; its schema blob still hashes to 99079e7712d0c6b5eef0f278822a6b04fdb9a3a55b446e1f73f0752e4e626d04. |

## Limits And Additional Notes

- Self-review, not independent approval.
- No record-level science is re-reviewed; legacy review ledgers remain immutable.
- Auto-merge was disabled after the failure; no failed gate has been bypassed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T054430Z-pr937-provenance-before
kind: repository
repository: CultureBotAI/CommunityMech
title: 'PR 937 historical schema integration review: before'
started_at: '2026-10-10T05:44:30Z'
finished_at: '2026-10-10T05:44:30Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Same agent implementing and reviewing the integration fix; not
    independent approval.
skill: pr-adversarial-review
completion: completed
verdict: needs_curation
scientific_review: false
summary: A reproduced merge-blocking test defect requires a provenance-preserving
  correction.
source:
  git_revision: 0e52bb53c1d7bba3805307c377d4fdab3683573b
  state: git_commit
  inputs:
  - path: reports/causal_graph_review/decisions/20261007-five-records-batch91.yaml
    sha256: 55c2dafc3c10346c37f864ef5acc1fdadefd37967c51f21696eef562a0296bbe
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e086ff2361e608dea1064d7eebab4f305efda2b0cd8ff25c8a532a1c34277e2a
    role: context
  - path: tests/test_causal_review_batch91.py
    sha256: ebe9c06685e16b5fd896f511b0cd8a3d12a4affdb0d0d67e5b28087d7916459f
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
- check_id: reproduction
  name: Batch91 regression reproduction
  status: failed
  required: true
  command: PYTHONPATH=src python -m pytest tests/test_causal_review_batch91.py -q
  exit_code: 1
  expected_exit_code: 0
  summary: One failed, seven passed locally; identical to the sole full-CI failure.
  target_ids:
  - guard
  evidence_ids:
  - failure
evidence:
- evidence_id: failure
  kind: validation
  reference: https://github.com/CultureBotAI/CommunityMech/actions/runs/38026533178
  accessed_at: '2026-10-10T05:44:30Z'
  support: supports
  summary: 'Full suite on 0e52bb53: 1 failed, 4799 passed, 86 skipped, 8 deselected.
    The only failure hashes current schema bytes against the historical digest.'
- evidence_id: historical
  kind: record_content
  reference: reports/causal_graph_review/decisions/20261007-five-records-batch91.yaml
  accessed_at: '2026-10-10T05:44:30Z'
  support: supports
  summary: Recorded base and tree match GitHub commit c12b1dc71b78f968854875181b0e3b1f8d9ef3df;
    its schema blob still hashes to 99079e7712d0c6b5eef0f278822a6b04fdb9a3a55b446e1f73f0752e4e626d04.
assessments:
- assessment_id: provenance-boundary
  area: provenance
  topic: Historical input versus live semantic invariants
  outcome: concern
  summary: The guard must verify historical schema bytes at the recorded revision
    while preserving live semantic and evidence checks.
  target_ids:
  - guard
  evidence_ids:
  - failure
  - historical
findings:
- finding_id: historical-schema
  issue_key: pr937-historical-schema-guard
  category: provenance
  severity: major
  status: open
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
actions:
- action_id: repair-guard
  description: Verify historical schema at recorded base without changing the immutable
    ledger.
  finding_ids:
  - historical-schema
  target_ids:
  - guard
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_causal_review_batch91.py
    role: test owner
  acceptance_checks:
  - Fail closed for wrong hashes or unavailable revisions.
  - Keep current SYNTROPHY and evidence-byte guards.
  - Add mutation/control/restore tests and rerun protected CI.
limitations:
- Self-review, not independent approval.
- No record-level science is re-reviewed; legacy review ledgers remain immutable.
- Auto-merge was disabled after the failure; no failed gate has been bypassed.
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261010T050841Z-pr937-after
  relationship: Later integration failure outside the earlier focused-test scope
links:
- https://github.com/CultureBotAI/CommunityMech/pull/937
- https://github.com/CultureBotAI/CommunityMech/issues/1984
```
