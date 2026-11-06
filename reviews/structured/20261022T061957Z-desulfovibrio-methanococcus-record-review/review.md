# Desulfovibrio–Methanococcus syntrophy record review

- Review: 20261022T061957Z-desulfovibrio-methanococcus-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T06:11:33.078003Z
- Finished UTC: 2026-10-22T06:19:57.618214Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The strain pair and qualified three-node, three-arrow syntrophic mechanism are supported. Two major findings concern the mixed medium/culture protocol and incorrect NATURAL origin. Three minor groups address claim-local evidence and metal scope, GTDB provenance, and array/link traceability. All eight required checks passed. Literal completeness 90 and capped quality 100 (raw 109) do not establish source correctness.

## Scope And Provenance

Whole released target and encoded claims, using fresh complete main text, actual tables, all main figures/equations, bounded resource metadata and native/authority checks.

Selection: Only released CommunityMech:000023 in owned batch15.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb7a782c8ba80299dca8761ad0a2c90bccd8a117.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000023 | kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml | maintained | Desulfovibrio-Methanococcus Syntrophic Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000023 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000023 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000023 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000023 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000023 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000023 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000023 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000023 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000023 | Actual corpus exit 1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000023 | Actual corpus exit 1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000023 | Unavailable in owned runtime. |

## Scientific And Domain Assessments

### Constructed strain pair and community origin

identity: concern. Targets: CommunityMech:000023.

The intended strains are correct; NATURAL misstates the assembly of this laboratory pair.

Retain SYNTROPHY and STABLE for the maintained chemostat state, not every batch or mutant curve. Environmental occurrence of related partnerships does not establish a naturally co-isolated community.

### Lactate Oxidation and H2 Production

graph: supported. Targets: CommunityMech:000023.

Retain lactate oxidation and hydrogen production.

Exact selector ecological_interactions[0]; interaction_type SYNTROPHY; scope PAIRWISE. Current participants: {"source_taxon": {"preferred_term": "Desulfovibrio vulgaris Hildenborough", "term": {"id": "NCBITaxon:882", "label": "Nitratidesulfovibrio vulgaris str. Hildenborough"}}, "target_taxon": {"preferred_term": "Methanococcus maripaludis S2", "term": {"id": "NCBITaxon:267377", "label": "Methanococcus maripaludis S2"}}}. Canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "ea43200ba6a9a624b93e51d94128f775ca5232bbeaab4580a729c02275914c53", "reference": "PMID:19581361", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}, {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "bf737a095da07448801a048769cbaffa7b5931ac67e5f95606861d709b72f440", "reference": "PMID:19581361", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 d4a788e6c8a47d7914e6bc6934dc04712b0d8f8ca6b4c61b2d44f164a7caba94. PMID:19581361 locator: Results sec8 paragraphs1,3–4,7; Discussion sec9 paragraphs1–6; Figures 1–3 and equation 1 versus8. The two Abstract excerpts provide expression context; body/figures support the culture phenotype. Residual 3–5 mM lactate and 24–27 mM acetate are steady-state values, not input recipe. The uphill initial step is distinct from favorable whole fermentation.

### D. vulgaris Hydrogenase-Cytochrome Electron Transfer

graph: supported. Targets: CommunityMech:000023.

Retain the qualified intrinsic donor machinery.

Exact selector ecological_interactions[1]; interaction_type None; scope PAIRWISE. Current participants: {"source_taxon": {"preferred_term": "Desulfovibrio vulgaris Hildenborough", "term": {"id": "NCBITaxon:882", "label": "Nitratidesulfovibrio vulgaris str. Hildenborough"}}, "target_taxon": null}. Canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "8d589ad229872db2c25a5aeb9c6fb7930038eb0fc74a1565dd1bed60608dacf0", "reference": "PMID:19581361", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}, {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "a390d31367e5503ce1b2f26f9cd4d7a9a1ded5da7e188cd4418e64fb91e92876", "reference": "PMID:19581361", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 d4a788e6c8a47d7914e6bc6934dc04712b0d8f8ca6b4c61b2d44f164a7caba94. PMID:19581361 locator: Results sec8 paragraphs3 and7; Discussion sec9 paragraphs1,5–8; Figure 2 and proposed Figure 3. Coo/Hmc strongly impair lactate syntrophy; Hyd/Hyn slow growth but do not abolish final yield. Hmc also affects respiratory growth. Source-only PAIRWISE representation is valid; no new recipient or universal necessity is inferred.

### Interspecies Hydrogen Transfer and Methanogenesis

graph: supported. Targets: CommunityMech:000023.

Retain hydrogenotrophic methanogenesis and product-removal feedback.

Exact selector ecological_interactions[2]; interaction_type SYNTROPHY; scope PAIRWISE. Current participants: {"source_taxon": {"preferred_term": "Methanococcus maripaludis S2", "term": {"id": "NCBITaxon:267377", "label": "Methanococcus maripaludis S2"}}, "target_taxon": {"preferred_term": "Desulfovibrio vulgaris Hildenborough", "term": {"id": "NCBITaxon:882", "label": "Nitratidesulfovibrio vulgaris str. Hildenborough"}}}. Canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "218bfe7b153e3d3f7df815ff434907ab83c26050788b7b010548bdeb04383835", "reference": "PMID:19581361", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}, {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "218bfe7b153e3d3f7df815ff434907ab83c26050788b7b010548bdeb04383835", "reference": "PMID:19581361", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 d4a788e6c8a47d7914e6bc6934dc04712b0d8f8ca6b4c61b2d44f164a7caba94. PMID:19581361 locator: Results sec8 paragraphs1 and7; Discussion sec9 paragraph6; Figures 1–3 and equation3. The two duplicate broad Abstract snippets remain PARTIAL context, not independent exact-pair experiments. Body evidence supplies methane dynamics, methanogen recovery and the benefit of hydrogen removal. The source taxon denotes the hydrogen sink, not nutrient donation back to the bacterium.

### Lactate Oxidation and H2 Production → D. vulgaris Hydrogenase-Cytochrome Electron Transfer

graph: supported. Targets: CommunityMech:000023.

Keep the PARTIAL donor-pathway link.

Exact selector ecological_interactions[0].downstream[0]; source Lactate Oxidation and H2 Production; target D. vulgaris Hydrogenase-Cytochrome Electron Transfer. Participants and exact node evidence are bound in the corresponding node assessments. Exact description: PARTIAL - lactate-derived electrons feed the proposed hydrogenase/cytochrome route. Expression and mutant phenotypes support contributions, not a fully resolved electron path or universal component necessity. Description SHA256 396ad4537a724481a616caf186e9a9d00dc39760a0dc677d97cc1acdd6bed448. PMID:19581361, Results sec8 paragraph7, Discussion sec9 paragraphs1,5–8 and Figures 2–3. Lactate-derived electrons are linked to proposed donor machinery by expression and mutant phenotypes; the complete carrier/coupling route is unresolved.

### D. vulgaris Hydrogenase-Cytochrome Electron Transfer → Interspecies Hydrogen Transfer and Methanogenesis

graph: supported. Targets: CommunityMech:000023.

Keep the PARTIAL machinery-to-hydrogen-consumer link.

Exact selector ecological_interactions[1].downstream[0]; source D. vulgaris Hydrogenase-Cytochrome Electron Transfer; target Interspecies Hydrogen Transfer and Methanogenesis. Participants and exact node evidence are bound in the corresponding node assessments. Exact description: PARTIAL - donor electron-transfer machinery supports hydrogen provision to the methanogen. Genetic phenotypes support contribution, while the detailed route and coupling remain unresolved. Description SHA256 3b4c2a5c66d2fd6594882b2f7dec603a261f2c058a9a6a854a5ff301433cf61b. PMID:19581361, Results sec8 paragraph7, Discussion sec9 paragraphs1,5–8 and Figures 2–3. Donor phenotypes support hydrogen supply to the methanogen without establishing one exclusive route or equal necessity of all hydrogenases.

### Interspecies Hydrogen Transfer and Methanogenesis → Lactate Oxidation and H2 Production

graph: supported. Targets: CommunityMech:000023.

Keep the physiological hydrogen-removal feedback.

Exact selector ecological_interactions[2].downstream[0]; source Interspecies Hydrogen Transfer and Methanogenesis; target Lactate Oxidation and H2 Production. Participants and exact node evidence are bound in the corresponding node assessments. Exact description: Methanogen hydrogen consumption supports the low-hydrogen conditions favorable to continued donor lactate fermentation, closing the physiological feedback loop. Description SHA256 17bfb9dd735de834e30a3b896ede6914577ef8e70fcfd947f087aeb02351ace3. PMID:19581361, Results sec8 paragraph7, Discussion sec9 paragraphs1,5–8 and Figures 2–3. Methanogen consumption lowers a donor product and makes continued lactate oxidation more favorable. It is not reverse nutrient donation or a self-edge.

### Source CCM versus imported formulation

evidence: concern. Targets: CommunityMech:000023.

The current medium combines incompatible formulations and mixes source assay stages.

Source CCM uses30 mM sodium DL-lactate; per liter 2.17 g NaCl,5.5 g MgCl2·6H2O,0.14 g CaCl2·2H2O,0.5 g NH4Cl and0.335 g KCl;1.1 mM K2HPO4 and 30 mM bicarbonate;1 mM each cysteine hydrochloride/sulfide nonahydrate;1 mg/L resazurin. Nonchelated trace and vitamin stocks are each added at 1 mL/L; choline belongs to the vitamin-stock amendment. Current L-lactate20 mM, other doses, SL-10 assumption and yeast extract are not this formulation. CultureMech:000423 is DSMZ 1007 nitrate medium; its stock solutes must not be flattened into final CCM.

### Exact claim placement and conditional interpretation

evidence: concern. Targets: CommunityMech:000023.

Some Abstract excerpts are authentic but too broad for their attached protocol and identity claims.

Taxonomy[1] excerpt names DvH, not S2; Table 1/Methods establish S2. Use role-local body support for both members, actual Methods for dilution and culture values, and source thermodynamics for hydrogen dependence. Bound obligate and sulfate-absence wording to the stated lactate regime. SIGNIFICANT metal/REE metabolism and keyword-derived measurement notes are unsupported; transport-expression interpretation is narrower. Correct these bounded metadata claims without regrading the supported graph or claiming iron absence.

### Correct strain groundings and GTDB provenance

grounding: concern. Targets: CommunityMech:000023.

All 22 ontology pairs match; both GTDB cores reproduce, while release/build wording needs correction.

The local strain-ID routes support 1.0/7 for Hildenborough and 1.0/2 for S2. Those counts describe reference mapping, not cell abundance. Chemical label agreement does not make an L-only or anhydrous formulation equivalent to the source.

### Expression-array and cross-Mech traceability

representation: concern. Targets: CommunityMech:000023.

The source-declared array is recoverable; legacy ingredient links need verified identity handling.

Represent GSE17831 with GSM444833 and GPL9107 in its actual DvH whole-genome expression-array scope. Preserve archive design and sample-count boundaries. All 21 encoded cross-Mech URLs are broken; all 20 legacy numeric MIM IDs are absent from the complete current index. Current chemical candidates include hydrate ambiguity and rejected rows, so names alone do not authorize replacement. The wrong CultureMech formulation is graded only in the medium finding.

### Complete main-claim audit with bounded SI access

scope: supported. Targets: CommunityMech:000023.

The main text, tables, figures and equations suffice for all currently encoded claims.

Lead read 69,502 main characters, both biological tables, all 3 main figures and all 9 formula images. Supplementary tables, COG and accuracy plots were not recovered or read; no raw array reanalysis is claimed. This limits supplementary detail, not the source-grounded review of the present record.

### Maintained owner and prior decisions

ownership: supported. Targets: CommunityMech:000023.

Any repair belongs to the canonical YAML under separate curation authorization.

Ignored-inclusive discovery pinned the sole cache, history, batch32 decision/adversarial and four cohort contexts. Prior graph repair is retained; this review changes no canonical data, cache, history, issue or Git state.

### Actual required validation

schema: supported. Targets: CommunityMech:000023.

All eight required native checks passed.

Keep nonrequired corpus failures, optional-adapter unavailability and ancillary reader failures separate from actual native target outcomes.

### Literal native completeness and validation quality

completeness: supported. Targets: CommunityMech:000023.

Completeness90; raw quality109, capped 100.

## Findings

### medium-assay: Reconstruct source CCM and separate culture stages

major / open / confirmed; issue key: cm-000023-medium-assay.

The current recipe and imported DSMZ 1007 nitrate-medium components do not represent the source CCM. Culture conditions combine chemostat and phenotype stages.

### constructed-origin: Correct the community origin

major / open / confirmed; issue key: cm-000023-constructed-origin.

NATURAL conflicts with the explicitly constructed two-member laboratory model.

### claim-evidence: Use exact claim evidence and bounded non-graph interpretation

minor / open / confirmed; issue key: cm-000023-claim-evidence.

Generic Abstract snippets are attached to specific identity/protocol claims. Unconditional dependence and significant measured metal/REE claims exceed the source context.

### gtdb-provenance: Correct GTDB release/build provenance

minor / open / confirmed; issue key: cm-000023-gtdb-provenance.

Both mapping_source strings overstate the meaning of a local filesystem modification date; the actual cores reproduce.

### resource-traceability: Add the source array and repair verified legacy links

minor / open / confirmed; issue key: cm-000023-resource-traceability.

The declared GEO array resource is absent, and legacy ingredient URLs need current identity handling. Wrong medium identity is already graded once in medium-assay.

## Recommended Actions And Acceptance Checks

### repair-medium

Replace the mixed recipe with source CCM and distinct assay contexts.

- Use the source 30 mM sodium DL-lactate formulation and exact salts/units from Biomass production first paragraph; retain correct 1 mM reducing agents and 30 mM bicarbonate. Verified candidate CHEBI:75228 is non-stereospecific sodium lactate, so retain DL explicitly. Use CHEBI:86345 and CHEBI:86158 for source weighed Mg/Ca hydrates where appropriate.
- Remove the unrelated CultureMech:000423/DSMZ 1007 identity and imported nitrate-medium component block. Do not treat its trace-stock solute concentrations as final CCM or invent a replacement CultureMech record. Preserve1 mL/L nonchelated trace/vitamin stock boundaries; do not equate the source stock to SL-10 without evidence.
- Represent100 mL in200 mL starter vial at 37 °C/dark/250 rpm; then2 L in3 L chemostat with90:10 N2/CO2, 250 rpm, pH 7.0–7.2 and0.039 h−1. Distinguish batch startup and subsequent continuous operation.
- Represent phenotype cultures separately:8 mL in17 mL Hungate tubes,37 °C/dark/300 rpm,80:20 N2/CO2,30 mM lactate or pyruvate. Preserve sulfate-amended comparator and H2/acetate methanogen preculture separately, plus source inoculation/transfers. Do not transfer the phenotype headspace to the chemostat.

### repair-origin

Represent the deliberately assembled pair.

- Set source-supported SYNTHETIC or ENGINEERED origin with Introduction/Methods/Table 1 evidence; retain exact strain IDs and category. Keep STABLE limited to the observed chemostat steady state.

### repair-claim-evidence

Replace broad evidence placements and qualify non-graph scope.

- Use source Strains/Table 1 for S2 and Hildenborough, role-local Results/Discussion for metabolism, and Biomass production for dilution and medium conditions. Existing broad node2 excerpts may be supplemented by direct body evidence without changing the supported graph.
- Qualify dependence to the tested lactate/no-added-bulk-sulfate regime and preserve authors’ trace sulfate acknowledgment. Do not call the whole fermentation uphill; equations 1/8 and observed-state calculations describe different reactions.
- Remove unsupported SIGNIFICANT metal/REE metabolism and keyword-based environmental-measurement notes. If a metal annotation remains, ground it only in the source transport-expression interpretation and actual trace/machinery context; do not claim iron is absent.

### repair-provenance

Record actual crosswalk and source-resource provenance.

- Replace latest/build-date wording with actual crosswalk hash/access provenance; preserve both exact strain-ID GTDB cores and reference counts.
- Add GSE17831 and its verified GSM444833/GPL9107 context as DvH expression profiling by array, using exact metadata. Do not label it community RNA sequencing or infer independent sample counts from merged array entries.
- Resolve ingredient links by verified chemical identity, hydration and stock scope. All 20 legacy numeric MIM identifiers are absent from the current complete index; rejected or ambiguous candidates must not be automatically remapped. Repair broken URLs only where exact identity is established.

### validate-curation

Validate any separately authorized canonical repair.

- Run focused schema/strict/ontology/reference/GTDB/history checks and required generated-document checks after actual canonical changes. Preserve original caches/history and existing graph repair.
- Recheck all three node scopes and three arrow directions against Figures 1–3/Results/Discussion. Root alone saves this review and runs post-save gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml; Whole maintained YAML | supports | Two strain-grounded members, three nodes and three directed arrows. |
| abstract | PMID:19581361; DOI:10.1128/JB.00356-09; Fresh MED resultList.result[0].abstractText | supports | Whole Abstract supports expression and mutant context; it does not supply the detailed medium or dilution protocol. |
| identity | PMID:19581361; DOI:10.1128/JB.00356-09; Introduction first paragraph after Abstract; Methods Strains., sec2 sole paragraph; Table 1 | supports | Authors constructed the two-member model from Hildenborough and M. maripaludis S2; mutants are comparator derivatives. |
| cultivation | PMID:19581361; DOI:10.1128/JB.00356-09; MATERIALS AND METHODS, Biomass production., first direct paragraph, HTML sec3/p[1]; quoted words in that paragraph. Second paragraph specifies staged vessels and operation. | supports | CCM formulation, starter and chemostat stages must remain distinct from phenotype assays. |
| phenotypes | PMID:19581361; DOI:10.1128/JB.00356-09; Methods Phenotypic growth analyses., sec6 sole direct paragraph; Results sec8 seventh direct paragraph; Figure 2 and Table 2 | supports | Phenotypic tube cultures and single-species precultures have distinct gas, substrate and inoculation conditions. Mutants test contributions, not a universal exclusive route. |
| performance | PMID:19581361; DOI:10.1128/JB.00356-09; Results sec8 first and fifth direct paragraphs; Figure 1 | supports | Steady-state lactate, acetate, methane and cell ratio support the culture phenotype; authors acknowledge trace sulfate. |
| machinery | PMID:19581361; DOI:10.1128/JB.00356-09; Results sec8 third, fourth and seventh direct paragraphs; Discussion sec9 first and fifth through eighth direct paragraphs; Figures 2–3 | supports | Expression and growth defects support a proposed donor electron-transfer model with Coo/Hmc and Hyd/Hyn effects distinguished. |
| thermodynamics | PMID:19581361; DOI:10.1128/JB.00356-09; Discussion sec9 second through sixth direct paragraphs; equation images M2–M9, equations 1–8 | supports | Whole fermentation and the uphill initial lactate-to-pyruvate step are distinct. Methanogen hydrogen removal supports continued donor metabolism. |
| metal-context | PMID:19581361; DOI:10.1128/JB.00356-09; Discussion sec9 tenth direct paragraph | supports | Metal transport-expression interpretation and iron-containing machinery do not establish measured significant metal/REE metabolism. |
| archive-declaration | PMID:19581361; DOI:10.1128/JB.00356-09; Methods Gene expression database accession numbers., sec7 sole direct paragraph; Transcriptional analysis., sec4 | supports | GSE17831, GSM444833 and GPL9107 identify the source expression-array resource; no community RNA-sequencing claim. |
| ontology | /private/tmp/cm-review-session/batch-15/000023/ontology-authority.json; 22 exact ID/label pairs,32 placements | supports | All labels match; source formulation and phenotype support are assessed separately. |
| schema | /private/tmp/cm-review-session/batch-15/000023/child-schema-semantics.json; Current role, interaction, origin, state, medium and evidence definitions | supports | SYNTROPHY requires beneficial product removal, not obligacy; significant metal metabolism is a separate claim. |
| gtdb | /private/tmp/cm-review-session/batch-15/000023/child-gtdb-crosswalk.json; Exact NCBI strain-ID crosswalk routes | supports | Both cores reproduce; local filemtime does not establish GTDB release/build provenance. |
| strains | /private/tmp/cm-review-session/batch-15/000023/child-strain-scope.json; Source Table 1 and current local strain identity | supports | Hildenborough=ATCC29579 and S2 are the intended wild-type members; mutant derivatives remain distinct. |
| chemistry | /private/tmp/cm-review-session/batch-15/000023/child-chemical-candidates.json; Bounded exact local chemical identities | supports | Non-stereospecific sodium lactate and explicit chloride hydrates are verified candidates; DL formulation remains source text. |
| formulation | /private/tmp/cm-review-session/batch-15/000023/child-medium-formulation-audit.json; All25 medium rows | supports | Separate 13 community-curated rows from 12 imported provider rows and stock concentrations. |
| semantics | /private/tmp/cm-review-session/batch-15/000023/ontology-semantic-notes.json; Final source-local semantic assessment | supports | Retain the three-node, three-arrow graph and bounded steady state; repair the agreed five groups. |
| resources | /private/tmp/cm-review-session/batch-15/000023/dataset-verification.json; Source-declared GEO identities and access scope | supports | Verified expression-array metadata should be represented without raw-data or SI reanalysis claims. |
| external-links | /private/tmp/cm-review-session/batch-15/000023/external-resource-verification.json; Encoded CultureMech/MIM identifiers and current records | supports | The wrong medium identity is distinct from broken routes and unresolved legacy ingredient IDs. |
| snippets | /private/tmp/cm-review-session/batch-15/000023/snippet-audit.json; All 15 canonical excerpt placements | supports | Exact Abstract matching does not establish detailed claim entailment. |
| provenance | /private/tmp/cm-review-session/batch-15/000023/provenance-audit.json; Sole history, exact batch32 row, cohort and current issues | supports | Preserve previous graph repair and remaining medium/evidence follow-up. |
| inspection | /private/tmp/cm-review-session/batch-15/000023/inspect.json; Official30-input inspection | supports | Canonical target,21 authorities and8 focal contexts were pinned before assessment. |
| assets | /private/tmp/cm-review-session/batch-15/000023/lead-source-assets.json; Fresh main, actual figures/formulas and failed supplementary routes | supports | Genuine main payloads are distinct from challenge/error responses; no supplementary payload was read. |
| lead-read | /private/tmp/cm-review-session/batch-15/000023/lead-primary-read-scope.json; Actual whole-main and visual reading | supports | All69502 main characters, two biological tables, three figures and nine formula images were read. |
| locators | /private/tmp/cm-review-session/batch-15/000023/source-locator-verification.json; Direct HTML section and paragraph inventory | supports | Source locators and the sole two-word quote were checked against actual paragraphs. |
| source-audit | /private/tmp/cm-review-session/batch-15/000023/source-audit.json; Final lead source judgment and graph bindings | supports | Completed scientific review with two major and three minor findings; SI limits explicit. |
| root-source | /private/tmp/cm-review-session/batch-15/000023/root-independent-source-audit.json; Independent root source and input audit | supports | Independent whole main and visual reading agrees with the bounded source conclusions. |
| root-addendum | /private/tmp/cm-review-session/batch-15/000023/root-final-source-addendum.json; Final independent source/resource acceptance | supports | Root read final resources and retained the same source judgment. |
| metrics | /private/tmp/cm-review-session/batch-15/000023/support-final-audit.json; Final independent reconciliation | supports | Literal completeness 90; base 135 less 26 gives raw 109, capped 100. |
| support-manifest | /private/tmp/cm-review-session/batch-15/000023/support-frozen-manifest.json; Frozen supporting dependencies | supports | Actual input and source/resource pins verified. |
| auxiliary | /private/tmp/cm-review-session/batch-15/000023/auxiliary-frozen-manifest.json; Frozen authority/native dependencies | supports | Eight actual required checks passed; ancillary reader failure is preserved separately. |
| native-summary | /private/tmp/cm-review-session/batch-15/000023/final-validator-summary.json; Eight actual native receipts | supports | No native target failure; label and reference success do not substitute for science. |
| corpus-context | /private/tmp/cm-review-session/batch-15/000023/child-corpus-context.json; Fresh batch15 corpus baseline | supports | Two nonrequired corpus commands returned 1 with 44 warnings across 16/477 records and zero errors. |
| adapter | /private/tmp/cm-review-session/batch-15/000023/adapter-check.json; Current owned-runtime availability and explicit reused discovery | supports | Optional structured adapter unavailable in owned runtime; no global absence or biological inference. |
| check-validate | /private/tmp/cm-review-session/batch-15/000023/validate.json; Actual command/stdout/stderr | supports | Actual native exit 0; science assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-15/000023/validate-strict.json; Actual command/stdout/stderr | supports | Actual native exit 0; science assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-15/000023/validate-terms.json; Actual command/stdout/stderr | supports | Actual native exit 0; science assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-15/000023/validate-references-explained.json; Actual command/stdout/stderr | supports | Actual native exit 0; science assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-15/000023/validate-gtdb.json; Actual command/stdout/stderr | supports | Actual native exit 0; science assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-15/000023/validate-gtdb-domain.json; Actual command/stdout/stderr | supports | Actual native exit 0; science assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-15/000023/validate-history.json; Actual command/stdout/stderr | supports | Actual native exit 0; science assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-15/000023/normalize-cache-names-check.json; Actual command/stdout/stderr | supports | Actual native exit 0; science assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-15/audit-network.json; Fresh batch15 corpus baseline | supports | Actual exit 1 with 44 warnings across 16/477 records, zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-15/check-network-quality.json; Fresh batch15 corpus baseline | supports | Actual exit 1 with 44 warnings across 16/477 records, zero errors. |

## Limits And Additional Notes

- Supplementary table/figure PDFs were not recovered after bounded ordinary public routes. All failed/challenge/error payloads are preserved and excluded as scientific sources. No SI transcript-list, COG or accuracy-plot read is claimed; full main and figures suffice for current encoded claims.
- Expression changes and mutant phenotypes support the proposed donor model but do not resolve an exclusive carrier/proton-coupling route. Whole fermentation is favorable; the initial lactate-to-pyruvate step and reverse-flow requirement retain the source uncertainty.
- Chemostat, starter, mutant phenotype assays and single-species precultures have distinct conditions. Authors acknowledge trace sulfate; no universal zero-sulfate or obligacy claim is inferred.
- No raw microarray matrix reanalysis or uncited-reference audit was performed. GEO metadata and cross-Mech identity checks retain their declared scope. Rejected or ambiguous modern ingredient candidates are not replacements.
- Optional structured adapter was unavailable in the owned runtime; separate corpus diagnostic exits and ancillary reader failures are not native target failures.
- Eight evidence-linked dimensions cover stable identity, source strains, community scope, taxonomy, medium, setting, environment and evidence tier. Six canonical graph excerpt hashes and three exact arrow descriptions are bound once in their assessments.
- The sole primary-source quote contains two words. Thirty official inputs remain unchanged; snapshots preserve actual access and read scope.
- Completed scientific review is distinct from repository persistence; root owns save and required post-save gates.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T061957Z-desulfovibrio-methanococcus-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Desulfovibrio–Methanococcus syntrophy record review
started_at: '2026-10-22T06:11:33.078003Z'
finished_at: '2026-10-22T06:19:57.618214Z'
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
summary: The strain pair and qualified three-node, three-arrow syntrophic mechanism
  are supported. Two major findings concern the mixed medium/culture protocol and
  incorrect NATURAL origin. Three minor groups address claim-local evidence and metal
  scope, GTDB provenance, and array/link traceability. All eight required checks passed.
  Literal completeness 90 and capped quality 100 (raw 109) do not establish source
  correctness.
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
  - path: history/records/Desulfovibrio_Methanococcus_Syntrophy/2026-10-06T063854Z-codex-5aa5f3.yaml
    sha256: 47cb697241ffd65cbd6e8151f96d89a1d9e4bdf65c447daf551be8de1713fe98
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    sha256: 62ab309b887d822437b62ca6fdc9a90f055e70c7bd32d05be255d6e087eee8b0
    role: target
  - path: references_cache/PMID_19581361.txt
    sha256: 3ea81471d9639d080ceb9c85f86fa0254e0f942ff02eb450b36297e84009d1ff
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch32.yaml
    sha256: fb31af941ac34e88b7c749a987c6fef46ab8a95dc173b8ccbdd890e23ee1c279
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch32.yaml
    sha256: 400a8403214d7c2fbd88bb8e533cc5e22c2982013a5c900f6ebd62c9a0263f16
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
- target_id: CommunityMech:000023
  path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
  label: Desulfovibrio-Methanococcus Syntrophic Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
scope:
  description: Whole released target and encoded claims, using fresh complete main
    text, actual tables, all main figures/equations, bounded resource metadata and
    native/authority checks.
  selection: Only released CommunityMech:000023 in owned batch15.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000023
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000023
  command: just --no-dotenv validate kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000023
  command: just --no-dotenv validate-strict kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    --out /private/tmp/cm-review-session/batch-15/000023/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000023
  command: just --no-dotenv validate-terms kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000023
  command: just --no-dotenv validate-references-explained kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000023
  command: just --no-dotenv validate-gtdb kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000023
  command: just --no-dotenv validate-gtdb-domain kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000023
  command: just --no-dotenv validate-history history/records/Desulfovibrio_Methanococcus_Syntrophy
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000023
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Target/history checks; cache-name preflight is corpus-wide. All 30 official
    inputs unchanged.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000023
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-15/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, not target or candidate failure.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000023
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-15/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, not target or candidate failure.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in owned runtime.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - adapter
  scope_note: No execution in another checkout, installation or biological absence
    inference.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
  locator: Whole maintained YAML
  summary: Two strain-grounded members, three nodes and three directed arrows.
  support: supports
  accessed_at: '2026-10-22T06:19:57.601563Z'
- evidence_id: abstract
  kind: primary_source
  reference: PMID:19581361; DOI:10.1128/JB.00356-09
  locator: Fresh MED resultList.result[0].abstractText
  summary: Whole Abstract supports expression and mutant context; it does not supply
    the detailed medium or dilution protocol.
  support: supports
  accessed_at: '2026-10-22T06:19:57.601811Z'
  snapshot_sha256: b8aabea5f01f9eff950e11d8e7894ce5d928211358b75950c79b8dd7332c0289
- evidence_id: identity
  kind: primary_source
  reference: PMID:19581361; DOI:10.1128/JB.00356-09
  locator: Introduction first paragraph after Abstract; Methods Strains., sec2 sole
    paragraph; Table 1
  summary: Authors constructed the two-member model from Hildenborough and M. maripaludis
    S2; mutants are comparator derivatives.
  support: supports
  accessed_at: '2026-10-22T06:19:57.602149Z'
  snapshot_sha256: 0661fbcd7692e8e3188d850aaba615928fb3582ebed617a2eb946dee1e6ed6c4
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:19581361; DOI:10.1128/JB.00356-09
  locator: MATERIALS AND METHODS, Biomass production., first direct paragraph, HTML
    sec3/p[1]; quoted words in that paragraph. Second paragraph specifies staged vessels
    and operation.
  summary: CCM formulation, starter and chemostat stages must remain distinct from
    phenotype assays.
  support: supports
  accessed_at: '2026-10-22T06:19:57.602922Z'
  snapshot_sha256: 0661fbcd7692e8e3188d850aaba615928fb3582ebed617a2eb946dee1e6ed6c4
  quote: coculture medium
- evidence_id: phenotypes
  kind: primary_source
  reference: PMID:19581361; DOI:10.1128/JB.00356-09
  locator: Methods Phenotypic growth analyses., sec6 sole direct paragraph; Results
    sec8 seventh direct paragraph; Figure 2 and Table 2
  summary: Phenotypic tube cultures and single-species precultures have distinct gas,
    substrate and inoculation conditions. Mutants test contributions, not a universal
    exclusive route.
  support: supports
  accessed_at: '2026-10-22T06:19:57.603210Z'
  snapshot_sha256: 0661fbcd7692e8e3188d850aaba615928fb3582ebed617a2eb946dee1e6ed6c4
- evidence_id: performance
  kind: primary_source
  reference: PMID:19581361; DOI:10.1128/JB.00356-09
  locator: Results sec8 first and fifth direct paragraphs; Figure 1
  summary: Steady-state lactate, acetate, methane and cell ratio support the culture
    phenotype; authors acknowledge trace sulfate.
  support: supports
  accessed_at: '2026-10-22T06:19:57.603365Z'
  snapshot_sha256: 0661fbcd7692e8e3188d850aaba615928fb3582ebed617a2eb946dee1e6ed6c4
- evidence_id: machinery
  kind: primary_source
  reference: PMID:19581361; DOI:10.1128/JB.00356-09
  locator: Results sec8 third, fourth and seventh direct paragraphs; Discussion sec9
    first and fifth through eighth direct paragraphs; Figures 2–3
  summary: Expression and growth defects support a proposed donor electron-transfer
    model with Coo/Hmc and Hyd/Hyn effects distinguished.
  support: supports
  accessed_at: '2026-10-22T06:19:57.603483Z'
  snapshot_sha256: 0661fbcd7692e8e3188d850aaba615928fb3582ebed617a2eb946dee1e6ed6c4
- evidence_id: thermodynamics
  kind: primary_source
  reference: PMID:19581361; DOI:10.1128/JB.00356-09
  locator: Discussion sec9 second through sixth direct paragraphs; equation images
    M2–M9, equations 1–8
  summary: Whole fermentation and the uphill initial lactate-to-pyruvate step are
    distinct. Methanogen hydrogen removal supports continued donor metabolism.
  support: supports
  accessed_at: '2026-10-22T06:19:57.603618Z'
  snapshot_sha256: 0661fbcd7692e8e3188d850aaba615928fb3582ebed617a2eb946dee1e6ed6c4
- evidence_id: metal-context
  kind: primary_source
  reference: PMID:19581361; DOI:10.1128/JB.00356-09
  locator: Discussion sec9 tenth direct paragraph
  summary: Metal transport-expression interpretation and iron-containing machinery
    do not establish measured significant metal/REE metabolism.
  support: supports
  accessed_at: '2026-10-22T06:19:57.603779Z'
  snapshot_sha256: 0661fbcd7692e8e3188d850aaba615928fb3582ebed617a2eb946dee1e6ed6c4
- evidence_id: archive-declaration
  kind: primary_source
  reference: PMID:19581361; DOI:10.1128/JB.00356-09
  locator: Methods Gene expression database accession numbers., sec7 sole direct paragraph;
    Transcriptional analysis., sec4
  summary: GSE17831, GSM444833 and GPL9107 identify the source expression-array resource;
    no community RNA-sequencing claim.
  support: supports
  accessed_at: '2026-10-22T06:19:57.604017Z'
  snapshot_sha256: 0661fbcd7692e8e3188d850aaba615928fb3582ebed617a2eb946dee1e6ed6c4
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000023/ontology-authority.json
  locator: 22 exact ID/label pairs,32 placements
  summary: All labels match; source formulation and phenotype support are assessed
    separately.
  support: supports
  accessed_at: '2026-10-22T06:19:57.604261Z'
  snapshot_sha256: 6972d76047bcf9d7233eab11e959cc6bb9e72b82d6d9f4c1dab058b7459e24f6
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000023/child-schema-semantics.json
  locator: Current role, interaction, origin, state, medium and evidence definitions
  summary: SYNTROPHY requires beneficial product removal, not obligacy; significant
    metal metabolism is a separate claim.
  support: supports
  accessed_at: '2026-10-22T06:19:57.604602Z'
  snapshot_sha256: 813e3e75c5aaa3db448da49ca5031aeaa91881dda95409f5aa5c8495fc707b60
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000023/child-gtdb-crosswalk.json
  locator: Exact NCBI strain-ID crosswalk routes
  summary: Both cores reproduce; local filemtime does not establish GTDB release/build
    provenance.
  support: supports
  accessed_at: '2026-10-22T06:19:57.605045Z'
  snapshot_sha256: 92721a100440083014bbbe2f46e5dac128f2079ff8fb9b6ace7836316940418d
- evidence_id: strains
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000023/child-strain-scope.json
  locator: Source Table 1 and current local strain identity
  summary: Hildenborough=ATCC29579 and S2 are the intended wild-type members; mutant
    derivatives remain distinct.
  support: supports
  accessed_at: '2026-10-22T06:19:57.606080Z'
  snapshot_sha256: 40ae77664b4b5a745b2285acb6b791d671d9e021eedb5a38e66bc4d6a993b4dd
- evidence_id: chemistry
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000023/child-chemical-candidates.json
  locator: Bounded exact local chemical identities
  summary: Non-stereospecific sodium lactate and explicit chloride hydrates are verified
    candidates; DL formulation remains source text.
  support: supports
  accessed_at: '2026-10-22T06:19:57.606748Z'
  snapshot_sha256: 84b3c4190cb1b7e3ebebbb0a70aef29e8553a4817be20c67a7cc0ec081b2476e
- evidence_id: formulation
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/child-medium-formulation-audit.json
  locator: All25 medium rows
  summary: Separate 13 community-curated rows from 12 imported provider rows and stock
    concentrations.
  support: supports
  accessed_at: '2026-10-22T06:19:57.607059Z'
  snapshot_sha256: ccacdfde799c86d2c9ab6f9f5f5b5370f084cdc57fe14eb0342a5bf7897b58f7
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000023/ontology-semantic-notes.json
  locator: Final source-local semantic assessment
  summary: Retain the three-node, three-arrow graph and bounded steady state; repair
    the agreed five groups.
  support: supports
  accessed_at: '2026-10-22T06:19:57.607506Z'
  snapshot_sha256: d6992651e1fcdb8a41e5a0353bd8d44270fa45d59b09b117f94f6b9cde2379fb
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/dataset-verification.json
  locator: Source-declared GEO identities and access scope
  summary: Verified expression-array metadata should be represented without raw-data
    or SI reanalysis claims.
  support: supports
  accessed_at: '2026-10-22T06:19:57.608013Z'
  snapshot_sha256: daec0519fd28f110735012de5f6566b49a3a86857d20ab31c86662b55e89a5c7
- evidence_id: external-links
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/external-resource-verification.json
  locator: Encoded CultureMech/MIM identifiers and current records
  summary: The wrong medium identity is distinct from broken routes and unresolved
    legacy ingredient IDs.
  support: supports
  accessed_at: '2026-10-22T06:19:57.608375Z'
  snapshot_sha256: 19dc0b4145d3359fbba3b3dba98a4e6337df96aa6f8239bd8ac3354b7d0156d1
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/snippet-audit.json
  locator: All 15 canonical excerpt placements
  summary: Exact Abstract matching does not establish detailed claim entailment.
  support: supports
  accessed_at: '2026-10-22T06:19:57.608442Z'
  snapshot_sha256: d4a788e6c8a47d7914e6bc6934dc04712b0d8f8ca6b4c61b2d44f164a7caba94
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-15/000023/provenance-audit.json
  locator: Sole history, exact batch32 row, cohort and current issues
  summary: Preserve previous graph repair and remaining medium/evidence follow-up.
  support: supports
  accessed_at: '2026-10-22T06:19:57.608727Z'
  snapshot_sha256: b9c80414436e7f252f5b96fb1ed4a23744493e938a8e376ecfa89779fafbda92
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/inspect.json
  locator: Official30-input inspection
  summary: Canonical target,21 authorities and8 focal contexts were pinned before
    assessment.
  support: supports
  accessed_at: '2026-10-22T06:19:57.609137Z'
  snapshot_sha256: 18297e20b6adb8e63aac29157cc3832d46ddfca24d1e4247e2ef38c788e928a8
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/lead-source-assets.json
  locator: Fresh main, actual figures/formulas and failed supplementary routes
  summary: Genuine main payloads are distinct from challenge/error responses; no supplementary
    payload was read.
  support: supports
  accessed_at: '2026-10-22T06:19:57.609198Z'
  snapshot_sha256: 85876a32f8da31f7b1019d84442752251ad7dd30a75f8ea1eebc22b1690bd817
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/lead-primary-read-scope.json
  locator: Actual whole-main and visual reading
  summary: All69502 main characters, two biological tables, three figures and nine
    formula images were read.
  support: supports
  accessed_at: '2026-10-22T06:19:57.609532Z'
  snapshot_sha256: a658684deb14c916f044e01484cae8b56f68891a8c2e39741a0960d9dd3830a3
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/source-locator-verification.json
  locator: Direct HTML section and paragraph inventory
  summary: Source locators and the sole two-word quote were checked against actual
    paragraphs.
  support: supports
  accessed_at: '2026-10-22T06:19:57.609812Z'
  snapshot_sha256: 8cf9b25cefc7979428e15838514f4b85ef4e3c13eab0bd5f8332aabe1e579c00
- evidence_id: source-audit
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/source-audit.json
  locator: Final lead source judgment and graph bindings
  summary: Completed scientific review with two major and three minor findings; SI
    limits explicit.
  support: supports
  accessed_at: '2026-10-22T06:19:57.610358Z'
  snapshot_sha256: a5cc0231bc3884ab297ae56c76dfbe3212ad74b81a7135cca2837937054a0ad8
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/root-independent-source-audit.json
  locator: Independent root source and input audit
  summary: Independent whole main and visual reading agrees with the bounded source
    conclusions.
  support: supports
  accessed_at: '2026-10-22T06:19:57.610636Z'
  snapshot_sha256: 100031e2651f4816be1d30b9ca5bb88d9dcac7ba95fba37c18f321b472e4e9db
- evidence_id: root-addendum
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/root-final-source-addendum.json
  locator: Final independent source/resource acceptance
  summary: Root read final resources and retained the same source judgment.
  support: supports
  accessed_at: '2026-10-22T06:19:57.610790Z'
  snapshot_sha256: 424a6324cb1008ea2a10a1ca1c926e05911efa54ec73fe994678e81b02f13aab
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/support-final-audit.json
  locator: Final independent reconciliation
  summary: Literal completeness 90; base 135 less 26 gives raw 109, capped 100.
  support: supports
  accessed_at: '2026-10-22T06:19:57.610962Z'
  snapshot_sha256: 67bf2b1ccf2c4c6df017476a6d414b151e1fa5e8a1f80a91fdd9770fb9ec112b
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/support-frozen-manifest.json
  locator: Frozen supporting dependencies
  summary: Actual input and source/resource pins verified.
  support: supports
  accessed_at: '2026-10-22T06:19:57.611090Z'
  snapshot_sha256: d7965c172a6bb5cfb5c4c0573206404252ce935ad420d326b0f4a5964ec207b7
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/auxiliary-frozen-manifest.json
  locator: Frozen authority/native dependencies
  summary: Eight actual required checks passed; ancillary reader failure is preserved
    separately.
  support: supports
  accessed_at: '2026-10-22T06:19:57.611699Z'
  snapshot_sha256: d4719b6272269ff1937b9f4c70db930d31b8280646d713f671b9c2583bba9e6e
- evidence_id: native-summary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/final-validator-summary.json
  locator: Eight actual native receipts
  summary: No native target failure; label and reference success do not substitute
    for science.
  support: supports
  accessed_at: '2026-10-22T06:19:57.611916Z'
  snapshot_sha256: 2322727aec6314e531a2c306000a0c5ca694c0265a33ddfcae080e4b48f7c6bb
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/child-corpus-context.json
  locator: Fresh batch15 corpus baseline
  summary: Two nonrequired corpus commands returned 1 with 44 warnings across 16/477
    records and zero errors.
  support: supports
  accessed_at: '2026-10-22T06:19:57.612177Z'
  snapshot_sha256: 2ca687048bafd227cf5601ff127588c72a89c1e6e567c75ebb5ba8e413c83c64
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/adapter-check.json
  locator: Current owned-runtime availability and explicit reused discovery
  summary: Optional structured adapter unavailable in owned runtime; no global absence
    or biological inference.
  support: supports
  accessed_at: '2026-10-22T06:19:57.612740Z'
  snapshot_sha256: 52ee2ad34d952c99ea513abe118be0b14a8e4b0e96d8774b65225f98b9ed1387
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/validate.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; science assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:19:57.613585Z'
  snapshot_sha256: de04bfb7b42163771e5e455e35d2aa025fb0f287f712a2a55098fcd80c2ff094
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/validate-strict.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; science assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:19:57.613936Z'
  snapshot_sha256: 1f42e90fbb715fe5a43f91052213ffd29755f3fe7403ad47365b8db7efe62797
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/validate-terms.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; science assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:19:57.614326Z'
  snapshot_sha256: 1a8ee8d1d05ee166de63aad0fc036d00b301b0f8da819c0c7c751da78a220afd
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/validate-references-explained.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; science assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:19:57.614872Z'
  snapshot_sha256: 216c11885d05d872bbba094b027e9fa609e50b2b2662750aa54e95e13632da40
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/validate-gtdb.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; science assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:19:57.615630Z'
  snapshot_sha256: f3a0a469e89fb39bee81ba04c455e36989ef25ed4a81197e796dc93bbecee38c
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/validate-gtdb-domain.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; science assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:19:57.616015Z'
  snapshot_sha256: e33ab889e5c331fa5d4fa9fdfd3880d2a7b5e125e76055563591e991d598d47b
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/validate-history.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; science assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:19:57.616473Z'
  snapshot_sha256: 30b5732b16a9cdee6c1e2bdf4ee1cc43ff359395cfbb215e2d273454479e7f3a
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000023/normalize-cache-names-check.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; science assessed separately.
  support: supports
  accessed_at: '2026-10-22T06:19:57.616855Z'
  snapshot_sha256: e0e1cb2e78359e4e62e5292181e0e0dfe17f92e2768716d77ed97ae773954846
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/audit-network.json
  locator: Fresh batch15 corpus baseline
  summary: Actual exit 1 with 44 warnings across 16/477 records, zero errors.
  support: supports
  accessed_at: '2026-10-22T06:19:57.617517Z'
  snapshot_sha256: b92af84b02acf105f8dc7c3625cc2a7e52a436b24a8243fe7e1d53012c9be1d9
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/check-network-quality.json
  locator: Fresh batch15 corpus baseline
  summary: Actual exit 1 with 44 warnings across 16/477 records, zero errors.
  support: supports
  accessed_at: '2026-10-22T06:19:57.617993Z'
  snapshot_sha256: 10b4cbb4180b20137e22c994ff8cd71d5ca52ab6ac3ef21fef5580eb4c9200fc
assessments:
- assessment_id: identity
  area: identity
  topic: Constructed strain pair and community origin
  outcome: concern
  summary: The intended strains are correct; NATURAL misstates the assembly of this
    laboratory pair.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - identity
  - record
  - strains
  - schema
  dimensions:
  - name: stable_id
    value: CommunityMech:000023
    definition: Maintained community record and exact PMID:19581361/DOI:10.1128/JB.00356-09
      source.
    evidence_ids:
    - record
    - inspection
    - abstract
  - name: source_strains
    value: D. vulgaris Hildenborough (=ATCC29579) and M. maripaludis S2
    definition: Wild-type pair; JW3040, H801, Hyd100 and NiFe100 are comparator mutants.
    evidence_ids:
    - identity
    - strains
  - name: community_scope
    value: Deliberately constructed two-member lactate-fed laboratory model
    definition: Source-dependent syntrophy is distinct from universal obligacy or
      a naturally isolated community.
    evidence_ids:
    - identity
    - schema
    - phenotypes
  details: Retain SYNTROPHY and STABLE for the maintained chemostat state, not every
    batch or mutant curve. Environmental occurrence of related partnerships does not
    establish a naturally co-isolated community.
- assessment_id: node-0
  area: graph
  topic: Lactate Oxidation and H2 Production
  outcome: supported
  summary: Retain lactate oxidation and hydrogen production.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - performance
  - machinery
  - thermodynamics
  - snippets
  details: 'Exact selector ecological_interactions[0]; interaction_type SYNTROPHY;
    scope PAIRWISE. Current participants: {"source_taxon": {"preferred_term": "Desulfovibrio
    vulgaris Hildenborough", "term": {"id": "NCBITaxon:882", "label": "Nitratidesulfovibrio
    vulgaris str. Hildenborough"}}, "target_taxon": {"preferred_term": "Methanococcus
    maripaludis S2", "term": {"id": "NCBITaxon:267377", "label": "Methanococcus maripaludis
    S2"}}}. Canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "ea43200ba6a9a624b93e51d94128f775ca5232bbeaab4580a729c02275914c53",
    "reference": "PMID:19581361", "supports": "PARTIAL", "evidence_source": "IN_VITRO"},
    {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "bf737a095da07448801a048769cbaffa7b5931ac67e5f95606861d709b72f440",
    "reference": "PMID:19581361", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 d4a788e6c8a47d7914e6bc6934dc04712b0d8f8ca6b4c61b2d44f164a7caba94.
    PMID:19581361 locator: Results sec8 paragraphs1,3–4,7; Discussion sec9 paragraphs1–6;
    Figures 1–3 and equation 1 versus8. The two Abstract excerpts provide expression
    context; body/figures support the culture phenotype. Residual 3–5 mM lactate and
    24–27 mM acetate are steady-state values, not input recipe. The uphill initial
    step is distinct from favorable whole fermentation.'
- assessment_id: node-1
  area: graph
  topic: D. vulgaris Hydrogenase-Cytochrome Electron Transfer
  outcome: supported
  summary: Retain the qualified intrinsic donor machinery.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - machinery
  - phenotypes
  - snippets
  details: 'Exact selector ecological_interactions[1]; interaction_type None; scope
    PAIRWISE. Current participants: {"source_taxon": {"preferred_term": "Desulfovibrio
    vulgaris Hildenborough", "term": {"id": "NCBITaxon:882", "label": "Nitratidesulfovibrio
    vulgaris str. Hildenborough"}}, "target_taxon": null}. Canonical snippet bindings:
    [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "8d589ad229872db2c25a5aeb9c6fb7930038eb0fc74a1565dd1bed60608dacf0",
    "reference": "PMID:19581361", "supports": "SUPPORT", "evidence_source": "IN_VITRO"},
    {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "a390d31367e5503ce1b2f26f9cd4d7a9a1ded5da7e188cd4418e64fb91e92876",
    "reference": "PMID:19581361", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 d4a788e6c8a47d7914e6bc6934dc04712b0d8f8ca6b4c61b2d44f164a7caba94.
    PMID:19581361 locator: Results sec8 paragraphs3 and7; Discussion sec9 paragraphs1,5–8;
    Figure 2 and proposed Figure 3. Coo/Hmc strongly impair lactate syntrophy; Hyd/Hyn
    slow growth but do not abolish final yield. Hmc also affects respiratory growth.
    Source-only PAIRWISE representation is valid; no new recipient or universal necessity
    is inferred.'
- assessment_id: node-2
  area: graph
  topic: Interspecies Hydrogen Transfer and Methanogenesis
  outcome: supported
  summary: Retain hydrogenotrophic methanogenesis and product-removal feedback.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - performance
  - phenotypes
  - thermodynamics
  - snippets
  details: 'Exact selector ecological_interactions[2]; interaction_type SYNTROPHY;
    scope PAIRWISE. Current participants: {"source_taxon": {"preferred_term": "Methanococcus
    maripaludis S2", "term": {"id": "NCBITaxon:267377", "label": "Methanococcus maripaludis
    S2"}}, "target_taxon": {"preferred_term": "Desulfovibrio vulgaris Hildenborough",
    "term": {"id": "NCBITaxon:882", "label": "Nitratidesulfovibrio vulgaris str. Hildenborough"}}}.
    Canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet",
    "sha256": "218bfe7b153e3d3f7df815ff434907ab83c26050788b7b010548bdeb04383835",
    "reference": "PMID:19581361", "supports": "PARTIAL", "evidence_source": "IN_VITRO"},
    {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "218bfe7b153e3d3f7df815ff434907ab83c26050788b7b010548bdeb04383835",
    "reference": "PMID:19581361", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 d4a788e6c8a47d7914e6bc6934dc04712b0d8f8ca6b4c61b2d44f164a7caba94.
    PMID:19581361 locator: Results sec8 paragraphs1 and7; Discussion sec9 paragraph6;
    Figures 1–3 and equation3. The two duplicate broad Abstract snippets remain PARTIAL
    context, not independent exact-pair experiments. Body evidence supplies methane
    dynamics, methanogen recovery and the benefit of hydrogen removal. The source
    taxon denotes the hydrogen sink, not nutrient donation back to the bacterium.'
- assessment_id: edge-0-0
  area: graph
  topic: Lactate Oxidation and H2 Production → D. vulgaris Hydrogenase-Cytochrome
    Electron Transfer
  outcome: supported
  summary: Keep the PARTIAL donor-pathway link.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - machinery
  - phenotypes
  - thermodynamics
  details: 'Exact selector ecological_interactions[0].downstream[0]; source Lactate
    Oxidation and H2 Production; target D. vulgaris Hydrogenase-Cytochrome Electron
    Transfer. Participants and exact node evidence are bound in the corresponding
    node assessments. Exact description: PARTIAL - lactate-derived electrons feed
    the proposed hydrogenase/cytochrome route. Expression and mutant phenotypes support
    contributions, not a fully resolved electron path or universal component necessity.
    Description SHA256 396ad4537a724481a616caf186e9a9d00dc39760a0dc677d97cc1acdd6bed448.
    PMID:19581361, Results sec8 paragraph7, Discussion sec9 paragraphs1,5–8 and Figures
    2–3. Lactate-derived electrons are linked to proposed donor machinery by expression
    and mutant phenotypes; the complete carrier/coupling route is unresolved.'
- assessment_id: edge-1-0
  area: graph
  topic: D. vulgaris Hydrogenase-Cytochrome Electron Transfer → Interspecies Hydrogen
    Transfer and Methanogenesis
  outcome: supported
  summary: Keep the PARTIAL machinery-to-hydrogen-consumer link.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - machinery
  - phenotypes
  - thermodynamics
  details: 'Exact selector ecological_interactions[1].downstream[0]; source D. vulgaris
    Hydrogenase-Cytochrome Electron Transfer; target Interspecies Hydrogen Transfer
    and Methanogenesis. Participants and exact node evidence are bound in the corresponding
    node assessments. Exact description: PARTIAL - donor electron-transfer machinery
    supports hydrogen provision to the methanogen. Genetic phenotypes support contribution,
    while the detailed route and coupling remain unresolved. Description SHA256 3b4c2a5c66d2fd6594882b2f7dec603a261f2c058a9a6a854a5ff301433cf61b.
    PMID:19581361, Results sec8 paragraph7, Discussion sec9 paragraphs1,5–8 and Figures
    2–3. Donor phenotypes support hydrogen supply to the methanogen without establishing
    one exclusive route or equal necessity of all hydrogenases.'
- assessment_id: edge-2-0
  area: graph
  topic: Interspecies Hydrogen Transfer and Methanogenesis → Lactate Oxidation and
    H2 Production
  outcome: supported
  summary: Keep the physiological hydrogen-removal feedback.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - machinery
  - phenotypes
  - thermodynamics
  details: 'Exact selector ecological_interactions[2].downstream[0]; source Interspecies
    Hydrogen Transfer and Methanogenesis; target Lactate Oxidation and H2 Production.
    Participants and exact node evidence are bound in the corresponding node assessments.
    Exact description: Methanogen hydrogen consumption supports the low-hydrogen conditions
    favorable to continued donor lactate fermentation, closing the physiological feedback
    loop. Description SHA256 17bfb9dd735de834e30a3b896ede6914577ef8e70fcfd947f087aeb02351ace3.
    PMID:19581361, Results sec8 paragraph7, Discussion sec9 paragraphs1,5–8 and Figures
    2–3. Methanogen consumption lowers a donor product and makes continued lactate
    oxidation more favorable. It is not reverse nutrient donation or a self-edge.'
- assessment_id: medium
  area: evidence
  topic: Source CCM versus imported formulation
  outcome: concern
  summary: The current medium combines incompatible formulations and mixes source
    assay stages.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - cultivation
  - phenotypes
  - formulation
  - chemistry
  - external-links
  dimensions:
  - name: medium
    value: Source CCM with 30 mM sodium DL-lactate; separately sulfate-amended controls
    definition: Preserve source salt hydration, original mass units and stock/final
      concentrations. Correct core formulation before remapping provider links.
    evidence_ids:
    - cultivation
    - chemistry
    - formulation
    - external-links
  - name: experimental_setting
    value: Starter100 mL/200 mL vial; continuous2 L/3 L chemostat; phenotype8 mL/17
      mL Hungate tubes
    definition: Vessel capacity and working volume differ; inoculation, batch startup
      and continuous operation are separate stages.
    evidence_ids:
    - cultivation
    - phenotypes
  - name: environment
    value: 37 °C; chemostat250 rpm, pH 7.0–7.2,N2/CO2 90:10; phenotype 300 rpm, N2/CO2
      80:20
    definition: Both are controlled anoxic experiments. Methanogen-only H2/CO2 preculture
      is not the pair atmosphere; no-added-bulk-sulfate is not chemical zero sulfate.
    evidence_ids:
    - cultivation
    - phenotypes
    - performance
  details: Source CCM uses30 mM sodium DL-lactate; per liter 2.17 g NaCl,5.5 g MgCl2·6H2O,0.14
    g CaCl2·2H2O,0.5 g NH4Cl and0.335 g KCl;1.1 mM K2HPO4 and 30 mM bicarbonate;1
    mM each cysteine hydrochloride/sulfide nonahydrate;1 mg/L resazurin. Nonchelated
    trace and vitamin stocks are each added at 1 mL/L; choline belongs to the vitamin-stock
    amendment. Current L-lactate20 mM, other doses, SL-10 assumption and yeast extract
    are not this formulation. CultureMech:000423 is DSMZ 1007 nitrate medium; its
    stock solutes must not be flattened into final CCM.
- assessment_id: claim-evidence
  area: evidence
  topic: Exact claim placement and conditional interpretation
  outcome: concern
  summary: Some Abstract excerpts are authentic but too broad for their attached protocol
    and identity claims.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - abstract
  - identity
  - cultivation
  - performance
  - metal-context
  - schema
  - snippets
  details: Taxonomy[1] excerpt names DvH, not S2; Table 1/Methods establish S2. Use
    role-local body support for both members, actual Methods for dilution and culture
    values, and source thermodynamics for hydrogen dependence. Bound obligate and
    sulfate-absence wording to the stated lactate regime. SIGNIFICANT metal/REE metabolism
    and keyword-derived measurement notes are unsupported; transport-expression interpretation
    is narrower. Correct these bounded metadata claims without regrading the supported
    graph or claiming iron absence.
- assessment_id: grounding
  area: grounding
  topic: Correct strain groundings and GTDB provenance
  outcome: concern
  summary: All 22 ontology pairs match; both GTDB cores reproduce, while release/build
    wording needs correction.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - ontology
  - gtdb
  - strains
  - chemistry
  dimensions:
  - name: taxon_grounding
    value: NCBITaxon:882 and NCBITaxon:267377; GTDB:s__Nitratidesulfovibrio_vulgaris
      and GTDB:s__Methanococcus_maripaludis
    definition: Exact strain identity and current crosswalk routes are retained. Filemtime
      is not a release/build date.
    evidence_ids:
    - ontology
    - gtdb
    - strains
  details: The local strain-ID routes support 1.0/7 for Hildenborough and 1.0/2 for
    S2. Those counts describe reference mapping, not cell abundance. Chemical label
    agreement does not make an L-only or anhydrous formulation equivalent to the source.
- assessment_id: resources
  area: representation
  topic: Expression-array and cross-Mech traceability
  outcome: concern
  summary: The source-declared array is recoverable; legacy ingredient links need
    verified identity handling.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - archive-declaration
  - resources
  - external-links
  details: Represent GSE17831 with GSM444833 and GPL9107 in its actual DvH whole-genome
    expression-array scope. Preserve archive design and sample-count boundaries. All
    21 encoded cross-Mech URLs are broken; all 20 legacy numeric MIM IDs are absent
    from the complete current index. Current chemical candidates include hydrate ambiguity
    and rejected rows, so names alone do not authorize replacement. The wrong CultureMech
    formulation is graded only in the medium finding.
- assessment_id: source-scope
  area: scope
  topic: Complete main-claim audit with bounded SI access
  outcome: supported
  summary: The main text, tables, figures and equations suffice for all currently
    encoded claims.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - assets
  - lead-read
  - locators
  - root-source
  dimensions:
  - name: evidence_tier
    value: Full main IN_VITRO phenotype/expression evidence plus explicitly proposed
      mechanistic model; SI unavailable
    definition: Authentic excerpts, direct observations and interpretations remain
      separate. Search results only identified fallback routes and filenames.
    evidence_ids:
    - abstract
    - machinery
    - thermodynamics
    - assets
    - lead-read
  details: Lead read 69,502 main characters, both biological tables, all 3 main figures
    and all 9 formula images. Supplementary tables, COG and accuracy plots were not
    recovered or read; no raw array reanalysis is claimed. This limits supplementary
    detail, not the source-grounded review of the present record.
- assessment_id: ownership
  area: ownership
  topic: Maintained owner and prior decisions
  outcome: supported
  summary: Any repair belongs to the canonical YAML under separate curation authorization.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - inspection
  - provenance
  details: Ignored-inclusive discovery pinned the sole cache, history, batch32 decision/adversarial
    and four cohort contexts. Prior graph repair is retained; this review changes
    no canonical data, cache, history, issue or Git state.
- assessment_id: native
  area: schema
  topic: Actual required validation
  outcome: supported
  summary: All eight required native checks passed.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - native-summary
  - auxiliary
  - corpus-context
  - adapter
  details: Keep nonrequired corpus failures, optional-adapter unavailability and ancillary
    reader failures separate from actual native target outcomes.
- assessment_id: metrics
  area: completeness
  topic: Literal native completeness and validation quality
  outcome: supported
  summary: Completeness90; raw quality109, capped 100.
  target_ids:
  - CommunityMech:000023
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 90
    unit: points
    minimum: 0
    maximum: 100
    definition: Required-and-roles 50 +environment 5 +four factors 10 +three nodes
      10 +medium 10 +metabolites 5 =90. No external-resource or dataset bonus. Literal
      completeness does not certify source correctness.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: Base 100 +20*min((6 evidence/3 nodes)/2,1)=20 +15 COMPLETE =135; subtract
      2 major*10 and 3 minor*2 to obtain 109, capped 100. Network completion does
      not establish causation.
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
- finding_id: medium-assay
  issue_key: cm-000023-medium-assay
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material source identity or experimental-condition misrepresentation.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Reconstruct source CCM and separate culture stages
  description: The current recipe and imported DSMZ 1007 nitrate-medium components
    do not represent the source CCM. Culture conditions combine chemostat and phenotype
    stages.
  target_ids:
  - CommunityMech:000023
  field_paths:
  - growth_media[0]
  - cultivation_setup
  evidence_ids:
  - cultivation
  - phenotypes
  - chemistry
  - formulation
  - external-links
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable sources/history/review
    artifacts remain unchanged.
- finding_id: constructed-origin
  issue_key: cm-000023-constructed-origin
  category: identity
  severity: major
  native_severity: P2
  normalization_reason: Material source identity or experimental-condition misrepresentation.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Correct the community origin
  description: NATURAL conflicts with the explicitly constructed two-member laboratory
    model.
  target_ids:
  - CommunityMech:000023
  field_paths:
  - community_origin
  evidence_ids:
  - identity
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable sources/history/review
    artifacts remain unchanged.
- finding_id: claim-evidence
  issue_key: cm-000023-claim-evidence
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: Bounded provenance, evidence-placement or resource follow-up;
    core source-supported mechanism remains intact.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Use exact claim evidence and bounded non-graph interpretation
  description: Generic Abstract snippets are attached to specific identity/protocol
    claims. Unconditional dependence and significant measured metal/REE claims exceed
    the source context.
  target_ids:
  - CommunityMech:000023
  field_paths:
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  - description
  - environmental_factors
  - growth_media[0].evidence
  - metal_relevance
  - metal_notes
  evidence_ids:
  - identity
  - cultivation
  - performance
  - thermodynamics
  - metal-context
  - snippets
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable sources/history/review
    artifacts remain unchanged.
- finding_id: gtdb-provenance
  issue_key: cm-000023-gtdb-provenance
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Bounded provenance, evidence-placement or resource follow-up;
    core source-supported mechanism remains intact.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Correct GTDB release/build provenance
  description: Both mapping_source strings overstate the meaning of a local filesystem
    modification date; the actual cores reproduce.
  target_ids:
  - CommunityMech:000023
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable sources/history/review
    artifacts remain unchanged.
- finding_id: resource-traceability
  issue_key: cm-000023-resource-traceability
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded provenance, evidence-placement or resource follow-up;
    core source-supported mechanism remains intact.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Add the source array and repair verified legacy links
  description: The declared GEO array resource is absent, and legacy ingredient URLs
    need current identity handling. Wrong medium identity is already graded once in
    medium-assay.
  target_ids:
  - CommunityMech:000023
  field_paths:
  - associated_datasets
  - external_resources
  - growth_media[0].composition
  evidence_ids:
  - archive-declaration
  - resources
  - external-links
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
  ownership_note: Future canonical curation only; immutable sources/history/review
    artifacts remain unchanged.
actions:
- action_id: repair-medium
  description: Replace the mixed recipe with source CCM and distinct assay contexts.
  finding_ids:
  - medium-assay
  target_ids:
  - CommunityMech:000023
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Use the source 30 mM sodium DL-lactate formulation and exact salts/units from
    Biomass production first paragraph; retain correct 1 mM reducing agents and 30
    mM bicarbonate. Verified candidate CHEBI:75228 is non-stereospecific sodium lactate,
    so retain DL explicitly. Use CHEBI:86345 and CHEBI:86158 for source weighed Mg/Ca
    hydrates where appropriate.
  - Remove the unrelated CultureMech:000423/DSMZ 1007 identity and imported nitrate-medium
    component block. Do not treat its trace-stock solute concentrations as final CCM
    or invent a replacement CultureMech record. Preserve1 mL/L nonchelated trace/vitamin
    stock boundaries; do not equate the source stock to SL-10 without evidence.
  - Represent100 mL in200 mL starter vial at 37 °C/dark/250 rpm; then2 L in3 L chemostat
    with90:10 N2/CO2, 250 rpm, pH 7.0–7.2 and0.039 h−1. Distinguish batch startup
    and subsequent continuous operation.
  - Represent phenotype cultures separately:8 mL in17 mL Hungate tubes,37 °C/dark/300
    rpm,80:20 N2/CO2,30 mM lactate or pyruvate. Preserve sulfate-amended comparator
    and H2/acetate methanogen preculture separately, plus source inoculation/transfers.
    Do not transfer the phenotype headspace to the chemostat.
- action_id: repair-origin
  description: Represent the deliberately assembled pair.
  finding_ids:
  - constructed-origin
  target_ids:
  - CommunityMech:000023
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Set source-supported SYNTHETIC or ENGINEERED origin with Introduction/Methods/Table
    1 evidence; retain exact strain IDs and category. Keep STABLE limited to the observed
    chemostat steady state.
- action_id: repair-claim-evidence
  description: Replace broad evidence placements and qualify non-graph scope.
  finding_ids:
  - claim-evidence
  target_ids:
  - CommunityMech:000023
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Use source Strains/Table 1 for S2 and Hildenborough, role-local Results/Discussion
    for metabolism, and Biomass production for dilution and medium conditions. Existing
    broad node2 excerpts may be supplemented by direct body evidence without changing
    the supported graph.
  - Qualify dependence to the tested lactate/no-added-bulk-sulfate regime and preserve
    authors’ trace sulfate acknowledgment. Do not call the whole fermentation uphill;
    equations 1/8 and observed-state calculations describe different reactions.
  - Remove unsupported SIGNIFICANT metal/REE metabolism and keyword-based environmental-measurement
    notes. If a metal annotation remains, ground it only in the source transport-expression
    interpretation and actual trace/machinery context; do not claim iron is absent.
- action_id: repair-provenance
  description: Record actual crosswalk and source-resource provenance.
  finding_ids:
  - gtdb-provenance
  - resource-traceability
  target_ids:
  - CommunityMech:000023
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Replace latest/build-date wording with actual crosswalk hash/access provenance;
    preserve both exact strain-ID GTDB cores and reference counts.
  - Add GSE17831 and its verified GSM444833/GPL9107 context as DvH expression profiling
    by array, using exact metadata. Do not label it community RNA sequencing or infer
    independent sample counts from merged array entries.
  - Resolve ingredient links by verified chemical identity, hydration and stock scope.
    All 20 legacy numeric MIM identifiers are absent from the current complete index;
    rejected or ambiguous candidates must not be automatically remapped. Repair broken
    URLs only where exact identity is established.
- action_id: validate-curation
  description: Validate any separately authorized canonical repair.
  finding_ids:
  - medium-assay
  - constructed-origin
  - claim-evidence
  - gtdb-provenance
  - resource-traceability
  target_ids:
  - CommunityMech:000023
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Desulfovibrio_Methanococcus_Syntrophy.yaml
    role: canonical_record
  acceptance_checks:
  - Run focused schema/strict/ontology/reference/GTDB/history checks and required
    generated-document checks after actual canonical changes. Preserve original caches/history
    and existing graph repair.
  - Recheck all three node scopes and three arrow directions against Figures 1–3/Results/Discussion.
    Root alone saves this review and runs post-save gates.
limitations:
- Supplementary table/figure PDFs were not recovered after bounded ordinary public
  routes. All failed/challenge/error payloads are preserved and excluded as scientific
  sources. No SI transcript-list, COG or accuracy-plot read is claimed; full main
  and figures suffice for current encoded claims.
- Expression changes and mutant phenotypes support the proposed donor model but do
  not resolve an exclusive carrier/proton-coupling route. Whole fermentation is favorable;
  the initial lactate-to-pyruvate step and reverse-flow requirement retain the source
  uncertainty.
- Chemostat, starter, mutant phenotype assays and single-species precultures have
  distinct conditions. Authors acknowledge trace sulfate; no universal zero-sulfate
  or obligacy claim is inferred.
- No raw microarray matrix reanalysis or uncited-reference audit was performed. GEO
  metadata and cross-Mech identity checks retain their declared scope. Rejected or
  ambiguous modern ingredient candidates are not replacements.
- Optional structured adapter was unavailable in the owned runtime; separate corpus
  diagnostic exits and ancillary reader failures are not native target failures.
notes:
- Eight evidence-linked dimensions cover stable identity, source strains, community
  scope, taxonomy, medium, setting, environment and evidence tier. Six canonical graph
  excerpt hashes and three exact arrow descriptions are bound once in their assessments.
- The sole primary-source quote contains two words. Thirty official inputs remain
  unchanged; snapshots preserve actual access and read scope.
- Completed scientific review is distinct from repository persistence; root owns save
  and required post-save gates.
tags:
- record-review
- syntrophy
- methanogenesis
- batch-15
```
