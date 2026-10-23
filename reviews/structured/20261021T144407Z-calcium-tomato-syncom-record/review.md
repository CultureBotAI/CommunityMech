# Calcium-tomato bacterial wilt SynCom review

- Review: 20261021T144407Z-calcium-tomato-syncom-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T14:33:27.756419Z
- Finished UTC: 2026-10-21T14:44:07.930646Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The full primary main and all eight figures support the four-member identity and qualified three-node, one-arrow graph. Three minor findings concern recoverable assay context, inoculum-design placement and separate amplicon/isolate resource scope. Cited scientific supplementary figures/table remain unread; current-claim completion does not certify those details.

## Scope And Provenance

Entire record and every node/arrow assessed using direct primary main, all eight main figures, source-specific archives, authority, history and native checks, with explicit unread scientific-SI limits.

Selection: Only released CommunityMech:000393 in the owned batch 08 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000393 | kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml | maintained | Calcium-Tomato Bacterial Wilt SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000393 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000393 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000393 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000393 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000393 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000393 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000393 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000393 | Reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000393 | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000393 | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| Primary article identity | passed | True | CommunityMech:000393 | Direct PubMed, EPMC, Crossref and full XML/publisher main agree on article identity. |
| Current claim verification | passed | True | CommunityMech:000393 | Entire primary scientific main and all eight main figures support assessment of current qualified claims; source-specific archive and authority checks are separately bounded. |
| Cited scientific supplement inspection | unavailable | False | CommunityMech:000393 | Returned package contains main images and video abstracts, not the cited S1–S5/Table S1 document. Those details remain unread. No SI-only numerical or sequence-level result is certified. |
| Exact focal medium linkage | not_applicable | False | CommunityMech:000393 | Named LB and nutrient broth describe different preparations and assay dilutions; no exact CultureMech recipe correspondence was established or required for the current findings. |
| Optional structured expression adapter | unavailable | False | CommunityMech:000393 | Same-runtime discovery is explicitly reused; no exact expression-module claim was established and no external checkout adapter was executed. |

## Scientific And Domain Assessments

### Four-member SynCom and external host/pathogen

identity: supported. Targets: CommunityMech:000393.

Retain all four source species, deliberate assembly and tomato-root context.

### State, origin and category

scope: supported. Targets: CommunityMech:000393.

Retain ENGINEERED state, SYNTHETIC origin and RHIZOSPHERE category.

The deliberate four-isolate assembly is explicit. No equilibrium, genetic modification or permanent in-situ community stability is inferred. Tomato-root source and applied rhizosphere context are compatible with the broad environmental terms, while exudate assays remain laboratory experiments.

### Antagonist roles, ordinal prominence and local evidence

evidence: supported. Targets: CommunityMech:000393.

Retain PATHOGEN_ANTAGONIST for all four members and coequal inoculum-level DOMINANT.

Figure 5b and the plate Methods establish antagonist activity, despite the local taxonomy excerpts naming identity alone. Add narrow role evidence with assay scope. Equal-volume OD-normalized preparation is not a measured equal cell fraction or persistent root abundance. Predicted gene functions do not establish expression, production or a necessary mechanism of protection.

### NCBI and GTDB correspondence

grounding: supported. Targets: CommunityMech:000393.

Keep source species labels and transparent GTDB uncertainty; no automatic isolate-level reassignment.

The manually curated Rhodanobacter pin is an existing plausible reference-cluster choice without source-run genome classification. The exact 582702 crosswalk and species-name rows are not present in the pinned table; cluster existence is independently verified. Dyella uses another strain’s species-name fallback; Pseudomonas has an aggregate species mapping; Paenibacillus stays ambiguous. These are bounded unresolved mapping questions, not demonstrated wrong NCBI species identities.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000393.

Retain differential compound responses without interorganism colonization or exudate-mediator claims.

Calcium and purified metabolites were tested separately in specified media. Tissue abundance is not exudate concentration. The broad differential-response phrasing accommodates compound/time-specific responses and the source prose/SA-panel tension; it does not prove each compound inhibits the pathogen under every tested condition.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000393.

Retain the compound-to-whole-exudate link only as HYPOTHESIZED.

No selective depletion/add-back or equivalent test identifies these molecules as necessary whole-exudate mediators. Preserve the current explicit hypothesis, with no stronger causal promotion or new exudate-to-pot arrow.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000393.

Retain whole-exudate/SynCom-associated reduction in pathogen qPCR gene copies.

The 150 microlitre coculture is distinct from the 140 microlitre single-culture OD assay. Gene copies are not viable-cell counts. The 20 mM value describes seedling conditioning, not measured calcium in concentrated exudates or the final well. No reciprocal-negative competition or unique mediator is established.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000393.

Retain the source-reported 74.07% to 0% disease-incidence result under the tested low-dose pot treatment.

Figure 7 shows the four arms and zero observed wilt in the combined group. Preserve the one-week pathogen-to-SynCom sequence. Disease incidence does not establish pathogen eradication, field efficacy, long-term stability or a formal factorial interaction. The earlier high-calcium host-defense experiment is a separate context.

### Related ingredients and metabolite evidence

grounding: supported. Targets: CommunityMech:000393.

Retain the named tested compounds and calcium salt with dose and evidence boundaries.

Calcium doses per kg soil are elemental-Ca basis, not equal CaCl2 mass. Root-tissue metabolomics is not exudate chemistry. Salicylic-acid inhibition wording follows the main prose, but Figure 6d does not show uniform high-dose inhibition; retain explicit source attribution and response specificity rather than deriving a new numeric result from pixels. Generic trehalose does not assert an anomer.

### Exudate preparation, pot context and role evidence

completeness: concern. Targets: CommunityMech:000393.

Recover the concentrated-exudate preparation and final-pot protocol without importing unrelated conditions.

The record correctly gives150 microlitres, preparation OD values and sampling times, but omits the 1100-to 22 mL concentration step and separate 80 g nursery-soil/10 mL inoculation context. These are source-supported reproducibility details. Do not restore the 28 C/150 rpm final-culture settings removed by prior review.

### environmental_factors[0]

representation: concern. Targets: CommunityMech:000393.

The equal-ratio inoculum entry is assembly information, not an environmental condition.

Its content is valid and already represented in engineering_design and growth_media. Preserve it in the appropriate location while retaining the actual calcium/exudate treatment factors.

### associated_datasets[0] and source-linked isolates

provenance: concern. Targets: CommunityMech:000393.

Separate the amplicon project from four isolate projects and retain source/archive disagreement explicitly.

PRJNA1125171 does not contain the four verified isolate runs. Their metadata identify distinct projects and BJJ strain names. Paper genome-sequencing claims conflict with AMPLICON/GENOMIC/PCR annotations, and paper HiSeq conflicts with the one currently returned project run’s NovaSeq. These are scope and provenance limits, not proof of payload content or complete project coverage.

### History and retained uncertainty

provenance: supported. Targets: CommunityMech:000393.

Retain prior graph, calcium-ingredient and cultivation repairs and open mechanism questions.

The full present main/figure review does not restore a direct exudate-to-pot mediation link or infer exact-strain colonization from relative ASVs. Current graph and discussions already separate assay tiers. Native/reference success does not settle study-level causal gaps.

### Native checks and claim-specific evidence

schema: supported. Targets: CommunityMech:000393.

All eight focused native gates pass; three bounded provenance/representation findings remain.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000393.

Current scores include the encoded dataset and three environmental-factor entries; scores do not certify their placement.

## Findings

### assay-context: Recover concentrated-exudate and final-pot context

minor / open / confirmed; issue key: cm-000393-assay-context.

The record gives the coculture recipe and sampling times but omits the exudate concentration step and final 80 g pot setup. Available narrow antagonist evidence can also replace reliance on identity-only local excerpts. Recover these details with their experiment-specific limits, preserving the prior removal of unsupported final-culture setpoints.

### inoculum-factor: Keep inoculum assembly outside environmental conditions

minor / open / confirmed; issue key: cm-000393-inoculum-factor.

environmental_factors[0] describes the defined four-member inoculum, which is already represented as assembly and preparation. Its content is source-supported, but it is not an environmental condition.

### dataset-partition: Separate amplicon and isolate resource scope

minor / open / confirmed; issue key: cm-000393-dataset-partition.

The PRJNA1125171 dataset entry includes raw isolate-genome sample types, while direct run metadata places each isolate in a separate project. Keep the paper and portal platform/read-type disagreements explicit; neither source is silently substituted for the other.

## Recommended Actions And Acceptance Checks

### recover-assay-context

Add reproducible source context while retaining separate experimental arms and evidence tiers.

- State that collected exudate was filtered, lyophilized and reconstituted from 1100 mL to 22 mL before adding 30 microlitres per coculture. Describe nominal fiftyfold concentration of collected solution, not measured concentrations of calcium, salicylic acid, sucrose or trehalose.
- Keep seedling conditioning at 0/20 mM calcium for five days separate from 48 h collection in deionized water after rinsing. The 28 C and 16/8 h light/dark regime belongs to conditioning/collection, not automatically to final coculture incubation.
- Preserve the 150 microlitre coculture recipe, OD600 0.1 ± 0.05 preparation and 6/12/24/48 h qPCR sampling. Do not merge the 140 microlitre single-culture OD assay or the purified-compound assay conditions. Do not restore unsupported final SynCom/coculture 28 C or 150 rpm settings.
- Add a distinct final-pot context: 80 g sterilized nursery soil, calcium one week after sprouting, 10 mL pathogen at the triloba stage and 10 mL SynCom one week later, with the source-reported replicate description. Do not transfer the 2 kg gradient soil, 50 mL challenge or 20/30-day sampling schedule.
- Attach narrow plate-antagonism evidence for each supported role while retaining genomic traits as predictions. Keep DOMINANT explicitly at coequal prepared-inoculum scope; OD normalization does not measure equal cell fractions or in-planta persistence.
- Preserve all three nodes and the single HYPOTHESIZED arrow. Compound responses should remain dose/time/source-specific, with the main-prose versus Figure 6d SA discrepancy explicit when asserting inhibition; no replacement numeric effect, direct viable-cell loss or causal pot mediator is inferred. Re-run the native checks after separately authorized curation.
- Treat OD600 1 as the density of the harvested-cell suspension prepared for equal-volume assembly, not an established starting inoculum density for LB growth. Move or explicitly qualify growth_media[0].inoculum_size and inoculum_unit in preparation notes accordingly. The source reports harvested-pellet resuspension in sterile water but no explicit wash step; remove wash wording from engineering_design.inoculation_strategy and growth_media[0].preparation_notes unless direct source support is supplied.

### move-inoculum-design

Represent the existing inoculum facts in assembly/preparation fields.

- Remove environmental_factors[0] after preserving its 1:1:1:1 / OD600 1 preparation facts and evidence in engineering_design or the existing preparation notes. Do not discard the valid source evidence.
- Retain the actual 20 mM seedling-conditioning and 100 mg Ca/kg soil treatment contexts as distinct factors; do not turn them into one uniform medium or an exact final-well calcium concentration. Validate the revised field placement.

### partition-public-resources

Keep project/run/strain associations and conflicting technical metadata traceable.

- Scope PRJNA1125171 to the source-reported root/rhizosphere amplicon study and use a compatible dataset type. Remove isolate-run sample types from that project entry; a shared article does not establish project containment.
- Represent SRR33220703/BJJ-A/Dyella under PRJNA1252363, SRR33220740/BJJ-B/Rhodanobacter under PRJNA1252364, SRR33221449/BJJ-C/Paenibacillus under PRJNA1252366 and SRR33221452/BJJ-D/Pseudomonas under PRJNA1252367, or link the runs individually with the verified project relationships. The exact strain names are optional structured enrichment, not new organisms.
- Preserve the paper HiSeq2500 PE250 amplicon and PE150 genome wording alongside the portal’s currently returned NovaSeq6000 amplicon-project record and AMPLICON/GENOMIC/PCR isolate annotations. Mark these unresolved source/archive disagreements; do not certify raw genome content or replace the source platform merely from one portal response.
- Do not equate one returned project run with the complete 112-sample experiment, infer assembly availability, or use run identity to certify GTDB strain placement. Keep the existing manual glycinis_A uncertainty and Paenibacillus candidates; any later genome-based re-grounding needs direct isolate-specific evidence.
- Preserve source citations, the original repaired history and named public identifiers; re-run resource/reference, schema, ontology, GTDB/domain and history validation after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml; Entire record, three community-level nodes and one HYPOTHESIZED arrow | supports | The record represents the four-member calcium-selected tomato SynCom, with explicit distinctions among isolated-compound assays, whole-exudate qPCR and a separate low-calcium pot intervention. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=41387930&amp;retmode=xml; Article identity and available abstract | supports | The focal PMID, DOI, title and abstract agree. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41387930%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article identity and available abstract | supports | Direct article metadata identifies the open primary article and PMC12817675. |
| crossref | https://api.crossref.org/works/10.1186/s40168-025-02228-1; Article identity and available abstract | supports | DOI metadata agrees with the focal calcium/tomato study. |
| identity | PMID:41387930; Methods: Bacterial isolation and taxonomic identification; Construction of synthetic community; Results/Figure5 | supports | Four isolates from surface-sterilized calcium-treated tomato roots were identified as Dyella japonica, Rhodanobacter glycinis, Paenibacillus polymyxa and Pseudomonas aeruginosa. Tomato is the host and Ralstonia solanacearum P380 the challenged pathogen, not additional SynCom members. |
| assembly | PMID:41387930; Methods: Construction of synthetic community; In vitro interactions among members | supports | LB-grown pellets were resuspended in sterile water, individually adjusted to OD600 1 and mixed 1:1:1:1. Exudate coculture used a separate OD600 0.1 ± 0.05 combined suspension. The 28 C/150 rpm preparation is expressly reported for the separate plate-pair assay and must not be restored as a final-assembly or exudate incubation setpoint. |
| roles | PMID:41387930; Methods: Antagonistic activity against R. solanacearum; Results/Figure5b–c | supports | Plate tests establish antagonistic activity for all four isolates. Gene annotation describes potential plant-growth-related functions, not measured production, expression or the necessary mechanism of pot protection. The local taxonomy identity excerpt does not itself establish the role; narrow plate-assay evidence is available. |
| compounds | PMID:41387930; Methods: Growth of antagonistic bacteria in response to Ca and Ca-enriched root metabolites; Figure6c–f | supports | Separate additions used calcium chloride in NB and salicylic acid/sucrose/trehalose in one-tenth LB. Their concentrations, 28 C/150 rpm conditions and 4/12/24 h readout belong to those assays. Root-tissue metabolomics and compound growth responses do not establish the composition or necessary mediators of whole exudates. |
| exudate-preparation | PMID:41387930; Methods: Effect of whole root exudates on growth | supports | Thirty-day seedlings underwent five days in 0 or 20 mM calcium Hoagland solution, followed by rinsing and 48 h collection in 50 mL deionized water per plant. Collection conditions were 28 C and 16/8 h light/dark. Per treatment, 1100 mL was filtered, lyophilized and redissolved in 22 mL: nominal fiftyfold concentration of the collected solution, not a measured concentration of any one metabolite or calcium ion. |
| exudate-assay | PMID:41387930; Methods: Effect of whole root exudates on growth; Results/Figure6a–b | supports | The coculture contains 100 microlitres half NB, 10 pathogen suspension, 10 SynCom and 30 concentrated exudate solution, totaling 150 microlitres. Samples at 6/12/24/48 h were quantified by pathogen-specific qPCR. The separate single-culture OD assay totals 140 microlitres; it is not the same preparation or endpoint. |
| pot-assay | PMID:41387930; Methods: Biocontrol ability of SynCom; Figure7 | supports | The final intervention uses 80 g sterilized nursery soil, calcium applied one week after sprouting, 10 mL pathogen at the triloba stage and 10 mL SynCom one week later. Four calcium/SynCom treatment groups are compared. This is distinct from the earlier 2 kg soil calcium-gradient experiment, its 50 mL pathogen challenge and 20/30-day root sampling. |
| pot-outcome | PMID:41387930; Results: Combined application of SynCom and Ca controlled bacterial wilt; Figure7; Statistical analysis | supports | The source reports wilt incidence from 74.07% to zero for the combined low-dose treatment. One-way ANOVA/LSD treatment contrasts do not establish a factorial interaction term, pathogen eradication, universal protection or necessity of high-dose host-defense responses. |
| resource-source | PMID:41387930; Data availability; Methods: Root and rhizosphere microbial community; Genome sequencing | supports | The paper separately assigns amplicons to PRJNA1125171 and names four isolate runs. Methods reports HiSeq2500 PE250 for amplicons and HiSeq2500 PE150 for isolate genome sequencing; current archive metadata requires a separate, explicitly scoped comparison. |
| figures | PMID:41387930; All eight main figures; direct publisher PNGs inventoried in root-primary/figures-fetch.json | supports | All eight images were inspected. Figure 5b supports plate antagonism; Figure 6 separates OD and log gene-copy endpoints; Figure 7 shows the four pot arms; Figure 8 is a conceptual synthesis, not a mediation experiment. Figure 6d does not visually support simple uniform high-SA inhibition of P380, despite stronger Results wording; no replacement quantitative result is inferred. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity; AbundanceEnum; FunctionalRoleEnum; EnvironmentalFactor; EngineeringDesign; GtdbClassification | supports | DOMINANT is ordinal and permits coequal prominence. PATHOGEN_ANTAGONIST identifies suppressive members, not the challenged organism. Environmental factors are environmental conditions; inoculum composition belongs to assembly/cultivation. ENGINEERED and SYNTHETIC are valid here. GTDB mapping/name comparison is not source-isolate genome classification. |
| dataset-schema | src/communitymech/schema/mech_shared.yaml; Dataset and DatasetTypeEnum | supports | Dataset identity, accession, sample types and platform must describe the same independently verified collection; article-level co-reporting does not establish project containment. |
| ontology | ontology-authority.json; Whole bounded receipt | supports | Ten unique ontology pairs across seventeen occurrences match local labels; the four microbial taxon identifiers are species-ranked. |
| semantics | ontology-semantic-notes.json; Whole bounded receipt | supports | Species identity, ordinal inoculum prominence, genotype/phenotype and assay-specific chemistry remain bounded. Prior incubation-setpoint removals are preserved. |
| gtdb | gtdb-bounded-mapping-check.json; Whole bounded receipt | supports | Crosswalk checks substantiate the recorded name-based Dyella fallback and Pseudomonas species-level mapping; they do not classify the exact study isolates. |
| gtdb-reference | rhodanobacter-gtdb-taxonomy-presence.json; Whole bounded receipt | supports | The glycinis_A cluster exists in a pinned local reference taxonomy, but the study strain placement and a crosswalk majority remain unresolved. |
| resources | dataset-verification.json; Whole bounded receipt | supports | Direct NCBI/ENA metadata verifies the four species and BJJ-A/B/C/D strain labels, each in a separate project. Metadata read types differ from the paper genome wording; no raw payload was inspected. |
| platform | dataset-platform-clarification.json; Whole bounded receipt | supports | The paper supports HiSeq2500 for both sequencing arms. Current PRJNA1125171 metadata instead exposes NovaSeq6000 for one public run; preserve this source/archive discrepancy without overwriting the published platform. |
| snippets | snippet-audit.json; Whole bounded receipt | supports | All twenty-four excerpts match direct full XML and the pinned cache using Unicode NFKC/whitespace with inline concatenation. Matching does not validate every attached inference. |
| history | provenance-audit.json; Whole bounded receipt | supports | All three histories and the exact prior graph row were read. Closed issues961–963 document cultivation, chemical and manual-GTDB repairs; previous certification is not inherited beyond its scope. |
| native-target | support-audit.json; Whole bounded receipt | supports | The native network is COMPLETE with three nodes, one arrow and five node-evidence entries. Encoded completeness is 95; this is not proof of source-specific completeness. |
| supplement | supplement-access-audit.json; Whole bounded receipt | supports | Complete inventory of the returned ZIP and current HTML/XML links found main images and video abstracts only. Cited scientific S1–S5/Table S1 remain unread; no global absence or complete source-package claim. |
| source-scope | source-audit.json; Whole bounded receipt | supports | Whole current record, full primary main and all eight main figures were assessed; current-claim completion explicitly excludes unread scientific SI and raw-data reanalysis. |
| independent-source | root-independent-source-audit.json; Whole bounded receipt | supports | Root independently assessed the primary science and current claim boundaries and concurred with three minor findings. |
| adapter | adapter-check.json; Whole bounded receipt | supports | Same-runtime optional adapter discovery is explicitly reused with its original timestamp. No appropriate strain-specific expression-module verification or paid call was substituted for primary evidence. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml; Actual execution 2026-10-21T14:33:58.458487+00:00 to 2026-10-21T14:33:59.284554+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-strict kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml --out /private/tmp/cm-review-session/batch-08/000393/strict-report.tsv; Actual execution 2026-10-21T14:33:58.458817+00:00 to 2026-10-21T14:34:01.113356+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-terms kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml; Actual execution 2026-10-21T14:33:58.458934+00:00 to 2026-10-21T14:34:00.673151+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml; Actual execution 2026-10-21T14:33:59.284810+00:00 to 2026-10-21T14:33:59.379395+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb-domain kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml; Actual execution 2026-10-21T14:33:59.379688+00:00 to 2026-10-21T14:34:01.237244+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-history history/records/Calcium_Tomato_Bacterial_Wilt_SynCom; Actual execution 2026-10-21T14:34:00.673727+00:00 to 2026-10-21T14:34:01.484457+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T14:34:01.485042+00:00 to 2026-10-21T14:34:01.545921+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-references-explained kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml; Actual execution 2026-10-21T14:34:01.546170+00:00 to 2026-10-21T14:34:02.619166+00:00 | supports | Reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00 | supports | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00 | supports | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |

## Limits And Additional Notes

- Completed scientific review concerns current encoded claims, supported by the full main and all eight main figures. It is not certification of the entire source package: cited scientific Figures S1–S5/Table S1 remain unread, including sequence-comparison and pairwise-plate details.
- The actual EPMC returned package was inventoried in full; it contained main images and two video abstracts, not the cited scientific SI document. Ordinary PMC HTML returned a CAPTCHA, OA metadata 404, and a guessed publisher supplemental route failed DNS. No access restriction was bypassed.
- No raw sequence, assembly, statistical model, image-based numerical reanalysis, molecular mediation, viability assay, exact-isolate GTDB classification or video content was independently verified.
- Equal OD and volume do not prove equal cell counts, biomass or persistent abundance. Relative ASVs do not establish colonization by the four sequenced isolates.
- Published HiSeq settings and archive NovaSeq/AMPLICON annotations are separately preserved. One returned public project run does not establish completeness of the 112-sample experiment.
- Main Figure 6d and prose have a compound-response tension; general differential-response graph wording is retained. No replacement quantitative claim or new mechanism is invented.
- All 24 existing snippets match fresh full XML and cache. No canonical, cache, history, generated or saved-review edits; no paid provider, author contact or later target.
- No canonical, cache, history, generated or saved-review file changed; all 25 inspected inputs remain pinned.
- All 24 existing snippets match direct primary full XML and the unchanged cache; narrow evidence placement still matters.
- Completeness 95 and quality 100/raw 125.6666666667 are mechanical scores, not proof of complete source-package access or scientific correctness of dataset classifications.
- No raw sequencing, statistical reproduction, genome classification, molecular mediation assay, model execution, video analysis, author contact, paid provider or later-target work.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T144407Z-calcium-tomato-syncom-record
kind: record
repository: CultureBotAI/CommunityMech
title: Calcium-tomato bacterial wilt SynCom review
started_at: '2026-10-21T14:33:27.756419Z'
finished_at: '2026-10-21T14:44:07.930646Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents reviewed primary science, native/ontology checks
    and supporting provenance; no person-level independence asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The full primary main and all eight figures support the four-member identity
  and qualified three-node, one-arrow graph. Three minor findings concern recoverable
  assay context, inoculum-design placement and separate amplicon/isolate resource
  scope. Cited scientific supplementary figures/table remain unread; current-claim
  completion does not certify those details.
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
  - path: history/records/Calcium_Tomato_Bacterial_Wilt_SynCom/2026-09-20T120926Z-codex-41387930.yaml
    sha256: b96b183365521d89ced30de1b4010a9d2c8bda824d7547e2141682a8de60c4eb
    role: context
  - path: history/records/Calcium_Tomato_Bacterial_Wilt_SynCom/2026-09-20T122242Z-codex-961-963.yaml
    sha256: 6f51cd86ddc9666adb7e4c0257067cfd82df20c0221314ba1f991ef0d484fac3
    role: context
  - path: history/records/Calcium_Tomato_Bacterial_Wilt_SynCom/2026-10-05T142600Z-codex-b12f8f.yaml
    sha256: 827cce28ef1f64a3eaf2d9b271e5267dae3711f14f2424cceb3e95099177d1c8
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
    sha256: 2003158329c3f2113f6239f65b1e6a1b85bd3c19204f7aaf9d90be7f1f5c68f0
    role: target
  - path: references_cache/PMID_41387930.txt
    sha256: 28088317360ce0a54f4245a898a662748ffce070f080cf47f96994f5eaa5588f
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
- target_id: CommunityMech:000393
  path: kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  label: Calcium-Tomato Bacterial Wilt SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
    role: canonical_record
scope:
  description: Entire record and every node/arrow assessed using direct primary main,
    all eight main figures, source-specific archives, authority, history and native
    checks, with explicit unread scientific-SI limits.
  selection: Only released CommunityMech:000393 in the owned batch 08 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000393
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000393
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support, viability measures or correct dataset containment.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000393
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-08/000393/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support, viability measures or correct dataset containment.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000393
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support, viability measures or correct dataset containment.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000393
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support, viability measures or correct dataset containment.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000393
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support, viability measures or correct dataset containment.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000393
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Calcium_Tomato_Bacterial_Wilt_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support, viability measures or correct dataset containment.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000393
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support, viability measures or correct dataset containment.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000393
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support, viability measures or correct dataset containment.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000393
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse, not a focal scientific failure
    or inherited source certification.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000393
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse, not a focal scientific failure
    or inherited source certification.
- check_id: source-identity
  name: Primary article identity
  status: passed
  required: true
  summary: Direct PubMed, EPMC, Crossref and full XML/publisher main agree on article
    identity.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - pubmed
  - epmc
  - crossref
  - source-scope
- check_id: scientific-source
  name: Current claim verification
  status: passed
  required: true
  summary: Entire primary scientific main and all eight main figures support assessment
    of current qualified claims; source-specific archive and authority checks are
    separately bounded.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - source-scope
  - independent-source
  - figures
- check_id: scientific-supplement
  name: Cited scientific supplement inspection
  status: unavailable
  required: false
  summary: Returned package contains main images and video abstracts, not the cited
    S1–S5/Table S1 document. Those details remain unread. No SI-only numerical or
    sequence-level result is certified.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - supplement
  - source-scope
- check_id: cross-mech
  name: Exact focal medium linkage
  status: not_applicable
  required: false
  summary: Named LB and nutrient broth describe different preparations and assay dilutions;
    no exact CultureMech recipe correspondence was established or required for the
    current findings.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - assembly
  - compounds
  - exudate-assay
- check_id: structured-adapter
  name: Optional structured expression adapter
  status: unavailable
  required: false
  summary: Same-runtime discovery is explicitly reused; no exact expression-module
    claim was established and no external checkout adapter was executed.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  locator: Entire record, three community-level nodes and one HYPOTHESIZED arrow
  summary: The record represents the four-member calcium-selected tomato SynCom, with
    explicit distinctions among isolated-compound assays, whole-exudate qPCR and a
    separate low-calcium pot intervention.
  support: supports
  accessed_at: '2026-10-21T14:42:51.134794Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41387930&retmode=xml
  locator: Article identity and available abstract
  summary: The focal PMID, DOI, title and abstract agree.
  support: supports
  accessed_at: '2026-10-21T14:33:58.871977Z'
  snapshot_sha256: bbe35d6fee3c9160f8269f190ae9d04cf96e527831a512756c3f67fa10244d13
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41387930%20AND%20SRC:MED&format=json&resultType=core
  locator: Article identity and available abstract
  summary: Direct article metadata identifies the open primary article and PMC12817675.
  support: supports
  accessed_at: '2026-10-21T14:33:59.184601Z'
  snapshot_sha256: 3066331fcf79ff77a539a0e6b6b781aaf217aa5f978e36ccf5aeb334f412e294
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1186/s40168-025-02228-1
  locator: Article identity and available abstract
  summary: DOI metadata agrees with the focal calcium/tomato study.
  support: supports
  accessed_at: '2026-10-21T14:33:58.897707Z'
  snapshot_sha256: 40677d5ad5691b0c1c27f2d44aaa5f7d7138d9558ca9bdc3fea4b133b73bfb8b
- evidence_id: identity
  kind: primary_source
  reference: PMID:41387930
  locator: 'Methods: Bacterial isolation and taxonomic identification; Construction
    of synthetic community; Results/Figure5'
  summary: Four isolates from surface-sterilized calcium-treated tomato roots were
    identified as Dyella japonica, Rhodanobacter glycinis, Paenibacillus polymyxa
    and Pseudomonas aeruginosa. Tomato is the host and Ralstonia solanacearum P380
    the challenged pathogen, not additional SynCom members.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135037Z'
  snapshot_sha256: 06448e424461373171d81d3864bd44f4c0458a86bec328d358baaa520a291046
- evidence_id: assembly
  kind: primary_source
  reference: PMID:41387930
  locator: 'Methods: Construction of synthetic community; In vitro interactions among
    members'
  summary: LB-grown pellets were resuspended in sterile water, individually adjusted
    to OD600 1 and mixed 1:1:1:1. Exudate coculture used a separate OD600 0.1 ± 0.05
    combined suspension. The 28 C/150 rpm preparation is expressly reported for the
    separate plate-pair assay and must not be restored as a final-assembly or exudate
    incubation setpoint.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135106Z'
  snapshot_sha256: 06448e424461373171d81d3864bd44f4c0458a86bec328d358baaa520a291046
  quote: mixed in equal volumes (1:1:1:1)
- evidence_id: roles
  kind: primary_source
  reference: PMID:41387930
  locator: 'Methods: Antagonistic activity against R. solanacearum; Results/Figure5b–c'
  summary: Plate tests establish antagonistic activity for all four isolates. Gene
    annotation describes potential plant-growth-related functions, not measured production,
    expression or the necessary mechanism of pot protection. The local taxonomy identity
    excerpt does not itself establish the role; narrow plate-assay evidence is available.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135173Z'
  snapshot_sha256: 06448e424461373171d81d3864bd44f4c0458a86bec328d358baaa520a291046
- evidence_id: compounds
  kind: primary_source
  reference: PMID:41387930
  locator: 'Methods: Growth of antagonistic bacteria in response to Ca and Ca-enriched
    root metabolites; Figure6c–f'
  summary: Separate additions used calcium chloride in NB and salicylic acid/sucrose/trehalose
    in one-tenth LB. Their concentrations, 28 C/150 rpm conditions and 4/12/24 h readout
    belong to those assays. Root-tissue metabolomics and compound growth responses
    do not establish the composition or necessary mediators of whole exudates.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135238Z'
  snapshot_sha256: 06448e424461373171d81d3864bd44f4c0458a86bec328d358baaa520a291046
- evidence_id: exudate-preparation
  kind: primary_source
  reference: PMID:41387930
  locator: 'Methods: Effect of whole root exudates on growth'
  summary: 'Thirty-day seedlings underwent five days in 0 or 20 mM calcium Hoagland
    solution, followed by rinsing and 48 h collection in 50 mL deionized water per
    plant. Collection conditions were 28 C and 16/8 h light/dark. Per treatment, 1100
    mL was filtered, lyophilized and redissolved in 22 mL: nominal fiftyfold concentration
    of the collected solution, not a measured concentration of any one metabolite
    or calcium ion.'
  support: supports
  accessed_at: '2026-10-21T14:42:51.135308Z'
  snapshot_sha256: 06448e424461373171d81d3864bd44f4c0458a86bec328d358baaa520a291046
- evidence_id: exudate-assay
  kind: primary_source
  reference: PMID:41387930
  locator: 'Methods: Effect of whole root exudates on growth; Results/Figure6a–b'
  summary: The coculture contains 100 microlitres half NB, 10 pathogen suspension,
    10 SynCom and 30 concentrated exudate solution, totaling 150 microlitres. Samples
    at 6/12/24/48 h were quantified by pathogen-specific qPCR. The separate single-culture
    OD assay totals 140 microlitres; it is not the same preparation or endpoint.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135375Z'
  snapshot_sha256: 06448e424461373171d81d3864bd44f4c0458a86bec328d358baaa520a291046
- evidence_id: pot-assay
  kind: primary_source
  reference: PMID:41387930
  locator: 'Methods: Biocontrol ability of SynCom; Figure7'
  summary: The final intervention uses 80 g sterilized nursery soil, calcium applied
    one week after sprouting, 10 mL pathogen at the triloba stage and 10 mL SynCom
    one week later. Four calcium/SynCom treatment groups are compared. This is distinct
    from the earlier 2 kg soil calcium-gradient experiment, its 50 mL pathogen challenge
    and 20/30-day root sampling.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135441Z'
  snapshot_sha256: 06448e424461373171d81d3864bd44f4c0458a86bec328d358baaa520a291046
- evidence_id: pot-outcome
  kind: primary_source
  reference: PMID:41387930
  locator: 'Results: Combined application of SynCom and Ca controlled bacterial wilt;
    Figure7; Statistical analysis'
  summary: The source reports wilt incidence from 74.07% to zero for the combined
    low-dose treatment. One-way ANOVA/LSD treatment contrasts do not establish a factorial
    interaction term, pathogen eradication, universal protection or necessity of high-dose
    host-defense responses.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135505Z'
  snapshot_sha256: 06448e424461373171d81d3864bd44f4c0458a86bec328d358baaa520a291046
  quote: with wilt incidence dropping from 74.07 to 0%
- evidence_id: resource-source
  kind: primary_source
  reference: PMID:41387930
  locator: 'Data availability; Methods: Root and rhizosphere microbial community;
    Genome sequencing'
  summary: The paper separately assigns amplicons to PRJNA1125171 and names four isolate
    runs. Methods reports HiSeq2500 PE250 for amplicons and HiSeq2500 PE150 for isolate
    genome sequencing; current archive metadata requires a separate, explicitly scoped
    comparison.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135572Z'
  snapshot_sha256: 06448e424461373171d81d3864bd44f4c0458a86bec328d358baaa520a291046
- evidence_id: figures
  kind: primary_source
  reference: PMID:41387930
  locator: All eight main figures; direct publisher PNGs inventoried in root-primary/figures-fetch.json
  summary: All eight images were inspected. Figure 5b supports plate antagonism; Figure
    6 separates OD and log gene-copy endpoints; Figure 7 shows the four pot arms;
    Figure 8 is a conceptual synthesis, not a mediation experiment. Figure 6d does
    not visually support simple uniform high-SA inhibition of P380, despite stronger
    Results wording; no replacement quantitative result is inferred.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135602Z'
  snapshot_sha256: 5f970445977cfb85c8383930f39a2543a5daf47d1e7ff379b96eea58dc735b1d
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity; AbundanceEnum; FunctionalRoleEnum; EnvironmentalFactor;
    EngineeringDesign; GtdbClassification
  summary: DOMINANT is ordinal and permits coequal prominence. PATHOGEN_ANTAGONIST
    identifies suppressive members, not the challenged organism. Environmental factors
    are environmental conditions; inoculum composition belongs to assembly/cultivation.
    ENGINEERED and SYNTHETIC are valid here. GTDB mapping/name comparison is not source-isolate
    genome classification.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135656Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: dataset-schema
  kind: authority
  reference: src/communitymech/schema/mech_shared.yaml
  locator: Dataset and DatasetTypeEnum
  summary: Dataset identity, accession, sample types and platform must describe the
    same independently verified collection; article-level co-reporting does not establish
    project containment.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135680Z'
  snapshot_sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded receipt
  summary: Ten unique ontology pairs across seventeen occurrences match local labels;
    the four microbial taxon identifiers are species-ranked.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135715Z'
  snapshot_sha256: 58ea38c004ec101864a6455d4f212bfcb3b2985d8c2c777e66335088422130dc
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole bounded receipt
  summary: Species identity, ordinal inoculum prominence, genotype/phenotype and assay-specific
    chemistry remain bounded. Prior incubation-setpoint removals are preserved.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135744Z'
  snapshot_sha256: 0c3682ae95709c668820973018aca58836a65a4c53c0dea9c2753ec2b96378c4
- evidence_id: gtdb
  kind: authority
  reference: gtdb-bounded-mapping-check.json
  locator: Whole bounded receipt
  summary: Crosswalk checks substantiate the recorded name-based Dyella fallback and
    Pseudomonas species-level mapping; they do not classify the exact study isolates.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135771Z'
  snapshot_sha256: 761af0eb90a73761574bc48b30ceb5b2d63bbcb3f7f30b76005c2132c35b3995
- evidence_id: gtdb-reference
  kind: authority
  reference: rhodanobacter-gtdb-taxonomy-presence.json
  locator: Whole bounded receipt
  summary: The glycinis_A cluster exists in a pinned local reference taxonomy, but
    the study strain placement and a crosswalk majority remain unresolved.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135797Z'
  snapshot_sha256: 77c04b6e8d29f3e25f519021e7c2faac6c896113005a58be55fc6fd6a3578d70
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded receipt
  summary: Direct NCBI/ENA metadata verifies the four species and BJJ-A/B/C/D strain
    labels, each in a separate project. Metadata read types differ from the paper
    genome wording; no raw payload was inspected.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135825Z'
  snapshot_sha256: cb86f48f1664085905b4fb5201f2c6f4818ce04da9380d6522065bd295894831
- evidence_id: platform
  kind: database
  reference: dataset-platform-clarification.json
  locator: Whole bounded receipt
  summary: The paper supports HiSeq2500 for both sequencing arms. Current PRJNA1125171
    metadata instead exposes NovaSeq6000 for one public run; preserve this source/archive
    discrepancy without overwriting the published platform.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135850Z'
  snapshot_sha256: 0c17d40e5cddf80385da178ece12064066f01ddeb7b1c4a6c28e67323cb7228f
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded receipt
  summary: All twenty-four excerpts match direct full XML and the pinned cache using
    Unicode NFKC/whitespace with inline concatenation. Matching does not validate
    every attached inference.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135879Z'
  snapshot_sha256: c994be8f6dd13f4813392c620c51a0c92fa5c0014c1c64a95a48fb83511ae590
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded receipt
  summary: All three histories and the exact prior graph row were read. Closed issues961–963
    document cultivation, chemical and manual-GTDB repairs; previous certification
    is not inherited beyond its scope.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135912Z'
  snapshot_sha256: d720dc5778069f1eff0c465275591815c1dd4e59d52920a8d26a9e39787c5750
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded receipt
  summary: The native network is COMPLETE with three nodes, one arrow and five node-evidence
    entries. Encoded completeness is 95; this is not proof of source-specific completeness.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135932Z'
  snapshot_sha256: 0db41d5a5388d6da25557cfd5fb7ed75f31603304e18b6861f5ddeecef4eea07
- evidence_id: supplement
  kind: validation
  reference: supplement-access-audit.json
  locator: Whole bounded receipt
  summary: Complete inventory of the returned ZIP and current HTML/XML links found
    main images and video abstracts only. Cited scientific S1–S5/Table S1 remain unread;
    no global absence or complete source-package claim.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135956Z'
  snapshot_sha256: 57db46223037876d47158d9ada70c9f64aa9d26dd4c0ca7066b8df42f76859c1
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded receipt
  summary: Whole current record, full primary main and all eight main figures were
    assessed; current-claim completion explicitly excludes unread scientific SI and
    raw-data reanalysis.
  support: supports
  accessed_at: '2026-10-21T14:42:51.135978Z'
  snapshot_sha256: 39220fff5bb993d9a6a1b26038e6e3eb53ed71b7637cb9c31a0ed8d4447867e1
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded receipt
  summary: Root independently assessed the primary science and current claim boundaries
    and concurred with three minor findings.
  support: supports
  accessed_at: '2026-10-21T14:42:51.136005Z'
  snapshot_sha256: 55c9cc1c5f735c07d7ffcea46baf3a78d0416d5d2f18a36efa518e9718b5228b
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Whole bounded receipt
  summary: Same-runtime optional adapter discovery is explicitly reused with its original
    timestamp. No appropriate strain-specific expression-module verification or paid
    call was substituted for primary evidence.
  support: supports
  accessed_at: '2026-10-21T14:42:51.136029Z'
  snapshot_sha256: 33a4e9bebba3dfa442ef80aca0321571c05979c494fc5d2b9c73b36a96c173a5
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  locator: Actual execution 2026-10-21T14:33:58.458487+00:00 to 2026-10-21T14:33:59.284554+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T14:33:59.284554Z'
  snapshot_sha256: bcd06a1b1db7d227ffcf4ec4ffc398b0b4897f18f4e62d90db0cd1248c3a8196
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-08/000393/strict-report.tsv
  locator: Actual execution 2026-10-21T14:33:58.458817+00:00 to 2026-10-21T14:34:01.113356+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T14:34:01.113356Z'
  snapshot_sha256: 1c838f8bb672de64ef757debfd77f81d996347169cbd1ceaa32c985145b9ea43
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  locator: Actual execution 2026-10-21T14:33:58.458934+00:00 to 2026-10-21T14:34:00.673151+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T14:34:00.673151Z'
  snapshot_sha256: 547ff1c77005fb088b998051ab07eb1a4a7886e271b0b81d27b83ab29f5c7ad7
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  locator: Actual execution 2026-10-21T14:33:59.284810+00:00 to 2026-10-21T14:33:59.379395+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T14:33:59.379395Z'
  snapshot_sha256: af24ee712a6871f83ab1d418c0eb87e7d38028dc4b6546c7ec6e8e1f4278dc2e
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  locator: Actual execution 2026-10-21T14:33:59.379688+00:00 to 2026-10-21T14:34:01.237244+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T14:34:01.237244Z'
  snapshot_sha256: 70e27365775809abab420f380ed8d5b8db2b298557a47d9a573e7c1f15adb86f
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Calcium_Tomato_Bacterial_Wilt_SynCom
  locator: Actual execution 2026-10-21T14:34:00.673727+00:00 to 2026-10-21T14:34:01.484457+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T14:34:01.484457Z'
  snapshot_sha256: 34ea061d09879c97531ea582fcec3c0f03552a0a4cd12fad7f41b39dca39eec8
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T14:34:01.485042+00:00 to 2026-10-21T14:34:01.545921+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T14:34:01.545921Z'
  snapshot_sha256: fdc466ec14b52f37e8a6b2db1dd5bf0333933012065384af3357db6995c06cd9
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
  locator: Actual execution 2026-10-21T14:34:01.546170+00:00 to 2026-10-21T14:34:02.619166+00:00
  summary: Reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T14:34:02.619166Z'
  snapshot_sha256: f1ad6a5cf0ce3e3a31ab182ebf285f9dc5785192b222fda0f9cb70cde260997a
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:11.311177Z'
  snapshot_sha256: 2d17097db768619fa7fea156f7c37781fa9cd463a6abdce6f529112518848cf0
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:15.408522Z'
  snapshot_sha256: 1332cfd7980ec54d517d625aff43fa6328c1a19fd405a7aef071f78af9774f3f
assessments:
- assessment_id: identity
  area: identity
  topic: Four-member SynCom and external host/pathogen
  outcome: supported
  summary: Retain all four source species, deliberate assembly and tomato-root context.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - identity
  - assembly
  - ontology
  - resources
  dimensions:
  - name: community_scope
    value: Defined four-isolate synthetic community
    definition: Not the whole calcium-enriched root microbiome or the external pathogen.
    evidence_ids:
    - identity
  - name: taxon_rank
    value: Four species-grounded isolates
    definition: Taxon identifiers describe species; sequencing runs and strain designations
      are separate entities.
    evidence_ids:
    - ontology
    - resources
  - name: strain
    value: BJJ-A/B/C/D respectively in direct archive attributes
    definition: Optional structured precision can enrich the already source-linked
      isolates without inventing a strain taxid.
    evidence_ids:
    - resources
  - name: grounding_status
    value: Existing GTDB uncertainty retained
    definition: Manual glycinis_A name pin and other crosswalk results do not certify
      exact-isolate placement; preserve candidates and uncertainty.
    evidence_ids:
    - gtdb
    - gtdb-reference
    - semantics
  - name: environment
    value: Tomato root-associated soil and laboratory exudate assays
    definition: Root isolation, soil application and plate assays are distinct physical
      contexts.
    evidence_ids:
    - identity
    - exudate-assay
    - pot-assay
  - name: medium
    value: LB preparation and half NB exudate coculture
    definition: Do not merge the other isolation, compound-screening or plate-pair
      media into a universal SynCom recipe.
    evidence_ids:
    - assembly
    - compounds
    - exudate-assay
  - name: evidence_tier
    value: Direct full main/eight figures plus archive metadata
    definition: Scientific SI and raw sequencing payloads remain uninspected.
    evidence_ids:
    - source-scope
    - supplement
- assessment_id: state
  area: scope
  topic: State, origin and category
  outcome: supported
  summary: Retain ENGINEERED state, SYNTHETIC origin and RHIZOSPHERE category.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - assembly
  - identity
  - schema
  details: The deliberate four-isolate assembly is explicit. No equilibrium, genetic
    modification or permanent in-situ community stability is inferred. Tomato-root
    source and applied rhizosphere context are compatible with the broad environmental
    terms, while exudate assays remain laboratory experiments.
- assessment_id: roles
  area: evidence
  topic: Antagonist roles, ordinal prominence and local evidence
  outcome: supported
  summary: Retain PATHOGEN_ANTAGONIST for all four members and coequal inoculum-level
    DOMINANT.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - roles
  - assembly
  - schema
  - semantics
  details: Figure 5b and the plate Methods establish antagonist activity, despite
    the local taxonomy excerpts naming identity alone. Add narrow role evidence with
    assay scope. Equal-volume OD-normalized preparation is not a measured equal cell
    fraction or persistent root abundance. Predicted gene functions do not establish
    expression, production or a necessary mechanism of protection.
- assessment_id: grounding
  area: grounding
  topic: NCBI and GTDB correspondence
  outcome: supported
  summary: Keep source species labels and transparent GTDB uncertainty; no automatic
    isolate-level reassignment.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - ontology
  - gtdb
  - gtdb-reference
  - resources
  details: The manually curated Rhodanobacter pin is an existing plausible reference-cluster
    choice without source-run genome classification. The exact 582702 crosswalk and
    species-name rows are not present in the pinned table; cluster existence is independently
    verified. Dyella uses another strain’s species-name fallback; Pseudomonas has
    an aggregate species mapping; Paenibacillus stays ambiguous. These are bounded
    unresolved mapping questions, not demonstrated wrong NCBI species identities.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain differential compound responses without interorganism colonization
    or exudate-mediator claims.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - compounds
  - figures
  details: Calcium and purified metabolites were tested separately in specified media.
    Tissue abundance is not exudate concentration. The broad differential-response
    phrasing accommodates compound/time-specific responses and the source prose/SA-panel
    tension; it does not prove each compound inhibits the pathogen under every tested
    condition.
- assessment_id: arrow-0-1
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: Retain the compound-to-whole-exudate link only as HYPOTHESIZED.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - compounds
  - exudate-preparation
  - exudate-assay
  details: No selective depletion/add-back or equivalent test identifies these molecules
    as necessary whole-exudate mediators. Preserve the current explicit hypothesis,
    with no stronger causal promotion or new exudate-to-pot arrow.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain whole-exudate/SynCom-associated reduction in pathogen qPCR gene
    copies.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - exudate-assay
  - figures
  details: The 150 microlitre coculture is distinct from the 140 microlitre single-culture
    OD assay. Gene copies are not viable-cell counts. The 20 mM value describes seedling
    conditioning, not measured calcium in concentrated exudates or the final well.
    No reciprocal-negative competition or unique mediator is established.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: Retain the source-reported 74.07% to 0% disease-incidence result under
    the tested low-dose pot treatment.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - pot-assay
  - pot-outcome
  - figures
  details: Figure 7 shows the four arms and zero observed wilt in the combined group.
    Preserve the one-week pathogen-to-SynCom sequence. Disease incidence does not
    establish pathogen eradication, field efficacy, long-term stability or a formal
    factorial interaction. The earlier high-calcium host-defense experiment is a separate
    context.
- assessment_id: ingredients
  area: grounding
  topic: Related ingredients and metabolite evidence
  outcome: supported
  summary: Retain the named tested compounds and calcium salt with dose and evidence
    boundaries.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - compounds
  - ontology
  - exudate-preparation
  - figures
  details: Calcium doses per kg soil are elemental-Ca basis, not equal CaCl2 mass.
    Root-tissue metabolomics is not exudate chemistry. Salicylic-acid inhibition wording
    follows the main prose, but Figure 6d does not show uniform high-dose inhibition;
    retain explicit source attribution and response specificity rather than deriving
    a new numeric result from pixels. Generic trehalose does not assert an anomer.
- assessment_id: cultivation
  area: completeness
  topic: Exudate preparation, pot context and role evidence
  outcome: concern
  summary: Recover the concentrated-exudate preparation and final-pot protocol without
    importing unrelated conditions.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - exudate-preparation
  - exudate-assay
  - pot-assay
  - roles
  details: The record correctly gives150 microlitres, preparation OD values and sampling
    times, but omits the 1100-to 22 mL concentration step and separate 80 g nursery-soil/10
    mL inoculation context. These are source-supported reproducibility details. Do
    not restore the 28 C/150 rpm final-culture settings removed by prior review.
- assessment_id: factor-placement
  area: representation
  topic: environmental_factors[0]
  outcome: concern
  summary: The equal-ratio inoculum entry is assembly information, not an environmental
    condition.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - assembly
  - schema
  details: Its content is valid and already represented in engineering_design and
    growth_media. Preserve it in the appropriate location while retaining the actual
    calcium/exudate treatment factors.
- assessment_id: dataset
  area: provenance
  topic: associated_datasets[0] and source-linked isolates
  outcome: concern
  summary: Separate the amplicon project from four isolate projects and retain source/archive
    disagreement explicitly.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - resource-source
  - resources
  - platform
  - dataset-schema
  details: PRJNA1125171 does not contain the four verified isolate runs. Their metadata
    identify distinct projects and BJJ strain names. Paper genome-sequencing claims
    conflict with AMPLICON/GENOMIC/PCR annotations, and paper HiSeq conflicts with
    the one currently returned project run’s NovaSeq. These are scope and provenance
    limits, not proof of payload content or complete project coverage.
- assessment_id: prior-review
  area: provenance
  topic: History and retained uncertainty
  outcome: supported
  summary: Retain prior graph, calcium-ingredient and cultivation repairs and open
    mechanism questions.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - history
  - snippets
  - source-scope
  details: The full present main/figure review does not restore a direct exudate-to-pot
    mediation link or infer exact-strain colonization from relative ASVs. Current
    graph and discussions already separate assay tiers. Native/reference success does
    not settle study-level causal gaps.
- assessment_id: validation
  area: schema
  topic: Native checks and claim-specific evidence
  outcome: supported
  summary: All eight focused native gates pass; three bounded provenance/representation
    findings remain.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - ontology
  - check-validate
  - check-validate-references-explained
  - source-scope
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Current scores include the encoded dataset and three environmental-factor
    entries; scores do not certify their placement.
  target_ids:
  - CommunityMech:000393
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 95
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role component +5 environment +10 at least
      three factors +10 at least three interaction nodes +10 growth media +5 dataset
      +5 metabolites; no external-resource bonus.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0/P2=0/P3=3/P4=0; five evidence/three nodes gives 16.6666666667, COMPLETE
      adds 15; raw 125.6666666667 capped 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 3
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
findings:
- finding_id: assay-context
  issue_key: cm-000393-assay-context
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded method/provenance completeness; no incorrect
    focal membership, mandatory cultivation field or new mechanism is asserted.'
  rule_id: review-checklist.claim-specific-context-and-resource-provenance
  status: open
  certainty: confirmed
  title: Recover concentrated-exudate and final-pot context
  description: The record gives the coculture recipe and sampling times but omits
    the exudate concentration step and final 80 g pot setup. Available narrow antagonist
    evidence can also replace reliance on identity-only local excerpts. Recover these
    details with their experiment-specific limits, preserving the prior removal of
    unsupported final-culture setpoints.
  target_ids:
  - CommunityMech:000393
  field_paths:
  - growth_media[1].preparation_notes
  - cultivation_setup
  - engineering_design.inoculation_strategy
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  - taxonomy[2].evidence
  - taxonomy[3].evidence
  - growth_media[0]
  evidence_ids:
  - exudate-preparation
  - exudate-assay
  - pot-assay
  - roles
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
    role: canonical_record
- finding_id: inoculum-factor
  issue_key: cm-000393-inoculum-factor
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: local field placement; retain the valid composition and
    actual calcium treatments.'
  rule_id: review-checklist.claim-specific-context-and-resource-provenance
  status: open
  certainty: confirmed
  title: Keep inoculum assembly outside environmental conditions
  description: environmental_factors[0] describes the defined four-member inoculum,
    which is already represented as assembly and preparation. Its content is source-supported,
    but it is not an environmental condition.
  target_ids:
  - CommunityMech:000393
  field_paths:
  - environmental_factors[0]
  - engineering_design
  - growth_media[0]
  evidence_ids:
  - assembly
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
    role: canonical_record
- finding_id: dataset-partition
  issue_key: cm-000393-dataset-partition
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: correct project identity is retained, but dataset containment
    and technical provenance need partitioning; no raw-payload misidentification or
    complete-project inventory is proven.'
  rule_id: review-checklist.claim-specific-context-and-resource-provenance
  status: open
  certainty: confirmed
  title: Separate amplicon and isolate resource scope
  description: The PRJNA1125171 dataset entry includes raw isolate-genome sample types,
    while direct run metadata places each isolate in a separate project. Keep the
    paper and portal platform/read-type disagreements explicit; neither source is
    silently substituted for the other.
  target_ids:
  - CommunityMech:000393
  field_paths:
  - associated_datasets[0]
  - taxonomy[0].strain_designation
  - taxonomy[1].strain_designation
  - taxonomy[2].strain_designation
  - taxonomy[3].strain_designation
  evidence_ids:
  - resource-source
  - resources
  - platform
  - dataset-schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
    role: canonical_record
actions:
- action_id: recover-assay-context
  description: Add reproducible source context while retaining separate experimental
    arms and evidence tiers.
  finding_ids:
  - assay-context
  target_ids:
  - CommunityMech:000393
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - State that collected exudate was filtered, lyophilized and reconstituted from
    1100 mL to 22 mL before adding 30 microlitres per coculture. Describe nominal
    fiftyfold concentration of collected solution, not measured concentrations of
    calcium, salicylic acid, sucrose or trehalose.
  - Keep seedling conditioning at 0/20 mM calcium for five days separate from 48 h
    collection in deionized water after rinsing. The 28 C and 16/8 h light/dark regime
    belongs to conditioning/collection, not automatically to final coculture incubation.
  - Preserve the 150 microlitre coculture recipe, OD600 0.1 ± 0.05 preparation and
    6/12/24/48 h qPCR sampling. Do not merge the 140 microlitre single-culture OD
    assay or the purified-compound assay conditions. Do not restore unsupported final
    SynCom/coculture 28 C or 150 rpm settings.
  - 'Add a distinct final-pot context: 80 g sterilized nursery soil, calcium one week
    after sprouting, 10 mL pathogen at the triloba stage and 10 mL SynCom one week
    later, with the source-reported replicate description. Do not transfer the 2 kg
    gradient soil, 50 mL challenge or 20/30-day sampling schedule.'
  - Attach narrow plate-antagonism evidence for each supported role while retaining
    genomic traits as predictions. Keep DOMINANT explicitly at coequal prepared-inoculum
    scope; OD normalization does not measure equal cell fractions or in-planta persistence.
  - Preserve all three nodes and the single HYPOTHESIZED arrow. Compound responses
    should remain dose/time/source-specific, with the main-prose versus Figure 6d
    SA discrepancy explicit when asserting inhibition; no replacement numeric effect,
    direct viable-cell loss or causal pot mediator is inferred. Re-run the native
    checks after separately authorized curation.
  - Treat OD600 1 as the density of the harvested-cell suspension prepared for equal-volume
    assembly, not an established starting inoculum density for LB growth. Move or
    explicitly qualify growth_media[0].inoculum_size and inoculum_unit in preparation
    notes accordingly. The source reports harvested-pellet resuspension in sterile
    water but no explicit wash step; remove wash wording from engineering_design.inoculation_strategy
    and growth_media[0].preparation_notes unless direct source support is supplied.
- action_id: move-inoculum-design
  description: Represent the existing inoculum facts in assembly/preparation fields.
  finding_ids:
  - inoculum-factor
  target_ids:
  - CommunityMech:000393
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Remove environmental_factors[0] after preserving its 1:1:1:1 / OD600 1 preparation
    facts and evidence in engineering_design or the existing preparation notes. Do
    not discard the valid source evidence.
  - Retain the actual 20 mM seedling-conditioning and 100 mg Ca/kg soil treatment
    contexts as distinct factors; do not turn them into one uniform medium or an exact
    final-well calcium concentration. Validate the revised field placement.
- action_id: partition-public-resources
  description: Keep project/run/strain associations and conflicting technical metadata
    traceable.
  finding_ids:
  - dataset-partition
  target_ids:
  - CommunityMech:000393
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Calcium_Tomato_Bacterial_Wilt_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Scope PRJNA1125171 to the source-reported root/rhizosphere amplicon study and
    use a compatible dataset type. Remove isolate-run sample types from that project
    entry; a shared article does not establish project containment.
  - Represent SRR33220703/BJJ-A/Dyella under PRJNA1252363, SRR33220740/BJJ-B/Rhodanobacter
    under PRJNA1252364, SRR33221449/BJJ-C/Paenibacillus under PRJNA1252366 and SRR33221452/BJJ-D/Pseudomonas
    under PRJNA1252367, or link the runs individually with the verified project relationships.
    The exact strain names are optional structured enrichment, not new organisms.
  - Preserve the paper HiSeq2500 PE250 amplicon and PE150 genome wording alongside
    the portal’s currently returned NovaSeq6000 amplicon-project record and AMPLICON/GENOMIC/PCR
    isolate annotations. Mark these unresolved source/archive disagreements; do not
    certify raw genome content or replace the source platform merely from one portal
    response.
  - Do not equate one returned project run with the complete 112-sample experiment,
    infer assembly availability, or use run identity to certify GTDB strain placement.
    Keep the existing manual glycinis_A uncertainty and Paenibacillus candidates;
    any later genome-based re-grounding needs direct isolate-specific evidence.
  - Preserve source citations, the original repaired history and named public identifiers;
    re-run resource/reference, schema, ontology, GTDB/domain and history validation
    after authorized curation.
limitations:
- 'Completed scientific review concerns current encoded claims, supported by the full
  main and all eight main figures. It is not certification of the entire source package:
  cited scientific Figures S1–S5/Table S1 remain unread, including sequence-comparison
  and pairwise-plate details.'
- The actual EPMC returned package was inventoried in full; it contained main images
  and two video abstracts, not the cited scientific SI document. Ordinary PMC HTML
  returned a CAPTCHA, OA metadata 404, and a guessed publisher supplemental route
  failed DNS. No access restriction was bypassed.
- No raw sequence, assembly, statistical model, image-based numerical reanalysis,
  molecular mediation, viability assay, exact-isolate GTDB classification or video
  content was independently verified.
- Equal OD and volume do not prove equal cell counts, biomass or persistent abundance.
  Relative ASVs do not establish colonization by the four sequenced isolates.
- Published HiSeq settings and archive NovaSeq/AMPLICON annotations are separately
  preserved. One returned public project run does not establish completeness of the
  112-sample experiment.
- Main Figure 6d and prose have a compound-response tension; general differential-response
  graph wording is retained. No replacement quantitative claim or new mechanism is
  invented.
- All 24 existing snippets match fresh full XML and cache. No canonical, cache, history,
  generated or saved-review edits; no paid provider, author contact or later target.
notes:
- No canonical, cache, history, generated or saved-review file changed; all 25 inspected
  inputs remain pinned.
- All 24 existing snippets match direct primary full XML and the unchanged cache;
  narrow evidence placement still matters.
- Completeness 95 and quality 100/raw 125.6666666667 are mechanical scores, not proof
  of complete source-package access or scientific correctness of dataset classifications.
- No raw sequencing, statistical reproduction, genome classification, molecular mediation
  assay, model execution, video analysis, author contact, paid provider or later-target
  work.
tags:
- record-review
- calcium
- tomato
- syncom
- main-assessed
- bounded-supplements
- batch-08
```
