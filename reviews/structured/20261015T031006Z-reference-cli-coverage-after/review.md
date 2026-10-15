# Reference CLI count interpretation corrected

- Review: 20261015T031006Z-reference-cli-coverage-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-15T03:02:06.753415Z
- Finished UTC: 2026-10-15T03:10:06.717930Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: false

## Summary

Correct the reporting interpretation only: Phormidium 21 checked/2 Discussion omissions, Alseth 27/1, PHA 24/0. Zero CLI findings is not zero checks. No scientific claim or graph status changes.

## Scope And Provenance

Four reporting surfaces and three exact current record fixtures; not a scientific review.

Selection: Recurrence found while checking #1994/#1996 follow-up and existing #1469.
Coverage: full; 4 reviewed / 4 in the declared population.
Source: git_commit at Git base ade419a81fe378a78ef06f672b1002c96c8dffc9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| explained-cli | scripts/annotate_reference_errors.py | maintained | explained-cli |
| review-index | reports/causal_graph_review/README.md | maintained | review-index |
| batch132-coverage | reviews/structured/20261015T014050Z-phormidium-identity-after/review.yaml | maintained | batch132-coverage |
| batch130-coverage | reviews/structured/20261014T222155Z-phage-graphs-after/review.yaml | maintained | batch130-coverage |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Reporting regression and CLI controls | passed | True | explained-cli, review-index, batch132-coverage, batch130-coverage | b/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553: PydanticDeprecatedSince211: Accessing the 'model_fields' attribute on the instance is deprecated. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.<br>    imports=imports, **{k: getattr(self, k, None) for k in self.model_fields if k != "imports"}<br><br>-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html<br>48 passed, 14 warnings in 104.08s (0:01:44) |
| lint | passed | True | explained-cli, review-index, batch132-coverage, batch130-coverage | All checks passed!<br>Success: no issues found in 49 source files |
| explained-cli | passed | True | explained-cli, review-index, batch132-coverage, batch130-coverage | Validating kb/communities/Phormidium_Alkaline_Consortium.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| review-contract-before | passed | True | explained-cli, review-index, batch132-coverage, batch130-coverage | {<br>  "repository": "culturebotai/CommunityMech",<br>  "valid_reviews": 25,<br>  "coverage": "declared_scopes_only"<br>} |
| preservation | passed | True | explained-cli, review-index, batch132-coverage, batch130-coverage | No changed canonical, source, history, generated community or prior-review bytes. |

## Scientific And Domain Assessments

### Counter semantics versus actual traversal

provenance: supported. Targets: explained-cli, review-index, batch132-coverage, batch130-coverage.

CLI canaries establish the concrete coverage counts and the remaining Discussion omission. This correction supersedes only the mistaken zero-coverage interpretation, not the prior scientific findings.

## Findings

### cli-count-recurrence: Issue-count output misclassified as zero validation coverage

minor / resolved / confirmed; issue key: communitymech-1469-20261015-recurrence.

Batch132 marked reference-cli failed from Total checks: 0. Batch130 and the current index also describe zero checks. Actual CLI probes trace 21, 27 and 24 checked excerpts with negative controls. The counter is not coverage.

Disposition: Append-only correction and maintained index now distinguish a clean native finding count from measured coverage; explained CLI labels the counter correctly and regression controls pass. No historical bundle or raw output is rewritten.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| final-phormidium-cli | reports/reference_cli_coverage/final-phormidium-cli.json; actual CLI output, traced excerpt paths, mutation/restoration exits, input hashes | supports | Native CLI checks EvidenceItem snippets; the summary counts issues. Discussion mutations remain invisible where present. |
| alseth-cli | reports/reference_cli_coverage/alseth-cli.json; actual CLI output, traced excerpt paths, mutation/restoration exits, input hashes | supports | Native CLI checks EvidenceItem snippets; the summary counts issues. Discussion mutations remain invisible where present. |
| final-pha-cli | reports/reference_cli_coverage/final-pha-cli.json; actual CLI output, traced excerpt paths, mutation/restoration exits, input hashes | supports | Native CLI checks EvidenceItem snippets; the summary counts issues. Discussion mutations remain invisible where present. |
| surfaces | scripts/annotate_reference_errors.py; main() summary handling and all four declared target surfaces | supports | Explained output labels issue counts explicitly; current index and this successor correct the historical claim. |
| regression | reports/reference_cli_coverage/after-regression.json; command, exit, stdout/stderr, input hashes | supports | b/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553: PydanticDeprecatedSince211: Accessing the 'model_fields' attribute on the instance is deprecated. Instead, you should access this attribute from the model class. Deprecated in Pydantic V2.11 to be removed in V3.0.<br>    imports=imports, **{k: getattr(self, k, None) for k in self.model_fields if k != "imports"}<br><br>-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html<br>48 passed, 14 warnings in 104.08s (0:01:44) |
| lint | reports/reference_cli_coverage/lint.json; command and exact output | supports | Successful bounded check: lint |
| explained-cli | reports/reference_cli_coverage/explained-cli.json; command and exact output | supports | Successful bounded check: explained-cli |
| review-contract-before | reports/reference_cli_coverage/review-contract-before.json; command and exact output | supports | Successful bounded check: review-contract-before |
| preservation | reports/reference_cli_coverage/preservation.json; command and exact output | supports | Successful bounded check: preservation |

## Limits And Additional Notes

- Source-based implementing-agent self-review, not independent approval or scientific recertification.
- Native Discussion traversal #476 and supplement routing #1996 remain open; no sources are combined and no matching thresholds change.
- This scoped disposition does not retire unrelated findings in the two earlier reviews or claim whole-corpus completion.
- Remote CI/protected merge is recorded separately after this immutable local snapshot.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T031006Z-reference-cli-coverage-after
kind: repository
repository: CultureBotAI/CommunityMech
title: Reference CLI count interpretation corrected
started_at: '2026-10-15T03:02:06.753415Z'
finished_at: '2026-10-15T03:10:06.717930Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Implementing-agent adversarial review and executable controls,
    not independent approval.
skill: communitymech-causal-graphs
completion: completed
verdict: pass_with_limitations
scientific_review: false
source:
  git_revision: ade419a81fe378a78ef06f672b1002c96c8dffc9
  state: git_commit
  inputs:
  - path: conf/reference_validator.yaml
    sha256: 5cd4781c7e15b7c5472f0b008e41764842cc023a7ba99f4273298f421be36652
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: justfile
    sha256: 120e67eb143d957828d0d242e9585e82a2c84d7a5322528c1fad475cba912118
    role: context
  - path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    sha256: cef1f3c47035ef336cb809456b25a185e0397bb9f0a16c492becdb5b371529f5
    role: context
  - path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
    sha256: aebd6497b6d5a6f49e9e9ef956d4ec0847960acc0fd2413dce5e0960ed748488
    role: context
  - path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    sha256: 0f03389e79ddcf2e97ebb0f32bd51a776b6bcbaea3ddad52c21ada8feca2939b
    role: context
  - path: references_cache/PMID_38648198.txt
    sha256: babc54ddb60c3ed882e817d1970ff9c7ba24069b0b06d67730e12eb974b58df3
    role: context
  - path: references_cache/PMID_40152616.txt
    sha256: 65e30e4f8aed4b1c7cde1fb173376207bbf90d92306c7f59997fd41bfeddbe8b
    role: context
  - path: references_cache/doi_10.3389_fmicb.2022.780346.md
    sha256: a3ba7f3dfd3bd6b6ae6338a05beead53f2cb15c89f70f0a89700cbfa0dc2b929
    role: context
  - path: reports/causal_graph_review/README.md
    sha256: 525b309dee76a6b472977ec646f004d66665922fc35e4a692f7aabd54f84d49c
    role: target
  - path: reports/reference_cli_coverage/README.md
    sha256: ff553cfefb5ee1a8ad10c3fa00dcea40bcdc9f677b5660f9b6a11a3f00baef3a
    role: context
  - path: reports/reference_cli_coverage/after-regression.json
    sha256: c45aee9afc501b2c12b8bbffe6768cdeafda76e8ac3359a8beaf973232ca24b7
    role: context
  - path: reports/reference_cli_coverage/alseth-cli.json
    sha256: 9edf3eb3ce845487f281902920553b55dda524742d3d25fb030221c0c2108e1a
    role: context
  - path: reports/reference_cli_coverage/before-regression.json
    sha256: b39451216b07b2640c37ca16594becbadd234b1ec1435e488cd9d2371527b4ae
    role: context
  - path: reports/reference_cli_coverage/candidate-statements.json
    sha256: 49d8828e6b7d02952d3f05f8ff0820b7929ad0dde0f321475762822aea0e7262
    role: context
  - path: reports/reference_cli_coverage/explained-cli.json
    sha256: 3c947035b0aae1abe73774c5ced614dff6d4b219ff8648523c4bad89ba1caf98
    role: context
  - path: reports/reference_cli_coverage/final-pha-cli.json
    sha256: fe7e70439857ea816419e49b4b54b218762c4cbad79a5d1a0b41663cf7933e62
    role: context
  - path: reports/reference_cli_coverage/final-phormidium-cli.json
    sha256: 9398943cf653a07b92dafed684d4c0b7663678238b66ccfa3f54dd46749630e0
    role: context
  - path: reports/reference_cli_coverage/lint.json
    sha256: cd27339a30171dafcdcfe7dd26d7a4d722fd895f1c87439d28e13df60433bf00
    role: context
  - path: reports/reference_cli_coverage/preservation.json
    sha256: 585e84cd9b814a15420426c403e431576204c4896d68ee64dafa2fb603b02028
    role: context
  - path: reports/reference_cli_coverage/probe.py
    sha256: 8e3782125ca5f5b022ec94527993bebca3e9a74fe93dc9d52037678dd4c127bd
    role: context
  - path: reports/reference_cli_coverage/review-contract-before.json
    sha256: ad51daafc9df440433de20d0cb8f2b374876305797014a99d97ee8ca79a64943
    role: context
  - path: reviews/structured/20261014T222155Z-phage-graphs-after/review.yaml
    sha256: 3367e0fc4cbde8c21001e47e7b3602d81cb66624a7bab14932645fe69202b854
    role: target
  - path: reviews/structured/20261015T014050Z-phormidium-identity-after/review.yaml
    sha256: 73c90525c74399990d7f2689ac14f74ac487561dd96ab091dfb7b5d8188b5a0b
    role: target
  - path: reviews/structured/20261015T030500Z-reference-cli-coverage-before/review.yaml
    sha256: 04c479f133c3559120bb7aa7dd6150cc272c767188f5939663a7011cacf996c0
    role: context
  - path: scripts/annotate_reference_errors.py
    sha256: 5bd5b6dd088714faed97c41230eee0f2268c7e1e1dc205dd5c04b560b51616ec
    role: target
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_reference_cli_coverage.py
    sha256: 193a54faa7742d15aeada599c8e8ffe8d0c33cc341418f061a6c3a5ead1e42e0
    role: context
  - path: tests/test_reference_error_annotation.py
    sha256: a38ecf5ec88f72139fd6f1a83372cd5cb1f77f8205669ddb4ad1521b907cae1f
    role: context
  - path: uv.lock
    sha256: 937fc64c52ddde9859c4231c12177e5b662ca40a7323fe21a5c0794d58ebbbc0
    role: context
targets:
- target_id: explained-cli
  path: scripts/annotate_reference_errors.py
  label: explained-cli
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: scripts/annotate_reference_errors.py
    role: maintained reporting surface
  - repository: CultureBotAI/CommunityMech
    path: reports/causal_graph_review/README.md
    role: maintained reporting surface
- target_id: review-index
  path: reports/causal_graph_review/README.md
  label: review-index
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: scripts/annotate_reference_errors.py
    role: maintained reporting surface
  - repository: CultureBotAI/CommunityMech
    path: reports/causal_graph_review/README.md
    role: maintained reporting surface
- target_id: batch132-coverage
  path: reviews/structured/20261015T014050Z-phormidium-identity-after/review.yaml
  label: batch132-coverage
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: scripts/annotate_reference_errors.py
    role: maintained reporting surface
  - repository: CultureBotAI/CommunityMech
    path: reports/causal_graph_review/README.md
    role: maintained reporting surface
- target_id: batch130-coverage
  path: reviews/structured/20261014T222155Z-phage-graphs-after/review.yaml
  label: batch130-coverage
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: scripts/annotate_reference_errors.py
    role: maintained reporting surface
  - repository: CultureBotAI/CommunityMech
    path: reports/causal_graph_review/README.md
    role: maintained reporting surface
summary: 'Correct the reporting interpretation only: Phormidium 21 checked/2 Discussion
  omissions, Alseth 27/1, PHA 24/0. Zero CLI findings is not zero checks. No scientific
  claim or graph status changes.'
scope:
  description: Four reporting surfaces and three exact current record fixtures; not
    a scientific review.
  selection: 'Recurrence found while checking #1994/#1996 follow-up and existing #1469.'
  coverage: full
  population_size: 4
  reviewed_target_ids:
  - explained-cli
  - review-index
  - batch132-coverage
  - batch130-coverage
  exclusions:
  - target: Scientific findings and the full graph corpus
    reason: No new primary-source or graph assessment.
checks:
- check_id: regression
  name: Reporting regression and CLI controls
  status: passed
  required: true
  command: .venv/bin/python -m pytest tests/test_reference_cli_coverage.py tests/test_reference_error_annotation.py
    tests/test_reference_validator_actually_validates.py tests/test_causal_review_batch42.py
    tests/test_causal_review_batch130.py tests/test_phormidium_identity.py -q --no-cov
  exit_code: 0
  summary: "b/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553:\
    \ PydanticDeprecatedSince211: Accessing the 'model_fields' attribute on the instance\
    \ is deprecated. Instead, you should access this attribute from the model class.\
    \ Deprecated in Pydantic V2.11 to be removed in V3.0.\n    imports=imports, **{k:\
    \ getattr(self, k, None) for k in self.model_fields if k != \"imports\"}\n\n--\
    \ Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html\n48 passed,\
    \ 14 warnings in 104.08s (0:01:44)"
  target_ids:
  - explained-cli
  - review-index
  - batch132-coverage
  - batch130-coverage
  evidence_ids:
  - regression
- check_id: lint
  name: lint
  status: passed
  required: true
  command: just --no-dotenv lint
  exit_code: 0
  summary: 'All checks passed!

    Success: no issues found in 49 source files'
  target_ids:
  - explained-cli
  - review-index
  - batch132-coverage
  - batch130-coverage
  evidence_ids:
  - lint
- check_id: explained-cli
  name: explained-cli
  status: passed
  required: true
  command: just --no-dotenv validate-references-explained kb/communities/Phormidium_Alkaline_Consortium.yaml
  exit_code: 0
  summary: "Validating kb/communities/Phormidium_Alkaline_Consortium.yaml against\
    \ schema src/communitymech/schema/communitymech.yaml\nCache directory: references_cache\n\
    \nValidation Summary:\n  Reported validation issues: 0\n  All validations passed!\n\
    \n[annotate] This is not a count of checked excerpts (#1469). Native Discussion\
    \ evidence coverage remains incomplete (#476)."
  target_ids:
  - explained-cli
  - review-index
  - batch132-coverage
  - batch130-coverage
  evidence_ids:
  - explained-cli
- check_id: review-contract-before
  name: review-contract-before
  status: passed
  required: true
  command: just --no-dotenv check-record-reviews
  exit_code: 0
  summary: "{\n  \"repository\": \"culturebotai/CommunityMech\",\n  \"valid_reviews\"\
    : 25,\n  \"coverage\": \"declared_scopes_only\"\n}"
  target_ids:
  - explained-cli
  - review-index
  - batch132-coverage
  - batch130-coverage
  evidence_ids:
  - review-contract-before
- check_id: preservation
  name: preservation
  status: passed
  required: true
  command: git diff --exit-code f293d935 -- kb/communities data/isolates references_cache
    history docs/communities reviews/structured/20261015T014050Z-phormidium-identity-after
    reviews/structured/20261014T222155Z-phage-graphs-after
  exit_code: 0
  summary: No changed canonical, source, history, generated community or prior-review
    bytes.
  target_ids:
  - explained-cli
  - review-index
  - batch132-coverage
  - batch130-coverage
  evidence_ids:
  - preservation
evidence:
- evidence_id: final-phormidium-cli
  kind: validation
  reference: reports/reference_cli_coverage/final-phormidium-cli.json
  locator: actual CLI output, traced excerpt paths, mutation/restoration exits, input
    hashes
  accessed_at: '2026-10-15T03:10:06.717930Z'
  support: supports
  summary: Native CLI checks EvidenceItem snippets; the summary counts issues. Discussion
    mutations remain invisible where present.
- evidence_id: alseth-cli
  kind: validation
  reference: reports/reference_cli_coverage/alseth-cli.json
  locator: actual CLI output, traced excerpt paths, mutation/restoration exits, input
    hashes
  accessed_at: '2026-10-15T03:10:06.717930Z'
  support: supports
  summary: Native CLI checks EvidenceItem snippets; the summary counts issues. Discussion
    mutations remain invisible where present.
- evidence_id: final-pha-cli
  kind: validation
  reference: reports/reference_cli_coverage/final-pha-cli.json
  locator: actual CLI output, traced excerpt paths, mutation/restoration exits, input
    hashes
  accessed_at: '2026-10-15T03:10:06.717930Z'
  support: supports
  summary: Native CLI checks EvidenceItem snippets; the summary counts issues. Discussion
    mutations remain invisible where present.
- evidence_id: surfaces
  kind: record_content
  reference: scripts/annotate_reference_errors.py
  locator: main() summary handling and all four declared target surfaces
  accessed_at: '2026-10-15T03:10:06.717930Z'
  support: supports
  summary: Explained output labels issue counts explicitly; current index and this
    successor correct the historical claim.
- evidence_id: regression
  kind: validation
  reference: reports/reference_cli_coverage/after-regression.json
  locator: command, exit, stdout/stderr, input hashes
  accessed_at: '2026-10-15T03:10:06.717930Z'
  support: supports
  summary: "b/python3.13/site-packages/linkml/generators/pydanticgen/template.py:553:\
    \ PydanticDeprecatedSince211: Accessing the 'model_fields' attribute on the instance\
    \ is deprecated. Instead, you should access this attribute from the model class.\
    \ Deprecated in Pydantic V2.11 to be removed in V3.0.\n    imports=imports, **{k:\
    \ getattr(self, k, None) for k in self.model_fields if k != \"imports\"}\n\n--\
    \ Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html\n48 passed,\
    \ 14 warnings in 104.08s (0:01:44)"
- evidence_id: lint
  kind: validation
  reference: reports/reference_cli_coverage/lint.json
  locator: command and exact output
  accessed_at: '2026-10-15T03:10:06.717930Z'
  support: supports
  summary: 'Successful bounded check: lint'
- evidence_id: explained-cli
  kind: validation
  reference: reports/reference_cli_coverage/explained-cli.json
  locator: command and exact output
  accessed_at: '2026-10-15T03:10:06.717930Z'
  support: supports
  summary: 'Successful bounded check: explained-cli'
- evidence_id: review-contract-before
  kind: validation
  reference: reports/reference_cli_coverage/review-contract-before.json
  locator: command and exact output
  accessed_at: '2026-10-15T03:10:06.717930Z'
  support: supports
  summary: 'Successful bounded check: review-contract-before'
- evidence_id: preservation
  kind: validation
  reference: reports/reference_cli_coverage/preservation.json
  locator: command and exact output
  accessed_at: '2026-10-15T03:10:06.717930Z'
  support: supports
  summary: 'Successful bounded check: preservation'
assessments:
- assessment_id: reporting
  area: provenance
  topic: Counter semantics versus actual traversal
  outcome: supported
  summary: CLI canaries establish the concrete coverage counts and the remaining Discussion
    omission. This correction supersedes only the mistaken zero-coverage interpretation,
    not the prior scientific findings.
  target_ids:
  - explained-cli
  - review-index
  - batch132-coverage
  - batch130-coverage
  evidence_ids:
  - final-phormidium-cli
  - alseth-cli
  - final-pha-cli
  - surfaces
  - regression
findings:
- finding_id: cli-count-recurrence
  issue_key: communitymech-1469-20261015-recurrence
  category: provenance
  severity: minor
  status: resolved
  certainty: confirmed
  title: Issue-count output misclassified as zero validation coverage
  description: 'Batch132 marked reference-cli failed from Total checks: 0. Batch130
    and the current index also describe zero checks. Actual CLI probes trace 21, 27
    and 24 checked excerpts with negative controls. The counter is not coverage.'
  target_ids:
  - explained-cli
  - review-index
  - batch132-coverage
  - batch130-coverage
  field_paths:
  - checks[reference-cli]
  - limitations
  - main()
  - Batch130/Batch132 summaries
  evidence_ids:
  - final-phormidium-cli
  - alseth-cli
  - final-pha-cli
  - surfaces
  - regression
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: scripts/annotate_reference_errors.py
    role: maintained reporting surface
  - repository: CultureBotAI/CommunityMech
    path: reports/causal_graph_review/README.md
    role: maintained reporting surface
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1469
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T030500Z-reference-cli-coverage-before
    finding_id: cli-count-recurrence
  disposition_reason: Append-only correction and maintained index now distinguish
    a clean native finding count from measured coverage; explained CLI labels the
    counter correctly and regression controls pass. No historical bundle or raw output
    is rewritten.
actions: []
limitations:
- Source-based implementing-agent self-review, not independent approval or scientific
  recertification.
- 'Native Discussion traversal #476 and supplement routing #1996 remain open; no sources
  are combined and no matching thresholds change.'
- This scoped disposition does not retire unrelated findings in the two earlier reviews
  or claim whole-corpus completion.
- Remote CI/protected merge is recorded separately after this immutable local snapshot.
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261015T014050Z-phormidium-identity-after
  relationship: Corrects CLI coverage interpretation only; other findings retained
- repository: CultureBotAI/CommunityMech
  review_id: 20261014T222155Z-phage-graphs-after
  relationship: Corrects CLI coverage interpretation only; other findings retained
links:
- https://github.com/CultureBotAI/CommunityMech/issues/1469
```
