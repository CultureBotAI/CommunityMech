# Diclofenac activated-sludge consortium record review

- Review: 20261022T065743Z-diclofenac-consortium-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T06:44:11.062763Z
- Finished UTC: 2026-10-22T06:57:43.124423Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The source supports the enrichment, parent-DCF loss and qualified before/after community observations. Two major findings correct MC product attribution and a combined-genus classifier narrowed to Burkholderia; two minor findings address the basal MSM recipe and GTDB completion/provenance. All eight required native checks passed. Literal completeness is 30 and quality is capped at 100 (raw 111).

## Scope And Provenance

Whole released target and encoded claims using complete fresh primary text, all six main figures, three SI pages, all non-sequence S4–S6 cells, bounded archive/authority metadata and actual native checks.

Selection: Only released CommunityMech:000379 in owned batch16.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb7a782c8ba80299dca8761ad0a2c90bccd8a117.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000379 | kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml | maintained | Diclofenac Activated Sludge Microbial Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000379 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000379 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000379 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000379 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000379 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000379 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000379 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000379 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000379 | Actual corpus exit 1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000379 | Actual corpus exit 1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000379 | Unavailable in the owned runtime. |

## Scientific And Domain Assessments

### Focal enrichment and partial roster

identity: supported. Targets: CommunityMech:000379.

The record denotes the correct sludge-derived enrichment; narrow genus resolution requires repair.

ENGINEERED origin/state and BIOREMEDIATION are supported. Ten curated descriptors are a partial roster, not ten isolated strains. Main and SI distinguish MC from CSWD.1/CSWD.2 comparison arms.

### Consortium-specific transformation products

evidence: concern. Targets: CommunityMech:000379.

The opening description transfers isolate-only 5-OH-DCF detection to MC.

Node 0 already states the correct non-detection and tentative nitro-product limits. Correct the summary consistently; retain observed parent removal and mixture toxicity without claiming mineralization, detoxification or metabolite-specific causal toxicity.

### Glucose-Amended Diclofenac Dissipation by MC

graph: concern. Targets: CommunityMech:000379.

Retain the qualified community-level parent-loss observation; qualify the first participant.

Exact selector ecological_interactions[0]; scope COMMUNITY_LEVEL; no interaction_type, source_taxon or target_taxon is asserted. Exact participants: [{"preferred_term": "Burkholderia", "term": {"id": "NCBITaxon:32008", "label": "Burkholderia"}}, {"preferred_term": "Klebsiella", "term": {"id": "NCBITaxon:570", "label": "Klebsiella"}}, {"preferred_term": "Ochrobactrum", "term": {"id": "NCBITaxon:528", "label": "Ochrobactrum"}}, {"preferred_term": "Chthoniobacter", "term": {"id": "NCBITaxon:295577", "label": "Chthoniobacter"}}, {"preferred_term": "Parachlamydia", "term": {"id": "NCBITaxon:83551", "label": "Parachlamydia"}}, {"preferred_term": "Talaromyces", "term": {"id": "NCBITaxon:5094", "label": "Talaromyces"}}, {"preferred_term": "Aspergillus", "term": {"id": "NCBITaxon:5052", "label": "Aspergillus"}}, {"preferred_term": "Debaryomycetaceae", "term": {"id": "NCBITaxon:766764", "label": "Debaryomycetaceae"}}, {"preferred_term": "Malassezia", "term": {"id": "NCBITaxon:55193", "label": "Malassezia"}}, {"preferred_term": "Cladosporium", "term": {"id": "NCBITaxon:5498", "label": "Cladosporium"}}]. Exact canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "a8910e421cb2d429dbb1d68c728868342236732bc53f72d20d0af1b65e1be1b3", "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}, {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "ee4c80f9c44b0510e68dd8fa191071dedf338483995c5d56e3fc8a1cbd361b66", "reference": "PMID:41718267", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}]. PMID:41718267 source locators: Methods 2.2.4 paragraphs 1–2; Results 3.3 paragraph 7; Figures 3–4, Tables 3–4; Results 3.4 paragraphs 3–4. SUPPORT for MC disappearance is sound. The pooled Abstract metabolite excerpt is correctly PARTIAL. GO xenobiotic/glucose processes are community assay context, not individual flux. Parent loss is distinct from mineralization and detoxification.

### DCF-Selected Community Shift

graph: concern. Targets: CommunityMech:000379.

Retain the bounded before/after profile observation; reconcile the combined genus label.

Exact selector ecological_interactions[1]; scope COMMUNITY_LEVEL; no interaction_type, source_taxon or target_taxon is asserted. Exact participants: [{"preferred_term": "Burkholderia", "term": {"id": "NCBITaxon:32008", "label": "Burkholderia"}}, {"preferred_term": "Klebsiella", "term": {"id": "NCBITaxon:570", "label": "Klebsiella"}}, {"preferred_term": "Ochrobactrum", "term": {"id": "NCBITaxon:528", "label": "Ochrobactrum"}}, {"preferred_term": "Chthoniobacter", "term": {"id": "NCBITaxon:295577", "label": "Chthoniobacter"}}, {"preferred_term": "Parachlamydia", "term": {"id": "NCBITaxon:83551", "label": "Parachlamydia"}}, {"preferred_term": "Talaromyces", "term": {"id": "NCBITaxon:5094", "label": "Talaromyces"}}, {"preferred_term": "Aspergillus", "term": {"id": "NCBITaxon:5052", "label": "Aspergillus"}}, {"preferred_term": "Debaryomycetaceae", "term": {"id": "NCBITaxon:766764", "label": "Debaryomycetaceae"}}, {"preferred_term": "Malassezia", "term": {"id": "NCBITaxon:55193", "label": "Malassezia"}}, {"preferred_term": "Cladosporium", "term": {"id": "NCBITaxon:5498", "label": "Cladosporium"}}]. Exact canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "de326593817836b0b34534b4825577a8a5483711aef130f2b416828780122b2e", "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "72cd1badd8cb706081d3682842670ee49fa50cfe0ed6e69bf5eb9b3a1cac3022", "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[1].evidence[2].snippet", "sha256": "b72681c33e1e09abda98d61def26017b4493721bc2a589accb33a65956acdc27", "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[1].evidence[3].snippet", "sha256": "7f29d1c03e72ba2c3fb88441463ef6fecf7e2c8067e21cf93a49dce0dd2392b0", "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[1].evidence[4].snippet", "sha256": "967aa86847f0ad45f5a1794f35d135b3d29b7af2f892f8ad84d9261c03d9a8d7", "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[1].evidence[5].snippet", "sha256": "1224bbb9a517b2b30462567f9b6052e039ca2dbf4e40303561ce1ccdbd6f1452", "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[1].evidence[6].snippet", "sha256": "2336f23d2a647ebedfb01548476f489a7b2a09a42fdf2f4c73f227129022bdfd", "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}]. PMID:41718267 source locators: Methods 2.2.7 sole paragraph; Results 3.5 paragraphs 3–4, 10 and 12; Figures 5–6; Tables S4–S6. Measured DNA followed by computational assignment supports relative profiles. It does not establish absolute growth, DCF-only causation, niche partitioning or member degradation. Preserve the author-reported bacterial and fungal percentages with distinct denominators; S5 pooled columns cannot validate the individual endpoints. The first participant and Burkholderia summary need the combined-classifier qualification.

### No downstream arrows

graph: supported. Targets: CommunityMech:000379.

Retain the two observations with zero downstream arrows.

No arrow assessment is omitted: both current downstream arrays are absent. Sampling the same cultures does not establish a directed ecological mechanism. The classifier finding concerns participant grounding, not graph connectivity.

### MSM formulation and assay stages

evidence: concern. Targets: CommunityMech:000379.

Current assay settings are supported; the structured medium omits the basal MSM recipe.

Methods 2.1 specifies twelve basal components. Recover the source formulation and separately document LB revival/washing if expanded. The source iron entry joins FeSO4 and 7 H2O awkwardly; retain that uncertainty rather than silently certify a hydrate. The SI 100 mL LB/125 rpm isolate growth curve is not the MC degradation protocol.

### Taxon resolution and GTDB provenance

grounding: concern. Targets: CommunityMech:000379.

Valid ID/label pairs do not resolve a combined assay classifier to one genus.

S5 contains 31 ASVs labelled Burkholderia-Caballeronia-Paraburkholderia. Current NCBI identifies three distinct sibling genera. Do not infer that all three occur separately or select another genus without evidence. Burkholderia 8896/8908 and Klebsiella 44527/44529 GTDB cores reproduce, but the former applies only to the narrower named taxon. Chthoniobacter maps 2/2 and Parachlamydia 13/13; Ochrobactrum has three genus candidates. Five fungal NO_GTDB_EQUIVALENT statuses are appropriate. Local mtime establishes neither latest release nor build date.

### Verified marker-specific archive

representation: supported. Targets: CommunityMech:000379.

Both encoded PRJEB98466 marker resources match the source and six sample records.

All six S4 aliases/accessions map to bacterial/fungal initial/final samples plus two negative sequencing controls. ENA reports paired Illumina MiSeq amplicon/PCR libraries. No raw FASTQ or new statistical analysis was needed; no resource omission is graded.

### Complete main and bounded supplement analysis

scope: supported. Targets: CommunityMech:000379.

The full article, six main figures and all declared supplement objects were inspected.

The lead read all 124,031 projected article characters and 129 references, the three-page SI PDF and all non-sequence S4/S5/S6 cells. Sequence column L was excluded except initial exemplars. Stale workbook dimensions and missing drawing references were handled with preserved read-only extraction corrections. Root independently read scientific main sections, all figure pixels and non-sequence SI cells; no claim that every reviewer read the bibliography or raw sequences.

### Maintained inputs and historical review scope

ownership: supported. Targets: CommunityMech:000379.

Future repairs belong to the maintained community YAML under separate curation authorization.

All 35 official inputs remain unchanged. The exact prior batch33 row repaired the graph while preserving non-graph metadata; cohort completeness 77 is a different proportional metric. Closed issue 1405 had a withdrawn ingredient premise and is not reused as proof of the present description finding. No history, issue, cache or Git changes are made.

### Actual native validation

schema: supported. Targets: CommunityMech:000379.

All eight required native checks passed.

Native label/reference/network success does not establish taxonomic resolution or causal support. The two-node network has zero reported structural issues.

### Literal native metrics

completeness: supported. Targets: CommunityMech:000379.

Completeness 30; raw quality 111, capped 100.

## Findings

### product-scope: Correct the MC product summary

major / open / confirmed; issue key: cm-000379-product-scope.

The description assigns 5-OH-DCF formation to MC although Results and Figure 4 explicitly report non-detection in MC. The Abstract pools separate isolate and consortium assays.

### classifier-resolution: Preserve the combined classifier resolution

major / open / confirmed; issue key: cm-000379-classifier-resolution.

The S5 group spans three distinct genera, so NCBITaxon:32008 alone is narrower than the assay assignment. Main shorthand and valid name mappings do not resolve the sample.

### medium-completeness: Recover the source basal MSM formulation

minor / open / confirmed; issue key: cm-000379-medium-completeness.

The current composition contains the two supplements but omits the twelve basal constituents specified in Methods 2.1.

### gtdb-provenance: Complete bounded genus mappings and snapshot provenance

minor / open / confirmed; issue key: cm-000379-gtdb-provenance.

Current genus crosswalks resolve two UNRESOLVED entries and expose three Ochrobactrum candidates. Existing numerical cores reproduce, but latest/build wording is not established by filesystem mtime.

## Recommended Actions And Acceptance Checks

### repair-products

Align the summary with MC-specific observations.

- State no detected 5-OH-DCF in MC while retaining 4′-OH-DCF and tentative TP339/NO2-DCF. Attribute 5-OH detection to the separate isolate arms.
- Preserve node 0 qualifications, parent disappearance versus mineralization, and endpoint mixture toxicity without assigning toxicity to one identified metabolite.

### repair-classifier

Represent the combined assay label consistently before selecting narrower taxon grounding.

- Record the S5 Burkholderia-Caballeronia-Paraburkholderia resolution and explain the main text/Figure 5 shorthand. Reconcile taxonomy[0], both first participant copies, description, taxon notes and abundance wording together.
- Do not arbitrarily replace Burkholderia with a sister genus, assert all three independently occur, or force the entire family as an exact identity. Use a supported unresolved representation or source-supported reanalysis before narrowing.
- Retain author-reported 26.9% and 88.9% only with their source and classifier qualification. Do not derive endpoints from pooled S5 RA or treat valid reference GTDB mapping as sample classification.
- Retain both community observations, zero arrows and partial roster; do not assign individual degrader roles from amplicon abundance.

### repair-medium

Add the source recipe while preserving assay stages.

- Recover the twelve basal solutes from Methods 2.1 with exact concentrations/forms; verify source FeSO4/7 H2O typography rather than invent a hydrate or separate water dose. A deliberately partial formulation must be explicit.
- Keep the supported 50 mL/250 mL, 30 °C, 180 rpm, aerobic, 28-day assay and initial pH. If documenting revival, separate 24-hour LB preparation and MSM washes from the degradation medium.
- Do not import the SI isolate growth curve, IC50 broth assay or generic medium recipe into MC conditions. Attach an exact Methods excerpt to added details.

### repair-gtdb

Use verified genus routes and honest local provenance.

- Add current Chthoniobacter GTDB:g__Chthoniobacter (2/2) and Parachlamydia GTDB:g__Parachlamydia (13/13) mappings with full lineage and method.
- Represent Ochrobactrum as AMBIGUOUS with the three genus candidates Ochrobactrum_A, Ochrobactrum_B and Ochrobactrum; do not promote its isolated exact-ID row to a species assignment.
- Replace unsupported latest/build assertions with actual snapshot hash and method. Keep all fungal NO_GTDB_EQUIVALENT statuses. Re-ground any changed first participant only after the separate sample-resolution repair.

### validate-curation

Validate separately authorized future changes.

- Run focused schema, strict, term, reference, GTDB and history checks after actual edits, plus applicable generated-document gates. Preserve original caches/history and existing graph qualifications. Root alone saves this review and runs post-save gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml; Whole maintained YAML | supports | Sludge-derived enrichment with a partial genus/family roster, two community-level nodes and no arrows. |
| abstract | PMID:41718267; DOI:10.3390/jox16010024; Fresh MED resultList.result[0], complete Abstract and bibliographic identity | supports | The Abstract pools consortium and separate isolate outcomes; five canonical excerpts use this rendered representation. |
| identity | PMID:41718267; DOI:10.3390/jox16010024; Methods 2.1 Material, paragraph 2; 2.2.1 Enrichment and Isolation of DCF-Degrading Consortium and DCF-Degrading Strains, all three paragraphs; Results 3.1, all five paragraphs | supports | The focal MC is a glucose-enriched activated-sludge consortium from Seville. CSWD.1 and CSWD.2 are separate isolate comparisons. |
| medium-definition | PMID:41718267; DOI:10.3390/jox16010024; Methods 2.1 Material, first direct paragraph | supports | Twelve basal MSM constituents are specified per liter, in addition to assay glucose and DCF. Iron-hydrate typography requires qualification. |
| cultivation | PMID:41718267; DOI:10.3390/jox16010024; Methods 2.2.4 DCF Biodegradation Test in Solution, first direct paragraph (quoted words here), and second paragraph for revival; XPath //*[@id="sec2dot2dot4-jox-16-00024"]/p[1] | supports | The MC assay uses 50 mL MSM in 250 mL flasks, 3 g/L glucose, 10 mg/L DCF sodium, initial OD600 about 1, 30 °C and 180 rpm. LB revival is a separate stage. |
| performance | PMID:41718267; DOI:10.3390/jox16010024; Results 3.3 Diclofenac Biodegradation in Solution, seventh direct paragraph; Figure 3 and Table 3 | supports | MC removes parent DCF within five days. It retains 4′-OH-DCF and tentative TP339, with no detected 5-OH-DCF. |
| products | PMID:41718267; DOI:10.3390/jox16010024; Results 3.3 paragraph 7 and 3.4 Ecotoxicity Studies in Diclofenac-Contaminated Aqueous Samples, paragraph 4; Figure 4 bottom MC panels | supports | The explicit MC non-detection differs from isolate results. Metabolite detection does not establish mineralization or detoxification. |
| toxicity | PMID:41718267; DOI:10.3390/jox16010024; Methods 2.2.5 Analytical Methods and 2.2.6 Ecotoxicity Bioassays; Results 3.4 paragraphs 3–4 and Table 4 | supports | The day-28 MC mixture remains acutely toxic. Individual metabolite causation is unresolved; TP339 is tentative and semi-quantitative. |
| community | PMID:41718267; DOI:10.3390/jox16010024; Methods 2.2.7 Characterization of Microbial Consortium by DNA Metabarcoding, sole direct paragraph; Results 3.5, all fifteen paragraphs; Figures 5 and 6 | supports | Before/after bacterial and fungal profiles have separate denominators. Main-text Burkholderia shorthand conflicts with the combined S5 classifier resolution. |
| classifier | PMID:41718267; DOI:10.3390/jox16010024; Supplement Table S5.xlsx, sole worksheet Sheet1, J1 genus header and 31 combined-label cells including J3, J9, J47 and J129; compare Results 3.5 paragraphs 3–4 and Figure 5 | supports | The classifier is Burkholderia-Caballeronia-Paraburkholderia. The pooled columns do not independently reconstruct endpoint percentages. |
| supplement | PMID:41718267; DOI:10.3390/jox16010024; Supplement PDF pages 1–3, Figure S1 and Tables S1–S3; separate Tables S4–S6 non-sequence cells | supports | Isolate growth curves and chromatographic identification are distinct from the MC assay; S4 provides six sample identifiers. All non-sequence table cells were read. |
| ontology | /private/tmp/cm-review-session/batch-16/000379/ontology-authority.json; Nineteen exact ID/label pairs, 43 placements | supports | All labels match; term validity is separate from sample identity. |
| schema | /private/tmp/cm-review-session/batch-16/000379/child-schema-semantics.json; Current enum and slot definitions | supports | No optional role is fabricated; ordinal abundance is not a numerical cutoff. |
| gtdb | /private/tmp/cm-review-session/batch-16/000379/child-gtdb-crosswalk.json; All ten encoded taxon routes | supports | Two current numeric cores reproduce; two unresolved genera resolve and Ochrobactrum has three alternatives. Local mtime is not release provenance. |
| classifier-authority | /private/tmp/cm-review-session/batch-16/000379/child-combined-classifier-scope.json; Raw S5 cells and local NCBI sibling genera | supports | Burkholderia 32008, Caballeronia 1827195 and Paraburkholderia 1822464 are distinct genera, all under Burkholderiaceae 119060. |
| semantics | /private/tmp/cm-review-session/batch-16/000379/ontology-semantic-notes.json; Final source-aware native and ontology assessment | supports | Two major and two minor findings; retain the two community observations and zero arrows, with participant resolution qualified. |
| resources | /private/tmp/cm-review-session/batch-16/000379/dataset-verification.json; Complete six-sample Table S4 to ENA bridge | supports | PRJEB98466, bacterial/fungal initial/final samples and two sequencing controls match; no raw read reanalysis. |
| resource-locator | /private/tmp/cm-review-session/batch-16/000379/dataset-locator-erratum.json; Exact Methods 2.2.7 heading clarification | supports | The preserved resource wrapper used a descriptive heading; the exact source heading is Characterization of Microbial Consortium by DNA Metabarcoding. |
| external-links | /private/tmp/cm-review-session/batch-16/000379/external-resource-verification.json; Publication and encoded resource identifiers | supports | The DOI and both marker-specific ENA entries resolve. Isolate Table 1 sequences are not MC genomes. |
| snippets | /private/tmp/cm-review-session/batch-16/000379/snippet-audit.json; All 35 canonical excerpt placements | supports | Thirty match fresh JATS; five match rendered fresh MED Abstract. All 35 also match cache, with no lexical exception. |
| provenance | /private/tmp/cm-review-session/batch-16/000379/provenance-audit.json; Exact focal history, batch33 row, cohort and current issue scopes | supports | Prior graph repair is preserved. All seven selected issues are closed; withdrawn issue 1405 is not the present description defect. |
| inspection | /private/tmp/cm-review-session/batch-16/000379/inspect.json; Official 35-input inspection | supports | Target, 21 authorities and thirteen focal contexts were pinned before assessment. |
| assets | /private/tmp/cm-review-session/batch-16/000379/lead-source-assets.json; Fresh manuscript, six main figures and declared supplement package | supports | Complete source retrieval and all extraction corrections are preserved. |
| lead-read | /private/tmp/cm-review-session/batch-16/000379/lead-primary-read-scope.json; Actual complete source and bounded contextual reads | supports | Whole 124,031-character article including 129 references, six main figures, three SI pages and all non-sequence workbook cells were read. |
| locators | /private/tmp/cm-review-session/batch-16/000379/source-locator-verification.json; Direct section, paragraph, table and caption verification | supports | The two-word quote is in Methods 2.2.4 first direct paragraph. |
| source-audit | /private/tmp/cm-review-session/batch-16/000379/source-audit.json; Final lead source judgment | supports | Two major and two minor findings; nine graph excerpt hashes and no arrows. |
| writer-correction | /private/tmp/cm-review-session/batch-16/000379/source-writer-correction.json; Preserved ancillary receipt-writer failure | supports | An unlabelled non-main table stopped the initial locator writer; source bytes and native outcomes were unaffected. |
| selector-correction | /private/tmp/cm-review-session/batch-16/000379/source-writer-selector-correction.json; Preserved pre-freeze selector assertion | supports | The correct existing status path is taxon_term.gtdb_grounding_status; no candidate existed during the failed preflight. |
| root-source | /private/tmp/cm-review-session/batch-16/000379/root-independent-source-audit.json; Independent root main, SI and authority assessment | supports | Completed source review agrees with two major and two minor findings. |
| metrics | /private/tmp/cm-review-session/batch-16/000379/support-final-audit.json; Final independent reconciliation | supports | Literal completeness 30; base quality 135 less 24 gives raw 111, capped 100. |
| support-manifest | /private/tmp/cm-review-session/batch-16/000379/support-frozen-manifest.json; Frozen supporting dependencies | supports | All current input and nested source pins verified. |
| auxiliary | /private/tmp/cm-review-session/batch-16/000379/auxiliary-frozen-manifest.json; Frozen authority and native dependencies | supports | All eight actual required native checks passed. |
| native-summary | /private/tmp/cm-review-session/batch-16/000379/final-validator-summary.json; Actual eight native checks | supports | Native success is separate from scientific support. |
| corpus-context | /private/tmp/cm-review-session/batch-16/000379/child-corpus-context.json; Fresh batch16 corpus baseline | supports | Actual warning-only corpus exits remain explicit. |
| adapter | /private/tmp/cm-review-session/batch-16/000379/adapter-check.json; Owned-runtime optional adapter scope | supports | Unavailable optional adapter is not negative biological evidence; no installation or paid provider was used. |
| check-validate | /private/tmp/cm-review-session/batch-16/000379/validate.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-16/000379/validate-strict.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-16/000379/validate-terms.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-16/000379/validate-references-explained.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-16/000379/validate-gtdb.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-16/000379/validate-gtdb-domain.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-16/000379/validate-history.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-16/000379/normalize-cache-names-check.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-16/audit-network.json; Fresh batch16 corpus baseline | supports | Actual exit 1 with warning-only corpus findings; zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-16/check-network-quality.json; Fresh batch16 corpus baseline | supports | Actual exit 1 with warning-only corpus findings; zero errors. |

## Limits And Additional Notes

- The combined classifier does not resolve which of three genera contributed individual ASVs; no raw sequence realignment or classifier rerun was performed. S5/S6 pooled columns do not reconstruct time-specific abundance.
- The complete non-sequence supplement tables were read. Sequence column L was excluded except initial exemplars; no claim of whole sequence reading or raw-data reanalysis is made.
- TP339 identity is tentative and semi-quantitative. Increased mixture toxicity does not establish which metabolite caused it. Parent loss does not prove mineralization or detoxification.
- The source iron-hydrate typography and unencoded IC50/plot inconsistencies remain explicit limits; no silent numerical or chemical repair is inferred. Initial pH is not continuous control.
- Background pathways in cited organisms are not focal strain gene evidence. No optional roles, exact MC strain stocks or exhaustive roster are invented.
- Completion applies to this reviewed record and source scope. It does not close issues, promote native record status or authorize canonical curation.
- Eight evidence-linked dimensions and all nine exact graph snippet hashes are present. There are no downstream arrows to assess.
- All 35 official inputs remain unchanged. Required native failures are zero; ancillary retrieval/extraction/display failures and corrections are preserved separately.
- The sole direct source quote has two words. The supporting reviewer read cache and current issue/cohort provenance; individual reviewers retain their actual stated read scopes.
- Root owns persistence and post-save gates; this candidate itself makes no canonical/cache/history/Git change.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T065743Z-diclofenac-consortium-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Diclofenac activated-sludge consortium record review
started_at: '2026-10-22T06:44:11.062763Z'
finished_at: '2026-10-22T06:57:43.124423Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, auxiliary and supporting reviewers; no
    person-level independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The source supports the enrichment, parent-DCF loss and qualified before/after
  community observations. Two major findings correct MC product attribution and a
  combined-genus classifier narrowed to Burkholderia; two minor findings address the
  basal MSM recipe and GTDB completion/provenance. All eight required native checks
  passed. Literal completeness is 30 and quality is capped at 100 (raw 111).
source:
  git_revision: cb7a782c8ba80299dca8761ad0a2c90bccd8a117
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
  - path: history/records/Diclofenac_Activated_Sludge_Microbial_Consortium/2026-09-15T003946Z-codex-f0f048.yaml
    sha256: 8fc34e60b3a6e92016768e3cadb09166a40c4d117d98537ad8d095cb9b3c32cf
    role: context
  - path: history/records/Diclofenac_Activated_Sludge_Microbial_Consortium/2026-09-15T004548Z-codex-9e2763.yaml
    sha256: 906d4592ade99370ba28c8d0e208b5e09478decd3930c6ce57cd5b7bb328cc3c
    role: context
  - path: history/records/Diclofenac_Activated_Sludge_Microbial_Consortium/2026-09-15T011402Z-codex-85c686.yaml
    sha256: 6bc74b3c98fed5edb37506afce5a62639308c7f25d4a0d6a5ee73f6541a6faa5
    role: context
  - path: history/records/Diclofenac_Activated_Sludge_Microbial_Consortium/2026-09-15T013550Z-codex-908c0a.yaml
    sha256: 0e2c215275657173d92f470e1eb711c08592e116dafd68d08b3367391d6581f7
    role: context
  - path: history/records/Diclofenac_Activated_Sludge_Microbial_Consortium/2026-10-02T054552Z-codex-c7c379.yaml
    sha256: 533c5f32b3c4f637b3507959d0f93ab5067337f3f79189ff6eece1a44a4e88fd
    role: context
  - path: history/records/Diclofenac_Activated_Sludge_Microbial_Consortium/2026-10-06T070209Z-codex-da2945.yaml
    sha256: e45bf24f4b52903e3641df10fc48d634960a696901bd34354af765b271a464fb
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    sha256: d8e197f2bb938229e5e6cb3424a509aad5c4f62e45022ae2e1a7860eaac5a1b1
    role: target
  - path: references_cache/PMID_41718267.txt
    sha256: 8947f5a963338a91a87024a35d7691338b63dd4dcd0c95815e25d024d10a334e
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch33.yaml
    sha256: bbc95a9fdbe89641db5ed5315e01160fea0aed3524a6252080b2aa806e81d4ae
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch33.yaml
    sha256: a8fb32ab2e18b2b6cba09c2d4a607c74cb4d2d60a4871712ed26fdf4b03a2e4a
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
- target_id: CommunityMech:000379
  path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
  label: Diclofenac Activated Sludge Microbial Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    role: canonical_record
scope:
  description: Whole released target and encoded claims using complete fresh primary
    text, all six main figures, three SI pages, all non-sequence S4–S6 cells, bounded
    archive/authority metadata and actual native checks.
  selection: Only released CommunityMech:000379 in owned batch16.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000379
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000379
  command: just --no-dotenv validate kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 35 official
    inputs unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000379
  command: just --no-dotenv validate-strict kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-16/000379/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 35 official
    inputs unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000379
  command: just --no-dotenv validate-terms kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 35 official
    inputs unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000379
  command: just --no-dotenv validate-references-explained kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 35 official
    inputs unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000379
  command: just --no-dotenv validate-gtdb kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 35 official
    inputs unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000379
  command: just --no-dotenv validate-gtdb-domain kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 35 official
    inputs unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000379
  command: just --no-dotenv validate-history history/records/Diclofenac_Activated_Sludge_Microbial_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 35 official
    inputs unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000379
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 35 official
    inputs unchanged.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000379
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, not a target or candidate failure.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000379
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, not a target or candidate failure.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in the owned runtime.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - adapter
  scope_note: No focal gene, protein, locus or expression dataset is asserted; iModulonDB
    is not applicable. No installation or biological absence inference.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
  locator: Whole maintained YAML
  summary: Sludge-derived enrichment with a partial genus/family roster, two community-level
    nodes and no arrows.
  support: supports
  accessed_at: '2026-10-22T06:56:17.913563Z'
- evidence_id: abstract
  kind: primary_source
  reference: PMID:41718267; DOI:10.3390/jox16010024
  locator: Fresh MED resultList.result[0], complete Abstract and bibliographic identity
  summary: The Abstract pools consortium and separate isolate outcomes; five canonical
    excerpts use this rendered representation.
  support: supports
  accessed_at: '2026-10-22T06:56:17.913628Z'
  snapshot_sha256: b341272cc06fd93c7999c0ea0067c520c9b0f0e8818f9d3f1c3a5c9bc034f54b
- evidence_id: identity
  kind: primary_source
  reference: PMID:41718267; DOI:10.3390/jox16010024
  locator: Methods 2.1 Material, paragraph 2; 2.2.1 Enrichment and Isolation of DCF-Degrading
    Consortium and DCF-Degrading Strains, all three paragraphs; Results 3.1, all five
    paragraphs
  summary: The focal MC is a glucose-enriched activated-sludge consortium from Seville.
    CSWD.1 and CSWD.2 are separate isolate comparisons.
  support: supports
  accessed_at: '2026-10-22T06:56:17.913753Z'
  snapshot_sha256: 4e7a927aa04abc1d0372f5ec45e340fb8fcf813dd2676968360ecac08a33c7df
- evidence_id: medium-definition
  kind: primary_source
  reference: PMID:41718267; DOI:10.3390/jox16010024
  locator: Methods 2.1 Material, first direct paragraph
  summary: Twelve basal MSM constituents are specified per liter, in addition to assay
    glucose and DCF. Iron-hydrate typography requires qualification.
  support: supports
  accessed_at: '2026-10-22T06:56:17.913888Z'
  snapshot_sha256: 4e7a927aa04abc1d0372f5ec45e340fb8fcf813dd2676968360ecac08a33c7df
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:41718267; DOI:10.3390/jox16010024
  locator: Methods 2.2.4 DCF Biodegradation Test in Solution, first direct paragraph
    (quoted words here), and second paragraph for revival; XPath //*[@id="sec2dot2dot4-jox-16-00024"]/p[1]
  summary: The MC assay uses 50 mL MSM in 250 mL flasks, 3 g/L glucose, 10 mg/L DCF
    sodium, initial OD600 about 1, 30 °C and 180 rpm. LB revival is a separate stage.
  support: supports
  accessed_at: '2026-10-22T06:56:17.913996Z'
  snapshot_sha256: 4e7a927aa04abc1d0372f5ec45e340fb8fcf813dd2676968360ecac08a33c7df
  quote: cotton plug
- evidence_id: performance
  kind: primary_source
  reference: PMID:41718267; DOI:10.3390/jox16010024
  locator: Results 3.3 Diclofenac Biodegradation in Solution, seventh direct paragraph;
    Figure 3 and Table 3
  summary: MC removes parent DCF within five days. It retains 4′-OH-DCF and tentative
    TP339, with no detected 5-OH-DCF.
  support: supports
  accessed_at: '2026-10-22T06:56:17.914106Z'
  snapshot_sha256: 4e7a927aa04abc1d0372f5ec45e340fb8fcf813dd2676968360ecac08a33c7df
- evidence_id: products
  kind: primary_source
  reference: PMID:41718267; DOI:10.3390/jox16010024
  locator: Results 3.3 paragraph 7 and 3.4 Ecotoxicity Studies in Diclofenac-Contaminated
    Aqueous Samples, paragraph 4; Figure 4 bottom MC panels
  summary: The explicit MC non-detection differs from isolate results. Metabolite
    detection does not establish mineralization or detoxification.
  support: supports
  accessed_at: '2026-10-22T06:56:17.914217Z'
  snapshot_sha256: 03a0f28efa512d0312641e04cc05e0ea6c740e308d3aa4695f471b86d1f0cc97
- evidence_id: toxicity
  kind: primary_source
  reference: PMID:41718267; DOI:10.3390/jox16010024
  locator: Methods 2.2.5 Analytical Methods and 2.2.6 Ecotoxicity Bioassays; Results
    3.4 paragraphs 3–4 and Table 4
  summary: The day-28 MC mixture remains acutely toxic. Individual metabolite causation
    is unresolved; TP339 is tentative and semi-quantitative.
  support: supports
  accessed_at: '2026-10-22T06:56:17.914616Z'
  snapshot_sha256: 4e7a927aa04abc1d0372f5ec45e340fb8fcf813dd2676968360ecac08a33c7df
- evidence_id: community
  kind: primary_source
  reference: PMID:41718267; DOI:10.3390/jox16010024
  locator: Methods 2.2.7 Characterization of Microbial Consortium by DNA Metabarcoding,
    sole direct paragraph; Results 3.5, all fifteen paragraphs; Figures 5 and 6
  summary: Before/after bacterial and fungal profiles have separate denominators.
    Main-text Burkholderia shorthand conflicts with the combined S5 classifier resolution.
  support: supports
  accessed_at: '2026-10-22T06:56:17.914728Z'
  snapshot_sha256: 4e7a927aa04abc1d0372f5ec45e340fb8fcf813dd2676968360ecac08a33c7df
- evidence_id: classifier
  kind: primary_source
  reference: PMID:41718267; DOI:10.3390/jox16010024
  locator: Supplement Table S5.xlsx, sole worksheet Sheet1, J1 genus header and 31
    combined-label cells including J3, J9, J47 and J129; compare Results 3.5 paragraphs
    3–4 and Figure 5
  summary: The classifier is Burkholderia-Caballeronia-Paraburkholderia. The pooled
    columns do not independently reconstruct endpoint percentages.
  support: supports
  accessed_at: '2026-10-22T06:56:17.914837Z'
  snapshot_sha256: e7af0b1799e6587eb4e9d4a72ffef5fa821582379dfe38480b2521e8d1b8921b
- evidence_id: supplement
  kind: primary_source
  reference: PMID:41718267; DOI:10.3390/jox16010024
  locator: Supplement PDF pages 1–3, Figure S1 and Tables S1–S3; separate Tables S4–S6
    non-sequence cells
  summary: Isolate growth curves and chromatographic identification are distinct from
    the MC assay; S4 provides six sample identifiers. All non-sequence table cells
    were read.
  support: supports
  accessed_at: '2026-10-22T06:56:17.915054Z'
  snapshot_sha256: bf67cd54f35a7f4500278d39a846bbb3d40a1ca1010a2e083743137ee88042b0
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000379/ontology-authority.json
  locator: Nineteen exact ID/label pairs, 43 placements
  summary: All labels match; term validity is separate from sample identity.
  support: supports
  accessed_at: '2026-10-22T06:56:17.915103Z'
  snapshot_sha256: 655c530f065f5b5a88aa023ebf4226032d68e418892ffdd22f48a98874b4e1cd
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000379/child-schema-semantics.json
  locator: Current enum and slot definitions
  summary: No optional role is fabricated; ordinal abundance is not a numerical cutoff.
  support: supports
  accessed_at: '2026-10-22T06:56:17.915248Z'
  snapshot_sha256: 0d854a5371ead2a97e74a52d02b463bee46ee4d13e6b77205bbc10c44ffc92bc
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000379/child-gtdb-crosswalk.json
  locator: All ten encoded taxon routes
  summary: Two current numeric cores reproduce; two unresolved genera resolve and
    Ochrobactrum has three alternatives. Local mtime is not release provenance.
  support: supports
  accessed_at: '2026-10-22T06:56:17.915423Z'
  snapshot_sha256: 7e9716ccb9fd46b9dc5e2cf9761c9fcb65594b4607b390f4109d4b1beebc33c2
- evidence_id: classifier-authority
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000379/child-combined-classifier-scope.json
  locator: Raw S5 cells and local NCBI sibling genera
  summary: Burkholderia 32008, Caballeronia 1827195 and Paraburkholderia 1822464 are
    distinct genera, all under Burkholderiaceae 119060.
  support: supports
  accessed_at: '2026-10-22T06:56:17.915538Z'
  snapshot_sha256: 503dcf43e5064672421753058a82e97867c88b41ad7c3d70f3acaa4251dba80c
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000379/ontology-semantic-notes.json
  locator: Final source-aware native and ontology assessment
  summary: Two major and two minor findings; retain the two community observations
    and zero arrows, with participant resolution qualified.
  support: supports
  accessed_at: '2026-10-22T06:56:17.915652Z'
  snapshot_sha256: 6a94daa84b6821eff3fb16a40e803febff216ac1a18adeefa1b6b5bb87f0423d
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/dataset-verification.json
  locator: Complete six-sample Table S4 to ENA bridge
  summary: PRJEB98466, bacterial/fungal initial/final samples and two sequencing controls
    match; no raw read reanalysis.
  support: supports
  accessed_at: '2026-10-22T06:56:17.915775Z'
  snapshot_sha256: e74048db4157aabf9b7f9cacc34257ab2d2143b5a55a1ee2dea1405977c8f990
- evidence_id: resource-locator
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/dataset-locator-erratum.json
  locator: Exact Methods 2.2.7 heading clarification
  summary: The preserved resource wrapper used a descriptive heading; the exact source
    heading is Characterization of Microbial Consortium by DNA Metabarcoding.
  support: supports
  accessed_at: '2026-10-22T06:56:17.915894Z'
  snapshot_sha256: 8ea53a60b626370eceb250fb642bcd25cf170c70172b1824c201c898c33dcaa5
- evidence_id: external-links
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/external-resource-verification.json
  locator: Publication and encoded resource identifiers
  summary: The DOI and both marker-specific ENA entries resolve. Isolate Table 1 sequences
    are not MC genomes.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916013Z'
  snapshot_sha256: ffefd8fdc7c8007e6c38b980b226485fa7e5f860d49e6cd984c4bbe6e75dc293
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/snippet-audit.json
  locator: All 35 canonical excerpt placements
  summary: Thirty match fresh JATS; five match rendered fresh MED Abstract. All 35
    also match cache, with no lexical exception.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916120Z'
  snapshot_sha256: e2a921d3c07aae619ce8475ad4cc8dc47bbcbe892716572cc655ac7fb3236e9e
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-16/000379/provenance-audit.json
  locator: Exact focal history, batch33 row, cohort and current issue scopes
  summary: Prior graph repair is preserved. All seven selected issues are closed;
    withdrawn issue 1405 is not the present description defect.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916244Z'
  snapshot_sha256: 44a9cdbb33bf00c88a7897b5a1bd097b24fa6267a84866a0aba402a6ad974f02
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/inspect.json
  locator: Official 35-input inspection
  summary: Target, 21 authorities and thirteen focal contexts were pinned before assessment.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916347Z'
  snapshot_sha256: 375f61d663fe4dfc2828c8a7cdda0ffd7604754ce03e02f707f078a7b981a6af
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/lead-source-assets.json
  locator: Fresh manuscript, six main figures and declared supplement package
  summary: Complete source retrieval and all extraction corrections are preserved.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916370Z'
  snapshot_sha256: bf67cd54f35a7f4500278d39a846bbb3d40a1ca1010a2e083743137ee88042b0
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/lead-primary-read-scope.json
  locator: Actual complete source and bounded contextual reads
  summary: Whole 124,031-character article including 129 references, six main figures,
    three SI pages and all non-sequence workbook cells were read.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916391Z'
  snapshot_sha256: 9714d9f7ef953600afd2fd124ebb2fc919639f6aaefd5143445c692822fc4cf3
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/source-locator-verification.json
  locator: Direct section, paragraph, table and caption verification
  summary: The two-word quote is in Methods 2.2.4 first direct paragraph.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916501Z'
  snapshot_sha256: 7250f8b63c29cd6d55118ac0439bae01fa93ddeed2974ad40dc68ea262bf5e7e
- evidence_id: source-audit
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/source-audit.json
  locator: Final lead source judgment
  summary: Two major and two minor findings; nine graph excerpt hashes and no arrows.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916620Z'
  snapshot_sha256: 87fe6af6400c89985035d42db74f740cb4f8361be60252f3175c161dc7c25f09
- evidence_id: writer-correction
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/source-writer-correction.json
  locator: Preserved ancillary receipt-writer failure
  summary: An unlabelled non-main table stopped the initial locator writer; source
    bytes and native outcomes were unaffected.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916727Z'
  snapshot_sha256: d718ac00922eb46db8d7bb18f12fe295ea199c35fe5a72f8c5233315e3923395
- evidence_id: selector-correction
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/source-writer-selector-correction.json
  locator: Preserved pre-freeze selector assertion
  summary: The correct existing status path is taxon_term.gtdb_grounding_status; no
    candidate existed during the failed preflight.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916814Z'
  snapshot_sha256: 7783d8b38a4176c6eadb405f6cb2dbfdda25c1c0d3a945e271a310b1e6615121
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/root-independent-source-audit.json
  locator: Independent root main, SI and authority assessment
  summary: Completed source review agrees with two major and two minor findings.
  support: supports
  accessed_at: '2026-10-22T06:56:17.916921Z'
  snapshot_sha256: f82b68ac2c7d27d6fac917e40a65bc4b31f22ebe22b25b6d272987843c86518c
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/support-final-audit.json
  locator: Final independent reconciliation
  summary: Literal completeness 30; base quality 135 less 24 gives raw 111, capped
    100.
  support: supports
  accessed_at: '2026-10-22T06:56:17.917030Z'
  snapshot_sha256: 17d76a912237bcce2cd335c96e2fa033954f4631b91fb709869b3cb6588ea3ec
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/support-frozen-manifest.json
  locator: Frozen supporting dependencies
  summary: All current input and nested source pins verified.
  support: supports
  accessed_at: '2026-10-22T06:56:17.917057Z'
  snapshot_sha256: c25a2481a49746fd438db0df8b1cac4a804d608d94770d0ae8484843c08676c2
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/auxiliary-frozen-manifest.json
  locator: Frozen authority and native dependencies
  summary: All eight actual required native checks passed.
  support: supports
  accessed_at: '2026-10-22T06:56:17.917175Z'
  snapshot_sha256: 6f264baec45bd48bf17b3c47112b9b7bcba812ac65424141e388c0df6e44904a
- evidence_id: native-summary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/final-validator-summary.json
  locator: Actual eight native checks
  summary: Native success is separate from scientific support.
  support: supports
  accessed_at: '2026-10-22T06:56:17.917301Z'
  snapshot_sha256: de364b66806fbfb0e30acbd2811daacce575b4d9fd7cd53561f9654c8f72b48d
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/child-corpus-context.json
  locator: Fresh batch16 corpus baseline
  summary: Actual warning-only corpus exits remain explicit.
  support: supports
  accessed_at: '2026-10-22T06:56:17.917456Z'
  snapshot_sha256: 5d16615af2c90f014b178914b1b7f76aba3220135842da608f5b64de55f9e9f0
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/adapter-check.json
  locator: Owned-runtime optional adapter scope
  summary: Unavailable optional adapter is not negative biological evidence; no installation
    or paid provider was used.
  support: supports
  accessed_at: '2026-10-22T06:56:17.917602Z'
  snapshot_sha256: 27a08e82fefefb9bd7a2f429b8d6782da33dc717416940fab8ef3d75ce1e1dc9
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/validate.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:56:17.917951Z'
  snapshot_sha256: 5b9a3482b0984a877321e5bf32753c598cc202e791e4f04543103d539c255ac0
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/validate-strict.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:56:17.918119Z'
  snapshot_sha256: 04d18bbcb544867129f41821dc141af9ffc36d666994684c1522f71427c337f3
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/validate-terms.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:56:17.918277Z'
  snapshot_sha256: a16fdbba67bcd4c5dc841341bb2e0c6b3e48b2783cf1104519aae612170e6bdf
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/validate-references-explained.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:56:17.918455Z'
  snapshot_sha256: f906c530f1091003c07689880b57592a9e94b3f358e59b831d1f0df90f10517c
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/validate-gtdb.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:56:17.918610Z'
  snapshot_sha256: 58b091a978c12e1983f316c8ddc2bbe57f367611e97322ed7ec406b94b7e0a63
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/validate-gtdb-domain.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:56:17.918750Z'
  snapshot_sha256: 2971579a0078d8159462b43551ecd5ec29e4c1581bfd6936ef988ac8cd187599
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/validate-history.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:56:17.918924Z'
  snapshot_sha256: bb13cd4c1ffb112d90f37b24c3edfade314eb9808707685c634b5fb8962e02c5
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000379/normalize-cache-names-check.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:56:17.919047Z'
  snapshot_sha256: 307223bd3f81161741ab40dec9b56154d175c51e0c467f0b3f79a055c0e649eb
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/audit-network.json
  locator: Fresh batch16 corpus baseline
  summary: Actual exit 1 with warning-only corpus findings; zero errors.
  support: supports
  accessed_at: '2026-10-22T06:56:17.919229Z'
  snapshot_sha256: f4809c6a349f1496dbfe0243fb5ce661f469f7235f2aa00e6294ee3aa04f3123
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/check-network-quality.json
  locator: Fresh batch16 corpus baseline
  summary: Actual exit 1 with warning-only corpus findings; zero errors.
  support: supports
  accessed_at: '2026-10-22T06:56:17.919375Z'
  snapshot_sha256: 759ba13f2cda067251275491bbafc401d0be8bddf7907c7f962eb4369f61688f
assessments:
- assessment_id: identity
  area: identity
  topic: Focal enrichment and partial roster
  outcome: supported
  summary: The record denotes the correct sludge-derived enrichment; narrow genus
    resolution requires repair.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - record
  - identity
  - classifier
  - classifier-authority
  dimensions:
  - name: stable_id
    value: CommunityMech:000379; PMID:41718267; DOI:10.3390/jox16010024
    definition: Exact maintained target and fresh primary publication identity.
    evidence_ids:
    - record
    - inspection
    - abstract
  - name: source_strains
    value: MC has no resolved study strains; CSWD.1 and CSWD.2 are separate assay
      arms
    definition: Do not add the Pseudomonas isolates as inferred members or import
      their 16S accessions as MC genomes.
    evidence_ids:
    - identity
    - community
    - external-links
  - name: community_scope
    value: Glucose-enriched activated-sludge community with bacterial and fungal marker
      profiles
    definition: Partial roster and separate marker denominators are explicit; the
      combined classifier is not three independently demonstrated members.
    evidence_ids:
    - identity
    - community
    - classifier
  details: ENGINEERED origin/state and BIOREMEDIATION are supported. Ten curated descriptors
    are a partial roster, not ten isolated strains. Main and SI distinguish MC from
    CSWD.1/CSWD.2 comparison arms.
- assessment_id: summary-products
  area: evidence
  topic: Consortium-specific transformation products
  outcome: concern
  summary: The opening description transfers isolate-only 5-OH-DCF detection to MC.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - abstract
  - performance
  - products
  - toxicity
  details: Node 0 already states the correct non-detection and tentative nitro-product
    limits. Correct the summary consistently; retain observed parent removal and mixture
    toxicity without claiming mineralization, detoxification or metabolite-specific
    causal toxicity.
- assessment_id: node-0
  area: graph
  topic: Glucose-Amended Diclofenac Dissipation by MC
  outcome: concern
  summary: Retain the qualified community-level parent-loss observation; qualify the
    first participant.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - performance
  - products
  - toxicity
  - cultivation
  - classifier
  - snippets
  details: 'Exact selector ecological_interactions[0]; scope COMMUNITY_LEVEL; no interaction_type,
    source_taxon or target_taxon is asserted. Exact participants: [{"preferred_term":
    "Burkholderia", "term": {"id": "NCBITaxon:32008", "label": "Burkholderia"}}, {"preferred_term":
    "Klebsiella", "term": {"id": "NCBITaxon:570", "label": "Klebsiella"}}, {"preferred_term":
    "Ochrobactrum", "term": {"id": "NCBITaxon:528", "label": "Ochrobactrum"}}, {"preferred_term":
    "Chthoniobacter", "term": {"id": "NCBITaxon:295577", "label": "Chthoniobacter"}},
    {"preferred_term": "Parachlamydia", "term": {"id": "NCBITaxon:83551", "label":
    "Parachlamydia"}}, {"preferred_term": "Talaromyces", "term": {"id": "NCBITaxon:5094",
    "label": "Talaromyces"}}, {"preferred_term": "Aspergillus", "term": {"id": "NCBITaxon:5052",
    "label": "Aspergillus"}}, {"preferred_term": "Debaryomycetaceae", "term": {"id":
    "NCBITaxon:766764", "label": "Debaryomycetaceae"}}, {"preferred_term": "Malassezia",
    "term": {"id": "NCBITaxon:55193", "label": "Malassezia"}}, {"preferred_term":
    "Cladosporium", "term": {"id": "NCBITaxon:5498", "label": "Cladosporium"}}]. Exact
    canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "a8910e421cb2d429dbb1d68c728868342236732bc53f72d20d0af1b65e1be1b3",
    "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "IN_VITRO"},
    {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "ee4c80f9c44b0510e68dd8fa191071dedf338483995c5d56e3fc8a1cbd361b66",
    "reference": "PMID:41718267", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}].
    PMID:41718267 source locators: Methods 2.2.4 paragraphs 1–2; Results 3.3 paragraph
    7; Figures 3–4, Tables 3–4; Results 3.4 paragraphs 3–4. SUPPORT for MC disappearance
    is sound. The pooled Abstract metabolite excerpt is correctly PARTIAL. GO xenobiotic/glucose
    processes are community assay context, not individual flux. Parent loss is distinct
    from mineralization and detoxification.'
- assessment_id: node-1
  area: graph
  topic: DCF-Selected Community Shift
  outcome: concern
  summary: Retain the bounded before/after profile observation; reconcile the combined
    genus label.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - community
  - classifier
  - classifier-authority
  - supplement
  - snippets
  details: 'Exact selector ecological_interactions[1]; scope COMMUNITY_LEVEL; no interaction_type,
    source_taxon or target_taxon is asserted. Exact participants: [{"preferred_term":
    "Burkholderia", "term": {"id": "NCBITaxon:32008", "label": "Burkholderia"}}, {"preferred_term":
    "Klebsiella", "term": {"id": "NCBITaxon:570", "label": "Klebsiella"}}, {"preferred_term":
    "Ochrobactrum", "term": {"id": "NCBITaxon:528", "label": "Ochrobactrum"}}, {"preferred_term":
    "Chthoniobacter", "term": {"id": "NCBITaxon:295577", "label": "Chthoniobacter"}},
    {"preferred_term": "Parachlamydia", "term": {"id": "NCBITaxon:83551", "label":
    "Parachlamydia"}}, {"preferred_term": "Talaromyces", "term": {"id": "NCBITaxon:5094",
    "label": "Talaromyces"}}, {"preferred_term": "Aspergillus", "term": {"id": "NCBITaxon:5052",
    "label": "Aspergillus"}}, {"preferred_term": "Debaryomycetaceae", "term": {"id":
    "NCBITaxon:766764", "label": "Debaryomycetaceae"}}, {"preferred_term": "Malassezia",
    "term": {"id": "NCBITaxon:55193", "label": "Malassezia"}}, {"preferred_term":
    "Cladosporium", "term": {"id": "NCBITaxon:5498", "label": "Cladosporium"}}]. Exact
    canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "de326593817836b0b34534b4825577a8a5483711aef130f2b416828780122b2e",
    "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "72cd1badd8cb706081d3682842670ee49fa50cfe0ed6e69bf5eb9b3a1cac3022",
    "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[1].evidence[2].snippet", "sha256": "b72681c33e1e09abda98d61def26017b4493721bc2a589accb33a65956acdc27",
    "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[1].evidence[3].snippet", "sha256": "7f29d1c03e72ba2c3fb88441463ef6fecf7e2c8067e21cf93a49dce0dd2392b0",
    "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[1].evidence[4].snippet", "sha256": "967aa86847f0ad45f5a1794f35d135b3d29b7af2f892f8ad84d9261c03d9a8d7",
    "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[1].evidence[5].snippet", "sha256": "1224bbb9a517b2b30462567f9b6052e039ca2dbf4e40303561ce1ccdbd6f1452",
    "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[1].evidence[6].snippet", "sha256": "2336f23d2a647ebedfb01548476f489a7b2a09a42fdf2f4c73f227129022bdfd",
    "reference": "PMID:41718267", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}].
    PMID:41718267 source locators: Methods 2.2.7 sole paragraph; Results 3.5 paragraphs
    3–4, 10 and 12; Figures 5–6; Tables S4–S6. Measured DNA followed by computational
    assignment supports relative profiles. It does not establish absolute growth,
    DCF-only causation, niche partitioning or member degradation. Preserve the author-reported
    bacterial and fungal percentages with distinct denominators; S5 pooled columns
    cannot validate the individual endpoints. The first participant and Burkholderia
    summary need the combined-classifier qualification.'
- assessment_id: graph-topology
  area: graph
  topic: No downstream arrows
  outcome: supported
  summary: Retain the two observations with zero downstream arrows.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - record
  - community
  - semantics
  details: 'No arrow assessment is omitted: both current downstream arrays are absent.
    Sampling the same cultures does not establish a directed ecological mechanism.
    The classifier finding concerns participant grounding, not graph connectivity.'
- assessment_id: cultivation
  area: evidence
  topic: MSM formulation and assay stages
  outcome: concern
  summary: Current assay settings are supported; the structured medium omits the basal
    MSM recipe.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - medium-definition
  - cultivation
  - identity
  - supplement
  dimensions:
  - name: medium
    value: MSM plus 3 g/L glucose and 10 mg/L diclofenac sodium
    definition: Source basal recipe is distinct from the two encoded supplements and
      from separate LB revival.
    evidence_ids:
    - medium-definition
    - cultivation
  - name: experimental_setting
    value: 'Triplicate MC flasks: 50 mL in 250 mL cotton-plugged Erlenmeyers; initial
      OD600 about 1'
    definition: Three biological treatments plus abiotic control total twelve flasks.
      Preserve MC versus isolate and initial enrichment stages.
    evidence_ids:
    - cultivation
    - identity
  - name: environment
    value: 30 °C, 180 rpm, aerobic; preparation pH 7.0 ± 0.2
    definition: Laboratory assay represents sludge/WWTP origin. No continuous pH or
      dissolved-oxygen control is inferred.
    evidence_ids:
    - medium-definition
    - cultivation
    - identity
  details: Methods 2.1 specifies twelve basal components. Recover the source formulation
    and separately document LB revival/washing if expanded. The source iron entry
    joins FeSO4 and 7 H2O awkwardly; retain that uncertainty rather than silently
    certify a hydrate. The SI 100 mL LB/125 rpm isolate growth curve is not the MC
    degradation protocol.
- assessment_id: grounding
  area: grounding
  topic: Taxon resolution and GTDB provenance
  outcome: concern
  summary: Valid ID/label pairs do not resolve a combined assay classifier to one
    genus.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - ontology
  - classifier
  - classifier-authority
  - gtdb
  - schema
  dimensions:
  - name: taxon_grounding
    value: Nine encoded genera and Debaryomycetaceae family; first genus overresolves
      the S5 group
    definition: Keep source classifier resolution separate from current NCBI/GTDB
      name correspondence and reference-genome counts.
    evidence_ids:
    - ontology
    - classifier-authority
    - gtdb
  details: S5 contains 31 ASVs labelled Burkholderia-Caballeronia-Paraburkholderia.
    Current NCBI identifies three distinct sibling genera. Do not infer that all three
    occur separately or select another genus without evidence. Burkholderia 8896/8908
    and Klebsiella 44527/44529 GTDB cores reproduce, but the former applies only to
    the narrower named taxon. Chthoniobacter maps 2/2 and Parachlamydia 13/13; Ochrobactrum
    has three genus candidates. Five fungal NO_GTDB_EQUIVALENT statuses are appropriate.
    Local mtime establishes neither latest release nor build date.
- assessment_id: resources
  area: representation
  topic: Verified marker-specific archive
  outcome: supported
  summary: Both encoded PRJEB98466 marker resources match the source and six sample
    records.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - resources
  - resource-locator
  - external-links
  - community
  details: All six S4 aliases/accessions map to bacterial/fungal initial/final samples
    plus two negative sequencing controls. ENA reports paired Illumina MiSeq amplicon/PCR
    libraries. No raw FASTQ or new statistical analysis was needed; no resource omission
    is graded.
- assessment_id: source-scope
  area: scope
  topic: Complete main and bounded supplement analysis
  outcome: supported
  summary: The full article, six main figures and all declared supplement objects
    were inspected.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - assets
  - lead-read
  - locators
  - root-source
  - supplement
  dimensions:
  - name: evidence_tier
    value: IN_VITRO degradation and mixture toxicity; computational interpretation
      of measured 16S/ITS profiles
    definition: Exact 35 lexical matches comprise 30 fresh JATS and five rendered
      fresh MED matches; entailment and assay scope are separately assessed.
    evidence_ids:
    - performance
    - toxicity
    - community
    - snippets
    - lead-read
  details: The lead read all 124,031 projected article characters and 129 references,
    the three-page SI PDF and all non-sequence S4/S5/S6 cells. Sequence column L was
    excluded except initial exemplars. Stale workbook dimensions and missing drawing
    references were handled with preserved read-only extraction corrections. Root
    independently read scientific main sections, all figure pixels and non-sequence
    SI cells; no claim that every reviewer read the bibliography or raw sequences.
- assessment_id: ownership
  area: ownership
  topic: Maintained inputs and historical review scope
  outcome: supported
  summary: Future repairs belong to the maintained community YAML under separate curation
    authorization.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - inspection
  - provenance
  details: All 35 official inputs remain unchanged. The exact prior batch33 row repaired
    the graph while preserving non-graph metadata; cohort completeness 77 is a different
    proportional metric. Closed issue 1405 had a withdrawn ingredient premise and
    is not reused as proof of the present description finding. No history, issue,
    cache or Git changes are made.
- assessment_id: native
  area: schema
  topic: Actual native validation
  outcome: supported
  summary: All eight required native checks passed.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - native-summary
  - auxiliary
  - corpus-context
  - adapter
  details: Native label/reference/network success does not establish taxonomic resolution
    or causal support. The two-node network has zero reported structural issues.
- assessment_id: metrics
  area: completeness
  topic: Literal native metrics
  outcome: supported
  summary: Completeness 30; raw quality 111, capped 100.
  target_ids:
  - CommunityMech:000379
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 30
    unit: points
    minimum: 0
    maximum: 100
    definition: 0 required-fields-and-roles +5 environment +0 three-environmental-factors
      +0 three-interaction-nodes +5 external resources +10 medium +5 datasets +5 interaction
      metabolites =30. Optional role absence is not a biological defect; do not invent
      roles to obtain the 50-point component.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 +20*min((9/2)/2,1) +15 -10*2 -2*2 =111, capped at 100. The evidence
      bonus is 20 and the structural COMPLETE bonus is 15; neither establishes causal
      or taxonomic truth.
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
- finding_id: product-scope
  issue_key: cm-000379-product-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material product attribution or sample-taxonomic scope error.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Correct the MC product summary
  description: The description assigns 5-OH-DCF formation to MC although Results and
    Figure 4 explicitly report non-detection in MC. The Abstract pools separate isolate
    and consortium assays.
  target_ids:
  - CommunityMech:000379
  field_paths:
  - description
  evidence_ids:
  - abstract
  - performance
  - products
  - toxicity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable sources, caches, history
    and prior reviews remain unchanged.
- finding_id: classifier-resolution
  issue_key: cm-000379-classifier-resolution
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: Material product attribution or sample-taxonomic scope error.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Preserve the combined classifier resolution
  description: The S5 group spans three distinct genera, so NCBITaxon:32008 alone
    is narrower than the assay assignment. Main shorthand and valid name mappings
    do not resolve the sample.
  target_ids:
  - CommunityMech:000379
  field_paths:
  - taxonomy[0]
  - ecological_interactions[0].participating_taxa[0]
  - ecological_interactions[1].participating_taxa[0]
  - ecological_interactions[1].description
  evidence_ids:
  - community
  - classifier
  - classifier-authority
  - gtdb
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable sources, caches, history
    and prior reviews remain unchanged.
- finding_id: medium-completeness
  issue_key: cm-000379-medium-completeness
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded formulation or mapping-provenance repair; the community
    phenotype and core assay remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Recover the source basal MSM formulation
  description: The current composition contains the two supplements but omits the
    twelve basal constituents specified in Methods 2.1.
  target_ids:
  - CommunityMech:000379
  field_paths:
  - growth_media[0].composition
  - growth_media[0].preparation_notes
  evidence_ids:
  - medium-definition
  - cultivation
  - supplement
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable sources, caches, history
    and prior reviews remain unchanged.
- finding_id: gtdb-provenance
  issue_key: cm-000379-gtdb-provenance
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Bounded formulation or mapping-provenance repair; the community
    phenotype and core assay remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Complete bounded genus mappings and snapshot provenance
  description: Current genus crosswalks resolve two UNRESOLVED entries and expose
    three Ochrobactrum candidates. Existing numerical cores reproduce, but latest/build
    wording is not established by filesystem mtime.
  target_ids:
  - CommunityMech:000379
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  - taxonomy[2].taxon_term.gtdb_grounding_status
  - taxonomy[3].taxon_term.gtdb_grounding_status
  - taxonomy[4].taxon_term.gtdb_grounding_status
  evidence_ids:
  - gtdb
  - ontology
  - schema
  - classifier-authority
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable sources, caches, history
    and prior reviews remain unchanged.
actions:
- action_id: repair-products
  description: Align the summary with MC-specific observations.
  finding_ids:
  - product-scope
  target_ids:
  - CommunityMech:000379
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - State no detected 5-OH-DCF in MC while retaining 4′-OH-DCF and tentative TP339/NO2-DCF.
    Attribute 5-OH detection to the separate isolate arms.
  - Preserve node 0 qualifications, parent disappearance versus mineralization, and
    endpoint mixture toxicity without assigning toxicity to one identified metabolite.
- action_id: repair-classifier
  description: Represent the combined assay label consistently before selecting narrower
    taxon grounding.
  finding_ids:
  - classifier-resolution
  target_ids:
  - CommunityMech:000379
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Record the S5 Burkholderia-Caballeronia-Paraburkholderia resolution and explain
    the main text/Figure 5 shorthand. Reconcile taxonomy[0], both first participant
    copies, description, taxon notes and abundance wording together.
  - Do not arbitrarily replace Burkholderia with a sister genus, assert all three
    independently occur, or force the entire family as an exact identity. Use a supported
    unresolved representation or source-supported reanalysis before narrowing.
  - Retain author-reported 26.9% and 88.9% only with their source and classifier qualification.
    Do not derive endpoints from pooled S5 RA or treat valid reference GTDB mapping
    as sample classification.
  - Retain both community observations, zero arrows and partial roster; do not assign
    individual degrader roles from amplicon abundance.
- action_id: repair-medium
  description: Add the source recipe while preserving assay stages.
  finding_ids:
  - medium-completeness
  target_ids:
  - CommunityMech:000379
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Recover the twelve basal solutes from Methods 2.1 with exact concentrations/forms;
    verify source FeSO4/7 H2O typography rather than invent a hydrate or separate
    water dose. A deliberately partial formulation must be explicit.
  - Keep the supported 50 mL/250 mL, 30 °C, 180 rpm, aerobic, 28-day assay and initial
    pH. If documenting revival, separate 24-hour LB preparation and MSM washes from
    the degradation medium.
  - Do not import the SI isolate growth curve, IC50 broth assay or generic medium
    recipe into MC conditions. Attach an exact Methods excerpt to added details.
- action_id: repair-gtdb
  description: Use verified genus routes and honest local provenance.
  finding_ids:
  - gtdb-provenance
  target_ids:
  - CommunityMech:000379
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Add current Chthoniobacter GTDB:g__Chthoniobacter (2/2) and Parachlamydia GTDB:g__Parachlamydia
    (13/13) mappings with full lineage and method.
  - Represent Ochrobactrum as AMBIGUOUS with the three genus candidates Ochrobactrum_A,
    Ochrobactrum_B and Ochrobactrum; do not promote its isolated exact-ID row to a
    species assignment.
  - Replace unsupported latest/build assertions with actual snapshot hash and method.
    Keep all fungal NO_GTDB_EQUIVALENT statuses. Re-ground any changed first participant
    only after the separate sample-resolution repair.
- action_id: validate-curation
  description: Validate separately authorized future changes.
  finding_ids:
  - product-scope
  - classifier-resolution
  - medium-completeness
  - gtdb-provenance
  target_ids:
  - CommunityMech:000379
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Diclofenac_Activated_Sludge_Microbial_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Run focused schema, strict, term, reference, GTDB and history checks after actual
    edits, plus applicable generated-document gates. Preserve original caches/history
    and existing graph qualifications. Root alone saves this review and runs post-save
    gates.
limitations:
- The combined classifier does not resolve which of three genera contributed individual
  ASVs; no raw sequence realignment or classifier rerun was performed. S5/S6 pooled
  columns do not reconstruct time-specific abundance.
- The complete non-sequence supplement tables were read. Sequence column L was excluded
  except initial exemplars; no claim of whole sequence reading or raw-data reanalysis
  is made.
- TP339 identity is tentative and semi-quantitative. Increased mixture toxicity does
  not establish which metabolite caused it. Parent loss does not prove mineralization
  or detoxification.
- The source iron-hydrate typography and unencoded IC50/plot inconsistencies remain
  explicit limits; no silent numerical or chemical repair is inferred. Initial pH
  is not continuous control.
- Background pathways in cited organisms are not focal strain gene evidence. No optional
  roles, exact MC strain stocks or exhaustive roster are invented.
- Completion applies to this reviewed record and source scope. It does not close issues,
  promote native record status or authorize canonical curation.
notes:
- Eight evidence-linked dimensions and all nine exact graph snippet hashes are present.
  There are no downstream arrows to assess.
- All 35 official inputs remain unchanged. Required native failures are zero; ancillary
  retrieval/extraction/display failures and corrections are preserved separately.
- The sole direct source quote has two words. The supporting reviewer read cache and
  current issue/cohort provenance; individual reviewers retain their actual stated
  read scopes.
- Root owns persistence and post-save gates; this candidate itself makes no canonical/cache/history/Git
  change.
tags:
- record-review
- bioremediation
- diclofenac
- batch-16
```
