# DCPP DBS4-DCP-4-DCP-11d record review

- Review: 20261022T030952Z-dcpp-three-strain-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T03:01:26.898757Z
- Finished UTC: 2026-10-22T03:09:52.238055Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Whole primary text and four main figures support the three-strain design and measured degradation phenotypes. One major finding narrows experimentally verified exchange claims; three minor findings concern cultivation stages, GTDB grounding/provenance and source resources. Critical supplementary assay/model payloads remain unavailable, so scientific completion is partial. Eight focused checks pass; literal completeness is 85 and raw quality 119, capped 100.

## Scope And Provenance

Whole target and fresh public main article with four main figures; bounded direct genome metadata and current authority checks. Main-page SI captions were read, but the three declared supplementary/model files were inaccessible.

Selection: Only released CommunityMech:000410 in the owned batch14 checkout.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e117e3d37c65bfad2e04af53ab34e1325d8d7f98.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000410 | kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml | maintained | DCPP DBS4-DCP-4-DCP-11d Degradation SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000410 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000410 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000410 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000410 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000410 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000410 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000410 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000410 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000410 | Actual corpus exit 1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000410 | Actual corpus exit 1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000410 | Unavailable in owned runtime. |

## Scientific And Domain Assessments

### Three-strain synthetic community

identity: supported. Targets: CommunityMech:000410.

The exact DBS4/DCP-4/DCP-11d design, synthetic origin and engineered state are supported.

Retain separate Sphingopyxis strains despite their shared genus CURIE. Bosea DCP-2 and Pigmentiphaga DCP-6d are larger-design comparators, not additional focal members. Laboratory environment and modeled contaminated soil are separate contexts.

### Model-selected DCPP degradation

graph: concern. Targets: CommunityMech:000410.

Retain model selection and measured performance; distinguish the CROSS_FEEDING interpretation from removal endpoints.

Exact selector ecological_interactions[0]; name Model-selected DCPP degradation; scope COMMUNITY_LEVEL; interaction_type CROSS_FEEDING. Encoded taxa: {"source": null, "target": null, "participants": []}. Canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "c3e35789dd9301572c447a8a25f537c89141496c4d33ecaf38d7ef71d2a18442", "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "8f5766abd3bfc914c2c7dd7a9aa934597cbf1e82bd756c7b98a71c39becf2874", "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 f340db57e8ec4fe7c3d47ae79653d92af48d9d37932649c7613ed4a775d108a7. PMID:42613016 locator: Methods 2.5–2.7; Results 3.3 paragraph 1 and 3.4 paragraphs 1–2; Figures 3–4. Keep SUPPORT/COMPUTATIONAL for model selection and SUPPORT/IN_VITRO for removal performance. An explicit computational or PARTIAL mechanistic qualifier is needed if this contextual node remains typed CROSS_FEEDING.

### DBS4 to DCP-11d 2,4-DCP detoxification

graph: concern. Targets: CommunityMech:000410.

Retain the modeled DBS4-to-DCP-11d 2,4-DCP direction, while qualifying the asserted experimental rescue.

Exact selector ecological_interactions[1]; name DBS4 to DCP-11d 2,4-DCP detoxification; scope PAIRWISE; interaction_type CROSS_FEEDING. Encoded taxa: {"source": {"preferred_term": "Sphingopyxis sp. DBS4", "term": {"id": "NCBITaxon:165697", "label": "Sphingopyxis"}}, "target": {"preferred_term": "Achromobacter sp. DCP-11d", "term": {"id": "NCBITaxon:222", "label": "Achromobacter"}}, "participants": []}. Canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "a0fbd4d5e34581e318e06c8e579c08308c6ddbfbd8d5b902ffc6b9f248609320", "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "7170a0f8df205dc8afcdd143936144afbe7df5f4cca4403e1b0a244eb4ad0588", "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 f340db57e8ec4fe7c3d47ae79653d92af48d9d37932649c7613ed4a775d108a7. PMID:42613016 locator: Results 3.3 paragraph 2 and 3.1 paragraph 3; Results 3.4 paragraph 5; Discussion paragraphs 5 and 9; Figure 3C; exposed Figure S4 caption. Keep SUPPORT/COMPUTATIONAL for predicted direction. The IN_VITRO excerpt is an author interpretation in Discussion, supported by substrate capacity and inhibition observations but not an independently isolated rescue arm in the available description. Qualify mechanistic support as PARTIAL; do not claim the unread SI rules out additional assays.

### Predicted exchanged metabolite validation

graph: concern. Targets: CommunityMech:000410.

Retain liquid LC-MS detection as partial mechanistic support, not measured donor-recipient exchange.

Exact selector ecological_interactions[2]; name Predicted exchanged metabolite validation; scope COMMUNITY_LEVEL; interaction_type CROSS_FEEDING. Encoded taxa: {"source": null, "target": null, "participants": [{"preferred_term": "Sphingopyxis sp. DBS4", "term": {"id": "NCBITaxon:165697", "label": "Sphingopyxis"}}, {"preferred_term": "Sphingopyxis sp. DCP-4", "term": {"id": "NCBITaxon:165697", "label": "Sphingopyxis"}}, {"preferred_term": "Achromobacter sp. DCP-11d", "term": {"id": "NCBITaxon:222", "label": "Achromobacter"}}]}. Canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "cbc1ed190db4dd9a056e6cb48f6f697576adeee51d3cbadc48cff49340c6a8a6", "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}, {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "ae24390a52371dca674ada3facfd06b76e2f5d220840f8f6e6eccfbe13f1919e", "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 f340db57e8ec4fe7c3d47ae79653d92af48d9d37932649c7613ed4a775d108a7. PMID:42613016 locator: Methods 2.7 paragraph 3; Results 3.4 paragraph 4; Discussion paragraph 9; exposed Figure S3 caption. Keep IN_VITRO for bulk extracellular detection and the three-strain culture. Change only the mechanistic interpretation/tier as needed: presence does not resolve production, consumption, transfer or rates. Six of seven selected compounds is narrower than all model-predicted exchanges.

### No downstream arrows

graph: supported. Targets: CommunityMech:000410.

Three current nodes and zero arrows are structurally valid; no causal edge is required.

No duplicate-CURIE deletion or forced reciprocal benefit. Preserve valid modeled directions while narrowing their experimental interpretation.

### Separate assay and analytical stages

completeness: concern. Targets: CommunityMech:000410.

The existing LC-MS medium is supported; omitted liquid setup and stage-specific inocula can be recovered.

Keep the 15 h LC-MS endpoint separate from liquid time courses and soil degradation. Do not copy soil extraction settings into cultivation or infer a vessel capacity.

### Genus mappings and exact DBS4 boundary

grounding: concern. Targets: CommunityMech:000410.

Current NCBI identities are valid; both Sphingopyxis blocks can be grounded at genus rank.

Achromobacter core mapping reproduces but latest/build provenance does not. Optional DBS4 accession refinement must not propagate to DCP-4. Source-modeled roles need source-specific qualifiers, not blanket deletion.

### Prior genomes and declared models

provenance: concern. Targets: CommunityMech:000410.

The publication links are correct, but source-linked genome/model traceability is incomplete.

Add verified DBS4 components with member-specific scope. Preserve unresolved SUB submissions and the unread status of Data S1/S2; do not invent accessions for other members.

### Main-text review with critical supplementary limits

scope: unknown. Targets: CommunityMech:000410.

Whole primary reading supports bounded findings; model files and detailed supporting assays remain unavailable.

Fresh main retrieval resolves the old main-access gap, not supplementary validation. Existing mechanistic discussion remains a useful knowledge gap. Source-internal nitrogen, comparator and table inconsistencies are retained as limitations, not extra record findings.

### Maintained record and append-only context

ownership: supported. Targets: CommunityMech:000410.

Repairs belong to the focal YAML; historical reviews and cache provenance remain unchanged.

Current issue states are context only. No issue closure, curation-history event or scientific-status promotion is performed.

### Focused validity and independent source support

schema: supported. Targets: CommunityMech:000410.

Eight focused checks pass; corpus failures and optional-adapter limits remain explicit.

### Two literal native scores

completeness: supported. Targets: CommunityMech:000410.

Completeness 85; raw quality 119, capped 100.

## Findings

### mechanism-scope: Separate model predictions, measured outcomes and exchange inference

major / open / confirmed; issue key: cm-000410-mechanism-scope.

The description extends exchange validation to soil, while LC-MS is a liquid assay. Node 0 measures selection/performance; node 1 asserts helper rescue beyond the available isolated perturbation description; node 2 detects pooled compounds without donor-recipient resolution. Preserve the model and observed phenotypes with explicit claim-level support.

### culture-stages: Recover the liquid setup and distinguish assay stages

minor / open / confirmed; issue key: cm-000410-culture-stages.

The source reports 20 mL liquid assays, 180 rpm and stage-specific strain inocula. The existing salts/pH/temperature/15 h LC-MS block is sound but does not encode those distinctions.

### gtdb-grounding: Resolve genus blocks and correct mapping provenance

minor / open / confirmed; issue key: cm-000410-gtdb-grounding.

Both Sphingopyxis descriptors remain UNRESOLVED despite a supported genus mapping. Achromobacter uses an unsupported latest-release/build-date claim derived from file mtime.

### source-resources: Link verified genome components and declared model outputs

minor / open / confirmed; issue key: cm-000410-source-resources.

Publication links omit five verified DBS4 genome components and the declared model archives. Other strains have SUB submissions, not verified public sequence identifiers; unavailable archive contents must remain explicitly unreviewed.

## Recommended Actions And Acceptance Checks

### qualify-mechanism

Retain the model and measured phenotypes with the correct experimental scope.

- Describe soil results as degradation-performance validation. Limit LC-MS detection to liquid culture and keep the initial soil lag/day-7 convergence rather than universal equivalence.
- For node 0 retain computational selection and IN_VITRO removal evidence separately. If retaining CROSS_FEEDING, label its mechanistic interpretation as modeled or PARTIAL rather than experimentally resolved exchange.
- For node 1 retain the DBS4 to DCP-11d modeled 2,4-DCP direction, observed helper substrate capability and DBS4 inhibition. Attribute rescue to the authors’ interpretation and mark experimental mechanistic support PARTIAL until detailed perturbation evidence is inspected; do not claim no such experiment exists in unread SI.
- For node 2 retain six-of-seven selected metabolite detection with IN_VITRO evidence, while treating exchange direction and flux as inferred. Four nutrients were added together; do not convert this into four independent causal tests. Keep the existing unresolved-mechanism discussion and zero downstream arrows.

### recover-culture

Encode available liquid conditions while preserving stage boundaries.

- Retain the current per-litre mineral salts, MgSO4 heptahydrate, pH 7, 30 mg/L DCPP and 30°C. Keep the 15 h endpoint specifically attached to LC-MS under Methods 2.7 paragraph 3.
- Use Methods 2.7 paragraph 1 for 20 mL liquid assays, 180 rpm, uninoculated control and 3 h HPLC sampling. State that each strain was prepared at 1.5×10^6 CFU/mL; do not silently convert a prepared inoculum concentration into an unstated final concentration or infer vessel capacity.
- Use Methods 2.7 paragraph 2 for 5 mg/kg soil DCPP and final approximately 10^6 CFU/g per strain. Keep 5 g aliquots, 50 mL extraction tubes and 30°C/180 rpm/1 h extraction out of soil cultivation setpoints. BATCH may describe individual assay stages if justified, without merging experiments.
- Preserve exact source snippets containing the sole-carbon-and-nitrogen wording, but explain its conflict with NH4Cl-containing medium and nitrogen-free DCPP rather than reproducing that error as medium chemistry.

### repair-gtdb

Ground the existing genus descriptors with precise snapshot provenance.

- Add GROUNDED genus blocks for both Sphingopyxis descriptors using GTDB:g__Sphingopyxis, 79/79 reference genomes, majority fraction 1.0 and ncbi_rank_g. Keep DBS4 and DCP-4 separate source strains.
- Retain Achromobacter 325/328, majority fraction 0.991 and two total GTDB destinations. Record actual mapping SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd and rank route; identify filesystem mtime only as mtime, not release latest or build date.
- Optional DBS4-specific enrichment may cite NCBITaxon:2968500 and its verified archive identity/GTDB Sphingopyxis sp024628865. Do not transfer this to DCP-4 or invent a named species or strain accession.

### add-resources

Add source-scoped genome and model traceability.

- Link CP102384.1 as the DBS4 chromosome and CP102385.1–CP102388.1 as its four plasmids, with SAMN30005345 context. These are nucleotide components of a prior genome, not assembly identifiers for strain_designation.genome_accession or new SynCom sequencing.
- Link declared Data S1 five single-strain models and Data S2 fifteen community models as source resources; record that their payloads were unavailable in this review. Do not assert model contents, versions or executable reproducibility from captions alone.
- Keep SUB15680332, SUB15680937, SUB15681044 and SUB15681330 as unresolved submission leads. Preserve the Data Availability SUB1568104 versus Methods SUB15681044 conflict; do not substitute invented public accessions.

### validate-future-curation

Validate any separately authorized record repair.

- Recheck source snippets, exact strain/role scope and all three node selectors with the modeled-versus-observed distinction. Run focused schema, strict, terms, explained references, GTDB/domain and history checks.
- After authorized curation run just gen-html and just check-docs-current. Preserve existing histories and source/cache bytes and add curation provenance. This review performs no canonical repair, generated-page change, Git operation or issue mutation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml; Whole maintained YAML | supports | Defined DBS4/DCP-4/DCP-11d SynCom; three CROSS_FEEDING nodes, zero downstream arrows. Canonical YAML owns future repairs. |
| publication | PMID:42613016; DOI:10.1111/1462-2920.70404; Fresh MED identity and complete PMC article metadata | supports | PMID, DOI and PMC13485441 agree. Fresh public PMC HTML is complete despite failed XML/publisher routes and the MED non-OA flag. Supplementary payloads remain unavailable. |
| culture | PMID:42613016; DOI:10.1111/1462-2920.70404; Material and Methods / Chemicals, Medium, Bacterial Strains, and Culture Conditions (2.1), sole paragraph; In Vitro Experiments Testing Predictions by Modelling (2.7), three direct paragraphs | supports | The existing mineral salts, pH 7 and 30°C/15 h LC-MS stage are supported. Liquid degradation assays use 20 mL, 30 mg/L DCPP and 180 rpm. Soil degradation and solvent extraction are separate operations; the 30°C/180 rpm/1 h extraction is not a soil cultivation condition. |
| model | PMID:42613016; DOI:10.1111/1462-2920.70404; Material and Methods / Construction of Multi-Compartment Models for Bacterial Communities (2.5), sole paragraph; Metabolic Model-Based Simulations of Growth and DCPP Degradation (2.6), both paragraphs; Results / Simulation-Based SynCom Design and Metabolic Interaction Analysis (3.3), all three paragraphs; Figure 3 | supports | Fifteen DBS4-containing models rank candidate communities by predicted biomass. Equal initial ratios are shared with experiments. Predicted nutrient and 2,4-DCP flows remain computational; biomass optimization does not directly measure exchange. |
| performance | PMID:42613016; DOI:10.1111/1462-2920.70404; Results / Experimental Validation of Metabolic Model-Based Simulations (3.4), paragraphs 1–3; Figure 4; Material and Methods (2.7), paragraphs 1–2 | supports | Liquid removal and soil degradation support the selected design. In soil the three-member treatment initially lags and becomes comparable by day 7. These assays measure pesticide removal, not interstrain metabolite transfer. |
| metabolites | PMID:42613016; DOI:10.1111/1462-2920.70404; Material and Methods (2.7), paragraph 3; Results (3.4), paragraphs 4–5; Supporting information, exposed Figure S3 and Figure S4 captions | supports | LC-MS detected six of seven selected metabolites in the liquid consortium. Main-text addback experiments describe DBS4 with a four-nutrient mixture, 2,4-DCP or control. Bulk detection does not identify donor, consumer or transfer rate; mixture effects are not four independent metabolite effects. Only captions of S3/S4 were read, not their inaccessible payload. |
| mechanism-limits | PMID:42613016; DOI:10.1111/1462-2920.70404; Discussion (4), ninth direct paragraph; HTML section emi70404-sec-0015, p[9] | supports | The authors distinguish validation of model predictions from quantitative dissection of nutrient exchange and detoxification. Discussion paragraph 5 asserts helper rescue, while the available experimental description does not isolate that route. The inaccessible supplement prevents an exhaustive absence claim. |
| substrates | PMID:42613016; DOI:10.1111/1462-2920.70404; Results / Whole-Genome Sequencing and Analysis of DCPP Metabolic Pathway (3.1), paragraphs 1–3; Discussion (4), paragraph 5 | supports | DBS4 uses both DCPP enantiomers, DCP-4 uses R-DCPP, and DCP-11d can use 2,4-DCP. These substrate capabilities and model predictions support qualified degrader/cross-feeder roles without claiming measured recipient-specific exchange. |
| resource-source | PMID:42613016; DOI:10.1111/1462-2920.70404; Material and Methods / Genome Sequencing (2.3), sole paragraph; Results (3.2), paragraphs 1–2; Data Availability Statement; Supporting information declarations | supports | The paper cites DBS4 CP102384–CP102388, other-member SUB submissions and two model archives. Data S1/S2 and the supporting DOCX were identified but not read. Methods and Data Availability differ by one digit in the DCP-6d SUB identifier. |
| ontology | /private/tmp/cm-review-session/batch-14/000410/ontology-authority.json; Seven ID-label pairs, 15 placements and definitions | supports | All current labels match; dichlorprop and 2,4-dichlorophenol remain distinct. Shared genus IDs do not merge separate source strains. |
| schema | /private/tmp/cm-review-session/batch-14/000410/child-schema-semantics.json; Literal interaction, role, evidence, state and culture semantics | supports | Computational CROSS_FEEDING is permitted when explicitly qualified. No polymer-only degrader threshold, mandatory abundance percentage or invented reciprocal benefit is imposed. |
| gtdb | /private/tmp/cm-review-session/batch-14/000410/child-gtdb-crosswalk.json; Current exact rank mappings and snapshot provenance | supports | Sphingopyxis resolves at genus rank with 79/79 reference genomes; Achromobacter reproduces 325/328 and two total destinations. Filesystem mtime does not establish latest release or build date. |
| strain-authority | /private/tmp/cm-review-session/batch-14/000410/child-strain-authority.json; DBS4 accession/NCBI identity and optional strain-specific mapping | supports | Five DBS4 genome components identify taxon 2968500, an unnamed species-rank node, with optional GTDB Sphingopyxis sp024628865 mapping. This does not identify DCP-4 or force a species-name replacement. |
| semantics | /private/tmp/cm-review-session/batch-14/000410/ontology-semantic-notes.json; Final taxonomy, mechanism and cultivation scope | supports | Separate the three source strains, observed substrate capacities, modeled exchange, pooled metabolite detection and liquid/soil stages. |
| resources | /private/tmp/cm-review-session/batch-14/000410/dataset-verification.json; Five direct NCBI component identities and bounded publication resources | supports | CP102384.1 is the DBS4 chromosome; CP102385.1–CP102388.1 are four plasmids. These prior genome records are not new SynCom experiments. SUB identifiers are not verified public nucleotide accessions; model payloads remain unread. |
| snippets | /private/tmp/cm-review-session/batch-14/000410/snippet-audit.json; All 21 canonical excerpt placements | supports | Nineteen placements match fresh HTML body; two match fresh MED bibliographic projections. All 21 occur in raw TXT, but only two belong to its production-trusted prefix. The selected appendix is not independent evidence of source coverage. |
| provenance | /private/tmp/cm-review-session/batch-14/000410/provenance-audit.json; Three histories, original review, batch27 row, current issues and cohort context | supports | Prior snippet, equal-ratio, pH/duration and dangling-edge repairs remain valid dated context. Fresh retrieval neither rewrites historical access limitations nor closes shared issue 596. |
| inspection | /private/tmp/cm-review-session/batch-14/000410/inspect.json; 34 immutable official inputs | supports | Ignored-inclusive discovery bound 12 focal contexts plus 21 unchanged authorities and the target. Repeated generic corpus/build mentions were discovery-only. |
| assets | /private/tmp/cm-review-session/batch-14/000410/lead-source-assets.json; Actual primary, four figures and declared supplementary routes | supports | Complete fresh article and all four main figure pixels were read. Three declared supplementary/model payloads yielded challenge/error responses through bounded ordinary routes; no payload, model or SI figure inspection is claimed. |
| lead-read | /private/tmp/cm-review-session/batch-14/000410/lead-primary-read-scope.json; Whole main and bounded supplementary scope | supports | Whole 85,259-character main projection, all tables/captions/references and four main figures were reviewed. Main-page SI captions are distinguished from inaccessible files; no raw-data or model rerun. |
| sections | /private/tmp/cm-review-session/batch-14/000410/source-section-projection.json; Direct HTML sections and paragraph inventory | supports | All used section labels and paragraph counts are checked against the fresh HTML. The sole three-word quotation is in Discussion paragraph 9. |
| source-scope | /private/tmp/cm-review-session/batch-14/000410/source-audit.json; Final lead assessment | supports | One major mechanistic scope finding and three minor cultivation, GTDB and resource findings. Critical supporting model/assay details remain inaccessible; scientific completion is partial. |
| root-source | /private/tmp/cm-review-session/batch-14/000410/root-independent-source-audit.json; Independent root source assessment | supports | Root independently read the whole primary and all four main figures, checked source locators and agreed the bounded final findings. |
| metrics | /private/tmp/cm-review-session/batch-14/000410/support-final-audit.json; Final support and literal arithmetic | supports | Completeness 85; base quality 135 minus 10 for one P2 and 6 for three P3 gives 119 raw, capped 100. Partial scientific review is not changed by those scores. |
| support-manifest | /private/tmp/cm-review-session/batch-14/000410/supporting-artifact-manifest.json; Frozen supporting inputs | supports | Distinct final support follows source and authority reconciliation; preliminary receipts remain immutable. |
| auxiliary | /private/tmp/cm-review-session/batch-14/000410/auxiliary-frozen-manifest.json; Frozen native and authority outputs | supports | Eight focused checks pass and all 34 official inputs remain unchanged. |
| final-native | /private/tmp/cm-review-session/batch-14/000410/final-validator-summary.json; Eight actual command/stdout/stderr outcomes | supports | Focused checks pass. Zero reported reference issues is not a claim that the trusted cache covers all excerpts. |
| corpus-context | /private/tmp/cm-review-session/batch-14/000410/child-current-corpus-context.json; Actual batch14 baseline | supports | Both corpus commands exited 1 with 44 warnings across 16 of 477 records and zero errors; these are nonrequired context. |
| adapter | /private/tmp/cm-review-session/batch-14/000410/adapter-check.json; Optional adapter in owned runtime | supports | Unavailable; no external-checkout structured adapter was executed. |
| check-validate | /private/tmp/cm-review-session/batch-14/000410/validate.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment is assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-14/000410/validate-strict.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment is assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-14/000410/validate-terms.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment is assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-14/000410/validate-references-explained.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment is assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-14/000410/validate-gtdb.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment is assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-14/000410/validate-gtdb-domain.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment is assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-14/000410/validate-history.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment is assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-14/000410/normalize-cache-names-check.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment is assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-14/audit-network.json; Fresh batch14 corpus baseline | supports | Actual exit 1: 44 warnings across 16 of 477 records and zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-14/check-network-quality.json; Fresh batch14 corpus baseline | supports | Actual exit 1: 44 warnings across 16 of 477 records and zero errors. |

## Limits And Additional Notes

- Supporting DOCX and Data S1/S2 model ZIP payloads remain unavailable after ordinary public requests. No detailed SI figures/tables, genome sequences, raw LC-MS data or executable models were inspected or reanalysed. Main-page captions do not establish exhaustive assay absence.
- Methods 2.7 calls DCPP the sole carbon and nitrogen source despite the NH4Cl recipe and nitrogen-free dichlorprop. Source quotations remain unchanged; this is an internal source conflict, not evidence to remove ammonium.
- Results 3.3 names DCP-6d in the optimal four-member model, while the soil assay description in Methods 2.7 uses DCP-2. Main Table 1 also differs from Results 3.1 in DCP-6d/DCP-11d genome values and one initial reaction count. Preserve arm-specific labels rather than harmonizing unencoded values.
- Nicotinamide-ribonucleotide is discussed as a modeled exchange but excluded from the selected detection panel. Six of seven selected metabolites is not all modeled exchanges, and nondetection alone does not prove instability or consumption.
- The selected cache appendix contains 19 canonical excerpts excluded by production cache trust. Independent fresh HTML verification supports them here without upgrading cache provenance or closing broader historical access issues.
- Three node assessments bind all six exact canonical snippet hashes and actual taxa; there are no downstream arrows. The sole direct quotation is three words from Discussion paragraph 9.
- All 34 inspected inputs remain unchanged. Candidate validation, parent saving and post-save gates occur separately; no future pass is asserted.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T030952Z-dcpp-three-strain-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: DCPP DBS4-DCP-4-DCP-11d record review
started_at: '2026-10-22T03:01:26.898757Z'
finished_at: '2026-10-22T03:09:52.238055Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, supporting and auxiliary reviewers; no
    person-level independence claim.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: Whole primary text and four main figures support the three-strain design
  and measured degradation phenotypes. One major finding narrows experimentally verified
  exchange claims; three minor findings concern cultivation stages, GTDB grounding/provenance
  and source resources. Critical supplementary assay/model payloads remain unavailable,
  so scientific completion is partial. Eight focused checks pass; literal completeness
  is 85 and raw quality 119, capped 100.
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
  - path: history/records/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom/2026-09-21T172849Z-codex-f34c71.yaml
    sha256: 5e24a51157fed4c1f5e0f52ce772589906d1a20af86c4ccd082e2a99d2864b07
    role: context
  - path: history/records/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom/2026-09-21T173342Z-claude-code-f8f7b3.yaml
    sha256: 5d3e4e3e5104bc0ff9b29e8174098d895708ccc0b5a11a8745745edc18c327d5
    role: context
  - path: history/records/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom/2026-09-21T173842Z-claude-code-157268.yaml
    sha256: a11d7a131eaf7f973ddd1965f78a15db46e2773687b12f3584dad68f6e612af5
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    sha256: f9b1a67fb3fcd903a1adcb16f0eb5279a3738ff6807ddc4cc9203553be36bc3a
    role: target
  - path: references_cache/PMID_42613016.txt
    sha256: a5b89d867b4d0264fe7cbce7ff2e0abdf55a50e00d93ef3ee63a23511895b398
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch27.yaml
    sha256: e643b8f12adfc71acdd4f9bca108689885b70c32ea93b44b1055d73f3022cad0
    role: context
  - path: reports/causal_graph_review/cache-provenance-20261006-batch26.json
    sha256: 12ced6a1723bea20a770a917796b87273067197aec267303da144f09e07dacd3
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch27.yaml
    sha256: 90e6a0ad3e095a1301744958f706782510d03bdf40852999837d12401019ded0
    role: context
  - path: reports/yaml_record_review/20260921T173112Z-DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.md
    sha256: f2379d7d457aa98c862ccdde76f52780c6a3593c4afcac2c056aa98509411f00
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
- target_id: CommunityMech:000410
  path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
  label: DCPP DBS4-DCP-4-DCP-11d Degradation SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    role: canonical_record
scope:
  description: Whole target and fresh public main article with four main figures;
    bounded direct genome metadata and current authority checks. Main-page SI captions
    were read, but the three declared supplementary/model files were inaccessible.
  selection: Only released CommunityMech:000410 in the owned batch14 checkout.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000410
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000410
  command: just --no-dotenv validate kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
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
  - CommunityMech:000410
  command: just --no-dotenv validate-strict kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-14/000410/strict-report.tsv
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
  - CommunityMech:000410
  command: just --no-dotenv validate-terms kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
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
  - CommunityMech:000410
  command: just --no-dotenv validate-references-explained kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
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
  - CommunityMech:000410
  command: just --no-dotenv validate-gtdb kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
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
  - CommunityMech:000410
  command: just --no-dotenv validate-gtdb-domain kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
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
  - CommunityMech:000410
  command: just --no-dotenv validate-history history/records/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom
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
  - CommunityMech:000410
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
  - CommunityMech:000410
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context; not wholly attributed to this target.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000410
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context; not wholly attributed to this target.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in owned runtime.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - adapter
  scope_note: No external-checkout adapter executed.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
  locator: Whole maintained YAML
  summary: Defined DBS4/DCP-4/DCP-11d SynCom; three CROSS_FEEDING nodes, zero downstream
    arrows. Canonical YAML owns future repairs.
  support: supports
  accessed_at: '2026-10-22T03:09:52.235309Z'
- evidence_id: publication
  kind: database
  reference: PMID:42613016; DOI:10.1111/1462-2920.70404
  locator: Fresh MED identity and complete PMC article metadata
  summary: PMID, DOI and PMC13485441 agree. Fresh public PMC HTML is complete despite
    failed XML/publisher routes and the MED non-OA flag. Supplementary payloads remain
    unavailable.
  support: supports
  accessed_at: '2026-10-22T03:09:52.235392Z'
  snapshot_sha256: 89b167b3209317fd827da8b1d014aa476feeccaa24c2d5c2dc84ab1dfed485cf
- evidence_id: culture
  kind: primary_source
  reference: PMID:42613016; DOI:10.1111/1462-2920.70404
  locator: Material and Methods / Chemicals, Medium, Bacterial Strains, and Culture
    Conditions (2.1), sole paragraph; In Vitro Experiments Testing Predictions by
    Modelling (2.7), three direct paragraphs
  summary: The existing mineral salts, pH 7 and 30°C/15 h LC-MS stage are supported.
    Liquid degradation assays use 20 mL, 30 mg/L DCPP and 180 rpm. Soil degradation
    and solvent extraction are separate operations; the 30°C/180 rpm/1 h extraction
    is not a soil cultivation condition.
  support: supports
  accessed_at: '2026-10-22T03:09:52.235433Z'
  snapshot_sha256: 66534fbf59a527df88908c16f82d0575e40b38fcecaed7c22a5e2513c01c277a
- evidence_id: model
  kind: primary_source
  reference: PMID:42613016; DOI:10.1111/1462-2920.70404
  locator: Material and Methods / Construction of Multi-Compartment Models for Bacterial
    Communities (2.5), sole paragraph; Metabolic Model-Based Simulations of Growth
    and DCPP Degradation (2.6), both paragraphs; Results / Simulation-Based SynCom
    Design and Metabolic Interaction Analysis (3.3), all three paragraphs; Figure
    3
  summary: Fifteen DBS4-containing models rank candidate communities by predicted
    biomass. Equal initial ratios are shared with experiments. Predicted nutrient
    and 2,4-DCP flows remain computational; biomass optimization does not directly
    measure exchange.
  support: supports
  accessed_at: '2026-10-22T03:09:52.235584Z'
  snapshot_sha256: 66534fbf59a527df88908c16f82d0575e40b38fcecaed7c22a5e2513c01c277a
- evidence_id: performance
  kind: primary_source
  reference: PMID:42613016; DOI:10.1111/1462-2920.70404
  locator: Results / Experimental Validation of Metabolic Model-Based Simulations
    (3.4), paragraphs 1–3; Figure 4; Material and Methods (2.7), paragraphs 1–2
  summary: Liquid removal and soil degradation support the selected design. In soil
    the three-member treatment initially lags and becomes comparable by day 7. These
    assays measure pesticide removal, not interstrain metabolite transfer.
  support: supports
  accessed_at: '2026-10-22T03:09:52.235706Z'
  snapshot_sha256: 66534fbf59a527df88908c16f82d0575e40b38fcecaed7c22a5e2513c01c277a
- evidence_id: metabolites
  kind: primary_source
  reference: PMID:42613016; DOI:10.1111/1462-2920.70404
  locator: Material and Methods (2.7), paragraph 3; Results (3.4), paragraphs 4–5;
    Supporting information, exposed Figure S3 and Figure S4 captions
  summary: LC-MS detected six of seven selected metabolites in the liquid consortium.
    Main-text addback experiments describe DBS4 with a four-nutrient mixture, 2,4-DCP
    or control. Bulk detection does not identify donor, consumer or transfer rate;
    mixture effects are not four independent metabolite effects. Only captions of
    S3/S4 were read, not their inaccessible payload.
  support: supports
  accessed_at: '2026-10-22T03:09:52.235829Z'
  snapshot_sha256: 66534fbf59a527df88908c16f82d0575e40b38fcecaed7c22a5e2513c01c277a
- evidence_id: mechanism-limits
  kind: primary_source
  reference: PMID:42613016; DOI:10.1111/1462-2920.70404
  locator: Discussion (4), ninth direct paragraph; HTML section emi70404-sec-0015,
    p[9]
  summary: The authors distinguish validation of model predictions from quantitative
    dissection of nutrient exchange and detoxification. Discussion paragraph 5 asserts
    helper rescue, while the available experimental description does not isolate that
    route. The inaccessible supplement prevents an exhaustive absence claim.
  support: supports
  accessed_at: '2026-10-22T03:09:52.235949Z'
  snapshot_sha256: 66534fbf59a527df88908c16f82d0575e40b38fcecaed7c22a5e2513c01c277a
  quote: not quantitatively resolved
- evidence_id: substrates
  kind: primary_source
  reference: PMID:42613016; DOI:10.1111/1462-2920.70404
  locator: Results / Whole-Genome Sequencing and Analysis of DCPP Metabolic Pathway
    (3.1), paragraphs 1–3; Discussion (4), paragraph 5
  summary: DBS4 uses both DCPP enantiomers, DCP-4 uses R-DCPP, and DCP-11d can use
    2,4-DCP. These substrate capabilities and model predictions support qualified
    degrader/cross-feeder roles without claiming measured recipient-specific exchange.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236067Z'
  snapshot_sha256: 66534fbf59a527df88908c16f82d0575e40b38fcecaed7c22a5e2513c01c277a
- evidence_id: resource-source
  kind: primary_source
  reference: PMID:42613016; DOI:10.1111/1462-2920.70404
  locator: Material and Methods / Genome Sequencing (2.3), sole paragraph; Results
    (3.2), paragraphs 1–2; Data Availability Statement; Supporting information declarations
  summary: The paper cites DBS4 CP102384–CP102388, other-member SUB submissions and
    two model archives. Data S1/S2 and the supporting DOCX were identified but not
    read. Methods and Data Availability differ by one digit in the DCP-6d SUB identifier.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236202Z'
  snapshot_sha256: 66534fbf59a527df88908c16f82d0575e40b38fcecaed7c22a5e2513c01c277a
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000410/ontology-authority.json
  locator: Seven ID-label pairs, 15 placements and definitions
  summary: All current labels match; dichlorprop and 2,4-dichlorophenol remain distinct.
    Shared genus IDs do not merge separate source strains.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236356Z'
  snapshot_sha256: 7ac364a64fdefbf27a6156f9e767ee78fb85318811a2622311b51e9d80a06134
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000410/child-schema-semantics.json
  locator: Literal interaction, role, evidence, state and culture semantics
  summary: Computational CROSS_FEEDING is permitted when explicitly qualified. No
    polymer-only degrader threshold, mandatory abundance percentage or invented reciprocal
    benefit is imposed.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236418Z'
  snapshot_sha256: 773603f9b3266eb38444c859568edbfff1feaafc8ceec2f62597d7b5bf989b06
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000410/child-gtdb-crosswalk.json
  locator: Current exact rank mappings and snapshot provenance
  summary: Sphingopyxis resolves at genus rank with 79/79 reference genomes; Achromobacter
    reproduces 325/328 and two total destinations. Filesystem mtime does not establish
    latest release or build date.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236466Z'
  snapshot_sha256: 720710b490209f925870d648594ef8964a0f898ba2430f14acb7d55170288b70
- evidence_id: strain-authority
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000410/child-strain-authority.json
  locator: DBS4 accession/NCBI identity and optional strain-specific mapping
  summary: Five DBS4 genome components identify taxon 2968500, an unnamed species-rank
    node, with optional GTDB Sphingopyxis sp024628865 mapping. This does not identify
    DCP-4 or force a species-name replacement.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236501Z'
  snapshot_sha256: 32395bbde224026a08f81aa553c682302a6bcf17a7bbde46cedb328425b10e0c
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000410/ontology-semantic-notes.json
  locator: Final taxonomy, mechanism and cultivation scope
  summary: Separate the three source strains, observed substrate capacities, modeled
    exchange, pooled metabolite detection and liquid/soil stages.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236536Z'
  snapshot_sha256: 15e23ad9432ac04c54f7194f7bfe176936e5ad7ba715dcc00a8bea765f8a156f
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/dataset-verification.json
  locator: Five direct NCBI component identities and bounded publication resources
  summary: CP102384.1 is the DBS4 chromosome; CP102385.1–CP102388.1 are four plasmids.
    These prior genome records are not new SynCom experiments. SUB identifiers are
    not verified public nucleotide accessions; model payloads remain unread.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236577Z'
  snapshot_sha256: f2265e9c7c59bbe12aa994c5d4f83f0f17cc5d38402345878a4126f3c0cbdd29
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/snippet-audit.json
  locator: All 21 canonical excerpt placements
  summary: Nineteen placements match fresh HTML body; two match fresh MED bibliographic
    projections. All 21 occur in raw TXT, but only two belong to its production-trusted
    prefix. The selected appendix is not independent evidence of source coverage.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236620Z'
  snapshot_sha256: f340db57e8ec4fe7c3d47ae79653d92af48d9d37932649c7613ed4a775d108a7
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-14/000410/provenance-audit.json
  locator: Three histories, original review, batch27 row, current issues and cohort
    context
  summary: Prior snippet, equal-ratio, pH/duration and dangling-edge repairs remain
    valid dated context. Fresh retrieval neither rewrites historical access limitations
    nor closes shared issue 596.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236655Z'
  snapshot_sha256: e5cf93ab87cd8d6d8c8762c81545bd6aca1e9a7cb8195a3c5736ded6c14f260a
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/inspect.json
  locator: 34 immutable official inputs
  summary: Ignored-inclusive discovery bound 12 focal contexts plus 21 unchanged authorities
    and the target. Repeated generic corpus/build mentions were discovery-only.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236698Z'
  snapshot_sha256: 6f49e761c8fc37befdeeca753068ff218e5d3c98c8b16e2cc7211668262219a2
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/lead-source-assets.json
  locator: Actual primary, four figures and declared supplementary routes
  summary: Complete fresh article and all four main figure pixels were read. Three
    declared supplementary/model payloads yielded challenge/error responses through
    bounded ordinary routes; no payload, model or SI figure inspection is claimed.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236730Z'
  snapshot_sha256: 7d53222054d4b131a1f41627ed37ba9367339604ec5f33422160793beda10bc2
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/lead-primary-read-scope.json
  locator: Whole main and bounded supplementary scope
  summary: Whole 85,259-character main projection, all tables/captions/references
    and four main figures were reviewed. Main-page SI captions are distinguished from
    inaccessible files; no raw-data or model rerun.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236766Z'
  snapshot_sha256: 94fb981100884cbac605b4e28190fce7d794c1c3b015e688126f448488781a37
- evidence_id: sections
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/source-section-projection.json
  locator: Direct HTML sections and paragraph inventory
  summary: All used section labels and paragraph counts are checked against the fresh
    HTML. The sole three-word quotation is in Discussion paragraph 9.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236797Z'
  snapshot_sha256: bf3c0d470f5ab744c8e594eaceeabb1e3a2fed78c6bfb832cb75d3b81c585879
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/source-audit.json
  locator: Final lead assessment
  summary: One major mechanistic scope finding and three minor cultivation, GTDB and
    resource findings. Critical supporting model/assay details remain inaccessible;
    scientific completion is partial.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236848Z'
  snapshot_sha256: 316bbca088fc19e760cd794f093b8ef430a6ef1ad315ffc2ff7474bffdaaf317
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/root-independent-source-audit.json
  locator: Independent root source assessment
  summary: Root independently read the whole primary and all four main figures, checked
    source locators and agreed the bounded final findings.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236879Z'
  snapshot_sha256: 2cf6e4a2ab9e602cae46e35ab2984e7a1f300e6b0cdd325ba01f848f207285bd
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/support-final-audit.json
  locator: Final support and literal arithmetic
  summary: Completeness 85; base quality 135 minus 10 for one P2 and 6 for three P3
    gives 119 raw, capped 100. Partial scientific review is not changed by those scores.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236911Z'
  snapshot_sha256: 58d95668ee363bb84bf2c624c0e5f7311e0f44b0aee4a21d77fb6b233855e2b1
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/supporting-artifact-manifest.json
  locator: Frozen supporting inputs
  summary: Distinct final support follows source and authority reconciliation; preliminary
    receipts remain immutable.
  support: supports
  accessed_at: '2026-10-22T03:09:52.236977Z'
  snapshot_sha256: 94690d4bf607fa8d4fa6fda0511fa0e5059ce9fdb47c662a7c3c037070fd49d8
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/auxiliary-frozen-manifest.json
  locator: Frozen native and authority outputs
  summary: Eight focused checks pass and all 34 official inputs remain unchanged.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237009Z'
  snapshot_sha256: 87140ecf3fd651de18819132a529c4e32cc356e7bd4714aecba97c0327b5a691
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/final-validator-summary.json
  locator: Eight actual command/stdout/stderr outcomes
  summary: Focused checks pass. Zero reported reference issues is not a claim that
    the trusted cache covers all excerpts.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237039Z'
  snapshot_sha256: 544b0609f045649c818936b7a6dd01e9a4282fedadf3a31a9a29bd15eace6a93
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/child-current-corpus-context.json
  locator: Actual batch14 baseline
  summary: Both corpus commands exited 1 with 44 warnings across 16 of 477 records
    and zero errors; these are nonrequired context.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237070Z'
  snapshot_sha256: 6b60f351e93666f28cfbac2098352437bc61df9dc8f0ed09ff435ec277daa6cc
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/adapter-check.json
  locator: Optional adapter in owned runtime
  summary: Unavailable; no external-checkout structured adapter was executed.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237097Z'
  snapshot_sha256: 64189224f2736cc60165312b4e81b91b3b9ec32287cab86121c19e1acc5fa887
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/validate.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237327Z'
  snapshot_sha256: ff073a9c8961a95509fa51b0e8601ad5b1145a62a7e551e13831476a86ddfc53
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/validate-strict.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237388Z'
  snapshot_sha256: 9f7cb3666fbbf22ebd2a6c6292f38368e37d656eb8bf8c633b659d16f1d7cd77
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/validate-terms.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237439Z'
  snapshot_sha256: eae7c50bb77389fff105c65603596d900f6522820407ea4d614a900cad305816
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/validate-references-explained.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237490Z'
  snapshot_sha256: 0a808a233cba72ff43a2cdb9befa806bbf72d34cdee8eafcb8eb88b484bdcd73
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/validate-gtdb.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237541Z'
  snapshot_sha256: 1d9c41b74de32f7fb1a1a9cd4ec56b6d9e9479d244e64fd4b8741b3e76d7ddaa
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/validate-gtdb-domain.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237592Z'
  snapshot_sha256: f0fe529cf787516b7a7f1a6f894b44b8a237836b52bf91207fad1cfaaa8c62b9
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/validate-history.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237660Z'
  snapshot_sha256: e8e95ca2f2450e3ed4cd3cf9d47e15e620227443e7662efdff7502dc69af113e
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000410/normalize-cache-names-check.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:09:52.237711Z'
  snapshot_sha256: 77cc753b4c878738d4983dc3109cd4a7c47c795ab8db3b08144ca3ef8ac9750b
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/audit-network.json
  locator: Fresh batch14 corpus baseline
  summary: 'Actual exit 1: 44 warnings across 16 of 477 records and zero errors.'
  support: supports
  accessed_at: '2026-10-22T03:09:52.237787Z'
  snapshot_sha256: 3110e0bb1dbe3ea63b81aea82871ac4adb2915c8fce1d15249422d0f5db266c6
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/check-network-quality.json
  locator: Fresh batch14 corpus baseline
  summary: 'Actual exit 1: 44 warnings across 16 of 477 records and zero errors.'
  support: supports
  accessed_at: '2026-10-22T03:09:52.238000Z'
  snapshot_sha256: 18896ef4136601b37550cb5612abc06784abcbf982e4778cbf2b9c10368cb66a
assessments:
- assessment_id: identity
  area: identity
  topic: Three-strain synthetic community
  outcome: supported
  summary: The exact DBS4/DCP-4/DCP-11d design, synthetic origin and engineered state
    are supported.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - record
  - model
  - substrates
  - ontology
  - schema
  dimensions:
  - name: member_scope
    value: DBS4, DCP-4 and DCP-11d
    definition: Three source strains; two Sphingopyxis genus descriptors and one Achromobacter
      genus descriptor.
    evidence_ids:
    - substrates
    - ontology
  - name: experimental_setting
    value: Liquid mineral-medium assays and DCPP-spiked soil
    definition: Defined synthetic design, not an asserted natural three-strain community.
    evidence_ids:
    - culture
    - performance
  details: Retain separate Sphingopyxis strains despite their shared genus CURIE.
    Bosea DCP-2 and Pigmentiphaga DCP-6d are larger-design comparators, not additional
    focal members. Laboratory environment and modeled contaminated soil are separate
    contexts.
- assessment_id: node-0
  area: graph
  topic: Model-selected DCPP degradation
  outcome: concern
  summary: Retain model selection and measured performance; distinguish the CROSS_FEEDING
    interpretation from removal endpoints.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - model
  - performance
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[0]; name Model-selected DCPP degradation;
    scope COMMUNITY_LEVEL; interaction_type CROSS_FEEDING. Encoded taxa: {"source":
    null, "target": null, "participants": []}. Canonical snippet bindings: [{"selector":
    "ecological_interactions[0].evidence[0].snippet", "sha256": "c3e35789dd9301572c447a8a25f537c89141496c4d33ecaf38d7ef71d2a18442",
    "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[0].evidence[1].snippet", "sha256": "8f5766abd3bfc914c2c7dd7a9aa934597cbf1e82bd756c7b98a71c39becf2874",
    "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 f340db57e8ec4fe7c3d47ae79653d92af48d9d37932649c7613ed4a775d108a7.
    PMID:42613016 locator: Methods 2.5–2.7; Results 3.3 paragraph 1 and 3.4 paragraphs
    1–2; Figures 3–4. Keep SUPPORT/COMPUTATIONAL for model selection and SUPPORT/IN_VITRO
    for removal performance. An explicit computational or PARTIAL mechanistic qualifier
    is needed if this contextual node remains typed CROSS_FEEDING.'
- assessment_id: node-1
  area: graph
  topic: DBS4 to DCP-11d 2,4-DCP detoxification
  outcome: concern
  summary: Retain the modeled DBS4-to-DCP-11d 2,4-DCP direction, while qualifying
    the asserted experimental rescue.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - model
  - substrates
  - metabolites
  - mechanism-limits
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[1]; name DBS4 to DCP-11d 2,4-DCP
    detoxification; scope PAIRWISE; interaction_type CROSS_FEEDING. Encoded taxa:
    {"source": {"preferred_term": "Sphingopyxis sp. DBS4", "term": {"id": "NCBITaxon:165697",
    "label": "Sphingopyxis"}}, "target": {"preferred_term": "Achromobacter sp. DCP-11d",
    "term": {"id": "NCBITaxon:222", "label": "Achromobacter"}}, "participants": []}.
    Canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "a0fbd4d5e34581e318e06c8e579c08308c6ddbfbd8d5b902ffc6b9f248609320",
    "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "7170a0f8df205dc8afcdd143936144afbe7df5f4cca4403e1b0a244eb4ad0588",
    "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 f340db57e8ec4fe7c3d47ae79653d92af48d9d37932649c7613ed4a775d108a7.
    PMID:42613016 locator: Results 3.3 paragraph 2 and 3.1 paragraph 3; Results 3.4
    paragraph 5; Discussion paragraphs 5 and 9; Figure 3C; exposed Figure S4 caption.
    Keep SUPPORT/COMPUTATIONAL for predicted direction. The IN_VITRO excerpt is an
    author interpretation in Discussion, supported by substrate capacity and inhibition
    observations but not an independently isolated rescue arm in the available description.
    Qualify mechanistic support as PARTIAL; do not claim the unread SI rules out additional
    assays.'
- assessment_id: node-2
  area: graph
  topic: Predicted exchanged metabolite validation
  outcome: concern
  summary: Retain liquid LC-MS detection as partial mechanistic support, not measured
    donor-recipient exchange.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - metabolites
  - mechanism-limits
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[2]; name Predicted exchanged metabolite
    validation; scope COMMUNITY_LEVEL; interaction_type CROSS_FEEDING. Encoded taxa:
    {"source": null, "target": null, "participants": [{"preferred_term": "Sphingopyxis
    sp. DBS4", "term": {"id": "NCBITaxon:165697", "label": "Sphingopyxis"}}, {"preferred_term":
    "Sphingopyxis sp. DCP-4", "term": {"id": "NCBITaxon:165697", "label": "Sphingopyxis"}},
    {"preferred_term": "Achromobacter sp. DCP-11d", "term": {"id": "NCBITaxon:222",
    "label": "Achromobacter"}}]}. Canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet",
    "sha256": "cbc1ed190db4dd9a056e6cb48f6f697576adeee51d3cbadc48cff49340c6a8a6",
    "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "IN_VITRO"},
    {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "ae24390a52371dca674ada3facfd06b76e2f5d220840f8f6e6eccfbe13f1919e",
    "reference": "PMID:42613016", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 f340db57e8ec4fe7c3d47ae79653d92af48d9d37932649c7613ed4a775d108a7.
    PMID:42613016 locator: Methods 2.7 paragraph 3; Results 3.4 paragraph 4; Discussion
    paragraph 9; exposed Figure S3 caption. Keep IN_VITRO for bulk extracellular detection
    and the three-strain culture. Change only the mechanistic interpretation/tier
    as needed: presence does not resolve production, consumption, transfer or rates.
    Six of seven selected compounds is narrower than all model-predicted exchanges.'
- assessment_id: topology
  area: graph
  topic: No downstream arrows
  outcome: supported
  summary: Three current nodes and zero arrows are structurally valid; no causal edge
    is required.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - record
  - schema
  - provenance
  details: No duplicate-CURIE deletion or forced reciprocal benefit. Preserve valid
    modeled directions while narrowing their experimental interpretation.
- assessment_id: cultivation
  area: completeness
  topic: Separate assay and analytical stages
  outcome: concern
  summary: The existing LC-MS medium is supported; omitted liquid setup and stage-specific
    inocula can be recovered.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - culture
  - schema
  details: Keep the 15 h LC-MS endpoint separate from liquid time courses and soil
    degradation. Do not copy soil extraction settings into cultivation or infer a
    vessel capacity.
- assessment_id: taxonomy
  area: grounding
  topic: Genus mappings and exact DBS4 boundary
  outcome: concern
  summary: Current NCBI identities are valid; both Sphingopyxis blocks can be grounded
    at genus rank.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - ontology
  - gtdb
  - strain-authority
  details: Achromobacter core mapping reproduces but latest/build provenance does
    not. Optional DBS4 accession refinement must not propagate to DCP-4. Source-modeled
    roles need source-specific qualifiers, not blanket deletion.
- assessment_id: resource-traceability
  area: provenance
  topic: Prior genomes and declared models
  outcome: concern
  summary: The publication links are correct, but source-linked genome/model traceability
    is incomplete.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - resource-source
  - resources
  details: Add verified DBS4 components with member-specific scope. Preserve unresolved
    SUB submissions and the unread status of Data S1/S2; do not invent accessions
    for other members.
- assessment_id: source-limits
  area: scope
  topic: Main-text review with critical supplementary limits
  outcome: unknown
  summary: Whole primary reading supports bounded findings; model files and detailed
    supporting assays remain unavailable.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - assets
  - lead-read
  - mechanism-limits
  - source-scope
  details: Fresh main retrieval resolves the old main-access gap, not supplementary
    validation. Existing mechanistic discussion remains a useful knowledge gap. Source-internal
    nitrogen, comparator and table inconsistencies are retained as limitations, not
    extra record findings.
- assessment_id: ownership
  area: ownership
  topic: Maintained record and append-only context
  outcome: supported
  summary: Repairs belong to the focal YAML; historical reviews and cache provenance
    remain unchanged.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - inspection
  - provenance
  details: Current issue states are context only. No issue closure, curation-history
    event or scientific-status promotion is performed.
- assessment_id: native
  area: schema
  topic: Focused validity and independent source support
  outcome: supported
  summary: Eight focused checks pass; corpus failures and optional-adapter limits
    remain explicit.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - final-native
  - auxiliary
  - snippets
  - corpus-context
  - adapter
- assessment_id: metrics
  area: completeness
  topic: Two literal native scores
  outcome: supported
  summary: Completeness 85; raw quality 119, capped 100.
  target_ids:
  - CommunityMech:000410
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields/roles 50 + environment 5 + three nodes 10 + external
      resources 5 + medium 10 + node metabolites 5. Only two factors and no associated_datasets
      give 0 for those components.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 - 1 major*10 - 3 minor*2 + 20*min((6 evidence/3 nodes)/2,1) +
      15 COMPLETE = 119 raw, capped 100. Three typed nodes, zero arrows. Neither score
      certifies mechanistic support or scientific completion.
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
- finding_id: mechanism-scope
  issue_key: cm-000410-mechanism-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material inflation from modeled or pooled observations to
    experimentally established interstrain exchange.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Separate model predictions, measured outcomes and exchange inference
  description: The description extends exchange validation to soil, while LC-MS is
    a liquid assay. Node 0 measures selection/performance; node 1 asserts helper rescue
    beyond the available isolated perturbation description; node 2 detects pooled
    compounds without donor-recipient resolution. Preserve the model and observed
    phenotypes with explicit claim-level support.
  target_ids:
  - CommunityMech:000410
  field_paths:
  - description
  - ecological_interactions[0]
  - ecological_interactions[1]
  - ecological_interactions[2]
  evidence_ids:
  - model
  - performance
  - metabolites
  - mechanism-limits
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    role: canonical_record
  ownership_note: The maintained record owns repair; historical/shared issues are
    not closed or superseded.
- finding_id: culture-stages
  issue_key: cm-000410-culture-stages
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable cultivation, grounding or source-resource
    gap; core community identity remains valid.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Recover the liquid setup and distinguish assay stages
  description: The source reports 20 mL liquid assays, 180 rpm and stage-specific
    strain inocula. The existing salts/pH/temperature/15 h LC-MS block is sound but
    does not encode those distinctions.
  target_ids:
  - CommunityMech:000410
  field_paths:
  - growth_media
  - cultivation_setup
  evidence_ids:
  - culture
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    role: canonical_record
  ownership_note: The maintained record owns repair; historical/shared issues are
    not closed or superseded.
- finding_id: gtdb-grounding
  issue_key: cm-000410-gtdb-grounding
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable cultivation, grounding or source-resource
    gap; core community identity remains valid.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Resolve genus blocks and correct mapping provenance
  description: Both Sphingopyxis descriptors remain UNRESOLVED despite a supported
    genus mapping. Achromobacter uses an unsupported latest-release/build-date claim
    derived from file mtime.
  target_ids:
  - CommunityMech:000410
  field_paths:
  - taxonomy[0].taxon_term
  - taxonomy[1].taxon_term
  - taxonomy[2].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - strain-authority
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    role: canonical_record
  ownership_note: The maintained record owns repair; historical/shared issues are
    not closed or superseded.
- finding_id: source-resources
  issue_key: cm-000410-source-resources
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable cultivation, grounding or source-resource
    gap; core community identity remains valid.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Link verified genome components and declared model outputs
  description: Publication links omit five verified DBS4 genome components and the
    declared model archives. Other strains have SUB submissions, not verified public
    sequence identifiers; unavailable archive contents must remain explicitly unreviewed.
  target_ids:
  - CommunityMech:000410
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - resource-source
  - resources
  - assets
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    role: canonical_record
  ownership_note: The maintained record owns repair; historical/shared issues are
    not closed or superseded.
actions:
- action_id: qualify-mechanism
  description: Retain the model and measured phenotypes with the correct experimental
    scope.
  finding_ids:
  - mechanism-scope
  target_ids:
  - CommunityMech:000410
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Describe soil results as degradation-performance validation. Limit LC-MS detection
    to liquid culture and keep the initial soil lag/day-7 convergence rather than
    universal equivalence.
  - For node 0 retain computational selection and IN_VITRO removal evidence separately.
    If retaining CROSS_FEEDING, label its mechanistic interpretation as modeled or
    PARTIAL rather than experimentally resolved exchange.
  - For node 1 retain the DBS4 to DCP-11d modeled 2,4-DCP direction, observed helper
    substrate capability and DBS4 inhibition. Attribute rescue to the authors’ interpretation
    and mark experimental mechanistic support PARTIAL until detailed perturbation
    evidence is inspected; do not claim no such experiment exists in unread SI.
  - For node 2 retain six-of-seven selected metabolite detection with IN_VITRO evidence,
    while treating exchange direction and flux as inferred. Four nutrients were added
    together; do not convert this into four independent causal tests. Keep the existing
    unresolved-mechanism discussion and zero downstream arrows.
- action_id: recover-culture
  description: Encode available liquid conditions while preserving stage boundaries.
  finding_ids:
  - culture-stages
  target_ids:
  - CommunityMech:000410
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Retain the current per-litre mineral salts, MgSO4 heptahydrate, pH 7, 30 mg/L
    DCPP and 30°C. Keep the 15 h endpoint specifically attached to LC-MS under Methods
    2.7 paragraph 3.
  - Use Methods 2.7 paragraph 1 for 20 mL liquid assays, 180 rpm, uninoculated control
    and 3 h HPLC sampling. State that each strain was prepared at 1.5×10^6 CFU/mL;
    do not silently convert a prepared inoculum concentration into an unstated final
    concentration or infer vessel capacity.
  - Use Methods 2.7 paragraph 2 for 5 mg/kg soil DCPP and final approximately 10^6
    CFU/g per strain. Keep 5 g aliquots, 50 mL extraction tubes and 30°C/180 rpm/1
    h extraction out of soil cultivation setpoints. BATCH may describe individual
    assay stages if justified, without merging experiments.
  - Preserve exact source snippets containing the sole-carbon-and-nitrogen wording,
    but explain its conflict with NH4Cl-containing medium and nitrogen-free DCPP rather
    than reproducing that error as medium chemistry.
- action_id: repair-gtdb
  description: Ground the existing genus descriptors with precise snapshot provenance.
  finding_ids:
  - gtdb-grounding
  target_ids:
  - CommunityMech:000410
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Add GROUNDED genus blocks for both Sphingopyxis descriptors using GTDB:g__Sphingopyxis,
    79/79 reference genomes, majority fraction 1.0 and ncbi_rank_g. Keep DBS4 and
    DCP-4 separate source strains.
  - Retain Achromobacter 325/328, majority fraction 0.991 and two total GTDB destinations.
    Record actual mapping SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    and rank route; identify filesystem mtime only as mtime, not release latest or
    build date.
  - Optional DBS4-specific enrichment may cite NCBITaxon:2968500 and its verified
    archive identity/GTDB Sphingopyxis sp024628865. Do not transfer this to DCP-4
    or invent a named species or strain accession.
- action_id: add-resources
  description: Add source-scoped genome and model traceability.
  finding_ids:
  - source-resources
  target_ids:
  - CommunityMech:000410
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Link CP102384.1 as the DBS4 chromosome and CP102385.1–CP102388.1 as its four plasmids,
    with SAMN30005345 context. These are nucleotide components of a prior genome,
    not assembly identifiers for strain_designation.genome_accession or new SynCom
    sequencing.
  - Link declared Data S1 five single-strain models and Data S2 fifteen community
    models as source resources; record that their payloads were unavailable in this
    review. Do not assert model contents, versions or executable reproducibility from
    captions alone.
  - Keep SUB15680332, SUB15680937, SUB15681044 and SUB15681330 as unresolved submission
    leads. Preserve the Data Availability SUB1568104 versus Methods SUB15681044 conflict;
    do not substitute invented public accessions.
- action_id: validate-future-curation
  description: Validate any separately authorized record repair.
  finding_ids:
  - mechanism-scope
  - culture-stages
  - gtdb-grounding
  - source-resources
  target_ids:
  - CommunityMech:000410
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DCPP_DBS4_DCP4_DCP11d_Degradation_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Recheck source snippets, exact strain/role scope and all three node selectors
    with the modeled-versus-observed distinction. Run focused schema, strict, terms,
    explained references, GTDB/domain and history checks.
  - After authorized curation run just gen-html and just check-docs-current. Preserve
    existing histories and source/cache bytes and add curation provenance. This review
    performs no canonical repair, generated-page change, Git operation or issue mutation.
limitations:
- Supporting DOCX and Data S1/S2 model ZIP payloads remain unavailable after ordinary
  public requests. No detailed SI figures/tables, genome sequences, raw LC-MS data
  or executable models were inspected or reanalysed. Main-page captions do not establish
  exhaustive assay absence.
- Methods 2.7 calls DCPP the sole carbon and nitrogen source despite the NH4Cl recipe
  and nitrogen-free dichlorprop. Source quotations remain unchanged; this is an internal
  source conflict, not evidence to remove ammonium.
- Results 3.3 names DCP-6d in the optimal four-member model, while the soil assay
  description in Methods 2.7 uses DCP-2. Main Table 1 also differs from Results 3.1
  in DCP-6d/DCP-11d genome values and one initial reaction count. Preserve arm-specific
  labels rather than harmonizing unencoded values.
- Nicotinamide-ribonucleotide is discussed as a modeled exchange but excluded from
  the selected detection panel. Six of seven selected metabolites is not all modeled
  exchanges, and nondetection alone does not prove instability or consumption.
- The selected cache appendix contains 19 canonical excerpts excluded by production
  cache trust. Independent fresh HTML verification supports them here without upgrading
  cache provenance or closing broader historical access issues.
notes:
- Three node assessments bind all six exact canonical snippet hashes and actual taxa;
  there are no downstream arrows. The sole direct quotation is three words from Discussion
  paragraph 9.
- All 34 inspected inputs remain unchanged. Candidate validation, parent saving and
  post-save gates occur separately; no future pass is asserted.
tags:
- record-review
- bioremediation
- partial-source
- batch-14
```
