# Thiothrix active-lineage nomenclature after repair

- Review: 20261009T075714Z-thiothrix-lineage-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-09T07:57:14Z
- Finished UTC: 2026-10-09T07:57:14Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Scoped adversarial integration review of active nomenclature and source-preservation boundaries; not a completed scientific review of the community.

## Scope And Provenance

One active-lineage field and its provenance/evidence boundary, with corpus hierarchy validation.

Selection: Exact record identified by the failing CI assertion.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 57b17a7c3116feae7b6d7deefa9c54680c0ae816.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml # taxonomy[0].taxon_term.gtdb_classification | maintained | Thiothrix active GTDB lineage |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | CommunityMech:000222 | Recorded output SHA256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de |
| strict | passed | True | CommunityMech:000222 | Recorded output SHA256 6be49f93b2afb14fd31fca109f637d8c0d464e0c510d9303440c6642e47fab17 |
| terms | passed | True | CommunityMech:000222 | Recorded output SHA256 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018 |
| references-explained | passed | True | CommunityMech:000222 | Recorded output SHA256 8cd6f93e79f318dc66a116ff04c214a7af5ebb9834256956d9e645e0de845dfd |
| snippets | passed | True | CommunityMech:000222 | Recorded output SHA256 829e364135583b30eb2c4897e95fe4d47f8a921f6ac4accafa8cb390b1fae9df |
| rank-target | passed | True | CommunityMech:000222 | Recorded output SHA256 f607ab39497fa68d2ccde5b5646041924e9625c0a4c78ed650861e90159516af |
| history | passed | True | CommunityMech:000222 | Recorded output SHA256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de |
| inventory | passed | True | CommunityMech:000222 | Recorded output SHA256 fd404eeff18570a306e41613f1d84dac58112d17dde158feca764841174cc902 |
| network | passed | True | CommunityMech:000222 | Recorded output SHA256 6a349ee70c3b3deb2e3171d0a85501f53c7faa0aca02351007a8296feed367e9 |
| network-just | passed | True | CommunityMech:000222 | Recorded output SHA256 8595db43420d3f0a01c57acd6ad733a531a72e962486d20b4e1c2840dda55bff |
| rank-all | passed | True | CommunityMech:000222 | Recorded output SHA256 10d78f3d42b5f267152c14af4ea26af028af0b8f822b68fd80dd24ed9dc852e2 |
| render | passed | True | CommunityMech:000222 | Recorded output SHA256 69ef08bd0f7c149868e33e82aa41d9117ee7d402960323115a921889615aaf21 |
| render-repeat | passed | True | CommunityMech:000222 | Recorded output SHA256 69ef08bd0f7c149868e33e82aa41d9117ee7d402960323115a921889615aaf21 |
| regressions | passed | True | CommunityMech:000222 | Recorded output SHA256 4c3fb9c8c6a094a4cd61463106dc8b22e2d97d836a3504936bd83d574bd37c54 |
| diff-check | passed | True | CommunityMech:000222 | Recorded output SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| black-check | passed | True | CommunityMech:000222 | Recorded output SHA256 45a468fa6205768496f23f1716ebb7575e9b723449d2099b88bf2afef60b721f |
| ruff-check | passed | True | CommunityMech:000222 | Recorded output SHA256 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18 |
| structured-before-check | passed | True | CommunityMech:000222 | Recorded output SHA256 d82db5169aa589d6e5678a011d879f9faf56829409c5c8d37059fdd3f317250c |
| final-diff-check | passed | True | CommunityMech:000222 | Recorded output SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| Full local suite | unavailable | False | CommunityMech:000222 | 246 focused tests passed and 17 external-crosswalk-dependent cases skipped, including the unchanged whole-corpus hierarchy regression. Full local suite could not collect because UMAP was absent; locked isolated dependency installation failed in llvmlite. Complete exact-head and merge-group CI remain required before merge. |

## Scientific And Domain Assessments

### Active hierarchy versus verbatim evidence

nomenclature: supported. Targets: CommunityMech:000222.

Historical source spelling must remain verbatim; normalized active taxonomy must remain coherent without claiming a reclassified genome.

## Findings

### lineage-phylum: Historical phylum spelling conflicts with the active corpus hierarchy

major / resolved / confirmed; issue key: communitymech-1978-lineage-phylum.

Batch127 copied historical source nomenclature into the active GTDB lineage, causing a corpus-level hierarchy conflict.

Disposition: Active nomenclature normalized with explicit provenance; unchanged hierarchy validator and preservation/mutation tests pass. GitHub issue remains open until protected-main merge.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ci | https://github.com/CultureBotAI/CommunityMech/actions/runs/37845443207; tests/test_gtdb_lineage_tree.py::test_the_committed_kb_is_a_consistent_hierarchy | supports | Original CI detects Gammaproteobacteria under both Proteobacteria and Pseudomonadota; focused predecessor validation omitted this corpus test. |
| record | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml; taxonomy[0].taxon_term.gtdb_classification.gtdb_lineage | supports | The active lineage and three historical source quotations have distinct roles. Only the active phylum spelling requires normalization. |
| source-row | PMID:38273328; Table S4, row104, ALUMROCK_MS4_Thiothrix_nivea-related_50_537_curated | supports | The retained manifest uses Proteobacteria, identifies Thiothrix genus and leaves species blank; neither source values nor participant identity should be rewritten. |
| gtdb | https://forum.gtdb.ecogenomic.org/t/announcing-gtdb-r08-rs214/456; Release changes: phylum names | supports | The GTDB maintainer announcement documents adoption of published phylum names including Pseudomonadota. The resource paper doi:10.1093/nar/gkaf1040 discusses the Proteobacteria rename. This supports nomenclature, not a fresh genome placement. |
| validation | reports/causal_graph_review/validation-20261009-batch128.json | supports | ........................................................................ [ 27%]<br>...............s....................s....sssssss.............s.....sssss [ 54%]<br>ss...................................................................... [ 82%]<br>...............................................                          [100%]<br>246 passed, 17 skipped in 284.35s (0:04:44)<br> |

## Limits And Additional Notes

- No new biological identities, participants, nodes, arrows, mechanistic claims, or genome-count votes are certified.
- Issue1841 remains open; the record stays needs_research. Complete source-body and study-genome reclassification were not repeated.
- A completed scoped diagnostic review is not independent approval, whole-record scientific certification, a passing new CI result, or a merged PR.
- Saved using the canonical record-review helper and schema at main commit4bad95490b1d03a2dc9bbdd7854e124d00daac57. Legacy ledgers are not migrated or rewritten.
- Issue1979: archival tag review-provenance/20261009-batch128 retains the Git source base through squash merge and branch cleanup. Fresh main-only database failed before the tag fetch and verified historical blobs after it; receipt is reports/causal_graph_review/provenance-20261009-batch128.json.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261009T075714Z-thiothrix-lineage-after
kind: record
repository: CultureBotAI/CommunityMech
title: Thiothrix active-lineage nomenclature after repair
started_at: '2026-10-09T07:57:14Z'
finished_at: '2026-10-09T07:57:14Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Same agent assessed and repaired the change; not independent
    approval.
skill: communitymech-causal-graphs
completion: completed
verdict: pass_with_limitations
scientific_review: false
summary: Scoped adversarial integration review of active nomenclature and source-preservation
  boundaries; not a completed scientific review of the community.
source:
  git_revision: 57b17a7c3116feae7b6d7deefa9c54680c0ae816
  state: working_tree
  inputs:
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 4c55cbbcf80785d2ad004ad3eab44d533811b7418c5995e5ba1893cb66864e36
    role: target
  - path: reports/causal_graph_review/decisions/20261008-spring-identity-batch127.yaml
    sha256: 9166b3bb643162691aeee39ebb7b98b9ad22ef63505fa3e9cc5654be228519ef
    role: context
  - path: reports/causal_graph_review/decisions/20261009-spring-lineage-batch128.yaml
    sha256: 19a158bac0d3e294c5406c1cd0ddf7577ddf3b213212b4fe67b779aeafcee7b3
    role: context
  - path: reports/causal_graph_review/provenance-20261009-batch128.json
    sha256: 4bf697287239aa0a8396548b08e888b8b2b31d5a2e44e762f12b0523929baf18
    role: context
  - path: reports/causal_graph_review/sources/20261008-spring-supplements-batch127.json
    sha256: e95387a98bd9afe49b2c51830fa02f05002d8936985d739efda40f5e7ccd7505
    role: context
  - path: reports/causal_graph_review/validation-20261009-batch128.json
    sha256: c4613bfd11b2e4f4a659e6afa835df67492f254c49321cd9c162f2e1e9b4660b
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: 99079e7712d0c6b5eef0f278822a6b04fdb9a3a55b446e1f73f0752e4e626d04
    role: context
  - path: src/communitymech/validators/gtdb_lineage_tree.py
    sha256: 1bf2f371b064f83bcba1589d05151fe3443fe826538e5a4ab6b7c3c3bde8fef0
    role: context
  - path: tests/test_causal_review_batch107.py
    sha256: 4d31b9b6523bd2219ad69f21286fe35cd1b17e660ed57076344139ac7baefb09
    role: context
  - path: tests/test_causal_review_batch127.py
    sha256: 751cc31cf0f6e533558642cf21d2feb0c50fa263bf5e4ebdf2cad00c3d43113c
    role: context
  - path: tests/test_causal_review_batch128.py
    sha256: fe834061a74b9a614c5af1d5f65e868e3c0f8a246bfe58cf906d37f34c1cf8b0
    role: context
  - path: tests/test_gtdb_lineage_tree.py
    sha256: 091ca38968ebc844ab02491c767e4b1cd42a90f1bd71be2e931ac4ba0c845d57
    role: context
scope:
  description: One active-lineage field and its provenance/evidence boundary, with
    corpus hierarchy validation.
  selection: Exact record identified by the failing CI assertion.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000222
targets:
- target_id: CommunityMech:000222
  path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  selector: taxonomy[0].taxon_term.gtdb_classification
  label: Thiothrix active GTDB lineage
  record_class: MicrobialCommunity
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    role: maintained taxon grounding
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  summary: Recorded output SHA256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/l58VlyFvdmnkl0CcAx5Gk/bin/linkml-validate
    -s src/communitymech/schema/communitymech.yaml kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: strict
  name: strict
  status: passed
  required: true
  summary: Recorded output SHA256 6be49f93b2afb14fd31fca109f637d8c0d464e0c510d9303440c6642e47fab17
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/neDBQyZXv0RYv8B1GH0dI/bin/python3 scripts/validate_strict.py
    --workers 1 --out /private/tmp/communitymech-batch128/strict.tsv kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: terms
  name: terms
  status: passed
  required: true
  summary: Recorded output SHA256 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/neDBQyZXv0RYv8B1GH0dI/bin/linkml-term-validator
    validate-data kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml -s src/communitymech/schema/communitymech.yaml
    --labels
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: references-explained
  name: references-explained
  status: passed
  required: true
  summary: Recorded output SHA256 8cd6f93e79f318dc66a116ff04c214a7af5ebb9834256956d9e645e0de845dfd
  target_ids:
  - CommunityMech:000222
  command: just validate-references-explained kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: snippets
  name: snippets
  status: passed
  required: true
  summary: Recorded output SHA256 829e364135583b30eb2c4897e95fe4d47f8a921f6ac4accafa8cb390b1fae9df
  target_ids:
  - CommunityMech:000222
  command: just audit-snippets kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    --list-mismatch --list-nocontent --list-rendering --list-assembled
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: rank-target
  name: rank-target
  status: passed
  required: true
  summary: Recorded output SHA256 f607ab39497fa68d2ccde5b5646041924e9625c0a4c78ed650861e90159516af
  target_ids:
  - CommunityMech:000222
  command: just rank-causal-graphs kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: history
  name: history
  status: passed
  required: true
  summary: Recorded output SHA256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
  target_ids:
  - CommunityMech:000222
  command: just validate-history history/records/Sulfide_Spring_Autotrophic_CPR_Biofilm/2026-10-09T073735Z-codex-6e2f4b.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: inventory
  name: inventory
  status: passed
  required: true
  summary: Recorded output SHA256 fd404eeff18570a306e41613f1d84dac58112d17dde158feca764841174cc902
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/l58VlyFvdmnkl0CcAx5Gk/bin/python3 reports/causal_graph_review/build_inventory.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: network
  name: network
  status: passed
  required: true
  summary: Recorded output SHA256 6a349ee70c3b3deb2e3171d0a85501f53c7faa0aca02351007a8296feed367e9
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/l58VlyFvdmnkl0CcAx5Gk/bin/python3 -m
    communitymech.cli audit-network --json
  exit_code: 1
  expected_exit_code: 1
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: network-just
  name: network-just
  status: passed
  required: true
  summary: Recorded output SHA256 8595db43420d3f0a01c57acd6ad733a531a72e962486d20b4e1c2840dda55bff
  target_ids:
  - CommunityMech:000222
  command: just audit-network-json
  exit_code: 2
  expected_exit_code: 2
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: rank-all
  name: rank-all
  status: passed
  required: true
  summary: Recorded output SHA256 10d78f3d42b5f267152c14af4ea26af028af0b8f822b68fd80dd24ed9dc852e2
  target_ids:
  - CommunityMech:000222
  command: just rank-causal-graphs
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: render
  name: render
  status: passed
  required: true
  summary: Recorded output SHA256 69ef08bd0f7c149868e33e82aa41d9117ee7d402960323115a921889615aaf21
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/l58VlyFvdmnkl0CcAx5Gk/bin/python3 -m
    communitymech.render
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: render-repeat
  name: render-repeat
  status: passed
  required: true
  summary: Recorded output SHA256 69ef08bd0f7c149868e33e82aa41d9117ee7d402960323115a921889615aaf21
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/l58VlyFvdmnkl0CcAx5Gk/bin/python3 -m
    communitymech.render
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: regressions
  name: regressions
  status: passed
  required: true
  summary: Recorded output SHA256 4c3fb9c8c6a094a4cd61463106dc8b22e2d97d836a3504936bd83d574bd37c54
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/l58VlyFvdmnkl0CcAx5Gk/bin/python3 -m
    pytest -q tests/test_causal_review_batch107.py tests/test_causal_review_batch126.py
    tests/test_causal_review_batch127.py tests/test_causal_review_batch128.py tests/test_gtdb_lineage_tree.py
    tests/test_gtdb_coherence_validator.py tests/test_gtdb_support_counts.py tests/test_gtdb_status_writer.py
    tests/test_causal_review_inventory.py tests/test_network_auditor.py tests/test_participating_taxa.py
    tests/test_no_paywalled_text_in_repo.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: diff-check
  name: diff-check
  status: passed
  required: true
  summary: Recorded output SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  target_ids:
  - CommunityMech:000222
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: black-check
  name: black-check
  status: passed
  required: true
  summary: Recorded output SHA256 45a468fa6205768496f23f1716ebb7575e9b723449d2099b88bf2afef60b721f
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/3Q_kifQtLB624D5bBWGIf/bin/black --check
    tests/test_causal_review_batch107.py tests/test_causal_review_batch127.py tests/test_causal_review_batch128.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: ruff-check
  name: ruff-check
  status: passed
  required: true
  summary: Recorded output SHA256 82b3e6a6c090a57601d22943bd23fca9218d1031dbe5a7b754092f9a156b4f18
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/wCcxEYRM4HeHgwYPZemHX/bin/ruff check
    tests/test_causal_review_batch107.py tests/test_causal_review_batch127.py tests/test_causal_review_batch128.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: structured-before-check
  name: structured-before-check
  status: passed
  required: true
  summary: Recorded output SHA256 d82db5169aa589d6e5678a011d879f9faf56829409c5c8d37059fdd3f317250c
  target_ids:
  - CommunityMech:000222
  command: /Users/marcin/.cache/uv/archive-v0/l58VlyFvdmnkl0CcAx5Gk/bin/python3 /private/tmp/communitymech-review-contract-20261009/scripts/record_review.py
    --repo-root /private/tmp/communitymech-causal-batch126 check --require-reviews
    --base 57b17a7c3116feae7b6d7deefa9c54680c0ae816
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: final-diff-check
  name: final-diff-check
  status: passed
  required: true
  summary: Recorded output SHA256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
  target_ids:
  - CommunityMech:000222
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - validation
  scope_note: Network exit codes retain existing warnings; no gate was weakened.
- check_id: full-suite-local
  name: Full local suite
  status: unavailable
  required: false
  summary: 246 focused tests passed and 17 external-crosswalk-dependent cases skipped,
    including the unchanged whole-corpus hierarchy regression. Full local suite could
    not collect because UMAP was absent; locked isolated dependency installation failed
    in llvmlite. Complete exact-head and merge-group CI remain required before merge.
  target_ids:
  - CommunityMech:000222
  evidence_ids:
  - validation
  scope_note: Outside this completed focused diagnostic review. Full exact-head and
    merge-group CI must pass before merge; no full-suite pass is claimed.
evidence:
- evidence_id: ci
  kind: validation
  reference: https://github.com/CultureBotAI/CommunityMech/actions/runs/37845443207
  locator: tests/test_gtdb_lineage_tree.py::test_the_committed_kb_is_a_consistent_hierarchy
  accessed_at: '2026-10-09T07:57:14Z'
  support: supports
  summary: Original CI detects Gammaproteobacteria under both Proteobacteria and Pseudomonadota;
    focused predecessor validation omitted this corpus test.
  snapshot_sha256: 94d8ebd1c08357a0218be412a56a780321b1d232d125b855adfe432433c6c733
- evidence_id: record
  kind: record_content
  reference: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  locator: taxonomy[0].taxon_term.gtdb_classification.gtdb_lineage
  accessed_at: '2026-10-09T07:57:14Z'
  support: supports
  summary: The active lineage and three historical source quotations have distinct
    roles. Only the active phylum spelling requires normalization.
- evidence_id: source-row
  kind: primary_source
  reference: PMID:38273328
  locator: Table S4, row104, ALUMROCK_MS4_Thiothrix_nivea-related_50_537_curated
  accessed_at: '2026-10-09T07:57:14Z'
  support: supports
  summary: The retained manifest uses Proteobacteria, identifies Thiothrix genus and
    leaves species blank; neither source values nor participant identity should be
    rewritten.
  snapshot_sha256: e95387a98bd9afe49b2c51830fa02f05002d8936985d739efda40f5e7ccd7505
- evidence_id: gtdb
  kind: authority
  reference: https://forum.gtdb.ecogenomic.org/t/announcing-gtdb-r08-rs214/456
  locator: 'Release changes: phylum names'
  accessed_at: '2026-10-09T07:57:14Z'
  support: supports
  summary: The GTDB maintainer announcement documents adoption of published phylum
    names including Pseudomonadota. The resource paper doi:10.1093/nar/gkaf1040 discusses
    the Proteobacteria rename. This supports nomenclature, not a fresh genome placement.
- evidence_id: validation
  kind: validation
  reference: reports/causal_graph_review/validation-20261009-batch128.json
  accessed_at: '2026-10-09T07:57:14Z'
  support: supports
  summary: '........................................................................
    [ 27%]

    ...............s....................s....sssssss.............s.....sssss [ 54%]

    ss...................................................................... [ 82%]

    ...............................................                          [100%]

    246 passed, 17 skipped in 284.35s (0:04:44)

    '
  snapshot_sha256: c4613bfd11b2e4f4a659e6afa835df67492f254c49321cd9c162f2e1e9b4660b
assessments:
- assessment_id: active-vs-source
  area: nomenclature
  topic: Active hierarchy versus verbatim evidence
  outcome: supported
  summary: Historical source spelling must remain verbatim; normalized active taxonomy
    must remain coherent without claiming a reclassified genome.
  target_ids:
  - CommunityMech:000222
  evidence_ids:
  - record
  - source-row
  - gtdb
  - validation
findings:
- finding_id: lineage-phylum
  issue_key: communitymech-1978-lineage-phylum
  category: nomenclature
  severity: major
  status: resolved
  certainty: confirmed
  title: Historical phylum spelling conflicts with the active corpus hierarchy
  description: Batch127 copied historical source nomenclature into the active GTDB
    lineage, causing a corpus-level hierarchy conflict.
  target_ids:
  - CommunityMech:000222
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.gtdb_lineage
  evidence_ids:
  - ci
  - record
  - source-row
  - gtdb
  rule_id: gtdb-single-parent-hierarchy
  native_severity: P2
  normalization_reason: Major integration defect blocks required CI while the supported
    genus identity remains intact.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    role: maintained taxon grounding
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1978
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261009T074053Z-thiothrix-lineage-before
    finding_id: lineage-phylum
  disposition_reason: Active nomenclature normalized with explicit provenance; unchanged
    hierarchy validator and preservation/mutation tests pass. GitHub issue remains
    open until protected-main merge.
actions: []
limitations:
- No new biological identities, participants, nodes, arrows, mechanistic claims, or
  genome-count votes are certified.
- Issue1841 remains open; the record stays needs_research. Complete source-body and
  study-genome reclassification were not repeated.
- A completed scoped diagnostic review is not independent approval, whole-record scientific
  certification, a passing new CI result, or a merged PR.
notes:
- Saved using the canonical record-review helper and schema at main commit4bad95490b1d03a2dc9bbdd7854e124d00daac57.
  Legacy ledgers are not migrated or rewritten.
- 'Issue1979: archival tag review-provenance/20261009-batch128 retains the Git source
  base through squash merge and branch cleanup. Fresh main-only database failed before
  the tag fetch and verified historical blobs after it; receipt is reports/causal_graph_review/provenance-20261009-batch128.json.'
links:
- https://github.com/CultureBotAI/CommunityMech/pull/1975
- https://github.com/CultureBotAI/CommunityMech/issues/1841
tags:
- causal-graphs
- batch128
- self-review
```
