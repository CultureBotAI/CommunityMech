# Historical causal-research prompt direction review

- Review: 20261014T234638Z-causal-prompt-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-14T23:46:38.511339Z
- Finished UTC: 2026-10-14T23:46:38.511339Z
- Reviewer: codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The original template reverses the hydrogen producer/consumer effect in its causal-edge example. This historical observation records the defect before the successor assesses the current fix.

## Scope And Provenance

Scientific direction of the hydrogen example in one maintained research template.

Selection: Prompt used by the next Phormidium causal-graph dry run.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base ec5e6468b74e874f5474c52d1825fa91a0b595b7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| causal-template | templates/community_causal_graph_research.md | maintained | Causal-graph research template |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Primary-source direction assessment | passed | True | causal-template | Read the original template and primary study abstract; added hydrogen inhibits conversion and product removal enables the syntrophic process. |

## Scientific And Domain Assessments

### Producer/consumer direction in a causal research example

graph: concern. Targets: causal-template.

The direction is reversed and can bias future graph research. Correct the example and distinguish it from target-community evidence.

## Findings

### hydrogen-direction: Shared prompt reverses hydrogen-mediated facilitation

major / open / confirmed; issue key: communitymech-2007-hydrogen-direction.

Hydrogen production does not itself lower hydrogen partial pressure; a consuming partner can enable thermodynamically constrained oxidation. The generic chain is not evidence for the queried community.

## Recommended Actions And Acceptance Checks

### correct-example

Correct consumption/production direction and bound illustration versus target evidence.

- Render-path regressions reject the old example and retain target context.
- Illustrative example is not used as source evidence for another community.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| primary | PMID:16347751; https://pubmed.ncbi.nlm.nih.gov/16347751/ ; Abstract, hydrogen inhibition and product removal | refutes | Ahring and Westermann (1988) experimentally report inhibition of thermophilic syntrophic butyrate conversion by hydrogen; growth depends on removing hydrogen and acetate, not on hydrogen production lowering its own partial pressure. |
| original | templates/community_causal_graph_research.md; Causal edges / causal link example at commit ec5e6468b74e874f5474c52d1825fa91a0b595b7 | supports | The example attributes lower pH2 to hydrogen produced by syntrophic oxidation and then appends an unsupported generic acetogen/methanogen chain. |

## Limits And Additional Notes

- Historical source review at the stated commit, not an assessment of the already edited working tree.
- Primary abstract inspected; no quantitative thermodynamic model or whole-record completeness score is asserted.
- New regression tests and current Phormidium source research are assessed separately in the successor.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T234638Z-causal-prompt-before
kind: repository
repository: CultureBotAI/CommunityMech
title: Historical causal-research prompt direction review
started_at: '2026-10-14T23:46:38.511339Z'
finished_at: '2026-10-14T23:46:38.511339Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: Implementing-agent review of the original prompt; not independent
    approval.
skill: communitymech-causal-graphs
completion: completed
verdict: needs_curation
scientific_review: true
summary: The original template reverses the hydrogen producer/consumer effect in its
  causal-edge example. This historical observation records the defect before the successor
  assesses the current fix.
source:
  git_revision: ec5e6468b74e874f5474c52d1825fa91a0b595b7
  state: git_commit
  inputs:
  - path: templates/community_causal_graph_research.md
    sha256: 9b6da51cf48437572e0319dbc0388f49c5fe3014e7c618e94127dae1110ef694
    role: target
scope:
  description: Scientific direction of the hydrogen example in one maintained research
    template.
  selection: Prompt used by the next Phormidium causal-graph dry run.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - causal-template
  exclusions:
  - target: Canonical graphs and whole-template schema synchronization
    reason: Not the scope of this historical direction finding.
targets:
- target_id: causal-template
  path: templates/community_causal_graph_research.md
  label: Causal-graph research template
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: templates/community_causal_graph_research.md
    role: maintained research prompt
checks:
- check_id: source-direction
  name: Primary-source direction assessment
  status: passed
  required: true
  summary: Read the original template and primary study abstract; added hydrogen inhibits
    conversion and product removal enables the syntrophic process.
  target_ids:
  - causal-template
  evidence_ids:
  - primary
  - original
evidence:
- evidence_id: primary
  kind: primary_source
  reference: PMID:16347751
  locator: https://pubmed.ncbi.nlm.nih.gov/16347751/ ; Abstract, hydrogen inhibition
    and product removal
  accessed_at: '2026-10-14T23:46:38.511339Z'
  support: refutes
  summary: Ahring and Westermann (1988) experimentally report inhibition of thermophilic
    syntrophic butyrate conversion by hydrogen; growth depends on removing hydrogen
    and acetate, not on hydrogen production lowering its own partial pressure.
- evidence_id: original
  kind: record_content
  reference: templates/community_causal_graph_research.md
  locator: Causal edges / causal link example at commit ec5e6468b74e874f5474c52d1825fa91a0b595b7
  accessed_at: '2026-10-14T23:46:38.511339Z'
  support: supports
  summary: The example attributes lower pH2 to hydrogen produced by syntrophic oxidation
    and then appends an unsupported generic acetogen/methanogen chain.
assessments:
- assessment_id: hydrogen-direction
  area: graph
  topic: Producer/consumer direction in a causal research example
  outcome: concern
  summary: The direction is reversed and can bias future graph research. Correct the
    example and distinguish it from target-community evidence.
  target_ids:
  - causal-template
  evidence_ids:
  - primary
  - original
findings:
- finding_id: hydrogen-direction
  issue_key: communitymech-2007-hydrogen-direction
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Shared prompt reverses hydrogen-mediated facilitation
  description: Hydrogen production does not itself lower hydrogen partial pressure;
    a consuming partner can enable thermodynamically constrained oxidation. The generic
    chain is not evidence for the queried community.
  target_ids:
  - causal-template
  field_paths:
  - Causal edges / causal link example
  evidence_ids:
  - primary
  - original
  rule_id: causal-research-direction
  native_severity: P2
  normalization_reason: A systematic scientific-direction error in a prompt shared
    by graph-extension research.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: templates/community_causal_graph_research.md
    role: maintained research prompt
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2007
actions:
- action_id: correct-example
  description: Correct consumption/production direction and bound illustration versus
    target evidence.
  finding_ids:
  - hydrogen-direction
  target_ids:
  - causal-template
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: templates/community_causal_graph_research.md
    role: maintained research prompt
  acceptance_checks:
  - Render-path regressions reject the old example and retain target context.
  - Illustrative example is not used as source evidence for another community.
limitations:
- Historical source review at the stated commit, not an assessment of the already
  edited working tree.
- Primary abstract inspected; no quantitative thermodynamic model or whole-record
  completeness score is asserted.
- New regression tests and current Phormidium source research are assessed separately
  in the successor.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2007
tags:
- batch131
- causal-graphs
- self-review
```
