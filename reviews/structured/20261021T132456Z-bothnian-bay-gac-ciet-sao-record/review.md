# Bothnian Bay GAC-dependent CIET-SAO consortium record review

- Review: 20261021T132456Z-bothnian-bay-gac-ciet-sao-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T13:16:13.963914Z
- Finished UTC: 2026-10-21T13:24:56.222801Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-source review retains three qualified interaction nodes and no arrows. One major finding resolves the exact core MAG beyond domain-level Bacteria; two minor findings separate cultivation phases and preserve residual Methanosarcina in non-graph wording. Source presentation discrepancies and genomic inference limits remain explicit.

## Scope And Provenance

Entire record and all three nodes assessed against full primary science, critical figures/supplements, current taxon/archive authorities, history and native checks.

Selection: Only released CommunityMech:000349 in the owned batch08 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000349 | kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml | maintained | Bothnian Bay GAC-Dependent CIET-SAO Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000349 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000349 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000349 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000349 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000349 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000349 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000349 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000349 | Reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000349 | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000349 | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |
| Primary source identity and excerpts | passed | True | CommunityMech:000349 | Exact DOI/PMID/PMCID agree and all 24 snippets match directly retrieved full XML. |
| Whole source and critical supplementary assessment | passed | True | CommunityMech:000349 | Entire main, all main figures and critical supplementary/read scopes assessed with explicit annotation and precursor-study limits. |
| Project, exact core MAGs and comparator scope | passed | True | CommunityMech:000349 | Exact source-linked project and five BioSamples verified through bounded metadata; no raw-data analysis. |
| Exact modified-medium correspondence | not_applicable | False | CommunityMech:000349 | No exact modified-medium identifier established; no guessed CultureMech or ingredient link. |
| Optional structured source adapter | unavailable | False | CommunityMech:000349 | Same-runtime fresh batch08 discovery explicitly reused; no runnable adapter established or external checkout executed. |

## Scientific And Domain Assessments

### Enrichment identity and physical context

identity: supported. Targets: CommunityMech:000349.

Retain the natural sediment origin, sediment-free enrichment environment and GAC-mediated CIET scope. The five taxa are selected core/auxiliary members, not an exhaustive MAG inventory.

### taxonomy[0] and ecological_interactions[0].source_taxon

grounding: concern. Targets: CommunityMech:000349.

Replace domain-only Bacteria grounding for the exact GAC.MBAT.93 participant with the verified species authority and reassess its GTDB status.

Local canonical label is Candidatus Geosyntrophus acetoxidans; live archive nomenclature is Geosyntrophus acetoxidans (SeqCode). Preserve that version distinction and the exact MAG label. Current Methanosarcina genus remains defensible; do not force a named species or incomplete printed GTDB identifier.

### Five taxon roles and abundance fields

evidence: supported. Targets: CommunityMech:000349.

Retain experimental core electron-transfer roles and explicitly inferred auxiliary alternatives. DOMINANT does not mean more than half of all reads.

9.4% and 12% are focal metagenomic read shares. Lentimicrobium EET versus fermentative recycling and Sedimentibacter/Desulforhopalus secondary roles remain source hypotheses. Do not claim all capacities operate simultaneously. The 6.5%/6.4% Sedimentibacter variation is an upstream source discrepancy, not a silently repaired value.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000349.

Retain GAC-dependent acetate oxidation coupled to methane production with the current residual-population and molecular limits; correct its source taxon grounding.

The record combines enrichment physiology, genomics and explicitly attributed precursor work. GAC dependence is not reduced to gene presence alone; specific PCC/MmcA/pilus routes were not independently isolated in these MAGs. Residual Methanosarcina is already correctly acknowledged here.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000349.

Retain the PARTIAL COMPUTATIONAL Lentimicrobium interaction as alternative EET-linked acetate oxidation or fermentative recycling.

Genomic transport, metabolism and cytochrome capacity supports the proposed route, not measured species-resolved transfer or compulsory use of one pathway.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000349.

Retain the PARTIAL community-level biomass-turnover hypothesis for the three auxiliary genera.

This is inferred recycling of biomass-derived organic matter; the current record does not establish the exact donor, metabolite flux or requirement of each auxiliary lineage.

### All downstream fields

graph: supported. Targets: CommunityMech:000349.

There are no downstream arrows. No new causal edge is required to connect genomic capacities and community endpoints.

### Ecological state, origin and category

scope: supported. Targets: CommunityMech:000349.

Retain NATURAL source origin and DIET with explicit conductive-particle mediation; read STABLE within maintained GAC enrichment conditions.

The source reports long-term persistence of the core partnership under GAC cultivation. This does not assert equilibrium of unperturbed sediment or invariant abundance of every member. Serial enrichment alone does not require changing community_origin from NATURAL to ENGINEERED; ecological_state is a separate optional field.

### growth_media[0] and cultivation_setup[0]

representation: concern. Targets: CommunityMech:000349.

The medium, anaerobic handling, temperature, light and GAC concentration are supported; the single setup merges initial liquid volume with later vessel capacity.

Scope 50 mL working liquid to the initial 100 mL bottles. Later 50 mL glass-vial capacity does not establish 50 mL fill. Preserve Methods 22 transfers versus Results 30 GAC-free transfers as unresolved reporting context.

### environmental_factors[0]

evidence: concern. Targets: CommunityMech:000349.

The factor correctly identifies GAC dependence, but categorical loss of both core MAGs contradicts residual Methanosarcina and the qualified node.

Align description and nearby interpretation with depletion/poor detection; do not infer extinction, absolute absence or viability from relative metagenomic abundance.

### Dataset, publication, metal fields and history

provenance: supported. Targets: CommunityMech:000349.

The encoded BioProject and publication are correct, comparator P39 is distinguished, and no metal-cycling claim is made merely because GAC conducts electrons.

Core sample/assembly identifiers can support the taxonomy correction. Current inventory counts are metadata scope, not verification of all analyses. Preserve the prior graph repair and open non-graph follow-up; no exact modified-medium CultureMech link is established.

### Native checks and ontology labels

schema: supported. Targets: CommunityMech:000349.

All eight native checks and 11 current ID/label pairs pass. The exact species grounding finding concerns resolution, not a mislabeled Bacteria identifier.

### Native mechanical scores

completeness: supported. Targets: CommunityMech:000349.

Scores measure structural completeness and native checks, separately from the three scientific findings.

## Findings

### core-species-grounding: Ground the exact core MAG beyond the bacterial domain

major / open / confirmed; issue key: cm-000349-core-species-grounding.

The named GAC.MBAT.93 partner remains NCBITaxon:2/Bacteria in membership and the core node, with a domain-level GTDB aggregate. Its exact BioSample/assembly now resolves to NCBITaxon:3714907 and the local species authority. This loses material participant resolution despite a valid Bacteria label.

### phase-specific-cultivation: Separate initial culture volume from subsequent vial capacity

minor / open / confirmed; issue key: cm-000349-phase-specific-cultivation.

cultivation_setup[0] combines initial serum bottles and later vials but assigns 50 mL working volume without phase scope. Only the initial 100 mL bottle explicitly contains 50 mL culture; later vials have 50 mL vessel capacity. Existing discussion also flags unresolved transfer counts.

### residual-methanosarcina: Retain residual Methanosarcina in the non-graph control description

minor / open / confirmed; issue key: cm-000349-residual-methanosarcina.

environmental_factors[0].description says the controls lost both key MAGs, although the source reports approximately 0.06% Methanosarcina and ecological_interactions[0] already preserves this limit.

## Recommended Actions And Acceptance Checks

### ground-core-mag

Update the exact Geosyntrophus MAG consistently and re-ground its GTDB representation.

- Use NCBITaxon:3714907 with the pinned canonical label Candidatus Geosyntrophus acetoxidans in taxonomy[0].taxon_term.term and ecological_interactions[0].source_taxon.term; preserve GAC.MBAT.93 and cite SAMN54926496/GCA_057407595.1.
- Document the live SeqCode name versus local canonical-label version. Re-run GTDB grounding against the corrected NCBI identifier; replace stale NCBITaxon:2/domain aggregate metadata or retain an explicit unresolved status if no supported specific mapping is available. Do not assert JACRCG01 correspondence from a placeholder alone.
- Keep Methanosarcina at its justified genus and preserve all five focal memberships, three qualified nodes and zero arrows. Run schema, strict, terms, GTDB/domain, reference and history checks after separately authorized curation.

### scope-cultivation

Represent the initial and later cultivation phases separately or scope each reported value explicitly.

- Limit 50 mL liquid/50 mL headspace to the initial 100 mL serum bottle. Record later 50 mL glass vials as vessel capacity with unspecified fill; do not infer their headspace or working volume.
- Preserve supported 10% or 20% inoculum, 10 mM acetate, 10 g/L GAC, static dark 22 °C and anaerobic handling with their source context; do not invent a full DSMZ modified-120 recipe.
- Record the Methods 22 transfers/nine years versus Results 30 GAC-free transfers discrepancy without silently choosing one count. Keep earlier graph-only history intact and validate any separately authorized correction.

### qualify-control-populations

Align the environmental-factor interpretation with the measured residual population and existing node.

- Describe severe depletion or poor detection and near inactivity in particle-free transfers; explicitly retain residual Methanosarcina near 0.06%. Do not claim both populations disappeared.
- Keep any exact source quotation unchanged, but qualify its interpretation with the quantitative result. Relative read abundance does not establish extinction or viability.
- Preserve the GAC-dependence endpoint and the molecular/auxiliary hypotheses; no new node or causal arrow is warranted.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml; Entire canonical record | supports | Five focal taxa, three interaction nodes and no downstream arrows describe the long-term sediment-derived GAC enrichment; two non-graph fields retain stronger or less scoped wording than the graph. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=41876513&amp;retmode=xml; Article-level bibliographic metadata | supports | PMID 41876513, DOI 10.1038/s41467-026-70468-2 and PMC13013709 identify the same primary article. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41876513%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article-level bibliographic metadata | supports | PMID 41876513, DOI 10.1038/s41467-026-70468-2 and PMC13013709 identify the same primary article. |
| crossref | https://api.crossref.org/works/10.1038/s41467-026-70468-2; Article-level bibliographic metadata | supports | PMID 41876513, DOI 10.1038/s41467-026-70468-2 and PMC13013709 identify the same primary article. |
| core | PMID:41876513; Results and Discussion: GAC-dependent activity, core MAGs; Figures 1 and 2 captions | supports | Acetate oxidation and methane formation persist in GAC cultures; particle-free cultures are nearly inactive. The source assigns the proposed core route to GAC.MBAT.93 and GAC.MBAT.2 using physiology and genomic evidence. |
| residual | PMID:41876513; Results and Discussion: particle-free population comparison | supports | Methanosarcina remains detectable at approximately 0.06%; this contradicts categorical loss of both core MAGs, while preserving severe depletion and low activity. |
| auxiliary | PMID:41876513; Results and Discussion: Lentimicrobium and auxiliary lineages | supports | Lentimicrobium EET-linked acetate oxidation and fermentative recycling are alternatives; Sedimentibacter and Desulforhopalus detrital recycling remains inferred. |
| cultivation | PMID:41876513; Methods: Cultivation | supports | Initial inoculations used 100 mL bottles containing 50 mL culture and 50 mL headspace. Subsequent transfers used 50 mL glass vials without a separately specified liquid fill. The source also gives 10% or 20% inoculum, modified DSMZ 120, 10 mM acetate, 10 g/L GAC, anaerobic gas handling, dark/static 22 °C conditions. |
| transfer-conflict | PMID:41876513; Methods: Cultivation; Results and Discussion: GAC-free propagation | supports | Methods reports 22 transfers in nine years; Results reports 30 successive transfers without GAC. Preserve the source discrepancy rather than selecting one unqualified count. |
| datasets-main | PMID:41876513; Data availability | supports | The source identifies PRJNA1140524 and exact community, core-MAG and comparator BioSamples; P39 is a separately sequenced comparison organism, not an enrichment member. |
| figures | PMID:41876513; Figures 1–5; valid asset-manifest.json paths | supports | All five main images support the experimental/genomic distinction. Figure 2 supplies focal read shares. Figures 3–5 provide proposed pathways and comparative genomic context, not molecular perturbation assays. |
| supplement | PMID:41876513; Supplementary Figures S1–S11 captions; inspected S3–S5 and S7–S11 images | supports | Supplemental abundance and comparative sequence displays refine the source interpretation without measuring species-resolved exchanged fluxes. S3 gives Sedimentibacter 6.4%, differing from main/Figure 2 6.5%. |
| workbook | PMID:41876513; Supplementary Tables S1–S3: headers and focal rows recorded in workbook-focal-read.json | supports | Selected acetate-metabolism, PilA/cytochrome and Rnf/Fpo annotations support proposed genetic capacities, not direct pathway activity or necessity. |
| source-data | PMID:41876513; Source Data PDF: all five pages | supports | Inspected the reported time-course means/variation, multiheme comparisons and homology data without recomputation or raw-data reanalysis. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity; CultivationSetup; InteractionTypeEnum; FunctionalRoleEnum; AbundanceEnum; EcologicalStateEnum | supports | DIET does not impose a cell-contact-only rule. SYNTROPHY does not require obligacy. Abundance is ordinal; ecological_state is optional. Working volume denotes culture liquid, not vessel capacity. |
| ontology | ontology-authority.json; Whole bounded receipt | supports | All 11 encoded ontology pairs across 21 occurrences match canonical labels; a valid broad label does not establish adequate participant resolution. |
| candidate-taxonomy | taxon-grounding-candidates.json; Whole bounded receipt | supports | NCBITaxon:3714907 is locally Candidatus Geosyntrophus acetoxidans, species rank, parent 3714906. Methanosarcina sp. 2213 is a placeholder under genus 2207, not a named-species requirement. |
| resources | dataset-verification.json; Whole bounded receipt | supports | Exact GAC.MBAT.93 links SAMN54926496/GCA_057407595.1 to taxid 3714907. GAC.MBAT.2 links SAMN54926476 to GCA/GCF_057408005.1. The bounded inventory has 24 GAC, 30 Control and one P39 records; no raw sequences were read. |
| snippets | snippet-audit.json; Whole bounded receipt | supports | All 24 encoded excerpts match the directly retrieved complete XML and pinned cache; two also match the abstract. |
| history | provenance-audit.json; Whole bounded receipt | supports | Both histories and exact prior decision were read. Issue 1264 is closed after graph repair; issue 1268 remains open for non-graph follow-up. Its recent same-batch retrieval is explicitly reused. |
| native-target | support-audit.json; Whole bounded receipt | supports | Native completeness is 90 and network status COMPLETE. Final P1/P2/P3/P4 counts are 0/1/2/0; quality is capped at 100 from 117.6666666667. |
| support-manifest | supporting-artifact-manifest.json; Whole bounded receipt | supports | Frozen supporting artifact hashes preserve direct-source, current issue, archive and input-integrity boundaries. |
| source-scope | source-audit.json; Whole bounded receipt | supports | Whole main and critical supplemental/figure scopes support a completed assessment, with explicit uninspected assets and no raw-data reanalysis. |
| independent-source | root-independent-source-audit.json; Whole bounded receipt | supports | Root independently concurs with one major and two minor findings and retention of the qualified graph. |
| independent-authority | root-ontology-dataset-confirmation.json; Whole bounded receipt | supports | Root independently confirms current taxonomy authority, exact archive linkage, semantic boundaries and native checks. |
| local-search | Maintained corpus and mappings; local-search.json; local-search-interpretation.json | supports | Ignored-inclusive bounded searches found no focal reusable taxon match. A broad Bacteria substring hit and a comparator citation are explicitly excluded as false identity matches. |
| adapter | Optional structured source adapter; adapter-check.json | supports | Explicit same-runtime reuse of fresh batch08 discovery found no runnable adapter in the task environment; no external checkout was executed. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml; Actual execution 2026-10-21T13:17:10.806030+00:00 to 2026-10-21T13:17:12.812149+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-strict kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml --out /private/tmp/cm-review-session/batch-08/000349/strict-report.tsv; Actual execution 2026-10-21T13:17:10.810119+00:00 to 2026-10-21T13:17:16.568915+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-terms kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml; Actual execution 2026-10-21T13:17:10.812976+00:00 to 2026-10-21T13:17:15.114026+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml; Actual execution 2026-10-21T13:17:12.813061+00:00 to 2026-10-21T13:17:12.956965+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb-domain kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml; Actual execution 2026-10-21T13:17:12.957364+00:00 to 2026-10-21T13:17:16.770616+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-history history/records/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium; Actual execution 2026-10-21T13:17:15.114575+00:00 to 2026-10-21T13:17:17.081496+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T13:17:17.083859+00:00 to 2026-10-21T13:17:17.223829+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-references-explained kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml; Actual execution 2026-10-21T13:17:17.224241+00:00 to 2026-10-21T13:17:20.666921+00:00 | supports | Reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00 | supports | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00 | supports | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |

## Limits And Additional Notes

- No raw-read reanalysis, biochemical validation, experimental rerun, proteome reannotation or independent reread of precursor physiological papers. Current-paper summaries of earlier isotope/inhibitor/NanoSIMS work retain that attribution.
- Specific EET proteins and auxiliary recycling routes remain genomic hypotheses. Read shares are not cell counts, viability or absolute extinction measurements.
- Methods reports 22 transfers over nine years; Results reports 30 successive GAC-free transfers. Initial bottle and later vial configurations must remain distinct.
- Main/Figure 2 gives Sedimentibacter 6.5%, whereas later prose/S3 gives 6.4%. The 24 GAC MAG statement and archive inventory are not silently equated with the different Figure 2 Venn and S3 caption counts.
- The initial figure/supplement URL attempts returned HTML errors and remain preserved. Valid assets were subsequently recovered from the directly fetched EPMC ZIP into assets/. Reporting-summary content and peer-review file were not reviewed.
- Local canonical Candidatus Geosyntrophus acetoxidans and live archive Geosyntrophus acetoxidans (SeqCode) are authority-version labels for the verified taxid; no forced Methanosarcina named species or exact GTDB placeholder mapping.
- No canonical, cache, history, generated or saved-review file changed; all 24 official input pins remain intact.
- All 24 evidence occurrences match direct full XML and the pinned cache. Critical source scopes are complete for the assessed claims, not a whole-omics reanalysis.
- Native completeness 90 and quality 100/raw 117.6667 do not erase the one major and two minor findings.
- NATURAL origin, GAC-conditioned stability, explicit CIET route, core experimental evidence and PARTIAL auxiliary hypotheses are retained.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T132456Z-bothnian-bay-gac-ciet-sao-record
kind: record
repository: CultureBotAI/CommunityMech
title: Bothnian Bay GAC-dependent CIET-SAO consortium record review
started_at: '2026-10-21T13:16:13.963914Z'
finished_at: '2026-10-21T13:24:56.222801Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, native/ontology checks
    and supporting provenance; no person-level independence asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole-source review retains three qualified interaction nodes and no arrows.
  One major finding resolves the exact core MAG beyond domain-level Bacteria; two
  minor findings separate cultivation phases and preserve residual Methanosarcina
  in non-graph wording. Source presentation discrepancies and genomic inference limits
  remain explicit.
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
  - path: history/records/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium/2026-09-11T164213Z-codex-418765.yaml
    sha256: e4f3510bf35727a6ae4bf79aef4b4bf15859432a890a740f4bdcd34cba3981ef
    role: context
  - path: history/records/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium/2026-10-05T142559Z-codex-bb27ab.yaml
    sha256: 94a149e4cb3bfced2b4b37c04eda2f447515f28da5d8c195f7d91c1a45c6315d
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
    sha256: 1f5a47edf08cf2ef71d33f42caaa341929e6900422787e13dea0c61c1f0b1453
    role: target
  - path: references_cache/PMID_41876513.txt
    sha256: a505eb5947488ad1903638447461880f6397685e6517ee1c741267f555892e81
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch8.yaml
    sha256: a03eceb4ca205fdd9092a4f18c0fa4c068e8ec91ee5a62d09da97b87a4f50a25
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
- target_id: CommunityMech:000349
  path: kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  label: Bothnian Bay GAC-Dependent CIET-SAO Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
    role: canonical_record
scope:
  description: Entire record and all three nodes assessed against full primary science,
    critical figures/supplements, current taxon/archive authorities, history and native
    checks.
  selection: Only released CommunityMech:000349 in the owned batch08 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000349
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000349
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000349
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-08/000349/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000349
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000349
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000349
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000349
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000349
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000349
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  target_ids:
  - CommunityMech:000349
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit reuse of fresh batch08 corpus receipts, not a target-specific
    pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  target_ids:
  - CommunityMech:000349
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit reuse of fresh batch08 corpus receipts, not a target-specific
    pass.
- check_id: source-identity
  name: Primary source identity and excerpts
  status: passed
  required: true
  summary: Exact DOI/PMID/PMCID agree and all 24 snippets match directly retrieved
    full XML.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - pubmed
  - epmc
  - crossref
  - snippets
- check_id: scientific-source
  name: Whole source and critical supplementary assessment
  status: passed
  required: true
  summary: Entire main, all main figures and critical supplementary/read scopes assessed
    with explicit annotation and precursor-study limits.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - source-scope
  - independent-source
  - figures
  - supplement
  - workbook
  - source-data
- check_id: resource-identity
  name: Project, exact core MAGs and comparator scope
  status: passed
  required: true
  summary: Exact source-linked project and five BioSamples verified through bounded
    metadata; no raw-data analysis.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - resources
  - candidate-taxonomy
- check_id: cross-mech
  name: Exact modified-medium correspondence
  status: not_applicable
  required: false
  summary: No exact modified-medium identifier established; no guessed CultureMech
    or ingredient link.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - cultivation
  - resources
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Same-runtime fresh batch08 discovery explicitly reused; no runnable adapter
    established or external checkout executed.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  locator: Entire canonical record
  summary: Five focal taxa, three interaction nodes and no downstream arrows describe
    the long-term sediment-derived GAC enrichment; two non-graph fields retain stronger
    or less scoped wording than the graph.
  support: supports
  accessed_at: '2026-10-21T13:23:37.592082Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41876513&retmode=xml
  locator: Article-level bibliographic metadata
  summary: PMID 41876513, DOI 10.1038/s41467-026-70468-2 and PMC13013709 identify
    the same primary article.
  support: supports
  accessed_at: '2026-10-21T13:16:51.456643Z'
  snapshot_sha256: bba08750c23b5690eb86d2d7d447057df460521762fdbef9e71ac5f2069bc119
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41876513%20AND%20SRC:MED&format=json&resultType=core
  locator: Article-level bibliographic metadata
  summary: PMID 41876513, DOI 10.1038/s41467-026-70468-2 and PMC13013709 identify
    the same primary article.
  support: supports
  accessed_at: '2026-10-21T13:16:51.774616Z'
  snapshot_sha256: aca67e41b935dd986fe5c591b94393053eb839efcaaba2f4f9732ed02308bd1a
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1038/s41467-026-70468-2
  locator: Article-level bibliographic metadata
  summary: PMID 41876513, DOI 10.1038/s41467-026-70468-2 and PMC13013709 identify
    the same primary article.
  support: supports
  accessed_at: '2026-10-21T13:16:51.536982Z'
  snapshot_sha256: ddfcaccdd915f81d3063bee92c5d30716e4cf513fed3dea5677b998d69cd7423
- evidence_id: core
  kind: primary_source
  reference: PMID:41876513
  locator: 'Results and Discussion: GAC-dependent activity, core MAGs; Figures 1 and
    2 captions'
  summary: Acetate oxidation and methane formation persist in GAC cultures; particle-free
    cultures are nearly inactive. The source assigns the proposed core route to GAC.MBAT.93
    and GAC.MBAT.2 using physiology and genomic evidence.
  support: supports
  accessed_at: '2026-10-21T13:23:37.592737Z'
  snapshot_sha256: 82ee3c0dbe21da0af34a8ad0a889dddeddd7a01bf4f88f6e45b1840b6c901abb
  quote: through the GAC matrix
- evidence_id: residual
  kind: primary_source
  reference: PMID:41876513
  locator: 'Results and Discussion: particle-free population comparison'
  summary: Methanosarcina remains detectable at approximately 0.06%; this contradicts
    categorical loss of both core MAGs, while preserving severe depletion and low
    activity.
  support: supports
  accessed_at: '2026-10-21T13:23:37.592822Z'
  snapshot_sha256: 82ee3c0dbe21da0af34a8ad0a889dddeddd7a01bf4f88f6e45b1840b6c901abb
  quote: 0.06%
- evidence_id: auxiliary
  kind: primary_source
  reference: PMID:41876513
  locator: 'Results and Discussion: Lentimicrobium and auxiliary lineages'
  summary: Lentimicrobium EET-linked acetate oxidation and fermentative recycling
    are alternatives; Sedimentibacter and Desulforhopalus detrital recycling remains
    inferred.
  support: supports
  accessed_at: '2026-10-21T13:23:37.592905Z'
  snapshot_sha256: 82ee3c0dbe21da0af34a8ad0a889dddeddd7a01bf4f88f6e45b1840b6c901abb
  quote: may sustain its activity
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:41876513
  locator: 'Methods: Cultivation'
  summary: Initial inoculations used 100 mL bottles containing 50 mL culture and 50
    mL headspace. Subsequent transfers used 50 mL glass vials without a separately
    specified liquid fill. The source also gives 10% or 20% inoculum, modified DSMZ
    120, 10 mM acetate, 10 g/L GAC, anaerobic gas handling, dark/static 22 °C conditions.
  support: supports
  accessed_at: '2026-10-21T13:23:37.592987Z'
  snapshot_sha256: 82ee3c0dbe21da0af34a8ad0a889dddeddd7a01bf4f88f6e45b1840b6c901abb
  quote: 50 mL culture
- evidence_id: transfer-conflict
  kind: primary_source
  reference: PMID:41876513
  locator: 'Methods: Cultivation; Results and Discussion: GAC-free propagation'
  summary: Methods reports 22 transfers in nine years; Results reports 30 successive
    transfers without GAC. Preserve the source discrepancy rather than selecting one
    unqualified count.
  support: supports
  accessed_at: '2026-10-21T13:23:37.593068Z'
  snapshot_sha256: 82ee3c0dbe21da0af34a8ad0a889dddeddd7a01bf4f88f6e45b1840b6c901abb
- evidence_id: datasets-main
  kind: primary_source
  reference: PMID:41876513
  locator: Data availability
  summary: The source identifies PRJNA1140524 and exact community, core-MAG and comparator
    BioSamples; P39 is a separately sequenced comparison organism, not an enrichment
    member.
  support: supports
  accessed_at: '2026-10-21T13:23:37.593149Z'
  snapshot_sha256: 82ee3c0dbe21da0af34a8ad0a889dddeddd7a01bf4f88f6e45b1840b6c901abb
- evidence_id: figures
  kind: primary_source
  reference: PMID:41876513
  locator: Figures 1–5; valid asset-manifest.json paths
  summary: All five main images support the experimental/genomic distinction. Figure
    2 supplies focal read shares. Figures 3–5 provide proposed pathways and comparative
    genomic context, not molecular perturbation assays.
  support: supports
  accessed_at: '2026-10-21T13:23:37.593169Z'
  snapshot_sha256: 3a80687d12d4740229316d70700b85c991ab41f3a81f954e425c13e6451dd6d3
- evidence_id: supplement
  kind: primary_source
  reference: PMID:41876513
  locator: Supplementary Figures S1–S11 captions; inspected S3–S5 and S7–S11 images
  summary: Supplemental abundance and comparative sequence displays refine the source
    interpretation without measuring species-resolved exchanged fluxes. S3 gives Sedimentibacter
    6.4%, differing from main/Figure 2 6.5%.
  support: supports
  accessed_at: '2026-10-21T13:23:37.595734Z'
  snapshot_sha256: f270ce09dbd9213fb5100f4ac39ce71c0799d51ccc76f4990f60b22e9265465c
- evidence_id: workbook
  kind: primary_source
  reference: PMID:41876513
  locator: 'Supplementary Tables S1–S3: headers and focal rows recorded in workbook-focal-read.json'
  summary: Selected acetate-metabolism, PilA/cytochrome and Rnf/Fpo annotations support
    proposed genetic capacities, not direct pathway activity or necessity.
  support: supports
  accessed_at: '2026-10-21T13:23:37.595931Z'
  snapshot_sha256: a85b0dccbf3a56e7e58be50adb83364086eee5fa8b67bac3dacc51c4710d8afe
- evidence_id: source-data
  kind: primary_source
  reference: PMID:41876513
  locator: 'Source Data PDF: all five pages'
  summary: Inspected the reported time-course means/variation, multiheme comparisons
    and homology data without recomputation or raw-data reanalysis.
  support: supports
  accessed_at: '2026-10-21T13:23:37.596123Z'
  snapshot_sha256: f6446abf5ff8f4ec33fe5e90bdedeee30820b0661dd48b25e2b3b46b1106c4dd
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity; CultivationSetup; InteractionTypeEnum; FunctionalRoleEnum;
    AbundanceEnum; EcologicalStateEnum
  summary: DIET does not impose a cell-contact-only rule. SYNTROPHY does not require
    obligacy. Abundance is ordinal; ecological_state is optional. Working volume denotes
    culture liquid, not vessel capacity.
  support: supports
  accessed_at: '2026-10-21T13:23:37.596184Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded receipt
  summary: All 11 encoded ontology pairs across 21 occurrences match canonical labels;
    a valid broad label does not establish adequate participant resolution.
  support: supports
  accessed_at: '2026-10-21T13:23:37.596347Z'
  snapshot_sha256: 988176e49ccff4db8f4b4aeb033e0b96b7619a80383256ff2f4417e670e7aa19
- evidence_id: candidate-taxonomy
  kind: authority
  reference: taxon-grounding-candidates.json
  locator: Whole bounded receipt
  summary: NCBITaxon:3714907 is locally Candidatus Geosyntrophus acetoxidans, species
    rank, parent 3714906. Methanosarcina sp. 2213 is a placeholder under genus 2207,
    not a named-species requirement.
  support: supports
  accessed_at: '2026-10-21T13:23:37.596465Z'
  snapshot_sha256: 0d49508b6ebc7563f468c424f3fef77d452ab7f6e0f0994fdde5472b71aff29a
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded receipt
  summary: Exact GAC.MBAT.93 links SAMN54926496/GCA_057407595.1 to taxid 3714907.
    GAC.MBAT.2 links SAMN54926476 to GCA/GCF_057408005.1. The bounded inventory has
    24 GAC, 30 Control and one P39 records; no raw sequences were read.
  support: supports
  accessed_at: '2026-10-21T13:23:37.596614Z'
  snapshot_sha256: ec9af89e60fc5c20f37576a6b77a49d2984e160fcd744df0d4c3d564d4d93a77
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded receipt
  summary: All 24 encoded excerpts match the directly retrieved complete XML and pinned
    cache; two also match the abstract.
  support: supports
  accessed_at: '2026-10-21T13:23:37.596715Z'
  snapshot_sha256: c970d8038de070d084a8bd6b55c60bb999397309500791133b764eefd47126f4
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded receipt
  summary: Both histories and exact prior decision were read. Issue 1264 is closed
    after graph repair; issue 1268 remains open for non-graph follow-up. Its recent
    same-batch retrieval is explicitly reused.
  support: supports
  accessed_at: '2026-10-21T13:23:37.596830Z'
  snapshot_sha256: de39edec90c08d1356779e6dd6a3312d679f3df9310f23a4d7c8d351c8d90e20
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded receipt
  summary: Native completeness is 90 and network status COMPLETE. Final P1/P2/P3/P4
    counts are 0/1/2/0; quality is capped at 100 from 117.6666666667.
  support: supports
  accessed_at: '2026-10-21T13:23:37.596853Z'
  snapshot_sha256: 6e07e2e37f0ef15dac822e37ca4a1117e48f19a4438af74ae92580f98629fc36
- evidence_id: support-manifest
  kind: validation
  reference: supporting-artifact-manifest.json
  locator: Whole bounded receipt
  summary: Frozen supporting artifact hashes preserve direct-source, current issue,
    archive and input-integrity boundaries.
  support: supports
  accessed_at: '2026-10-21T13:23:37.597278Z'
  snapshot_sha256: 8a914dbc0a3e953d7e46c4d9db7fb1beecbdfeb6f94274ee1c4f259388237f86
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded receipt
  summary: Whole main and critical supplemental/figure scopes support a completed
    assessment, with explicit uninspected assets and no raw-data reanalysis.
  support: supports
  accessed_at: '2026-10-21T13:23:37.597309Z'
  snapshot_sha256: 760508fe6dcaf7cdca95ca15966d335eec9337db8a176e8bd1d9eaaa102c71a0
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded receipt
  summary: Root independently concurs with one major and two minor findings and retention
    of the qualified graph.
  support: supports
  accessed_at: '2026-10-21T13:23:37.597335Z'
  snapshot_sha256: c08164f721b44f4774f5b711b64394604a44133aa5a810bb87faa1eb171096c2
- evidence_id: independent-authority
  kind: validation
  reference: root-ontology-dataset-confirmation.json
  locator: Whole bounded receipt
  summary: Root independently confirms current taxonomy authority, exact archive linkage,
    semantic boundaries and native checks.
  support: supports
  accessed_at: '2026-10-21T13:23:37.597357Z'
  snapshot_sha256: b2cae58eb1062071b8c4a600d324b0e092bf7a31cdc27357d999c0f47b94f7df
- evidence_id: local-search
  kind: search
  reference: Maintained corpus and mappings
  locator: local-search.json; local-search-interpretation.json
  summary: Ignored-inclusive bounded searches found no focal reusable taxon match.
    A broad Bacteria substring hit and a comparator citation are explicitly excluded
    as false identity matches.
  support: supports
  accessed_at: '2026-10-21T13:23:37.597456Z'
  snapshot_sha256: e4602b062be3ff427158399230bef88620891bb838842814d35ea693b2c3012c
  search_scope: Maintained record, taxon and mapping roots including ignored files;
    no global absence claim.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: adapter-check.json
  summary: Explicit same-runtime reuse of fresh batch08 discovery found no runnable
    adapter in the task environment; no external checkout was executed.
  support: supports
  accessed_at: '2026-10-21T13:23:37.597569Z'
  snapshot_sha256: 77164f316cdfd7ebbfea410d55a51fc50e5dda2bf7a15516e42be099fa6fed86
  search_scope: Original batch08 PATH, venv/module and ignored-inclusive filename
    discovery plus current runtime verification; not a new global search.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  locator: Actual execution 2026-10-21T13:17:10.806030+00:00 to 2026-10-21T13:17:12.812149+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T13:17:12.812149Z'
  snapshot_sha256: c205ab803f6e1065d269c31251ad94750c20744d8f31890c89ea9fc9a2bceb8f
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-08/000349/strict-report.tsv
  locator: Actual execution 2026-10-21T13:17:10.810119+00:00 to 2026-10-21T13:17:16.568915+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T13:17:16.568915Z'
  snapshot_sha256: 56ae4007e7b6e7b0754bc98db67fbf8255b27e9d55c2d0c5f6d981f1a89816d4
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  locator: Actual execution 2026-10-21T13:17:10.812976+00:00 to 2026-10-21T13:17:15.114026+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T13:17:15.114026Z'
  snapshot_sha256: 177682fadccffd16d1828c0e3fc415e796a99372bcce89f405368e38b8690e6b
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  locator: Actual execution 2026-10-21T13:17:12.813061+00:00 to 2026-10-21T13:17:12.956965+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T13:17:12.956965Z'
  snapshot_sha256: 7697fdec9f5b7fef498db365c5eaa48eb151b1e76d8fad9c482087f181573c35
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  locator: Actual execution 2026-10-21T13:17:12.957364+00:00 to 2026-10-21T13:17:16.770616+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T13:17:16.770616Z'
  snapshot_sha256: 6343764ffab948d176b5bc29b9bf9c4337ccf06577b599c1472d39b36aa5304b
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium
  locator: Actual execution 2026-10-21T13:17:15.114575+00:00 to 2026-10-21T13:17:17.081496+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T13:17:17.081496Z'
  snapshot_sha256: f38a992a91bbd50a223527bf94351365cd35843e9e7fbc75b4bb665377b570d3
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T13:17:17.083859+00:00 to 2026-10-21T13:17:17.223829+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T13:17:17.223829Z'
  snapshot_sha256: 27375a3680a4a83248e46e8dd028cc435bd6d51151328d77dc59aebe04fa9031
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
  locator: Actual execution 2026-10-21T13:17:17.224241+00:00 to 2026-10-21T13:17:20.666921+00:00
  summary: Reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T13:17:20.666921Z'
  snapshot_sha256: 155d11ab69f4b85cd65c9e692889ea588db8477cd025659461b8a6a14a8070aa
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:11.311177Z'
  snapshot_sha256: 2d17097db768619fa7fea156f7c37781fa9cd463a6abdce6f529112518848cf0
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:15.408522Z'
  snapshot_sha256: 1332cfd7980ec54d517d625aff43fa6328c1a19fd405a7aef071f78af9774f3f
assessments:
- assessment_id: identity
  area: identity
  topic: Enrichment identity and physical context
  outcome: supported
  summary: Retain the natural sediment origin, sediment-free enrichment environment
    and GAC-mediated CIET scope. The five taxa are selected core/auxiliary members,
    not an exhaustive MAG inventory.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - core
  - datasets-main
  - record
  - schema
  dimensions:
  - name: community_scope
    value: Long-term GAC-amended Bothnian Bay enrichment
    definition: Distinct from unmodified sediment, particle-free transfers and comparator
      P39.
    evidence_ids:
    - core
    - datasets-main
  - name: source_strain
    value: GAC.MBAT.93 and GAC.MBAT.2 are MAG designations
    definition: Do not present these as isolated culture-collection strains.
    evidence_ids:
    - resources
  - name: taxon_rank
    value: One named species currently represented only at domain rank; four genus-level
      entries
    definition: Exact core MAG authority now supports specific Geosyntrophus grounding.
    evidence_ids:
    - candidate-taxonomy
    - resources
  - name: grounding_status
    value: Geosyntrophus requires coordinated NCBI/GTDB review
    definition: Do not retain the domain aggregate as if it were a species mapping.
    evidence_ids:
    - ontology
    - candidate-taxonomy
  - name: environment
    value: Active anaerobic enrichment; source sediment modeled separately
    definition: Current physical and source-environment distinction is appropriate.
    evidence_ids:
    - cultivation
    - record
  - name: medium
    value: Modified DSMZ 120, 10 mM acetate and 10 g/L GAC
    definition: No exact full recipe or cross-Mech identity is inferred from the base-medium
      number.
    evidence_ids:
    - cultivation
  - name: experimental_setting
    value: Initial bottles, later serial-transfer vials and current GAC/control assays
    definition: Working volume and transfer counts require phase/source qualifiers.
    evidence_ids:
    - cultivation
    - transfer-conflict
  - name: evidence_tier
    value: Community physiology plus genome-informed mechanisms
    definition: Specific protein function and auxiliary metabolite exchange remain
      hypotheses.
    evidence_ids:
    - core
    - auxiliary
    - workbook
- assessment_id: taxonomy
  area: grounding
  topic: taxonomy[0] and ecological_interactions[0].source_taxon
  outcome: concern
  summary: Replace domain-only Bacteria grounding for the exact GAC.MBAT.93 participant
    with the verified species authority and reassess its GTDB status.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - record
  - candidate-taxonomy
  - resources
  - ontology
  details: Local canonical label is Candidatus Geosyntrophus acetoxidans; live archive
    nomenclature is Geosyntrophus acetoxidans (SeqCode). Preserve that version distinction
    and the exact MAG label. Current Methanosarcina genus remains defensible; do not
    force a named species or incomplete printed GTDB identifier.
- assessment_id: roles
  area: evidence
  topic: Five taxon roles and abundance fields
  outcome: supported
  summary: Retain experimental core electron-transfer roles and explicitly inferred
    auxiliary alternatives. DOMINANT does not mean more than half of all reads.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - core
  - auxiliary
  - supplement
  - schema
  details: 9.4% and 12% are focal metagenomic read shares. Lentimicrobium EET versus
    fermentative recycling and Sedimentibacter/Desulforhopalus secondary roles remain
    source hypotheses. Do not claim all capacities operate simultaneously. The 6.5%/6.4%
    Sedimentibacter variation is an upstream source discrepancy, not a silently repaired
    value.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain GAC-dependent acetate oxidation coupled to methane production with
    the current residual-population and molecular limits; correct its source taxon
    grounding.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - core
  - residual
  - figures
  - candidate-taxonomy
  details: The record combines enrichment physiology, genomics and explicitly attributed
    precursor work. GAC dependence is not reduced to gene presence alone; specific
    PCC/MmcA/pilus routes were not independently isolated in these MAGs. Residual
    Methanosarcina is already correctly acknowledged here.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain the PARTIAL COMPUTATIONAL Lentimicrobium interaction as alternative
    EET-linked acetate oxidation or fermentative recycling.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - auxiliary
  - workbook
  - figures
  details: Genomic transport, metabolism and cytochrome capacity supports the proposed
    route, not measured species-resolved transfer or compulsory use of one pathway.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: Retain the PARTIAL community-level biomass-turnover hypothesis for the
    three auxiliary genera.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - auxiliary
  - workbook
  details: This is inferred recycling of biomass-derived organic matter; the current
    record does not establish the exact donor, metabolite flux or requirement of each
    auxiliary lineage.
- assessment_id: arrows
  area: graph
  topic: All downstream fields
  outcome: supported
  summary: There are no downstream arrows. No new causal edge is required to connect
    genomic capacities and community endpoints.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - record
  - core
  - auxiliary
- assessment_id: state
  area: scope
  topic: Ecological state, origin and category
  outcome: supported
  summary: Retain NATURAL source origin and DIET with explicit conductive-particle
    mediation; read STABLE within maintained GAC enrichment conditions.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - core
  - schema
  - record
  details: The source reports long-term persistence of the core partnership under
    GAC cultivation. This does not assert equilibrium of unperturbed sediment or invariant
    abundance of every member. Serial enrichment alone does not require changing community_origin
    from NATURAL to ENGINEERED; ecological_state is a separate optional field.
- assessment_id: cultivation
  area: representation
  topic: growth_media[0] and cultivation_setup[0]
  outcome: concern
  summary: The medium, anaerobic handling, temperature, light and GAC concentration
    are supported; the single setup merges initial liquid volume with later vessel
    capacity.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - cultivation
  - transfer-conflict
  details: Scope 50 mL working liquid to the initial 100 mL bottles. Later 50 mL glass-vial
    capacity does not establish 50 mL fill. Preserve Methods 22 transfers versus Results
    30 GAC-free transfers as unresolved reporting context.
- assessment_id: environmental-factor
  area: evidence
  topic: environmental_factors[0]
  outcome: concern
  summary: The factor correctly identifies GAC dependence, but categorical loss of
    both core MAGs contradicts residual Methanosarcina and the qualified node.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - residual
  - core
  - record
  details: Align description and nearby interpretation with depletion/poor detection;
    do not infer extinction, absolute absence or viability from relative metagenomic
    abundance.
- assessment_id: resources
  area: provenance
  topic: Dataset, publication, metal fields and history
  outcome: supported
  summary: The encoded BioProject and publication are correct, comparator P39 is distinguished,
    and no metal-cycling claim is made merely because GAC conducts electrons.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - datasets-main
  - resources
  - history
  - snippets
  - record
  details: Core sample/assembly identifiers can support the taxonomy correction. Current
    inventory counts are metadata scope, not verification of all analyses. Preserve
    the prior graph repair and open non-graph follow-up; no exact modified-medium
    CultureMech link is established.
- assessment_id: validation
  area: schema
  topic: Native checks and ontology labels
  outcome: supported
  summary: All eight native checks and 11 current ID/label pairs pass. The exact species
    grounding finding concerns resolution, not a mislabeled Bacteria identifier.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - candidate-taxonomy
- assessment_id: metrics
  area: completeness
  topic: Native mechanical scores
  outcome: supported
  summary: Scores measure structural completeness and native checks, separately from
    the three scientific findings.
  target_ids:
  - CommunityMech:000349
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 90
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role component +5 environment +10 interaction
      count +5 resource +10 medium +5 dataset +5 node metabolites; no three-factor
      bonus.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      Counts 0/1/2/0; five node evidence/three nodes gives 16.6667 bonus; COMPLETE
      gives 15; raw 117.6667, capped 100.
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
- finding_id: core-species-grounding
  issue_key: cm-000349-core-species-grounding
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: 'P2: material grounding deficiency for a named mechanistic
    participant; exact archive linkage supports correction without guessing identity.'
  rule_id: review-checklist.identity-source-and-context
  status: open
  certainty: confirmed
  title: Ground the exact core MAG beyond the bacterial domain
  description: The named GAC.MBAT.93 partner remains NCBITaxon:2/Bacteria in membership
    and the core node, with a domain-level GTDB aggregate. Its exact BioSample/assembly
    now resolves to NCBITaxon:3714907 and the local species authority. This loses
    material participant resolution despite a valid Bacteria label.
  target_ids:
  - CommunityMech:000349
  field_paths:
  - taxonomy[0].taxon_term
  - ecological_interactions[0].source_taxon
  evidence_ids:
  - candidate-taxonomy
  - resources
  - record
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
    role: canonical_record
- finding_id: phase-specific-cultivation
  issue_key: cm-000349-phase-specific-cultivation
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded protocol representation; supported medium and
    overall enrichment identity remain intact.'
  rule_id: review-checklist.identity-source-and-context
  status: open
  certainty: confirmed
  title: Separate initial culture volume from subsequent vial capacity
  description: cultivation_setup[0] combines initial serum bottles and later vials
    but assigns 50 mL working volume without phase scope. Only the initial 100 mL
    bottle explicitly contains 50 mL culture; later vials have 50 mL vessel capacity.
    Existing discussion also flags unresolved transfer counts.
  target_ids:
  - CommunityMech:000349
  field_paths:
  - cultivation_setup[0].instrument_detail
  - cultivation_setup[0].working_volume
  - cultivation_setup[0].controls_notes
  - discussions[0].rationale
  evidence_ids:
  - cultivation
  - transfer-conflict
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
    role: canonical_record
- finding_id: residual-methanosarcina
  issue_key: cm-000349-residual-methanosarcina
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: one bounded non-graph overstatement; community GAC dependence
    and the corrected interaction remain supported.'
  rule_id: review-checklist.identity-source-and-context
  status: open
  certainty: confirmed
  title: Retain residual Methanosarcina in the non-graph control description
  description: environmental_factors[0].description says the controls lost both key
    MAGs, although the source reports approximately 0.06% Methanosarcina and ecological_interactions[0]
    already preserves this limit.
  target_ids:
  - CommunityMech:000349
  field_paths:
  - environmental_factors[0].description
  - environmental_factors[0].evidence[0].explanation
  evidence_ids:
  - residual
  - core
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
    role: canonical_record
actions:
- action_id: ground-core-mag
  description: Update the exact Geosyntrophus MAG consistently and re-ground its GTDB
    representation.
  finding_ids:
  - core-species-grounding
  target_ids:
  - CommunityMech:000349
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Use NCBITaxon:3714907 with the pinned canonical label Candidatus Geosyntrophus
    acetoxidans in taxonomy[0].taxon_term.term and ecological_interactions[0].source_taxon.term;
    preserve GAC.MBAT.93 and cite SAMN54926496/GCA_057407595.1.
  - Document the live SeqCode name versus local canonical-label version. Re-run GTDB
    grounding against the corrected NCBI identifier; replace stale NCBITaxon:2/domain
    aggregate metadata or retain an explicit unresolved status if no supported specific
    mapping is available. Do not assert JACRCG01 correspondence from a placeholder
    alone.
  - Keep Methanosarcina at its justified genus and preserve all five focal memberships,
    three qualified nodes and zero arrows. Run schema, strict, terms, GTDB/domain,
    reference and history checks after separately authorized curation.
- action_id: scope-cultivation
  description: Represent the initial and later cultivation phases separately or scope
    each reported value explicitly.
  finding_ids:
  - phase-specific-cultivation
  target_ids:
  - CommunityMech:000349
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Limit 50 mL liquid/50 mL headspace to the initial 100 mL serum bottle. Record
    later 50 mL glass vials as vessel capacity with unspecified fill; do not infer
    their headspace or working volume.
  - Preserve supported 10% or 20% inoculum, 10 mM acetate, 10 g/L GAC, static dark
    22 °C and anaerobic handling with their source context; do not invent a full DSMZ
    modified-120 recipe.
  - Record the Methods 22 transfers/nine years versus Results 30 GAC-free transfers
    discrepancy without silently choosing one count. Keep earlier graph-only history
    intact and validate any separately authorized correction.
- action_id: qualify-control-populations
  description: Align the environmental-factor interpretation with the measured residual
    population and existing node.
  finding_ids:
  - residual-methanosarcina
  target_ids:
  - CommunityMech:000349
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bothnian_Bay_GAC_Dependent_CIET_SAO_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Describe severe depletion or poor detection and near inactivity in particle-free
    transfers; explicitly retain residual Methanosarcina near 0.06%. Do not claim
    both populations disappeared.
  - Keep any exact source quotation unchanged, but qualify its interpretation with
    the quantitative result. Relative read abundance does not establish extinction
    or viability.
  - Preserve the GAC-dependence endpoint and the molecular/auxiliary hypotheses; no
    new node or causal arrow is warranted.
limitations:
- No raw-read reanalysis, biochemical validation, experimental rerun, proteome reannotation
  or independent reread of precursor physiological papers. Current-paper summaries
  of earlier isotope/inhibitor/NanoSIMS work retain that attribution.
- Specific EET proteins and auxiliary recycling routes remain genomic hypotheses.
  Read shares are not cell counts, viability or absolute extinction measurements.
- Methods reports 22 transfers over nine years; Results reports 30 successive GAC-free
  transfers. Initial bottle and later vial configurations must remain distinct.
- Main/Figure 2 gives Sedimentibacter 6.5%, whereas later prose/S3 gives 6.4%. The
  24 GAC MAG statement and archive inventory are not silently equated with the different
  Figure 2 Venn and S3 caption counts.
- The initial figure/supplement URL attempts returned HTML errors and remain preserved.
  Valid assets were subsequently recovered from the directly fetched EPMC ZIP into
  assets/. Reporting-summary content and peer-review file were not reviewed.
- Local canonical Candidatus Geosyntrophus acetoxidans and live archive Geosyntrophus
  acetoxidans (SeqCode) are authority-version labels for the verified taxid; no forced
  Methanosarcina named species or exact GTDB placeholder mapping.
notes:
- No canonical, cache, history, generated or saved-review file changed; all 24 official
  input pins remain intact.
- All 24 evidence occurrences match direct full XML and the pinned cache. Critical
  source scopes are complete for the assessed claims, not a whole-omics reanalysis.
- Native completeness 90 and quality 100/raw 117.6667 do not erase the one major and
  two minor findings.
- NATURAL origin, GAC-conditioned stability, explicit CIET route, core experimental
  evidence and PARTIAL auxiliary hypotheses are retained.
tags:
- record-review
- syntrophy
- biomethanation
- full-source
- batch-08
```
