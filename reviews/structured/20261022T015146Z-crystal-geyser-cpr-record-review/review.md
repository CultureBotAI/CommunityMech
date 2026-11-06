# Crystal Geyser CPR lipid community record review

- Review: 20261022T015146Z-crystal-geyser-cpr-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T01:42:15.058487Z
- Finished UTC: 2026-10-22T01:51:46.564515Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Complete primary and supplementary source review supports retaining three qualified nodes and two HYPOTHESIZED arrows. One major finding groups stronger non-graph role, lipid-origin and pressure-adaptation claims; two minor findings concern unsupported equilibrium state and declared-resource traceability. All eight focused checks pass. Literal completeness 75 and raw quality117.66666666666669/cap100 do not certify a clean biological record.

## Scope And Provenance

Whole maintained record and fresh main including79references,Table1 and five main figures; whole supplementary text,31references,12figures and three printed tables; bounded inspection of both workbooks and current authority/provenance/registry checks.

Selection: Only released CommunityMech:000252 in owned batch13.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e117e3d37c65bfad2e04af53ab34e1325d8d7f98.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000252 | kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml | maintained | Crystal Geyser CO2-Rich Aquifer Autotrophic CPR Lysolipid Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000252 | Actual native exit0. |
| validate-strict | passed | True | CommunityMech:000252 | Actual native exit0. |
| validate-terms | passed | True | CommunityMech:000252 | Actual native exit0. |
| validate-references-explained | passed | True | CommunityMech:000252 | Actual native exit0. |
| validate-gtdb | passed | True | CommunityMech:000252 | Actual native exit0. |
| validate-gtdb-domain | passed | True | CommunityMech:000252 | Actual native exit0. |
| validate-history | passed | True | CommunityMech:000252 | Actual native exit0. |
| normalize-cache-names-check | passed | True | CommunityMech:000252 | Actual native exit0. |
| audit-network corpus context | failed | False | CommunityMech:000252 | Actual corpus exit1;44 warnings and zero errors. |
| check-network-quality corpus context | failed | False | CommunityMech:000252 | Actual corpus exit1;44 warnings and zero errors. |
| Optional structured source adapter | unavailable | False | CommunityMech:000252 | Unavailable in the owned runtime. |

## Scientific And Domain Assessments

### Broad CPR clade and carbon-fixing functional pool

identity: supported. Targets: CommunityMech:000252.

The two descriptors are explicit broad community roles rather than cultured species or resolved partners.

Retain NCBITaxon1783273 Patescibacteria group and the explicitly CO2-fixing bacterial/archaeal pool under131567. Ancestor overlap does not require deletion. Source names such as Gallionella, Sulfurimonas and Altiarchaeum provide context, not a mandatory roster expansion or exact donor assignment. S5 reference-similarity strings do not identify collected culture strains.

### Role, lipid origin and pressure-adaptation certainty

evidence: concern. Targets: CommunityMech:000252.

Several categorical fields are stronger than the measured associations and current qualified graph.

The optional CPR SYNTROPHIC_PARTNER role is not established merely by putative symbiosis or genomic deficits. Preserve the observed pathway deficit while retaining near-complete Nealsonbacteria and unknown biosynthesis alternatives. Lipid donation remains proposed; scavenging degraded biomass and direct-host acquisition are alternatives. Pressure-linked unsaturation is an observational association with a proposed explanation, not an experimentally induced response. The description already qualifies lipid origin and curvature; target its categorical pressure clause rather than falsely calling the entire description unqualified.

### Predominantly Autotrophic Carbon Supply

graph: supported. Targets: CommunityMech:000252.

Retain community-scale predominantly autotrophic carbon supply with fractionation and heterotrophic-reuse limits; it does not identify a lipid donor.

Exact selector ecological_interactions[0]; name Predominantly Autotrophic Carbon Supply; scope COMMUNITY_LEVEL; interaction_type not asserted. Actual taxa: {"source": null, "target": null, "participants": [{"id": "NCBITaxon:131567", "label": "cellular organisms"}]}. Canonical evidence bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "794b912fa0d0f412d5d6cd699a73cf323e3888fed01c34e1c2f718e07d70bdef", "reference": "PMID:32203118", "supports": "SUPPORT", "evidence_source": "IN_VIVO"}]. Snippet audit SHA256 963eb2cc02c63aad6b827bd23b6ded0ca89b72e859cfa2a4785e77967550af80. PMID32203118 source locator: Results and discussion → In situ carbon fixation sustains microbial communities irrespective of aquifer depth, paragraphs1–3, Figure 2a–b; Model of lipid transfer in the community and conclusions, paragraph 1. Retain actual evidence tiers: SUPPORT IN_VIVO. Retain community-scale predominantly autotrophic carbon supply with fractionation and heterotrophic-reuse limits; it does not identify a lipid donor.

### Predominantly Autotrophic Carbon Supply → Putative CPR Lipid Acquisition

graph: supported. Targets: CommunityMech:000252.

Retain the existing HYPOTHESIZED direction and its uncertainty.

Exact selector ecological_interactions[0].downstream[0]; actual direction/participants: {"source_node": "Predominantly Autotrophic Carbon Supply", "target_node": "Putative CPR Lipid Acquisition", "source_scope": "COMMUNITY_LEVEL", "target_scope": "COMMUNITY_LEVEL", "source_taxa": {"source": null, "target": null, "participants": [{"id": "NCBITaxon:131567", "label": "cellular organisms"}]}, "target_taxa": {"source": null, "target": null, "participants": [{"id": "NCBITaxon:1783273", "label": "Patescibacteria group"}, {"id": "NCBITaxon:131567", "label": "cellular organisms"}]}}. Current arrow description: HYPOTHESIZED - autotrophically fixed carbon can supply bacterial lipid production and the community material available for CPR acquisition. The isotope, lipid and genomic observations support this proposed carbon route but do not trace transfer from a particular producer to CPR cells.. Retain HYPOTHESIZED. PMID32203118 Results and discussion → In situ carbon fixation sustains microbial communities irrespective of aquifer depth, paragraphs1–3, Figure 2a–b; Model of lipid transfer in the community and conclusions, paragraph 1, and Results and discussion → Lysolipids and Candidate Phyla Radiation bacteria, paragraph 3; Predicting linkage of IPLs to uncultivated organisms, paragraphs1–4; Model of lipid transfer in the community and conclusions, paragraph 2/Figure 5. No separate edge-local excerpt exists; source-node exact excerpt bindings and these paragraphs define support. Community fixed carbon could supply material for CPR acquisition, but producer-resolved transfer is not traced.

### Putative CPR Lipid Acquisition

graph: supported. Targets: CommunityMech:000252.

Retain proposed acquisition of lipids or precursors with unresolved donors, scavenging and unknown-biosynthesis alternatives; no measured directed flux.

Exact selector ecological_interactions[1]; name Putative CPR Lipid Acquisition; scope COMMUNITY_LEVEL; interaction_type CROSS_FEEDING. Actual taxa: {"source": null, "target": null, "participants": [{"id": "NCBITaxon:1783273", "label": "Patescibacteria group"}, {"id": "NCBITaxon:131567", "label": "cellular organisms"}]}. Canonical evidence bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "e4890a6eb1a599d27be5fd1240288fae1f200f208c0586379b5dfd79eb3f9add", "reference": "PMID:32203118", "supports": "PARTIAL", "evidence_source": "IN_VIVO"}, {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "9330f3aa5d699822b8cbf89a50f3282114b701a34760f3a8f8dd234da80885cb", "reference": "PMID:32203118", "supports": "PARTIAL", "evidence_source": "IN_VIVO"}, {"selector": "ecological_interactions[1].evidence[2].snippet", "sha256": "aa0baeca6e4e0b80c7366096bef1ee67730d300b78af7d57140836e7b7aafcdc", "reference": "PMID:32203118", "supports": "PARTIAL", "evidence_source": "OTHER"}]. Snippet audit SHA256 963eb2cc02c63aad6b827bd23b6ded0ca89b72e859cfa2a4785e77967550af80. PMID32203118 source locator: Results and discussion → Lysolipids and Candidate Phyla Radiation bacteria, paragraph 3; Predicting linkage of IPLs to uncultivated organisms, paragraphs1–4; Model of lipid transfer in the community and conclusions, paragraph 2/Figure 5. Retain actual evidence tiers: PARTIAL IN_VIVO, PARTIAL IN_VIVO, PARTIAL OTHER. Retain proposed acquisition of lipids or precursors with unresolved donors, scavenging and unknown-biosynthesis alternatives; no measured directed flux.

### Putative CPR Lipid Acquisition → CPR-Associated Lysolipids and Proposed Curvature Adaptation

graph: supported. Targets: CommunityMech:000252.

Retain the existing HYPOTHESIZED direction and its uncertainty.

Exact selector ecological_interactions[1].downstream[0]; actual direction/participants: {"source_node": "Putative CPR Lipid Acquisition", "target_node": "CPR-Associated Lysolipids and Proposed Curvature Adaptation", "source_scope": "COMMUNITY_LEVEL", "target_scope": "COMMUNITY_LEVEL", "source_taxa": {"source": null, "target": null, "participants": [{"id": "NCBITaxon:1783273", "label": "Patescibacteria group"}, {"id": "NCBITaxon:131567", "label": "cellular organisms"}]}, "target_taxa": {"source": null, "target": null, "participants": [{"id": "NCBITaxon:1783273", "label": "Patescibacteria group"}]}}. Current arrow description: HYPOTHESIZED - acquired community lipids or precursors could provide material for CPR-associated lysolipid membranes and their proposed curvature adaptation. Lipid correlations and mixed-fraction spectroscopy do not demonstrate that acquisition causes lysolipid enrichment or that enrichment improves curvature tolerance.. Retain HYPOTHESIZED. PMID32203118 Results and discussion → Lysolipids and Candidate Phyla Radiation bacteria, paragraph 3; Predicting linkage of IPLs to uncultivated organisms, paragraphs1–4; Model of lipid transfer in the community and conclusions, paragraph 2/Figure 5, and Results and discussion → Lysolipids and Candidate Phyla Radiation bacteria, paragraphs1–3; Figure 4; Supplementary FiguresS10–S12 and separate2014 sample in TableS1. No separate edge-local excerpt exists; source-node exact excerpt bindings and these paragraphs define support. Proposed acquisition could supply lysolipids, but uptake-to-curvature benefit and causal membrane fitness remain unresolved.

### CPR-Associated Lysolipids and Proposed Curvature Adaptation

graph: supported. Targets: CommunityMech:000252.

Retain CPR-associated lysolipids in mixed enriched fractions and proposed curvature benefit; no pure-isolate or membrane-mechanical fitness assay.

Exact selector ecological_interactions[2]; name CPR-Associated Lysolipids and Proposed Curvature Adaptation; scope COMMUNITY_LEVEL; interaction_type not asserted. Actual taxa: {"source": null, "target": null, "participants": [{"id": "NCBITaxon:1783273", "label": "Patescibacteria group"}]}. Canonical evidence bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "d8ee2375479dcfdea7375e97ee97f1c2178905f0237631066c56dab5139e87ac", "reference": "PMID:32203118", "supports": "PARTIAL", "evidence_source": "IN_VIVO"}]. Snippet audit SHA256 963eb2cc02c63aad6b827bd23b6ded0ca89b72e859cfa2a4785e77967550af80. PMID32203118 source locator: Results and discussion → Lysolipids and Candidate Phyla Radiation bacteria, paragraphs1–3; Figure 4; Supplementary FiguresS10–S12 and separate2014 sample in TableS1. Retain actual evidence tiers: PARTIAL IN_VIVO. Retain CPR-associated lysolipids in mixed enriched fractions and proposed curvature benefit; no pure-isolate or membrane-mechanical fitness assay.

### Natural origin versus equilibrium state

identity: concern. Targets: CommunityMech:000252.

NATURAL is supported; optional STABLE is not established by one cyclic sampling trajectory.

The final sample near the beginning of an ordination trajectory supports restoration of a sampled assemblage. The study documents pronounced phase-dependent community changes, not stable equilibrium. Remove unsupported optional STABLE or attach actual equilibrium evidence; do not automatically substitute TRANSIENT or PERTURBED.

### Field environment and absence of cultivation

completeness: supported. Targets: CommunityMech:000252.

Groundwater, CO2-rich aquifer context and natural sampling are appropriate; empty growth_media is not a defect.

Sampling spans recovery/intermediate, minor/deep and major/shallow sources. Measured conduit pressure, temperature and conductivity, together with cited pH, are not controlled growth conditions or direct depth-pressure manipulation. No vessel, incubation, nutrient recipe or operating mode should be invented from filters, cold storage, chromatography temperature or the approximately five-day field cycle.

### Ontology meaning and unresolved taxonomic mappings

grounding: supported. Targets: CommunityMech:000252.

Eight ID-label pairs match and both current UNRESOLVED statuses remain justified.

Broad lipid/fatty-acid classes and carbon-fixation/lipid-metabolism GO terms fit the declared context without identifying exchanged molecules. The source differentiates DIC, bicarbonate and CO2; the CO2 term need not encode every inorganic-carbon species. No forced species, phylum, single GTDB domain or new functional-role assignment is warranted.

### Source-declared data and code traceability

completeness: concern. Targets: CommunityMech:000252.

Verified declared resources are not represented by the two publication-only external links.

Add bounded project and source-specific resource links, distinguishing derived MAG submissions from raw-read samples, supplementary tables and code. Preserve differing sample layers and any unavailable public endpoint. No analysis software citation is automatically a focal deposit and no source accession range establishes exact run counts by arithmetic alone.

### Strict snippets and title representation

evidence: supported. Targets: CommunityMech:000252.

Twelve fresh strict matches plus one explicit title projection; all thirteen match selected cache.

The title CO(2)/CO2 difference is representational. The Results-level author interpretation matches fresh XML and full MD but is absent from the short TXT. Native success is not a thirteen-strict-fresh-match certificate. The MD has appended main despite abstract_only metadata; preserve original cache bytes and document the distinction, without a separate scored finding.

### Both prior reviews and current follow-up

ownership: supported. Targets: CommunityMech:000252.

Batch27 and later direct batch91 preserve the existing qualified graph; new science scope does not rewrite their history.

Both exact prior rows and current issue contexts are bound. Prior1365 graph repair is closed, 1366 metadata follow-up remains open. Shared1744/596/746/524 do not automatically become focal defects or close from this review. Earlier dated uninspected-source statements remain accurate at their original dates; a new follow-up can record present full access.

### Main and supplementary material with bounded workbook inspection

scope: supported. Targets: CommunityMech:000252.

Available critical material supports completed scientific review of the current qualitative claims.

Whole main and supplementary text, all 5main/12SIfigures and three printed supplementary tables were inspected. Four small workbook sheets were read completely; remaining headers and selected reference-annotation rows were read. No complete raw lipid matrix or raw sequencing reanalysis is claimed. Source-internal phase, sample-label, count and volume discrepancies are retained as limits rather than imported as record errors.

### Focused checks and contextual diagnostics

schema: supported. Targets: CommunityMech:000252.

Eight focused native checks pass; nonrequired corpus failures and adapter unavailability remain explicit.

No native failure is inferred from the title projection or scientific overclaims. Reference validation has known Discussion-coverage limits and cannot certify mechanistic entailment.

### Literal metrics

completeness: supported. Targets: CommunityMech:000252.

Completeness75; raw quality117.66666666666669, capped100.

## Findings

### non-graph-scope: Align role and mechanism prose with source uncertainty

major / open / confirmed; issue key: cm-000252-non-graph-scope.

The hard CPR SYNTROPHIC_PARTNER role and categorical lipid-origin/pressure-adaptation fields overstate hypotheses that the existing graph already qualifies. Known-pathway deficits, mixed-fraction observations and depth associations do not resolve a syntrophic partner exchange, universal synthesis inability or induced pressure response.

### state-scope: Support or omit the equilibrium-state assertion

minor / open / confirmed; issue key: cm-000252-state-scope.

The optional STABLE value asserts equilibrium. Observed phase-dependent turnover and cyclic return near an initial sample do not establish that state.

### resources: Add declared data and code traceability with exact scopes

minor / open / confirmed; issue key: cm-000252-resources.

The current external links identify only the publication. The source supplies project, derived-genome, raw-sample, supplementary-table and code resources that can be represented with verified scope.

## Recommended Actions And Acceptance Checks

### qualify-nongraph

Align non-graph statements with the source-supported hypotheses.

- Retain positive isotope/genomic support for predominantly autotrophic carbon supply and PRIMARY_PRODUCER. Qualify the hard CPR SYNTROPHIC_PARTNER role or omit it unless claim-local evidence establishes syntrophic metabolism; do not force another role, named donor, obligacy, reciprocal growth or product-removal requirement.
- Represent absence of known complete pathways in the analyzed CPR genomes without a universal inability claim. Preserve near-complete Nealsonbacteria pathways and possible ACP-independent/unknown synthesis, plus degraded-biomass scavenging and direct-host acquisition alternatives.
- Qualify taxonomy[1].taxon_term.notes and related_ingredients[1] donor-origin wording as a proposed contribution; preserve the broad bacterial/archaeal carbon-fixing pool without treating all of it as demonstrated CPR lipid donors. Figure 5 bacterial-to-CPR and archaeal/DPANN contexts remain distinct.
- Qualify the categorical pressure clause in description and related_ingredients[2] as a depth-associated profile interpreted as possible pressure adaptation. Do not claim a controlled pressure response, an exact producing taxon, exclusively double bonds or a tested curvature/fitness benefit.
- Retain three nodes and both HYPOTHESIZED arrows with actual directions, participants and current evidence tiers. Preserve mixed2015 lipid fraction versus separate2014 FTIR sample; no pure-CPR isolation or mandatory graph expansion.

### repair-state

Remove unsupported equilibrium certainty without inventing a substitute.

- Support ecological_state STABLE with actual equilibrium evidence, or omit this optional field. NATURAL origin and recurring geyser behavior alone are insufficient.
- Retain observed phase-dependent community shifts and final-sample restoration as the reported findings. Do not automatically substitute TRANSIENT or PERTURBED; do not treat the five-day sampling cycle as an incubation period.

### add-resources

Represent verified source-linked data and code with bounded provenance.

- Add PRJNA602879 and the source SAMN13287258–SAMN13287462 derived-genome context. The two verified endpoint BioSamples explicitly derive from community samples; the interior range was not exhaustively verified. Preserve the separate paper206 new genomes, 205 inclusive accession numbers and current201 linked assemblies; do not equate these denominators.
- Keep all 28 resolved TableS1 SRS identities separate from newly deposited MAGs:27 cycle samples plus the separate2014 FTIR sample. The exact umbrella query returns26 WGS METAGENOMIC libraries, mapping CG02–CG26B. CG01/WGA SAMN07631059 and 2014 SAMN07960332 are outside this returned set; no global SRA/ENA absence is inferred.
- Link source TablesS4–S5 as supplied workbooks, with sample-label/date discrepancies explicit if those details are used. S5 reference-similarity annotations must not become exact collected-strain identities.
- Link https://ggkbase.berkeley.edu/genome_summaries/1491-Bacterial_membrane_lipids_AJP as a verified named landing page without claiming all 675 dynamic annotation rows were inspected. Link https://github.com/AJProbst/lip_metgen and https://github.com/AJProbst/rpS3_trckr as verified source-specific analysis repositories; metadata verification is not code execution. Generic analysis tools are not study deposits.

### validate-future-curation

Validate separately authorized repairs and preserve the review chain.

- After authorized curation, attach exact source-local evidence, update history and run schema, strict, terms, explained references, GTDB, domain and history checks, then just gen-html and just check-docs-current. This review does not modify canonical, cache, history or generated files.
- Preserve both prior-review records, current source/asset and support receipts, all source-internal discrepancies and the explicit title representation projection. No paid retrieval, contact, automatic issue closure or full raw-data reanalysis is implied.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml; Whole maintained YAML | supports | Two broad descriptors represent CPR bacteria and a CO2-fixing bacterial/archaeal functional pool. Three nodes and two HYPOTHESIZED arrows already separate supported observations from proposed lipid acquisition and curvature benefit. Stronger non-graph wording and optional STABLE state need repair. |
| sampling | PMID:32203118; DOI:10.1038/s41396-020-0624-4; Material and methods → Sampling scheme, sole paragraph; Results and discussion → Microbial community profile based on marker genes, paragraphs 1–2; Figure 1; Supplementary Tables S1–S2 and Figure S1 | supports | This is field sampling over an approximately five-day geyser cycle, with 27 metagenomes and 14 lipidomes. Recovery, minor and major phases access differing water sources; a final size-fractionated sample near initial composition suggests restoration, not demonstrated equilibrium. Filtration, storage and analytical temperatures are not a growth recipe. |
| carbon | PMID:32203118; DOI:10.1038/s41396-020-0624-4; Results and discussion → In situ carbon fixation sustains microbial communities irrespective of aquifer depth, paragraphs 1–3, especially paragraph 2; Figure 2a–b | supports | Stable isotopic compositions of bacterial fatty acids and archaeal phytane, genomic pathways and geological context support predominantly autotrophic biomass. Mass-balance estimates assume fractionation ranges and permit heterotrophic reuse; they do not trace a particular producer-to-CPR lipid flux. |
| pressure | PMID:32203118; DOI:10.1038/s41396-020-0624-4; Results and discussion → Degree of unsaturation of bacterial IPL changes with groundwater source depth, sole paragraph; Figure 2c; Supplementary Figures S7–S8 | supports | Relative highly unsaturated lipid abundance correlates with deeper groundwater sources at nearly constant temperature. The source proposes pressure adaptation, considers eukaryotic contributions and cannot strictly exclude cycloalkyl features among double-bond equivalents. No within-organism pressure perturbation demonstrates induced adaptation. |
| correlations | PMID:32203118; DOI:10.1038/s41396-020-0624-4; Material and methods → Statistical analysis to correlate taxa abundance with IPLs, sole paragraph; Results and discussion → Predicting linkage of IPLs to uncultivated organisms, paragraphs 1–5; Figure 3 and Table 1 | supports | Relative rpS3 marker and lipid profiles identify significant primary correlations and secondary lipid co-correlations. Shared lipid sources, DNA/lipid turnover and filtration-associated lysis limit causal assignment. The separate Altiarchaeum/Huberiarchaeum model is not proof of an archaeal donor to CPR. |
| fractions | PMID:32203118; DOI:10.1038/s41396-020-0624-4; Results and discussion → Lysolipids and Candidate Phyla Radiation bacteria, paragraphs 1–2; Figure 4; Supplementary Figures S10–S12 and Table S1 | supports | The 2015 post-0.2-µm lipid fraction contains 186 organisms, 165 classified as CPR, but Sulfurimonas is the most abundant organism. A separate 2014 recovery-phase FTIR sample has CPR in the first seven abundance ranks. Mixed-fraction lipidomics and micrometre-resolution FTIR support CPR-associated lysolipids, not purified-isolate membrane quantification. |
| biosynthesis | PMID:32203118; DOI:10.1038/s41396-020-0624-4; Material and methods → Genomic analysis of lipid biosynthesis pathways in CPR genomes, sole paragraph; Results and discussion → Lysolipids and Candidate Phyla Radiation bacteria, paragraph 3 | supports | The analysis of 675 CPR genomes finds no known complete lipid synthesis pathway. Near-complete Nealsonbacteria pathways and possible ACP-independent synthesis remain explicit alternatives. The proposed acquisition of lipids or precursors from coexisting bacteria could involve degraded biomass or direct host derivation; no resolved partner exchange is demonstrated. |
| model | PMID:32203118; DOI:10.1038/s41396-020-0624-4; Results and discussion → Model of lipid transfer in the community and conclusions, paragraphs 1–2; Figure 5; preceding Lysolipids and Candidate Phyla Radiation bacteria, paragraph 3 | supports | The authors synthesize isotope, genome, lipidomic and FTIR evidence into a carbon/lipid redistribution model. Figure 5 depicts bacterial lipids toward CPR and a separate archaeal/DPANN context. Lysolipid curvature-stress reduction is proposed; it is not a measured fitness, membrane-mechanical or obligatory syntrophic interaction. |
| deposition | PMID:32203118; DOI:10.1038/s41396-020-0624-4; Material and methods → Binning of genomes, sole paragraph; Tracking taxa across time using ribosomal protein S3, sole paragraph; Statistical analysis to correlate taxa abundance with IPLs, sole paragraph; Results and discussion → Lysolipids and Candidate Phyla Radiation bacteria, paragraph 3; Supplementary Table S1 and Tables S4–S5 | supports | The source declares PRJNA602879 and a BioSample range for newly reconstructed genomes, ggKbase genome summary 1491, source-specific analysis repositories, raw-read sample accessions in S1 and lipid/relative-abundance workbooks S4–S5. These resource layers must retain their distinct raw-read, derived-genome, table and code scopes. |
| ontology | /private/tmp/cm-review-session/batch-13/000252/ontology-authority.json; All eight exact ID-label definitions/ranks and seventeen placements | supports | All labels match. Carbon fixation and lipid metabolic process are appropriate broad contexts; neither a chemical class nor a GO term demonstrates donor-specific uptake or membrane adaptation. |
| schema | /private/tmp/cm-review-session/batch-13/000252/child-schema-semantics.json; Literal functional roles, ecological state, interaction and evidence semantics | supports | SYNTROPHIC_PARTNER means engagement in syntrophic metabolism, not generic putative symbiosis. No obligatory coupling or separate product-removal criterion is imposed. STABLE asserts equilibrium; IN_VIVO explicitly permits field studies. |
| lineage | /private/tmp/cm-review-session/batch-13/000252/child-taxon-lineage.json; Both encoded taxonomic ranks and complete current ancestry | supports | Patescibacteria group is a clade, not a species or automatically one phylum. Cellular organisms is a multi-domain root narrowed by the preferred functional-pool label. Overlapping ancestry alone is not a duplicate-member defect. |
| gtdb | /private/tmp/cm-review-session/batch-13/000252/child-gtdb-crosswalk.json; Exact encoded ID/name lookup results | supports | Neither encoded group resolves in the current local crosswalk. Preserve both UNRESOLVED statuses; there is no encoded latest/build claim to repair and no requirement to assign a species or single domain to the broad pool. |
| gtdb-synonym | /private/tmp/cm-review-session/batch-13/000252/child-gtdb-synonym-probe.json; One authority-supported Patescibacteria synonym probe | supports | The bounded alternate name also has no resolution. This is a snapshot lookup boundary, not evidence that the organisms lack genomes or that GTDB has no related taxa globally. |
| semantics | /private/tmp/cm-review-session/batch-13/000252/ontology-semantic-notes.json; Final claim-specific role, state, chemistry and graph assessment | supports | Retain PRIMARY_PRODUCER, NATURAL origin, broad taxa and the qualified graph. Align categorical non-graph lipid dependence, donor contribution and pressure adaptation with source uncertainty; assess equilibrium separately. |
| snippets | /private/tmp/cm-review-session/batch-13/000252/snippet-audit.json; All thirteen exact reference-specific excerpt occurrences | supports | Twelve occurrences strictly match fresh XML; all thirteen match selected cache. The title uses CO(2) in the cache versus CO2 in fresh XML and has an explicit representation projection. The full Results sentence is present in fresh XML/MD but not the short TXT cache. |
| title-projection | /private/tmp/cm-review-session/batch-13/000252/snippet-title-representation-projection.json; Exact external_resources[0].evidence[0].snippet title representation | supports | The CO(2)/CO2 title difference is explicitly recorded as a representation projection. It does not invalidate publication identity or create an additional scientific finding. |
| contexts | /private/tmp/cm-review-session/batch-13/000252/snippet-source-contexts.json; Whole Abstract, Results lysolipid paragraph 3 and Article title contexts | supports | All three containing contexts were read. Abstract lexical support does not supersede the fuller pathway exceptions, alternative acquisition routes and observational design. Five exact node excerpt hashes are bound below without reproducing long quotations. |
| resources | /private/tmp/cm-review-session/batch-13/000252/dataset-verification.json; Direct bounded project, accession, table and code verification | supports | PRJNA602879 returns26 WGS metagenomic run/sample pairs; all 28 S1 SRS records resolve. CG01/WGA and separate2014 FTIR are outside that returned run set, not globally absent. Two declared MAG endpoints are derived assemblies. Both named GitHub repositories and ggKbase1491 landing identity resolve; no code execution or full dynamic annotation review occurred. |
| provenance | /private/tmp/cm-review-session/batch-13/000252/provenance-audit.json; Sole history, exact batch27 records[0] and batch91 records[1], cohort and current issue scope | supports | Batch91 is a later direct review that preserved this graph. Current1365 graph repair is closed; 1366 non-graph follow-up remains open. Both caches remain unchanged, with an appended main body despite stale abstract_only MD metadata. Historical uninspected-SI statements remain dated facts. |
| inspection | /private/tmp/cm-review-session/batch-13/000252/inspect.json; Thirty-three immutable official inputs | supports | Target, 21 shared authorities and 11 focal context files are pinned, including both direct prior decisions. Discovery included ignored files; generic inventories and cross-citation-only caches were not promoted to source reviews. |
| assets | /private/tmp/cm-review-session/batch-13/000252/lead-source-assets.json; Complete main, declared PDF and two workbooks with bounded data reading | supports | All 70842 main characters, 79 references, Table 1 and five main figures were read/viewed. Whole supplementary text and 31references were read; all 12 supplementary figures and three printed tables were visually inspected. Workbook coverage is explicitly bounded rather than claimed as full matrix reanalysis. |
| workbooks | /private/tmp/cm-review-session/batch-13/000252/lead-primary/supplement/workbook-bounded-read.json; All sheet inventories, four complete small S4 sheets, headers and selected S5 annotations | supports | All nonempty rows of Sampling, Lipid identification FigS3, S4, Core lipid concentrations and Core lipid and DIC d13C were read. Fourteen IPL sheet headers and the S5 header plus eight selected annotation rows were read. Formatting max_row values are not organism counts; reference-similarity labels are not exact sampled strains. |
| source-sections | /private/tmp/cm-review-session/batch-13/000252/source-section-projection.json; Fresh JATS section titles and direct paragraph numbering | supports | Named primary locators were checked against actual section structure; nested figure/table content is preserved in parent paragraphs. The only quotation is located in the carbon-fixation Results paragraph 2. |
| lead-read | /private/tmp/cm-review-session/batch-13/000252/lead-primary-read-scope.json; Actual independent lead source and authority read boundaries | supports | Lead whole main/SI and figure reads plus bounded workbook inspection are explicit. Sibling owns full cache/history/current issue and raw registry reads; this receipt makes no duplicate complete raw-data review claim. |
| source-scope | /private/tmp/cm-review-session/batch-13/000252/source-audit.json; Final one-major/two-minor scientific grouping | supports | Completed scientific review covers current qualitative claims, with source-internal conflicts retained as limits. No critical source remains inaccessible. Completion is not a clean biological verdict. |
| root-source | /private/tmp/cm-review-session/batch-13/000252/root-independent-source-audit.json; Independent root scientific assessment and precise read scope | supports | Root independently reviewed the main, figures, supplementary text/tables and bounded workbook/source authority context. Its final scientific decision is reconciled with the source and support receipts. |
| metrics | /private/tmp/cm-review-session/batch-13/000252/support-final-audit.json; Distinct frozen support and literal metrics | supports | Completeness75; base131.66666666666669 minus one major and two minor findings gives raw117.66666666666669, capped100. Scores do not override biological findings or require a culture recipe for field samples. |
| support-manifest | /private/tmp/cm-review-session/batch-13/000252/supporting-artifact-manifest.json; Final immutable supporting artifact manifest | supports | Final support follows source/authority freeze; preliminary support, prior records, source bytes and all 33 maintained inputs remain unchanged. |
| auxiliary | /private/tmp/cm-review-session/batch-13/000252/auxiliary-frozen-manifest.json; Final native/authority artifact manifest | supports | Eight ontology pairs across seventeen placements match; all eight focused checks pass. Both unresolved mappings and source-aware semantic boundaries are retained. |
| final-native | /private/tmp/cm-review-session/batch-13/000252/final-validator-summary.json; Eight actual focused commands and immutable outputs | supports | All eight executed checks pass. Reference-validator zero issues is not an excerpt count or independent proof of claim entailment; Discussion coverage remains limited. |
| corpus-context | /private/tmp/cm-review-session/batch-13/000252/child-current-corpus-context.json; Fresh batch13 corpus diagnostics | supports | Both corpus diagnostics exited1 with 44 warnings across 16 of 477 records and zero errors. They are contextual nonrequired checks, distinct from focused target validation. |
| adapter | /private/tmp/cm-review-session/batch-13/000252/adapter-check.json; Optional adapter availability in the owned runtime | supports | The optional structured adapter is unavailable. No paid provider, dotenv credential lookup or external-checkout execution was used. |
| check-validate | /private/tmp/cm-review-session/batch-13/000252/validate.json; Actual immutable command/stdout/stderr | supports | Focused native command passed; claim entailment is assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-13/000252/validate-strict.json; Actual immutable command/stdout/stderr | supports | Focused native command passed; claim entailment is assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-13/000252/validate-terms.json; Actual immutable command/stdout/stderr | supports | Focused native command passed; claim entailment is assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-13/000252/validate-references-explained.json; Actual immutable command/stdout/stderr | supports | Focused native command passed; claim entailment is assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-13/000252/validate-gtdb.json; Actual immutable command/stdout/stderr | supports | Focused native command passed; claim entailment is assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-13/000252/validate-gtdb-domain.json; Actual immutable command/stdout/stderr | supports | Focused native command passed; claim entailment is assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-13/000252/validate-history.json; Actual immutable command/stdout/stderr | supports | Focused native command passed; claim entailment is assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-13/000252/normalize-cache-names-check.json; Actual immutable command/stdout/stderr | supports | Focused native command passed; claim entailment is assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-13/audit-network.json; Actual fresh batch13 corpus baseline | supports | Exit1 with 44 warnings across 16 of 477 records and zero errors; contextual scope preserved. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-13/check-network-quality.json; Actual fresh batch13 corpus baseline | supports | Exit1 with 44 warnings across 16 of 477 records and zero errors; contextual scope preserved. |

## Limits And Additional Notes

- The source Figure 2c caption calls major eruptions deep, whereas main text, Figure 1 and S1 identify minor/deep and major/shallow. This internal conflict is retained rather than silently harmonized.
- The2015post-0.2µm lipid fraction is mixed and has abundant Sulfurimonas; the separate2014 FTIR sample is CPR-enriched. Neither establishes isolated-cell lipid percentages, exact donors or membrane-mechanical fitness.
- Genomic deficits concern known pathways; unknown/ACP-independent synthesis remains possible. Lipid scavenging and direct-host acquisition are alternatives. Isotope mass-balance estimates depend on fractionation and permit heterotrophic reuse.
- Source TableS2 maximum388L differs from main338L; TableS3 DOC wording/dates and FigureS8 protein/cluster counts are internally inconsistent. No current encoded numeric claim is corrected from these unencoded conflicts.
- S4 sample dates/phase labels and CG29/CG12 sheet labels differ from PDF summaries. Selected S5 annotations are reference similarities, not exact collected strains; complete raw matrices and raw sequence libraries were not independently reanalysed.
- Twelve snippets strictly match fresh XML; the title has an explicit CO(2)/CO2 representation projection. All thirteen match selected cache; the full Results sentence is absent from the short TXT cache. The full MD append coexists with stale abstract_only metadata.
- Registry, raw-sample, derived-genome, code and supplementary-table scopes remain distinct. No global absence statement or unverified accession-to-experiment assignment is inferred from a bounded query.
- Three exact node assessments bind all five canonical excerpt hashes; both HYPOTHESIZED arrows bind actual directions and participants. No long canonical source excerpts are copied.
- The only two-word quotation is predominantly autotrophic, directly from Results and discussion → In situ carbon fixation sustains microbial communities irrespective of aquifer depth, paragraph 2.
- All 33 official inputs remain unchanged. Both direct prior-review contexts, batch27 and batch91, are retained; root alone saves after independent acceptance.
- Focused native 8passes, actual nonrequired corpus failures and unavailable optional adapter are explicitly represented. No new candidate-validation failure is assumed from a scientific finding.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T015146Z-crystal-geyser-cpr-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Crystal Geyser CPR lipid community record review
started_at: '2026-10-22T01:42:15.058487Z'
finished_at: '2026-10-22T01:51:46.564515Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, authority and supporting reviewers; no
    person-level independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Complete primary and supplementary source review supports retaining three
  qualified nodes and two HYPOTHESIZED arrows. One major finding groups stronger non-graph
  role, lipid-origin and pressure-adaptation claims; two minor findings concern unsupported
  equilibrium state and declared-resource traceability. All eight focused checks pass.
  Literal completeness 75 and raw quality117.66666666666669/cap100 do not certify
  a clean biological record.
source:
  git_revision: e117e3d37c65bfad2e04af53ab34e1325d8d7f98
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
  - path: history/records/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community/2026-10-06T041950Z-codex-5086e8.yaml
    sha256: aac2a1a4a2859cc228b0b270468f3c387efd22aed03e34f334d7091d1a03ff3a
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
    sha256: b219156340ab8170a318ed82b9bf47e7a5a5b67e490870d42fabb2c9a8e25051
    role: target
  - path: references_cache/PMID_32203118.md
    sha256: ed47b1021b5307304a7ac65b99353942f4db7873cf2bf8cec3ccd52e573872b6
    role: context
  - path: references_cache/PMID_32203118.txt
    sha256: 5d873129a219c729435a36dfe6c9c59a29be4befe7dde10294a8db6025d452f3
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch27.yaml
    sha256: e643b8f12adfc71acdd4f9bca108689885b70c32ea93b44b1055d73f3022cad0
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261007-batch91.yaml
    sha256: 973b2a59f1e53a1bb9405f813af5a20a8593a8f4efb1837e4fa847772636105e
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch27.yaml
    sha256: 90e6a0ad3e095a1301744958f706782510d03bdf40852999837d12401019ded0
    role: context
  - path: reports/causal_graph_review/decisions/20261007-five-records-batch91.yaml
    sha256: 55c2dafc3c10346c37f864ef5acc1fdadefd37967c51f21696eef562a0296bbe
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.md
    sha256: e432615b147787c8d009d96d2f11e5b78a45927bf9c69e45ec0d31123d1fc2e9
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.yaml
    sha256: 37d089fd55c077793dd20d868b50c47cb1cceab6dae6a82887cc938bee05fa6d
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/frozen_inventory_metrics.tsv
    sha256: d5a47bbcc3745a489ff507680aa7360a6a65ce070ce4ec88f886b70128791313
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/review_report.md
    sha256: 4e7781aa8cdfc4bb42d896ebe75920719d9dcade92ffc4a0ae07af7481cb37b3
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
- target_id: CommunityMech:000252
  path: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
  label: Crystal Geyser CO2-Rich Aquifer Autotrophic CPR Lysolipid Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
    role: canonical_record
scope:
  description: Whole maintained record and fresh main including79references,Table1
    and five main figures; whole supplementary text,31references,12figures and three
    printed tables; bounded inspection of both workbooks and current authority/provenance/registry
    checks.
  selection: Only released CommunityMech:000252 in owned batch13.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000252
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000252
  command: just --no-dotenv validate kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused current record/history check; cache-name preflight is corpus-wide.
    All33 official inputs remain unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000252
  command: just --no-dotenv validate-strict kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
    --out /private/tmp/cm-review-session/batch-13/000252/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused current record/history check; cache-name preflight is corpus-wide.
    All33 official inputs remain unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000252
  command: just --no-dotenv validate-terms kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused current record/history check; cache-name preflight is corpus-wide.
    All33 official inputs remain unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000252
  command: just --no-dotenv validate-references-explained kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused current record/history check; cache-name preflight is corpus-wide.
    All33 official inputs remain unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000252
  command: just --no-dotenv validate-gtdb kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused current record/history check; cache-name preflight is corpus-wide.
    All33 official inputs remain unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000252
  command: just --no-dotenv validate-gtdb-domain kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused current record/history check; cache-name preflight is corpus-wide.
    All33 official inputs remain unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000252
  command: just --no-dotenv validate-history history/records/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused current record/history check; cache-name preflight is corpus-wide.
    All33 official inputs remain unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000252
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused current record/history check; cache-name preflight is corpus-wide.
    All33 official inputs remain unchanged.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit1;44 warnings and zero errors.
  target_ids:
  - CommunityMech:000252
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-13/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus baseline, separate from focused record checks.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit1;44 warnings and zero errors.
  target_ids:
  - CommunityMech:000252
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-13/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus baseline, separate from focused record checks.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in the owned runtime.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - adapter
  scope_note: No external-checkout provider executed.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
  locator: Whole maintained YAML
  summary: Two broad descriptors represent CPR bacteria and a CO2-fixing bacterial/archaeal
    functional pool. Three nodes and two HYPOTHESIZED arrows already separate supported
    observations from proposed lipid acquisition and curvature benefit. Stronger non-graph
    wording and optional STABLE state need repair.
  support: supports
  accessed_at: '2026-10-22T01:50:26.348980Z'
- evidence_id: sampling
  kind: primary_source
  reference: PMID:32203118; DOI:10.1038/s41396-020-0624-4
  locator: Material and methods → Sampling scheme, sole paragraph; Results and discussion
    → Microbial community profile based on marker genes, paragraphs 1–2; Figure 1;
    Supplementary Tables S1–S2 and Figure S1
  summary: This is field sampling over an approximately five-day geyser cycle, with
    27 metagenomes and 14 lipidomes. Recovery, minor and major phases access differing
    water sources; a final size-fractionated sample near initial composition suggests
    restoration, not demonstrated equilibrium. Filtration, storage and analytical
    temperatures are not a growth recipe.
  support: supports
  accessed_at: '2026-10-22T01:50:26.349054Z'
  snapshot_sha256: 1a1adc25720a700480fd7ed2db7998e557e3f6e098915fe38b15eb2eaff05eaa
- evidence_id: carbon
  kind: primary_source
  reference: PMID:32203118; DOI:10.1038/s41396-020-0624-4
  locator: Results and discussion → In situ carbon fixation sustains microbial communities
    irrespective of aquifer depth, paragraphs 1–3, especially paragraph 2; Figure
    2a–b
  summary: Stable isotopic compositions of bacterial fatty acids and archaeal phytane,
    genomic pathways and geological context support predominantly autotrophic biomass.
    Mass-balance estimates assume fractionation ranges and permit heterotrophic reuse;
    they do not trace a particular producer-to-CPR lipid flux.
  support: supports
  accessed_at: '2026-10-22T01:50:26.349382Z'
  snapshot_sha256: 1a1adc25720a700480fd7ed2db7998e557e3f6e098915fe38b15eb2eaff05eaa
  quote: predominantly autotrophic
- evidence_id: pressure
  kind: primary_source
  reference: PMID:32203118; DOI:10.1038/s41396-020-0624-4
  locator: Results and discussion → Degree of unsaturation of bacterial IPL changes
    with groundwater source depth, sole paragraph; Figure 2c; Supplementary Figures
    S7–S8
  summary: Relative highly unsaturated lipid abundance correlates with deeper groundwater
    sources at nearly constant temperature. The source proposes pressure adaptation,
    considers eukaryotic contributions and cannot strictly exclude cycloalkyl features
    among double-bond equivalents. No within-organism pressure perturbation demonstrates
    induced adaptation.
  support: supports
  accessed_at: '2026-10-22T01:50:26.349469Z'
  snapshot_sha256: 1a1adc25720a700480fd7ed2db7998e557e3f6e098915fe38b15eb2eaff05eaa
- evidence_id: correlations
  kind: primary_source
  reference: PMID:32203118; DOI:10.1038/s41396-020-0624-4
  locator: Material and methods → Statistical analysis to correlate taxa abundance
    with IPLs, sole paragraph; Results and discussion → Predicting linkage of IPLs
    to uncultivated organisms, paragraphs 1–5; Figure 3 and Table 1
  summary: Relative rpS3 marker and lipid profiles identify significant primary correlations
    and secondary lipid co-correlations. Shared lipid sources, DNA/lipid turnover
    and filtration-associated lysis limit causal assignment. The separate Altiarchaeum/Huberiarchaeum
    model is not proof of an archaeal donor to CPR.
  support: supports
  accessed_at: '2026-10-22T01:50:26.349550Z'
  snapshot_sha256: 1a1adc25720a700480fd7ed2db7998e557e3f6e098915fe38b15eb2eaff05eaa
- evidence_id: fractions
  kind: primary_source
  reference: PMID:32203118; DOI:10.1038/s41396-020-0624-4
  locator: Results and discussion → Lysolipids and Candidate Phyla Radiation bacteria,
    paragraphs 1–2; Figure 4; Supplementary Figures S10–S12 and Table S1
  summary: The 2015 post-0.2-µm lipid fraction contains 186 organisms, 165 classified
    as CPR, but Sulfurimonas is the most abundant organism. A separate 2014 recovery-phase
    FTIR sample has CPR in the first seven abundance ranks. Mixed-fraction lipidomics
    and micrometre-resolution FTIR support CPR-associated lysolipids, not purified-isolate
    membrane quantification.
  support: supports
  accessed_at: '2026-10-22T01:50:26.349630Z'
  snapshot_sha256: 1a1adc25720a700480fd7ed2db7998e557e3f6e098915fe38b15eb2eaff05eaa
- evidence_id: biosynthesis
  kind: primary_source
  reference: PMID:32203118; DOI:10.1038/s41396-020-0624-4
  locator: Material and methods → Genomic analysis of lipid biosynthesis pathways
    in CPR genomes, sole paragraph; Results and discussion → Lysolipids and Candidate
    Phyla Radiation bacteria, paragraph 3
  summary: The analysis of 675 CPR genomes finds no known complete lipid synthesis
    pathway. Near-complete Nealsonbacteria pathways and possible ACP-independent synthesis
    remain explicit alternatives. The proposed acquisition of lipids or precursors
    from coexisting bacteria could involve degraded biomass or direct host derivation;
    no resolved partner exchange is demonstrated.
  support: supports
  accessed_at: '2026-10-22T01:50:26.349708Z'
  snapshot_sha256: 1a1adc25720a700480fd7ed2db7998e557e3f6e098915fe38b15eb2eaff05eaa
- evidence_id: model
  kind: primary_source
  reference: PMID:32203118; DOI:10.1038/s41396-020-0624-4
  locator: Results and discussion → Model of lipid transfer in the community and conclusions,
    paragraphs 1–2; Figure 5; preceding Lysolipids and Candidate Phyla Radiation bacteria,
    paragraph 3
  summary: The authors synthesize isotope, genome, lipidomic and FTIR evidence into
    a carbon/lipid redistribution model. Figure 5 depicts bacterial lipids toward
    CPR and a separate archaeal/DPANN context. Lysolipid curvature-stress reduction
    is proposed; it is not a measured fitness, membrane-mechanical or obligatory syntrophic
    interaction.
  support: supports
  accessed_at: '2026-10-22T01:50:26.349785Z'
  snapshot_sha256: 1a1adc25720a700480fd7ed2db7998e557e3f6e098915fe38b15eb2eaff05eaa
- evidence_id: deposition
  kind: primary_source
  reference: PMID:32203118; DOI:10.1038/s41396-020-0624-4
  locator: Material and methods → Binning of genomes, sole paragraph; Tracking taxa
    across time using ribosomal protein S3, sole paragraph; Statistical analysis to
    correlate taxa abundance with IPLs, sole paragraph; Results and discussion → Lysolipids
    and Candidate Phyla Radiation bacteria, paragraph 3; Supplementary Table S1 and
    Tables S4–S5
  summary: The source declares PRJNA602879 and a BioSample range for newly reconstructed
    genomes, ggKbase genome summary 1491, source-specific analysis repositories, raw-read
    sample accessions in S1 and lipid/relative-abundance workbooks S4–S5. These resource
    layers must retain their distinct raw-read, derived-genome, table and code scopes.
  support: supports
  accessed_at: '2026-10-22T01:50:26.349863Z'
  snapshot_sha256: 1a1adc25720a700480fd7ed2db7998e557e3f6e098915fe38b15eb2eaff05eaa
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-13/000252/ontology-authority.json
  locator: All eight exact ID-label definitions/ranks and seventeen placements
  summary: All labels match. Carbon fixation and lipid metabolic process are appropriate
    broad contexts; neither a chemical class nor a GO term demonstrates donor-specific
    uptake or membrane adaptation.
  support: supports
  accessed_at: '2026-10-22T01:50:26.349946Z'
  snapshot_sha256: 2518c8fa2dd08cbb6c820e4edaa293dbf26dc51a607a80cfaa1938fe165cfd9b
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-13/000252/child-schema-semantics.json
  locator: Literal functional roles, ecological state, interaction and evidence semantics
  summary: SYNTROPHIC_PARTNER means engagement in syntrophic metabolism, not generic
    putative symbiosis. No obligatory coupling or separate product-removal criterion
    is imposed. STABLE asserts equilibrium; IN_VIVO explicitly permits field studies.
  support: supports
  accessed_at: '2026-10-22T01:50:26.350156Z'
  snapshot_sha256: 127a7b036ecc15b59071e1350fb61e4de8e469d8a9491af889b84104d13676ac
- evidence_id: lineage
  kind: authority
  reference: /private/tmp/cm-review-session/batch-13/000252/child-taxon-lineage.json
  locator: Both encoded taxonomic ranks and complete current ancestry
  summary: Patescibacteria group is a clade, not a species or automatically one phylum.
    Cellular organisms is a multi-domain root narrowed by the preferred functional-pool
    label. Overlapping ancestry alone is not a duplicate-member defect.
  support: supports
  accessed_at: '2026-10-22T01:50:26.350333Z'
  snapshot_sha256: 5e4c6c13cd93af0e3cab9825925e0cacc706653513292fdd9b70a94ba1df04cf
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-13/000252/child-gtdb-crosswalk.json
  locator: Exact encoded ID/name lookup results
  summary: Neither encoded group resolves in the current local crosswalk. Preserve
    both UNRESOLVED statuses; there is no encoded latest/build claim to repair and
    no requirement to assign a species or single domain to the broad pool.
  support: supports
  accessed_at: '2026-10-22T01:50:26.350497Z'
  snapshot_sha256: 1539032662ef96ece7ad157c46beeef3b834bcd12711af0b3585fcdaeeb1a353
- evidence_id: gtdb-synonym
  kind: authority
  reference: /private/tmp/cm-review-session/batch-13/000252/child-gtdb-synonym-probe.json
  locator: One authority-supported Patescibacteria synonym probe
  summary: The bounded alternate name also has no resolution. This is a snapshot lookup
    boundary, not evidence that the organisms lack genomes or that GTDB has no related
    taxa globally.
  support: supports
  accessed_at: '2026-10-22T01:50:26.350605Z'
  snapshot_sha256: 6cf8738350901e3f74fbdaae35b92bf8f2ee86e70498909cc9b8af519ef69f2a
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-13/000252/ontology-semantic-notes.json
  locator: Final claim-specific role, state, chemistry and graph assessment
  summary: Retain PRIMARY_PRODUCER, NATURAL origin, broad taxa and the qualified graph.
    Align categorical non-graph lipid dependence, donor contribution and pressure
    adaptation with source uncertainty; assess equilibrium separately.
  support: supports
  accessed_at: '2026-10-22T01:50:26.350759Z'
  snapshot_sha256: a8facc67bbaeca468a33e133ae10ff96af3d945c421a1f17a16a30ca8a10930c
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/snippet-audit.json
  locator: All thirteen exact reference-specific excerpt occurrences
  summary: Twelve occurrences strictly match fresh XML; all thirteen match selected
    cache. The title uses CO(2) in the cache versus CO2 in fresh XML and has an explicit
    representation projection. The full Results sentence is present in fresh XML/MD
    but not the short TXT cache.
  support: supports
  accessed_at: '2026-10-22T01:50:26.350909Z'
  snapshot_sha256: 963eb2cc02c63aad6b827bd23b6ded0ca89b72e859cfa2a4785e77967550af80
- evidence_id: title-projection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/snippet-title-representation-projection.json
  locator: Exact external_resources[0].evidence[0].snippet title representation
  summary: The CO(2)/CO2 title difference is explicitly recorded as a representation
    projection. It does not invalidate publication identity or create an additional
    scientific finding.
  support: supports
  accessed_at: '2026-10-22T01:50:26.351063Z'
  snapshot_sha256: c3ebd3e55e5cbd9d34b399db3e71720d8d18cb743a0abb9c1bf9541557d2189e
- evidence_id: contexts
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/snippet-source-contexts.json
  locator: Whole Abstract, Results lysolipid paragraph 3 and Article title contexts
  summary: All three containing contexts were read. Abstract lexical support does
    not supersede the fuller pathway exceptions, alternative acquisition routes and
    observational design. Five exact node excerpt hashes are bound below without reproducing
    long quotations.
  support: supports
  accessed_at: '2026-10-22T01:50:26.351206Z'
  snapshot_sha256: bd064f29e966e3a5fe274f8cd79372edbc0035bd91ebb39284695ebddfe72025
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/dataset-verification.json
  locator: Direct bounded project, accession, table and code verification
  summary: PRJNA602879 returns26 WGS metagenomic run/sample pairs; all 28 S1 SRS records
    resolve. CG01/WGA and separate2014 FTIR are outside that returned run set, not
    globally absent. Two declared MAG endpoints are derived assemblies. Both named
    GitHub repositories and ggKbase1491 landing identity resolve; no code execution
    or full dynamic annotation review occurred.
  support: supports
  accessed_at: '2026-10-22T01:50:26.351336Z'
  snapshot_sha256: 9ffbc6f2917c2ecc21e13df411cc34bfe3648f8fb31e1ae6481ac90b007b1986
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-13/000252/provenance-audit.json
  locator: Sole history, exact batch27 records[0] and batch91 records[1], cohort and
    current issue scope
  summary: Batch91 is a later direct review that preserved this graph. Current1365
    graph repair is closed; 1366 non-graph follow-up remains open. Both caches remain
    unchanged, with an appended main body despite stale abstract_only MD metadata.
    Historical uninspected-SI statements remain dated facts.
  support: supports
  accessed_at: '2026-10-22T01:50:26.351559Z'
  snapshot_sha256: 41bdbefb33465971c00aac0ef307c0e9fe162cb4d54b20cd287df0825b916923
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/inspect.json
  locator: Thirty-three immutable official inputs
  summary: Target, 21 shared authorities and 11 focal context files are pinned, including
    both direct prior decisions. Discovery included ignored files; generic inventories
    and cross-citation-only caches were not promoted to source reviews.
  support: supports
  accessed_at: '2026-10-22T01:50:26.351713Z'
  snapshot_sha256: 955ce9513b512c4b77e9c437530cd1756e751ed0a46680c86a3e6c1f23a813e9
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/lead-source-assets.json
  locator: Complete main, declared PDF and two workbooks with bounded data reading
  summary: All 70842 main characters, 79 references, Table 1 and five main figures
    were read/viewed. Whole supplementary text and 31references were read; all 12
    supplementary figures and three printed tables were visually inspected. Workbook
    coverage is explicitly bounded rather than claimed as full matrix reanalysis.
  support: supports
  accessed_at: '2026-10-22T01:50:26.351747Z'
  snapshot_sha256: 57040e14a53e27a2c034d24d16172ecbb7956c1a5d9964a541b58d0c35fe868a
- evidence_id: workbooks
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/lead-primary/supplement/workbook-bounded-read.json
  locator: All sheet inventories, four complete small S4 sheets, headers and selected
    S5 annotations
  summary: All nonempty rows of Sampling, Lipid identification FigS3, S4, Core lipid
    concentrations and Core lipid and DIC d13C were read. Fourteen IPL sheet headers
    and the S5 header plus eight selected annotation rows were read. Formatting max_row
    values are not organism counts; reference-similarity labels are not exact sampled
    strains.
  support: supports
  accessed_at: '2026-10-22T01:50:26.351897Z'
  snapshot_sha256: 7e26a939d608ce10dff07a18ce98ce47c505a3dde9f4d7b92e7bcce538539086
- evidence_id: source-sections
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/source-section-projection.json
  locator: Fresh JATS section titles and direct paragraph numbering
  summary: Named primary locators were checked against actual section structure; nested
    figure/table content is preserved in parent paragraphs. The only quotation is
    located in the carbon-fixation Results paragraph 2.
  support: supports
  accessed_at: '2026-10-22T01:50:26.352096Z'
  snapshot_sha256: a09663f57528aa0f595d6e576419686a860dda831d853e426c4ff809ba67d314
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/lead-primary-read-scope.json
  locator: Actual independent lead source and authority read boundaries
  summary: Lead whole main/SI and figure reads plus bounded workbook inspection are
    explicit. Sibling owns full cache/history/current issue and raw registry reads;
    this receipt makes no duplicate complete raw-data review claim.
  support: supports
  accessed_at: '2026-10-22T01:50:26.352287Z'
  snapshot_sha256: 6e8548447fdbff0abc13a72170a09ff5f96400fcbac58dd6c26d46ea7d0ae0df
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/source-audit.json
  locator: Final one-major/two-minor scientific grouping
  summary: Completed scientific review covers current qualitative claims, with source-internal
    conflicts retained as limits. No critical source remains inaccessible. Completion
    is not a clean biological verdict.
  support: supports
  accessed_at: '2026-10-22T01:50:26.352428Z'
  snapshot_sha256: 61ac776ed673c711ae9830e996e0a10917111a0300fc8596825afd4aea19d059
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/root-independent-source-audit.json
  locator: Independent root scientific assessment and precise read scope
  summary: Root independently reviewed the main, figures, supplementary text/tables
    and bounded workbook/source authority context. Its final scientific decision is
    reconciled with the source and support receipts.
  support: supports
  accessed_at: '2026-10-22T01:50:26.352612Z'
  snapshot_sha256: 5128c2a91829c50c8213e6e90ba53eef03665d7cb325327db3254fdea36e4e80
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/support-final-audit.json
  locator: Distinct frozen support and literal metrics
  summary: Completeness75; base131.66666666666669 minus one major and two minor findings
    gives raw117.66666666666669, capped100. Scores do not override biological findings
    or require a culture recipe for field samples.
  support: supports
  accessed_at: '2026-10-22T01:50:26.352772Z'
  snapshot_sha256: 4ace3f7f36325d9e7fc2c0a792c2beee75f4ee1d9491d0a1e94d00bd67d724dc
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/supporting-artifact-manifest.json
  locator: Final immutable supporting artifact manifest
  summary: Final support follows source/authority freeze; preliminary support, prior
    records, source bytes and all 33 maintained inputs remain unchanged.
  support: supports
  accessed_at: '2026-10-22T01:50:26.352806Z'
  snapshot_sha256: 9df362e9c3b30b183b14ccb598942634d323eccdece3466f1d33d2d8a903b0f0
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/auxiliary-frozen-manifest.json
  locator: Final native/authority artifact manifest
  summary: Eight ontology pairs across seventeen placements match; all eight focused
    checks pass. Both unresolved mappings and source-aware semantic boundaries are
    retained.
  support: supports
  accessed_at: '2026-10-22T01:50:26.352939Z'
  snapshot_sha256: 895d9eb68cd305f21de17304432f985a9aaab6210cc29e940d34fe9c2cfa57e3
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/final-validator-summary.json
  locator: Eight actual focused commands and immutable outputs
  summary: All eight executed checks pass. Reference-validator zero issues is not
    an excerpt count or independent proof of claim entailment; Discussion coverage
    remains limited.
  support: supports
  accessed_at: '2026-10-22T01:50:26.353086Z'
  snapshot_sha256: 2a16fc12b6274092dfab0ae60152774d2cd6e770cb33302d5213597ca5121147
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/child-current-corpus-context.json
  locator: Fresh batch13 corpus diagnostics
  summary: Both corpus diagnostics exited1 with 44 warnings across 16 of 477 records
    and zero errors. They are contextual nonrequired checks, distinct from focused
    target validation.
  support: supports
  accessed_at: '2026-10-22T01:50:26.353235Z'
  snapshot_sha256: 1c20a7c8d8d3abf12f4752957070865bb053f8d94ba05f704371c752fd1f3da6
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/adapter-check.json
  locator: Optional adapter availability in the owned runtime
  summary: The optional structured adapter is unavailable. No paid provider, dotenv
    credential lookup or external-checkout execution was used.
  support: supports
  accessed_at: '2026-10-22T01:50:26.353385Z'
  snapshot_sha256: 681262cbec7e7431e9de16418e6651d3819d47d4ab7962326b76aba41f39643c
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/validate.json
  locator: Actual immutable command/stdout/stderr
  summary: Focused native command passed; claim entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T01:50:26.353871Z'
  snapshot_sha256: caba5bae14be40fc6a9091dd424efca8c13ab5ef98ec48054cec9d0ed4174597
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/validate-strict.json
  locator: Actual immutable command/stdout/stderr
  summary: Focused native command passed; claim entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T01:50:26.354069Z'
  snapshot_sha256: 2ff0c974cb49900fb1354211ccbd26051585a0940a845fca3237b181b1f1b041
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/validate-terms.json
  locator: Actual immutable command/stdout/stderr
  summary: Focused native command passed; claim entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T01:50:26.354264Z'
  snapshot_sha256: 8185be1206c6da06f88f6232cff1b7ae3b9fb6a3095a9b9b051842f683e1be50
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/validate-references-explained.json
  locator: Actual immutable command/stdout/stderr
  summary: Focused native command passed; claim entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T01:50:26.354468Z'
  snapshot_sha256: 7535b12a2ade57be8d195f667e3841e47c90ea3b4d224f374efaf7ace88c4f44
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/validate-gtdb.json
  locator: Actual immutable command/stdout/stderr
  summary: Focused native command passed; claim entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T01:50:26.354623Z'
  snapshot_sha256: c8ce53ea2afe04e299b9ff8d6a719c61ba3b756b8c389e2370bcfd137d3c939e
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/validate-gtdb-domain.json
  locator: Actual immutable command/stdout/stderr
  summary: Focused native command passed; claim entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T01:50:26.354787Z'
  snapshot_sha256: 74dfb9e24437d01a33e2f58d39441f0038f869178d9a44685be14d5e25d2bfc3
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/validate-history.json
  locator: Actual immutable command/stdout/stderr
  summary: Focused native command passed; claim entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T01:50:26.354956Z'
  snapshot_sha256: 2f6ea4cc3e452a9912f8c0a20440a3e4308e3729d7854fcace7729da920f348f
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/000252/normalize-cache-names-check.json
  locator: Actual immutable command/stdout/stderr
  summary: Focused native command passed; claim entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T01:50:26.355094Z'
  snapshot_sha256: c5f21bd32b44fd6d3bf735635d7b0ddc41e275712cf8edfe5302b74f4736dce4
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/audit-network.json
  locator: Actual fresh batch13 corpus baseline
  summary: Exit1 with 44 warnings across 16 of 477 records and zero errors; contextual
    scope preserved.
  support: supports
  accessed_at: '2026-10-22T01:50:26.355298Z'
  snapshot_sha256: 6760159390e2e4f424c5084dcfa9e720ec717b7a055f7e6a7561dc71eae0a088
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-13/check-network-quality.json
  locator: Actual fresh batch13 corpus baseline
  summary: Exit1 with 44 warnings across 16 of 477 records and zero errors; contextual
    scope preserved.
  support: supports
  accessed_at: '2026-10-22T01:50:26.355482Z'
  snapshot_sha256: 21ceb139810361c7edb174cfa3d407ef5f8f691278da89c382f6148b904c7e69
assessments:
- assessment_id: identity
  area: identity
  topic: Broad CPR clade and carbon-fixing functional pool
  outcome: supported
  summary: The two descriptors are explicit broad community roles rather than cultured
    species or resolved partners.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - lineage
  - gtdb
  - gtdb-synonym
  - sampling
  details: Retain NCBITaxon1783273 Patescibacteria group and the explicitly CO2-fixing
    bacterial/archaeal pool under131567. Ancestor overlap does not require deletion.
    Source names such as Gallionella, Sulfurimonas and Altiarchaeum provide context,
    not a mandatory roster expansion or exact donor assignment. S5 reference-similarity
    strings do not identify collected culture strains.
- assessment_id: nongraph
  area: evidence
  topic: Role, lipid origin and pressure-adaptation certainty
  outcome: concern
  summary: Several categorical fields are stronger than the measured associations
    and current qualified graph.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - biosynthesis
  - pressure
  - fractions
  - model
  - schema
  details: The optional CPR SYNTROPHIC_PARTNER role is not established merely by putative
    symbiosis or genomic deficits. Preserve the observed pathway deficit while retaining
    near-complete Nealsonbacteria and unknown biosynthesis alternatives. Lipid donation
    remains proposed; scavenging degraded biomass and direct-host acquisition are
    alternatives. Pressure-linked unsaturation is an observational association with
    a proposed explanation, not an experimentally induced response. The description
    already qualifies lipid origin and curvature; target its categorical pressure
    clause rather than falsely calling the entire description unqualified.
- assessment_id: node-0
  area: graph
  topic: Predominantly Autotrophic Carbon Supply
  outcome: supported
  summary: Retain community-scale predominantly autotrophic carbon supply with fractionation
    and heterotrophic-reuse limits; it does not identify a lipid donor.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - carbon
  - snippets
  - contexts
  details: 'Exact selector ecological_interactions[0]; name Predominantly Autotrophic
    Carbon Supply; scope COMMUNITY_LEVEL; interaction_type not asserted. Actual taxa:
    {"source": null, "target": null, "participants": [{"id": "NCBITaxon:131567", "label":
    "cellular organisms"}]}. Canonical evidence bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "794b912fa0d0f412d5d6cd699a73cf323e3888fed01c34e1c2f718e07d70bdef",
    "reference": "PMID:32203118", "supports": "SUPPORT", "evidence_source": "IN_VIVO"}].
    Snippet audit SHA256 963eb2cc02c63aad6b827bd23b6ded0ca89b72e859cfa2a4785e77967550af80.
    PMID32203118 source locator: Results and discussion → In situ carbon fixation
    sustains microbial communities irrespective of aquifer depth, paragraphs1–3, Figure
    2a–b; Model of lipid transfer in the community and conclusions, paragraph 1. Retain
    actual evidence tiers: SUPPORT IN_VIVO. Retain community-scale predominantly autotrophic
    carbon supply with fractionation and heterotrophic-reuse limits; it does not identify
    a lipid donor.'
- assessment_id: edge-0-0
  area: graph
  topic: Predominantly Autotrophic Carbon Supply → Putative CPR Lipid Acquisition
  outcome: supported
  summary: Retain the existing HYPOTHESIZED direction and its uncertainty.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - carbon
  - biosynthesis
  - correlations
  - model
  - snippets
  details: 'Exact selector ecological_interactions[0].downstream[0]; actual direction/participants:
    {"source_node": "Predominantly Autotrophic Carbon Supply", "target_node": "Putative
    CPR Lipid Acquisition", "source_scope": "COMMUNITY_LEVEL", "target_scope": "COMMUNITY_LEVEL",
    "source_taxa": {"source": null, "target": null, "participants": [{"id": "NCBITaxon:131567",
    "label": "cellular organisms"}]}, "target_taxa": {"source": null, "target": null,
    "participants": [{"id": "NCBITaxon:1783273", "label": "Patescibacteria group"},
    {"id": "NCBITaxon:131567", "label": "cellular organisms"}]}}. Current arrow description:
    HYPOTHESIZED - autotrophically fixed carbon can supply bacterial lipid production
    and the community material available for CPR acquisition. The isotope, lipid and
    genomic observations support this proposed carbon route but do not trace transfer
    from a particular producer to CPR cells.. Retain HYPOTHESIZED. PMID32203118 Results
    and discussion → In situ carbon fixation sustains microbial communities irrespective
    of aquifer depth, paragraphs1–3, Figure 2a–b; Model of lipid transfer in the community
    and conclusions, paragraph 1, and Results and discussion → Lysolipids and Candidate
    Phyla Radiation bacteria, paragraph 3; Predicting linkage of IPLs to uncultivated
    organisms, paragraphs1–4; Model of lipid transfer in the community and conclusions,
    paragraph 2/Figure 5. No separate edge-local excerpt exists; source-node exact
    excerpt bindings and these paragraphs define support. Community fixed carbon could
    supply material for CPR acquisition, but producer-resolved transfer is not traced.'
- assessment_id: node-1
  area: graph
  topic: Putative CPR Lipid Acquisition
  outcome: supported
  summary: Retain proposed acquisition of lipids or precursors with unresolved donors,
    scavenging and unknown-biosynthesis alternatives; no measured directed flux.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - biosynthesis
  - correlations
  - model
  - snippets
  - contexts
  details: 'Exact selector ecological_interactions[1]; name Putative CPR Lipid Acquisition;
    scope COMMUNITY_LEVEL; interaction_type CROSS_FEEDING. Actual taxa: {"source":
    null, "target": null, "participants": [{"id": "NCBITaxon:1783273", "label": "Patescibacteria
    group"}, {"id": "NCBITaxon:131567", "label": "cellular organisms"}]}. Canonical
    evidence bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "e4890a6eb1a599d27be5fd1240288fae1f200f208c0586379b5dfd79eb3f9add",
    "reference": "PMID:32203118", "supports": "PARTIAL", "evidence_source": "IN_VIVO"},
    {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "9330f3aa5d699822b8cbf89a50f3282114b701a34760f3a8f8dd234da80885cb",
    "reference": "PMID:32203118", "supports": "PARTIAL", "evidence_source": "IN_VIVO"},
    {"selector": "ecological_interactions[1].evidence[2].snippet", "sha256": "aa0baeca6e4e0b80c7366096bef1ee67730d300b78af7d57140836e7b7aafcdc",
    "reference": "PMID:32203118", "supports": "PARTIAL", "evidence_source": "OTHER"}].
    Snippet audit SHA256 963eb2cc02c63aad6b827bd23b6ded0ca89b72e859cfa2a4785e77967550af80.
    PMID32203118 source locator: Results and discussion → Lysolipids and Candidate
    Phyla Radiation bacteria, paragraph 3; Predicting linkage of IPLs to uncultivated
    organisms, paragraphs1–4; Model of lipid transfer in the community and conclusions,
    paragraph 2/Figure 5. Retain actual evidence tiers: PARTIAL IN_VIVO, PARTIAL IN_VIVO,
    PARTIAL OTHER. Retain proposed acquisition of lipids or precursors with unresolved
    donors, scavenging and unknown-biosynthesis alternatives; no measured directed
    flux.'
- assessment_id: edge-1-0
  area: graph
  topic: Putative CPR Lipid Acquisition → CPR-Associated Lysolipids and Proposed Curvature
    Adaptation
  outcome: supported
  summary: Retain the existing HYPOTHESIZED direction and its uncertainty.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - biosynthesis
  - correlations
  - model
  - fractions
  - snippets
  details: 'Exact selector ecological_interactions[1].downstream[0]; actual direction/participants:
    {"source_node": "Putative CPR Lipid Acquisition", "target_node": "CPR-Associated
    Lysolipids and Proposed Curvature Adaptation", "source_scope": "COMMUNITY_LEVEL",
    "target_scope": "COMMUNITY_LEVEL", "source_taxa": {"source": null, "target": null,
    "participants": [{"id": "NCBITaxon:1783273", "label": "Patescibacteria group"},
    {"id": "NCBITaxon:131567", "label": "cellular organisms"}]}, "target_taxa": {"source":
    null, "target": null, "participants": [{"id": "NCBITaxon:1783273", "label": "Patescibacteria
    group"}]}}. Current arrow description: HYPOTHESIZED - acquired community lipids
    or precursors could provide material for CPR-associated lysolipid membranes and
    their proposed curvature adaptation. Lipid correlations and mixed-fraction spectroscopy
    do not demonstrate that acquisition causes lysolipid enrichment or that enrichment
    improves curvature tolerance.. Retain HYPOTHESIZED. PMID32203118 Results and discussion
    → Lysolipids and Candidate Phyla Radiation bacteria, paragraph 3; Predicting linkage
    of IPLs to uncultivated organisms, paragraphs1–4; Model of lipid transfer in the
    community and conclusions, paragraph 2/Figure 5, and Results and discussion →
    Lysolipids and Candidate Phyla Radiation bacteria, paragraphs1–3; Figure 4; Supplementary
    FiguresS10–S12 and separate2014 sample in TableS1. No separate edge-local excerpt
    exists; source-node exact excerpt bindings and these paragraphs define support.
    Proposed acquisition could supply lysolipids, but uptake-to-curvature benefit
    and causal membrane fitness remain unresolved.'
- assessment_id: node-2
  area: graph
  topic: CPR-Associated Lysolipids and Proposed Curvature Adaptation
  outcome: supported
  summary: Retain CPR-associated lysolipids in mixed enriched fractions and proposed
    curvature benefit; no pure-isolate or membrane-mechanical fitness assay.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - fractions
  - biosynthesis
  - model
  - snippets
  - contexts
  details: 'Exact selector ecological_interactions[2]; name CPR-Associated Lysolipids
    and Proposed Curvature Adaptation; scope COMMUNITY_LEVEL; interaction_type not
    asserted. Actual taxa: {"source": null, "target": null, "participants": [{"id":
    "NCBITaxon:1783273", "label": "Patescibacteria group"}]}. Canonical evidence bindings:
    [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "d8ee2375479dcfdea7375e97ee97f1c2178905f0237631066c56dab5139e87ac",
    "reference": "PMID:32203118", "supports": "PARTIAL", "evidence_source": "IN_VIVO"}].
    Snippet audit SHA256 963eb2cc02c63aad6b827bd23b6ded0ca89b72e859cfa2a4785e77967550af80.
    PMID32203118 source locator: Results and discussion → Lysolipids and Candidate
    Phyla Radiation bacteria, paragraphs1–3; Figure 4; Supplementary FiguresS10–S12
    and separate2014 sample in TableS1. Retain actual evidence tiers: PARTIAL IN_VIVO.
    Retain CPR-associated lysolipids in mixed enriched fractions and proposed curvature
    benefit; no pure-isolate or membrane-mechanical fitness assay.'
- assessment_id: state
  area: identity
  topic: Natural origin versus equilibrium state
  outcome: concern
  summary: NATURAL is supported; optional STABLE is not established by one cyclic
    sampling trajectory.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - sampling
  - schema
  details: The final sample near the beginning of an ordination trajectory supports
    restoration of a sampled assemblage. The study documents pronounced phase-dependent
    community changes, not stable equilibrium. Remove unsupported optional STABLE
    or attach actual equilibrium evidence; do not automatically substitute TRANSIENT
    or PERTURBED.
- assessment_id: environment
  area: completeness
  topic: Field environment and absence of cultivation
  outcome: supported
  summary: Groundwater, CO2-rich aquifer context and natural sampling are appropriate;
    empty growth_media is not a defect.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - sampling
  - carbon
  - ontology
  - schema
  details: Sampling spans recovery/intermediate, minor/deep and major/shallow sources.
    Measured conduit pressure, temperature and conductivity, together with cited pH,
    are not controlled growth conditions or direct depth-pressure manipulation. No
    vessel, incubation, nutrient recipe or operating mode should be invented from
    filters, cold storage, chromatography temperature or the approximately five-day
    field cycle.
- assessment_id: grounding
  area: grounding
  topic: Ontology meaning and unresolved taxonomic mappings
  outcome: supported
  summary: Eight ID-label pairs match and both current UNRESOLVED statuses remain
    justified.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - ontology
  - lineage
  - gtdb
  - gtdb-synonym
  - semantics
  details: Broad lipid/fatty-acid classes and carbon-fixation/lipid-metabolism GO
    terms fit the declared context without identifying exchanged molecules. The source
    differentiates DIC, bicarbonate and CO2; the CO2 term need not encode every inorganic-carbon
    species. No forced species, phylum, single GTDB domain or new functional-role
    assignment is warranted.
- assessment_id: resources
  area: completeness
  topic: Source-declared data and code traceability
  outcome: concern
  summary: Verified declared resources are not represented by the two publication-only
    external links.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - deposition
  - resources
  - workbooks
  details: Add bounded project and source-specific resource links, distinguishing
    derived MAG submissions from raw-read samples, supplementary tables and code.
    Preserve differing sample layers and any unavailable public endpoint. No analysis
    software citation is automatically a focal deposit and no source accession range
    establishes exact run counts by arithmetic alone.
- assessment_id: excerpt-provenance
  area: evidence
  topic: Strict snippets and title representation
  outcome: supported
  summary: Twelve fresh strict matches plus one explicit title projection; all thirteen
    match selected cache.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - snippets
  - title-projection
  - contexts
  - provenance
  details: The title CO(2)/CO2 difference is representational. The Results-level author
    interpretation matches fresh XML and full MD but is absent from the short TXT.
    Native success is not a thirteen-strict-fresh-match certificate. The MD has appended
    main despite abstract_only metadata; preserve original cache bytes and document
    the distinction, without a separate scored finding.
- assessment_id: prior-scope
  area: ownership
  topic: Both prior reviews and current follow-up
  outcome: supported
  summary: Batch27 and later direct batch91 preserve the existing qualified graph;
    new science scope does not rewrite their history.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - provenance
  - inspection
  details: Both exact prior rows and current issue contexts are bound. Prior1365 graph
    repair is closed, 1366 metadata follow-up remains open. Shared1744/596/746/524
    do not automatically become focal defects or close from this review. Earlier dated
    uninspected-source statements remain accurate at their original dates; a new follow-up
    can record present full access.
- assessment_id: source-access
  area: scope
  topic: Main and supplementary material with bounded workbook inspection
  outcome: supported
  summary: Available critical material supports completed scientific review of the
    current qualitative claims.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - assets
  - workbooks
  - lead-read
  - source-sections
  - source-scope
  - root-source
  details: Whole main and supplementary text, all 5main/12SIfigures and three printed
    supplementary tables were inspected. Four small workbook sheets were read completely;
    remaining headers and selected reference-annotation rows were read. No complete
    raw lipid matrix or raw sequencing reanalysis is claimed. Source-internal phase,
    sample-label, count and volume discrepancies are retained as limits rather than
    imported as record errors.
- assessment_id: native
  area: schema
  topic: Focused checks and contextual diagnostics
  outcome: supported
  summary: Eight focused native checks pass; nonrequired corpus failures and adapter
    unavailability remain explicit.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - final-native
  - auxiliary
  - snippets
  - corpus-context
  - adapter
  details: No native failure is inferred from the title projection or scientific overclaims.
    Reference validation has known Discussion-coverage limits and cannot certify mechanistic
    entailment.
- assessment_id: metrics
  area: completeness
  topic: Literal metrics
  outcome: supported
  summary: Completeness75; raw quality117.66666666666669, capped100.
  target_ids:
  - CommunityMech:000252
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: Required/roles50+environment5+three nodes10+external5+metabolites5=75.
      Two environmental factors earn no threshold bonus; empty field growth_media
      and datasets earn no points but do not automatically create defects.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100−1×10major−2×2minor+20×min(((5/3)/2),1)+15COMPLETE=117.66666666666669
      raw, capped100. Three nodes, one typed, two arrows and five node evidence. Scientific
      concerns remain.
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
- finding_id: non-graph-scope
  issue_key: cm-000252-non-graph-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: This changes the asserted biological mechanism and certainty;
    related role/prose manifestations are grouped once. No separate graph defect or
    obligatory-product-removal requirement is invented.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Align role and mechanism prose with source uncertainty
  description: The hard CPR SYNTROPHIC_PARTNER role and categorical lipid-origin/pressure-adaptation
    fields overstate hypotheses that the existing graph already qualifies. Known-pathway
    deficits, mixed-fraction observations and depth associations do not resolve a
    syntrophic partner exchange, universal synthesis inability or induced pressure
    response.
  target_ids:
  - CommunityMech:000252
  field_paths:
  - description
  - taxonomy[0].functional_role
  - taxonomy[0].taxon_term.notes
  - taxonomy[1].taxon_term.notes
  - related_ingredients[1].relevance
  - related_ingredients[1].evidence[0].explanation
  - related_ingredients[2].relevance
  - related_ingredients[2].evidence[0].explanation
  evidence_ids:
  - biosynthesis
  - fractions
  - pressure
  - model
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
    role: canonical_record
  ownership_note: The focal record owns these changes. Preserve current1366 non-graph
    follow-up and closed1365 graph scope; no automatic issue closure, cache mutation
    or cross-record edit.
- finding_id: state-scope
  issue_key: cm-000252-state-scope
  category: identity
  severity: minor
  native_severity: P3
  normalization_reason: A bounded metadata claim can be omitted without changing natural
    origin, community membership or the supported graph; no replacement state is imposed.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Support or omit the equilibrium-state assertion
  description: The optional STABLE value asserts equilibrium. Observed phase-dependent
    turnover and cyclic return near an initial sample do not establish that state.
  target_ids:
  - CommunityMech:000252
  field_paths:
  - ecological_state
  evidence_ids:
  - sampling
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
    role: canonical_record
  ownership_note: The focal record owns these changes. Preserve current1366 non-graph
    follow-up and closed1365 graph scope; no automatic issue closure, cache mutation
    or cross-record edit.
- finding_id: resources
  issue_key: cm-000252-resources
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: A specific recoverable traceability gap is supported by source
    declarations and direct metadata; an empty optional list alone is not the finding.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Add declared data and code traceability with exact scopes
  description: The current external links identify only the publication. The source
    supplies project, derived-genome, raw-sample, supplementary-table and code resources
    that can be represented with verified scope.
  target_ids:
  - CommunityMech:000252
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - deposition
  - resources
  - workbooks
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
    role: canonical_record
  ownership_note: The focal record owns these changes. Preserve current1366 non-graph
    follow-up and closed1365 graph scope; no automatic issue closure, cache mutation
    or cross-record edit.
actions:
- action_id: qualify-nongraph
  description: Align non-graph statements with the source-supported hypotheses.
  finding_ids:
  - non-graph-scope
  target_ids:
  - CommunityMech:000252
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Retain positive isotope/genomic support for predominantly autotrophic carbon supply
    and PRIMARY_PRODUCER. Qualify the hard CPR SYNTROPHIC_PARTNER role or omit it
    unless claim-local evidence establishes syntrophic metabolism; do not force another
    role, named donor, obligacy, reciprocal growth or product-removal requirement.
  - Represent absence of known complete pathways in the analyzed CPR genomes without
    a universal inability claim. Preserve near-complete Nealsonbacteria pathways and
    possible ACP-independent/unknown synthesis, plus degraded-biomass scavenging and
    direct-host acquisition alternatives.
  - Qualify taxonomy[1].taxon_term.notes and related_ingredients[1] donor-origin wording
    as a proposed contribution; preserve the broad bacterial/archaeal carbon-fixing
    pool without treating all of it as demonstrated CPR lipid donors. Figure 5 bacterial-to-CPR
    and archaeal/DPANN contexts remain distinct.
  - Qualify the categorical pressure clause in description and related_ingredients[2]
    as a depth-associated profile interpreted as possible pressure adaptation. Do
    not claim a controlled pressure response, an exact producing taxon, exclusively
    double bonds or a tested curvature/fitness benefit.
  - Retain three nodes and both HYPOTHESIZED arrows with actual directions, participants
    and current evidence tiers. Preserve mixed2015 lipid fraction versus separate2014
    FTIR sample; no pure-CPR isolation or mandatory graph expansion.
- action_id: repair-state
  description: Remove unsupported equilibrium certainty without inventing a substitute.
  finding_ids:
  - state-scope
  target_ids:
  - CommunityMech:000252
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Support ecological_state STABLE with actual equilibrium evidence, or omit this
    optional field. NATURAL origin and recurring geyser behavior alone are insufficient.
  - Retain observed phase-dependent community shifts and final-sample restoration
    as the reported findings. Do not automatically substitute TRANSIENT or PERTURBED;
    do not treat the five-day sampling cycle as an incubation period.
- action_id: add-resources
  description: Represent verified source-linked data and code with bounded provenance.
  finding_ids:
  - resources
  target_ids:
  - CommunityMech:000252
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Add PRJNA602879 and the source SAMN13287258–SAMN13287462 derived-genome context.
    The two verified endpoint BioSamples explicitly derive from community samples;
    the interior range was not exhaustively verified. Preserve the separate paper206
    new genomes, 205 inclusive accession numbers and current201 linked assemblies;
    do not equate these denominators.
  - Keep all 28 resolved TableS1 SRS identities separate from newly deposited MAGs:27
    cycle samples plus the separate2014 FTIR sample. The exact umbrella query returns26
    WGS METAGENOMIC libraries, mapping CG02–CG26B. CG01/WGA SAMN07631059 and 2014
    SAMN07960332 are outside this returned set; no global SRA/ENA absence is inferred.
  - Link source TablesS4–S5 as supplied workbooks, with sample-label/date discrepancies
    explicit if those details are used. S5 reference-similarity annotations must not
    become exact collected-strain identities.
  - Link https://ggkbase.berkeley.edu/genome_summaries/1491-Bacterial_membrane_lipids_AJP
    as a verified named landing page without claiming all 675 dynamic annotation rows
    were inspected. Link https://github.com/AJProbst/lip_metgen and https://github.com/AJProbst/rpS3_trckr
    as verified source-specific analysis repositories; metadata verification is not
    code execution. Generic analysis tools are not study deposits.
- action_id: validate-future-curation
  description: Validate separately authorized repairs and preserve the review chain.
  finding_ids:
  - non-graph-scope
  - state-scope
  - resources
  target_ids:
  - CommunityMech:000252
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Crystal_Geyser_CO2_Aquifer_CPR_Lipid_Community.yaml
    role: canonical_record
  acceptance_checks:
  - After authorized curation, attach exact source-local evidence, update history
    and run schema, strict, terms, explained references, GTDB, domain and history
    checks, then just gen-html and just check-docs-current. This review does not modify
    canonical, cache, history or generated files.
  - Preserve both prior-review records, current source/asset and support receipts,
    all source-internal discrepancies and the explicit title representation projection.
    No paid retrieval, contact, automatic issue closure or full raw-data reanalysis
    is implied.
limitations:
- The source Figure 2c caption calls major eruptions deep, whereas main text, Figure
  1 and S1 identify minor/deep and major/shallow. This internal conflict is retained
  rather than silently harmonized.
- The2015post-0.2µm lipid fraction is mixed and has abundant Sulfurimonas; the separate2014
  FTIR sample is CPR-enriched. Neither establishes isolated-cell lipid percentages,
  exact donors or membrane-mechanical fitness.
- Genomic deficits concern known pathways; unknown/ACP-independent synthesis remains
  possible. Lipid scavenging and direct-host acquisition are alternatives. Isotope
  mass-balance estimates depend on fractionation and permit heterotrophic reuse.
- Source TableS2 maximum388L differs from main338L; TableS3 DOC wording/dates and
  FigureS8 protein/cluster counts are internally inconsistent. No current encoded
  numeric claim is corrected from these unencoded conflicts.
- S4 sample dates/phase labels and CG29/CG12 sheet labels differ from PDF summaries.
  Selected S5 annotations are reference similarities, not exact collected strains;
  complete raw matrices and raw sequence libraries were not independently reanalysed.
- Twelve snippets strictly match fresh XML; the title has an explicit CO(2)/CO2 representation
  projection. All thirteen match selected cache; the full Results sentence is absent
  from the short TXT cache. The full MD append coexists with stale abstract_only metadata.
- Registry, raw-sample, derived-genome, code and supplementary-table scopes remain
  distinct. No global absence statement or unverified accession-to-experiment assignment
  is inferred from a bounded query.
notes:
- Three exact node assessments bind all five canonical excerpt hashes; both HYPOTHESIZED
  arrows bind actual directions and participants. No long canonical source excerpts
  are copied.
- The only two-word quotation is predominantly autotrophic, directly from Results
  and discussion → In situ carbon fixation sustains microbial communities irrespective
  of aquifer depth, paragraph 2.
- All 33 official inputs remain unchanged. Both direct prior-review contexts, batch27
  and batch91, are retained; root alone saves after independent acceptance.
- Focused native 8passes, actual nonrequired corpus failures and unavailable optional
  adapter are explicitly represented. No new candidate-validation failure is assumed
  from a scientific finding.
tags:
- record-review
- groundwater
- cpr
- lipid-metabolism
- batch-13
```
