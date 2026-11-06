# CRC Fusobacterium control SynCom record review

- Review: 20261021T141906Z-crc-fusobacterium-syncom-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T14:09:09.766666Z
- Finished UTC: 2026-10-21T14:19:06.436697Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The main paper and supplement support the seven-strain experimental community and its qualified four-node, one-arrow graph. Two major findings concern collapsed membership/blanket role assignment and unqualified ingredient mediation; three minors concern assay provenance, design placement and verified public resources.

## Scope And Provenance

Entire record, all four nodes and its one PARTIAL arrow assessed against complete primary science, critical figures, SI, authority, provenance and native checks.

Selection: Only released CommunityMech:000128 in the owned batch 08 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000128 | kb/communities/CRC_Fusobacterium_Control_SynCom.yaml | maintained | CRC Fusobacterium Control SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000128 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000128 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000128 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000128 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000128 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000128 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000128 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000128 | Reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000128 | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000128 | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| Primary and supplement identity | passed | True | CommunityMech:000128 | Direct article metadata, complete primary XML and validated supplementary archive agree. |
| Whole main and critical supplemental verification | passed | True | CommunityMech:000128 | Full scientific main and SI, relevant figures and assay/roster/resource scopes were assessed; no raw-data reproduction is claimed. |
| Exact cultivation-recipe correspondence | not_applicable | False | CommunityMech:000128 | GAM is source-named, but no exact complete formulation/manufacturer is verified for a unique CultureMech link. |
| Optional structured expression adapter | unavailable | False | CommunityMech:000128 | No applicable expression-module dataset established; bounded runtime discovery is preserved. |

## Scientific And Domain Assessments

### Final seven-member SynCom and external challenge

identity: concern. Targets: CommunityMech:000128.

The community identity is clear, but the Bacteria placeholder omits seven recoverable species and strain designations.

### State, origin and category

scope: supported. Targets: CommunityMech:000128.

Retain ENGINEERED, SYNTHETIC and OTHER for the deliberately designed experimental SynCom.

The study combines computational selection with experimental assembly. These labels do not assert an engineered genotype or ecological equilibrium. Ecological state remains a separate optional field.

### Blanket CROSS_FEEDER role

evidence: concern. Targets: CommunityMech:000128.

Community design and validation do not establish that all seven members utilize metabolites from other taxa.

Recover member-specific role evidence and distinguish model-predicted complementarity from observed substrate transfer. The model can support a qualified hypothesis where a particular member and interaction are identified; a generic membership excerpt cannot support a domain-wide recipient assignment. No specific tracer assay is required and cross-feeding is not declared biologically absent.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000128.

Retain low modeled competition and observed colonization with the current causal qualification.

Low competition is a model selection criterion, not measured niche partitioning. Normal-mouse colonization/safety and CRC-model measurements are separate source contexts. Add the relevant narrow evidence rather than letting the generic design-validation abstract excerpt support every part. No colonization-to-suppression arrow is restored.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000128.

Retain context-dependent Fn suppression without reciprocal-negative competition or established-infection eradication.

The source reports in-vitro and in-vivo measurements. Its broad competition terminology does not require the schema COMPETITION type. Amino-acid supplementation slows Fn decline, and pH/qPCR wording remains bounded. Co-gavage cannot isolate clearance of a pre-established infection.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000128.

Retain intervention-associated metabolic changes and the explicit PARTIAL interpretation.

Correlations and expression are not necessary-mediation tests. Preserve the main/figure LCA-ratio discrepancy and do not infer a numerical conversion direction from conflicting definitions. Bile-acid class and L-tryptophan identifiers match the intended broad entities.

### ecological_interactions[3]

graph: supported. Targets: CommunityMech:000128.

Retain measured mouse disease endpoints with the current clinical and significance limits.

The source supports bounded tumor, tissue-lipid and inflammatory outcomes. It does not support universal biomarker improvement, significant blood-triglyceride reduction or human clinical efficacy. The nonsignificant S5 TNF-alpha panel does not invalidate the generic endpoint supported by other inflammatory measurements.

### ecological_interactions[2].downstream[0]

graph: supported. Targets: CommunityMech:000128.

Keep the proposed metabolism-to-disease link explicitly PARTIAL.

Concurrent changes and the conceptual model motivate the authors’ hypothesis but do not isolate required mediation. Preserve the single arrow and keep previously removed colonization-to-suppression and suppression-to-metabolism links absent.

### related_ingredients[0]

evidence: concern. Targets: CommunityMech:000128.

The ingredient prose asserts a temporal and causal chain that the graph correctly qualifies.

Replace after-decolonization restoration and tumor-suppression mediation with intervention-associated metabolism and an explicitly proposed contribution. The amino-acid supplementation result must not be inverted into evidence that adding tryptophan promotes pathogen suppression.

### Recoverable assay and model context

completeness: concern. Targets: CommunityMech:000128.

The main and SI provide additional reproducible context beyond the current GAM/anaerobic statement.

Record 37 C and distinguish 96 h plate tests, normalized-seed liquid serial cultures, the SynCom2 plus Fn experiment and animal gavage. Initial 1 mL into 40 mL and later 0.4 mL into 40 mL are not a universal 40 mL final volume. Preserve the printed SynCom3 1.10 mL inconsistency and unspecified percentage basis/complete mGAM recipe. Model reachability inputs belong in computational provenance, not growth-medium composition.

### environmental_factors[0]

representation: concern. Targets: CommunityMech:000128.

Network reconstruction and low-competition selection are design/provenance content, not environmental conditions.

Consolidate this content under the existing engineering design and appropriate computational evidence. Do not delete the supported design information or replace it with an invented condition.

### Named public resource omissions

provenance: concern. Targets: CommunityMech:000128.

Verified focal SynCom metagenomics and metabolomics resources are absent from the record.

Prioritize PRJNA1214893 and OMIX008965. Keep discovery cohorts, earlier interventions, the B. animalis genome and human serum context distinct. Some project titles specify 16S despite the paper’s aggregate sequencing label; no blanket shotgun annotation is justified. File counts are not independent sample or animal counts.

### Previous repairs and current source coverage

provenance: supported. Targets: CommunityMech:000128.

Retain graph and obsolete-GO repairs while updating the recoverable roster and source-context gaps.

The old decision used full main/captions without figures or supplements. The current assessment adds those sources without rewriting historical scope. GO:0006568 remains absent; no unsupported biosynthesis/catabolism alternative is selected. Eleven direct-source snippet matches do not by themselves validate the attached blanket role or causal explanation.

### Native checks and source-specific review

schema: supported. Targets: CommunityMech:000128.

Eight focused native gates pass; source-backed identity, causal and provenance findings remain.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000128.

Scores measure current encoded fields and diagnostics, not biological certainty.

## Findings

### recover-members-and-roles: Recover the seven-member roster and individual role support

major / open / confirmed; issue key: cm-000128-recover-members-and-roles.

The single Bacteria descriptor omits seven directly identified species and collection strains. Its blanket CROSS_FEEDER role is attached to a generic design/validation excerpt, which does not establish use of other taxa’s metabolites by every member. The source resolves membership, so the broad placeholder and unqualified role are materially incomplete.

### ingredient-mediation: Qualify the ingredient’s temporal and causal interpretation

major / open / confirmed; issue key: cm-000128-ingredient-mediation.

The L-tryptophan relevance and evidence explanation assert metabolic restoration after Fn displacement and a role in suppressing tumor growth. The experiments show intervention-associated changes and support a proposed mechanism; they do not isolate that temporal/causal chain. This non-graph wording contradicts the carefully qualified graph.

### assay-provenance: Recover model, culture and evidence context

minor / open / confirmed; issue key: cm-000128-assay-provenance.

The current record gives GAM and anaerobiosis but omits available source-specific temperature, assembly/transfer context and model provenance. Generic IN_VIVO design evidence also stands in for several distinct computational, bench and animal claims.

### design-placement: Move network design out of environmental conditions

minor / open / confirmed; issue key: cm-000128-design-placement.

environmental_factors[0] describes metabolic-network reconstruction and SynCom selection, rather than an environmental condition. The supported information already belongs with engineering design and computational evidence.

### focal-resources: Link verified focal SynCom datasets

minor / open / confirmed; issue key: cm-000128-focal-resources.

The record omits directly identified public metagenomics and metabolomics deposits. PRJNA1214893 and OMIX008965 specifically describe the focal SynCom intervention, whereas other source-listed deposits have distinct discovery, prior-intervention or genome scopes.

## Recommended Actions And Acceptance Checks

### restore-roster

Replace the domain placeholder with source-specific final membership and narrowly supported roles.

- Represent Bifidobacterium animalis, NCBITaxon:28025, CGMCC 1.15623; Limosilactobacillus reuteri, NCBITaxon:1598, GDMCC 1.614; Akkermansia muciniphila, NCBITaxon:239935, GDMCC 1.1346; Bacteroides thetaiotaomicron, NCBITaxon:818, GDMCC 1.1104; Clostridium sporogenes, NCBITaxon:1509, GDMCC 1.1481; Parabacteroides distasonis, NCBITaxon:823, GDMCC 1.1564; and Bacteroides fragilis, NCBITaxon:817, GDMCC 1.385. Use current canonical labels and direct SI evidence for collection names.
- B. animalis subsp. lactis, NCBITaxon:302911, is an optional supported finer candidate; preserve the distinction between source strain designation, species/subspecies authority and a verified strain taxid. Do not invent exact strain identifiers or catalogue aliases.
- Keep Fn CGMCC 1.2526 as the external challenge and B. longum CGMCC 1.5082 as an excluded candidate, not final members. The mouse is not a microbial member.
- Re-ground GTDB separately for each restored member; do not reuse the Bacteria-domain classification. Attach role-specific evidence and explicit computational qualifiers where supported; otherwise omit unsupported categorical roles rather than copying CROSS_FEEDER to every species.
- Retain four community-level nodes and the one PARTIAL arrow; roster completion does not require new mechanistic edges. Re-run native term, GTDB/domain, strict/schema and reference checks after separately authorized curation.

### qualify-ingredient

Align ingredient relevance and evidence with intervention-associated metabolism and the existing hypothesis-level graph.

- Remove the unestablished after-displacement sequence from related_ingredients[0].relevance and explanation. Describe altered tryptophan metabolism under SynCom treatment, with a proposed contribution to disease outcomes.
- Use PARTIAL support for the proposed metabolic mediation when retaining that interpretation, or separate a directly supported measured-outcome statement from the mechanistic hypothesis. A stronger source sentence does not remove the experiment’s causal limits.
- Preserve the existing supplementation result: added arginine/tryptophan reduces acidity and slows Fn decline. Do not claim that tryptophan supplementation itself improves suppression.
- Keep the existing co-gavage, missing SynCom-only CRC arm and LCA-ratio limitations, and preserve the graph’s single PARTIAL metabolic-response-to-disease arrow.

### recover-assay-context

Add bounded experimental and computational provenance from the main and supplement.

- Add source-supported 37 C anaerobic GAM cultivation. Separate 96 h plate compatibility assays from serial liquid cultures and the animal intervention; do not import centrifugation as incubation or invent vessel, shaking, gas composition or a complete GAM recipe.
- Document OD600 1.0 normalized seeds, four assembly variants and the use of SynCom2 with Fn. Initial 1 mL into 40 mL medium and subsequent 0.4 mL into 40 mL fresh medium every 24 h over six to eight generations require their own scope. Do not label 40 mL a verified final working volume.
- Preserve the printed SynCom3 1.10 mL sum versus 1 mL wording as a source discrepancy. Do not silently normalize it or infer the mass/volume basis of the 1% amino-acid supplements.
- Separate m2m/PathwayTools reachability/minimum-community design from RevEcoR KO-based competition/complementarity. Attach available ComputationalProvenance to COMPUTATIONAL evidence without calling the workflow FBA, measured transfer or an executed reproduction.
- Use narrow IN_VITRO and IN_VIVO evidence for their respective outcomes; distinguish normal-mouse colonization/safety from the AOM-DSS experiment. Preserve 200 microlitre co-gavage and preparation concentrations without converting them into unverified per-animal CFU doses.
- Update the current knowledge-gap discussion to acknowledge recovered roster/SI context while retaining unresolved mechanistic questions and prior historical scope. Source-only pH, LCA and nonsignificant-marker inconsistencies do not require unsupported new graph claims.

### move-design

Consolidate the supported network-design statement under the appropriate existing structure.

- Remove or relocate environmental_factors[0] as a design item, preserving its supported content in engineering_design and appropriate computational evidence.
- Keep actual laboratory or host conditions distinct from model selection criteria. Do not add a placeholder condition merely to preserve completeness points.

### link-focal-data

Add exact public resources with publication, cohort and assay scope.

- Link PRJNA1214893 as focal mouse fecal metagenomics after SynCom intervention and OMIX008965 as focal mouse fecal metabolomics after SynCom. Use the verified public metadata and main Data Availability Statement.
- If including other deposits, label PRJNA1079906 and OMIX008762 as human fecal discovery; PRJNA1086363/1086371 as their separately described interventions with archive titles specifying 16S; PRJNA1182847 as the B. animalis genome; OMIX008772/008761 as B. animalis metabolomics; and OMIX008758 as UDCA context. Do not relabel all as seven-member SynCom data.
- Treat OMIX008770 separately as SI-linked human serum metabolomics whose landing page links a related publication; keep that association explicit. Source-reported IMG identifiers do not establish cultured-strain genome equivalence.
- Do not treat positive/negative MS file counts as animal counts or metadata verification as raw-data validation. Re-run resource/reference checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/CRC_Fusobacterium_Control_SynCom.yaml; Entire record, four interaction nodes and one downstream arrow | supports | The record describes a seven-member experimental SynCom but represents its members by one Bacteria descriptor with a blanket recipient role. The graph already distinguishes intervention outcomes from proposed metabolic mediation. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=40433987&amp;retmode=xml; Article identity and available abstract | supports | Direct title, abstract and article identifiers identify the focal SynCom paper. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40433987%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article identity and available abstract | supports | Direct metadata identifies PMC12376641 and the focal DOI. |
| crossref | https://api.crossref.org/works/10.1002/advs.202414232; Article identity and available abstract | supports | Direct DOI metadata agrees with the primary article identity; metadata alone do not certify Methods. |
| members | PMID:40433987; Results 2.3–2.4 and Figure 3 caption | supports | Eight culturable candidates were considered, then B. longum was removed for slow growth in GAM. The final seven are B. animalis, L. reuteri, A. muciniphila, B. thetaiotaomicron, C. sporogenes, P. distasonis and B. fragilis. F. nucleatum is the challenge organism, not an eighth SynCom member. |
| strain-culture | PMID:40433987; SI Methods: Bacterial culture and co-culture of SynCom; source culture-collection paragraph | supports | The supplement gives all seven collection designations and GAM cultivation at 37 C anaerobically. Plate tests use adjacent inocula and 96 h incubation; liquid serial cultures normalize seeds to OD600 1.0 and transfer every 24 h. These are different assay contexts. |
| serial-assembly | PMID:40433987; SI Methods: four SynCom inoculation proportions, generation transfers and SynCom plus Fn | supports | SynCom2 is used in the Fn coculture. The first inoculation is 1 mL into 40 mL medium; later transfers use 0.4 mL into 40 mL fresh medium over six to eight generations. Printed SynCom3 component volumes sum to 1.10 mL despite the 1 mL wording; this discrepancy must not be silently normalized. |
| model-design | PMID:40433987; Results 2.3; Experimental Section: design of a minimal microbial community | supports | m2m with PathwayTools uses genome annotations and seed inputs to identify reachable metabolites and a minimum community. RevEcoR derives competition/complementarity indices from KO profiles. These are model-derived design criteria, not direct metabolite exchange or an automatically identified flux-balance simulation. |
| model-inputs | PMID:40433987; SI Methods: metabolic-network reconstruction, m2m and RevEcoR | supports | The supplement gives annotation inputs, seed-set context and reachability/minimum-community operations. Source-reported IMG inputs are not independently verified here as the exact genomes of the cultured collection strains; model seeds must not be treated as the GAM recipe. |
| suppression | PMID:40433987; Results 2.4; Figure 4J–L and Figure S4G | supports | Arginine or tryptophan supplementation reduces acidity and slows Fn decline in the coculture. This supports the existing context-dependent suppression description and does not establish that added tryptophan enhances suppression. |
| animal-design | PMID:40433987; Experimental Section: Mouse CRC Model; Results 2.5–2.6; Figures 4M–R and 5A | supports | Separate normal-mouse colonization/safety and AOM-DSS disease experiments are reported. The disease treatment mixes Fn and SynCom before 200 microlitre oral administration. Preparation CFU/mL values are concentrations, not automatically per-animal doses. There is no SynCom-only disease-model arm. |
| metabolism | PMID:40433987; Results 2.7; Figures 6–7 and Figure S6 | supports | Intervention-associated tryptophan and bile-acid profiles, gene expression and correlations support the authors’ mechanistic proposal. They do not isolate an after-decolonization metabolic pathway as a necessary mediator of tumor suppression. Main-text and figure LCA-ratio definitions differ; the current graph appropriately avoids a numerical direction claim. |
| disease | PMID:40433987; Results 2.6; Figure 5 and Figure S5 | supports | The combination arm improves measured tumor, tissue-lipid and inflammatory endpoints in the mouse model. Blood triglyceride reduction is nonsignificant. SI S5 also marks TNF-alpha nonsignificant despite stronger main prose; other inflammatory measurements support the current bounded generic endpoint, not universal significance. |
| data-statement | PMID:40433987; Data Availability Statement | supports | The source names five BioProjects and five OMIX deposits. Public metadata distinguish focal SynCom outputs from human discovery cohorts, prior interventions and a single bacterial genome. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity.taxonomy, environmental_factors, engineering_design; FunctionalRoleEnum.CROSS_FEEDER; EvidenceItem.computational_provenance | supports | Membership excludes the host, antagonist and screened-out candidates. CROSS_FEEDER means use of other taxa’s metabolites and requires role-specific support. Environmental factors are conditions; model design belongs in design and computational provenance. Ecological state is optional, and ENGINEERED is a valid state. |
| ontology | ontology-authority.json; Whole bounded receipt | supports | All five encoded ontology pairs across eight occurrences match local canonical labels; that does not make the domain placeholder a complete roster. |
| semantics | ontology-semantic-notes.json; Whole bounded receipt | supports | The broad GO interaction process and bile-acid class are compatible with the retained scope. The source does not justify choosing a specific obsolete-tryptophan-process replacement. |
| roster-authority | roster-taxonomy-candidates.json; Whole bounded receipt | supports | All seven source species have verified local NCBITaxon candidates. No GTDB mapping, strain identity or functional role follows automatically from these species-label checks. |
| strain-authority | source-strains-and-subspecies-candidate.json; Whole bounded receipt | supports | Seven collection designations come directly from SI. B. animalis subsp. lactis, NCBITaxon:302911, is a separately verified optional finer candidate; no exact strain taxid or catalogue alias is invented. |
| resources | dataset-verification.json; Whole bounded receipt | supports | All five BioProjects and five OMIX metadata pages were verified. PRJNA1214893 and OMIX008965 are focal mouse SynCom metagenomics and metabolomics. Other deposits have different experiment or discovery scopes; MS file counts are not animal counts. |
| si-resources | si-resource-context.json; Whole bounded receipt | supports | Additional OMIX008770 is human serum metabolomics associated through focal SI; its landing page links a related publication. IMG model-input strings remain source-reported, without a cultured-strain equivalence claim. |
| snippets | snippet-audit.json; Whole bounded receipt | supports | All eleven excerpts match the direct cited-source union and pinned cache. Five repeated AOM-DSS excerpts match the direct abstract but differ typographically in the main XML; this is not a fabricated-source finding. |
| history | provenance-audit.json; Whole bounded receipt | supports | Both histories, the exact prior decision and linked issue provenance were assessed. Earlier obsolete-GO removal and graph qualification are retained; historical source limits are not current certification. |
| native-target | support-audit.json; Whole bounded receipt | supports | The native network is COMPLETE with four nodes, one arrow and five node-evidence entries. Completeness and quality scores describe encoded fields and diagnostics, not proof of every biological claim. |
| source-scope | source-audit.json; Whole bounded receipt | supports | Completed source assessment covers the full main, complete scientific SI, critical lead figure inspection and complementary independent root coverage. It does not include raw-data or model reanalysis. |
| independent-source | root-independent-source-audit.json; Whole bounded receipt | supports | Root independently read the full main and SI, viewed all seven main and six SI figures, and agreed with two major and three minor findings. |
| supplement-retrieval | asset-extraction.json; Whole bounded receipt | supports | Validated EPMC ZIP supplied the real DOCX and primary image files after the direct PMC supplement route returned an HTML challenge. |
| supplement-render | supp-image-render.json; Whole bounded receipt | supports | Bounded display derivatives preserve original SI image bytes. All six scientific SI figures were inspected; dense labels were not exhaustively transcribed. |
| adapter | adapter-check.json; Actual optional adapter/runtime discovery | supports | No relevant expression-module dataset was established; no paid provider or model execution was used. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate kb/communities/CRC_Fusobacterium_Control_SynCom.yaml; Actual execution 2026-10-21T14:09:48.820408+00:00 to 2026-10-21T14:09:49.547500+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-strict kb/communities/CRC_Fusobacterium_Control_SynCom.yaml --out /private/tmp/cm-review-session/batch-08/000128/strict-report.tsv; Actual execution 2026-10-21T14:09:48.820552+00:00 to 2026-10-21T14:09:50.612649+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-terms kb/communities/CRC_Fusobacterium_Control_SynCom.yaml; Actual execution 2026-10-21T14:09:48.820604+00:00 to 2026-10-21T14:09:50.404661+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb kb/communities/CRC_Fusobacterium_Control_SynCom.yaml; Actual execution 2026-10-21T14:09:49.554241+00:00 to 2026-10-21T14:09:49.628444+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb-domain kb/communities/CRC_Fusobacterium_Control_SynCom.yaml; Actual execution 2026-10-21T14:09:49.628672+00:00 to 2026-10-21T14:09:50.641125+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-history history/records/CRC_Fusobacterium_Control_SynCom; Actual execution 2026-10-21T14:09:50.404887+00:00 to 2026-10-21T14:09:50.995209+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T14:09:50.995698+00:00 to 2026-10-21T14:09:51.049219+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-references-explained kb/communities/CRC_Fusobacterium_Control_SynCom.yaml; Actual execution 2026-10-21T14:09:51.049412+00:00 to 2026-10-21T14:09:51.845868+00:00 | supports | Reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00 | supports | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00 | supports | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |

## Limits And Additional Notes

- Completed scientific assessment covers current encoded claims and recoverable follow-up; it is not raw-data quality assessment, statistical reproduction, model execution or a full review of every cited prior study.
- No catalogue medium, exact GAM formulation, unreported vessel, atmosphere composition, software version or percent-concentration basis was invented. Model seed sets are not bench formulations.
- All six SI images and critical main figures were inspected at display resolution. Dense molecular labels and primer sequences were not exhaustively validated.
- Wiley returned an access error and the direct PMC supplement route returned an HTML challenge; the real main XML, primary images and validated EPMC supplement ZIP supplied the required source coverage.
- The public archive and culture-source metadata support exact stated scopes only. No raw sequences, clinical records, model payloads or code were executed or reanalysed.
- Eleven existing snippets match the direct cited-source union and cache. Five AOM-DSS excerpts differ typographically in XML but match the direct abstract; this is not a fabricated quotation finding.
- No canonical, cache, history or saved-review edits; no author contact, paid provider or later-target work.
- No canonical, cache, history, generated or saved-review file changed; all 24 inspected inputs remain pinned.
- Eleven existing snippets match the directly retrieved source union and pinned cache. Five repeated abstract excerpts have a harmless hyphen-rendering difference in main XML.
- Completeness 80 and quality 100/raw 101.5 are mechanical scores. Scientific completion describes the bounded claim review, not reproducibility of every source analysis.
- No raw sequence/metabolomics reanalysis, model execution, author contact, paid provider or later-target work.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T141906Z-crc-fusobacterium-syncom-record
kind: record
repository: CultureBotAI/CommunityMech
title: CRC Fusobacterium control SynCom record review
started_at: '2026-10-21T14:09:09.766666Z'
finished_at: '2026-10-21T14:19:06.436697Z'
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
summary: The main paper and supplement support the seven-strain experimental community
  and its qualified four-node, one-arrow graph. Two major findings concern collapsed
  membership/blanket role assignment and unqualified ingredient mediation; three minors
  concern assay provenance, design placement and verified public resources.
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
  - path: history/records/CRC_Fusobacterium_Control_SynCom/2026-10-02T045300Z-codex-f28720.yaml
    sha256: 80d9b88a208f041e3f3b2d96dec3ca62163b628ce273e810cd264de532d48543
    role: context
  - path: history/records/CRC_Fusobacterium_Control_SynCom/2026-10-05T142601Z-codex-96e3db.yaml
    sha256: c8a932deaef0459b0a342998f45e93ed35e37c008eac18bd59dde14d942b49d0
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    sha256: ce036791082c01e1713952a2e090090a3cebce535c994e2b63885bfa5554d8cb
    role: target
  - path: references_cache/PMID_40433987.txt
    sha256: 07e484de7eeff619787c0c8bbb04a61723efe076f69fd932e13169bd5ec1eacb
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
- target_id: CommunityMech:000128
  path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  label: CRC Fusobacterium Control SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
scope:
  description: Entire record, all four nodes and its one PARTIAL arrow assessed against
    complete primary science, critical figures, SI, authority, provenance and native
    checks.
  selection: Only released CommunityMech:000128 in the owned batch 08 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000128
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000128
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused native checks; label and schema validity do not establish
    complete membership or mechanistic support.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000128
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-08/000128/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused native checks; label and schema validity do not establish
    complete membership or mechanistic support.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000128
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused native checks; label and schema validity do not establish
    complete membership or mechanistic support.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000128
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused native checks; label and schema validity do not establish
    complete membership or mechanistic support.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000128
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused native checks; label and schema validity do not establish
    complete membership or mechanistic support.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000128
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/CRC_Fusobacterium_Control_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused native checks; label and schema validity do not establish
    complete membership or mechanistic support.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000128
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused native checks; label and schema validity do not establish
    complete membership or mechanistic support.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000128
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused native checks; label and schema validity do not establish
    complete membership or mechanistic support.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000128
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse, not a focal scientific failure
    or source certification.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000128
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse, not a focal scientific failure
    or source certification.
- check_id: source-identity
  name: Primary and supplement identity
  status: passed
  required: true
  summary: Direct article metadata, complete primary XML and validated supplementary
    archive agree.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - pubmed
  - epmc
  - crossref
  - supplement-retrieval
- check_id: scientific-source
  name: Whole main and critical supplemental verification
  status: passed
  required: true
  summary: Full scientific main and SI, relevant figures and assay/roster/resource
    scopes were assessed; no raw-data reproduction is claimed.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - source-scope
  - independent-source
  - supplement-render
- check_id: cross-mech
  name: Exact cultivation-recipe correspondence
  status: not_applicable
  required: false
  summary: GAM is source-named, but no exact complete formulation/manufacturer is
    verified for a unique CultureMech link.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - strain-culture
  - serial-assembly
  - source-scope
- check_id: structured-adapter
  name: Optional structured expression adapter
  status: unavailable
  required: false
  summary: No applicable expression-module dataset established; bounded runtime discovery
    is preserved.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  locator: Entire record, four interaction nodes and one downstream arrow
  summary: The record describes a seven-member experimental SynCom but represents
    its members by one Bacteria descriptor with a blanket recipient role. The graph
    already distinguishes intervention outcomes from proposed metabolic mediation.
  support: supports
  accessed_at: '2026-10-21T14:19:06.412068Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=40433987&retmode=xml
  locator: Article identity and available abstract
  summary: Direct title, abstract and article identifiers identify the focal SynCom
    paper.
  support: supports
  accessed_at: '2026-10-21T14:09:36.285997Z'
  snapshot_sha256: af681fb1685d9cd1f96dc04f03ce9ff0604a37c73fd13e61565b54d472338835
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40433987%20AND%20SRC:MED&format=json&resultType=core
  locator: Article identity and available abstract
  summary: Direct metadata identifies PMC12376641 and the focal DOI.
  support: supports
  accessed_at: '2026-10-21T14:09:36.613585Z'
  snapshot_sha256: 1625d0f8aa0616c64a5dbeb9fd410d836695dabbc6711c193693f72d180694ad
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1002/advs.202414232
  locator: Article identity and available abstract
  summary: Direct DOI metadata agrees with the primary article identity; metadata
    alone do not certify Methods.
  support: supports
  accessed_at: '2026-10-21T14:09:36.285062Z'
  snapshot_sha256: ffbf8cc091472e7cc0078fca57ec2e17cc57eeae4fd96ad63908e1144103dab6
- evidence_id: members
  kind: primary_source
  reference: PMID:40433987
  locator: Results 2.3–2.4 and Figure 3 caption
  summary: Eight culturable candidates were considered, then B. longum was removed
    for slow growth in GAM. The final seven are B. animalis, L. reuteri, A. muciniphila,
    B. thetaiotaomicron, C. sporogenes, P. distasonis and B. fragilis. F. nucleatum
    is the challenge organism, not an eighth SynCom member.
  support: supports
  accessed_at: '2026-10-21T14:19:06.412747Z'
  snapshot_sha256: 06bcc70c1f72ef40cf14f2f36dd60ef242485e25b6bbde6e1b9647cbb4ab21de
- evidence_id: strain-culture
  kind: primary_source
  reference: PMID:40433987
  locator: 'SI Methods: Bacterial culture and co-culture of SynCom; source culture-collection
    paragraph'
  summary: The supplement gives all seven collection designations and GAM cultivation
    at 37 C anaerobically. Plate tests use adjacent inocula and 96 h incubation; liquid
    serial cultures normalize seeds to OD600 1.0 and transfer every 24 h. These are
    different assay contexts.
  support: supports
  accessed_at: '2026-10-21T14:19:06.419385Z'
  snapshot_sha256: 27b90340c6b8b1b8da61142dded15b0887ddf3b400f37d3e6d7b24b2eaeffe8a
- evidence_id: serial-assembly
  kind: primary_source
  reference: PMID:40433987
  locator: 'SI Methods: four SynCom inoculation proportions, generation transfers
    and SynCom plus Fn'
  summary: SynCom2 is used in the Fn coculture. The first inoculation is 1 mL into
    40 mL medium; later transfers use 0.4 mL into 40 mL fresh medium over six to eight
    generations. Printed SynCom3 component volumes sum to 1.10 mL despite the 1 mL
    wording; this discrepancy must not be silently normalized.
  support: supports
  accessed_at: '2026-10-21T14:19:06.425153Z'
  snapshot_sha256: 27b90340c6b8b1b8da61142dded15b0887ddf3b400f37d3e6d7b24b2eaeffe8a
- evidence_id: model-design
  kind: primary_source
  reference: PMID:40433987
  locator: 'Results 2.3; Experimental Section: design of a minimal microbial community'
  summary: m2m with PathwayTools uses genome annotations and seed inputs to identify
    reachable metabolites and a minimum community. RevEcoR derives competition/complementarity
    indices from KO profiles. These are model-derived design criteria, not direct
    metabolite exchange or an automatically identified flux-balance simulation.
  support: supports
  accessed_at: '2026-10-21T14:19:06.425255Z'
  snapshot_sha256: 06bcc70c1f72ef40cf14f2f36dd60ef242485e25b6bbde6e1b9647cbb4ab21de
- evidence_id: model-inputs
  kind: primary_source
  reference: PMID:40433987
  locator: 'SI Methods: metabolic-network reconstruction, m2m and RevEcoR'
  summary: The supplement gives annotation inputs, seed-set context and reachability/minimum-community
    operations. Source-reported IMG inputs are not independently verified here as
    the exact genomes of the cultured collection strains; model seeds must not be
    treated as the GAM recipe.
  support: supports
  accessed_at: '2026-10-21T14:19:06.431051Z'
  snapshot_sha256: 27b90340c6b8b1b8da61142dded15b0887ddf3b400f37d3e6d7b24b2eaeffe8a
- evidence_id: suppression
  kind: primary_source
  reference: PMID:40433987
  locator: Results 2.4; Figure 4J–L and Figure S4G
  summary: Arginine or tryptophan supplementation reduces acidity and slows Fn decline
    in the coculture. This supports the existing context-dependent suppression description
    and does not establish that added tryptophan enhances suppression.
  support: supports
  accessed_at: '2026-10-21T14:19:06.431171Z'
  snapshot_sha256: 06bcc70c1f72ef40cf14f2f36dd60ef242485e25b6bbde6e1b9647cbb4ab21de
  quote: slowed down the decline of Fn
- evidence_id: animal-design
  kind: primary_source
  reference: PMID:40433987
  locator: 'Experimental Section: Mouse CRC Model; Results 2.5–2.6; Figures 4M–R and
    5A'
  summary: Separate normal-mouse colonization/safety and AOM-DSS disease experiments
    are reported. The disease treatment mixes Fn and SynCom before 200 microlitre
    oral administration. Preparation CFU/mL values are concentrations, not automatically
    per-animal doses. There is no SynCom-only disease-model arm.
  support: supports
  accessed_at: '2026-10-21T14:19:06.431250Z'
  snapshot_sha256: 06bcc70c1f72ef40cf14f2f36dd60ef242485e25b6bbde6e1b9647cbb4ab21de
  quote: SynCom was mixed with Fn
- evidence_id: metabolism
  kind: primary_source
  reference: PMID:40433987
  locator: Results 2.7; Figures 6–7 and Figure S6
  summary: Intervention-associated tryptophan and bile-acid profiles, gene expression
    and correlations support the authors’ mechanistic proposal. They do not isolate
    an after-decolonization metabolic pathway as a necessary mediator of tumor suppression.
    Main-text and figure LCA-ratio definitions differ; the current graph appropriately
    avoids a numerical direction claim.
  support: supports
  accessed_at: '2026-10-21T14:19:06.431323Z'
  snapshot_sha256: 06bcc70c1f72ef40cf14f2f36dd60ef242485e25b6bbde6e1b9647cbb4ab21de
- evidence_id: disease
  kind: primary_source
  reference: PMID:40433987
  locator: Results 2.6; Figure 5 and Figure S5
  summary: The combination arm improves measured tumor, tissue-lipid and inflammatory
    endpoints in the mouse model. Blood triglyceride reduction is nonsignificant.
    SI S5 also marks TNF-alpha nonsignificant despite stronger main prose; other inflammatory
    measurements support the current bounded generic endpoint, not universal significance.
  support: supports
  accessed_at: '2026-10-21T14:19:06.431397Z'
  snapshot_sha256: 06bcc70c1f72ef40cf14f2f36dd60ef242485e25b6bbde6e1b9647cbb4ab21de
- evidence_id: data-statement
  kind: primary_source
  reference: PMID:40433987
  locator: Data Availability Statement
  summary: The source names five BioProjects and five OMIX deposits. Public metadata
    distinguish focal SynCom outputs from human discovery cohorts, prior interventions
    and a single bacterial genome.
  support: supports
  accessed_at: '2026-10-21T14:19:06.431469Z'
  snapshot_sha256: 06bcc70c1f72ef40cf14f2f36dd60ef242485e25b6bbde6e1b9647cbb4ab21de
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity.taxonomy, environmental_factors, engineering_design;
    FunctionalRoleEnum.CROSS_FEEDER; EvidenceItem.computational_provenance
  summary: Membership excludes the host, antagonist and screened-out candidates. CROSS_FEEDER
    means use of other taxa’s metabolites and requires role-specific support. Environmental
    factors are conditions; model design belongs in design and computational provenance.
    Ecological state is optional, and ENGINEERED is a valid state.
  support: supports
  accessed_at: '2026-10-21T14:19:06.431531Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded receipt
  summary: All five encoded ontology pairs across eight occurrences match local canonical
    labels; that does not make the domain placeholder a complete roster.
  support: supports
  accessed_at: '2026-10-21T14:19:06.431757Z'
  snapshot_sha256: d33f72023fd6edb92f8c2f269f932514967df84051fef09a5fa6b1f7282b2073
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole bounded receipt
  summary: The broad GO interaction process and bile-acid class are compatible with
    the retained scope. The source does not justify choosing a specific obsolete-tryptophan-process
    replacement.
  support: supports
  accessed_at: '2026-10-21T14:19:06.431935Z'
  snapshot_sha256: cc665b1f23db01630cc39d67f127d0e120f5b7c9ff41f1ced65321e9749e95c2
- evidence_id: roster-authority
  kind: authority
  reference: roster-taxonomy-candidates.json
  locator: Whole bounded receipt
  summary: All seven source species have verified local NCBITaxon candidates. No GTDB
    mapping, strain identity or functional role follows automatically from these species-label
    checks.
  support: supports
  accessed_at: '2026-10-21T14:19:06.432373Z'
  snapshot_sha256: 3a83bf62ca1635326dc061100ee0ce1dd86d639196e184731626e6b74a0fb964
- evidence_id: strain-authority
  kind: authority
  reference: source-strains-and-subspecies-candidate.json
  locator: Whole bounded receipt
  summary: Seven collection designations come directly from SI. B. animalis subsp.
    lactis, NCBITaxon:302911, is a separately verified optional finer candidate; no
    exact strain taxid or catalogue alias is invented.
  support: supports
  accessed_at: '2026-10-21T14:19:06.432526Z'
  snapshot_sha256: a531e06e66ec8802ba785362269607ee26b86be6ae76d761e505b19c5d70e1ab
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded receipt
  summary: All five BioProjects and five OMIX metadata pages were verified. PRJNA1214893
    and OMIX008965 are focal mouse SynCom metagenomics and metabolomics. Other deposits
    have different experiment or discovery scopes; MS file counts are not animal counts.
  support: supports
  accessed_at: '2026-10-21T14:19:06.432687Z'
  snapshot_sha256: 6c80d12ea8119b5f2e3f7f461ffc9e40477c1b40ded29ff7488bdb6e8d632860
- evidence_id: si-resources
  kind: database
  reference: si-resource-context.json
  locator: Whole bounded receipt
  summary: Additional OMIX008770 is human serum metabolomics associated through focal
    SI; its landing page links a related publication. IMG model-input strings remain
    source-reported, without a cultured-strain equivalence claim.
  support: supports
  accessed_at: '2026-10-21T14:19:06.432898Z'
  snapshot_sha256: 297b9b17f1a0ced9c4ef7862efe57a957a78a387af3cfed602a083298e915ed5
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded receipt
  summary: All eleven excerpts match the direct cited-source union and pinned cache.
    Five repeated AOM-DSS excerpts match the direct abstract but differ typographically
    in the main XML; this is not a fabricated-source finding.
  support: supports
  accessed_at: '2026-10-21T14:19:06.433093Z'
  snapshot_sha256: 3ce681eecbf5d472b0152be65ff8ac6b3148ed941720d6e0c01980e464e4cf09
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded receipt
  summary: Both histories, the exact prior decision and linked issue provenance were
    assessed. Earlier obsolete-GO removal and graph qualification are retained; historical
    source limits are not current certification.
  support: supports
  accessed_at: '2026-10-21T14:19:06.433298Z'
  snapshot_sha256: 6fae65cca47fc512e87b191ba9405dabe0bfc8bd0156b6cb2c13f0c9eca05c77
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded receipt
  summary: The native network is COMPLETE with four nodes, one arrow and five node-evidence
    entries. Completeness and quality scores describe encoded fields and diagnostics,
    not proof of every biological claim.
  support: supports
  accessed_at: '2026-10-21T14:19:06.433329Z'
  snapshot_sha256: 3e886727a928066ce339d594f15421d545aaee077e9096d6098ed92b51b53395
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded receipt
  summary: Completed source assessment covers the full main, complete scientific SI,
    critical lead figure inspection and complementary independent root coverage. It
    does not include raw-data or model reanalysis.
  support: supports
  accessed_at: '2026-10-21T14:19:06.433355Z'
  snapshot_sha256: 7e9fd043cc474de656260ed511ead9400342d253744dd9185e52912618b5e526
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded receipt
  summary: Root independently read the full main and SI, viewed all seven main and
    six SI figures, and agreed with two major and three minor findings.
  support: supports
  accessed_at: '2026-10-21T14:19:06.433490Z'
  snapshot_sha256: 25064e6322f0a5f8d2d8db938448e260507a8426564d6665dc353c15dd9fa786
- evidence_id: supplement-retrieval
  kind: validation
  reference: asset-extraction.json
  locator: Whole bounded receipt
  summary: Validated EPMC ZIP supplied the real DOCX and primary image files after
    the direct PMC supplement route returned an HTML challenge.
  support: supports
  accessed_at: '2026-10-21T14:19:06.433628Z'
  snapshot_sha256: 98125e65b1d64bcc3fb7d5cbb5783124d0283e00c3310ec332ba7f7dd7d17bcb
- evidence_id: supplement-render
  kind: validation
  reference: supp-image-render.json
  locator: Whole bounded receipt
  summary: Bounded display derivatives preserve original SI image bytes. All six scientific
    SI figures were inspected; dense labels were not exhaustively transcribed.
  support: supports
  accessed_at: '2026-10-21T14:19:06.433755Z'
  snapshot_sha256: 1054e8b12a4fd11d69cb4e6ede217e385b8c3b3de06f2043d642a6fa9d9199c5
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Actual optional adapter/runtime discovery
  summary: No relevant expression-module dataset was established; no paid provider
    or model execution was used.
  support: supports
  accessed_at: '2026-10-21T14:19:06.433890Z'
  snapshot_sha256: 72324cd7427873cb63b0ef269467dba2a5960cdcc3060157e6378506538f68e1
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  locator: Actual execution 2026-10-21T14:09:48.820408+00:00 to 2026-10-21T14:09:49.547500+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T14:09:49.547500Z'
  snapshot_sha256: f956024e23a00ffedcbeb1a0279117b7ce13d31439a39277f41281f5e35e16e6
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-08/000128/strict-report.tsv
  locator: Actual execution 2026-10-21T14:09:48.820552+00:00 to 2026-10-21T14:09:50.612649+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T14:09:50.612649Z'
  snapshot_sha256: f9fa0151553e57a8c6ac1484680a4ebd5e42d5777627e51b421fd6df04541d58
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  locator: Actual execution 2026-10-21T14:09:48.820604+00:00 to 2026-10-21T14:09:50.404661+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T14:09:50.404661Z'
  snapshot_sha256: 9ecddc6cba0a70641c5ab2edeb53b6d21813a828ca8955117c9d46fc8b1cfc0e
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  locator: Actual execution 2026-10-21T14:09:49.554241+00:00 to 2026-10-21T14:09:49.628444+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T14:09:49.628444Z'
  snapshot_sha256: 919dc050d4649d67adc095b30f071d564596b5b5d434fdb46d306160a421f712
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  locator: Actual execution 2026-10-21T14:09:49.628672+00:00 to 2026-10-21T14:09:50.641125+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T14:09:50.641125Z'
  snapshot_sha256: 22506ccb118081c788145b8a76eb1744c0e509c150654f9f2cccadc2980509f9
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/CRC_Fusobacterium_Control_SynCom
  locator: Actual execution 2026-10-21T14:09:50.404887+00:00 to 2026-10-21T14:09:50.995209+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T14:09:50.995209Z'
  snapshot_sha256: fcb856cfcf6764c19936f32c85b118351d5a3a7e21b5336b8fffadd9423c6f64
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T14:09:50.995698+00:00 to 2026-10-21T14:09:51.049219+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T14:09:51.049219Z'
  snapshot_sha256: f3267976c9927a54508aa511a4d31d1ab191e47e37c17e9f6dde3a3a2119494e
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
  locator: Actual execution 2026-10-21T14:09:51.049412+00:00 to 2026-10-21T14:09:51.845868+00:00
  summary: Reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T14:09:51.845868Z'
  snapshot_sha256: c4ba109a11e25dabf45e0a72d42e513f0ec3125e75908e77d8339d5750073336
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
  topic: Final seven-member SynCom and external challenge
  outcome: concern
  summary: The community identity is clear, but the Bacteria placeholder omits seven
    recoverable species and strain designations.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - record
  - members
  - strain-culture
  - roster-authority
  - strain-authority
  dimensions:
  - name: community_scope
    value: Seven selected commensal strains
    definition: B. longum was excluded; F. nucleatum and the mouse are outside the
      final membership.
    evidence_ids:
    - members
    - strain-culture
  - name: taxon_rank
    value: Current domain descriptor; seven verified species candidates available
    definition: The valid Bacteria ID is insufficiently specific for a defined seven-species
      assembly.
    evidence_ids:
    - ontology
    - roster-authority
  - name: strain
    value: Seven source-reported collection designations
    definition: Exact SI culture names are available; reference annotation inputs
      are not assumed identical to cultures.
    evidence_ids:
    - strain-authority
    - model-inputs
  - name: grounding_status
    value: Re-ground each restored member independently
    definition: Do not copy the Bacteria-domain GTDB mapping to species descriptors
      or infer unique mappings.
    evidence_ids:
    - ontology
    - roster-authority
  - name: environment
    value: Colon host context plus separate laboratory cultures
    definition: UBERON colon is compatible with the in-vivo arm; it is not the physical
      medium of bench culture.
    evidence_ids:
    - animal-design
    - strain-culture
  - name: medium
    value: Anaerobic GAM and separately specified modified/supplemented assays
    definition: Model seed sets, bench formulations and animal dosing are distinct.
    evidence_ids:
    - serial-assembly
    - model-inputs
    - suppression
  - name: evidence_tier
    value: Direct primary main, complete scientific supplement and authority metadata
    definition: No raw-omics reanalysis or experimental reproduction.
    evidence_ids:
    - source-scope
    - independent-source
- assessment_id: state
  area: scope
  topic: State, origin and category
  outcome: supported
  summary: Retain ENGINEERED, SYNTHETIC and OTHER for the deliberately designed experimental
    SynCom.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - schema
  - members
  - model-design
  details: The study combines computational selection with experimental assembly.
    These labels do not assert an engineered genotype or ecological equilibrium. Ecological
    state remains a separate optional field.
- assessment_id: roles
  area: evidence
  topic: Blanket CROSS_FEEDER role
  outcome: concern
  summary: Community design and validation do not establish that all seven members
    utilize metabolites from other taxa.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - schema
  - record
  - model-design
  - model-inputs
  details: Recover member-specific role evidence and distinguish model-predicted complementarity
    from observed substrate transfer. The model can support a qualified hypothesis
    where a particular member and interaction are identified; a generic membership
    excerpt cannot support a domain-wide recipient assignment. No specific tracer
    assay is required and cross-feeding is not declared biologically absent.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain low modeled competition and observed colonization with the current
    causal qualification.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - model-design
  - animal-design
  details: Low competition is a model selection criterion, not measured niche partitioning.
    Normal-mouse colonization/safety and CRC-model measurements are separate source
    contexts. Add the relevant narrow evidence rather than letting the generic design-validation
    abstract excerpt support every part. No colonization-to-suppression arrow is restored.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain context-dependent Fn suppression without reciprocal-negative competition
    or established-infection eradication.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - suppression
  - animal-design
  - record
  details: The source reports in-vitro and in-vivo measurements. Its broad competition
    terminology does not require the schema COMPETITION type. Amino-acid supplementation
    slows Fn decline, and pH/qPCR wording remains bounded. Co-gavage cannot isolate
    clearance of a pre-established infection.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: Retain intervention-associated metabolic changes and the explicit PARTIAL
    interpretation.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - metabolism
  - record
  details: Correlations and expression are not necessary-mediation tests. Preserve
    the main/figure LCA-ratio discrepancy and do not infer a numerical conversion
    direction from conflicting definitions. Bile-acid class and L-tryptophan identifiers
    match the intended broad entities.
- assessment_id: node-3
  area: graph
  topic: ecological_interactions[3]
  outcome: supported
  summary: Retain measured mouse disease endpoints with the current clinical and significance
    limits.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - disease
  - animal-design
  details: The source supports bounded tumor, tissue-lipid and inflammatory outcomes.
    It does not support universal biomarker improvement, significant blood-triglyceride
    reduction or human clinical efficacy. The nonsignificant S5 TNF-alpha panel does
    not invalidate the generic endpoint supported by other inflammatory measurements.
- assessment_id: arrow-2-3
  area: graph
  topic: ecological_interactions[2].downstream[0]
  outcome: supported
  summary: Keep the proposed metabolism-to-disease link explicitly PARTIAL.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - metabolism
  - animal-design
  - history
  details: Concurrent changes and the conceptual model motivate the authors’ hypothesis
    but do not isolate required mediation. Preserve the single arrow and keep previously
    removed colonization-to-suppression and suppression-to-metabolism links absent.
- assessment_id: ingredient
  area: evidence
  topic: related_ingredients[0]
  outcome: concern
  summary: The ingredient prose asserts a temporal and causal chain that the graph
    correctly qualifies.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - record
  - metabolism
  - suppression
  - animal-design
  details: Replace after-decolonization restoration and tumor-suppression mediation
    with intervention-associated metabolism and an explicitly proposed contribution.
    The amino-acid supplementation result must not be inverted into evidence that
    adding tryptophan promotes pathogen suppression.
- assessment_id: cultivation
  area: completeness
  topic: Recoverable assay and model context
  outcome: concern
  summary: The main and SI provide additional reproducible context beyond the current
    GAM/anaerobic statement.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - strain-culture
  - serial-assembly
  - model-design
  - model-inputs
  - animal-design
  details: Record 37 C and distinguish 96 h plate tests, normalized-seed liquid serial
    cultures, the SynCom2 plus Fn experiment and animal gavage. Initial 1 mL into
    40 mL and later 0.4 mL into 40 mL are not a universal 40 mL final volume. Preserve
    the printed SynCom3 1.10 mL inconsistency and unspecified percentage basis/complete
    mGAM recipe. Model reachability inputs belong in computational provenance, not
    growth-medium composition.
- assessment_id: environmental-placement
  area: representation
  topic: environmental_factors[0]
  outcome: concern
  summary: Network reconstruction and low-competition selection are design/provenance
    content, not environmental conditions.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - record
  - schema
  - model-design
  details: Consolidate this content under the existing engineering design and appropriate
    computational evidence. Do not delete the supported design information or replace
    it with an invented condition.
- assessment_id: resources
  area: provenance
  topic: Named public resource omissions
  outcome: concern
  summary: Verified focal SynCom metagenomics and metabolomics resources are absent
    from the record.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - data-statement
  - resources
  - si-resources
  details: Prioritize PRJNA1214893 and OMIX008965. Keep discovery cohorts, earlier
    interventions, the B. animalis genome and human serum context distinct. Some project
    titles specify 16S despite the paper’s aggregate sequencing label; no blanket
    shotgun annotation is justified. File counts are not independent sample or animal
    counts.
- assessment_id: history
  area: provenance
  topic: Previous repairs and current source coverage
  outcome: supported
  summary: Retain graph and obsolete-GO repairs while updating the recoverable roster
    and source-context gaps.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - history
  - snippets
  - semantics
  details: The old decision used full main/captions without figures or supplements.
    The current assessment adds those sources without rewriting historical scope.
    GO:0006568 remains absent; no unsupported biosynthesis/catabolism alternative
    is selected. Eleven direct-source snippet matches do not by themselves validate
    the attached blanket role or causal explanation.
- assessment_id: validation
  area: schema
  topic: Native checks and source-specific review
  outcome: supported
  summary: Eight focused native gates pass; source-backed identity, causal and provenance
    findings remain.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - ontology
  - check-validate
  - check-validate-references-explained
  - source-scope
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Scores measure current encoded fields and diagnostics, not biological certainty.
  target_ids:
  - CommunityMech:000128
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role score + 5 environment + 10 for at least
      three interaction nodes + 10 growth media + 5 metabolites. No three-factor,
      external-resource or dataset bonus.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 − 50P1 − 10P2 − 2P3 + 20min(mean node evidence/2,1) + 15
      if COMPLETE,0,100). P1=0/P2=2/P3=3/P4=0; five evidence/four nodes gives 12.5;
      COMPLETE adds 15; raw 101.5 capped 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 2
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
- finding_id: recover-members-and-roles
  issue_key: cm-000128-recover-members-and-roles
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: 'P2: recoverable defined-community membership and role evidence
    are missing at the maintained taxonomy surface; the intended community remains
    identifiable, so this is not a blocking wrong-record identity.'
  rule_id: review-checklist.claim-specific-identity-evidence-and-provenance
  status: open
  certainty: confirmed
  title: Recover the seven-member roster and individual role support
  description: The single Bacteria descriptor omits seven directly identified species
    and collection strains. Its blanket CROSS_FEEDER role is attached to a generic
    design/validation excerpt, which does not establish use of other taxa’s metabolites
    by every member. The source resolves membership, so the broad placeholder and
    unqualified role are materially incomplete.
  target_ids:
  - CommunityMech:000128
  field_paths:
  - taxonomy[0].taxon_term
  - taxonomy[0].functional_role
  - taxonomy[0].evidence
  - taxonomy
  evidence_ids:
  - members
  - strain-culture
  - schema
  - roster-authority
  - strain-authority
  - model-design
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
- finding_id: ingredient-mediation
  issue_key: cm-000128-ingredient-mediation
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: mechanistic and temporal overstatement remains outside
    a correctly bounded graph; retain the hypothesis with accurate qualification rather
    than declaring it absent.'
  rule_id: review-checklist.claim-specific-identity-evidence-and-provenance
  status: open
  certainty: confirmed
  title: Qualify the ingredient’s temporal and causal interpretation
  description: The L-tryptophan relevance and evidence explanation assert metabolic
    restoration after Fn displacement and a role in suppressing tumor growth. The
    experiments show intervention-associated changes and support a proposed mechanism;
    they do not isolate that temporal/causal chain. This non-graph wording contradicts
    the carefully qualified graph.
  target_ids:
  - CommunityMech:000128
  field_paths:
  - related_ingredients[0].relevance
  - related_ingredients[0].evidence[0].supports
  - related_ingredients[0].evidence[0].explanation
  evidence_ids:
  - metabolism
  - animal-design
  - suppression
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
- finding_id: assay-provenance
  issue_key: cm-000128-assay-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded recoverable context and evidence placement improve
    reproducibility without invalidating the retained experimental outcomes or requiring
    an invented full recipe.'
  rule_id: review-checklist.claim-specific-identity-evidence-and-provenance
  status: open
  certainty: confirmed
  title: Recover model, culture and evidence context
  description: The current record gives GAM and anaerobiosis but omits available source-specific
    temperature, assembly/transfer context and model provenance. Generic IN_VIVO design
    evidence also stands in for several distinct computational, bench and animal claims.
  target_ids:
  - CommunityMech:000128
  field_paths:
  - growth_media[0]
  - cultivation_setup
  - engineering_design
  - engineering_design.evidence[0]
  - ecological_interactions[0].evidence
  - ecological_interactions[1].evidence
  evidence_ids:
  - strain-culture
  - serial-assembly
  - model-design
  - model-inputs
  - animal-design
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
- finding_id: design-placement
  issue_key: cm-000128-design-placement
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: field-placement inconsistency with a direct, bounded
    correction; no scientific content needs to be discarded.'
  rule_id: review-checklist.claim-specific-identity-evidence-and-provenance
  status: open
  certainty: confirmed
  title: Move network design out of environmental conditions
  description: environmental_factors[0] describes metabolic-network reconstruction
    and SynCom selection, rather than an environmental condition. The supported information
    already belongs with engineering design and computational evidence.
  target_ids:
  - CommunityMech:000128
  field_paths:
  - environmental_factors[0]
  - engineering_design
  evidence_ids:
  - record
  - schema
  - model-design
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
- finding_id: focal-resources
  issue_key: cm-000128-focal-resources
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: specific verified resource omissions; no unverified accession,
    raw-data quality judgment or generic dataset-absence claim is made.'
  rule_id: review-checklist.claim-specific-identity-evidence-and-provenance
  status: open
  certainty: confirmed
  title: Link verified focal SynCom datasets
  description: The record omits directly identified public metagenomics and metabolomics
    deposits. PRJNA1214893 and OMIX008965 specifically describe the focal SynCom intervention,
    whereas other source-listed deposits have distinct discovery, prior-intervention
    or genome scopes.
  target_ids:
  - CommunityMech:000128
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - data-statement
  - resources
  - si-resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
actions:
- action_id: restore-roster
  description: Replace the domain placeholder with source-specific final membership
    and narrowly supported roles.
  finding_ids:
  - recover-members-and-roles
  target_ids:
  - CommunityMech:000128
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Represent Bifidobacterium animalis, NCBITaxon:28025, CGMCC 1.15623; Limosilactobacillus
    reuteri, NCBITaxon:1598, GDMCC 1.614; Akkermansia muciniphila, NCBITaxon:239935,
    GDMCC 1.1346; Bacteroides thetaiotaomicron, NCBITaxon:818, GDMCC 1.1104; Clostridium
    sporogenes, NCBITaxon:1509, GDMCC 1.1481; Parabacteroides distasonis, NCBITaxon:823,
    GDMCC 1.1564; and Bacteroides fragilis, NCBITaxon:817, GDMCC 1.385. Use current
    canonical labels and direct SI evidence for collection names.
  - B. animalis subsp. lactis, NCBITaxon:302911, is an optional supported finer candidate;
    preserve the distinction between source strain designation, species/subspecies
    authority and a verified strain taxid. Do not invent exact strain identifiers
    or catalogue aliases.
  - Keep Fn CGMCC 1.2526 as the external challenge and B. longum CGMCC 1.5082 as an
    excluded candidate, not final members. The mouse is not a microbial member.
  - Re-ground GTDB separately for each restored member; do not reuse the Bacteria-domain
    classification. Attach role-specific evidence and explicit computational qualifiers
    where supported; otherwise omit unsupported categorical roles rather than copying
    CROSS_FEEDER to every species.
  - Retain four community-level nodes and the one PARTIAL arrow; roster completion
    does not require new mechanistic edges. Re-run native term, GTDB/domain, strict/schema
    and reference checks after separately authorized curation.
- action_id: qualify-ingredient
  description: Align ingredient relevance and evidence with intervention-associated
    metabolism and the existing hypothesis-level graph.
  finding_ids:
  - ingredient-mediation
  target_ids:
  - CommunityMech:000128
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Remove the unestablished after-displacement sequence from related_ingredients[0].relevance
    and explanation. Describe altered tryptophan metabolism under SynCom treatment,
    with a proposed contribution to disease outcomes.
  - Use PARTIAL support for the proposed metabolic mediation when retaining that interpretation,
    or separate a directly supported measured-outcome statement from the mechanistic
    hypothesis. A stronger source sentence does not remove the experiment’s causal
    limits.
  - 'Preserve the existing supplementation result: added arginine/tryptophan reduces
    acidity and slows Fn decline. Do not claim that tryptophan supplementation itself
    improves suppression.'
  - Keep the existing co-gavage, missing SynCom-only CRC arm and LCA-ratio limitations,
    and preserve the graph’s single PARTIAL metabolic-response-to-disease arrow.
- action_id: recover-assay-context
  description: Add bounded experimental and computational provenance from the main
    and supplement.
  finding_ids:
  - assay-provenance
  target_ids:
  - CommunityMech:000128
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Add source-supported 37 C anaerobic GAM cultivation. Separate 96 h plate compatibility
    assays from serial liquid cultures and the animal intervention; do not import
    centrifugation as incubation or invent vessel, shaking, gas composition or a complete
    GAM recipe.
  - Document OD600 1.0 normalized seeds, four assembly variants and the use of SynCom2
    with Fn. Initial 1 mL into 40 mL medium and subsequent 0.4 mL into 40 mL fresh
    medium every 24 h over six to eight generations require their own scope. Do not
    label 40 mL a verified final working volume.
  - Preserve the printed SynCom3 1.10 mL sum versus 1 mL wording as a source discrepancy.
    Do not silently normalize it or infer the mass/volume basis of the 1% amino-acid
    supplements.
  - Separate m2m/PathwayTools reachability/minimum-community design from RevEcoR KO-based
    competition/complementarity. Attach available ComputationalProvenance to COMPUTATIONAL
    evidence without calling the workflow FBA, measured transfer or an executed reproduction.
  - Use narrow IN_VITRO and IN_VIVO evidence for their respective outcomes; distinguish
    normal-mouse colonization/safety from the AOM-DSS experiment. Preserve 200 microlitre
    co-gavage and preparation concentrations without converting them into unverified
    per-animal CFU doses.
  - Update the current knowledge-gap discussion to acknowledge recovered roster/SI
    context while retaining unresolved mechanistic questions and prior historical
    scope. Source-only pH, LCA and nonsignificant-marker inconsistencies do not require
    unsupported new graph claims.
- action_id: move-design
  description: Consolidate the supported network-design statement under the appropriate
    existing structure.
  finding_ids:
  - design-placement
  target_ids:
  - CommunityMech:000128
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Remove or relocate environmental_factors[0] as a design item, preserving its supported
    content in engineering_design and appropriate computational evidence.
  - Keep actual laboratory or host conditions distinct from model selection criteria.
    Do not add a placeholder condition merely to preserve completeness points.
- action_id: link-focal-data
  description: Add exact public resources with publication, cohort and assay scope.
  finding_ids:
  - focal-resources
  target_ids:
  - CommunityMech:000128
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/CRC_Fusobacterium_Control_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Link PRJNA1214893 as focal mouse fecal metagenomics after SynCom intervention
    and OMIX008965 as focal mouse fecal metabolomics after SynCom. Use the verified
    public metadata and main Data Availability Statement.
  - If including other deposits, label PRJNA1079906 and OMIX008762 as human fecal
    discovery; PRJNA1086363/1086371 as their separately described interventions with
    archive titles specifying 16S; PRJNA1182847 as the B. animalis genome; OMIX008772/008761
    as B. animalis metabolomics; and OMIX008758 as UDCA context. Do not relabel all
    as seven-member SynCom data.
  - Treat OMIX008770 separately as SI-linked human serum metabolomics whose landing
    page links a related publication; keep that association explicit. Source-reported
    IMG identifiers do not establish cultured-strain genome equivalence.
  - Do not treat positive/negative MS file counts as animal counts or metadata verification
    as raw-data validation. Re-run resource/reference checks after separately authorized
    curation.
limitations:
- Completed scientific assessment covers current encoded claims and recoverable follow-up;
  it is not raw-data quality assessment, statistical reproduction, model execution
  or a full review of every cited prior study.
- No catalogue medium, exact GAM formulation, unreported vessel, atmosphere composition,
  software version or percent-concentration basis was invented. Model seed sets are
  not bench formulations.
- All six SI images and critical main figures were inspected at display resolution.
  Dense molecular labels and primer sequences were not exhaustively validated.
- Wiley returned an access error and the direct PMC supplement route returned an HTML
  challenge; the real main XML, primary images and validated EPMC supplement ZIP supplied
  the required source coverage.
- The public archive and culture-source metadata support exact stated scopes only.
  No raw sequences, clinical records, model payloads or code were executed or reanalysed.
- Eleven existing snippets match the direct cited-source union and cache. Five AOM-DSS
  excerpts differ typographically in XML but match the direct abstract; this is not
  a fabricated quotation finding.
- No canonical, cache, history or saved-review edits; no author contact, paid provider
  or later-target work.
notes:
- No canonical, cache, history, generated or saved-review file changed; all 24 inspected
  inputs remain pinned.
- Eleven existing snippets match the directly retrieved source union and pinned cache.
  Five repeated abstract excerpts have a harmless hyphen-rendering difference in main
  XML.
- Completeness 80 and quality 100/raw 101.5 are mechanical scores. Scientific completion
  describes the bounded claim review, not reproducibility of every source analysis.
- No raw sequence/metabolomics reanalysis, model execution, author contact, paid provider
  or later-target work.
tags:
- record-review
- crc
- fusobacterium
- syncom
- source-complete
- batch-08
```
