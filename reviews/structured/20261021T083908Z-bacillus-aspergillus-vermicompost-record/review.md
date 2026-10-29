# Bacillus-Aspergillus vermicomposting SynCom: whole-record review

- Review: 20261021T083908Z-bacillus-aspergillus-vermicompost-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T08:33:46.287723Z
- Finished UTC: 2026-10-21T08:39:08.843047Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major finding groups unsupported syntrophy, gene activation and two causal mediations while preserving measured treatment effects. Three minor findings recover cultivation/design, source-strain provenance and measured feedstock-metal context. All three nodes and both arrows were assessed individually. Seven focused gates and cache preflight pass; corpus network warning failures remain explicit.

## Scope And Provenance

Entire record: all four species, three nodes, two arrows and thirteen evidence occurrences. Fresh main text, Tables S1-S9, supplementary captions S1-S4, visual S1 and relevant main figures were assessed; no raw metagenome, sequence, enzyme or statistical reanalysis was performed.

Selection: Final assigned maintained path of batch04 after CommunityMech:000358; one resolved four-member inoculant and its vermicomposting application.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c6e5a9b9af2d05e12eaafb2555a53f3a079268f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000473 | kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml | maintained | Bacillus and Aspergillus Lignocellulose-Degrading Co-Vermicomposting SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000473 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000473 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000473 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000473 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000473 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000473 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000473 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000473 | Target native references passed; all thirteen snippets also match fresh XML. |
| audit-network | failed | True | CommunityMech:000473 | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-network-quality | failed | True | CommunityMech:000473 | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| Publication identity and full scientific assessment | passed | True | CommunityMech:000473 | Fresh main text, all supplementary tables/captions and relevant figures support a complete source assessment. |
| Bounded source-code and dataset inventory | passed | True | CommunityMech:000473 | Supplementary source codes were recovered; no deposited inoculant/metagenome accession was identified in the inspected material. |
| Encoded medium and ingredient-Mech links | not_applicable | False | CommunityMech:000473 | No CultureMech or MediaIngredientMech ID is encoded, and no exact external recipe equivalence was certified. |
| Optional structured source adapter | unavailable | False | CommunityMech:000473 | Same-runtime discovery was reused; no strain-module coverage was queried. |

## Scientific And Domain Assessments

### Inoculant, compost community and study design

identity: supported. Targets: CommunityMech:000473.

Four source species form the applied inoculant, while measured community functions and quality belong to the broader compost system.

### All four species, source codes, roles and prominence

grounding: concern. Targets: CommunityMech:000473.

Species membership and broad degradation roles are supported, but source strain codes and activity attribution need precision.

S1/source context links No.2 CL-2 to B. licheniformis, No.5 lou2/tree lou to B. subtilis, No.11 ITS1 to A. rugulosus, and No.A to the laboratory-preserved fungal component. The B. subtilis hemicellulolytic note lacks isolate-specific support in the inspected assays. DOMINANT can describe inoculant prominence, not measured dominance or persistence of all four in compost; Aspergillus declines despite addition.

### ecological_interactions[0]: Coordinated Carbohydrate Esterase Enrichment and Nitrification Gene Activation

graph: concern. Targets: CommunityMech:000473.

Gene-abundance changes are supported, but activation, inoculant-specific attribution and SYNTROPHY exceed the evidence.

The intervention is the four-species inoculum; the response is indigenous-plus-introduced compost taxa and relative DNA gene abundance under T4 and other amendment contrasts. Luteimonas/Pseudomonas are measured responders, not added members. Direction is amendment to functional potential; no partner-product-use/removal mechanism or complete ammonia-oxidation rate is established.

### ecological_interactions[1]: Cross-Kingdom Fungal-Bacterial Lignocellulose Hydrolysis and Urease Activation

graph: concern. Targets: CommunityMech:000473.

Bulk enzyme responses support a community phenotype, but not the typed syntrophic interaction among the four encoded taxa.

The four inoculant species are treatment components; extracted compost enzymes are the endpoint. Use matched manure-baseline/factorial comparisons and the sampled times. Cellulose/lignin terms capture substrate context without identifying which member supplied each activity or claiming every assay/time favored T4.

### ecological_interactions[2]: Accelerated Co-Vermicomposting Maturity, Humification, and Nitrate Accumulation

graph: concern. Targets: CommunityMech:000473.

Product-quality changes are supported with treatment-specific boundaries; SYNTROPHY is not demonstrated by these outcomes.

Participants are the applied four-species inoculum within the broader compost/earthworm system. The direction is treatment to C/N, humic-substance, nitrate and germination/quality endpoints; no donor-recipient identity or thermodynamic product-removal coupling follows. T4 overall quality and T5 fiber residuals are distinct rankings.

### ecological_interactions[0].downstream[0]: gene enrichment to enzyme activities

graph: concern. Targets: CommunityMech:000473.

The proposed mediation is plausible but is not directly demonstrated by DNA abundance and jointly measured enzyme responses.

Source node concerns whole-compost CE/GT/hao potential; target concerns extracted lignocellulolytic and urease activities after four-species inoculation. Gene abundance is not transcription, and hao does not itself establish urease mediation. Remove the asserted direct causal link or retain only a specifically source-attributed hypothesis with this scope.

### ecological_interactions[1].downstream[0]: enzyme activities to product quality

graph: concern. Targets: CommunityMech:000473.

The source proposes enzyme-associated humification, but selective causal mediation of every listed outcome was not tested.

Source is bulk enzyme activity in amended compost; target is C/N, humic substances, nitrate, germination and final quality. Treatment-level co-response does not isolate enzyme causation, and the endpoint-specific rankings differ. Preserve measured treatment effects while qualifying or removing the mechanistic arrow.

### Missing engineering, media, setup and environmental-factor fields

completeness: concern. Targets: CommunityMech:000473.

Main Methods provides a reproducible inoculum and reactor design that is absent from structured fields.

Retain 5% v/w on dry substrate, repeated addition and the distinct optimization/trial phases. Initial formulations, moisture control and measurement temperatures are not interchangeable.

### Origin, category, state, compost and elemental context

scope: concern. Targets: CommunityMech:000473.

SYNTHETIC, ENGINEERED and LIGNOCELLULOSE are appropriate; the measured feedstock metal inventory is omitted.

NOT_APPLICABLE metal processing can remain: detecting total metals in feedstocks does not establish removal, speciation, bioavailability or final-product safety. No rare-earth finding follows.

### Source resource and dataset boundaries

completeness: supported. Targets: CommunityMech:000473.

Main text and supplements were available, but no verified source-isolate or metagenome archive accession was recovered.

The primary publication and supplement can be linked as resources. Reference strains in phylogenetic trees must not be substituted for inoculant accessions; absence is bounded to the inspected material.

### Exact snippets and prior causal decision

provenance: concern. Targets: CommunityMech:000473.

All snippets are supported as text, but the prior chain certification does not resolve source entailment.

### Native checks, ontology and fresh evidence

schema: supported. Targets: CommunityMech:000473.

Seven focused gates and cache preflight pass; ten term pairs and thirteen snippets verify, while native graph completeness does not resolve the causal concerns.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000473.

Completeness is 70 and capped quality is 100; neither score overrides the scientific needs-curation verdict.

## Findings

### mechanistic-overclaim: Treatment effects are promoted to a syntrophic causal chain

major / open / confirmed; issue key: cm-000473-mechanistic-overclaim.

All three nodes use SYNTROPHY, although the source does not demonstrate partner-product use/removal making another member metabolism favorable. Node 0 further calls metagenomic abundance activation, and two DIRECTLY IMPLIED arrows promote jointly measured potential, enzymes and quality into causal mediation. Whole-compost measurements do not identify all four inoculants as the functional actors, and treatment rankings vary by endpoint.

### cultivation-completeness: Reported inoculum and reactor design are not represented

minor / open / confirmed; issue key: cm-000473-cultivation-completeness.

The record reduces inoculation to an unspecified 5%, omitting the v/w dry-substrate basis, selected ratio, repeated dosing, feedstock controls and two-stage earthworm reactor conditions reported in Methods.

### strain-provenance: Recoverable isolate codes and role boundaries are missing

minor / open / confirmed; issue key: cm-000473-strain-provenance.

Species-only taxonomy omits source isolate codes recoverable from Supplementary Figure S1 and mixture tables. The B. subtilis note adds hemicellulolysis without isolate-specific support; all-four dominance must remain an inoculant description rather than demonstrated compost persistence.

### feedstock-metals: Measured feedstock metals are absent from the inventory

minor / open / confirmed; issue key: cm-000473-feedstock-metals.

metals_present is empty although Supplementary Table S1 reports total Fe, Cu, Zn, Cr, Pb, Ni and Mn in both feedstocks. The schema covers metals present as well as processed; the absence of a metal-processing role does not erase their measured presence.

## Recommended Actions And Acceptance Checks

### fix-mechanistic-overclaim

Retain supported treatment phenotypes while removing unsupported syntrophy and qualifying or removing mechanistic arrows.

- Describe CE/GT/hao as relative DNA gene abundance or potential, not expression/activation or complete ammonia oxidation.
- Keep four-member inoculum identity separate from broader compost responders and measured functions.
- Remove SYNTROPHY unless direct partner-product-use/removal evidence is supplied; non-antagonism alone is insufficient.
- Replace direct causal language with a specific source-supported hypothesis or remove each unsupported arrow.
- Use T4 versus appropriate baseline and endpoint/time comparisons; preserve T5 fiber-degradation advantage and T4 composite quality advantage.
- Run strict, reference and native network checks and append a new review history event without rewriting prior decisions.

### fix-cultivation-completeness

Add source-backed structured preparation and reactor conditions with separate optimization and treatment contexts.

- Retain the 1:2:2:1 ordered ratio, standardized bacterial/fungal stocks and 5% v/w dry-substrate inoculum.
- Represent initial day-10 application and seven-day reinoculation, three replicates, five treatments and SSP contrasts.
- Capture reactor capacity, trial feedstock masses, 15+29-day stages, 30 worms, dark 27 +/- 0.5 C, 65 +/- 5% moisture and two-day turning.
- Do not substitute the optimization 3:7 substrate mixture for the trial formulation or count worms as microbial members.
- Use claim-level Methods evidence and validate the record without inventing a unique CultureMech recipe.

### fix-strain-provenance

Preserve source isolate codes and qualify functional/prominence claims at their measured scope.

- Record No.2/CL-2, No.5/caption lou2 with tree lou, and No.11/ITS1 with precise figure provenance.
- Treat No.A as the source laboratory-fungus code with explicit contextual attribution; do not invent a culture-collection accession.
- Remove or qualify isolate-specific hemicellulolysis unless separate evidence supports it.
- Clarify that four encoded members form the inoculant, without claiming stable dominance in the whole compost microbiome.
- Do not import comparator-tree strain accessions or recompute GTDB mapping counts from species labels.

### fix-feedstock-metals

Represent measured feedstock presence with elemental and experimental scope while retaining the supported processing classification.

- Use the existing IRON, COPPER, ZINC, CHROMIUM, LEAD and NICKEL enums as element inventory, with source-attributed total-metal notes and no inferred oxidation state.
- Record manganese in source-attributed notes because the current metal enum has no manganese value; do not expand schema within this record task.
- Keep raw-material concentrations distinct from end-product measurements or microbial removal.
- Retain NOT_APPLICABLE for significant metal processing unless new evidence establishes a role.
- Run strict and reference validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml; Entire target: four inoculant species, three nodes and two arrows | supports | The record describes a four-member inoculant applied to an earthworm-associated compost system; these are distinct biological scopes. |
| fulltext | PMID:42780861; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13597777/fullTextXML | supports | Fresh XML supplied the complete Introduction, Methods, Results/Discussion and Conclusion. |
| root-publisher-pdf | PMID:42780861; https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1927926/pdf | supports | Fresh publisher PDF independently supplied the complete main study and relevant figures. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42780861&amp;retmode=xml; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42780861&amp;retmode=xml | supports | Fresh PubMed identifies PMID42780861, PMC13597777, DOI10.3389/fmicb.2026.1927926 and the matching abstract. |
| crossref | https://api.crossref.org/works/10.3389/fmicb.2026.1927926; https://api.crossref.org/works/10.3389/fmicb.2026.1927926 | supports | Fresh Crossref identifies the DOI and matching journal-article title. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42780861&amp;format=json&amp;resultType=core; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42780861&amp;format=json&amp;resultType=core | supports | Fresh Europe PMC metadata identifies the matching article and open full text. |
| supplements | PMID:42780861; Public supplementary archive; Table_1.docx, Tables S1-S9 and captions S1-S4 | supports | All supplementary table text and captions were read; Figure S1 was visually inspected. The package contains source material, not an independently deposited sequence archive. |
| strain-source | PMID:42780861; Methods 2.2-2.3; Supplementary Figure S1 and Tables S2-S3 | supports | The source selects three compost isolates plus laboratory-preserved A. nidulans. S1 maps No.2 to CL-2, No.5 to caption lou2 (tree lou), and No.11 to ITS1; the fourth laboratory inoculum is coded No.A. These source codes are not culture-collection or sequence accessions. |
| design | PMID:42780861; Methods 2.3-2.4; Tables S2-S3 | supports | The selected A. nidulans:B. licheniformis:A. rugulosus:B. subtilis ratio is 1:2:2:1. The trial distinguishes green waste, manure-adjusted baseline, SSP, SynCom and combined treatments with three replicates. A 5% v/w dry-substrate inoculum starts on day 10 and is repeated every seven days; the 35-day mixture optimization is separate. |
| cultivation | PMID:42780861; Methods 2.1-2.4 | supports | Fourteen-point-nine-liter reactors contain 1,000 g green waste plus 358.95 g manure in the composite substrate. Fifteen days of pre-composting precede 29 days with 30 E. fetida adults per reactor. Conditions are dark, 27 +/- 0.5 C, 65 +/- 5% moisture and turning every two days. Stocks use LB/PDB and standardized bacterial CFU/fungal spores; preparation is distinct from reactor cultivation. |
| genes | PMID:42780861; Methods 2.5; Results 3.6-3.8; Figures 4-6 | supports | DNA metagenomes describe the whole compost community. Higher CE/GT and hao abundance indicates functional potential; AOB amoA was not detected, and complete ammonia oxidation, transcription, flux and inoculant-specific gene attribution are not established. |
| enzymes | PMID:42780861; Methods 2.4; Results 3.1; Figure 1 | supports | Bulk enzyme activities respond to inoculation, with endpoint- and time-specific comparisons. T4 enhances late-stage cellulase and ligninolytic activities; urease comparisons should use the manure baseline and relevant factorial arms, not universal superiority to T1. |
| quality | PMID:42780861; Results 3.2-3.5; Figures 2-3; Tables S4-S8 | supports | T4 has the highest composite quality ranking and final humic-substance content, but T5 has the lowest final fiber residuals and higher germination index. Product endpoints do not demonstrate syntrophy or a universal T4 maximum. |
| mediation | PMID:42780861; Results 3.1-3.2 and 3.7-3.8; Supplementary Figure S4 caption | supports | The authors propose links among substrate transformation, indigenous microbes, enzyme activities and product quality; selective mediation and partner-product removal were not tested. |
| metals | PMID:42780861; Supplementary Table S1: raw-material total-metal rows | supports | Green waste and cattle manure contain measured total Mn, Fe, Cu, Zn, Cr, Pb and Ni. These are feedstock totals, not final-product concentrations, chemical speciation or demonstrated metal processing. |
| ontology | Local OAK NCBITaxon, ENVO, CHEBI and GO snapshots; Ten unique ID/label pairs at twenty-five occurrences | supports | All labels match. Broad process terms fit the subject but do not establish measured rates or causal direction; fungi correctly lack GTDB equivalents. |
| schema | src/communitymech/schema/communitymech.yaml; InteractionTypeEnum.SYNTROPHY; AbundanceEnum; metals_present; MetalElementEnum; strain/cultivation fields | supports | SYNTROPHY requires partner-product use/removal making producer metabolism favorable, without requiring obligacy. DOMINANT is ordinal. Metals may be present without processing; six reported elements have enums, while manganese requires notes under the current schema. |
| snippets | kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml; Thirteen snippet occurrences: snippet-audit.json | supports | All thirteen snippets match both the pinned cache and fresh XML; exact text does not establish the encoded causal interpretation. |
| datasets | Primary data statement and complete supplementary material; dataset-verification.json: bounded accession and source-code audit | supports | No deposited source-strain or metagenome accession was identified in the inspected main text, tables or S1 labels. Comparator tree leaves are not inoculant accessions; no arbitrary archive association was made. |
| history | history/records/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom; reports/causal_graph_review/decisions; Two sidecars; batch133 target lines636-789 | supports | The recorded prior hash matches, but its abstract/cache-based causal-chain judgment is reassessed against full Methods and explicit potential limits. No linked issue was found within the inspected target/history/decision scope. |
| search | Owned-worktree kb/taxa, community/isolate roots and source IDs; Ignored-inclusive bounded identity lookup | supports | No reusable target taxon/isolate record was identified within the stored exact search scope; unrelated shared species names do not authenticate these isolates. |
| adapter | Optional kg-microbe-sources adapter; Explicit same-batch04-runtime discovery reuse | supports | No installed runner/module was available in the recorded runtime; no external runner or strain-module coverage query was executed. |
| native-target | NetworkIntegrityAuditor().audit_community(target); support-audit.json: actual targeted API and native rubric | supports | Native COMPLETE reports no issues; five evidence items across three nodes give mean evidence 5/3. Structural connectivity does not certify the two causal arrows. |
| independent-source | PMID:42780861; root-source-audit.json: whole main study, figures and complete supplementary tables/captions | supports | Independent source reading supports one major causal-scope group and three minor completeness/provenance groups. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml; Actual execution 2026-10-21T08:34:03.939332+00:00 to 2026-10-21T08:34:06.466502+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-strict kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml --out /private/tmp/cm-review-session/batch-04/000473/strict-report.tsv; Actual execution 2026-10-21T08:34:03.943027+00:00 to 2026-10-21T08:34:09.126779+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-terms kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml; Actual execution 2026-10-21T08:34:03.945761+00:00 to 2026-10-21T08:34:08.331306+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-gtdb kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml; Actual execution 2026-10-21T08:34:06.473988+00:00 to 2026-10-21T08:34:06.623535+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml; Actual execution 2026-10-21T08:34:06.623905+00:00 to 2026-10-21T08:34:09.661802+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-history history/records/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom; Actual execution 2026-10-21T08:34:08.331783+00:00 to 2026-10-21T08:34:09.840359+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T08:34:09.841976+00:00 to 2026-10-21T08:34:09.934362+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-references-explained kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml; Actual execution 2026-10-21T08:34:09.934723+00:00 to 2026-10-21T08:34:11.581653+00:00 | supports | Target native references passed; all thirteen snippets also match fresh XML. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T07:06:05.543108+00:00 to 2026-10-21T07:06:16.498440+00:00 | supports | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T07:06:16.498920+00:00 to 2026-10-21T07:06:23.361213+00:00 | supports | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |

## Limits And Additional Notes

- Species-level identities and local source codes are supported by the paper and supplementary figure; no deposited source-strain or metagenome accession was identified. Reference-tree culture strains are not the study inoculants and were not substituted.
- Bacterial GTDB mapping fractions, genome counts and release claims are inherited historical curation metadata and were not recomputed; native checks verify syntax/domain consistency only. Fungi appropriately have no GTDB equivalent.
- The S1 caption spells the B. subtilis code lou2 while its tree tip reads lou; preserve both source forms rather than silently resolving that difference. No.A is the laboratory fungal component in the source design, not an external accession.
- Supplementary Table S3 has a middle-time column labeled 18 d while its footnote says 8 d. The selected 35-day endpoint and mixture ratio are clear; no intermediate-time correction was inferred.
- The inoculant ratio optimization uses its own 3:7 manure:green-waste substrate and 35-day incubation; these are separate from the 44-day vermicomposting trial. Repeated additions and host/indigenous-community context preclude treating this as a closed four-strain culture.
- Main Figure 1 and Figure 6 were visually inspected, as was supplementary Figure S1. All supplementary table text and captions were read, but other supplementary image measurements were not independently digitized or reanalyzed.
- Gene abundance reflects DNA-based potential, not transcription, process rate or complete ammonia oxidation. The study did not quantify strain persistence, earthworm biomass/survival changes, N2O flux or selective causal mediation of product quality.
- Feedstock total metals are not end-product concentrations, oxidation states, bioavailability or microbial processing. Manganese lacks a current enum value and can be retained in source-attributed notes without a schema change.
- Optional structured-adapter discovery was reused with its original same-runtime scope; no external-checkout runner, paid provider or strain-module query was used.
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 20 words for this publication and its supplement combined.
- All repository inputs were pinned by official inspect before assessment and rechecked at candidate construction.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T083908Z-bacillus-aspergillus-vermicompost-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Bacillus-Aspergillus vermicomposting SynCom: whole-record review'
started_at: '2026-10-21T08:33:46.287723Z'
finished_at: '2026-10-21T08:39:08.843047Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Canonical target unchanged; separate agents assessed the primary
    study/figures, ontology, native checks, snippets, history, resources and metrics.
    No person-level independence beyond the recorded task roles is claimed.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: One major finding groups unsupported syntrophy, gene activation and two causal
  mediations while preserving measured treatment effects. Three minor findings recover
  cultivation/design, source-strain provenance and measured feedstock-metal context.
  All three nodes and both arrows were assessed individually. Seven focused gates
  and cache preflight pass; corpus network warning failures remain explicit.
source:
  git_revision: c6e5a9b9af2d05e12eaafb2555a53f3a079268f3
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
  - path: history/records/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom/2026-10-19T053000Z-antigravity-2978.yaml
    sha256: 5b9a160a047d9a84ed4eea990be1c0142056c8dbbdbceb2d38583e75ed967c9d
    role: context
  - path: history/records/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom/2026-10-20T041800Z-antigravity-79d195.yaml
    sha256: ac7be2fe81f83f396b8a3edfdad205d118183882dabe9ae6465cb7f59c17c42c
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    sha256: 79d1950ceed0b63d7eed71a21cccb19fc7dde96ea32b0d8010714a4bfbff0769
    role: target
  - path: references_cache/PMID_42780861.txt
    sha256: 6218fb4a297c0f1361df5c127251be95c7274a4eb28e89a69536d94ee0f09356
    role: context
  - path: reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml
    sha256: e9ded35a2333f9994869573f9f952b3af3191ab55528813a7f2c03639a362d3f
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
- target_id: CommunityMech:000473
  path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  label: Bacillus and Aspergillus Lignocellulose-Degrading Co-Vermicomposting SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    role: canonical_record
scope:
  description: 'Entire record: all four species, three nodes, two arrows and thirteen
    evidence occurrences. Fresh main text, Tables S1-S9, supplementary captions S1-S4,
    visual S1 and relevant main figures were assessed; no raw metagenome, sequence,
    enzyme or statistical reanalysis was performed.'
  selection: Final assigned maintained path of batch04 after CommunityMech:000358;
    one resolved four-member inoculant and its vermicomposting application.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000473
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000473
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000473
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-strict kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-04/000473/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000473
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-terms kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000473
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000473
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000473
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-history history/records/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000473
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target native references passed; all thirteen snippets also match fresh
    XML.
  target_ids:
  - CommunityMech:000473
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-references-explained kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000473
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Reused fresh full-corpus batch04 execution; neither a target-specific
    failure nor a pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000473
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Reused fresh full-corpus batch04 execution; neither a target-specific
    failure nor a pass.
- check_id: primary-source
  name: Publication identity and full scientific assessment
  status: passed
  required: true
  summary: Fresh main text, all supplementary tables/captions and relevant figures
    support a complete source assessment.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - fulltext
  - root-publisher-pdf
  - pubmed
  - crossref
  - epmc
  - supplements
  - independent-source
- check_id: source-data
  name: Bounded source-code and dataset inventory
  status: passed
  required: true
  summary: Supplementary source codes were recovered; no deposited inoculant/metagenome
    accession was identified in the inspected material.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - strain-source
  - datasets
  - supplements
- check_id: cross-mech
  name: Encoded medium and ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech ID is encoded, and no exact external
    recipe equivalence was certified.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - record
  - cultivation
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Same-runtime discovery was reused; no strain-module coverage was queried.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  locator: 'Entire target: four inoculant species, three nodes and two arrows'
  summary: The record describes a four-member inoculant applied to an earthworm-associated
    compost system; these are distinct biological scopes.
  support: supports
  accessed_at: '2026-10-21T08:39:08.830339Z'
- evidence_id: fulltext
  kind: primary_source
  reference: PMID:42780861
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13597777/fullTextXML
  summary: Fresh XML supplied the complete Introduction, Methods, Results/Discussion
    and Conclusion.
  support: supports
  accessed_at: '2026-10-21T08:33:56.078606Z'
  snapshot_sha256: 9d43b9e521f32b89e98e000f9dac485bd4e84708e022eb25e7e00b548ad3dc96
- evidence_id: root-publisher-pdf
  kind: primary_source
  reference: PMID:42780861
  locator: https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2026.1927926/pdf
  summary: Fresh publisher PDF independently supplied the complete main study and
    relevant figures.
  support: supports
  accessed_at: '2026-10-21T08:34:03.709299Z'
  snapshot_sha256: f278319596eb4ca8445b50b8ed996b13afbe13a126f60d35c715f7f47a676fa7
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42780861&retmode=xml
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42780861&retmode=xml
  summary: Fresh PubMed identifies PMID42780861, PMC13597777, DOI10.3389/fmicb.2026.1927926
    and the matching abstract.
  support: supports
  accessed_at: '2026-10-21T08:33:51.854200Z'
  snapshot_sha256: bf0197ebd952d193b2200c9788664df5aea34f6b8fee7355542a60c94a815fed
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.3389/fmicb.2026.1927926
  locator: https://api.crossref.org/works/10.3389/fmicb.2026.1927926
  summary: Fresh Crossref identifies the DOI and matching journal-article title.
  support: supports
  accessed_at: '2026-10-21T08:33:51.844606Z'
  snapshot_sha256: ebb0288685e2ba66e7b36fc9dddd4086adfd4501b763a0cca240d91f64c048ab
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42780861&format=json&resultType=core
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42780861&format=json&resultType=core
  summary: Fresh Europe PMC metadata identifies the matching article and open full
    text.
  support: supports
  accessed_at: '2026-10-21T08:33:52.232570Z'
  snapshot_sha256: 59a31e6042f0b5ff468344514f9d29c74dccc19195d9e1fe0fc6ec933f899ba3
- evidence_id: supplements
  kind: primary_source
  reference: PMID:42780861
  locator: Public supplementary archive; Table_1.docx, Tables S1-S9 and captions S1-S4
  summary: All supplementary table text and captions were read; Figure S1 was visually
    inspected. The package contains source material, not an independently deposited
    sequence archive.
  support: supports
  accessed_at: '2026-10-21T08:35:00.220253Z'
  snapshot_sha256: 9fcbb7660ed837abf7e61b4bad96525382f271d27dd60f22db68015c3a8d4407
- evidence_id: strain-source
  kind: primary_source
  reference: PMID:42780861
  locator: Methods 2.2-2.3; Supplementary Figure S1 and Tables S2-S3
  summary: The source selects three compost isolates plus laboratory-preserved A.
    nidulans. S1 maps No.2 to CL-2, No.5 to caption lou2 (tree lou), and No.11 to
    ITS1; the fourth laboratory inoculum is coded No.A. These source codes are not
    culture-collection or sequence accessions.
  support: supports
  accessed_at: '2026-10-21T08:39:08.833840Z'
  snapshot_sha256: 513faa579a742dfd6f59e6ca93a3aba9134b52919a0809c3aed53a5de0300d47
- evidence_id: design
  kind: primary_source
  reference: PMID:42780861
  locator: Methods 2.3-2.4; Tables S2-S3
  summary: The selected A. nidulans:B. licheniformis:A. rugulosus:B. subtilis ratio
    is 1:2:2:1. The trial distinguishes green waste, manure-adjusted baseline, SSP,
    SynCom and combined treatments with three replicates. A 5% v/w dry-substrate inoculum
    starts on day 10 and is repeated every seven days; the 35-day mixture optimization
    is separate.
  support: supports
  accessed_at: '2026-10-21T08:39:08.833847Z'
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:42780861
  locator: Methods 2.1-2.4
  summary: Fourteen-point-nine-liter reactors contain 1,000 g green waste plus 358.95
    g manure in the composite substrate. Fifteen days of pre-composting precede 29
    days with 30 E. fetida adults per reactor. Conditions are dark, 27 +/- 0.5 C,
    65 +/- 5% moisture and turning every two days. Stocks use LB/PDB and standardized
    bacterial CFU/fungal spores; preparation is distinct from reactor cultivation.
  support: supports
  accessed_at: '2026-10-21T08:39:08.833849Z'
- evidence_id: genes
  kind: primary_source
  reference: PMID:42780861
  locator: Methods 2.5; Results 3.6-3.8; Figures 4-6
  summary: DNA metagenomes describe the whole compost community. Higher CE/GT and
    hao abundance indicates functional potential; AOB amoA was not detected, and complete
    ammonia oxidation, transcription, flux and inoculant-specific gene attribution
    are not established.
  support: supports
  accessed_at: '2026-10-21T08:39:08.834131Z'
  quote: metabolic potential rather than actual process rates
  snapshot_sha256: f906d6983ea423b5b350eda19e61687c4a23fdf92de652e0fc1c027d58d0614e
- evidence_id: enzymes
  kind: primary_source
  reference: PMID:42780861
  locator: Methods 2.4; Results 3.1; Figure 1
  summary: Bulk enzyme activities respond to inoculation, with endpoint- and time-specific
    comparisons. T4 enhances late-stage cellulase and ligninolytic activities; urease
    comparisons should use the manure baseline and relevant factorial arms, not universal
    superiority to T1.
  support: supports
  accessed_at: '2026-10-21T08:39:08.834331Z'
  quote: associated with enhanced ligninolytic enzyme activities
  snapshot_sha256: 3fcbcd33950a1b2c8cd123b97235d5bbabde6e0a70a72de96e6df336fc91794a
- evidence_id: quality
  kind: primary_source
  reference: PMID:42780861
  locator: Results 3.2-3.5; Figures 2-3; Tables S4-S8
  summary: T4 has the highest composite quality ranking and final humic-substance
    content, but T5 has the lowest final fiber residuals and higher germination index.
    Product endpoints do not demonstrate syntrophy or a universal T4 maximum.
  support: supports
  accessed_at: '2026-10-21T08:39:08.834334Z'
  quote: highest-quality vermicompost product
- evidence_id: mediation
  kind: primary_source
  reference: PMID:42780861
  locator: Results 3.1-3.2 and 3.7-3.8; Supplementary Figure S4 caption
  summary: The authors propose links among substrate transformation, indigenous microbes,
    enzyme activities and product quality; selective mediation and partner-product
    removal were not tested.
  support: supports
  accessed_at: '2026-10-21T08:39:08.834336Z'
  quote: may have promoted humification
- evidence_id: metals
  kind: primary_source
  reference: PMID:42780861
  locator: 'Supplementary Table S1: raw-material total-metal rows'
  summary: Green waste and cattle manure contain measured total Mn, Fe, Cu, Zn, Cr,
    Pb and Ni. These are feedstock totals, not final-product concentrations, chemical
    speciation or demonstrated metal processing.
  support: supports
  accessed_at: '2026-10-21T08:39:08.836738Z'
  snapshot_sha256: a34834cf0881040371ddc3424d57b6bca33c838da916241d5638af336615bf7d
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, CHEBI and GO snapshots
  locator: Ten unique ID/label pairs at twenty-five occurrences
  summary: All labels match. Broad process terms fit the subject but do not establish
    measured rates or causal direction; fungi correctly lack GTDB equivalents.
  support: supports
  accessed_at: '2026-10-21T08:39:08.837301Z'
  snapshot_sha256: ad6dc58dcafb12ff1a9a2d20660856fc5b643c733c26da800be019ac306da61c
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: InteractionTypeEnum.SYNTROPHY; AbundanceEnum; metals_present; MetalElementEnum;
    strain/cultivation fields
  summary: SYNTROPHY requires partner-product use/removal making producer metabolism
    favorable, without requiring obligacy. DOMINANT is ordinal. Metals may be present
    without processing; six reported elements have enums, while manganese requires
    notes under the current schema.
  support: supports
  accessed_at: '2026-10-21T08:39:08.837309Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  locator: 'Thirteen snippet occurrences: snippet-audit.json'
  summary: All thirteen snippets match both the pinned cache and fresh XML; exact
    text does not establish the encoded causal interpretation.
  support: supports
  accessed_at: '2026-10-21T08:39:08.837610Z'
  snapshot_sha256: ad1d22e990f07299bb03967d11a408ba24b2fd0ff12c05e6b8742cf12bacbc84
- evidence_id: datasets
  kind: validation
  reference: Primary data statement and complete supplementary material
  locator: 'dataset-verification.json: bounded accession and source-code audit'
  summary: No deposited source-strain or metagenome accession was identified in the
    inspected main text, tables or S1 labels. Comparator tree leaves are not inoculant
    accessions; no arbitrary archive association was made.
  support: supports
  accessed_at: '2026-10-21T08:39:08.837762Z'
  snapshot_sha256: 654677389b1d330941d4b90a98be77e6df5400fd984d7e6673e75498cef803e2
- evidence_id: history
  kind: record_content
  reference: history/records/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom;
    reports/causal_graph_review/decisions
  locator: Two sidecars; batch133 target lines636-789
  summary: The recorded prior hash matches, but its abstract/cache-based causal-chain
    judgment is reassessed against full Methods and explicit potential limits. No
    linked issue was found within the inspected target/history/decision scope.
  support: supports
  accessed_at: '2026-10-21T08:39:08.838113Z'
  snapshot_sha256: 0b5d990144f648695f08aedb378f82d554e54193755fd1214a96b8e543cb0fb1
- evidence_id: search
  kind: search
  reference: Owned-worktree kb/taxa, community/isolate roots and source IDs
  locator: Ignored-inclusive bounded identity lookup
  summary: No reusable target taxon/isolate record was identified within the stored
    exact search scope; unrelated shared species names do not authenticate these isolates.
  support: supports
  accessed_at: '2026-10-21T08:39:08.838317Z'
  snapshot_sha256: 46adb065fad2e5ae757358c36041a85f1405d5c6acef1058333a7891bb543a5a
  search_scope: rg --no-ignore --hidden for recorded identifiers, species names, source
    PMID/DOI and record identity; not exhaustive synonym coverage.
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources adapter
  locator: Explicit same-batch04-runtime discovery reuse
  summary: No installed runner/module was available in the recorded runtime; no external
    runner or strain-module coverage query was executed.
  support: supports
  accessed_at: '2026-10-21T08:39:08.838828Z'
  snapshot_sha256: b85ff9e5a0d491dd98f3ee5374310fc7ced1062e97bb89fcfd51031bd89caa4f
  search_scope: Reused original batch04 runtime/module and ignored-inclusive bounded
    discovery.
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: 'support-audit.json: actual targeted API and native rubric'
  summary: Native COMPLETE reports no issues; five evidence items across three nodes
    give mean evidence 5/3. Structural connectivity does not certify the two causal
    arrows.
  support: supports
  accessed_at: '2026-10-21T08:39:08.839013Z'
  snapshot_sha256: 3abace1282548d19c04e3f6fddbed09bee3bc2c89959cdd1cc485d6c8d755f25
- evidence_id: independent-source
  kind: validation
  reference: PMID:42780861
  locator: 'root-source-audit.json: whole main study, figures and complete supplementary
    tables/captions'
  summary: Independent source reading supports one major causal-scope group and three
    minor completeness/provenance groups.
  support: supports
  accessed_at: '2026-10-21T08:39:08.839057Z'
  snapshot_sha256: 2997d2117472661e7c502b2afc99b9ee4fe53ef28597ac79eba469d80ee31403
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  locator: Actual execution 2026-10-21T08:34:03.939332+00:00 to 2026-10-21T08:34:06.466502+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T08:34:06.466502Z'
  snapshot_sha256: 3dcfc5f05549c4d7b448617cecb0c508f52ecf71f2527c2e30bc3bb12f7ae85e
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-strict kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-04/000473/strict-report.tsv
  locator: Actual execution 2026-10-21T08:34:03.943027+00:00 to 2026-10-21T08:34:09.126779+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T08:34:09.126779Z'
  snapshot_sha256: ba63cdb8a279d31548c6c652d32a78ec96eb704f1f436bb5b11f531f620129ba
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-terms kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  locator: Actual execution 2026-10-21T08:34:03.945761+00:00 to 2026-10-21T08:34:08.331306+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T08:34:08.331306Z'
  snapshot_sha256: 4a5d24c5a269a9af24ac92e4a3ed8c4b125e161db211a6fd82036b85afc55967
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  locator: Actual execution 2026-10-21T08:34:06.473988+00:00 to 2026-10-21T08:34:06.623535+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T08:34:06.623535Z'
  snapshot_sha256: c0d5a29111c6d51a247300e0a9b81826c757f4f2c5acb6aa685c2bcc7d3fb07a
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  locator: Actual execution 2026-10-21T08:34:06.623905+00:00 to 2026-10-21T08:34:09.661802+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T08:34:09.661802Z'
  snapshot_sha256: 1d5453e6540e7304901d9529f64ccd7bc5faf8f86145a74be69816f1334f5110
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-history history/records/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom
  locator: Actual execution 2026-10-21T08:34:08.331783+00:00 to 2026-10-21T08:34:09.840359+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T08:34:09.840359Z'
  snapshot_sha256: 683fd05bd302347e37a8ab1562b1667bc39182f6534baa1f2a042046b07e1703
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T08:34:09.841976+00:00 to 2026-10-21T08:34:09.934362+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T08:34:09.934362Z'
  snapshot_sha256: b30df3f334302458e9406fb9606b54a2c45b608bf9922e39515ae0cae5f3ab1f
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-references-explained kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
  locator: Actual execution 2026-10-21T08:34:09.934723+00:00 to 2026-10-21T08:34:11.581653+00:00
  summary: Target native references passed; all thirteen snippets also match fresh
    XML.
  support: supports
  accessed_at: '2026-10-21T08:34:11.581653Z'
  snapshot_sha256: d887cbc8c50297fff5c2b61f7b528fa1a112ccae4f3a81d5774b0af3358f685d
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T07:06:05.543108+00:00 to 2026-10-21T07:06:16.498440+00:00
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  support: supports
  accessed_at: '2026-10-21T07:06:16.498440Z'
  snapshot_sha256: 7e9c998a5a9fe2b1a28c809bd5eb651205b3256dd64666ef7a9ca6fbde7504fa
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T07:06:16.498920+00:00 to 2026-10-21T07:06:23.361213+00:00
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  support: supports
  accessed_at: '2026-10-21T07:06:23.361213Z'
  snapshot_sha256: 5ba6a0b7c789574c80df1b60d81f0e54454b66e4f919949ad352cff92dd9744e
assessments:
- assessment_id: identity
  area: identity
  topic: Inoculant, compost community and study design
  outcome: supported
  summary: Four source species form the applied inoculant, while measured community
    functions and quality belong to the broader compost system.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - record
  - strain-source
  - design
  - cultivation
  - genes
  - ontology
  dimensions:
  - name: community_scope
    value: Four-species inoculant applied to a complex vermicomposting community
    definition: Bacillus/Aspergillus membership describes the inoculum, not all indigenous
      microbes or the earthworm host.
    evidence_ids:
    - strain-source
    - genes
  - name: source_strain
    value: Three compost isolates and one laboratory-preserved fungus
    definition: Source codes are recoverable from S1 and mixture tables; no deposited
      strain genome or unique isolate taxID is established.
    evidence_ids:
    - strain-source
    - datasets
  - name: environment
    value: Green-waste/cattle-manure compost with E. fetida
    definition: The compost ENVO term is appropriate; the animal context belongs to
      the cultivation design rather than microbial membership.
    evidence_ids:
    - cultivation
    - ontology
  - name: medium
    value: Solid feedstocks with separate LB/PDB inoculum preparation
    definition: Optimization uses a 3:7 manure:green-waste ratio; the vermicomposting
      trial uses its own masses and C/N adjustment.
    evidence_ids:
    - design
    - cultivation
  - name: experimental_setting
    value: Five treatments over 15-day pre-composting and 29-day vermicomposting
    definition: SSP and repeated SynCom addition form a factorial comparison within
      manure-adjusted treatments; moisture, light, temperature and turning are reported.
    evidence_ids:
    - design
    - cultivation
  - name: evidence_tier
    value: Treatment effects, bulk enzyme assays, product chemistry and DNA metagenomic
      potential
    definition: No member-resolved metabolite removal, transcriptional activation
      or selective enzyme mediation was measured.
    evidence_ids:
    - genes
    - enzymes
    - quality
    - mediation
  - name: grounding_status
    value: Ten canonical term pairs; historical bacterial GTDB mappings
    definition: Syntax/domain checks pass, but stored mapping fractions/counts and
      release provenance were not recomputed; fungi are outside GTDB scope.
    evidence_ids:
    - ontology
    - adapter
- assessment_id: taxonomy
  area: grounding
  topic: All four species, source codes, roles and prominence
  outcome: concern
  summary: Species membership and broad degradation roles are supported, but source
    strain codes and activity attribution need precision.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - strain-source
  - schema
  - genes
  - ontology
  details: S1/source context links No.2 CL-2 to B. licheniformis, No.5 lou2/tree lou
    to B. subtilis, No.11 ITS1 to A. rugulosus, and No.A to the laboratory-preserved
    fungal component. The B. subtilis hemicellulolytic note lacks isolate-specific
    support in the inspected assays. DOMINANT can describe inoculant prominence, not
    measured dominance or persistence of all four in compost; Aspergillus declines
    despite addition.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Coordinated Carbohydrate Esterase Enrichment
    and Nitrification Gene Activation'
  outcome: concern
  summary: Gene-abundance changes are supported, but activation, inoculant-specific
    attribution and SYNTROPHY exceed the evidence.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - record
  - genes
  - schema
  - ontology
  details: The intervention is the four-species inoculum; the response is indigenous-plus-introduced
    compost taxa and relative DNA gene abundance under T4 and other amendment contrasts.
    Luteimonas/Pseudomonas are measured responders, not added members. Direction is
    amendment to functional potential; no partner-product-use/removal mechanism or
    complete ammonia-oxidation rate is established.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Cross-Kingdom Fungal-Bacterial Lignocellulose
    Hydrolysis and Urease Activation'
  outcome: concern
  summary: Bulk enzyme responses support a community phenotype, but not the typed
    syntrophic interaction among the four encoded taxa.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - record
  - enzymes
  - design
  - schema
  - ontology
  details: The four inoculant species are treatment components; extracted compost
    enzymes are the endpoint. Use matched manure-baseline/factorial comparisons and
    the sampled times. Cellulose/lignin terms capture substrate context without identifying
    which member supplied each activity or claiming every assay/time favored T4.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Accelerated Co-Vermicomposting Maturity, Humification,
    and Nitrate Accumulation'
  outcome: concern
  summary: Product-quality changes are supported with treatment-specific boundaries;
    SYNTROPHY is not demonstrated by these outcomes.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - record
  - quality
  - genes
  - schema
  details: Participants are the applied four-species inoculum within the broader compost/earthworm
    system. The direction is treatment to C/N, humic-substance, nitrate and germination/quality
    endpoints; no donor-recipient identity or thermodynamic product-removal coupling
    follows. T4 overall quality and T5 fiber residuals are distinct rankings.
- assessment_id: arrow-0
  area: graph
  topic: 'ecological_interactions[0].downstream[0]: gene enrichment to enzyme activities'
  outcome: concern
  summary: The proposed mediation is plausible but is not directly demonstrated by
    DNA abundance and jointly measured enzyme responses.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - genes
  - enzymes
  - mediation
  - schema
  details: Source node concerns whole-compost CE/GT/hao potential; target concerns
    extracted lignocellulolytic and urease activities after four-species inoculation.
    Gene abundance is not transcription, and hao does not itself establish urease
    mediation. Remove the asserted direct causal link or retain only a specifically
    source-attributed hypothesis with this scope.
- assessment_id: arrow-1
  area: graph
  topic: 'ecological_interactions[1].downstream[0]: enzyme activities to product quality'
  outcome: concern
  summary: The source proposes enzyme-associated humification, but selective causal
    mediation of every listed outcome was not tested.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - enzymes
  - quality
  - mediation
  details: Source is bulk enzyme activity in amended compost; target is C/N, humic
    substances, nitrate, germination and final quality. Treatment-level co-response
    does not isolate enzyme causation, and the endpoint-specific rankings differ.
    Preserve measured treatment effects while qualifying or removing the mechanistic
    arrow.
- assessment_id: cultivation
  area: completeness
  topic: Missing engineering, media, setup and environmental-factor fields
  outcome: concern
  summary: Main Methods provides a reproducible inoculum and reactor design that is
    absent from structured fields.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - design
  - cultivation
  - strain-source
  details: Retain 5% v/w on dry substrate, repeated addition and the distinct optimization/trial
    phases. Initial formulations, moisture control and measurement temperatures are
    not interchangeable.
- assessment_id: environment
  area: scope
  topic: Origin, category, state, compost and elemental context
  outcome: concern
  summary: SYNTHETIC, ENGINEERED and LIGNOCELLULOSE are appropriate; the measured
    feedstock metal inventory is omitted.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - record
  - cultivation
  - metals
  - schema
  - ontology
  details: 'NOT_APPLICABLE metal processing can remain: detecting total metals in
    feedstocks does not establish removal, speciation, bioavailability or final-product
    safety. No rare-earth finding follows.'
- assessment_id: resources
  area: completeness
  topic: Source resource and dataset boundaries
  outcome: supported
  summary: Main text and supplements were available, but no verified source-isolate
    or metagenome archive accession was recovered.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - datasets
  - supplements
  details: The primary publication and supplement can be linked as resources. Reference
    strains in phylogenetic trees must not be substituted for inoculant accessions;
    absence is bounded to the inspected material.
- assessment_id: provenance
  area: provenance
  topic: Exact snippets and prior causal decision
  outcome: concern
  summary: All snippets are supported as text, but the prior chain certification does
    not resolve source entailment.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - snippets
  - history
  - genes
  - mediation
  - search
- assessment_id: validation
  area: schema
  topic: Native checks, ontology and fresh evidence
  outcome: supported
  summary: Seven focused gates and cache preflight pass; ten term pairs and thirteen
    snippets verify, while native graph completeness does not resolve the causal concerns.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - ontology
  - snippets
  - check-validate
  - check-validate-strict
  - check-audit-network
  - native-target
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality
  outcome: supported
  summary: Completeness is 70 and capped quality is 100; neither score overrides the
    scientific needs-curation verdict.
  target_ids:
  - CommunityMech:000473
  evidence_ids:
  - record
  - native-target
  metrics:
  - name: completeness
    value: 70
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including all taxon roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). 50 + 5 + 0 + 10 + 0 + 0 + 0 + 5 = 70.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1=0, P2=1, P3=3, P4=0; 5 items / 3 nodes
      = 1.6666667; native COMPLETE. 100 - 10 - 6 + 16.6666667 + 15 = 115.6666667 before
      capping; structural completeness does not certify causal mediation.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P2
    value: 1
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P3
    value: 3
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
findings:
- finding_id: mechanistic-overclaim
  issue_key: cm-000473-mechanistic-overclaim
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: treatment-level associations are promoted to a
    specific syntrophic causal mechanism.'
  rule_id: review-checklist.causal_support
  status: open
  certainty: confirmed
  title: Treatment effects are promoted to a syntrophic causal chain
  description: All three nodes use SYNTROPHY, although the source does not demonstrate
    partner-product use/removal making another member metabolism favorable. Node 0
    further calls metagenomic abundance activation, and two DIRECTLY IMPLIED arrows
    promote jointly measured potential, enzymes and quality into causal mediation.
    Whole-compost measurements do not identify all four inoculants as the functional
    actors, and treatment rankings vary by endpoint.
  target_ids:
  - CommunityMech:000473
  field_paths:
  - ecological_interactions[0]
  - ecological_interactions[1]
  - ecological_interactions[2]
  - description
  evidence_ids:
  - genes
  - enzymes
  - quality
  - mediation
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    role: canonical_record
- finding_id: cultivation-completeness
  issue_key: cm-000473-cultivation-completeness
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: recoverable cultivation, source-strain or substrate
    context is missing or imprecise; community identity remains resolved.'
  rule_id: review-checklist.cultivation
  status: open
  certainty: confirmed
  title: Reported inoculum and reactor design are not represented
  description: The record reduces inoculation to an unspecified 5%, omitting the v/w
    dry-substrate basis, selected ratio, repeated dosing, feedstock controls and two-stage
    earthworm reactor conditions reported in Methods.
  target_ids:
  - CommunityMech:000473
  field_paths:
  - description
  - engineering_design
  - growth_media
  - cultivation_setup
  - environmental_factors
  evidence_ids:
  - design
  - cultivation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    role: canonical_record
- finding_id: strain-provenance
  issue_key: cm-000473-strain-provenance
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: recoverable cultivation, source-strain or substrate
    context is missing or imprecise; community identity remains resolved.'
  rule_id: review-checklist.source_strain
  status: open
  certainty: confirmed
  title: Recoverable isolate codes and role boundaries are missing
  description: Species-only taxonomy omits source isolate codes recoverable from Supplementary
    Figure S1 and mixture tables. The B. subtilis note adds hemicellulolysis without
    isolate-specific support; all-four dominance must remain an inoculant description
    rather than demonstrated compost persistence.
  target_ids:
  - CommunityMech:000473
  field_paths:
  - taxonomy[0].strain_designation
  - taxonomy[1].strain_designation
  - taxonomy[2].strain_designation
  - taxonomy[3].strain_designation
  - taxonomy[1].taxon_term.notes
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  - taxonomy[2].abundance_level
  - taxonomy[3].abundance_level
  evidence_ids:
  - strain-source
  - genes
  - schema
  - datasets
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    role: canonical_record
- finding_id: feedstock-metals
  issue_key: cm-000473-feedstock-metals
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: recoverable cultivation, source-strain or substrate
    context is missing or imprecise; community identity remains resolved.'
  rule_id: review-checklist.environment
  status: open
  certainty: confirmed
  title: Measured feedstock metals are absent from the inventory
  description: metals_present is empty although Supplementary Table S1 reports total
    Fe, Cu, Zn, Cr, Pb, Ni and Mn in both feedstocks. The schema covers metals present
    as well as processed; the absence of a metal-processing role does not erase their
    measured presence.
  target_ids:
  - CommunityMech:000473
  field_paths:
  - metals_present
  - metal_notes
  evidence_ids:
  - metals
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    role: canonical_record
actions:
- action_id: fix-mechanistic-overclaim
  description: Retain supported treatment phenotypes while removing unsupported syntrophy
    and qualifying or removing mechanistic arrows.
  finding_ids:
  - mechanistic-overclaim
  target_ids:
  - CommunityMech:000473
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Describe CE/GT/hao as relative DNA gene abundance or potential, not expression/activation
    or complete ammonia oxidation.
  - Keep four-member inoculum identity separate from broader compost responders and
    measured functions.
  - Remove SYNTROPHY unless direct partner-product-use/removal evidence is supplied;
    non-antagonism alone is insufficient.
  - Replace direct causal language with a specific source-supported hypothesis or
    remove each unsupported arrow.
  - Use T4 versus appropriate baseline and endpoint/time comparisons; preserve T5
    fiber-degradation advantage and T4 composite quality advantage.
  - Run strict, reference and native network checks and append a new review history
    event without rewriting prior decisions.
- action_id: fix-cultivation-completeness
  description: Add source-backed structured preparation and reactor conditions with
    separate optimization and treatment contexts.
  finding_ids:
  - cultivation-completeness
  target_ids:
  - CommunityMech:000473
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Retain the 1:2:2:1 ordered ratio, standardized bacterial/fungal stocks and 5%
    v/w dry-substrate inoculum.
  - Represent initial day-10 application and seven-day reinoculation, three replicates,
    five treatments and SSP contrasts.
  - Capture reactor capacity, trial feedstock masses, 15+29-day stages, 30 worms,
    dark 27 +/- 0.5 C, 65 +/- 5% moisture and two-day turning.
  - Do not substitute the optimization 3:7 substrate mixture for the trial formulation
    or count worms as microbial members.
  - Use claim-level Methods evidence and validate the record without inventing a unique
    CultureMech recipe.
- action_id: fix-strain-provenance
  description: Preserve source isolate codes and qualify functional/prominence claims
    at their measured scope.
  finding_ids:
  - strain-provenance
  target_ids:
  - CommunityMech:000473
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Record No.2/CL-2, No.5/caption lou2 with tree lou, and No.11/ITS1 with precise
    figure provenance.
  - Treat No.A as the source laboratory-fungus code with explicit contextual attribution;
    do not invent a culture-collection accession.
  - Remove or qualify isolate-specific hemicellulolysis unless separate evidence supports
    it.
  - Clarify that four encoded members form the inoculant, without claiming stable
    dominance in the whole compost microbiome.
  - Do not import comparator-tree strain accessions or recompute GTDB mapping counts
    from species labels.
- action_id: fix-feedstock-metals
  description: Represent measured feedstock presence with elemental and experimental
    scope while retaining the supported processing classification.
  finding_ids:
  - feedstock-metals
  target_ids:
  - CommunityMech:000473
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Aspergillus_Green_Waste_Vermicomposting_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Use the existing IRON, COPPER, ZINC, CHROMIUM, LEAD and NICKEL enums as element
    inventory, with source-attributed total-metal notes and no inferred oxidation
    state.
  - Record manganese in source-attributed notes because the current metal enum has
    no manganese value; do not expand schema within this record task.
  - Keep raw-material concentrations distinct from end-product measurements or microbial
    removal.
  - Retain NOT_APPLICABLE for significant metal processing unless new evidence establishes
    a role.
  - Run strict and reference validation.
limitations:
- Species-level identities and local source codes are supported by the paper and supplementary
  figure; no deposited source-strain or metagenome accession was identified. Reference-tree
  culture strains are not the study inoculants and were not substituted.
- Bacterial GTDB mapping fractions, genome counts and release claims are inherited
  historical curation metadata and were not recomputed; native checks verify syntax/domain
  consistency only. Fungi appropriately have no GTDB equivalent.
- The S1 caption spells the B. subtilis code lou2 while its tree tip reads lou; preserve
  both source forms rather than silently resolving that difference. No.A is the laboratory
  fungal component in the source design, not an external accession.
- Supplementary Table S3 has a middle-time column labeled 18 d while its footnote
  says 8 d. The selected 35-day endpoint and mixture ratio are clear; no intermediate-time
  correction was inferred.
- The inoculant ratio optimization uses its own 3:7 manure:green-waste substrate and
  35-day incubation; these are separate from the 44-day vermicomposting trial. Repeated
  additions and host/indigenous-community context preclude treating this as a closed
  four-strain culture.
- Main Figure 1 and Figure 6 were visually inspected, as was supplementary Figure
  S1. All supplementary table text and captions were read, but other supplementary
  image measurements were not independently digitized or reanalyzed.
- Gene abundance reflects DNA-based potential, not transcription, process rate or
  complete ammonia oxidation. The study did not quantify strain persistence, earthworm
  biomass/survival changes, N2O flux or selective causal mediation of product quality.
- Feedstock total metals are not end-product concentrations, oxidation states, bioavailability
  or microbial processing. Manganese lacks a current enum value and can be retained
  in source-attributed notes without a schema change.
- Optional structured-adapter discovery was reused with its original same-runtime
  scope; no external-checkout runner, paid provider or strain-module query was used.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 20 words for this publication and its supplement combined.
- All repository inputs were pinned by official inspect before assessment and rechecked
  at candidate construction.
tags:
- record-review
- synthetic-community
- vermicomposting
- lignocellulose
- batch-04
```
