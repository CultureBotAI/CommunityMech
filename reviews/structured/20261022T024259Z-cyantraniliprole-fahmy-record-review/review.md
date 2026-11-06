# Cyantraniliprole Fahmy T4 consortium record review

- Review: 20261022T024259Z-cyantraniliprole-fahmy-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T02:32:59.891734Z
- Finished UTC: 2026-10-22T02:42:59.557083Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The six-strain identity, qualified predicted repertoire and HPLC removal node are supported. One major finding corrects the salinity optimum; three minor findings address the conflicting broad-assay temperature, recoverable protocol detail and four available GTDB mappings. Full focal source review is complete, with bounded earlier-strain evidence. Eight focused checks pass. Literal completeness is 85 and raw quality 109, capped at 100.

## Scope And Provenance

Whole focal record and full fresh manuscript, all five figures/eight tables, local authorities and exact historical context; bounded earlier primary strain assays.

Selection: Only released CommunityMech:000369 in owned batch14.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e117e3d37c65bfad2e04af53ab34e1325d8d7f98.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000369 | kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml | maintained | Cyantraniliprole Fahmy Consortium T4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000369 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000369 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000369 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000369 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000369 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000369 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000369 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000369 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000369 | Actual corpus exit 1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000369 | Actual corpus exit 1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000369 | Unavailable in the owned runtime. |

## Scientific And Domain Assessments

### Six-strain benchmark and community scope

identity: supported. Targets: CommunityMech:000369.

The defined T4 inoculum is correctly distinguished from native water microbes and the other consortia.

Retain SYNTHETIC origin, ENGINEERED state and BIOREMEDIATION. Exact source strains are AZFS3, AZFS5, AZFS15, AZFS18, KZFS4 and KZFS11. Their marker-identified species/subspecies descriptors are not study-strain genome classifications.

### T4 distributed cyantraniliprole enzyme potential

graph: supported. Targets: CommunityMech:000369.

Retain predicted enzyme potential with its existing computational qualifications.

Exact selector ecological_interactions[0]; name T4 distributed cyantraniliprole enzyme potential; scope COMMUNITY_LEVEL; interaction_type absent. Actual encoded taxa: {"source": null, "target": null, "participants": [{"id": "NCBITaxon:135461", "label": "Bacillus subtilis subsp. subtilis"}, {"id": "NCBITaxon:1408", "label": "Bacillus pumilus"}, {"id": "NCBITaxon:72360", "label": "Bacillus mojavensis"}, {"id": "NCBITaxon:2026194", "label": "Bacillus paramycoides"}, {"id": "NCBITaxon:287", "label": "Pseudomonas aeruginosa"}, {"id": "NCBITaxon:323284", "label": "Alcaligenes aquatilis"}]}. Canonical evidence bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "460ead14eda420110d469d8295ccee0dcf96814a945b55c1da99247a695cf5c6", "reference": "PMID:42354927", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}]. Snippet-audit SHA256 f7bf6c5a584a30cd321a29b1393b63aad3a9f0b5bf725f0511349815048ceac1. PMID:42354927 Methods 2.11 and Results 3.6.3, Table 8, Figures 4–5. Retain SUPPORT / COMPUTATIONAL: post-assay repertoire predictions do not establish enzyme expression/activity, exchange, reciprocal fitness or the necessity/sufficiency of a four-strain subset.

### HPLC-confirmed cyantraniliprole removal

graph: supported. Targets: CommunityMech:000369.

Retain the measured community-level parent-removal outcome.

Exact selector ecological_interactions[1]; name HPLC-confirmed cyantraniliprole removal; scope COMMUNITY_LEVEL; interaction_type absent. Actual encoded taxa: {"source": null, "target": null, "participants": [{"id": "NCBITaxon:135461", "label": "Bacillus subtilis subsp. subtilis"}, {"id": "NCBITaxon:1408", "label": "Bacillus pumilus"}, {"id": "NCBITaxon:72360", "label": "Bacillus mojavensis"}, {"id": "NCBITaxon:2026194", "label": "Bacillus paramycoides"}, {"id": "NCBITaxon:287", "label": "Pseudomonas aeruginosa"}, {"id": "NCBITaxon:323284", "label": "Alcaligenes aquatilis"}]}. Canonical evidence bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "da478a74902b1891779aa4b92b468bfe635f8f82bf5f2faed204c9d53f5176ef", "reference": "PMID:42354927", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet-audit SHA256 f7bf6c5a584a30cd321a29b1393b63aad3a9f0b5bf725f0511349815048ceac1. PMID:42354927 Abstract removal sentence; Results 3.6.2, Table 7 and Figure 3. Retain SUPPORT / IN_VITRO: observed HPLC parent decline from 57.79 to 1.00 mg/L over 20 days at 30 °C, with native-water and nutrient-control context. No product balance, detoxification, mineralization or individual member contribution is established.

### Zero downstream arrows

graph: supported. Targets: CommunityMech:000369.

Predicted repertoire and measured removal remain separate observations.

No directed causal edge is warranted solely by their occurrence in the same study. Both nodes retain all six participants, with no encoded pairwise source or target.

### Broad degrader roles versus current mechanism

evidence: supported. Targets: CommunityMech:000369.

Prior exact-strain pesticide assays support the broad role annotations.

Keep PRIMARY_DEGRADER without a polymer-only restriction. Add precise earlier-source context if enriching taxonomy evidence; neither membership excerpts nor predicted enzyme assignments prove individual cyantraniliprole flux. No role-deletion finding is made.

### Salinity optimum and broad-assay temperature

scope: concern. Targets: CommunityMech:000369.

The record promotes a contradicted salinity optimum and omits a temperature disagreement.

Separate tested tolerance from highest OD600 growth and distinguish the broad diamide assay from optimization and water-removal conditions. Exact source excerpts may remain verbatim while explanations disclose the conflicts.

### Recoverable recipe and inoculation details

completeness: concern. Targets: CommunityMech:000369.

The source supplies useful protocol detail beyond the current summary.

Retain source-specific units and hydrate forms, stock versus final inoculum, water portion versus total liquid volume, and assay-specific shaking. Batch/OTHER remains appropriate; analytical sampling does not imply feeding or medium replacement.

### Ontology and current GTDB scope

grounding: concern. Targets: CommunityMech:000369.

Ontology labels fit, and four unresolved reference taxa can be grounded.

Four exact-ID candidates are available; two ambiguous name routes can be represented as AMBIGUOUS with candidate lists. No forced strain classification, NCBI relabeling or guessed genome assignment follows.

### Markers and experiment data

provenance: supported. Targets: CommunityMech:000369.

Existing marker identities are verified without promoting them to current experiment deposits.

LC599401–LC599406 are partial 16S sequences with exact strain associations. The paper offers further experiment data on request; no mandatory archive omission is inferred and no contact was made.

### Maintained record and prior decisions

ownership: supported. Targets: CommunityMech:000369.

The focal YAML owns future repairs; historical observations remain immutable.

Preserve current exponent and recovered-baseline fixes, zero graph arrows and exact historical scope. No issue status, cache or history entry is changed by this review.

### Complete focal source coverage

scope: supported. Targets: CommunityMech:000369.

Actual full text and all declared figures resolve the misleading metadata access flags.

All eight tables and 129 reference entries were read; the actual JATS declares no supplement. Earlier ref32 was read only for identity and role-relevant methods/results, without expanding to a full citation audit.

### Native validation and exact excerpts

schema: supported. Targets: CommunityMech:000369.

Eight focused checks pass; all 24 excerpts match fresh source and cache.

The separate corpus failures and unavailable optional adapter remain explicit. Deterministic passes do not resolve source contradictions.

### Two literal native scores

completeness: supported. Targets: CommunityMech:000369.

Completeness 85; raw quality 109, capped at 100.

## Findings

### salinity-optimum: Distinguish the detailed growth optimum from the abstract range

major / open / confirmed; issue key: cm-000369-salinity-optimum.

Current optimized-condition fields repeat 0.5–5.0% NaCl, despite Results 3.2.3 and Figure 1C locating maximal OD600 growth at 0.0–0.5%. The source contradiction needs explicit treatment.

### assay-temperature: Disclose the broad-diamide temperature conflict

minor / open / confirmed; issue key: cm-000369-assay-temperature.

Table 6 supports the encoded 35 °C, while Methods 2.7 specifies 30 °C. Reporting only the former conceals an unresolved source discrepancy.

### protocol-detail: Add available assay-specific medium and inoculation detail

minor / open / confirmed; issue key: cm-000369-protocol-detail.

The record summarizes MSM and NPK but omits the recoverable quantitative recipe, actual nutrient sources and inoculum/vessel preparation. This is an enrichment gap, not a claim that the paper lacks Methods.

### gtdb-resolution: Document four available reference-taxon mappings

minor / open / confirmed; issue key: cm-000369-gtdb-resolution.

All six taxa remain UNRESOLVED although four exact encoded IDs resolve in the inspected crosswalk. The other two name routes are ambiguous and should retain that unresolved boundary.

## Recommended Actions And Acceptance Checks

### qualify-salinity

Correct the salinity claim while preserving source disagreement.

- Use Results 3.2.3 and Figure 1C to describe highest OD600 growth at 0.0–0.5% NaCl. Distinguish this from growth across the four tested concentrations and from the abstract 0.5–5.0% statement.
- Keep quoted source text exact; qualify or replace its associated claim-local explanation. Do not present the OD600 optimum as a directly measured degradation-rate optimum, or confuse MSM 500 mg/L NaCl with 0.5%.

### qualify-temperature

Preserve the unresolved assay temperature.

- Record Methods 2.7 at 30 °C and Table 6 at 35 °C, explicitly unresolved. Do not silently choose one, merge it with optimization 30–35 °C, or transfer the separate water-microcosm setpoint.
- Retain five separate 100 mg/L treatments and the measured OD600 range, with growth rather than complete-degradation interpretation.

### recover-protocol

Enrich each assay with its own Methods context.

- Methods 2.1 MSM in mg/L: K2HPO4 500; KH2PO4 250; NaCl 500; (NH4)2SO4 230; CaCl2·2H2O 7.5; MgSO4·7H2O 100; source-printed MnSO4·7H2O 100; FeCl3 1; distilled water to 1 L, pH 7.0. Preserve the source formula without silently correcting it or borrowing an unrelated medium.
- Methods 2.4: 1 mL of 10^7 CFU/mL stock into 250 mL MS broth, 50 mg/L cyantraniliprole, OVAT/OD600, 150 rpm. Methods 2.7 separately specifies TSB preculture, washing, 250 mL Erlenmeyer vessels, 0.5 g/L NaCl, 11 days and 150 rpm; vessel capacity is not an established working volume.
- Methods 2.8: 500 mL freshwater portions, sealed plastic jars, 20 mL of the 10^7 CFU/mL stock, initial mixing and C:N:P 100:15:1 using ammonium sulfate and KH2PO4. Do not label stock density as final density, manufacture a commercial NPK formulation, replace the stated water volume with 520 mL, or import continuous shaking.
- Retain native-water and uninoculated nutrient controls, 30 °C and 20-day HPLC scope. Keep DCPIP, biomass/biofilm and broad-diamide growth protocols distinct. Analytical sampling alone does not establish fed-batch operation.
- Optional claim-local taxonomy evidence can cite ref32 Methods 2.2/2.5–2.7 and Results 3.3/Table 5 for prior CAP/FBD capability. Retain broad degrader roles without transferring prior substrates, percentages or individual activity to the focal cyantraniliprole experiment.

### resolve-gtdb

Enrich reference-taxon grounding without classifying marker-identified strains.

- Use exact-ID candidates: 135461→GTDB:s__Bacillus_subtilis (1.0,101 genomes); 2026194→GTDB:s__Bacillus_A_paramycoides (1.0,9); 287→GTDB:s__Pseudomonas_aeruginosa (0.99,17191); 323284→GTDB:s__Alcaligenes_aquatilis (1.0,12). Preserve complete recorded lineages, ncbi_id route and taxon scope; do not derive an integer support count from rounded 0.99.
- Refine AZFS5/B. pumilus and AZFS15/B. mojavensis to AMBIGUOUS with gtdb_candidates if adding the verified ambiguity results. B. pumilus has four total destinations: Bacillus altitudinis, Bacillus pumilus, Bacillus pumilus_O and Bacillus sp002998085; B. mojavensis has Bacillus halotolerans and Bacillus mojavensis. Use exact CURIEs from the crosswalk receipt; select no bin for either study strain. Preserve source strain labels and NCBI IDs.
- Record mapping SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. Filesystem mtime does not establish release/build date; name differences do not prove reclassification of the studied strain.

### validate-future-curation

Validate separately authorized record repairs.

- Recheck source locators, exact excerpts, identifiers and graph references; run schema, strict, terms, explained-reference, GTDB/domain and history gates, then just gen-html and just check-docs-current for authorized record changes.
- Preserve source conflicts, prior decisions and all original receipts. This review proposes changes but does not mutate canonical records, caches, history, issues or Git.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml; Whole maintained record | supports | Six named strains form the T4 benchmark consortium. Two untyped community-level nodes distinguish predicted repertoire from HPLC removal; no downstream arrows are encoded. |
| identity | PMID:42354927; DOI:10.3390/microorganisms14061303; Methods 2.2; Tables 2–3 | supports | T4 is the previously characterized six-strain benchmark, distinct from newly assembled T1–T3. Source strain codes and marker accessions match the record. |
| salinity | PMID:42354927; DOI:10.3390/microorganisms14061303; Abstract; Results 3.2.3, sole paragraph; Figure 1C; Discussion | supports | The abstract reports 0.5–5.0% NaCl as optimal, but detailed Results and Figure 1C show highest OD600 growth at 0.0–0.5%. Tolerance across the tested range does not make that entire range optimal. |
| recipe | PMID:42354927; DOI:10.3390/microorganisms14061303; Methods 2.1 Pesticides and Media, sole paragraph; Methods 2.4, sole paragraph | supports | The complete MSM formulation and OVAT growth assay are available. One millilitre of 10^7 CFU/mL inoculum enters 250 mL broth with 50 mg/L cyantraniliprole; OD600 is the readout. |
| diamide | PMID:42354927; DOI:10.3390/microorganisms14061303; Methods 2.7 Biodegradation of Some Diamide Pesticides, sole paragraph; Table 6 | supports | The five separate 100 mg/L diamide treatments yield T4 OD600 values 2.211–2.272. Methods specifies 30 °C, while the table caption specifies 35 °C; the source does not resolve this conflict. |
| microcosm | PMID:42354927; DOI:10.3390/microorganisms14061303; Methods 2.8 → Water Microcosm System, fourth direct paragraph for quote; surrounding preparation, nutrient and inoculation paragraphs; Table 2 | supports | Water portions are placed in sealed plastic jars. The protocol supplies stock preparation, initial mixing, C:N:P adjustment and nutrient sources. Stock concentration and nominal water volume must remain distinct from final inoculum concentration and total liquid volume. |
| removal | PMID:42354927; DOI:10.3390/microorganisms14061303; Methods 2.10 Cyantraniliprole (CPS) Residue Analysis; Results 3.6.2 and Table 7; Figure 3 | supports | T4 recovered zero-day residue is 57.79 mg/L and day-20 residue is 1.00 mg/L: 98.27% removal relative to the recovered baseline. The treatment is nominally 60 mg/L in native water at 30 °C; this is parent-compound disappearance, not demonstrated mineralization or detoxification. |
| prediction | PMID:42354927; DOI:10.3390/microorganisms14061303; Methods 2.11 Cyantraniliprole Pathway Prediction; Results 3.6.3; Table 8 and Figures 4–5; Discussion | supports | Five enzyme classes and proposed pathway coverage are computational assignments. The source does not measure strain-resolved enzyme activity, exchange, flux or the performance of the proposed reduced consortium. |
| redox | PMID:42354927; DOI:10.3390/microorganisms14061303; Methods 2.5–2.6; Results 3.3–3.4; Tables 4–5 | supports | T4 decolorizes DCPIP at 17 h; biomass and crystal-violet biofilm measurements are separate assays. These readouts do not establish product identities or direct catalytic flux. |
| prior-role | DOI:10.3390/pr10122527; Recovered published PDF: Methods 2.1–2.7; Results 3.1 and 3.3; Table 5 | supports | The exact six strains previously grew on chlorantraniliprole/flubendiamide and were tested individually by controlled soil respirometry. This supports broad pesticide-degrader capability, without proving individual cyantraniliprole turnover in the present consortium. Only these bounded earlier-source sections were assessed. |
| ontology | /private/tmp/cm-review-session/batch-14/000369/ontology-authority.json; Ten ID-label pairs, definitions and 26 placements | supports | All encoded labels match; cyantraniliprole chemistry, laboratory/freshwater scopes and xenobiotic-process context fit the claims. |
| schema | /private/tmp/cm-review-session/batch-14/000369/child-schema-semantics.json; Literal role, origin, state, scope and cultivation definitions | supports | Complex-substrate degradation is not restricted to polymers. Predicted potential, observed removal, stock concentration and community-level scope remain distinct. |
| gtdb | /private/tmp/cm-review-session/batch-14/000369/child-gtdb-crosswalk.json; All six current taxon resolutions and mapping snapshot | supports | Four exact IDs resolve; B. pumilus and B. mojavensis name fallbacks remain ambiguous. Reference-taxon mappings do not classify the inoculated strains. |
| semantics | /private/tmp/cm-review-session/batch-14/000369/ontology-semantic-notes.json; Final source-aware semantic assessment | supports | Broad roles remain defensible with earlier-pesticide context. Two qualified nodes and no arrows remain appropriate; salinity, temperature, protocol detail and GTDB enrichment require curation. |
| prior-role-context | /private/tmp/cm-review-session/batch-14/000369/child-prior-pesticide-role-context.json; Independent bounded earlier-source assessment | supports | The earlier six-strain assays support broad roles, with no transfer of CAP/FBD conditions or respirometric percentages to the focal cyantraniliprole experiment. |
| resources | /private/tmp/cm-review-session/batch-14/000369/dataset-verification.json; Six direct ENA marker identities and source Data Availability | supports | All six encoded partial 16S markers match strain codes and taxon identities. Their 2019 sampling and 2021 submission predate the current experiment; request-only data availability creates no missing-deposit finding. |
| snippets | /private/tmp/cm-review-session/batch-14/000369/snippet-audit.json; All 24 canonical excerpt placements | supports | All 24 match fresh source and cache under the stated normalization. Exact matching does not resolve contradictory source sections or establish entailment. |
| provenance | /private/tmp/cm-review-session/batch-14/000369/provenance-audit.json; Four histories, exact batch28 focal row, cohort context and current issues | supports | Earlier graph and numeric repairs remain preserved. Open issues 869/870 do not negate repaired current wording; 1368 is closed and 1371 tracks current condition discrepancies. No shared issue is closed here. |
| inspection | /private/tmp/cm-review-session/batch-14/000369/inspect.json; 33 official immutable inputs | supports | Target, 21 authorities and eleven focal contexts were inspected before judgment; source discovery included ignored files. |
| assets | /private/tmp/cm-review-session/batch-14/000369/lead-source-assets.json; Actual primary retrieval and declared inventory | supports | Fresh full JATS, five linked figures, eight tables and 129 references were inspected. No supplement is declared in the JATS inventory. Incorrect MED availability flags and failed publisher routes remain preserved. |
| lead-read | /private/tmp/cm-review-session/batch-14/000369/lead-primary-read-scope.json; Exact lead reading boundaries | supports | Whole focal main and all five figures were read, plus bounded earlier-source sections. No full audit of the 129 cited papers, raw data or prior-paper figures is claimed. |
| source-scope | /private/tmp/cm-review-session/batch-14/000369/source-audit.json; Final scientific assessment | supports | Completed scientific review finds one major and three minor issues while preserving the existing qualified graph and principal removal result. |
| selector-correction | /private/tmp/cm-review-session/batch-14/000369/source-selector-clarification.json; Exact correction to source-audit finding 3 scope | supports | The actual slot is gtdb_grounding_status. The frozen source receipt typo is corrected explicitly; the later root clarification confirms schema support for AMBIGUOUS. No finding or score changes. |
| root-source | /private/tmp/cm-review-session/batch-14/000369/root-independent-source-audit.json; Independent source assessment | supports | Root independently agrees with completed science, one P2 and three P3 findings after whole focal source and bounded earlier-role review. |
| gtdb-status | /private/tmp/cm-review-session/batch-14/000369/root-gtdb-status-clarification.json; Actual schema AMBIGUOUS and candidate-list support | supports | Future curation may mark the two unresolved name routes AMBIGUOUS with verified gtdb_candidates, without assigning either studied strain to a candidate. |
| metrics | /private/tmp/cm-review-session/batch-14/000369/support-final-audit.json; Distinct final support and literal metrics | supports | Completeness 85; quality base 125 minus 10 and 6 gives raw 109, capped at 100. Scores do not validate biological claims. |
| support-manifest | /private/tmp/cm-review-session/batch-14/000369/supporting-artifact-manifest.json; Frozen final supporting artifacts | supports | Final support follows reconciliation; earlier receipts and failed retrievals remain unchanged. |
| auxiliary | /private/tmp/cm-review-session/batch-14/000369/auxiliary-frozen-manifest.json; Native and authority receipts | supports | Eight native checks pass; ten ID-label pairs match and all 33 inspected inputs remain unchanged. |
| final-native | /private/tmp/cm-review-session/batch-14/000369/final-validator-summary.json; Actual eight native command receipts | supports | All focused checks pass. A zero reference-issue count is not a count of checked excerpts or evidence of causal validity. |
| corpus-context | /private/tmp/cm-review-session/batch-14/000369/child-current-corpus-context.json; Fresh batch14 corpus baseline | supports | Both corpus commands exited 1 with 44 warnings across 16 of 477 records and zero errors; these are nonrequired contextual checks. |
| adapter | /private/tmp/cm-review-session/batch-14/000369/adapter-check.json; Owned-runtime optional adapter availability | supports | The optional adapter is unavailable in the owned runtime. The dated prior filename-search boundary is explicit; no external-checkout adapter was executed. |
| check-validate | /private/tmp/cm-review-session/batch-14/000369/validate.json; Actual command/stdout/stderr | supports | Native exit 0; scientific support is assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-14/000369/validate-strict.json; Actual command/stdout/stderr | supports | Native exit 0; scientific support is assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-14/000369/validate-terms.json; Actual command/stdout/stderr | supports | Native exit 0; scientific support is assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-14/000369/validate-references-explained.json; Actual command/stdout/stderr | supports | Native exit 0; scientific support is assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-14/000369/validate-gtdb.json; Actual command/stdout/stderr | supports | Native exit 0; scientific support is assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-14/000369/validate-gtdb-domain.json; Actual command/stdout/stderr | supports | Native exit 0; scientific support is assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-14/000369/validate-history.json; Actual command/stdout/stderr | supports | Native exit 0; scientific support is assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-14/000369/normalize-cache-names-check.json; Actual command/stdout/stderr | supports | Native exit 0; scientific support is assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-14/audit-network.json; Fresh batch14 corpus baseline | supports | Actual exit 1; 44 warnings across 16 of 477 records, zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-14/check-network-quality.json; Fresh batch14 corpus baseline | supports | Actual exit 1; 44 warnings across 16 of 477 records, zero errors. |
| locator-verification | /private/tmp/cm-review-session/batch-14/000369/source-locator-verification.json; Actual complete JATS heading inventory and all nine primary evidence locators | supports | Direct heading checks confirm HPLC Methods 2.10 and pathway Methods 2.11 / Results 3.6.3. The prior candidate shorthand is corrected append-only; source science and findings remain unchanged. |

## Limits And Additional Notes

- The publication itself conflicts on salinity optimum and broad-assay temperature. Additional unencoded differences include optimization sampling at 15 versus 16 days, Table 4 caption versus column concentrations, prose versus Table 2 treatment count, and some control values; these were not silently reconciled or scored as new record errors.
- Predicted enzyme coverage, OD600 growth and DCPIP decolorization are distinct from measured enzyme flux and complete chemical fate. HPLC disappearance does not establish mineralization, detoxification, reciprocal fitness or a necessary/sufficient reduced consortium.
- Only role-relevant sections of ref32 were read; its CAP/FBD soil assays do not measure individual cyantraniliprole flux here. No whole earlier-paper, raw-sequence or statistical reanalysis is claimed.
- The actual fresh JATS and five figures resolve erroneous MED access flags. No supplementary material is declared in that inventory; this is an inspected-source boundary, not a global absence claim.
- Two node assessments bind their exact canonical excerpt selectors and SHA256 values, all six participants, retained evidence tiers and zero downstream arrows.
- The sole quotation is two words from Methods 2.8, Water Microcosm System, fourth direct paragraph. All other source content is paraphrased or referenced by exact selectors.
- All 33 official inputs remain unchanged. Native candidate validation and parent-owned saving/post-save gates follow this assessment; none is asserted in advance.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T024259Z-cyantraniliprole-fahmy-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Cyantraniliprole Fahmy T4 consortium record review
started_at: '2026-10-22T02:32:59.891734Z'
finished_at: '2026-10-22T02:42:59.557083Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, auxiliary authority and supporting reviewers;
    no person-level independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The six-strain identity, qualified predicted repertoire and HPLC removal
  node are supported. One major finding corrects the salinity optimum; three minor
  findings address the conflicting broad-assay temperature, recoverable protocol detail
  and four available GTDB mappings. Full focal source review is complete, with bounded
  earlier-strain evidence. Eight focused checks pass. Literal completeness is 85 and
  raw quality 109, capped at 100.
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
  - path: history/records/Cyantraniliprole_Fahmy_Consortium_T4/2026-09-13T231325Z-codex-59b4de.yaml
    sha256: 5acedb3c230b07e11a1dca30a44d69ad6c3d7dd9cd50933a8851a72ef3139d3d
    role: context
  - path: history/records/Cyantraniliprole_Fahmy_Consortium_T4/2026-09-13T232259Z-codex-a73a76.yaml
    sha256: 551588c8c11123deb30f566e62a1cf1622375aa4b7b53f3fd11ff6e0968fc7d9
    role: context
  - path: history/records/Cyantraniliprole_Fahmy_Consortium_T4/2026-10-02T054552Z-codex-c7c369.yaml
    sha256: b8d525a50c34128679ec1803675e4a6d6a82f6742aeef0b3faa9a67277e969af
    role: context
  - path: history/records/Cyantraniliprole_Fahmy_Consortium_T4/2026-10-06T045256Z-codex-c09567.yaml
    sha256: eb8118899b754f7eab9a6b7eb7b12c40d2dfbe97688f9a06cd632593af56f1e2
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    sha256: 0ecd37ff8b4675764844c6d704c634832fecd8635b80e6f9c5759c217345595c
    role: target
  - path: references_cache/PMID_42354927.txt
    sha256: 2b47a77cf230a1f61781cf3020710ad3e469dfe4fdebe0eb0c1981a457082f43
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch28.yaml
    sha256: 73b5f403e73107baf98d379cdc613b947a72382fddd9faf765b784cb63b98913
    role: context
  - path: reports/causal_graph_review/decisions/20261006-four-records-batch28.yaml
    sha256: b6c1f9081c2d4a75c3db896187e3e20dffac6d339c7ad455c03e07719c17a29f
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
- target_id: CommunityMech:000369
  path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
  label: Cyantraniliprole Fahmy Consortium T4
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    role: canonical_record
scope:
  description: Whole focal record and full fresh manuscript, all five figures/eight
    tables, local authorities and exact historical context; bounded earlier primary
    strain assays.
  selection: Only released CommunityMech:000369 in owned batch14.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000369
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000369
  command: just --no-dotenv validate kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused record/history gate; cache-name preflight is corpus-wide.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000369
  command: just --no-dotenv validate-strict kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    --out /private/tmp/cm-review-session/batch-14/000369/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused record/history gate; cache-name preflight is corpus-wide.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000369
  command: just --no-dotenv validate-terms kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused record/history gate; cache-name preflight is corpus-wide.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000369
  command: just --no-dotenv validate-references-explained kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused record/history gate; cache-name preflight is corpus-wide.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000369
  command: just --no-dotenv validate-gtdb kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused record/history gate; cache-name preflight is corpus-wide.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000369
  command: just --no-dotenv validate-gtdb-domain kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused record/history gate; cache-name preflight is corpus-wide.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000369
  command: just --no-dotenv validate-history history/records/Cyantraniliprole_Fahmy_Consortium_T4
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused record/history gate; cache-name preflight is corpus-wide.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000369
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused record/history gate; cache-name preflight is corpus-wide.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000369
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, not a focused failure assigned entirely
    to this record.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000369
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, not a focused failure assigned entirely
    to this record.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in the owned runtime.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - adapter
  scope_note: No external-checkout adapter executed.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
  locator: Whole maintained record
  summary: Six named strains form the T4 benchmark consortium. Two untyped community-level
    nodes distinguish predicted repertoire from HPLC removal; no downstream arrows
    are encoded.
  support: supports
  accessed_at: '2026-10-22T02:41:16.340871Z'
- evidence_id: identity
  kind: primary_source
  reference: PMID:42354927; DOI:10.3390/microorganisms14061303
  locator: Methods 2.2; Tables 2–3
  summary: T4 is the previously characterized six-strain benchmark, distinct from
    newly assembled T1–T3. Source strain codes and marker accessions match the record.
  support: supports
  accessed_at: '2026-10-22T02:41:16.340941Z'
  snapshot_sha256: 7bc15dfb10d2de6e34ae432bae1f7fcf6d77e173730e988ca2e36e35751e6ca8
- evidence_id: salinity
  kind: primary_source
  reference: PMID:42354927; DOI:10.3390/microorganisms14061303
  locator: Abstract; Results 3.2.3, sole paragraph; Figure 1C; Discussion
  summary: The abstract reports 0.5–5.0% NaCl as optimal, but detailed Results and
    Figure 1C show highest OD600 growth at 0.0–0.5%. Tolerance across the tested range
    does not make that entire range optimal.
  support: supports
  accessed_at: '2026-10-22T02:41:16.341387Z'
  snapshot_sha256: 7bc15dfb10d2de6e34ae432bae1f7fcf6d77e173730e988ca2e36e35751e6ca8
- evidence_id: recipe
  kind: primary_source
  reference: PMID:42354927; DOI:10.3390/microorganisms14061303
  locator: Methods 2.1 Pesticides and Media, sole paragraph; Methods 2.4, sole paragraph
  summary: The complete MSM formulation and OVAT growth assay are available. One millilitre
    of 10^7 CFU/mL inoculum enters 250 mL broth with 50 mg/L cyantraniliprole; OD600
    is the readout.
  support: supports
  accessed_at: '2026-10-22T02:41:16.341517Z'
  snapshot_sha256: 7bc15dfb10d2de6e34ae432bae1f7fcf6d77e173730e988ca2e36e35751e6ca8
- evidence_id: diamide
  kind: primary_source
  reference: PMID:42354927; DOI:10.3390/microorganisms14061303
  locator: Methods 2.7 Biodegradation of Some Diamide Pesticides, sole paragraph;
    Table 6
  summary: The five separate 100 mg/L diamide treatments yield T4 OD600 values 2.211–2.272.
    Methods specifies 30 °C, while the table caption specifies 35 °C; the source does
    not resolve this conflict.
  support: supports
  accessed_at: '2026-10-22T02:41:16.341644Z'
  snapshot_sha256: 7bc15dfb10d2de6e34ae432bae1f7fcf6d77e173730e988ca2e36e35751e6ca8
- evidence_id: microcosm
  kind: primary_source
  reference: PMID:42354927; DOI:10.3390/microorganisms14061303
  locator: Methods 2.8 → Water Microcosm System, fourth direct paragraph for quote;
    surrounding preparation, nutrient and inoculation paragraphs; Table 2
  summary: Water portions are placed in sealed plastic jars. The protocol supplies
    stock preparation, initial mixing, C:N:P adjustment and nutrient sources. Stock
    concentration and nominal water volume must remain distinct from final inoculum
    concentration and total liquid volume.
  support: supports
  accessed_at: '2026-10-22T02:41:16.341763Z'
  snapshot_sha256: 7bc15dfb10d2de6e34ae432bae1f7fcf6d77e173730e988ca2e36e35751e6ca8
  quote: plastic jars
- evidence_id: removal
  kind: primary_source
  reference: PMID:42354927; DOI:10.3390/microorganisms14061303
  locator: Methods 2.10 Cyantraniliprole (CPS) Residue Analysis; Results 3.6.2 and
    Table 7; Figure 3
  summary: 'T4 recovered zero-day residue is 57.79 mg/L and day-20 residue is 1.00
    mg/L: 98.27% removal relative to the recovered baseline. The treatment is nominally
    60 mg/L in native water at 30 °C; this is parent-compound disappearance, not demonstrated
    mineralization or detoxification.'
  support: supports
  accessed_at: '2026-10-22T02:41:16.341880Z'
  snapshot_sha256: 7bc15dfb10d2de6e34ae432bae1f7fcf6d77e173730e988ca2e36e35751e6ca8
- evidence_id: prediction
  kind: primary_source
  reference: PMID:42354927; DOI:10.3390/microorganisms14061303
  locator: Methods 2.11 Cyantraniliprole Pathway Prediction; Results 3.6.3; Table
    8 and Figures 4–5; Discussion
  summary: Five enzyme classes and proposed pathway coverage are computational assignments.
    The source does not measure strain-resolved enzyme activity, exchange, flux or
    the performance of the proposed reduced consortium.
  support: supports
  accessed_at: '2026-10-22T02:41:16.341997Z'
  snapshot_sha256: 7bc15dfb10d2de6e34ae432bae1f7fcf6d77e173730e988ca2e36e35751e6ca8
- evidence_id: redox
  kind: primary_source
  reference: PMID:42354927; DOI:10.3390/microorganisms14061303
  locator: Methods 2.5–2.6; Results 3.3–3.4; Tables 4–5
  summary: T4 decolorizes DCPIP at 17 h; biomass and crystal-violet biofilm measurements
    are separate assays. These readouts do not establish product identities or direct
    catalytic flux.
  support: supports
  accessed_at: '2026-10-22T02:41:16.342115Z'
  snapshot_sha256: 7bc15dfb10d2de6e34ae432bae1f7fcf6d77e173730e988ca2e36e35751e6ca8
- evidence_id: prior-role
  kind: primary_source
  reference: DOI:10.3390/pr10122527
  locator: 'Recovered published PDF: Methods 2.1–2.7; Results 3.1 and 3.3; Table 5'
  summary: The exact six strains previously grew on chlorantraniliprole/flubendiamide
    and were tested individually by controlled soil respirometry. This supports broad
    pesticide-degrader capability, without proving individual cyantraniliprole turnover
    in the present consortium. Only these bounded earlier-source sections were assessed.
  support: supports
  accessed_at: '2026-10-22T02:41:16.342231Z'
  snapshot_sha256: 0b362c20542fb91e0316e3dfd4a94d7278b2957a86274cc2272329dc540ff5b1
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000369/ontology-authority.json
  locator: Ten ID-label pairs, definitions and 26 placements
  summary: All encoded labels match; cyantraniliprole chemistry, laboratory/freshwater
    scopes and xenobiotic-process context fit the claims.
  support: supports
  accessed_at: '2026-10-22T02:41:16.343547Z'
  snapshot_sha256: 84c73d38a8fcb05f38d8cbb4799d9a298ac480a838923924e0195d6d89614114
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000369/child-schema-semantics.json
  locator: Literal role, origin, state, scope and cultivation definitions
  summary: Complex-substrate degradation is not restricted to polymers. Predicted
    potential, observed removal, stock concentration and community-level scope remain
    distinct.
  support: supports
  accessed_at: '2026-10-22T02:41:16.343763Z'
  snapshot_sha256: ff82f1a1d4c54a280dd499072c895c733bd860b1d4f40c0e2ee0379298f99635
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000369/child-gtdb-crosswalk.json
  locator: All six current taxon resolutions and mapping snapshot
  summary: Four exact IDs resolve; B. pumilus and B. mojavensis name fallbacks remain
    ambiguous. Reference-taxon mappings do not classify the inoculated strains.
  support: supports
  accessed_at: '2026-10-22T02:41:16.343964Z'
  snapshot_sha256: b5c03667bf99227c1490f4a6b4c1005e4b72b263116adc259d6cfea8b4c7e0b6
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000369/ontology-semantic-notes.json
  locator: Final source-aware semantic assessment
  summary: Broad roles remain defensible with earlier-pesticide context. Two qualified
    nodes and no arrows remain appropriate; salinity, temperature, protocol detail
    and GTDB enrichment require curation.
  support: supports
  accessed_at: '2026-10-22T02:41:16.344121Z'
  snapshot_sha256: a3af31d1c4fa9638d4b5fda4915ad06c3033e6745b3c60e5c1dfe8d77837ac6d
- evidence_id: prior-role-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/child-prior-pesticide-role-context.json
  locator: Independent bounded earlier-source assessment
  summary: The earlier six-strain assays support broad roles, with no transfer of
    CAP/FBD conditions or respirometric percentages to the focal cyantraniliprole
    experiment.
  support: supports
  accessed_at: '2026-10-22T02:41:16.344279Z'
  snapshot_sha256: ad52ac0495b5b0fe8930afe1ee59655758366b8c91885ce5e1637b267bdde3d3
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/dataset-verification.json
  locator: Six direct ENA marker identities and source Data Availability
  summary: All six encoded partial 16S markers match strain codes and taxon identities.
    Their 2019 sampling and 2021 submission predate the current experiment; request-only
    data availability creates no missing-deposit finding.
  support: supports
  accessed_at: '2026-10-22T02:41:16.344422Z'
  snapshot_sha256: 69ec13c8992fb6c572c22983ab019db77823791df844f25aed8065a4ce7837cc
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/snippet-audit.json
  locator: All 24 canonical excerpt placements
  summary: All 24 match fresh source and cache under the stated normalization. Exact
    matching does not resolve contradictory source sections or establish entailment.
  support: supports
  accessed_at: '2026-10-22T02:41:16.344580Z'
  snapshot_sha256: f7bf6c5a584a30cd321a29b1393b63aad3a9f0b5bf725f0511349815048ceac1
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-14/000369/provenance-audit.json
  locator: Four histories, exact batch28 focal row, cohort context and current issues
  summary: Earlier graph and numeric repairs remain preserved. Open issues 869/870
    do not negate repaired current wording; 1368 is closed and 1371 tracks current
    condition discrepancies. No shared issue is closed here.
  support: supports
  accessed_at: '2026-10-22T02:41:16.344734Z'
  snapshot_sha256: 59e82a9bb89d109bf43ee0e00779225b635efbc85a30096b6b1d9596e1a46428
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/inspect.json
  locator: 33 official immutable inputs
  summary: Target, 21 authorities and eleven focal contexts were inspected before
    judgment; source discovery included ignored files.
  support: supports
  accessed_at: '2026-10-22T02:41:16.344873Z'
  snapshot_sha256: a29d567fbcbe68104873dfd6bf7f5ea95b892bb9d5b8843e72a0f39ad60389f4
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/lead-source-assets.json
  locator: Actual primary retrieval and declared inventory
  summary: Fresh full JATS, five linked figures, eight tables and 129 references were
    inspected. No supplement is declared in the JATS inventory. Incorrect MED availability
    flags and failed publisher routes remain preserved.
  support: supports
  accessed_at: '2026-10-22T02:41:16.344907Z'
  snapshot_sha256: 98565254a50b0e63ffc77bf33dc25898e01922999c729322492023b1ecf0c7f5
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/lead-primary-read-scope.json
  locator: Exact lead reading boundaries
  summary: Whole focal main and all five figures were read, plus bounded earlier-source
    sections. No full audit of the 129 cited papers, raw data or prior-paper figures
    is claimed.
  support: supports
  accessed_at: '2026-10-22T02:41:16.345046Z'
  snapshot_sha256: 804c9fd98ba380016a604a1241fbcb1a61ad43c0dfb897972efbf2c1cc56824e
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/source-audit.json
  locator: Final scientific assessment
  summary: Completed scientific review finds one major and three minor issues while
    preserving the existing qualified graph and principal removal result.
  support: supports
  accessed_at: '2026-10-22T02:41:16.345260Z'
  snapshot_sha256: 5b29f785f1e588693a22f0d95a76ffd1a24c1fdaf0e94cb37dfa536a81a380b1
- evidence_id: selector-correction
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/source-selector-clarification.json
  locator: Exact correction to source-audit finding 3 scope
  summary: The actual slot is gtdb_grounding_status. The frozen source receipt typo
    is corrected explicitly; the later root clarification confirms schema support
    for AMBIGUOUS. No finding or score changes.
  support: supports
  accessed_at: '2026-10-22T02:41:16.345995Z'
  snapshot_sha256: a9b6bb9f67f0acc7dac867e2edd7c636ab1e40645ee553800c785c95372c1a12
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/root-independent-source-audit.json
  locator: Independent source assessment
  summary: Root independently agrees with completed science, one P2 and three P3 findings
    after whole focal source and bounded earlier-role review.
  support: supports
  accessed_at: '2026-10-22T02:41:16.346162Z'
  snapshot_sha256: 17bb1c2081eb8d5add87a29e50d5bc73e0776e6e4c99d52adf4530572cd2f50f
- evidence_id: gtdb-status
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000369/root-gtdb-status-clarification.json
  locator: Actual schema AMBIGUOUS and candidate-list support
  summary: Future curation may mark the two unresolved name routes AMBIGUOUS with
    verified gtdb_candidates, without assigning either studied strain to a candidate.
  support: supports
  accessed_at: '2026-10-22T02:41:16.346333Z'
  snapshot_sha256: ed9f7e40885d9f052d22d6f0a4e4d108bc6b2b4fbfb2e406a7e4e06f19536cb3
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/support-final-audit.json
  locator: Distinct final support and literal metrics
  summary: Completeness 85; quality base 125 minus 10 and 6 gives raw 109, capped
    at 100. Scores do not validate biological claims.
  support: supports
  accessed_at: '2026-10-22T02:41:16.346377Z'
  snapshot_sha256: 3e93c421658726cfed6c2b6ee5d0f8a971acdcd6547b6eb99d25e6d3aba5fb44
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/supporting-artifact-manifest.json
  locator: Frozen final supporting artifacts
  summary: Final support follows reconciliation; earlier receipts and failed retrievals
    remain unchanged.
  support: supports
  accessed_at: '2026-10-22T02:41:16.346405Z'
  snapshot_sha256: c413e21b8bdbff5343ae56a3e95aaaf82111b8c0775ad88910b76af1aa31b751
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/auxiliary-frozen-manifest.json
  locator: Native and authority receipts
  summary: Eight native checks pass; ten ID-label pairs match and all 33 inspected
    inputs remain unchanged.
  support: supports
  accessed_at: '2026-10-22T02:41:16.346613Z'
  snapshot_sha256: ecdc13a74686540ece009addb22914e18dae60346bd4e124c783b307e9b26b8e
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/final-validator-summary.json
  locator: Actual eight native command receipts
  summary: All focused checks pass. A zero reference-issue count is not a count of
    checked excerpts or evidence of causal validity.
  support: supports
  accessed_at: '2026-10-22T02:41:16.346648Z'
  snapshot_sha256: 22fe107d890bd1e56108e68cc95a3e95e51938b3df3577cad720b92415b27d6e
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/child-current-corpus-context.json
  locator: Fresh batch14 corpus baseline
  summary: Both corpus commands exited 1 with 44 warnings across 16 of 477 records
    and zero errors; these are nonrequired contextual checks.
  support: supports
  accessed_at: '2026-10-22T02:41:16.346838Z'
  snapshot_sha256: 393d7a3e540552b84a87ac6376e25a6fa774c12031d569e5e3f0688138836c6c
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/adapter-check.json
  locator: Owned-runtime optional adapter availability
  summary: The optional adapter is unavailable in the owned runtime. The dated prior
    filename-search boundary is explicit; no external-checkout adapter was executed.
  support: supports
  accessed_at: '2026-10-22T02:41:16.346991Z'
  snapshot_sha256: c1c091f5ba106d75749d66590ea5c01b83a1331d8b4d501b9deff9136f0a3a7e
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/validate.json
  locator: Actual command/stdout/stderr
  summary: Native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:41:16.347395Z'
  snapshot_sha256: 225a55ac3506413830cc81570aa37b052d7c07c4535d66572650b6de6cd5f546
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/validate-strict.json
  locator: Actual command/stdout/stderr
  summary: Native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:41:16.347570Z'
  snapshot_sha256: dc77d0e6c2c98d5d7c6890c6472f45131902fe8bd8a543b7fbd7b0961a439cb6
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/validate-terms.json
  locator: Actual command/stdout/stderr
  summary: Native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:41:16.347750Z'
  snapshot_sha256: 1fa1d29e3d0ed9100e6fa3d6ed801e6972e0d0de8c02d5496472fa8a21577cad
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/validate-references-explained.json
  locator: Actual command/stdout/stderr
  summary: Native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:41:16.348009Z'
  snapshot_sha256: a7697d9ea5790b7390804c24ce9a325871824828894cb0461490594df3dc44e8
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/validate-gtdb.json
  locator: Actual command/stdout/stderr
  summary: Native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:41:16.348359Z'
  snapshot_sha256: e2042721c61726a483dbe2a629b8a4dae0f6ad9878eef2dbfe88907c6be6982a
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/validate-gtdb-domain.json
  locator: Actual command/stdout/stderr
  summary: Native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:41:16.348516Z'
  snapshot_sha256: 7ab1110fc8f5483629395688163cd6b62f5881568f282d72ee20fee56a6c71d8
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/validate-history.json
  locator: Actual command/stdout/stderr
  summary: Native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:41:16.348677Z'
  snapshot_sha256: 420ef7298d80de4536a56f8cf320194a7edd5788dd7cde05565d4d2cca02a387
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/normalize-cache-names-check.json
  locator: Actual command/stdout/stderr
  summary: Native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T02:41:16.348875Z'
  snapshot_sha256: 44e5c325796770ed82db40fef0fb5a5b9830a2f56e6bbc5d5b9a94bc73097ef5
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/audit-network.json
  locator: Fresh batch14 corpus baseline
  summary: Actual exit 1; 44 warnings across 16 of 477 records, zero errors.
  support: supports
  accessed_at: '2026-10-22T02:41:16.349205Z'
  snapshot_sha256: 3110e0bb1dbe3ea63b81aea82871ac4adb2915c8fce1d15249422d0f5db266c6
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/check-network-quality.json
  locator: Fresh batch14 corpus baseline
  summary: Actual exit 1; 44 warnings across 16 of 477 records, zero errors.
  support: supports
  accessed_at: '2026-10-22T02:41:16.349454Z'
  snapshot_sha256: 18896ef4136601b37550cb5612abc06784abcbf982e4778cbf2b9c10368cb66a
- evidence_id: locator-verification
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000369/source-locator-verification.json
  locator: Actual complete JATS heading inventory and all nine primary evidence locators
  summary: Direct heading checks confirm HPLC Methods 2.10 and pathway Methods 2.11
    / Results 3.6.3. The prior candidate shorthand is corrected append-only; source
    science and findings remain unchanged.
  support: supports
  accessed_at: '2026-10-22T02:42:59.556865Z'
  snapshot_sha256: ede007599e7e5be09eec37476f2155bba7de0275ff78936bd8caf00e58bc005b
assessments:
- assessment_id: identity
  area: identity
  topic: Six-strain benchmark and community scope
  outcome: supported
  summary: The defined T4 inoculum is correctly distinguished from native water microbes
    and the other consortia.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - identity
  - resources
  - schema
  - prior-role
  dimensions:
  - name: strain_scope
    value: AZFS3 / AZFS5 / AZFS15 / AZFS18 / KZFS4 / KZFS11
    definition: Six deliberate benchmark inoculum members; native water background
      remains present.
    evidence_ids:
    - identity
    - resources
  - name: experimental_setting
    value: Laboratory MSM assays and augmented freshwater microcosms
    definition: Distinct growth, proxy and HPLC experiments.
    evidence_ids:
    - recipe
    - diamide
    - microcosm
  details: Retain SYNTHETIC origin, ENGINEERED state and BIOREMEDIATION. Exact source
    strains are AZFS3, AZFS5, AZFS15, AZFS18, KZFS4 and KZFS11. Their marker-identified
    species/subspecies descriptors are not study-strain genome classifications.
- assessment_id: node-0
  area: graph
  topic: T4 distributed cyantraniliprole enzyme potential
  outcome: supported
  summary: Retain predicted enzyme potential with its existing computational qualifications.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - prediction
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[0]; name T4 distributed cyantraniliprole
    enzyme potential; scope COMMUNITY_LEVEL; interaction_type absent. Actual encoded
    taxa: {"source": null, "target": null, "participants": [{"id": "NCBITaxon:135461",
    "label": "Bacillus subtilis subsp. subtilis"}, {"id": "NCBITaxon:1408", "label":
    "Bacillus pumilus"}, {"id": "NCBITaxon:72360", "label": "Bacillus mojavensis"},
    {"id": "NCBITaxon:2026194", "label": "Bacillus paramycoides"}, {"id": "NCBITaxon:287",
    "label": "Pseudomonas aeruginosa"}, {"id": "NCBITaxon:323284", "label": "Alcaligenes
    aquatilis"}]}. Canonical evidence bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "460ead14eda420110d469d8295ccee0dcf96814a945b55c1da99247a695cf5c6",
    "reference": "PMID:42354927", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}].
    Snippet-audit SHA256 f7bf6c5a584a30cd321a29b1393b63aad3a9f0b5bf725f0511349815048ceac1.
    PMID:42354927 Methods 2.11 and Results 3.6.3, Table 8, Figures 4–5. Retain SUPPORT
    / COMPUTATIONAL: post-assay repertoire predictions do not establish enzyme expression/activity,
    exchange, reciprocal fitness or the necessity/sufficiency of a four-strain subset.'
- assessment_id: node-1
  area: graph
  topic: HPLC-confirmed cyantraniliprole removal
  outcome: supported
  summary: Retain the measured community-level parent-removal outcome.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - removal
  - microcosm
  - snippets
  details: 'Exact selector ecological_interactions[1]; name HPLC-confirmed cyantraniliprole
    removal; scope COMMUNITY_LEVEL; interaction_type absent. Actual encoded taxa:
    {"source": null, "target": null, "participants": [{"id": "NCBITaxon:135461", "label":
    "Bacillus subtilis subsp. subtilis"}, {"id": "NCBITaxon:1408", "label": "Bacillus
    pumilus"}, {"id": "NCBITaxon:72360", "label": "Bacillus mojavensis"}, {"id": "NCBITaxon:2026194",
    "label": "Bacillus paramycoides"}, {"id": "NCBITaxon:287", "label": "Pseudomonas
    aeruginosa"}, {"id": "NCBITaxon:323284", "label": "Alcaligenes aquatilis"}]}.
    Canonical evidence bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "da478a74902b1891779aa4b92b468bfe635f8f82bf5f2faed204c9d53f5176ef",
    "reference": "PMID:42354927", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet-audit SHA256 f7bf6c5a584a30cd321a29b1393b63aad3a9f0b5bf725f0511349815048ceac1.
    PMID:42354927 Abstract removal sentence; Results 3.6.2, Table 7 and Figure 3.
    Retain SUPPORT / IN_VITRO: observed HPLC parent decline from 57.79 to 1.00 mg/L
    over 20 days at 30 °C, with native-water and nutrient-control context. No product
    balance, detoxification, mineralization or individual member contribution is established.'
- assessment_id: graph-boundary
  area: graph
  topic: Zero downstream arrows
  outcome: supported
  summary: Predicted repertoire and measured removal remain separate observations.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - prediction
  - removal
  - provenance
  details: No directed causal edge is warranted solely by their occurrence in the
    same study. Both nodes retain all six participants, with no encoded pairwise source
    or target.
- assessment_id: roles
  area: evidence
  topic: Broad degrader roles versus current mechanism
  outcome: supported
  summary: Prior exact-strain pesticide assays support the broad role annotations.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - prior-role
  - prior-role-context
  - schema
  - prediction
  details: Keep PRIMARY_DEGRADER without a polymer-only restriction. Add precise earlier-source
    context if enriching taxonomy evidence; neither membership excerpts nor predicted
    enzyme assignments prove individual cyantraniliprole flux. No role-deletion finding
    is made.
- assessment_id: conditions
  area: scope
  topic: Salinity optimum and broad-assay temperature
  outcome: concern
  summary: The record promotes a contradicted salinity optimum and omits a temperature
    disagreement.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - salinity
  - diamide
  details: Separate tested tolerance from highest OD600 growth and distinguish the
    broad diamide assay from optimization and water-removal conditions. Exact source
    excerpts may remain verbatim while explanations disclose the conflicts.
- assessment_id: protocol
  area: completeness
  topic: Recoverable recipe and inoculation details
  outcome: concern
  summary: The source supplies useful protocol detail beyond the current summary.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - recipe
  - microcosm
  - redox
  details: Retain source-specific units and hydrate forms, stock versus final inoculum,
    water portion versus total liquid volume, and assay-specific shaking. Batch/OTHER
    remains appropriate; analytical sampling does not imply feeding or medium replacement.
- assessment_id: grounding
  area: grounding
  topic: Ontology and current GTDB scope
  outcome: concern
  summary: Ontology labels fit, and four unresolved reference taxa can be grounded.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - ontology
  - gtdb
  - schema
  - gtdb-status
  details: Four exact-ID candidates are available; two ambiguous name routes can be
    represented as AMBIGUOUS with candidate lists. No forced strain classification,
    NCBI relabeling or guessed genome assignment follows.
- assessment_id: resources
  area: provenance
  topic: Markers and experiment data
  outcome: supported
  summary: Existing marker identities are verified without promoting them to current
    experiment deposits.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - resources
  - identity
  details: LC599401–LC599406 are partial 16S sequences with exact strain associations.
    The paper offers further experiment data on request; no mandatory archive omission
    is inferred and no contact was made.
- assessment_id: prior
  area: ownership
  topic: Maintained record and prior decisions
  outcome: supported
  summary: The focal YAML owns future repairs; historical observations remain immutable.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - inspection
  - provenance
  - selector-correction
  details: Preserve current exponent and recovered-baseline fixes, zero graph arrows
    and exact historical scope. No issue status, cache or history entry is changed
    by this review.
- assessment_id: access
  area: scope
  topic: Complete focal source coverage
  outcome: supported
  summary: Actual full text and all declared figures resolve the misleading metadata
    access flags.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - assets
  - lead-read
  - root-source
  details: All eight tables and 129 reference entries were read; the actual JATS declares
    no supplement. Earlier ref32 was read only for identity and role-relevant methods/results,
    without expanding to a full citation audit.
- assessment_id: native
  area: schema
  topic: Native validation and exact excerpts
  outcome: supported
  summary: Eight focused checks pass; all 24 excerpts match fresh source and cache.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - final-native
  - auxiliary
  - snippets
  - corpus-context
  - adapter
  details: The separate corpus failures and unavailable optional adapter remain explicit.
    Deterministic passes do not resolve source contradictions.
- assessment_id: metrics
  area: completeness
  topic: Two literal native scores
  outcome: supported
  summary: Completeness 85; raw quality 109, capped at 100.
  target_ids:
  - CommunityMech:000369
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required fields/roles + 5 environment + 10 at least three factors
      + 0 fewer than three nodes + 5 external resources + 10 medium + 0 datasets +
      5 metabolites = 85.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 - 1 major*10 - 3 minor*2 + 20*min((2 evidence/2 nodes)/2,1) +
      15 COMPLETE = 109 raw, capped 100. Two untyped nodes, zero arrows. Scores do
      not certify science.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 1
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
- finding_id: salinity-optimum
  issue_key: cm-000369-salinity-optimum
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: The asserted optimum materially misstates detailed experimental
    results.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Distinguish the detailed growth optimum from the abstract range
  description: Current optimized-condition fields repeat 0.5–5.0% NaCl, despite Results
    3.2.3 and Figure 1C locating maximal OD600 growth at 0.0–0.5%. The source contradiction
    needs explicit treatment.
  target_ids:
  - CommunityMech:000369
  field_paths:
  - environmental_factors[4].value
  - environmental_factors[4].evidence[0].explanation
  - growth_media[0].salinity
  - growth_media[0].evidence[1].explanation
  evidence_ids:
  - salinity
  - recipe
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    role: canonical_record
  ownership_note: Future curation belongs to the maintained focal record. Shared and
    historical issues are context, not automatically superseded or closed.
- finding_id: assay-temperature
  issue_key: cm-000369-assay-temperature
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: Bounded source qualification, protocol completeness or taxonomic
    provenance gap; principal community identity and qualified graph remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Disclose the broad-diamide temperature conflict
  description: Table 6 supports the encoded 35 °C, while Methods 2.7 specifies 30
    °C. Reporting only the former conceals an unresolved source discrepancy.
  target_ids:
  - CommunityMech:000369
  field_paths:
  - environmental_factors[3].description
  - growth_media[1].temperature
  - growth_media[1].evidence[0].explanation
  evidence_ids:
  - diamide
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    role: canonical_record
  ownership_note: Future curation belongs to the maintained focal record. Shared and
    historical issues are context, not automatically superseded or closed.
- finding_id: protocol-detail
  issue_key: cm-000369-protocol-detail
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded source qualification, protocol completeness or taxonomic
    provenance gap; principal community identity and qualified graph remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Add available assay-specific medium and inoculation detail
  description: The record summarizes MSM and NPK but omits the recoverable quantitative
    recipe, actual nutrient sources and inoculum/vessel preparation. This is an enrichment
    gap, not a claim that the paper lacks Methods.
  target_ids:
  - CommunityMech:000369
  field_paths:
  - growth_media[0].composition
  - growth_media[0].preparation_notes
  - growth_media[1].preparation_notes
  - growth_media[2].composition
  - growth_media[2].preparation_notes
  - cultivation_setup[0].instrument_detail
  - cultivation_setup[0].controls_notes
  evidence_ids:
  - recipe
  - microcosm
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    role: canonical_record
  ownership_note: Future curation belongs to the maintained focal record. Shared and
    historical issues are context, not automatically superseded or closed.
- finding_id: gtdb-resolution
  issue_key: cm-000369-gtdb-resolution
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Bounded source qualification, protocol completeness or taxonomic
    provenance gap; principal community identity and qualified graph remain supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Document four available reference-taxon mappings
  description: All six taxa remain UNRESOLVED although four exact encoded IDs resolve
    in the inspected crosswalk. The other two name routes are ambiguous and should
    retain that unresolved boundary.
  target_ids:
  - CommunityMech:000369
  field_paths:
  - taxonomy[0].taxon_term.gtdb_grounding_status
  - taxonomy[3].taxon_term.gtdb_grounding_status
  - taxonomy[4].taxon_term.gtdb_grounding_status
  - taxonomy[5].taxon_term.gtdb_grounding_status
  evidence_ids:
  - gtdb
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    role: canonical_record
  ownership_note: Future curation belongs to the maintained focal record. Shared and
    historical issues are context, not automatically superseded or closed.
actions:
- action_id: qualify-salinity
  description: Correct the salinity claim while preserving source disagreement.
  finding_ids:
  - salinity-optimum
  target_ids:
  - CommunityMech:000369
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    role: canonical_record
  acceptance_checks:
  - Use Results 3.2.3 and Figure 1C to describe highest OD600 growth at 0.0–0.5% NaCl.
    Distinguish this from growth across the four tested concentrations and from the
    abstract 0.5–5.0% statement.
  - Keep quoted source text exact; qualify or replace its associated claim-local explanation.
    Do not present the OD600 optimum as a directly measured degradation-rate optimum,
    or confuse MSM 500 mg/L NaCl with 0.5%.
- action_id: qualify-temperature
  description: Preserve the unresolved assay temperature.
  finding_ids:
  - assay-temperature
  target_ids:
  - CommunityMech:000369
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    role: canonical_record
  acceptance_checks:
  - Record Methods 2.7 at 30 °C and Table 6 at 35 °C, explicitly unresolved. Do not
    silently choose one, merge it with optimization 30–35 °C, or transfer the separate
    water-microcosm setpoint.
  - Retain five separate 100 mg/L treatments and the measured OD600 range, with growth
    rather than complete-degradation interpretation.
- action_id: recover-protocol
  description: Enrich each assay with its own Methods context.
  finding_ids:
  - protocol-detail
  target_ids:
  - CommunityMech:000369
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    role: canonical_record
  acceptance_checks:
  - 'Methods 2.1 MSM in mg/L: K2HPO4 500; KH2PO4 250; NaCl 500; (NH4)2SO4 230; CaCl2·2H2O
    7.5; MgSO4·7H2O 100; source-printed MnSO4·7H2O 100; FeCl3 1; distilled water to
    1 L, pH 7.0. Preserve the source formula without silently correcting it or borrowing
    an unrelated medium.'
  - 'Methods 2.4: 1 mL of 10^7 CFU/mL stock into 250 mL MS broth, 50 mg/L cyantraniliprole,
    OVAT/OD600, 150 rpm. Methods 2.7 separately specifies TSB preculture, washing,
    250 mL Erlenmeyer vessels, 0.5 g/L NaCl, 11 days and 150 rpm; vessel capacity
    is not an established working volume.'
  - 'Methods 2.8: 500 mL freshwater portions, sealed plastic jars, 20 mL of the 10^7
    CFU/mL stock, initial mixing and C:N:P 100:15:1 using ammonium sulfate and KH2PO4.
    Do not label stock density as final density, manufacture a commercial NPK formulation,
    replace the stated water volume with 520 mL, or import continuous shaking.'
  - Retain native-water and uninoculated nutrient controls, 30 °C and 20-day HPLC
    scope. Keep DCPIP, biomass/biofilm and broad-diamide growth protocols distinct.
    Analytical sampling alone does not establish fed-batch operation.
  - Optional claim-local taxonomy evidence can cite ref32 Methods 2.2/2.5–2.7 and
    Results 3.3/Table 5 for prior CAP/FBD capability. Retain broad degrader roles
    without transferring prior substrates, percentages or individual activity to the
    focal cyantraniliprole experiment.
- action_id: resolve-gtdb
  description: Enrich reference-taxon grounding without classifying marker-identified
    strains.
  finding_ids:
  - gtdb-resolution
  target_ids:
  - CommunityMech:000369
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    role: canonical_record
  acceptance_checks:
  - 'Use exact-ID candidates: 135461→GTDB:s__Bacillus_subtilis (1.0,101 genomes);
    2026194→GTDB:s__Bacillus_A_paramycoides (1.0,9); 287→GTDB:s__Pseudomonas_aeruginosa
    (0.99,17191); 323284→GTDB:s__Alcaligenes_aquatilis (1.0,12). Preserve complete
    recorded lineages, ncbi_id route and taxon scope; do not derive an integer support
    count from rounded 0.99.'
  - 'Refine AZFS5/B. pumilus and AZFS15/B. mojavensis to AMBIGUOUS with gtdb_candidates
    if adding the verified ambiguity results. B. pumilus has four total destinations:
    Bacillus altitudinis, Bacillus pumilus, Bacillus pumilus_O and Bacillus sp002998085;
    B. mojavensis has Bacillus halotolerans and Bacillus mojavensis. Use exact CURIEs
    from the crosswalk receipt; select no bin for either study strain. Preserve source
    strain labels and NCBI IDs.'
  - Record mapping SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd.
    Filesystem mtime does not establish release/build date; name differences do not
    prove reclassification of the studied strain.
- action_id: validate-future-curation
  description: Validate separately authorized record repairs.
  finding_ids:
  - salinity-optimum
  - assay-temperature
  - protocol-detail
  - gtdb-resolution
  target_ids:
  - CommunityMech:000369
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyantraniliprole_Fahmy_Consortium_T4.yaml
    role: canonical_record
  acceptance_checks:
  - Recheck source locators, exact excerpts, identifiers and graph references; run
    schema, strict, terms, explained-reference, GTDB/domain and history gates, then
    just gen-html and just check-docs-current for authorized record changes.
  - Preserve source conflicts, prior decisions and all original receipts. This review
    proposes changes but does not mutate canonical records, caches, history, issues
    or Git.
limitations:
- The publication itself conflicts on salinity optimum and broad-assay temperature.
  Additional unencoded differences include optimization sampling at 15 versus 16 days,
  Table 4 caption versus column concentrations, prose versus Table 2 treatment count,
  and some control values; these were not silently reconciled or scored as new record
  errors.
- Predicted enzyme coverage, OD600 growth and DCPIP decolorization are distinct from
  measured enzyme flux and complete chemical fate. HPLC disappearance does not establish
  mineralization, detoxification, reciprocal fitness or a necessary/sufficient reduced
  consortium.
- Only role-relevant sections of ref32 were read; its CAP/FBD soil assays do not measure
  individual cyantraniliprole flux here. No whole earlier-paper, raw-sequence or statistical
  reanalysis is claimed.
- The actual fresh JATS and five figures resolve erroneous MED access flags. No supplementary
  material is declared in that inventory; this is an inspected-source boundary, not
  a global absence claim.
notes:
- Two node assessments bind their exact canonical excerpt selectors and SHA256 values,
  all six participants, retained evidence tiers and zero downstream arrows.
- The sole quotation is two words from Methods 2.8, Water Microcosm System, fourth
  direct paragraph. All other source content is paraphrased or referenced by exact
  selectors.
- All 33 official inputs remain unchanged. Native candidate validation and parent-owned
  saving/post-save gates follow this assessment; none is asserted in advance.
tags:
- record-review
- bioremediation
- cyantraniliprole
- batch-14
```
