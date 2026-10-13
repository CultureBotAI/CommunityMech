# PR 1997 historical-cache integration review: before

- Review: 20261013T052657Z-1994-integration-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-13T05:26:57Z
- Finished UTC: 2026-10-13T05:26:57Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: false

## Summary

Reproduced all six PR integration failures.

## Scope And Provenance

The six integration failures in required CI on eabe5851c5af19bdabec42a46ccbd8fcd4989795.

Selection: All five failing causal-review test modules plus the guide policy owner.
Coverage: full; 6 reviewed / 6 in the declared population.
Source: working_tree at Git base eabe5851c5af19bdabec42a46ccbd8fcd4989795.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| tests/test_causal_review_batch15.py | tests/test_causal_review_batch15.py | maintained | tests/test_causal_review_batch15.py |
| tests/test_causal_review_batch48.py | tests/test_causal_review_batch48.py | maintained | tests/test_causal_review_batch48.py |
| tests/test_causal_review_batch64.py | tests/test_causal_review_batch64.py | maintained | tests/test_causal_review_batch64.py |
| tests/test_causal_review_batch88.py | tests/test_causal_review_batch88.py | maintained | tests/test_causal_review_batch88.py |
| tests/test_causal_review_batch92.py | tests/test_causal_review_batch92.py | maintained | tests/test_causal_review_batch92.py |
| CLAUDE.md | CLAUDE.md | maintained | CLAUDE.md |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused integration reproduction | failed | True | tests/test_causal_review_batch15.py, tests/test_causal_review_batch48.py, tests/test_causal_review_batch64.py, tests/test_causal_review_batch88.py, tests/test_causal_review_batch92.py, CLAUDE.md | 6 failed, 33 passed; failures match CI. |

## Scientific And Domain Assessments

### Historical inputs versus current source boundaries

provenance: concern. Targets: tests/test_causal_review_batch15.py.

Confirmed failing integration assertion.

### Historical inputs versus current source boundaries

provenance: concern. Targets: tests/test_causal_review_batch48.py.

Confirmed failing integration assertion.

### Historical inputs versus current source boundaries

provenance: concern. Targets: tests/test_causal_review_batch64.py.

Confirmed failing integration assertion.

### Historical inputs versus current source boundaries

provenance: concern. Targets: tests/test_causal_review_batch88.py.

Confirmed failing integration assertion.

### Historical inputs versus current source boundaries

provenance: concern. Targets: tests/test_causal_review_batch92.py.

Confirmed failing integration assertion.

### Historical inputs versus current source boundaries

provenance: concern. Targets: CLAUDE.md.

Confirmed failing integration assertion.

## Findings

### historical-cache-ci: Historical cache assertions block source-boundary repair

major / open / confirmed; issue key: 1998-historical-cache-ci.

Five historical cache checks incorrectly compare old digests with live files; a sixth guide-contract failure requires restoring the literal supplementary text wording without changing the corrected policy.

## Recommended Actions And Acceptance Checks

### repair

Bind cache hashes to recorded commits, preserve optional legacy-tree distinction, restore guide wording.

- Control/mutation/restoration checks reject wrong hashes, revision, tree and path.
- Current record assertions and old ledgers unchanged.
- Protected CI must pass before merge.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| integration | https://github.com/CultureBotAI/CommunityMech/actions/runs/38348079855 | supports | CI reported 6 failures and 4868 passes. Local control reproduced the same six failures. All 19 cache digests across the five ledgers match their recorded base_commit Git blobs. Repair not yet applied. |

## Limits And Additional Notes

- Self-review, not independent approval or scientific review.
- This is a local integration assessment, not a full-CI pass or release authorization.
- Native supplement-only validation failures remain open in #1996; no fallback added.
- Batch 15 has no recorded base_tree; its immutable full commit remains enforced explicitly.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T052657Z-1994-integration-before
kind: repository
repository: CultureBotAI/CommunityMech
title: 'PR 1997 historical-cache integration review: before'
started_at: '2026-10-13T05:26:57Z'
finished_at: '2026-10-13T05:26:57Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Same agent implements and reviews; not independent approval.
skill: pr-adversarial-review
completion: completed
verdict: needs_curation
scientific_review: false
summary: Reproduced all six PR integration failures.
source:
  git_revision: eabe5851c5af19bdabec42a46ccbd8fcd4989795
  state: working_tree
  inputs:
  - path: CLAUDE.md
    sha256: 4b0b8740d5a99b264d99d24c7ba19d7e22a404659b813011d90729d317de7c50
    role: target
  - path: reports/causal_graph_review/decisions/20261005-three-records-batch15.yaml
    sha256: 9a91951bf6002151122053f4d0ad0c13ada0c7b4f61bff989a612268c9750dc0
    role: context
  - path: reports/causal_graph_review/decisions/20261006-assay-boundaries-batch64.yaml
    sha256: c1ee5014ea7d83ad47d2a03e7392fb2e5f86722f7d29f90b1b132f41804982b4
    role: context
  - path: reports/causal_graph_review/decisions/20261006-ginseng-s11-batch48.yaml
    sha256: c36d6bc71789c7f48d2e2c93d66e5f587aea15dd5c2c7bc9665092074befae33
    role: context
  - path: reports/causal_graph_review/decisions/20261007-four-records-batch88.yaml
    sha256: ce41340909e65c676be7e53756385800335224b44432760dacd3a4ca98179429
    role: context
  - path: reports/causal_graph_review/decisions/20261007-four-records-batch92.yaml
    sha256: 73d40c40dca10b7548a1fe0346ea8de924df5bb224ae256fcba5b48912d1fff5
    role: context
  - path: tests/test_causal_review_batch15.py
    sha256: 57848b5c521e560c8a8ad8b09c33dd48f0289db5a1740cf251dee9c7f6346817
    role: target
  - path: tests/test_causal_review_batch48.py
    sha256: 94c3f6cf818fe5b1bb4883a65b2a94bd837860a2c627e01b531651f513311661
    role: target
  - path: tests/test_causal_review_batch64.py
    sha256: 4a864fd15d4cb6988952b8f1a31364989276e99280b2225a06c88e051f847b70
    role: target
  - path: tests/test_causal_review_batch88.py
    sha256: d5c366e8b3861feaabe007572761be4230532f05fe5a3e02d7b5b408c5476b5c
    role: target
  - path: tests/test_causal_review_batch91.py
    sha256: 43e1dfce5356c250f6932ee600631afe695bc45054dd5a1cb5224b67d56007f6
    role: context
  - path: tests/test_causal_review_batch92.py
    sha256: ae0fe5de3c7a381e9b268c3bf8f65179a7c257b3527f64a90838595a0bb56612
    role: target
  - path: tests/test_claude_guide_contract.py
    sha256: 7fb401954f3eab1612453ccda0d1b819b7fe8869663bbb28c416ca6034bcc728
    role: context
targets:
- target_id: tests/test_causal_review_batch15.py
  path: tests/test_causal_review_batch15.py
  label: tests/test_causal_review_batch15.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_causal_review_batch15.py
    role: maintained
- target_id: tests/test_causal_review_batch48.py
  path: tests/test_causal_review_batch48.py
  label: tests/test_causal_review_batch48.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_causal_review_batch48.py
    role: maintained
- target_id: tests/test_causal_review_batch64.py
  path: tests/test_causal_review_batch64.py
  label: tests/test_causal_review_batch64.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_causal_review_batch64.py
    role: maintained
- target_id: tests/test_causal_review_batch88.py
  path: tests/test_causal_review_batch88.py
  label: tests/test_causal_review_batch88.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_causal_review_batch88.py
    role: maintained
- target_id: tests/test_causal_review_batch92.py
  path: tests/test_causal_review_batch92.py
  label: tests/test_causal_review_batch92.py
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_causal_review_batch92.py
    role: maintained
- target_id: CLAUDE.md
  path: CLAUDE.md
  label: CLAUDE.md
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: CLAUDE.md
    role: maintained
scope:
  description: The six integration failures in required CI on eabe5851c5af19bdabec42a46ccbd8fcd4989795.
  selection: All five failing causal-review test modules plus the guide policy owner.
  coverage: full
  population_size: 6
  reviewed_target_ids:
  - tests/test_causal_review_batch15.py
  - tests/test_causal_review_batch48.py
  - tests/test_causal_review_batch64.py
  - tests/test_causal_review_batch88.py
  - tests/test_causal_review_batch92.py
  - CLAUDE.md
  exclusions:
  - target: Scientific claims, canonical records, native supplement routing
    reason: 'Unchanged; source-boundary reviews and #1996 cover the separate provenance
      limitation.'
checks:
- check_id: integration
  name: Focused integration reproduction
  status: failed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/communitymech-1994-uv-cache
    .venv/bin/python -m pytest tests/test_causal_review_batch15.py tests/test_causal_review_batch48.py
    tests/test_causal_review_batch64.py tests/test_causal_review_batch88.py tests/test_causal_review_batch92.py
    tests/test_claude_guide_contract.py -q --no-cov
  exit_code: 1
  expected_exit_code: 0
  summary: 6 failed, 33 passed; failures match CI.
  target_ids:
  - tests/test_causal_review_batch15.py
  - tests/test_causal_review_batch48.py
  - tests/test_causal_review_batch64.py
  - tests/test_causal_review_batch88.py
  - tests/test_causal_review_batch92.py
  - CLAUDE.md
  evidence_ids:
  - integration
evidence:
- evidence_id: integration
  kind: validation
  reference: https://github.com/CultureBotAI/CommunityMech/actions/runs/38348079855
  accessed_at: '2026-10-13T05:26:57Z'
  support: supports
  summary: CI reported 6 failures and 4868 passes. Local control reproduced the same
    six failures. All 19 cache digests across the five ledgers match their recorded
    base_commit Git blobs. Repair not yet applied.
assessments:
- assessment_id: target-0
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: concern
  target_ids:
  - tests/test_causal_review_batch15.py
  evidence_ids:
  - integration
  summary: Confirmed failing integration assertion.
- assessment_id: target-1
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: concern
  target_ids:
  - tests/test_causal_review_batch48.py
  evidence_ids:
  - integration
  summary: Confirmed failing integration assertion.
- assessment_id: target-2
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: concern
  target_ids:
  - tests/test_causal_review_batch64.py
  evidence_ids:
  - integration
  summary: Confirmed failing integration assertion.
- assessment_id: target-3
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: concern
  target_ids:
  - tests/test_causal_review_batch88.py
  evidence_ids:
  - integration
  summary: Confirmed failing integration assertion.
- assessment_id: target-4
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: concern
  target_ids:
  - tests/test_causal_review_batch92.py
  evidence_ids:
  - integration
  summary: Confirmed failing integration assertion.
- assessment_id: target-5
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: concern
  target_ids:
  - CLAUDE.md
  evidence_ids:
  - integration
  summary: Confirmed failing integration assertion.
findings:
- finding_id: historical-cache-ci
  issue_key: 1998-historical-cache-ci
  category: provenance
  severity: major
  status: open
  certainty: confirmed
  title: Historical cache assertions block source-boundary repair
  description: Five historical cache checks incorrectly compare old digests with live
    files; a sixth guide-contract failure requires restoring the literal supplementary
    text wording without changing the corrected policy.
  target_ids:
  - tests/test_causal_review_batch15.py
  - tests/test_causal_review_batch48.py
  - tests/test_causal_review_batch64.py
  - tests/test_causal_review_batch88.py
  - tests/test_causal_review_batch92.py
  - CLAUDE.md
  field_paths:
  - historical cache digest assertions
  - Evidence policy
  evidence_ids:
  - integration
  ownership_note: Five test modules and CLAUDE.md; old decision ledgers remain immutable.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1998
actions:
- action_id: repair
  description: Bind cache hashes to recorded commits, preserve optional legacy-tree
    distinction, restore guide wording.
  finding_ids:
  - historical-cache-ci
  target_ids:
  - tests/test_causal_review_batch15.py
  - tests/test_causal_review_batch48.py
  - tests/test_causal_review_batch64.py
  - tests/test_causal_review_batch88.py
  - tests/test_causal_review_batch92.py
  - CLAUDE.md
  ownership_note: Test helpers and six maintained target files.
  acceptance_checks:
  - Control/mutation/restoration checks reject wrong hashes, revision, tree and path.
  - Current record assertions and old ledgers unchanged.
  - Protected CI must pass before merge.
limitations:
- Self-review, not independent approval or scientific review.
- This is a local integration assessment, not a full-CI pass or release authorization.
- 'Native supplement-only validation failures remain open in #1996; no fallback added.'
- Batch 15 has no recorded base_tree; its immutable full commit remains enforced explicitly.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/1998
- https://github.com/CultureBotAI/CommunityMech/pull/1997
```
