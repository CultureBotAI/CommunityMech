# Pending phage graphs: pre-repair scientific review

- Review: 20261014T215456Z-phage-graphs-before
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-14T21:54:56.164161Z
- Finished UTC: 2026-10-14T21:54:56.164161Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Both pending graph records were read completely and their graph claims compared with primary passages. Three confirmed Alseth findings require repair. PHA's five bounded nodes and zero arrows have no additional confirmed defect in this graph scope. This is a pre-repair observation, not release approval.

## Scope And Provenance

Ten graph nodes and three arrows across the two inventory-pending records; related discussions and record description for consistency.

Selection: All two records pending in the freshly rebuilt full-corpus inventory.
Coverage: partial; 2 reviewed / 462 in the declared population.
Source: working_tree at Git base b68d71e702200cd7ce9afdec001705dc8b0890fd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000467 | kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml | maintained | Alseth four-species phage community |
| CommunityMech:000468 | kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml | maintained | PHA mixed-culture phage succession community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Fresh full-corpus inventory | passed | True | CommunityMech:000467, CommunityMech:000468 | Actual inventory command completed with exit0; structural health does not establish causal support. |
| Post-repair record gates | skipped | True | CommunityMech:000467, CommunityMech:000468 | Not yet run: this pre-repair review records findings before curation and cannot claim release validation. |

## Scientific And Domain Assessments

### Measured treatment effects versus mechanism and model claims

graph: concern. Targets: CommunityMech:000467.

Retain observed pairwise infection, competitive release, resistance evolution and diversity outcomes. Narrow the two mediation arrows and the model-inferred context dependence; correct optional type misuse without inventing new topology.

### Observed turnover and explicitly modeled/predicted process context

graph: supported. Targets: CommunityMech:000468.

Retain the kill-the-winner hypothesis as partial, coupled turnover as association, SEM diversity/activity effects as modeled associations, AMG transcripts without a yield claim, and defense predictions without functional resistance claims. These qualified context nodes do not supply causal arrows; the graph remains arrow-free.

## Findings

### typing: Outcome and model nodes carry unsupported mechanistic types

major / open / confirmed; issue key: communitymech-2005-typing.

The diversity outcome is not another lytic infection; resistance-route observations and fitted-model failure do not establish reciprocal negative effects. Keep measured infection and competitive release, and omit inappropriate optional types.

### mediation: Two arrows exceed their measured causal support

major / open / confirmed; issue key: communitymech-2005-mediation.

Receptor targeting is stated to cause the resistance route's fitness cost, and competitive release is stated to be the established diversity-maintaining mechanism. The source supports a partial cost explanation and joint treatment outcomes, not isolated necessary or sufficient mediation.

### model-scope: Model failure and improved prediction are overgeneralized

major / open / confirmed; issue key: communitymech-2005-model-scope.

The record omits the phage-free condition on improved quantitative four-species prediction and turns failure of tested pairwise-fitted models into general non-reconstructibility. Retain the published computational observation without treating it as proof of one higher-order mechanism or an impossibility theorem.

## Recommended Actions And Acceptance Checks

### repair-alseth

Correct existing Alseth graph types, mediation wording and modeling context through the guarded writer; preserve raw unrelated blocks and add history and regression tests.

- All three findings have source-backed scoped corrections and regression controls.
- Five nodes and three existing directions remain with explicit mediation limits and no new topology.
- Exact quotations, schema, strict, terms, histories, generated docs and full-corpus graph checks pass with limitations recorded.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| alseth | PMID:38648198; Publisher Results: phage effects, resistance, competitive release and diversity; Figures 3-5 and 8-10 captions; modeling Results and Discussion | partial | Phage treatment altered dominance and diversity. The resistance-cost explanation is partial. Adding three-species data improved phage-free quantitative prediction; phage-present models retained quantitative failure despite qualitative release prediction. Caption text, not figure pixels, was inspected. |
| pha | PMID:40152616; Publisher Abstract; Results and Discussion: community overview, SEM/turnover, predicted host links/defenses and AMG expression; cached computational Methods | supports | The observational time series supports correlated turnover and modeled associations. Sequence-derived host links/defenses and AMG transcripts remain qualified predictions or observations, not experimentally established lysis, resistance or yield effects. |
| schema | src/communitymech/schema/communitymech.yaml; InteractionTypeEnum and EcologicalInteraction | supports | LYTIC_INFECTION requires virus-to-host infection; COMPETITION asserts reciprocal negative effects. The optional type need not be filled when neither applies. Community-level phenomena and explicitly bounded computational evidence can be represented without such a type. |
| records | research/causal-batch130/targets.yaml; Both complete canonical YAML records | supports | Each record has five nodes. Alseth has three arrows and the identified type/mediation/model-scope overstatements; PHA has zero arrows and preserves the earlier modality and cultivation-context repair. |
| baseline | reports/causal_graph_review/20261014-batch130/baseline-inventory.json | supports | Fresh ignored-inclusive inventory: 462 records, 1383 nodes, 533 arrows; 406 reviewed, 54 needs_research, two pending; no structural defects. Network CLI exit1 is 57 warnings, not zero-warning success. |

## Limits And Additional Notes

- This is a causal-graph review, not whole-record completeness or validation-quality scoring; those separate whole-record metrics are not computed here.
- Publisher passages and captions were inspected, not figure pixels, raw data, all supplementary materials or executable models.
- PMC access later returned a browser challenge; accessible publisher copies were used, without bypassing the challenge. Local article caches remain unchanged.
- The 54 existing needs_research records remain unresolved; this batch does not complete the corpus goal.
- No new topology, paid provider call, experimental protocol or biological optimization instruction is introduced.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261014T215456Z-phage-graphs-before
kind: batch
repository: CultureBotAI/CommunityMech
title: 'Pending phage graphs: pre-repair scientific review'
started_at: '2026-10-14T21:54:56.164161Z'
finished_at: '2026-10-14T21:54:56.164161Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The same agent is assessing and will implement repairs; this
    is not independent approval.
skill: communitymech-causal-graphs
completion: partial
verdict: needs_curation
scientific_review: true
summary: Both pending graph records were read completely and their graph claims compared
  with primary passages. Three confirmed Alseth findings require repair. PHA's five
  bounded nodes and zero arrows have no additional confirmed defect in this graph
  scope. This is a pre-repair observation, not release approval.
source:
  git_revision: b68d71e702200cd7ce9afdec001705dc8b0890fd
  state: working_tree
  inputs:
  - path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    sha256: 8980255bd37deba9af78f32382d4035cd32ce9de32c7c08472cce54f21750b80
    role: target
  - path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
    sha256: aebd6497b6d5a6f49e9e9ef956d4ec0847960acc0fd2413dce5e0960ed748488
    role: target
  - path: references_cache/PMID_38648198.txt
    sha256: babc54ddb60c3ed882e817d1970ff9c7ba24069b0b06d67730e12eb974b58df3
    role: context
  - path: references_cache/PMID_40152616.txt
    sha256: 65e30e4f8aed4b1c7cde1fb173376207bbf90d92306c7f59997fd41bfeddbe8b
    role: context
  - path: reports/causal_graph_review/20261014-batch130/baseline-inventory.json
    sha256: 8473701ff2c1eeff60c3133290cb5af80ea53d1b3e74866cca531d2e2a8b3034
    role: context
  - path: reports/causal_graph_review/20261014-batch130/baseline-network.json
    sha256: bf6a0d75f159686d9116c33ce7b45c565c527f494994e936889f200d052d401d
    role: context
  - path: reports/causal_graph_review/build_inventory.py
    sha256: 5cb9aeb35b34b67077dddf434715d1ee9314f71130f9e165f5c41967180a9483
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_phage_review_regressions.py
    sha256: 6b682e06de18099caa5142ed266b8c3c250ff8437c9caf2b2221225cbd80a9d6
    role: context
targets:
- target_id: CommunityMech:000467
  path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  label: Alseth four-species phage community
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    role: canonical_record
- target_id: CommunityMech:000468
  path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
  label: PHA mixed-culture phage succession community
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
    role: canonical_record
scope:
  description: Ten graph nodes and three arrows across the two inventory-pending records;
    related discussions and record description for consistency.
  selection: All two records pending in the freshly rebuilt full-corpus inventory.
  coverage: partial
  population_size: 462
  reviewed_target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  exclusions:
  - target: Other 460 corpus records
    reason: Structural census only, not a new semantic review.
  - target: Non-graph assertions, raw data, model code, supplements and figure pixels
    reason: Read for context where available, not globally recertified or independently
      reanalyzed.
checks:
- check_id: inventory
  name: Fresh full-corpus inventory
  status: passed
  required: true
  summary: Actual inventory command completed with exit0; structural health does not
    establish causal support.
  command: .venv/bin/python reports/causal_graph_review/build_inventory.py
  exit_code: 0
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
  evidence_ids:
  - baseline
- check_id: record-gates
  name: Post-repair record gates
  status: skipped
  required: true
  summary: 'Not yet run: this pre-repair review records findings before curation and
    cannot claim release validation.'
  target_ids:
  - CommunityMech:000467
  - CommunityMech:000468
evidence:
- evidence_id: alseth
  kind: primary_source
  reference: PMID:38648198
  locator: 'Publisher Results: phage effects, resistance, competitive release and
    diversity; Figures 3-5 and 8-10 captions; modeling Results and Discussion'
  accessed_at: '2026-10-14T21:54:56.164161Z'
  support: partial
  summary: Phage treatment altered dominance and diversity. The resistance-cost explanation
    is partial. Adding three-species data improved phage-free quantitative prediction;
    phage-present models retained quantitative failure despite qualitative release
    prediction. Caption text, not figure pixels, was inspected.
- evidence_id: pha
  kind: primary_source
  reference: PMID:40152616
  locator: 'Publisher Abstract; Results and Discussion: community overview, SEM/turnover,
    predicted host links/defenses and AMG expression; cached computational Methods'
  accessed_at: '2026-10-14T21:54:56.164161Z'
  support: supports
  summary: The observational time series supports correlated turnover and modeled
    associations. Sequence-derived host links/defenses and AMG transcripts remain
    qualified predictions or observations, not experimentally established lysis, resistance
    or yield effects.
- evidence_id: schema
  kind: record_content
  reference: src/communitymech/schema/communitymech.yaml
  locator: InteractionTypeEnum and EcologicalInteraction
  accessed_at: '2026-10-14T21:54:56.164161Z'
  support: supports
  summary: LYTIC_INFECTION requires virus-to-host infection; COMPETITION asserts reciprocal
    negative effects. The optional type need not be filled when neither applies. Community-level
    phenomena and explicitly bounded computational evidence can be represented without
    such a type.
- evidence_id: records
  kind: record_content
  reference: research/causal-batch130/targets.yaml
  locator: Both complete canonical YAML records
  accessed_at: '2026-10-14T21:54:56.164161Z'
  support: supports
  summary: Each record has five nodes. Alseth has three arrows and the identified
    type/mediation/model-scope overstatements; PHA has zero arrows and preserves the
    earlier modality and cultivation-context repair.
- evidence_id: baseline
  kind: validation
  reference: reports/causal_graph_review/20261014-batch130/baseline-inventory.json
  accessed_at: '2026-10-14T21:54:56.164161Z'
  support: supports
  summary: 'Fresh ignored-inclusive inventory: 462 records, 1383 nodes, 533 arrows;
    406 reviewed, 54 needs_research, two pending; no structural defects. Network CLI
    exit1 is 57 warnings, not zero-warning success.'
assessments:
- assessment_id: alseth-graph
  area: graph
  topic: Measured treatment effects versus mechanism and model claims
  outcome: concern
  summary: Retain observed pairwise infection, competitive release, resistance evolution
    and diversity outcomes. Narrow the two mediation arrows and the model-inferred
    context dependence; correct optional type misuse without inventing new topology.
  target_ids:
  - CommunityMech:000467
  evidence_ids:
  - alseth
  - schema
  - records
- assessment_id: pha-graph
  area: graph
  topic: Observed turnover and explicitly modeled/predicted process context
  outcome: supported
  summary: Retain the kill-the-winner hypothesis as partial, coupled turnover as association,
    SEM diversity/activity effects as modeled associations, AMG transcripts without
    a yield claim, and defense predictions without functional resistance claims. These
    qualified context nodes do not supply causal arrows; the graph remains arrow-free.
  target_ids:
  - CommunityMech:000468
  evidence_ids:
  - pha
  - records
findings:
- finding_id: typing
  issue_key: communitymech-2005-typing
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Outcome and model nodes carry unsupported mechanistic types
  description: The diversity outcome is not another lytic infection; resistance-route
    observations and fitted-model failure do not establish reciprocal negative effects.
    Keep measured infection and competitive release, and omit inappropriate optional
    types.
  target_ids:
  - CommunityMech:000467
  field_paths:
  - ecological_interactions[2].interaction_type
  - ecological_interactions[3].interaction_type
  - ecological_interactions[4].interaction_type
  evidence_ids:
  - alseth
  - schema
  - records
  rule_id: graph-interaction-type-scope
  native_severity: P2
  normalization_reason: Material causal or mechanistic scope inflation in a graph
    consumed as structured scientific claims.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    role: canonical_record
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2005
- finding_id: mediation
  issue_key: communitymech-2005-mediation
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Two arrows exceed their measured causal support
  description: Receptor targeting is stated to cause the resistance route's fitness
    cost, and competitive release is stated to be the established diversity-maintaining
    mechanism. The source supports a partial cost explanation and joint treatment
    outcomes, not isolated necessary or sufficient mediation.
  target_ids:
  - CommunityMech:000467
  field_paths:
  - ecological_interactions[0].downstream[1].description
  - ecological_interactions[1].downstream[0].description
  evidence_ids:
  - alseth
  - schema
  - records
  rule_id: graph-causal-mediation
  native_severity: P2
  normalization_reason: Material causal or mechanistic scope inflation in a graph
    consumed as structured scientific claims.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    role: canonical_record
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2005
- finding_id: model-scope
  issue_key: communitymech-2005-model-scope
  category: graph
  severity: major
  status: open
  certainty: confirmed
  title: Model failure and improved prediction are overgeneralized
  description: The record omits the phage-free condition on improved quantitative
    four-species prediction and turns failure of tested pairwise-fitted models into
    general non-reconstructibility. Retain the published computational observation
    without treating it as proof of one higher-order mechanism or an impossibility
    theorem.
  target_ids:
  - CommunityMech:000467
  field_paths:
  - description
  - ecological_interactions[4]
  evidence_ids:
  - alseth
  - schema
  - records
  rule_id: graph-model-context-boundary
  native_severity: P2
  normalization_reason: Material causal or mechanistic scope inflation in a graph
    consumed as structured scientific claims.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    role: canonical_record
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2005
actions:
- action_id: repair-alseth
  description: Correct existing Alseth graph types, mediation wording and modeling
    context through the guarded writer; preserve raw unrelated blocks and add history
    and regression tests.
  finding_ids:
  - typing
  - mediation
  - model-scope
  target_ids:
  - CommunityMech:000467
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    role: canonical_record
  acceptance_checks:
  - All three findings have source-backed scoped corrections and regression controls.
  - Five nodes and three existing directions remain with explicit mediation limits
    and no new topology.
  - Exact quotations, schema, strict, terms, histories, generated docs and full-corpus
    graph checks pass with limitations recorded.
limitations:
- This is a causal-graph review, not whole-record completeness or validation-quality
  scoring; those separate whole-record metrics are not computed here.
- Publisher passages and captions were inspected, not figure pixels, raw data, all
  supplementary materials or executable models.
- PMC access later returned a browser challenge; accessible publisher copies were
  used, without bypassing the challenge. Local article caches remain unchanged.
- The 54 existing needs_research records remain unresolved; this batch does not complete
  the corpus goal.
- No new topology, paid provider call, experimental protocol or biological optimization
  instruction is introduced.
links:
- https://github.com/CultureBotAI/CommunityMech/issues/2005
tags:
- causal-graphs
- batch130
- self-review
```
