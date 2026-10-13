# PR 1997 historical-cache integration review: after

- Review: 20261013T052919Z-1994-integration-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-13T05:29:19Z
- Finished UTC: 2026-10-13T05:29:19Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

The scoped historical-cache and guide-contract regressions are repaired without rewriting prior evidence. Protected CI remains a separate merge prerequisite.

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
| Focused integration reproduction | passed | True | tests/test_causal_review_batch15.py, tests/test_causal_review_batch48.py, tests/test_causal_review_batch64.py, tests/test_causal_review_batch88.py, tests/test_causal_review_batch92.py, CLAUDE.md | 51 passed in 23.44s after formatting, including 12 control/mutation/restoration provenance tests. The same 39 integration tests previously produced 6 failures and 33 passes. Lint passes Black (388 files), Ruff and mypy (49 source files); historical byte verification passes all 11 repaired caches and unchanged records. |

## Scientific And Domain Assessments

### Historical inputs versus current source boundaries

provenance: supported. Targets: tests/test_causal_review_batch15.py.

Historical provenance remains enforced while current source-boundary repair is permitted; scientific assertions are not relaxed.

### Historical inputs versus current source boundaries

provenance: supported. Targets: tests/test_causal_review_batch48.py.

Historical provenance remains enforced while current source-boundary repair is permitted; scientific assertions are not relaxed.

### Historical inputs versus current source boundaries

provenance: supported. Targets: tests/test_causal_review_batch64.py.

Historical provenance remains enforced while current source-boundary repair is permitted; scientific assertions are not relaxed.

### Historical inputs versus current source boundaries

provenance: supported. Targets: tests/test_causal_review_batch88.py.

Historical provenance remains enforced while current source-boundary repair is permitted; scientific assertions are not relaxed.

### Historical inputs versus current source boundaries

provenance: supported. Targets: tests/test_causal_review_batch92.py.

Historical provenance remains enforced while current source-boundary repair is permitted; scientific assertions are not relaxed.

### Historical inputs versus current source boundaries

provenance: supported. Targets: CLAUDE.md.

Historical provenance remains enforced while current source-boundary repair is permitted; scientific assertions are not relaxed.

## Findings

### historical-cache-ci: Historical cache assertions block source-boundary repair

major / resolved / confirmed; issue key: 1998-historical-cache-ci.

Five historical cache checks incorrectly compare old digests with live files; a sixth guide-contract failure requires restoring the literal supplementary text wording without changing the corrected policy.

Disposition: Historical source hashes now use immutable recorded Git blobs with fail-closed provenance checks. Batch 15 explicitly permits its legacy commit-only ledger; other batches require recorded trees. Current record and non-cache artifact assertions remain enforced. Supplementary text wording restored. Old ledgers, canonical records, caches and earlier saved reviews unchanged by this integration repair.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| integration | https://github.com/CultureBotAI/CommunityMech/actions/runs/38348079855 | supports | CI reported 6 failures and 4868 passes. Local control reproduced the same six failures. All 19 cache digests across the five ledgers match their recorded base_commit Git blobs. 51 passed in 23.44s after formatting, including 12 control/mutation/restoration provenance tests. The same 39 integration tests previously produced 6 failures and 33 passes. Lint passes Black (388 files), Ruff and mypy (49 source files); historical byte verification passes all 11 repaired caches and unchanged records. |

## Limits And Additional Notes

- Self-review, not independent approval or scientific review.
- This is a local integration assessment, not a full-CI pass or release authorization.
- Native supplement-only validation failures remain open in #1996; no fallback added.
- Batch 15 has no recorded base_tree; its immutable full commit remains enforced explicitly.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261013T052919Z-1994-integration-after
kind: repository
repository: CultureBotAI/CommunityMech
title: 'PR 1997 historical-cache integration review: after'
started_at: '2026-10-13T05:29:19Z'
finished_at: '2026-10-13T05:29:19Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Same agent implements and reviews; not independent approval.
skill: pr-adversarial-review
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: The scoped historical-cache and guide-contract regressions are repaired without
  rewriting prior evidence. Protected CI remains a separate merge prerequisite.
source:
  git_revision: eabe5851c5af19bdabec42a46ccbd8fcd4989795
  state: working_tree
  inputs:
  - path: CLAUDE.md
    sha256: 8458fc2ca6663fea0e94c8e5b79730aafe6f4b3ac2c0f1079a3b64a2bb4d3d98
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
  - path: tests/historical_cache.py
    sha256: 806f371f38e1def7cec87b5756be3419d278aa92412b922e5451e3099f0eed3c
    role: context
  - path: tests/test_causal_review_batch15.py
    sha256: 89c823b38000ed9b77422c1d98475837f48b65d76c0a424f79397b7c15282117
    role: target
  - path: tests/test_causal_review_batch48.py
    sha256: 45465e7e27ab52f0eaff635a302b971d57bc5b30382a792469a22e6e1fde313e
    role: target
  - path: tests/test_causal_review_batch64.py
    sha256: 236ecb2e34ebbc328e5d96104d0bc41787484de6142f4285e869b7ec7b27aafc
    role: target
  - path: tests/test_causal_review_batch88.py
    sha256: 6c3b2f3284005dca3cf31162840950c60a92e79f16eeed650c7dbe98b52529f2
    role: target
  - path: tests/test_causal_review_batch91.py
    sha256: 43e1dfce5356c250f6932ee600631afe695bc45054dd5a1cb5224b67d56007f6
    role: context
  - path: tests/test_causal_review_batch92.py
    sha256: e1eb04d2b093712284692bc14aa39d15b586e8de94886f9d7f5e6fcbf0685523
    role: target
  - path: tests/test_claude_guide_contract.py
    sha256: 7fb401954f3eab1612453ccda0d1b819b7fe8869663bbb28c416ca6034bcc728
    role: context
  - path: tests/test_historical_cache.py
    sha256: 7ddb11db7c00a2eb28f759b00dbccf5aaafe249402c013636982ad3d3eb0c8c6
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
  status: passed
  required: true
  command: env UV_NO_SYNC=1 UV_CACHE_DIR=/private/tmp/communitymech-1994-uv-cache
    .venv/bin/python -m pytest tests/test_causal_review_batch15.py tests/test_causal_review_batch48.py
    tests/test_causal_review_batch64.py tests/test_causal_review_batch88.py tests/test_causal_review_batch92.py
    tests/test_claude_guide_contract.py tests/test_historical_cache.py -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  summary: 51 passed in 23.44s after formatting, including 12 control/mutation/restoration
    provenance tests. The same 39 integration tests previously produced 6 failures
    and 33 passes. Lint passes Black (388 files), Ruff and mypy (49 source files);
    historical byte verification passes all 11 repaired caches and unchanged records.
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
  accessed_at: '2026-10-13T05:29:19Z'
  support: supports
  summary: CI reported 6 failures and 4868 passes. Local control reproduced the same
    six failures. All 19 cache digests across the five ledgers match their recorded
    base_commit Git blobs. 51 passed in 23.44s after formatting, including 12 control/mutation/restoration
    provenance tests. The same 39 integration tests previously produced 6 failures
    and 33 passes. Lint passes Black (388 files), Ruff and mypy (49 source files);
    historical byte verification passes all 11 repaired caches and unchanged records.
assessments:
- assessment_id: target-0
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: supported
  target_ids:
  - tests/test_causal_review_batch15.py
  evidence_ids:
  - integration
  summary: Historical provenance remains enforced while current source-boundary repair
    is permitted; scientific assertions are not relaxed.
- assessment_id: target-1
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: supported
  target_ids:
  - tests/test_causal_review_batch48.py
  evidence_ids:
  - integration
  summary: Historical provenance remains enforced while current source-boundary repair
    is permitted; scientific assertions are not relaxed.
- assessment_id: target-2
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: supported
  target_ids:
  - tests/test_causal_review_batch64.py
  evidence_ids:
  - integration
  summary: Historical provenance remains enforced while current source-boundary repair
    is permitted; scientific assertions are not relaxed.
- assessment_id: target-3
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: supported
  target_ids:
  - tests/test_causal_review_batch88.py
  evidence_ids:
  - integration
  summary: Historical provenance remains enforced while current source-boundary repair
    is permitted; scientific assertions are not relaxed.
- assessment_id: target-4
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: supported
  target_ids:
  - tests/test_causal_review_batch92.py
  evidence_ids:
  - integration
  summary: Historical provenance remains enforced while current source-boundary repair
    is permitted; scientific assertions are not relaxed.
- assessment_id: target-5
  area: provenance
  topic: Historical inputs versus current source boundaries
  outcome: supported
  target_ids:
  - CLAUDE.md
  evidence_ids:
  - integration
  summary: Historical provenance remains enforced while current source-boundary repair
    is permitted; scientific assertions are not relaxed.
findings:
- finding_id: historical-cache-ci
  issue_key: 1998-historical-cache-ci
  category: provenance
  severity: major
  status: resolved
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
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261013T052657Z-1994-integration-before
    finding_id: historical-cache-ci
  disposition_reason: Historical source hashes now use immutable recorded Git blobs
    with fail-closed provenance checks. Batch 15 explicitly permits its legacy commit-only
    ledger; other batches require recorded trees. Current record and non-cache artifact
    assertions remain enforced. Supplementary text wording restored. Old ledgers,
    canonical records, caches and earlier saved reviews unchanged by this integration
    repair.
actions: []
limitations:
- Self-review, not independent approval or scientific review.
- This is a local integration assessment, not a full-CI pass or release authorization.
- 'Native supplement-only validation failures remain open in #1996; no fallback added.'
- Batch 15 has no recorded base_tree; its immutable full commit remains enforced explicitly.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/1998
- https://github.com/CultureBotAI/CommunityMech/pull/1997
```
