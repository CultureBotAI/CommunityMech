# Okeke participant census after

- Review: 20261015T115628Z-okeke-census-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-15T11:56:23.467881Z
- Finished UTC: 2026-10-15T11:56:28.968586Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Track the CI-discovered participant-census omission without weakening any connectivity gate.

## Scope And Provenance

One maintained exact-set census and its integration with the Okeke repair.

Selection: Sole failing test in PR2018 run38725691675.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e92858eb2efc07bd6d76485d7212683a055ce96a.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| participant-census-okeke | tests/test_participating_taxa.py | maintained | Explicit participant census |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| census-after | passed | True | participant-census-okeke | Recorded focused checks passed. |
| census-lint | passed | True | participant-census-okeke | Recorded focused checks passed. |
| census-mutation | passed | True | participant-census-okeke | Recorded focused checks passed. |
| Revised PR and merge-queue checks | unavailable | True | participant-census-okeke | Fresh revised-head PR and queue checks must still pass; the original run failed and is not counted as green. |

## Scientific And Domain Assessments

### Explicit participant population and unchanged connectivity

consistency: supported. Targets: participant-census-okeke.

The explicit set includes exactly the new record and the independent connectivity survey is unchanged.

## Findings

### census-entry: Explicit participant census omitted the intentionally changed record

major / resolved / confirmed; issue key: okeke-participant-census-entry.

The new Okeke participant lists change the exact user set from 303 to 304, but USERS did not include the record.

Disposition: Added only Okeke to the measured explicit set; exact equality and all connectivity bounds remain unchanged. A controlled omission fails with green controls before and after restoration.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| census-after | reports/causal_graph_review/20261015-okeke-participants/census-after.json; command, timestamps, exit code and full output | supports | Focused regression and style verification after the explicit entry update. |
| census-lint | reports/causal_graph_review/20261015-okeke-participants/census-lint.json; command, timestamps, exit code and full output | supports | Focused regression and style verification after the explicit entry update. |
| census-mutation | reports/causal_graph_review/20261015-okeke-participants/census-mutation.json; command, timestamps, exit code and full output | supports | Focused regression and style verification after the explicit entry update. |
| measurement | reports/causal_graph_review/20261015-okeke-participants/census-measurement.json; Both-root before/after survey and explicit-user set difference | supports | Only Okeke joins the explicit-user set (303 to 304); every connectivity survey count is unchanged. |
| ci | https://github.com/CultureBotAI/CommunityMech/actions/runs/38725691675; Run tests, sole failure in test_the_corpus_is_unchanged_by_this_feature at 262d1716 | supports | First PR run: 1 failed, 4962 passed, 86 skipped, 8 deselected; the local scoped suite had omitted this module. |

## Limits And Additional Notes

- Technical regression review only; literature and scientific completeness were not reassessed.
- Original scientific review and needs_research status remain unchanged; issues1657 and1658 remain open.
- Local checks do not replace revised-head PR and protected queue validation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T115628Z-okeke-census-after
kind: repository
repository: CultureBotAI/CommunityMech
title: Okeke participant census after
started_at: '2026-10-15T11:56:23.467881Z'
finished_at: '2026-10-15T11:56:28.968586Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Implementing-agent technical adversarial review; no independent
    approval.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
scientific_review: false
summary: Track the CI-discovered participant-census omission without weakening any
  connectivity gate.
source:
  git_revision: e92858eb2efc07bd6d76485d7212683a055ce96a
  state: working_tree
  inputs:
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
    sha256: 49138a663308a7331c64b2be0a72a6127ad800063b78a7648c27712fc9dd87ef
    role: context
  - path: reports/causal_graph_review/20261015-okeke-participants/census-after.json
    sha256: a3cb9993eeec69bcd375dc4599d19f687cd9b48ea85466851f36eaab6463e9d5
    role: context
  - path: reports/causal_graph_review/20261015-okeke-participants/census-before.json
    sha256: 35f3279f654aff683f54fb0830867eabe08969d0030a01fb903aa1d2dffe4ed2
    role: context
  - path: reports/causal_graph_review/20261015-okeke-participants/census-lint.json
    sha256: 84582af184ec62f60584ac02275cbf5f17c789efde787c8c3f5d95d4676204af
    role: context
  - path: reports/causal_graph_review/20261015-okeke-participants/census-measurement.json
    sha256: 5a4d55159f03f064bb6fee4cee43a9557ef0ede4575d302c3d19257c12707025
    role: context
  - path: reports/causal_graph_review/20261015-okeke-participants/census-mutation.json
    sha256: 6ae2cf6b95a36174c3fa4c04236473a416794c5f6ceb74bae26c01c673c07117
    role: context
  - path: reviews/structured/20261015T115235Z-okeke-census-before/review.yaml
    sha256: 1b27e168dcb179b71d1234f22273a052b1066777e2164b5e982eceff96b98ab8
    role: context
  - path: tests/test_community_level_connectivity_credit.py
    sha256: 69af5ff490cde0307d60a1d59389647a158f9d7f16c9f11796c7bf48480747ce
    role: context
  - path: tests/test_okeke_participant_census.py
    sha256: e024605da9262d532d07c8dafe6b8aa173d4b0bca0d0d7ebe75cd8239f383a7e
    role: context
  - path: tests/test_participating_taxa.py
    sha256: e9634f8ae5ee8c2685885a5314e92ebaa46124a718c088af583818390ec9550e
    role: target
targets:
- kind: maintained
  label: Explicit participant census
  owner_paths:
  - path: tests/test_participating_taxa.py
    repository: CultureBotAI/CommunityMech
    role: maintained_test
  path: tests/test_participating_taxa.py
  target_id: participant-census-okeke
scope:
  description: One maintained exact-set census and its integration with the Okeke
    repair.
  selection: Sole failing test in PR2018 run38725691675.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - participant-census-okeke
checks:
- check_id: census-after
  name: census-after
  status: passed
  required: true
  target_ids:
  - participant-census-okeke
  evidence_ids:
  - census-after
  command: .venv/bin/pytest tests/test_participating_taxa.py tests/test_community_level_connectivity_credit.py
    tests/test_okeke_participant_census.py tests/test_okeke_assay_participants.py
    tests/test_causal_review_batch79.py tests/test_causal_review_inventory.py tests/test_network_auditor.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  summary: Recorded focused checks passed.
- check_id: census-lint
  name: census-lint
  status: passed
  required: true
  target_ids:
  - participant-census-okeke
  evidence_ids:
  - census-lint
  command: just --no-dotenv lint
  exit_code: 0
  expected_exit_code: 0
  summary: Recorded focused checks passed.
- check_id: census-mutation
  name: census-mutation
  status: passed
  required: true
  target_ids:
  - participant-census-okeke
  evidence_ids:
  - census-mutation
  command: .venv/bin/pytest tests/test_okeke_participant_census.py -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  summary: Recorded focused checks passed.
- check_id: protected-ci
  name: Revised PR and merge-queue checks
  status: unavailable
  required: true
  target_ids:
  - participant-census-okeke
  evidence_ids:
  - ci
  summary: Fresh revised-head PR and queue checks must still pass; the original run
    failed and is not counted as green.
evidence:
- evidence_id: census-after
  kind: validation
  reference: reports/causal_graph_review/20261015-okeke-participants/census-after.json
  locator: command, timestamps, exit code and full output
  accessed_at: '2026-10-15T11:56:28.968586Z'
  support: supports
  summary: Focused regression and style verification after the explicit entry update.
- evidence_id: census-lint
  kind: validation
  reference: reports/causal_graph_review/20261015-okeke-participants/census-lint.json
  locator: command, timestamps, exit code and full output
  accessed_at: '2026-10-15T11:56:28.968586Z'
  support: supports
  summary: Focused regression and style verification after the explicit entry update.
- evidence_id: census-mutation
  kind: validation
  reference: reports/causal_graph_review/20261015-okeke-participants/census-mutation.json
  locator: command, timestamps, exit code and full output
  accessed_at: '2026-10-15T11:56:28.968586Z'
  support: supports
  summary: Focused regression and style verification after the explicit entry update.
- evidence_id: measurement
  kind: validation
  reference: reports/causal_graph_review/20261015-okeke-participants/census-measurement.json
  locator: Both-root before/after survey and explicit-user set difference
  accessed_at: '2026-10-15T11:56:28.968586Z'
  support: supports
  summary: Only Okeke joins the explicit-user set (303 to 304); every connectivity
    survey count is unchanged.
- evidence_id: ci
  kind: validation
  reference: https://github.com/CultureBotAI/CommunityMech/actions/runs/38725691675
  locator: Run tests, sole failure in test_the_corpus_is_unchanged_by_this_feature
    at 262d1716
  accessed_at: '2026-10-15T11:56:28.968586Z'
  support: supports
  summary: 'First PR run: 1 failed, 4962 passed, 86 skipped, 8 deselected; the local
    scoped suite had omitted this module.'
assessments:
- assessment_id: census
  area: consistency
  topic: Explicit participant population and unchanged connectivity
  outcome: supported
  target_ids:
  - participant-census-okeke
  evidence_ids:
  - census-after
  - measurement
  summary: The explicit set includes exactly the new record and the independent connectivity
    survey is unchanged.
findings:
- finding_id: census-entry
  issue_key: okeke-participant-census-entry
  title: Explicit participant census omitted the intentionally changed record
  description: The new Okeke participant lists change the exact user set from 303
    to 304, but USERS did not include the record.
  category: consistency
  severity: major
  status: resolved
  certainty: confirmed
  target_ids:
  - participant-census-okeke
  field_paths:
  - USERS
  evidence_ids:
  - census-after
  - measurement
  - ci
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_participating_taxa.py
    role: maintained_test
  rule_id: participant-census-exact-set
  native_severity: P2
  normalization_reason: Deterministic required CI failure blocks publication of this
    curation change.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2019
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T115235Z-okeke-census-before
    finding_id: census-entry
  disposition_reason: Added only Okeke to the measured explicit set; exact equality
    and all connectivity bounds remain unchanged. A controlled omission fails with
    green controls before and after restoration.
actions: []
limitations:
- Technical regression review only; literature and scientific completeness were not
  reassessed.
- Original scientific review and needs_research status remain unchanged; issues1657
  and1658 remain open.
- Local checks do not replace revised-head PR and protected queue validation.
```
