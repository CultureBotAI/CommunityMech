# California grassland precipitation legacy soil community review

- Review: 20261021T153033Z-california-grassland-precipitation-legacy-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T15:18:22.190378Z
- Finished UTC: 2026-10-21T15:30:33.089057Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full scientific main, figures and scoped supplements support the natural soil identity and qualified three-node, two-arrow graph. Two major findings concern trophic-role scope and stronger non-graph chemical/mechanistic claims. Two minor findings concern field/laboratory metadata and omitted public resources. Existing graph hypotheses and measurement limits remain intact.

## Scope And Provenance

Whole canonical record and every node/arrow assessed using direct primary main, figures, scoped supplements, authority/archive evidence and actual native checks.

Selection: Only released CommunityMech:000215 in the owned batch 09 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f491097e6f3cd52baf6c2e89b3e614756ebce558.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000215 | kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml | maintained | California Grassland Precipitation Legacy Soil Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000215 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000215 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000215 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000215 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000215 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000215 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000215 | Read-only cache-name preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000215 | Reference validation passed; independent matching separates eleven abstract and nine body excerpts. |
| audit-network | failed | True | CommunityMech:000215 | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000215 | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |
| Primary scientific review | passed | True | CommunityMech:000215 | Whole scientific main, six main figures, seven scientific SI figures and bounded workbook fields assessed against all current nodes and arrows. |
| Public resource identity | passed | True | CommunityMech:000215 | All declared project identities and bounded Figshare/repository metadata verified. |
| Scientific supplements | passed | True | CommunityMech:000215 | All seven scientific SI images/captions and selected workbook data read to declared scope. |
| Ancillary video abstract | skipped | False | CommunityMech:000215 | XML identifies a Video Abstract and the archive preserves MP4 files. Videos were not viewed; no encoded claim depends on their content. |
| Raw omics and statistical reproduction | skipped | False | CommunityMech:000215 | No raw sequence analysis, formula reassignment, pathway-flux analysis, PLSR refitting or significance test was performed. |
| Optional structured expression adapter | unavailable | False | CommunityMech:000215 | No applicable expression-module evidence established through bounded runtime discovery. |

## Scientific And Domain Assessments

### Natural soil community, membership and evidence scope

identity: concern. Targets: CommunityMech:000215.

The source identity is correct; recover representative membership and separate roles from measurement coverage.

### State, origin and category

scope: supported. Targets: CommunityMech:000215.

Retain PERTURBED, NATURAL and the carbon-storage research category.

Natural origin is compatible with field manipulation and laboratory wet-up. CARBON_SEQUESTRATION labels the research topic; it does not prove measured net carbon fixation, storage gain or multiyear carbon-stock loss. No alternate ecological_state is required.

### taxonomy[0].functional_role and evidence

evidence: concern. Targets: CommunityMech:000215.

The flat SECONDARY_FERMENTER assignment exceeds the demonstrated source-specific trophic relation.

Fermentation annotations exist, so their absence is not the rationale. The missing relation is fermentation of products established to come from primary degraders. Omit the optional enum unless narrow evidence supports it; do not require the primary degrader to be a different species. PRIMARY_DEGRADER may remain an explicitly qualified aggregate interpretation with pathway-specific evidence, not a property assigned to every bacterial member.

### ecological_interactions[0]: Necromass Recycling at High Community Growth Efficiency

graph: supported. Targets: CommunityMech:000215.

Retain the existing HYPOTHESIZED interpretation and PARTIAL evidence.

Amino-acid and peptidoglycan synthesis and aromatic-degradation associations motivate the source hypothesis. The chemical classes and GO annotations do not establish identified exchange molecules, substrate uptake or pathway flux.

### ecological_interactions[1]: Plant Detritus Degradation at Low Community Growth Efficiency

graph: supported. Targets: CommunityMech:000215.

Retain the qualified allocation interpretation.

Carbohydrate/lipid transcript patterns can support the reported hypothesis of detritus use and maintenance. They do not directly measure membrane-repair activity or detritus-specific degradation flux.

### ecological_interactions[2]: Precipitation-Legacy Turnover Suppression

graph: supported. Targets: CommunityMech:000215.

Retain the laboratory turnover observation with its current measurement limits.

The node correctly limits the treatment to one winter season, qSIP to bacteria/archaea, CO2 to a nonsignificant difference and CGE to a normalized proxy. Neither fungi nor multiyear carbon stocks inherit the turnover result.

### ecological_interactions[2].downstream[0]

graph: supported. Targets: CommunityMech:000215.

Retain only the HYPOTHESIZED link to Necromass Recycling at High Community Growth Efficiency.

Shared treatment responses and the conceptual model do not isolate this pathway as a causal mediator. No new arrow, transferred compound, donor/recipient identity or mechanistic necessity is warranted.

### ecological_interactions[2].downstream[1]

graph: supported. Targets: CommunityMech:000215.

Retain only the HYPOTHESIZED link to Plant Detritus Degradation at Low Community Growth Efficiency.

Shared treatment responses and the conceptual model do not isolate this pathway as a causal mediator. No new arrow, transferred compound, donor/recipient identity or mechanistic necessity is warranted.

### description and environmental_factors[2]

evidence: concern. Targets: CommunityMech:000215.

Apply the graph’s proxy and hypothesis qualifications consistently outside the graph.

The overview describes source-derived compounds and consumption more definitively than the measurements permit. Attribute the necromass/plant-origin and allocation interpretations, distinguish treatment-unique formula distributions from whole SOC, and move the compositional response out of environmental conditions. Explain the source-defined relative CGE metric rather than a generic biomass/respiration ratio.

### Field season, laboratory evidence, baseline and cultivation geometry

completeness: concern. Targets: CommunityMech:000215.

Correct bounded duration, vessel-volume and evidence-context inconsistencies while retaining the detailed soil protocol.

One October 2017–May 2018 season is not multiple winters. The 15 mL vial capacity is not a working volume and cannot be replaced with the 1 mL water addition or 5 g soil mass. Time zero precedes wet-up. Field pH 5.9 may be recorded as site characterization, while laboratory pH and numerical room temperature remain unspecified. Keep controller fields unset and preserve the bracket-parser workaround.

### associated_datasets and external_resources

provenance: concern. Targets: CommunityMech:000215.

Add the directly verified public data and code resources with assay-specific scope.

Separate metagenomics, 16S, transcriptomics, FTICR/CO2 and analysis code. Forty-seven transcriptome project identifiers are not a validated sample count; twelve Figshare file entries include a metadata-system file and do not mean twelve scientific datasets. No raw data or code was executed.

### Prior graph repair and current public issues

provenance: supported. Targets: CommunityMech:000215.

Preserve the existing graph repair and unresolved non-graph follow-up.

Issue 1274 already identifies duration and vessel capacity; no duplicate issue is proposed. Issue 1272’s closure covers graph repair rather than the present non-graph claims. The full MD body and abstract-only TXT are independently recognized despite stale MD frontmatter. No canonical history, status or cache is changed.

### Native and authority checks

schema: supported. Targets: CommunityMech:000215.

All eight focused native checks pass; two major and two minor source-specific findings remain.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000215.

Mechanical completeness is high but does not certify the scientific claims.

## Findings

### membership-role-scope: Reconcile broad membership and unsupported secondary fermentation

major / open / confirmed; issue key: cm-000215-membership-role-scope.

The single Bacteria entry carries SECONDARY_FERMENTER on a membership excerpt. Fermentation-related annotations do not establish the required primary-degrader-product relation. The full source also resolves Archaea and representative bacterial phyla beyond the abstract-only note. Major severity rests chiefly on the unsupported role, not a demand for an exhaustive soil census.

### non-graph-proxy-scope: Keep chemical origins and consumption at the source interpretation level

major / open / confirmed; issue key: cm-000215-non-graph-proxy-scope.

The description presents necromass-derived compounds and consumption more definitively than the formula-class and transcript measurements justify. The SOC shift is also stored as an environmental condition. The already qualified graph provides the appropriate interpretation boundary.

### assay-context: Separate one-season field history from laboratory assay metadata

minor / open / confirmed; issue key: cm-000215-assay-context.

Multiple-winter wording, 15 mL working volume and IN_VIVO labels on laboratory measurements conflict with the full Methods and existing graph. Source field pH is available but does not define laboratory pH; time zero is a pre-wet-up baseline.

### public-resources: Link the verified study data and analysis resources

minor / open / confirmed; issue key: cm-000215-public-resources.

The empty dataset list and publication-only resource links omit directly verified study deposits and analysis provenance. Resource types and experimental scopes must remain distinct.

## Recommended Actions And Acceptance Checks

### repair-membership-role-scope

Recover representative source membership and attach evidence only to the roles it supports.

- Omit SECONDARY_FERMENTER unless claim-specific evidence establishes fermentation of products from primary degraders. Do not infer that relation from a curated fermentation KO list, a transcript association or the membership/qSIP excerpt. A different species need not perform the primary-degradation step. Functional roles are optional.
- Retain PRIMARY_DEGRADER only as a clearly qualified aggregate interpretation with narrow complex-carbon pathway evidence; do not assign it uniformly to every bacterial member or automatically copy it to newly represented groups. Preserve the source’s observed and inferred levels separately.
- Reconcile the Bacteria-only placeholder with the measured bacterial/archaeal scope. Add Archaea at the supported domain level and representative source-reported bacterial phyla with verified current labels, preserving the legacy names in source context. Do not invent archaeal species, strain identities, a complete ASV census or fungal growth rates.
- Retain Bacteria DOMINANT with Figure S7 transcript-context evidence; do not convert read shares into cell biomass or impose a fixed abundance threshold. Fungal/other transcript presence may be described separately without importing host plant reads as microbial members.
- Re-ground each added taxon independently. Keep the valid existing Bacteria domain mapping, but do not copy its historical genome counts to new groups or replace counts using a naive mixed-rank sum. Preserve the three qualified nodes and two HYPOTHESIZED arrows.

### qualify-non-graph-proxies

Synchronize overview and outcome placement with the existing qualified graph.

- Rewrite the description to distinguish measured turnover, formula-class distributions and transcript associations from proposed necromass recycling, plant-detritus use and membrane maintenance. Attribute source-origin and consumption interpretations; do not state identified molecules, absolute pools, uptake, pathway flux or causal mediation.
- Clarify that the strongest chemical comparison concerns treatment-unique water-extractable formulas and related class distributions, with methanol extracts assessed separately. Do not generalize formula-class counts to the entire soil carbon stock or prove multiyear carbon loss.
- Define CGE consistently with the existing node: cumulative new biomass divided by cumulative CO2, normalized to the maximum observed ratio. Preserve nonsignificant rather than equivalent CO2 differences and the absence of measured fungal turnover.
- Move environmental_factors[2] from controlled conditions to the existing qualified phenotype/interpretation context, preserving its supported formula-class observation and laboratory evidence. Do not create an extra causal edge or restore stronger wording already removed by the prior graph review.

### repair-assay-context

Apply the existing issue 1274 follow-up and reconcile field, laboratory and vessel metadata.

- Replace multiple-winter/long-term-treatment wording with the one October 2017–May 2018 experimental season, August 2018 collection and subsequent laboratory rewetting. If adding 930/465 mm targets, identify them as the source’s 100%/50% mean annual precipitation conditions. Preserve open issue 1274 as the existing follow-up.
- Remove working_volume=15 mL and its unit unless an actual culture working volume is separately supported. Retain 15 mL vial capacity, 5 g soil, 1 mL water addition and two vials per 500 mL jar in their proper fields/notes; neither water dose nor soil mass supplies a substitute liquid working volume.
- Describe 0 h as the before-labeling/rewetting baseline, followed by 3–168 h sampling. Keep the nitrogen-filled serum bottles and 5 mL withdrawal scoped to gas analysis, not the growth vessel or a defined incubation gas mix.
- Use IN_VITRO for laboratory qSIP/wet-up and derived chemistry/turnover evidence, including the taxonomy membership and publication-summary evidence where the cited claim is laboratory-derived. Keep IN_VIVO for the actual field precipitation manipulation. Bibliographic identity alone need not be assigned a biological assay type.
- Replace the blanket no-pH-reported statement with a distinction: field soil pH 5.9 is available, but an incubation pH setpoint is not reported. Do not populate a laboratory pH or numerical temperature from field characterization or conventional room temperature. Keep temperature/ph/oxygen control fields unset where unsupported and preserve issue 646’s decision and issue 622’s quote workaround.
- Following separately authorized curation, append a fresh history event and run focused schema, strict, term, reference, GTDB/domain and history checks, then just gen-html and just check-docs-current. No canonical edit or generator is run as part of this review. Do not change caches, schema or saved reviews to hide source or validator limitations.

### add-public-resources

Add the independently verified datasets and immutable code provenance.

- Add PRJNA856348 for metagenomics and PRJNA1311596 for 16S sequencing, with the focal publication and source-specific sample/material descriptions. Do not infer taxon membership or experimental sample counts from project existence.
- Represent the exact source-declared transcriptome projects PRJNA1087816–PRJNA1087833, PRJNA1088038–PRJNA1088059 and PRJNA1088064–PRJNA1088070 using valid resolvable accessions/links. Forty-seven project identities are verified; this is not an independently resolved sample-count denominator. Preserve the transcriptome titles versus generic archive metagenome datatype discrepancy.
- Add Figshare DOI 10.6084/m9.figshare.29825273, with verified v1 scope for FTICR and CO2 data. Its twelve file entries include .DS_Store; do not call them twelve scientific datasets or claim payload analysis.
- Add the author repository linneakh/CA_grassland_omics as code/analysis provenance, with verified commit 1a7e471b6d1ed4ce38e595164508d51754b9098c and inspected README/tree scope. Do not claim execution, reproducibility certification or raw-data reanalysis. Preserve the existing publication links.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml; Entire canonical record, including three nodes and two arrows | supports | The record represents naturally sourced California grassland soil under field precipitation history and subsequent laboratory wet-up. The existing graph qualifies the carbon-allocation interpretations and limits qSIP, CGE and CO2 claims. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=41964077&amp;retmode=xml; Direct bibliographic metadata | supports | Fresh title, abstract and identifiers establish the focal publication. Eleven existing excerpts match the abstract. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41964077%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Direct bibliographic metadata | supports | PMID 41964077, PMC13188737 and DOI 10.1186/s40168-026-02395-9 identify the same open primary paper. |
| crossref | https://api.crossref.org/works/10.1186/s40168-026-02395-9; Direct bibliographic metadata | supports | DOI metadata corroborates the focal publication identity. |
| field | PMID:41964077; Methods: Field site description; Laboratory 18O-H2O wet-up and sample collection | supports | The experiment imposed 100% versus 50% mean annual precipitation during one October 2017–May 2018 season, followed by August 2018 soil sampling. Annual targets were 930 and 465 mm. Field soil pH was 5.9; that value is not a measured or controlled incubation pH. The plant-dominated field source is not a defined microbial inoculum. |
| cultivation | PMID:41964077; Abstract: Background; Methods: Laboratory 18O-H2O wet-up and sample collection | supports | Five grams of sieved soil received 1 mL labeled or control water in a 15 mL vial; two vials were enclosed in a 500 mL jar. The 15 mL value is vessel capacity, not measured working culture volume. Incubation was dark at unquantified room temperature. Time zero preceded labeling/rewetting; later destructive samples were collected at 3, 24, 48, 72 and 168 h. Nitrogen-filled gas-sampling bottles were separate from the soil culture. |
| membership | PMID:41964077; Methods: 16S-qSIP and metagenomics; Results: Growth, microbial turnover, and community growth efficiency; Figure 1; Figure S7 | supports | The measured 16S turnover scope includes bacteria and archaea. The main text resolves prominent bacterial groups under the legacy names Proteobacteria, Actinobacteria and Firmicutes. S7 shows bacterial transcript dominance, small archaeal representation and fungal/other reads. Transcript proportions do not measure cell biomass, and fungal turnover was not measured. Representative phyla can be recovered without asserting a complete species census. |
| roles | PMID:41964077; Results: Gene expression and community growth efficiency metric; Discussion: Microbial energy, degradation, and biosynthesis metabolisms associated with CGE; Table 1; Figures S4–S6 | supports | The source reports complex-carbon degradation interpretations and fermentation-associated annotations, including an acetate-related KO. It does not assign fermentation of demonstrated primary-degrader products to the entire bacterial aggregate. The current membership excerpt cannot support a uniform trophic role. A bounded aggregate PRIMARY_DEGRADER interpretation may be retained with explicit pathway evidence; SECONDARY_FERMENTER needs separate source-specific support. |
| turnover | PMID:41964077; Methods: Taxon-specific growth and mortality rate calculations; Proxy or metric for community growth efficiency; Results: Growth, microbial turnover, and community growth efficiency; Figures 1–2 | supports | qSIP estimates interval-average bacterial/archaeal growth and mortality from 16S copies. Reduced precipitation history lowered those estimates. CGE is cumulative new biomass divided by cumulative CO2 and scaled to the maximum observed ratio, not absolute conventional carbon-use efficiency. CO2 differences were nonsignificant, not equivalent; fungal respiration can contribute without measured fungal growth. |
| chemistry | PMID:41964077; Methods: Fourier-transform ion cyclotron resonance mass spectrometry; Results: Water-extractable organic carbon and Methanol extractable organic carbon; Figure 3; Figures S1–S3 | supports | Water- and methanol-extractable molecular formula classes are semiquantitative compositional proxies. Treatment-unique formulas and their relative class distributions do not establish named molecules, absolute necromass pools, plant-origin tracing or substrate-specific flux. The source interprets these chemical patterns together with turnover and transcription. |
| pathways | PMID:41964077; Abstract: Results; Methods: Partial least squares regression and Correlations; Results: Gene expression and community growth efficiency metric; Figures 4–5; Figures S4–S6 | supports | Gene-transcript associations support proposed biosynthesis/degradation allocation differences. They do not measure enzyme activity, nutrient transfer or the causal effect of one pathway on CGE. Peptidoglycan and amino-acid synthesis annotations do not themselves demonstrate necromass consumption. |
| mechanism | PMID:41964077; Discussion: Influence of bioavailable substrate composition on CGE; Figure 6; Conclusions | supports | The proposed shift between necromass recycling and plant-detritus use is a conceptual explanation of associated observations. The three existing nodes and two HYPOTHESIZED arrows preserve this status. The overview and environmental-factor outcome should use the same qualification rather than treating source-derived chemical pools and consumption as directly established. |
| availability | PMID:41964077; Data availability | supports | The paper names metagenomic and 16S projects, three ranges of transcriptome projects, a Figshare FTICR/CO2 deposit and the author analysis repository. These are distinct resource types and experimental scopes; none is a substitute for claim-level evidence. |
| figures | PMID:41964077; All six main images and all seven scientific SI figure images; captions | supports | Figure 1 provides representative taxonomic patterns; S7 supports ordinal bacterial transcript dominance. Figures 3/S1–S3 show formula-class distributions; Figures 4–5/S4–S6 show association analyses; Figure 6 is conceptual. No image digitization or statistical reanalysis was performed. |
| workbooks | PMID:41964077; Table S1 headers and fermentation rows 989–1085; selected Table S2 rows; all 26 Table S3 data rows | supports | Curated KOs and PLSR annotations include fermentation, peptidoglycan and CAZy substrate interpretations. These are not taxon-resolved demonstrations of secondary fermentation or measured substrate utilization. The pinned scope records exact selected fields and recovered output truncation; it does not claim all cells in the large workbook were read. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity; TaxonomicComposition; FunctionalRoleEnum; AbundanceEnum; EnvironmentalFactor; CultivationSetup; EvidenceSourceEnum | supports | SECONDARY_FERMENTER means fermentation of products from primary degraders, without requiring a different species as the degrader. Roles and ecological_state are optional. DOMINANT is ordinal. Environmental factors are conditions; working_volume is actual culture volume. Field studies and laboratory assays use different evidence contexts. |
| ontology | ontology-authority.json; Whole bounded frozen receipt | supports | All nine encoded ID-label pairs match local OAK; the valid Bacteria domain term does not include Archaea. |
| semantics | ontology-semantic-notes.json; Whole bounded frozen receipt | supports | Native semantic review distinguishes aggregate roles, transcript-based dominance, experimental scope, optional conditions and qualified graph interpretations. |
| gtdb | child-gtdb-mapping-check.json; Whole bounded frozen receipt | supports | The Bacteria domain mapping is coherent. A naive sum over mixed-rank crosswalk rows cannot reproduce or replace the historical aggregation counts; these are not study genome counts. |
| taxon-candidates | child-supplementary-taxonomy.json; Whole bounded frozen receipt | supports | Local OAK verifies Archaea (NCBITaxon:2157), Pseudomonadota (1224; source Proteobacteria), Actinomycetota (201174; source Actinobacteria) and Bacillota (1239; source Firmicutes). The latter three are phyla. These are representative source groups, not strains, species or a complete census; GTDB mapping must be resolved separately at its own rank. |
| resources | dataset-verification.json; Whole bounded frozen receipt | supports | All 49 declared project identities, Figshare v1 and the immutable author repository are verified at metadata/inventory/README scope. The 47 transcriptome project titles are distinguished from a generic archive metagenome datatype. |
| snippets | snippet-audit.json; Whole bounded frozen receipt | supports | All 20 excerpts match direct sources: eleven abstract spans and nine body spans. All twenty match the full appended MD cache; eleven match the abstract-only TXT. |
| history | provenance-audit.json; Whole bounded frozen receipt | supports | The exact prior graph-only row is preserved. Open issue 1274 already identifies one-season and vessel-capacity corrections; closed 1272 does not certify untouched non-graph fields. Issues 622 and 646 retain their bracket-parser and unset-control boundaries. |
| native-target | support-audit.json; Whole bounded frozen receipt | supports | Native graph COMPLETE: three nodes, two arrows and six node-evidence entries. Completeness 95 and capped quality 100 are mechanical scores, not scientific certification. |
| source-scope | source-audit.json; Whole bounded frozen receipt | supports | Whole-record assessment finds two major and two minor groups. Scientific main, all six main and seven scientific SI figures and bounded workbook data were inspected; video and raw-data limits are explicit. |
| lead-read | lead-primary-read-scope.json; Whole bounded frozen receipt | supports | Pins full scientific-main reading, figure inspection, scoped workbook review and the unviewed video-abstract boundary. |
| independent-source | root-independent-source-audit.json; Whole bounded frozen receipt | supports | Root independently reviewed the scientific main, figures, critical workbook fields, source metadata and claim scope and concurs with final grading. |
| auxiliary | auxiliary-frozen-manifest.json; Whole bounded frozen receipt | supports | Child-owned native, ontology and adapter receipts remain frozen; supplementary taxon candidates are a separate receipt. |
| access-fulltext | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13188737/fullTextXML; Preserved actual access receipt | supports | Direct full primary XML retrieved. |
| access-publisher | https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-026-02395-9; Preserved actual access receipt | supports | Direct publisher HTML retrieved. |
| access-supplement-zip | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13188737/supplementaryFiles; Preserved actual access receipt | supports | The source-linked archive contains six main images, seven scientific figure supplements, two XLSX supplements and ancillary MP4 files. Scientific assets were inspected to declared scope; videos were not viewed. |
| adapter | adapter-check.json; Bounded same-runtime discovery with original timestamps | supports | No applicable expression-module evidence was established. This optional adapter limitation is not negative biological evidence. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml; Actual execution 2026-10-21T15:19:03.682437+00:00 to 2026-10-21T15:19:04.442892+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-strict kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml --out /private/tmp/cm-review-session/batch-09/000215/strict-report.tsv; Actual execution 2026-10-21T15:19:03.682696+00:00 to 2026-10-21T15:19:05.794322+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-terms kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml; Actual execution 2026-10-21T15:19:03.682822+00:00 to 2026-10-21T15:19:05.405665+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-gtdb kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml; Actual execution 2026-10-21T15:19:04.443205+00:00 to 2026-10-21T15:19:04.518095+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-gtdb-domain kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml; Actual execution 2026-10-21T15:19:04.518442+00:00 to 2026-10-21T15:19:05.845265+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-history history/records/California_Grassland_Precipitation_Legacy_Soil_Community; Actual execution 2026-10-21T15:19:05.405960+00:00 to 2026-10-21T15:19:06.292788+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T15:19:06.294067+00:00 to 2026-10-21T15:19:06.381533+00:00 | supports | Read-only cache-name preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src just --no-dotenv validate-references-explained kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml; Actual execution 2026-10-21T15:19:06.382020+00:00 to 2026-10-21T15:19:07.525331+00:00 | supports | Reference validation passed; independent matching separates eleven abstract and nine body excerpts. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T14:53:06.814378+00:00 to 2026-10-21T14:53:14.616064+00:00 | supports | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T14:53:06.817734+00:00 to 2026-10-21T14:53:14.704428+00:00 | supports | Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities; the focal graph separately reports COMPLETE. |

## Limits And Additional Notes

- Current-claim completion covers the whole primary scientific main, all six main figures, all seven scientific SI figures and targeted workbook checks. The video abstract was not viewed; no claim depends on its content.
- Workbook inspection was bounded: S1 headers, complete fermentation KO/subpathway range and selected peptidoglycan rows; selected S2 rows; all 26 S3 data rows. No claim to read every gene-name cell in the large curated lists.
- No raw reads, new taxonomy assignment, transcript reanalysis, molecular-formula reassignment, enzyme assay, flux tracing, PLSR refitting or new significance test.
- Bacterial/archaeal 16S-qSIP interval averages do not measure fungal turnover. S7 transcript dominance is not a biomass or cell-count fraction. No resolved archaeal species or complete soil census is inferred.
- CGE is cumulative estimated new biomass divided by cumulative CO2 and normalized to the observed maximum; it is not absolute conventional carbon-use efficiency or a demonstrated long-term carbon-stock balance.
- FTICR-MS formula classes are semiquantitative chemical proxies, not identified source-derived molecules or measured nutrient transfers. Transcript associations do not establish enzyme activities, pathway fluxes or mediation.
- Source inconsistencies remain explicit: CO2 p=0.4 in text versus 0.8 in Figure 2; 48 transcript samples versus 2×3×6 and 47 after exclusion; PLSR 644 versus 389+254; Table 1 versus Discussion energy counts; and one aromatic-correlation sign differing from S5. No convenient reconciliation or new record defect is invented from these.
- Direct archive checks verify project identities, listed assets and immutable code provenance only; no dataset payload or repository code was executed. Archive generic datatype labels and source-specific transcriptomic titles are distinguished.
- Existing Bacteria GTDB domain identity is valid, but the historical aggregation count cannot be reproduced by summing mixed-rank mapping rows. No replacement count or study genome count is inferred.
- No canonical, cache, history, generated or saved-review files changed; all 24 inspected inputs remain pinned.
- All 20 excerpts match direct sources: eleven abstract and nine body spans. The full appended MD matches all twenty; the abstract-only TXT matches eleven. Its stale MD frontmatter is not used to infer absence of full text.
- Completeness 95 and quality 100 (raw 111) are native mechanical scores, not scientific certification.
- The original source has internal count/sign/p-value inconsistencies; these are preserved as bounded limitations without adding unencoded defects or rerunning analyses.
- No raw omics/statistical reanalysis, code execution, paid provider, author contact or later-target review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T153033Z-california-grassland-precipitation-legacy-record
kind: record
repository: CultureBotAI/CommunityMech
title: California grassland precipitation legacy soil community review
started_at: '2026-10-21T15:18:22.190378Z'
finished_at: '2026-10-21T15:30:33.089057Z'
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
summary: Full scientific main, figures and scoped supplements support the natural
  soil identity and qualified three-node, two-arrow graph. Two major findings concern
  trophic-role scope and stronger non-graph chemical/mechanistic claims. Two minor
  findings concern field/laboratory metadata and omitted public resources. Existing
  graph hypotheses and measurement limits remain intact.
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
  - path: history/records/California_Grassland_Precipitation_Legacy_Soil_Community/2026-10-05T173107Z-codex-e7e0fd.yaml
    sha256: 99028cc1b267e87137186c462b5ae97a67b5c239eee9d7f67e5472dfce5c7c59
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    sha256: 7d75f820906ff9d78b5b0af28c3f11f89399f0f7b80c28df6438d9f19b3b368d
    role: target
  - path: references_cache/PMID_41964077.md
    sha256: 3e02992e16bdbcf65e7ca6bb8afbd49af326525f3a8710fc4c63003a71042b0e
    role: context
  - path: references_cache/PMID_41964077.txt
    sha256: 4786227083311c7398a05b9beacf68ae58fb65b40543d7daf4f6ceccd4129a66
    role: context
  - path: reports/causal_graph_review/decisions/20261005-ten-records-batch10.yaml
    sha256: 7149a6a81f091ff27d40deaf5bf99cb0a9b6486344db20009517f48652fe855d
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
- target_id: CommunityMech:000215
  path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  label: California Grassland Precipitation Legacy Soil Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    role: canonical_record
scope:
  description: Whole canonical record and every node/arrow assessed using direct primary
    main, figures, scoped supplements, authority/archive evidence and actual native
    checks.
  selection: Only released CommunityMech:000215 in the owned batch 09 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000215
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000215
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, chemical origins or causal pathway flux.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000215
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-strict kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    --out /private/tmp/cm-review-session/batch-09/000215/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, chemical origins or causal pathway flux.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000215
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-terms kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, chemical origins or causal pathway flux.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000215
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, chemical origins or causal pathway flux.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000215
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb-domain kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, chemical origins or causal pathway flux.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000215
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-history history/records/California_Grassland_Precipitation_Legacy_Soil_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, chemical origins or causal pathway flux.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-name preflight passed.
  target_ids:
  - CommunityMech:000215
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, chemical origins or causal pathway flux.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed; independent matching separates eleven abstract
    and nine body excerpts.
  target_ids:
  - CommunityMech:000215
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-references-explained kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused native execution. Mechanical validity does not establish
    trophic roles, chemical origins or causal pathway flux.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities;
    the focal graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000215
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse; existing corpus warnings are
    retained and not attributed to this focal record.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 09 corpus diagnostics report 57 warnings across 21 of 477 communities;
    the focal graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000215
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse; existing corpus warnings are
    retained and not attributed to this focal record.
- check_id: scientific-source
  name: Primary scientific review
  status: passed
  required: true
  summary: Whole scientific main, six main figures, seven scientific SI figures and
    bounded workbook fields assessed against all current nodes and arrows.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - source-scope
  - independent-source
  - lead-read
  - workbooks
- check_id: source-resources
  name: Public resource identity
  status: passed
  required: true
  summary: All declared project identities and bounded Figshare/repository metadata
    verified.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - resources
- check_id: supplements
  name: Scientific supplements
  status: passed
  required: true
  summary: All seven scientific SI images/captions and selected workbook data read
    to declared scope.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - figures
  - workbooks
- check_id: video-abstract
  name: Ancillary video abstract
  status: skipped
  required: false
  summary: XML identifies a Video Abstract and the archive preserves MP4 files. Videos
    were not viewed; no encoded claim depends on their content.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - access-supplement-zip
  - lead-read
- check_id: raw-reanalysis
  name: Raw omics and statistical reproduction
  status: skipped
  required: false
  summary: No raw sequence analysis, formula reassignment, pathway-flux analysis,
    PLSR refitting or significance test was performed.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - workbooks
  - resources
  - source-scope
- check_id: structured-adapter
  name: Optional structured expression adapter
  status: unavailable
  required: false
  summary: No applicable expression-module evidence established through bounded runtime
    discovery.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  locator: Entire canonical record, including three nodes and two arrows
  summary: The record represents naturally sourced California grassland soil under
    field precipitation history and subsequent laboratory wet-up. The existing graph
    qualifies the carbon-allocation interpretations and limits qSIP, CGE and CO2 claims.
  support: supports
  accessed_at: '2026-10-21T15:30:33.083264Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41964077&retmode=xml
  locator: Direct bibliographic metadata
  summary: Fresh title, abstract and identifiers establish the focal publication.
    Eleven existing excerpts match the abstract.
  support: supports
  accessed_at: '2026-10-21T15:18:52.566522Z'
  snapshot_sha256: c8cd47c63ea4acff1abc912d7fb05940838c7633a210f4b688a5e4fb4ef5b02e
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41964077%20AND%20SRC:MED&format=json&resultType=core
  locator: Direct bibliographic metadata
  summary: PMID 41964077, PMC13188737 and DOI 10.1186/s40168-026-02395-9 identify
    the same open primary paper.
  support: supports
  accessed_at: '2026-10-21T15:18:53.086567Z'
  snapshot_sha256: bace183caf1a8f4d68675e9dd45d26c2f1ae0639690ba5179e3294423c86ef85
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1186/s40168-026-02395-9
  locator: Direct bibliographic metadata
  summary: DOI metadata corroborates the focal publication identity.
  support: supports
  accessed_at: '2026-10-21T15:18:52.611917Z'
  snapshot_sha256: 903c835f2c006e2e07dbe0f95f7b118ec59ffb6d73ac048119f12a07a9cb4d78
- evidence_id: field
  kind: primary_source
  reference: PMID:41964077
  locator: 'Methods: Field site description; Laboratory 18O-H2O wet-up and sample
    collection'
  summary: The experiment imposed 100% versus 50% mean annual precipitation during
    one October 2017–May 2018 season, followed by August 2018 soil sampling. Annual
    targets were 930 and 465 mm. Field soil pH was 5.9; that value is not a measured
    or controlled incubation pH. The plant-dominated field source is not a defined
    microbial inoculum.
  support: supports
  accessed_at: '2026-10-21T15:19:04.144052Z'
  snapshot_sha256: c78381e8fdbab9f2b347f66d70c5813057ccf3fd94213dbc630219d810858bb3
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:41964077
  locator: 'Abstract: Background; Methods: Laboratory 18O-H2O wet-up and sample collection'
  summary: Five grams of sieved soil received 1 mL labeled or control water in a 15
    mL vial; two vials were enclosed in a 500 mL jar. The 15 mL value is vessel capacity,
    not measured working culture volume. Incubation was dark at unquantified room
    temperature. Time zero preceded labeling/rewetting; later destructive samples
    were collected at 3, 24, 48, 72 and 168 h. Nitrogen-filled gas-sampling bottles
    were separate from the soil culture.
  support: supports
  accessed_at: '2026-10-21T15:19:04.144052Z'
  snapshot_sha256: c78381e8fdbab9f2b347f66d70c5813057ccf3fd94213dbc630219d810858bb3
  quote: soils were rewetted in the laboratory
- evidence_id: membership
  kind: primary_source
  reference: PMID:41964077
  locator: 'Methods: 16S-qSIP and metagenomics; Results: Growth, microbial turnover,
    and community growth efficiency; Figure 1; Figure S7'
  summary: The measured 16S turnover scope includes bacteria and archaea. The main
    text resolves prominent bacterial groups under the legacy names Proteobacteria,
    Actinobacteria and Firmicutes. S7 shows bacterial transcript dominance, small
    archaeal representation and fungal/other reads. Transcript proportions do not
    measure cell biomass, and fungal turnover was not measured. Representative phyla
    can be recovered without asserting a complete species census.
  support: supports
  accessed_at: '2026-10-21T15:19:04.144052Z'
  snapshot_sha256: c78381e8fdbab9f2b347f66d70c5813057ccf3fd94213dbc630219d810858bb3
- evidence_id: roles
  kind: primary_source
  reference: PMID:41964077
  locator: 'Results: Gene expression and community growth efficiency metric; Discussion:
    Microbial energy, degradation, and biosynthesis metabolisms associated with CGE;
    Table 1; Figures S4–S6'
  summary: The source reports complex-carbon degradation interpretations and fermentation-associated
    annotations, including an acetate-related KO. It does not assign fermentation
    of demonstrated primary-degrader products to the entire bacterial aggregate. The
    current membership excerpt cannot support a uniform trophic role. A bounded aggregate
    PRIMARY_DEGRADER interpretation may be retained with explicit pathway evidence;
    SECONDARY_FERMENTER needs separate source-specific support.
  support: supports
  accessed_at: '2026-10-21T15:19:04.144052Z'
  snapshot_sha256: c78381e8fdbab9f2b347f66d70c5813057ccf3fd94213dbc630219d810858bb3
- evidence_id: turnover
  kind: primary_source
  reference: PMID:41964077
  locator: 'Methods: Taxon-specific growth and mortality rate calculations; Proxy
    or metric for community growth efficiency; Results: Growth, microbial turnover,
    and community growth efficiency; Figures 1–2'
  summary: qSIP estimates interval-average bacterial/archaeal growth and mortality
    from 16S copies. Reduced precipitation history lowered those estimates. CGE is
    cumulative new biomass divided by cumulative CO2 and scaled to the maximum observed
    ratio, not absolute conventional carbon-use efficiency. CO2 differences were nonsignificant,
    not equivalent; fungal respiration can contribute without measured fungal growth.
  support: supports
  accessed_at: '2026-10-21T15:19:04.144052Z'
  snapshot_sha256: c78381e8fdbab9f2b347f66d70c5813057ccf3fd94213dbc630219d810858bb3
- evidence_id: chemistry
  kind: primary_source
  reference: PMID:41964077
  locator: 'Methods: Fourier-transform ion cyclotron resonance mass spectrometry;
    Results: Water-extractable organic carbon and Methanol extractable organic carbon;
    Figure 3; Figures S1–S3'
  summary: Water- and methanol-extractable molecular formula classes are semiquantitative
    compositional proxies. Treatment-unique formulas and their relative class distributions
    do not establish named molecules, absolute necromass pools, plant-origin tracing
    or substrate-specific flux. The source interprets these chemical patterns together
    with turnover and transcription.
  support: supports
  accessed_at: '2026-10-21T15:19:04.144052Z'
  snapshot_sha256: c78381e8fdbab9f2b347f66d70c5813057ccf3fd94213dbc630219d810858bb3
- evidence_id: pathways
  kind: primary_source
  reference: PMID:41964077
  locator: 'Abstract: Results; Methods: Partial least squares regression and Correlations;
    Results: Gene expression and community growth efficiency metric; Figures 4–5;
    Figures S4–S6'
  summary: Gene-transcript associations support proposed biosynthesis/degradation
    allocation differences. They do not measure enzyme activity, nutrient transfer
    or the causal effect of one pathway on CGE. Peptidoglycan and amino-acid synthesis
    annotations do not themselves demonstrate necromass consumption.
  support: supports
  accessed_at: '2026-10-21T15:19:04.144052Z'
  snapshot_sha256: c78381e8fdbab9f2b347f66d70c5813057ccf3fd94213dbc630219d810858bb3
  quote: microbes appeared to consume
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:41964077
  locator: 'Discussion: Influence of bioavailable substrate composition on CGE; Figure
    6; Conclusions'
  summary: The proposed shift between necromass recycling and plant-detritus use is
    a conceptual explanation of associated observations. The three existing nodes
    and two HYPOTHESIZED arrows preserve this status. The overview and environmental-factor
    outcome should use the same qualification rather than treating source-derived
    chemical pools and consumption as directly established.
  support: supports
  accessed_at: '2026-10-21T15:19:04.144052Z'
  snapshot_sha256: c78381e8fdbab9f2b347f66d70c5813057ccf3fd94213dbc630219d810858bb3
- evidence_id: availability
  kind: primary_source
  reference: PMID:41964077
  locator: Data availability
  summary: The paper names metagenomic and 16S projects, three ranges of transcriptome
    projects, a Figshare FTICR/CO2 deposit and the author analysis repository. These
    are distinct resource types and experimental scopes; none is a substitute for
    claim-level evidence.
  support: supports
  accessed_at: '2026-10-21T15:19:04.144052Z'
  snapshot_sha256: c78381e8fdbab9f2b347f66d70c5813057ccf3fd94213dbc630219d810858bb3
- evidence_id: figures
  kind: primary_source
  reference: PMID:41964077
  locator: All six main images and all seven scientific SI figure images; captions
  summary: Figure 1 provides representative taxonomic patterns; S7 supports ordinal
    bacterial transcript dominance. Figures 3/S1–S3 show formula-class distributions;
    Figures 4–5/S4–S6 show association analyses; Figure 6 is conceptual. No image
    digitization or statistical reanalysis was performed.
  support: supports
  accessed_at: '2026-10-21T15:30:33.085361Z'
  snapshot_sha256: d7fbd717431bd39250ae97e369fd04207a8e1389363935546e5c4b1e9bdfbde0
- evidence_id: workbooks
  kind: primary_source
  reference: PMID:41964077
  locator: Table S1 headers and fermentation rows 989–1085; selected Table S2 rows;
    all 26 Table S3 data rows
  summary: Curated KOs and PLSR annotations include fermentation, peptidoglycan and
    CAZy substrate interpretations. These are not taxon-resolved demonstrations of
    secondary fermentation or measured substrate utilization. The pinned scope records
    exact selected fields and recovered output truncation; it does not claim all cells
    in the large workbook were read.
  support: supports
  accessed_at: '2026-10-21T15:30:33.085462Z'
  snapshot_sha256: b04a2af7eba147cb36a7d2bbfe63a2b2c6bf977b639f16884a802f4f65b83d9e
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity; TaxonomicComposition; FunctionalRoleEnum; AbundanceEnum;
    EnvironmentalFactor; CultivationSetup; EvidenceSourceEnum
  summary: SECONDARY_FERMENTER means fermentation of products from primary degraders,
    without requiring a different species as the degrader. Roles and ecological_state
    are optional. DOMINANT is ordinal. Environmental factors are conditions; working_volume
    is actual culture volume. Field studies and laboratory assays use different evidence
    contexts.
  support: supports
  accessed_at: '2026-10-21T15:30:33.085517Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded frozen receipt
  summary: All nine encoded ID-label pairs match local OAK; the valid Bacteria domain
    term does not include Archaea.
  support: supports
  accessed_at: '2026-10-21T15:30:33.085628Z'
  snapshot_sha256: 5cbe54250bb13dba816ceec524a8009021ce2d6e63f7ed38716340510272700a
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole bounded frozen receipt
  summary: Native semantic review distinguishes aggregate roles, transcript-based
    dominance, experimental scope, optional conditions and qualified graph interpretations.
  support: supports
  accessed_at: '2026-10-21T15:30:33.085745Z'
  snapshot_sha256: 1e7b0c443c07e97cf17961f6dee6af2a08616c36fd7ef964135231ae5d971a60
- evidence_id: gtdb
  kind: authority
  reference: child-gtdb-mapping-check.json
  locator: Whole bounded frozen receipt
  summary: The Bacteria domain mapping is coherent. A naive sum over mixed-rank crosswalk
    rows cannot reproduce or replace the historical aggregation counts; these are
    not study genome counts.
  support: supports
  accessed_at: '2026-10-21T15:30:33.085841Z'
  snapshot_sha256: 10ac6e3ec3d972baf4a9a3f44760326f63e64e92633f4fdeaa019e3aed7f8d46
- evidence_id: taxon-candidates
  kind: authority
  reference: child-supplementary-taxonomy.json
  locator: Whole bounded frozen receipt
  summary: Local OAK verifies Archaea (NCBITaxon:2157), Pseudomonadota (1224; source
    Proteobacteria), Actinomycetota (201174; source Actinobacteria) and Bacillota
    (1239; source Firmicutes). The latter three are phyla. These are representative
    source groups, not strains, species or a complete census; GTDB mapping must be
    resolved separately at its own rank.
  support: supports
  accessed_at: '2026-10-21T15:30:33.085869Z'
  snapshot_sha256: c14220ae16a955b5dfa37a5bcf38cad31386ceb5d4fd30b97064e83f809783a9
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded frozen receipt
  summary: All 49 declared project identities, Figshare v1 and the immutable author
    repository are verified at metadata/inventory/README scope. The 47 transcriptome
    project titles are distinguished from a generic archive metagenome datatype.
  support: supports
  accessed_at: '2026-10-21T15:30:33.086043Z'
  snapshot_sha256: 457d9210e246b8462374b7b5ba15f501d5a32136e8cd998a98296f770d98c346
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded frozen receipt
  summary: 'All 20 excerpts match direct sources: eleven abstract spans and nine body
    spans. All twenty match the full appended MD cache; eleven match the abstract-only
    TXT.'
  support: supports
  accessed_at: '2026-10-21T15:30:33.086187Z'
  snapshot_sha256: 83dace10af4b080c4a6909f255467167696ede3e506bdac460b2f83c25b97b02
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded frozen receipt
  summary: The exact prior graph-only row is preserved. Open issue 1274 already identifies
    one-season and vessel-capacity corrections; closed 1272 does not certify untouched
    non-graph fields. Issues 622 and 646 retain their bracket-parser and unset-control
    boundaries.
  support: supports
  accessed_at: '2026-10-21T15:30:33.086332Z'
  snapshot_sha256: 1b3478882f08195cc9b5029dba0d52f62e8e752ff0045489dee10af94d89c42c
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded frozen receipt
  summary: 'Native graph COMPLETE: three nodes, two arrows and six node-evidence entries.
    Completeness 95 and capped quality 100 are mechanical scores, not scientific certification.'
  support: supports
  accessed_at: '2026-10-21T15:30:33.086353Z'
  snapshot_sha256: e791606287956c5d110f0b0e819a9e724d050c69f9be978d2d8d18dc026bfd02
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded frozen receipt
  summary: Whole-record assessment finds two major and two minor groups. Scientific
    main, all six main and seven scientific SI figures and bounded workbook data were
    inspected; video and raw-data limits are explicit.
  support: supports
  accessed_at: '2026-10-21T15:30:33.086374Z'
  snapshot_sha256: 15bf93b8031e854146cb5025dd93bf3fe4ea1c528df7b5f1bf95296263cbf736
- evidence_id: lead-read
  kind: validation
  reference: lead-primary-read-scope.json
  locator: Whole bounded frozen receipt
  summary: Pins full scientific-main reading, figure inspection, scoped workbook review
    and the unviewed video-abstract boundary.
  support: supports
  accessed_at: '2026-10-21T15:30:33.086394Z'
  snapshot_sha256: d7fbd717431bd39250ae97e369fd04207a8e1389363935546e5c4b1e9bdfbde0
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded frozen receipt
  summary: Root independently reviewed the scientific main, figures, critical workbook
    fields, source metadata and claim scope and concurs with final grading.
  support: supports
  accessed_at: '2026-10-21T15:30:33.086519Z'
  snapshot_sha256: 4f4fa9fbeac3b1fe8729eff2b6803cdc8525e4a98176250c353d97949e1f95e1
- evidence_id: auxiliary
  kind: validation
  reference: auxiliary-frozen-manifest.json
  locator: Whole bounded frozen receipt
  summary: Child-owned native, ontology and adapter receipts remain frozen; supplementary
    taxon candidates are a separate receipt.
  support: supports
  accessed_at: '2026-10-21T15:30:33.086613Z'
  snapshot_sha256: 85c35aec7af9d25053934a933da076bdd7c7dd6a839a86a36167dc7fcd0976de
- evidence_id: access-fulltext
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13188737/fullTextXML
  locator: Preserved actual access receipt
  summary: Direct full primary XML retrieved.
  support: supports
  accessed_at: '2026-10-21T15:19:04.144052Z'
  snapshot_sha256: 8c181373809e68524fbf8d81039b07368bf77f0608e11519c4a27db07da56e45
- evidence_id: access-publisher
  kind: validation
  reference: https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-026-02395-9
  locator: Preserved actual access receipt
  summary: Direct publisher HTML retrieved.
  support: supports
  accessed_at: '2026-10-21T15:18:54.062401Z'
  snapshot_sha256: ad933fc0d017637393369c223340212cc1f548031e1abb5fb496cf0cbe7760a2
- evidence_id: access-supplement-zip
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13188737/supplementaryFiles
  locator: Preserved actual access receipt
  summary: The source-linked archive contains six main images, seven scientific figure
    supplements, two XLSX supplements and ancillary MP4 files. Scientific assets were
    inspected to declared scope; videos were not viewed.
  support: supports
  accessed_at: '2026-10-21T15:21:18.369024Z'
  snapshot_sha256: f42774fdfc9654cb6b8f5d4e55956b70629d36b2be513eece684e0f5685e2662
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Bounded same-runtime discovery with original timestamps
  summary: No applicable expression-module evidence was established. This optional
    adapter limitation is not negative biological evidence.
  support: supports
  accessed_at: '2026-10-21T15:30:33.087176Z'
  snapshot_sha256: ba1eafe7e4ef8c0462cc862f26e487704659acc7f7b4195c2aaddea21e22b1c9
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  locator: Actual execution 2026-10-21T15:19:03.682437+00:00 to 2026-10-21T15:19:04.442892+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T15:19:04.442892Z'
  snapshot_sha256: 4fa8fce93e76f22f555153ec3bccba772dd0964b23554b1f033e2970e5ce0805
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-strict kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    --out /private/tmp/cm-review-session/batch-09/000215/strict-report.tsv
  locator: Actual execution 2026-10-21T15:19:03.682696+00:00 to 2026-10-21T15:19:05.794322+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T15:19:05.794322Z'
  snapshot_sha256: ce262cc15d80fa31959a8c6f951b3f00616fc85b682db09690573ac11263f69c
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-terms kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  locator: Actual execution 2026-10-21T15:19:03.682822+00:00 to 2026-10-21T15:19:05.405665+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T15:19:05.405665Z'
  snapshot_sha256: d9e3da56e2f8dfd3e0b6c7cca59254f1cbab4a6fc8a46cdd915e8a4c255aedce
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  locator: Actual execution 2026-10-21T15:19:04.443205+00:00 to 2026-10-21T15:19:04.518095+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T15:19:04.518095Z'
  snapshot_sha256: ab4b0edd0ce76f516977e90325c818b2da6dc5fda68ceb9926c607f1d5248f56
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-gtdb-domain kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  locator: Actual execution 2026-10-21T15:19:04.518442+00:00 to 2026-10-21T15:19:05.845265+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T15:19:05.845265Z'
  snapshot_sha256: 8e59fcbf135e641bd684b80af04a917a9d287d645c66aaaf7efba5c904c53f8c
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-history history/records/California_Grassland_Precipitation_Legacy_Soil_Community
  locator: Actual execution 2026-10-21T15:19:05.405960+00:00 to 2026-10-21T15:19:06.292788+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T15:19:06.292788Z'
  snapshot_sha256: ed7fa4a8f8838a624e5685ae8f7f7708e53a7748d8f64724f4a8ff81d712297d
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T15:19:06.294067+00:00 to 2026-10-21T15:19:06.381533+00:00
  summary: Read-only cache-name preflight passed.
  support: supports
  accessed_at: '2026-10-21T15:19:06.381533Z'
  snapshot_sha256: 103c2584e514d3815c85a5d8eb97071c8f13b217d604cee2be48e60b901ce090
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-09/src
    just --no-dotenv validate-references-explained kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  locator: Actual execution 2026-10-21T15:19:06.382020+00:00 to 2026-10-21T15:19:07.525331+00:00
  summary: Reference validation passed; independent matching separates eleven abstract
    and nine body excerpts.
  support: supports
  accessed_at: '2026-10-21T15:19:07.525331Z'
  snapshot_sha256: 9b21222a98c1f47c2d860c982811b96b4c0a58300ababfa9110720b38cbd8fb4
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
  topic: Natural soil community, membership and evidence scope
  outcome: concern
  summary: The source identity is correct; recover representative membership and separate
    roles from measurement coverage.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - membership
  - roles
  - schema
  - ontology
  - taxon-candidates
  - figures
  dimensions:
  - name: community_scope
    value: Natural grassland soil after one field-treatment season and laboratory
      rewetting
    definition: The record is not an isolated strain mixture or an in situ isotope
      assay.
    evidence_ids:
    - field
    - cultivation
  - name: taxon_rank
    value: Bacteria domain with recoverable Archaea and representative bacterial phyla
    definition: Source-resolved groups are not a complete species census.
    evidence_ids:
    - membership
    - taxon-candidates
  - name: abundance
    value: Bacteria DOMINANT at the ordinal transcript-context scope
    definition: S7 read proportions do not measure biomass or cell fraction.
    evidence_ids:
    - figures
    - membership
  - name: environment
    value: Grassland soil physically incubated in laboratory microcosms
    definition: Soil identity remains valid despite laboratory handling.
    evidence_ids:
    - field
    - cultivation
  - name: medium
    value: Unformulated soil substrate/inoculum with labeled or control water
    definition: No synthetic-medium recipe or exact cross-Mech formulation is inferred.
    evidence_ids:
    - cultivation
  - name: evidence_tier
    value: Field treatment, laboratory qSIP/chemistry and transcript associations
    definition: Each measurement retains its own biological and assay scope.
    evidence_ids:
    - turnover
    - chemistry
    - pathways
- assessment_id: state
  area: scope
  topic: State, origin and category
  outcome: supported
  summary: Retain PERTURBED, NATURAL and the carbon-storage research category.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - field
  - cultivation
  - schema
  details: Natural origin is compatible with field manipulation and laboratory wet-up.
    CARBON_SEQUESTRATION labels the research topic; it does not prove measured net
    carbon fixation, storage gain or multiyear carbon-stock loss. No alternate ecological_state
    is required.
- assessment_id: roles
  area: evidence
  topic: taxonomy[0].functional_role and evidence
  outcome: concern
  summary: The flat SECONDARY_FERMENTER assignment exceeds the demonstrated source-specific
    trophic relation.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - roles
  - workbooks
  - schema
  - semantics
  details: Fermentation annotations exist, so their absence is not the rationale.
    The missing relation is fermentation of products established to come from primary
    degraders. Omit the optional enum unless narrow evidence supports it; do not require
    the primary degrader to be a different species. PRIMARY_DEGRADER may remain an
    explicitly qualified aggregate interpretation with pathway-specific evidence,
    not a property assigned to every bacterial member.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Necromass Recycling at High Community Growth
    Efficiency'
  outcome: supported
  summary: Retain the existing HYPOTHESIZED interpretation and PARTIAL evidence.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - pathways
  - chemistry
  - mechanism
  - figures
  details: Amino-acid and peptidoglycan synthesis and aromatic-degradation associations
    motivate the source hypothesis. The chemical classes and GO annotations do not
    establish identified exchange molecules, substrate uptake or pathway flux.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Plant Detritus Degradation at Low Community
    Growth Efficiency'
  outcome: supported
  summary: Retain the qualified allocation interpretation.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - pathways
  - chemistry
  - mechanism
  - workbooks
  details: Carbohydrate/lipid transcript patterns can support the reported hypothesis
    of detritus use and maintenance. They do not directly measure membrane-repair
    activity or detritus-specific degradation flux.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Precipitation-Legacy Turnover Suppression'
  outcome: supported
  summary: Retain the laboratory turnover observation with its current measurement
    limits.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - turnover
  - field
  - figures
  details: The node correctly limits the treatment to one winter season, qSIP to bacteria/archaea,
    CO2 to a nonsignificant difference and CGE to a normalized proxy. Neither fungi
    nor multiyear carbon stocks inherit the turnover result.
- assessment_id: arrow-2-0
  area: graph
  topic: ecological_interactions[2].downstream[0]
  outcome: supported
  summary: Retain only the HYPOTHESIZED link to Necromass Recycling at High Community
    Growth Efficiency.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - mechanism
  - pathways
  - history
  details: Shared treatment responses and the conceptual model do not isolate this
    pathway as a causal mediator. No new arrow, transferred compound, donor/recipient
    identity or mechanistic necessity is warranted.
- assessment_id: arrow-2-1
  area: graph
  topic: ecological_interactions[2].downstream[1]
  outcome: supported
  summary: Retain only the HYPOTHESIZED link to Plant Detritus Degradation at Low
    Community Growth Efficiency.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - mechanism
  - pathways
  - history
  details: Shared treatment responses and the conceptual model do not isolate this
    pathway as a causal mediator. No new arrow, transferred compound, donor/recipient
    identity or mechanistic necessity is warranted.
- assessment_id: overview
  area: evidence
  topic: description and environmental_factors[2]
  outcome: concern
  summary: Apply the graph’s proxy and hypothesis qualifications consistently outside
    the graph.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - chemistry
  - pathways
  - mechanism
  - schema
  details: The overview describes source-derived compounds and consumption more definitively
    than the measurements permit. Attribute the necromass/plant-origin and allocation
    interpretations, distinguish treatment-unique formula distributions from whole
    SOC, and move the compositional response out of environmental conditions. Explain
    the source-defined relative CGE metric rather than a generic biomass/respiration
    ratio.
- assessment_id: assay
  area: completeness
  topic: Field season, laboratory evidence, baseline and cultivation geometry
  outcome: concern
  summary: Correct bounded duration, vessel-volume and evidence-context inconsistencies
    while retaining the detailed soil protocol.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - field
  - cultivation
  - turnover
  - schema
  - history
  details: One October 2017–May 2018 season is not multiple winters. The 15 mL vial
    capacity is not a working volume and cannot be replaced with the 1 mL water addition
    or 5 g soil mass. Time zero precedes wet-up. Field pH 5.9 may be recorded as site
    characterization, while laboratory pH and numerical room temperature remain unspecified.
    Keep controller fields unset and preserve the bracket-parser workaround.
- assessment_id: resources
  area: provenance
  topic: associated_datasets and external_resources
  outcome: concern
  summary: Add the directly verified public data and code resources with assay-specific
    scope.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - availability
  - resources
  details: Separate metagenomics, 16S, transcriptomics, FTICR/CO2 and analysis code.
    Forty-seven transcriptome project identifiers are not a validated sample count;
    twelve Figshare file entries include a metadata-system file and do not mean twelve
    scientific datasets. No raw data or code was executed.
- assessment_id: history
  area: provenance
  topic: Prior graph repair and current public issues
  outcome: supported
  summary: Preserve the existing graph repair and unresolved non-graph follow-up.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - history
  - snippets
  - source-scope
  details: Issue 1274 already identifies duration and vessel capacity; no duplicate
    issue is proposed. Issue 1272’s closure covers graph repair rather than the present
    non-graph claims. The full MD body and abstract-only TXT are independently recognized
    despite stale MD frontmatter. No canonical history, status or cache is changed.
- assessment_id: validation
  area: schema
  topic: Native and authority checks
  outcome: supported
  summary: All eight focused native checks pass; two major and two minor source-specific
    findings remain.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - ontology
  - check-validate
  - check-validate-references-explained
  - native-target
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Mechanical completeness is high but does not certify the scientific claims.
  target_ids:
  - CommunityMech:000215
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 95
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role rubric points +5 environment +10 for
      at least three interactions +10 for at least three environmental factors +5
      external resources +10 growth medium +0 datasets +5 metabolites.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0, P2=2, P3=2, P4=0; six evidence entries / three nodes gives 20 evidence
      points; COMPLETE adds 15. Raw 111 is capped at 100.
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
- finding_id: membership-role-scope
  issue_key: cm-000215-membership-role-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: unsupported trophic-role or chemical/mechanistic scope
    materially changes the represented biological claim; valid identifiers and qualified
    graph text do not repair stronger non-graph claims.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Reconcile broad membership and unsupported secondary fermentation
  description: The single Bacteria entry carries SECONDARY_FERMENTER on a membership
    excerpt. Fermentation-related annotations do not establish the required primary-degrader-product
    relation. The full source also resolves Archaea and representative bacterial phyla
    beyond the abstract-only note. Major severity rests chiefly on the unsupported
    role, not a demand for an exhaustive soil census.
  target_ids:
  - CommunityMech:000215
  field_paths:
  - taxonomy
  - taxonomy[0].taxon_term.notes
  - taxonomy[0].functional_role
  - taxonomy[0].evidence
  evidence_ids:
  - membership
  - roles
  - workbooks
  - schema
  - taxon-candidates
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    role: canonical_record
- finding_id: non-graph-proxy-scope
  issue_key: cm-000215-non-graph-proxy-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: unsupported trophic-role or chemical/mechanistic scope
    materially changes the represented biological claim; valid identifiers and qualified
    graph text do not repair stronger non-graph claims.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Keep chemical origins and consumption at the source interpretation level
  description: The description presents necromass-derived compounds and consumption
    more definitively than the formula-class and transcript measurements justify.
    The SOC shift is also stored as an environmental condition. The already qualified
    graph provides the appropriate interpretation boundary.
  target_ids:
  - CommunityMech:000215
  field_paths:
  - description
  - environmental_factors[2]
  evidence_ids:
  - chemistry
  - pathways
  - mechanism
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    role: canonical_record
- finding_id: assay-context
  issue_key: cm-000215-assay-context
  category: scope
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded experimental-context or public-resource completeness
    repair; the natural community identity and qualified core outcomes remain supported.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Separate one-season field history from laboratory assay metadata
  description: Multiple-winter wording, 15 mL working volume and IN_VIVO labels on
    laboratory measurements conflict with the full Methods and existing graph. Source
    field pH is available but does not define laboratory pH; time zero is a pre-wet-up
    baseline.
  target_ids:
  - CommunityMech:000215
  field_paths:
  - environmental_factors[0].description
  - environmental_factors[1].evidence[0].evidence_source
  - taxonomy[0].evidence[0].evidence_source
  - external_resources[0].evidence[0].evidence_source
  - growth_media[0].preparation_notes
  - cultivation_setup[0].working_volume
  - cultivation_setup[0].working_volume_unit
  - cultivation_setup[0].instrument_detail
  evidence_ids:
  - field
  - cultivation
  - turnover
  - schema
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    role: canonical_record
- finding_id: public-resources
  issue_key: cm-000215-public-resources
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded experimental-context or public-resource completeness
    repair; the natural community identity and qualified core outcomes remain supported.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Link the verified study data and analysis resources
  description: The empty dataset list and publication-only resource links omit directly
    verified study deposits and analysis provenance. Resource types and experimental
    scopes must remain distinct.
  target_ids:
  - CommunityMech:000215
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - availability
  - resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    role: canonical_record
actions:
- action_id: repair-membership-role-scope
  description: Recover representative source membership and attach evidence only to
    the roles it supports.
  finding_ids:
  - membership-role-scope
  target_ids:
  - CommunityMech:000215
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Omit SECONDARY_FERMENTER unless claim-specific evidence establishes fermentation
    of products from primary degraders. Do not infer that relation from a curated
    fermentation KO list, a transcript association or the membership/qSIP excerpt.
    A different species need not perform the primary-degradation step. Functional
    roles are optional.
  - Retain PRIMARY_DEGRADER only as a clearly qualified aggregate interpretation with
    narrow complex-carbon pathway evidence; do not assign it uniformly to every bacterial
    member or automatically copy it to newly represented groups. Preserve the source’s
    observed and inferred levels separately.
  - Reconcile the Bacteria-only placeholder with the measured bacterial/archaeal scope.
    Add Archaea at the supported domain level and representative source-reported bacterial
    phyla with verified current labels, preserving the legacy names in source context.
    Do not invent archaeal species, strain identities, a complete ASV census or fungal
    growth rates.
  - Retain Bacteria DOMINANT with Figure S7 transcript-context evidence; do not convert
    read shares into cell biomass or impose a fixed abundance threshold. Fungal/other
    transcript presence may be described separately without importing host plant reads
    as microbial members.
  - Re-ground each added taxon independently. Keep the valid existing Bacteria domain
    mapping, but do not copy its historical genome counts to new groups or replace
    counts using a naive mixed-rank sum. Preserve the three qualified nodes and two
    HYPOTHESIZED arrows.
- action_id: qualify-non-graph-proxies
  description: Synchronize overview and outcome placement with the existing qualified
    graph.
  finding_ids:
  - non-graph-proxy-scope
  target_ids:
  - CommunityMech:000215
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Rewrite the description to distinguish measured turnover, formula-class distributions
    and transcript associations from proposed necromass recycling, plant-detritus
    use and membrane maintenance. Attribute source-origin and consumption interpretations;
    do not state identified molecules, absolute pools, uptake, pathway flux or causal
    mediation.
  - Clarify that the strongest chemical comparison concerns treatment-unique water-extractable
    formulas and related class distributions, with methanol extracts assessed separately.
    Do not generalize formula-class counts to the entire soil carbon stock or prove
    multiyear carbon loss.
  - 'Define CGE consistently with the existing node: cumulative new biomass divided
    by cumulative CO2, normalized to the maximum observed ratio. Preserve nonsignificant
    rather than equivalent CO2 differences and the absence of measured fungal turnover.'
  - Move environmental_factors[2] from controlled conditions to the existing qualified
    phenotype/interpretation context, preserving its supported formula-class observation
    and laboratory evidence. Do not create an extra causal edge or restore stronger
    wording already removed by the prior graph review.
- action_id: repair-assay-context
  description: Apply the existing issue 1274 follow-up and reconcile field, laboratory
    and vessel metadata.
  finding_ids:
  - assay-context
  target_ids:
  - CommunityMech:000215
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Replace multiple-winter/long-term-treatment wording with the one October 2017–May
    2018 experimental season, August 2018 collection and subsequent laboratory rewetting.
    If adding 930/465 mm targets, identify them as the source’s 100%/50% mean annual
    precipitation conditions. Preserve open issue 1274 as the existing follow-up.
  - Remove working_volume=15 mL and its unit unless an actual culture working volume
    is separately supported. Retain 15 mL vial capacity, 5 g soil, 1 mL water addition
    and two vials per 500 mL jar in their proper fields/notes; neither water dose
    nor soil mass supplies a substitute liquid working volume.
  - Describe 0 h as the before-labeling/rewetting baseline, followed by 3–168 h sampling.
    Keep the nitrogen-filled serum bottles and 5 mL withdrawal scoped to gas analysis,
    not the growth vessel or a defined incubation gas mix.
  - Use IN_VITRO for laboratory qSIP/wet-up and derived chemistry/turnover evidence,
    including the taxonomy membership and publication-summary evidence where the cited
    claim is laboratory-derived. Keep IN_VIVO for the actual field precipitation manipulation.
    Bibliographic identity alone need not be assigned a biological assay type.
  - 'Replace the blanket no-pH-reported statement with a distinction: field soil pH
    5.9 is available, but an incubation pH setpoint is not reported. Do not populate
    a laboratory pH or numerical temperature from field characterization or conventional
    room temperature. Keep temperature/ph/oxygen control fields unset where unsupported
    and preserve issue 646’s decision and issue 622’s quote workaround.'
  - Following separately authorized curation, append a fresh history event and run
    focused schema, strict, term, reference, GTDB/domain and history checks, then
    just gen-html and just check-docs-current. No canonical edit or generator is run
    as part of this review. Do not change caches, schema or saved reviews to hide
    source or validator limitations.
- action_id: add-public-resources
  description: Add the independently verified datasets and immutable code provenance.
  finding_ids:
  - public-resources
  target_ids:
  - CommunityMech:000215
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Add PRJNA856348 for metagenomics and PRJNA1311596 for 16S sequencing, with the
    focal publication and source-specific sample/material descriptions. Do not infer
    taxon membership or experimental sample counts from project existence.
  - Represent the exact source-declared transcriptome projects PRJNA1087816–PRJNA1087833,
    PRJNA1088038–PRJNA1088059 and PRJNA1088064–PRJNA1088070 using valid resolvable
    accessions/links. Forty-seven project identities are verified; this is not an
    independently resolved sample-count denominator. Preserve the transcriptome titles
    versus generic archive metagenome datatype discrepancy.
  - Add Figshare DOI 10.6084/m9.figshare.29825273, with verified v1 scope for FTICR
    and CO2 data. Its twelve file entries include .DS_Store; do not call them twelve
    scientific datasets or claim payload analysis.
  - Add the author repository linneakh/CA_grassland_omics as code/analysis provenance,
    with verified commit 1a7e471b6d1ed4ce38e595164508d51754b9098c and inspected README/tree
    scope. Do not claim execution, reproducibility certification or raw-data reanalysis.
    Preserve the existing publication links.
limitations:
- Current-claim completion covers the whole primary scientific main, all six main
  figures, all seven scientific SI figures and targeted workbook checks. The video
  abstract was not viewed; no claim depends on its content.
- 'Workbook inspection was bounded: S1 headers, complete fermentation KO/subpathway
  range and selected peptidoglycan rows; selected S2 rows; all 26 S3 data rows. No
  claim to read every gene-name cell in the large curated lists.'
- No raw reads, new taxonomy assignment, transcript reanalysis, molecular-formula
  reassignment, enzyme assay, flux tracing, PLSR refitting or new significance test.
- Bacterial/archaeal 16S-qSIP interval averages do not measure fungal turnover. S7
  transcript dominance is not a biomass or cell-count fraction. No resolved archaeal
  species or complete soil census is inferred.
- CGE is cumulative estimated new biomass divided by cumulative CO2 and normalized
  to the observed maximum; it is not absolute conventional carbon-use efficiency or
  a demonstrated long-term carbon-stock balance.
- FTICR-MS formula classes are semiquantitative chemical proxies, not identified source-derived
  molecules or measured nutrient transfers. Transcript associations do not establish
  enzyme activities, pathway fluxes or mediation.
- 'Source inconsistencies remain explicit: CO2 p=0.4 in text versus 0.8 in Figure
  2; 48 transcript samples versus 2×3×6 and 47 after exclusion; PLSR 644 versus 389+254;
  Table 1 versus Discussion energy counts; and one aromatic-correlation sign differing
  from S5. No convenient reconciliation or new record defect is invented from these.'
- Direct archive checks verify project identities, listed assets and immutable code
  provenance only; no dataset payload or repository code was executed. Archive generic
  datatype labels and source-specific transcriptomic titles are distinguished.
- Existing Bacteria GTDB domain identity is valid, but the historical aggregation
  count cannot be reproduced by summing mixed-rank mapping rows. No replacement count
  or study genome count is inferred.
notes:
- No canonical, cache, history, generated or saved-review files changed; all 24 inspected
  inputs remain pinned.
- 'All 20 excerpts match direct sources: eleven abstract and nine body spans. The
  full appended MD matches all twenty; the abstract-only TXT matches eleven. Its stale
  MD frontmatter is not used to infer absence of full text.'
- Completeness 95 and quality 100 (raw 111) are native mechanical scores, not scientific
  certification.
- The original source has internal count/sign/p-value inconsistencies; these are preserved
  as bounded limitations without adding unencoded defects or rerunning analyses.
- No raw omics/statistical reanalysis, code execution, paid provider, author contact
  or later-target review.
tags:
- record-review
- grassland-soil
- precipitation-legacy
- main-and-scientific-supplements-assessed
- batch-09
```
