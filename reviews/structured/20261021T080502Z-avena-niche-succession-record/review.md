# Avena rhizosphere and detritusphere succession: whole-record review

- Review: 20261021T080502Z-avena-niche-succession-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T07:59:42.409517Z
- Finished UTC: 2026-10-21T08:05:02.581213Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major finding groups non-graph guild and ingredient overclaims already covered by open issue 1296. Four minor findings concern stability, cultivation/control completeness, composite-detritus grounding and omitted data links. All five graph nodes and both hypothesized arrows remain supported at their qualified scope. Seven focused gates and cache preflight pass; unrelated corpus network warning failures remain explicit.

## Scope And Provenance

Entire record, all thirteen evidence occurrences, fresh published main text, relevant supplementary Methods/captions and complete Table S1, publication metadata and bounded project/archive metadata. All five nodes and two directed arrows assessed; no sequence, transcript or ecological reanalysis.

Selection: Next uncovered maintained path after CommunityMech:000236 in batch04; one resolved natural-community record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c6e5a9b9af2d05e12eaafb2555a53f3a079268f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000245 | kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml | maintained | Avena Rhizosphere and Detritusphere Niche-Differentiated Decomposer Guilds |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000245 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000245 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000245 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000245 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000245 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000245 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000245 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000245 | Target native reference validation passed; scientific meaning was assessed separately. |
| audit-network | failed | True | CommunityMech:000245 | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-network-quality | failed | True | CommunityMech:000245 | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| Publication identity and full scientific source assessment | passed | True | CommunityMech:000245 | Fresh published main text and relevant supplementary Methods were read with explicit inference limits. |
| Source data inventory and bounded metadata verification | passed | True | CommunityMech:000245 | The input BioProject verifies; source-reported JGI IDs and anonymous-access limitations remain explicit. |
| Encoded medium and ingredient-Mech linkages | not_applicable | False | CommunityMech:000245 | The record encodes no CultureMech or MediaIngredientMech links to verify. |
| Optional structured source adapter | unavailable | False | CommunityMech:000245 | Same-runtime discovery was reused; no expression-module coverage was queried. |

## Scientific And Domain Assessments

### Community, source populations and experimental context

identity: supported. Targets: CommunityMech:000245.

The record resolves to the Nuccio Avena soil study and explicitly represents an aggregate decomposer community.

### Aggregate Bacteria and PRIMARY_DEGRADER

grounding: concern. Targets: CommunityMech:000245.

The functional aggregate is defensible as expressed degradation potential, but its notes and binning-only evidence overstate substrate specialization.

Retain the explicit aggregate rather than inventing species or treating 282 reference genomes as a verified consortium. If greater granularity is curated, Fig. 4 supplies reference-population labels with mapping limits.

### ecological_interactions[0]: Functional Succession Outpaces Compositional Change

graph: supported. Targets: CommunityMech:000245.

The node is supported at its stated observational or qualified interpretive scope.

Community-wide transcript and 16S composition changes in paired compartments; temporal comparison, not organism-to-organism flux. GO carbohydrate metabolism identifies the measured functional context, not a reaction-rate assay.

### ecological_interactions[1]: Four Decomposition-Gene Expression Response Groups

graph: supported. Targets: CommunityMech:000245.

The node is supported at its stated observational or qualified interpretive scope.

The bacterial aggregate contains 24 responsive reference populations. Habitat/time contrasts yield expression groups; PARTIAL NICHE_PARTITIONING and polysaccharide context do not establish four obligate specialists or exchange among them.

### ecological_interactions[2]: Rhizosphere Upregulates Carbohydrate Depolymerization Transcripts

graph: supported. Targets: CommunityMech:000245.

The node is supported at its stated observational or qualified interpretive scope.

Living-root treatment is the exposure and the bacterial aggregate transcript response is the endpoint. The node correctly separates expression from enzyme activity, with final-timepoint treatment ranking qualified.

### ecological_interactions[3]: Proposed Niche-Differentiated Guild Coexistence

graph: supported. Targets: CommunityMech:000245.

The node is supported at its stated observational or qualified interpretive scope.

Direction is proposed resource differentiation among bacterial guilds toward coexistence. PARTIAL support preserves the diversity significance limits; broad GO:0044419 represents proposed interspecies context rather than proven facilitation.

### ecological_interactions[4]: Predicted Soil Carbon Cycling Consequences of Guild Succession

graph: supported. Targets: CommunityMech:000245.

The node is supported at its stated observational or qualified interpretive scope.

Direction is proposed guild expression toward polymer processing and soil-carbon fate. HYPOTHESIZED wording and broad carbohydrate/polysaccharide terms preserve the unmeasured flux, persistence and mineral-association endpoints.

### ecological_interactions[1].downstream[0]

graph: supported. Targets: CommunityMech:000245.

Expression-response groups to proposed guild coexistence is defensible as HYPOTHESIZED.

Source participants are bacterial response guilds; target is their proposed coexistence in paired root/detritus treatments. Reduced resource overlap is a plausible mediation, not a tested necessity. The evidence links retain exact source locators and short excerpts.

### ecological_interactions[2].downstream[0]

graph: supported. Targets: CommunityMech:000245.

Transcript upregulation to predicted soil-carbon consequences is defensible as HYPOTHESIZED.

Source is the bacterial aggregate carbohydrate-expression response; target is downstream polymer processing and soil-carbon fate. The proposed enzyme-mediated direction remains unmeasured; no numerical carbon flux, stabilization or persistence is certified.

### Origin, category, ecological state and habitat factors

scope: concern. Targets: CommunityMech:000245.

NATURAL/RHIZOSPHERE and host are supported; STABLE and the incomplete control description need correction.

### Empty growth_media and missing cultivation setup

completeness: concern. Targets: CommunityMech:000245.

Published Methods supplies concrete soil preparation, amendment and sampling context that is absent from structured cultivation fields.

Temperature, photoperiod and atmospheric settings were not reported in inspected cultivation text; do not import previous Avena trial values. Sample-processing temperatures are not growth conditions.

### Both related ingredients and metal/REE relevance

grounding: concern. Targets: CommunityMech:000245.

Polysaccharide class grounding is valid, but substrate necessity, universal maxima and whole-detritus molecular equivalence are not.

NOT_APPLICABLE metal relevance is consistent with the absence of a demonstrated metal-processing role; predicted mineral association in the Discussion does not establish one.

### Source input project and output-library inventory

completeness: concern. Targets: CommunityMech:000245.

The empty dataset list misses source-linked resources that can be represented with explicit input/output and access boundaries.

### Caches, snippets, previous decisions and current issues

provenance: supported. Targets: CommunityMech:000245.

Exact source snippets coexist with overbroad interpretations; the prior graph repair and open non-graph follow-up remain distinct.

### Native gates, source references and ontology labels

schema: supported. Targets: CommunityMech:000245.

Seven focused gates and cache preflight pass; six ontology pairs and thirteen snippets verify, with corpus network warning failures retained.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000245.

Completeness is 75 and capped quality is 100; the native score does not override the scientific needs-curation verdict.

## Findings

### ecological-overclaims: Non-graph guild and ingredient claims exceed the qualified source

major / open / confirmed; issue key: cm-000245-ecological-overclaims.

The description and taxonomy notes recast expression groups as four substrate specialists, while published Results includes Low Response without habitat preference. Ingredient prose conflates detritus response with Aging Root, claims universal combined-treatment maxima and requires plant polysaccharides as the central medium carbon source. These exceed the Results and the corrected graph; taxonomy evidence only describes binning.

### stable-state: STABLE does not represent the measured developing community

minor / open / confirmed; issue key: cm-000245-stable-state.

The study deliberately follows root-associated community assembly and functional succession; equilibrium is not established, and final-timepoint drying adds a changing environmental context.

### cultivation-controls: Cultivation context and unamended bulk controls are missing

minor / open / confirmed; issue key: cm-000245-cultivation-controls.

The habitat factor lists only three habitats and omits the unamended bulk baseline used for differential expression; growth_media is empty despite explicit native-soil and root-litter preparation details. The graph partly restores this context, so the defect is bounded but consequential for reproducing comparisons.

### detritus-grounding: Whole root detritus is not a single organic molecular entity

minor / open / confirmed; issue key: cm-000245-detritus-grounding.

CHEBI:50860 has the correct canonical label, but dried mixed root biomass is not equivalent to one molecular entity. The source establishes a heterogeneous amendment rather than a chemically resolved constituent.

### dataset-links: Source-linked reference and transcriptomic resources are not represented

minor / open / confirmed; issue key: cm-000245-dataset-links.

associated_datasets is empty although the main Methods and Table S1 identify reference-genome and output-library resources. The verified BioProject is one reference input; source-reported JGI library IDs require their own scope and access qualification.

## Recommended Actions And Acceptance Checks

### fix-ecological-overclaims

Align non-graph prose and claim-specific evidence with the published four response groups and transcriptional inference limits, through the existing follow-up 1296.

- Name Low Response and distinguish it from a combined-resource specialist.
- Do not make detritus and Aging Root groups equivalent or claim maximum expression at every harvest.
- Replace the universal medium requirement with measured amendment context; retain any proposed analog as an untested suggestion.
- Use CAZy Results for the expressed-potential role rather than the binning-method quote alone.
- Preserve all graph qualifications and run strict, term, reference and network checks.

### fix-stable-state

Use a source-supported developing/transient state or remove the unsupported equilibrium assertion.

- Apply the schema state to the study context rather than to stable soil carbon or another cited study.
- Retain NATURAL origin and the distinction between transcriptional and compositional change.
- Strict validation passes.

### fix-cultivation-controls

Represent the paired rhizosphere/bulk with/without-detritus design and source-backed native-soil cultivation details.

- Include unamended bulk soil as the comparator and retain three biological replicates/four destructive harvests.
- Capture pH 5.6, packing density 1.2 g/cm3 and preparation/amendment quantities with claim-level Methods evidence.
- Separate six-week pre-growth from 3/6/12/22-day root-age harvests.
- Do not invent growth temperature/light settings or treat processing buffers as media.
- Run strict and reference validation.

### fix-detritus-grounding

Represent root detritus as the source-described composite material or remove the unsupported exact CHEBI equivalence; retain supported constituent classes separately.

- Do not replace the broad term with an unverified single molecule.
- Preserve the actual aged-root amendment and material preparation.
- Validate any verified replacement identity and its canonical label.

### fix-dataset-links

Add evidence-backed resource links with explicit reference-input versus output-library roles and bounded verification.

- Do not describe PRJNA517182 as the complete metatranscriptome trial.
- Retain Table S1 identifiers as source-reported where archive access is unavailable.
- Keep 47 table-library rows distinct from 48 design samples; do not infer exclusion or reconcile data without evidence.
- Preserve source version and run strict/reference checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml; Entire target: one aggregate taxon, five nodes, two arrows, two factors and two related ingredients | supports | This is a natural soil-community study in planted microcosms, not a defined one-member culture. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=31953507&amp;retmode=xml; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=31953507&amp;retmode=xml | supports | Fresh PMID/DOI/PMCID and title metadata identifies Nuccio et al. 2020. |
| crossref | https://api.crossref.org/works/10.1038/s41396-019-0582-x; https://api.crossref.org/works/10.1038/s41396-019-0582-x | supports | Fresh DOI/title metadata agrees with the cited publication. |
| publisher | PMID:31953507; https://www.nature.com/articles/s41396-019-0582-x | supports | Fresh published main text, all Methods/Results/Discussion and Conclusions were assessed. |
| root-published-pdf | PMID:31953507; https://sydneyglassman.wordpress.com/wp-content/uploads/2020/02/nuccioetal_isme_2020.pdf | supports | Fresh author-hosted published PDF agrees with the publisher article; the earlier preprint was not substituted. |
| supplement-methods | PMID:31953507; https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41396-019-0582-x/MediaObjects/41396_2019_582_MOESM1_ESM.docx | supports | All supplementary Methods and figure captions were read; separate embedded figure images were not reanalyzed. |
| supplement-table-s1 | PMID:31953507; https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41396-019-0582-x/MediaObjects/41396_2019_582_MOESM2_ESM.xlsx | supports | The complete source table inventories sequencing libraries and repository IDs; design counts and deposited-library rows remain distinct. |
| xml-access | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7082339/fullTextXML; EPMC fullTextXML retrieval | supports | HTTP 500 is an access-path failure; fresh publisher HTML and published PDF supplied the main text. |
| timing | PMID:31953507; Results Sec17; Discussion Sec25; Fig. 1 | supports | Transcript profiles changed faster than composition; final-timepoint drying covaried with time. |
| guilds | PMID:31953507; Methods Sec9, Sec12-Sec14; Results Sec21-Sec23; Fig. 4 | supports | The 24 responsive aggregate populations form Rhizosphere, Detritusphere, Aging Root and Low Response groups; 80% mapping identity does not resolve strains. |
| expression | PMID:31953507; Results Sec19; Fig. 2c; Discussion Sec29 | supports | Combined treatment did not maximize upregulated-gene counts at day 22; transcript abundance is not enzyme flux or a universal medium requirement. |
| coexistence | PMID:31953507; Results Sec18; Fig. 2a-b; Discussion Sec28 | supports | The source interprets resource-dependent diversity as niche differentiation; statistical contrasts and observational design limit causal coexistence claims. |
| carbon | PMID:31953507; Discussion Sec29, final paragraph; Conclusions Sec30 | supports | Guild-dependent carbon persistence and mineral association are proposed consequences requiring further experiments. |
| conditions | PMID:31953507; Methods Sec3-Sec4; Results Sec16; supplementary Fig. S1 caption | supports | Native Hopland soil (pH 5.6; packing density 1.2 g/cm3) was used in paired rhizosphere/bulk compartments with and without aged root detritus. Harvests were at 3, 6, 12 and 22 days with three biological replicates; total design 48 samples. Root litter was dried, chopped to 1 mm and aged one year; 0.4 g was added to 50 g soil, while bulk bags used 0.016 g per 2 g soil. |
| potential | PMID:31953507; Methods Sec8-Sec12; Results Sec20-Sec23; Fig. 3-5 | supports | The selected decomposer aggregate has expressed CAZy potential. The binning-method snippet alone does not establish its role, and neither the whole reference database nor all Bacteria are demonstrated degraders. |
| schema | src/communitymech/schema/communitymech.yaml; EcologicalStateEnum; FunctionalRoleEnum; ingredient and cultivation slots | supports | STABLE denotes equilibrium; TRANSIENT permits a developing community. PRIMARY_DEGRADER concerns complex-substrate degradation, with evidence scope retained. |
| ontology | Local OAK NCBITaxon, ENVO, GO and CHEBI snapshots; Six unique ID/label pairs across eleven occurrences | supports | All labels match. Bacteria is an explicit aggregate anchor; polysaccharide is a defensible broad class. CHEBI:50860 denotes a molecular entity, not a whole mixed root-litter material. |
| snippets | kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml; All thirteen snippet occurrences against pinned abstracts, fresh PubMed and publisher text | supports | All snippets match both caches and PubMed; publisher matches include two typographic-dash differences. PDF extraction watermark and inline-spacing effects are documented, not unsupported-source findings. |
| history | history/records/Avena_Rhizosphere_Detritusphere_Niche_Succession; reports/causal_graph_review/decisions; One sidecar; batch5 deferral; batch12 target lines 26-148 | supports | The later graph review matches the current record hash and supersedes the earlier deferral only within graph scope. |
| issue-1295 | https://github.com/CultureBotAI/CommunityMech/issues/1295; Fresh public issue body and status | supports | Closed graph-repair issue; it does not certify non-graph metadata. |
| issue-1296 | https://github.com/CultureBotAI/CommunityMech/issues/1296; Fresh public issue body and status | supports | Open target-specific follow-up already identifies summary, habitat-control and ingredient overclaims; this review neither closes it nor creates a duplicate issue. |
| search | Owned-worktree kb/taxa, community/isolate records, caches and provenance; Ignored-inclusive exact identity/source lookup | supports | No reusable taxon for the encoded aggregate was found within the stated scope; the source/ID record lookup locates this target only. |
| datasets-source | PMID:31953507; Methods Sec7-Sec8; Supplementary Table S1 Sheet1 rows 3-49 | supports | PRJNA517182 supplies soil MAGs to the reference database. Table S1 provides 47 unique JGI library IDs; this inventory must not be equated with the 48-sample experimental design or with complete output-archive verification. |
| bioproject | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&amp;id=517182&amp;retmode=xml; PRJNA517182 public metadata | supports | The project cites PMID31953507 and identifies California soil metagenomes; its verified role is reference input, not the entire transcriptomic trial. |
| datasets | Public project metadata and source Table S1; dataset-verification.json | supports | Reference-project metadata verifies; output IDs remain source-reported where anonymous JGI access is denied. No library exclusion, sample reconciliation or raw-data analysis is inferred. |
| adapter | Optional kg-microbe-sources adapter; Explicit same-batch04-runtime discovery reuse | supports | No installed runtime runner/module was available; no expression-module coverage was queried and the external-checkout candidate was not executed. |
| native-target | NetworkIntegrityAuditor().audit_community(target); support-audit.json: diagnostic and native rubric | supports | The aggregate taxon is covered by community-level nodes; native COMPLETE does not certify individual guild membership. Seven node evidence items across five nodes give mean evidence 1.4. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml; Actual execution 2026-10-21T08:00:08.358284+00:00 to 2026-10-21T08:00:10.192203+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-strict kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml --out /private/tmp/cm-review-session/batch-04/000245/strict-report.tsv; Actual execution 2026-10-21T08:00:08.358581+00:00 to 2026-10-21T08:00:12.292545+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-terms kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml; Actual execution 2026-10-21T08:00:08.365362+00:00 to 2026-10-21T08:00:11.452952+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-gtdb kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml; Actual execution 2026-10-21T08:00:10.192654+00:00 to 2026-10-21T08:00:10.340500+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-gtdb-domain kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml; Actual execution 2026-10-21T08:00:10.340808+00:00 to 2026-10-21T08:00:12.585213+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-history history/records/Avena_Rhizosphere_Detritusphere_Niche_Succession; Actual execution 2026-10-21T08:00:11.453296+00:00 to 2026-10-21T08:00:12.466353+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T08:00:12.589990+00:00 to 2026-10-21T08:00:12.681606+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-references-explained kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml; Actual execution 2026-10-21T08:00:12.682023+00:00 to 2026-10-21T08:00:14.448090+00:00 | supports | Target native reference validation passed; scientific meaning was assessed separately. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T07:06:05.543108+00:00 to 2026-10-21T07:06:16.498440+00:00 | supports | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T07:06:16.498920+00:00 to 2026-10-21T07:06:23.361213+00:00 | supports | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| independent-source | PMID:31953507; root-source-audit.json: complete main text, Methods/captions and visual Figures 2-4 | supports | Independent source reading confirms the graph qualifications and the five bounded findings. |

## Limits And Additional Notes

- Fresh publisher HTML and the author-hosted published PDF were read after EPMC XML returned HTTP 500. The earlier preprint was not used. Both committed source caches contain abstracts only and remain unchanged.
- Root independently inspected main Figures 2-4; supplementary caption text was read but embedded figure images and other supplementary tables were not reanalyzed. All relevant main Methods were available.
- The main paper and Figure 4 identify 24 responsive populations; supplementary Figure S7 caption says 26 despite its A-X labeling. Preserve this source discrepancy without changing the source-backed main-paper count.
- The design describes 48 samples, while Table S1 lists 47 unique library IDs with its own harvest distribution. The source does not resolve that difference here; no excluded sample, error or raw-data reconciliation is inferred.
- PRJNA517182 verifies as a reference-genome input. Representative JGI routes return anonymous accessDenied pages, so output-library IDs remain source-reported and no complete archive coverage is certified.
- Expression, gyrase-based abundance proxies and transcriptional synergy do not directly measure substrate flux, cross-feeding, coexistence necessity or carbon persistence. Soil drying covaries with the final timepoint.
- Growth temperature, photoperiod and atmospheric settings were not recovered from the inspected cultivation Methods; earlier Avena experiments were not imported. Initial soil pH 5.6 is not a constant across amended treatments and harvests.
- Historical GTDB mapping counts were not recomputed. The optional structured adapter was unavailable in the task runtime; prior discovery was reused without executing an external-checkout runner.
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 20 words for Nuccio 2020, including its supplements.
- The initial malformed inspect target document was corrected before assessment; successful official inspect pins all used repository inputs.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T080502Z-avena-niche-succession-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Avena rhizosphere and detritusphere succession: whole-record review'
started_at: '2026-10-21T07:59:42.409517Z'
finished_at: '2026-10-21T08:05:02.581213Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Canonical target unchanged; prior codex graph curation prevents
    person-level independence claims. Separate agents assessed source text, ontology,
    native gates, snippets, history, resources and metrics.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: One major finding groups non-graph guild and ingredient overclaims already
  covered by open issue 1296. Four minor findings concern stability, cultivation/control
  completeness, composite-detritus grounding and omitted data links. All five graph
  nodes and both hypothesized arrows remain supported at their qualified scope. Seven
  focused gates and cache preflight pass; unrelated corpus network warning failures
  remain explicit.
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
  - path: history/records/Avena_Rhizosphere_Detritusphere_Niche_Succession/2026-10-05T201241Z-codex-e8b93d.yaml
    sha256: e353057d56e108b7d7a4f124f05b2577b0c67959a2b5a00d56a963470d17f74f
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    sha256: ea5631e37d2dbf65e26ed28a09fca23168c4c79e26160cbcb31ea93aa1e3e9e9
    role: target
  - path: references_cache/PMID_31953507.md
    sha256: b489a47668b357ed56d153fddcdea3cd6688b50f49590877f1571bf534e2376c
    role: context
  - path: references_cache/PMID_31953507.txt
    sha256: d25034db4953fdf847271e955a67baa77393d2a67e7f98b774eec944fdbe5cc1
    role: context
  - path: reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml
    sha256: 5076ec8295dacfaae0ae1d829836e4380a312a702c4a43df5f604c3b1b1e0ad3
    role: context
  - path: reports/causal_graph_review/decisions/20261005-two-records-batch12.yaml
    sha256: 7fd9cacc313e6f9db6e6836f0b4618db45ce8ac4fa58744bce36a4b7275d0a46
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
- target_id: CommunityMech:000245
  path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
  label: Avena Rhizosphere and Detritusphere Niche-Differentiated Decomposer Guilds
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
scope:
  description: Entire record, all thirteen evidence occurrences, fresh published main
    text, relevant supplementary Methods/captions and complete Table S1, publication
    metadata and bounded project/archive metadata. All five nodes and two directed
    arrows assessed; no sequence, transcript or ecological reanalysis.
  selection: Next uncovered maintained path after CommunityMech:000236 in batch04;
    one resolved natural-community record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000245
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000245
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
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
  - CommunityMech:000245
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-strict kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    --out /private/tmp/cm-review-session/batch-04/000245/strict-report.tsv
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
  - CommunityMech:000245
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-terms kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
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
  - CommunityMech:000245
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
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
  - CommunityMech:000245
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb-domain kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
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
  - CommunityMech:000245
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-history history/records/Avena_Rhizosphere_Detritusphere_Niche_Succession
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
  - CommunityMech:000245
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
  - CommunityMech:000245
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-references-explained kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
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
  - CommunityMech:000245
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
  - CommunityMech:000245
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
  name: Publication identity and full scientific source assessment
  status: passed
  required: true
  summary: Fresh published main text and relevant supplementary Methods were read
    with explicit inference limits.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - publisher
  - root-published-pdf
  - pubmed
  - crossref
  - supplement-methods
  - xml-access
- check_id: source-data
  name: Source data inventory and bounded metadata verification
  status: passed
  required: true
  summary: The input BioProject verifies; source-reported JGI IDs and anonymous-access
    limitations remain explicit.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - datasets
  - bioproject
  - supplement-table-s1
- check_id: cross-mech
  name: Encoded medium and ingredient-Mech linkages
  status: not_applicable
  required: false
  summary: The record encodes no CultureMech or MediaIngredientMech links to verify.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - conditions
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Same-runtime discovery was reused; no expression-module coverage was queried.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
  locator: 'Entire target: one aggregate taxon, five nodes, two arrows, two factors
    and two related ingredients'
  summary: This is a natural soil-community study in planted microcosms, not a defined
    one-member culture.
  support: supports
  accessed_at: '2026-10-21T08:05:02.570143Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=31953507&retmode=xml
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=31953507&retmode=xml
  summary: Fresh PMID/DOI/PMCID and title metadata identifies Nuccio et al. 2020.
  support: supports
  accessed_at: '2026-10-21T07:59:49.546794Z'
  snapshot_sha256: 75a14231e9d9871a5b64257ae5d8083bf580120eba3a1a092aaf5090261aab1f
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1038/s41396-019-0582-x
  locator: https://api.crossref.org/works/10.1038/s41396-019-0582-x
  summary: Fresh DOI/title metadata agrees with the cited publication.
  support: supports
  accessed_at: '2026-10-21T07:59:49.550193Z'
  snapshot_sha256: 5ab73be3212f0480ca6d2eab14bf1709dd6f536fcfce5d8e5af11b4b4e37bb3b
- evidence_id: publisher
  kind: primary_source
  reference: PMID:31953507
  locator: https://www.nature.com/articles/s41396-019-0582-x
  summary: Fresh published main text, all Methods/Results/Discussion and Conclusions
    were assessed.
  support: supports
  accessed_at: '2026-10-21T08:00:46.514710Z'
  snapshot_sha256: 46d4ac69fc99274a6ef80da7ebc82320b710eb575288234d0087eb6ba2cc1f39
- evidence_id: root-published-pdf
  kind: primary_source
  reference: PMID:31953507
  locator: https://sydneyglassman.wordpress.com/wp-content/uploads/2020/02/nuccioetal_isme_2020.pdf
  summary: Fresh author-hosted published PDF agrees with the publisher article; the
    earlier preprint was not substituted.
  support: supports
  accessed_at: '2026-10-21T07:59:42.611923Z'
  snapshot_sha256: 8316bde2ce9eafd97f971c846d430f155b6e59394477803769fe49fe2a1b820f
- evidence_id: supplement-methods
  kind: primary_source
  reference: PMID:31953507
  locator: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41396-019-0582-x/MediaObjects/41396_2019_582_MOESM1_ESM.docx
  summary: All supplementary Methods and figure captions were read; separate embedded
    figure images were not reanalyzed.
  support: supports
  accessed_at: '2026-10-21T08:02:16.237132Z'
  snapshot_sha256: 36463c09d55f7a3898c7e9f910e73a904d0811222d14b77487def35a5d4b1158
- evidence_id: supplement-table-s1
  kind: primary_source
  reference: PMID:31953507
  locator: https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41396-019-0582-x/MediaObjects/41396_2019_582_MOESM2_ESM.xlsx
  summary: The complete source table inventories sequencing libraries and repository
    IDs; design counts and deposited-library rows remain distinct.
  support: supports
  accessed_at: '2026-10-21T08:01:20.234050Z'
  snapshot_sha256: 196f4ff7805c955c65f1ab62933e296fd4a291ee8b94721898981048c1ce5a2d
- evidence_id: xml-access
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7082339/fullTextXML
  locator: EPMC fullTextXML retrieval
  summary: HTTP 500 is an access-path failure; fresh publisher HTML and published
    PDF supplied the main text.
  support: supports
  accessed_at: '2026-10-21T07:59:50.212526Z'
  snapshot_sha256: c59cf6d45199214bf58238f6f9c30c8f1a816351bbec663d508b9985ff669c5c
- evidence_id: timing
  kind: primary_source
  reference: PMID:31953507
  locator: Results Sec17; Discussion Sec25; Fig. 1
  summary: Transcript profiles changed faster than composition; final-timepoint drying
    covaried with time.
  support: supports
  accessed_at: '2026-10-21T08:05:02.572452Z'
  quote: functional composition distinctly shifted
- evidence_id: guilds
  kind: primary_source
  reference: PMID:31953507
  locator: Methods Sec9, Sec12-Sec14; Results Sec21-Sec23; Fig. 4
  summary: The 24 responsive aggregate populations form Rhizosphere, Detritusphere,
    Aging Root and Low Response groups; 80% mapping identity does not resolve strains.
  support: supports
  accessed_at: '2026-10-21T08:05:02.572456Z'
  quote: no discernable habitat preference
- evidence_id: expression
  kind: primary_source
  reference: PMID:31953507
  locator: Results Sec19; Fig. 2c; Discussion Sec29
  summary: Combined treatment did not maximize upregulated-gene counts at day 22;
    transcript abundance is not enzyme flux or a universal medium requirement.
  support: supports
  accessed_at: '2026-10-21T08:05:02.572458Z'
  quote: exception of the final timepoint
- evidence_id: coexistence
  kind: primary_source
  reference: PMID:31953507
  locator: Results Sec18; Fig. 2a-b; Discussion Sec28
  summary: The source interprets resource-dependent diversity as niche differentiation;
    statistical contrasts and observational design limit causal coexistence claims.
  support: supports
  accessed_at: '2026-10-21T08:05:02.572459Z'
  quote: spatial and temporal niche differentiation
- evidence_id: carbon
  kind: primary_source
  reference: PMID:31953507
  locator: Discussion Sec29, final paragraph; Conclusions Sec30
  summary: Guild-dependent carbon persistence and mineral association are proposed
    consequences requiring further experiments.
  support: supports
  accessed_at: '2026-10-21T08:05:02.572461Z'
  quote: Experimental tests
- evidence_id: conditions
  kind: primary_source
  reference: PMID:31953507
  locator: Methods Sec3-Sec4; Results Sec16; supplementary Fig. S1 caption
  summary: Native Hopland soil (pH 5.6; packing density 1.2 g/cm3) was used in paired
    rhizosphere/bulk compartments with and without aged root detritus. Harvests were
    at 3, 6, 12 and 22 days with three biological replicates; total design 48 samples.
    Root litter was dried, chopped to 1 mm and aged one year; 0.4 g was added to 50
    g soil, while bulk bags used 0.016 g per 2 g soil.
  support: supports
  accessed_at: '2026-10-21T08:05:02.572462Z'
- evidence_id: potential
  kind: primary_source
  reference: PMID:31953507
  locator: Methods Sec8-Sec12; Results Sec20-Sec23; Fig. 3-5
  summary: The selected decomposer aggregate has expressed CAZy potential. The binning-method
    snippet alone does not establish its role, and neither the whole reference database
    nor all Bacteria are demonstrated degraders.
  support: supports
  accessed_at: '2026-10-21T08:05:02.572464Z'
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: EcologicalStateEnum; FunctionalRoleEnum; ingredient and cultivation slots
  summary: STABLE denotes equilibrium; TRANSIENT permits a developing community. PRIMARY_DEGRADER
    concerns complex-substrate degradation, with evidence scope retained.
  support: supports
  accessed_at: '2026-10-21T08:05:02.572466Z'
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, GO and CHEBI snapshots
  locator: Six unique ID/label pairs across eleven occurrences
  summary: All labels match. Bacteria is an explicit aggregate anchor; polysaccharide
    is a defensible broad class. CHEBI:50860 denotes a molecular entity, not a whole
    mixed root-litter material.
  support: supports
  accessed_at: '2026-10-21T08:05:02.572723Z'
  snapshot_sha256: 81ed6ccfcd1ffed8e2f449b70060f5edde5f68a8f115d92cb00a7d7f913562dc
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
  locator: All thirteen snippet occurrences against pinned abstracts, fresh PubMed
    and publisher text
  summary: All snippets match both caches and PubMed; publisher matches include two
    typographic-dash differences. PDF extraction watermark and inline-spacing effects
    are documented, not unsupported-source findings.
  support: supports
  accessed_at: '2026-10-21T08:05:02.572960Z'
  snapshot_sha256: d6212413f830c7d36c5216b4b93c8af1990572f113179df108e907571c6693ea
- evidence_id: history
  kind: record_content
  reference: history/records/Avena_Rhizosphere_Detritusphere_Niche_Succession; reports/causal_graph_review/decisions
  locator: One sidecar; batch5 deferral; batch12 target lines 26-148
  summary: The later graph review matches the current record hash and supersedes the
    earlier deferral only within graph scope.
  support: supports
  accessed_at: '2026-10-21T08:05:02.573122Z'
  snapshot_sha256: 37932cf338570eb24b9b0c644024ed80a6d9cd6053f1d2ebc7f90709a26de9ec
- evidence_id: issue-1295
  kind: database
  reference: https://github.com/CultureBotAI/CommunityMech/issues/1295
  locator: Fresh public issue body and status
  summary: Closed graph-repair issue; it does not certify non-graph metadata.
  support: supports
  accessed_at: '2026-10-21T07:58:05.590455Z'
  snapshot_sha256: effc384dc55fa94f26416811552d5eb399a5c6d60ccf39161a6bc68112f453a5
- evidence_id: issue-1296
  kind: database
  reference: https://github.com/CultureBotAI/CommunityMech/issues/1296
  locator: Fresh public issue body and status
  summary: Open target-specific follow-up already identifies summary, habitat-control
    and ingredient overclaims; this review neither closes it nor creates a duplicate
    issue.
  support: supports
  accessed_at: '2026-10-21T07:58:23.726872Z'
  snapshot_sha256: 359f102a7bf892aab8da2294fe74ed903afde51b85cd997391bd6a1a2e687821
- evidence_id: search
  kind: search
  reference: Owned-worktree kb/taxa, community/isolate records, caches and provenance
  locator: Ignored-inclusive exact identity/source lookup
  summary: No reusable taxon for the encoded aggregate was found within the stated
    scope; the source/ID record lookup locates this target only.
  support: supports
  accessed_at: '2026-10-21T08:05:02.574268Z'
  snapshot_sha256: 4f303cc565bdfa0295d93718638396a8ce6d70f0c0ef220ddc92b5fa418cccbe
  search_scope: rg --no-ignore --hidden over the listed directories, exact source
    IDs/slug and NCBITaxon:2 aggregate; not global synonym coverage.
- evidence_id: datasets-source
  kind: primary_source
  reference: PMID:31953507
  locator: Methods Sec7-Sec8; Supplementary Table S1 Sheet1 rows 3-49
  summary: PRJNA517182 supplies soil MAGs to the reference database. Table S1 provides
    47 unique JGI library IDs; this inventory must not be equated with the 48-sample
    experimental design or with complete output-archive verification.
  support: supports
  accessed_at: '2026-10-21T08:05:02.574275Z'
- evidence_id: bioproject
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=517182&retmode=xml
  locator: PRJNA517182 public metadata
  summary: The project cites PMID31953507 and identifies California soil metagenomes;
    its verified role is reference input, not the entire transcriptomic trial.
  support: supports
  accessed_at: '2026-10-21T08:01:06.993407Z'
  snapshot_sha256: c464515916c283a1f7e4da0906a230993916a141b82a627b82053fece69c744e
- evidence_id: datasets
  kind: validation
  reference: Public project metadata and source Table S1
  locator: dataset-verification.json
  summary: Reference-project metadata verifies; output IDs remain source-reported
    where anonymous JGI access is denied. No library exclusion, sample reconciliation
    or raw-data analysis is inferred.
  support: supports
  accessed_at: '2026-10-21T08:05:02.574712Z'
  snapshot_sha256: 6790d175a7794616785cb56e60ca885c32d14ad0b68eb55029e5252f8936f02a
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources adapter
  locator: Explicit same-batch04-runtime discovery reuse
  summary: No installed runtime runner/module was available; no expression-module
    coverage was queried and the external-checkout candidate was not executed.
  support: supports
  accessed_at: '2026-10-21T08:05:02.574887Z'
  snapshot_sha256: b58eb7d867349c1cb249c614666f4ef2f00c65215c15f0769727c35ed05fd59c
  search_scope: Previously recorded batch04 PATH/virtualenv/module and ignored-inclusive
    bounded discovery, explicitly reused.
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: 'support-audit.json: diagnostic and native rubric'
  summary: The aggregate taxon is covered by community-level nodes; native COMPLETE
    does not certify individual guild membership. Seven node evidence items across
    five nodes give mean evidence 1.4.
  support: supports
  accessed_at: '2026-10-21T08:05:02.575001Z'
  snapshot_sha256: 80d419725a25172831316535dfe5e51d76d82038c37fa5c2cff5321435374ccc
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
  locator: Actual execution 2026-10-21T08:00:08.358284+00:00 to 2026-10-21T08:00:10.192203+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T08:00:10.192203Z'
  snapshot_sha256: 5f2bb4bdb2cb1d35d35a21be39163cb2d677a318dc5fd6c5328d0fa41e4478a1
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-strict kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    --out /private/tmp/cm-review-session/batch-04/000245/strict-report.tsv
  locator: Actual execution 2026-10-21T08:00:08.358581+00:00 to 2026-10-21T08:00:12.292545+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T08:00:12.292545Z'
  snapshot_sha256: d376216b3a64548c1ab6c76f8bc07f6258b1b896f5f5385e0fd2e87a95d747d5
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-terms kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
  locator: Actual execution 2026-10-21T08:00:08.365362+00:00 to 2026-10-21T08:00:11.452952+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T08:00:11.452952Z'
  snapshot_sha256: 70d5c359e6dd81923491e0e54889f5d5c7d501722fdbf12f9313a9d804d73b82
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
  locator: Actual execution 2026-10-21T08:00:10.192654+00:00 to 2026-10-21T08:00:10.340500+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T08:00:10.340500Z'
  snapshot_sha256: ea7b3665f1e3326782e95cc734f28404102c5e090379a2af677b0164dd09c0bd
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb-domain kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
  locator: Actual execution 2026-10-21T08:00:10.340808+00:00 to 2026-10-21T08:00:12.585213+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T08:00:12.585213Z'
  snapshot_sha256: 9d196444f9abcf6d83dde206667509e508b2c37f86ce62f9038c2dacbf244daf
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-history history/records/Avena_Rhizosphere_Detritusphere_Niche_Succession
  locator: Actual execution 2026-10-21T08:00:11.453296+00:00 to 2026-10-21T08:00:12.466353+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T08:00:12.466353Z'
  snapshot_sha256: dcee5af194b630270f8760db74d05d6691f6b443498467dd50f9e1dae2e0adfa
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T08:00:12.589990+00:00 to 2026-10-21T08:00:12.681606+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T08:00:12.681606Z'
  snapshot_sha256: 1eb0d0eef4593f229274d26bd0a9d0d0f31e31c8d501743a566d737cf24d0560
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-references-explained kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
  locator: Actual execution 2026-10-21T08:00:12.682023+00:00 to 2026-10-21T08:00:14.448090+00:00
  summary: Target native reference validation passed; scientific meaning was assessed
    separately.
  support: supports
  accessed_at: '2026-10-21T08:00:14.448090Z'
  snapshot_sha256: 55425764c0a53e4f03ec5c04fffd1387ceedee1c71ae6ecbb922aead1d930071
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
- evidence_id: independent-source
  kind: validation
  reference: PMID:31953507
  locator: 'root-source-audit.json: complete main text, Methods/captions and visual
    Figures 2-4'
  summary: Independent source reading confirms the graph qualifications and the five
    bounded findings.
  support: supports
  accessed_at: '2026-10-21T08:05:02.581174Z'
  snapshot_sha256: 7b603e80c2cce211efc2be6d34d2076540f7cbb79952a24e1da0c0ec454be8ad
assessments:
- assessment_id: identity
  area: identity
  topic: Community, source populations and experimental context
  outcome: supported
  summary: The record resolves to the Nuccio Avena soil study and explicitly represents
    an aggregate decomposer community.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - conditions
  - guilds
  - potential
  - ontology
  dimensions:
  - name: community_scope
    value: Natural rhizosphere/detritusphere community in a planted-soil experiment
    definition: One taxonomic aggregate represents functional guilds, not one species
      or a defined consortium.
    evidence_ids:
    - record
    - potential
  - name: source_strain
    value: Aggregated population transcriptomes matched to reference genomes
    definition: Twenty-four responsive populations are selected from 282 references;
      80% identity mapping may pool genus/family relatives and does not authenticate
      strains.
    evidence_ids:
    - guilds
    - potential
  - name: environment
    value: Hopland grassland soil with living Avena fatua roots and root-litter treatments
    definition: Rhizosphere grounding is valid focal habitat; paired bulk controls
      remain part of the design.
    evidence_ids:
    - conditions
    - ontology
  - name: medium
    value: Native Bearwallow-Hellman loam, with defined litter amendment contrasts
    definition: Main Methods supplies soil and preparation details; no standard isolate
      medium is established.
    evidence_ids:
    - conditions
  - name: experimental_setting
    value: Paired 2-by-2 compartment/amendment design over four harvests
    definition: Three biological replicates per contrast; final-timepoint moisture
      covaries with succession.
    evidence_ids:
    - conditions
    - timing
  - name: evidence_tier
    value: Expression profiles, community composition and inferred ecological consequences
    definition: In-vivo microcosm observations support transcriptional response; direct
      polymer flux, partner facilitation and coexistence necessity were not measured.
    evidence_ids:
    - guilds
    - expression
    - coexistence
    - carbon
  - name: grounding_status
    value: Six canonical labels with a composite-material mismatch
    definition: GTDB syntax/domain checks do not recompute historical aggregate mapping
      counts.
    evidence_ids:
    - ontology
- assessment_id: taxonomy
  area: grounding
  topic: Aggregate Bacteria and PRIMARY_DEGRADER
  outcome: concern
  summary: The functional aggregate is defensible as expressed degradation potential,
    but its notes and binning-only evidence overstate substrate specialization.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - potential
  - guilds
  - schema
  - ontology
  details: Retain the explicit aggregate rather than inventing species or treating
    282 reference genomes as a verified consortium. If greater granularity is curated,
    Fig. 4 supplies reference-population labels with mapping limits.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Functional Succession Outpaces Compositional
    Change'
  outcome: supported
  summary: The node is supported at its stated observational or qualified interpretive
    scope.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - timing
  - ontology
  details: Community-wide transcript and 16S composition changes in paired compartments;
    temporal comparison, not organism-to-organism flux. GO carbohydrate metabolism
    identifies the measured functional context, not a reaction-rate assay.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Four Decomposition-Gene Expression Response
    Groups'
  outcome: supported
  summary: The node is supported at its stated observational or qualified interpretive
    scope.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - guilds
  - ontology
  details: The bacterial aggregate contains 24 responsive reference populations. Habitat/time
    contrasts yield expression groups; PARTIAL NICHE_PARTITIONING and polysaccharide
    context do not establish four obligate specialists or exchange among them.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Rhizosphere Upregulates Carbohydrate Depolymerization
    Transcripts'
  outcome: supported
  summary: The node is supported at its stated observational or qualified interpretive
    scope.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - expression
  - ontology
  details: Living-root treatment is the exposure and the bacterial aggregate transcript
    response is the endpoint. The node correctly separates expression from enzyme
    activity, with final-timepoint treatment ranking qualified.
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Proposed Niche-Differentiated Guild Coexistence'
  outcome: supported
  summary: The node is supported at its stated observational or qualified interpretive
    scope.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - coexistence
  - ontology
  details: Direction is proposed resource differentiation among bacterial guilds toward
    coexistence. PARTIAL support preserves the diversity significance limits; broad
    GO:0044419 represents proposed interspecies context rather than proven facilitation.
- assessment_id: node-4
  area: graph
  topic: 'ecological_interactions[4]: Predicted Soil Carbon Cycling Consequences of
    Guild Succession'
  outcome: supported
  summary: The node is supported at its stated observational or qualified interpretive
    scope.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - carbon
  - ontology
  details: Direction is proposed guild expression toward polymer processing and soil-carbon
    fate. HYPOTHESIZED wording and broad carbohydrate/polysaccharide terms preserve
    the unmeasured flux, persistence and mineral-association endpoints.
- assessment_id: arrow-1
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: supported
  summary: Expression-response groups to proposed guild coexistence is defensible
    as HYPOTHESIZED.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - guilds
  - coexistence
  details: Source participants are bacterial response guilds; target is their proposed
    coexistence in paired root/detritus treatments. Reduced resource overlap is a
    plausible mediation, not a tested necessity. The evidence links retain exact source
    locators and short excerpts.
- assessment_id: arrow-2
  area: graph
  topic: ecological_interactions[2].downstream[0]
  outcome: supported
  summary: Transcript upregulation to predicted soil-carbon consequences is defensible
    as HYPOTHESIZED.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - expression
  - carbon
  details: Source is the bacterial aggregate carbohydrate-expression response; target
    is downstream polymer processing and soil-carbon fate. The proposed enzyme-mediated
    direction remains unmeasured; no numerical carbon flux, stabilization or persistence
    is certified.
- assessment_id: environment
  area: scope
  topic: Origin, category, ecological state and habitat factors
  outcome: concern
  summary: NATURAL/RHIZOSPHERE and host are supported; STABLE and the incomplete control
    description need correction.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - conditions
  - timing
  - schema
- assessment_id: cultivation
  area: completeness
  topic: Empty growth_media and missing cultivation setup
  outcome: concern
  summary: Published Methods supplies concrete soil preparation, amendment and sampling
    context that is absent from structured cultivation fields.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - conditions
  - supplement-methods
  details: Temperature, photoperiod and atmospheric settings were not reported in
    inspected cultivation text; do not import previous Avena trial values. Sample-processing
    temperatures are not growth conditions.
- assessment_id: ingredients
  area: grounding
  topic: Both related ingredients and metal/REE relevance
  outcome: concern
  summary: Polysaccharide class grounding is valid, but substrate necessity, universal
    maxima and whole-detritus molecular equivalence are not.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - expression
  - guilds
  - ontology
  - conditions
  details: NOT_APPLICABLE metal relevance is consistent with the absence of a demonstrated
    metal-processing role; predicted mineral association in the Discussion does not
    establish one.
- assessment_id: datasets
  area: completeness
  topic: Source input project and output-library inventory
  outcome: concern
  summary: The empty dataset list misses source-linked resources that can be represented
    with explicit input/output and access boundaries.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - datasets-source
  - bioproject
  - datasets
- assessment_id: provenance
  area: provenance
  topic: Caches, snippets, previous decisions and current issues
  outcome: supported
  summary: Exact source snippets coexist with overbroad interpretations; the prior
    graph repair and open non-graph follow-up remain distinct.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - snippets
  - history
  - issue-1295
  - issue-1296
  - search
- assessment_id: validation
  area: schema
  topic: Native gates, source references and ontology labels
  outcome: supported
  summary: Seven focused gates and cache preflight pass; six ontology pairs and thirteen
    snippets verify, with corpus network warning failures retained.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - ontology
  - snippets
  - check-validate
  - check-validate-strict
  - check-audit-network
  - native-target
  - independent-source
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality
  outcome: supported
  summary: Completeness is 75 and capped quality is 100; the native score does not
    override the scientific needs-curation verdict.
  target_ids:
  - CommunityMech:000245
  evidence_ids:
  - record
  - native-target
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including all taxon roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). 50 + 5 + 0 + 10 + 5 + 0 + 0 + 5 = 75.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1=0, P2=1, P3=4, P4=0; 7 items / 5 nodes
      = 1.4; native COMPLETE. 100 - 10 - 8 + 14 + 15 = 111 before capping; this is
      not a scientific pass.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P2
    value: 1
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P3
    value: 4
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
findings:
- finding_id: ecological-overclaims
  issue_key: cm-000245-ecological-overclaims
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: the non-graph interpretation materially overstates
    substrate specificity and cultivation requirements.'
  rule_id: review-checklist.claim_support
  status: open
  certainty: confirmed
  title: Non-graph guild and ingredient claims exceed the qualified source
  description: The description and taxonomy notes recast expression groups as four
    substrate specialists, while published Results includes Low Response without habitat
    preference. Ingredient prose conflates detritus response with Aging Root, claims
    universal combined-treatment maxima and requires plant polysaccharides as the
    central medium carbon source. These exceed the Results and the corrected graph;
    taxonomy evidence only describes binning.
  target_ids:
  - CommunityMech:000245
  field_paths:
  - description
  - taxonomy[0].taxon_term.notes
  - taxonomy[0].evidence
  - related_ingredients[0].relevance
  - related_ingredients[0].evidence[0].explanation
  - related_ingredients[1].relevance
  - related_ingredients[1].evidence[0].explanation
  evidence_ids:
  - guilds
  - expression
  - potential
  - conditions
  - issue-1296
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
- finding_id: stable-state
  issue_key: cm-000245-stable-state
  category: scope
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded state, context, chemical specificity or
    resource completeness issue; record identity and qualified graph remain intact.'
  rule_id: review-checklist.ecological_state
  status: open
  certainty: confirmed
  title: STABLE does not represent the measured developing community
  description: The study deliberately follows root-associated community assembly and
    functional succession; equilibrium is not established, and final-timepoint drying
    adds a changing environmental context.
  target_ids:
  - CommunityMech:000245
  field_paths:
  - ecological_state
  evidence_ids:
  - timing
  - guilds
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
- finding_id: cultivation-controls
  issue_key: cm-000245-cultivation-controls
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded state, context, chemical specificity or
    resource completeness issue; record identity and qualified graph remain intact.'
  rule_id: review-checklist.cultivation
  status: open
  certainty: confirmed
  title: Cultivation context and unamended bulk controls are missing
  description: The habitat factor lists only three habitats and omits the unamended
    bulk baseline used for differential expression; growth_media is empty despite
    explicit native-soil and root-litter preparation details. The graph partly restores
    this context, so the defect is bounded but consequential for reproducing comparisons.
  target_ids:
  - CommunityMech:000245
  field_paths:
  - environmental_factors[0]
  - environment_term.notes
  - growth_media
  - cultivation_setup
  evidence_ids:
  - conditions
  - guilds
  - issue-1296
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
- finding_id: detritus-grounding
  issue_key: cm-000245-detritus-grounding
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded state, context, chemical specificity or
    resource completeness issue; record identity and qualified graph remain intact.'
  rule_id: review-checklist.ingredient_identity
  status: open
  certainty: confirmed
  title: Whole root detritus is not a single organic molecular entity
  description: CHEBI:50860 has the correct canonical label, but dried mixed root biomass
    is not equivalent to one molecular entity. The source establishes a heterogeneous
    amendment rather than a chemically resolved constituent.
  target_ids:
  - CommunityMech:000245
  field_paths:
  - related_ingredients[1].chebi_term
  evidence_ids:
  - ontology
  - conditions
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
- finding_id: dataset-links
  issue_key: cm-000245-dataset-links
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded state, context, chemical specificity or
    resource completeness issue; record identity and qualified graph remain intact.'
  rule_id: review-checklist.datasets
  status: open
  certainty: confirmed
  title: Source-linked reference and transcriptomic resources are not represented
  description: associated_datasets is empty although the main Methods and Table S1
    identify reference-genome and output-library resources. The verified BioProject
    is one reference input; source-reported JGI library IDs require their own scope
    and access qualification.
  target_ids:
  - CommunityMech:000245
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - datasets-source
  - bioproject
  - datasets
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
actions:
- action_id: fix-ecological-overclaims
  description: Align non-graph prose and claim-specific evidence with the published
    four response groups and transcriptional inference limits, through the existing
    follow-up 1296.
  finding_ids:
  - ecological-overclaims
  target_ids:
  - CommunityMech:000245
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
  acceptance_checks:
  - Name Low Response and distinguish it from a combined-resource specialist.
  - Do not make detritus and Aging Root groups equivalent or claim maximum expression
    at every harvest.
  - Replace the universal medium requirement with measured amendment context; retain
    any proposed analog as an untested suggestion.
  - Use CAZy Results for the expressed-potential role rather than the binning-method
    quote alone.
  - Preserve all graph qualifications and run strict, term, reference and network
    checks.
- action_id: fix-stable-state
  description: Use a source-supported developing/transient state or remove the unsupported
    equilibrium assertion.
  finding_ids:
  - stable-state
  target_ids:
  - CommunityMech:000245
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
  acceptance_checks:
  - Apply the schema state to the study context rather than to stable soil carbon
    or another cited study.
  - Retain NATURAL origin and the distinction between transcriptional and compositional
    change.
  - Strict validation passes.
- action_id: fix-cultivation-controls
  description: Represent the paired rhizosphere/bulk with/without-detritus design
    and source-backed native-soil cultivation details.
  finding_ids:
  - cultivation-controls
  target_ids:
  - CommunityMech:000245
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
  acceptance_checks:
  - Include unamended bulk soil as the comparator and retain three biological replicates/four
    destructive harvests.
  - Capture pH 5.6, packing density 1.2 g/cm3 and preparation/amendment quantities
    with claim-level Methods evidence.
  - Separate six-week pre-growth from 3/6/12/22-day root-age harvests.
  - Do not invent growth temperature/light settings or treat processing buffers as
    media.
  - Run strict and reference validation.
- action_id: fix-detritus-grounding
  description: Represent root detritus as the source-described composite material
    or remove the unsupported exact CHEBI equivalence; retain supported constituent
    classes separately.
  finding_ids:
  - detritus-grounding
  target_ids:
  - CommunityMech:000245
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
  acceptance_checks:
  - Do not replace the broad term with an unverified single molecule.
  - Preserve the actual aged-root amendment and material preparation.
  - Validate any verified replacement identity and its canonical label.
- action_id: fix-dataset-links
  description: Add evidence-backed resource links with explicit reference-input versus
    output-library roles and bounded verification.
  finding_ids:
  - dataset-links
  target_ids:
  - CommunityMech:000245
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Avena_Rhizosphere_Detritusphere_Niche_Succession.yaml
    role: canonical_record
  acceptance_checks:
  - Do not describe PRJNA517182 as the complete metatranscriptome trial.
  - Retain Table S1 identifiers as source-reported where archive access is unavailable.
  - Keep 47 table-library rows distinct from 48 design samples; do not infer exclusion
    or reconcile data without evidence.
  - Preserve source version and run strict/reference checks.
limitations:
- Fresh publisher HTML and the author-hosted published PDF were read after EPMC XML
  returned HTTP 500. The earlier preprint was not used. Both committed source caches
  contain abstracts only and remain unchanged.
- Root independently inspected main Figures 2-4; supplementary caption text was read
  but embedded figure images and other supplementary tables were not reanalyzed. All
  relevant main Methods were available.
- The main paper and Figure 4 identify 24 responsive populations; supplementary Figure
  S7 caption says 26 despite its A-X labeling. Preserve this source discrepancy without
  changing the source-backed main-paper count.
- The design describes 48 samples, while Table S1 lists 47 unique library IDs with
  its own harvest distribution. The source does not resolve that difference here;
  no excluded sample, error or raw-data reconciliation is inferred.
- PRJNA517182 verifies as a reference-genome input. Representative JGI routes return
  anonymous accessDenied pages, so output-library IDs remain source-reported and no
  complete archive coverage is certified.
- Expression, gyrase-based abundance proxies and transcriptional synergy do not directly
  measure substrate flux, cross-feeding, coexistence necessity or carbon persistence.
  Soil drying covaries with the final timepoint.
- Growth temperature, photoperiod and atmospheric settings were not recovered from
  the inspected cultivation Methods; earlier Avena experiments were not imported.
  Initial soil pH 5.6 is not a constant across amended treatments and harvests.
- Historical GTDB mapping counts were not recomputed. The optional structured adapter
  was unavailable in the task runtime; prior discovery was reused without executing
  an external-checkout runner.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 20 words for Nuccio 2020, including its supplements.
- The initial malformed inspect target document was corrected before assessment; successful
  official inspect pins all used repository inputs.
tags:
- record-review
- rhizosphere
- detritusphere
- metatranscriptomics
- batch-04
```
