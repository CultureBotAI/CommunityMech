# Cheese-rind evidence-boundary before review

- Review: 20261015T091351Z-cheese-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-15T09:13:51.099910Z
- Finished UTC: 2026-10-15T09:13:51.099910Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Bound existing graph wording to retained evidence without declaring unresolved mechanisms false or closing the research gap.

## Scope And Provenance

All three existing graph nodes and their zero arrows, one record; non-graph fields read for context but not certified.

Selection: Cheese-rind follow-up to #765 and focused wording finding #2015.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 3b9026603de970a028d436c192a23b6e0ad792ea.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000153 | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml | maintained | Cheese rind graph evidence boundary |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| baseline-inventory | passed | True | CommunityMech:000153 | Passed; exact command output retained. |
| edison-dry-run | passed | True | CommunityMech:000153 | Passed; exact command output retained. |
| Exact-system primary methods and Table S5 | unavailable | True | CommunityMech:000153 | Access checks did not supply the full source; snippets cannot certify the assay roster. |
| Provider-assisted new-structure research | unavailable | True | CommunityMech:000153 | Dry run only. Spend authorized previously, but inherited credential names absent; dotenv is prohibited. No new structure is added. |

## Scientific And Domain Assessments

### Moisture-Structured Rind Community Assembly

graph: unknown. Targets: CommunityMech:000153.

Moisture mechanism is unresolved; no retained node evidence and no salt/moisture isolation certified.

Field ecological_interactions[0]. Scope COMMUNITY_LEVEL; individual source/target participants and strains unresolved. No downstream direction exists; zero arrows reviewed, none added.

### Proposed Fungal Deacidification and Bacterial Growth Responses

graph: unknown. Targets: CommunityMech:000153.

Deacidification is unresolved; no retained node evidence, responsive participant assignment or mediator necessity certified.

Field ecological_interactions[1]. Scope COMMUNITY_LEVEL; individual source/target participants and strains unresolved. No downstream direction exists; zero arrows reviewed, none added.

### Reproducible Natural-Rind Succession

graph: supported. Targets: CommunityMech:000153.

Retained abstract supports broad succession recapitulation, not member-specific facilitation or quantitative timing.

Field ecological_interactions[2]. Scope COMMUNITY_LEVEL; individual source/target participants and strains unresolved. No downstream direction exists; zero arrows reviewed, none added.

## Findings

### graph-wording: Graph descriptions exceed their retained evidence

major / open / confirmed; issue key: cheese-graph-abstract-boundary.

Moisture/salt effects, fungal pH/growth responses and relative succession speed were stated as observations although the retained abstract does not establish them. Their truth is not refuted; their evidence boundary must be explicit.

### evidence-gap: Assay-specific evidence and membership remain unresolved

major / open / confirmed; issue key: cheese-assay-evidence-gap.

Two nodes lack retained evidence. Exact memberships, growth versus recovery conditions and mechanism isolation need primary-source review. This one-record finding does not supersede the multi-record scope of #765.

## Recommended Actions And Acceptance Checks

### qualify-wording

Qualify existing unsupported mechanisms and narrow succession to abstract support.

- No new nodes/arrows, taxonomy or non-graph changes.
- Keep #765 and needs_research open.
- Run validators, regression, generated-docs and review-contract checks.

### source-reconciliation

Obtain permitted inspectable primary evidence and reconcile assay membership before graph extension.

- Inspect main methods, figures and Table S5, preserving any conflicts.
- Attach exact claim-level evidence with reuse provenance; no removed body restoration.
- Complete authorized Edison workflow before any new causal structure.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml; All three ecological_interactions and attached discussion; whole record read | context_only | Three community-level nodes, zero arrows, four genus entries; only succession has graph evidence. |
| abstract | PMID:25036636; references_cache/PMID_25036636.md and .txt, complete retained abstracts | partial | Supports broad composition/succession reproducibility and positive/negative interactions; not moisture/pH mediation, exact assay members or timing. |
| access | reports/causal_graph_review/20261015-cheese-evidence/source-access.md; Dated public access attempts and bounded local discovery | context_only | Full methods, figure images and Table S5 remain unverified. No publisher body restored. |
| baseline-inventory | reports/causal_graph_review/20261015-cheese-evidence/baseline-inventory.json; command, exit_code, stdout, stderr and record hashes | context_only | Passed; exact command output retained. |
| edison-dry-run | reports/causal_graph_review/20261015-cheese-evidence/edison-dry-run.json; command, exit_code, stdout, stderr and record hashes | context_only | Passed; exact command output retained. |

## Limits And Additional Notes

- Complete methods, original figures, Table S5 and raw data were not inspected; search-index leads are not canonical evidence.
- No independent review or whole-record scientific pass. Taxonomy, cultivation, aromas and other non-graph claims are preserved, not certified.
- Whole-record completeness/validation-quality metrics are not assessed by this graph-only review; graph evidence is one item across three nodes, not adequate evidence for all three.
- Edison real run unavailable; dry run spends zero credits. No new structure attempted.
- Historical pre-repair review: input hashes were inspected before editing and reproduced from the retained baseline commit. The unsaved draft initially failed the no-YAML-alias format rule; no scientific finding was changed by serializing without aliases.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261015T091351Z-cheese-before
kind: record
repository: CultureBotAI/CommunityMech
title: Cheese-rind evidence-boundary before review
started_at: '2026-10-15T09:13:51.099910Z'
finished_at: '2026-10-15T09:13:51.099910Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Implementing-agent adversarial self-review, not independent
    approval.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
native_verdict: needs_research
scientific_review: true
source:
  git_revision: 3b9026603de970a028d436c192a23b6e0ad792ea
  state: git_commit
  inputs:
  - path: .claude/skills/review-communities/reference/metrics-and-reports.md
    sha256: 2647416ac98a8f9569e0afbd826a0d1229bb4262639934848639ce536b0974fc
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    sha256: 70f98b384879211c2cb7141b419e33e144b90be0dbe11b950c0d4e8e97662135
    role: target
  - path: kb/communities/Kefir_Flavor_Lentilactobacillus_Kluyveromyces_Coculture.yaml
    sha256: f562c28689b45ec3c53061db80bb3c6f33c4e464fe82b7d2d8236eebf53c383d
    role: context
  - path: references_cache/PMID_25036636.md
    sha256: d26f0ccc376961a44db427ddc2e4c0bbabbcdc518453b017c40dde11c1e34850
    role: context
  - path: references_cache/PMID_25036636.txt
    sha256: ee66a8799e742652d72094e1d62b07dcf5f399bc6fb15b71738bd7320ee729b3
    role: context
  - path: reports/causal_graph_review/20261015-cheese-evidence/baseline-inventory.json
    sha256: 3dfdb0e28a536b1c3ce594eccd21b1383e583c9ffb98c6ae9bb1474b0f736fcf
    role: context
  - path: reports/causal_graph_review/20261015-cheese-evidence/edison-dry-run.json
    sha256: 77913811e1b5c539d785bfe51e85f36d348eece58b4da041d593e614c4433e25
    role: context
  - path: reports/causal_graph_review/20261015-cheese-evidence/source-access.md
    sha256: 4bacdb526dbbec6be3dfd21ce56831a1e269cb767c4e0abe42deb44716d6f5ea
    role: context
  - path: reports/causal_graph_review/decisions/20261005-ten-records-batch10.yaml
    sha256: 7149a6a81f091ff27d40deaf5bf99cb0a9b6486344db20009517f48652fe855d
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_causal_review_batch10.py
    sha256: 3a9bf68c9f95cf2630406ae0c031e491fb41538fbe14e44b5fc110b92c51eaeb
    role: context
targets:
- target_id: CommunityMech:000153
  path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
  label: Cheese rind graph evidence boundary
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical interaction descriptions and uncertainty
summary: Bound existing graph wording to retained evidence without declaring unresolved
  mechanisms false or closing the research gap.
scope:
  description: All three existing graph nodes and their zero arrows, one record; non-graph
    fields read for context but not certified.
  selection: 'Cheese-rind follow-up to #765 and focused wording finding #2015.'
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000153
checks:
- check_id: baseline-inventory
  name: baseline-inventory
  status: passed
  required: true
  command: .venv/bin/python reports/causal_graph_review/build_inventory.py
  exit_code: 0
  expected_exit_code: 0
  summary: Passed; exact command output retained.
  target_ids:
  - CommunityMech:000153
  evidence_ids:
  - baseline-inventory
- check_id: edison-dry-run
  name: edison-dry-run
  status: passed
  required: true
  command: just --no-dotenv research-community-causal Cheese_Rind_InSitu_InVitro_Model_Community
    --dry-run --out-dir research/cheese-scope/edison
  exit_code: 0
  expected_exit_code: 0
  summary: Passed; exact command output retained.
  target_ids:
  - CommunityMech:000153
  evidence_ids:
  - edison-dry-run
- check_id: primary-methods
  name: Exact-system primary methods and Table S5
  status: unavailable
  required: true
  target_ids:
  - CommunityMech:000153
  evidence_ids:
  - access
  summary: Access checks did not supply the full source; snippets cannot certify the
    assay roster.
- check_id: edison-real
  name: Provider-assisted new-structure research
  status: unavailable
  required: true
  target_ids:
  - CommunityMech:000153
  evidence_ids:
  - access
  summary: Dry run only. Spend authorized previously, but inherited credential names
    absent; dotenv is prohibited. No new structure is added.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
  locator: All three ecological_interactions and attached discussion; whole record
    read
  accessed_at: '2026-10-15T09:13:51.099910Z'
  support: context_only
  summary: Three community-level nodes, zero arrows, four genus entries; only succession
    has graph evidence.
- evidence_id: abstract
  kind: primary_source
  reference: PMID:25036636
  locator: references_cache/PMID_25036636.md and .txt, complete retained abstracts
  accessed_at: '2026-10-15T09:13:51.099910Z'
  support: partial
  summary: Supports broad composition/succession reproducibility and positive/negative
    interactions; not moisture/pH mediation, exact assay members or timing.
- evidence_id: access
  kind: search
  reference: reports/causal_graph_review/20261015-cheese-evidence/source-access.md
  locator: Dated public access attempts and bounded local discovery
  accessed_at: '2026-10-15T09:13:51.099910Z'
  support: context_only
  summary: Full methods, figure images and Table S5 remain unverified. No publisher
    body restored.
  search_scope: Ignored/hidden local files included in bounded searches; filename
    pass excluded JSON/JSONL and Edison output. Public source/author searches and
    access limits are itemized in the report; indexed results are leads only.
- evidence_id: baseline-inventory
  kind: validation
  reference: reports/causal_graph_review/20261015-cheese-evidence/baseline-inventory.json
  locator: command, exit_code, stdout, stderr and record hashes
  accessed_at: '2026-10-15T09:13:51.099910Z'
  support: context_only
  summary: Passed; exact command output retained.
- evidence_id: edison-dry-run
  kind: validation
  reference: reports/causal_graph_review/20261015-cheese-evidence/edison-dry-run.json
  locator: command, exit_code, stdout, stderr and record hashes
  accessed_at: '2026-10-15T09:13:51.099910Z'
  support: context_only
  summary: Passed; exact command output retained.
assessments:
- assessment_id: node-0
  area: graph
  topic: Moisture-Structured Rind Community Assembly
  outcome: unknown
  target_ids:
  - CommunityMech:000153
  evidence_ids:
  - record
  - abstract
  - access
  summary: Moisture mechanism is unresolved; no retained node evidence and no salt/moisture
    isolation certified.
  details: Field ecological_interactions[0]. Scope COMMUNITY_LEVEL; individual source/target
    participants and strains unresolved. No downstream direction exists; zero arrows
    reviewed, none added.
  dimensions:
  - name: source-tier
    value: retained abstract only
    definition: Inspected primary text for this reassessment
    evidence_ids:
    - abstract
  - name: experimental-scope
    value: in-situ survey plus in-vitro reconstruction, exact subsets unresolved
    definition: Do not equate four genus entries with each assay roster
    evidence_ids:
    - record
    - access
- assessment_id: node-1
  area: graph
  topic: Proposed Fungal Deacidification and Bacterial Growth Responses
  outcome: unknown
  target_ids:
  - CommunityMech:000153
  evidence_ids:
  - record
  - abstract
  - access
  summary: Deacidification is unresolved; no retained node evidence, responsive participant
    assignment or mediator necessity certified.
  details: Field ecological_interactions[1]. Scope COMMUNITY_LEVEL; individual source/target
    participants and strains unresolved. No downstream direction exists; zero arrows
    reviewed, none added.
  dimensions:
  - name: source-tier
    value: retained abstract only
    definition: Inspected primary text for this reassessment
    evidence_ids:
    - abstract
  - name: experimental-scope
    value: in-situ survey plus in-vitro reconstruction, exact subsets unresolved
    definition: Do not equate four genus entries with each assay roster
    evidence_ids:
    - record
    - access
- assessment_id: node-2
  area: graph
  topic: Reproducible Natural-Rind Succession
  outcome: supported
  target_ids:
  - CommunityMech:000153
  evidence_ids:
  - record
  - abstract
  - access
  summary: Retained abstract supports broad succession recapitulation, not member-specific
    facilitation or quantitative timing.
  details: Field ecological_interactions[2]. Scope COMMUNITY_LEVEL; individual source/target
    participants and strains unresolved. No downstream direction exists; zero arrows
    reviewed, none added.
  dimensions:
  - name: source-tier
    value: retained abstract only
    definition: Inspected primary text for this reassessment
    evidence_ids:
    - abstract
  - name: experimental-scope
    value: in-situ survey plus in-vitro reconstruction, exact subsets unresolved
    definition: Do not equate four genus entries with each assay roster
    evidence_ids:
    - record
    - access
findings:
- finding_id: graph-wording
  issue_key: cheese-graph-abstract-boundary
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Graph descriptions exceed their retained evidence
  description: Moisture/salt effects, fungal pH/growth responses and relative succession
    speed were stated as observations although the retained abstract does not establish
    them. Their truth is not refuted; their evidence boundary must be explicit.
  target_ids:
  - CommunityMech:000153
  field_paths:
  - ecological_interactions[0].description
  - ecological_interactions[1].description
  - ecological_interactions[2].description
  evidence_ids:
  - record
  - abstract
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical interaction descriptions and uncertainty
  rule_id: CLAUDE.evidence-policy
  native_severity: P2
  normalization_reason: Unsupported mechanistic detail changes scientific interpretation.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2015
- finding_id: evidence-gap
  issue_key: cheese-assay-evidence-gap
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Assay-specific evidence and membership remain unresolved
  description: 'Two nodes lack retained evidence. Exact memberships, growth versus
    recovery conditions and mechanism isolation need primary-source review. This one-record
    finding does not supersede the multi-record scope of #765.'
  target_ids:
  - CommunityMech:000153
  field_paths:
  - ecological_interactions
  - discussions
  evidence_ids:
  - record
  - abstract
  - access
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical interaction descriptions and uncertainty
  rule_id: CLAUDE.claim-level-evidence
  native_severity: P2
  normalization_reason: Missing mechanism and participant support prevents scientific
    completion.
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/765
actions:
- action_id: qualify-wording
  finding_ids:
  - graph-wording
  target_ids:
  - CommunityMech:000153
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical interaction descriptions and uncertainty
  description: Qualify existing unsupported mechanisms and narrow succession to abstract
    support.
  acceptance_checks:
  - No new nodes/arrows, taxonomy or non-graph changes.
  - 'Keep #765 and needs_research open.'
  - Run validators, regression, generated-docs and review-contract checks.
- action_id: source-reconciliation
  finding_ids:
  - evidence-gap
  target_ids:
  - CommunityMech:000153
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical interaction descriptions and uncertainty
  description: Obtain permitted inspectable primary evidence and reconcile assay membership
    before graph extension.
  acceptance_checks:
  - Inspect main methods, figures and Table S5, preserving any conflicts.
  - Attach exact claim-level evidence with reuse provenance; no removed body restoration.
  - Complete authorized Edison workflow before any new causal structure.
limitations:
- Complete methods, original figures, Table S5 and raw data were not inspected; search-index
  leads are not canonical evidence.
- No independent review or whole-record scientific pass. Taxonomy, cultivation, aromas
  and other non-graph claims are preserved, not certified.
- Whole-record completeness/validation-quality metrics are not assessed by this graph-only
  review; graph evidence is one item across three nodes, not adequate evidence for
  all three.
- Edison real run unavailable; dry run spends zero credits. No new structure attempted.
notes:
- 'Historical pre-repair review: input hashes were inspected before editing and reproduced
  from the retained baseline commit. The unsaved draft initially failed the no-YAML-alias
  format rule; no scientific finding was changed by serializing without aliases.'
```
