# Avena rhizosphere SIP: whole-record source review

- Review: 20261021T075602Z-avena-rhizosphere-sip-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T07:49:54.902339Z
- Finished UTC: 2026-10-21T07:56:02.802363Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two major findings concern the summary host-assignment method and aggregate functional attribution. Three minor findings concern unsupported stability, root-exclusion wording and absent source-data links. All four graph nodes and both hypothesized arrows remain supported at their stated scope. Seven focused gates and cache preflight pass; corpus network checks retain unrelated warning failures.

## Scope And Provenance

Entire record: five taxonomic entries, four nodes, two arrows, two factors, soil growth medium, cultivation setup and twenty-three evidence occurrences; fresh complete primary main text, Methods of its cited protocol paper, publication metadata and selected source data metadata. No raw sequencing, isotope, growth or biochemical analyses were repeated.

Selection: Next uncovered maintained path after CommunityMech:000451 in batch04; one resolved natural-community record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c6e5a9b9af2d05e12eaafb2555a53f3a079268f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000236 | kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml | maintained | Avena Rhizosphere Cross-Kingdom 13C-SIP Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000236 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000236 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000236 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000236 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000236 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000236 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000236 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000236 | Target native reference validation passed; scientific meaning was assessed separately. |
| audit-network | failed | True | CommunityMech:000236 | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-network-quality | failed | True | CommunityMech:000236 | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| Publication identity and scientific source assessment | passed | True | CommunityMech:000236 | The full primary main text and cited earlier protocol Methods were read with explicit study boundaries. |
| Selected public source data metadata | passed | True | CommunityMech:000236 | Project/collection and bounded accession metadata verify, with partial-18S and uninspected-range limits retained. |
| Encoded medium and ingredient-Mech linkages | not_applicable | False | CommunityMech:000236 | The soil microcosm record encodes no CultureMech or MediaIngredientMech links to verify. |
| Optional structured source adapter | unavailable | False | CommunityMech:000236 | Same-runtime discovery was reused; no expression-module coverage was queried. |

## Scientific And Domain Assessments

### Natural community, nested taxonomic scopes and experimental setting

identity: supported. Targets: CommunityMech:000236.

The target is resolved as the Avena rhizosphere SIP study; its aggregate taxonomy does not denote a five-member defined consortium.

### All five entries and four PRIMARY_DEGRADER assignments

grounding: concern. Targets: CommunityMech:000236.

Membership is source-backed, but recovered versus enriched subsets and taxon-specific functional potential must be separated from uniform degrader roles.

### Plant-Derived Carbon Incorporation into Phage DNA

graph: supported. Targets: CommunityMech:000236.

The node correctly separates tracer incorporation from inferred infection and lysis-driven recycling.

Participants are the Bacteria and Viruses aggregates. Direction is plant-derived carbon reaching phage DNA through candidate bacterial replication pathways in the labeled rhizosphere; isotope enrichment alone measures neither bacterial mortality nor nutrient-release flux.

### Candidate Burkholderiales Phage-Host Link

graph: supported. Targets: CommunityMech:000236.

The PARTIAL CRISPR-supported host hypothesis is appropriately qualified.

Direction is the phage aggregate toward the Burkholderiales_62_29 candidate represented by NCBITaxon:80840. Both infection and pathogenicity are inferred; GO:0044003 remains proposed host-perturbation context, not a measured disease phenotype.

### Candidate Catenulispora Phage-Host Link

graph: supported. Targets: CommunityMech:000236.

The node correctly identifies GH25/phylogeny support rather than CRISPR evidence.

Direction is the phage aggregate toward the Catenulisporales_70_18/Catenulispora candidate represented by NCBITaxon:414878. The source links phage 69_17 by shared gene history; infection and plant-growth benefit remain unvalidated.

### 13C-Labeled Plant-Signaling and Defense Functions

graph: supported. Targets: CommunityMech:000236.

The computational-potential node retains the source's homolog and assay limits.

Participants are Bacteria and the microeukaryotic/fungal aggregate. Direction is proposed bacterial effects on plant signaling and grazing defense; this is not an experimentally demonstrated competitive outcome or activity in every represented taxon.

### ecological_interactions[1].downstream[0]

graph: supported. Targets: CommunityMech:000236.

The candidate-host link to phage-DNA incorporation arrow is defensible as HYPOTHESIZED.

Replication in this source-specific candidate bacterial host could route labeled nucleotide carbon into phage DNA. Host assignment and infection dynamics remain inferred; the arrow does not establish measured lysis, mortality or nutrient release. The linked source evidence supplies the exact method and short excerpt.

### ecological_interactions[2].downstream[0]

graph: supported. Targets: CommunityMech:000236.

The candidate-host link to phage-DNA incorporation arrow is defensible as HYPOTHESIZED.

Replication in this source-specific candidate bacterial host could route labeled nucleotide carbon into phage DNA. Host assignment and infection dynamics remain inferred; the arrow does not establish measured lysis, mortality or nutrient release. The linked source evidence supplies the exact method and short excerpt.

### Origin, category, ecological state and two factors

scope: concern. Targets: CommunityMech:000236.

NATURAL, RHIZOSPHERE, labeling atmosphere and sampling times are supported; STABLE exceeds the temporal evidence.

### Growth medium and cultivation setup

scope: concern. Targets: CommunityMech:000236.

Reported current-study conditions are well attributed; root exclusion should not be restated as absence of all root influence.

Batch/OTHER microcosm context and a photosynthetic labeling atmosphere are appropriate. The 6/9-week harvests remain clear despite a nine-week maximum incubation field. Do not import the earlier trial's temperature, photoperiod, volume or soil classification without resolving their applicability.

### Carbon dioxide and metal/REE relevance

grounding: supported. Targets: CommunityMech:000236.

The carbon-dioxide anchor plus explicit isotope qualifiers preserves tracer identity; no demonstrated metal-processing phenotype is established.

Predicted siderophore biosynthetic potential occurs in the source and does not by itself require a metal-processing community classification. The graph correctly avoids making CO2 a measured phage-lysis product.

### Empty associated_datasets and available public source data

completeness: concern. Targets: CommunityMech:000236.

Source-linked projects and accession metadata permit concrete data enrichment within verified bounds.

The two named phages also have verified species anchors for optional pairwise-node precision; retain the broader community viral aggregate and the candidate-host qualifications.

### Snippets, caches, prior graph review and live issues

provenance: supported. Targets: CommunityMech:000236.

Fresh primary text confirms the cautious graph; earlier graph repair did not certify the remaining non-graph assertions.

### Native gates, terms, references and source boundaries

schema: supported. Targets: CommunityMech:000236.

Seven focused gates and cache preflight pass; nine ontology pairs and twenty-three snippets verify, while unrelated corpus network warning failures remain explicit.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000236.

Completeness is 30 and quality is 99; the low field score reflects the missing viral role component without making that a curation defect.

## Findings

### host-method-summary: The description assigns the wrong method to the second host link

major / open / confirmed; issue key: cm-000236-host-method-summary.

The summary says CRISPR targeting linked both phages to their candidate hosts. Only the Burkholderiales assignment uses CRISPR; the Catenulispora assignment uses shared GH25 sequence and phylogeny. The current graph already states this correctly, so the description gives readers a materially different evidentiary basis.

### aggregate-roles: Aggregate membership and enrichment do not establish uniform degrader roles

major / open / confirmed; issue key: cm-000236-aggregate-roles.

Four entries receive PRIMARY_DEGRADER from membership or predicted-host snippets. Isotope incorporation can arise through different trophic routes; annotation supports specific candidate functions, not a uniform complex-substrate-degradation phenotype across Bacteria, bacterivores/fungi and both host anchors. The bacterial entry also juxtaposes a labeled aggregate with all 55 recovered bins, although only 78% were detectably enriched.

### stable-state: STABLE is not established by the unreplicated time series

minor / open / confirmed; issue key: cm-000236-stable-state.

The source explicitly allows undetected succession because replication was inadequate. Lack of detected time separation therefore does not establish stable equilibrium, while the graph discussion already records this limitation.

### root-exclusion: Root exclusion is overstated as absence of root influence

minor / open / confirmed; issue key: cm-000236-root-exclusion.

cultivation_setup.instrument_detail says the mesh-bag soil experiences conditions without root influence. The design excludes roots while sharing microcosm conditions; the cited earlier method describes minimal influence, not complete exclusion of diffusible root effects.

### dataset-links: Source sequencing and annotation resources are not linked

minor / open / confirmed; issue key: cm-000236-dataset-links.

associated_datasets is empty despite accessible project, sequence-accession and annotation-collection metadata directly identified by the source. These distinguish recovered bacterial bins, phage genomes and eukaryotic marker sequences.

## Recommended Actions And Acceptance Checks

### fix-host-method-summary

Align the description with the two distinct candidate-host methods and retain their uncertainty.

- CRISPR is attributed only to the Burkholderiales candidate.
- GH25 similarity/phylogeny is attributed to the Catenulispora candidate.
- Neither candidate is described as an experimentally confirmed infection.
- Reference validation passes; supported graph qualifications remain intact.

### fix-aggregate-roles

Define recovered and detectably enriched subsets explicitly, attach source-bin functional evidence where available, and qualify or remove roles that exceed it.

- Do not treat all 55 recovered genomes as detectably labeled.
- Do not infer complex-substrate degradation solely from carbon assimilation, bacterivory, membership or predicted plant interaction.
- Specific genomic degradation potential may be retained with its taxon and computational tier; no uniform replacement role is invented.
- Keep nested aggregate identity explicit and rerun strict, term, reference and network checks.

### fix-stable-state

Remove or qualify the unsupported stability assertion using a source-backed state representation permitted by the schema.

- No equilibrium inference is drawn from a nonsignificant or underpowered temporal comparison.
- Laboratory observation alone is not treated as engineered community identity.
- Strict validation passes and the replication limitation remains explicit.

### fix-root-exclusion

Describe paired bulk soil as root-excluding soil sharing microcosm conditions, without claiming zero root-derived influence.

- Preserve the one-micrometer mesh and paired sampling design.
- Do not infer complete solute isolation from physical root exclusion.
- Do not import earlier trial conditions or its different soil classification.
- Reference validation passes.

### fix-dataset-links

Add evidence-backed data links with the correct data type, study scope and metadata-verification limits.

- Use PRJNA419965 and source accession/collection links without asserting raw-data reanalysis.
- Keep endpoint verification distinct from coverage of every range member.
- Do not generalize complete genome or complete 18S status across all deposits.
- Strict/reference checks pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml; Entire record: five taxonomic entries, four nodes, two arrows, soil growth medium and cultivation setup | supports | The record describes a natural rhizosphere sampled in planted microcosms; broad taxonomic aggregates overlap their named host candidates and are not five distinct isolates. |
| fulltext | PMID:34468166; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8550312/fullTextXML | supports | Fresh full main text, all Results/Discussion/Methods, figure captions and data availability were assessed. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=34468166&amp;retmode=xml; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=34468166&amp;retmode=xml | supports | Public publication metadata identifies the corresponding DOI/PMID and source article. |
| crossref | https://api.crossref.org/works/10.1128/mSphere.00085-21; https://api.crossref.org/works/10.1128/mSphere.00085-21 | supports | Public publication metadata identifies the corresponding DOI/PMID and source article. |
| reference41-fulltext | PMID:26242625; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4526712/fullTextXML | supports | The explicitly cited earlier protocol was inspected for identity and full Methods only, not certified as the same experiment. |
| reference41-pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=26242625&amp;retmode=xml; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=26242625&amp;retmode=xml | supports | Public publication metadata identifies the corresponding DOI/PMID and source article. |
| recovered-vs-enriched | PMID:34468166; Results s2-2; Fig. 3-4; enrichment Methods s4-5 | supports | Fifty-five bacterial bins were recovered, but 78% were detectably enriched. Eukaryotic scaffolds span multiple trophic types; isotope incorporation does not uniformly identify complex-substrate degraders. The threshold is model-derived and the trial lacks biological replication. |
| phage-label | PMID:34468166; Results s2-2 and s2-6; Discussion s3 | supports | Circular phage DNA contains tracer; active infection, host mortality and nutrient release are interpretations rather than directly measured rates. |
| burk-link | PMID:34468166; Results s2-6: Burkholderiales_62_29 and phage 68_11 | supports | The candidate link uses a 33-bp CRISPR spacer match with two mismatches; pathogenicity remains predicted from genome content. |
| cat-link | PMID:34468166; Results s2-6: Catenulisporales_70_18 and phage 69_17; Fig. S7 caption | supports | The separate candidate link uses GH25 similarity (77% amino-acid identity) and phylogeny, not CRISPR. |
| functional-potential | PMID:34468166; Results s2-3 to s2-5; Discussion s3; sequence annotation Methods s4-4 | supports | Annotations support proposed plant signaling, pathogenicity and grazing-defense functions, with alternative substrates and genomic contexts considered; related-study expression is not activity measured in this SIP trial. |
| state-limit | PMID:34468166; Discussion s3, opening section; enrichment Methods s4-5 | supports | Failure to detect temporal separation does not establish stability; insufficient replication could conceal succession. |
| trial-conditions | PMID:34468166; Methods s4-1: Plant growth and 13CO2 labeling | supports | The encoded soil source, moisture, labeling atmosphere and destructive 0/6/9-week design match the current paper. A root-excluding bag shares microcosm conditions; absence of roots is not proof of zero diffusible root influence. Temperature, pH and photoperiod are not supplied for this trial. |
| linked-protocol | PMID:26242625; Materials and Methods: Experimental design | supports | The cited method paper describes 160 microcosms, two seasons, 400/700-ppm CO2, 16-hour light and maximum air temperature 28 C. Its coarse-loamy Ultic Haploxeroll differs from the current paper's fine-loamy Typic Haploxeralf. These are method-attributed details, not automatically validated SIP-trial conditions. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum; EcologicalStateEnum; taxonomy and evidence definitions | supports | PRIMARY_DEGRADER means complex-substrate degradation; STABLE implies an equilibrium/stable community. Isotope enrichment, membership, genomic prediction and direct functional assays require distinct claim support. A missing optional viral role is not a schema defect. |
| ontology | Local OAK NCBITaxon, ENVO, GO and CHEBI snapshots; Nine unique ID/label pairs across eighteen occurrences | supports | All labels match. Domain/order/genus anchors remain broad; GO host perturbation is proposed infection context rather than validated infection. Carbon dioxide is the parent molecular identity, while isotope enrichment is explicit in the preferred term and experimental fields. |
| phage-grounding | Local OAK NCBITaxon snapshot and source accession metadata; phage-grounding-candidates.json | supports | Species anchors NCBITaxon:2718473 (Burkholderiales phage 68_11) and NCBITaxon:2718474 (Catenulispora phage 69_17) match the named source phages; they offer optional precision without validating the inferred hosts. |
| snippets | kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml; All 23 occurrences, 21 unique, against pinned caches and fresh primary XML | supports | All occurrences match fresh full text and the markdown cache after Unicode/whitespace normalization; twelve also occur in the text abstract cache. The markdown abstract_only header is stale despite appended substantive full text. |
| history | history/records/Avena_Rhizosphere_CrossKingdom_SIP_Community; reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml; One sidecar and exact prior-decision row, lines 264-321 | supports | The prior graph repair matches the current target hash and explicitly excludes non-graph metadata certification. |
| issue-1249 | https://github.com/CultureBotAI/CommunityMech/issues/1249; Fresh public issue body and status | supports | Issue 1249 is closed after graph-only repair; it does not certify non-graph metadata. |
| issue-529 | https://github.com/CultureBotAI/CommunityMech/issues/529; Fresh public issue body and status | supports | Issue 529 is a closed general historical warning about wrong-organism cultivation attribution, not evidence of an Avena defect. |
| search | Owned-worktree kb/taxa, records, caches, history and prior decisions; Ignored-inclusive target/member/source lookup | supports | The bounded search locates the pinned provenance and assesses reusable candidates without inferring species identity from broad labels. |
| datasets-source | PMID:34468166; Methods s4-6: Data availability | supports | The source lists PRJNA419965; experiments SRX6701119-SRX6701130; phages MN304815.1-MN304824.1; 18S records MT533858-MT533883; MAG masters JAEKKE000000000-JAEKMG000000000; and Figshare collection 5405805. Metadata checks cover only selected range endpoints, not all records or biological contents. |
| bioproject | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&amp;id=419965&amp;retmode=xml; Public project/collection metadata only | supports | The metadata identifies the source-linked project or collection; biological contents and sequence analyses were not repeated. |
| figshare-5405805 | https://api.figshare.com/v2/collections/5405805; Public project/collection metadata only | supports | The metadata identifies the source-linked project or collection; biological contents and sequence analyses were not repeated. |
| datasets | Source-linked project, collection and bounded accession endpoints; dataset-verification.json | supports | Project and collection metadata agree; selected phage and MAG endpoints link to the project. The two checked 18S endpoints describe partial sequences, so the source's several complete 18S sequences must not be generalized to every deposit. Intermediate accessions and data contents remain uninspected. |
| adapter | Optional kg-microbe-sources adapter; Explicit same-batch04-runtime discovery reuse | supports | No installed runner/module was available; no strain/expression-module coverage was queried and the external-checkout candidate was not executed. |
| native-target | NetworkIntegrityAuditor().audit_community(target); support-audit.json: targeted diagnostic and native rubric | supports | All five entries are covered through four nodes and two arrows; native status is COMPLETE. Four node evidence items give mean evidence one; missing viral role withholds the required-field score without constituting a schema failure. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml; Actual execution 2026-10-21T07:50:11.137968+00:00 to 2026-10-21T07:50:12.001587+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-strict kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml --out /private/tmp/cm-review-session/batch-04/000236/strict-report.tsv; Actual execution 2026-10-21T07:50:11.138195+00:00 to 2026-10-21T07:50:13.512798+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-terms kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml; Actual execution 2026-10-21T07:50:11.138331+00:00 to 2026-10-21T07:50:13.328045+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-gtdb kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml; Actual execution 2026-10-21T07:50:12.001862+00:00 to 2026-10-21T07:50:12.091092+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-gtdb-domain kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml; Actual execution 2026-10-21T07:50:12.091427+00:00 to 2026-10-21T07:50:13.588371+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-history history/records/Avena_Rhizosphere_CrossKingdom_SIP_Community; Actual execution 2026-10-21T07:50:13.328491+00:00 to 2026-10-21T07:50:14.098259+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T07:50:14.099026+00:00 to 2026-10-21T07:50:14.178231+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-references-explained kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml; Actual execution 2026-10-21T07:50:14.178518+00:00 to 2026-10-21T07:50:15.306849+00:00 | supports | Target native reference validation passed; scientific meaning was assessed separately. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T07:06:05.543108+00:00 to 2026-10-21T07:06:16.498440+00:00 | supports | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T07:06:16.498920+00:00 to 2026-10-21T07:06:23.361213+00:00 | supports | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |

## Limits And Additional Notes

- The main paper and all main Methods were read; separate supplement payloads, figure images and raw data were not reanalyzed. Supplement captions were inspected, and reference41 coverage is limited to publication identity and Methods.
- The unreplicated experiment uses a model-derived enrichment threshold and growth assumptions; isotope incorporation does not establish specific infection dynamics, mortality or lysis-mediated nutrient flux.
- Nested taxonomic aggregates and genome-bin identities do not authenticate isolates or establish uniform roles. Historical GTDB mapping counts were not recomputed, and no viral role was invented to improve completeness.
- The earlier method paper has different soil classification, scale and treatment design; its temperature, photoperiod and other parameters were not imported as verified current-trial conditions.
- Source data checks cover metadata and selected accession endpoints, not all range members or biological contents. Partial 18S endpoint metadata does not refute the narrower source statement that several complete sequences were recovered.
- The optional structured adapter was unavailable; same-runtime discovery was reused and no external-checkout runner was executed.
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 16 words for Starr2021 and 5 for Shi2015.
- The stale abstract_only cache header was documented without altering its substantive appended full text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T075602Z-avena-rhizosphere-sip-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Avena rhizosphere SIP: whole-record source review'
started_at: '2026-10-21T07:49:54.902339Z'
finished_at: '2026-10-21T07:56:02.802363Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Canonical target unchanged; prior codex graph curation prevents
    person-level independence claims. Separate agents checked ontology, native gates,
    snippets, history, metadata and metrics; root independently read the primary study
    and linked Methods.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Two major findings concern the summary host-assignment method and aggregate
  functional attribution. Three minor findings concern unsupported stability, root-exclusion
  wording and absent source-data links. All four graph nodes and both hypothesized
  arrows remain supported at their stated scope. Seven focused gates and cache preflight
  pass; corpus network checks retain unrelated warning failures.
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
  - path: history/records/Avena_Rhizosphere_CrossKingdom_SIP_Community/2026-10-05T101149Z-codex-564280.yaml
    sha256: 4931b2cde4f2d5abef468fe664bf851151e6033f5f6b257da735268b3ab9f0d8
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    sha256: 80f704ab28ca001665f3978357394d856e75221f2e58f9f9ab34eabd2b761ea9
    role: target
  - path: references_cache/PMID_34468166.md
    sha256: 74412ad7bd92ddbfe6cff558d2ccf001e08aff58aecd9ecefc37f46a127767e7
    role: context
  - path: references_cache/PMID_34468166.txt
    sha256: 669cdfc71bb01e2e6ed351af724a5aa8d13c6d10caa31a37e12ff48a4c58e0a8
    role: context
  - path: reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml
    sha256: 5076ec8295dacfaae0ae1d829836e4380a312a702c4a43df5f604c3b1b1e0ad3
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
- target_id: CommunityMech:000236
  path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  label: Avena Rhizosphere Cross-Kingdom 13C-SIP Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
scope:
  description: 'Entire record: five taxonomic entries, four nodes, two arrows, two
    factors, soil growth medium, cultivation setup and twenty-three evidence occurrences;
    fresh complete primary main text, Methods of its cited protocol paper, publication
    metadata and selected source data metadata. No raw sequencing, isotope, growth
    or biochemical analyses were repeated.'
  selection: Next uncovered maintained path after CommunityMech:000451 in batch04;
    one resolved natural-community record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000236
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000236
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000236
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-strict kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    --out /private/tmp/cm-review-session/batch-04/000236/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000236
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-terms kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000236
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000236
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb-domain kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000236
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-history history/records/Avena_Rhizosphere_CrossKingdom_SIP_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000236
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target native reference validation passed; scientific meaning was assessed
    separately.
  target_ids:
  - CommunityMech:000236
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-references-explained kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000236
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
  - CommunityMech:000236
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
  name: Publication identity and scientific source assessment
  status: passed
  required: true
  summary: The full primary main text and cited earlier protocol Methods were read
    with explicit study boundaries.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - fulltext
  - pubmed
  - crossref
  - reference41-fulltext
  - reference41-pubmed
- check_id: source-data
  name: Selected public source data metadata
  status: passed
  required: true
  summary: Project/collection and bounded accession metadata verify, with partial-18S
    and uninspected-range limits retained.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - datasets
  - bioproject
  - figshare-5405805
- check_id: cross-mech
  name: Encoded medium and ingredient-Mech linkages
  status: not_applicable
  required: false
  summary: The soil microcosm record encodes no CultureMech or MediaIngredientMech
    links to verify.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - trial-conditions
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Same-runtime discovery was reused; no expression-module coverage was queried.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  locator: 'Entire record: five taxonomic entries, four nodes, two arrows, soil growth
    medium and cultivation setup'
  summary: The record describes a natural rhizosphere sampled in planted microcosms;
    broad taxonomic aggregates overlap their named host candidates and are not five
    distinct isolates.
  support: supports
  accessed_at: '2026-10-21T07:56:02.797385Z'
- evidence_id: fulltext
  kind: primary_source
  reference: PMID:34468166
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8550312/fullTextXML
  summary: Fresh full main text, all Results/Discussion/Methods, figure captions and
    data availability were assessed.
  support: supports
  accessed_at: '2026-10-21T07:50:25.912812Z'
  snapshot_sha256: 1749e35214679e4511a5d73cdc632a82157ee86afd122970bdd6fa63312d5384
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=34468166&retmode=xml
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=34468166&retmode=xml
  summary: Public publication metadata identifies the corresponding DOI/PMID and source
    article.
  support: supports
  accessed_at: '2026-10-21T07:50:15.251018Z'
  snapshot_sha256: c8baa4afd8a717e07555efc2068e41449903904088ed2b8c6882116345238ea3
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1128/mSphere.00085-21
  locator: https://api.crossref.org/works/10.1128/mSphere.00085-21
  summary: Public publication metadata identifies the corresponding DOI/PMID and source
    article.
  support: supports
  accessed_at: '2026-10-21T07:50:15.296171Z'
  snapshot_sha256: e55ee5d56d0c1b3399ad38ea9e20db943c3062132ebb9c85a4bab3a5dedea609
- evidence_id: reference41-fulltext
  kind: primary_source
  reference: PMID:26242625
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4526712/fullTextXML
  summary: The explicitly cited earlier protocol was inspected for identity and full
    Methods only, not certified as the same experiment.
  support: supports
  accessed_at: '2026-10-21T07:51:00.553917Z'
  snapshot_sha256: 490a78a699ace566984c7eec47a658567aa73ec1854ce56b0e5b785bb83fec01
- evidence_id: reference41-pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=26242625&retmode=xml
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=26242625&retmode=xml
  summary: Public publication metadata identifies the corresponding DOI/PMID and source
    article.
  support: supports
  accessed_at: '2026-10-21T07:50:52.604837Z'
  snapshot_sha256: 202a1829056b27d7250f7f784443d343bea1a8e4697ab01218f40df3a88a6e21
- evidence_id: recovered-vs-enriched
  kind: primary_source
  reference: PMID:34468166
  locator: Results s2-2; Fig. 3-4; enrichment Methods s4-5
  summary: Fifty-five bacterial bins were recovered, but 78% were detectably enriched.
    Eukaryotic scaffolds span multiple trophic types; isotope incorporation does not
    uniformly identify complex-substrate degraders. The threshold is model-derived
    and the trial lacks biological replication.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798241Z'
- evidence_id: phage-label
  kind: primary_source
  reference: PMID:34468166
  locator: Results s2-2 and s2-6; Discussion s3
  summary: Circular phage DNA contains tracer; active infection, host mortality and
    nutrient release are interpretations rather than directly measured rates.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798243Z'
  quote: highly labeled
- evidence_id: burk-link
  kind: primary_source
  reference: PMID:34468166
  locator: 'Results s2-6: Burkholderiales_62_29 and phage 68_11'
  summary: The candidate link uses a 33-bp CRISPR spacer match with two mismatches;
    pathogenicity remains predicted from genome content.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798244Z'
  quote: possible host
- evidence_id: cat-link
  kind: primary_source
  reference: PMID:34468166
  locator: 'Results s2-6: Catenulisporales_70_18 and phage 69_17; Fig. S7 caption'
  summary: The separate candidate link uses GH25 similarity (77% amino-acid identity)
    and phylogeny, not CRISPR.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798246Z'
  quote: recent lateral gene transfer event
- evidence_id: functional-potential
  kind: primary_source
  reference: PMID:34468166
  locator: Results s2-3 to s2-5; Discussion s3; sequence annotation Methods s4-4
  summary: Annotations support proposed plant signaling, pathogenicity and grazing-defense
    functions, with alternative substrates and genomic contexts considered; related-study
    expression is not activity measured in this SIP trial.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798247Z'
  quote: genomic potential
- evidence_id: state-limit
  kind: primary_source
  reference: PMID:34468166
  locator: Discussion s3, opening section; enrichment Methods s4-5
  summary: Failure to detect temporal separation does not establish stability; insufficient
    replication could conceal succession.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798248Z'
  quote: not sufficient to detect them
- evidence_id: trial-conditions
  kind: primary_source
  reference: PMID:34468166
  locator: 'Methods s4-1: Plant growth and 13CO2 labeling'
  summary: The encoded soil source, moisture, labeling atmosphere and destructive
    0/6/9-week design match the current paper. A root-excluding bag shares microcosm
    conditions; absence of roots is not proof of zero diffusible root influence. Temperature,
    pH and photoperiod are not supplied for this trial.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798249Z'
- evidence_id: linked-protocol
  kind: primary_source
  reference: PMID:26242625
  locator: 'Materials and Methods: Experimental design'
  summary: The cited method paper describes 160 microcosms, two seasons, 400/700-ppm
    CO2, 16-hour light and maximum air temperature 28 C. Its coarse-loamy Ultic Haploxeroll
    differs from the current paper's fine-loamy Typic Haploxeralf. These are method-attributed
    details, not automatically validated SIP-trial conditions.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798251Z'
  quote: minimal influence by plant roots
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum; EcologicalStateEnum; taxonomy and evidence definitions
  summary: PRIMARY_DEGRADER means complex-substrate degradation; STABLE implies an
    equilibrium/stable community. Isotope enrichment, membership, genomic prediction
    and direct functional assays require distinct claim support. A missing optional
    viral role is not a schema defect.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798251Z'
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, GO and CHEBI snapshots
  locator: Nine unique ID/label pairs across eighteen occurrences
  summary: All labels match. Domain/order/genus anchors remain broad; GO host perturbation
    is proposed infection context rather than validated infection. Carbon dioxide
    is the parent molecular identity, while isotope enrichment is explicit in the
    preferred term and experimental fields.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798476Z'
  snapshot_sha256: 70f9ecebc38dbec8d5c5cd9bd5ab54fa913e17417c28b9eb2b03d6e614905b32
- evidence_id: phage-grounding
  kind: authority
  reference: Local OAK NCBITaxon snapshot and source accession metadata
  locator: phage-grounding-candidates.json
  summary: Species anchors NCBITaxon:2718473 (Burkholderiales phage 68_11) and NCBITaxon:2718474
    (Catenulispora phage 69_17) match the named source phages; they offer optional
    precision without validating the inferred hosts.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798632Z'
  snapshot_sha256: 2dfab90efe3ad881fccbd13dd82a9f5ef00e012abfd9361aca0527d19e25f77e
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  locator: All 23 occurrences, 21 unique, against pinned caches and fresh primary
    XML
  summary: All occurrences match fresh full text and the markdown cache after Unicode/whitespace
    normalization; twelve also occur in the text abstract cache. The markdown abstract_only
    header is stale despite appended substantive full text.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798779Z'
  snapshot_sha256: 7818c5cbb74708a3e9d6100d6124062d83c16e538f3657dae87cc2712d36bd8e
- evidence_id: history
  kind: record_content
  reference: history/records/Avena_Rhizosphere_CrossKingdom_SIP_Community; reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml
  locator: One sidecar and exact prior-decision row, lines 264-321
  summary: The prior graph repair matches the current target hash and explicitly excludes
    non-graph metadata certification.
  support: supports
  accessed_at: '2026-10-21T07:56:02.798900Z'
  snapshot_sha256: 8ed25e547ce2044fc4b4f41407464715b01fd000e7a86dcaba326e5fc466c7ad
- evidence_id: issue-1249
  kind: database
  reference: https://github.com/CultureBotAI/CommunityMech/issues/1249
  locator: Fresh public issue body and status
  summary: Issue 1249 is closed after graph-only repair; it does not certify non-graph
    metadata.
  support: supports
  accessed_at: '2026-10-21T07:49:59.871234Z'
  snapshot_sha256: cc8fb4aa47d6090a82b6dad8220e30d505001643ad6f9d1569be6c0581a1eaac
- evidence_id: issue-529
  kind: database
  reference: https://github.com/CultureBotAI/CommunityMech/issues/529
  locator: Fresh public issue body and status
  summary: Issue 529 is a closed general historical warning about wrong-organism cultivation
    attribution, not evidence of an Avena defect.
  support: supports
  accessed_at: '2026-10-21T07:51:35.682934Z'
  snapshot_sha256: 17f58bcdc422526ced964a124b061d0037e8986d813e04f410f5f9c90e718f4a
- evidence_id: search
  kind: search
  reference: Owned-worktree kb/taxa, records, caches, history and prior decisions
  locator: Ignored-inclusive target/member/source lookup
  summary: The bounded search locates the pinned provenance and assesses reusable
    candidates without inferring species identity from broad labels.
  support: supports
  accessed_at: '2026-10-21T07:56:02.799597Z'
  snapshot_sha256: b162a6a0302fd3938b61189484445ce7fb7ef5dff4e1df6c38f9375843cb5982
  search_scope: rg --no-ignore --hidden over the stated owned-worktree directories;
    no global absence claim.
- evidence_id: datasets-source
  kind: primary_source
  reference: PMID:34468166
  locator: 'Methods s4-6: Data availability'
  summary: The source lists PRJNA419965; experiments SRX6701119-SRX6701130; phages
    MN304815.1-MN304824.1; 18S records MT533858-MT533883; MAG masters JAEKKE000000000-JAEKMG000000000;
    and Figshare collection 5405805. Metadata checks cover only selected range endpoints,
    not all records or biological contents.
  support: supports
  accessed_at: '2026-10-21T07:56:02.799601Z'
- evidence_id: bioproject
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=419965&retmode=xml
  locator: Public project/collection metadata only
  summary: The metadata identifies the source-linked project or collection; biological
    contents and sequence analyses were not repeated.
  support: supports
  accessed_at: '2026-10-21T07:50:52.610688Z'
  snapshot_sha256: d80b292fed3ee7d0931f09d94711bb862f3ad0c728cf7e01d59658aa6a56204f
- evidence_id: figshare-5405805
  kind: database
  reference: https://api.figshare.com/v2/collections/5405805
  locator: Public project/collection metadata only
  summary: The metadata identifies the source-linked project or collection; biological
    contents and sequence analyses were not repeated.
  support: supports
  accessed_at: '2026-10-21T07:51:22.303937Z'
  snapshot_sha256: a99a3d8631bc4df1d3b072aeb1b32fb1198c036312fe3e2cb304363cee234be2
- evidence_id: datasets
  kind: validation
  reference: Source-linked project, collection and bounded accession endpoints
  locator: dataset-verification.json
  summary: Project and collection metadata agree; selected phage and MAG endpoints
    link to the project. The two checked 18S endpoints describe partial sequences,
    so the source's several complete 18S sequences must not be generalized to every
    deposit. Intermediate accessions and data contents remain uninspected.
  support: supports
  accessed_at: '2026-10-21T07:56:02.800052Z'
  snapshot_sha256: 21195a0722a5adc67c01d894344eb432b53dddf72c4e5073f088e3b4f9d81cba
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources adapter
  locator: Explicit same-batch04-runtime discovery reuse
  summary: No installed runner/module was available; no strain/expression-module coverage
    was queried and the external-checkout candidate was not executed.
  support: supports
  accessed_at: '2026-10-21T07:56:02.800169Z'
  snapshot_sha256: 53e2ef9a6bff241f76fa8ce579026ca60fe3eff4a83fc9ee3ddcbf2eeca64067
  search_scope: Prior fresh batch04 PATH, virtualenv, module and bounded ignored-inclusive
    discovery, explicitly reused.
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: 'support-audit.json: targeted diagnostic and native rubric'
  summary: All five entries are covered through four nodes and two arrows; native
    status is COMPLETE. Four node evidence items give mean evidence one; missing viral
    role withholds the required-field score without constituting a schema failure.
  support: supports
  accessed_at: '2026-10-21T07:56:02.800304Z'
  snapshot_sha256: 6dec56d6b93bafcd2b2ab2370018e044bf0e90480f79274c34e58476ce26cbf6
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  locator: Actual execution 2026-10-21T07:50:11.137968+00:00 to 2026-10-21T07:50:12.001587+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T07:50:12.001587Z'
  snapshot_sha256: 36764e2fb389f2df1186ef284e26138942758d8035b1293d29c5935e96640000
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-strict kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    --out /private/tmp/cm-review-session/batch-04/000236/strict-report.tsv
  locator: Actual execution 2026-10-21T07:50:11.138195+00:00 to 2026-10-21T07:50:13.512798+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T07:50:13.512798Z'
  snapshot_sha256: a805ca4701364be85c0865aa1c0dfc65d5ada736cf31e2ba00d356ef5677103e
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-terms kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  locator: Actual execution 2026-10-21T07:50:11.138331+00:00 to 2026-10-21T07:50:13.328045+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T07:50:13.328045Z'
  snapshot_sha256: 26d2a7cf64ecec367d52d6ad750828c40ad6d7af43d7347846a96c464afb4096
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  locator: Actual execution 2026-10-21T07:50:12.001862+00:00 to 2026-10-21T07:50:12.091092+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T07:50:12.091092Z'
  snapshot_sha256: 2ec9e82c2c0f39d8afbf1f4a0b505baa277d4e0c80dca151def8641611b9cdc1
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb-domain kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  locator: Actual execution 2026-10-21T07:50:12.091427+00:00 to 2026-10-21T07:50:13.588371+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T07:50:13.588371Z'
  snapshot_sha256: d18665a464f2604a12d80a6501f1a29fbdf863ef8b3f8e55c06ff7e244348a91
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-history history/records/Avena_Rhizosphere_CrossKingdom_SIP_Community
  locator: Actual execution 2026-10-21T07:50:13.328491+00:00 to 2026-10-21T07:50:14.098259+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T07:50:14.098259Z'
  snapshot_sha256: b644d0a44235fca1ffbb6cb86ea95e7b29936c3e722061ebf2e7c9971d70107f
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T07:50:14.099026+00:00 to 2026-10-21T07:50:14.178231+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T07:50:14.178231Z'
  snapshot_sha256: b988233a591cbcd54bd8bf89d872f4afe326bab241c5aaadf921169551956d4c
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-references-explained kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
  locator: Actual execution 2026-10-21T07:50:14.178518+00:00 to 2026-10-21T07:50:15.306849+00:00
  summary: Target native reference validation passed; scientific meaning was assessed
    separately.
  support: supports
  accessed_at: '2026-10-21T07:50:15.306849Z'
  snapshot_sha256: a4756f16c1cd97d0efa74d6f13aa5e5d4a9e9ce8b9363da70f475cb420fa33ff
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
  topic: Natural community, nested taxonomic scopes and experimental setting
  outcome: supported
  summary: The target is resolved as the Avena rhizosphere SIP study; its aggregate
    taxonomy does not denote a five-member defined consortium.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - recovered-vs-enriched
  - trial-conditions
  - ontology
  dimensions:
  - name: community_scope
    value: Natural rhizosphere community assayed in planted soil microcosms
    definition: Broad bacterial/eukaryotic/viral entries overlap nested host candidates
      and recovered populations.
    evidence_ids:
    - record
    - recovered-vs-enriched
  - name: source_strain
    value: Genome bins and marker scaffolds, not authenticated isolate strains
    definition: Burkholderiales_62_29 and Catenulisporales_70_18 identify candidate
      host populations; broad anchors do not transfer phenotypes to whole orders or
      genera.
    evidence_ids:
    - burk-link
    - cat-link
    - ontology
  - name: environment
    value: Avena fatua rhizosphere with paired root-excluding bulk soil
    definition: The host is ecological context rather than an additional microbial
      member.
    evidence_ids:
    - record
    - trial-conditions
  - name: medium
    value: Hopland grassland soil in labeled microcosms
    definition: Current-trial conditions are explicit; earlier protocol details remain
      separately attributed because design and soil classification differ.
    evidence_ids:
    - trial-conditions
    - linked-protocol
  - name: experimental_setting
    value: Destructive sampling at 0, 6 and 9 weeks without biological replication
    definition: Density fractions and paired compartments do not substitute for replicate
      communities.
    evidence_ids:
    - trial-conditions
    - recovered-vs-enriched
    - state-limit
  - name: evidence_tier
    value: Tracer incorporation, computed enrichment and inferred host/functions
    definition: SIP establishes incorporation within its model limits; CRISPR/GH25
      and functional homology support distinct computational inferences.
    evidence_ids:
    - phage-label
    - burk-link
    - cat-link
    - functional-potential
  - name: grounding_status
    value: Nine canonical pairs with explicit aggregate-rank limits
    definition: GTDB checks verify syntax/domain rather than recomputing historical
      mapping counts.
    evidence_ids:
    - ontology
- assessment_id: taxonomy
  area: grounding
  topic: All five entries and four PRIMARY_DEGRADER assignments
  outcome: concern
  summary: Membership is source-backed, but recovered versus enriched subsets and
    taxon-specific functional potential must be separated from uniform degrader roles.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - schema
  - recovered-vs-enriched
  - functional-potential
  - ontology
- assessment_id: node-0
  area: graph
  topic: Plant-Derived Carbon Incorporation into Phage DNA
  outcome: supported
  summary: The node correctly separates tracer incorporation from inferred infection
    and lysis-driven recycling.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - phage-label
  details: Participants are the Bacteria and Viruses aggregates. Direction is plant-derived
    carbon reaching phage DNA through candidate bacterial replication pathways in
    the labeled rhizosphere; isotope enrichment alone measures neither bacterial mortality
    nor nutrient-release flux.
- assessment_id: node-1
  area: graph
  topic: Candidate Burkholderiales Phage-Host Link
  outcome: supported
  summary: The PARTIAL CRISPR-supported host hypothesis is appropriately qualified.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - burk-link
  - functional-potential
  details: Direction is the phage aggregate toward the Burkholderiales_62_29 candidate
    represented by NCBITaxon:80840. Both infection and pathogenicity are inferred;
    GO:0044003 remains proposed host-perturbation context, not a measured disease
    phenotype.
- assessment_id: node-2
  area: graph
  topic: Candidate Catenulispora Phage-Host Link
  outcome: supported
  summary: The node correctly identifies GH25/phylogeny support rather than CRISPR
    evidence.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - cat-link
  details: Direction is the phage aggregate toward the Catenulisporales_70_18/Catenulispora
    candidate represented by NCBITaxon:414878. The source links phage 69_17 by shared
    gene history; infection and plant-growth benefit remain unvalidated.
- assessment_id: node-3
  area: graph
  topic: 13C-Labeled Plant-Signaling and Defense Functions
  outcome: supported
  summary: The computational-potential node retains the source's homolog and assay
    limits.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - functional-potential
  details: Participants are Bacteria and the microeukaryotic/fungal aggregate. Direction
    is proposed bacterial effects on plant signaling and grazing defense; this is
    not an experimentally demonstrated competitive outcome or activity in every represented
    taxon.
- assessment_id: arrow-1
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: supported
  summary: The candidate-host link to phage-DNA incorporation arrow is defensible
    as HYPOTHESIZED.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - burk-link
  - phage-label
  details: Replication in this source-specific candidate bacterial host could route
    labeled nucleotide carbon into phage DNA. Host assignment and infection dynamics
    remain inferred; the arrow does not establish measured lysis, mortality or nutrient
    release. The linked source evidence supplies the exact method and short excerpt.
- assessment_id: arrow-2
  area: graph
  topic: ecological_interactions[2].downstream[0]
  outcome: supported
  summary: The candidate-host link to phage-DNA incorporation arrow is defensible
    as HYPOTHESIZED.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - cat-link
  - phage-label
  details: Replication in this source-specific candidate bacterial host could route
    labeled nucleotide carbon into phage DNA. Host assignment and infection dynamics
    remain inferred; the arrow does not establish measured lysis, mortality or nutrient
    release. The linked source evidence supplies the exact method and short excerpt.
- assessment_id: environment
  area: scope
  topic: Origin, category, ecological state and two factors
  outcome: concern
  summary: NATURAL, RHIZOSPHERE, labeling atmosphere and sampling times are supported;
    STABLE exceeds the temporal evidence.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - trial-conditions
  - state-limit
  - schema
- assessment_id: cultivation
  area: scope
  topic: Growth medium and cultivation setup
  outcome: concern
  summary: Reported current-study conditions are well attributed; root exclusion should
    not be restated as absence of all root influence.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - trial-conditions
  - linked-protocol
  - record
  details: Batch/OTHER microcosm context and a photosynthetic labeling atmosphere
    are appropriate. The 6/9-week harvests remain clear despite a nine-week maximum
    incubation field. Do not import the earlier trial's temperature, photoperiod,
    volume or soil classification without resolving their applicability.
- assessment_id: chemicals-metals
  area: grounding
  topic: Carbon dioxide and metal/REE relevance
  outcome: supported
  summary: The carbon-dioxide anchor plus explicit isotope qualifiers preserves tracer
    identity; no demonstrated metal-processing phenotype is established.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - ontology
  - functional-potential
  details: Predicted siderophore biosynthetic potential occurs in the source and does
    not by itself require a metal-processing community classification. The graph correctly
    avoids making CO2 a measured phage-lysis product.
- assessment_id: datasets
  area: completeness
  topic: Empty associated_datasets and available public source data
  outcome: concern
  summary: Source-linked projects and accession metadata permit concrete data enrichment
    within verified bounds.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - datasets-source
  - bioproject
  - figshare-5405805
  - datasets
  - phage-grounding
  details: The two named phages also have verified species anchors for optional pairwise-node
    precision; retain the broader community viral aggregate and the candidate-host
    qualifications.
- assessment_id: history
  area: provenance
  topic: Snippets, caches, prior graph review and live issues
  outcome: supported
  summary: Fresh primary text confirms the cautious graph; earlier graph repair did
    not certify the remaining non-graph assertions.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - history
  - snippets
  - issue-1249
  - issue-529
  - search
- assessment_id: validation
  area: schema
  topic: Native gates, terms, references and source boundaries
  outcome: supported
  summary: Seven focused gates and cache preflight pass; nine ontology pairs and twenty-three
    snippets verify, while unrelated corpus network warning failures remain explicit.
  target_ids:
  - CommunityMech:000236
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
  summary: Completeness is 30 and quality is 99; the low field score reflects the
    missing viral role component without making that a curation defect.
  target_ids:
  - CommunityMech:000236
  evidence_ids:
  - record
  - schema
  - native-target
  metrics:
  - name: completeness
    value: 30
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including all taxon roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). 0 + 5 + 0 + 10 + 5 + 10 + 0 + 0 = 30; a missing optional
      viral role withholds the required-field component, not schema validity.
  - name: validation_quality
    value: 99
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1=0, P2=2, P3=3, P4=0; 4 items / 4 nodes
      = 1; native COMPLETE. 100 - 20 - 6 + 10 + 15 = 99; this metric is not a scientific
      pass.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P2
    value: 2
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
- finding_id: host-method-summary
  issue_key: cm-000236-host-method-summary
  category: provenance
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: source or taxonomic attribution materially changes
    the inferred ecological mechanism.'
  rule_id: review-checklist.causal_claims
  status: open
  certainty: confirmed
  title: The description assigns the wrong method to the second host link
  description: The summary says CRISPR targeting linked both phages to their candidate
    hosts. Only the Burkholderiales assignment uses CRISPR; the Catenulispora assignment
    uses shared GH25 sequence and phylogeny. The current graph already states this
    correctly, so the description gives readers a materially different evidentiary
    basis.
  target_ids:
  - CommunityMech:000236
  field_paths:
  - description
  evidence_ids:
  - record
  - burk-link
  - cat-link
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
- finding_id: aggregate-roles
  issue_key: cm-000236-aggregate-roles
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: source or taxonomic attribution materially changes
    the inferred ecological mechanism.'
  rule_id: P2.4
  status: open
  certainty: confirmed
  title: Aggregate membership and enrichment do not establish uniform degrader roles
  description: Four entries receive PRIMARY_DEGRADER from membership or predicted-host
    snippets. Isotope incorporation can arise through different trophic routes; annotation
    supports specific candidate functions, not a uniform complex-substrate-degradation
    phenotype across Bacteria, bacterivores/fungi and both host anchors. The bacterial
    entry also juxtaposes a labeled aggregate with all 55 recovered bins, although
    only 78% were detectably enriched.
  target_ids:
  - CommunityMech:000236
  field_paths:
  - taxonomy[0].taxon_term
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  - taxonomy[3].functional_role
  - taxonomy[4].functional_role
  - taxonomy[*].evidence
  evidence_ids:
  - schema
  - recovered-vs-enriched
  - functional-potential
  - burk-link
  - cat-link
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
- finding_id: stable-state
  issue_key: cm-000236-stable-state
  category: scope
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded state, comparator wording or dataset-completeness
    defect with the qualified graph preserved.'
  rule_id: review-checklist.ecological_state
  status: open
  certainty: confirmed
  title: STABLE is not established by the unreplicated time series
  description: The source explicitly allows undetected succession because replication
    was inadequate. Lack of detected time separation therefore does not establish
    stable equilibrium, while the graph discussion already records this limitation.
  target_ids:
  - CommunityMech:000236
  field_paths:
  - ecological_state
  evidence_ids:
  - state-limit
  - schema
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
- finding_id: root-exclusion
  issue_key: cm-000236-root-exclusion
  category: scope
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded state, comparator wording or dataset-completeness
    defect with the qualified graph preserved.'
  rule_id: review-checklist.cultivation
  status: open
  certainty: confirmed
  title: Root exclusion is overstated as absence of root influence
  description: cultivation_setup.instrument_detail says the mesh-bag soil experiences
    conditions without root influence. The design excludes roots while sharing microcosm
    conditions; the cited earlier method describes minimal influence, not complete
    exclusion of diffusible root effects.
  target_ids:
  - CommunityMech:000236
  field_paths:
  - cultivation_setup[0].instrument_detail
  evidence_ids:
  - trial-conditions
  - linked-protocol
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
- finding_id: dataset-links
  issue_key: cm-000236-dataset-links
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded state, comparator wording or dataset-completeness
    defect with the qualified graph preserved.'
  rule_id: review-checklist.datasets
  status: open
  certainty: confirmed
  title: Source sequencing and annotation resources are not linked
  description: associated_datasets is empty despite accessible project, sequence-accession
    and annotation-collection metadata directly identified by the source. These distinguish
    recovered bacterial bins, phage genomes and eukaryotic marker sequences.
  target_ids:
  - CommunityMech:000236
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - datasets-source
  - bioproject
  - figshare-5405805
  - datasets
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
actions:
- action_id: fix-host-method-summary
  description: Align the description with the two distinct candidate-host methods
    and retain their uncertainty.
  finding_ids:
  - host-method-summary
  target_ids:
  - CommunityMech:000236
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
  acceptance_checks:
  - CRISPR is attributed only to the Burkholderiales candidate.
  - GH25 similarity/phylogeny is attributed to the Catenulispora candidate.
  - Neither candidate is described as an experimentally confirmed infection.
  - Reference validation passes; supported graph qualifications remain intact.
- action_id: fix-aggregate-roles
  description: Define recovered and detectably enriched subsets explicitly, attach
    source-bin functional evidence where available, and qualify or remove roles that
    exceed it.
  finding_ids:
  - aggregate-roles
  target_ids:
  - CommunityMech:000236
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Do not treat all 55 recovered genomes as detectably labeled.
  - Do not infer complex-substrate degradation solely from carbon assimilation, bacterivory,
    membership or predicted plant interaction.
  - Specific genomic degradation potential may be retained with its taxon and computational
    tier; no uniform replacement role is invented.
  - Keep nested aggregate identity explicit and rerun strict, term, reference and
    network checks.
- action_id: fix-stable-state
  description: Remove or qualify the unsupported stability assertion using a source-backed
    state representation permitted by the schema.
  finding_ids:
  - stable-state
  target_ids:
  - CommunityMech:000236
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
  acceptance_checks:
  - No equilibrium inference is drawn from a nonsignificant or underpowered temporal
    comparison.
  - Laboratory observation alone is not treated as engineered community identity.
  - Strict validation passes and the replication limitation remains explicit.
- action_id: fix-root-exclusion
  description: Describe paired bulk soil as root-excluding soil sharing microcosm
    conditions, without claiming zero root-derived influence.
  finding_ids:
  - root-exclusion
  target_ids:
  - CommunityMech:000236
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve the one-micrometer mesh and paired sampling design.
  - Do not infer complete solute isolation from physical root exclusion.
  - Do not import earlier trial conditions or its different soil classification.
  - Reference validation passes.
- action_id: fix-dataset-links
  description: Add evidence-backed data links with the correct data type, study scope
    and metadata-verification limits.
  finding_ids:
  - dataset-links
  target_ids:
  - CommunityMech:000236
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_CrossKingdom_SIP_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Use PRJNA419965 and source accession/collection links without asserting raw-data
    reanalysis.
  - Keep endpoint verification distinct from coverage of every range member.
  - Do not generalize complete genome or complete 18S status across all deposits.
  - Strict/reference checks pass.
limitations:
- The main paper and all main Methods were read; separate supplement payloads, figure
  images and raw data were not reanalyzed. Supplement captions were inspected, and
  reference41 coverage is limited to publication identity and Methods.
- The unreplicated experiment uses a model-derived enrichment threshold and growth
  assumptions; isotope incorporation does not establish specific infection dynamics,
  mortality or lysis-mediated nutrient flux.
- Nested taxonomic aggregates and genome-bin identities do not authenticate isolates
  or establish uniform roles. Historical GTDB mapping counts were not recomputed,
  and no viral role was invented to improve completeness.
- The earlier method paper has different soil classification, scale and treatment
  design; its temperature, photoperiod and other parameters were not imported as verified
  current-trial conditions.
- Source data checks cover metadata and selected accession endpoints, not all range
  members or biological contents. Partial 18S endpoint metadata does not refute the
  narrower source statement that several complete sequences were recovered.
- The optional structured adapter was unavailable; same-runtime discovery was reused
  and no external-checkout runner was executed.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 16 words for Starr2021 and 5 for Shi2015.
- The stale abstract_only cache header was documented without altering its substantive
  appended full text.
tags:
- record-review
- rhizosphere
- stable-isotope-probing
- batch-04
```
