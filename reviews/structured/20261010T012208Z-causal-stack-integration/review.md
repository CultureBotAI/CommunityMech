# Adversarial review of cumulative causal-graph integration

- Review: 20261010T012208Z-causal-stack-integration
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-10T01:22:08Z
- Finished UTC: 2026-10-10T01:22:08Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

No new blocking defect found in the bounded integration review. Existing review findings1978 and1979 are repaired; merge and cleanup remain contingent on protected-main checks.

## Scope And Provenance

Review cumulative patch inclusion, immutable review evidence, shared test changes, graph palette semantics, upstream authority pin and research-boundary preservation.

Selection: Two integration surfaces; prior record-level scientific reviews are retained, not repeated.
Coverage: full; 2 reviewed / 2 in the declared population.
Source: working_tree at Git base dcb31fb1ad68bbf653c79f6b6d84b696dc89e543.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| causal-integration | reports/causal_graph_review/integration-20261010.json | maintained | Cumulative integration receipt |
| network-palette | src/communitymech/templates/community.html # network palette and accessible description | maintained | Graph palette integration |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| All native changes retained | passed | True | causal-integration | 99/99 native heads are ancestors of the cumulative head and each own binary patch matches its previously reviewed SHA256. |
| Existing cumulative code and data full CI | passed | True | causal-integration, network-palette | 4684 passed; 86 skipped; 8 deselected on 253544137c655443aaf270672f6c724db8d5b6c5. |
| Canonical artifacts unchanged during integration | passed | True | causal-integration | Every baseline artifact hash matches. Actual upstream authority-pin update preserved. |
| Integration regression tests | passed | True | causal-integration, network-palette | 89 passed in121.08s across network palette, participant resolution, connectivity credit, inventory supersession, corpus hierarchy and review contract tests. |
| Deterministic complete corpus inventory | passed | True | causal-integration | Inventory rebuilt from both canonical roots including ignored files, with no tracked diff, zero structural defects and unchanged research statuses. |

## Scientific And Domain Assessments

### Squash and branch cleanup

provenance: supported. Targets: causal-integration.

Published archival tag retains integration base and all current stack commits; earlier provenance tag retains pre-cascade historical review inputs. Cleanup must verify local and remote branch heads before deleting only refs.

### Structural validity versus scientific completeness

scope: supported. Targets: causal-integration.

406 reviewed and54 needs_research remain distinct; no unresolved research issue is closed by consolidation.

### Shared regression changes and palette behavior

representation: supported. Targets: network-palette.

Synthetic fixtures retain prior auditor counterexamples; corpus census updates name source-backed issues; connectivity share guard remains intact. Rare interaction types share Other with exact textual labels retained and accurate accessible description.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| receipt | reports/causal_graph_review/integration-20261010.json | supports | Fresh GitHub head comparison and byte-identical binary patches for all 99 remaining native members; artifact preservation and exact prior-head CI. |
| inventory | reports/causal_graph_review/summary.json | supports | Hash-bound ledger coverage and actual network counts, with 54 records still needs_research and 57 warnings. |
| tests | https://github.com/CultureBotAI/CommunityMech/actions/runs/37903574419 | supports | Prior exact cumulative head: 4684 passed, 86 skipped, 8 deselected; separate structured contract step: 4 passed. New integration-head CI remains required. |
| repair | reviews/structured/20261009T075714Z-thiothrix-lineage-after/review.yaml | supports | Issue1978 active nomenclature repair and Issue1979 retained source provenance; unresolved scientific boundaries stay explicit. |

## Limits And Additional Notes

- Bounded self-adversarial integration review, not independent approval or fresh scientific assessment of every record.
- 54 research gaps and57 network warnings remain documented. No new Edison job or graph topology was introduced for integration.
- The full local suite remains unavailable due to previously recorded macOS dependency installation failure; real CI supplies full-suite verification.
- Native-stack missing CI incident1980 is worked around by targeting the cumulative PR directly to protected main; its platform root cause is not claimed fixed.
- New exact-head PR and merge-group CI must pass before merge; this pre-publication record does not claim successful merge or cleanup.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T012208Z-causal-stack-integration
kind: repository
repository: CultureBotAI/CommunityMech
title: Adversarial review of cumulative causal-graph integration
started_at: '2026-10-10T01:22:08Z'
finished_at: '2026-10-10T01:22:08Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Same agent prepared integration and reviewed it; not independent
    approval.
skill: communitymech-causal-graphs
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: No new blocking defect found in the bounded integration review. Existing
  review findings1978 and1979 are repaired; merge and cleanup remain contingent on
  protected-main checks.
source:
  git_revision: dcb31fb1ad68bbf653c79f6b6d84b696dc89e543
  state: working_tree
  inputs:
  - path: reports/causal_graph_review/build_inventory.py
    sha256: 5cb9aeb35b34b67077dddf434715d1ee9314f71130f9e165f5c41967180a9483
    role: context
  - path: reports/causal_graph_review/integration-20261010.json
    sha256: b3efc77cf34e9ad8145ec1ebb292b50980a94d0c8d5964f07ba01886b9881ed2
    role: target
  - path: reports/causal_graph_review/inventory.tsv
    sha256: 8954083558b4a59cdda34a848af8fbb20f9d31e8f94e7df1372b5b6de196830f
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: 1b154cbc194777a0f7b3283816eacba106c5db3395bf7422af1dd4a0df223e63
    role: context
  - path: reviews/structured/20261009T075714Z-thiothrix-lineage-after/review.yaml
    sha256: fb1794ab1ef754f45fad2cee35b00d2cca4398ed0de531d7f9e90bee883a0bf9
    role: context
  - path: scripts/.vendored_canon_ref
    sha256: 22e662fe0c5839a4101a92a4d3b4040e46e2b76e1229d4f15d5c6085229a4454
    role: context
  - path: src/communitymech/templates/community.html
    sha256: 26100aace84e8a249d69a439592cc8f696549cf8e72ab121df1f830f4c603096
    role: target
  - path: tests/test_causal_review_inventory.py
    sha256: 43a297fcbff5a2882d6a2c3d70f00a29c92ee48a9626bb94e8ed9fefa68b321d
    role: context
  - path: tests/test_community_level_connectivity_credit.py
    sha256: 0f02b8c5d89eed7a6578075899bfe4fa481f929515b4fd5b2641a61eedd4c88e
    role: context
  - path: tests/test_gtdb_lineage_tree.py
    sha256: 091ca38968ebc844ab02491c767e4b1cd42a90f1bd71be2e931ac4ba0c845d57
    role: context
  - path: tests/test_network_palette.py
    sha256: 4d1242f7ecb93e366646595922eb24d56a5ead745133a4afa07518020f7473bc
    role: context
  - path: tests/test_participating_taxa.py
    sha256: db84a4aedbbc553907c6ad35737d3f0f3900aa3ce50eb0aad61ef65b3855a8e7
    role: context
scope:
  description: Review cumulative patch inclusion, immutable review evidence, shared
    test changes, graph palette semantics, upstream authority pin and research-boundary
    preservation.
  selection: Two integration surfaces; prior record-level scientific reviews are retained,
    not repeated.
  coverage: full
  population_size: 2
  reviewed_target_ids:
  - causal-integration
  - network-palette
targets:
- target_id: causal-integration
  path: reports/causal_graph_review/integration-20261010.json
  kind: maintained
  label: Cumulative integration receipt
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: reports/causal_graph_review/integration-20261010.json
    role: maintained integration surface
- target_id: network-palette
  path: src/communitymech/templates/community.html
  selector: network palette and accessible description
  kind: maintained
  label: Graph palette integration
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/templates/community.html
    role: maintained integration surface
checks:
- check_id: patch-preservation
  name: All native changes retained
  status: passed
  required: true
  summary: 99/99 native heads are ancestors of the cumulative head and each own binary
    patch matches its previously reviewed SHA256.
  target_ids:
  - causal-integration
  evidence_ids:
  - receipt
- check_id: prior-full-suite
  name: Existing cumulative code and data full CI
  status: passed
  required: true
  summary: 4684 passed; 86 skipped; 8 deselected on 253544137c655443aaf270672f6c724db8d5b6c5.
  target_ids:
  - causal-integration
  - network-palette
  evidence_ids:
  - tests
  scope_note: This result does not authorize a new head or replace merge-group validation.
- check_id: artifact-boundaries
  name: Canonical artifacts unchanged during integration
  status: passed
  required: true
  summary: Every baseline artifact hash matches. Actual upstream authority-pin update
    preserved.
  target_ids:
  - causal-integration
  evidence_ids:
  - receipt
  - inventory
- check_id: focused-regressions
  name: Integration regression tests
  status: passed
  required: true
  summary: 89 passed in121.08s across network palette, participant resolution, connectivity
    credit, inventory supersession, corpus hierarchy and review contract tests.
  target_ids:
  - causal-integration
  - network-palette
  command: python3 -m pytest -q tests/test_network_palette.py tests/test_participating_taxa.py
    tests/test_community_level_connectivity_credit.py tests/test_causal_review_inventory.py
    tests/test_gtdb_lineage_tree.py tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
- check_id: inventory-rebuild
  name: Deterministic complete corpus inventory
  status: passed
  required: true
  summary: Inventory rebuilt from both canonical roots including ignored files, with
    no tracked diff, zero structural defects and unchanged research statuses.
  target_ids:
  - causal-integration
  command: python3 reports/causal_graph_review/build_inventory.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - inventory
evidence:
- evidence_id: receipt
  kind: validation
  reference: reports/causal_graph_review/integration-20261010.json
  accessed_at: '2026-10-10T01:22:08Z'
  support: supports
  summary: Fresh GitHub head comparison and byte-identical binary patches for all
    99 remaining native members; artifact preservation and exact prior-head CI.
  snapshot_sha256: b3efc77cf34e9ad8145ec1ebb292b50980a94d0c8d5964f07ba01886b9881ed2
- evidence_id: inventory
  kind: record_content
  reference: reports/causal_graph_review/summary.json
  accessed_at: '2026-10-10T01:22:08Z'
  support: supports
  summary: Hash-bound ledger coverage and actual network counts, with 54 records still
    needs_research and 57 warnings.
- evidence_id: tests
  kind: validation
  reference: https://github.com/CultureBotAI/CommunityMech/actions/runs/37903574419
  accessed_at: '2026-10-10T01:22:08Z'
  support: supports
  summary: 'Prior exact cumulative head: 4684 passed, 86 skipped, 8 deselected; separate
    structured contract step: 4 passed. New integration-head CI remains required.'
- evidence_id: repair
  kind: prior_review
  reference: reviews/structured/20261009T075714Z-thiothrix-lineage-after/review.yaml
  accessed_at: '2026-10-10T01:22:08Z'
  support: supports
  summary: Issue1978 active nomenclature repair and Issue1979 retained source provenance;
    unresolved scientific boundaries stay explicit.
assessments:
- assessment_id: source-preservation
  area: provenance
  topic: Squash and branch cleanup
  outcome: supported
  summary: Published archival tag retains integration base and all current stack commits;
    earlier provenance tag retains pre-cascade historical review inputs. Cleanup must
    verify local and remote branch heads before deleting only refs.
  target_ids:
  - causal-integration
  evidence_ids:
  - receipt
  - repair
- assessment_id: coverage-boundary
  area: scope
  topic: Structural validity versus scientific completeness
  outcome: supported
  summary: 406 reviewed and54 needs_research remain distinct; no unresolved research
    issue is closed by consolidation.
  target_ids:
  - causal-integration
  evidence_ids:
  - inventory
- assessment_id: test-and-template
  area: representation
  topic: Shared regression changes and palette behavior
  outcome: supported
  summary: Synthetic fixtures retain prior auditor counterexamples; corpus census
    updates name source-backed issues; connectivity share guard remains intact. Rare
    interaction types share Other with exact textual labels retained and accurate
    accessible description.
  target_ids:
  - network-palette
  evidence_ids:
  - tests
  - receipt
findings: []
actions: []
limitations:
- Bounded self-adversarial integration review, not independent approval or fresh scientific
  assessment of every record.
- 54 research gaps and57 network warnings remain documented. No new Edison job or
  graph topology was introduced for integration.
- The full local suite remains unavailable due to previously recorded macOS dependency
  installation failure; real CI supplies full-suite verification.
- Native-stack missing CI incident1980 is worked around by targeting the cumulative
  PR directly to protected main; its platform root cause is not claimed fixed.
- New exact-head PR and merge-group CI must pass before merge; this pre-publication
  record does not claim successful merge or cleanup.
links:
- https://github.com/CultureBotAI/CommunityMech/pull/1975
- https://github.com/CultureBotAI/CommunityMech/issues/1978
- https://github.com/CultureBotAI/CommunityMech/issues/1979
- https://github.com/CultureBotAI/CommunityMech/issues/1980
tags:
- causal-graphs
- integration
- self-review
```
