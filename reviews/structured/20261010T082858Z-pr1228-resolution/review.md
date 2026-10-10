# PR 1228: source-bound correction and regression review

- Review: 20261010T082858Z-pr1228-resolution
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-10T08:28:58Z
- Finished UTC: 2026-10-10T08:28:58Z
- Reviewer: codex (self_review)
- Completion: partial
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Three confirmed findings corrected and regression-tested after integrating main 01013cc. No remaining confirmed defect in this bounded review; full protected CI and ontology-dependent gates remain pending.

## Scope And Provenance

Post-fix adversarial review of integrated main and the two added phage communities.

Selection: Maintained implementation, generated-artifact provenance, and source-backed record assertions implicated by the PR.
Coverage: partial; 5 reviewed / 20 in the declared population.
Source: git_commit at Git base 10a01cdcb798917688095067242a4b390a203726.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| pha | kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml | maintained | pha |
| alseth | kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml | maintained | alseth |
| schema | src/communitymech/schema/communitymech.yaml | maintained | schema |
| guide | docs/PHAGE_BACTERIA_GUIDE.md | maintained | guide |
| corpus-tests | tests/test_network_palette.py | maintained | corpus-tests |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Source and context corrections | passed | True | pha, alseth, schema, guide | Predictions and modeled associations retain modality and uncertainty; unsupported arrows and lytic typing removed; assay oxygen control separated; definition corrected. |
| Focused integrated regression and validation | passed | True | pha, alseth, schema, guide, corpus-tests | Focused tests and source-bound mutation controls pass; baselines retain current-main fixes and explicitly account for nine added unresolved bacterial members. |
| Complete protected CI and ontology validation | unavailable | True | pha, alseth, schema, corpus-tests | Not yet run on the pushed final head. This review does not substitute for required head and merge-group checks. |

## Scientific And Domain Assessments

### Evidence modality and experimental scope

evidence: supported. Targets: pha.

PHA observations now preserve computational provenance, hypothesis status, and vessel-specific cultivation context.

### Distinct engineered phage perturbation community

scope: supported. Targets: alseth.

Alseth remains unchanged; inspected source and scoped validation support its competitive-release experiment, without certifying all taxonomy assertions.

### New vocabulary and integration

consistency: supported. Targets: schema, guide, corpus-tests.

Definition, guide, generated model, and corpus baselines are integrated with current main and protected by focused regressions.

## Findings

### pr1228-evidence-modality: Do not encode genomic predictions as demonstrated lytic infection

major / resolved / confirmed; issue key: pr1228-evidence-modality.

PHA ecological_interactions[4] asserts LYTIC_INFECTION with SUPPORT/IN_VITRO from a DefenseFinder survey of encoded defense systems, which does not demonstrate infection, replication, or host lysis. Interaction[3] similarly uses this type for AMG identification/transcription. Interaction[0] drops the SEM qualifier from its first supporting snippet and represents a modeled succession mechanism as SUPPORT/IN_VITRO. Preserve computational provenance and uncertainty, and represent the actual observation instead of using an infection relation as a catch-all phage category.

Disposition: Issue #1985: Removed infection typing from associations, AMG transcription and predicted defences; restored SEM qualifier and PARTIAL computational evidence; removed unsupported causal chain and uniform lytic role. Regression mutations reject reintroductions.

### pr1228-assay-context: Keep the fed-batch assay oxygen setting out of the 2 L cultivation setup

major / resolved / confirmed; issue key: pr1228-assay-context.

cultivation_setup[0] describes the five 2 L sequencing batch enrichment reactors but sets do_controlled=true using oxygen control from separate 400 mL fed-batch PHA-accumulation assays. controls_notes acknowledges the assay, but structured consumers still receive the setting on the wrong setup. Split the assay into a separately evidenced setup or omit the unsupported enrichment control flag.

Disposition: Issue #1986: Removed enrichment do_controlled/controls_notes and misplaced media preparation detail; retained the separate 400 mL assay context in notes. Regression rejects reattached oxygen flags.

### pr1228-density-distinction: Do not define lytic infection by unique prey-density dependence

major / resolved / confirmed; issue key: pr1228-density-distinction.

The original schema and guide incorrectly distinguish phages from grazers by population dependence on host/prey density. Use intracellular viral replication and host lysis instead.

Disposition: Issue #1989: Schema and guide now distinguish intracellular replication and lysis from grazing without claiming unique density dependence. Model regenerated and regression passed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| pha-source | https://journals.asm.org/doi/10.1128/msystems.00200-25; Results: phage-host interactions and AMGs; Methods: PHA-MMC enrichment/accumulation, bacterial MAG analyses, APC identification, statistical analysis. | supports | The publisher full text and committed PMID_40152616 cache distinguish DefenseFinder genome predictions, transcript measurements, SEM inference, 2 L enrichments, and separate 400 mL accumulation assays. |
| enum-contract | src/communitymech/schema/communitymech.yaml; InteractionTypeEnum.LYTIC_INFECTION and ComputationalPredictionTypeEnum | supports | The new infection relation asserts viral infection, replication, and lysis; it is not a generic label for any viral-associated genomic or ecological observation. The guide also requires modeled-direction provenance. |
| alseth-source | https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002346; Abstract and experimental design; committed PMID_38648198 full-text cache | supports | The primary experiment supports phage-mediated competitive release and separates wild-type/CRISPR-KO treatments and failed pairwise gLV predictions. No additional confirmed defect was found in the scoped Alseth inspection. |
| density-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2211389/ | supports | Primary experimental/model study includes prey-density-dependent protozoan feeding and growth; density dependence is not unique to phage populations. |
| replication-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC4425896/ | supports | Primary study distinguishes protist consumption before reproduction from multiple phage progeny produced through infection of a host bacterium. |
| fix-validation | tests/test_phage_review_regressions.py | supports | 225 focused tests passed and one mapping-dependent test skipped; the single failed assertion was corrected and rerun successfully. Final phage/palette rerun: 37 passed, including 12 phage tests. Strict two-record validation has zero error rows (NCBITaxon-backed checks unavailable); both network audits have no findings; 48 evidence snippets match primary caches; history validates. Generated pages reproduce without unstaged differences. |

## Limits And Additional Notes

- Self-review, not an independent human or agent approval.
- Bounded PR review, not full native record completeness scoring or all-assertion certification.
- Full suite, ontology-backed checks, and exact-head/merge-group CI remain pending; unavailable local checks are not counted as passes.
- Original raw reference caches retain pre-existing trailing whitespace; curated and generated fix files pass whitespace checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261010T082858Z-pr1228-resolution
kind: repository
repository: CultureBotAI/CommunityMech
title: 'PR 1228: source-bound correction and regression review'
started_at: '2026-10-10T08:28:58Z'
finished_at: '2026-10-10T08:28:58Z'
reviewer:
  identity: codex
  kind: agent
  independence: self_review
  independence_basis: The same Codex agent implemented and reviewed these corrections;
    this is not independent approval.
skill: pr-adversarial-review
completion: partial
verdict: pass_with_limitations
scientific_review: true
summary: Three confirmed findings corrected and regression-tested after integrating
  main 01013cc. No remaining confirmed defect in this bounded review; full protected
  CI and ontology-dependent gates remain pending.
source:
  git_revision: 10a01cdcb798917688095067242a4b390a203726
  state: git_commit
  inputs:
  - path: docs/PHAGE_BACTERIA_GUIDE.md
    sha256: 600e3de67a49561bc0f2523693f54dbe631a20e44f4bec38fc99996924248c6c
    role: target
  - path: history/records/PHA_MixedCulture_Phage_Succession_Community/2026-10-10T081819Z-codex-dc7bf2.yaml
    sha256: c4236bb26da8384e667efb5f30ad9b075308db907fb62bba1b403abe7754622c
    role: context
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
  - path: src/communitymech/datamodel/communitymech.py
    sha256: f0dc1a20274d484aff93ffbe3871cbe98daa93fe8cc1574742fd7489cf987eca
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: target
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_gtdb_coherence_validator.py
    sha256: e3d274e76837dbf08bfd2c916167eb3f30a005ed571824caa26236eb7019dcfc
    role: context
  - path: tests/test_network_palette.py
    sha256: 6403f353a5cc1f5291c5b983789758b9146549a44cb16c5e7082b2d64d9d26da
    role: target
  - path: tests/test_participating_taxa.py
    sha256: 9d4c2a5c3924e87fbb44e71187e9ae092e8f935912cbf093a09f49511e788810
    role: context
  - path: tests/test_phage_review_regressions.py
    sha256: d6a765b147166b58278d97a90521de4df2fc6988fb84be155eacae35d881ad69
    role: context
targets:
- target_id: pha
  path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
  kind: maintained
  label: pha
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
    role: maintained source owner
- target_id: alseth
  path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  kind: maintained
  label: alseth
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    role: maintained source owner
- target_id: schema
  path: src/communitymech/schema/communitymech.yaml
  kind: maintained
  label: schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/schema/communitymech.yaml
    role: maintained source owner
- target_id: guide
  path: docs/PHAGE_BACTERIA_GUIDE.md
  kind: maintained
  label: guide
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: docs/PHAGE_BACTERIA_GUIDE.md
    role: maintained source owner
- target_id: corpus-tests
  path: tests/test_network_palette.py
  kind: maintained
  label: corpus-tests
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: tests/test_network_palette.py
    role: maintained source owner
scope:
  description: Post-fix adversarial review of integrated main and the two added phage
    communities.
  selection: Maintained implementation, generated-artifact provenance, and source-backed
    record assertions implicated by the PR.
  coverage: partial
  population_size: 20
  reviewed_target_ids:
  - pha
  - alseth
  - schema
  - guide
  - corpus-tests
checks:
- check_id: source-fixes
  name: Source and context corrections
  status: passed
  required: true
  target_ids:
  - pha
  - alseth
  - schema
  - guide
  evidence_ids:
  - pha-source
  - alseth-source
  - fix-validation
  - density-primary
  summary: Predictions and modeled associations retain modality and uncertainty; unsupported
    arrows and lytic typing removed; assay oxygen control separated; definition corrected.
- check_id: regressions
  name: Focused integrated regression and validation
  status: passed
  required: true
  target_ids:
  - pha
  - alseth
  - schema
  - guide
  - corpus-tests
  evidence_ids:
  - fix-validation
  summary: Focused tests and source-bound mutation controls pass; baselines retain
    current-main fixes and explicitly account for nine added unresolved bacterial
    members.
- check_id: complete-ci
  name: Complete protected CI and ontology validation
  status: unavailable
  required: true
  target_ids:
  - pha
  - alseth
  - schema
  - corpus-tests
  evidence_ids: []
  summary: Not yet run on the pushed final head. This review does not substitute for
    required head and merge-group checks.
evidence:
- evidence_id: pha-source
  kind: primary_source
  reference: https://journals.asm.org/doi/10.1128/msystems.00200-25
  support: supports
  locator: 'Results: phage-host interactions and AMGs; Methods: PHA-MMC enrichment/accumulation,
    bacterial MAG analyses, APC identification, statistical analysis.'
  summary: The publisher full text and committed PMID_40152616 cache distinguish DefenseFinder
    genome predictions, transcript measurements, SEM inference, 2 L enrichments, and
    separate 400 mL accumulation assays.
  accessed_at: '2026-10-10T07:43:46Z'
- evidence_id: enum-contract
  kind: record_content
  reference: src/communitymech/schema/communitymech.yaml
  support: supports
  locator: InteractionTypeEnum.LYTIC_INFECTION and ComputationalPredictionTypeEnum
  summary: The new infection relation asserts viral infection, replication, and lysis;
    it is not a generic label for any viral-associated genomic or ecological observation.
    The guide also requires modeled-direction provenance.
  accessed_at: '2026-10-10T07:43:46Z'
- evidence_id: alseth-source
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3002346
  support: supports
  locator: Abstract and experimental design; committed PMID_38648198 full-text cache
  summary: The primary experiment supports phage-mediated competitive release and
    separates wild-type/CRISPR-KO treatments and failed pairwise gLV predictions.
    No additional confirmed defect was found in the scoped Alseth inspection.
  accessed_at: '2026-10-10T07:43:46Z'
- evidence_id: density-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2211389/
  support: supports
  accessed_at: '2026-10-10T08:28:22Z'
  summary: Primary experimental/model study includes prey-density-dependent protozoan
    feeding and growth; density dependence is not unique to phage populations.
- evidence_id: replication-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4425896/
  support: supports
  accessed_at: '2026-10-10T08:28:22Z'
  summary: Primary study distinguishes protist consumption before reproduction from
    multiple phage progeny produced through infection of a host bacterium.
- evidence_id: fix-validation
  kind: validation
  support: supports
  reference: tests/test_phage_review_regressions.py
  accessed_at: '2026-10-10T08:28:58Z'
  summary: '225 focused tests passed and one mapping-dependent test skipped; the single
    failed assertion was corrected and rerun successfully. Final phage/palette rerun:
    37 passed, including 12 phage tests. Strict two-record validation has zero error
    rows (NCBITaxon-backed checks unavailable); both network audits have no findings;
    48 evidence snippets match primary caches; history validates. Generated pages
    reproduce without unstaged differences.'
assessments:
- assessment_id: pha-evidence
  area: evidence
  topic: Evidence modality and experimental scope
  outcome: supported
  target_ids:
  - pha
  evidence_ids:
  - pha-source
  - enum-contract
  - fix-validation
  summary: PHA observations now preserve computational provenance, hypothesis status,
    and vessel-specific cultivation context.
- assessment_id: alseth-scope
  area: scope
  topic: Distinct engineered phage perturbation community
  outcome: supported
  target_ids:
  - alseth
  evidence_ids:
  - alseth-source
  - fix-validation
  summary: Alseth remains unchanged; inspected source and scoped validation support
    its competitive-release experiment, without certifying all taxonomy assertions.
- assessment_id: schema-guide-tests
  area: consistency
  topic: New vocabulary and integration
  outcome: supported
  target_ids:
  - schema
  - guide
  - corpus-tests
  evidence_ids:
  - enum-contract
  - fix-validation
  summary: Definition, guide, generated model, and corpus baselines are integrated
    with current main and protected by focused regressions.
findings:
- finding_id: pr1228-evidence-modality
  issue_key: pr1228-evidence-modality
  title: Do not encode genomic predictions as demonstrated lytic infection
  description: PHA ecological_interactions[4] asserts LYTIC_INFECTION with SUPPORT/IN_VITRO
    from a DefenseFinder survey of encoded defense systems, which does not demonstrate
    infection, replication, or host lysis. Interaction[3] similarly uses this type
    for AMG identification/transcription. Interaction[0] drops the SEM qualifier from
    its first supporting snippet and represents a modeled succession mechanism as
    SUPPORT/IN_VITRO. Preserve computational provenance and uncertainty, and represent
    the actual observation instead of using an infection relation as a catch-all phage
    category.
  category: consistency
  severity: major
  status: resolved
  certainty: confirmed
  target_ids:
  - pha
  field_paths:
  - ecological_interactions[4].interaction_type (line 326)
  - ecological_interactions[4].evidence[0] (lines 329-334)
  - ecological_interactions[3].interaction_type (line 292)
  - ecological_interactions[0].evidence[0] (lines 207-216)
  evidence_ids:
  - pha-source
  - enum-contract
  - fix-validation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
    role: maintained source owner
  native_severity: P2
  normalization_reason: Misrepresents structured evidence or permits a post-merge
    publication failure.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261010T074445Z-pr1228-final
    finding_id: pr1228-evidence-modality
  disposition_reason: 'Issue #1985: Removed infection typing from associations, AMG
    transcription and predicted defences; restored SEM qualifier and PARTIAL computational
    evidence; removed unsupported causal chain and uniform lytic role. Regression
    mutations reject reintroductions.'
- finding_id: pr1228-assay-context
  issue_key: pr1228-assay-context
  title: Keep the fed-batch assay oxygen setting out of the 2 L cultivation setup
  description: cultivation_setup[0] describes the five 2 L sequencing batch enrichment
    reactors but sets do_controlled=true using oxygen control from separate 400 mL
    fed-batch PHA-accumulation assays. controls_notes acknowledges the assay, but
    structured consumers still receive the setting on the wrong setup. Split the assay
    into a separately evidenced setup or omit the unsupported enrichment control flag.
  category: consistency
  severity: major
  status: resolved
  certainty: confirmed
  target_ids:
  - pha
  field_paths:
  - cultivation_setup[0].do_controlled (line 420)
  - cultivation_setup[0].controls_notes (lines 421-423)
  evidence_ids:
  - pha-source
  - fix-validation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/PHA_MixedCulture_Phage_Succession_Community.yaml
    role: maintained source owner
  native_severity: P2
  normalization_reason: Misrepresents structured evidence or permits a post-merge
    publication failure.
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261010T074445Z-pr1228-final
    finding_id: pr1228-assay-context
  disposition_reason: 'Issue #1986: Removed enrichment do_controlled/controls_notes
    and misplaced media preparation detail; retained the separate 400 mL assay context
    in notes. Regression rejects reattached oxygen flags.'
- finding_id: pr1228-density-distinction
  issue_key: pr1228-density-distinction
  title: Do not define lytic infection by unique prey-density dependence
  description: The original schema and guide incorrectly distinguish phages from grazers
    by population dependence on host/prey density. Use intracellular viral replication
    and host lysis instead.
  category: consistency
  severity: major
  status: resolved
  certainty: confirmed
  target_ids:
  - schema
  - guide
  evidence_ids:
  - density-primary
  - replication-primary
  - fix-validation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: src/communitymech/schema/communitymech.yaml
    role: maintained source owner
  - repository: CultureBotAI/CommunityMech
    path: docs/PHAGE_BACTERIA_GUIDE.md
    role: maintained source owner
  disposition_reason: 'Issue #1989: Schema and guide now distinguish intracellular
    replication and lysis from grazing without claiming unique density dependence.
    Model regenerated and regression passed.'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261010T082822Z-pr1228-vocabulary
    finding_id: pr1228-density-distinction
actions: []
limitations:
- Self-review, not an independent human or agent approval.
- Bounded PR review, not full native record completeness scoring or all-assertion
  certification.
- Full suite, ontology-backed checks, and exact-head/merge-group CI remain pending;
  unavailable local checks are not counted as passes.
- Original raw reference caches retain pre-existing trailing whitespace; curated and
  generated fix files pass whitespace checks.
links:
- https://github.com/CultureBotAI/CommunityMech/pull/1228
- https://github.com/CultureBotAI/CommunityMech/issues/1985
- https://github.com/CultureBotAI/CommunityMech/issues/1986
- https://github.com/CultureBotAI/CommunityMech/issues/1989
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261010T074445Z-pr1228-final
  relationship: Evidence-backed correction of previously open findings; earlier observation
    remains immutable.
- repository: CultureBotAI/CommunityMech
  review_id: 20261010T082822Z-pr1228-vocabulary
  relationship: Evidence-backed correction of previously open findings; earlier observation
    remains immutable.
```
