# Parachlorella assay scope after

- Review: 20261015T134821Z-parachlorella-after
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-15T13:48:21.671217Z
- Finished UTC: 2026-10-15T13:48:21.671217Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Correct existing assay attribution while preserving unresolved mechanistic scope.

## Scope And Provenance

Four existing graph nodes and two edges; full record read but non-graph metadata not certified.

Selection: Source follow-up to issue1681 and new bounded correction2020
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a633f798a2515cbc903d205bef94b69458783120.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | Parachlorella-Saccharomyces coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| check-diff | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-docs-current | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-gen-html | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-history | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-inventory | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-lint | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-network | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-rank | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-references | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-regression | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-snippets | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-strict | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-terms | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| check-validate | passed | True | CommunityMech:000295 | Passed within recorded scope; not scientific certification. |
| Full local suite collection | failed | True | CommunityMech:000295 | Not a passing local full-suite run; require GitHub validate-strict full suite before merge. |
| Separate supplementary assays | unavailable | True | CommunityMech:000295 | S1/S2/S3 and TableS1 were not inspected; issue1681 remains open. |

## Scientific And Domain Assessments

### Proposed Reciprocal Oxygen and Carbon Dioxide Exchange

graph: unknown. Targets: CommunityMech:000295.

Retain gas exchange as proposed mediation; main text does not isolate it with direct flux/perturbation assays.

ecological_interactions[0]; PMID42217804. Methods2.1-2.4; Results3.2-3.5. No strain identity replacement or taxonomic recertification.

### Yeast support of microalgal growth and lipid accumulation

graph: supported. Targets: CommunityMech:000295.

Retain observed yeast-associated algal growth; nutrient competition remains the authors' interpretation of lipid response.

ecological_interactions[1]; PMID42217804. Methods2.1-2.4; Results3.2-3.5. No strain identity replacement or taxonomic recertification.

### Proposed EPS-Derived Metabolic Support of Yeast

graph: unknown. Targets: CommunityMech:000295.

Retain viable yeast and physical observations without inferring EPS uptake or necessity.

ecological_interactions[2]; PMID42217804. Methods2.1-2.4; Results3.2-3.5. No strain identity replacement or taxonomic recertification.

### Coculture Algal Cell Increase and Relative Lipid Signal

graph: supported. Targets: CommunityMech:000295.

Distinguish day12 algal cell counts from day14 normalized bulk lipid fluorescence, with matched-medium control and conflicting source numbers.

ecological_interactions[3]; PMID42217804. Methods2.1-2.4; Results3.2-3.5. No strain identity replacement or taxonomic recertification.

### Retained incoming link 0

graph: unknown. Targets: CommunityMech:000295.

Retain proposed gas mediation.

ecological_interactions[0].downstream[0] -&gt; Coculture Algal Cell Increase and Relative Lipid Signal. HYPOTHESIZED - Respiratory CO2 and photosynthetic oxygen could support coculture growth. Main-text comparisons do not isolate gas exchange as the cause of the species-resolved algal cell increase or bulk relative lipid signal; medium enrichment contributes to the growth comparison.

### Retained incoming link 1

graph: supported. Targets: CommunityMech:000295.

Retain partial physiological contribution; total fold change includes medium enrichment.

ecological_interactions[1].downstream[0] -&gt; Coculture Algal Cell Increase and Relative Lipid Signal. PARTIAL - Yeast-associated maintenance of algal growth contributes to the cell-count endpoint. Nutrient competition is the authors' proposed explanation of increased relative lipid signal. The enriched-medium control also increases growth, so the full control-relative fold change cannot be assigned to yeast or a particular exchanged metabolite.

## Findings

### assay-scope: Growth and lipid endpoint conflation

major / resolved / confirmed; issue key: parachlorella-assay-scope.

Existing endpoint conflates algal cell counts with bulk fluorescence and obscures the matched-medium comparator. Correct wording/evidence without adding topology.

Disposition: Re-read current graph against Methods2.1.2/2.3, Results3.2 and Fig3; exact primary excerpts, separate endpoint scopes, source conflicts and regression checks now retained.

### remaining-research: Supplement and physical-adhesion structure review remains incomplete

major / open / confirmed; issue key: parachlorella-remaining-research.

Main article access resolves the prior main-text barrier, but not separate supplements, dye/fold reporting conflicts, mediator specificity or provider-required new structure.

## Recommended Actions And Acceptance Checks

### follow-remaining-research

Main article access resolves the prior main-text barrier, but not separate supplements, dye/fold reporting conflicts, mediator specificity or provider-required new structure.

- Attach exact primary evidence at the affected claims.
- Preserve source conflicts and remaining research limits.
- Run required provider workflow before any new topology.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | doi:10.1016/j.biortech.2026.135004; HAL PDF; Methods2.1-2.4, Results3.1-3.5, Fig3,4,6; source-access.md gives PDF hash and inspection scope | supports | Species-resolved algal counts differ from bulk relative Nile Red signal; medium control and source reporting conflicts must be retained. |
| record | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml; Whole record read; four graph nodes and two downstream links assessed | context_only | Existing topology retained; no new physical-adhesion node or independent approval. |
| access | reports/causal_graph_review/20261015-parachlorella-assays/source-access.md; Dated public access, figure scope and search exclusions | context_only | Primary main article available; separate supplements and raw data uninspected. |
| check-diff | reports/causal_graph_review/20261015-parachlorella-assays/check-diff.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-docs-current | reports/causal_graph_review/20261015-parachlorella-assays/check-docs-current.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-gen-html | reports/causal_graph_review/20261015-parachlorella-assays/check-gen-html.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-history | reports/causal_graph_review/20261015-parachlorella-assays/check-history.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-inventory | reports/causal_graph_review/20261015-parachlorella-assays/check-inventory.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-lint | reports/causal_graph_review/20261015-parachlorella-assays/check-lint.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-network | reports/causal_graph_review/20261015-parachlorella-assays/check-network.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-rank | reports/causal_graph_review/20261015-parachlorella-assays/check-rank.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-references | reports/causal_graph_review/20261015-parachlorella-assays/check-references.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-regression | reports/causal_graph_review/20261015-parachlorella-assays/check-regression.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-snippets | reports/causal_graph_review/20261015-parachlorella-assays/check-snippets.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-strict | reports/causal_graph_review/20261015-parachlorella-assays/check-strict.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-terms | reports/causal_graph_review/20261015-parachlorella-assays/check-terms.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| check-validate | reports/causal_graph_review/20261015-parachlorella-assays/check-validate.json; Exact command, exit code, timestamps and stdout/stderr | context_only | Scoped gate receipt; network exit1 consists only of existing warnings. |
| local-suite | reports/causal_graph_review/20261015-parachlorella-assays/local-full-suite.json; Collection traceback and command | context_only | Local full-suite collection failed for missing numba. Locked numba/llvmlite installation also failed to build on this x86_64 macOS environment; CI remains required. |

## Limits And Additional Notes

- Separate supplements and raw data uninspected; no independent approval.
- No new topology or provider report; remaining research is not completed by structural validation.
- Whole-record native completeness/validation-quality scores not assessed by this graph-only review; node/edge coverage denominators are 4 and 2.
- Non-graph metadata issue1683 is outside this correction, preserved and not disposed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T134821Z-parachlorella-after
kind: record
repository: CultureBotAI/CommunityMech
title: Parachlorella assay scope after
started_at: '2026-10-15T13:48:21.671217Z'
finished_at: '2026-10-15T13:48:21.671217Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Source-based adversarial review by the implementing agent; not
    independent approval.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
native_verdict: needs_research
scientific_review: true
source:
  git_revision: a633f798a2515cbc903d205bef94b69458783120
  state: working_tree
  inputs:
  - path: docs/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.html
    sha256: 42a0a535e9130f4770a36b9884c33c6100751a096152651a0e3dd5974cecaa77
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/Parachlorella_Saccharomyces_Mutualistic_Coculture/2026-10-15T134007Z-claude-code-904656.yaml
    sha256: a0600bf8f962373bb97cfa58061456d17f1d93d27713f35b5478aa1849afcb65
    role: context
  - path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    sha256: 1e5ee2a939774f3954bdb42b6c4124c1de1f0b36a3dc7b3e93e74ad52baa199b
    role: target
  - path: references_cache/PMID_42217804.md
    sha256: ddb1c398c3cf5bbf87c3197543ed17d3a581e33635f72f09b2750fb2e24a973b
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-diff.json
    sha256: e55caed38f22d7b64f8cd716d8e0a6d730f47ef59d55ecb959684b685476be83
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-docs-current.json
    sha256: 9dae5d2ae204a00e40a9d7092f98d6a16a0980a40c5ef89ca3d8a2644bb6b8e7
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-gen-html.json
    sha256: e22fcb649931798f9d0dad5904075873fa53ef6f3bf6f6b618f4de7d9ed5434a
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-history.json
    sha256: d8a26172c0131135101936faa539b73f6dbe7f9d1c400b28e4c43e4fa2fdbbf3
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-inventory.json
    sha256: 68cb6ba0d40a4a546a0dc704009a972a1baea35434b883341c8783e90637f410
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-lint.json
    sha256: 47620c4e5962b9dbdde6e804b07933850d96ab89707ed19645a15c7ac1bec89e
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-network.json
    sha256: 3ac88547346b32ddfdcb97006ff1a964d7932c941c0f352fe02f02ee1691f250
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-rank.json
    sha256: 21b8c14e410f669df5e2caaf374b5a776a2b023922c25dbf5336989d3bd27e23
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-references.json
    sha256: f6d5ae549e39a4df6224721f9fa49ea37e38d3f93cb1778587340c6fc0dc8b47
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-regression.json
    sha256: 07bc73b849979cd2e91b30d791462e18d14b2581a7231343d6745ea479279d43
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-snippets.json
    sha256: b238a0f66b02ab63e412c63381cf6285b7ba363c18425e0299294e0b2ecc41a6
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-strict.json
    sha256: fa7143c3dd3dedb1d9872d457082b3f97d0a5e25066f9c2f1a2c241e405e653f
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-terms.json
    sha256: 7c0ebcf244805a4bcad32e2d0d526467ef06ee014152b372b905276b5495c4f6
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/check-validate.json
    sha256: 5b5296bee1b1db05ea77f903507a85b273c713bf32fca13c1673ec5912f46e09
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/local-full-suite.json
    sha256: 8bccbe9fc898bc330c826b06f6515e10f4e1a6caaa70d3463343c0f1d437045d
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/primary-verification.json
    sha256: 8d4fa185f6fd3bfb4ff3fd9527bab60413beeeb8d6a0c30e24d0db57fae9379a
    role: context
  - path: reports/causal_graph_review/20261015-parachlorella-assays/source-access.md
    sha256: 4458e44a9d057ceb26d85a81a96178c7a02e2f99339f3ddc99a01abafe8d8aa1
    role: context
  - path: reports/causal_graph_review/decisions/20261007-four-records-batch82.yaml
    sha256: 287d391e90ad2e832c8cf57a63e6db79adfd6a73fa59a670dc6441c1466cea58
    role: context
  - path: reports/causal_graph_review/decisions/20261015-parachlorella-assays.yaml
    sha256: 95c5ad4a80fd5cb35e5c0ed76e3c8122a658b6afacf7ccf93479f85889d9e45a
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: tests/test_causal_review_batch82.py
    sha256: 197cc7c630a870d2dfe77bc448a0cb07782e6518687358a9ae139d6a3b73e105
    role: context
  - path: tests/test_parachlorella_assay_scope.py
    sha256: 407389928655c0dd2442094cdaf96facb9ea1d75abd5bf48a838103cb35f67d7
    role: context
targets:
- target_id: CommunityMech:000295
  path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  label: Parachlorella-Saccharomyces coculture
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
summary: Correct existing assay attribution while preserving unresolved mechanistic
  scope.
scope:
  description: Four existing graph nodes and two edges; full record read but non-graph
    metadata not certified.
  selection: Source follow-up to issue1681 and new bounded correction2020
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000295
checks:
- check_id: check-diff
  name: check-diff
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-diff
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-docs-current
  name: check-docs-current
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-docs-current
  command: just --no-dotenv check-docs-current
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-gen-html
  name: check-gen-html
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-gen-html
  command: just --no-dotenv gen-html
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-history
  name: check-history
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-history
  command: just --no-dotenv validate-history history/records/Parachlorella_Saccharomyces_Mutualistic_Coculture/2026-10-15T134007Z-claude-code-904656.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-inventory
  name: check-inventory
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-inventory
  command: /private/tmp/communitymech-causal-20261014/.venv/bin/python reports/causal_graph_review/build_inventory.py
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-lint
  name: check-lint
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-lint
  command: just --no-dotenv lint
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-network
  name: check-network
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-network
  command: just --no-dotenv audit-network-json
  exit_code: 1
  expected_exit_code: 1
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-rank
  name: check-rank
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-rank
  command: just --no-dotenv rank-causal-graphs kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-references
  name: check-references
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-references
  command: just --no-dotenv validate-references-explained kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-regression
  name: check-regression
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-regression
  command: /private/tmp/communitymech-causal-20261014/.venv/bin/pytest tests/test_parachlorella_assay_scope.py
    tests/test_causal_review_batch82.py tests/test_causal_review_inventory.py tests/test_network_auditor.py
    -q --no-cov
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-snippets
  name: check-snippets
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-snippets
  command: just --no-dotenv audit-snippets kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-strict
  name: check-strict
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-strict
  command: just --no-dotenv validate-strict kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-terms
  name: check-terms
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-terms
  command: just --no-dotenv validate-terms kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: check-validate
  name: check-validate
  status: passed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - check-validate
  command: just --no-dotenv validate kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Passed within recorded scope; not scientific certification.
- check_id: local-suite
  name: Full local suite collection
  status: failed
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - local-suite
  command: .venv/bin/pytest tests/ -q --no-cov
  exit_code: 2
  expected_exit_code: 0
  summary: Not a passing local full-suite run; require GitHub validate-strict full
    suite before merge.
- check_id: supplements
  name: Separate supplementary assays
  status: unavailable
  required: true
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - access
  summary: S1/S2/S3 and TableS1 were not inspected; issue1681 remains open.
evidence:
- evidence_id: primary
  kind: primary_source
  reference: doi:10.1016/j.biortech.2026.135004
  locator: HAL PDF; Methods2.1-2.4, Results3.1-3.5, Fig3,4,6; source-access.md gives
    PDF hash and inspection scope
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: supports
  summary: Species-resolved algal counts differ from bulk relative Nile Red signal;
    medium control and source reporting conflicts must be retained.
- evidence_id: record
  kind: record_content
  reference: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  locator: Whole record read; four graph nodes and two downstream links assessed
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Existing topology retained; no new physical-adhesion node or independent
    approval.
- evidence_id: access
  kind: search
  reference: reports/causal_graph_review/20261015-parachlorella-assays/source-access.md
  locator: Dated public access, figure scope and search exclusions
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Primary main article available; separate supplements and raw data uninspected.
  search_scope: Ignored/hidden-inclusive scoped local search; GitHub all-state Parachlorella
    title/body search.
- evidence_id: check-diff
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-diff.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-docs-current
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-docs-current.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-gen-html
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-gen-html.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-history
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-history.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-inventory
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-inventory.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-lint
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-lint.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-network
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-network.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-rank
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-rank.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-references
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-references.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-regression
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-regression.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-snippets
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-snippets.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-strict
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-strict.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-terms
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-terms.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: check-validate
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/check-validate.json
  locator: Exact command, exit code, timestamps and stdout/stderr
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Scoped gate receipt; network exit1 consists only of existing warnings.
- evidence_id: local-suite
  kind: validation
  reference: reports/causal_graph_review/20261015-parachlorella-assays/local-full-suite.json
  locator: Collection traceback and command
  accessed_at: '2026-10-15T13:48:21.671217Z'
  support: context_only
  summary: Local full-suite collection failed for missing numba. Locked numba/llvmlite
    installation also failed to build on this x86_64 macOS environment; CI remains
    required.
assessments:
- assessment_id: node-0
  area: graph
  topic: Proposed Reciprocal Oxygen and Carbon Dioxide Exchange
  outcome: unknown
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  - access
  summary: Retain gas exchange as proposed mediation; main text does not isolate it
    with direct flux/perturbation assays.
  details: ecological_interactions[0]; PMID42217804. Methods2.1-2.4; Results3.2-3.5.
    No strain identity replacement or taxonomic recertification.
  dimensions:
  - name: experimental-system
    value: P. kessleri UTEX2229 + S. cerevisiae BY4741; engineered coculture in glucose/peptone-supplemented
      BBM
    definition: Primary-source assay scope, not natural-community generalization
    evidence_ids:
    - primary
- assessment_id: node-1
  area: graph
  topic: Yeast support of microalgal growth and lipid accumulation
  outcome: supported
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  - access
  summary: Retain observed yeast-associated algal growth; nutrient competition remains
    the authors' interpretation of lipid response.
  details: ecological_interactions[1]; PMID42217804. Methods2.1-2.4; Results3.2-3.5.
    No strain identity replacement or taxonomic recertification.
  dimensions:
  - name: experimental-system
    value: P. kessleri UTEX2229 + S. cerevisiae BY4741; engineered coculture in glucose/peptone-supplemented
      BBM
    definition: Primary-source assay scope, not natural-community generalization
    evidence_ids:
    - primary
- assessment_id: node-2
  area: graph
  topic: Proposed EPS-Derived Metabolic Support of Yeast
  outcome: unknown
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  - access
  summary: Retain viable yeast and physical observations without inferring EPS uptake
    or necessity.
  details: ecological_interactions[2]; PMID42217804. Methods2.1-2.4; Results3.2-3.5.
    No strain identity replacement or taxonomic recertification.
  dimensions:
  - name: experimental-system
    value: P. kessleri UTEX2229 + S. cerevisiae BY4741; engineered coculture in glucose/peptone-supplemented
      BBM
    definition: Primary-source assay scope, not natural-community generalization
    evidence_ids:
    - primary
- assessment_id: node-3
  area: graph
  topic: Coculture Algal Cell Increase and Relative Lipid Signal
  outcome: supported
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  - access
  summary: Distinguish day12 algal cell counts from day14 normalized bulk lipid fluorescence,
    with matched-medium control and conflicting source numbers.
  details: ecological_interactions[3]; PMID42217804. Methods2.1-2.4; Results3.2-3.5.
    No strain identity replacement or taxonomic recertification.
  dimensions:
  - name: experimental-system
    value: P. kessleri UTEX2229 + S. cerevisiae BY4741; engineered coculture in glucose/peptone-supplemented
      BBM
    definition: Primary-source assay scope, not natural-community generalization
    evidence_ids:
    - primary
- assessment_id: edge-0
  area: graph
  topic: Retained incoming link 0
  outcome: unknown
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  summary: Retain proposed gas mediation.
  details: ecological_interactions[0].downstream[0] -> Coculture Algal Cell Increase
    and Relative Lipid Signal. HYPOTHESIZED - Respiratory CO2 and photosynthetic oxygen
    could support coculture growth. Main-text comparisons do not isolate gas exchange
    as the cause of the species-resolved algal cell increase or bulk relative lipid
    signal; medium enrichment contributes to the growth comparison.
- assessment_id: edge-1
  area: graph
  topic: Retained incoming link 1
  outcome: supported
  target_ids:
  - CommunityMech:000295
  evidence_ids:
  - primary
  - record
  summary: Retain partial physiological contribution; total fold change includes medium
    enrichment.
  details: ecological_interactions[1].downstream[0] -> Coculture Algal Cell Increase
    and Relative Lipid Signal. PARTIAL - Yeast-associated maintenance of algal growth
    contributes to the cell-count endpoint. Nutrient competition is the authors' proposed
    explanation of increased relative lipid signal. The enriched-medium control also
    increases growth, so the full control-relative fold change cannot be assigned
    to yeast or a particular exchanged metabolite.
findings:
- finding_id: assay-scope
  issue_key: parachlorella-assay-scope
  title: Growth and lipid endpoint conflation
  description: Existing endpoint conflates algal cell counts with bulk fluorescence
    and obscures the matched-medium comparator. Correct wording/evidence without adding
    topology.
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  target_ids:
  - CommunityMech:000295
  field_paths:
  - ecological_interactions
  - discussions
  evidence_ids:
  - primary
  - record
  - access
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  rule_id: CLAUDE.claim-level-evidence
  native_severity: P2
  normalization_reason: Assay attribution and mediator certainty affect scientific
    interpretation.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2020
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T133733Z-parachlorella-before
    finding_id: assay-scope
  disposition_reason: Re-read current graph against Methods2.1.2/2.3, Results3.2 and
    Fig3; exact primary excerpts, separate endpoint scopes, source conflicts and regression
    checks now retained.
- finding_id: remaining-research
  issue_key: parachlorella-remaining-research
  title: Supplement and physical-adhesion structure review remains incomplete
  description: Main article access resolves the prior main-text barrier, but not separate
    supplements, dye/fold reporting conflicts, mediator specificity or provider-required
    new structure.
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  target_ids:
  - CommunityMech:000295
  field_paths:
  - ecological_interactions
  - discussions
  evidence_ids:
  - primary
  - record
  - access
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  rule_id: CLAUDE.claim-level-evidence
  native_severity: P2
  normalization_reason: Assay attribution and mediator certainty affect scientific
    interpretation.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T133733Z-parachlorella-before
    finding_id: remaining-research
actions:
- action_id: follow-remaining-research
  finding_ids:
  - remaining-research
  target_ids:
  - CommunityMech:000295
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  description: Main article access resolves the prior main-text barrier, but not separate
    supplements, dye/fold reporting conflicts, mediator specificity or provider-required
    new structure.
  acceptance_checks:
  - Attach exact primary evidence at the affected claims.
  - Preserve source conflicts and remaining research limits.
  - Run required provider workflow before any new topology.
limitations:
- Separate supplements and raw data uninspected; no independent approval.
- No new topology or provider report; remaining research is not completed by structural
  validation.
- Whole-record native completeness/validation-quality scores not assessed by this
  graph-only review; node/edge coverage denominators are 4 and 2.
- Non-graph metadata issue1683 is outside this correction, preserved and not disposed.
```
