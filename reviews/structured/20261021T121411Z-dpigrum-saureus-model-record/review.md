# D. pigrum–S. aureus community model review

- Review: 20261021T121411Z-dpigrum-saureus-model-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T12:07:12.078382Z
- Finished UTC: 2026-10-21T12:14:11.699365Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The correct modeled pair and two qualified nodes are retained. One major finding addresses omitted growth-enabling nutrients; two minor findings address static endpoints/computational provenance and source-strain/resource organization.

## Scope And Provenance

Whole record, fresh primary main, declared critical figures/supplementary tables and direct model/code/strain authorities.

Selection: Only released CommunityMech:000010 after 000009 save and both mandatory gates.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000010 | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml | maintained | BioModels MODEL2209060002 D pigrum - S aureus Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000010 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000010 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000010 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000010 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000010 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000010 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000010 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000010 | Reference validation passed against pinned caches. |
| audit-network | failed | True | CommunityMech:000010 | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; target-native structure is COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000010 | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; target-native structure is COMPLETE. |
| Primary source and resource identity | passed | True | CommunityMech:000010 | Direct primary publication and focal model identities verified; input assembly-name discrepancy is preserved. |
| Whole-record scientific assessment | passed | True | CommunityMech:000010 | Complete main and declared critical figure/table/model scopes inspected; no simulation executed. |
| Medium and ingredient external links | not_applicable | False | CommunityMech:000010 | No CultureMech or MediaIngredientMech identifier is encoded; simulated media do not establish a unique physical recipe link. |
| Optional structured source adapter | unavailable | False | CommunityMech:000010 | No runnable applicable adapter was established in recorded discovery. |

## Scientific And Domain Assessments

### Pair, computational scope and source strains

identity: supported. Targets: CommunityMech:000010.

The correct two-species community model is linked; source strains and individual configurations should be made explicit.

### Species and conditional CROSS_FEEDER roles

grounding: supported. Targets: CommunityMech:000010.

Both recipient roles have computational support when restricted to the appropriate scenarios.

Sa→Dp amino-acid support is explicit in forced-growth/rescue scenarios; Dp→Sa ornithine exchange appears in selected supplementary shuttle tables. The author notebook closes Sa ornithine uptake in one setup, whereas other outputs/deposited settings allow it. Add local role evidence and scenario qualifiers; no unconditional reciprocal dependence or experimental transfer is established. No abundance field needs repair.

### ecological_interactions[0]: exchange-factor prediction

graph: supported. Targets: CommunityMech:000010.

Retain D. pigrum → S. aureus as a qualified pairwise computational prediction, not an inhibitory mechanism.

Figure 4 and its caption support D. pigrum cysteine uptake and D-serine release across tested media/objectives, while explicitly stating that S. aureus does not depend on these highlighted fluxes. The broad GO term is compatible with the stated modeled interaction. No antimicrobial synthesis or mediator arrow is warranted.

### ecological_interactions[1]: growth-inhibition hypothesis

graph: supported. Targets: CommunityMech:000010.

Retain D. pigrum → S. aureus as conditional modeled growth suppression.

The pooled 10:1 objective case gives zero Sa growth; other formulations retain growth and can require Sa→Dp nutritional support. The record correctly distinguishes objective weights from measured inoculation dynamics and competition indices from reciprocal negative fitness. Background association and proposed application remain PARTIAL, not direct clinical proof.

### Downstream causal scope

graph: supported. Targets: CommunityMech:000010.

There are no downstream arrows; preserve that restraint.

Assembly, constraints and medium construction are workflow steps. Neither cysteine/D-serine fluxes nor the static scenarios establish a measured causal chain to inhibition.

### Growth-enabling nutrients and model conditions

completeness: concern. Targets: CommunityMech:000010.

The SNM3 block omits additions necessary to interpret whether D. pigrum can grow.

Separate baseline non-growing Dp, supplemented growth, and the constrained Sa amino-acid rescue with manually supplied DAP. Keep COMPM/COOPM and exchange medium distinct. Absence of temperature/pH/vessel metadata is appropriate for this computational study; oxygen bounds are not physical headspace.

### Static endpoints and structured computational provenance

evidence: concern. Targets: CommunityMech:000010.

Generic abundance/persistence tracking is unsupported; modeled outputs and run conditions are recoverable.

Retain ENGINEERED as computational assembly. Replace generic design text with source formulations and predicted biomass/exchange outputs. Add computational provenance to model-claim evidence; bibliographic-only evidence does not need invented simulation settings.

### Model, publication, code and input strains

provenance: concern. Targets: CommunityMech:000010.

The correct current model file resolves, but publication and dataset roles are conflated and input provenance is incomplete.

Keep SA_DP_community.xml/MODEL2209060002. A primary publication is evidence rather than a separate scientific dataset. Link source code and verified input-strain metadata with version/access scope; preserve the printed ASM19771v1 versus archive ASM719771v1 discrepancy. No claim of complete model reproduction or raw genome inspection follows.

### Prior graph repairs and reference support

provenance: supported. Targets: CommunityMech:000010.

All 12 snippets are directly source-verifiable, and the two-node/no-arrow repair remains justified.

Open 1262 is current follow-up context; closed 1258 is a completed graph repair. Historical unavailable figure/SI scope is not a limitation of this fresh assessment.

### Native checks

schema: supported. Targets: CommunityMech:000010.

All eight native checks pass; semantic completeness findings remain.

### Mechanical metrics

completeness: supported. Targets: CommunityMech:000010.

Capped quality does not negate one major and two minor findings.

## Findings

### growth-enabling-nutrients: Represent growth-enabling nutrients and rescue scenarios

major / open / confirmed; issue key: cm-000010-growth-enabling-nutrients.

The current SNM3 description names only oxygen/iron exceptions and closes all other exchanges, omitting L-isoleucine, L-methionine and meso-2,6-diaminoheptanedioate required for Dp growth. These omissions change the modeled feasibility, not merely recipe detail.

### static-provenance: Replace generic tracking endpoints with model-specific provenance

minor / open / confirmed; issue key: cm-000010-static-provenance.

engineering_design claims abundance/persistence tracking although this is static constraint-based analysis. Computational provenance is recoverable but unstructured, and an oxygen uptake bound occupies physical headspace_gas.

### strain-resource-provenance: Clarify source strains and resource types

minor / open / confirmed; issue key: cm-000010-strain-resource-provenance.

Species-level identity is valid, but source reconstruction strains and local role evidence are missing, while the primary paper is listed as a dataset. Current model/code/strain authorities allow a bounded provenance improvement.

## Recommended Actions And Acceptance Checks

### repair-growth-enabling-nutrients

Represent growth-enabling nutrients and rescue scenarios.

- State baseline Dp does not grow on unaugmented SNM3 and identify the three growth-enabling additions with source evidence. Preserve model flux units rather than inventing bench concentrations.
- Separate supplemented growth from the Section 3.12 rescue: Sa supplies isoleucine/methionine under imposed constraints, while DAP is manually supplied because the model does not provide it through Sa exchange.
- Retain scenario-specific objective weights, survival constraints and exchange/COMPM/COOPM definitions. Do not apply notebook addition bounds or deposited FVA-derived defaults to every published run.
- Keep the medium explicitly computational and preserve the absence of reported physical incubation conditions.

### repair-static-provenance

Replace generic tracking endpoints with model-specific provenance.

- Replace tracking endpoints with predicted member/community biomass, exchange fluxes and scenario-dependent inhibition; describe integrated, compartmentalized and pooled constructions as applicable.
- Populate computational_provenance for actual model claims with FBA/FVA, toolchain, model/version, simulated medium and objective/constraint settings. Preserve source-reported software versions and avoid inventing unreported versions.
- Move the oxygen bound to model parameters; distinguish modeled nasal habitat from physical headspace. Retain ENGINEERED only with explicit computational assembly scope.
- Preserve both qualified nodes and zero arrows; do not restore exchange-to-inhibition mediation, physical population dynamics or clinical efficacy.

### repair-strain-resource-provenance

Clarify source strains and resource types.

- Record source_strain values 83VPs-KB5 and USA300 JE2 with source evidence, without claiming all biological strains of either species share the simulated response.
- Attach scenario-specific recipient evidence to CROSS_FEEDER: Dp amino-acid uptake and Sa ornithine uptake in selected model outputs. Preserve external ornithine supply and notebook closure as limits; do not claim obligate or universal reciprocal dependence.
- Keep the correct BioModels file and link immutable author code/input provenance. Move the primary publication to evidence or literature resources rather than counting it as a dataset.
- If input accessions are added, preserve CP020619.1 and the documented printed ASM19771v1 versus live exact-strain ASM719771v1 discrepancy; resolve with explicit provenance, not silent source correction. Do not label input assemblies as newly generated focal data.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; Whole record: two taxa, two computational nodes and no arrows | supports | The record identifies the correct pair/model and explicitly distinguishes in-silico constraints from bench culture, but lacks growth-enabling nutrient and scenario provenance. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=36605126&amp;retmode=xml; Article-level metadata and abstract where supplied | supports | PMID36605126, DOI and article title/abstract identify the focal study. |
| crossref | https://api.crossref.org/works/10.3389/fcimb.2022.925215; Article-level metadata and abstract where supplied | supports | DOI/title/authors verified as bibliographic metadata. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:36605126&amp;format=json&amp;resultType=core; Article-level metadata and abstract where supplied | supports | PMID36605126/PMC9810029 and direct full-text availability identify the source. |
| assembly | doi:10.3389/fcimb.2022.925215; Fresh XML s1 Introduction; s2 Methods; s3_3 artificial pairwise design | supports | The study combines D. pigrum 83VPs-KB5 and S. aureus USA300 JE2 reconstructions, using integrated, compartmentalized and pooled formulations. ENGINEERED is defensible when explicitly scoped to the artificial computational assembly. |
| medium | doi:10.3389/fcimb.2022.925215; Fresh XML s2_4; s3_1; s3_9 Tables 3–4; s3_12 Figures 10–11/Table 6 | supports | Baseline D. pigrum has no growth in SNM3. L-isoleucine, L-methionine and meso-2,6-diaminoheptanedioate enable growth. The later constrained rescue lets S. aureus supply the two amino acids while DAP is manually supplied. |
| exchange | doi:10.3389/fcimb.2022.925215; Fresh XML s3_6 and Figure 4 caption; Figure 4 pixels | partial | D. pigrum cysteine uptake and D-serine secretion vary with formulation and objective. The highlighted exchanges do not establish antimicrobial synthesis or mediate the S. aureus outcome. |
| inhibition | doi:10.3389/fcimb.2022.925215; Fresh XML s3_7; s3_9 Figure 7; s3_12 Figures 10–11 | partial | The pooled model at 10:1 weight favoring D. pigrum yields zero S. aureus growth. Other media/objectives allow S. aureus growth and conditional support of D. pigrum; the result is not clinical efficacy. |
| static-method | doi:10.3389/fcimb.2022.925215; Fresh XML s2_1–s2_6; s3_5–s3_8; s4 Discussion; s5 Data Availability | supports | FBA/FVA, objectives, weights, uptake bounds and solver choices describe static predictions. The paper explicitly distinguishes this work from dynamic behavior; generic abundance/persistence tracking is not a measured endpoint. |
| conditional-roles | doi:10.3389/fcimb.2022.925215; Fresh XML s3_2, s3_9 Table 4, s3_12 Table 6; Table_2.xlsx Summary_exchange_shuttels_SNM_1 row 10 and Summary_exchange_shuttels_Exch1 row 13 | partial | D. pigrum is a conditional amino-acid recipient. S. aureus can take up ornithine while D. pigrum secretes it in selected model scenarios; ornithine is also supplied externally, and this is not exclusive partner dependence. |
| supplement | doi:10.3389/fcimb.2022.925215; workbook-scope.json: declared Table 1, Table 2 and Table 3 scope | supports | Supplementary medium dictionaries and shuttle tables support scenario separation. Numeric strings were parsed for table inspection; no solver or statistical reanalysis was performed. |
| availability | doi:10.3389/fcimb.2022.925215; Fresh XML s1 Introduction and s5 Data Availability | supports | The exact BioModels community accession, author repository and software requirements are reported. CP020619.1 and the printed ASM19771v1 identify input-reconstruction provenance, not new experimental datasets. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity; FunctionalRoleEnum; EngineeringDesign; GrowthMedia.headspace_gas; ComputationalProvenance | supports | Recipient roles need scenario-specific evidence; headspace describes physical gas, while computational provenance provides model, method, toolchain, medium and parameter fields. |
| ontology | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; ontology-authority.json | supports | All four unique pairs/nine occurrences match. Species grounding and broad interaction GO terms are valid; no replacement is required. |
| model-boundary | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; root-model-boundary.json | supports | The focal deposit is a two-species community with seven compartments and two equally weighted biomass objectives. Its current open nutrient exchanges are one configuration, not all published run settings. |
| resources | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; dataset-verification.json | supports | BioModels file identity, immutable author code/input and bounded CP020619.1/exact-strain assembly metadata are verified. Notebook nutrient additions and ornithine closure are preserved as configuration-specific. |
| snippets | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; snippet-audit.json | supports | All 12 snippets match directly retrieved full XML and the pinned cache; lexical support does not establish every attached scope claim. |
| history | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; provenance-audit.json | supports | Closed 1258 preserves the prior graph repair; open 1262 specifically tracks missing nutrient handling and generic endpoints. |
| native-target | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; support-audit.json | supports | Native completeness and quality are mechanical measures, separate from the one major and two minor findings. |
| source-scope | doi:10.3389/fcimb.2022.925215; source-audit.json | supports | Whole main and declared critical figure/table/model scopes were inspected. |
| independent-source | doi:10.3389/fcimb.2022.925215; root-independent-source-audit.json | context_only | Independent whole-record and primary/supplementary source assessment corroborates the bounded findings. |
| search | Owned maintained roots; local-search.json: ignored-inclusive bounded discovery | supports | Local identity/reuse results apply only to the recorded roots. |
| adapter | Optional structured source adapter; adapter-check.json | supports | No applicable runnable adapter was established in recorded local discovery. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; Actual execution 2026-10-21T12:07:48.430343+00:00 to 2026-10-21T12:07:49.308295+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-strict kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml --out /private/tmp/cm-review-session/batch-07/000010/strict-report.tsv; Actual execution 2026-10-21T12:07:48.430522+00:00 to 2026-10-21T12:07:50.761826+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-terms kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; Actual execution 2026-10-21T12:07:48.430662+00:00 to 2026-10-21T12:07:50.310920+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; Actual execution 2026-10-21T12:07:49.308640+00:00 to 2026-10-21T12:07:49.386430+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; Actual execution 2026-10-21T12:07:49.386681+00:00 to 2026-10-21T12:07:50.815424+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-history history/records/BioModels_MODEL2209060002_DPigrum_SAureus_Community; Actual execution 2026-10-21T12:07:50.311263+00:00 to 2026-10-21T12:07:51.042698+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T12:07:51.043534+00:00 to 2026-10-21T12:07:51.103271+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml; Actual execution 2026-10-21T12:07:51.103544+00:00 to 2026-10-21T12:07:52.173393+00:00 | supports | Reference validation passed against pinned caches. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T11:32:06.425768+00:00 to 2026-10-21T11:32:16.427975+00:00 | supports | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; target-native structure is COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T11:32:06.426382+00:00 to 2026-10-21T11:32:14.966232+00:00 | supports | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; target-native structure is COMPLETE. |

## Limits And Additional Notes

- No flux optimization, model reproduction, clinical efficacy assessment, raw sequence analysis or independent audit of the cited wet-lab studies.
- Table 1 full intracellular flux worksheets were inventoried, not exhaustively interpreted; Table 2 inspection is scenario-specific and does not establish experimental metabolite transfer.
- The author notebook, deposited model and published tables encode different configurations. Default bounds and objectives must not be silently assigned to every published run.
- The source prints ASM19771v1; live exact-strain metadata identifies ASM719771v1. Preserve that discrepancy rather than silently correcting the source or changing strain identity.
- No unique physical medium, new environmental CURIE or strain-level taxon substitution was certified.
- Source statements interpreting time lag, antibacterial chemistry or clinical benefit remain hypotheses; this review does not reproduce underlying wet-lab studies.
- No canonical, cache, history or generated files changed. All 25 repository inputs remain pinned.
- All quotations from this publication and its supplements share one 25-word limit.
- Native quality 100 is capped from 121; scientific completeness findings remain.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T121411Z-dpigrum-saureus-model-record
kind: record
repository: CultureBotAI/CommunityMech
title: D. pigrum–S. aureus community model review
started_at: '2026-10-21T12:07:12.078382Z'
finished_at: '2026-10-21T12:14:11.699365Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, native/ontology checks
    and supporting metadata; no person-level independence asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The correct modeled pair and two qualified nodes are retained. One major
  finding addresses omitted growth-enabling nutrients; two minor findings address
  static endpoints/computational provenance and source-strain/resource organization.
source:
  git_revision: 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/review-communities/reference/execution-protocol.md
    sha256: 0d4448074611c020c54b6b20c478b24e2cf2a195f7fc4f7dbcfac19134f731c4
    role: context
  - path: .claude/skills/review-communities/reference/metrics-and-reports.md
    sha256: 2647416ac98a8f9569e0afbd826a0d1229bb4262639934848639ce536b0974fc
    role: context
  - path: .claude/skills/review-communities/reference/validation-rules.md
    sha256: 3860e91a64f7c1f55f80e3d7a361d0798bbd00cbaf5cb7720a7533673e5afe2e
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 1005e1b9eb7f83306a1f88a6d22ec7954a54c2bf2e2fc15923fdaaa1111a3d2b
    role: context
  - path: AGENTS.md
    sha256: 4a3fccdfa03ff1f7f6ecd68465064bfaba97a0efbc1efd4f7809c3ca0529a557
    role: context
  - path: CLAUDE.md
    sha256: 8458fc2ca6663fea0e94c8e5b79730aafe6f4b3ac2c0f1079a3b64a2bb4d3d98
    role: context
  - path: conf/record_review.yaml
    sha256: 8cbd8f9d209f78de47a8c35091e43bf1dadbe41ee07492c7860b6d4be30112a8
    role: context
  - path: conf/reference_validator.yaml
    sha256: 5cd4781c7e15b7c5472f0b008e41764842cc023a7ba99f4273298f421be36652
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: 86c0347d77402bcecdec466b01974ad53beddb9cf1bd17cf085674970542a101
    role: context
  - path: history/records/BioModels_MODEL2209060002_DPigrum_SAureus_Community/2026-10-02T052108Z-codex-df3921.yaml
    sha256: dfebe9408587f2640dc1b85735adbdc427bf33b79dc9d19eaeed12f3ca443cd5
    role: context
  - path: history/records/BioModels_MODEL2209060002_DPigrum_SAureus_Community/2026-10-05T124959Z-codex-d0275f.yaml
    sha256: 5182b7bcacfd890a2f4793698ab8786672fed087326b29dddf48a93a5830d55d
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    sha256: 45ea96efd71094d61fc28d38e2ce107358b785f173e2982e48c87edf69ca73d6
    role: target
  - path: references_cache/doi_10.3389_fcimb.2022.925215.json
    sha256: 148b2fbda688d8aba95a75fe4c1a27c6eded1bc381d474ecbdf9baff26268937
    role: context
  - path: references_cache/doi_10.3389_fcimb.2022.925215.md
    sha256: 8c5708554946ab3296e92aab20711d17e43b7f882ba5eb2f966049726c1f35b4
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch7.yaml
    sha256: c96f00489d2ad14f63cd035adc778adbf72d7fe6a11c2dffd81cd1a904cc0a75
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000010
  path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  label: BioModels MODEL2209060002 D pigrum - S aureus Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    role: canonical_record
scope:
  description: Whole record, fresh primary main, declared critical figures/supplementary
    tables and direct model/code/strain authorities.
  selection: Only released CommunityMech:000010 after 000009 save and both mandatory
    gates.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000010
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000010
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh target/history checks plus corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000010
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-strict kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    --out /private/tmp/cm-review-session/batch-07/000010/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh target/history checks plus corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000010
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-terms kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh target/history checks plus corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000010
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh target/history checks plus corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000010
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh target/history checks plus corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000010
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-history history/records/BioModels_MODEL2209060002_DPigrum_SAureus_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh target/history checks plus corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000010
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh target/history checks plus corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against pinned caches.
  target_ids:
  - CommunityMech:000010
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh target/history checks plus corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records;
    target-native structure is COMPLETE.
  target_ids:
  - CommunityMech:000010
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit reuse of fresh batch 07 corpus receipts, not a target-specific
    pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records;
    target-native structure is COMPLETE.
  target_ids:
  - CommunityMech:000010
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit reuse of fresh batch 07 corpus receipts, not a target-specific
    pass.
- check_id: source-identity
  name: Primary source and resource identity
  status: passed
  required: true
  summary: Direct primary publication and focal model identities verified; input assembly-name
    discrepancy is preserved.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - pubmed
  - resources
  - assembly
- check_id: scientific-source
  name: Whole-record scientific assessment
  status: passed
  required: true
  summary: Complete main and declared critical figure/table/model scopes inspected;
    no simulation executed.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - source-scope
  - independent-source
- check_id: cross-mech
  name: Medium and ingredient external links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech identifier is encoded; simulated
    media do not establish a unique physical recipe link.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - record
  - medium
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No runnable applicable adapter was established in recorded discovery.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: 'Whole record: two taxa, two computational nodes and no arrows'
  summary: The record identifies the correct pair/model and explicitly distinguishes
    in-silico constraints from bench culture, but lacks growth-enabling nutrient and
    scenario provenance.
  support: supports
  accessed_at: '2026-10-21T12:14:11.695275Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=36605126&retmode=xml
  locator: Article-level metadata and abstract where supplied
  summary: PMID36605126, DOI and article title/abstract identify the focal study.
  support: supports
  accessed_at: '2026-10-21T12:07:45.310033Z'
  snapshot_sha256: b4fd02afda63850e5bc64a6b8b4b6e04d273cc45254d61ef21523304a258c4e2
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.3389/fcimb.2022.925215
  locator: Article-level metadata and abstract where supplied
  summary: DOI/title/authors verified as bibliographic metadata.
  support: supports
  accessed_at: '2026-10-21T12:07:45.308872Z'
  snapshot_sha256: 94e9e3ab8614cab273506a93c07cf106464f84bf3667169a3569fef67f9d6c97
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:36605126&format=json&resultType=core
  locator: Article-level metadata and abstract where supplied
  summary: PMID36605126/PMC9810029 and direct full-text availability identify the
    source.
  support: supports
  accessed_at: '2026-10-21T12:07:45.678780Z'
  snapshot_sha256: f3d78ce6e4372745a5e1a5b9e5b21e8aff8ec8f98e3ef8940911ce08a4be9656
- evidence_id: assembly
  kind: primary_source
  reference: doi:10.3389/fcimb.2022.925215
  locator: Fresh XML s1 Introduction; s2 Methods; s3_3 artificial pairwise design
  summary: The study combines D. pigrum 83VPs-KB5 and S. aureus USA300 JE2 reconstructions,
    using integrated, compartmentalized and pooled formulations. ENGINEERED is defensible
    when explicitly scoped to the artificial computational assembly.
  support: supports
  accessed_at: '2026-10-21T12:14:11.695863Z'
  snapshot_sha256: f6573f6f212ba2899f001bcdc74a6323ddf7f324175e8f26ad9d07c4ac2f8a84
- evidence_id: medium
  kind: primary_source
  reference: doi:10.3389/fcimb.2022.925215
  locator: Fresh XML s2_4; s3_1; s3_9 Tables 3–4; s3_12 Figures 10–11/Table 6
  summary: Baseline D. pigrum has no growth in SNM3. L-isoleucine, L-methionine and
    meso-2,6-diaminoheptanedioate enable growth. The later constrained rescue lets
    S. aureus supply the two amino acids while DAP is manually supplied.
  support: supports
  accessed_at: '2026-10-21T12:14:11.695972Z'
  quote: no growth on SNM3
  snapshot_sha256: f6573f6f212ba2899f001bcdc74a6323ddf7f324175e8f26ad9d07c4ac2f8a84
- evidence_id: exchange
  kind: primary_source
  reference: doi:10.3389/fcimb.2022.925215
  locator: Fresh XML s3_6 and Figure 4 caption; Figure 4 pixels
  summary: D. pigrum cysteine uptake and D-serine secretion vary with formulation
    and objective. The highlighted exchanges do not establish antimicrobial synthesis
    or mediate the S. aureus outcome.
  support: partial
  accessed_at: '2026-10-21T12:14:11.696078Z'
  quote: does not depend
  snapshot_sha256: f6573f6f212ba2899f001bcdc74a6323ddf7f324175e8f26ad9d07c4ac2f8a84
- evidence_id: inhibition
  kind: primary_source
  reference: doi:10.3389/fcimb.2022.925215
  locator: Fresh XML s3_7; s3_9 Figure 7; s3_12 Figures 10–11
  summary: The pooled model at 10:1 weight favoring D. pigrum yields zero S. aureus
    growth. Other media/objectives allow S. aureus growth and conditional support
    of D. pigrum; the result is not clinical efficacy.
  support: partial
  accessed_at: '2026-10-21T12:14:11.696182Z'
  quote: failed to grow
  snapshot_sha256: f6573f6f212ba2899f001bcdc74a6323ddf7f324175e8f26ad9d07c4ac2f8a84
- evidence_id: static-method
  kind: primary_source
  reference: doi:10.3389/fcimb.2022.925215
  locator: Fresh XML s2_1–s2_6; s3_5–s3_8; s4 Discussion; s5 Data Availability
  summary: FBA/FVA, objectives, weights, uptake bounds and solver choices describe
    static predictions. The paper explicitly distinguishes this work from dynamic
    behavior; generic abundance/persistence tracking is not a measured endpoint.
  support: supports
  accessed_at: '2026-10-21T12:14:11.696287Z'
  quote: not the dynamic behavior
  snapshot_sha256: f6573f6f212ba2899f001bcdc74a6323ddf7f324175e8f26ad9d07c4ac2f8a84
- evidence_id: conditional-roles
  kind: primary_source
  reference: doi:10.3389/fcimb.2022.925215
  locator: Fresh XML s3_2, s3_9 Table 4, s3_12 Table 6; Table_2.xlsx Summary_exchange_shuttels_SNM_1
    row 10 and Summary_exchange_shuttels_Exch1 row 13
  summary: D. pigrum is a conditional amino-acid recipient. S. aureus can take up
    ornithine while D. pigrum secretes it in selected model scenarios; ornithine is
    also supplied externally, and this is not exclusive partner dependence.
  support: partial
  accessed_at: '2026-10-21T12:14:11.696308Z'
  snapshot_sha256: 39ebe6e1061a8d339b352d5c886eb7cdea620f5e8eecd5543d98581d05cee0a4
- evidence_id: supplement
  kind: primary_source
  reference: doi:10.3389/fcimb.2022.925215
  locator: 'workbook-scope.json: declared Table 1, Table 2 and Table 3 scope'
  summary: Supplementary medium dictionaries and shuttle tables support scenario separation.
    Numeric strings were parsed for table inspection; no solver or statistical reanalysis
    was performed.
  support: supports
  accessed_at: '2026-10-21T12:14:11.696327Z'
  snapshot_sha256: 39ebe6e1061a8d339b352d5c886eb7cdea620f5e8eecd5543d98581d05cee0a4
- evidence_id: availability
  kind: primary_source
  reference: doi:10.3389/fcimb.2022.925215
  locator: Fresh XML s1 Introduction and s5 Data Availability
  summary: The exact BioModels community accession, author repository and software
    requirements are reported. CP020619.1 and the printed ASM19771v1 identify input-reconstruction
    provenance, not new experimental datasets.
  support: supports
  accessed_at: '2026-10-21T12:14:11.696429Z'
  snapshot_sha256: f6573f6f212ba2899f001bcdc74a6323ddf7f324175e8f26ad9d07c4ac2f8a84
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity; FunctionalRoleEnum; EngineeringDesign; GrowthMedia.headspace_gas;
    ComputationalProvenance
  summary: Recipient roles need scenario-specific evidence; headspace describes physical
    gas, while computational provenance provides model, method, toolchain, medium
    and parameter fields.
  support: supports
  accessed_at: '2026-10-21T12:14:11.696487Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: ontology-authority.json
  summary: All four unique pairs/nine occurrences match. Species grounding and broad
    interaction GO terms are valid; no replacement is required.
  support: supports
  accessed_at: '2026-10-21T12:14:11.696684Z'
  snapshot_sha256: dc476a33fba6687a5f8330d92d1746a7620fe77800c0d68876ddc739fca45ecb
- evidence_id: model-boundary
  kind: database
  reference: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: root-model-boundary.json
  summary: The focal deposit is a two-species community with seven compartments and
    two equally weighted biomass objectives. Its current open nutrient exchanges are
    one configuration, not all published run settings.
  support: supports
  accessed_at: '2026-10-21T12:14:11.696723Z'
  snapshot_sha256: a4b8bf21fea8e7c348fe99ae2e90b4f51d9ba91d7fb9dd96d82434b550aa7d20
- evidence_id: resources
  kind: database
  reference: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: dataset-verification.json
  summary: BioModels file identity, immutable author code/input and bounded CP020619.1/exact-strain
    assembly metadata are verified. Notebook nutrient additions and ornithine closure
    are preserved as configuration-specific.
  support: supports
  accessed_at: '2026-10-21T12:14:11.696756Z'
  snapshot_sha256: 0b3f57231e92061a54d8f5a7dcb24145c283fae75f596383df2cce8cbfd776bc
- evidence_id: snippets
  kind: validation
  reference: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: snippet-audit.json
  summary: All 12 snippets match directly retrieved full XML and the pinned cache;
    lexical support does not establish every attached scope claim.
  support: supports
  accessed_at: '2026-10-21T12:14:11.696892Z'
  snapshot_sha256: 08d9b9cf074ed525c77ce4397aef2a10f8469121b73335751d601d4b9ad7bfb8
- evidence_id: history
  kind: record_content
  reference: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: provenance-audit.json
  summary: Closed 1258 preserves the prior graph repair; open 1262 specifically tracks
    missing nutrient handling and generic endpoints.
  support: supports
  accessed_at: '2026-10-21T12:14:11.697048Z'
  snapshot_sha256: 3fe935b3cf5e26d0ea47ad0a78cd7a62fbb02c764964f887509586363b6cf6f3
- evidence_id: native-target
  kind: validation
  reference: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: support-audit.json
  summary: Native completeness and quality are mechanical measures, separate from
    the one major and two minor findings.
  support: supports
  accessed_at: '2026-10-21T12:14:11.697180Z'
  snapshot_sha256: 122d0233aff5a419d1a4c48a6e0cb3c6e099f4dc20266cf5a246ba5dc1c8e56c
- evidence_id: source-scope
  kind: validation
  reference: doi:10.3389/fcimb.2022.925215
  locator: source-audit.json
  summary: Whole main and declared critical figure/table/model scopes were inspected.
  support: supports
  accessed_at: '2026-10-21T12:14:11.697215Z'
  snapshot_sha256: 4252462af5329d81147aeabedfefb14ca4686118aadd01556fa0267e03cd82e4
- evidence_id: independent-source
  kind: validation
  reference: doi:10.3389/fcimb.2022.925215
  locator: root-independent-source-audit.json
  summary: Independent whole-record and primary/supplementary source assessment corroborates
    the bounded findings.
  support: context_only
  accessed_at: '2026-10-21T12:14:11.697242Z'
  snapshot_sha256: a71532bdc96f968b8b5b1fb34ceb4f8f898de133057d57fcedb6edb50d252aa9
- evidence_id: search
  kind: search
  reference: Owned maintained roots
  locator: 'local-search.json: ignored-inclusive bounded discovery'
  summary: Local identity/reuse results apply only to the recorded roots.
  support: supports
  accessed_at: '2026-10-21T12:14:11.697367Z'
  snapshot_sha256: 5ce13b4b3a3914abeed9bd94c61f4077a7d86b1a2a7eb305e1e07abfd806da2a
  search_scope: Ignored-inclusive maintained community, isolate and reusable-taxon
    roots and recorded mapping-file discovery.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: adapter-check.json
  summary: No applicable runnable adapter was established in recorded local discovery.
  support: supports
  accessed_at: '2026-10-21T12:14:11.697488Z'
  snapshot_sha256: 19e4bd3f2720f1c464d02df86e4a946007f03068b670a5f8b4d2761da3938517
  search_scope: Recorded runtime and ignored-inclusive local discovery; no outside-checkout
    execution or paid provider.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: Actual execution 2026-10-21T12:07:48.430343+00:00 to 2026-10-21T12:07:49.308295+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T12:07:49.308295Z'
  snapshot_sha256: f6a591cec160a9aa820897113756fc57caae565c8186dd9da8876a76dc6637ba
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-strict kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    --out /private/tmp/cm-review-session/batch-07/000010/strict-report.tsv
  locator: Actual execution 2026-10-21T12:07:48.430522+00:00 to 2026-10-21T12:07:50.761826+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T12:07:50.761826Z'
  snapshot_sha256: 3018f877d10f364ce2c8e0acfec383ef0e270ee8311a7bc46c21014130ad492d
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-terms kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: Actual execution 2026-10-21T12:07:48.430662+00:00 to 2026-10-21T12:07:50.310920+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T12:07:50.310920Z'
  snapshot_sha256: 0857c25dbe3f5c7def685a44abf31457d426f419cc70efae3be34457f4b57423
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: Actual execution 2026-10-21T12:07:49.308640+00:00 to 2026-10-21T12:07:49.386430+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T12:07:49.386430Z'
  snapshot_sha256: 1aaf04a8e6dfcbd4cf8a515162bd40360117b4519e914a77fd603d696af55925
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: Actual execution 2026-10-21T12:07:49.386681+00:00 to 2026-10-21T12:07:50.815424+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T12:07:50.815424Z'
  snapshot_sha256: 22bdb38bce972421e2f7998c79dd64c73e3cbae5f14cac99b57c3bae980b8d24
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-history history/records/BioModels_MODEL2209060002_DPigrum_SAureus_Community
  locator: Actual execution 2026-10-21T12:07:50.311263+00:00 to 2026-10-21T12:07:51.042698+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T12:07:51.042698Z'
  snapshot_sha256: 74689bfde94ed0e41d240edc333e9e6e7f09a21cae137b3a3d8799ba2282c48d
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T12:07:51.043534+00:00 to 2026-10-21T12:07:51.103271+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T12:07:51.103271Z'
  snapshot_sha256: 8a58ddb21aa9d7293ada96bd6a09c4fab3596136462c05d26c763aa30bc369d7
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  locator: Actual execution 2026-10-21T12:07:51.103544+00:00 to 2026-10-21T12:07:52.173393+00:00
  summary: Reference validation passed against pinned caches.
  support: supports
  accessed_at: '2026-10-21T12:07:52.173393Z'
  snapshot_sha256: 96ec8e05d93724b8073f54b71b94c61da54e6bff9a9afe73923776a7500029f7
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T11:32:06.425768+00:00 to 2026-10-21T11:32:16.427975+00:00
  summary: Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records;
    target-native structure is COMPLETE.
  support: supports
  accessed_at: '2026-10-21T11:32:16.427975Z'
  snapshot_sha256: c16b3a28b790e90191e9c5fb067c97a8038a813593fbfbe1796bf78d116abafb
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T11:32:06.426382+00:00 to 2026-10-21T11:32:14.966232+00:00
  summary: Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records;
    target-native structure is COMPLETE.
  support: supports
  accessed_at: '2026-10-21T11:32:14.966232Z'
  snapshot_sha256: 6a321df993e978ed76cacc843bf792ecb9969ab237ca14c6e8575723ee3410f3
assessments:
- assessment_id: identity
  area: identity
  topic: Pair, computational scope and source strains
  outcome: supported
  summary: The correct two-species community model is linked; source strains and individual
    configurations should be made explicit.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - record
  - assembly
  - resources
  - model-boundary
  dimensions:
  - name: community_scope
    value: Artificial two-species genome-scale community
    definition: The modeled pair is not a measured whole nasal microbiome or clinical
      intervention.
    evidence_ids:
    - assembly
    - model-boundary
  - name: source_strain
    value: D. pigrum 83VPs-KB5; S. aureus USA300 JE2
    definition: Source reconstruction identities are recoverable. The printed D. pigrum
      assembly name differs from current exact-strain archive metadata.
    evidence_ids:
    - assembly
    - resources
  - name: environment
    value: Human nasal habitat represented computationally
    definition: The laboratory term is broad context; distinguish modeled nasal habitat
      from a physically sampled or cultured community.
    evidence_ids:
    - assembly
    - ontology
  - name: medium
    value: SNM3 and separately constrained exchange/COMPM/COOPM media
    definition: Growth-enabling additions and transfer-rescue conditions must accompany
      the bound conventions. They are not a wet-lab recipe.
    evidence_ids:
    - medium
    - supplement
  - name: experimental_setting
    value: Static FBA/FVA and alternative community formulations
    definition: Objective weights and survival constraints are imposed model parameters,
      not observed inoculum fractions or longitudinal persistence.
    evidence_ids:
    - static-method
  - name: evidence_tier
    value: Computational prediction; background empirical motivation
    definition: Prior association and wet-lab studies are cited as motivation, not
      reproduced here. No demonstrated mediator or clinical effect is claimed.
    evidence_ids:
    - exchange
    - inhibition
  - name: grounding_status
    value: Four valid ontology pairs; both species GTDB-grounded
    definition: No strain-level taxon or new medium CURIE is inferred from accession
      metadata alone.
    evidence_ids:
    - ontology
    - resources
- assessment_id: roles
  area: grounding
  topic: Species and conditional CROSS_FEEDER roles
  outcome: supported
  summary: Both recipient roles have computational support when restricted to the
    appropriate scenarios.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - conditional-roles
  - supplement
  - resources
  details: Sa→Dp amino-acid support is explicit in forced-growth/rescue scenarios;
    Dp→Sa ornithine exchange appears in selected supplementary shuttle tables. The
    author notebook closes Sa ornithine uptake in one setup, whereas other outputs/deposited
    settings allow it. Add local role evidence and scenario qualifiers; no unconditional
    reciprocal dependence or experimental transfer is established. No abundance field
    needs repair.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: exchange-factor prediction'
  outcome: supported
  summary: Retain D. pigrum → S. aureus as a qualified pairwise computational prediction,
    not an inhibitory mechanism.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - exchange
  - static-method
  details: Figure 4 and its caption support D. pigrum cysteine uptake and D-serine
    release across tested media/objectives, while explicitly stating that S. aureus
    does not depend on these highlighted fluxes. The broad GO term is compatible with
    the stated modeled interaction. No antimicrobial synthesis or mediator arrow is
    warranted.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: growth-inhibition hypothesis'
  outcome: supported
  summary: Retain D. pigrum → S. aureus as conditional modeled growth suppression.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - inhibition
  - medium
  - static-method
  details: The pooled 10:1 objective case gives zero Sa growth; other formulations
    retain growth and can require Sa→Dp nutritional support. The record correctly
    distinguishes objective weights from measured inoculation dynamics and competition
    indices from reciprocal negative fitness. Background association and proposed
    application remain PARTIAL, not direct clinical proof.
- assessment_id: arrows
  area: graph
  topic: Downstream causal scope
  outcome: supported
  summary: There are no downstream arrows; preserve that restraint.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - record
  - exchange
  - inhibition
  details: Assembly, constraints and medium construction are workflow steps. Neither
    cysteine/D-serine fluxes nor the static scenarios establish a measured causal
    chain to inhibition.
- assessment_id: conditions
  area: completeness
  topic: Growth-enabling nutrients and model conditions
  outcome: concern
  summary: The SNM3 block omits additions necessary to interpret whether D. pigrum
    can grow.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - medium
  - supplement
  - resources
  details: Separate baseline non-growing Dp, supplemented growth, and the constrained
    Sa amino-acid rescue with manually supplied DAP. Keep COMPM/COOPM and exchange
    medium distinct. Absence of temperature/pH/vessel metadata is appropriate for
    this computational study; oxygen bounds are not physical headspace.
- assessment_id: design
  area: evidence
  topic: Static endpoints and structured computational provenance
  outcome: concern
  summary: Generic abundance/persistence tracking is unsupported; modeled outputs
    and run conditions are recoverable.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - static-method
  - schema
  - model-boundary
  details: Retain ENGINEERED as computational assembly. Replace generic design text
    with source formulations and predicted biomass/exchange outputs. Add computational
    provenance to model-claim evidence; bibliographic-only evidence does not need
    invented simulation settings.
- assessment_id: resources
  area: provenance
  topic: Model, publication, code and input strains
  outcome: concern
  summary: The correct current model file resolves, but publication and dataset roles
    are conflated and input provenance is incomplete.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - availability
  - resources
  - assembly
  details: Keep SA_DP_community.xml/MODEL2209060002. A primary publication is evidence
    rather than a separate scientific dataset. Link source code and verified input-strain
    metadata with version/access scope; preserve the printed ASM19771v1 versus archive
    ASM719771v1 discrepancy. No claim of complete model reproduction or raw genome
    inspection follows.
- assessment_id: history
  area: provenance
  topic: Prior graph repairs and reference support
  outcome: supported
  summary: All 12 snippets are directly source-verifiable, and the two-node/no-arrow
    repair remains justified.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - snippets
  - history
  - exchange
  details: Open 1262 is current follow-up context; closed 1258 is a completed graph
    repair. Historical unavailable figure/SI scope is not a limitation of this fresh
    assessment.
- assessment_id: validation
  area: schema
  topic: Native checks
  outcome: supported
  summary: All eight native checks pass; semantic completeness findings remain.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
- assessment_id: metrics
  area: completeness
  topic: Mechanical metrics
  outcome: supported
  summary: Capped quality does not negate one major and two minor findings.
  target_ids:
  - CommunityMech:000010
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required metadata/roles +5 environment +5 resources +10 media +5
      datasets; no three-node, environmental-factor or metabolite bonus.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0,P2=1,P3=2,P4=0; 4/2 mean evidence gives20 bonus, network15:121 before capping.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 1
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 2
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
findings:
- finding_id: growth-enabling-nutrients
  issue_key: cm-000010-growth-enabling-nutrients
  category: completeness
  severity: major
  native_severity: P2
  normalization_reason: 'P2: missing inputs materially change whether one modeled
    member grows and how cross-feeding is interpreted.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Represent growth-enabling nutrients and rescue scenarios
  description: The current SNM3 description names only oxygen/iron exceptions and
    closes all other exchanges, omitting L-isoleucine, L-methionine and meso-2,6-diaminoheptanedioate
    required for Dp growth. These omissions change the modeled feasibility, not merely
    recipe detail.
  target_ids:
  - CommunityMech:000010
  field_paths:
  - growth_media[0].composition
  - growth_media[0].preparation_notes
  evidence_ids:
  - medium
  - supplement
  - resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    role: canonical_record
- finding_id: static-provenance
  issue_key: cm-000010-static-provenance
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: existing descriptions already qualify the model correctly;
    this repairs bounded generic endpoints and parameter placement rather than the
    scientific interaction conclusions.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Replace generic tracking endpoints with model-specific provenance
  description: engineering_design claims abundance/persistence tracking although this
    is static constraint-based analysis. Computational provenance is recoverable but
    unstructured, and an oxygen uptake bound occupies physical headspace_gas.
  target_ids:
  - CommunityMech:000010
  field_paths:
  - engineering_design
  - growth_media[0].headspace_gas
  - ecological_interactions[0].evidence
  - ecological_interactions[1].evidence
  evidence_ids:
  - static-method
  - schema
  - model-boundary
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    role: canonical_record
- finding_id: strain-resource-provenance
  issue_key: cm-000010-strain-resource-provenance
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: correct pair/model identity is already traceable; this
    is recoverable strain, claim-level role and resource organization.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Clarify source strains and resource types
  description: Species-level identity is valid, but source reconstruction strains
    and local role evidence are missing, while the primary paper is listed as a dataset.
    Current model/code/strain authorities allow a bounded provenance improvement.
  target_ids:
  - CommunityMech:000010
  field_paths:
  - taxonomy[0]
  - taxonomy[1]
  - associated_datasets
  - external_resources
  evidence_ids:
  - assembly
  - conditional-roles
  - availability
  - resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    role: canonical_record
actions:
- action_id: repair-growth-enabling-nutrients
  description: Represent growth-enabling nutrients and rescue scenarios.
  finding_ids:
  - growth-enabling-nutrients
  target_ids:
  - CommunityMech:000010
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    role: canonical_record
  acceptance_checks:
  - State baseline Dp does not grow on unaugmented SNM3 and identify the three growth-enabling
    additions with source evidence. Preserve model flux units rather than inventing
    bench concentrations.
  - 'Separate supplemented growth from the Section 3.12 rescue: Sa supplies isoleucine/methionine
    under imposed constraints, while DAP is manually supplied because the model does
    not provide it through Sa exchange.'
  - Retain scenario-specific objective weights, survival constraints and exchange/COMPM/COOPM
    definitions. Do not apply notebook addition bounds or deposited FVA-derived defaults
    to every published run.
  - Keep the medium explicitly computational and preserve the absence of reported
    physical incubation conditions.
- action_id: repair-static-provenance
  description: Replace generic tracking endpoints with model-specific provenance.
  finding_ids:
  - static-provenance
  target_ids:
  - CommunityMech:000010
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Replace tracking endpoints with predicted member/community biomass, exchange fluxes
    and scenario-dependent inhibition; describe integrated, compartmentalized and
    pooled constructions as applicable.
  - Populate computational_provenance for actual model claims with FBA/FVA, toolchain,
    model/version, simulated medium and objective/constraint settings. Preserve source-reported
    software versions and avoid inventing unreported versions.
  - Move the oxygen bound to model parameters; distinguish modeled nasal habitat from
    physical headspace. Retain ENGINEERED only with explicit computational assembly
    scope.
  - Preserve both qualified nodes and zero arrows; do not restore exchange-to-inhibition
    mediation, physical population dynamics or clinical efficacy.
- action_id: repair-strain-resource-provenance
  description: Clarify source strains and resource types.
  finding_ids:
  - strain-resource-provenance
  target_ids:
  - CommunityMech:000010
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Record source_strain values 83VPs-KB5 and USA300 JE2 with source evidence, without
    claiming all biological strains of either species share the simulated response.
  - 'Attach scenario-specific recipient evidence to CROSS_FEEDER: Dp amino-acid uptake
    and Sa ornithine uptake in selected model outputs. Preserve external ornithine
    supply and notebook closure as limits; do not claim obligate or universal reciprocal
    dependence.'
  - Keep the correct BioModels file and link immutable author code/input provenance.
    Move the primary publication to evidence or literature resources rather than counting
    it as a dataset.
  - If input accessions are added, preserve CP020619.1 and the documented printed
    ASM19771v1 versus live exact-strain ASM719771v1 discrepancy; resolve with explicit
    provenance, not silent source correction. Do not label input assemblies as newly
    generated focal data.
limitations:
- No flux optimization, model reproduction, clinical efficacy assessment, raw sequence
  analysis or independent audit of the cited wet-lab studies.
- Table 1 full intracellular flux worksheets were inventoried, not exhaustively interpreted;
  Table 2 inspection is scenario-specific and does not establish experimental metabolite
  transfer.
- The author notebook, deposited model and published tables encode different configurations.
  Default bounds and objectives must not be silently assigned to every published run.
- The source prints ASM19771v1; live exact-strain metadata identifies ASM719771v1.
  Preserve that discrepancy rather than silently correcting the source or changing
  strain identity.
- No unique physical medium, new environmental CURIE or strain-level taxon substitution
  was certified.
- Source statements interpreting time lag, antibacterial chemistry or clinical benefit
  remain hypotheses; this review does not reproduce underlying wet-lab studies.
notes:
- No canonical, cache, history or generated files changed. All 25 repository inputs
  remain pinned.
- All quotations from this publication and its supplements share one 25-word limit.
- Native quality 100 is capped from 121; scientific completeness findings remain.
tags:
- record-review
- nasal-model
- metabolic-model
- batch-07
```
