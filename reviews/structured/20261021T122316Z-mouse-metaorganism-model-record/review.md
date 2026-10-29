# Mouse metaorganism model review

- Review: 20261021T122316Z-mouse-metaorganism-model-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T12:15:33.863705Z
- Finished UTC: 2026-10-21T12:23:16.900135Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Three qualified computational nodes and no arrows remain supported. Two major findings address incomplete microbial roster scope and unsupported ecological stability; two minor findings address cohort/diet/model provenance and public resource organization.

## Scope And Provenance

Whole record, fresh primary main, declared figures and supplementary tables, and direct model/data authorities.

Selection: Only released CommunityMech:000011 after 000010 save and both mandatory gates.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000011 | kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml | maintained | BioModels MODEL2310020001 Mouse Metaorganism Model |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000011 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000011 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000011 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000011 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000011 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000011 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000011 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000011 | Reference validation passed against pinned cache. |
| audit-network | failed | True | CommunityMech:000011 | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; target-native structure is COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000011 | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; target-native structure is COMPLETE. |
| Primary source and resource identity | passed | True | CommunityMech:000011 | Direct publication and model/project identities verified within explicit metadata/static-inspection scope. |
| Whole-record scientific assessment | passed | True | CommunityMech:000011 | Complete main and declared critical figure/supplement/model scopes inspected; no simulation executed. |
| Medium and ingredient external links | not_applicable | False | CommunityMech:000011 | No CultureMech or MediaIngredientMech identifier is encoded. Modeled diet does not imply a microbial cultivation recipe. |
| Optional structured source adapter | unavailable | False | CommunityMech:000011 | No runnable applicable adapter was established in recorded discovery. |

## Scientific And Domain Assessments

### Natural source community and modeled representation

identity: concern. Targets: CommunityMech:000011.

The model identity is correct, but taxonomy exposes only two of eight source phyla without declaring representative coverage.

### Ecological state and origin

evidence: concern. Targets: CommunityMech:000011.

NATURAL origin is supported; STABLE equilibrium is not established.

Aging-associated composition, interaction and metabolic shifts are compared across separate cohorts. Computational steady-state constraints or stable reconstruction clusters are not evidence of ecological equilibrium. The state field is optional in the schema but contributes to the native completeness score. Omit unsupported state or qualify its representation without automatically substituting ENGINEERED or TRANSIENT.

### Taxa, roles and abundance

grounding: concern. Targets: CommunityMech:000011.

The two aggregates are valid but incomplete for the whole modeled microbial source.

Keep host tissues excluded. Add explicit representative scope or recover the remaining source phyla with verified grounding. Do not invent generic phylum functions to improve completeness. No numerical abundance field is encoded; global GTDB support counts are mapping statistics, not cohort abundance.

### ecological_interactions[0]: beneficial interaction predictions

graph: supported. Targets: CommunityMech:000011.

Retain community-level comparison of single and paired microbial growth across age cohorts.

Participants are the modeled bacterial MAG pairs, not merely the two displayed phylum aggregates. Source comparisons support reduced commensal/beneficial interaction frequency but not universal decline of every positive category; mutualism is unchanged in S4.10. No loss-to-metabolite causal arrow is established.

### ecological_interactions[1]: competitive interaction shift

graph: supported. Targets: CommunityMech:000011.

Retain community-level COMPETITION as a predicted paired-growth category.

The normalized frequency rises with age while amensal, commensal and neutral categories decline. This does not demonstrate longitudinal competitive exclusion or mediation of all concurrent metabolite shifts; the existing wording preserves those limits.

### ecological_interactions[2]: host nucleotide support

graph: supported. Targets: CommunityMech:000011.

Retain pooled microbial ↔ host-colon/liver/brain metabolic predictions with PARTIAL barrier interpretation.

The direction is reciprocal and metabolite-specific, not blanket commensalism. Predicted ATP/NAD/CoA and other nucleotide-related routes support the pathway scope; nucleosides/precursors must not all be relabeled as nucleotides. Broad germ-free/colonization validation and literature support do not establish donor-specific flux or route-specific rescue.

### Downstream causal scope

graph: supported. Targets: CommunityMech:000011.

Preserve zero downstream arrows between the three qualified nodes.

Species-pair ecological classification and pooled host-metabolism analysis are separate. Their aging association does not establish a directed causal chain through competition to host barrier dysfunction.

### Host conditions and computational provenance

completeness: concern. Targets: CommunityMech:000011.

Housing, model diet, reconstruction proxy and analysis-specific settings are source-resolvable but largely unstructured.

Add housing as host context and diet/absorption/FBA/FVA settings as computational provenance. Empty growth_media is appropriate; no culturing protocol is implied. Preserve physical cohort, model feasibility and validation differences.

### Nucleotide, succinate and butyrate scope

grounding: supported. Targets: CommunityMech:000011.

Current broad chemical terms support the stated qualified pathway outputs.

S3.2 contains genuine nucleotide/cofactor exchanges alongside nucleosides and precursors. Keep this chemical distinction if adding specific mediators. Succinate/butyrate age associations are predicted metabolism with supporting omics context, not a measured causal route to host aging.

### Model and dataset organization

provenance: concern. Targets: CommunityMech:000011.

The BioModels file and ENA project are traceable; the primary paper is not itself a dataset and additional direct source resources can be linked.

Keep separate metagenomic, transcriptomic, metabolomic and reconstructed-model/code scopes. Archive metadata do not certify all MAG sequence deposits, every raw payload or equivalence of artifact versions.

### Prior repair and snippet support

provenance: supported. Targets: CommunityMech:000011.

All 12 excerpts match direct source text; the earlier three-node/no-arrow repair remains appropriate.

Old unread figure/SI/model limits describe the earlier review, not this assessment. Current source comparison independently preserves its caution about human reconstruction proxies, separate cohorts and unproven mediation.

### Native checks

schema: supported. Targets: CommunityMech:000011.

All eight native checks pass; semantic findings remain.

### Mechanical metrics

completeness: supported. Targets: CommunityMech:000011.

Capped quality does not negate two major and two minor findings.

## Findings

### membership-scope: Resolve incomplete microbial roster coverage

major / open / confirmed; issue key: cm-000011-membership-scope.

The whole metamodel includes 181 MAGs across eight broad phyla, while taxonomy exposes only Bacillota and Bacteroidota without declaring partial coverage. Six phyla and 19 MAGs are omitted from the represented membership.

### stable-state: Qualify the unsupported ecological equilibrium designation

major / open / confirmed; issue key: cm-000011-stable-state.

STABLE asserts equilibrium, which is not demonstrated by separate age cohorts or steady-state metabolic optimization. The source instead describes substantial age-associated ecological and functional shifts.

### computational-context: Structure cohort, diet and simulation context

minor / open / confirmed; issue key: cm-000011-computational-context.

The record has useful prose cautions but lacks structured host conditions and computational provenance needed to distinguish its separate analyses.

### resource-types: Clarify publication and public data resource roles

minor / open / confirmed; issue key: cm-000011-resource-types.

The primary publication is listed as a dataset, while directly reported transcriptomic, metabolomic and model/code resources are not represented.

## Recommended Actions And Acceptance Checks

### repair-membership-scope

Resolve incomplete microbial roster coverage.

- Either complete the source-supported phylum roster or explicitly declare the taxonomy as a representative subset and link the complete S1.2 roster. Do not imply the two aggregates are the entire microbiome.
- Preserve the other source groups: 9 Pseudomonadota, 4 Cyanobacteriota, 3 Campylobacterota, 1 Deferribacterota, 1 Desulfobacterota and 1 Verrucomicrobiota. Use verified candidates where appropriate; do not automatically replace source Desulfobacterota with the current Thermodesulfobacteriota label solely from a related synonym.
- Distinguish source GTDB Bacillota_A (80), Bacillota_B (1) and unsuffixed Bacillota (16) from the global crosswalk majority attached to NCBI Bacillota. Do not infer cohort assignments from global mapping fractions.
- Keep host tissues outside microbial taxonomy and preserve the pooled model versus species-resolved pairwise analysis distinction. Do not invent phylum roles.

### repair-stable-state

Qualify the unsupported ecological equilibrium designation.

- Provide source-specific ecological equilibrium evidence or revise the state representation with explicit uncertainty and rationale.
- The schema makes ecological_state optional; its inclusion in the native completeness rubric does not make it mandatory. Omit unsupported state or retain only a source-justified representation; do not automatically substitute ENGINEERED/TRANSIENT.
- Retain NATURAL source origin and distinguish model steady-state assumptions from measured community stability.

### repair-computational-context

Structure cohort, diet and simulation context.

- Record main-cohort housing and host strain/sex/age context separately from female germ-free validation and metabolomics cohorts. Do not describe the study as longitudinal tracking of the same mice.
- Populate computational_provenance with reconstructed V1534-300 diet, assumed 3.5 g/day intake, human-cohort fibre imputation and pre-colonic absorption; keep these assumptions distinct from measured feed consumption or a bench growth medium.
- Separate species-resolved FBA/pair classification from pooled Recon 2.2 host metamodel/FVA/EFM analysis, with source-specific tools, constraints and thresholds. Preserve 50 feasible community-flux cases versus 52 sampled/context-model mice.
- Preserve the three qualified nodes and no arrows; no route-specific nucleotide rescue or causal competition-to-host chain is established.

### repair-resource-types

Clarify publication and public data resource roles.

- Move PMID40140706 to publication evidence/resources rather than treating it as a scientific dataset.
- Link verified GSE262290/GSE278548, MSV000094409/MSV000094410/MSV000094436, Zenodo10844502 and immutable author code with their source-defined data types and cohort scopes.
- Retain MODEL2310020001/metamodel_20230510.xml and PRJEB73981; distinguish the article-reported MAG deposit from what the inspected archive endpoints independently confirm.
- Preserve archive format/version discrepancies and static-inspection limits. Do not claim raw-data inspection, per-MAG revalidation or simulation reproduction.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; Whole record: two phylum aggregates, three computational nodes and zero arrows | supports | The correct pooled metaorganism model is linked. Host tissues are kept outside microbial taxonomy, and graph descriptions separate computational association from causal mediation. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=40140706&amp;retmode=xml; Article-level metadata and abstract where supplied | supports | PMID40140706, DOI and article title/abstract identify the focal study. |
| crossref | https://api.crossref.org/works/10.1038/s41564-025-01959-z; Article-level metadata and abstract where supplied | supports | DOI/title/authors verified as bibliographic metadata. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40140706&amp;format=json&amp;resultType=core; Article-level metadata and abstract where supplied | supports | PMID40140706/PMC11964932 and direct full-text availability identify the source. |
| membership | PMID:40140706; Fresh XML Sec3; Figure 1; Supplementary Table S1.2 rows 2–182, identifier/phylum/reference columns | supports | The model source comprises 181 MAGs across eight broad phyla: 97 Bacillota, 65 Bacteroidota and 19 MAGs across six other phyla. S1.2 subdivides Bacillota into A (80), B (1) and unsuffixed (16); the two encoded aggregates are not the complete roster. |
| cohorts | PMID:40140706; Fresh XML Sec3 and Sec10–Sec19; Supplementary Information community-modelling lines 118–144 | supports | The main study compares separate male age cohorts. The source does not demonstrate community equilibrium; 52 sampled mice, 50 feasible community-flux models and the separate female validation cohort have distinct scopes. |
| pairwise | PMID:40140706; Fresh XML Sec24; Sec6/Figure 4e; Supplementary Table S4.10 rows 12–19 | supports | Individual and paired modeled growth classify interactions. The commensal fraction declines and competitive fraction increases with age, while mutualism is not significantly age-associated in S4.10. |
| competition | PMID:40140706; Fresh XML Sec6 and Figure 4e; Supplementary Table S4.10 rows 14–19 | supports | Normalized frequencies shift toward the modeled competition category. Amensalism and neutralism are separate categories, and their decline does not mean loss of beneficial commensalism. |
| host-support | PMID:40140706; Fresh XML Sec5/Sec8/Sec27–Sec31; Figure 3; Supplementary Table S3.2 focal ATP/NAD/CoA/uridine/deoxycytidine/orotate/uracil rows | partial | The pooled metamodel predicts bidirectional host–microbiota nucleotide-related metabolism. The source treats intestinal barrier consequences as a hypothesis, despite broad colonization and literature validation. |
| proxy | PMID:40140706; Fresh XML Sec27–Sec29 | supports | Three human Recon 2.2 instances represent mouse colon, liver and brain; all bacterial reactions are pooled. Context-specific models and FVA ranges do not resolve every microbial donor or establish measured transfer. |
| conditions | PMID:40140706; Fresh XML Sec13, Sec22 and Sec27; Supplementary Tables S1.3–S1.11 | supports | Main-cohort housing is 22±2°C, 14:10-hour light/dark and 55±10% relative humidity. Model diet uses V1534-300 at assumed 3.5 g/day with human-cohort fibre imputation and pre-colonic absorption. These are different physical/model dimensions. |
| supplement | PMID:40140706; MOESM1 Supplementary Information lines 81–90 and 118–184; workbook-scope.json declared selections | supports | Community FBA uses abundance-linked biomass and coupling constraints, with two old-community infeasibilities leaving 50 models. S4.10 retains predicted pair classes; focal S3.2 includes nucleotides as well as nucleosides and precursors. |
| resources-source | PMID:40140706; Fresh XML Data availability and Code availability | supports | The source names BioModels, PRJEB73981, two GEO series, three MassIVE deposits, Zenodo 10844502 and the author code repository. These are different resources, not equivalent datasets. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity.taxonomy; EcologicalStateEnum.STABLE; ComputationalProvenance; environmental_factors | supports | Taxonomy represents microbial membership; STABLE denotes ecological equilibrium. FBA steady state, natural origin and repeated age-cohort sampling do not by themselves demonstrate that state. |
| ontology | kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; ontology-authority.json | supports | All nine pairs/11 occurrences match. Both taxa are phyla; GO growth includes organism/cell mass increase. Nucleotide is narrower than all nucleotide-pathway intermediates. |
| resources | kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; dataset-verification.json | supports | Focal model identity/structure and public project, GEO, MassIVE, Zenodo and immutable repository metadata are checked at stated scopes. No model or raw-data execution. |
| snippets | kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; snippet-audit.json | supports | All 12 excerpts match direct full XML and the pinned cache. |
| history | kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; provenance-audit.json | supports | Current linked issue states and prior graph repairs are preserved with their original source limits. |
| native-target | kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; support-audit.json | supports | Native metrics are mechanical measures, separate from the two major and two minor findings. |
| source-scope | PMID:40140706; source-audit.json | supports | Whole main and declared critical figure/table/model scopes were inspected. |
| independent-source | PMID:40140706; root-independent-source-audit.json | context_only | Independent whole-record/source review corroborates the bounded findings and supplementary analysis distinctions. |
| phylum-candidates | Local NCBITaxon OAK snapshot; omitted-phyla-grounding-candidates.json: exact names, ranks and synonym boundary | supports | Five omitted phyla have exact current labels. Desulfobacterota is a related synonym of Thermodesulfobacteriota NCBITaxon:200940; its circumscription requires review before any replacement. |
| search | Owned maintained roots; local-search.json: ignored-inclusive bounded discovery | supports | Local identity/reuse results apply only to the recorded roots. |
| adapter | Optional structured source adapter; adapter-check.json | supports | No applicable runnable adapter was established in recorded discovery. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; Actual execution 2026-10-21T12:16:21.696833+00:00 to 2026-10-21T12:16:22.771545+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-strict kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml --out /private/tmp/cm-review-session/batch-07/000011/strict-report.tsv; Actual execution 2026-10-21T12:16:21.697573+00:00 to 2026-10-21T12:16:24.927946+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-terms kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; Actual execution 2026-10-21T12:16:21.698021+00:00 to 2026-10-21T12:16:24.164350+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; Actual execution 2026-10-21T12:16:22.771855+00:00 to 2026-10-21T12:16:22.852303+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; Actual execution 2026-10-21T12:16:22.852674+00:00 to 2026-10-21T12:16:25.075507+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-history history/records/BioModels_MODEL2310020001_Mouse_Metaorganism_Model; Actual execution 2026-10-21T12:16:24.165115+00:00 to 2026-10-21T12:16:25.638491+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T12:16:25.641689+00:00 to 2026-10-21T12:16:25.876929+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml; Actual execution 2026-10-21T12:16:25.877690+00:00 to 2026-10-21T12:16:31.445546+00:00 | supports | Reference validation passed against pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T11:32:06.425768+00:00 to 2026-10-21T11:32:16.427975+00:00 | supports | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; target-native structure is COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T11:32:06.426382+00:00 to 2026-10-21T11:32:14.966232+00:00 | supports | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; target-native structure is COMPLETE. |

## Limits And Additional Notes

- The large supplementary workbook was inspected only at the declared table/row scope; no all-sheet audit, statistical recomputation or metabolic optimization was performed.
- Pairwise microbial growth classification, species-resolved community FBA and the pooled host–microbiome metamodel are distinct analyses. Flux ranges and ecological classes are predictions, not traced transfers or route-specific interventions.
- Main cohort 52 males, feasible community-flux subset 50, independent metabolomics cohort and 24-female germ-free validation are not interchangeable. Nominal figure sample sizes do not override analysis-specific feasibility/exclusion notes.
- BioModels metadata/listing and static XML were checked. ENA run metadata does not independently verify every MAG deposit; a bounded empty analysis response is not global absence. No accession or taxonomic identity was inferred from a reference genome alone.
- No automatic ecological-state replacement, novel organism role or new culture-medium identity was certified.
- Independent validation supports broad microbiome-dependent biology, not the necessity or causal sufficiency of a specific nucleotide route.
- No canonical, cache, history or generated files changed. All 23 repository inputs remain pinned.
- All quotations from the publication and supplements share one 25-word limit.
- Native quality 100 is capped from 111; scientific scope findings remain material.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T122316Z-mouse-metaorganism-model-record
kind: record
repository: CultureBotAI/CommunityMech
title: Mouse metaorganism model review
started_at: '2026-10-21T12:15:33.863705Z'
finished_at: '2026-10-21T12:23:16.900135Z'
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
summary: Three qualified computational nodes and no arrows remain supported. Two major
  findings address incomplete microbial roster scope and unsupported ecological stability;
  two minor findings address cohort/diet/model provenance and public resource organization.
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
  - path: history/records/BioModels_MODEL2310020001_Mouse_Metaorganism_Model/2026-10-05T124958Z-codex-9d96eb.yaml
    sha256: c2bc3d3724d239c5ce489db36add8ffec3e2bcb808046032d0d7f15791398501
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    sha256: a1cef55da6c4c9d5fd0ed26cc9d862595854b6525d47a2c6939fee84cb7bf841
    role: target
  - path: references_cache/PMID_40140706.txt
    sha256: b84507e91c4d37a6578cf649436a37f90063d747a974f521b13fccd446565ad5
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
- target_id: CommunityMech:000011
  path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  label: BioModels MODEL2310020001 Mouse Metaorganism Model
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    role: canonical_record
scope:
  description: Whole record, fresh primary main, declared figures and supplementary
    tables, and direct model/data authorities.
  selection: Only released CommunityMech:000011 after 000010 save and both mandatory
    gates.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000011
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000011
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
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
  - CommunityMech:000011
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-strict kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    --out /private/tmp/cm-review-session/batch-07/000011/strict-report.tsv
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
  - CommunityMech:000011
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-terms kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
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
  - CommunityMech:000011
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
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
  - CommunityMech:000011
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
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
  - CommunityMech:000011
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-history history/records/BioModels_MODEL2310020001_Mouse_Metaorganism_Model
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
  - CommunityMech:000011
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
  summary: Reference validation passed against pinned cache.
  target_ids:
  - CommunityMech:000011
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
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
  - CommunityMech:000011
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
  - CommunityMech:000011
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
  summary: Direct publication and model/project identities verified within explicit
    metadata/static-inspection scope.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - pubmed
  - resources
- check_id: scientific-source
  name: Whole-record scientific assessment
  status: passed
  required: true
  summary: Complete main and declared critical figure/supplement/model scopes inspected;
    no simulation executed.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - source-scope
  - independent-source
- check_id: cross-mech
  name: Medium and ingredient external links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech identifier is encoded. Modeled diet
    does not imply a microbial cultivation recipe.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - record
  - conditions
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No runnable applicable adapter was established in recorded discovery.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: 'Whole record: two phylum aggregates, three computational nodes and zero
    arrows'
  summary: The correct pooled metaorganism model is linked. Host tissues are kept
    outside microbial taxonomy, and graph descriptions separate computational association
    from causal mediation.
  support: supports
  accessed_at: '2026-10-21T12:21:04.571313Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=40140706&retmode=xml
  locator: Article-level metadata and abstract where supplied
  summary: PMID40140706, DOI and article title/abstract identify the focal study.
  support: supports
  accessed_at: '2026-10-21T12:16:11.972567Z'
  snapshot_sha256: dc27be36de05e9859133c3766160457f9f339909d55aa206fd19cbc4d1e8cda0
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1038/s41564-025-01959-z
  locator: Article-level metadata and abstract where supplied
  summary: DOI/title/authors verified as bibliographic metadata.
  support: supports
  accessed_at: '2026-10-21T12:16:21.858071Z'
  snapshot_sha256: eb07a6a261ab18d6147c10c4a4e5c72462011784a052bd5c74188afbbb20a256
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40140706&format=json&resultType=core
  locator: Article-level metadata and abstract where supplied
  summary: PMID40140706/PMC11964932 and direct full-text availability identify the
    source.
  support: supports
  accessed_at: '2026-10-21T12:16:12.351379Z'
  snapshot_sha256: cc3787a93ff64610c7ff9de06751cba4158f7abb36a78836690a9a0f31d84852
- evidence_id: membership
  kind: primary_source
  reference: PMID:40140706
  locator: Fresh XML Sec3; Figure 1; Supplementary Table S1.2 rows 2–182, identifier/phylum/reference
    columns
  summary: 'The model source comprises 181 MAGs across eight broad phyla: 97 Bacillota,
    65 Bacteroidota and 19 MAGs across six other phyla. S1.2 subdivides Bacillota
    into A (80), B (1) and unsuffixed (16); the two encoded aggregates are not the
    complete roster.'
  support: supports
  accessed_at: '2026-10-21T12:21:04.571957Z'
  snapshot_sha256: f721dc1cbf8a937ad31839dbfed84b608df25c8e115fb1f6371356517e04fdfc
- evidence_id: cohorts
  kind: primary_source
  reference: PMID:40140706
  locator: Fresh XML Sec3 and Sec10–Sec19; Supplementary Information community-modelling
    lines 118–144
  summary: The main study compares separate male age cohorts. The source does not
    demonstrate community equilibrium; 52 sampled mice, 50 feasible community-flux
    models and the separate female validation cohort have distinct scopes.
  support: supports
  accessed_at: '2026-10-21T12:21:04.572075Z'
  quote: separated into 5 age groups
  snapshot_sha256: f721dc1cbf8a937ad31839dbfed84b608df25c8e115fb1f6371356517e04fdfc
- evidence_id: pairwise
  kind: primary_source
  reference: PMID:40140706
  locator: Fresh XML Sec24; Sec6/Figure 4e; Supplementary Table S4.10 rows 12–19
  summary: Individual and paired modeled growth classify interactions. The commensal
    fraction declines and competitive fraction increases with age, while mutualism
    is not significantly age-associated in S4.10.
  support: supports
  accessed_at: '2026-10-21T12:21:04.572191Z'
  quote: single growth and community FBA
  snapshot_sha256: f721dc1cbf8a937ad31839dbfed84b608df25c8e115fb1f6371356517e04fdfc
- evidence_id: competition
  kind: primary_source
  reference: PMID:40140706
  locator: Fresh XML Sec6 and Figure 4e; Supplementary Table S4.10 rows 14–19
  summary: Normalized frequencies shift toward the modeled competition category. Amensalism
    and neutralism are separate categories, and their decline does not mean loss of
    beneficial commensalism.
  support: supports
  accessed_at: '2026-10-21T12:21:04.572303Z'
  quote: increased competitive interactions
  snapshot_sha256: f721dc1cbf8a937ad31839dbfed84b608df25c8e115fb1f6371356517e04fdfc
- evidence_id: host-support
  kind: primary_source
  reference: PMID:40140706
  locator: Fresh XML Sec5/Sec8/Sec27–Sec31; Figure 3; Supplementary Table S3.2 focal
    ATP/NAD/CoA/uridine/deoxycytidine/orotate/uracil rows
  summary: The pooled metamodel predicts bidirectional host–microbiota nucleotide-related
    metabolism. The source treats intestinal barrier consequences as a hypothesis,
    despite broad colonization and literature validation.
  support: partial
  accessed_at: '2026-10-21T12:21:04.572417Z'
  quote: could underlie
  snapshot_sha256: f721dc1cbf8a937ad31839dbfed84b608df25c8e115fb1f6371356517e04fdfc
- evidence_id: proxy
  kind: primary_source
  reference: PMID:40140706
  locator: Fresh XML Sec27–Sec29
  summary: Three human Recon 2.2 instances represent mouse colon, liver and brain;
    all bacterial reactions are pooled. Context-specific models and FVA ranges do
    not resolve every microbial donor or establish measured transfer.
  support: supports
  accessed_at: '2026-10-21T12:21:04.572531Z'
  quote: human metabolic reconstruction Recon 2.2
  snapshot_sha256: f721dc1cbf8a937ad31839dbfed84b608df25c8e115fb1f6371356517e04fdfc
- evidence_id: conditions
  kind: primary_source
  reference: PMID:40140706
  locator: Fresh XML Sec13, Sec22 and Sec27; Supplementary Tables S1.3–S1.11
  summary: Main-cohort housing is 22±2°C, 14:10-hour light/dark and 55±10% relative
    humidity. Model diet uses V1534-300 at assumed 3.5 g/day with human-cohort fibre
    imputation and pre-colonic absorption. These are different physical/model dimensions.
  support: supports
  accessed_at: '2026-10-21T12:21:04.572641Z'
  snapshot_sha256: f721dc1cbf8a937ad31839dbfed84b608df25c8e115fb1f6371356517e04fdfc
- evidence_id: supplement
  kind: primary_source
  reference: PMID:40140706
  locator: MOESM1 Supplementary Information lines 81–90 and 118–184; workbook-scope.json
    declared selections
  summary: Community FBA uses abundance-linked biomass and coupling constraints, with
    two old-community infeasibilities leaving 50 models. S4.10 retains predicted pair
    classes; focal S3.2 includes nucleotides as well as nucleosides and precursors.
  support: supports
  accessed_at: '2026-10-21T12:21:04.572676Z'
  snapshot_sha256: c850a1777c9042111006c4a8c933376af389efb6f7e798bc99d2708c8ddc9f29
- evidence_id: resources-source
  kind: primary_source
  reference: PMID:40140706
  locator: Fresh XML Data availability and Code availability
  summary: The source names BioModels, PRJEB73981, two GEO series, three MassIVE deposits,
    Zenodo 10844502 and the author code repository. These are different resources,
    not equivalent datasets.
  support: supports
  accessed_at: '2026-10-21T12:21:04.572868Z'
  snapshot_sha256: f721dc1cbf8a937ad31839dbfed84b608df25c8e115fb1f6371356517e04fdfc
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity.taxonomy; EcologicalStateEnum.STABLE; ComputationalProvenance;
    environmental_factors
  summary: Taxonomy represents microbial membership; STABLE denotes ecological equilibrium.
    FBA steady state, natural origin and repeated age-cohort sampling do not by themselves
    demonstrate that state.
  support: supports
  accessed_at: '2026-10-21T12:21:04.572946Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: ontology-authority.json
  summary: All nine pairs/11 occurrences match. Both taxa are phyla; GO growth includes
    organism/cell mass increase. Nucleotide is narrower than all nucleotide-pathway
    intermediates.
  support: supports
  accessed_at: '2026-10-21T12:21:04.573077Z'
  snapshot_sha256: 4944fee49ee156ddbe84078ec1fa7583dbc4ff34880f7dab78593f8ef2620609
- evidence_id: resources
  kind: database
  reference: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: dataset-verification.json
  summary: Focal model identity/structure and public project, GEO, MassIVE, Zenodo
    and immutable repository metadata are checked at stated scopes. No model or raw-data
    execution.
  support: supports
  accessed_at: '2026-10-21T12:21:04.573114Z'
  snapshot_sha256: 9668ca2d6df88811a71aa2cfac58e7c353a8b158e93efafc6f3037bad05005bd
- evidence_id: snippets
  kind: validation
  reference: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: snippet-audit.json
  summary: All 12 excerpts match direct full XML and the pinned cache.
  support: supports
  accessed_at: '2026-10-21T12:21:04.573260Z'
  snapshot_sha256: 5159fa4d0e62bf17dfb4ead97266fe4a7a8d13773c33163c5757fa379b86ead6
- evidence_id: history
  kind: record_content
  reference: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: provenance-audit.json
  summary: Current linked issue states and prior graph repairs are preserved with
    their original source limits.
  support: supports
  accessed_at: '2026-10-21T12:21:04.573410Z'
  snapshot_sha256: d4c3475defb3acf60e9c6856c3297cbbf82e4c313f64eb3f1e53b397d7567e03
- evidence_id: native-target
  kind: validation
  reference: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: support-audit.json
  summary: Native metrics are mechanical measures, separate from the two major and
    two minor findings.
  support: supports
  accessed_at: '2026-10-21T12:21:04.573560Z'
  snapshot_sha256: 8630b6526044cc988110970b7a441abf8d8ab828f0ef3ab18698430f4d47b710
- evidence_id: source-scope
  kind: validation
  reference: PMID:40140706
  locator: source-audit.json
  summary: Whole main and declared critical figure/table/model scopes were inspected.
  support: supports
  accessed_at: '2026-10-21T12:21:04.573601Z'
  snapshot_sha256: 07637ba6d4c5942388330e01b2f897e5910012f0d0ed2ee244389b812299a886
- evidence_id: independent-source
  kind: validation
  reference: PMID:40140706
  locator: root-independent-source-audit.json
  summary: Independent whole-record/source review corroborates the bounded findings
    and supplementary analysis distinctions.
  support: context_only
  accessed_at: '2026-10-21T12:21:04.573627Z'
  snapshot_sha256: 576dd87c59b8b173cdd0760f1005c821707453dc0475954805b48d10f9fe8b1a
- evidence_id: phylum-candidates
  kind: authority
  reference: Local NCBITaxon OAK snapshot
  locator: 'omitted-phyla-grounding-candidates.json: exact names, ranks and synonym
    boundary'
  summary: Five omitted phyla have exact current labels. Desulfobacterota is a related
    synonym of Thermodesulfobacteriota NCBITaxon:200940; its circumscription requires
    review before any replacement.
  support: supports
  accessed_at: '2026-10-21T12:21:04.573761Z'
  snapshot_sha256: bf91688a6e37e2164bb315edc936483f935ae9fac6153c6bb01a8db05ab50e0f
- evidence_id: search
  kind: search
  reference: Owned maintained roots
  locator: 'local-search.json: ignored-inclusive bounded discovery'
  summary: Local identity/reuse results apply only to the recorded roots.
  support: supports
  accessed_at: '2026-10-21T12:21:04.573881Z'
  snapshot_sha256: 6bae38b88aec72763e626020dc63cae5fa2e8e1874c5bcb5ea28ce2875f6c382
  search_scope: Ignored-inclusive maintained community, isolate and reusable-taxon
    roots and recorded mapping-file discovery.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: adapter-check.json
  summary: No applicable runnable adapter was established in recorded discovery.
  support: supports
  accessed_at: '2026-10-21T12:21:04.574014Z'
  snapshot_sha256: 2b46332df0c317299b4d40cbfc36b3eb1b6e99e0452d1b53fe75b66fcb272450
  search_scope: Recorded runtime and ignored-inclusive local discovery; no outside-checkout
    execution or paid provider.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: Actual execution 2026-10-21T12:16:21.696833+00:00 to 2026-10-21T12:16:22.771545+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T12:16:22.771545Z'
  snapshot_sha256: 5e14c7020485de07df9515a573f013d51008f05f45c1fe68db8697a792242ea0
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-strict kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    --out /private/tmp/cm-review-session/batch-07/000011/strict-report.tsv
  locator: Actual execution 2026-10-21T12:16:21.697573+00:00 to 2026-10-21T12:16:24.927946+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T12:16:24.927946Z'
  snapshot_sha256: 74bed65e0d1f36067e826569f120a32ae6b331764f3d905ef753eb1f069d7292
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-terms kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: Actual execution 2026-10-21T12:16:21.698021+00:00 to 2026-10-21T12:16:24.164350+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T12:16:24.164350Z'
  snapshot_sha256: 091b3d16015127f57291eadb6a320e07931e08beeb622d31d61e122184679c06
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: Actual execution 2026-10-21T12:16:22.771855+00:00 to 2026-10-21T12:16:22.852303+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T12:16:22.852303Z'
  snapshot_sha256: 798d60e265763458f0c88a7b0ee8a425af9658fb6a6d8067f230ff398c35c9fb
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb-domain kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: Actual execution 2026-10-21T12:16:22.852674+00:00 to 2026-10-21T12:16:25.075507+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T12:16:25.075507Z'
  snapshot_sha256: 1ebf72b65bdb689adb37596a0e65c3594bd35eefc4f62c92267f231be894b9c0
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-history history/records/BioModels_MODEL2310020001_Mouse_Metaorganism_Model
  locator: Actual execution 2026-10-21T12:16:24.165115+00:00 to 2026-10-21T12:16:25.638491+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T12:16:25.638491Z'
  snapshot_sha256: e14154ba1c22e19225397aef5fba836cb50f7d039da749e8cd69f616fa2040a1
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T12:16:25.641689+00:00 to 2026-10-21T12:16:25.876929+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T12:16:25.876929Z'
  snapshot_sha256: 11b415dcc3110730d4a6a4daf19bc929cf35e09cce5d454f901a0df8bea3f669
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-references-explained kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
  locator: Actual execution 2026-10-21T12:16:25.877690+00:00 to 2026-10-21T12:16:31.445546+00:00
  summary: Reference validation passed against pinned cache.
  support: supports
  accessed_at: '2026-10-21T12:16:31.445546Z'
  snapshot_sha256: abc76ce37a756831e960c5c4c4fb8a72b4b6be178044f3f858bc0a3f1b0ddd68
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
  topic: Natural source community and modeled representation
  outcome: concern
  summary: The model identity is correct, but taxonomy exposes only two of eight source
    phyla without declaring representative coverage.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - membership
  - proxy
  - resources
  - record
  dimensions:
  - name: community_scope
    value: 181 microbial MAGs and pooled host–microbiome metamodel
    definition: The source community spans eight broad phyla; the pooled model merges
      reactions rather than preserving species compartments.
    evidence_ids:
    - membership
    - proxy
  - name: source_strain
    value: Natural MAG collection; male C57BL/6J/Ukj source hosts
    definition: MAG identifiers and quality/reference mappings are in S1.2. Host strain
      is context, not microbial taxonomy; female C57BL/6J validation is separate.
    evidence_ids:
    - membership
    - cohorts
  - name: environment
    value: Laboratory-host housing and modeled intestine
    definition: The two existing environment terms are compatible when physical housing
      and modeled habitat remain distinct.
    evidence_ids:
    - conditions
    - ontology
  - name: medium
    value: Reconstructed dietary inputs, not a bench culture medium
    definition: V1534-300, assumed intake, imputed fibre and absorption determine
      modeled availability. Do not turn this into a microbial culture recipe.
    evidence_ids:
    - conditions
  - name: experimental_setting
    value: Cross-sectional multi-omics cohorts and separate computational analyses
    definition: 52 main mice, 50 feasible community-flux cases, 52 context metamodels
      and 24-female validation are method-specific groups.
    evidence_ids:
    - cohorts
    - supplement
    - proxy
  - name: evidence_tier
    value: Omics/colonization associations and computational predictions
    definition: Pairwise growth classes and host flux dependencies are not causal
      ecological or donor-tracer experiments.
    evidence_ids:
    - pairwise
    - host-support
  - name: grounding_status
    value: Valid phylum terms and broad GO/CHEBI grounding
    definition: Global GTDB crosswalk proportions do not establish the cohort-specific
      MAG assignments or completeness of the two-entry roster.
    evidence_ids:
    - ontology
    - membership
- assessment_id: state
  area: evidence
  topic: Ecological state and origin
  outcome: concern
  summary: NATURAL origin is supported; STABLE equilibrium is not established.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - cohorts
  - schema
  details: Aging-associated composition, interaction and metabolic shifts are compared
    across separate cohorts. Computational steady-state constraints or stable reconstruction
    clusters are not evidence of ecological equilibrium. The state field is optional
    in the schema but contributes to the native completeness score. Omit unsupported
    state or qualify its representation without automatically substituting ENGINEERED
    or TRANSIENT.
- assessment_id: taxa
  area: grounding
  topic: Taxa, roles and abundance
  outcome: concern
  summary: The two aggregates are valid but incomplete for the whole modeled microbial
    source.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - membership
  - ontology
  details: Keep host tissues excluded. Add explicit representative scope or recover
    the remaining source phyla with verified grounding. Do not invent generic phylum
    functions to improve completeness. No numerical abundance field is encoded; global
    GTDB support counts are mapping statistics, not cohort abundance.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: beneficial interaction predictions'
  outcome: supported
  summary: Retain community-level comparison of single and paired microbial growth
    across age cohorts.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - pairwise
  - supplement
  details: Participants are the modeled bacterial MAG pairs, not merely the two displayed
    phylum aggregates. Source comparisons support reduced commensal/beneficial interaction
    frequency but not universal decline of every positive category; mutualism is unchanged
    in S4.10. No loss-to-metabolite causal arrow is established.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: competitive interaction shift'
  outcome: supported
  summary: Retain community-level COMPETITION as a predicted paired-growth category.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - competition
  - pairwise
  details: The normalized frequency rises with age while amensal, commensal and neutral
    categories decline. This does not demonstrate longitudinal competitive exclusion
    or mediation of all concurrent metabolite shifts; the existing wording preserves
    those limits.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: host nucleotide support'
  outcome: supported
  summary: Retain pooled microbial ↔ host-colon/liver/brain metabolic predictions
    with PARTIAL barrier interpretation.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - host-support
  - proxy
  - supplement
  details: The direction is reciprocal and metabolite-specific, not blanket commensalism.
    Predicted ATP/NAD/CoA and other nucleotide-related routes support the pathway
    scope; nucleosides/precursors must not all be relabeled as nucleotides. Broad
    germ-free/colonization validation and literature support do not establish donor-specific
    flux or route-specific rescue.
- assessment_id: arrows
  area: graph
  topic: Downstream causal scope
  outcome: supported
  summary: Preserve zero downstream arrows between the three qualified nodes.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - record
  - pairwise
  - host-support
  details: Species-pair ecological classification and pooled host-metabolism analysis
    are separate. Their aging association does not establish a directed causal chain
    through competition to host barrier dysfunction.
- assessment_id: conditions
  area: completeness
  topic: Host conditions and computational provenance
  outcome: concern
  summary: Housing, model diet, reconstruction proxy and analysis-specific settings
    are source-resolvable but largely unstructured.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - conditions
  - proxy
  - supplement
  - schema
  details: Add housing as host context and diet/absorption/FBA/FVA settings as computational
    provenance. Empty growth_media is appropriate; no culturing protocol is implied.
    Preserve physical cohort, model feasibility and validation differences.
- assessment_id: chemistry
  area: grounding
  topic: Nucleotide, succinate and butyrate scope
  outcome: supported
  summary: Current broad chemical terms support the stated qualified pathway outputs.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - host-support
  - ontology
  - supplement
  details: S3.2 contains genuine nucleotide/cofactor exchanges alongside nucleosides
    and precursors. Keep this chemical distinction if adding specific mediators. Succinate/butyrate
    age associations are predicted metabolism with supporting omics context, not a
    measured causal route to host aging.
- assessment_id: resources
  area: provenance
  topic: Model and dataset organization
  outcome: concern
  summary: The BioModels file and ENA project are traceable; the primary paper is
    not itself a dataset and additional direct source resources can be linked.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - resources-source
  - resources
  details: Keep separate metagenomic, transcriptomic, metabolomic and reconstructed-model/code
    scopes. Archive metadata do not certify all MAG sequence deposits, every raw payload
    or equivalence of artifact versions.
- assessment_id: history
  area: provenance
  topic: Prior repair and snippet support
  outcome: supported
  summary: All 12 excerpts match direct source text; the earlier three-node/no-arrow
    repair remains appropriate.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - snippets
  - history
  - record
  details: Old unread figure/SI/model limits describe the earlier review, not this
    assessment. Current source comparison independently preserves its caution about
    human reconstruction proxies, separate cohorts and unproven mediation.
- assessment_id: validation
  area: schema
  topic: Native checks
  outcome: supported
  summary: All eight native checks pass; semantic findings remain.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
- assessment_id: metrics
  area: completeness
  topic: Mechanical metrics
  outcome: supported
  summary: Capped quality does not negate two major and two minor findings.
  target_ids:
  - CommunityMech:000011
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 30
    unit: points
    minimum: 0
    maximum: 100
    definition: 0 required-role component +5 environment +10 three nodes +5 resources
      +5 datasets +5 metabolites. No arbitrary roles are invented to increase this
      score.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0,P2=2,P3=2,P4=0; 6/3 mean evidence gives20 bonus, network15:111 before capping.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 2
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
- finding_id: membership-scope
  issue_key: cm-000011-membership-scope
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2: material membership coverage mismatch for the modeled
    community; the two encoded labels remain valid.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Resolve incomplete microbial roster coverage
  description: The whole metamodel includes 181 MAGs across eight broad phyla, while
    taxonomy exposes only Bacillota and Bacteroidota without declaring partial coverage.
    Six phyla and 19 MAGs are omitted from the represented membership.
  target_ids:
  - CommunityMech:000011
  field_paths:
  - taxonomy
  - description
  evidence_ids:
  - membership
  - proxy
  - ontology
  - phylum-candidates
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    role: canonical_record
- finding_id: stable-state
  issue_key: cm-000011-stable-state
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: an unqualified community-level state assertion conflicts
    with the evidentiary scope; natural origin and model identity remain valid.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Qualify the unsupported ecological equilibrium designation
  description: STABLE asserts equilibrium, which is not demonstrated by separate age
    cohorts or steady-state metabolic optimization. The source instead describes substantial
    age-associated ecological and functional shifts.
  target_ids:
  - CommunityMech:000011
  field_paths:
  - ecological_state
  evidence_ids:
  - cohorts
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    role: canonical_record
- finding_id: computational-context
  issue_key: cm-000011-computational-context
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: recoverable context and reproducibility metadata; existing
    graph qualifications prevent a major causal overstatement.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Structure cohort, diet and simulation context
  description: The record has useful prose cautions but lacks structured host conditions
    and computational provenance needed to distinguish its separate analyses.
  target_ids:
  - CommunityMech:000011
  field_paths:
  - environmental_factors
  - ecological_interactions[0].evidence
  - ecological_interactions[1].evidence
  - ecological_interactions[2].evidence
  evidence_ids:
  - conditions
  - proxy
  - supplement
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    role: canonical_record
- finding_id: resource-types
  issue_key: cm-000011-resource-types
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded resource organization and completeness, not a
    failure of the correct BioModels/ENA identity.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Clarify publication and public data resource roles
  description: The primary publication is listed as a dataset, while directly reported
    transcriptomic, metabolomic and model/code resources are not represented.
  target_ids:
  - CommunityMech:000011
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - resources-source
  - resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    role: canonical_record
actions:
- action_id: repair-membership-scope
  description: Resolve incomplete microbial roster coverage.
  finding_ids:
  - membership-scope
  target_ids:
  - CommunityMech:000011
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    role: canonical_record
  acceptance_checks:
  - Either complete the source-supported phylum roster or explicitly declare the taxonomy
    as a representative subset and link the complete S1.2 roster. Do not imply the
    two aggregates are the entire microbiome.
  - 'Preserve the other source groups: 9 Pseudomonadota, 4 Cyanobacteriota, 3 Campylobacterota,
    1 Deferribacterota, 1 Desulfobacterota and 1 Verrucomicrobiota. Use verified candidates
    where appropriate; do not automatically replace source Desulfobacterota with the
    current Thermodesulfobacteriota label solely from a related synonym.'
  - Distinguish source GTDB Bacillota_A (80), Bacillota_B (1) and unsuffixed Bacillota
    (16) from the global crosswalk majority attached to NCBI Bacillota. Do not infer
    cohort assignments from global mapping fractions.
  - Keep host tissues outside microbial taxonomy and preserve the pooled model versus
    species-resolved pairwise analysis distinction. Do not invent phylum roles.
- action_id: repair-stable-state
  description: Qualify the unsupported ecological equilibrium designation.
  finding_ids:
  - stable-state
  target_ids:
  - CommunityMech:000011
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    role: canonical_record
  acceptance_checks:
  - Provide source-specific ecological equilibrium evidence or revise the state representation
    with explicit uncertainty and rationale.
  - The schema makes ecological_state optional; its inclusion in the native completeness
    rubric does not make it mandatory. Omit unsupported state or retain only a source-justified
    representation; do not automatically substitute ENGINEERED/TRANSIENT.
  - Retain NATURAL source origin and distinguish model steady-state assumptions from
    measured community stability.
- action_id: repair-computational-context
  description: Structure cohort, diet and simulation context.
  finding_ids:
  - computational-context
  target_ids:
  - CommunityMech:000011
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    role: canonical_record
  acceptance_checks:
  - Record main-cohort housing and host strain/sex/age context separately from female
    germ-free validation and metabolomics cohorts. Do not describe the study as longitudinal
    tracking of the same mice.
  - Populate computational_provenance with reconstructed V1534-300 diet, assumed 3.5
    g/day intake, human-cohort fibre imputation and pre-colonic absorption; keep these
    assumptions distinct from measured feed consumption or a bench growth medium.
  - Separate species-resolved FBA/pair classification from pooled Recon 2.2 host metamodel/FVA/EFM
    analysis, with source-specific tools, constraints and thresholds. Preserve 50
    feasible community-flux cases versus 52 sampled/context-model mice.
  - Preserve the three qualified nodes and no arrows; no route-specific nucleotide
    rescue or causal competition-to-host chain is established.
- action_id: repair-resource-types
  description: Clarify publication and public data resource roles.
  finding_ids:
  - resource-types
  target_ids:
  - CommunityMech:000011
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2310020001_Mouse_Metaorganism_Model.yaml
    role: canonical_record
  acceptance_checks:
  - Move PMID40140706 to publication evidence/resources rather than treating it as
    a scientific dataset.
  - Link verified GSE262290/GSE278548, MSV000094409/MSV000094410/MSV000094436, Zenodo10844502
    and immutable author code with their source-defined data types and cohort scopes.
  - Retain MODEL2310020001/metamodel_20230510.xml and PRJEB73981; distinguish the
    article-reported MAG deposit from what the inspected archive endpoints independently
    confirm.
  - Preserve archive format/version discrepancies and static-inspection limits. Do
    not claim raw-data inspection, per-MAG revalidation or simulation reproduction.
limitations:
- The large supplementary workbook was inspected only at the declared table/row scope;
  no all-sheet audit, statistical recomputation or metabolic optimization was performed.
- Pairwise microbial growth classification, species-resolved community FBA and the
  pooled host–microbiome metamodel are distinct analyses. Flux ranges and ecological
  classes are predictions, not traced transfers or route-specific interventions.
- Main cohort 52 males, feasible community-flux subset 50, independent metabolomics
  cohort and 24-female germ-free validation are not interchangeable. Nominal figure
  sample sizes do not override analysis-specific feasibility/exclusion notes.
- BioModels metadata/listing and static XML were checked. ENA run metadata does not
  independently verify every MAG deposit; a bounded empty analysis response is not
  global absence. No accession or taxonomic identity was inferred from a reference
  genome alone.
- No automatic ecological-state replacement, novel organism role or new culture-medium
  identity was certified.
- Independent validation supports broad microbiome-dependent biology, not the necessity
  or causal sufficiency of a specific nucleotide route.
notes:
- No canonical, cache, history or generated files changed. All 23 repository inputs
  remain pinned.
- All quotations from the publication and supplements share one 25-word limit.
- Native quality 100 is capped from 111; scientific scope findings remain material.
tags:
- record-review
- mouse-metaorganism
- metabolic-model
- batch-07
```
