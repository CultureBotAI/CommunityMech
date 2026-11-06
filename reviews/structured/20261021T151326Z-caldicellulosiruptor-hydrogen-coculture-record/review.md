# Caldicellulosiruptor two-species hydrogen coculture review

- Review: 20261021T151326Z-caldicellulosiruptor-hydrogen-coculture-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T15:06:17.184717Z
- Finished UTC: 2026-10-21T15:13:26.514580Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full main, figures and supplements support the exact pair and the qualified three-node, one-arrow graph. One major finding concerns unsupported trophic roles; two minor findings concern recoverable assay/model context and hydrogen condition/outcome scope. Observed growth stimulation remains distinct from nutrient transfer and modeled coexistence.

## Scope And Provenance

Whole canonical record and every node/arrow assessed using direct primary main, tables, figures, supplements, bounded authority/archive evidence and actual native checks.

Selection: Only released CommunityMech:000185 in the owned batch 09 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f491097e6f3cd52baf6c2e89b3e614756ebce558.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000185 | kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml | maintained | Caldicellulosiruptor Two-Species Hydrogen Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000185 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000185 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000185 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000185 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000185 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000185 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000185 | Read-only cache-name preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000185 | Reference validation passed against the pinned abstract cache. |
| audit-network | failed | True | CommunityMech:000185 | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000185 | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |
| Primary scientific review | passed | True | CommunityMech:000185 | Full main, all five main tables, all six figures and both scientific supplements assessed against every current node and arrow. |
| Strain and genome identity | passed | True | CommunityMech:000185 | Direct source, catalogue and archive metadata verify the exact strains and isolate reference genomes. |
| Source-linked scientific supplements | passed | True | CommunityMech:000185 | S1 and all eight S2 tables read; source file identity and checksums verified. |
| Earlier exact-pair full paper | skipped | False | CommunityMech:000185 | Bibliographic identity and direct institutional abstract inspected; no full-paper certification or borrowed quantitative comparison. |
| Earlier DSM 640 base formulation | skipped | False | CommunityMech:000185 | The cited precursor recipe was not fully reviewed; only current-source conditions and modifications are certified. |
| Numerical model reproduction | skipped | False | CommunityMech:000185 | No execution, parameter refitting or correction of the printed sign discrepancy. Model evidence remains hypothetical. |
| Optional structured expression adapter | unavailable | False | CommunityMech:000185 | No applicable expression-module evidence established through explicitly reused bounded runtime discovery. |

## Scientific And Domain Assessments

### Exact two-strain community and current taxonomy

identity: supported. Targets: CommunityMech:000185.

Retain DSM 8903 and DSM 12137/I77R1B with source names separated from current canonical labels.

### State, origin, category and engineering design

scope: supported. Targets: CommunityMech:000185.

Retain ENGINEERED, SYNTHETIC and BIOTECHNOLOGY.

The source deliberately assembles known strains in a controlled reactor. The engineered state remains appropriate even though experimental coexistence is stable. Optional ecological_state does not require a replacement, and no genetic engineering is implied.

### taxonomy[0:2].functional_role and membership evidence

evidence: concern. Targets: CommunityMech:000185.

Flat CROSS_FEEDER assignments are unsupported; generic fermentation does not by itself establish SECONDARY_FERMENTER.

The donor and treated recipient are known, but no recipient role is demonstrated for the donor and nutrient utilization by the treated strain is unresolved. Omit unsupported role enums unless claim-specific evidence satisfies their definitions. Retain the measured donor-to-recipient growth response untyped. Do not invent a requirement that a primary degrader must be another species.

### ecological_interactions[0]: Stable Chemostat Coexistence

graph: supported. Targets: CommunityMech:000185.

Retain coexistence as an observed reactor outcome with the current mechanistic limits.

Both named strains persist under reported continuous regimes, including glucose-only limitation. Changing abundance ratios do not identify niche partitioning or establish that coexistence causes higher hydrogen yield.

### ecological_interactions[1]: Growth-Supernatant Enhancement

graph: supported. Targets: CommunityMech:000185.

Retain the directional batch growth response without cross-feeding or reciprocal-fitness typing.

C. saccharolyticus is the supernatant donor and C. kristjanssonii the treated recipient. Shorter lag and about 18% greater maximum biomass are supported; maximum specific growth rate is unchanged within the reported comparison. The compound, nutritional mechanism and secretion-versus-lysis source remain unknown.

### ecological_interactions[1].downstream[0]

graph: supported. Targets: CommunityMech:000185.

Retain only the HYPOTHESIZED stimulation-to-coexistence edge.

The model assumes effects on both recipient growth rate and biomass yield, while the batch experiment supports only part of that mechanism. The current arrow does not assert necessity or measured nutrient transfer. Source parameter guesses and the printed equation discrepancy limit model certification; neither creates a new demonstrated biological edge.

### ecological_interactions[2]: Enhanced Glucose-Limited Hydrogen Yield

graph: concern. Targets: CommunityMech:000185.

The endpoint description is sound; its metabolite list and evidence should match the glucose-only comparison.

Retain 3.7 mol H2/mol glucose at dilution 0.06/h and the distinction between yield and productivity. Xylose and the mixed-feed excerpt belong to a different experimental condition and should not imply xylose supplied this specific yield comparison. Acetate and fermentation are supported in the primary tables.

### growth_media[0], cultivation_setup[0] and model evidence context

completeness: concern. Targets: CommunityMech:000185.

Replace the obsolete unfetched-Methods boundary with available source-specific conditions and model provenance.

Preserve the existing rate-range caveat while recording exact temperature, pH, volume, mixing, gas and inoculum details. Separate mixed-feed, glucose-only, xylose-only and supernatant batch assays. Add computational provenance to model support without relabeling the measured growth phenotype as wholly computational.

### related_ingredients[0:3] and environmental_factors[2]

evidence: concern. Targets: CommunityMech:000185.

Glucose, xylose and dihydrogen identities are sound; the comparative yield statement and outcome placement need narrower scope.

The focal monoculture comparison is glucose-only. Mixed-sugar conversion is separately established but does not inherit the superiority comparison. The value 3.7 mol/mol is an outcome; glucose limitation and dilution rate are conditions. Preserve these conditions while placing the measured yield with the interaction endpoint.

### Strain genomes, S2 phenotype data and earlier publication

provenance: supported. Targets: CommunityMech:000185.

Retain the verified strain-reference projects and genuine supplementary fermentation dataset.

The genomic projects are isolate references rather than sequencing of the mixed coculture. The descriptive S2 locator can be supplemented with its direct asset URL, without inventing a registered accession or creating a data-absence finding. Earlier-paper bibliographic/abstract verification does not certify its full methods or transfer compost-community outcomes.

### Prior decisions, source cache and unresolved mechanism

provenance: supported. Targets: CommunityMech:000185.

Preserve the qualified graph and previous removed coexistence-to-yield arrow.

The original cache is abstract-only and remains unchanged. New main/SI inspection supports current-claim completion but does not silently promote prior reviews, close issues or append curation history.

### Native and authority checks

schema: supported. Targets: CommunityMech:000185.

All eight focused native checks pass; one major and two minor source-specific findings remain.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000185.

Mechanical completeness does not establish scientific adequacy.

## Findings

### functional-role-scope: Remove unsupported trophic-role assignments

major / open / confirmed; issue key: cm-000185-functional-role-scope.

Both taxa are assigned CROSS_FEEDER and SECONDARY_FERMENTER using membership excerpts. Donor-supernatant growth stimulation establishes neither reciprocal recipient status nor metabolite nutrition; supplied-sugar fermentation alone does not establish a primary-degrader-product trophic role.

### assay-model-context: Recover the available assay and model context

minor / open / confirmed; issue key: cm-000185-assay-model-context.

Cultivation notes still say working volume, temperature and the full dilution range remain unfetched. The full source supplies these and distinct feed, inoculum and gas regimes, plus a separately modeled explanation with assumed parameters.

### hydrogen-condition-scope: Keep hydrogen yield claims within their measured condition

minor / open / confirmed; issue key: cm-000185-hydrogen-condition-scope.

The hydrogen ingredient generalizes superiority to glucose and xylose, while the focal monoculture comparison is glucose-only. The glucose-limited node retains xylose/mixed-feed evidence, and an environmental-factor value stores a measured yield rather than an environmental condition.

## Recommended Actions And Acceptance Checks

### repair-functional-roles

Represent observed fermentation and directional stimulation without unsupported trophic enums.

- Omit both flat CROSS_FEEDER assignments unless separate claim-specific evidence establishes utilization of another taxon’s metabolites. Simply labeling the observed supernatant response proposed does not demonstrate that enum’s utilization relation. Keep the experimentally known donor and treated recipient and their untyped growth response.
- For each SECONDARY_FERMENTER assignment, require source-specific support for fermentation of products from primary degraders; supplied glucose/xylose fermentation and membership excerpts alone are insufficient. The schema does not require a different species as that degrader. Omit the enum if its narrower trophic scope cannot be supported, while retaining supported sugar-fermentation prose.
- Functional roles are optional. Do not force PRIMARY_DEGRADER or invent a generic fermenter enum as a substitute. Preserve strain identities, current NCBI/GTDB mapping, the three qualified nodes and the single HYPOTHESIZED arrow.
- Attach exact evidence to each retained claim. Do not add reciprocal fitness, named metabolites, secretion, nutrient uptake or mechanistic necessity from the supernatant experiment.

### recover-assay-model-context

Replace obsolete source-access gaps with scoped experimental conditions and separately labeled model provenance.

- Record source-reported modified DSM 640 with yeast extract 1 g/L, 70 ± 1 °C, pH 6.7 ± 0.1, a 3 L stirred reactor with 1 L working volume, 300 rpm and nitrogen sparging at 100 mL/min with less than 5 ppm oxygen. Preserve pH control with 3 M NaOH. Do not copy catalogue maintenance media or reconstruct the unread precursor recipe.
- Describe the twice-subcultured inocula, OD620 0.3–0.4, total 15% inoculum with equal strain volumes, and batch start-up followed by continuous operation. Scope initial cysteine hydrochloride 1 g/L separately from its omission in continuous feed; do not apply the supernatant batch-inoculum variants to all chemostats.
- Separate 10 g/L total mixed sugar (1:1; dilution 0.04–0.30/h), 4 g/L total mixed sugar (1:1), glucose-only 4 g/L and xylose-only 4 g/L comparisons at 0.06 and 0.15/h. Preserve condition-specific residual-sugar and steady-state criteria instead of one universal feed or limitation claim.
- Add computational provenance for the ODE model and MATLAB R2009a to model-specific evidence or an appropriate separate evidence item, retaining measured batch evidence as experimental. Distinguish assumed/guessed S1 parameters from measured values and note the unresolved printed equation sign; do not claim model reproduction.
- Remove stale statements that these Methods remain unfetched. Following separately authorized curation, run the focused schema, strict, terms, references, GTDB/domain and history checks; do not edit caches or schema merely to make new source evidence pass.

### scope-hydrogen-endpoint

Synchronize ingredient, node and condition representations with the glucose-only yield comparison.

- Restrict the superior-yield statement to the demonstrated 4 g/L glucose-only comparison: 3.7 mol H2/mol glucose at dilution 0.06/h versus 3.5 for each monoculture. Keep mixed-sugar and xylose-only production as separately scoped observations; earlier-paper abstract verification does not supply an unreviewed comparative result.
- Remove or clearly separate xylose and mixed-feed evidence from the glucose-limited yield node. Preserve glucose, measured hydrogen and acetate, the valid fermentation annotation, and the distinction between molar yield, specific production rate and volumetric productivity.
- Move the 3.7 mol/mol yield outcome out of environmental_factors, preserving it in the existing phenotype node. If retaining an environmental entry, encode glucose limitation and dilution 0.06/h as conditions with narrow evidence rather than using yield as the condition value.
- Do not restore the removed coexistence-to-yield edge or infer reciprocal fitness. Preserve S2’s hexose-equivalent denominator where relevant, replicate scope and the absence of a new statistical analysis.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml; Entire canonical record, including three nodes and one arrow | supports | The record represents the exact engineered two-strain hydrogen-producing coculture. Its current graph distinguishes observed coexistence, donor-supernatant growth stimulation and glucose-limited hydrogen yield; only the stimulation-to-coexistence link is hypothesized. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=21192828&amp;retmode=xml; Article identity and metadata | supports | Direct article metadata and abstract identify the focal paper and supply all 23 existing excerpts: 22 abstract spans and one title span. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21192828%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article identity and metadata | supports | Article identity and open full-text availability agree with PMID 21192828, PMC3022713 and DOI 10.1186/1475-2859-9-102. |
| crossref | https://api.crossref.org/works/10.1186/1475-2859-9-102; Article identity and metadata | supports | The DOI metadata identifies the same primary publication. |
| identity | PMID:21192828; Methods: Microorganisms; Background; study objective | supports | The focal pair is C. saccharolyticus DSM 8903 (ATCC 43494) and source-named C. kristjanssonii I77R1B (DSM 12137; ATCC 700853). The latter exact strain is currently classified as C. acetigenus. Preserve the paper name separately from current authority labels; this is not a different isolate. |
| roles | PMID:21192828; Methods: substrates and supernatant preparation; Results: growth stimulation; Discussion: mechanism alternatives | supports | Both strains ferment supplied glucose and/or xylose. The experiment transfers C. saccharolyticus cell-free supernatant to C. kristjanssonii; it does not test a reciprocal recipient role for C. saccharolyticus. The active material could signal or originate from lysis, and nutrient utilization is not established for the treated recipient. Membership, sugar fermentation and a growth response do not establish both encoded trophic roles. |
| coexistence | PMID:21192828; Results: mixed-sugar continuous culture, glucose limitation and species-specific qPCR; Figures 1–4 | supports | Both strains coexist during the reported 70-day continuous experiment and under single-substrate limitation; species ratios change with dilution rate and feed condition. This supports the existing persistence node without identifying a nutrient exchange, niche-partitioning mechanism or causal effect on hydrogen yield. |
| stimulation | PMID:21192828; Results: cell-free-supernatant batch test; Figure 6; Discussion | supports | Donor supernatant shortens the treated strain’s lag and raises maximum biomass by about 18%; maximum specific growth rate does not significantly change. C. saccharolyticus is the observed supernatant donor and C. kristjanssonii the treated recipient. Those experimental identities do not establish recipient CROSS_FEEDER roles or reciprocal nutrition. |
| model | PMID:21192828; Methods: Co-culture model; equations 1–8; Results: model; Figure 5; Discussion | supports | An ordinary-differential-equation model implemented in MATLAB R2009a assumes an unidentified compound proportional to donor biomass that enhances recipient growth rate and biomass yield. Its agreement with coexistence patterns is an explanatory hypothesis; the batch assay supports only part of that mechanism, not necessity in continuous culture. |
| cultivation | PMID:21192828; Methods: Inoculum development; Bioreactor setup; steady-state definition | supports | Modified DSM 640 with yeast extract 1 g/L (main Tables 2–5) is used at 70 ± 1 °C and pH 6.7 ± 0.1 in a 3 L stirred reactor with 1 L working volume, 300 rpm and nitrogen sparging at 100 mL/min with less than 5 ppm oxygen. Twice-subcultured inocula reach OD620 0.3–0.4; total inoculum is 15% by volume with equal volumes of the two strains. Initial cysteine hydrochloride is 1 g/L and is omitted from continuous feed. These are source conditions, not catalogue maintenance settings. |
| feed-regimes | PMID:21192828; Methods and Results; main Tables 2–5; supplementary fermentation tables | supports | Separate the 10 g/L total glucose/xylose feed (1:1, dilution 0.04–0.30/h) from the 4 g/L mixed feed (1:1), glucose-only 4 g/L and xylose-only 4 g/L comparisons at 0.06 and 0.15/h. The 10 g/L mixed-feed experiment remains carbon-sufficient; the lower-feed comparisons have condition-specific residual sugars. Do not turn glucose growth limitation into proof that no other medium nutrients exist. |
| hydrogen | PMID:21192828; Results: Competition for one growth-limiting substrate; main Table 4; Additional file 2 Table S4.2 | supports | At 4 g/L glucose and dilution 0.06/h, coculture hydrogen yield is 3.7 mol/mol glucose versus 3.5 for each monoculture; at 0.15/h it is 3.5 versus 3.1 and 3.0. This is a glucose-only comparison of yield, not universal mixed-sugar superiority, volumetric productivity or reciprocal fitness. |
| supplement-parameters | PMID:21192828; Additional file 1: entire S1 parameter table and explanatory footnote | supports | The glucose-affinity and compound-related parameters are explicitly guessed rather than experimentally determined. Source-dependent measured or earlier-study parameters remain distinct. No parameter fitting or model execution was performed. |
| supplement-data | PMID:21192828; Additional file 2: all eight fermentation tables, S2.1–S5.2 | supports | The tables distinguish 10 g/L mixed sugar, 4 g/L mixed sugar, 4 g/L glucose-only monoculture/coculture comparisons and 4 g/L xylose-only coculture. Product yields use mol per mol C6 equivalents. Replicated tables report two independent cultures and standard deviations; no new significance test or conversion to a different denominator was made. |
| publisher-equations | https://link.springer.com/article/10.1186/1475-2859-9-102; Publisher HTML equations 7–8, compared with S1 and enhancement narrative | supports | Both publisher HTML and XML print a minus sign before the enhanced-minus-baseline term, while S1 enhanced values exceed baseline and the narrative describes enhancement. This unresolved source-model discrepancy is not a new encoded-record defect; no model reproduction or corrected equation is certified. |
| figures | PMID:21192828; All six main JPG images and captions; S1 page 1 and S2 page 3 layouts | supports | Figures 1–4 show condition-dependent species ratios, Figure 5 simulated trajectories and Figure 6 supernatant growth response. Figure 1 displays dilution rates only through 0.25/h although text/tables also report 0.30/h. No bar digitization, raw-data analysis or fresh statistical calculation was performed. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity; TaxonomicComposition.functional_role; FunctionalRoleEnum; EnvironmentalFactor; ComputationalProvenance | supports | CROSS_FEEDER denotes utilization of metabolites from other taxa. SECONDARY_FERMENTER denotes fermentation of products from primary degraders, without requiring a different species as that degrader. Functional roles and ecological_state are optional. Environmental factors describe conditions rather than yield outcomes; computational provenance can separate model assumptions and software from experimental evidence. |
| ontology | ontology-authority.json; Whole bounded frozen receipt | supports | All nine distinct encoded ID-label pairs match local OAK across 23 occurrences. Current NCBI terms are strain rank; chemical and GO labels are valid. |
| semantics | ontology-semantic-notes.json; Whole bounded frozen receipt | supports | Semantic checks preserve exact strain identity, conditional mechanism interpretation and the distinction between generic sugar fermentation and trophic-role claims. |
| catalogues | child-strain-authority.json; Whole bounded frozen receipt | supports | Direct DSMZ catalogue and linked LPSN evidence verify both DSM/ATCC pairs and the current C. acetigenus classification of DSM 12137/I77R1B. No catalogue maintenance conditions are imported. |
| gtdb | child-gtdb-mapping-check.json; Whole bounded frozen receipt | supports | Exact local crosswalk rows agree with both encoded species mappings, lineages, fractions 1.0 and genome counts 2 and 4. The legacy release-latest wording is not a newly verified numbered release. |
| resources | dataset-verification.json; Whole bounded frozen receipt | supports | The two isolate reference-genome projects and chromosome accessions match their exact strains. The actual S2 phenotype asset is verified; its PMID-derived accession is a descriptive locator, not a registered archive identifier. Earlier DOI identity and institutional abstract are bounded separately. |
| snippets | snippet-audit.json; Whole bounded frozen receipt | supports | All 23 excerpts match direct PubMed and the pinned abstract cache: 22 abstract spans plus one title. The full XML has separate typography-sensitive coverage; no unmatched unit rendering is called fabricated evidence. |
| history | provenance-audit.json; Whole bounded frozen receipt | supports | The exact historical row and sidecar preserve the prior graph repairs. Current issue 1270 also covers another record, issue 516’s earlier species-attribution error at high dilution is already repaired, and broader issue 1268 is context only. No issue is closed by this review. |
| native-target | support-audit.json; Whole bounded frozen receipt | supports | Native graph COMPLETE: three nodes, one arrow and six node-evidence entries. Completeness 100 and quality 100 after capping describe fields and diagnostics, not scientific truth. |
| source-scope | source-audit.json; Whole bounded frozen receipt | supports | Whole-record source assessment supports one major role-scope finding and two minor context/condition findings. Full primary main, six figures and both scientific supplements were inspected; earlier-paper and model-reproduction limits remain explicit. |
| lead-read | lead-primary-read-scope.json; Whole bounded frozen receipt | supports | Pins full scientific-main and table reading, all six main image views, full S1/S2 text and critical supplement layout views. |
| independent-source | root-independent-source-audit.json; Whole bounded frozen receipt | supports | Root independently assessed the full main, all six figures, S1 and all eight S2 tables and concurs with the final finding groups and boundaries. |
| auxiliary | auxiliary-frozen-manifest.json; Whole bounded frozen receipt | supports | Child-owned native, authority and adapter receipts are immutable and independently pinned; no shared-filename overwrite was performed. |
| earlier-publication | doi:10.1016/j.ijhydene.2008.07.092; Directly opened Lund University publication abstract and bibliographic identity | supports | The earlier paper includes this exact pair, but its highlighted high hydrogen rates belong to C. saccharolyticus plus enriched compost microflora. Only the abstract and identity were inspected; it does not supply an independently reviewed mixed-sugar superiority comparison for this pair. |
| access-fulltext | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3022713/fullTextXML; Preserved actual access receipt | supports | The direct Europe PMC response contains the full primary XML. |
| access-publisher | https://microbialcellfactories.biomedcentral.com/articles/10.1186/1475-2859-9-102; Preserved actual access receipt | supports | The publisher response contains the primary article and equations. |
| access-supplement-zip | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3022713/supplementaryFiles; Preserved actual access receipt | supports | The direct supplement archive contains all six main images and both source-linked scientific PDFs; assets were safely extracted and their identity checked. |
| adapter | adapter-check.json; Verified same-runtime optional adapter discovery reuse | supports | The child explicitly reuses bounded batch 09 runtime discovery with its original timestamp and hashes. No applicable expression-module evidence is established; this is not negative biological evidence. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml; Actual execution 2026-10-21T15:08:14.394838+00:00 to 2026-10-21T15:08:15.159134+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-strict kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml --out /private/tmp/cm-review-session/batch-09/000185/strict-report.tsv; Actual execution 2026-10-21T15:08:14.395065+00:00 to 2026-10-21T15:08:16.462545+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-terms kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml; Actual execution 2026-10-21T15:08:14.395140+00:00 to 2026-10-21T15:08:16.107540+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-gtdb kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml; Actual execution 2026-10-21T15:08:15.159503+00:00 to 2026-10-21T15:08:15.238899+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-gtdb-domain kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml; Actual execution 2026-10-21T15:08:15.239152+00:00 to 2026-10-21T15:08:16.520459+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-history history/records/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture; Actual execution 2026-10-21T15:08:16.107826+00:00 to 2026-10-21T15:08:16.862576+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T15:08:16.863094+00:00 to 2026-10-21T15:08:16.914058+00:00 | supports | Read-only cache-name preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-references-explained kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml; Actual execution 2026-10-21T15:08:16.914350+00:00 to 2026-10-21T15:08:17.967335+00:00 | supports | Reference validation passed against the pinned abstract cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T14:53:06.814378+00:00 to 2026-10-21T14:53:14.616064+00:00 | supports | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T14:53:06.817734+00:00 to 2026-10-21T14:53:14.704428+00:00 | supports | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |

## Limits And Additional Notes

- No raw genome sequencing, genome reannotation, new statistical tests, model rerun or parameter refitting. Existing experimental and model outputs are assessed as reported.
- The earlier exact-pair DOI was verified only through bibliographic metadata and a directly opened institutional abstract. Its high production rates concern a different compost-microflora coculture; no transfer to this pair is made.
- Modified DSM 640 is source-reported, but its cited precursor full recipe was not independently reviewed. Source-reported modifications and reactor conditions may be recovered without inventing salts or an exact CultureMech mapping.
- S1 glucose-affinity and compound parameters are explicitly estimated guesses. Publisher and XML equations 7–8 contain a sign inconsistent with the enhancement narrative and S1 parameter ordering. The model has not been reproduced or corrected; its hypothesized explanatory scope is retained.
- Donor supernatant stimulation does not resolve metabolite nutrition versus signaling, secretion versus lysis, reciprocal transfer or mechanistic necessity. No named exchange compound or reciprocal fitness benefit is inferred.
- Figure 1 plots dilution rates through 0.25/h, whereas the experiment text and tables include 0.30/h. These source representations are not silently treated as identical.
- Reference genomes identify the two cultured strains; they are not mixed-coculture sequencing. Catalogue maintenance conditions are not the focal protocol.
- Current completion covers all encoded claims with full main, figures and critical SI. It does not certify every earlier paper, the precursor recipe, raw data or model reproducibility.
- No canonical, cache, history, generated or saved-review files changed; all 23 inspected inputs remain pinned.
- All 23 existing excerpts match direct PubMed and the abstract-only cache: 22 abstract spans and one title. Full XML coverage differs for three typographic unit renderings; no body-only literal support is implied by abstract matching.
- Completeness 100 and quality 100 (raw 121) are native mechanical scores, not scientific certification.
- No raw sequence/statistical reanalysis, model execution, paid provider, author contact or later-target review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T151326Z-caldicellulosiruptor-hydrogen-coculture-record
kind: record
repository: CultureBotAI/CommunityMech
title: Caldicellulosiruptor two-species hydrogen coculture review
started_at: '2026-10-21T15:06:17.184717Z'
finished_at: '2026-10-21T15:13:26.514580Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, native/ontology checks
    and supporting provenance; no person-level independence is asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Full main, figures and supplements support the exact pair and the qualified
  three-node, one-arrow graph. One major finding concerns unsupported trophic roles;
  two minor findings concern recoverable assay/model context and hydrogen condition/outcome
  scope. Observed growth stimulation remains distinct from nutrient transfer and modeled
  coexistence.
source:
  git_revision: f491097e6f3cd52baf6c2e89b3e614756ebce558
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
  - path: history/records/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture/2026-10-05T155420Z-codex-7daebc.yaml
    sha256: 4beec92a637182af22694f330c1e20bfa505b869000be47f400f6dd96ceaf320
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
    sha256: 8151dfbdf8e248288fbc2f31cc2a53bd770fb5bf34d1239538a2cb3e1b7ba990
    role: target
  - path: references_cache/PMID_21192828.md
    sha256: 6748b12408ca35c54d2962f2ec5bbe357b9cf5bdbc0ff8104a2ab56461fe2e9a
    role: context
  - path: reports/causal_graph_review/decisions/20261005-thermophile-pair-batch9.yaml
    sha256: 2e3b83e265ad0016f87051af9e80d4f825f78eeeebf9b29192e27e9c3675424f
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
- target_id: CommunityMech:000185
  path: kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  label: Caldicellulosiruptor Two-Species Hydrogen Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
    role: canonical_record
scope:
  description: Whole canonical record and every node/arrow assessed using direct primary
    main, tables, figures, supplements, bounded authority/archive evidence and actual
    native checks.
  selection: Only released CommunityMech:000185 in the owned batch 09 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000185
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000185
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, molecular exchange or condition-specific scientific support.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000185
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-strict kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-09/000185/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, molecular exchange or condition-specific scientific support.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000185
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-terms kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, molecular exchange or condition-specific scientific support.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000185
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, molecular exchange or condition-specific scientific support.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000185
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb-domain kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, molecular exchange or condition-specific scientific support.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000185
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-history history/records/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, molecular exchange or condition-specific scientific support.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-name preflight passed.
  target_ids:
  - CommunityMech:000185
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, molecular exchange or condition-specific scientific support.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned abstract cache.
  target_ids:
  - CommunityMech:000185
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-references-explained kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, molecular exchange or condition-specific scientific support.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities;
    the focal graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000185
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse; existing corpus warnings are
    not concealed or attributed to this focal record.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities;
    the focal graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000185
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse; existing corpus warnings are
    not concealed or attributed to this focal record.
- check_id: scientific-source
  name: Primary scientific review
  status: passed
  required: true
  summary: Full main, all five main tables, all six figures and both scientific supplements
    assessed against every current node and arrow.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - source-scope
  - independent-source
  - lead-read
- check_id: strain-resources
  name: Strain and genome identity
  status: passed
  required: true
  summary: Direct source, catalogue and archive metadata verify the exact strains
    and isolate reference genomes.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - catalogues
  - resources
  - gtdb
- check_id: supplements
  name: Source-linked scientific supplements
  status: passed
  required: true
  summary: S1 and all eight S2 tables read; source file identity and checksums verified.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - supplement-parameters
  - supplement-data
  - resources
- check_id: earlier-full-paper
  name: Earlier exact-pair full paper
  status: skipped
  required: false
  summary: Bibliographic identity and direct institutional abstract inspected; no
    full-paper certification or borrowed quantitative comparison.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - earlier-publication
  - resources
- check_id: precursor-medium
  name: Earlier DSM 640 base formulation
  status: skipped
  required: false
  summary: The cited precursor recipe was not fully reviewed; only current-source
    conditions and modifications are certified.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - cultivation
  - source-scope
- check_id: model-reproduction
  name: Numerical model reproduction
  status: skipped
  required: false
  summary: No execution, parameter refitting or correction of the printed sign discrepancy.
    Model evidence remains hypothetical.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - model
  - supplement-parameters
  - publisher-equations
- check_id: structured-adapter
  name: Optional structured expression adapter
  status: unavailable
  required: false
  summary: No applicable expression-module evidence established through explicitly
    reused bounded runtime discovery.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  locator: Entire canonical record, including three nodes and one arrow
  summary: The record represents the exact engineered two-strain hydrogen-producing
    coculture. Its current graph distinguishes observed coexistence, donor-supernatant
    growth stimulation and glucose-limited hydrogen yield; only the stimulation-to-coexistence
    link is hypothesized.
  support: supports
  accessed_at: '2026-10-21T15:13:26.507592Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=21192828&retmode=xml
  locator: Article identity and metadata
  summary: 'Direct article metadata and abstract identify the focal paper and supply
    all 23 existing excerpts: 22 abstract spans and one title span.'
  support: supports
  accessed_at: '2026-10-21T15:06:42.085409Z'
  snapshot_sha256: d2eb85e853585bf19ae47f21734337a126b09982fbb436007e08306f02c9fe1d
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:21192828%20AND%20SRC:MED&format=json&resultType=core
  locator: Article identity and metadata
  summary: Article identity and open full-text availability agree with PMID 21192828,
    PMC3022713 and DOI 10.1186/1475-2859-9-102.
  support: supports
  accessed_at: '2026-10-21T15:06:42.377782Z'
  snapshot_sha256: 3e144b6f2cea817403f871b2ad27998acb737f9ed172a404244acf4b34b437fb
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1186/1475-2859-9-102
  locator: Article identity and metadata
  summary: The DOI metadata identifies the same primary publication.
  support: supports
  accessed_at: '2026-10-21T15:06:42.043866Z'
  snapshot_sha256: b02ad764caaa51b572c299c436c5ac17c9a3bc095e8382ecef532b40564f74ca
- evidence_id: identity
  kind: primary_source
  reference: PMID:21192828
  locator: 'Methods: Microorganisms; Background; study objective'
  summary: The focal pair is C. saccharolyticus DSM 8903 (ATCC 43494) and source-named
    C. kristjanssonii I77R1B (DSM 12137; ATCC 700853). The latter exact strain is
    currently classified as C. acetigenus. Preserve the paper name separately from
    current authority labels; this is not a different isolate.
  support: supports
  accessed_at: '2026-10-21T15:06:53.313023Z'
  snapshot_sha256: e5fb2df6667be10f6fd9ed50de3bcfc3087de65c11b1d961bdc053b5ad028a23
- evidence_id: roles
  kind: primary_source
  reference: PMID:21192828
  locator: 'Methods: substrates and supernatant preparation; Results: growth stimulation;
    Discussion: mechanism alternatives'
  summary: Both strains ferment supplied glucose and/or xylose. The experiment transfers
    C. saccharolyticus cell-free supernatant to C. kristjanssonii; it does not test
    a reciprocal recipient role for C. saccharolyticus. The active material could
    signal or originate from lysis, and nutrient utilization is not established for
    the treated recipient. Membership, sugar fermentation and a growth response do
    not establish both encoded trophic roles.
  support: supports
  accessed_at: '2026-10-21T15:06:53.313023Z'
  snapshot_sha256: e5fb2df6667be10f6fd9ed50de3bcfc3087de65c11b1d961bdc053b5ad028a23
- evidence_id: coexistence
  kind: primary_source
  reference: PMID:21192828
  locator: 'Results: mixed-sugar continuous culture, glucose limitation and species-specific
    qPCR; Figures 1–4'
  summary: Both strains coexist during the reported 70-day continuous experiment and
    under single-substrate limitation; species ratios change with dilution rate and
    feed condition. This supports the existing persistence node without identifying
    a nutrient exchange, niche-partitioning mechanism or causal effect on hydrogen
    yield.
  support: supports
  accessed_at: '2026-10-21T15:06:53.313023Z'
  snapshot_sha256: e5fb2df6667be10f6fd9ed50de3bcfc3087de65c11b1d961bdc053b5ad028a23
  quote: over a period of 70 days
- evidence_id: stimulation
  kind: primary_source
  reference: PMID:21192828
  locator: 'Results: cell-free-supernatant batch test; Figure 6; Discussion'
  summary: Donor supernatant shortens the treated strain’s lag and raises maximum
    biomass by about 18%; maximum specific growth rate does not significantly change.
    C. saccharolyticus is the observed supernatant donor and C. kristjanssonii the
    treated recipient. Those experimental identities do not establish recipient CROSS_FEEDER
    roles or reciprocal nutrition.
  support: supports
  accessed_at: '2026-10-21T15:06:53.313023Z'
  snapshot_sha256: e5fb2df6667be10f6fd9ed50de3bcfc3087de65c11b1d961bdc053b5ad028a23
  quote: enhance the growth of C. kristjanssonii
- evidence_id: model
  kind: primary_source
  reference: PMID:21192828
  locator: 'Methods: Co-culture model; equations 1–8; Results: model; Figure 5; Discussion'
  summary: An ordinary-differential-equation model implemented in MATLAB R2009a assumes
    an unidentified compound proportional to donor biomass that enhances recipient
    growth rate and biomass yield. Its agreement with coexistence patterns is an explanatory
    hypothesis; the batch assay supports only part of that mechanism, not necessity
    in continuous culture.
  support: supports
  accessed_at: '2026-10-21T15:06:53.313023Z'
  snapshot_sha256: e5fb2df6667be10f6fd9ed50de3bcfc3087de65c11b1d961bdc053b5ad028a23
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:21192828
  locator: 'Methods: Inoculum development; Bioreactor setup; steady-state definition'
  summary: Modified DSM 640 with yeast extract 1 g/L (main Tables 2–5) is used at
    70 ± 1 °C and pH 6.7 ± 0.1 in a 3 L stirred reactor with 1 L working volume, 300
    rpm and nitrogen sparging at 100 mL/min with less than 5 ppm oxygen. Twice-subcultured
    inocula reach OD620 0.3–0.4; total inoculum is 15% by volume with equal volumes
    of the two strains. Initial cysteine hydrochloride is 1 g/L and is omitted from
    continuous feed. These are source conditions, not catalogue maintenance settings.
  support: supports
  accessed_at: '2026-10-21T15:06:53.313023Z'
  snapshot_sha256: e5fb2df6667be10f6fd9ed50de3bcfc3087de65c11b1d961bdc053b5ad028a23
- evidence_id: feed-regimes
  kind: primary_source
  reference: PMID:21192828
  locator: Methods and Results; main Tables 2–5; supplementary fermentation tables
  summary: Separate the 10 g/L total glucose/xylose feed (1:1, dilution 0.04–0.30/h)
    from the 4 g/L mixed feed (1:1), glucose-only 4 g/L and xylose-only 4 g/L comparisons
    at 0.06 and 0.15/h. The 10 g/L mixed-feed experiment remains carbon-sufficient;
    the lower-feed comparisons have condition-specific residual sugars. Do not turn
    glucose growth limitation into proof that no other medium nutrients exist.
  support: supports
  accessed_at: '2026-10-21T15:06:53.313023Z'
  snapshot_sha256: e5fb2df6667be10f6fd9ed50de3bcfc3087de65c11b1d961bdc053b5ad028a23
- evidence_id: hydrogen
  kind: primary_source
  reference: PMID:21192828
  locator: 'Results: Competition for one growth-limiting substrate; main Table 4;
    Additional file 2 Table S4.2'
  summary: At 4 g/L glucose and dilution 0.06/h, coculture hydrogen yield is 3.7 mol/mol
    glucose versus 3.5 for each monoculture; at 0.15/h it is 3.5 versus 3.1 and 3.0.
    This is a glucose-only comparison of yield, not universal mixed-sugar superiority,
    volumetric productivity or reciprocal fitness.
  support: supports
  accessed_at: '2026-10-21T15:06:53.313023Z'
  snapshot_sha256: e5fb2df6667be10f6fd9ed50de3bcfc3087de65c11b1d961bdc053b5ad028a23
  quote: H2 yields on glucose exceeded
- evidence_id: supplement-parameters
  kind: primary_source
  reference: PMID:21192828
  locator: 'Additional file 1: entire S1 parameter table and explanatory footnote'
  summary: The glucose-affinity and compound-related parameters are explicitly guessed
    rather than experimentally determined. Source-dependent measured or earlier-study
    parameters remain distinct. No parameter fitting or model execution was performed.
  support: supports
  accessed_at: '2026-10-21T15:13:26.509448Z'
  snapshot_sha256: e10c0d64e25d78ec02610e6027e4b3e46ebd080389cd5079f332d1ddf0f7ba46
- evidence_id: supplement-data
  kind: primary_source
  reference: PMID:21192828
  locator: 'Additional file 2: all eight fermentation tables, S2.1–S5.2'
  summary: The tables distinguish 10 g/L mixed sugar, 4 g/L mixed sugar, 4 g/L glucose-only
    monoculture/coculture comparisons and 4 g/L xylose-only coculture. Product yields
    use mol per mol C6 equivalents. Replicated tables report two independent cultures
    and standard deviations; no new significance test or conversion to a different
    denominator was made.
  support: supports
  accessed_at: '2026-10-21T15:13:26.509676Z'
  snapshot_sha256: fb627d6e62d0dae39c90a6adc7eb0c273a2ba85a94cb6de3b03ed0972952dad9
- evidence_id: publisher-equations
  kind: primary_source
  reference: https://link.springer.com/article/10.1186/1475-2859-9-102
  locator: Publisher HTML equations 7–8, compared with S1 and enhancement narrative
  summary: Both publisher HTML and XML print a minus sign before the enhanced-minus-baseline
    term, while S1 enhanced values exceed baseline and the narrative describes enhancement.
    This unresolved source-model discrepancy is not a new encoded-record defect; no
    model reproduction or corrected equation is certified.
  support: supports
  accessed_at: '2026-10-21T15:13:26.510095Z'
  snapshot_sha256: 1854bf04932e69a227a8a890a67e6eb6dcdf3bf700627ea0bc2f22d08328377a
- evidence_id: figures
  kind: primary_source
  reference: PMID:21192828
  locator: All six main JPG images and captions; S1 page 1 and S2 page 3 layouts
  summary: Figures 1–4 show condition-dependent species ratios, Figure 5 simulated
    trajectories and Figure 6 supernatant growth response. Figure 1 displays dilution
    rates only through 0.25/h although text/tables also report 0.30/h. No bar digitization,
    raw-data analysis or fresh statistical calculation was performed.
  support: supports
  accessed_at: '2026-10-21T15:13:26.510270Z'
  snapshot_sha256: cf96f403cc0902ffa609924d15ba53c8c8b6d0474355fbd429f775cb86bac046
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity; TaxonomicComposition.functional_role; FunctionalRoleEnum;
    EnvironmentalFactor; ComputationalProvenance
  summary: CROSS_FEEDER denotes utilization of metabolites from other taxa. SECONDARY_FERMENTER
    denotes fermentation of products from primary degraders, without requiring a different
    species as that degrader. Functional roles and ecological_state are optional.
    Environmental factors describe conditions rather than yield outcomes; computational
    provenance can separate model assumptions and software from experimental evidence.
  support: supports
  accessed_at: '2026-10-21T15:13:26.510329Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded frozen receipt
  summary: All nine distinct encoded ID-label pairs match local OAK across 23 occurrences.
    Current NCBI terms are strain rank; chemical and GO labels are valid.
  support: supports
  accessed_at: '2026-10-21T15:13:26.510479Z'
  snapshot_sha256: 91d7da27579f32f8ec2bb54ecbee4aa2a2d08eeb098c046da26e76b5dd37b208
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole bounded frozen receipt
  summary: Semantic checks preserve exact strain identity, conditional mechanism interpretation
    and the distinction between generic sugar fermentation and trophic-role claims.
  support: supports
  accessed_at: '2026-10-21T15:13:26.510705Z'
  snapshot_sha256: b280193b998fc33962c3a0a9f715772c5449cd1221d6e1061894d3a9026e139d
- evidence_id: catalogues
  kind: authority
  reference: child-strain-authority.json
  locator: Whole bounded frozen receipt
  summary: Direct DSMZ catalogue and linked LPSN evidence verify both DSM/ATCC pairs
    and the current C. acetigenus classification of DSM 12137/I77R1B. No catalogue
    maintenance conditions are imported.
  support: supports
  accessed_at: '2026-10-21T15:13:26.510830Z'
  snapshot_sha256: 3d26d5b6cbf51744bae24c75fffcf77836c8a5b7e09d831f2212c6b933c5029d
- evidence_id: gtdb
  kind: authority
  reference: child-gtdb-mapping-check.json
  locator: Whole bounded frozen receipt
  summary: Exact local crosswalk rows agree with both encoded species mappings, lineages,
    fractions 1.0 and genome counts 2 and 4. The legacy release-latest wording is
    not a newly verified numbered release.
  support: supports
  accessed_at: '2026-10-21T15:13:26.511030Z'
  snapshot_sha256: 484bb0dd05fa9825a4711530a137d705a30b5635e8539d8b9734f436aa97894f
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded frozen receipt
  summary: The two isolate reference-genome projects and chromosome accessions match
    their exact strains. The actual S2 phenotype asset is verified; its PMID-derived
    accession is a descriptive locator, not a registered archive identifier. Earlier
    DOI identity and institutional abstract are bounded separately.
  support: supports
  accessed_at: '2026-10-21T15:13:26.511222Z'
  snapshot_sha256: e29209ed8a64286d0d0d4ad2da0e7b24c46d19381c8674d48b1fcf1497e92bf9
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded frozen receipt
  summary: 'All 23 excerpts match direct PubMed and the pinned abstract cache: 22
    abstract spans plus one title. The full XML has separate typography-sensitive
    coverage; no unmatched unit rendering is called fabricated evidence.'
  support: supports
  accessed_at: '2026-10-21T15:13:26.511356Z'
  snapshot_sha256: 94b8ea4a980edec25f4ee6eaa9076377e1d48224a763e22edaac7ee95cccacce
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded frozen receipt
  summary: The exact historical row and sidecar preserve the prior graph repairs.
    Current issue 1270 also covers another record, issue 516’s earlier species-attribution
    error at high dilution is already repaired, and broader issue 1268 is context
    only. No issue is closed by this review.
  support: supports
  accessed_at: '2026-10-21T15:13:26.511509Z'
  snapshot_sha256: 80d8ea857f70cf0a8039619c2292d7ae0a870fd16d91379aa11a14246bdc3617
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded frozen receipt
  summary: 'Native graph COMPLETE: three nodes, one arrow and six node-evidence entries.
    Completeness 100 and quality 100 after capping describe fields and diagnostics,
    not scientific truth.'
  support: supports
  accessed_at: '2026-10-21T15:13:26.511534Z'
  snapshot_sha256: 13f95fbe576f8af7457f3d6f5d690d792fd5925d72b77ef74a26157781f66e30
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded frozen receipt
  summary: Whole-record source assessment supports one major role-scope finding and
    two minor context/condition findings. Full primary main, six figures and both
    scientific supplements were inspected; earlier-paper and model-reproduction limits
    remain explicit.
  support: supports
  accessed_at: '2026-10-21T15:13:26.511554Z'
  snapshot_sha256: f428d2c5bcfb82863a277ee2408580e57e91a2d6fe07228bdcf5cd82c7203302
- evidence_id: lead-read
  kind: validation
  reference: lead-primary-read-scope.json
  locator: Whole bounded frozen receipt
  summary: Pins full scientific-main and table reading, all six main image views,
    full S1/S2 text and critical supplement layout views.
  support: supports
  accessed_at: '2026-10-21T15:13:26.511573Z'
  snapshot_sha256: cf96f403cc0902ffa609924d15ba53c8c8b6d0474355fbd429f775cb86bac046
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded frozen receipt
  summary: Root independently assessed the full main, all six figures, S1 and all
    eight S2 tables and concurs with the final finding groups and boundaries.
  support: supports
  accessed_at: '2026-10-21T15:13:26.511786Z'
  snapshot_sha256: fb7f320ea5af2d56b566d0571b6556224c847be43b637592b2d90baeaff344ce
- evidence_id: auxiliary
  kind: validation
  reference: auxiliary-frozen-manifest.json
  locator: Whole bounded frozen receipt
  summary: Child-owned native, authority and adapter receipts are immutable and independently
    pinned; no shared-filename overwrite was performed.
  support: supports
  accessed_at: '2026-10-21T15:13:26.511991Z'
  snapshot_sha256: 62bad1ecda78dcf82475c8536f749b54495ffb60f22e133f2635d634ec476685
- evidence_id: earlier-publication
  kind: primary_source
  reference: doi:10.1016/j.ijhydene.2008.07.092
  locator: Directly opened Lund University publication abstract and bibliographic
    identity
  summary: The earlier paper includes this exact pair, but its highlighted high hydrogen
    rates belong to C. saccharolyticus plus enriched compost microflora. Only the
    abstract and identity were inspected; it does not supply an independently reviewed
    mixed-sugar superiority comparison for this pair.
  support: supports
  accessed_at: '2026-10-21T15:13:26.512126Z'
  snapshot_sha256: cf2b928ab27a5930701dc2c1454c044e1496f4913d107c893843ab423db4a14e
- evidence_id: access-fulltext
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3022713/fullTextXML
  locator: Preserved actual access receipt
  summary: The direct Europe PMC response contains the full primary XML.
  support: supports
  accessed_at: '2026-10-21T15:06:53.313023Z'
  snapshot_sha256: 6cccd3a823491a0bf252722f48c14138e8b506b11bb55f44039fb4ea4f67228b
- evidence_id: access-publisher
  kind: validation
  reference: https://microbialcellfactories.biomedcentral.com/articles/10.1186/1475-2859-9-102
  locator: Preserved actual access receipt
  summary: The publisher response contains the primary article and equations.
  support: supports
  accessed_at: '2026-10-21T15:06:43.527948Z'
  snapshot_sha256: 72fe4d6528b0e29277473f93db91d7aeccac099a677e59168ee8eb375ab737c5
- evidence_id: access-supplement-zip
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3022713/supplementaryFiles
  locator: Preserved actual access receipt
  summary: The direct supplement archive contains all six main images and both source-linked
    scientific PDFs; assets were safely extracted and their identity checked.
  support: supports
  accessed_at: '2026-10-21T15:06:59.082416Z'
  snapshot_sha256: 6f13ddbefc61f65e7d1e1039228e882736938abba2e2908610437f8d768bb9af
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Verified same-runtime optional adapter discovery reuse
  summary: The child explicitly reuses bounded batch 09 runtime discovery with its
    original timestamp and hashes. No applicable expression-module evidence is established;
    this is not negative biological evidence.
  support: supports
  accessed_at: '2026-10-21T15:13:26.512586Z'
  snapshot_sha256: 0220c940be7904777b3e255e93ef9ff215febcbe78233cfd5e8b676d95200591
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  locator: Actual execution 2026-10-21T15:08:14.394838+00:00 to 2026-10-21T15:08:15.159134+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T15:08:15.159134Z'
  snapshot_sha256: d62efa53d26c606a5fb545b9f7589a67273f633128119b00d9713110190bf57e
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-strict kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-09/000185/strict-report.tsv
  locator: Actual execution 2026-10-21T15:08:14.395065+00:00 to 2026-10-21T15:08:16.462545+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T15:08:16.462545Z'
  snapshot_sha256: 1a2b69c76183c3be6a315481bb8c2e932302f08a927297efefdc4a38c5ad2480
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-terms kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  locator: Actual execution 2026-10-21T15:08:14.395140+00:00 to 2026-10-21T15:08:16.107540+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T15:08:16.107540Z'
  snapshot_sha256: a649306d56124af462815bbde35a85a52040a80fe76648a715d438abc8288eff
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  locator: Actual execution 2026-10-21T15:08:15.159503+00:00 to 2026-10-21T15:08:15.238899+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T15:08:15.238899Z'
  snapshot_sha256: 7c69206e96e002892517ab4a5435d4ca4d35d131be5ab2e980a31a0a42439c9b
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb-domain kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  locator: Actual execution 2026-10-21T15:08:15.239152+00:00 to 2026-10-21T15:08:16.520459+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T15:08:16.520459Z'
  snapshot_sha256: d49019387c946f998ffcb82903ddc30604c91ae43256ee6de87634645eca7727
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-history history/records/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture
  locator: Actual execution 2026-10-21T15:08:16.107826+00:00 to 2026-10-21T15:08:16.862576+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T15:08:16.862576Z'
  snapshot_sha256: ec6afafb4ce0b6fb4126f8d6d9425d149ed08b58658a856ebbdeeba0f9aabb88
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T15:08:16.863094+00:00 to 2026-10-21T15:08:16.914058+00:00
  summary: Read-only cache-name preflight passed.
  support: supports
  accessed_at: '2026-10-21T15:08:16.914058Z'
  snapshot_sha256: 3b82266553906544f01dc5db66969e2fb65fa5f5f72d5f67f49e25c9bb6ed806
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-references-explained kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
  locator: Actual execution 2026-10-21T15:08:16.914350+00:00 to 2026-10-21T15:08:17.967335+00:00
  summary: Reference validation passed against the pinned abstract cache.
  support: supports
  accessed_at: '2026-10-21T15:08:17.967335Z'
  snapshot_sha256: cccd138cd3f341f8437af908eb65f2e607d822a255923dd52ed1134567416e3c
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T14:53:06.814378+00:00 to 2026-10-21T14:53:14.616064+00:00
  summary: Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities;
    the focal graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T14:53:14.616064Z'
  snapshot_sha256: af46c37677bdc80eb1866f799958882492e9f72ed8eff4c304f69cd667f99156
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T14:53:06.817734+00:00 to 2026-10-21T14:53:14.704428+00:00
  summary: Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities;
    the focal graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T14:53:14.704428Z'
  snapshot_sha256: 6bf7d1eaf4ddc02de94aaea33610660d4b12689dc78ff47a6e29148baeffdd4f
assessments:
- assessment_id: identity
  area: identity
  topic: Exact two-strain community and current taxonomy
  outcome: supported
  summary: Retain DSM 8903 and DSM 12137/I77R1B with source names separated from current
    canonical labels.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - identity
  - ontology
  - catalogues
  - gtdb
  - resources
  dimensions:
  - name: community_scope
    value: Designed two-strain continuous-culture system
    definition: No enriched compost microflora or comparator community is imported.
    evidence_ids:
    - identity
    - earlier-publication
  - name: strain
    value: DSM 8903/ATCC 43494; DSM 12137/ATCC 700853/I77R1B
    definition: The Methods, catalogues and reference genomes establish exact strain
      equivalence.
    evidence_ids:
    - identity
    - catalogues
    - resources
  - name: taxon_rank
    value: NCBITaxon:351627 and NCBITaxon:632335 are strain-level terms
    definition: Legacy C. kristjanssonii and current C. acetigenus denote the same
      source strain here.
    evidence_ids:
    - ontology
    - catalogues
  - name: grounding_status
    value: Both GTDB species mappings supported by the local crosswalk
    definition: No new classification or release identity is inferred from legacy
      provenance text.
    evidence_ids:
    - gtdb
  - name: environment
    value: Anaerobic thermophilic laboratory stirred reactor
    definition: The laboratory is the physical study environment, with applied biohydrogen
      motivation.
    evidence_ids:
    - cultivation
  - name: medium
    value: Modified DSM 640 with distinct sugar feeds and start-up modifications
    definition: The cited full base formulation was not independently reconstructed.
    evidence_ids:
    - feed-regimes
    - cultivation
  - name: evidence_tier
    value: Full main, five main tables, six figures and both supplements
    definition: Observed stimulation, hypothesized model mechanism and measured yield
      remain distinct.
    evidence_ids:
    - source-scope
- assessment_id: state
  area: scope
  topic: State, origin, category and engineering design
  outcome: supported
  summary: Retain ENGINEERED, SYNTHETIC and BIOTECHNOLOGY.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - identity
  - schema
  - coexistence
  details: The source deliberately assembles known strains in a controlled reactor.
    The engineered state remains appropriate even though experimental coexistence
    is stable. Optional ecological_state does not require a replacement, and no genetic
    engineering is implied.
- assessment_id: roles
  area: evidence
  topic: taxonomy[0:2].functional_role and membership evidence
  outcome: concern
  summary: Flat CROSS_FEEDER assignments are unsupported; generic fermentation does
    not by itself establish SECONDARY_FERMENTER.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - roles
  - schema
  - stimulation
  details: The donor and treated recipient are known, but no recipient role is demonstrated
    for the donor and nutrient utilization by the treated strain is unresolved. Omit
    unsupported role enums unless claim-specific evidence satisfies their definitions.
    Retain the measured donor-to-recipient growth response untyped. Do not invent
    a requirement that a primary degrader must be another species.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Stable Chemostat Coexistence'
  outcome: supported
  summary: Retain coexistence as an observed reactor outcome with the current mechanistic
    limits.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - coexistence
  - feed-regimes
  - figures
  details: Both named strains persist under reported continuous regimes, including
    glucose-only limitation. Changing abundance ratios do not identify niche partitioning
    or establish that coexistence causes higher hydrogen yield.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Growth-Supernatant Enhancement'
  outcome: supported
  summary: Retain the directional batch growth response without cross-feeding or reciprocal-fitness
    typing.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - stimulation
  - roles
  - figures
  details: C. saccharolyticus is the supernatant donor and C. kristjanssonii the treated
    recipient. Shorter lag and about 18% greater maximum biomass are supported; maximum
    specific growth rate is unchanged within the reported comparison. The compound,
    nutritional mechanism and secretion-versus-lysis source remain unknown.
- assessment_id: arrow-1-0
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: supported
  summary: Retain only the HYPOTHESIZED stimulation-to-coexistence edge.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - model
  - stimulation
  - supplement-parameters
  - publisher-equations
  - history
  details: The model assumes effects on both recipient growth rate and biomass yield,
    while the batch experiment supports only part of that mechanism. The current arrow
    does not assert necessity or measured nutrient transfer. Source parameter guesses
    and the printed equation discrepancy limit model certification; neither creates
    a new demonstrated biological edge.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Enhanced Glucose-Limited Hydrogen Yield'
  outcome: concern
  summary: The endpoint description is sound; its metabolite list and evidence should
    match the glucose-only comparison.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - hydrogen
  - supplement-data
  - feed-regimes
  details: Retain 3.7 mol H2/mol glucose at dilution 0.06/h and the distinction between
    yield and productivity. Xylose and the mixed-feed excerpt belong to a different
    experimental condition and should not imply xylose supplied this specific yield
    comparison. Acetate and fermentation are supported in the primary tables.
- assessment_id: cultivation
  area: completeness
  topic: growth_media[0], cultivation_setup[0] and model evidence context
  outcome: concern
  summary: Replace the obsolete unfetched-Methods boundary with available source-specific
    conditions and model provenance.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - cultivation
  - feed-regimes
  - model
  - supplement-parameters
  details: Preserve the existing rate-range caveat while recording exact temperature,
    pH, volume, mixing, gas and inoculum details. Separate mixed-feed, glucose-only,
    xylose-only and supernatant batch assays. Add computational provenance to model
    support without relabeling the measured growth phenotype as wholly computational.
- assessment_id: ingredients
  area: evidence
  topic: related_ingredients[0:3] and environmental_factors[2]
  outcome: concern
  summary: Glucose, xylose and dihydrogen identities are sound; the comparative yield
    statement and outcome placement need narrower scope.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - hydrogen
  - feed-regimes
  - schema
  - earlier-publication
  details: The focal monoculture comparison is glucose-only. Mixed-sugar conversion
    is separately established but does not inherit the superiority comparison. The
    value 3.7 mol/mol is an outcome; glucose limitation and dilution rate are conditions.
    Preserve these conditions while placing the measured yield with the interaction
    endpoint.
- assessment_id: resources
  area: provenance
  topic: Strain genomes, S2 phenotype data and earlier publication
  outcome: supported
  summary: Retain the verified strain-reference projects and genuine supplementary
    fermentation dataset.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - resources
  - catalogues
  - earlier-publication
  - supplement-data
  details: The genomic projects are isolate references rather than sequencing of the
    mixed coculture. The descriptive S2 locator can be supplemented with its direct
    asset URL, without inventing a registered accession or creating a data-absence
    finding. Earlier-paper bibliographic/abstract verification does not certify its
    full methods or transfer compost-community outcomes.
- assessment_id: history
  area: provenance
  topic: Prior decisions, source cache and unresolved mechanism
  outcome: supported
  summary: Preserve the qualified graph and previous removed coexistence-to-yield
    arrow.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - history
  - snippets
  - source-scope
  details: The original cache is abstract-only and remains unchanged. New main/SI
    inspection supports current-claim completion but does not silently promote prior
    reviews, close issues or append curation history.
- assessment_id: validation
  area: schema
  topic: Native and authority checks
  outcome: supported
  summary: All eight focused native checks pass; one major and two minor source-specific
    findings remain.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - ontology
  - check-validate
  - check-validate-references-explained
  - native-target
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Mechanical completeness does not establish scientific adequacy.
  target_ids:
  - CommunityMech:000185
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role rubric points +5 environment +10 for
      at least three interaction nodes +10 for at least three environmental factors
      +5 external resources +10 growth medium +5 datasets +5 metabolites.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0, P2=1, P3=2, P4=0; six evidence entries / three nodes gives 20 evidence
      points; COMPLETE adds 15. Raw 121 is capped at 100.
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
- finding_id: functional-role-scope
  issue_key: cm-000185-functional-role-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: unsupported trophic-role assignments materially change
    the represented functional relationship; valid organism identity and a qualified
    graph do not supply the missing role-specific evidence.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Remove unsupported trophic-role assignments
  description: Both taxa are assigned CROSS_FEEDER and SECONDARY_FERMENTER using membership
    excerpts. Donor-supernatant growth stimulation establishes neither reciprocal
    recipient status nor metabolite nutrition; supplied-sugar fermentation alone does
    not establish a primary-degrader-product trophic role.
  target_ids:
  - CommunityMech:000185
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].evidence
  - taxonomy[1].functional_role
  - taxonomy[1].evidence
  evidence_ids:
  - roles
  - stimulation
  - schema
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
    role: canonical_record
- finding_id: assay-model-context
  issue_key: cm-000185-assay-model-context
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded assay-context or condition/evidence-placement
    repair; the exact pair and core qualified outcomes remain supported. Optional
    fields are not treated as mandatory.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Recover the available assay and model context
  description: Cultivation notes still say working volume, temperature and the full
    dilution range remain unfetched. The full source supplies these and distinct feed,
    inoculum and gas regimes, plus a separately modeled explanation with assumed parameters.
  target_ids:
  - CommunityMech:000185
  field_paths:
  - growth_media[0]
  - cultivation_setup[0]
  - ecological_interactions[1].evidence
  evidence_ids:
  - cultivation
  - feed-regimes
  - model
  - supplement-parameters
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
    role: canonical_record
- finding_id: hydrogen-condition-scope
  issue_key: cm-000185-hydrogen-condition-scope
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded assay-context or condition/evidence-placement
    repair; the exact pair and core qualified outcomes remain supported. Optional
    fields are not treated as mandatory.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Keep hydrogen yield claims within their measured condition
  description: The hydrogen ingredient generalizes superiority to glucose and xylose,
    while the focal monoculture comparison is glucose-only. The glucose-limited node
    retains xylose/mixed-feed evidence, and an environmental-factor value stores a
    measured yield rather than an environmental condition.
  target_ids:
  - CommunityMech:000185
  field_paths:
  - related_ingredients[2].relevance
  - ecological_interactions[2].metabolites
  - ecological_interactions[2].evidence
  - environmental_factors[2]
  evidence_ids:
  - hydrogen
  - feed-regimes
  - supplement-data
  - schema
  - earlier-publication
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
    role: canonical_record
actions:
- action_id: repair-functional-roles
  description: Represent observed fermentation and directional stimulation without
    unsupported trophic enums.
  finding_ids:
  - functional-role-scope
  target_ids:
  - CommunityMech:000185
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Omit both flat CROSS_FEEDER assignments unless separate claim-specific evidence
    establishes utilization of another taxon’s metabolites. Simply labeling the observed
    supernatant response proposed does not demonstrate that enum’s utilization relation.
    Keep the experimentally known donor and treated recipient and their untyped growth
    response.
  - For each SECONDARY_FERMENTER assignment, require source-specific support for fermentation
    of products from primary degraders; supplied glucose/xylose fermentation and membership
    excerpts alone are insufficient. The schema does not require a different species
    as that degrader. Omit the enum if its narrower trophic scope cannot be supported,
    while retaining supported sugar-fermentation prose.
  - Functional roles are optional. Do not force PRIMARY_DEGRADER or invent a generic
    fermenter enum as a substitute. Preserve strain identities, current NCBI/GTDB
    mapping, the three qualified nodes and the single HYPOTHESIZED arrow.
  - Attach exact evidence to each retained claim. Do not add reciprocal fitness, named
    metabolites, secretion, nutrient uptake or mechanistic necessity from the supernatant
    experiment.
- action_id: recover-assay-model-context
  description: Replace obsolete source-access gaps with scoped experimental conditions
    and separately labeled model provenance.
  finding_ids:
  - assay-model-context
  target_ids:
  - CommunityMech:000185
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Record source-reported modified DSM 640 with yeast extract 1 g/L, 70 ± 1 °C, pH
    6.7 ± 0.1, a 3 L stirred reactor with 1 L working volume, 300 rpm and nitrogen
    sparging at 100 mL/min with less than 5 ppm oxygen. Preserve pH control with 3
    M NaOH. Do not copy catalogue maintenance media or reconstruct the unread precursor
    recipe.
  - Describe the twice-subcultured inocula, OD620 0.3–0.4, total 15% inoculum with
    equal strain volumes, and batch start-up followed by continuous operation. Scope
    initial cysteine hydrochloride 1 g/L separately from its omission in continuous
    feed; do not apply the supernatant batch-inoculum variants to all chemostats.
  - Separate 10 g/L total mixed sugar (1:1; dilution 0.04–0.30/h), 4 g/L total mixed
    sugar (1:1), glucose-only 4 g/L and xylose-only 4 g/L comparisons at 0.06 and
    0.15/h. Preserve condition-specific residual-sugar and steady-state criteria instead
    of one universal feed or limitation claim.
  - Add computational provenance for the ODE model and MATLAB R2009a to model-specific
    evidence or an appropriate separate evidence item, retaining measured batch evidence
    as experimental. Distinguish assumed/guessed S1 parameters from measured values
    and note the unresolved printed equation sign; do not claim model reproduction.
  - Remove stale statements that these Methods remain unfetched. Following separately
    authorized curation, run the focused schema, strict, terms, references, GTDB/domain
    and history checks; do not edit caches or schema merely to make new source evidence
    pass.
- action_id: scope-hydrogen-endpoint
  description: Synchronize ingredient, node and condition representations with the
    glucose-only yield comparison.
  finding_ids:
  - hydrogen-condition-scope
  target_ids:
  - CommunityMech:000185
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Caldicellulosiruptor_TwoSpecies_Hydrogen_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - 'Restrict the superior-yield statement to the demonstrated 4 g/L glucose-only
    comparison: 3.7 mol H2/mol glucose at dilution 0.06/h versus 3.5 for each monoculture.
    Keep mixed-sugar and xylose-only production as separately scoped observations;
    earlier-paper abstract verification does not supply an unreviewed comparative
    result.'
  - Remove or clearly separate xylose and mixed-feed evidence from the glucose-limited
    yield node. Preserve glucose, measured hydrogen and acetate, the valid fermentation
    annotation, and the distinction between molar yield, specific production rate
    and volumetric productivity.
  - Move the 3.7 mol/mol yield outcome out of environmental_factors, preserving it
    in the existing phenotype node. If retaining an environmental entry, encode glucose
    limitation and dilution 0.06/h as conditions with narrow evidence rather than
    using yield as the condition value.
  - Do not restore the removed coexistence-to-yield edge or infer reciprocal fitness.
    Preserve S2’s hexose-equivalent denominator where relevant, replicate scope and
    the absence of a new statistical analysis.
limitations:
- No raw genome sequencing, genome reannotation, new statistical tests, model rerun
  or parameter refitting. Existing experimental and model outputs are assessed as
  reported.
- The earlier exact-pair DOI was verified only through bibliographic metadata and
  a directly opened institutional abstract. Its high production rates concern a different
  compost-microflora coculture; no transfer to this pair is made.
- Modified DSM 640 is source-reported, but its cited precursor full recipe was not
  independently reviewed. Source-reported modifications and reactor conditions may
  be recovered without inventing salts or an exact CultureMech mapping.
- S1 glucose-affinity and compound parameters are explicitly estimated guesses. Publisher
  and XML equations 7–8 contain a sign inconsistent with the enhancement narrative
  and S1 parameter ordering. The model has not been reproduced or corrected; its hypothesized
  explanatory scope is retained.
- Donor supernatant stimulation does not resolve metabolite nutrition versus signaling,
  secretion versus lysis, reciprocal transfer or mechanistic necessity. No named exchange
  compound or reciprocal fitness benefit is inferred.
- Figure 1 plots dilution rates through 0.25/h, whereas the experiment text and tables
  include 0.30/h. These source representations are not silently treated as identical.
- Reference genomes identify the two cultured strains; they are not mixed-coculture
  sequencing. Catalogue maintenance conditions are not the focal protocol.
- Current completion covers all encoded claims with full main, figures and critical
  SI. It does not certify every earlier paper, the precursor recipe, raw data or model
  reproducibility.
notes:
- No canonical, cache, history, generated or saved-review files changed; all 23 inspected
  inputs remain pinned.
- 'All 23 existing excerpts match direct PubMed and the abstract-only cache: 22 abstract
  spans and one title. Full XML coverage differs for three typographic unit renderings;
  no body-only literal support is implied by abstract matching.'
- Completeness 100 and quality 100 (raw 121) are native mechanical scores, not scientific
  certification.
- No raw sequence/statistical reanalysis, model execution, paid provider, author contact
  or later-target review.
tags:
- record-review
- hydrogen
- thermophilic-coculture
- main-and-supplements-assessed
- batch-09
```
