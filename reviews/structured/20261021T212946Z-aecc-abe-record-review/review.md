# AECC ABE coculture medium, roles and strain review

- Review: 20261021T212946Z-aecc-abe-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T21:23:43.213751Z
- Finished UTC: 2026-10-21T21:29:46.285442Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Completed full-source review finds two major issues in medium input/output placement and non-graph recipient-role/acid-use scope, plus two minor issues in RNA/cDNA endpoint wording and exact strain-mapping provenance. Retain the qualified three-node/zero-arrow graph. All eight focused native checks pass; completeness 95, raw quality 111/capped 100.

## Scope And Provenance

Whole maintained record, fresh primary text/table/equations/references and all four figures, current authority and provenance assessed.

Selection: Only released CommunityMech:000323 in owned batch 11.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95812d3412d5aab41fd03422340cf736ac7b56f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000323 | kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml | maintained | Clostridium cellulovorans-Beijerinckii AECC ABE Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000323 | Focused native command exit 0. |
| validate-strict | passed | True | CommunityMech:000323 | Focused native command exit 0. |
| validate-terms | passed | True | CommunityMech:000323 | Focused native command exit 0. |
| validate-references-explained | passed | True | CommunityMech:000323 | Focused native command exit 0. |
| validate-gtdb | passed | True | CommunityMech:000323 | Focused native command exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000323 | Focused native command exit 0. |
| validate-history | passed | True | CommunityMech:000323 | Focused native command exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000323 | Focused native command exit 0. |
| audit-network | failed | True | CommunityMech:000323 | Same-batch corpus diagnostic retained. |
| check-network-quality | failed | True | CommunityMech:000323 | Same-batch corpus diagnostic retained. |
| Claim-critical primary source assessment | passed | True | CommunityMech:000323 | Whole main, all four figures, table, equations and source asset inventory assessed. |
| Reference-specific excerpt verification | passed | True | CommunityMech:000323 | All 23 occurrences match: 19 abstract, three title and one PMCID metadata. |
| Ontology and source-specific schema assessment | passed | True | CommunityMech:000323 | Eleven pairs/21 occurrences match; exact strain and roles separately assessed. |
| Optional structured adapter | unavailable | False | CommunityMech:000323 | Same-batch discovery reused with current runtime compatibility. |
| Raw-data or experimental reproduction | skipped | False | CommunityMech:000323 | No assay, image, genome or biological reanalysis. |

## Scientific And Domain Assessments

### Focal pair, origin and category

identity: supported. Targets: CommunityMech:000323.

The record denotes the intended defined laboratory coculture.

Retain ENGINEERED, SYNTHETIC and LIGNOCELLULOSE. Comparator organisms, monocultures, stock storage and analytical protocols are not additional community members or universal culture conditions.

### Species/strain resolution and GTDB provenance

grounding: concern. Targets: CommunityMech:000323.

Exact NCIMB 8052 evidence resolves the stored absent-row uncertainty.

NCBITaxon:1520 remains a valid species term; exact 290402 supports an optional coherent strain descriptor and its own 1.0/two-genome mapping. Preserve 743B 573061 and its four-genome result. No name-only selection among the species group is needed.

### Functional roles and ordinal abundance

scope: concern. Targets: CommunityMech:000323.

Donor CROSS_FEEDER needs recipient evidence; supported roles and ordinals remain.

Sugar release and relief of feedback inhibition establish donor function and a proposed benefit, not use of a named partner metabolite. Retain recipient fermentation/cross-feeding and donor primary degradation. ABUNDANT need not be replaced by a fixed numerical percentage.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000323.

Sugar-provision CROSS_FEEDING remains properly qualified.

Monoculture/coculture profiles support functional provision. Cellulose is substrate and ABE compounds are products; their co-listing does not make all of them transferred currencies. Inoculation and pH affect performance, so no provision-to-competition arrow is restored.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000323.

The PARTIAL in-situ acid contribution preserves the evidence limit.

Keep the C. cellulovorans-to-C. beijerinckii interpretation, pH/sugar covariates and lack of traced donor-resolved flux or isolated necessity. No butyrate-to-upstream-saccharification arrow is supported.

### ecological_interactions[2] and discussions[0]

graph: supported. Targets: CommunityMech:000323.

The untyped experimental population/competition node is appropriately bounded.

RNA/cDNA proportions and operating-condition comparisons do not isolate molecular competition. Keep the open mechanistic discussion and zero downstream arrows; do not promote uncertain QS annotations.

### description and related_ingredients

consistency: concern. Targets: CommunityMech:000323.

Non-graph acid-use wording should preserve the graph’s inference.

Retain source-supported in-situ cosubstrate contribution without asserting each molecule is donor-resolved. Cellulose denotes a major AECC component; butanol is a product. Butyric-acid naming matches the source and need not be forcibly changed to an anion.

### growth_media[0] input and endpoint placement

quantity: concern. Targets: CommunityMech:000323.

The recorded degraded amount and butanol output are not the initial recipe.

Replace composition input 68.6 g/L with the source-specific nominal 70 g/L initial AECC condition; move butanol out of feed composition. Preserve 68.6 g/L degradation and 11.8 g/L ABE as optimized endpoints. Do not invent exact supplementation pulses.

### Preculture, production and optimization stages

scope: concern. Targets: CommunityMech:000323.

Recoverable full Methods can replace stale abstract-only preparation prose.

Separate TGY/AECC precultures, 5-L/2-L production reactor and 500-mL/400-mL optimization flasks, pH-control durations and volumetric inocula. Pretreatment, storage, analytical temperature and N2 cooling are distinct stages. No unstated flask rpm or maintained gas-feed setpoint is inferred.

### Environment and sole-carbon wording

grounding: concern. Targets: CommunityMech:000323.

Laboratory environment is valid; chemical carbon exclusivity is not.

AECC is the authors’ designated feedstock. Sodium acetate, yeast extract, tryptone and cysteine remain explicit organic constituents. Preserve author terminology with recipe context instead of calling this chemically exclusive or defined carbon supply.

### engineering_design abundance endpoints

evidence: concern. Targets: CommunityMech:000323.

Non-graph endpoint wording should identify the RNA/cDNA 16S proxy.

The graph/discussion already gives the correct limitation. Nine/fourteen-copy normalization does not calibrate direct viable-cell counts. Keep the experimental evidence mode and stage-specific interpretation.

### GO processes, CHEBI terms and metal relevance

grounding: supported. Targets: CommunityMech:000323.

Terms are correctly labeled and their bounded process/product roles are sound.

Cellulose catabolism belongs to the primary degrader; fermentation and broad interspecies process do not prove molecular competition. Trace salts do not establish a metal-processing purpose; retain NOT_APPLICABLE.

### Reference identity, excerpts and claim support

evidence: supported. Targets: CommunityMech:000323.

All 23 occurrences are source-faithful with distinct identity and scientific scopes.

The current short cache is abstract-only. Full Methods evidence can support separately authorized enrichment; no cache refresh occurred. Title/PMCID matching validates identity, not experimental effects.

### Publications, supplements and datasets

representation: supported. Targets: CommunityMech:000323.

The two external links identify the same primary paper.

No dataset omission or cross-Mech recipe finding is established. The acquired package and XML expose no separate SI; uncertain background Gene IDs do not become focal deposits or validated genes.

### Prior review and current ownership

provenance: supported. Targets: CommunityMech:000323.

Existing graph repair and open non-graph follow-up remain correctly scoped.

Issue 1327 owns follow-up while 1325 is closed. New exact strain evidence can resolve its prior mapping uncertainty without changing historical receipts. The old source path is metadata only; all active inputs and snapshots are verified.

### Native checks and scientific completion

schema: supported. Targets: CommunityMech:000323.

Eight focused checks pass; current-claim scientific review is completed.

Corpus diagnostics retain their actual failures. The separate source audit establishes scientific scope; validation alone does not certify biology. Parent saves only the new review bundle after independent whole-candidate checks.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000323.

Completeness 95; raw quality 111, capped 100.

## Findings

### separate-medium-inputs: Separate feed recipe from degradation and solvent endpoints

major / open / confirmed; issue key: cm-000323-separate-medium-inputs.

The medium stores 68.6 g/L degraded AECC as an input and butanol as a component. Sole-carbon wording omits organic supplements and source-specific preparation/fermentation stages. Use nominal initial 70 g/L AECC and the actual recipe, keep degradation and ABE concentrations as endpoints, and document source-described supplementation without invented feed pulses. Recover stage-specific precultures, reactor/flask conditions, pH schedules and volumetric inocula. Qualify author sole-carbon wording with acetate and complex supplements.

### qualify-recipient-role: Qualify donor recipient-role and acid-use claims

major / open / confirmed; issue key: cm-000323-qualify-recipient-role.

Donor CROSS_FEEDER lacks local recipient evidence, and non-graph acid-use wording drops the source-supported inference already preserved by the graph. Identify provider, currency and utilization evidence before retaining the optional donor recipient role; otherwise omit it. Retain primary degradation, recipient fermentation/cross-feeding and inferred acid contribution. Align non-graph wording with qualified graph; do not claim transfer is impossible or demand traced flux for all broad exchange.

### qualify-population-assay: Describe the RNA/cDNA population proxy consistently

minor / open / confirmed; issue key: cm-000323-qualify-population-assay.

Non-graph 16S gene-qPCR endpoint wording omits RNA extraction and cDNA, despite correct graph/discussion caveats. Describe the experimental RNA/cDNA-based 16S proportion proxy, its nine/fourteen-copy normalization and stage-specific interpretation. Do not call it direct cell counts or validate absolute viable-cell fractions. Retain ordinal ABUNDANT and experimental evidence mode.

### resolve-strain-mapping: Resolve exact NCIMB 8052 mapping and snapshot provenance

minor / open / confirmed; issue key: cm-000323-resolve-strain-mapping.

The stored no-exact-NCIMB8052-row rationale is contradicted by verified exact strain 290402; 743B mapping provenance also overstates latest/build information. Reconcile WITHHELD using exact strain 290402, unsuffixed GTDB species, 1.0/two genomes, with coherent descriptor and ncbi_source_id. Do not substitute broad species 1520 counts or a name-only choice. Preserve valid 743B 1.0/four genomes and document the verified crosswalk hash and exact-ID routes instead of treating mtime as release.

## Recommended Actions And Acceptance Checks

### correct-feed-and-protocol

Represent source-specific medium inputs and experimental stages.

- At growth_media[0].composition, use nominal initial 70 g/L AECC from Methods and remove butanol as an added component. Preserve 68.6 g/L degraded AECC and 8.30 g/L butanol in endpoint contexts. Record fed-batch AECC supplementation without inventing exact feed doses or times from Figure 4A. Do not replace the distinct monoculture Results value 67.2 g/L with an assumed identical measurement.
- Recover the per-litre AECC recipe from Strain and medium: NH4Cl 1.5 g, K2HPO4·3H2O 1 g, KCl 0.5 g, MgSO4·7H2O 0.5 g, sodium acetate 1.65 g, yeast extract 0.5 g, tryptone 0.5 g, L-cysteine HCl 0.5 g, resazurin 0.001 g, trace-metal stock 20 mL, p-aminobenzoic acid 100 µg, thiamine 100 µg and biotin 1 µg, initially pH 7. Keep the unrecovered reference-42 trace-stock formulation explicit. Author sole-carbon wording must retain acetate/complex-supplement context in assembly_strategy, environment notes and environmental_factors[0].
- Separate C. beijerinckii TGY preculture at pH 6.5, static anaerobic 37°C for 12–16 h from C. cellulovorans AECC preculture at pH 7, static 37°C for 24 h. Preserve their actual recipe differences. Do not copy glycerol storage, biomass pretreatment or analytical temperatures into fermentation conditions; N2 cooling is preparation scope.
- Represent the 5-L/2-L production reactor at 37°C and 100 rpm separately from 500-mL/400-mL optimization flasks. Initial 0.5%/10% v/v inocula and 36-h pH control differ from optimized simultaneous 1%/10% v/v and first-24-h pH 7 control followed by uncontrolled pH. Keep 5 N NaOH as the control reagent; do not infer flask rpm, nutrient feeding from titrant, or cell fractions from volume ratios.
- Replace obsolete abstract-only preparation prose with precise Methods evidence. Keep optimized less-than-80-h abstract timing separate from generic incubation and the Conclusion 80-h statement. Future cache enrichment must preserve exact source/version and existing cache bytes/history through the authorized workflow.

### qualify-role-and-acid

Align non-graph interpretation with source-local recipient evidence.

- For taxonomy[0].functional_role CROSS_FEEDER, identify the partner provider, metabolite and utilization evidence before retention; otherwise omit this optional recipient role. Sugar donation, improved cellulose degradation and benefit from product removal alone do not meet the literal utilization definition. Do not claim reciprocal utilization is impossible.
- Qualify acid contribution consistently in description, taxonomy[1].taxon_term.notes and related_ingredients[1].relevance, using monoculture/coculture acid profiles and reassimilation as support for an inferred in-situ cosubstrate contribution. Preserve the lack of donor-resolved molecular flux and isolated butyrate necessity, without requiring such proof for every broad exchange statement.
- Retain C. cellulovorans PRIMARY_DEGRADER and C. beijerinckii SECONDARY_FERMENTER/CROSS_FEEDER. Preserve all three graph nodes, zero arrows and open mechanistic discussion. Do not restore acid-to-saccharification or provision-to-competition arrows; do not promote uncertain QS Gene IDs.

### qualify-assay

Make the non-graph abundance endpoint match the actual method.

- Update engineering_design.perturbation_design and measurement_endpoints[5] to state experimental RNA extraction, cDNA synthesis and species-specific 16S assay proportions. Keep the source’s target-copy terminology attributed and the nine/fourteen-copy normalization explicit if described.
- State that this proxy is not direct cell counting or an independent calibration of absolute viable-cell fractions. Preserve early/late stage scope, current graph/discussion qualification, ordinal ABUNDANT and IN_VITRO evidence. No universal percentage, equal biomass or fixed dominance is inferred.

### resolve-taxonomy

Use exact strain evidence with coherent mapping provenance.

- Reconcile taxonomy[1].taxon_term WITHHELD and its no-direct-row rationale using exact NCBITaxon:290402, Clostridium beijerinckii NCIMB 8052, parent 1520. The verified exact row maps to GTDB:s__Clostridium_beijerinckii with majority 1.0 and two genomes via ncbi_id. If representing this strain classification, keep term rank, descriptor and ncbi_source_id coherent; do not attach strain support counts to a 1520 species block.
- Keep broad species 1520 aggregate 0.87/741 distinct from the exact strain evidence and its A/E name-group context. Retain valid 743B 573061 mapping to Clostridium_K cellulovorans at 1.0/four genomes. Replace latest/build-date assertions with verified crosswalk SHA 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd, exact-ID route and accurately labeled snapshot date.
- Keep source designations separate from optional collection aliases. Direct DSMZ verifies 743B/DSM 3052/ATCC 35296; ATCC 51743/NCIMB 8052 is only primary indexed-product-sheet corroboration because direct opens timed out. Historical deposited-as acetobutylicum does not identify ATCC 824. No catalogue medium or newly sequenced genome is inferred.

### verify-future-curation

Validate separately authorized repairs and preserve the graph.

- Attach exact source/section evidence to each changed claim and retain the existing graph qualifications and source-specific uncertainties. Coordinate through existing 1327 without reopening closed 1325 solely because non-graph changes remain.
- After authorized canonical edits, append required history and run schema, strict, terms, references, GTDB, domain and history checks, followed by just gen-html and just check-docs-current. Verify changed-input hashes rather than silently refreshing them.
- This review modifies no canonical YAML, cache, history or generated output. Parent may save only the new immutable review bundle after independent whole-candidate checks. Native completeness/quality scores are not biological validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml; Whole maintained YAML | supports | Defined AECC-to-ABE coculture, three nodes and zero arrows. The graph already qualifies acid contribution and the population assay; non-graph fields need consistent scope. |
| identity | PMID:25023325; DOI:10.1186/s12934-014-0092-5; Methods: Strain and medium; Background; Table 1 | supports | The study pairs C. cellulovorans 743B from DSMZ with supplied C. beijerinckii NCIMB 8052. Other organisms in Background and Table 1 are comparison systems. This is deliberate laboratory assembly; engineered state does not mean the strains were genetically engineered. |
| pretreatment | PMID:25023325; DOI:10.1186/s12934-014-0092-5; Methods: Alkali extracted deshelled corn cobs (AECC) | supports | Ground corn cobs are pretreated with 1% w/v NaOH at 121°C for 20 min, neutralized with 1% w/v sulfuric acid, washed and dried at 80°C for 24 h. AECC contains 69.8% cellulose, 27.4% hemicellulose and 1.47% lignin by weight. It is heterogeneous feedstock; CHEBI cellulose represents a component. These temperatures are pretreatment conditions. |
| medium | PMID:25023325; DOI:10.1186/s12934-014-0092-5; Methods: Strain and medium, AECC-medium paragraph | supports | Nominal initial medium contains 70 g/L AECC, NH4Cl 1.5 g/L, K2HPO4·3H2O 1 g/L, KCl 0.5 g/L, MgSO4·7H2O 0.5 g/L, sodium acetate 1.65 g/L, yeast extract 0.5 g/L, tryptone 0.5 g/L, L-cysteine HCl 0.5 g/L, resazurin 0.001 g/L, trace-metal stock 20 mL/L, p-aminobenzoic acid 100 µg/L, thiamine 100 µg/L and biotin 1 µg/L, initially pH 7. The trace-stock formulation is cited to reference 42 and was not independently recovered. |
| preculture | PMID:25023325; DOI:10.1186/s12934-014-0092-5; Methods: Strain and medium, stock and preculture paragraphs | supports | C. beijerinckii TGY preculture has tryptone 5 g/L, yeast extract 3 g/L, glucose 2 g/L, L-cysteine HCl 0.25 g/L and resazurin 0.001 g/L, pH 6.5, static anaerobic 37°C for 12–16 h. C. cellulovorans uses 200 mL AECC medium, static 37°C for 24 h. Storage in 25% glycerol at −80°C is separate. Cooling medium under 100% N2 describes anaerobic preparation, not a quantified continuous gas feed. |
| culture | PMID:25023325; DOI:10.1186/s12934-014-0092-5; Methods: ABE fermentation from AECC; Results and discussion: Optimization of the co-culture conditions and its three subsections; Figure 3 | supports | Fermentations use a 5-L reactor with 2-L working volume at 37°C and 100 rpm. Optimization uses 500-mL flasks with 400-mL working volume and pH-control equipment. Initial coculture uses C. beijerinckii 0.5% and C. cellulovorans 10% v/v with pH 7 for 36 h; the optimized condition uses simultaneous 1%/10% v/v inocula and pH 7 for 24 h, then uncontrolled pH. Volumetric inocula are not direct cell fractions; flask rpm is not independently specified. |
| endpoints | PMID:25023325; DOI:10.1186/s12934-014-0092-5; Abstract Results; Results and discussion: ABE fermentation from AECC under optimized co-culture conditions; Conclusion; Figure 4A–C | supports | Optimized 68.6 g/L AECC degraded and 11.8 g/L ABE, comprising 2.64 acetone, 8.30 butanol and 0.87 ethanol, are outcomes. Butanol is not a feed component. The main describes fed-batch AECC supplementation; exact pulse quantities or times are not extracted from the plot. Abstract less than 80 h and Conclusion 80 h remain attributed descriptions of this experiment. |
| supply | PMID:25023325; DOI:10.1186/s12934-014-0092-5; Results and discussion: Construction of symbiosis by co-culture of C. beijerinckii and C. cellulovorans with AECC as the sole carbon source; Figures 1–2 | supports | Monocultures and coculture show cellulose degradation, soluble-sugar profiles, acid formation and solvent production. C. beijerinckii grows poorly on AECC alone. Reduced sugar accumulation in coculture supports provision of hydrolysis products and a proposed reduction of cellulase feedback inhibition. Process improvement does not identify a reciprocal metabolite utilized by C. cellulovorans. |
| acid | PMID:25023325; DOI:10.1186/s12934-014-0092-5; Results and discussion: Construction of symbiosis by co-culture of C. beijerinckii and C. cellulovorans with AECC as the sole carbon source; ABE fermentation from AECC under optimized co-culture conditions; Figures 1–2 and 4 | supports | C. cellulovorans produces butyric acid and the coculture produces butanol without external butyric-acid supplementation. Acid accumulation and reassimilation support an in-situ cosubstrate interpretation. This does not trace each acid molecule to its donor or isolate butyrate necessity from pH, sugar availability and inoculation changes. Retain the inference; do not turn absence of resolved flux into proof that transfer cannot occur. |
| population | PMID:25023325; DOI:10.1186/s12934-014-0092-5; Methods: Real-time PCR, equations 1–2; Results and discussion: Dynamics of the abundance of C. beijerinckii and C. cellulovorans during the co-culture process; Figure 4D | supports | The assay extracts total RNA, reverse transcribes cDNA and measures species-specific 16S targets. Equations divide the two target estimates by nine and fourteen before normalization. This is an experimental proportion proxy, not direct cell counting. Early and late dominance are assay- and stage-specific; the source leaves molecular cooperation/competition mechanisms unresolved. |
| analysis | PMID:25023325; DOI:10.1186/s12934-014-0092-5; Methods: Analysis | supports | Cell mass on AECC is estimated from protein using a protein/dry-weight factor calibrated on cellobiose and assumed for AECC. Residual AECC is estimated from pellet dry weight minus estimated cell mass. Analytical cellulase, chromatographic and PCR conditions are separate from cultivation. No independent assay reanalysis or biomass recalibration was performed. |
| ontology | /private/tmp/cm-review-session/batch-11/000323/ontology-authority.json; Eleven ID-label pairs across 21 occurrences; definitions and field locations | supports | All labels match. Five chemical identities cover cellulose, butyric acid and ABE products; cellulose is a feedstock component. Source-specific process scope does not make every participant cellulolytic or every listed metabolite a transferred currency. |
| schema | /private/tmp/cm-review-session/batch-11/000323/child-schema-semantics.json; FunctionalRoleEnum, InteractionTypeEnum, AbundanceEnum and cultivation boundaries | supports | CROSS_FEEDER requires utilization of another taxon metabolite; PRIMARY_DEGRADER concerns complex substrates; SECONDARY_FERMENTER concerns fermentation of primary-degradation products. ABUNDANT is ordinal. No obligacy, carbon-assimilation-only or fixed-percentage requirement is imposed. |
| gtdb | /private/tmp/cm-review-session/batch-11/000323/child-gtdb-crosswalk.json; Exact encoded rows 573061 and 1520, snapshot and routes | supports | The current 743B assignment reproduces 1.0/four genomes via exact ID. Species 1520 independently has 0.87/741 genomes. These aggregate counts must not be used as the exact NCIMB 8052 strain result. File mtime is not a verified GTDB release or build date. |
| strain | /private/tmp/cm-review-session/batch-11/000323/child-strain-authority.json; Source strain identity, current NCBI ranks/parents, catalogues and exact_ncimb8052_gtdb | supports | Exact strain NCBITaxon:290402 explicitly names NCIMB 8052 and resolves to GTDB:s__Clostridium_beijerinckii with 1.0/two genomes via ncbi_id. This contradicts the stored absent-row rationale. Direct DSMZ supports 743B/DSM 3052/ATCC 35296; ATCC 51743/NCIMB 8052 is corroborated by a primary search-index product-sheet excerpt, while direct ATCC opens timed out. No strain-count transfer into a species descriptor is justified. |
| semantics | /private/tmp/cm-review-session/batch-11/000323/ontology-semantic-notes.json; Final source-specific roles, chemistry, abundance and mapping assessment | supports | Retain all three nodes and zero arrows, donor PRIMARY_DEGRADER, recipient SECONDARY_FERMENTER/CROSS_FEEDER and ordinal ABUNDANT. Repair donor recipient-role support, medium input/output placement, non-graph assay scope and exact strain provenance. |
| resources | /private/tmp/cm-review-session/batch-11/000323/dataset-verification.json; Publication identity, full Methods/resource contexts and eight-file inventory | supports | PMID and PMCID identify the same primary publication and are correctly represented as external resources. Four JPEGs and four thumbnails match the package; no separate supplement is declared in inspected XML. Uncertain QS Gene IDs in Discussion are hypotheses, not new deposits or validated mechanisms. No dataset omission finding is established. |
| snippets | /private/tmp/cm-review-session/batch-11/000323/snippet-source-audit.json; 23 reference-specific excerpt occurrences | supports | All 23 excerpts strictly match their fresh source and short cache: 19 abstract, three title and one PMCID metadata occurrence. This is a partition of field occurrences, not distinct experiments or exclusively body evidence. Literal matching does not establish role direction, chemical exclusivity or medium-input placement. |
| history | /private/tmp/cm-review-session/batch-11/000323/provenance-audit.json; Sole history, exact batch 19 decision/adversarial context, fresh 1325/1327 bodies and comments | supports | The prior review removed unsupported causal edges and qualified population/acid claims. Issue 1325 is closed with one comment; 1327 remains open with zero comments and owns non-graph follow-up. The current exact strain row is new evidence resolving its older mapping uncertainty. No issue mutation occurred. |
| historical-source | /private/tmp/cm-review-session/batch-11/000323/historical-source-byte-comparison.json; Exact prior source hash versus fresh XML | supports | Fresh XML equals the prior recorded hash. The unavailable old pathname remains historical metadata; no old file is reconstructed and no active hash exception is used. |
| inspect | /private/tmp/cm-review-session/batch-11/000323/inspect.json; Fresh official 26-input inspection | supports | The exact canonical owner and base were inspected before judgments. Ignored-inclusive discovery found the focal cache, history and batch 19 decision/adversarial pair; no batch 91 transfer from another record. |
| assets | /private/tmp/cm-review-session/batch-11/000323/lead-source-assets.json; Fresh main and genuine package inventory; four figure reads | supports | Fresh main is available despite the initial PMC browser captcha. The acquired package has four main figures and thumbnails only; zero XML supplementary-material/media elements and no separate SI declaration were identified. This bounded inventory leaves no current-claim-critical gap, without asserting global absence. |
| lead-read | /private/tmp/cm-review-session/batch-11/000323/lead-primary-read-scope.json; Whole primary text, equations, table, references and four figures | supports | Lead read the complete 42,911-character main projection, all 47 references, Table 1 and both equations, and viewed all four JPEGs. Source/authority scopes and limits are explicit; no numerical reanalysis or exact feed-pulse digitization occurred. |
| source-scope | /private/tmp/cm-review-session/batch-11/000323/source-audit.json; Final four finding groups and source completion | supports | Completed scientific assessment: two major findings concern feed/product placement and recipient-role/acid-use scope; two minors concern RNA/cDNA endpoint wording and recoverable strain-mapping provenance. |
| root-source | /private/tmp/cm-review-session/batch-11/000323/root-independent-source-audit.json; Independent whole primary, figure, authority and provenance assessment | supports | Root independently read the full main, all references, table and equations, all four figures, and the exact raw 290402 crosswalk row. Its completed assessment agrees with all four groups and the explicit source limits. |
| metrics | /private/tmp/cm-review-session/batch-11/000323/support-final-audit.json; Distinct final support and native arithmetic | supports | Completeness 95. Three nodes, zero arrows and six node-evidence occurrences give mean two. Two major/two minor findings yield raw quality 111, capped 100; all 26 inspected inputs remain unchanged. |
| support-manifest | /private/tmp/cm-review-session/batch-11/000323/supporting-artifact-manifest.json; Final supporting artifacts and hashes | supports | The manifest binds finalized source-specific resources, excerpts, provenance and actual read scopes. Preliminary support remains immutable. |
| auxiliary | /private/tmp/cm-review-session/batch-11/000323/auxiliary-frozen-manifest.json; Final native/authority receipts and unchanged inputs | supports | Eight focused native checks pass, eleven ontology pairs across 21 occurrences match, and the exact strain lookup is preserved separately from species mappings. No canonical or cache mutation. |
| final-native | /private/tmp/cm-review-session/batch-11/000323/final-validator-summary.json; Actual eight command results and final input integrity | supports | Schema, strict, terms, references, GTDB, domain, history and cache-name checks pass. Initial summary remains unchanged; native success does not prove every scientific interpretation. |
| adapter | /private/tmp/cm-review-session/batch-11/000323/adapter-check.json; Batch 11 discovery from 403 at 2026-10-21T19:20:45.556660+00:00; current runtime compatibility | supports | Optional adapter unavailability is scoped to the owned runtime with explicit same-batch discovery reuse. The other-checkout runner was not executed; no installation or global absence claim occurred. |
| check-validate | /private/tmp/cm-review-session/batch-11/000323/validate.json; Actual focused command and output | supports | Recorded native result; biological entailment assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-11/000323/validate-strict.json; Actual focused command and output | supports | Recorded native result; biological entailment assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-11/000323/validate-terms.json; Actual focused command and output | supports | Recorded native result; biological entailment assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-11/000323/validate-references-explained.json; Actual focused command and output | supports | Recorded native result; biological entailment assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-11/000323/validate-gtdb.json; Actual focused command and output | supports | Recorded native result; biological entailment assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-11/000323/validate-gtdb-domain.json; Actual focused command and output | supports | Recorded native result; biological entailment assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-11/000323/validate-history.json; Actual focused command and output | supports | Recorded native result; biological entailment assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-11/000323/normalize-cache-names-check.json; Actual focused command and output | supports | Recorded native result; biological entailment assessed separately. |
| check-audit-network | /private/tmp/cm-review-session/batch-11/audit-network.json; Same-batch corpus diagnostic | supports | Actual corpus nonzero result retained; no later record is assessed. |
| check-check-network-quality | /private/tmp/cm-review-session/batch-11/check-network-quality.json; Same-batch corpus diagnostic | supports | Actual corpus nonzero result retained; no later record is assessed. |

## Limits And Additional Notes

- All current claim-critical main sources are assessed. The acquired eight-file package contains four main JPEGs and four thumbnails; inspected XML has no separate supplement declaration. This bounded inventory is not proof that no other material exists elsewhere. The trace-stock formulation cited to reference 42 remains unrecovered.
- No raw data, image digitization, biological experiment, genome analysis or model execution was performed. AECC feed pulses are not quantified from Figure 4A. Protein-derived biomass, pellet-derived substrate estimates and RNA/cDNA proportions retain their analytical assumptions.
- Sugar supply and in-situ acid contribution remain source-supported interpretations. Partner-resolved flux, unique butyrate necessity and molecular competition/QS are not established. Source author terminology does not erase these limits or impose an obligatory/nutrient-only role definition.
- All 23 excerpt occurrences strictly match the short cache and fresh reference-specific source: 19 abstract, three title and one PMCID metadata. No cache enrichment occurred, and metadata/lexical matching is not scientific entailment.
- Strain 290402 mapping is exact local-crosswalk evidence, not a new genome analysis. Species aggregate 1520 counts remain distinct. ATCC alias corroboration uses an indexed primary excerpt; direct opens timed out. Crosswalk mtime is not a verified release/build date.
- The old source pathname is historical metadata with an independently matching fresh XML hash, not an active missing pin. Preliminary support and initial validators remain immutable. Adapter discovery is explicitly reused from record 403 with current compatibility checks; no external other-checkout runner was invoked.
- Completed scientific review; two major/two minor findings; completeness 95, raw quality 111/capped 100.
- Preserve valid pair identity, ordinals, graph and metal scope; no dataset omission finding.
- No canonical edits or save by lead; parent persistence follows whole-candidate checks.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T212946Z-aecc-abe-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: AECC ABE coculture medium, roles and strain review
started_at: '2026-10-21T21:23:43.213751Z'
finished_at: '2026-10-21T21:29:46.285442Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed science, auxiliary authorities and
    support; no person-level independence asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Completed full-source review finds two major issues in medium input/output
  placement and non-graph recipient-role/acid-use scope, plus two minor issues in
  RNA/cDNA endpoint wording and exact strain-mapping provenance. Retain the qualified
  three-node/zero-arrow graph. All eight focused native checks pass; completeness
  95, raw quality 111/capped 100.
source:
  git_revision: 95812d3412d5aab41fd03422340cf736ac7b56f3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/ground-taxa-gtdb/SKILL.md
    sha256: 6358a4324781ce2598554dca18ef952ec03c9d4a9df33f82f5db8ea5e986969b
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
  - path: history/records/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture/2026-10-05T234230Z-codex-a71416.yaml
    sha256: 94a6b1d25e02ba4f21d80fa3e398b616df4aa31468735fe727fb4ad2468237f0
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    sha256: caf85d65ddbfd4b6c591335118414b5a2ceda81b17fbd201a4b1c8fb8641ce2c
    role: target
  - path: references_cache/PMID_25023325.md
    sha256: f7a1480962fad030f4ad09055620073fdd4dfd22adcef1d4afe357d43386cf18
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261005-batch19.yaml
    sha256: 08d6f18b92836076a26b7aad98a6bfdbfbcfcea4a27124ead6d0546fa7b0e70b
    role: context
  - path: reports/causal_graph_review/decisions/20261005-three-records-batch19.yaml
    sha256: 2f4684d88aa8b70f6ed84c0726aadad8dfb5f1b31c8a2e93b5f682264da69490
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
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
- target_id: CommunityMech:000323
  path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
  label: Clostridium cellulovorans-Beijerinckii AECC ABE Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    role: canonical_record
scope:
  description: Whole maintained record, fresh primary text/table/equations/references
    and all four figures, current authority and provenance assessed.
  selection: Only released CommunityMech:000323 in owned batch 11.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000323
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000323
  command: just --no-dotenv validate kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Owned batch 11 runtime; unchanged canonical inputs.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000323
  command: just --no-dotenv validate-strict kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-11/000323/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Owned batch 11 runtime; unchanged canonical inputs.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000323
  command: just --no-dotenv validate-terms kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Owned batch 11 runtime; unchanged canonical inputs.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000323
  command: just --no-dotenv validate-references-explained kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Owned batch 11 runtime; unchanged canonical inputs.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000323
  command: just --no-dotenv validate-gtdb kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Owned batch 11 runtime; unchanged canonical inputs.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000323
  command: just --no-dotenv validate-gtdb-domain kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Owned batch 11 runtime; unchanged canonical inputs.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000323
  command: just --no-dotenv validate-history history/records/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Owned batch 11 runtime; unchanged canonical inputs.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000323
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Owned batch 11 runtime; unchanged canonical inputs.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Same-batch corpus diagnostic retained.
  target_ids:
  - CommunityMech:000323
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - metrics
  scope_note: Explicit batch 11 diagnostic reuse; focused target checks pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Same-batch corpus diagnostic retained.
  target_ids:
  - CommunityMech:000323
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-11/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - metrics
  scope_note: Explicit batch 11 diagnostic reuse; focused target checks pass.
- check_id: scientific-source
  name: Claim-critical primary source assessment
  status: passed
  required: true
  summary: Whole main, all four figures, table, equations and source asset inventory
    assessed.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - assets
  - lead-read
  - source-scope
  - root-source
- check_id: direct-excerpts
  name: Reference-specific excerpt verification
  status: passed
  required: true
  summary: 'All 23 occurrences match: 19 abstract, three title and one PMCID metadata.'
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - snippets
- check_id: authority-review
  name: Ontology and source-specific schema assessment
  status: passed
  required: true
  summary: Eleven pairs/21 occurrences match; exact strain and roles separately assessed.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - ontology
  - schema
  - strain
  - gtdb
- check_id: adapter
  name: Optional structured adapter
  status: unavailable
  required: false
  summary: Same-batch discovery reused with current runtime compatibility.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - adapter
- check_id: reanalysis
  name: Raw-data or experimental reproduction
  status: skipped
  required: false
  summary: No assay, image, genome or biological reanalysis.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - lead-read
  - resources
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
  locator: Whole maintained YAML
  summary: Defined AECC-to-ABE coculture, three nodes and zero arrows. The graph already
    qualifies acid contribution and the population assay; non-graph fields need consistent
    scope.
  support: supports
  accessed_at: '2026-10-21T21:29:46.280273Z'
- evidence_id: identity
  kind: primary_source
  reference: PMID:25023325; DOI:10.1186/s12934-014-0092-5
  locator: 'Methods: Strain and medium; Background; Table 1'
  summary: The study pairs C. cellulovorans 743B from DSMZ with supplied C. beijerinckii
    NCIMB 8052. Other organisms in Background and Table 1 are comparison systems.
    This is deliberate laboratory assembly; engineered state does not mean the strains
    were genetically engineered.
  support: supports
  accessed_at: '2026-10-21T21:29:46.280345Z'
  snapshot_sha256: 6a213942846cec1ba99d6fe3df0d65f9add34568a818adfb69fce41cac2c8968
- evidence_id: pretreatment
  kind: primary_source
  reference: PMID:25023325; DOI:10.1186/s12934-014-0092-5
  locator: 'Methods: Alkali extracted deshelled corn cobs (AECC)'
  summary: Ground corn cobs are pretreated with 1% w/v NaOH at 121°C for 20 min, neutralized
    with 1% w/v sulfuric acid, washed and dried at 80°C for 24 h. AECC contains 69.8%
    cellulose, 27.4% hemicellulose and 1.47% lignin by weight. It is heterogeneous
    feedstock; CHEBI cellulose represents a component. These temperatures are pretreatment
    conditions.
  support: supports
  accessed_at: '2026-10-21T21:29:46.280677Z'
  snapshot_sha256: 6a213942846cec1ba99d6fe3df0d65f9add34568a818adfb69fce41cac2c8968
- evidence_id: medium
  kind: primary_source
  reference: PMID:25023325; DOI:10.1186/s12934-014-0092-5
  locator: 'Methods: Strain and medium, AECC-medium paragraph'
  summary: Nominal initial medium contains 70 g/L AECC, NH4Cl 1.5 g/L, K2HPO4·3H2O
    1 g/L, KCl 0.5 g/L, MgSO4·7H2O 0.5 g/L, sodium acetate 1.65 g/L, yeast extract
    0.5 g/L, tryptone 0.5 g/L, L-cysteine HCl 0.5 g/L, resazurin 0.001 g/L, trace-metal
    stock 20 mL/L, p-aminobenzoic acid 100 µg/L, thiamine 100 µg/L and biotin 1 µg/L,
    initially pH 7. The trace-stock formulation is cited to reference 42 and was not
    independently recovered.
  support: supports
  accessed_at: '2026-10-21T21:29:46.280744Z'
  snapshot_sha256: 6a213942846cec1ba99d6fe3df0d65f9add34568a818adfb69fce41cac2c8968
- evidence_id: preculture
  kind: primary_source
  reference: PMID:25023325; DOI:10.1186/s12934-014-0092-5
  locator: 'Methods: Strain and medium, stock and preculture paragraphs'
  summary: C. beijerinckii TGY preculture has tryptone 5 g/L, yeast extract 3 g/L,
    glucose 2 g/L, L-cysteine HCl 0.25 g/L and resazurin 0.001 g/L, pH 6.5, static
    anaerobic 37°C for 12–16 h. C. cellulovorans uses 200 mL AECC medium, static 37°C
    for 24 h. Storage in 25% glycerol at −80°C is separate. Cooling medium under 100%
    N2 describes anaerobic preparation, not a quantified continuous gas feed.
  support: supports
  accessed_at: '2026-10-21T21:29:46.280802Z'
  snapshot_sha256: 6a213942846cec1ba99d6fe3df0d65f9add34568a818adfb69fce41cac2c8968
- evidence_id: culture
  kind: primary_source
  reference: PMID:25023325; DOI:10.1186/s12934-014-0092-5
  locator: 'Methods: ABE fermentation from AECC; Results and discussion: Optimization
    of the co-culture conditions and its three subsections; Figure 3'
  summary: Fermentations use a 5-L reactor with 2-L working volume at 37°C and 100
    rpm. Optimization uses 500-mL flasks with 400-mL working volume and pH-control
    equipment. Initial coculture uses C. beijerinckii 0.5% and C. cellulovorans 10%
    v/v with pH 7 for 36 h; the optimized condition uses simultaneous 1%/10% v/v inocula
    and pH 7 for 24 h, then uncontrolled pH. Volumetric inocula are not direct cell
    fractions; flask rpm is not independently specified.
  support: supports
  accessed_at: '2026-10-21T21:29:46.280855Z'
  snapshot_sha256: 6a213942846cec1ba99d6fe3df0d65f9add34568a818adfb69fce41cac2c8968
- evidence_id: endpoints
  kind: primary_source
  reference: PMID:25023325; DOI:10.1186/s12934-014-0092-5
  locator: 'Abstract Results; Results and discussion: ABE fermentation from AECC under
    optimized co-culture conditions; Conclusion; Figure 4A–C'
  summary: Optimized 68.6 g/L AECC degraded and 11.8 g/L ABE, comprising 2.64 acetone,
    8.30 butanol and 0.87 ethanol, are outcomes. Butanol is not a feed component.
    The main describes fed-batch AECC supplementation; exact pulse quantities or times
    are not extracted from the plot. Abstract less than 80 h and Conclusion 80 h remain
    attributed descriptions of this experiment.
  support: supports
  accessed_at: '2026-10-21T21:29:46.280910Z'
  snapshot_sha256: 6a213942846cec1ba99d6fe3df0d65f9add34568a818adfb69fce41cac2c8968
- evidence_id: supply
  kind: primary_source
  reference: PMID:25023325; DOI:10.1186/s12934-014-0092-5
  locator: 'Results and discussion: Construction of symbiosis by co-culture of C.
    beijerinckii and C. cellulovorans with AECC as the sole carbon source; Figures
    1–2'
  summary: Monocultures and coculture show cellulose degradation, soluble-sugar profiles,
    acid formation and solvent production. C. beijerinckii grows poorly on AECC alone.
    Reduced sugar accumulation in coculture supports provision of hydrolysis products
    and a proposed reduction of cellulase feedback inhibition. Process improvement
    does not identify a reciprocal metabolite utilized by C. cellulovorans.
  support: supports
  accessed_at: '2026-10-21T21:29:46.280974Z'
  snapshot_sha256: 6a213942846cec1ba99d6fe3df0d65f9add34568a818adfb69fce41cac2c8968
- evidence_id: acid
  kind: primary_source
  reference: PMID:25023325; DOI:10.1186/s12934-014-0092-5
  locator: 'Results and discussion: Construction of symbiosis by co-culture of C.
    beijerinckii and C. cellulovorans with AECC as the sole carbon source; ABE fermentation
    from AECC under optimized co-culture conditions; Figures 1–2 and 4'
  summary: C. cellulovorans produces butyric acid and the coculture produces butanol
    without external butyric-acid supplementation. Acid accumulation and reassimilation
    support an in-situ cosubstrate interpretation. This does not trace each acid molecule
    to its donor or isolate butyrate necessity from pH, sugar availability and inoculation
    changes. Retain the inference; do not turn absence of resolved flux into proof
    that transfer cannot occur.
  support: supports
  accessed_at: '2026-10-21T21:29:46.281026Z'
  snapshot_sha256: 6a213942846cec1ba99d6fe3df0d65f9add34568a818adfb69fce41cac2c8968
- evidence_id: population
  kind: primary_source
  reference: PMID:25023325; DOI:10.1186/s12934-014-0092-5
  locator: 'Methods: Real-time PCR, equations 1–2; Results and discussion: Dynamics
    of the abundance of C. beijerinckii and C. cellulovorans during the co-culture
    process; Figure 4D'
  summary: The assay extracts total RNA, reverse transcribes cDNA and measures species-specific
    16S targets. Equations divide the two target estimates by nine and fourteen before
    normalization. This is an experimental proportion proxy, not direct cell counting.
    Early and late dominance are assay- and stage-specific; the source leaves molecular
    cooperation/competition mechanisms unresolved.
  support: supports
  accessed_at: '2026-10-21T21:29:46.281078Z'
  snapshot_sha256: 6a213942846cec1ba99d6fe3df0d65f9add34568a818adfb69fce41cac2c8968
  quote: Total RNA
- evidence_id: analysis
  kind: primary_source
  reference: PMID:25023325; DOI:10.1186/s12934-014-0092-5
  locator: 'Methods: Analysis'
  summary: Cell mass on AECC is estimated from protein using a protein/dry-weight
    factor calibrated on cellobiose and assumed for AECC. Residual AECC is estimated
    from pellet dry weight minus estimated cell mass. Analytical cellulase, chromatographic
    and PCR conditions are separate from cultivation. No independent assay reanalysis
    or biomass recalibration was performed.
  support: supports
  accessed_at: '2026-10-21T21:29:46.281129Z'
  snapshot_sha256: 6a213942846cec1ba99d6fe3df0d65f9add34568a818adfb69fce41cac2c8968
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-11/000323/ontology-authority.json
  locator: Eleven ID-label pairs across 21 occurrences; definitions and field locations
  summary: All labels match. Five chemical identities cover cellulose, butyric acid
    and ABE products; cellulose is a feedstock component. Source-specific process
    scope does not make every participant cellulolytic or every listed metabolite
    a transferred currency.
  support: supports
  accessed_at: '2026-10-21T21:29:46.281187Z'
  snapshot_sha256: b2ca9add4ab6f59dfca4353c3a3add44162ef52b9d49529875030105331fb605
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-11/000323/child-schema-semantics.json
  locator: FunctionalRoleEnum, InteractionTypeEnum, AbundanceEnum and cultivation
    boundaries
  summary: CROSS_FEEDER requires utilization of another taxon metabolite; PRIMARY_DEGRADER
    concerns complex substrates; SECONDARY_FERMENTER concerns fermentation of primary-degradation
    products. ABUNDANT is ordinal. No obligacy, carbon-assimilation-only or fixed-percentage
    requirement is imposed.
  support: supports
  accessed_at: '2026-10-21T21:29:46.281405Z'
  snapshot_sha256: af81baf7c8442ff203f2494fa3197cc9903dd94336d11351997158060f964605
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-11/000323/child-gtdb-crosswalk.json
  locator: Exact encoded rows 573061 and 1520, snapshot and routes
  summary: The current 743B assignment reproduces 1.0/four genomes via exact ID. Species
    1520 independently has 0.87/741 genomes. These aggregate counts must not be used
    as the exact NCIMB 8052 strain result. File mtime is not a verified GTDB release
    or build date.
  support: supports
  accessed_at: '2026-10-21T21:29:46.281600Z'
  snapshot_sha256: 3cad4f3a7a6b1b9483f6b1c3634dd0b4b672b1f214be4714b34ee72334141dd8
- evidence_id: strain
  kind: authority
  reference: /private/tmp/cm-review-session/batch-11/000323/child-strain-authority.json
  locator: Source strain identity, current NCBI ranks/parents, catalogues and exact_ncimb8052_gtdb
  summary: Exact strain NCBITaxon:290402 explicitly names NCIMB 8052 and resolves
    to GTDB:s__Clostridium_beijerinckii with 1.0/two genomes via ncbi_id. This contradicts
    the stored absent-row rationale. Direct DSMZ supports 743B/DSM 3052/ATCC 35296;
    ATCC 51743/NCIMB 8052 is corroborated by a primary search-index product-sheet
    excerpt, while direct ATCC opens timed out. No strain-count transfer into a species
    descriptor is justified.
  support: supports
  accessed_at: '2026-10-21T21:29:46.281734Z'
  snapshot_sha256: c0d744fbe267c3e1605226fcb23dd0379c1c1edd3f1742ce000329f1ffe52a69
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-11/000323/ontology-semantic-notes.json
  locator: Final source-specific roles, chemistry, abundance and mapping assessment
  summary: Retain all three nodes and zero arrows, donor PRIMARY_DEGRADER, recipient
    SECONDARY_FERMENTER/CROSS_FEEDER and ordinal ABUNDANT. Repair donor recipient-role
    support, medium input/output placement, non-graph assay scope and exact strain
    provenance.
  support: supports
  accessed_at: '2026-10-21T21:29:46.281912Z'
  snapshot_sha256: b01ec4aa5539e67076fa7ae85d82387824f74f62844327034a2ea4846f641b87
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/dataset-verification.json
  locator: Publication identity, full Methods/resource contexts and eight-file inventory
  summary: PMID and PMCID identify the same primary publication and are correctly
    represented as external resources. Four JPEGs and four thumbnails match the package;
    no separate supplement is declared in inspected XML. Uncertain QS Gene IDs in
    Discussion are hypotheses, not new deposits or validated mechanisms. No dataset
    omission finding is established.
  support: supports
  accessed_at: '2026-10-21T21:29:46.282078Z'
  snapshot_sha256: d7da7aa3b809e573ee1bf5a86f0dcfa065dd71283f7d4263afa32b296981e649
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/snippet-source-audit.json
  locator: 23 reference-specific excerpt occurrences
  summary: 'All 23 excerpts strictly match their fresh source and short cache: 19
    abstract, three title and one PMCID metadata occurrence. This is a partition of
    field occurrences, not distinct experiments or exclusively body evidence. Literal
    matching does not establish role direction, chemical exclusivity or medium-input
    placement.'
  support: supports
  accessed_at: '2026-10-21T21:29:46.282218Z'
  snapshot_sha256: 7679132caf44d0e40e5444dd576f8c7da647a10374d5895e9b19da07f3b91a68
- evidence_id: history
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-11/000323/provenance-audit.json
  locator: Sole history, exact batch 19 decision/adversarial context, fresh 1325/1327
    bodies and comments
  summary: The prior review removed unsupported causal edges and qualified population/acid
    claims. Issue 1325 is closed with one comment; 1327 remains open with zero comments
    and owns non-graph follow-up. The current exact strain row is new evidence resolving
    its older mapping uncertainty. No issue mutation occurred.
  support: supports
  accessed_at: '2026-10-21T21:29:46.282378Z'
  snapshot_sha256: e7362ea760fceb80f510a52407115929299740f7554c439353f1acdf7aff087d
- evidence_id: historical-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/historical-source-byte-comparison.json
  locator: Exact prior source hash versus fresh XML
  summary: Fresh XML equals the prior recorded hash. The unavailable old pathname
    remains historical metadata; no old file is reconstructed and no active hash exception
    is used.
  support: supports
  accessed_at: '2026-10-21T21:29:46.282524Z'
  snapshot_sha256: 5dfb169ca2b7d6e1be49e9142d940a6885173da0d49d4a5ec4038da885999996
- evidence_id: inspect
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/inspect.json
  locator: Fresh official 26-input inspection
  summary: The exact canonical owner and base were inspected before judgments. Ignored-inclusive
    discovery found the focal cache, history and batch 19 decision/adversarial pair;
    no batch 91 transfer from another record.
  support: supports
  accessed_at: '2026-10-21T21:29:46.282647Z'
  snapshot_sha256: 5b705bdc25f47d5f9399cee23029baa244bf37eb4a593e9c95ba2bf8c3e7dc55
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/lead-source-assets.json
  locator: Fresh main and genuine package inventory; four figure reads
  summary: Fresh main is available despite the initial PMC browser captcha. The acquired
    package has four main figures and thumbnails only; zero XML supplementary-material/media
    elements and no separate SI declaration were identified. This bounded inventory
    leaves no current-claim-critical gap, without asserting global absence.
  support: supports
  accessed_at: '2026-10-21T21:29:46.282681Z'
  snapshot_sha256: b8c2b2be30d60fb42f5d12463d6277efec311641db0fa7bb7df72860ac469677
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/lead-primary-read-scope.json
  locator: Whole primary text, equations, table, references and four figures
  summary: Lead read the complete 42,911-character main projection, all 47 references,
    Table 1 and both equations, and viewed all four JPEGs. Source/authority scopes
    and limits are explicit; no numerical reanalysis or exact feed-pulse digitization
    occurred.
  support: supports
  accessed_at: '2026-10-21T21:29:46.282814Z'
  snapshot_sha256: 59d9a0e74b0ccd3e503ac83f359ccfa2d753552e7761b30761cff5ff0d3a8fe6
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/source-audit.json
  locator: Final four finding groups and source completion
  summary: 'Completed scientific assessment: two major findings concern feed/product
    placement and recipient-role/acid-use scope; two minors concern RNA/cDNA endpoint
    wording and recoverable strain-mapping provenance.'
  support: supports
  accessed_at: '2026-10-21T21:29:46.282969Z'
  snapshot_sha256: 3fb5710de9f5daf8e2d89113ef61717d4bcfb3201bd00bfac0c6f7f6b52e045b
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/root-independent-source-audit.json
  locator: Independent whole primary, figure, authority and provenance assessment
  summary: Root independently read the full main, all references, table and equations,
    all four figures, and the exact raw 290402 crosswalk row. Its completed assessment
    agrees with all four groups and the explicit source limits.
  support: supports
  accessed_at: '2026-10-21T21:29:46.283158Z'
  snapshot_sha256: f893d2710bb21c4e41ad1e3321f55c06487779eabca15aecb3720576934453b8
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/support-final-audit.json
  locator: Distinct final support and native arithmetic
  summary: Completeness 95. Three nodes, zero arrows and six node-evidence occurrences
    give mean two. Two major/two minor findings yield raw quality 111, capped 100;
    all 26 inspected inputs remain unchanged.
  support: supports
  accessed_at: '2026-10-21T21:29:46.283193Z'
  snapshot_sha256: 859cf66c830dc0d4b344e128168286af0e8a6147cf9e190fc400f846b4efd01b
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/supporting-artifact-manifest.json
  locator: Final supporting artifacts and hashes
  summary: The manifest binds finalized source-specific resources, excerpts, provenance
    and actual read scopes. Preliminary support remains immutable.
  support: supports
  accessed_at: '2026-10-21T21:29:46.283223Z'
  snapshot_sha256: b6cae3c1a93216f88564cbab6bca0a7fdfa6ec4e0dc8fb5db3681077fcea4bed
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/auxiliary-frozen-manifest.json
  locator: Final native/authority receipts and unchanged inputs
  summary: Eight focused native checks pass, eleven ontology pairs across 21 occurrences
    match, and the exact strain lookup is preserved separately from species mappings.
    No canonical or cache mutation.
  support: supports
  accessed_at: '2026-10-21T21:29:46.283366Z'
  snapshot_sha256: 4490df4aefce39ea372cda6fdf6c9d89662797cefb7dbf37f079edd33a4fc47c
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/final-validator-summary.json
  locator: Actual eight command results and final input integrity
  summary: Schema, strict, terms, references, GTDB, domain, history and cache-name
    checks pass. Initial summary remains unchanged; native success does not prove
    every scientific interpretation.
  support: supports
  accessed_at: '2026-10-21T21:29:46.283518Z'
  snapshot_sha256: 429b150b74ee4fefa9df2834d25dd95e71612ae9e0e110dd778c895fc7c2ae40
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/adapter-check.json
  locator: Batch 11 discovery from 403 at 2026-10-21T19:20:45.556660+00:00; current
    runtime compatibility
  summary: Optional adapter unavailability is scoped to the owned runtime with explicit
    same-batch discovery reuse. The other-checkout runner was not executed; no installation
    or global absence claim occurred.
  support: supports
  accessed_at: '2026-10-21T21:29:46.283648Z'
  snapshot_sha256: 535b73250ebc1a50a6639a988af690b39bfbfacec8a7c895b30751b7ed82ece1
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/validate.json
  locator: Actual focused command and output
  summary: Recorded native result; biological entailment assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:29:46.283849Z'
  snapshot_sha256: 5579eb7ce20ebf3fcbb2dd6a04e6fe298fef6dc9f7cff52124a3d93ed67b932f
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/validate-strict.json
  locator: Actual focused command and output
  summary: Recorded native result; biological entailment assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:29:46.284058Z'
  snapshot_sha256: 3f8a97d3608c82967030dbf206e37d066e16c2bf0b8d80635a499bd2b02737ef
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/validate-terms.json
  locator: Actual focused command and output
  summary: Recorded native result; biological entailment assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:29:46.284236Z'
  snapshot_sha256: b76462d261cc78f61c7e0d72f5661c489a91ff3b5c8392f2433def8bb027cf0d
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/validate-references-explained.json
  locator: Actual focused command and output
  summary: Recorded native result; biological entailment assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:29:46.284386Z'
  snapshot_sha256: 156e79a2f909def2855dbf93e92a15491aaa49a50f7be84dee65346f775ef438
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/validate-gtdb.json
  locator: Actual focused command and output
  summary: Recorded native result; biological entailment assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:29:46.284522Z'
  snapshot_sha256: f038bedf119bf94764aeb673c2f56aec2349f2abb934ee790043deb48fa1c3e1
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/validate-gtdb-domain.json
  locator: Actual focused command and output
  summary: Recorded native result; biological entailment assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:29:46.284685Z'
  snapshot_sha256: 28628259a3e3f3f7b6e33668dab1bd731b7b530295f8e6b1a283d0b625aba6c2
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/validate-history.json
  locator: Actual focused command and output
  summary: Recorded native result; biological entailment assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:29:46.284830Z'
  snapshot_sha256: ad818907d1505933e24c86e3148f20d0e3fe4e41820165968e1f6b8231c65850
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/000323/normalize-cache-names-check.json
  locator: Actual focused command and output
  summary: Recorded native result; biological entailment assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:29:46.284971Z'
  snapshot_sha256: 69e887a8da67fdad30f4b3db6e132eea6adf200f73da0cdc0fd7c1d486315162
- evidence_id: check-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/audit-network.json
  locator: Same-batch corpus diagnostic
  summary: Actual corpus nonzero result retained; no later record is assessed.
  support: supports
  accessed_at: '2026-10-21T21:29:46.285184Z'
  snapshot_sha256: 5c91360a50ff296c596ef7b3fa3ca70cfa3f0423923df3104fa1aafcfcd96b61
- evidence_id: check-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-11/check-network-quality.json
  locator: Same-batch corpus diagnostic
  summary: Actual corpus nonzero result retained; no later record is assessed.
  support: supports
  accessed_at: '2026-10-21T21:29:46.285361Z'
  snapshot_sha256: 5052a95a78eea50710110e7c8d5488631b3eb5df1705369d5ba42b9c3c0ee9f7
assessments:
- assessment_id: identity
  area: identity
  topic: Focal pair, origin and category
  outcome: supported
  summary: The record denotes the intended defined laboratory coculture.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - identity
  - strain
  - schema
  details: Retain ENGINEERED, SYNTHETIC and LIGNOCELLULOSE. Comparator organisms,
    monocultures, stock storage and analytical protocols are not additional community
    members or universal culture conditions.
- assessment_id: taxonomy
  area: grounding
  topic: Species/strain resolution and GTDB provenance
  outcome: concern
  summary: Exact NCIMB 8052 evidence resolves the stored absent-row uncertainty.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - strain
  - gtdb
  - ontology
  details: NCBITaxon:1520 remains a valid species term; exact 290402 supports an optional
    coherent strain descriptor and its own 1.0/two-genome mapping. Preserve 743B 573061
    and its four-genome result. No name-only selection among the species group is
    needed.
- assessment_id: roles
  area: scope
  topic: Functional roles and ordinal abundance
  outcome: concern
  summary: Donor CROSS_FEEDER needs recipient evidence; supported roles and ordinals
    remain.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - supply
  - acid
  - schema
  - semantics
  details: Sugar release and relief of feedback inhibition establish donor function
    and a proposed benefit, not use of a named partner metabolite. Retain recipient
    fermentation/cross-feeding and donor primary degradation. ABUNDANT need not be
    replaced by a fixed numerical percentage.
- assessment_id: sugar-node
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Sugar-provision CROSS_FEEDING remains properly qualified.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - supply
  - culture
  details: Monoculture/coculture profiles support functional provision. Cellulose
    is substrate and ABE compounds are products; their co-listing does not make all
    of them transferred currencies. Inoculation and pH affect performance, so no provision-to-competition
    arrow is restored.
- assessment_id: acid-node
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: The PARTIAL in-situ acid contribution preserves the evidence limit.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - acid
  details: Keep the C. cellulovorans-to-C. beijerinckii interpretation, pH/sugar covariates
    and lack of traced donor-resolved flux or isolated necessity. No butyrate-to-upstream-saccharification
    arrow is supported.
- assessment_id: population-node
  area: graph
  topic: ecological_interactions[2] and discussions[0]
  outcome: supported
  summary: The untyped experimental population/competition node is appropriately bounded.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - population
  details: RNA/cDNA proportions and operating-condition comparisons do not isolate
    molecular competition. Keep the open mechanistic discussion and zero downstream
    arrows; do not promote uncertain QS annotations.
- assessment_id: chemical-claims
  area: consistency
  topic: description and related_ingredients
  outcome: concern
  summary: Non-graph acid-use wording should preserve the graph’s inference.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - acid
  - ontology
  details: Retain source-supported in-situ cosubstrate contribution without asserting
    each molecule is donor-resolved. Cellulose denotes a major AECC component; butanol
    is a product. Butyric-acid naming matches the source and need not be forcibly
    changed to an anion.
- assessment_id: medium
  area: quantity
  topic: growth_media[0] input and endpoint placement
  outcome: concern
  summary: The recorded degraded amount and butanol output are not the initial recipe.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - medium
  - endpoints
  details: Replace composition input 68.6 g/L with the source-specific nominal 70
    g/L initial AECC condition; move butanol out of feed composition. Preserve 68.6
    g/L degradation and 11.8 g/L ABE as optimized endpoints. Do not invent exact supplementation
    pulses.
- assessment_id: cultivation
  area: scope
  topic: Preculture, production and optimization stages
  outcome: concern
  summary: Recoverable full Methods can replace stale abstract-only preparation prose.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - preculture
  - culture
  - pretreatment
  - analysis
  details: Separate TGY/AECC precultures, 5-L/2-L production reactor and 500-mL/400-mL
    optimization flasks, pH-control durations and volumetric inocula. Pretreatment,
    storage, analytical temperature and N2 cooling are distinct stages. No unstated
    flask rpm or maintained gas-feed setpoint is inferred.
- assessment_id: carbon-environment
  area: grounding
  topic: Environment and sole-carbon wording
  outcome: concern
  summary: Laboratory environment is valid; chemical carbon exclusivity is not.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - medium
  - pretreatment
  - ontology
  details: AECC is the authors’ designated feedstock. Sodium acetate, yeast extract,
    tryptone and cysteine remain explicit organic constituents. Preserve author terminology
    with recipe context instead of calling this chemically exclusive or defined carbon
    supply.
- assessment_id: assay
  area: evidence
  topic: engineering_design abundance endpoints
  outcome: concern
  summary: Non-graph endpoint wording should identify the RNA/cDNA 16S proxy.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - population
  - analysis
  details: The graph/discussion already gives the correct limitation. Nine/fourteen-copy
    normalization does not calibrate direct viable-cell counts. Keep the experimental
    evidence mode and stage-specific interpretation.
- assessment_id: process-metal
  area: grounding
  topic: GO processes, CHEBI terms and metal relevance
  outcome: supported
  summary: Terms are correctly labeled and their bounded process/product roles are
    sound.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - ontology
  - schema
  - medium
  details: Cellulose catabolism belongs to the primary degrader; fermentation and
    broad interspecies process do not prove molecular competition. Trace salts do
    not establish a metal-processing purpose; retain NOT_APPLICABLE.
- assessment_id: excerpts
  area: evidence
  topic: Reference identity, excerpts and claim support
  outcome: supported
  summary: All 23 occurrences are source-faithful with distinct identity and scientific
    scopes.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - snippets
  - lead-read
  details: The current short cache is abstract-only. Full Methods evidence can support
    separately authorized enrichment; no cache refresh occurred. Title/PMCID matching
    validates identity, not experimental effects.
- assessment_id: resources
  area: representation
  topic: Publications, supplements and datasets
  outcome: supported
  summary: The two external links identify the same primary paper.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - resources
  - assets
  details: No dataset omission or cross-Mech recipe finding is established. The acquired
    package and XML expose no separate SI; uncertain background Gene IDs do not become
    focal deposits or validated genes.
- assessment_id: provenance
  area: provenance
  topic: Prior review and current ownership
  outcome: supported
  summary: Existing graph repair and open non-graph follow-up remain correctly scoped.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - history
  - historical-source
  - inspect
  details: Issue 1327 owns follow-up while 1325 is closed. New exact strain evidence
    can resolve its prior mapping uncertainty without changing historical receipts.
    The old source path is metadata only; all active inputs and snapshots are verified.
- assessment_id: validation
  area: schema
  topic: Native checks and scientific completion
  outcome: supported
  summary: Eight focused checks pass; current-claim scientific review is completed.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - final-native
  - auxiliary
  - source-scope
  - root-source
  details: Corpus diagnostics retain their actual failures. The separate source audit
    establishes scientific scope; validation alone does not certify biology. Parent
    saves only the new review bundle after independent whole-candidate checks.
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Completeness 95; raw quality 111, capped 100.
  target_ids:
  - CommunityMech:000323
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 95
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields with taxon roles 50 + environment term 5 + at least
      three environmental factors 10 + at least three interaction nodes 10 + external
      resources 5 + growth media 10 + node metabolites 5. Empty associated_datasets
      earns no bonus; presence does not prove source support.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 − 50P1 − 10P2 − 2P3 + 20min(mean node evidence/2,1) + 15
      if COMPLETE,0,100). P1=0, P2=2, P3=2, P4=0. Six node-evidence occurrences/three
      nodes give mean two and bonus 20; COMPLETE adds 15. Raw 111 caps at 100.
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
- finding_id: separate-medium-inputs
  issue_key: cm-000323-separate-medium-inputs
  category: consistency
  severity: major
  native_severity: P2
  normalization_reason: Incorrect inputs and stage placement materially misrepresent
    the experimental medium.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Separate feed recipe from degradation and solvent endpoints
  description: The medium stores 68.6 g/L degraded AECC as an input and butanol as
    a component. Sole-carbon wording omits organic supplements and source-specific
    preparation/fermentation stages. Use nominal initial 70 g/L AECC and the actual
    recipe, keep degradation and ABE concentrations as endpoints, and document source-described
    supplementation without invented feed pulses. Recover stage-specific precultures,
    reactor/flask conditions, pH schedules and volumetric inocula. Qualify author
    sole-carbon wording with acetate and complex supplements.
  target_ids:
  - CommunityMech:000323
  field_paths:
  - growth_media[0].composition
  - growth_media[0].preparation_notes
  - growth_media[0].incubation_time
  - growth_media[0].evidence
  - engineering_design.assembly_strategy
  - environment_term.notes
  - environmental_factors[0].value
  - environmental_factors[0].evidence
  evidence_ids:
  - medium
  - preculture
  - culture
  - endpoints
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_25023325.md
    role: source_cache
  ownership_note: Maintained YAML owns the repair; source cache owns any future exact
    Methods enrichment. Existing issue 1327 covers non-graph follow-up; preserve closed
    1325 graph repair. No issue mutation.
- finding_id: qualify-recipient-role
  issue_key: cm-000323-qualify-recipient-role
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: The optional recipient role and unqualified acid-use direction
    overstate local support, despite an appropriately qualified graph.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Qualify donor recipient-role and acid-use claims
  description: Donor CROSS_FEEDER lacks local recipient evidence, and non-graph acid-use
    wording drops the source-supported inference already preserved by the graph. Identify
    provider, currency and utilization evidence before retaining the optional donor
    recipient role; otherwise omit it. Retain primary degradation, recipient fermentation/cross-feeding
    and inferred acid contribution. Align non-graph wording with qualified graph;
    do not claim transfer is impossible or demand traced flux for all broad exchange.
  target_ids:
  - CommunityMech:000323
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].evidence
  - description
  - taxonomy[1].taxon_term.notes
  - related_ingredients[1].relevance
  - related_ingredients[1].evidence
  evidence_ids:
  - supply
  - acid
  - schema
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns the repair; source cache owns any future exact
    Methods enrichment. Existing issue 1327 covers non-graph follow-up; preserve closed
    1325 graph repair. No issue mutation.
- finding_id: qualify-population-assay
  issue_key: cm-000323-qualify-population-assay
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: The graph already preserves this method limitation; the remaining
    inconsistency is localized endpoint wording.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Describe the RNA/cDNA population proxy consistently
  description: Non-graph 16S gene-qPCR endpoint wording omits RNA extraction and cDNA,
    despite correct graph/discussion caveats. Describe the experimental RNA/cDNA-based
    16S proportion proxy, its nine/fourteen-copy normalization and stage-specific
    interpretation. Do not call it direct cell counts or validate absolute viable-cell
    fractions. Retain ordinal ABUNDANT and experimental evidence mode.
  target_ids:
  - CommunityMech:000323
  field_paths:
  - engineering_design.perturbation_design
  - engineering_design.measurement_endpoints[5]
  evidence_ids:
  - population
  - analysis
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns the repair; source cache owns any future exact
    Methods enrichment. Existing issue 1327 covers non-graph follow-up; preserve closed
    1325 graph repair. No issue mutation.
- finding_id: resolve-strain-mapping
  issue_key: cm-000323-resolve-strain-mapping
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Current identities are valid; exact strain evidence resolves
    a prior provenance uncertainty without changing supported biology.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Resolve exact NCIMB 8052 mapping and snapshot provenance
  description: The stored no-exact-NCIMB8052-row rationale is contradicted by verified
    exact strain 290402; 743B mapping provenance also overstates latest/build information.
    Reconcile WITHHELD using exact strain 290402, unsuffixed GTDB species, 1.0/two
    genomes, with coherent descriptor and ncbi_source_id. Do not substitute broad
    species 1520 counts or a name-only choice. Preserve valid 743B 1.0/four genomes
    and document the verified crosswalk hash and exact-ID routes instead of treating
    mtime as release.
  target_ids:
  - CommunityMech:000323
  field_paths:
  - taxonomy[1].taxon_term.gtdb_grounding_status
  - taxonomy[1].taxon_term.notes
  - taxonomy[1].taxon_term.term
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - strain
  - gtdb
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns the repair; source cache owns any future exact
    Methods enrichment. Existing issue 1327 covers non-graph follow-up; preserve closed
    1325 graph repair. No issue mutation.
actions:
- action_id: correct-feed-and-protocol
  description: Represent source-specific medium inputs and experimental stages.
  finding_ids:
  - separate-medium-inputs
  target_ids:
  - CommunityMech:000323
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_25023325.md
    role: source_cache
  acceptance_checks:
  - At growth_media[0].composition, use nominal initial 70 g/L AECC from Methods and
    remove butanol as an added component. Preserve 68.6 g/L degraded AECC and 8.30
    g/L butanol in endpoint contexts. Record fed-batch AECC supplementation without
    inventing exact feed doses or times from Figure 4A. Do not replace the distinct
    monoculture Results value 67.2 g/L with an assumed identical measurement.
  - 'Recover the per-litre AECC recipe from Strain and medium: NH4Cl 1.5 g, K2HPO4·3H2O
    1 g, KCl 0.5 g, MgSO4·7H2O 0.5 g, sodium acetate 1.65 g, yeast extract 0.5 g,
    tryptone 0.5 g, L-cysteine HCl 0.5 g, resazurin 0.001 g, trace-metal stock 20
    mL, p-aminobenzoic acid 100 µg, thiamine 100 µg and biotin 1 µg, initially pH
    7. Keep the unrecovered reference-42 trace-stock formulation explicit. Author
    sole-carbon wording must retain acetate/complex-supplement context in assembly_strategy,
    environment notes and environmental_factors[0].'
  - Separate C. beijerinckii TGY preculture at pH 6.5, static anaerobic 37°C for 12–16
    h from C. cellulovorans AECC preculture at pH 7, static 37°C for 24 h. Preserve
    their actual recipe differences. Do not copy glycerol storage, biomass pretreatment
    or analytical temperatures into fermentation conditions; N2 cooling is preparation
    scope.
  - Represent the 5-L/2-L production reactor at 37°C and 100 rpm separately from 500-mL/400-mL
    optimization flasks. Initial 0.5%/10% v/v inocula and 36-h pH control differ from
    optimized simultaneous 1%/10% v/v and first-24-h pH 7 control followed by uncontrolled
    pH. Keep 5 N NaOH as the control reagent; do not infer flask rpm, nutrient feeding
    from titrant, or cell fractions from volume ratios.
  - Replace obsolete abstract-only preparation prose with precise Methods evidence.
    Keep optimized less-than-80-h abstract timing separate from generic incubation
    and the Conclusion 80-h statement. Future cache enrichment must preserve exact
    source/version and existing cache bytes/history through the authorized workflow.
- action_id: qualify-role-and-acid
  description: Align non-graph interpretation with source-local recipient evidence.
  finding_ids:
  - qualify-recipient-role
  target_ids:
  - CommunityMech:000323
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - For taxonomy[0].functional_role CROSS_FEEDER, identify the partner provider, metabolite
    and utilization evidence before retention; otherwise omit this optional recipient
    role. Sugar donation, improved cellulose degradation and benefit from product
    removal alone do not meet the literal utilization definition. Do not claim reciprocal
    utilization is impossible.
  - Qualify acid contribution consistently in description, taxonomy[1].taxon_term.notes
    and related_ingredients[1].relevance, using monoculture/coculture acid profiles
    and reassimilation as support for an inferred in-situ cosubstrate contribution.
    Preserve the lack of donor-resolved molecular flux and isolated butyrate necessity,
    without requiring such proof for every broad exchange statement.
  - Retain C. cellulovorans PRIMARY_DEGRADER and C. beijerinckii SECONDARY_FERMENTER/CROSS_FEEDER.
    Preserve all three graph nodes, zero arrows and open mechanistic discussion. Do
    not restore acid-to-saccharification or provision-to-competition arrows; do not
    promote uncertain QS Gene IDs.
- action_id: qualify-assay
  description: Make the non-graph abundance endpoint match the actual method.
  finding_ids:
  - qualify-population-assay
  target_ids:
  - CommunityMech:000323
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Update engineering_design.perturbation_design and measurement_endpoints[5] to
    state experimental RNA extraction, cDNA synthesis and species-specific 16S assay
    proportions. Keep the source’s target-copy terminology attributed and the nine/fourteen-copy
    normalization explicit if described.
  - State that this proxy is not direct cell counting or an independent calibration
    of absolute viable-cell fractions. Preserve early/late stage scope, current graph/discussion
    qualification, ordinal ABUNDANT and IN_VITRO evidence. No universal percentage,
    equal biomass or fixed dominance is inferred.
- action_id: resolve-taxonomy
  description: Use exact strain evidence with coherent mapping provenance.
  finding_ids:
  - resolve-strain-mapping
  target_ids:
  - CommunityMech:000323
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Reconcile taxonomy[1].taxon_term WITHHELD and its no-direct-row rationale using
    exact NCBITaxon:290402, Clostridium beijerinckii NCIMB 8052, parent 1520. The
    verified exact row maps to GTDB:s__Clostridium_beijerinckii with majority 1.0
    and two genomes via ncbi_id. If representing this strain classification, keep
    term rank, descriptor and ncbi_source_id coherent; do not attach strain support
    counts to a 1520 species block.
  - Keep broad species 1520 aggregate 0.87/741 distinct from the exact strain evidence
    and its A/E name-group context. Retain valid 743B 573061 mapping to Clostridium_K
    cellulovorans at 1.0/four genomes. Replace latest/build-date assertions with verified
    crosswalk SHA 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd,
    exact-ID route and accurately labeled snapshot date.
  - Keep source designations separate from optional collection aliases. Direct DSMZ
    verifies 743B/DSM 3052/ATCC 35296; ATCC 51743/NCIMB 8052 is only primary indexed-product-sheet
    corroboration because direct opens timed out. Historical deposited-as acetobutylicum
    does not identify ATCC 824. No catalogue medium or newly sequenced genome is inferred.
- action_id: verify-future-curation
  description: Validate separately authorized repairs and preserve the graph.
  finding_ids:
  - separate-medium-inputs
  - qualify-recipient-role
  - qualify-population-assay
  - resolve-strain-mapping
  target_ids:
  - CommunityMech:000323
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Beijerinckii_AECC_ABE_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_25023325.md
    role: source_cache
  acceptance_checks:
  - Attach exact source/section evidence to each changed claim and retain the existing
    graph qualifications and source-specific uncertainties. Coordinate through existing
    1327 without reopening closed 1325 solely because non-graph changes remain.
  - After authorized canonical edits, append required history and run schema, strict,
    terms, references, GTDB, domain and history checks, followed by just gen-html
    and just check-docs-current. Verify changed-input hashes rather than silently
    refreshing them.
  - This review modifies no canonical YAML, cache, history or generated output. Parent
    may save only the new immutable review bundle after independent whole-candidate
    checks. Native completeness/quality scores are not biological validation.
limitations:
- All current claim-critical main sources are assessed. The acquired eight-file package
  contains four main JPEGs and four thumbnails; inspected XML has no separate supplement
  declaration. This bounded inventory is not proof that no other material exists elsewhere.
  The trace-stock formulation cited to reference 42 remains unrecovered.
- No raw data, image digitization, biological experiment, genome analysis or model
  execution was performed. AECC feed pulses are not quantified from Figure 4A. Protein-derived
  biomass, pellet-derived substrate estimates and RNA/cDNA proportions retain their
  analytical assumptions.
- Sugar supply and in-situ acid contribution remain source-supported interpretations.
  Partner-resolved flux, unique butyrate necessity and molecular competition/QS are
  not established. Source author terminology does not erase these limits or impose
  an obligatory/nutrient-only role definition.
- 'All 23 excerpt occurrences strictly match the short cache and fresh reference-specific
  source: 19 abstract, three title and one PMCID metadata. No cache enrichment occurred,
  and metadata/lexical matching is not scientific entailment.'
- Strain 290402 mapping is exact local-crosswalk evidence, not a new genome analysis.
  Species aggregate 1520 counts remain distinct. ATCC alias corroboration uses an
  indexed primary excerpt; direct opens timed out. Crosswalk mtime is not a verified
  release/build date.
- The old source pathname is historical metadata with an independently matching fresh
  XML hash, not an active missing pin. Preliminary support and initial validators
  remain immutable. Adapter discovery is explicitly reused from record 403 with current
  compatibility checks; no external other-checkout runner was invoked.
notes:
- Completed scientific review; two major/two minor findings; completeness 95, raw
  quality 111/capped 100.
- Preserve valid pair identity, ordinals, graph and metal scope; no dataset omission
  finding.
- No canonical edits or save by lead; parent persistence follows whole-candidate checks.
tags:
- record-review
- aecc
- abe-fermentation
- batch-11
```
