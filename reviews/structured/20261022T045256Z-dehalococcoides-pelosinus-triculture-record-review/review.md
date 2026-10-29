# Dhc195–DvH–PfR7 corrinoid triculture review

- Review: 20261022T045256Z-dehalococcoides-pelosinus-triculture-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T04:47:20.207583Z
- Finished UTC: 2026-10-22T04:52:56.379397Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact strain identities and all four qualified nodes/three arrows are supported. Two major findings concern donor role labels and array classification/comparison scope; three minor findings concern protocol completeness, experimental evidence tier and GTDB provenance. Eight focused native checks pass. Literal completeness 100 and capped quality 100 (raw 109) do not negate these findings.

## Scope And Provenance

Whole target and sole primary main article including both tables, six figures and fresh MED record; bounded declared SI attempts; exact stock/ontology/archive/prior context. Source bytes reused by verified immutable hashes.

Selection: Only released CommunityMech:000200 in owned batch 15.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb7a782c8ba80299dca8761ad0a2c90bccd8a117.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000200 | kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml | maintained | Dehalococcoides-Desulfovibrio-Pelosinus Corrinoid Triculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000200 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000200 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000200 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000200 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000200 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000200 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000200 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000200 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000200 | Actual corpus exit 1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000200 | Actual corpus exit 1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000200 | Unavailable in owned runtime. |

## Scientific And Domain Assessments

### Defined three-strain scope

identity: supported. Targets: CommunityMech:000200.

Retain the exact laboratory triculture and existing source synonyms.

The NCBI IDs are strain-level: 243164, 882 and 1122947. R7/DSM 17108/ATCC BAA-1133 identity, type status and kaolin locality are supported. PfR7 catalogue isolation years differ, but no year is encoded. Figure 2 supports qualitative Dhc195 prominence; no fixed percentage threshold or exact cross-table population conversion is imposed.

### Directed function of both donors

grounding: concern. Targets: CommunityMech:000200.

Two optional role labels on each fermenter exceed the demonstrated uptake direction.

DvH and PfR7 compete for supplied lactate. DvH also ferments its own formate; Dhc195 hydrogen removal supports energetics. Neither observation establishes fermentation of primary-degrader products or uptake of another member’s metabolites by these donors. Retain Dhc195 PRIMARY_DEGRADER and the supported syntrophic relationship; do not invent replacement roles.

### Hydrogen Provision By Desulfovibrio

graph: supported. Targets: CommunityMech:000200.

Retain hydrogen provision and reciprocal hydrogen-removal energetics.

Exact selector ecological_interactions[0]; scope PAIRWISE; interaction_type SYNTROPHY. Actual taxa: {"source": {"preferred_term": "Desulfovibrio vulgaris Hildenborough", "term": {"id": "NCBITaxon:882", "label": "Nitratidesulfovibrio vulgaris str. Hildenborough"}}, "target": {"preferred_term": "Dehalococcoides mccartyi strain 195", "term": {"id": "NCBITaxon:243164", "label": "Dehalococcoides mccartyi 195"}}, "participants": []}. Canonical excerpt bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "e626d8bedde7b1e2919564bd3ef15aabe80156d5ed6a3daeb8d07b56d2cc62c2", "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}, {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "27e5965896f3e918d5a4c954c3a5cb823f4051988e62b3ba03d496713c83e5ff", "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 a581622c0adeb013f05bb720fc808a26787d562cfc5404739b4f79f7daf24c0d. PMID24463969 source locators: Results #sec3-1 paragraphs 1–4, Table 1 and Figures 1–2. Retain SUPPORT and IN_VITRO. 882 → 243164. Cobalamin-free sustainability additionally requires PfR7 and external DMB; hydrogen alone is insufficient.

### Corrinoid Provision By Pelosinus

graph: supported. Targets: CommunityMech:000200.

Retain PfR7 corrinoid provision with the external-DMB qualifier.

Exact selector ecological_interactions[1]; scope PAIRWISE; interaction_type CROSS_FEEDING. Actual taxa: {"source": {"preferred_term": "Pelosinus fermentans R7", "term": {"id": "NCBITaxon:1122947", "label": "Pelosinus fermentans DSM 17108"}}, "target": {"preferred_term": "Dehalococcoides mccartyi strain 195", "term": {"id": "NCBITaxon:243164", "label": "Dehalococcoides mccartyi 195"}}, "participants": []}. Canonical excerpt bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "8380a899d81f43350ace337478368e32442ec7a01d34e49115dce4ad62eed03e", "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}, {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "48eb91b34421fefd729a0d39942ae90ef54692cc1a7795bfa51c187065b7f788", "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 a581622c0adeb013f05bb720fc808a26787d562cfc5404739b4f79f7daf24c0d. PMID24463969 source locators: Results #sec3-2 sole paragraph, Table 2/Figure 3; Discussion paragraphs 2–4. Retain SUPPORT and IN_VITRO. 1122947 → 243164. Donor guided cobalamin biosynthesis remains possible; cobalamin is not every transferred corrinoid.

### Dhc195 Corrinoid Salvaging And Remodeling

graph: supported. Targets: CommunityMech:000200.

Retain recipient-intrinsic salvaging/remodeling as a qualified process.

Exact selector ecological_interactions[2]; scope PAIRWISE; interaction_type absent. Actual taxa: {"source": {"preferred_term": "Dehalococcoides mccartyi strain 195", "term": {"id": "NCBITaxon:243164", "label": "Dehalococcoides mccartyi 195"}}, "target": null, "participants": []}. Canonical excerpt bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "0a409ec15aa1978cd357354003a3cc16d4266d3c34624efef889467c2778be37", "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}, {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "971f9216ff8282d5b59b3fdc1949e37dc3b0c1046fd7c4f648c9618253f3c4f0", "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 a581622c0adeb013f05bb720fc808a26787d562cfc5404739b4f79f7daf24c0d. PMID24463969 source locators: Results #sec3-2 and #sec3-3 paragraphs 2–3; Figures 3, 5–6; Discussion paragraphs 4 and 6–7. Retain SUPPORT and IN_VITRO. Source 243164, target absent. The source-only PAIRWISE scope is valid. Measured induction is not a selective gene-necessity or transporter-activity experiment.

### Hydrogen- and Corrinoid-Supported TCE Dechlorination

graph: supported. Targets: CommunityMech:000200.

Retain the conditional community dechlorination and growth outcome.

Exact selector ecological_interactions[3]; scope COMMUNITY_LEVEL; interaction_type absent. Actual taxa: {"source": null, "target": null, "participants": [{"preferred_term": "Dehalococcoides mccartyi strain 195", "term": {"id": "NCBITaxon:243164", "label": "Dehalococcoides mccartyi 195"}}, {"preferred_term": "Desulfovibrio vulgaris Hildenborough", "term": {"id": "NCBITaxon:882", "label": "Nitratidesulfovibrio vulgaris str. Hildenborough"}}, {"preferred_term": "Pelosinus fermentans R7", "term": {"id": "NCBITaxon:1122947", "label": "Pelosinus fermentans DSM 17108"}}]}. Canonical excerpt bindings: [{"selector": "ecological_interactions[3].evidence[0].snippet", "sha256": "75c687ed36de54591adf6524c7927af8d26332848845422c45c556670f242ba2", "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}, {"selector": "ecological_interactions[3].evidence[1].snippet", "sha256": "02821924274a3570e4f91fc9896be06d5e265bf3e9b978dc932271489dd1a2b3", "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 a581622c0adeb013f05bb720fc808a26787d562cfc5404739b4f79f7daf24c0d. PMID24463969 source locators: Results #sec3-1 paragraphs 1–3 and Figure 2; Abstract sustainable-growth sentence. Retain SUPPORT and IN_VITRO. Participants 243164, 882 and 1122947. Cobalamin-free performance depends on DMB; cobalamin-amended controls and hydrogen-supplemented alternative pairs are not denied.

### Hydrogen Provision By Desulfovibrio → Hydrogen- and Corrinoid-Supported TCE Dechlorination

graph: supported. Targets: CommunityMech:000200.

Retain the hydrogen input to the conditional community endpoint.

Exact selector ecological_interactions[0].downstream[0]; source node 0 → target node 3. 882 → recipient 243164 within the three-member community. Exact edge description: DvH-supplied hydrogen supports the electron-donor requirement of Dhc195 in the lactate-fed triculture, together with partner corrinoids and externally supplied DMB. Hydrogen provision alone does not make the cobalamin-free two-member coculture sustainable. Description SHA256 1bc84c883128af76af6593d060f7fc04fdf49efbdec9e66c454e256a5ae11e74. PMID24463969 locators: Results #sec3-1 paragraphs 1–4, Table 1/Figures 1–2. External DMB, donor guided biosynthesis and lack of selective route partition remain explicit.

### Corrinoid Provision By Pelosinus → Dhc195 Corrinoid Salvaging And Remodeling

graph: supported. Targets: CommunityMech:000200.

Retain precursor provision to recipient remodeling without making it exclusive.

Exact selector ecological_interactions[1].downstream[0]; source node 1 → target node 2. 1122947 → 243164; DMB is externally supplied. Exact edge description: PfR7 supplies corrinoid substrates that Dhc195 can salvage and remodel in the presence of externally supplied DMB. This does not exclude donor guided cobalamin biosynthesis or establish that all functional cofactor passes through recipient remodeling. Description SHA256 c7e20401c8f8ca2b55186473a8cb9c572d19c95ece87f491f35c28f1537faa2d. PMID24463969 locators: Results #sec3-2, Table 2/Figure 3; Discussion paragraph 4. External DMB, donor guided biosynthesis and lack of selective route partition remain explicit.

### Dhc195 Corrinoid Salvaging And Remodeling → Hydrogen- and Corrinoid-Supported TCE Dechlorination

graph: supported. Targets: CommunityMech:000200.

Retain the qualified compatible-cofactor contribution to community function.

Exact selector ecological_interactions[2].downstream[0]; source node 2 → target node 3. Recipient 243164 process → community participants 243164/882/1122947. Exact edge description: Recipient salvaging and remodeling contributes compatible cofactor for sustainable TCE dechlorination in the DMB-amended triculture when DvH supplies hydrogen. The source supports this route but does not selectively separate its contribution from cobalamin formed by the donor in the presence of DMB. Description SHA256 7e1c37c9f2b1f1ab5ef0d19973e56471e99b82e40e659b6e47d40b33136d02d1. PMID24463969 locators: Results #sec3-1 paragraphs 1–3 and #sec3-2; Discussion paragraphs 4 and 6–7. External DMB, donor guided biosynthesis and lack of selective route partition remain explicit.

### Recoverable protocol and assay boundaries

scope: concern. Targets: CommunityMech:000200.

The partial medium is accurate but omits source-specific culture details.

The preparation note declines to assert the complete recipe; it does not claim the source lacks conditions. The current paper supplies the vessel, gas, doses, inoculation, incubation and passages. Basal salts/vitamins refer to earlier study 24 and are not reconstructed here. Keep pure-PfR7 pH 7.5 and catalogue recipes separate.

### Chemical and process scope

grounding: supported. Targets: CommunityMech:000200.

All thirteen ID-label pairs are correct at the stated scope.

Preserve lactate, TCE, hydrogen, cobalamin and DMB identities. Cobalamin is not a generic label for all corrinoids. GO cobalamin transport denotes movement, while current prose correctly separates measured transcript induction from direct transporter activity. No additional transporter or gene-necessity claim is inferred.

### Array classification and experimental comparisons

evidence: concern. Targets: CommunityMech:000200.

GSE45533 is a strain-targeted expression array, not community RNA sequencing.

Its nine samples compare Dhc195 in a cobalamin-amended Dhc195/DvH pair, cobalamin-amended triculture and DMB-amended cobalamin-free triculture. A Dhc195/PfR7-only array arm is not present. Preserve the correct accession and reference assemblies.

### Measured transcript evidence

evidence: concern. Targets: CommunityMech:000200.

The resource evidence is experimental; COMPUTATIONAL is the wrong tier.

Change only the incorrectly tagged external-resource evidence and its claim-local explanation. Existing node-2 experimental evidence and mechanistic caveats are already appropriate.

### Verified mappings and unsupported build wording

provenance: concern. Targets: CommunityMech:000200.

All three mapping cores reproduce; release/build provenance needs repair.

Keep exact strain routes, domain, lineage, fraction 1.0 and denominators 5/7/3. The local timestamp is mtime, not an upstream GTDB build date or proof of latest release.

### Prior graph repair and curation owner

ownership: supported. Targets: CommunityMech:000200.

The maintained focal YAML owns the five future repairs.

The sole history and exact batch 30 focal review remain intact. The dated discussion accurately records its earlier reading scope; this review adds current evidence without rewriting that event. Shared open issue scope is not closed by this target review.

### Completion at explicit source scope

scope: supported. Targets: CommunityMech:000200.

The complete main article resolves the current claims; supplementary limits remain explicit.

Current lead reading covers the whole main, two tables, six figures and fresh MED record. The declared supplementary PDF/XLS returned challenge or error payloads and were not read. No negative biological inference or required correction rests on their absence. No raw sequence/expression reanalysis or figure digitization was performed.

### Native and contextual checks

schema: supported. Targets: CommunityMech:000200.

All eight required native checks passed.

The two corpus failures and optional adapter are nonrequired. Actual candidate validation and parent saving are not asserted in advance.

### Literal native metrics

completeness: supported. Targets: CommunityMech:000200.

Completeness 100; raw validation quality 109, capped 100.

## Findings

### donor-roles: Align both fermenter role tags with metabolic direction

major / open / confirmed; issue key: cm-000200-donor-roles.

DvH and PfR7 use supplied lactate. Their donor functions do not establish utilization of other members’ metabolites or fermentation of products from primary degraders. DvH self-produced formate fermentation and hydrogen removal do not supply the missing directed evidence.

### dataset-type: Correct array category, repository and comparison scope

major / open / confirmed; issue key: cm-000200-dataset-type.

GSE45533 measures strain-195 expression by array. METATRANSCRIPTOMICS denotes community RNA sequencing, and the description obscures the three actual pair/triculture conditions.

### cultivation: Encode available triculture protocol details

minor / open / confirmed; issue key: cm-000200-cultivation.

The partial medium omits recoverable vessel, gas, dose, inoculation, incubation and passage details. These can be added without inventing a full basal recipe or merging controls.

### omics-evidence: Use experimental evidence for measured array expression

minor / open / confirmed; issue key: cm-000200-omics-evidence.

The external-resource excerpt is exact but COMPUTATIONAL mislabels a laboratory measurement. Keep molecular inference distinct from the experimental evidence tier.

### gtdb-provenance: Correct unsupported GTDB release/build provenance

minor / open / confirmed; issue key: cm-000200-gtdb-provenance.

Three valid mapping cores carry latest-release/build wording derived from local mtime rather than verified upstream metadata.

## Recommended Actions And Acceptance Checks

### repair-roles

Qualify or remove the unsupported optional donor-role labels.

- For both donors, omit SECONDARY_FERMENTER and CROSS_FEEDER unless source-local evidence supports the literal precursor/recipient definitions. Do not imply the organisms can never perform such metabolism or invent replacement enums.
- Retain the supported hydrogen syntrophy, PfR7-to-Dhc195 corrinoid CROSS_FEEDING interaction, Dhc195 PRIMARY_DEGRADER, and all current graph caveats. Role-enum uptake semantics do not invalidate a donor-to-recipient exchange node.

### repair-dataset

Represent the verified array and its three comparisons precisely.

- Use TRANSCRIPTOMICS and NCBI_GEO for GSE45533, including the external-resource repository. Preserve accession/URL and identify the strain-195 GPL10838 array with nine samples.
- Name the +B12 Dhc195/DvH pair, +B12 triculture and +DMB/no-B12 triculture. Do not assert a PfR7-only partner array arm, community RNA sequencing, or raw-data reanalysis. Keep reference assemblies separate from this expression dataset.

### enrich-cultivation

Add source-specific culture and transfer details.

- Cite Methods Bacterial cultures and growth conditions, sole paragraph: 160 mL sealed serum bottles,100 mL basal medium/60 mL N2:CO2 90:10;approximately0.7 mmol lactate and77 µmol TCE;1% pregrown Dhc195/DvH plus2% pregrown PfR7;34°C,dark,no shaking. Use structured values with normal units and source evidence.
- Separate the focal no-B12/36 nM DMB arm from74 nM B12 controls. Record measurements after six 3% vol/vol subcultures and biological triplicates. Do not convert this into an unreported fixed transfer interval or daily protocol.
- Do not assign pure-PfR7 maintenance pH 7.5 to the triculture or import vendor media. The complete basal recipe is cited to prior study 24; leave unverified components unasserted.

### repair-evidence

Correct the measured-expression evidence tier.

- Use IN_VITRO for external_resources[1].evidence[0], with a claim-local experimental explanation and exact Methods/Results excerpt if expanded. Existing node-2 IN_VITRO evidence remains intact.
- Keep transcript induction separate from gene necessity, direct transporter activity and exclusive cofactor-route partition. Revalidate exact excerpts.

### repair-gtdb

Retain reproduced cores with truthful snapshot provenance.

- Preserve exact strain-ID routes to Dehalococcoides mccartyi, Nitratidesulfovibrio vulgaris and Pelosinus fermentans;fraction 1.0, reference counts 5/7/3 and current lineages. These counts are not culture abundance.
- Use mapping SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd. Identify the 2026-07-25 filesystem date only as mtime; leave unverified upstream release/build unknown.

### validate-curation

Validate any separately authorized maintained-record repair.

- Recheck source-specific strains, treatments, doses and graph qualifiers, then focused schema/strict/terms/explained-reference/GTDB/domain/history checks. Run just gen-html and just check-docs-current when canonical curation is authorized.
- Preserve source/cache/history/prior bytes. This review does not authorize canonical, issue, Git or status mutations.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml; Whole maintained YAML | supports | Three exact strains, four scoped interaction nodes and three downstream arrows. |
| cultivation | PMID:24463969; DOI:10.1128/AEM.03477-13; Materials and methods → Bacterial cultures and growth conditions, sole direct paragraph (#sec2-1/p[1]; quoted words) | supports | Defines the vessel, gas, amendments, inoculation, incubation and repeated transfers. The pure-PfR7 maintenance pH is separate from the triculture. |
| growth | PMID:24463969; DOI:10.1128/AEM.03477-13; Results → Growth of Dhc195 in defined consortia with and without exogenous cobalamin, four direct paragraphs (#sec3-1); Figures 1–2 and Table 1 | supports | Lactate-fed partners supply hydrogen, acetate and corrinoids. Comparisons distinguish cobalamin-amended controls from the DMB-amended cobalamin-free triculture. Both fermenters compete for supplied lactate. |
| corrinoids | PMID:24463969; DOI:10.1128/AEM.03477-13; Results → Corrinoid production and modification, sole paragraph (#sec3-2), Table 2 and Figure 3; Discussion paragraphs 2–4 (#sec4) | supports | Corrinoid profiles support recipient remodeling but do not exclude PfR7 cobalamin production when DMB is provided. DvH nondetection is bounded to the assay; DMB is external. |
| microarray | PMID:24463969; DOI:10.1128/AEM.03477-13; Materials and methods → Transcriptomic microarray and data analysis, two paragraphs (#sec2-4), and Microarray data accession number, sole paragraph (#sec2-6); Results → Transcriptomic comparison of Dhc195 grown in co- and tricultures, three paragraphs (#sec3-3); Figures 4–6 | supports | Strain-195 expression was measured by array in three pair/triculture conditions. Induction is distinct from selective gene necessity or direct transporter activity. |
| mechanism | PMID:24463969; DOI:10.1128/AEM.03477-13; Discussion, paragraphs 4 and 6–7 (#sec4); Figures 3, 5 and 6 | supports | Metabolite and expression patterns support the qualified remodeling route; no exclusive partition of donor biosynthesis versus recipient remodeling is demonstrated. |
| ontology | /private/tmp/cm-review-session/batch-15/000200/ontology-authority.json; 13 distinct ontology pairs / 39 placements | supports | All labels match; relevant definitions and strain ranks were checked. |
| schema | /private/tmp/cm-review-session/batch-15/000200/child-schema-semantics.json; Literal role, interaction, evidence and cultivation definitions | supports | Recipient role tags require utilization of another taxon’s metabolites; a donor function alone is insufficient. |
| stocks | /private/tmp/cm-review-session/batch-15/000200/child-strain-authority.json; Exact strain and collection identity sections | supports | R7 equals DSM 17108 / ATCC BAA-1133. The other two exact stock authorities are reused with hashes. Catalogue maintenance conditions are not study conditions. |
| gtdb | /private/tmp/cm-review-session/batch-15/000200/child-gtdb-crosswalk.json; Three exact strain-ID routes | supports | Fractions 1.0 with reference counts 5/7/3 reproduce; local file mtime is not a verified upstream release or build date. |
| semantics | /private/tmp/cm-review-session/batch-15/000200/ontology-semantic-notes.json; Final source-local auxiliary assessment | supports | Preserves identities, chemistry and graph qualifiers; records the five agreed repair groups. |
| resources | /private/tmp/cm-review-session/batch-15/000200/dataset-verification.json; GSE45533 and three encoded assemblies | supports | Exact study and reference-stock resources are assessed separately; expression-array samples are not community RNA sequencing. |
| snippets | /private/tmp/cm-review-session/batch-15/000200/snippet-audit.json; All 28 canonical excerpt placements | supports | Exact source/cache matches establish textual provenance; entailment is assessed independently. |
| provenance | /private/tmp/cm-review-session/batch-15/000200/provenance-audit.json; Exact focal history/prior decision and cohort contexts | supports | The earlier graph repair remains valid. Shared non-graph follow-up is not silently closed. |
| inspection | /private/tmp/cm-review-session/batch-15/000200/inspect.json; 30 immutable inputs | supports | One target, 21 authorities and eight focal contexts, after ignored-inclusive discovery excluding environment files and Git/runtime internals. |
| reuse | /private/tmp/cm-review-session/batch-15/000200/source-reuse-verification.json; Verified immutable source reuse from 000199 | supports | Same PMID source bytes and retrieval receipts are reused explicitly; the preceding pair’s scientific judgment is not imported. |
| assets | /private/tmp/cm-review-session/batch-15/000200/lead-source-assets.json; Main article, six images and declared supplementary routes | supports | Complete main and all six figures are available. Declared PDF/XLS responses are HTML challenges or errors, not read supplementary payloads. |
| lead-read | /private/tmp/cm-review-session/batch-15/000200/lead-primary-read-scope.json; Actual current-target reading | supports | Entire main, both tables, six captions, all six figure images and fresh MED record were re-read at the explicit scope. |
| locators | /private/tmp/cm-review-session/batch-15/000200/source-locator-verification.json; Direct heading/paragraph inventory and main table rows | supports | The sole two-word quote was checked in the culture Methods paragraph; no inferred section numbering. |
| source-audit | /private/tmp/cm-review-session/batch-15/000200/source-audit.json; Reconciled source judgment | supports | Two major and three minor findings; current claims are adjudicated despite explicit supplementary-access limits. |
| root-source | /private/tmp/cm-review-session/batch-15/000200/root-independent-source-audit.json; Independent root science and exact read scope | supports | Root agrees with the five findings and preserves distinct current/reused figure and catalogue reading bounds. |
| metrics | /private/tmp/cm-review-session/batch-15/000200/support-final-audit.json; Final support reconciliation | supports | Literal completeness 100; base quality 135 minus 26 gives raw 109, capped 100. |
| support-manifest | /private/tmp/cm-review-session/batch-15/000200/support-frozen-manifest.json; Frozen supporting dependencies | supports | Source, resource, provenance and metric reconciliation is complete. |
| auxiliary | /private/tmp/cm-review-session/batch-15/000200/auxiliary-frozen-manifest.json; Frozen native/authority dependencies | supports | Eight required native checks pass; their success does not establish scientific entailment. |
| final-native | /private/tmp/cm-review-session/batch-15/000200/final-validator-summary.json; Actual eight command receipts | supports | Focused passes and unchanged official inputs are documented. |
| corpus-context | /private/tmp/cm-review-session/batch-15/000200/child-corpus-context.json; Fresh batch 15 corpus baseline | supports | Two nonrequired corpus checks returned exit 1 with 44 warnings across 16 of 477 records and zero errors. |
| adapter | /private/tmp/cm-review-session/batch-15/000200/adapter-check.json; Owned-runtime optional adapter | supports | Unavailable in this runtime; no external-checkout execution or global absence claim. |
| check-validate | /private/tmp/cm-review-session/batch-15/000200/validate.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support is assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-15/000200/validate-strict.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support is assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-15/000200/validate-terms.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support is assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-15/000200/validate-references-explained.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support is assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-15/000200/validate-gtdb.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support is assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-15/000200/validate-gtdb-domain.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support is assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-15/000200/validate-history.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support is assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-15/000200/normalize-cache-names-check.json; Actual command/stdout/stderr | supports | Actual native exit 0; scientific support is assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-15/audit-network.json; Fresh batch 15 corpus baseline | supports | Actual exit 1; 44 warnings across 16/477 records, zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-15/check-network-quality.json; Fresh batch 15 corpus baseline | supports | Actual exit 1; 44 warnings across 16/477 records, zero errors. |

## Limits And Additional Notes

- Declared supplementary PDF/XLS payloads were not recovered on bounded ordinary PMC/ASM/EPMC routes; challenge/error responses are preserved. No supplementary content or absence-based biological conclusion is claimed. The complete main resolves the current record claims.
- The complete basal recipe is referenced to earlier study 24 and was not reconstructed. Pure-PfR7 pH and catalogue maintenance conditions are not triculture conditions.
- No raw expression/genome reanalysis, figure digitization or exact cross-table per-cell population reconstruction. Qualitative abundance is supported independently of unresolved source reporting differences.
- Four node assessments bind eight exact canonical snippet hashes and actual taxa; three edge assessments preserve exact direction and description hashes.
- The only quoted primary wording is two words from the sole culture Methods paragraph. All 30 official inputs remain unchanged.
- Actual candidate validation and parent-owned saving/post-save gates follow this review.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T045256Z-dehalococcoides-pelosinus-triculture-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Dhc195–DvH–PfR7 corrinoid triculture review
started_at: '2026-10-22T04:47:20.207583Z'
finished_at: '2026-10-22T04:52:56.379397Z'
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
summary: Exact strain identities and all four qualified nodes/three arrows are supported.
  Two major findings concern donor role labels and array classification/comparison
  scope; three minor findings concern protocol completeness, experimental evidence
  tier and GTDB provenance. Eight focused native checks pass. Literal completeness
  100 and capped quality 100 (raw 109) do not negate these findings.
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
  - path: history/records/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture/2026-10-06T054824Z-codex-290d65.yaml
    sha256: 50b79b96818647aef72b689be1ae95fb6345496fda7e7c753413529682646581
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    sha256: 2d771dc7df594f59d55d100bdf4e7ed6bbc571dfea0a4e37a774583e831910dc
    role: target
  - path: references_cache/PMID_24463969.md
    sha256: 630100bad057e96e0bca2800ca31a2f1eae6ab54bccfb38c03375a70cc116de1
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch30.yaml
    sha256: 173e2bfe58bed7b38cbf3e535062651728c15533668958b6e56dc8332b5c9e2f
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch30.yaml
    sha256: cb60e4a113592fd34842090d5f2db473831a31066febb469d2438a8d8b217c3c
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
- target_id: CommunityMech:000200
  path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
  label: Dehalococcoides-Desulfovibrio-Pelosinus Corrinoid Triculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
scope:
  description: Whole target and sole primary main article including both tables, six
    figures and fresh MED record; bounded declared SI attempts; exact stock/ontology/archive/prior
    context. Source bytes reused by verified immutable hashes.
  selection: Only released CommunityMech:000200 in owned batch 15.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000200
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000200
  command: just --no-dotenv validate kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000200
  command: just --no-dotenv validate-strict kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    --out /private/tmp/cm-review-session/batch-15/000200/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000200
  command: just --no-dotenv validate-terms kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000200
  command: just --no-dotenv validate-references-explained kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000200
  command: just --no-dotenv validate-gtdb kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000200
  command: just --no-dotenv validate-gtdb-domain kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000200
  command: just --no-dotenv validate-history history/records/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000200
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000200
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-15/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, distinct from focused passes.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000200
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-15/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, distinct from focused passes.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in owned runtime.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - adapter
  scope_note: No external adapter execution or absence-based biological inference.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
  locator: Whole maintained YAML
  summary: Three exact strains, four scoped interaction nodes and three downstream
    arrows.
  support: supports
  accessed_at: '2026-10-22T04:52:56.376933Z'
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:24463969; DOI:10.1128/AEM.03477-13
  locator: Materials and methods → Bacterial cultures and growth conditions, sole
    direct paragraph (#sec2-1/p[1]; quoted words)
  summary: Defines the vessel, gas, amendments, inoculation, incubation and repeated
    transfers. The pure-PfR7 maintenance pH is separate from the triculture.
  support: supports
  accessed_at: '2026-10-22T04:52:56.376997Z'
  snapshot_sha256: d8c23d4d53ebac460e7576d25c6adc4cd34de7dfe3dc0cda47034902e6c953ce
  quote: without shaking
- evidence_id: growth
  kind: primary_source
  reference: PMID:24463969; DOI:10.1128/AEM.03477-13
  locator: Results → Growth of Dhc195 in defined consortia with and without exogenous
    cobalamin, four direct paragraphs (#sec3-1); Figures 1–2 and Table 1
  summary: Lactate-fed partners supply hydrogen, acetate and corrinoids. Comparisons
    distinguish cobalamin-amended controls from the DMB-amended cobalamin-free triculture.
    Both fermenters compete for supplied lactate.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377115Z'
  snapshot_sha256: d8c23d4d53ebac460e7576d25c6adc4cd34de7dfe3dc0cda47034902e6c953ce
- evidence_id: corrinoids
  kind: primary_source
  reference: PMID:24463969; DOI:10.1128/AEM.03477-13
  locator: Results → Corrinoid production and modification, sole paragraph (#sec3-2),
    Table 2 and Figure 3; Discussion paragraphs 2–4 (#sec4)
  summary: Corrinoid profiles support recipient remodeling but do not exclude PfR7
    cobalamin production when DMB is provided. DvH nondetection is bounded to the
    assay; DMB is external.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377207Z'
  snapshot_sha256: d8c23d4d53ebac460e7576d25c6adc4cd34de7dfe3dc0cda47034902e6c953ce
- evidence_id: microarray
  kind: primary_source
  reference: PMID:24463969; DOI:10.1128/AEM.03477-13
  locator: Materials and methods → Transcriptomic microarray and data analysis, two
    paragraphs (#sec2-4), and Microarray data accession number, sole paragraph (#sec2-6);
    Results → Transcriptomic comparison of Dhc195 grown in co- and tricultures, three
    paragraphs (#sec3-3); Figures 4–6
  summary: Strain-195 expression was measured by array in three pair/triculture conditions.
    Induction is distinct from selective gene necessity or direct transporter activity.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377298Z'
  snapshot_sha256: d8c23d4d53ebac460e7576d25c6adc4cd34de7dfe3dc0cda47034902e6c953ce
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:24463969; DOI:10.1128/AEM.03477-13
  locator: Discussion, paragraphs 4 and 6–7 (#sec4); Figures 3, 5 and 6
  summary: Metabolite and expression patterns support the qualified remodeling route;
    no exclusive partition of donor biosynthesis versus recipient remodeling is demonstrated.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377388Z'
  snapshot_sha256: d8c23d4d53ebac460e7576d25c6adc4cd34de7dfe3dc0cda47034902e6c953ce
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000200/ontology-authority.json
  locator: 13 distinct ontology pairs / 39 placements
  summary: All labels match; relevant definitions and strain ranks were checked.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377579Z'
  snapshot_sha256: 8aa10bedf3c97f4825beddd195867d488709809f9722e5710a71a5050a657290
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000200/child-schema-semantics.json
  locator: Literal role, interaction, evidence and cultivation definitions
  summary: Recipient role tags require utilization of another taxon’s metabolites;
    a donor function alone is insufficient.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377644Z'
  snapshot_sha256: 032fc2ecd9501d80de82c68688667ed9f9f162130c0e8155da8a3371707ac97e
- evidence_id: stocks
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000200/child-strain-authority.json
  locator: Exact strain and collection identity sections
  summary: R7 equals DSM 17108 / ATCC BAA-1133. The other two exact stock authorities
    are reused with hashes. Catalogue maintenance conditions are not study conditions.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377689Z'
  snapshot_sha256: 8c91af25156bb0ec2956ebb8f6521db42a9f323c76de8fd12600d3492c73ac4a
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000200/child-gtdb-crosswalk.json
  locator: Three exact strain-ID routes
  summary: Fractions 1.0 with reference counts 5/7/3 reproduce; local file mtime is
    not a verified upstream release or build date.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377736Z'
  snapshot_sha256: 5296f93ae0e0213e65db345acb7943506c66f121a7c91c0576470bf8c4ffca81
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-15/000200/ontology-semantic-notes.json
  locator: Final source-local auxiliary assessment
  summary: Preserves identities, chemistry and graph qualifiers; records the five
    agreed repair groups.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377771Z'
  snapshot_sha256: dd501b9406c7df7175f6efec1fe9b8124b98d63244c79cd8caca0728466decf9
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/dataset-verification.json
  locator: GSE45533 and three encoded assemblies
  summary: Exact study and reference-stock resources are assessed separately; expression-array
    samples are not community RNA sequencing.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377839Z'
  snapshot_sha256: 22d3d6fdf594e1a4f02e8972dd606913c8a715ad4847a984ad71b85d7da7b9f2
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/snippet-audit.json
  locator: All 28 canonical excerpt placements
  summary: Exact source/cache matches establish textual provenance; entailment is
    assessed independently.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377878Z'
  snapshot_sha256: a581622c0adeb013f05bb720fc808a26787d562cfc5404739b4f79f7daf24c0d
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-15/000200/provenance-audit.json
  locator: Exact focal history/prior decision and cohort contexts
  summary: The earlier graph repair remains valid. Shared non-graph follow-up is not
    silently closed.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377917Z'
  snapshot_sha256: cb9dc252fc83a8ac191fc4b1ec2b996ce9e9164b35e5168dc0a7737ad48578d8
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/inspect.json
  locator: 30 immutable inputs
  summary: One target, 21 authorities and eight focal contexts, after ignored-inclusive
    discovery excluding environment files and Git/runtime internals.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377955Z'
  snapshot_sha256: 56c603a587c7d830a7effbe4aace1f6100af390358c1293ca5d92c9981129710
- evidence_id: reuse
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/source-reuse-verification.json
  locator: Verified immutable source reuse from 000199
  summary: Same PMID source bytes and retrieval receipts are reused explicitly; the
    preceding pair’s scientific judgment is not imported.
  support: supports
  accessed_at: '2026-10-22T04:52:56.377987Z'
  snapshot_sha256: 4e2d2a1614614c605e6f173d72fcfb2b471dd3df7e7b76248fa960f7755dfffb
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/lead-source-assets.json
  locator: Main article, six images and declared supplementary routes
  summary: Complete main and all six figures are available. Declared PDF/XLS responses
    are HTML challenges or errors, not read supplementary payloads.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378017Z'
  snapshot_sha256: 1ac3f061929a770ed03b83553ba4cf1935030e341d601ff5adc7ad7ef0468740
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/lead-primary-read-scope.json
  locator: Actual current-target reading
  summary: Entire main, both tables, six captions, all six figure images and fresh
    MED record were re-read at the explicit scope.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378050Z'
  snapshot_sha256: ec892a9bd156a86a611ca58d830620a35dd0039692fbd399827a8616f4215a79
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/source-locator-verification.json
  locator: Direct heading/paragraph inventory and main table rows
  summary: The sole two-word quote was checked in the culture Methods paragraph; no
    inferred section numbering.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378147Z'
  snapshot_sha256: 2190b9f9502cabbfc5f900c43bc90864f70602375cd9ff58b3cbb738b0a3da5f
- evidence_id: source-audit
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/source-audit.json
  locator: Reconciled source judgment
  summary: Two major and three minor findings; current claims are adjudicated despite
    explicit supplementary-access limits.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378233Z'
  snapshot_sha256: 894d937e14ef1148d8b7982ec84acbc425eee86fcb96c96cb81645476be37541
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/root-independent-source-audit.json
  locator: Independent root science and exact read scope
  summary: Root agrees with the five findings and preserves distinct current/reused
    figure and catalogue reading bounds.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378288Z'
  snapshot_sha256: c183415170278bc63d436313fe2106f99642a6e9c42f8a57e2ea0aab65157a66
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/support-final-audit.json
  locator: Final support reconciliation
  summary: Literal completeness 100; base quality 135 minus 26 gives raw 109, capped
    100.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378371Z'
  snapshot_sha256: 3055a23a187d6d465e13a3915ab47e932c4cf34ae6ca00d0117966cc5bccd3f8
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/support-frozen-manifest.json
  locator: Frozen supporting dependencies
  summary: Source, resource, provenance and metric reconciliation is complete.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378409Z'
  snapshot_sha256: b97727717a0dc0d2d21bbc01f63609f005b878af24e0c66eee2e4124bc5b2449
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/auxiliary-frozen-manifest.json
  locator: Frozen native/authority dependencies
  summary: Eight required native checks pass; their success does not establish scientific
    entailment.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378446Z'
  snapshot_sha256: 79dd2fab4caea173d27ef473d5fe5a920577c86e9c469d4d230f3e12f580b380
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/final-validator-summary.json
  locator: Actual eight command receipts
  summary: Focused passes and unchanged official inputs are documented.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378491Z'
  snapshot_sha256: 7f206ec24071d53a534ea13cc7008baf2f4171c3bd01a1c57cd16b3de8f41556
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/child-corpus-context.json
  locator: Fresh batch 15 corpus baseline
  summary: Two nonrequired corpus checks returned exit 1 with 44 warnings across 16
    of 477 records and zero errors.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378529Z'
  snapshot_sha256: 3addd734986439a32d6e8e83204c0b8e7c75bc2a6a35846d510cb0a0c1bf51ee
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/adapter-check.json
  locator: Owned-runtime optional adapter
  summary: Unavailable in this runtime; no external-checkout execution or global absence
    claim.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378559Z'
  snapshot_sha256: 5e08323e4b0465c72c10c7e023c2fb0bfdcd5dc5f41fe981ff1a7ef602c18d42
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/validate.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378862Z'
  snapshot_sha256: 8bc968f40cf8804b3be974d5970f500a545a48be5835dcea2608ed645c5ac90e
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/validate-strict.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378918Z'
  snapshot_sha256: 5e6c763caacf7f30b57548f868a70c50d100cdb38c6bfcebf32340b7c4d11f51
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/validate-terms.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T04:52:56.378970Z'
  snapshot_sha256: 9ed537e4a935f7f490739b0388bfadc1a120ffab072b9f35a8ca8a5e518aecf3
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/validate-references-explained.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T04:52:56.379022Z'
  snapshot_sha256: 9f0d4337752c233d96c1ff110690429abbd20c9eccc732ce6218ce168cf6d986
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/validate-gtdb.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T04:52:56.379071Z'
  snapshot_sha256: 42734f64053d6c76a12e1b7142990f64086b4d253f4bb74e20b5939620ca0d59
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/validate-gtdb-domain.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T04:52:56.379122Z'
  snapshot_sha256: af0bc1ab7b55ef3b64a812335a4e9d54de6c8e6d037dad672bd6f7608d981c39
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/validate-history.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T04:52:56.379170Z'
  snapshot_sha256: 7a30007242e316fcb1e3c94e3831d999e3645f6b73b82d1baae0e8493da8cbf6
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/000200/normalize-cache-names-check.json
  locator: Actual command/stdout/stderr
  summary: Actual native exit 0; scientific support is assessed separately.
  support: supports
  accessed_at: '2026-10-22T04:52:56.379229Z'
  snapshot_sha256: c3122a1075b9ccc011e1be38ab823ca3bad096ba0d1e875557d884c9971e9c2f
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/audit-network.json
  locator: Fresh batch 15 corpus baseline
  summary: Actual exit 1; 44 warnings across 16/477 records, zero errors.
  support: supports
  accessed_at: '2026-10-22T04:52:56.379306Z'
  snapshot_sha256: b92af84b02acf105f8dc7c3625cc2a7e52a436b24a8243fe7e1d53012c9be1d9
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-15/check-network-quality.json
  locator: Fresh batch 15 corpus baseline
  summary: Actual exit 1; 44 warnings across 16/477 records, zero errors.
  support: supports
  accessed_at: '2026-10-22T04:52:56.379364Z'
  snapshot_sha256: 10b4cbb4180b20137e22c994ff8cd71d5ca52ab6ac3ef21fef5580eb4c9200fc
assessments:
- assessment_id: identity
  area: identity
  topic: Defined three-strain scope
  outcome: supported
  summary: Retain the exact laboratory triculture and existing source synonyms.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - record
  - stocks
  - growth
  - ontology
  - resources
  dimensions:
  - name: taxon_scope
    value: Dhc195, DvH Hildenborough and PfR7
    definition: Three experimental strains, with pair controls retained as distinct
      assay arms.
    evidence_ids:
    - stocks
    - growth
  - name: experimental_setting
    value: Synthetic anaerobic laboratory bioremediation model
    definition: ENGINEERED state and SYNTHETIC origin; catalogue isolation locality
      is not the experimental habitat.
    evidence_ids:
    - ontology
    - cultivation
  details: 'The NCBI IDs are strain-level: 243164, 882 and 1122947. R7/DSM 17108/ATCC
    BAA-1133 identity, type status and kaolin locality are supported. PfR7 catalogue
    isolation years differ, but no year is encoded. Figure 2 supports qualitative
    Dhc195 prominence; no fixed percentage threshold or exact cross-table population
    conversion is imposed.'
- assessment_id: roles
  area: grounding
  topic: Directed function of both donors
  outcome: concern
  summary: Two optional role labels on each fermenter exceed the demonstrated uptake
    direction.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - schema
  - growth
  - semantics
  details: DvH and PfR7 compete for supplied lactate. DvH also ferments its own formate;
    Dhc195 hydrogen removal supports energetics. Neither observation establishes fermentation
    of primary-degrader products or uptake of another member’s metabolites by these
    donors. Retain Dhc195 PRIMARY_DEGRADER and the supported syntrophic relationship;
    do not invent replacement roles.
- assessment_id: node-0
  area: graph
  topic: Hydrogen Provision By Desulfovibrio
  outcome: supported
  summary: Retain hydrogen provision and reciprocal hydrogen-removal energetics.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - growth
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[0]; scope PAIRWISE; interaction_type
    SYNTROPHY. Actual taxa: {"source": {"preferred_term": "Desulfovibrio vulgaris
    Hildenborough", "term": {"id": "NCBITaxon:882", "label": "Nitratidesulfovibrio
    vulgaris str. Hildenborough"}}, "target": {"preferred_term": "Dehalococcoides
    mccartyi strain 195", "term": {"id": "NCBITaxon:243164", "label": "Dehalococcoides
    mccartyi 195"}}, "participants": []}. Canonical excerpt bindings: [{"selector":
    "ecological_interactions[0].evidence[0].snippet", "sha256": "e626d8bedde7b1e2919564bd3ef15aabe80156d5ed6a3daeb8d07b56d2cc62c2",
    "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"},
    {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "27e5965896f3e918d5a4c954c3a5cb823f4051988e62b3ba03d496713c83e5ff",
    "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 a581622c0adeb013f05bb720fc808a26787d562cfc5404739b4f79f7daf24c0d.
    PMID24463969 source locators: Results #sec3-1 paragraphs 1–4, Table 1 and Figures
    1–2. Retain SUPPORT and IN_VITRO. 882 → 243164. Cobalamin-free sustainability
    additionally requires PfR7 and external DMB; hydrogen alone is insufficient.'
- assessment_id: node-1
  area: graph
  topic: Corrinoid Provision By Pelosinus
  outcome: supported
  summary: Retain PfR7 corrinoid provision with the external-DMB qualifier.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - corrinoids
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[1]; scope PAIRWISE; interaction_type
    CROSS_FEEDING. Actual taxa: {"source": {"preferred_term": "Pelosinus fermentans
    R7", "term": {"id": "NCBITaxon:1122947", "label": "Pelosinus fermentans DSM 17108"}},
    "target": {"preferred_term": "Dehalococcoides mccartyi strain 195", "term": {"id":
    "NCBITaxon:243164", "label": "Dehalococcoides mccartyi 195"}}, "participants":
    []}. Canonical excerpt bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "8380a899d81f43350ace337478368e32442ec7a01d34e49115dce4ad62eed03e",
    "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"},
    {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "48eb91b34421fefd729a0d39942ae90ef54692cc1a7795bfa51c187065b7f788",
    "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 a581622c0adeb013f05bb720fc808a26787d562cfc5404739b4f79f7daf24c0d.
    PMID24463969 source locators: Results #sec3-2 sole paragraph, Table 2/Figure 3;
    Discussion paragraphs 2–4. Retain SUPPORT and IN_VITRO. 1122947 → 243164. Donor
    guided cobalamin biosynthesis remains possible; cobalamin is not every transferred
    corrinoid.'
- assessment_id: node-2
  area: graph
  topic: Dhc195 Corrinoid Salvaging And Remodeling
  outcome: supported
  summary: Retain recipient-intrinsic salvaging/remodeling as a qualified process.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - corrinoids
  - microarray
  - mechanism
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[2]; scope PAIRWISE; interaction_type
    absent. Actual taxa: {"source": {"preferred_term": "Dehalococcoides mccartyi strain
    195", "term": {"id": "NCBITaxon:243164", "label": "Dehalococcoides mccartyi 195"}},
    "target": null, "participants": []}. Canonical excerpt bindings: [{"selector":
    "ecological_interactions[2].evidence[0].snippet", "sha256": "0a409ec15aa1978cd357354003a3cc16d4266d3c34624efef889467c2778be37",
    "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"},
    {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "971f9216ff8282d5b59b3fdc1949e37dc3b0c1046fd7c4f648c9618253f3c4f0",
    "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 a581622c0adeb013f05bb720fc808a26787d562cfc5404739b4f79f7daf24c0d.
    PMID24463969 source locators: Results #sec3-2 and #sec3-3 paragraphs 2–3; Figures
    3, 5–6; Discussion paragraphs 4 and 6–7. Retain SUPPORT and IN_VITRO. Source 243164,
    target absent. The source-only PAIRWISE scope is valid. Measured induction is
    not a selective gene-necessity or transporter-activity experiment.'
- assessment_id: node-3
  area: graph
  topic: Hydrogen- and Corrinoid-Supported TCE Dechlorination
  outcome: supported
  summary: Retain the conditional community dechlorination and growth outcome.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - growth
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[3]; scope COMMUNITY_LEVEL; interaction_type
    absent. Actual taxa: {"source": null, "target": null, "participants": [{"preferred_term":
    "Dehalococcoides mccartyi strain 195", "term": {"id": "NCBITaxon:243164", "label":
    "Dehalococcoides mccartyi 195"}}, {"preferred_term": "Desulfovibrio vulgaris Hildenborough",
    "term": {"id": "NCBITaxon:882", "label": "Nitratidesulfovibrio vulgaris str. Hildenborough"}},
    {"preferred_term": "Pelosinus fermentans R7", "term": {"id": "NCBITaxon:1122947",
    "label": "Pelosinus fermentans DSM 17108"}}]}. Canonical excerpt bindings: [{"selector":
    "ecological_interactions[3].evidence[0].snippet", "sha256": "75c687ed36de54591adf6524c7927af8d26332848845422c45c556670f242ba2",
    "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"},
    {"selector": "ecological_interactions[3].evidence[1].snippet", "sha256": "02821924274a3570e4f91fc9896be06d5e265bf3e9b978dc932271489dd1a2b3",
    "reference": "PMID:24463969", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 a581622c0adeb013f05bb720fc808a26787d562cfc5404739b4f79f7daf24c0d.
    PMID24463969 source locators: Results #sec3-1 paragraphs 1–3 and Figure 2; Abstract
    sustainable-growth sentence. Retain SUPPORT and IN_VITRO. Participants 243164,
    882 and 1122947. Cobalamin-free performance depends on DMB; cobalamin-amended
    controls and hydrogen-supplemented alternative pairs are not denied.'
- assessment_id: edge-0-0
  area: graph
  topic: Hydrogen Provision By Desulfovibrio → Hydrogen- and Corrinoid-Supported TCE
    Dechlorination
  outcome: supported
  summary: Retain the hydrogen input to the conditional community endpoint.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - growth
  - snippets
  details: 'Exact selector ecological_interactions[0].downstream[0]; source node 0
    → target node 3. 882 → recipient 243164 within the three-member community. Exact
    edge description: DvH-supplied hydrogen supports the electron-donor requirement
    of Dhc195 in the lactate-fed triculture, together with partner corrinoids and
    externally supplied DMB. Hydrogen provision alone does not make the cobalamin-free
    two-member coculture sustainable. Description SHA256 1bc84c883128af76af6593d060f7fc04fdf49efbdec9e66c454e256a5ae11e74.
    PMID24463969 locators: Results #sec3-1 paragraphs 1–4, Table 1/Figures 1–2. External
    DMB, donor guided biosynthesis and lack of selective route partition remain explicit.'
- assessment_id: edge-1-0
  area: graph
  topic: Corrinoid Provision By Pelosinus → Dhc195 Corrinoid Salvaging And Remodeling
  outcome: supported
  summary: Retain precursor provision to recipient remodeling without making it exclusive.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - corrinoids
  - mechanism
  - snippets
  details: 'Exact selector ecological_interactions[1].downstream[0]; source node 1
    → target node 2. 1122947 → 243164; DMB is externally supplied. Exact edge description:
    PfR7 supplies corrinoid substrates that Dhc195 can salvage and remodel in the
    presence of externally supplied DMB. This does not exclude donor guided cobalamin
    biosynthesis or establish that all functional cofactor passes through recipient
    remodeling. Description SHA256 c7e20401c8f8ca2b55186473a8cb9c572d19c95ece87f491f35c28f1537faa2d.
    PMID24463969 locators: Results #sec3-2, Table 2/Figure 3; Discussion paragraph
    4. External DMB, donor guided biosynthesis and lack of selective route partition
    remain explicit.'
- assessment_id: edge-2-0
  area: graph
  topic: Dhc195 Corrinoid Salvaging And Remodeling → Hydrogen- and Corrinoid-Supported
    TCE Dechlorination
  outcome: supported
  summary: Retain the qualified compatible-cofactor contribution to community function.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - growth
  - corrinoids
  - mechanism
  - snippets
  details: 'Exact selector ecological_interactions[2].downstream[0]; source node 2
    → target node 3. Recipient 243164 process → community participants 243164/882/1122947.
    Exact edge description: Recipient salvaging and remodeling contributes compatible
    cofactor for sustainable TCE dechlorination in the DMB-amended triculture when
    DvH supplies hydrogen. The source supports this route but does not selectively
    separate its contribution from cobalamin formed by the donor in the presence of
    DMB. Description SHA256 7e1c37c9f2b1f1ab5ef0d19973e56471e99b82e40e659b6e47d40b33136d02d1.
    PMID24463969 locators: Results #sec3-1 paragraphs 1–3 and #sec3-2; Discussion
    paragraphs 4 and 6–7. External DMB, donor guided biosynthesis and lack of selective
    route partition remain explicit.'
- assessment_id: cultivation
  area: scope
  topic: Recoverable protocol and assay boundaries
  outcome: concern
  summary: The partial medium is accurate but omits source-specific culture details.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - cultivation
  - growth
  dimensions:
  - name: medium
    value: Defined lactate/TCE medium, cobalamin-free with 36 nM DMB for the focal
      arm
    definition: 74 nM cobalamin controls are separate; external lower ligand is required.
    evidence_ids:
    - cultivation
    - growth
  - name: environmental_context
    value: Anaerobic sealed laboratory culture
    definition: Actual cultivation is distinct from strain isolation locality and
      modeled subsurface application.
    evidence_ids:
    - cultivation
    - ontology
  details: The preparation note declines to assert the complete recipe; it does not
    claim the source lacks conditions. The current paper supplies the vessel, gas,
    doses, inoculation, incubation and passages. Basal salts/vitamins refer to earlier
    study 24 and are not reconstructed here. Keep pure-PfR7 pH 7.5 and catalogue recipes
    separate.
- assessment_id: chemistry
  area: grounding
  topic: Chemical and process scope
  outcome: supported
  summary: All thirteen ID-label pairs are correct at the stated scope.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - ontology
  - semantics
  - corrinoids
  details: Preserve lactate, TCE, hydrogen, cobalamin and DMB identities. Cobalamin
    is not a generic label for all corrinoids. GO cobalamin transport denotes movement,
    while current prose correctly separates measured transcript induction from direct
    transporter activity. No additional transporter or gene-necessity claim is inferred.
- assessment_id: dataset
  area: evidence
  topic: Array classification and experimental comparisons
  outcome: concern
  summary: GSE45533 is a strain-targeted expression array, not community RNA sequencing.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - microarray
  - resources
  - schema
  details: Its nine samples compare Dhc195 in a cobalamin-amended Dhc195/DvH pair,
    cobalamin-amended triculture and DMB-amended cobalamin-free triculture. A Dhc195/PfR7-only
    array arm is not present. Preserve the correct accession and reference assemblies.
- assessment_id: evidence-mode
  area: evidence
  topic: Measured transcript evidence
  outcome: concern
  summary: The resource evidence is experimental; COMPUTATIONAL is the wrong tier.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - microarray
  - snippets
  - schema
  details: Change only the incorrectly tagged external-resource evidence and its claim-local
    explanation. Existing node-2 experimental evidence and mechanistic caveats are
    already appropriate.
- assessment_id: gtdb
  area: provenance
  topic: Verified mappings and unsupported build wording
  outcome: concern
  summary: All three mapping cores reproduce; release/build provenance needs repair.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - gtdb
  - semantics
  details: Keep exact strain routes, domain, lineage, fraction 1.0 and denominators
    5/7/3. The local timestamp is mtime, not an upstream GTDB build date or proof
    of latest release.
- assessment_id: ownership
  area: ownership
  topic: Prior graph repair and curation owner
  outcome: supported
  summary: The maintained focal YAML owns the five future repairs.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - inspection
  - provenance
  details: The sole history and exact batch 30 focal review remain intact. The dated
    discussion accurately records its earlier reading scope; this review adds current
    evidence without rewriting that event. Shared open issue scope is not closed by
    this target review.
- assessment_id: source-scope
  area: scope
  topic: Completion at explicit source scope
  outcome: supported
  summary: The complete main article resolves the current claims; supplementary limits
    remain explicit.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - reuse
  - assets
  - lead-read
  - locators
  - source-audit
  - root-source
  details: Current lead reading covers the whole main, two tables, six figures and
    fresh MED record. The declared supplementary PDF/XLS returned challenge or error
    payloads and were not read. No negative biological inference or required correction
    rests on their absence. No raw sequence/expression reanalysis or figure digitization
    was performed.
- assessment_id: native
  area: schema
  topic: Native and contextual checks
  outcome: supported
  summary: All eight required native checks passed.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - final-native
  - auxiliary
  - corpus-context
  - adapter
  details: The two corpus failures and optional adapter are nonrequired. Actual candidate
    validation and parent saving are not asserted in advance.
- assessment_id: metrics
  area: completeness
  topic: Literal native metrics
  outcome: supported
  summary: Completeness 100; raw validation quality 109, capped 100.
  target_ids:
  - CommunityMech:000200
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required/roles+5 environment+10 three factors+10 four nodes+5 external
      resources+10 medium+5 datasets+5 node metabolites=100. Populated slots do not
      prove scientific support.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100-2 major*10-3 minor*2+20*min((8 evidence/4 nodes)/2,1)+15 COMPLETE
      = 109 raw, capped 100. Four nodes (two typed), three arrows. Structural COMPLETE
      does not erase findings.
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
- finding_id: donor-roles
  issue_key: cm-000200-donor-roles
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material role or assay classification exceeds evidence.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Align both fermenter role tags with metabolic direction
  description: DvH and PfR7 use supplied lactate. Their donor functions do not establish
    utilization of other members’ metabolites or fermentation of products from primary
    degraders. DvH self-produced formate fermentation and hydrogen removal do not
    supply the missing directed evidence.
  target_ids:
  - CommunityMech:000200
  field_paths:
  - taxonomy[1].functional_role
  - taxonomy[2].functional_role
  evidence_ids:
  - growth
  - schema
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  ownership_note: Future authorized curation belongs to the maintained focal YAML;
    no shared issue or historical finding is closed.
- finding_id: dataset-type
  issue_key: cm-000200-dataset-type
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material role or assay classification exceeds evidence.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Correct array category, repository and comparison scope
  description: GSE45533 measures strain-195 expression by array. METATRANSCRIPTOMICS
    denotes community RNA sequencing, and the description obscures the three actual
    pair/triculture conditions.
  target_ids:
  - CommunityMech:000200
  field_paths:
  - associated_datasets[0].dataset_type
  - associated_datasets[0].repository
  - associated_datasets[0].description
  - external_resources[1].repository
  evidence_ids:
  - microarray
  - resources
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  ownership_note: Future authorized curation belongs to the maintained focal YAML;
    no shared issue or historical finding is closed.
- finding_id: cultivation
  issue_key: cm-000200-cultivation
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable protocol, evidence placement or provenance;
    qualified graph remains supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Encode available triculture protocol details
  description: The partial medium omits recoverable vessel, gas, dose, inoculation,
    incubation and passage details. These can be added without inventing a full basal
    recipe or merging controls.
  target_ids:
  - CommunityMech:000200
  field_paths:
  - growth_media[0]
  - cultivation_setup
  evidence_ids:
  - cultivation
  - growth
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  ownership_note: Future authorized curation belongs to the maintained focal YAML;
    no shared issue or historical finding is closed.
- finding_id: omics-evidence
  issue_key: cm-000200-omics-evidence
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable protocol, evidence placement or provenance;
    qualified graph remains supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Use experimental evidence for measured array expression
  description: The external-resource excerpt is exact but COMPUTATIONAL mislabels
    a laboratory measurement. Keep molecular inference distinct from the experimental
    evidence tier.
  target_ids:
  - CommunityMech:000200
  field_paths:
  - external_resources[1].evidence[0]
  evidence_ids:
  - microarray
  - snippets
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  ownership_note: Future authorized curation belongs to the maintained focal YAML;
    no shared issue or historical finding is closed.
- finding_id: gtdb-provenance
  issue_key: cm-000200-gtdb-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable protocol, evidence placement or provenance;
    qualified graph remains supported.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Correct unsupported GTDB release/build provenance
  description: Three valid mapping cores carry latest-release/build wording derived
    from local mtime rather than verified upstream metadata.
  target_ids:
  - CommunityMech:000200
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  - taxonomy[2].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  ownership_note: Future authorized curation belongs to the maintained focal YAML;
    no shared issue or historical finding is closed.
actions:
- action_id: repair-roles
  description: Qualify or remove the unsupported optional donor-role labels.
  finding_ids:
  - donor-roles
  target_ids:
  - CommunityMech:000200
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  acceptance_checks:
  - For both donors, omit SECONDARY_FERMENTER and CROSS_FEEDER unless source-local
    evidence supports the literal precursor/recipient definitions. Do not imply the
    organisms can never perform such metabolism or invent replacement enums.
  - Retain the supported hydrogen syntrophy, PfR7-to-Dhc195 corrinoid CROSS_FEEDING
    interaction, Dhc195 PRIMARY_DEGRADER, and all current graph caveats. Role-enum
    uptake semantics do not invalidate a donor-to-recipient exchange node.
- action_id: repair-dataset
  description: Represent the verified array and its three comparisons precisely.
  finding_ids:
  - dataset-type
  target_ids:
  - CommunityMech:000200
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  acceptance_checks:
  - Use TRANSCRIPTOMICS and NCBI_GEO for GSE45533, including the external-resource
    repository. Preserve accession/URL and identify the strain-195 GPL10838 array
    with nine samples.
  - Name the +B12 Dhc195/DvH pair, +B12 triculture and +DMB/no-B12 triculture. Do
    not assert a PfR7-only partner array arm, community RNA sequencing, or raw-data
    reanalysis. Keep reference assemblies separate from this expression dataset.
- action_id: enrich-cultivation
  description: Add source-specific culture and transfer details.
  finding_ids:
  - cultivation
  target_ids:
  - CommunityMech:000200
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  acceptance_checks:
  - 'Cite Methods Bacterial cultures and growth conditions, sole paragraph: 160 mL
    sealed serum bottles,100 mL basal medium/60 mL N2:CO2 90:10;approximately0.7 mmol
    lactate and77 µmol TCE;1% pregrown Dhc195/DvH plus2% pregrown PfR7;34°C,dark,no
    shaking. Use structured values with normal units and source evidence.'
  - Separate the focal no-B12/36 nM DMB arm from74 nM B12 controls. Record measurements
    after six 3% vol/vol subcultures and biological triplicates. Do not convert this
    into an unreported fixed transfer interval or daily protocol.
  - Do not assign pure-PfR7 maintenance pH 7.5 to the triculture or import vendor
    media. The complete basal recipe is cited to prior study 24; leave unverified
    components unasserted.
- action_id: repair-evidence
  description: Correct the measured-expression evidence tier.
  finding_ids:
  - omics-evidence
  target_ids:
  - CommunityMech:000200
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  acceptance_checks:
  - Use IN_VITRO for external_resources[1].evidence[0], with a claim-local experimental
    explanation and exact Methods/Results excerpt if expanded. Existing node-2 IN_VITRO
    evidence remains intact.
  - Keep transcript induction separate from gene necessity, direct transporter activity
    and exclusive cofactor-route partition. Revalidate exact excerpts.
- action_id: repair-gtdb
  description: Retain reproduced cores with truthful snapshot provenance.
  finding_ids:
  - gtdb-provenance
  target_ids:
  - CommunityMech:000200
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve exact strain-ID routes to Dehalococcoides mccartyi, Nitratidesulfovibrio
    vulgaris and Pelosinus fermentans;fraction 1.0, reference counts 5/7/3 and current
    lineages. These counts are not culture abundance.
  - Use mapping SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd.
    Identify the 2026-07-25 filesystem date only as mtime; leave unverified upstream
    release/build unknown.
- action_id: validate-curation
  description: Validate any separately authorized maintained-record repair.
  finding_ids:
  - donor-roles
  - dataset-type
  - cultivation
  - omics-evidence
  - gtdb-provenance
  target_ids:
  - CommunityMech:000200
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dehalococcoides_Desulfovibrio_Pelosinus_Corrinoid_Triculture.yaml
    role: canonical_record
  acceptance_checks:
  - Recheck source-specific strains, treatments, doses and graph qualifiers, then
    focused schema/strict/terms/explained-reference/GTDB/domain/history checks. Run
    just gen-html and just check-docs-current when canonical curation is authorized.
  - Preserve source/cache/history/prior bytes. This review does not authorize canonical,
    issue, Git or status mutations.
limitations:
- Declared supplementary PDF/XLS payloads were not recovered on bounded ordinary PMC/ASM/EPMC
  routes; challenge/error responses are preserved. No supplementary content or absence-based
  biological conclusion is claimed. The complete main resolves the current record
  claims.
- The complete basal recipe is referenced to earlier study 24 and was not reconstructed.
  Pure-PfR7 pH and catalogue maintenance conditions are not triculture conditions.
- No raw expression/genome reanalysis, figure digitization or exact cross-table per-cell
  population reconstruction. Qualitative abundance is supported independently of unresolved
  source reporting differences.
notes:
- Four node assessments bind eight exact canonical snippet hashes and actual taxa;
  three edge assessments preserve exact direction and description hashes.
- The only quoted primary wording is two words from the sole culture Methods paragraph.
  All 30 official inputs remain unchanged.
- Actual candidate validation and parent-owned saving/post-save gates follow this
  review.
tags:
- record-review
- corrinoids
- dechlorination
- batch-15
```
