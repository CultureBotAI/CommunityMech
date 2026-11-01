# Chlorochromatium consortium source and semantic review

- Review: 20261021T191221Z-chlorochromatium-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T19:02:07.760498Z
- Finished UTC: 2026-10-21T19:12:21.890371Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Both full cited sources and critical supplementary figures support a completed current-claim review. One major chemical-grounding correction and two minor cultivation/mechanism-provenance follow-ups remain. Retain the natural consortium, broad partner roles and three-node/two-arrow topology with explicit hypotheses; successful native checks do not resolve the source’s quinone inconsistencies or demonstrate transfer.

## Scope And Provenance

Whole maintained record assessed against both full scientific mains, primary and critical supplementary figures, bounded gene tables, current authorities and exact provenance.

Selection: Only released CommunityMech:000141 in the owned batch 10 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95812d3412d5aab41fd03422340cf736ac7b56f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000141 | kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml | maintained | Chlorochromatium aggregatum Phototrophic Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000141 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000141 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000141 | All encoded ID-label validation passed; chemical semantic fit was reviewed separately. |
| validate-gtdb | passed | True | CommunityMech:000141 | GTDB status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000141 | Both bacterial GTDB domain contexts passed. |
| validate-history | passed | True | CommunityMech:000141 | The existing history sidecar passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000141 | Read-only cache filename check passed. |
| validate-references-explained | passed | True | CommunityMech:000141 | Native references passed against unchanged source caches; direct source support and interpretation were reviewed separately. |
| audit-network | failed | True | CommunityMech:000141 | Batch 10 corpus diagnostic preserves its actual broader nonzero result; the focal graph separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000141 | Batch 10 corpus diagnostic preserves its actual broader nonzero result; the focal graph separately reports COMPLETE. |
| Current-claim scientific source assessment | passed | True | CommunityMech:000141 | Both full scientific mains, main figures and critical supplementary figures assessed. Remaining gene-table inventory is explicitly bounded and supplies no unverified current numerical claim. |
| Primary and supplementary figure assessment | passed | True | CommunityMech:000141 | Lead viewed six 2013 main figures, all seven 1998 pages/eight figures and all four SI figure pages. The S4/main conflict is preserved. |
| Fresh source-specific excerpt verification | passed | True | CommunityMech:000141 | All 22 occurrences strictly match fresh sources and unchanged caches, with abstract/body overlap explicitly counted. |
| Semantic and resource authority verification | passed | True | CommunityMech:000141 | Exact chemical candidate, taxon/GTDB ranks and encoded genome identities verified. Semantic mismatch remains a curation finding despite successful labels. |
| Exhaustive supplementary gene inventory reanalysis | skipped | False | CommunityMech:000141 | Selected orthology/cofactor/signaling rows and all 13 HGT pairs were read; all 30 pages and underlying sequences were not reanalyzed. |
| Raw-data or mechanistic reproduction | skipped | False | CommunityMech:000141 | No genome assembly, chromatogram integration, flux analysis, model execution or biological experiment performed. |
| Optional structured source adapter | unavailable | False | CommunityMech:000141 | Verified runtime discovery preserves unavailable status; expression-module analysis is not applicable to the encoded genomic/physiology claims. |

## Scientific And Domain Assessments

### Community membership, origin and taxonomy

identity: supported. Targets: CommunityMech:000141.

Retain the natural freshwater central-bacterium/epibiont consortium and supported NCBI identities.

Approximately 15 epibionts per central cell is structural stoichiometry. Culture enrichment can contain other organisms without adding them as defined consortium members. Both exact encoded genome identities are supported. The curated CaD3 genus fallback remains deliberate; no forced GTDB species promotion follows from a separate rank row.

### ecological_state, community_origin, community_category and environment

identity: concern. Targets: CommunityMech:000141.

NATURAL, freshwater environment and broad SYNTROPHY category are supported; qualify the scope of STABLE.

Organization, synchronous division and persistence through transfers describe a stable association in the ordinary structural sense. They do not independently measure demographic equilibrium. Explain this limit or omit the optional equilibrium-bearing state. Anoxic laboratory cultivation is distinct from all microenvironments or every possible central-bacterium oxygen response.

### All taxon roles and their evidence explanations

evidence: concern. Targets: CommunityMech:000141.

Retain the broad producer, syntrophic-partner and central cross-feeder roles with explicit inferential scope.

CaD3 phototrophy/carbon fixation supports PRIMARY_PRODUCER. Genomic capacity, axenic excretion and comparative physiology support the proposed central recipient role. Neither axenic epibiont growth nor failed central isolation establishes mutual obligacy. Replace the unqualified obligate-dependence explanation with the source-specific observation and inference; no narrow thermodynamic condition is imposed on broad roles.

### ecological_interactions[0] and its downstream arrow

graph: concern. Targets: CommunityMech:000141.

Retain the hypothetical nutrient-provision node and arrow, but review its optional interaction type.

The node identifies proposed C/N/cofactor transfer from epibiont to central bacterium; it does not encode the required product-removal mechanism. Omit interaction_type: SYNTROPHY unless claim-specific evidence supplies that relation. Preserve photosynthesis as the epibiont process, external 2-oxoglutarate dependence and the hypothetical quinone-supply arrow; do not add a new metabolic edge or treat inorganic inputs as transferred products.

### ecological_interactions[1] and its downstream arrow

graph: supported. Targets: CommunityMech:000141.

Retain partial navigation physiology and the hypothetical resource-access arrow.

The central flagellum, consortium taxis and recombinant photosensor endpoints are supported. Sensor necessity, sulfide sensing and effects on partner-resolved flux remain unisolated. Move the metabolite attractant/resource text out of concentration, and keep generic sulfide versus exact chemical-form interpretation bounded.

### ecological_interactions[2] and its three evidence entries

graph: concern. Targets: CommunityMech:000141.

Retain an explicitly hypothesized quinone energetic-coupling model and add the inspected supplementary conflict.

Bidirectional quinone/quinol cycling would make central electron transport more favourable and return electrons to the epibiont. That source-specific proposed coupling can justify a hypothesis-scoped interaction type, without claiming experimentally established product removal. HPLC presence and gene inventories do not establish direction, exchange flux or shared PMF. Preserve the exact main quotation while explaining S4 CK-7/MK-7 and caption discrepancies.

### description, environmental factors, related ingredients and discussion

evidence: concern. Targets: CommunityMech:000141.

Apply the existing graph’s qualification to nearby prose and replace the old unseen-supplement boundary.

Central light/sulfide sensing is not universally established, fixed nitrogen transfer is inferred, and source language of probable dependence is not proof of universal obligacy. Issue 1311 already owns the sensory-attribution scope. The discussion should now identify actual S4 and its conflicts while preserving unresolved transfer and sensory-causality questions.

### growth_media[0], environmental_factors[0] and assay stages

completeness: concern. Targets: CommunityMech:000141.

Recover direct 1998 K1 growth conditions and keep preparation/phenotyping separate.

Record source recipe, initial pH, temperature, light, static incubation, inoculum and vessel capacities. Do not transfer 2013 cell-disaggregation or recombinant spectroscopy temperatures. The taxis headspace, substrate concentration and light intensity belong to that assay. No filled volume is inferred from vessel capacity and no exact cross-Mech formulation follows from the K1 name.

### All six related ingredients, node metabolite and photosynthesis GO

grounding: concern. Targets: CommunityMech:000141.

Correct the thiosulfate ester grounding and preserve chemical/assay scope for the other terms.

CHEBI:16094 is the verified inorganic anion candidate. Sulfide donor/attractant roles are supported, but generic sulfide does not quantify H2S versus S(2-) speciation. 2-Oxoglutarate is an external growth substrate and attractant; citrate is an attractant without demonstrated growth support. CO2/N2 fixation capacity belongs to the epibiont, with N transfer inferred. GO photosynthesis does not imply oxygenic photosynthesis by this consortium.

### metal_relevance and metal_notes scope

evidence: not_applicable. Targets: CommunityMech:000141.

No distinct metal-processing community function is encoded.

Trace nutrients, iron-containing electron carriers or cofactors do not alone require a metal relevance finding. This does not assert that metals are absent from the referenced trace solution or biological proteins.

### associated_datasets and source accessibility

provenance: supported. Targets: CommunityMech:000141.

Both encoded genome resources are identity-supported, with current archive status and sample hierarchy to preserve.

CP000108 NCBI suppression and exact ENA metadata coexist. CP004885 CR is finer strain context within the encoded species. Optional SRS500535 traceability must identify an enriched-consortium SRA sample rather than a pure central-cell BioSample. No arbitrary replacement accession, global unavailability, sequence equivalence or missing-dataset conclusion is warranted.

### Caches, history, prior reviews and issue ownership

provenance: supported. Targets: CommunityMech:000141.

Preserve the graph-only repair and deliberate taxonomy history while reusing the existing non-graph issue scope.

The prior row matches current target/cache hashes. Current 1308, 376 and 384 are closed; 1311 remains open. The 1998 cache remains abstract-only even though a full PDF was newly read. New full-main excerpts require separate accurate cache/transcription provenance; no current cache was mutated.

### Native checks and immutable workflow

schema: supported. Targets: CommunityMech:000141.

All eight focused native checks pass; scientific completion is independently assessed.

No canonical, cache, history, generated or earlier review artifact was changed. Initial/final native summaries and preliminary/final support remain distinct. Only a new immutable review bundle may subsequently be persisted.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000141.

Completeness is 85; raw quality 121 caps at 100.

## Findings

### inorganic-thiosulfate-identity: Ground the inorganic thiosulfate attractant to its correct chemical class

major / open / confirmed; issue key: cm-000141-inorganic-thiosulfate-identity.

CHEBI:26977 has the right short label but denotes thiosulfate esters. The source physiological attractant is inorganic thiosulfate; verified CHEBI:16094 thiosulfate(2-) is the appropriate candidate. Successful label validation does not repair the semantic identity mismatch.

### recover-cultivation-stages: Recover K1 cultivation and separate assay stages

minor / open / confirmed; issue key: cm-000141-recover-cultivation-stages.

The generic anaerobic medium omits direct full-source recipe, initial pH, temperature, light, inoculum and vessel details. Add the 1998 growth stage without importing capillary/CTC/spectral assay settings or 2013 disaggregation/spectroscopy conditions.

### qualify-mechanisms-and-source-scope: Align nearby claims and interaction typing with the qualified source model

minor / open / confirmed; issue key: cm-000141-qualify-mechanisms-and-source-scope.

The graph already limits flux and sensory causality, but nearby wording strengthens central sensing, dependence and N provision. Nutrient-node SYNTROPHY lacks its narrow product-removal relation; the quinone node may retain a hypothesis-scoped energetic interpretation. Concentration contains role prose, STABLE needs bounded interpretation, and the now-read S4 and archive statuses should refine source notes.

## Recommended Actions And Acceptance Checks

### correct-inorganic-thiosulfate

Correct the source-grounded thiosulfate chemical identity.

- Replace related_ingredients[1].chebi_term with verified CHEBI:16094 and canonical label thiosulfate(2-), retaining the physiological attractant evidence. Confirm both ID-label correspondence and definition-level fit; do not invent a counterion or a source-specific reagent salt.
- Keep generic sulfide role statements distinct from measured chemical speciation. Any later choice among H2S, HS(-) or S(2-) must be justified by source context, not inferred solely from the word sulfide. This review does not mandate a guessed replacement.

### recover-k1-protocol

Add source-specific cultivation without conflating experimental stages.

- Represent the 1998 K1 recipe per litre: NaHCO3 4.0 g, KH2PO4 1.0 g, NH4Cl 0.5 g, MgCl2·6H2O 0.4 g, CaCl2·2H2O 0.1 g, vitamin solution 1 mL and SL12 trace solution 1 mL, plus Na2S 300 micromolar. Preserve cited vitamin/trace subrecipe identity without inventing uninspected components or exact cross-Mech equivalence.
- Record initial pH 7.3, successful 5 mM 2-oxoglutarate condition, 5% v/v inoculum, 22 C, static vertical incubation and 20 micromol quanta m−2 s−1. Record 22.5 mL tube/50 mL bottle capacities without asserting fill volumes. Distinguish initial sediment inoculation from routine transfers and source observation intervals from a universal incubation endpoint.
- Keep capillary taxis, spectral response, CTC staining and 2013 K4/disaggregation/DNA preparation separate. Do not transfer assay N2/CO2 headspace, 1 mM capillary substrates, 2 micromol assay light, 68 C disaggregation or 25 C spectroscopy into universal consortium growth conditions. K1 contains NH4Cl; do not label it nitrogen-free.

### qualify-source-mechanisms

Preserve the qualified graph while repairing local evidence and provenance.

- Qualify central light/sulfide sensing, probable dependence and fixed-N provision by their actual evidence. Preserve intact-consortium taxis, recombinant photosensor activity, unidentified sulfide sensors and possible indirect signaling. Reuse open issue 1311 for its matching focal concern; do not reopen closed graph/taxonomy issues merely because new source details are available.
- Omit ecological_interactions[0].interaction_type: SYNTROPHY unless claim-specific evidence supports partner-product removal making metabolism favourable. Retain its hypothetical nutrient-provision description and existing arrows. Node 2 may retain SYNTROPHY only as the explicitly proposed bidirectional quinone/quinol energetic-coupling model; no measured removal, flux, shared PMF or obligacy follows. Broad category and functional roles remain source-qualified.
- Move ecological_interactions[1].metabolites[0].concentration role prose to a description or notes with appropriate scope. Retain the actual approximate 15 epibionts per central cell. Explain STABLE as observed structural persistence with no measured equilibrium, or omit the optional state if that distinction cannot be represented.
- Preserve the exact historical main quotation, but attach inspected S4 context: CK-7 and MK-7 both identified; main cites S3 and says only MK-7; caption/legend disagree about carotenoid peak 4. Update discussion to state actual inspected scope. Keep central-fraction purity and flux limits; do not turn source discrepancies into invented biological results.
- If enriching dataset provenance, retain CP000108 NCBI suppressed status and separate ENA metadata availability, CP004885 CR strain scope, and the SRS500535/SAMN02391550/SRR1027750/PRJNA226624 hierarchy. Source calls SRS500535 a Biosample, but it is an SRA sample identifier. Preserve enriched-consortium sequencing, differing read-count/platform metadata and no raw reanalysis. No mandatory new dataset or identity replacement is inferred.

### validate-authorized-curation

Validate separately authorized changes and preserve source/history provenance.

- New 1998 Methods excerpts require exact-source page/section and scan-to-text provenance in the appropriate cache. The current abstract-only cache must not be relabeled full text merely because a PDF was read. Preserve existing quotations and source versions; do not manufacture matching through unrelated source union.
- After authorized canonical changes, append fresh history and run focused schema, strict, term, reference, GTDB/domain and history checks, then just gen-html and just check-docs-current. Preserve earlier reviews and all frozen source receipts. This review performs no canonical/cache/history/generator mutation; any persistence is only a new immutable review bundle.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml; Entire maintained YAML | supports | The natural freshwater consortium comprises CaD3 epibionts and a central Candidatus Symbiobacter mobilis bacterium. Current content includes three qualified nodes, two hypothetical arrows, two genome resources, six related ingredients and a generic anaerobic growth medium. |
| identity | PMID:24267588; doi:10.1186/gb-2013-14-11-r127; Background; Results and discussion: The two genomes of “Chlorochromatium aggregatum”; Figure 1 | supports | The organized consortium contains approximately 15 attached green sulfur epibionts per central motile bacterium. The epibiont can grow axenically; central independent growth has not been obtained. Genome loss and transport potential support inferred dependence, without proving that independent growth is impossible under every condition. Structural stoichiometry is source-supported, not an inferred community-wide percentage. |
| metabolism | PMID:24267588; doi:10.1186/gb-2013-14-11-r127; Results and discussion: Metabolism and metabolic coupling; Figure 4 | supports | Genome reconstruction and prior physiology motivate sugar, amino-acid and cofactor provision to the central heterotroph. Axenic epibiont excretion and central transporters are not direct intact-consortium transfer measurements. External 2-oxoglutarate utilization by the central partner is inferred from comparative physiology and a transporter. The proposed acetate return is likewise an inference. Neither one-way nutrient provision nor mutually beneficial exchange by itself establishes the narrower product-removal interaction definition. |
| sensing | PMID:24267588; doi:10.1186/gb-2013-14-11-r127; Results and discussion: Chemotaxis, phototaxis, and signal transduction; Materials and methods: Expression and characterization of bacteriophytochrome; Figure 5 | supports | Recombinant Cenrod_2641 activity was characterized in E. coli, with the adjacent heme oxygenase participating in chromophore production. This is direct protein-function evidence, not a loss-of-function test in intact consortia. The central flagellum and whole-consortium taxis are supported, while sulfide sensors and indirect signaling remain unresolved. Figure 5E locus wording differs from Methods; no erroneous locus assignment is imported. |
| quinone-model | PMID:24267588; doi:10.1186/gb-2013-14-11-r127; Results and discussion: Potential interspecies electron transfer; Figures 4 and 6 | supports | The authors propose transfer of MK-7 or an intermediate and bidirectional quinone/quinol cycling: central electron transport would become more favourable, and returned electrons could support epibiont CO2 fixation. This supplies a source-specific hypothetical energetic-coupling interpretation, not measured product removal, electron flux, shared protonmotive force or obligatory dependence. |
| quinone-main | PMID:24267588; doi:10.1186/gb-2013-14-11-r127; Results and discussion: Potential interspecies electron transfer; Materials and methods: HPLC analyses of quinones | supports | Main text reports MK-7 detection in intact consortia and central-bacterium-enriched fractions, with no ubiquinone detected. Enrichment is not purification. The main-only-MK-7 wording and S3 citation conflict with actual supplementary S4, which also identifies chlorobiumquinone. Preserve the exact old quotation while qualifying its interpretation with the inspected supplement. |
| quinone-si | PMID:24267588; doi:10.1186/gb-2013-14-11-r127; Additional file 1, Supplemental Figure S4, panels A–C and caption | supports | The black trace is intact-consortium extract; the gray trace is an E. coli standard mixture. S4 identifies CK-7 at peak 1 and MK-7 at peak 4, and excludes the stated UQ/MK forms in the inspected elution interval. Its caption also lists peak 4 among carotenoids before identifying MK-7, whereas the plotted legend uses peaks 2,3,5–7 for carotenoids. No separate enriched-fraction chromatogram or transfer experiment is shown. S3 is the photosensor phylogeny. |
| gene-tables | PMID:24267588; doi:10.1186/gb-2013-14-11-r127; Additional file 2: Table S2 orthology definition and selected quinone/cofactor rows; Table S3 definition and terminal signaling rows; entire Table S4 | supports | Selected missing-gene examples include ubiquinone-pathway and cofactor annotations; these are comparisons with reference-genome orthologs, not experimentally measured metabolite absence. All 13 S4 candidate HGT pairs were read. The remaining 30-page inventory was not exhaustively audited, and no new gene-count, locus-absence or phylogenetic conclusion is added. |
| preparation | PMID:24267588; doi:10.1186/gb-2013-14-11-r127; Materials and methods: Culture and DNA preparation; Sequencing and assembly; Expression and characterization of bacteriophytochrome | supports | K4 resuspension without H2S/NaHCO3, 68 C disaggregation and DNA fractionation are preparation stages; 25 C spectroscopy is a measurement condition. They must not become consortium growth parameters. The enriched sequencing material contained epibiont and other-organism reads, subsequently filtered during assembly. |
| k1 | PMID:9446684; doi:10.1007/s002030050552; Materials and methods: Culture media and growth conditions, page 130 | supports | K1 provides per litre NaHCO3 4.0 g, KH2PO4 1.0 g, NH4Cl 0.5 g, MgCl2·6H2O 0.4 g, CaCl2·2H2O 0.1 g, referenced vitamin solution 1 mL and SL12 trace solution 1 mL; Na2S is 300 micromolar. Initial pH is 7.3. Organic-carbon screening used 5 mM, and the successful 2-oxoglutarate condition used 5% v/v inoculum, vertical static 22 C incubation and 20 micromol quanta m−2 s−1. Airtight 22.5 mL tubes or 50 mL bottles are capacities, not reported fill volumes. Vitamin/trace subrecipes remain referenced rather than independently reconstructed. |
| growth | PMID:9446684; doi:10.1007/s002030050552; Materials and methods: Source of organisms; Results: Enrichment and growth characteristics; Figures 2–4; Discussion | supports | Sediment and overlaying water came from Lake Dagow in August 1996; initial enrichment used 2 mL sediment suspension per 50 mL medium. Intact-consortium growth required light and 2-oxoglutarate in the tested conditions, and persisted through repeated transfers. A 12:12 light/dark comparison is not a universally required photoperiod. Persistent structured association supports a bounded stability description, not a measured population-equilibrium claim. |
| taxis | PMID:9446684; doi:10.1007/s002030050552; Materials and methods: Chemotaxis assays; Results: Chemotaxis; Figure 5 | supports | The capillary assay uses 100 mL Meplats bottles with 20 mL suspension, N2/CO2 80:20 headspace, 5 microlitre capillaries containing 1 mM substrate, and one hour at 22 C in 2 micromol quanta m−2 s−1 light. Sulfide, thiosulfate, 2-oxoglutarate and citrate attract the consortium; citrate attraction does not establish citrate-supported growth. These assay concentrations and headspace are not universal growth-medium settings. |
| scototaxis | PMID:9446684; doi:10.1007/s002030050552; Materials and methods: Scotophobic response and bacteriospectrogram; Reduction of CTC; Figures 6–8 | supports | Microscopic light-response assays and CTC redox staining establish their respective whole-consortium phenotypes. Their sealed microchambers, spectral illumination, sulfide-free wash and redox incubation are separate from cultivation. The 1998 epibiont-signaling interpretation and 2013 central photosensor proposal remain distinguishable; neither establishes the necessary intact-consortium sensor or an interspecies flux. |
| ontology | ontology-authority.json; Eleven distinct ID-label pairs across 17 occurrences | supports | Encoded labels match OAK, including both taxa, freshwater environment, photosynthesis and seven chemical identities. Label success does not resolve semantic fit: thiosulfate is the wrong chemical class despite a matching literal label. |
| chemical | child-thiosulfate-grounding-candidate.json; CHEBI:26977 and CHEBI:16094 exact labels, definitions and metadata | supports | CHEBI:26977 thiosulfate denotes an ester of thiosulfuric acid. CHEBI:16094 thiosulfate(2-) denotes the inorganic dianion and is the verified candidate for this physiological attractant. No reagent counterion or directly measured speciation is inferred. |
| schema | child-schema-authority.json; FunctionalRoleEnum, CommunityCategoryEnum, InteractionTypeEnum.SYNTROPHY, EcologicalStateEnum and concentration slots | supports | Broad syntrophic roles/category differ from the interaction type requiring partner-product removal to make metabolism favourable. Obligacy is explicitly not asserted. STABLE includes equilibrium; metabolite concentration means measured concentration or amount. |
| gtdb | child-gtdb-crosswalk.json; Exact-ID rows 340177 and 1436290; separate name-matching rows 337090 and 946483 | supports | The exact CaD3 row supplies Chlorobium genus with blank species and one genome at fraction 1.0, supporting the curated genus fallback. The separate species row does not force promotion. The central species row reproduces Symbiobacter mobilis with one genome/fraction 1.0. Distinct-rank counts are not combined; file mtime is not a verified GTDB release. |
| lineage | child-taxon-lineage-authority.json; Current encoded NCBI labels and parent lineages | supports | CaD3 is the epibiont strain under its species, while central NCBITaxon:1436290 is species-level. Current labels are correct; a finer CR archive strain can be documented without silently replacing the maintained taxon. |
| semantics | ontology-semantic-notes.json; Whole-record auxiliary semantic interpretation | supports | Retain broad producer/partner/recipient roles with source qualification. Central sensing, dependence and N provision need the same boundaries as the graph. Generic sulfide language does not measure H2S versus S(2-) speciation, and resource prose is not a metabolite concentration. |
| resources | dataset-verification.json; Direct NCBI/ENA metadata for CP004885, CP000108 and source-named SRS500535 | supports | Both GENOMICS resources have exact source identity. CP000108 is suppressed in current NCBI metadata but resolves in exact ENA metadata, so it is not globally unavailable. CP004885 names central strain CR. SRS500535 is an SRA sample linked to SAMN02391550, SRR1027750 and PRJNA226624 in an enriched-consortium sequencing context, not purified central cells. Source/archive count and platform differences remain attributed; no raw reads or sequence equivalence were assessed. |
| source-metadata | source-metadata-audit.json; Exact two PMIDs, DOIs and titles | supports | Both cited publications are verified. Directly retrieved full 1998 PDF is scientifically assessable despite no PMC/Open Access flag in the metadata; access is judged from the actual artifact. |
| snippets | snippet-audit.json; All 22 canonical excerpt occurrences, reference-specific matching | supports | All 22 strictly match fresh sources and unchanged caches: 15 cite 2013 and seven cite 1998. Fourteen have abstract matches and ten have body matches, with two overlapping occurrences. These are 22 excerpt occurrences, not 24, and matching does not independently certify each explanation. |
| history | provenance-audit.json; Sole history, exact focal batch 15 row and fresh issues 1308, 1311, 376, 384 | supports | The current target and both cache hashes match the prior review. Closed 1308 records the qualified graph repair; open 1311 owns the focal non-graph sensory-attribution follow-up. Closed 376/384 explain deliberate CaD3 genus fallback. Historical unread-main/SI scope remains history; newly read sources can refine current prose. Other records in shared issues were not assessed. |
| inspect | inspect.json; Fresh official inspection and exact 26 inputs | supports | One maintained MicrobialCommunity target in the owned batch 10 checkout was inspected before assessment. All 26 input bytes remain unchanged. |
| metrics | support-final-audit.json; Final native arithmetic and source-specific support | supports | Completeness 85; three nodes/two arrows/seven node-evidence occurrences, mean 7/3 and COMPLETE. One major/two minor findings give raw quality 121, capped at 100. Mechanical scores do not certify unresolved flux or source errata. |
| support-manifest | supporting-artifact-manifest.json; Frozen final supporting artifacts | supports | Final support uses a distinct file and preserves preliminary support unchanged. All provenance, resource and lexical checks retain their original bytes and scopes. |
| lead-read | lead-primary-read-scope.json; Exact lead scientific and visual read scope | supports | Lead read both full scientific mains, all six 2013 main figures, all seven 1998 pages/eight figures, all four supplementary figure pages and selected gene-table scope. Lead did not read the entire 2013 cache or all 30 pages of supplementary gene inventory; sibling cache reading and bounded table reading are separately stated. |
| source-scope | source-audit.json; Final lead assessment and three actionable groups | supports | Completed scientific review of current claims, one major/two minor findings, preserves qualified topology and identifies chemical grounding, missing protocol details and mechanism/source qualification follow-up. |
| root-source | root-independent-source-audit.json; Independent root scientific assessment | supports | Root independently assessed both main sources, figures and supplementary evidence at its recorded scope and agreed the chemical correction and two bounded follow-up groups. |
| root-read | root-primary-read.json; Exact independent root reading and immutable source pins | supports | Root scope is recorded independently; no uninspected table inventory, raw sequence, chromatography or mechanistic reproduction is implied. |
| auxiliary | auxiliary-frozen-manifest.json; Frozen native/OAK/schema/GTDB/chemical authorities | supports | All eight focused native checks passed. Eleven ontology pairs match across 17 occurrences; semantic fit remains a separate scientific question. |
| final-native | final-validator-summary.json; Separate final native metadata | supports | Initial native summary is immutable. Separate final metadata records the same eight executions and unchanged inputs. |
| adapter | adapter-check.json; Verified runtime discovery and source applicability | supports | The optional structured adapter is unavailable in the verified runtime. Genomic model discussion is not an expression-module experiment; no external-checkout executable or paid source was invoked. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml; Actual execution 2026-10-21T19:02:46.275297+00:00 to 2026-10-21T19:02:46.950077+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-strict kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml --out /private/tmp/cm-review-session/batch-10/000141/strict-report.tsv; Actual execution 2026-10-21T19:02:46.275458+00:00 to 2026-10-21T19:02:48.175594+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-terms kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml; Actual execution 2026-10-21T19:02:46.275547+00:00 to 2026-10-21T19:02:47.879321+00:00 | supports | All encoded ID-label validation passed; chemical semantic fit was reviewed separately. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-gtdb kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml; Actual execution 2026-10-21T19:02:46.950326+00:00 to 2026-10-21T19:02:47.025038+00:00 | supports | GTDB status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-gtdb-domain kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml; Actual execution 2026-10-21T19:02:47.025268+00:00 to 2026-10-21T19:02:48.211615+00:00 | supports | Both bacterial GTDB domain contexts passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-history history/records/Chlorochromatium_Aggregatum_Phototrophic_Consortium; Actual execution 2026-10-21T19:02:47.879610+00:00 to 2026-10-21T19:02:48.482215+00:00 | supports | The existing history sidecar passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T19:02:48.482766+00:00 to 2026-10-21T19:02:48.527090+00:00 | supports | Read-only cache filename check passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-references-explained kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml; Actual execution 2026-10-21T19:02:48.527340+00:00 to 2026-10-21T19:02:50.479776+00:00 | supports | Native references passed against unchanged source caches; direct source support and interpretation were reviewed separately. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T17:04:17.819938+00:00 to 2026-10-21T17:04:25.370848+00:00 | supports | Batch 10 corpus diagnostic preserves its actual broader nonzero result; the focal graph separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T17:04:17.819995+00:00 to 2026-10-21T17:04:26.163649+00:00 | supports | Batch 10 corpus diagnostic preserves its actual broader nonzero result; the focal graph separately reports COMPLETE. |

## Limits And Additional Notes

- Completion covers all currently encoded claims, not exhaustive gene-table validation or experimentally established exchange. Both full scientific mains and critical figures were assessed. Additional file 2 was read only at the explicit selected-row scope; no new quantitative conclusion relies on unread inventory.
- Genome reconstruction, axenic excretion, transporters and enriched-fraction chemistry do not directly trace partner-specific C/N/cofactor or quinone transfer. Recombinant photosensor function does not demonstrate intact-consortium necessity; sulfide sensory mechanism remains unresolved.
- S4 identifies CK-7 and MK-7 and conflicts with main-only-MK-7 wording/S3 citation. The caption also inconsistently labels peak 4. Preserve attributed source text, actual figure scope and the absence of a separate enriched-fraction chromatogram. No chromatography or phylogeny was reanalyzed.
- K1 growth, initial sediment enrichment, capillary taxis, spectral/CTC assays and 2013 cell preparation are different stages. Vessel capacities are not fill volumes; initial pH is not a controlled time course. Referenced vitamin/SL12 subrecipes were not independently reconstructed. No exact CultureMech identity is inferred.
- Current CaD3 genus grounding is supported by its exact-row blank species column. A different NCBI species row is not a strain classification mandate, and mapping file mtime is not a verified release. No genome sequence or taxonomic reassignment was performed.
- NCBI CP000108 suppression and exact ENA metadata availability coexist. The source-named SRA sample contains enriched-consortium sequencing, not a pure central-cell culture. Manuscript/archive count and platform descriptions remain unresolved at their respective scopes; no raw reads or payload identity were verified.
- Twenty-two distinct excerpt occurrences match fresh reference-specific sources and caches. Abstract/body support overlaps for two occurrences. Native reference success and eleven correct ID-label pairs do not establish semantic fit or validate every explanation. Lead cache reading was narrower than sibling whole-cache reading.
- Persistent association is not an independently measured equilibrium; broad syntrophic roles do not impose obligacy, while interaction typing has its narrower product-removal meaning. These distinctions and the existing unresolved graph hypotheses remain explicit.
- Eight focused checks passed; broader same-batch corpus checks retain their actual nonzero results. Completeness 85 and quality 100/raw 121 are mechanical rubric outputs. No paid request, external contact, raw-data reproduction, canonical/cache/history/generated edit or later-record assessment occurred.
- All 26 official inputs remain unchanged. No canonical/cache/history/generated or earlier saved artifact was edited.
- Lead/root scientific reading, child authority/native scope and sibling lexical/resource scope remain separately documented. Final support has a distinct immutable filename.
- One major and two minor findings; completeness 85, quality 100/raw 121. Current-claim completion does not certify unresolved transfer or all supplementary gene annotations.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T191221Z-chlorochromatium-record
kind: record
repository: CultureBotAI/CommunityMech
title: Chlorochromatium consortium source and semantic review
started_at: '2026-10-21T19:02:07.760498Z'
finished_at: '2026-10-21T19:12:21.890371Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, auxiliary authorities
    and supporting provenance; no person-level independence is asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Both full cited sources and critical supplementary figures support a completed
  current-claim review. One major chemical-grounding correction and two minor cultivation/mechanism-provenance
  follow-ups remain. Retain the natural consortium, broad partner roles and three-node/two-arrow
  topology with explicit hypotheses; successful native checks do not resolve the source’s
  quinone inconsistencies or demonstrate transfer.
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
  - path: history/records/Chlorochromatium_Aggregatum_Phototrophic_Consortium/2026-10-05T215546Z-codex-2d267a.yaml
    sha256: fa9513e2a5d1ea7c96cada20cf1a3a7db995807b3b287efff967fa660583e8a5
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    sha256: 9869c805629d42d823727e6e21363628909725dadd532b3759d2238a7f5ef48d
    role: target
  - path: references_cache/PMID_24267588.txt
    sha256: 0b5e47fe0921ead0f46516888805b8a67c17c251d8e78eb21c2c8f483886cf3f
    role: context
  - path: references_cache/PMID_9446684.md
    sha256: d412a775b873f1d2e8e98ef405f2e6c98323483937ecc97b3b3622ee5cabd34d
    role: context
  - path: reports/causal_graph_review/decisions/20261005-three-records-batch15.yaml
    sha256: 9a91951bf6002151122053f4d0ad0c13ada0c7b4f61bff989a612268c9750dc0
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
- target_id: CommunityMech:000141
  path: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  label: Chlorochromatium aggregatum Phototrophic Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    role: canonical_record
scope:
  description: Whole maintained record assessed against both full scientific mains,
    primary and critical supplementary figures, bounded gene tables, current authorities
    and exact provenance.
  selection: Only released CommunityMech:000141 in the owned batch 10 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000141
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000141
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused native execution in the owned batch 10 checkout; scientific
    and semantic judgments are separate.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000141
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-strict kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-10/000141/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused native execution in the owned batch 10 checkout; scientific
    and semantic judgments are separate.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: All encoded ID-label validation passed; chemical semantic fit was reviewed
    separately.
  target_ids:
  - CommunityMech:000141
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-terms kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused native execution in the owned batch 10 checkout; scientific
    and semantic judgments are separate.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB status validation passed.
  target_ids:
  - CommunityMech:000141
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused native execution in the owned batch 10 checkout; scientific
    and semantic judgments are separate.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Both bacterial GTDB domain contexts passed.
  target_ids:
  - CommunityMech:000141
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb-domain kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused native execution in the owned batch 10 checkout; scientific
    and semantic judgments are separate.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: The existing history sidecar passed.
  target_ids:
  - CommunityMech:000141
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-history history/records/Chlorochromatium_Aggregatum_Phototrophic_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused native execution in the owned batch 10 checkout; scientific
    and semantic judgments are separate.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache filename check passed.
  target_ids:
  - CommunityMech:000141
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused native execution in the owned batch 10 checkout; scientific
    and semantic judgments are separate.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Native references passed against unchanged source caches; direct source
    support and interpretation were reviewed separately.
  target_ids:
  - CommunityMech:000141
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-references-explained kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused native execution in the owned batch 10 checkout; scientific
    and semantic judgments are separate.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Batch 10 corpus diagnostic preserves its actual broader nonzero result;
    the focal graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000141
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - metrics
  scope_note: Explicit same-batch corpus reuse; unrelated nonzero corpus findings
    are not new focal defects.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Batch 10 corpus diagnostic preserves its actual broader nonzero result;
    the focal graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000141
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - metrics
  scope_note: Explicit same-batch corpus reuse; unrelated nonzero corpus findings
    are not new focal defects.
- check_id: scientific-source
  name: Current-claim scientific source assessment
  status: passed
  required: true
  summary: Both full scientific mains, main figures and critical supplementary figures
    assessed. Remaining gene-table inventory is explicitly bounded and supplies no
    unverified current numerical claim.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - lead-read
  - root-source
  - source-scope
- check_id: source-figures
  name: Primary and supplementary figure assessment
  status: passed
  required: true
  summary: Lead viewed six 2013 main figures, all seven 1998 pages/eight figures and
    all four SI figure pages. The S4/main conflict is preserved.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - lead-read
  - quinone-si
  - root-read
- check_id: direct-snippets
  name: Fresh source-specific excerpt verification
  status: passed
  required: true
  summary: All 22 occurrences strictly match fresh sources and unchanged caches, with
    abstract/body overlap explicitly counted.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - snippets
- check_id: authorities
  name: Semantic and resource authority verification
  status: passed
  required: true
  summary: Exact chemical candidate, taxon/GTDB ranks and encoded genome identities
    verified. Semantic mismatch remains a curation finding despite successful labels.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - chemical
  - gtdb
  - lineage
  - resources
- check_id: full-gene-inventory
  name: Exhaustive supplementary gene inventory reanalysis
  status: skipped
  required: false
  summary: Selected orthology/cofactor/signaling rows and all 13 HGT pairs were read;
    all 30 pages and underlying sequences were not reanalyzed.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - gene-tables
  - lead-read
- check_id: experimental-reproduction
  name: Raw-data or mechanistic reproduction
  status: skipped
  required: false
  summary: No genome assembly, chromatogram integration, flux analysis, model execution
    or biological experiment performed.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - lead-read
  - resources
- check_id: adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Verified runtime discovery preserves unavailable status; expression-module
    analysis is not applicable to the encoded genomic/physiology claims.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  locator: Entire maintained YAML
  summary: The natural freshwater consortium comprises CaD3 epibionts and a central
    Candidatus Symbiobacter mobilis bacterium. Current content includes three qualified
    nodes, two hypothetical arrows, two genome resources, six related ingredients
    and a generic anaerobic growth medium.
  support: supports
  accessed_at: '2026-10-21T19:12:21.882435Z'
- evidence_id: identity
  kind: primary_source
  reference: PMID:24267588; doi:10.1186/gb-2013-14-11-r127
  locator: 'Background; Results and discussion: The two genomes of “Chlorochromatium
    aggregatum”; Figure 1'
  summary: The organized consortium contains approximately 15 attached green sulfur
    epibionts per central motile bacterium. The epibiont can grow axenically; central
    independent growth has not been obtained. Genome loss and transport potential
    support inferred dependence, without proving that independent growth is impossible
    under every condition. Structural stoichiometry is source-supported, not an inferred
    community-wide percentage.
  support: supports
  accessed_at: '2026-10-21T19:12:21.882501Z'
  snapshot_sha256: 7e2b832c29f67f0c5c66d5732b18e11d2de20c4dd62c8b792769fda4852596e2
- evidence_id: metabolism
  kind: primary_source
  reference: PMID:24267588; doi:10.1186/gb-2013-14-11-r127
  locator: 'Results and discussion: Metabolism and metabolic coupling; Figure 4'
  summary: Genome reconstruction and prior physiology motivate sugar, amino-acid and
    cofactor provision to the central heterotroph. Axenic epibiont excretion and central
    transporters are not direct intact-consortium transfer measurements. External
    2-oxoglutarate utilization by the central partner is inferred from comparative
    physiology and a transporter. The proposed acetate return is likewise an inference.
    Neither one-way nutrient provision nor mutually beneficial exchange by itself
    establishes the narrower product-removal interaction definition.
  support: supports
  accessed_at: '2026-10-21T19:12:21.882600Z'
  snapshot_sha256: 7e2b832c29f67f0c5c66d5732b18e11d2de20c4dd62c8b792769fda4852596e2
- evidence_id: sensing
  kind: primary_source
  reference: PMID:24267588; doi:10.1186/gb-2013-14-11-r127
  locator: 'Results and discussion: Chemotaxis, phototaxis, and signal transduction;
    Materials and methods: Expression and characterization of bacteriophytochrome;
    Figure 5'
  summary: Recombinant Cenrod_2641 activity was characterized in E. coli, with the
    adjacent heme oxygenase participating in chromophore production. This is direct
    protein-function evidence, not a loss-of-function test in intact consortia. The
    central flagellum and whole-consortium taxis are supported, while sulfide sensors
    and indirect signaling remain unresolved. Figure 5E locus wording differs from
    Methods; no erroneous locus assignment is imported.
  support: supports
  accessed_at: '2026-10-21T19:12:21.882676Z'
  snapshot_sha256: 7e2b832c29f67f0c5c66d5732b18e11d2de20c4dd62c8b792769fda4852596e2
- evidence_id: quinone-model
  kind: primary_source
  reference: PMID:24267588; doi:10.1186/gb-2013-14-11-r127
  locator: 'Results and discussion: Potential interspecies electron transfer; Figures
    4 and 6'
  summary: 'The authors propose transfer of MK-7 or an intermediate and bidirectional
    quinone/quinol cycling: central electron transport would become more favourable,
    and returned electrons could support epibiont CO2 fixation. This supplies a source-specific
    hypothetical energetic-coupling interpretation, not measured product removal,
    electron flux, shared protonmotive force or obligatory dependence.'
  support: supports
  accessed_at: '2026-10-21T19:12:21.882751Z'
  snapshot_sha256: 7e2b832c29f67f0c5c66d5732b18e11d2de20c4dd62c8b792769fda4852596e2
  quote: tested experimentally
- evidence_id: quinone-main
  kind: primary_source
  reference: PMID:24267588; doi:10.1186/gb-2013-14-11-r127
  locator: 'Results and discussion: Potential interspecies electron transfer; Materials
    and methods: HPLC analyses of quinones'
  summary: Main text reports MK-7 detection in intact consortia and central-bacterium-enriched
    fractions, with no ubiquinone detected. Enrichment is not purification. The main-only-MK-7
    wording and S3 citation conflict with actual supplementary S4, which also identifies
    chlorobiumquinone. Preserve the exact old quotation while qualifying its interpretation
    with the inspected supplement.
  support: supports
  accessed_at: '2026-10-21T19:12:21.882827Z'
  snapshot_sha256: 7e2b832c29f67f0c5c66d5732b18e11d2de20c4dd62c8b792769fda4852596e2
- evidence_id: quinone-si
  kind: primary_source
  reference: PMID:24267588; doi:10.1186/gb-2013-14-11-r127
  locator: Additional file 1, Supplemental Figure S4, panels A–C and caption
  summary: The black trace is intact-consortium extract; the gray trace is an E. coli
    standard mixture. S4 identifies CK-7 at peak 1 and MK-7 at peak 4, and excludes
    the stated UQ/MK forms in the inspected elution interval. Its caption also lists
    peak 4 among carotenoids before identifying MK-7, whereas the plotted legend uses
    peaks 2,3,5–7 for carotenoids. No separate enriched-fraction chromatogram or transfer
    experiment is shown. S3 is the photosensor phylogeny.
  support: supports
  accessed_at: '2026-10-21T19:12:21.882904Z'
  snapshot_sha256: 5bc5113b8a881eb25fbe53faad332927bf5516647d35d70b6672c3037f6e6e74
- evidence_id: gene-tables
  kind: primary_source
  reference: PMID:24267588; doi:10.1186/gb-2013-14-11-r127
  locator: 'Additional file 2: Table S2 orthology definition and selected quinone/cofactor
    rows; Table S3 definition and terminal signaling rows; entire Table S4'
  summary: Selected missing-gene examples include ubiquinone-pathway and cofactor
    annotations; these are comparisons with reference-genome orthologs, not experimentally
    measured metabolite absence. All 13 S4 candidate HGT pairs were read. The remaining
    30-page inventory was not exhaustively audited, and no new gene-count, locus-absence
    or phylogenetic conclusion is added.
  support: supports
  accessed_at: '2026-10-21T19:12:21.884609Z'
  snapshot_sha256: 75e494f270e49e24414bd1a37f65c926cc795b817dcdbb2953a64688a26b2462
- evidence_id: preparation
  kind: primary_source
  reference: PMID:24267588; doi:10.1186/gb-2013-14-11-r127
  locator: 'Materials and methods: Culture and DNA preparation; Sequencing and assembly;
    Expression and characterization of bacteriophytochrome'
  summary: K4 resuspension without H2S/NaHCO3, 68 C disaggregation and DNA fractionation
    are preparation stages; 25 C spectroscopy is a measurement condition. They must
    not become consortium growth parameters. The enriched sequencing material contained
    epibiont and other-organism reads, subsequently filtered during assembly.
  support: supports
  accessed_at: '2026-10-21T19:12:21.884960Z'
  snapshot_sha256: 7e2b832c29f67f0c5c66d5732b18e11d2de20c4dd62c8b792769fda4852596e2
- evidence_id: k1
  kind: primary_source
  reference: PMID:9446684; doi:10.1007/s002030050552
  locator: 'Materials and methods: Culture media and growth conditions, page 130'
  summary: K1 provides per litre NaHCO3 4.0 g, KH2PO4 1.0 g, NH4Cl 0.5 g, MgCl2·6H2O
    0.4 g, CaCl2·2H2O 0.1 g, referenced vitamin solution 1 mL and SL12 trace solution
    1 mL; Na2S is 300 micromolar. Initial pH is 7.3. Organic-carbon screening used
    5 mM, and the successful 2-oxoglutarate condition used 5% v/v inoculum, vertical
    static 22 C incubation and 20 micromol quanta m−2 s−1. Airtight 22.5 mL tubes
    or 50 mL bottles are capacities, not reported fill volumes. Vitamin/trace subrecipes
    remain referenced rather than independently reconstructed.
  support: supports
  accessed_at: '2026-10-21T19:12:21.885044Z'
  snapshot_sha256: 4cd448013eee848b3b8cf900b37ce57d681c8639adceadd6f9994781496ecccc
  quote: without shaking
- evidence_id: growth
  kind: primary_source
  reference: PMID:9446684; doi:10.1007/s002030050552
  locator: 'Materials and methods: Source of organisms; Results: Enrichment and growth
    characteristics; Figures 2–4; Discussion'
  summary: Sediment and overlaying water came from Lake Dagow in August 1996; initial
    enrichment used 2 mL sediment suspension per 50 mL medium. Intact-consortium growth
    required light and 2-oxoglutarate in the tested conditions, and persisted through
    repeated transfers. A 12:12 light/dark comparison is not a universally required
    photoperiod. Persistent structured association supports a bounded stability description,
    not a measured population-equilibrium claim.
  support: supports
  accessed_at: '2026-10-21T19:12:21.885594Z'
  snapshot_sha256: 4cd448013eee848b3b8cf900b37ce57d681c8639adceadd6f9994781496ecccc
- evidence_id: taxis
  kind: primary_source
  reference: PMID:9446684; doi:10.1007/s002030050552
  locator: 'Materials and methods: Chemotaxis assays; Results: Chemotaxis; Figure
    5'
  summary: The capillary assay uses 100 mL Meplats bottles with 20 mL suspension,
    N2/CO2 80:20 headspace, 5 microlitre capillaries containing 1 mM substrate, and
    one hour at 22 C in 2 micromol quanta m−2 s−1 light. Sulfide, thiosulfate, 2-oxoglutarate
    and citrate attract the consortium; citrate attraction does not establish citrate-supported
    growth. These assay concentrations and headspace are not universal growth-medium
    settings.
  support: supports
  accessed_at: '2026-10-21T19:12:21.885884Z'
  snapshot_sha256: 4cd448013eee848b3b8cf900b37ce57d681c8639adceadd6f9994781496ecccc
- evidence_id: scototaxis
  kind: primary_source
  reference: PMID:9446684; doi:10.1007/s002030050552
  locator: 'Materials and methods: Scotophobic response and bacteriospectrogram; Reduction
    of CTC; Figures 6–8'
  summary: Microscopic light-response assays and CTC redox staining establish their
    respective whole-consortium phenotypes. Their sealed microchambers, spectral illumination,
    sulfide-free wash and redox incubation are separate from cultivation. The 1998
    epibiont-signaling interpretation and 2013 central photosensor proposal remain
    distinguishable; neither establishes the necessary intact-consortium sensor or
    an interspecies flux.
  support: supports
  accessed_at: '2026-10-21T19:12:21.886145Z'
  snapshot_sha256: 4cd448013eee848b3b8cf900b37ce57d681c8639adceadd6f9994781496ecccc
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Eleven distinct ID-label pairs across 17 occurrences
  summary: 'Encoded labels match OAK, including both taxa, freshwater environment,
    photosynthesis and seven chemical identities. Label success does not resolve semantic
    fit: thiosulfate is the wrong chemical class despite a matching literal label.'
  support: supports
  accessed_at: '2026-10-21T19:12:21.886401Z'
  snapshot_sha256: 2fcf7eb57cffa2aa1532b6003729df769e1126e53066309ab63b6ff07fa56e98
- evidence_id: chemical
  kind: authority
  reference: child-thiosulfate-grounding-candidate.json
  locator: CHEBI:26977 and CHEBI:16094 exact labels, definitions and metadata
  summary: CHEBI:26977 thiosulfate denotes an ester of thiosulfuric acid. CHEBI:16094
    thiosulfate(2-) denotes the inorganic dianion and is the verified candidate for
    this physiological attractant. No reagent counterion or directly measured speciation
    is inferred.
  support: supports
  accessed_at: '2026-10-21T19:12:21.886622Z'
  snapshot_sha256: 7e70901f9da5b7e7e020cb953a2fce423df2cd766e3c6dda2bf79b99337e81e4
- evidence_id: schema
  kind: authority
  reference: child-schema-authority.json
  locator: FunctionalRoleEnum, CommunityCategoryEnum, InteractionTypeEnum.SYNTROPHY,
    EcologicalStateEnum and concentration slots
  summary: Broad syntrophic roles/category differ from the interaction type requiring
    partner-product removal to make metabolism favourable. Obligacy is explicitly
    not asserted. STABLE includes equilibrium; metabolite concentration means measured
    concentration or amount.
  support: supports
  accessed_at: '2026-10-21T19:12:21.886735Z'
  snapshot_sha256: 14441d7293263dcf4743d70890d94b1d7dacddd3da26608e7335f8959be6c8a0
- evidence_id: gtdb
  kind: authority
  reference: child-gtdb-crosswalk.json
  locator: Exact-ID rows 340177 and 1436290; separate name-matching rows 337090 and
    946483
  summary: The exact CaD3 row supplies Chlorobium genus with blank species and one
    genome at fraction 1.0, supporting the curated genus fallback. The separate species
    row does not force promotion. The central species row reproduces Symbiobacter
    mobilis with one genome/fraction 1.0. Distinct-rank counts are not combined; file
    mtime is not a verified GTDB release.
  support: supports
  accessed_at: '2026-10-21T19:12:21.886849Z'
  snapshot_sha256: 1b8db1d44672a7e871359f941f62af6e3295902dd54bb9f37ef2218a99860eaa
- evidence_id: lineage
  kind: authority
  reference: child-taxon-lineage-authority.json
  locator: Current encoded NCBI labels and parent lineages
  summary: CaD3 is the epibiont strain under its species, while central NCBITaxon:1436290
    is species-level. Current labels are correct; a finer CR archive strain can be
    documented without silently replacing the maintained taxon.
  support: supports
  accessed_at: '2026-10-21T19:12:21.886978Z'
  snapshot_sha256: df093c3b14d3a09c7683fee94a3dc60afc142d3956cb10684f3cec4b9df674fc
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole-record auxiliary semantic interpretation
  summary: Retain broad producer/partner/recipient roles with source qualification.
    Central sensing, dependence and N provision need the same boundaries as the graph.
    Generic sulfide language does not measure H2S versus S(2-) speciation, and resource
    prose is not a metabolite concentration.
  support: supports
  accessed_at: '2026-10-21T19:12:21.887049Z'
  snapshot_sha256: ce0232d9c8526487c0aa1764500ee8a7cca933b8a4d8c556aac6f19a8fda6cbc
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Direct NCBI/ENA metadata for CP004885, CP000108 and source-named SRS500535
  summary: Both GENOMICS resources have exact source identity. CP000108 is suppressed
    in current NCBI metadata but resolves in exact ENA metadata, so it is not globally
    unavailable. CP004885 names central strain CR. SRS500535 is an SRA sample linked
    to SAMN02391550, SRR1027750 and PRJNA226624 in an enriched-consortium sequencing
    context, not purified central cells. Source/archive count and platform differences
    remain attributed; no raw reads or sequence equivalence were assessed.
  support: supports
  accessed_at: '2026-10-21T19:12:21.887175Z'
  snapshot_sha256: f2bc023452a702df2d6243c67a9f946f4a4b8fdc4b070002dcd7af485885094f
- evidence_id: source-metadata
  kind: database
  reference: source-metadata-audit.json
  locator: Exact two PMIDs, DOIs and titles
  summary: Both cited publications are verified. Directly retrieved full 1998 PDF
    is scientifically assessable despite no PMC/Open Access flag in the metadata;
    access is judged from the actual artifact.
  support: supports
  accessed_at: '2026-10-21T19:12:21.887294Z'
  snapshot_sha256: 805a3ca05b6b5c11073b8f99534592bba1bd0d766473234fb49eaf56d39d0de4
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: All 22 canonical excerpt occurrences, reference-specific matching
  summary: 'All 22 strictly match fresh sources and unchanged caches: 15 cite 2013
    and seven cite 1998. Fourteen have abstract matches and ten have body matches,
    with two overlapping occurrences. These are 22 excerpt occurrences, not 24, and
    matching does not independently certify each explanation.'
  support: supports
  accessed_at: '2026-10-21T19:12:21.887422Z'
  snapshot_sha256: 9363779b87a81b656a800be81916b75f9344ddea553975805d75c0b596ab2d2f
- evidence_id: history
  kind: prior_review
  reference: provenance-audit.json
  locator: Sole history, exact focal batch 15 row and fresh issues 1308, 1311, 376,
    384
  summary: The current target and both cache hashes match the prior review. Closed
    1308 records the qualified graph repair; open 1311 owns the focal non-graph sensory-attribution
    follow-up. Closed 376/384 explain deliberate CaD3 genus fallback. Historical unread-main/SI
    scope remains history; newly read sources can refine current prose. Other records
    in shared issues were not assessed.
  support: supports
  accessed_at: '2026-10-21T19:12:21.887558Z'
  snapshot_sha256: 8fc17e38b9320cd106f0034238302bb8cb185344dde0bdf6e925bd513392bcc9
- evidence_id: inspect
  kind: validation
  reference: inspect.json
  locator: Fresh official inspection and exact 26 inputs
  summary: One maintained MicrobialCommunity target in the owned batch 10 checkout
    was inspected before assessment. All 26 input bytes remain unchanged.
  support: supports
  accessed_at: '2026-10-21T19:12:21.887695Z'
  snapshot_sha256: 1bf758c2f8862fc9276d7a1da73e30208e224f2ba02dde6e7eb16316c5811895
- evidence_id: metrics
  kind: validation
  reference: support-final-audit.json
  locator: Final native arithmetic and source-specific support
  summary: Completeness 85; three nodes/two arrows/seven node-evidence occurrences,
    mean 7/3 and COMPLETE. One major/two minor findings give raw quality 121, capped
    at 100. Mechanical scores do not certify unresolved flux or source errata.
  support: supports
  accessed_at: '2026-10-21T19:12:21.887719Z'
  snapshot_sha256: 9432a7ec1bfb8d6a0307073734b4425688afe5afef26b8a760d6a1f35812fb7c
- evidence_id: support-manifest
  kind: validation
  reference: supporting-artifact-manifest.json
  locator: Frozen final supporting artifacts
  summary: Final support uses a distinct file and preserves preliminary support unchanged.
    All provenance, resource and lexical checks retain their original bytes and scopes.
  support: supports
  accessed_at: '2026-10-21T19:12:21.887744Z'
  snapshot_sha256: 309b9dfee8cbfe2ce34eb7609a782621a2c1f88cc2f9d778bcad86049a9156f3
- evidence_id: lead-read
  kind: validation
  reference: lead-primary-read-scope.json
  locator: Exact lead scientific and visual read scope
  summary: Lead read both full scientific mains, all six 2013 main figures, all seven
    1998 pages/eight figures, all four supplementary figure pages and selected gene-table
    scope. Lead did not read the entire 2013 cache or all 30 pages of supplementary
    gene inventory; sibling cache reading and bounded table reading are separately
    stated.
  support: supports
  accessed_at: '2026-10-21T19:12:21.887862Z'
  snapshot_sha256: 2485030353739be34f7abec34cea5496088904816db42d82018f69fb1bd4573f
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Final lead assessment and three actionable groups
  summary: Completed scientific review of current claims, one major/two minor findings,
    preserves qualified topology and identifies chemical grounding, missing protocol
    details and mechanism/source qualification follow-up.
  support: supports
  accessed_at: '2026-10-21T19:12:21.887983Z'
  snapshot_sha256: e81945e8da64be21b6e9e07e92f602b08cbf366d40aeaf3d0b21138b4b5f8ca0
- evidence_id: root-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Independent root scientific assessment
  summary: Root independently assessed both main sources, figures and supplementary
    evidence at its recorded scope and agreed the chemical correction and two bounded
    follow-up groups.
  support: supports
  accessed_at: '2026-10-21T19:12:21.888102Z'
  snapshot_sha256: 5f135cfbe97ffbdf8b3f77969d3e4745005e9b054f1e3b3824a53f119adad067
- evidence_id: root-read
  kind: validation
  reference: root-primary-read.json
  locator: Exact independent root reading and immutable source pins
  summary: Root scope is recorded independently; no uninspected table inventory, raw
    sequence, chromatography or mechanistic reproduction is implied.
  support: supports
  accessed_at: '2026-10-21T19:12:21.888129Z'
  snapshot_sha256: 269140fb019d0a78122d6524195d3603c6632c0d8b4e0d20bd93d5c83f61f089
- evidence_id: auxiliary
  kind: validation
  reference: auxiliary-frozen-manifest.json
  locator: Frozen native/OAK/schema/GTDB/chemical authorities
  summary: All eight focused native checks passed. Eleven ontology pairs match across
    17 occurrences; semantic fit remains a separate scientific question.
  support: supports
  accessed_at: '2026-10-21T19:12:21.888260Z'
  snapshot_sha256: a973f7219baa1820e059167b571edfa4e434f8c23bbe03e570f3b6074e58dd30
- evidence_id: final-native
  kind: validation
  reference: final-validator-summary.json
  locator: Separate final native metadata
  summary: Initial native summary is immutable. Separate final metadata records the
    same eight executions and unchanged inputs.
  support: supports
  accessed_at: '2026-10-21T19:12:21.888359Z'
  snapshot_sha256: 7b2a91a3e4272b7075832cf93a5776c131860646dd0a887b44eed2443cd8af8b
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Verified runtime discovery and source applicability
  summary: The optional structured adapter is unavailable in the verified runtime.
    Genomic model discussion is not an expression-module experiment; no external-checkout
    executable or paid source was invoked.
  support: supports
  accessed_at: '2026-10-21T19:12:21.888457Z'
  snapshot_sha256: 2da6103459715a3c28b27bebdb0659d2a0f0f08fde8195f374643b69694d30a6
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  locator: Actual execution 2026-10-21T19:02:46.275297+00:00 to 2026-10-21T19:02:46.950077+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T19:02:46.950077Z'
  snapshot_sha256: 08772bd832a1332a28eceb7101d1f89ff143eb2c4e526ffcc68d93e9bfd25192
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-strict kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-10/000141/strict-report.tsv
  locator: Actual execution 2026-10-21T19:02:46.275458+00:00 to 2026-10-21T19:02:48.175594+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T19:02:48.175594Z'
  snapshot_sha256: b11e1fc49acc1c29645132042b784f9c652de67855328bd8aabacb8fd8c2bd89
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-terms kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  locator: Actual execution 2026-10-21T19:02:46.275547+00:00 to 2026-10-21T19:02:47.879321+00:00
  summary: All encoded ID-label validation passed; chemical semantic fit was reviewed
    separately.
  support: supports
  accessed_at: '2026-10-21T19:02:47.879321Z'
  snapshot_sha256: 8d0dbdd872c0a49225e0b091a48293ff335d7bf0f3bcd962e48fae313242cd57
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  locator: Actual execution 2026-10-21T19:02:46.950326+00:00 to 2026-10-21T19:02:47.025038+00:00
  summary: GTDB status validation passed.
  support: supports
  accessed_at: '2026-10-21T19:02:47.025038Z'
  snapshot_sha256: 33510f2110674861a44329e488eedbc5d98eaa45bf216a55161e2e126c4afbed
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb-domain kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  locator: Actual execution 2026-10-21T19:02:47.025268+00:00 to 2026-10-21T19:02:48.211615+00:00
  summary: Both bacterial GTDB domain contexts passed.
  support: supports
  accessed_at: '2026-10-21T19:02:48.211615Z'
  snapshot_sha256: 57268d951cc224ed5fae3f0cf9729c767834412e7bda3660526a5fa420e6a6e5
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-history history/records/Chlorochromatium_Aggregatum_Phototrophic_Consortium
  locator: Actual execution 2026-10-21T19:02:47.879610+00:00 to 2026-10-21T19:02:48.482215+00:00
  summary: The existing history sidecar passed.
  support: supports
  accessed_at: '2026-10-21T19:02:48.482215Z'
  snapshot_sha256: c4f10e995243dcb176f495659b14251c29116e03b9f9682fd6646c13a918b074
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T19:02:48.482766+00:00 to 2026-10-21T19:02:48.527090+00:00
  summary: Read-only cache filename check passed.
  support: supports
  accessed_at: '2026-10-21T19:02:48.527090Z'
  snapshot_sha256: a764ee1030d3cc38c87b7922f36ffc0cd0cb580aa3fa5e1882f1680fe10317c8
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-references-explained kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
  locator: Actual execution 2026-10-21T19:02:48.527340+00:00 to 2026-10-21T19:02:50.479776+00:00
  summary: Native references passed against unchanged source caches; direct source
    support and interpretation were reviewed separately.
  support: supports
  accessed_at: '2026-10-21T19:02:50.479776Z'
  snapshot_sha256: 6ba17fadc65448d78a12838a08eb9680cffc2286090b976f536537d8e0138f91
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T17:04:17.819938+00:00 to 2026-10-21T17:04:25.370848+00:00
  summary: Batch 10 corpus diagnostic preserves its actual broader nonzero result;
    the focal graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T17:04:25.370848Z'
  snapshot_sha256: 301cbda477198c0cff0f38601fdb49af8d805cafa7da106733150d64786d987d
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T17:04:17.819995+00:00 to 2026-10-21T17:04:26.163649+00:00
  summary: Batch 10 corpus diagnostic preserves its actual broader nonzero result;
    the focal graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T17:04:26.163649Z'
  snapshot_sha256: f8dae0e292e8e2f8c221450aacc2bb120abe0e3f32c16ed59f8406e8b859a895
assessments:
- assessment_id: identity
  area: identity
  topic: Community membership, origin and taxonomy
  outcome: supported
  summary: Retain the natural freshwater central-bacterium/epibiont consortium and
    supported NCBI identities.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - identity
  - lineage
  - gtdb
  - growth
  details: Approximately 15 epibionts per central cell is structural stoichiometry.
    Culture enrichment can contain other organisms without adding them as defined
    consortium members. Both exact encoded genome identities are supported. The curated
    CaD3 genus fallback remains deliberate; no forced GTDB species promotion follows
    from a separate rank row.
- assessment_id: state
  area: identity
  topic: ecological_state, community_origin, community_category and environment
  outcome: concern
  summary: NATURAL, freshwater environment and broad SYNTROPHY category are supported;
    qualify the scope of STABLE.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - identity
  - growth
  - schema
  details: Organization, synchronous division and persistence through transfers describe
    a stable association in the ordinary structural sense. They do not independently
    measure demographic equilibrium. Explain this limit or omit the optional equilibrium-bearing
    state. Anoxic laboratory cultivation is distinct from all microenvironments or
    every possible central-bacterium oxygen response.
- assessment_id: roles
  area: evidence
  topic: All taxon roles and their evidence explanations
  outcome: concern
  summary: Retain the broad producer, syntrophic-partner and central cross-feeder
    roles with explicit inferential scope.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - identity
  - metabolism
  - schema
  - semantics
  details: CaD3 phototrophy/carbon fixation supports PRIMARY_PRODUCER. Genomic capacity,
    axenic excretion and comparative physiology support the proposed central recipient
    role. Neither axenic epibiont growth nor failed central isolation establishes
    mutual obligacy. Replace the unqualified obligate-dependence explanation with
    the source-specific observation and inference; no narrow thermodynamic condition
    is imposed on broad roles.
- assessment_id: nutrition-node
  area: graph
  topic: ecological_interactions[0] and its downstream arrow
  outcome: concern
  summary: Retain the hypothetical nutrient-provision node and arrow, but review its
    optional interaction type.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - metabolism
  - quinone-model
  - schema
  details: 'The node identifies proposed C/N/cofactor transfer from epibiont to central
    bacterium; it does not encode the required product-removal mechanism. Omit interaction_type:
    SYNTROPHY unless claim-specific evidence supplies that relation. Preserve photosynthesis
    as the epibiont process, external 2-oxoglutarate dependence and the hypothetical
    quinone-supply arrow; do not add a new metabolic edge or treat inorganic inputs
    as transferred products.'
- assessment_id: navigation-node
  area: graph
  topic: ecological_interactions[1] and its downstream arrow
  outcome: supported
  summary: Retain partial navigation physiology and the hypothetical resource-access
    arrow.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - sensing
  - taxis
  - scototaxis
  details: The central flagellum, consortium taxis and recombinant photosensor endpoints
    are supported. Sensor necessity, sulfide sensing and effects on partner-resolved
    flux remain unisolated. Move the metabolite attractant/resource text out of concentration,
    and keep generic sulfide versus exact chemical-form interpretation bounded.
- assessment_id: quinone-node
  area: graph
  topic: ecological_interactions[2] and its three evidence entries
  outcome: concern
  summary: Retain an explicitly hypothesized quinone energetic-coupling model and
    add the inspected supplementary conflict.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - quinone-model
  - quinone-main
  - quinone-si
  - gene-tables
  details: Bidirectional quinone/quinol cycling would make central electron transport
    more favourable and return electrons to the epibiont. That source-specific proposed
    coupling can justify a hypothesis-scoped interaction type, without claiming experimentally
    established product removal. HPLC presence and gene inventories do not establish
    direction, exchange flux or shared PMF. Preserve the exact main quotation while
    explaining S4 CK-7/MK-7 and caption discrepancies.
- assessment_id: overview
  area: evidence
  topic: description, environmental factors, related ingredients and discussion
  outcome: concern
  summary: Apply the existing graph’s qualification to nearby prose and replace the
    old unseen-supplement boundary.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - sensing
  - metabolism
  - quinone-si
  - history
  details: Central light/sulfide sensing is not universally established, fixed nitrogen
    transfer is inferred, and source language of probable dependence is not proof
    of universal obligacy. Issue 1311 already owns the sensory-attribution scope.
    The discussion should now identify actual S4 and its conflicts while preserving
    unresolved transfer and sensory-causality questions.
- assessment_id: cultivation
  area: completeness
  topic: growth_media[0], environmental_factors[0] and assay stages
  outcome: concern
  summary: Recover direct 1998 K1 growth conditions and keep preparation/phenotyping
    separate.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - k1
  - growth
  - taxis
  - scototaxis
  - preparation
  details: Record source recipe, initial pH, temperature, light, static incubation,
    inoculum and vessel capacities. Do not transfer 2013 cell-disaggregation or recombinant
    spectroscopy temperatures. The taxis headspace, substrate concentration and light
    intensity belong to that assay. No filled volume is inferred from vessel capacity
    and no exact cross-Mech formulation follows from the K1 name.
  dimensions:
  - name: culture-context
    value: K1; 22 C; initial pH 7.3; 5 mM 2-oxoglutarate; 5% v/v inoculum; 20 micromol
      quanta m−2 s−1; static
    definition: Direct 1998 growth stage; vitamin/trace subrecipes remain referenced
      and vessel capacities are not fill volumes.
    evidence_ids:
    - k1
- assessment_id: chemistry
  area: grounding
  topic: All six related ingredients, node metabolite and photosynthesis GO
  outcome: concern
  summary: Correct the thiosulfate ester grounding and preserve chemical/assay scope
    for the other terms.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - chemical
  - ontology
  - semantics
  - k1
  - taxis
  - metabolism
  details: CHEBI:16094 is the verified inorganic anion candidate. Sulfide donor/attractant
    roles are supported, but generic sulfide does not quantify H2S versus S(2-) speciation.
    2-Oxoglutarate is an external growth substrate and attractant; citrate is an attractant
    without demonstrated growth support. CO2/N2 fixation capacity belongs to the epibiont,
    with N transfer inferred. GO photosynthesis does not imply oxygenic photosynthesis
    by this consortium.
- assessment_id: metal
  area: evidence
  topic: metal_relevance and metal_notes scope
  outcome: not_applicable
  summary: No distinct metal-processing community function is encoded.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - record
  - k1
  - metabolism
  details: Trace nutrients, iron-containing electron carriers or cofactors do not
    alone require a metal relevance finding. This does not assert that metals are
    absent from the referenced trace solution or biological proteins.
- assessment_id: resources
  area: provenance
  topic: associated_datasets and source accessibility
  outcome: supported
  summary: Both encoded genome resources are identity-supported, with current archive
    status and sample hierarchy to preserve.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - resources
  - source-metadata
  - preparation
  details: CP000108 NCBI suppression and exact ENA metadata coexist. CP004885 CR is
    finer strain context within the encoded species. Optional SRS500535 traceability
    must identify an enriched-consortium SRA sample rather than a pure central-cell
    BioSample. No arbitrary replacement accession, global unavailability, sequence
    equivalence or missing-dataset conclusion is warranted.
- assessment_id: history
  area: provenance
  topic: Caches, history, prior reviews and issue ownership
  outcome: supported
  summary: Preserve the graph-only repair and deliberate taxonomy history while reusing
    the existing non-graph issue scope.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - history
  - snippets
  - lead-read
  details: The prior row matches current target/cache hashes. Current 1308, 376 and
    384 are closed; 1311 remains open. The 1998 cache remains abstract-only even though
    a full PDF was newly read. New full-main excerpts require separate accurate cache/transcription
    provenance; no current cache was mutated.
- assessment_id: validation
  area: schema
  topic: Native checks and immutable workflow
  outcome: supported
  summary: All eight focused native checks pass; scientific completion is independently
    assessed.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - auxiliary
  - final-native
  - inspect
  - snippets
  details: No canonical, cache, history, generated or earlier review artifact was
    changed. Initial/final native summaries and preliminary/final support remain distinct.
    Only a new immutable review bundle may subsequently be persisted.
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Completeness is 85; raw quality 121 caps at 100.
  target_ids:
  - CommunityMech:000141
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields with taxon roles 50 + environment term 5 + at least
      three interaction nodes 10 + growth media 10 + associated datasets 5 + any node
      metabolites 5. No external-resource or three-environmental-factor bonus. Field
      presence is not scientific support.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 − 50P1 − 10P2 − 2P3 + 20min(mean node evidence/2,1) + 15
      if COMPLETE,0,100). P1=0, P2=1, P3=2, P4=0. Seven evidence entries/three nodes
      give mean 7/3 and capped bonus 20; COMPLETE adds 15. Raw 121 caps at 100.
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
- finding_id: inorganic-thiosulfate-identity
  issue_key: cm-000141-inorganic-thiosulfate-identity
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: Wrong ontology grounding changes the chemical entity, meeting
    the major rubric despite valid syntax and label.
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Ground the inorganic thiosulfate attractant to its correct chemical class
  description: CHEBI:26977 has the right short label but denotes thiosulfate esters.
    The source physiological attractant is inorganic thiosulfate; verified CHEBI:16094
    thiosulfate(2-) is the appropriate candidate. Successful label validation does
    not repair the semantic identity mismatch.
  target_ids:
  - CommunityMech:000141
  field_paths:
  - related_ingredients[1].chebi_term
  evidence_ids:
  - chemical
  - taxis
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    role: canonical_record
- finding_id: recover-cultivation-stages
  issue_key: cm-000141-recover-cultivation-stages
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: The existing culture context is correct but materially incomplete;
    this is a bounded source-recovery follow-up.
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Recover K1 cultivation and separate assay stages
  description: The generic anaerobic medium omits direct full-source recipe, initial
    pH, temperature, light, inoculum and vessel details. Add the 1998 growth stage
    without importing capillary/CTC/spectral assay settings or 2013 disaggregation/spectroscopy
    conditions.
  target_ids:
  - CommunityMech:000141
  field_paths:
  - growth_media[0]
  - environmental_factors[0]
  evidence_ids:
  - k1
  - growth
  - taxis
  - scototaxis
  - preparation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    role: canonical_record
- finding_id: qualify-mechanisms-and-source-scope
  issue_key: cm-000141-qualify-mechanisms-and-source-scope
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: Existing topology and principal model are appropriately qualified;
    localized wording, optional typing and provenance need consistent limits, not
    a new graph or role-removal verdict.
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Align nearby claims and interaction typing with the qualified source model
  description: The graph already limits flux and sensory causality, but nearby wording
    strengthens central sensing, dependence and N provision. Nutrient-node SYNTROPHY
    lacks its narrow product-removal relation; the quinone node may retain a hypothesis-scoped
    energetic interpretation. Concentration contains role prose, STABLE needs bounded
    interpretation, and the now-read S4 and archive statuses should refine source
    notes.
  target_ids:
  - CommunityMech:000141
  field_paths:
  - environmental_factors[1].value
  - taxonomy[1].evidence[1].explanation
  - related_ingredients[0].relevance
  - related_ingredients[5].relevance
  - related_ingredients[5].evidence[0].explanation
  - ecological_interactions[0].interaction_type
  - ecological_interactions[2].interaction_type
  - ecological_interactions[1].metabolites[0].concentration
  - ecological_interactions[2].evidence[2].explanation
  - discussions[0].rationale
  - ecological_state
  - associated_datasets
  evidence_ids:
  - sensing
  - metabolism
  - quinone-model
  - quinone-main
  - quinone-si
  - schema
  - resources
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    role: canonical_record
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1311
  ownership_note: Reuse issue 1311 for its directly matching sensory-attribution concern.
    The additional bounded source-placement details are stated here without asserting
    that every detail is already in that issue.
actions:
- action_id: correct-inorganic-thiosulfate
  description: Correct the source-grounded thiosulfate chemical identity.
  finding_ids:
  - inorganic-thiosulfate-identity
  target_ids:
  - CommunityMech:000141
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Replace related_ingredients[1].chebi_term with verified CHEBI:16094 and canonical
    label thiosulfate(2-), retaining the physiological attractant evidence. Confirm
    both ID-label correspondence and definition-level fit; do not invent a counterion
    or a source-specific reagent salt.
  - Keep generic sulfide role statements distinct from measured chemical speciation.
    Any later choice among H2S, HS(-) or S(2-) must be justified by source context,
    not inferred solely from the word sulfide. This review does not mandate a guessed
    replacement.
- action_id: recover-k1-protocol
  description: Add source-specific cultivation without conflating experimental stages.
  finding_ids:
  - recover-cultivation-stages
  target_ids:
  - CommunityMech:000141
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - 'Represent the 1998 K1 recipe per litre: NaHCO3 4.0 g, KH2PO4 1.0 g, NH4Cl 0.5
    g, MgCl2·6H2O 0.4 g, CaCl2·2H2O 0.1 g, vitamin solution 1 mL and SL12 trace solution
    1 mL, plus Na2S 300 micromolar. Preserve cited vitamin/trace subrecipe identity
    without inventing uninspected components or exact cross-Mech equivalence.'
  - Record initial pH 7.3, successful 5 mM 2-oxoglutarate condition, 5% v/v inoculum,
    22 C, static vertical incubation and 20 micromol quanta m−2 s−1. Record 22.5 mL
    tube/50 mL bottle capacities without asserting fill volumes. Distinguish initial
    sediment inoculation from routine transfers and source observation intervals from
    a universal incubation endpoint.
  - Keep capillary taxis, spectral response, CTC staining and 2013 K4/disaggregation/DNA
    preparation separate. Do not transfer assay N2/CO2 headspace, 1 mM capillary substrates,
    2 micromol assay light, 68 C disaggregation or 25 C spectroscopy into universal
    consortium growth conditions. K1 contains NH4Cl; do not label it nitrogen-free.
- action_id: qualify-source-mechanisms
  description: Preserve the qualified graph while repairing local evidence and provenance.
  finding_ids:
  - qualify-mechanisms-and-source-scope
  target_ids:
  - CommunityMech:000141
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Qualify central light/sulfide sensing, probable dependence and fixed-N provision
    by their actual evidence. Preserve intact-consortium taxis, recombinant photosensor
    activity, unidentified sulfide sensors and possible indirect signaling. Reuse
    open issue 1311 for its matching focal concern; do not reopen closed graph/taxonomy
    issues merely because new source details are available.
  - 'Omit ecological_interactions[0].interaction_type: SYNTROPHY unless claim-specific
    evidence supports partner-product removal making metabolism favourable. Retain
    its hypothetical nutrient-provision description and existing arrows. Node 2 may
    retain SYNTROPHY only as the explicitly proposed bidirectional quinone/quinol
    energetic-coupling model; no measured removal, flux, shared PMF or obligacy follows.
    Broad category and functional roles remain source-qualified.'
  - Move ecological_interactions[1].metabolites[0].concentration role prose to a description
    or notes with appropriate scope. Retain the actual approximate 15 epibionts per
    central cell. Explain STABLE as observed structural persistence with no measured
    equilibrium, or omit the optional state if that distinction cannot be represented.
  - 'Preserve the exact historical main quotation, but attach inspected S4 context:
    CK-7 and MK-7 both identified; main cites S3 and says only MK-7; caption/legend
    disagree about carotenoid peak 4. Update discussion to state actual inspected
    scope. Keep central-fraction purity and flux limits; do not turn source discrepancies
    into invented biological results.'
  - If enriching dataset provenance, retain CP000108 NCBI suppressed status and separate
    ENA metadata availability, CP004885 CR strain scope, and the SRS500535/SAMN02391550/SRR1027750/PRJNA226624
    hierarchy. Source calls SRS500535 a Biosample, but it is an SRA sample identifier.
    Preserve enriched-consortium sequencing, differing read-count/platform metadata
    and no raw reanalysis. No mandatory new dataset or identity replacement is inferred.
- action_id: validate-authorized-curation
  description: Validate separately authorized changes and preserve source/history
    provenance.
  finding_ids:
  - inorganic-thiosulfate-identity
  - recover-cultivation-stages
  - qualify-mechanisms-and-source-scope
  target_ids:
  - CommunityMech:000141
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Chlorochromatium_Aggregatum_Phototrophic_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_9446684.md
    role: source_cache
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_24267588.txt
    role: source_cache
  acceptance_checks:
  - New 1998 Methods excerpts require exact-source page/section and scan-to-text provenance
    in the appropriate cache. The current abstract-only cache must not be relabeled
    full text merely because a PDF was read. Preserve existing quotations and source
    versions; do not manufacture matching through unrelated source union.
  - After authorized canonical changes, append fresh history and run focused schema,
    strict, term, reference, GTDB/domain and history checks, then just gen-html and
    just check-docs-current. Preserve earlier reviews and all frozen source receipts.
    This review performs no canonical/cache/history/generator mutation; any persistence
    is only a new immutable review bundle.
limitations:
- Completion covers all currently encoded claims, not exhaustive gene-table validation
  or experimentally established exchange. Both full scientific mains and critical
  figures were assessed. Additional file 2 was read only at the explicit selected-row
  scope; no new quantitative conclusion relies on unread inventory.
- Genome reconstruction, axenic excretion, transporters and enriched-fraction chemistry
  do not directly trace partner-specific C/N/cofactor or quinone transfer. Recombinant
  photosensor function does not demonstrate intact-consortium necessity; sulfide sensory
  mechanism remains unresolved.
- S4 identifies CK-7 and MK-7 and conflicts with main-only-MK-7 wording/S3 citation.
  The caption also inconsistently labels peak 4. Preserve attributed source text,
  actual figure scope and the absence of a separate enriched-fraction chromatogram.
  No chromatography or phylogeny was reanalyzed.
- K1 growth, initial sediment enrichment, capillary taxis, spectral/CTC assays and
  2013 cell preparation are different stages. Vessel capacities are not fill volumes;
  initial pH is not a controlled time course. Referenced vitamin/SL12 subrecipes were
  not independently reconstructed. No exact CultureMech identity is inferred.
- Current CaD3 genus grounding is supported by its exact-row blank species column.
  A different NCBI species row is not a strain classification mandate, and mapping
  file mtime is not a verified release. No genome sequence or taxonomic reassignment
  was performed.
- NCBI CP000108 suppression and exact ENA metadata availability coexist. The source-named
  SRA sample contains enriched-consortium sequencing, not a pure central-cell culture.
  Manuscript/archive count and platform descriptions remain unresolved at their respective
  scopes; no raw reads or payload identity were verified.
- Twenty-two distinct excerpt occurrences match fresh reference-specific sources and
  caches. Abstract/body support overlaps for two occurrences. Native reference success
  and eleven correct ID-label pairs do not establish semantic fit or validate every
  explanation. Lead cache reading was narrower than sibling whole-cache reading.
- Persistent association is not an independently measured equilibrium; broad syntrophic
  roles do not impose obligacy, while interaction typing has its narrower product-removal
  meaning. These distinctions and the existing unresolved graph hypotheses remain
  explicit.
- Eight focused checks passed; broader same-batch corpus checks retain their actual
  nonzero results. Completeness 85 and quality 100/raw 121 are mechanical rubric outputs.
  No paid request, external contact, raw-data reproduction, canonical/cache/history/generated
  edit or later-record assessment occurred.
notes:
- All 26 official inputs remain unchanged. No canonical/cache/history/generated or
  earlier saved artifact was edited.
- Lead/root scientific reading, child authority/native scope and sibling lexical/resource
  scope remain separately documented. Final support has a distinct immutable filename.
- One major and two minor findings; completeness 85, quality 100/raw 121. Current-claim
  completion does not certify unresolved transfer or all supplementary gene annotations.
tags:
- record-review
- phototrophic-consortium
- main-assessed
- critical-supplements-assessed
- batch-10
```
