# PR 935: relevance and adversarial review

- Review: 20261010T074356Z-pr935-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-10T07:43:56Z
- Finished UTC: 2026-10-10T07:43:56Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Still relevant, not merge-ready: preserves an unfixed main coverage correction, but map inputs are stale and the real graph gate is deployment-only.

## Scope And Provenance

Risk-focused review of PR 935 against current main 01013cc1776136f2fc4a36a761b0d8c338e3a706.

Selection: Maintained implementation, generated-artifact provenance, and source-backed record assertions implicated by the PR.
Coverage: partial; 6 reviewed / 59 in the declared population.
Source: git_commit at Git base 91550e96300f805e08e8fb2a394a6abc7f33c9f7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| text-bundle | data/text_map/current.json | generated | text-bundle |
| site-policy | src/communitymech/text_map_site.py | maintained | site-policy |
| deployment | .github/workflows/generate-pages.yaml | maintained | deployment |
| graph-checker | scripts/check_graph_receipts.py | maintained | graph-checker |
| aggregation | src/communitymech/embedding/aggregator.py | maintained | aggregation |
| graph-receipt | docs/community_umap.metadata.json | generated | graph-receipt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| focused-regressions | passed | True | site-policy, graph-checker, aggregation | 33 text-map/receipt tests plus 9 numerical/source/aggregation/Graphviz tests passed, 42 total. |
| own-head-receipts | passed | True | text-bundle, graph-receipt, graph-checker | Actual committed graph checker passes both 373-point maps, and the BGE bundle validates against its own 378-record source snapshot. |
| current-main-artifact-compatibility | failed | True | text-bundle, graph-receipt, site-policy | BGE input validation fails against current main; both graph corpus receipts disagree with current corpus bytes/population. |
| premerge-receipt-gate | failed | True | deployment, graph-checker | Ignored-file-inclusive search of workflows, scripts, tests, and justfile confirms the real checker is invoked only by deployment; fixture tests do not validate committed artifacts. |
| integrated-full-suite | unavailable | True | site-policy, deployment, aggregation | Seven merge-conflict paths remain; no full integrated suite or heavy BGE/PaCMAP rebuild was performed. |

## Scientific And Domain Assessments

### Real requested-taxon denominator

quantity: supported. Targets: aggregation.

The underlying bug is still present on main and this change is relevant; focused tests verify true missing-taxon coverage and duplicate-ID behavior.

### Current corpus compatibility

provenance: concern. Targets: text-bundle, graph-receipt, site-policy.

Old-head maps are internally valid but not publishable against the current main corpus.

### Premerge publication readiness

consistency: concern. Targets: deployment, graph-checker.

Deployment detects stale graph artifacts too late; required premerge checks need to run the real read-only checker.

## Findings

### pr935-stale-current-main-artifacts: Rebuild all three maps against the current integrated corpus before enabling publication

blocker / open / confirmed; issue key: pr935-stale-current-main-artifacts.

The enabled BGE bundle passes at the PR head with 378 records but production validate_bundle rejects current-main inputs as stale: main has 460 records, with 82 added and 371 existing semantic texts changed. Both graph receipts describe 374 community inputs and 373 points, versus 456 current communities. Resolving textual merge conflicts alone cannot satisfy prepare_text_map or graph receipt checks; regenerate source-bound maps, ledgers, receipts, and pages together from the merged input snapshot.

### pr935-premerge-graph-gate: Run real graph receipt validation before merge, not only during deployment

major / open / confirmed; issue key: pr935-premerge-graph-gate.

The only workflow invocation of scripts/check_graph_receipts.py is the main-push Pages deployment. tests/test_graph_receipt_site.py exercises synthetic graph_site roots, not the committed site. A corpus change confined to evidence/comments can leave semantic input unchanged, satisfy the text-map check, and leave stale graph hashes undetected until after merge, blocking Pages. Wire a read-only real-corpus receipt check into a required pull_request/merge_group gate and add a real-artifact drift regression.

## Recommended Actions And Acceptance Checks

### pr935-stale-current-main-artifacts-repair

Rebuild all three maps against the current integrated corpus before enabling publication

- Correct the specific defect without weakening provenance or scientific evidence requirements.
- Add a regression or source-linked assertion check demonstrating the failure and correction.
- Rebase onto current main and pass required exact-head and merge-group checks.

### pr935-premerge-graph-gate-repair

Run real graph receipt validation before merge, not only during deployment

- Correct the specific defect without weakening provenance or scientific evidence requirements.
- Add a regression or source-linked assertion check demonstrating the failure and correction.
- Rebase onto current main and pass required exact-head and merge-group checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| map-reproduction | scripts/embedding_pipeline.py; validate_bundle against freshly exported PR and current-main JSONL; graph corpus_receipt comparisons | supports | Production verifier: PR inputs 378 pass; current-main inputs 460 fail with map is stale relative to current adapter input. 82 added, zero removed, 371 changed semantic hashes. Graph receipts: 374 old inputs/373 points versus 456 current communities; actual own-head graph checker passes. Compared against a checkout whose tree exactly matches main 01013cc1. |
| gate-routing | .github/workflows/generate-pages.yaml; push main trigger and graph receipt command; fixture-only tests/test_graph_receipt_site.py | supports | No pull_request/merge_group invocation of the real graph checker was found in the scoped ignored-file-inclusive search. The full pytest suite only exercises checker fixtures. |
| tests | tests/test_graph_projection_correctness.py | supports | 42 focused tests pass after preparing an isolated Python 3.13 environment with numpy/pandas/scikit-learn and repo-compatible LinkML; the initial missing-numpy collection error was an environment issue, not a PR defect. |
| relevance | https://github.com/CultureBotAI/CommunityMech/issues/900 | supports | Issue 900 is still open, and current main still defaults exclude_hosts=True and treats all absent vectors as host exclusions/100% coverage. This PR fixes that behavior. The related CLAW rollout PR 432 remains open; PR 935 is still draft. |

## Limits And Additional Notes

- No model weights were downloaded, provider credits spent, numerical maps rebuilt, or browser visual QA performed.
- The review covers high-risk integration/provenance behavior, not every line of the 59-file PR or fleet-wide governed-byte compatibility.
- Review-only: no curated source changes, GitHub review submission, issue creation, merge, or branch deletion.
- Review bundles are local and uncommitted in isolated detached worktrees.
- No full integrated-suite or protected merge-group run; both branches have merge conflicts with current main.
- This is a bounded PR review, not a completed per-record scientific certification or a full native P1-P4 completeness scoring exercise.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T074356Z-pr935-review
kind: repository
repository: CultureBotAI/CommunityMech
title: 'PR 935: relevance and adversarial review'
started_at: '2026-10-10T07:43:56Z'
finished_at: '2026-10-10T07:43:56Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Read-only agent review of an existing PR. No independent human
    approval or separation from all historical authorship is claimed.
skill: pr-adversarial-review
completion: partial
verdict: needs_curation
scientific_review: false
summary: 'Still relevant, not merge-ready: preserves an unfixed main coverage correction,
  but map inputs are stale and the real graph gate is deployment-only.'
source:
  git_revision: 91550e96300f805e08e8fb2a394a6abc7f33c9f7
  state: git_commit
  inputs:
  - path: .github/workflows/generate-pages.yaml
    sha256: fb6373a0694bb547470a82a84575e48bf8f619bddd43dfd0870afb63c7a6ff21
    role: target
  - path: conf/text_map.yaml
    sha256: bc21e0ff78a08d8a8436fc400095a96a9a530f8f520913eefcc2c326c744704f
    role: context
  - path: data/text_map/current.json
    sha256: ef2554501a8c12e7ef64a03a90e0d776bfa1dbce2ad1492f3922b7b0a5183873
    role: target
  - path: docs/community_graph.metadata.json
    sha256: f6f5b9c24883ff5cfa9546f82b312d2452c5c673d172a8cd493b82f26785220f
    role: context
  - path: docs/community_umap.metadata.json
    sha256: 07e4b22c4bc9eb11d581d80b66f51623318fc0012f9983a720a76bc2c3329216
    role: target
  - path: scripts/check_graph_receipts.py
    sha256: 3b27a1fbf4260082a9144c19e70ec0a12403074f1b288f7c09b2005f3515ad85
    role: target
  - path: scripts/embedding_pipeline.py
    sha256: 9ef7708303150938c8f2c2a81885d9184ed0a7af0a78d9acc88c01224339b5fe
    role: context
  - path: src/communitymech/embedding/aggregator.py
    sha256: 59a1de77313941fded71d29857ca2c3740f08a9a15b7407e92d10d19753c7802
    role: target
  - path: src/communitymech/graph_embedding_receipts.py
    sha256: a05bd278bc09c3a9b4948da4cb27dd42105f8bca543d8b920d391142b5da8b37
    role: context
  - path: src/communitymech/text_map_inputs.py
    sha256: 4362d3bc819527509f3f3e999a45bf354109286418d633682381ef05f4be7f4f
    role: context
  - path: src/communitymech/text_map_site.py
    sha256: c701feff8b3abdfac1a289803685214628393827d985844ba92330ae0f0f3014
    role: target
  - path: src/communitymech/visualization/umap_generator.py
    sha256: 0c5a0a5d0715d30871e318babd70a89f3893befdfadd6f2c69a106235b4f1884
    role: context
  - path: tests/test_graph_receipt_site.py
    sha256: fe274a44fffd99e7c9a0b4d70f3cd1d85ac4cf9ff4c3ed6411693892d35e38e3
    role: context
targets:
- target_id: text-bundle
  path: data/text_map/current.json
  kind: generated
  label: text-bundle
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: scripts/embedding_pipeline.py
    role: maintained source owner
- target_id: site-policy
  path: src/communitymech/text_map_site.py
  kind: maintained
  label: site-policy
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/text_map_site.py
    role: maintained source owner
- target_id: deployment
  path: .github/workflows/generate-pages.yaml
  kind: maintained
  label: deployment
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: .github/workflows/generate-pages.yaml
    role: maintained source owner
- target_id: graph-checker
  path: scripts/check_graph_receipts.py
  kind: maintained
  label: graph-checker
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: scripts/check_graph_receipts.py
    role: maintained source owner
- target_id: aggregation
  path: src/communitymech/embedding/aggregator.py
  kind: maintained
  label: aggregation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/embedding/aggregator.py
    role: maintained source owner
- target_id: graph-receipt
  path: docs/community_umap.metadata.json
  kind: generated
  label: graph-receipt
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/visualization/umap_generator.py
    role: maintained source owner
scope:
  description: Risk-focused review of PR 935 against current main 01013cc1776136f2fc4a36a761b0d8c338e3a706.
  selection: Maintained implementation, generated-artifact provenance, and source-backed
    record assertions implicated by the PR.
  coverage: partial
  population_size: 59
  reviewed_target_ids:
  - text-bundle
  - site-policy
  - deployment
  - graph-checker
  - aggregation
  - graph-receipt
checks:
- check_id: focused-regressions
  name: focused-regressions
  status: passed
  required: true
  summary: 33 text-map/receipt tests plus 9 numerical/source/aggregation/Graphviz
    tests passed, 42 total.
  target_ids:
  - site-policy
  - graph-checker
  - aggregation
  evidence_ids:
  - tests
- check_id: own-head-receipts
  name: own-head-receipts
  status: passed
  required: true
  summary: Actual committed graph checker passes both 373-point maps, and the BGE
    bundle validates against its own 378-record source snapshot.
  target_ids:
  - text-bundle
  - graph-receipt
  - graph-checker
  evidence_ids:
  - map-reproduction
- check_id: current-main-artifact-compatibility
  name: current-main-artifact-compatibility
  status: failed
  required: true
  summary: BGE input validation fails against current main; both graph corpus receipts
    disagree with current corpus bytes/population.
  target_ids:
  - text-bundle
  - graph-receipt
  - site-policy
  evidence_ids:
  - map-reproduction
- check_id: premerge-receipt-gate
  name: premerge-receipt-gate
  status: failed
  required: true
  summary: Ignored-file-inclusive search of workflows, scripts, tests, and justfile
    confirms the real checker is invoked only by deployment; fixture tests do not
    validate committed artifacts.
  target_ids:
  - deployment
  - graph-checker
  evidence_ids:
  - gate-routing
- check_id: integrated-full-suite
  name: integrated-full-suite
  status: unavailable
  required: true
  summary: Seven merge-conflict paths remain; no full integrated suite or heavy BGE/PaCMAP
    rebuild was performed.
  target_ids:
  - site-policy
  - deployment
  - aggregation
  evidence_ids: []
evidence:
- evidence_id: map-reproduction
  kind: validation
  reference: scripts/embedding_pipeline.py
  support: supports
  locator: validate_bundle against freshly exported PR and current-main JSONL; graph
    corpus_receipt comparisons
  summary: 'Production verifier: PR inputs 378 pass; current-main inputs 460 fail
    with map is stale relative to current adapter input. 82 added, zero removed, 371
    changed semantic hashes. Graph receipts: 374 old inputs/373 points versus 456
    current communities; actual own-head graph checker passes. Compared against a
    checkout whose tree exactly matches main 01013cc1.'
  accessed_at: '2026-10-10T07:43:56Z'
- evidence_id: gate-routing
  kind: record_content
  reference: .github/workflows/generate-pages.yaml
  support: supports
  locator: push main trigger and graph receipt command; fixture-only tests/test_graph_receipt_site.py
  summary: No pull_request/merge_group invocation of the real graph checker was found
    in the scoped ignored-file-inclusive search. The full pytest suite only exercises
    checker fixtures.
  accessed_at: '2026-10-10T07:43:56Z'
- evidence_id: tests
  kind: validation
  reference: tests/test_graph_projection_correctness.py
  support: supports
  summary: 42 focused tests pass after preparing an isolated Python 3.13 environment
    with numpy/pandas/scikit-learn and repo-compatible LinkML; the initial missing-numpy
    collection error was an environment issue, not a PR defect.
  accessed_at: '2026-10-10T07:43:56Z'
- evidence_id: relevance
  kind: record_content
  reference: https://github.com/CultureBotAI/CommunityMech/issues/900
  support: supports
  summary: Issue 900 is still open, and current main still defaults exclude_hosts=True
    and treats all absent vectors as host exclusions/100% coverage. This PR fixes
    that behavior. The related CLAW rollout PR 432 remains open; PR 935 is still draft.
  accessed_at: '2026-10-10T07:43:56Z'
assessments:
- assessment_id: coverage-fix
  area: quantity
  topic: Real requested-taxon denominator
  outcome: supported
  target_ids:
  - aggregation
  evidence_ids:
  - tests
  - relevance
  summary: The underlying bug is still present on main and this change is relevant;
    focused tests verify true missing-taxon coverage and duplicate-ID behavior.
- assessment_id: artifact-integration
  area: provenance
  topic: Current corpus compatibility
  outcome: concern
  target_ids:
  - text-bundle
  - graph-receipt
  - site-policy
  evidence_ids:
  - map-reproduction
  summary: Old-head maps are internally valid but not publishable against the current
    main corpus.
- assessment_id: gate-timing
  area: consistency
  topic: Premerge publication readiness
  outcome: concern
  target_ids:
  - deployment
  - graph-checker
  evidence_ids:
  - gate-routing
  summary: Deployment detects stale graph artifacts too late; required premerge checks
    need to run the real read-only checker.
findings:
- finding_id: pr935-stale-current-main-artifacts
  issue_key: pr935-stale-current-main-artifacts
  title: Rebuild all three maps against the current integrated corpus before enabling
    publication
  description: 'The enabled BGE bundle passes at the PR head with 378 records but
    production validate_bundle rejects current-main inputs as stale: main has 460
    records, with 82 added and 371 existing semantic texts changed. Both graph receipts
    describe 374 community inputs and 373 points, versus 456 current communities.
    Resolving textual merge conflicts alone cannot satisfy prepare_text_map or graph
    receipt checks; regenerate source-bound maps, ledgers, receipts, and pages together
    from the merged input snapshot.'
  category: consistency
  severity: blocker
  status: open
  certainty: confirmed
  target_ids:
  - text-bundle
  - graph-receipt
  - site-policy
  field_paths:
  - data/text_map/current.json (line 1)
  - prepare_text_map (lines 75-81)
  - docs/community_umap.metadata.json (line 1)
  evidence_ids:
  - map-reproduction
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: scripts/embedding_pipeline.py
    role: maintained source owner
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/visualization/umap_generator.py
    role: maintained source owner
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/text_map_site.py
    role: maintained source owner
  native_severity: P1
  normalization_reason: Prevents publication of the integrated repository.
- finding_id: pr935-premerge-graph-gate
  issue_key: pr935-premerge-graph-gate
  title: Run real graph receipt validation before merge, not only during deployment
  description: The only workflow invocation of scripts/check_graph_receipts.py is
    the main-push Pages deployment. tests/test_graph_receipt_site.py exercises synthetic
    graph_site roots, not the committed site. A corpus change confined to evidence/comments
    can leave semantic input unchanged, satisfy the text-map check, and leave stale
    graph hashes undetected until after merge, blocking Pages. Wire a read-only real-corpus
    receipt check into a required pull_request/merge_group gate and add a real-artifact
    drift regression.
  category: consistency
  severity: major
  status: open
  certainty: confirmed
  target_ids:
  - deployment
  - graph-checker
  field_paths:
  - .github/workflows/generate-pages.yaml (lines 60-61)
  - tests/test_graph_receipt_site.py (lines 90-113)
  evidence_ids:
  - gate-routing
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: .github/workflows/generate-pages.yaml
    role: maintained source owner
  - repository: CultureBotAI/CommunityMech
    path: scripts/check_graph_receipts.py
    role: maintained source owner
  native_severity: P2
  normalization_reason: Misrepresents structured evidence or permits a post-merge
    publication failure.
actions:
- action_id: pr935-stale-current-main-artifacts-repair
  description: Rebuild all three maps against the current integrated corpus before
    enabling publication
  target_ids:
  - text-bundle
  - graph-receipt
  - site-policy
  finding_ids:
  - pr935-stale-current-main-artifacts
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: scripts/embedding_pipeline.py
    role: maintained source owner
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/visualization/umap_generator.py
    role: maintained source owner
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/text_map_site.py
    role: maintained source owner
  acceptance_checks:
  - Correct the specific defect without weakening provenance or scientific evidence
    requirements.
  - Add a regression or source-linked assertion check demonstrating the failure and
    correction.
  - Rebase onto current main and pass required exact-head and merge-group checks.
- action_id: pr935-premerge-graph-gate-repair
  description: Run real graph receipt validation before merge, not only during deployment
  target_ids:
  - deployment
  - graph-checker
  finding_ids:
  - pr935-premerge-graph-gate
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: .github/workflows/generate-pages.yaml
    role: maintained source owner
  - repository: CultureBotAI/CommunityMech
    path: scripts/check_graph_receipts.py
    role: maintained source owner
  acceptance_checks:
  - Correct the specific defect without weakening provenance or scientific evidence
    requirements.
  - Add a regression or source-linked assertion check demonstrating the failure and
    correction.
  - Rebase onto current main and pass required exact-head and merge-group checks.
limitations:
- No model weights were downloaded, provider credits spent, numerical maps rebuilt,
  or browser visual QA performed.
- The review covers high-risk integration/provenance behavior, not every line of the
  59-file PR or fleet-wide governed-byte compatibility.
- 'Review-only: no curated source changes, GitHub review submission, issue creation,
  merge, or branch deletion.'
- Review bundles are local and uncommitted in isolated detached worktrees.
- No full integrated-suite or protected merge-group run; both branches have merge
  conflicts with current main.
- This is a bounded PR review, not a completed per-record scientific certification
  or a full native P1-P4 completeness scoring exercise.
links:
- https://github.com/CultureBotAI/CommunityMech/pull/935
- https://github.com/CultureBotAI/CommunityMech/commit/01013cc1776136f2fc4a36a761b0d8c338e3a706
```
