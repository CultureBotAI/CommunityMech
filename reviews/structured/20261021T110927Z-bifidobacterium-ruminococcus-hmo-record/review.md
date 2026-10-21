# Bifidobacterium–Ruminococcus infant HMO cross-feeding: record review

- Review: 20261021T110927Z-bifidobacterium-ruminococcus-hmo-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T11:01:48.875171Z
- Finished UTC: 2026-10-21T11:09:27.203850Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Complete source review supports all six qualified nodes and four PARTIAL arrows. One major finding concerns non-graph mechanism and substrate-necessity overstatement; three minor findings concern assay/environment context, lactose specificity and omitted source-linked datasets. Preserve the 144 h Methods versus 168 h Figure 4/source-data discrepancy.

## Scope And Provenance

Whole record, six nodes and four arrows assessed against complete scientific main, all main/SI figures and tables, two small gene workbooks, bounded Figure 4 source data and public archive metadata.

Selection: Next assigned maintained path after 000401 was saved and both mandatory post-save checks passed; only CommunityMech:000220 reviewed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000220 | kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml | maintained | Bifidobacterium-Ruminococcus Infant HMO Cross-Feeding Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000220 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000220 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000220 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000220 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000220 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000220 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000220 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000220 | Target reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000220 | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |
| check-network-quality | failed | True | CommunityMech:000220 | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |
| Primary publication and archive identity | passed | True | CommunityMech:000220 | Direct metadata, complete primary text and the reported archive identities were verified. |
| Full primary scientific assessment | passed | True | CommunityMech:000220 | Whole main, all main/SI figures and tables, two gene workbooks and bounded Figure 4 source data were inspected. |
| Encoded medium/ingredient-Mech links | not_applicable | False | CommunityMech:000220 | No CultureMech or MediaIngredientMech identifier is encoded; no exact recipe equivalence was inferred. |
| Optional structured source adapter | unavailable | False | CommunityMech:000220 | No runnable adapter was available in the owned runtime. |

## Scientific And Domain Assessments

### Experimental umbrella and exact source context

identity: concern. Targets: CommunityMech:000220.

The selected pair and wider infant-derived experiments are identifiable, but culture and source-material contexts need clearer separation.

### Both focal taxa, abundance and functional roles

grounding: supported. Targets: CommunityMech:000220.

Retain source-resolved species and the qualified donor/recipient interpretation, with claim-level evidence for roles.

B. breve CROSS_FEEDER is the author-inferred recipient role; R. gnavus PRIMARY_DEGRADER is supported by substrate growth and predicted 2′FL-cleaving capacity. Do not restate predicted extracellular activity as directly measured. Both ABUNDANT labels are contextual across the experimental umbrella; the approximately 80% B. breve result belongs to the 2′FL pair. No fixed dominance threshold, universal abundance or new strain accession is inferred. Existing GTDB syntax/status passes without independently re-certifying historical release counts.

### ecological_interactions[0]: B. breve 2′FL Transporter Constraint

graph: supported. Targets: CommunityMech:000220.

Retain the measured substrate constraint and explicitly PARTIAL genomic explanation.

The participant is the FT-1 B. breve isolate. Lack of substantial growth on 2′FL/fucose, lactose growth and predicted intracellular GH95 support the bounded description; no identified transporter is a search result, not a knockout. The node has no downstream arrow and does not cause donor hydrolysis.

### ecological_interactions[1]: R. gnavus Extracellular Fucosidase Capacity

graph: supported. Targets: CommunityMech:000220.

Retain computational potential, with FT-1 donor R. gnavus → B. breve as the proposed beneficiary direction.

Six encoded fucosidases and two predicted extracellular proteins provide a candidate route, not a secretion/activity measurement. The pairwise direction describes the proposed benefit and does not make gene presence a cross-feeding experiment or a mechanism shared by all three infant cultures.

### ecological_interactions[2]: R. gnavus 2′FL Hydrolysis Feeds B. breve

graph: supported. Targets: CommunityMech:000220.

Retain the PARTIAL R. gnavus → B. breve cross-feeding model.

Complementary growth on 2′FL, fucose and lactose, higher coculture OD and relative B. breve representation support the authors’ model. They do not directly establish released lactose, donor-to-recipient flux or reciprocal partner benefit. The current node states these limits correctly.

### ecological_interactions[3]: B. breve Coculture Dominance and Lactose Growth

graph: supported. Targets: CommunityMech:000220.

Retain the separation of 2′FL coculture composition from supplied-lactose growth controls.

The encoded R. gnavus → B. breve orientation follows the candidate model; the node does not assign a new interaction type. Approximate dominance is a source-reported summary, not a constant fraction at every sampling time. Relative sequencing representation, total OD and monoculture growth rate are different endpoints and do not trace lactose mediation.

### ecological_interactions[4]: Individualized HMO Utilization Capacity

graph: supported. Targets: CommunityMech:000220.

Retain the community-level comparison and its non-universal participant scope.

The listed R. gnavus/B. breve partners highlight FT-1 and the PT-1 donor experiment; FT-2 has other predicted extracellular-fucosidase producers. Treatment-specific responses and genome predictions support variability without making the two taxa the full roster or a universal causal circuit.

### ecological_interactions[5]: R. gnavus PT-1 2′FL Rescue

graph: supported. Targets: CommunityMech:000220.

Retain the measured donor intervention and unresolved mediator distinction.

FT-1 R. gnavus is added to PT-1 with 0.3% 2′FL, with B. breve as the response taxon. Enrichment and associated pH/diversity changes are measured; the extracellular-fucosidase/lactose explanation remains inferred. Low endpoint donor representation does not establish absence of donor exposure.

### ecological_interactions[1].downstream[0]: capacity → proposed hydrolysis/feeding

graph: supported. Targets: CommunityMech:000220.

Retain PARTIAL: predicted donor capacity supplies a plausible molecular route.

For the FT-1 R. gnavus → B. breve pair, extracellular-localization predictions can explain access to 2′FL-derived lactose. Localization, cleavage products and gene necessity were not selectively demonstrated; the arrow already states this.

### ecological_interactions[1].downstream[1]: capacity → PT-1 rescue

graph: supported. Targets: CommunityMech:000220.

Retain PARTIAL: an added candidate producer accompanies the measured PT-1 response.

The added organism is FT-1 R. gnavus and the responding population is PT-1 B. breve. Donor supplementation tests the organism-level intervention, not the necessity of either predicted extracellular fucosidase; do not generalize the FT-1 genome route to every infant community.

### ecological_interactions[2].downstream[0]: proposed lactose supply → dominance

graph: supported. Targets: CommunityMech:000220.

Retain PARTIAL: lactose growth controls support the proposed explanation without measuring mediation.

The candidate R. gnavus → B. breve transfer could favor B. breve in the FT-1 pair. Supplied-lactose growth and 2′FL relative composition are separate observations; neither establishes lactose flux or that this molecule uniquely causes dominance.

### ecological_interactions[2].downstream[1]: proposed lactose supply → PT-1 rescue

graph: supported. Targets: CommunityMech:000220.

Retain PARTIAL: measured donor supplementation and inferred lactose mediation remain separate.

FT-1 R. gnavus supplementation enriches PT-1 B. breve under the tested substrate condition. No lactose-selective intervention establishes mediation of enrichment, acidification or diversity, and the existing arrow appropriately avoids that conclusion.

### Description, engineering endpoint and ingredient rationale

evidence: concern. Targets: CommunityMech:000220.

Non-graph prose makes the proposed molecular route and medium necessity more definite than the inspected experiments.

The article abstract itself uses stronger wording, but the main Results explicitly infer released lactose and the supplements add no direct flux assay. Record prose should inherit the graph’s qualifications; substrate-dependent responses do not make 2′FL or lactose universal requirements of infant-gut cultivation. Preserve measured donor effects rather than dismissing the whole model.

### Culture regimes, medium and physical environment

completeness: concern. Targets: CommunityMech:000220.

Recover the reported assay media and separate context-specific settings while documenting the source timing conflict.

Community recovery and 30 µL into 3 mL passages at 37 °C are source-supported. The pair has distinct precultures, washed OD-standardized inocula and dextrose-free BHI with 1% individual sugar; the source does not expressly assign it the community vessel/working volume. PT-1 supplementation mixes donor and community at 1:4 before the community assay. Preserve the exact 144 h Methods quote but explain Figure 4/source-data 168 h. Fecal material is inoculum provenance, not the physical assay medium; no new ENVO term or exact CultureMech equivalent was verified.

### related_ingredients[1]: generic proposed lactose versus alpha-lactose

grounding: concern. Targets: CommunityMech:000220.

The inferred released metabolite is generic lactose; its anomer was not measured.

CHEBI:36219 is a valid alpha-lactose term but exceeds the evidence for the proposed released mediator. CHEBI:17716 is already used correctly in the graph. A possibly anomer-specific commercial control reagent would not establish the anomer released during coculture. No broader carbohydrate-ID error or metal/REE process is inferred.

### Public data and source lineage

completeness: concern. Targets: CommunityMech:000220.

The empty dataset list omits directly reported, resolvable study resources.

Figshare 22320865 v2 lists the manuscript-related new MAG archive. Figshare 13667816 v1 is an earlier dereplicated reference collection. Original stool samples SRS8184257, SRS8184183 and SRS8184427 correspond to FT-1, FT-2 and PT-1 aliases; they are not newly sequenced pure-culture deposits. Metadata were verified, not archive payloads or raw sequences.

### Caches, exact evidence and prior graph repair

provenance: supported. Targets: CommunityMech:000220.

The source comparisons support the quotations and preserve the earlier graph-only repair.

The TXT cache is abstract-only; the MD header says abstract_only despite appended main text. Fresh direct XML/publisher and PubMed spans resolve all 25 quotations. Closed issues 639/748 are historical context, not a reason to restore obsolete abundance thresholds; open 1256 concerns non-graph follow-up. The prior discussion’s unread-source statement describes its historical review scope, not the current expanded assessment.

### Native checks and current source assessment

schema: supported. Targets: CommunityMech:000220.

All eight native checks pass; the source audit identifies semantic and completeness issues beyond those gates.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000220.

Mechanical metrics remain distinct from evidence for the proposed molecular route.

## Findings

### mechanism-prose: Qualify non-graph lactose mediation and substrate necessity

major / open / confirmed; issue key: cm-000220-mechanism-prose.

Description and ingredient prose turn inferred extracellular lactose release into established mediation and prescribe general medium requirements beyond the tested comparisons.

### assay-context: Separate culture contexts and document the endpoint discrepancy

minor / open / confirmed; issue key: cm-000220-assay-context.

One cultivation block joins community serial-passage settings with pairwise sampling, omits recoverable assay media and uses fecal source material as the physical environment; Methods and reported Figure 4 data disagree on the final time.

### lactose-anomer: Use evidence-matched lactose specificity

minor / open / confirmed; issue key: cm-000220-lactose-anomer.

The related ingredient encodes alpha-lactose for an inferred released mediator whose anomer was not established.

### archive-links: Add the source-linked datasets with their correct provenance

minor / open / confirmed; issue key: cm-000220-archive-links.

Publicly resolved manuscript MAGs and original infant sample identifiers are absent from associated_datasets, while the earlier reference-genome collection needs separate attribution.

## Recommended Actions And Acceptance Checks

### repair-mechanism-prose

Qualify non-graph lactose mediation and substrate necessity.

- Describe extracellular localization as predicted and lactose release/mediation as the authors’ supported inference, not directly measured flux or enzyme activity.
- Retain the measured donor-dependent growth/enrichment results and distinguish total OD, composition and molecular mediation.
- Replace universal 2′FL/HMO/lactose medium requirements with the specific tested substrate contexts; do not require addition of both substrate and proposed product.
- Keep literal source quotations intact while qualifying their explanations against main Results and SI; retain all six bounded nodes and four PARTIAL arrows.

### repair-assay-context

Separate culture contexts and document the endpoint discrepancy.

- Separate community serial passages, FT-1 isolate mono/cocultures and PT-1 donor supplementation; attach each volume, vessel, temperature and schedule only to its supported assay.
- Add source-backed growth-media entries for the focal pair and relevant community contexts, including the distinct precultures and individual sugar treatments; do not invent an exact CultureMech recipe match.
- Preserve the verbatim 144 h Methods quotation and explicitly record that Figure 4 pixels, caption and Source Data use 168 h; do not silently claim a resolved author correction.
- Retain fecal inoculum provenance separately from the physical laboratory culture environment and modeled infant habitat; verify any replacement ontology grounding before applying it.
- Keep FT-1 isolate and PT-1 recipient context explicit without inventing collection-strain codes, pairwise vessel volume or universal abundance.

### repair-lactose-anomer

Use evidence-matched lactose specificity.

- Use verified generic lactose CHEBI:17716 for the proposed released mediator unless direct anomer-specific evidence is supplied.
- Keep reagent identity distinct from the inferred coculture product; a control-reagent specification does not establish the released anomer.
- Preserve the graph’s existing generic lactose grounding and rerun term/reference checks after authorized correction.

### repair-archive-links

Add the source-linked datasets with their correct provenance.

- Link manuscript-related MAG deposit Figshare 22320865 with its verified version and metadata scope; distinguish earlier reference collection Figshare 13667816.
- Record the original sample mappings FT-1 SRS8184257/SAMN17763864/L2_031_090G1, FT-2 SRS8184183/SAMN17764164/L3_130_056G1 and PT-1 SRS8184427/SAMN17764012/L3_069_015G1 with source evidence.
- Do not label these original stool samples as pure-culture genomes or certify uninspected archive contents, raw reads or accession ranges.

### preserve-qualified-graph

Preserve the six qualified nodes and four PARTIAL arrows during separately authorized follow-up.

- Keep genomic potential, total OD, relative composition, donor supplementation and inferred molecular mediation distinct.
- Do not turn the conceptual infant-feeding figure into an in-vivo trial or impose the FT-1 pair on every donor community.
- Preserve append-only history and rerun schema, strict, term, reference, history and target/corpus network checks after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml; Whole record: selected pair, three infant-derived systems, six nodes and four arrows | supports | The experimental umbrella is explicit and the graph is qualified; surrounding narrative, cultivation context, chemical specificity and archive links need bounded follow-up. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=37973815&amp;retmode=xml; Article-level metadata | supports | PubMed verifies the PMID, DOI, title and abstract. |
| crossref | https://api.crossref.org/works/10.1038/s41467-023-43279-y; Article-level metadata | supports | Crossref verifies the DOI/title and publication metadata. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:37973815&amp;format=json&amp;resultType=core; Article-level metadata | supports | Europe PMC verifies article-level identifiers and the open full-text route. |
| constraint | PMID:37973815; Fresh XML Sec7; Methods Sec15 and transporter search; Figure 4 and Supplementary Figure 7 | supports | The FT-1 B. breve isolate fails to show substantial 2′FL/fucose growth, while lactose growth and genomic predictions support a bounded substrate-access explanation. |
| capacity | PMID:37973815; Fresh XML Sec7; Methods functional annotation; Supplementary Data Files 1–2 | supports | FT-1 R. gnavus has six predicted fucosidases, two with predicted extracellular localization; this is not a measured secretion or enzyme-activity assay. |
| feeding | PMID:37973815; Fresh XML Sec7, final growth-comparison and interpretation paragraphs | supports | The authors infer lactose mediation from complementary substrate controls and coculture growth; released lactose, transfer flux and enzyme necessity were not directly resolved. |
| dominance | PMID:37973815; Fresh XML Sec7; Figure 4; Supplementary Table 3 | supports | The approximately 80% statement describes the 2′FL coculture; faster B. breve growth on supplied lactose is a separate control endpoint. |
| variation | PMID:37973815; Fresh XML Sec6–Sec8, including Sec7 opening comparison; Figures 3 and 5 | supports | The three infant-derived communities differ in composition, predicted capacity and response; the FT-1 pair is not a universal infant microbiome roster. |
| rescue | PMID:37973815; Fresh XML Sec8; Methods Sec17; Figure 5 | supports | Adding FT-1 R. gnavus to PT-1 with 0.3% 2′FL enriches B. breve and accompanies lower pH/diversity; selective lactose mediation remains unresolved. |
| methods | PMID:37973815; Fresh XML Methods Sec12, Sec13, Sec15–Sec17 | supports | Community serial passages, FT-1 isolate mono/cocultures and PT-1 supplementation have distinct preparations; the pair uses dextrose-free BHI with 1% individual test sugar and OD-standardized inocula. |
| main-figures | PMID:37973815; Figures 1–6: all pixels/panels and captions; individual hashes in source-audit.json | supports | Figures show cultivation-dependent composition, substrate-growth controls and the donor intervention; Figure 6 is a conceptual feeding model, not an infant intervention trial. |
| figure-4 | PMID:37973815; Figure 4 pixels: all growth and composition panels | supports | Growth curves extend to 168 h and composition bars are labeled 24, 72 and 168 h; total OD and relative composition do not measure transfer flux. |
| supplement | PMID:37973815; Supplementary Information: all seven figure images/captions and Tables 1–3 | supports | Supplementary controls support treatment-dependent composition and substrate-growth differences; they add no direct lactose-transfer or enzyme-necessity measurement. |
| supp-data | PMID:37973815; Supplementary Data Files 1–2: all cells; supplemental workbook inspection receipt | supports | Gene/pathway presence and localization predictions are computational evidence; they do not convert the proposed extracellular route into measured activity. |
| timing | PMID:37973815; Source Data: Figure 4 pt1 OD600 time/condition/culture columns and Figure 4 pt2 stacked bar chart, all 18 rows | supports | All 489 OD rows use times 0, 24, 55, 72, 120 or 168 h; composition times are 24, 72 and 168 h. This corroborates Figure 4 while retaining the conflicting 144 h Methods statement. |
| ontology | Local OAK NCBITaxon, ENVO, CHEBI and GO; ontology-authority.json: seven pairs across 33 occurrences and semantic notes | supports | All encoded ID/label strings match; alpha-lactose is an anomer-specific term, generic lactose allows either anomer, and fecal material denotes the inoculum material. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity.environment_term and modeled_environment; FunctionalRoleEnum; AbundanceLevelEnum | supports | Physical cultivation environment is distinct from modeled habitat and source material; functional roles and abundance remain contextual, with no arbitrary percentage cutoff. |
| snippets | kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml; snippet-audit.json | supports | All 25 snippets match a directly retrieved cited-source text: 15 XML/publisher and 11 abstract matches, with overlap; no indexed-only evidence. |
| history | kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml; provenance-audit.json | supports | The graph-only history remains bounded; closed 1254 preserves the repair and open 1256 includes the non-graph follow-up. |
| resources | kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml; dataset-verification.json | supports | Both Figshare deposits and all three original sample aliases resolve; new MAGs, prior reference genomes and original infant samples have distinct provenance. |
| native-target | kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml; support-audit.json | supports | The target network is COMPLETE: six nodes, four arrows and thirteen node evidence items; this does not certify causal mediation. |
| source-scope | PMID:37973815; source-audit.json | supports | Whole main, six figures, seven supplementary figures, three tables and two small gene workbooks were read; Source Data inspection was bounded to Figure 4 and workbook inventory. |
| independent-source | PMID:37973815; root-independent-source-audit.json | context_only | Independent full-source assessment agrees with the four bounded findings and preserves the existing graph qualifications. |
| search | Owned maintained roots; local-search.json: ignored-inclusive bounded searches | supports | Reusable identity and mapping discovery was bounded to recorded roots; no global absence is asserted. |
| adapter | Optional structured source adapter; adapter-check.json: same-runtime batch 06 discovery reuse | supports | No runnable adapter was available in the owned runtime; no external runner or paid provider was used. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml; Actual execution 2026-10-21T11:02:25.219397+00:00 to 2026-10-21T11:02:27.147795+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-strict kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml --out /private/tmp/cm-review-session/batch-06/000220/strict-report.tsv; Actual execution 2026-10-21T11:02:25.220090+00:00 to 2026-10-21T11:02:28.675562+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-terms kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml; Actual execution 2026-10-21T11:02:25.220425+00:00 to 2026-10-21T11:02:28.078821+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-gtdb kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml; Actual execution 2026-10-21T11:02:27.148211+00:00 to 2026-10-21T11:02:27.247498+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-gtdb-domain kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml; Actual execution 2026-10-21T11:02:27.247760+00:00 to 2026-10-21T11:02:28.726068+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-history history/records/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding; Actual execution 2026-10-21T11:02:28.079187+00:00 to 2026-10-21T11:02:28.892063+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T11:02:28.892808+00:00 to 2026-10-21T11:02:28.960593+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-references-explained kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml; Actual execution 2026-10-21T11:02:28.960991+00:00 to 2026-10-21T11:02:30.104711+00:00 | supports | Target reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T10:06:35.990708+00:00 to 2026-10-21T10:06:41.713287+00:00 | supports | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T10:06:35.990845+00:00 to 2026-10-21T10:06:41.708376+00:00 | supports | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |

## Limits And Additional Notes

- No raw sequences, genome/annotation pipelines, growth statistics or molecular flux were reanalyzed. Archive metadata and listings do not certify payload contents.
- Source Data inspection covers all Figure 4 time/condition/culture columns and 18 composition rows plus workbook inventory; other sheets were not read row by row. Reporting-summary and peer-review contents were not assessed.
- Methods state 144 h while Figure 4 pixels, caption and Source Data report 168 h; no author correction or resolved replacement protocol is asserted.
- The inferred released lactose anomer, direct transfer flux and enzyme necessity remain unmeasured in the inspected main/SI. A supplied reagent specification would not establish the released product’s anomer.
- The pair’s vessel/working volume and an exact CultureMech recipe equivalent are not independently resolved. Community settings and catalogue/reference genomes must not be transferred to that assay without source support.
- Existing GTDB mappings passed native checks; historical mapping-release statistics were not re-certified or replaced.
- No canonical, cache, history or generated file changed.
- All 24 repository inputs were pinned before assessment and rechecked.
- Eighteen quoted words from the focal publication, including the total budget for its supplements.
- Native quality 100 is capped from 119; source findings remain actionable.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110927Z-bifidobacterium-ruminococcus-hmo-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Bifidobacterium–Ruminococcus infant HMO cross-feeding: record review'
started_at: '2026-10-21T11:01:48.875171Z'
finished_at: '2026-10-21T11:09:27.203850Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, native/ontology checks
    and supporting snippets/provenance; no person-level independence is asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Complete source review supports all six qualified nodes and four PARTIAL
  arrows. One major finding concerns non-graph mechanism and substrate-necessity overstatement;
  three minor findings concern assay/environment context, lactose specificity and
  omitted source-linked datasets. Preserve the 144 h Methods versus 168 h Figure 4/source-data
  discrepancy.
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
  - path: history/records/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding/2026-10-05T112950Z-codex-80ba32.yaml
    sha256: c8647b1d6103d42c380071344e445339edbac1c9eee3d319634bd7911870effe
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    sha256: b66bdeaa74b0e354b43d2df5940e8c1cb36c3aed56a962f9c50f10df12edc3a1
    role: target
  - path: references_cache/PMID_37973815.md
    sha256: 4dc657ac520622a4524d10b5a3115461e1dea4d1d26acf5f4d08ce6eb2fa77e8
    role: context
  - path: references_cache/PMID_37973815.txt
    sha256: 5a04de439b90cf45dd5e7ecd1cc5a99716977d7e4ee08edd7d735b3fd427dadb
    role: context
  - path: reports/causal_graph_review/decisions/20261005-eleven-records-batch6.yaml
    sha256: 23f5fa6fc197e020f7cb3469749ebe4aa78886f8973cb6ed63fde321470a7f96
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
- target_id: CommunityMech:000220
  path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  label: Bifidobacterium-Ruminococcus Infant HMO Cross-Feeding Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    role: canonical_record
scope:
  description: Whole record, six nodes and four arrows assessed against complete scientific
    main, all main/SI figures and tables, two small gene workbooks, bounded Figure
    4 source data and public archive metadata.
  selection: Next assigned maintained path after 000401 was saved and both mandatory
    post-save checks passed; only CommunityMech:000220 reviewed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000220
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000220
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify molecular mediation.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000220
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-strict kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    --out /private/tmp/cm-review-session/batch-06/000220/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify molecular mediation.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000220
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-terms kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify molecular mediation.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000220
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify molecular mediation.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000220
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify molecular mediation.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000220
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-history history/records/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify molecular mediation.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000220
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify molecular mediation.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000220
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-references-explained kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify molecular mediation.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; target-native structure has no issue.
  target_ids:
  - CommunityMech:000220
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Reused fresh full-corpus batch 06 execution, not a target-specific pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; target-native structure has no issue.
  target_ids:
  - CommunityMech:000220
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Reused fresh full-corpus batch 06 execution, not a target-specific pass.
- check_id: source-identity
  name: Primary publication and archive identity
  status: passed
  required: true
  summary: Direct metadata, complete primary text and the reported archive identities
    were verified.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - resources
- check_id: scientific-source
  name: Full primary scientific assessment
  status: passed
  required: true
  summary: Whole main, all main/SI figures and tables, two gene workbooks and bounded
    Figure 4 source data were inspected.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - source-scope
  - independent-source
  - supplement
  - supp-data
  - timing
- check_id: cross-mech
  name: Encoded medium/ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech identifier is encoded; no exact recipe
    equivalence was inferred.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - record
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No runnable adapter was available in the owned runtime.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  locator: 'Whole record: selected pair, three infant-derived systems, six nodes and
    four arrows'
  summary: The experimental umbrella is explicit and the graph is qualified; surrounding
    narrative, cultivation context, chemical specificity and archive links need bounded
    follow-up.
  support: supports
  accessed_at: '2026-10-21T11:08:33.965647Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=37973815&retmode=xml
  locator: Article-level metadata
  summary: PubMed verifies the PMID, DOI, title and abstract.
  support: supports
  accessed_at: '2026-10-21T11:02:05.208128Z'
  snapshot_sha256: 77214fbdc8da393c8a7d25fe024167a44d6f469eed6e0528d4f1998a26fb20e1
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1038/s41467-023-43279-y
  locator: Article-level metadata
  summary: Crossref verifies the DOI/title and publication metadata.
  support: supports
  accessed_at: '2026-10-21T11:02:05.147428Z'
  snapshot_sha256: 516b8af10d1d1858ddff3e928a4cb66505e71545f1bbf44d20d7620a8cefa1a7
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:37973815&format=json&resultType=core
  locator: Article-level metadata
  summary: Europe PMC verifies article-level identifiers and the open full-text route.
  support: supports
  accessed_at: '2026-10-21T11:02:05.485726Z'
  snapshot_sha256: c0c1489806916c066010648f88277d398d81737b7a3c3ddf25d154d45ea071d6
- evidence_id: constraint
  kind: primary_source
  reference: PMID:37973815
  locator: Fresh XML Sec7; Methods Sec15 and transporter search; Figure 4 and Supplementary
    Figure 7
  summary: The FT-1 B. breve isolate fails to show substantial 2′FL/fucose growth,
    while lactose growth and genomic predictions support a bounded substrate-access
    explanation.
  support: supports
  accessed_at: '2026-10-21T11:08:33.966365Z'
  quote: No growth was detected
  snapshot_sha256: b682eed5035e9d8edceb6477c84ddacaa45a586b913829553d3ef703ecd7e85d
- evidence_id: capacity
  kind: primary_source
  reference: PMID:37973815
  locator: Fresh XML Sec7; Methods functional annotation; Supplementary Data Files
    1–2
  summary: FT-1 R. gnavus has six predicted fucosidases, two with predicted extracellular
    localization; this is not a measured secretion or enzyme-activity assay.
  support: supports
  accessed_at: '2026-10-21T11:08:33.966515Z'
  quote: predicted to be extracellular
  snapshot_sha256: b682eed5035e9d8edceb6477c84ddacaa45a586b913829553d3ef703ecd7e85d
- evidence_id: feeding
  kind: primary_source
  reference: PMID:37973815
  locator: Fresh XML Sec7, final growth-comparison and interpretation paragraphs
  summary: The authors infer lactose mediation from complementary substrate controls
    and coculture growth; released lactose, transfer flux and enzyme necessity were
    not directly resolved.
  support: supports
  accessed_at: '2026-10-21T11:08:33.966619Z'
  quote: we infer
  snapshot_sha256: b682eed5035e9d8edceb6477c84ddacaa45a586b913829553d3ef703ecd7e85d
- evidence_id: dominance
  kind: primary_source
  reference: PMID:37973815
  locator: Fresh XML Sec7; Figure 4; Supplementary Table 3
  summary: The approximately 80% statement describes the 2′FL coculture; faster B.
    breve growth on supplied lactose is a separate control endpoint.
  support: supports
  accessed_at: '2026-10-21T11:08:33.966725Z'
  quote: dominated the co-culture community
  snapshot_sha256: b682eed5035e9d8edceb6477c84ddacaa45a586b913829553d3ef703ecd7e85d
- evidence_id: variation
  kind: primary_source
  reference: PMID:37973815
  locator: Fresh XML Sec6–Sec8, including Sec7 opening comparison; Figures 3 and 5
  summary: The three infant-derived communities differ in composition, predicted capacity
    and response; the FT-1 pair is not a universal infant microbiome roster.
  support: supports
  accessed_at: '2026-10-21T11:08:33.966819Z'
  quote: distinct effects
  snapshot_sha256: b682eed5035e9d8edceb6477c84ddacaa45a586b913829553d3ef703ecd7e85d
- evidence_id: rescue
  kind: primary_source
  reference: PMID:37973815
  locator: Fresh XML Sec8; Methods Sec17; Figure 5
  summary: Adding FT-1 R. gnavus to PT-1 with 0.3% 2′FL enriches B. breve and accompanies
    lower pH/diversity; selective lactose mediation remains unresolved.
  support: supports
  accessed_at: '2026-10-21T11:08:33.966911Z'
  quote: significantly enriched
  snapshot_sha256: b682eed5035e9d8edceb6477c84ddacaa45a586b913829553d3ef703ecd7e85d
- evidence_id: methods
  kind: primary_source
  reference: PMID:37973815
  locator: Fresh XML Methods Sec12, Sec13, Sec15–Sec17
  summary: Community serial passages, FT-1 isolate mono/cocultures and PT-1 supplementation
    have distinct preparations; the pair uses dextrose-free BHI with 1% individual
    test sugar and OD-standardized inocula.
  support: supports
  accessed_at: '2026-10-21T11:08:33.967001Z'
  snapshot_sha256: b682eed5035e9d8edceb6477c84ddacaa45a586b913829553d3ef703ecd7e85d
- evidence_id: main-figures
  kind: primary_source
  reference: PMID:37973815
  locator: 'Figures 1–6: all pixels/panels and captions; individual hashes in source-audit.json'
  summary: Figures show cultivation-dependent composition, substrate-growth controls
    and the donor intervention; Figure 6 is a conceptual feeding model, not an infant
    intervention trial.
  support: supports
  accessed_at: '2026-10-21T11:08:33.967039Z'
  snapshot_sha256: bc6e8ee98b15cd879636b72ae747f055014e29d202c9b90502f413c6ae101111
- evidence_id: figure-4
  kind: primary_source
  reference: PMID:37973815
  locator: 'Figure 4 pixels: all growth and composition panels'
  summary: Growth curves extend to 168 h and composition bars are labeled 24, 72 and
    168 h; total OD and relative composition do not measure transfer flux.
  support: supports
  accessed_at: '2026-10-21T11:08:33.967112Z'
  snapshot_sha256: bb238c569ce5a1709f3daf107fa6c79d34e0644ae197caea913da31e5295ad22
- evidence_id: supplement
  kind: primary_source
  reference: PMID:37973815
  locator: 'Supplementary Information: all seven figure images/captions and Tables
    1–3'
  summary: Supplementary controls support treatment-dependent composition and substrate-growth
    differences; they add no direct lactose-transfer or enzyme-necessity measurement.
  support: supports
  accessed_at: '2026-10-21T11:08:33.967948Z'
  snapshot_sha256: 4fbca70f7efbcd0f9cf31037f5d0be673375661255b75a86acbf6bcd2d8c234c
- evidence_id: supp-data
  kind: primary_source
  reference: PMID:37973815
  locator: 'Supplementary Data Files 1–2: all cells; supplemental workbook inspection
    receipt'
  summary: Gene/pathway presence and localization predictions are computational evidence;
    they do not convert the proposed extracellular route into measured activity.
  support: supports
  accessed_at: '2026-10-21T11:08:33.968081Z'
  snapshot_sha256: dbad134117f90b683e1dc317e1265d9ed17e4dc87fb4146b051e4081fc009db6
- evidence_id: timing
  kind: primary_source
  reference: PMID:37973815
  locator: 'Source Data: Figure 4 pt1 OD600 time/condition/culture columns and Figure
    4 pt2 stacked bar chart, all 18 rows'
  summary: All 489 OD rows use times 0, 24, 55, 72, 120 or 168 h; composition times
    are 24, 72 and 168 h. This corroborates Figure 4 while retaining the conflicting
    144 h Methods statement.
  support: supports
  accessed_at: '2026-10-21T11:08:33.968214Z'
  snapshot_sha256: b7934a1bcf0c534e796d5527f059a9805c9e01b418341d7bad0882ee004ce39a
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, CHEBI and GO
  locator: 'ontology-authority.json: seven pairs across 33 occurrences and semantic
    notes'
  summary: All encoded ID/label strings match; alpha-lactose is an anomer-specific
    term, generic lactose allows either anomer, and fecal material denotes the inoculum
    material.
  support: supports
  accessed_at: '2026-10-21T11:08:33.968433Z'
  snapshot_sha256: 03bed86eb1b7c2d79d0008153b84cb30f8d806ac79f61d4c647ec1c4f56fc65f
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity.environment_term and modeled_environment; FunctionalRoleEnum;
    AbundanceLevelEnum
  summary: Physical cultivation environment is distinct from modeled habitat and source
    material; functional roles and abundance remain contextual, with no arbitrary
    percentage cutoff.
  support: supports
  accessed_at: '2026-10-21T11:08:33.968440Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  locator: snippet-audit.json
  summary: 'All 25 snippets match a directly retrieved cited-source text: 15 XML/publisher
    and 11 abstract matches, with overlap; no indexed-only evidence.'
  support: supports
  accessed_at: '2026-10-21T11:08:33.968617Z'
  snapshot_sha256: 856be5a51354e3777010fa4234c9db5076ee789c091116445e20c3c4a4770092
- evidence_id: history
  kind: record_content
  reference: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  locator: provenance-audit.json
  summary: The graph-only history remains bounded; closed 1254 preserves the repair
    and open 1256 includes the non-graph follow-up.
  support: supports
  accessed_at: '2026-10-21T11:08:33.969148Z'
  snapshot_sha256: 34bacdc08ff7ded355a9af2dacb618c137eba902adaac58178f92a6b5f673cf0
- evidence_id: resources
  kind: validation
  reference: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  locator: dataset-verification.json
  summary: Both Figshare deposits and all three original sample aliases resolve; new
    MAGs, prior reference genomes and original infant samples have distinct provenance.
  support: supports
  accessed_at: '2026-10-21T11:08:33.969351Z'
  snapshot_sha256: 0484447f90bd260e943257ad2162d0bc7e506df64f49a69e36cebc2869baa6d8
- evidence_id: native-target
  kind: validation
  reference: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  locator: support-audit.json
  summary: 'The target network is COMPLETE: six nodes, four arrows and thirteen node
    evidence items; this does not certify causal mediation.'
  support: supports
  accessed_at: '2026-10-21T11:08:33.969517Z'
  snapshot_sha256: 03f3c4b0cab788a11192bef815226f83163d7e289f6be99d342b2f96dcf5de7e
- evidence_id: source-scope
  kind: validation
  reference: PMID:37973815
  locator: source-audit.json
  summary: Whole main, six figures, seven supplementary figures, three tables and
    two small gene workbooks were read; Source Data inspection was bounded to Figure
    4 and workbook inventory.
  support: supports
  accessed_at: '2026-10-21T11:08:33.969576Z'
  snapshot_sha256: bc6e8ee98b15cd879636b72ae747f055014e29d202c9b90502f413c6ae101111
- evidence_id: independent-source
  kind: validation
  reference: PMID:37973815
  locator: root-independent-source-audit.json
  summary: Independent full-source assessment agrees with the four bounded findings
    and preserves the existing graph qualifications.
  support: context_only
  accessed_at: '2026-10-21T11:08:33.969747Z'
  snapshot_sha256: e34a63fcba823416539022367f7c9aafef5ecb4404d4d01cf8e99a51a53952b5
- evidence_id: search
  kind: search
  reference: Owned maintained roots
  locator: 'local-search.json: ignored-inclusive bounded searches'
  summary: Reusable identity and mapping discovery was bounded to recorded roots;
    no global absence is asserted.
  support: supports
  accessed_at: '2026-10-21T11:08:33.969911Z'
  snapshot_sha256: c0528bb05fc1680fc7d59f85bc2695c090e9583fea4c6e001872f5207169b9ad
  search_scope: Ignored-inclusive maintained community, isolate and reusable-taxon
    roots and bounded mapping-file discovery.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: 'adapter-check.json: same-runtime batch 06 discovery reuse'
  summary: No runnable adapter was available in the owned runtime; no external runner
    or paid provider was used.
  support: supports
  accessed_at: '2026-10-21T11:08:33.970081Z'
  snapshot_sha256: b22edd96de3dfb4f3f628183cd54dadeffd000232b15118e6f7693c766e4d840
  search_scope: Recorded batch 06 PATH/venv/module and ignored-inclusive discovery,
    reused in the same runtime.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  locator: Actual execution 2026-10-21T11:02:25.219397+00:00 to 2026-10-21T11:02:27.147795+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T11:02:27.147795Z'
  snapshot_sha256: 544adbf5a29dbfe3f4032907d2aae3c87587654ac8a4b70f8be52973122d34c6
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-strict kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    --out /private/tmp/cm-review-session/batch-06/000220/strict-report.tsv
  locator: Actual execution 2026-10-21T11:02:25.220090+00:00 to 2026-10-21T11:02:28.675562+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T11:02:28.675562Z'
  snapshot_sha256: ec9f79bf94a788e2718150ed7ccf8d7e50448fc864ee5e1c3ab512ad8cfd6af0
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-terms kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  locator: Actual execution 2026-10-21T11:02:25.220425+00:00 to 2026-10-21T11:02:28.078821+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T11:02:28.078821Z'
  snapshot_sha256: 581d8896dfeb577bee563618c651584763f4d484a97c9ba8882da94e0856bb58
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  locator: Actual execution 2026-10-21T11:02:27.148211+00:00 to 2026-10-21T11:02:27.247498+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T11:02:27.247498Z'
  snapshot_sha256: 1f89613dd689f58348fde3aa03dab73070c88c16bf90cbd4e132888aa895e1c7
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  locator: Actual execution 2026-10-21T11:02:27.247760+00:00 to 2026-10-21T11:02:28.726068+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T11:02:28.726068Z'
  snapshot_sha256: 75f1419d8f29ede11520220b67db2e6972cb6f480e637e8a7a0a39f11c6fc452
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-history history/records/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding
  locator: Actual execution 2026-10-21T11:02:28.079187+00:00 to 2026-10-21T11:02:28.892063+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T11:02:28.892063Z'
  snapshot_sha256: 2a21e807eb2206c1e4ff5feaf59b6c739a27fbf3cd0f80d4d8a7cc81e535c813
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T11:02:28.892808+00:00 to 2026-10-21T11:02:28.960593+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T11:02:28.960593Z'
  snapshot_sha256: 4ac9a88b3b313bd368a77de96152911bf0242766254c7f32df75deaf01b6aa30
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-references-explained kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
  locator: Actual execution 2026-10-21T11:02:28.960991+00:00 to 2026-10-21T11:02:30.104711+00:00
  summary: Target reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T11:02:30.104711Z'
  snapshot_sha256: e03cb273d358dccbdf4bf427449336afb2d78dd068dceaab9c59f4e397db0f8e
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T10:06:35.990708+00:00 to 2026-10-21T10:06:41.713287+00:00
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; target-native structure has no issue.
  support: supports
  accessed_at: '2026-10-21T10:06:41.713287Z'
  snapshot_sha256: 330e4d9c9367a126afe7da9d93d310348e0ba6cc1289d806f4ff8df350be9620
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T10:06:35.990845+00:00 to 2026-10-21T10:06:41.708376+00:00
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; target-native structure has no issue.
  support: supports
  accessed_at: '2026-10-21T10:06:41.708376Z'
  snapshot_sha256: 0420f90879ef008b71c8bfcfe444d05d2c030519aca57834b4e2587766c5b854
assessments:
- assessment_id: identity
  area: identity
  topic: Experimental umbrella and exact source context
  outcome: concern
  summary: The selected pair and wider infant-derived experiments are identifiable,
    but culture and source-material contexts need clearer separation.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - record
  - methods
  - variation
  - ontology
  dimensions:
  - name: community_scope
    value: Selected FT-1 pair within three infant-derived cultures
    definition: The two taxa are focal partners, not an exhaustive roster for FT-1,
      FT-2 and PT-1; retain the explicit wider study context.
    evidence_ids:
    - record
    - variation
  - name: source_strain
    value: B. breve and R. gnavus isolated from FT-1; FT-1 donor added to PT-1
    definition: Methods describe isolation and colony selection, without providing
      a verified collection-strain code for this pair; do not substitute reference
      genomes as isolates.
    evidence_ids:
    - methods
    - resources
  - name: environment
    value: Anaerobic laboratory cultures derived from infant fecal inocula
    definition: Fecal material identifies source material; the physical culture environment
      and modeled infant-gut habitat should be stated separately.
    evidence_ids:
    - schema
    - methods
    - ontology
  - name: medium
    value: Dextrose-free BHI plus individual 1% sugars for the pair
    definition: Community BHI–mucin/human-milk conditions, MRS/BHI precultures and
      0.3% 2′FL PT-1 supplementation are distinct contexts.
    evidence_ids:
    - methods
  - name: experimental_setting
    value: Community passages, pairwise batch growth and donor supplementation
    definition: Three-milliliter deep-well serial passage is explicit for community
      assays; it is not automatically the pairwise assay vessel/volume. Methods 144
      h conflicts with Figure 4/source-data 168 h.
    evidence_ids:
    - methods
    - figure-4
    - timing
  - name: evidence_tier
    value: Measured growth/composition, genomic predictions and inferred mediation
    definition: No direct released-lactose measurement, donor-resolved flux or selective
      enzyme perturbation was found in the inspected main/SI.
    evidence_ids:
    - feeding
    - capacity
    - supplement
    - supp-data
  - name: grounding_status
    value: Seven matched ontology pairs; one chemical-specificity concern
    definition: Current Mediterraneibacter labeling with source Ruminococcus naming
      is valid; alpha-lactose specificity is not established for the inferred mediator.
    evidence_ids:
    - ontology
- assessment_id: taxonomy
  area: grounding
  topic: Both focal taxa, abundance and functional roles
  outcome: supported
  summary: Retain source-resolved species and the qualified donor/recipient interpretation,
    with claim-level evidence for roles.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - capacity
  - feeding
  - dominance
  - variation
  - ontology
  - schema
  details: B. breve CROSS_FEEDER is the author-inferred recipient role; R. gnavus
    PRIMARY_DEGRADER is supported by substrate growth and predicted 2′FL-cleaving
    capacity. Do not restate predicted extracellular activity as directly measured.
    Both ABUNDANT labels are contextual across the experimental umbrella; the approximately
    80% B. breve result belongs to the 2′FL pair. No fixed dominance threshold, universal
    abundance or new strain accession is inferred. Existing GTDB syntax/status passes
    without independently re-certifying historical release counts.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: B. breve 2′FL Transporter Constraint'
  outcome: supported
  summary: Retain the measured substrate constraint and explicitly PARTIAL genomic
    explanation.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - constraint
  - methods
  - supplement
  details: The participant is the FT-1 B. breve isolate. Lack of substantial growth
    on 2′FL/fucose, lactose growth and predicted intracellular GH95 support the bounded
    description; no identified transporter is a search result, not a knockout. The
    node has no downstream arrow and does not cause donor hydrolysis.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: R. gnavus Extracellular Fucosidase Capacity'
  outcome: supported
  summary: Retain computational potential, with FT-1 donor R. gnavus → B. breve as
    the proposed beneficiary direction.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - capacity
  - supp-data
  - methods
  details: Six encoded fucosidases and two predicted extracellular proteins provide
    a candidate route, not a secretion/activity measurement. The pairwise direction
    describes the proposed benefit and does not make gene presence a cross-feeding
    experiment or a mechanism shared by all three infant cultures.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: R. gnavus 2′FL Hydrolysis Feeds B. breve'
  outcome: supported
  summary: Retain the PARTIAL R. gnavus → B. breve cross-feeding model.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - feeding
  - constraint
  - dominance
  - supplement
  - figure-4
  details: Complementary growth on 2′FL, fucose and lactose, higher coculture OD and
    relative B. breve representation support the authors’ model. They do not directly
    establish released lactose, donor-to-recipient flux or reciprocal partner benefit.
    The current node states these limits correctly.
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: B. breve Coculture Dominance and Lactose Growth'
  outcome: supported
  summary: Retain the separation of 2′FL coculture composition from supplied-lactose
    growth controls.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - dominance
  - figure-4
  - supplement
  - timing
  details: The encoded R. gnavus → B. breve orientation follows the candidate model;
    the node does not assign a new interaction type. Approximate dominance is a source-reported
    summary, not a constant fraction at every sampling time. Relative sequencing representation,
    total OD and monoculture growth rate are different endpoints and do not trace
    lactose mediation.
- assessment_id: node-4
  area: graph
  topic: 'ecological_interactions[4]: Individualized HMO Utilization Capacity'
  outcome: supported
  summary: Retain the community-level comparison and its non-universal participant
    scope.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - variation
  - supp-data
  - supplement
  details: The listed R. gnavus/B. breve partners highlight FT-1 and the PT-1 donor
    experiment; FT-2 has other predicted extracellular-fucosidase producers. Treatment-specific
    responses and genome predictions support variability without making the two taxa
    the full roster or a universal causal circuit.
- assessment_id: node-5
  area: graph
  topic: 'ecological_interactions[5]: R. gnavus PT-1 2′FL Rescue'
  outcome: supported
  summary: Retain the measured donor intervention and unresolved mediator distinction.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - rescue
  - methods
  - variation
  - supp-data
  details: FT-1 R. gnavus is added to PT-1 with 0.3% 2′FL, with B. breve as the response
    taxon. Enrichment and associated pH/diversity changes are measured; the extracellular-fucosidase/lactose
    explanation remains inferred. Low endpoint donor representation does not establish
    absence of donor exposure.
- assessment_id: edge-1-2
  area: graph
  topic: 'ecological_interactions[1].downstream[0]: capacity → proposed hydrolysis/feeding'
  outcome: supported
  summary: 'Retain PARTIAL: predicted donor capacity supplies a plausible molecular
    route.'
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - capacity
  - feeding
  - supp-data
  details: For the FT-1 R. gnavus → B. breve pair, extracellular-localization predictions
    can explain access to 2′FL-derived lactose. Localization, cleavage products and
    gene necessity were not selectively demonstrated; the arrow already states this.
- assessment_id: edge-1-5
  area: graph
  topic: 'ecological_interactions[1].downstream[1]: capacity → PT-1 rescue'
  outcome: supported
  summary: 'Retain PARTIAL: an added candidate producer accompanies the measured PT-1
    response.'
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - capacity
  - rescue
  - supp-data
  details: The added organism is FT-1 R. gnavus and the responding population is PT-1
    B. breve. Donor supplementation tests the organism-level intervention, not the
    necessity of either predicted extracellular fucosidase; do not generalize the
    FT-1 genome route to every infant community.
- assessment_id: edge-2-3
  area: graph
  topic: 'ecological_interactions[2].downstream[0]: proposed lactose supply → dominance'
  outcome: supported
  summary: 'Retain PARTIAL: lactose growth controls support the proposed explanation
    without measuring mediation.'
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - feeding
  - dominance
  - figure-4
  - supplement
  details: The candidate R. gnavus → B. breve transfer could favor B. breve in the
    FT-1 pair. Supplied-lactose growth and 2′FL relative composition are separate
    observations; neither establishes lactose flux or that this molecule uniquely
    causes dominance.
- assessment_id: edge-2-5
  area: graph
  topic: 'ecological_interactions[2].downstream[1]: proposed lactose supply → PT-1
    rescue'
  outcome: supported
  summary: 'Retain PARTIAL: measured donor supplementation and inferred lactose mediation
    remain separate.'
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - feeding
  - rescue
  - methods
  details: FT-1 R. gnavus supplementation enriches PT-1 B. breve under the tested
    substrate condition. No lactose-selective intervention establishes mediation of
    enrichment, acidification or diversity, and the existing arrow appropriately avoids
    that conclusion.
- assessment_id: narrative
  area: evidence
  topic: Description, engineering endpoint and ingredient rationale
  outcome: concern
  summary: Non-graph prose makes the proposed molecular route and medium necessity
    more definite than the inspected experiments.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - feeding
  - capacity
  - variation
  - record
  details: The article abstract itself uses stronger wording, but the main Results
    explicitly infer released lactose and the supplements add no direct flux assay.
    Record prose should inherit the graph’s qualifications; substrate-dependent responses
    do not make 2′FL or lactose universal requirements of infant-gut cultivation.
    Preserve measured donor effects rather than dismissing the whole model.
- assessment_id: cultivation
  area: completeness
  topic: Culture regimes, medium and physical environment
  outcome: concern
  summary: Recover the reported assay media and separate context-specific settings
    while documenting the source timing conflict.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - methods
  - figure-4
  - timing
  - schema
  - ontology
  details: Community recovery and 30 µL into 3 mL passages at 37 °C are source-supported.
    The pair has distinct precultures, washed OD-standardized inocula and dextrose-free
    BHI with 1% individual sugar; the source does not expressly assign it the community
    vessel/working volume. PT-1 supplementation mixes donor and community at 1:4 before
    the community assay. Preserve the exact 144 h Methods quote but explain Figure
    4/source-data 168 h. Fecal material is inoculum provenance, not the physical assay
    medium; no new ENVO term or exact CultureMech equivalent was verified.
- assessment_id: chemical
  area: grounding
  topic: 'related_ingredients[1]: generic proposed lactose versus alpha-lactose'
  outcome: concern
  summary: The inferred released metabolite is generic lactose; its anomer was not
    measured.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - ontology
  - feeding
  - methods
  details: CHEBI:36219 is a valid alpha-lactose term but exceeds the evidence for
    the proposed released mediator. CHEBI:17716 is already used correctly in the graph.
    A possibly anomer-specific commercial control reagent would not establish the
    anomer released during coculture. No broader carbohydrate-ID error or metal/REE
    process is inferred.
- assessment_id: resources
  area: completeness
  topic: Public data and source lineage
  outcome: concern
  summary: The empty dataset list omits directly reported, resolvable study resources.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - resources
  - methods
  - record
  details: Figshare 22320865 v2 lists the manuscript-related new MAG archive. Figshare
    13667816 v1 is an earlier dereplicated reference collection. Original stool samples
    SRS8184257, SRS8184183 and SRS8184427 correspond to FT-1, FT-2 and PT-1 aliases;
    they are not newly sequenced pure-culture deposits. Metadata were verified, not
    archive payloads or raw sequences.
- assessment_id: provenance
  area: provenance
  topic: Caches, exact evidence and prior graph repair
  outcome: supported
  summary: The source comparisons support the quotations and preserve the earlier
    graph-only repair.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - snippets
  - history
  - source-scope
  details: The TXT cache is abstract-only; the MD header says abstract_only despite
    appended main text. Fresh direct XML/publisher and PubMed spans resolve all 25
    quotations. Closed issues 639/748 are historical context, not a reason to restore
    obsolete abundance thresholds; open 1256 concerns non-graph follow-up. The prior
    discussion’s unread-source statement describes its historical review scope, not
    the current expanded assessment.
- assessment_id: validation
  area: schema
  topic: Native checks and current source assessment
  outcome: supported
  summary: All eight native checks pass; the source audit identifies semantic and
    completeness issues beyond those gates.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - source-scope
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality
  outcome: supported
  summary: Mechanical metrics remain distinct from evidence for the proposed molecular
    route.
  target_ids:
  - CommunityMech:000220
  evidence_ids:
  - native-target
  - record
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata including all roles +5 environment +10
      at least 3 factors +10 at least 3 nodes +5 resources +10 media +5 datasets +5
      node metabolites). 50+5+0+10+5+0+0+5=75.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50P1-10P2-2P3+20 min(mean node evidence/2,1)+15 if native
      COMPLETE,0,100). P1=0, P2=1, P3=3, P4=0; 13 evidence items/6 nodes gives the
      capped 20 evidence bonus; 100-10-6+20+15=119 before capping.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count.
  - name: P2
    value: 1
    unit: findings
    definition: Observed native severity count.
  - name: P3
    value: 3
    unit: findings
    definition: Observed native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count.
findings:
- finding_id: mechanism-prose
  issue_key: cm-000220-mechanism-prose
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: summary and ingredient rationale overstate the
    central molecular mechanism and generalize its necessity, despite the graph’s
    explicit limits.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Qualify non-graph lactose mediation and substrate necessity
  description: Description and ingredient prose turn inferred extracellular lactose
    release into established mediation and prescribe general medium requirements beyond
    the tested comparisons.
  target_ids:
  - CommunityMech:000220
  field_paths:
  - description
  - engineering_design.measurement_endpoints[2]
  - related_ingredients[0].relevance
  - related_ingredients[0].evidence[0].explanation
  - related_ingredients[1].relevance
  - related_ingredients[1].evidence[0].explanation
  evidence_ids:
  - feeding
  - capacity
  - variation
  - supplement
  - supp-data
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    role: canonical_record
- finding_id: assay-context
  issue_key: cm-000220-assay-context
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded protocol/context correction preserves valid
    community settings and the resolved focal model; it does not establish that the
    experiment or every recorded condition is wrong.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Separate culture contexts and document the endpoint discrepancy
  description: One cultivation block joins community serial-passage settings with
    pairwise sampling, omits recoverable assay media and uses fecal source material
    as the physical environment; Methods and reported Figure 4 data disagree on the
    final time.
  target_ids:
  - CommunityMech:000220
  field_paths:
  - cultivation_setup[0]
  - growth_media
  - environment_term
  evidence_ids:
  - methods
  - figure-4
  - timing
  - ontology
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    role: canonical_record
- finding_id: lactose-anomer
  issue_key: cm-000220-lactose-anomer
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: the broad chemical identity is correct, but anomer-specific
    grounding exceeds the mediator evidence.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Use evidence-matched lactose specificity
  description: The related ingredient encodes alpha-lactose for an inferred released
    mediator whose anomer was not established.
  target_ids:
  - CommunityMech:000220
  field_paths:
  - related_ingredients[1].chebi_term
  - related_ingredients[1].preferred_term
  evidence_ids:
  - ontology
  - feeding
  - methods
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    role: canonical_record
- finding_id: archive-links
  issue_key: cm-000220-archive-links
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: verified data links improve reproducibility without
    changing community identity or requiring raw-data reanalysis.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Add the source-linked datasets with their correct provenance
  description: Publicly resolved manuscript MAGs and original infant sample identifiers
    are absent from associated_datasets, while the earlier reference-genome collection
    needs separate attribution.
  target_ids:
  - CommunityMech:000220
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    role: canonical_record
actions:
- action_id: repair-mechanism-prose
  description: Qualify non-graph lactose mediation and substrate necessity.
  finding_ids:
  - mechanism-prose
  target_ids:
  - CommunityMech:000220
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    role: canonical_record
  acceptance_checks:
  - Describe extracellular localization as predicted and lactose release/mediation
    as the authors’ supported inference, not directly measured flux or enzyme activity.
  - Retain the measured donor-dependent growth/enrichment results and distinguish
    total OD, composition and molecular mediation.
  - Replace universal 2′FL/HMO/lactose medium requirements with the specific tested
    substrate contexts; do not require addition of both substrate and proposed product.
  - Keep literal source quotations intact while qualifying their explanations against
    main Results and SI; retain all six bounded nodes and four PARTIAL arrows.
- action_id: repair-assay-context
  description: Separate culture contexts and document the endpoint discrepancy.
  finding_ids:
  - assay-context
  target_ids:
  - CommunityMech:000220
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    role: canonical_record
  acceptance_checks:
  - Separate community serial passages, FT-1 isolate mono/cocultures and PT-1 donor
    supplementation; attach each volume, vessel, temperature and schedule only to
    its supported assay.
  - Add source-backed growth-media entries for the focal pair and relevant community
    contexts, including the distinct precultures and individual sugar treatments;
    do not invent an exact CultureMech recipe match.
  - Preserve the verbatim 144 h Methods quotation and explicitly record that Figure
    4 pixels, caption and Source Data use 168 h; do not silently claim a resolved
    author correction.
  - Retain fecal inoculum provenance separately from the physical laboratory culture
    environment and modeled infant habitat; verify any replacement ontology grounding
    before applying it.
  - Keep FT-1 isolate and PT-1 recipient context explicit without inventing collection-strain
    codes, pairwise vessel volume or universal abundance.
- action_id: repair-lactose-anomer
  description: Use evidence-matched lactose specificity.
  finding_ids:
  - lactose-anomer
  target_ids:
  - CommunityMech:000220
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    role: canonical_record
  acceptance_checks:
  - Use verified generic lactose CHEBI:17716 for the proposed released mediator unless
    direct anomer-specific evidence is supplied.
  - Keep reagent identity distinct from the inferred coculture product; a control-reagent
    specification does not establish the released anomer.
  - Preserve the graph’s existing generic lactose grounding and rerun term/reference
    checks after authorized correction.
- action_id: repair-archive-links
  description: Add the source-linked datasets with their correct provenance.
  finding_ids:
  - archive-links
  target_ids:
  - CommunityMech:000220
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    role: canonical_record
  acceptance_checks:
  - Link manuscript-related MAG deposit Figshare 22320865 with its verified version
    and metadata scope; distinguish earlier reference collection Figshare 13667816.
  - Record the original sample mappings FT-1 SRS8184257/SAMN17763864/L2_031_090G1,
    FT-2 SRS8184183/SAMN17764164/L3_130_056G1 and PT-1 SRS8184427/SAMN17764012/L3_069_015G1
    with source evidence.
  - Do not label these original stool samples as pure-culture genomes or certify uninspected
    archive contents, raw reads or accession ranges.
- action_id: preserve-qualified-graph
  description: Preserve the six qualified nodes and four PARTIAL arrows during separately
    authorized follow-up.
  finding_ids:
  - mechanism-prose
  - assay-context
  - lactose-anomer
  - archive-links
  target_ids:
  - CommunityMech:000220
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Ruminococcus_Infant_HMO_CrossFeeding.yaml
    role: canonical_record
  acceptance_checks:
  - Keep genomic potential, total OD, relative composition, donor supplementation
    and inferred molecular mediation distinct.
  - Do not turn the conceptual infant-feeding figure into an in-vivo trial or impose
    the FT-1 pair on every donor community.
  - Preserve append-only history and rerun schema, strict, term, reference, history
    and target/corpus network checks after authorized curation.
limitations:
- No raw sequences, genome/annotation pipelines, growth statistics or molecular flux
  were reanalyzed. Archive metadata and listings do not certify payload contents.
- Source Data inspection covers all Figure 4 time/condition/culture columns and 18
  composition rows plus workbook inventory; other sheets were not read row by row.
  Reporting-summary and peer-review contents were not assessed.
- Methods state 144 h while Figure 4 pixels, caption and Source Data report 168 h;
  no author correction or resolved replacement protocol is asserted.
- The inferred released lactose anomer, direct transfer flux and enzyme necessity
  remain unmeasured in the inspected main/SI. A supplied reagent specification would
  not establish the released product’s anomer.
- The pair’s vessel/working volume and an exact CultureMech recipe equivalent are
  not independently resolved. Community settings and catalogue/reference genomes must
  not be transferred to that assay without source support.
- Existing GTDB mappings passed native checks; historical mapping-release statistics
  were not re-certified or replaced.
notes:
- No canonical, cache, history or generated file changed.
- All 24 repository inputs were pinned before assessment and rechecked.
- Eighteen quoted words from the focal publication, including the total budget for
  its supplements.
- Native quality 100 is capped from 119; source findings remain actionable.
tags:
- record-review
- gut-coculture
- hmo
- cross-feeding
- batch-06
```
