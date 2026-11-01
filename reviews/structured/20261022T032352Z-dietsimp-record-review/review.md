# DIETsimp lignocellulose-to-methane record review

- Review: 20261022T032352Z-dietsimp-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T03:14:00.794672Z
- Finished UTC: 2026-10-22T03:23:52.373644Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Two major findings concern non-graph mechanism claims and a performance endpoint encoded as incubation protocol; one minor finding concerns GTDB provenance. The existing qualified three-node/two-arrow graph is retained. The full recovered supplement adds stage-specific conditions and gene-potential evidence, but the main body remains inaccessible. Eight focused checks pass; completeness80 and raw quality106.33333333333331(capped100) do not certify scientific completion.

## Scope And Provenance

Whole target, fresh Abstract, complete recovered supplement and all four SI figures plus graphical abstract; bounded publisher-indexed main preview and current authority/provenance checks.

Selection: Only released CommunityMech:000297 in owned batch14 checkout.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e117e3d37c65bfad2e04af53ab34e1325d8d7f98.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000297 | kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml | maintained | DIET-based Simplified Lignocellulose-to-Methane Consortia (DIETsimp) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000297 | Actual native exit0. |
| validate-strict | passed | True | CommunityMech:000297 | Actual native exit0. |
| validate-terms | passed | True | CommunityMech:000297 | Actual native exit0. |
| validate-references-explained | passed | True | CommunityMech:000297 | Actual native exit0. |
| validate-gtdb | passed | True | CommunityMech:000297 | Actual native exit0. |
| validate-gtdb-domain | passed | True | CommunityMech:000297 | Actual native exit0. |
| validate-history | passed | True | CommunityMech:000297 | Actual native exit0. |
| normalize-cache-names-check | passed | True | CommunityMech:000297 | Actual native exit0. |
| audit-network corpus context | failed | False | CommunityMech:000297 | Actual corpus exit1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000297 | Actual corpus exit1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000297 | Unavailable in owned runtime. |

## Scientific And Domain Assessments

### Two enriched consortia and prominent taxa

identity: supported. Targets: CommunityMech:000297.

Retain the two top-down consortia, engineered origin/state and source-attributed prominent species.

CMPS and CMMS are distinct inoculum-derived communities, not an exactly three-member isolated co-culture. Preserve source C.aceticum/current Andreesenella acetica synonym grounding. Additional annotated taxa and the graphical-abstract D.desulfuricans example do not automatically redefine the roster.

### Proposed S. globosa to M. mazei DIET Syntrophy

graph: supported. Targets: CommunityMech:000297.

Retain proposed S.globosa-to-M.mazei syntrophy with PARTIAL/OTHER support.

Exact selector ecological_interactions[0]; name Proposed S. globosa to M. mazei DIET Syntrophy; scope PAIRWISE; interaction_type SYNTROPHY. Encoded taxa: {"source": {"preferred_term": "Sphaerochaeta globosa", "term": {"id": "NCBITaxon:1131703", "label": "Sphaerochaeta globosa"}}, "target": {"preferred_term": "Methanosarcina mazei", "term": {"id": "NCBITaxon:2209", "label": "Methanosarcina mazei"}}, "participants": []}. Canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "a36d934591136cfd8acc085985cbdb3444198b922b2ba40d4dc41f64c8ba4204", "reference": "PMID:42229598", "supports": "PARTIAL", "evidence_source": "OTHER"}]. Snippet audit SHA256 7af8baf0c71d5211af65ac595c541c9fd4639e047db89f13dda158fa32591c38. PMID:42229598 Abstract eighth sentence; supplementary TextsS1–S3 and TablesS4/S5. Intermediate-metabolism assignments and community electrochemistry support plausibility, not donor-specific electrons or exclusion of hydrogen/formate.

### Proposed donor contribution to intrinsic methanogenesis

graph: supported. Targets: CommunityMech:000297.

Retain this parallel HYPOTHESIZED arrow at its existing qualified tier.

Exact selector ecological_interactions[0].downstream[0]; source node Proposed S. globosa to M. mazei DIET Syntrophy; actual target Proposed M. mazei CO2 Reduction to Methane; description HYPOTHESIZED - direct electron delivery by Sphaerochaeta globosa could supply reducing equivalents for the proposed M. mazei CO2-to-methane step. The available abstract proposes this contribution but does not trace donor-specific electrons, establish the carrier, or selectively perturb that route; this arrow does not assert a dependency between the two bacterial donors.; description SHA256 0b2aa63dfefe501e7ac6e6f31f967a3e6f9f2c3daabd15f361bc3bba5dfabd69. Supporting source: PMID:42229598 Abstract eighth sentence, with whole-community support in TextsS1–S3. No separate edge experiment or donor-to-donor dependency is asserted.

### Proposed C. aceticum to M. mazei DIET Syntrophy

graph: supported. Targets: CommunityMech:000297.

Retain proposed C.aceticum-to-M.mazei syntrophy with PARTIAL/OTHER support.

Exact selector ecological_interactions[1]; name Proposed C. aceticum to M. mazei DIET Syntrophy; scope PAIRWISE; interaction_type SYNTROPHY. Encoded taxa: {"source": {"preferred_term": "Clostridium aceticum", "term": {"id": "NCBITaxon:84022", "label": "Andreesenella acetica"}}, "target": {"preferred_term": "Methanosarcina mazei", "term": {"id": "NCBITaxon:2209", "label": "Methanosarcina mazei"}}, "participants": []}. Canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "a36d934591136cfd8acc085985cbdb3444198b922b2ba40d4dc41f64c8ba4204", "reference": "PMID:42229598", "supports": "PARTIAL", "evidence_source": "OTHER"}]. Snippet audit SHA256 7af8baf0c71d5211af65ac595c541c9fd4639e047db89f13dda158fa32591c38. PMID:42229598 Abstract eighth sentence; supplementary TextsS1–S3 and TablesS4/S5. C.aceticum CAZyme potential strengthens capability evidence but does not trace electron transfer to the methanogen.

### Proposed donor contribution to intrinsic methanogenesis

graph: supported. Targets: CommunityMech:000297.

Retain this parallel HYPOTHESIZED arrow at its existing qualified tier.

Exact selector ecological_interactions[1].downstream[0]; source node Proposed C. aceticum to M. mazei DIET Syntrophy; actual target Proposed M. mazei CO2 Reduction to Methane; description HYPOTHESIZED - direct electron delivery by Clostridium aceticum (Andreesenella acetica) could supply reducing equivalents for the proposed M. mazei CO2-to-methane step. The available abstract proposes this contribution but does not trace donor-specific electrons, establish the carrier, or selectively perturb that route; this arrow does not assert a dependency between the two bacterial donors.; description SHA256 2b30b019cf0f111074e53c826ff2e54572c9a22011b4d938cd20d1b29b537b3f. Supporting source: PMID:42229598 Abstract eighth sentence, with whole-community support in TextsS1–S3. No separate edge experiment or donor-to-donor dependency is asserted.

### Proposed M. mazei CO2 Reduction to Methane

graph: supported. Targets: CommunityMech:000297.

Retain the untyped intrinsic M.mazei CO2-to-methane step and separate community conductivity evidence.

Exact selector ecological_interactions[2]; name Proposed M. mazei CO2 Reduction to Methane; scope PAIRWISE; interaction_type untyped. Encoded taxa: {"source": {"preferred_term": "Methanosarcina mazei", "term": {"id": "NCBITaxon:2209", "label": "Methanosarcina mazei"}}, "target": null, "participants": []}. Canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "049bbe2ee2ba55e5a6091167223e5de21ec80291f13963acf536c3361074d372", "reference": "PMID:42229598", "supports": "PARTIAL", "evidence_source": "OTHER"}, {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "b23ad9cfd37391de3577b6370d39ae9f53640e43945e9c0c536bd04f587c5848", "reference": "PMID:42229598", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 7af8baf0c71d5211af65ac595c541c9fd4639e047db89f13dda158fa32591c38. PMID:42229598 Abstract fifth sentence (conductivity) and eighth sentence (proposed pathway); supplementary Texts S1–S3 and Tables S4/S5. Retain PARTIAL/OTHER for the proposed pathway and PARTIAL/IN_VITRO for whole-community conductivity. The source-only PAIRWISE node is valid; no artificial target or syntrophic interaction type is needed.

### Non-graph claims and member-role support

evidence: concern. Targets: CommunityMech:000297.

Description, taxon notes and hard roles need the same proposed/potential scope already present in the graph.

Distinguish taxonomy abundance from role evidence. C.aceticum degradation potential is supported by annotation; S.globosa complex-substrate degradation needs claim-local support. Do not convert community electrode observations into individual ELECTROGEN assays, or require universal obligacy to retain a proposed syntrophy.

### Performance endpoint and optimization stages

completeness: concern. Targets: CommunityMech:000297.

The15–16day performance period is not a universal incubation setting; actual stage conditions are recoverable.

Keep100mL as working volume,37°C/120rpm within the optimization arm, and initial pH as a measurement. The existing abstract-access note is historically scoped but current curation can now incorporate the supplement. No complete basal recipe, headspace composition or original selection protocol is inferred.

### Stable identities and mapping provenance

grounding: concern. Targets: CommunityMech:000297.

All current ontology labels and GTDB cores reproduce; latest/build-date provenance does not.

Qualitative dominance remains source-attributed without invented percentages. No forced isolate/strain inference, chemical stereoform replacement or named-species expansion.

### Available source traceability

provenance: supported. Targets: CommunityMech:000297.

Publication and supplement identities agree; no distinct resource defect was established.

Collection locations are preview-only enrichment leads. EC/KO identifiers and supplement bibliography are background/annotation classes, not verified focal sequence deposits.

### Maintained record and preserved history

ownership: supported. Targets: CommunityMech:000297.

All repairs belong to the focal maintained YAML.

Preserve prior graph edits, source/cache bytes and dated histories. Open issue1373 is context for the two major findings; no issue mutation or source-status promotion is performed.

### Focused checks and source limits

schema: supported. Targets: CommunityMech:000297.

All eight focused checks pass; corpus failures and adapter limits remain explicit.

### Two literal native scores

completeness: supported. Targets: CommunityMech:000297.

Completeness80; raw quality106.33333333333331, capped100.

## Findings

### mechanism-scope: Qualify non-graph mechanism and role assertions

major / open / confirmed; issue key: cm-000297-mechanism-scope.

The opening DIET claim, taxon notes and hard functional roles imply stronger member-specific mechanism support than the proposed pathway. Whole-community electrochemistry and pooled metagenomic annotations are positive but do not independently resolve each species’ electron flux. Preserve the qualified graph and supported gene potential.

### performance-protocol: Separate methane performance from incubation protocol

major / open / confirmed; issue key: cm-000297-performance-protocol.

growth_media encodes15–16days and explicitly calls that an incubation period, although the Abstract reports a performance endpoint and supplement TextS4 tests distinct durations and optimization stages. Recover available settings with their stage-specific scope.

### gtdb-provenance: Correct release and build-date provenance

minor / open / confirmed; issue key: cm-000297-gtdb-provenance.

All three mapping_source strings call the snapshot latest and use its filesystem modification date as a build date. Exact species mappings are valid; those provenance claims are not established.

## Recommended Actions And Acceptance Checks

### qualify-mechanism

Align non-graph assertions with the supported proposed model.

- Qualify the opening DIET mechanism and each taxon note as proposed/inferred. Preserve measured methane performance, community conductivity and cytochrome-associated spectra; do not present gene abundance as measured activity or flux.
- Attach member-specific evidence to each retained functional_role. Preserve C.aceticum degradation potential from TextS3/TablesS4–S5 as computational annotation; S.globosa has intermediate-metabolism support but its optional complex-substrate role needs source-local justification or qualification. Do not require polymer-only degradation or claim incapability.
- Use the literal ELECTROGEN solid-acceptor definition and distinguish whole-consortium electrode coatings from individual species assays. Qualify donor/acceptor/electrotroph/syntrophic roles as proposed where direct assignment is unresolved. No mandatory reciprocal-benefit or obligacy test is introduced.
- Retain all three nodes, four evidence excerpts and both parallel HYPOTHESIZED arrows. Keep PARTIAL/OTHER for the proposed pathway and PARTIAL/IN_VITRO for community conductivity; no forced target for the intrinsic source-only node. Retain the open mechanistic discussion and alternative-carrier uncertainty.

### recover-culture

Represent reported performance and distinct cultivation stages accurately.

- Keep approximately15–16days and32mL/gVS·d as reported methane-performance outcomes, with25–40days and10–25mL/gVS·d identified as present-level/literature comparisons, not matched controlled protocol. Remove the unsupported universal incubation interpretation from the structured time and its evidence explanation.
- Add TextS4 optimization-stage anaerobic flasks,100mL working volume,37°C and120rpm with exact source evidence. Do not invent vessel capacity, gas mixture, basal medium, pressure or a universal original enrichment protocol.
- Preserve sequential OFAT design: C/N1.1,2.2,4.4,6.6,8.8 at30%inoculum and15days; then1,5,10,15,30%inoculum at the selected C/N; then10,15,20,25,30days with optimized preceding factors. Keep BBD TableS2 levels separate and do not promote an unverified optimum.
- Treat TableS1 initial pH7.62±0.14(CMMS) and7.25±0.11(CMPS) as measurements, not setpoints. Keep analytical PBS/Nafion/ferricyanide and room temperature out of the culture recipe; TableS3 belongs to other studies.
- Update current source-availability notes to acknowledge the recovered supplement while preserving the unavailable main-body limitation and dated history. Any collection-location enrichment must identify the limited publisher-indexed preview tier and preserve the two inoculum-derived consortia.

### repair-gtdb

Retain valid species mappings with actual snapshot provenance.

- Keep GROUNDED species mappings for NCBITaxon2209,1131703,84022 with majority1.0 and197/1/6 reference genomes respectively; preserve source Clostridium aceticum/current Andreesenella acetica synonym scope.
- Record the actual NCBI2GTDB.tsv.gz SHA256761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd and exact ncbi_id route. Identify2026-07-25T23:28:31Z only as filesystem mtime, not latest release or build date. is_reclassified is a name comparison, not study-strain identification.

### validate-future-curation

Validate any separately authorized repair.

- Recheck all exact excerpts and the three-node/two-arrow source scope, then run focused schema/strict/term/reference/GTDB/domain/history checks.
- After authorized curation run just gen-html and just check-docs-current, preserve existing source/cache/history bytes and add append-only curation provenance. This review makes no canonical, generated-page, Git or issue changes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml; Whole maintained YAML | supports | Two inoculum-derived DIETsimp consortia, three prominent taxa and three qualified pathway nodes; the maintained YAML owns future repairs. |
| publication | PMID:42229598; DOI:10.1016/j.biortech.2026.135043; Complete fresh MED identity and Abstract | supports | The DOI, PMID and title agree with the recovered publisher supplement. No PMCID is reported. Direct main-body routes remain inaccessible; this is a bounded access result, not global absence. |
| pathway | PMID:42229598; DOI:10.1016/j.biortech.2026.135043; Abstract, eighth sentence beginning The potential DIET-based methanogenic pathway | supports | The authors propose a pathway involving the two bacterial taxa and M.mazei. This supports the existing hypotheses, not species-resolved transfer measurements. |
| performance | PMID:42229598; DOI:10.1016/j.biortech.2026.135043; Abstract, third through seventh sentences | supports | Top-down selection produced two consortia. The reported approximately15–16day methanogenesis period and32mL/gVS·d rate are performance outcomes;25–40days and10–25mL/gVS·d are present-level comparators. Conductivity and cytochrome-associated spectra are whole-community observations. |
| electrochemistry | PMID:42229598; DOI:10.1016/j.biortech.2026.135043; Supplement Text S1 Measurement of Electron Transfer Coefficient (ETC), sole assay paragraph; Text S2 Measurement of Scanning Electrochemical Microscopy (SECM) and Electrochemical Fourier Transform Infrared Spectroscopy (E-FTIR), both assay paragraphs; Figure S2 | supports | Washed community suspensions coat electrodes for CV, SECM and E-FTIR. These are positive community-level measurements. They do not independently assign solid-acceptor transfer or electron uptake to each species. PBS, Nafion and ferricyanide are analytical reagents, not culture ingredients. |
| genes | PMID:42229598; DOI:10.1016/j.biortech.2026.135043; Supplement Text S3 Metagenomic sequencing and analysis, both method paragraphs; Tables S4 and S5; Figures S3 and S4 | supports | DNA from three pooled biological replicates/group was sequenced and annotated. C.aceticum has xylan/arabinoxylan-associated assignments and S4 beta-glucosidases; S.globosa rows support intermediate metabolism. Other taxa carry hydrolytic and methanogenic assignments. These are predicted capabilities and gene abundances, not measured enzyme activity, transcription or taxon-specific flux. |
| culture | PMID:42229598; DOI:10.1016/j.biortech.2026.135043; Supplement Text S4 Single-factor experiments and their corresponding levels, sole method paragraph; Tables S1 and S2 | supports | Optimization experiments use anaerobic flasks with100mL working volume at37°C and120rpm. Sequential C/N, inoculum and duration tests are distinct stages. Initial measured pH7.62±0.14(CMMS) and7.25±0.11(CMPS) in TableS1 are not controlled setpoints. |
| optimization | PMID:42229598; DOI:10.1016/j.biortech.2026.135043; Supplement Text S4 Single-factor experiments and their corresponding levels, sole method paragraph; Tables S2, S3, S6, S7 and S8; Figure S1 | supports | Box–Behnken levels span inoculum5/10/15%, C/N2.2/4.4/6.6 and10/15/20days. OFAT duration tests instead span10–30days. TableS3 compares other studies and cannot supply a focal medium recipe; model fits and initial-mixture curves do not convert the abstract endpoint into a universal protocol. |
| preview | PMID:42229598; DOI:10.1016/j.biortech.2026.135043; Publisher-indexed focal result: Sample collection, short Performance and Conclusions excerpts; complete focal Introduction | supports | The indexed preview gives collection-location leads and reports no significant T5-to-T6 performance difference. It is not full Methods/Results. Those locations may be added with this limited source tier, without filling missing medium or selection details. |
| ontology | /private/tmp/cm-review-session/batch-14/000297/ontology-authority.json; 11 ID-label pairs and24 placements | supports | All labels match, including source Clostridium aceticum as a synonym of current Andreesenella acetica. Environment and chemical terms remain valid at the encoded scope. |
| schema | /private/tmp/cm-review-session/batch-14/000297/child-schema-semantics.json; Literal role and interaction definitions | supports | ELECTROGEN requires transfer to a solid extracellular acceptor; generic electroactivity is insufficient. PAIRWISE requires a source but not invariably a target. No polymer-only degrader or universal obligacy rule is imposed. |
| gtdb | /private/tmp/cm-review-session/batch-14/000297/child-gtdb-crosswalk.json; Three exact-ID resolutions and snapshot provenance | supports | Current species mappings reproduce at majority1.0 over197,1 and6 reference genomes. Filesystem mtime is not a release or build date; reference mappings do not identify individual study strains. |
| semantics | /private/tmp/cm-review-session/batch-14/000297/ontology-semantic-notes.json; Final source/ontology reconciliation | supports | Preserve positive gene-supported potential and whole-community assays while qualifying hard species-role claims. Keep the parallel proposed graph and separate culture stages. |
| resources | /private/tmp/cm-review-session/batch-14/000297/dataset-verification.json; Bounded available-source resource search | supports | Whole available supplement and abstract/preview contain no concrete study archive accession. EC/KO classes and background references are not study deposits. No resource finding or absence claim for unread main text. |
| snippets | /private/tmp/cm-review-session/batch-14/000297/snippet-audit.json; All11 canonical excerpt placements | supports | Eight match raw fresh MED and three require explicit CO subscript rendering to CO2; all11 match the cache. Text matching does not establish causal entailment. |
| rendering | /private/tmp/cm-review-session/batch-14/000297/snippet-rendering-projection.json; Exact source superscript/subscript rendering | supports | The three CO2 projections preserve source wording while removing HTML subscript markup; they are not raw-string matches. |
| provenance | /private/tmp/cm-review-session/batch-14/000297/provenance-audit.json; Whole history/cache, exact batch28records[3], cohort and current issues | supports | Prior graph repairs and open issue1373 remain context. Fresh supplementary recovery updates present access without rewriting the dated historical limitation. |
| inspection | /private/tmp/cm-review-session/batch-14/000297/inspect.json; 30 immutable official inputs | supports | Ignored-inclusive discovery bound eight focal contexts plus21authorities and the target; generic corpus/build mentions were discovery-only. |
| assets | /private/tmp/cm-review-session/batch-14/000297/lead-source-assets.json; Actual access attempts and recovered assets | supports | Main body unavailable; full matched supplementary DOCX, four SI figures and graphical abstract recovered and read. Original failed requests remain preserved. |
| lead-read | /private/tmp/cm-review-session/batch-14/000297/lead-primary-read-scope.json; Actual whole and bounded source reading | supports | Whole supplement text/tables and all four figures were read. S1/S3/S4 used a white display canvas for transparent labels; no data reanalysis or image-value change. |
| locators | /private/tmp/cm-review-session/batch-14/000297/source-locator-verification.json; Direct MED sentence and DOCX heading/table checks | supports | Every candidate source locator refers to inspected Abstract text or actual supplementary labels, not invented main section numbers. |
| source-scope | /private/tmp/cm-review-session/batch-14/000297/source-audit.json; Final lead findings | supports | Two major findings concern non-graph mechanism scope and performance-versus-protocol; one minor concerns GTDB provenance. Main-body access remains incomplete. |
| selector-clarification | /private/tmp/cm-review-session/batch-14/000297/source-selector-clarification.json; Exact frozen scratch selector erratum | supports | The canonical field is growth_media[0].preparation_notes; the original source audit is preserved and this candidate uses the actual selector. |
| root-source | /private/tmp/cm-review-session/batch-14/000297/root-independent-source-audit.json; Independent root source judgment | supports | Root independently read the available sources and figures and agreed the final scope/findings. |
| metrics | /private/tmp/cm-review-session/batch-14/000297/support-final-audit.json; Final support and native arithmetic | supports | Completeness80; base128.33333333333331 minus20 for two major and2 for one minor equals106.33333333333331 raw, capped100. Scores do not certify scientific completion. |
| support-manifest | /private/tmp/cm-review-session/batch-14/000297/supporting-artifact-manifest.json; Frozen supporting inputs | supports | Final support follows independent source, authority and provenance reconciliation; preliminary receipts remain unchanged. |
| auxiliary | /private/tmp/cm-review-session/batch-14/000297/auxiliary-frozen-manifest.json; Frozen authority/native outputs | supports | Eight focused checks pass and all30 official inputs remain unchanged. |
| final-native | /private/tmp/cm-review-session/batch-14/000297/final-validator-summary.json; Eight actual command/stdout/stderr outcomes | supports | Focused checks pass; zero reference issues is a native diagnostic, not a measure of mechanistic certainty. |
| corpus-context | /private/tmp/cm-review-session/batch-14/000297/child-current-corpus-context.json; Actual batch14 corpus baseline | supports | Both corpus commands exited1 with44warnings across16/477records and zero errors; nonrequired context. |
| adapter | /private/tmp/cm-review-session/batch-14/000297/adapter-check.json; Optional adapter in owned runtime | supports | Unavailable; no external-checkout adapter was executed. |
| check-validate | /private/tmp/cm-review-session/batch-14/000297/validate.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-14/000297/validate-strict.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-14/000297/validate-terms.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-14/000297/validate-references-explained.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-14/000297/validate-gtdb.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-14/000297/validate-gtdb-domain.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-14/000297/validate-history.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-14/000297/normalize-cache-names-check.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-14/audit-network.json; Actual batch14 corpus baseline | supports | Exit1,44warnings across16/477records and zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-14/check-network-quality.json; Actual batch14 corpus baseline | supports | Exit1,44warnings across16/477records and zero errors. |

## Limits And Additional Notes

- The complete main Methods, Results and Discussion and ordinary main figures remain unavailable through the bounded public routes. Indexed excerpts are not full-text access. No global absence of direct mechanistic experiments or archive deposits is asserted.
- The PII-matched recovered supplement has verified title/authors, four Texts, eight Tables and four true images. Its package does not establish an exhaustive publisher asset inventory. A ZIP directory entry was excluded from image counts; source bytes remain unchanged.
- Metagenomic DNA pooled three biological replicates per group. Annotation tables and FiguresS3/S4 represent potential and gene abundance, not transcription, enzyme activity, donor-resolved electron flux or an exhaustive three-species community.
- The graphical abstract uses D.desulfuricans among bacterial examples while the Abstract focuses C.aceticum. Preserve source/figure scope without replacing the encoded taxa. TextS2 electrode wording and supplementary rate/yield/CMMP terminology differ internally; these unencoded details were not silently harmonized.
- No raw sequence, optimization rerun or other-study recipe transfer was performed. TableS3 comparisons and analytical electrolytes are not focal cultivation conditions.
- All30 official input hashes remain unchanged. Three node assessments bind four exact canonical snippets; two arrow assessments bind actual endpoints/descriptions. Sole quotation: two words from the fresh Abstract.
- Candidate validation and parent save/post-save gates occur separately; no future pass is asserted.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T032352Z-dietsimp-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: DIETsimp lignocellulose-to-methane record review
started_at: '2026-10-22T03:14:00.794672Z'
finished_at: '2026-10-22T03:23:52.373644Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, support and auxiliary reviewers; no person-level
    independence claim.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: Two major findings concern non-graph mechanism claims and a performance endpoint
  encoded as incubation protocol; one minor finding concerns GTDB provenance. The
  existing qualified three-node/two-arrow graph is retained. The full recovered supplement
  adds stage-specific conditions and gene-potential evidence, but the main body remains
  inaccessible. Eight focused checks pass; completeness80 and raw quality106.33333333333331(capped100)
  do not certify scientific completion.
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
  - path: history/records/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia/2026-10-06T045256Z-codex-a98f56.yaml
    sha256: a2a74ca2516439d5ff72c5c723afa000de1e2a103d0f2828bcd2c21bc633e392
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
    sha256: 41e06f6c3fa5433a002180badb92870c4664a3863c394d4c7d25acf38a23a3be
    role: target
  - path: references_cache/PMID_42229598.md
    sha256: 8342a4ca3213eb3c7c9b2a14d8f1fce90c70fd37aae9270987ffeb7cd5247bb3
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
- target_id: CommunityMech:000297
  path: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
  label: DIET-based Simplified Lignocellulose-to-Methane Consortia (DIETsimp)
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
    role: canonical_record
scope:
  description: Whole target, fresh Abstract, complete recovered supplement and all
    four SI figures plus graphical abstract; bounded publisher-indexed main preview
    and current authority/provenance checks.
  selection: Only released CommunityMech:000297 in owned batch14 checkout.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000297
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000297
  command: just --no-dotenv validate kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000297
  command: just --no-dotenv validate-strict kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
    --out /private/tmp/cm-review-session/batch-14/000297/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000297
  command: just --no-dotenv validate-terms kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000297
  command: just --no-dotenv validate-references-explained kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000297
  command: just --no-dotenv validate-gtdb kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000297
  command: just --no-dotenv validate-gtdb-domain kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000297
  command: just --no-dotenv validate-history history/records/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000297
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
  summary: Actual corpus exit1 retained.
  target_ids:
  - CommunityMech:000297
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, not wholly attributed to this target.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit1 retained.
  target_ids:
  - CommunityMech:000297
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, not wholly attributed to this target.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in owned runtime.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - adapter
  scope_note: No external-checkout adapter execution.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
  locator: Whole maintained YAML
  summary: Two inoculum-derived DIETsimp consortia, three prominent taxa and three
    qualified pathway nodes; the maintained YAML owns future repairs.
  support: supports
  accessed_at: '2026-10-22T03:21:58.850389Z'
- evidence_id: publication
  kind: database
  reference: PMID:42229598; DOI:10.1016/j.biortech.2026.135043
  locator: Complete fresh MED identity and Abstract
  summary: The DOI, PMID and title agree with the recovered publisher supplement.
    No PMCID is reported. Direct main-body routes remain inaccessible; this is a bounded
    access result, not global absence.
  support: supports
  accessed_at: '2026-10-22T03:21:58.850444Z'
  snapshot_sha256: f71a1d122adbd4cab269e367b48c7c09174ee3652f65b0939cf7585d147a5acd
- evidence_id: pathway
  kind: primary_source
  reference: PMID:42229598; DOI:10.1016/j.biortech.2026.135043
  locator: Abstract, eighth sentence beginning The potential DIET-based methanogenic
    pathway
  summary: The authors propose a pathway involving the two bacterial taxa and M.mazei.
    This supports the existing hypotheses, not species-resolved transfer measurements.
  support: supports
  accessed_at: '2026-10-22T03:21:58.850474Z'
  snapshot_sha256: f71a1d122adbd4cab269e367b48c7c09174ee3652f65b0939cf7585d147a5acd
  quote: was proposed
- evidence_id: performance
  kind: primary_source
  reference: PMID:42229598; DOI:10.1016/j.biortech.2026.135043
  locator: Abstract, third through seventh sentences
  summary: Top-down selection produced two consortia. The reported approximately15–16day
    methanogenesis period and32mL/gVS·d rate are performance outcomes;25–40days and10–25mL/gVS·d
    are present-level comparators. Conductivity and cytochrome-associated spectra
    are whole-community observations.
  support: supports
  accessed_at: '2026-10-22T03:21:58.850493Z'
  snapshot_sha256: f71a1d122adbd4cab269e367b48c7c09174ee3652f65b0939cf7585d147a5acd
- evidence_id: electrochemistry
  kind: primary_source
  reference: PMID:42229598; DOI:10.1016/j.biortech.2026.135043
  locator: Supplement Text S1 Measurement of Electron Transfer Coefficient (ETC),
    sole assay paragraph; Text S2 Measurement of Scanning Electrochemical Microscopy
    (SECM) and Electrochemical Fourier Transform Infrared Spectroscopy (E-FTIR), both
    assay paragraphs; Figure S2
  summary: Washed community suspensions coat electrodes for CV, SECM and E-FTIR. These
    are positive community-level measurements. They do not independently assign solid-acceptor
    transfer or electron uptake to each species. PBS, Nafion and ferricyanide are
    analytical reagents, not culture ingredients.
  support: supports
  accessed_at: '2026-10-22T03:21:58.850512Z'
  snapshot_sha256: f013a4c0eb1ed3402168abbc2438379bbe16b100669126d7bd5c65c1bd8df720
- evidence_id: genes
  kind: primary_source
  reference: PMID:42229598; DOI:10.1016/j.biortech.2026.135043
  locator: Supplement Text S3 Metagenomic sequencing and analysis, both method paragraphs;
    Tables S4 and S5; Figures S3 and S4
  summary: DNA from three pooled biological replicates/group was sequenced and annotated.
    C.aceticum has xylan/arabinoxylan-associated assignments and S4 beta-glucosidases;
    S.globosa rows support intermediate metabolism. Other taxa carry hydrolytic and
    methanogenic assignments. These are predicted capabilities and gene abundances,
    not measured enzyme activity, transcription or taxon-specific flux.
  support: supports
  accessed_at: '2026-10-22T03:21:58.851710Z'
  snapshot_sha256: f013a4c0eb1ed3402168abbc2438379bbe16b100669126d7bd5c65c1bd8df720
- evidence_id: culture
  kind: primary_source
  reference: PMID:42229598; DOI:10.1016/j.biortech.2026.135043
  locator: Supplement Text S4 Single-factor experiments and their corresponding levels,
    sole method paragraph; Tables S1 and S2
  summary: Optimization experiments use anaerobic flasks with100mL working volume
    at37°C and120rpm. Sequential C/N, inoculum and duration tests are distinct stages.
    Initial measured pH7.62±0.14(CMMS) and7.25±0.11(CMPS) in TableS1 are not controlled
    setpoints.
  support: supports
  accessed_at: '2026-10-22T03:21:58.852742Z'
  snapshot_sha256: f013a4c0eb1ed3402168abbc2438379bbe16b100669126d7bd5c65c1bd8df720
- evidence_id: optimization
  kind: primary_source
  reference: PMID:42229598; DOI:10.1016/j.biortech.2026.135043
  locator: Supplement Text S4 Single-factor experiments and their corresponding levels,
    sole method paragraph; Tables S2, S3, S6, S7 and S8; Figure S1
  summary: Box–Behnken levels span inoculum5/10/15%, C/N2.2/4.4/6.6 and10/15/20days.
    OFAT duration tests instead span10–30days. TableS3 compares other studies and
    cannot supply a focal medium recipe; model fits and initial-mixture curves do
    not convert the abstract endpoint into a universal protocol.
  support: supports
  accessed_at: '2026-10-22T03:21:58.853755Z'
  snapshot_sha256: f013a4c0eb1ed3402168abbc2438379bbe16b100669126d7bd5c65c1bd8df720
- evidence_id: preview
  kind: primary_source
  reference: PMID:42229598; DOI:10.1016/j.biortech.2026.135043
  locator: 'Publisher-indexed focal result: Sample collection, short Performance and
    Conclusions excerpts; complete focal Introduction'
  summary: The indexed preview gives collection-location leads and reports no significant
    T5-to-T6 performance difference. It is not full Methods/Results. Those locations
    may be added with this limited source tier, without filling missing medium or
    selection details.
  support: supports
  accessed_at: '2026-10-22T03:21:58.854816Z'
  snapshot_sha256: 0fc0ab0d7f9d73ce27f8019e274430c3444da6927c7e94c5df63b99eca1348ea
  search_scope: Bounded exact DOI/title publisher search and ordinary direct HTML/abstract/API
    routes. Only the focal indexed result was read; other hits excluded. Direct publisher
    responses were403, so no successful full-page access is claimed.
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000297/ontology-authority.json
  locator: 11 ID-label pairs and24 placements
  summary: All labels match, including source Clostridium aceticum as a synonym of
    current Andreesenella acetica. Environment and chemical terms remain valid at
    the encoded scope.
  support: supports
  accessed_at: '2026-10-22T03:21:58.854902Z'
  snapshot_sha256: 939ce37d1daf046990b06592ba2ac973e74dd0025331df11e9d103d75632e7ed
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000297/child-schema-semantics.json
  locator: Literal role and interaction definitions
  summary: ELECTROGEN requires transfer to a solid extracellular acceptor; generic
    electroactivity is insufficient. PAIRWISE requires a source but not invariably
    a target. No polymer-only degrader or universal obligacy rule is imposed.
  support: supports
  accessed_at: '2026-10-22T03:21:58.854948Z'
  snapshot_sha256: c2fc814d4e8840f79c012dbe14669425d5fc72cebfc3481ed6493e255ec1a455
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000297/child-gtdb-crosswalk.json
  locator: Three exact-ID resolutions and snapshot provenance
  summary: Current species mappings reproduce at majority1.0 over197,1 and6 reference
    genomes. Filesystem mtime is not a release or build date; reference mappings do
    not identify individual study strains.
  support: supports
  accessed_at: '2026-10-22T03:21:58.854986Z'
  snapshot_sha256: ac37ed2261e6c126dc8af072d805c43f7f2f162c0d1e7e20c7019746b0ad71c7
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000297/ontology-semantic-notes.json
  locator: Final source/ontology reconciliation
  summary: Preserve positive gene-supported potential and whole-community assays while
    qualifying hard species-role claims. Keep the parallel proposed graph and separate
    culture stages.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855021Z'
  snapshot_sha256: 37a592679a95039bd3878c547b1b62d312a97e9615b2d2c5321b860c0889ec18
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/dataset-verification.json
  locator: Bounded available-source resource search
  summary: Whole available supplement and abstract/preview contain no concrete study
    archive accession. EC/KO classes and background references are not study deposits.
    No resource finding or absence claim for unread main text.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855057Z'
  snapshot_sha256: 8e628e651d08d78d5dc4173b77e826f40a72f97e682a4d62563fcf30683c2e29
  search_scope: Bounded fresh MED, focal publisher preview and whole recovered supplement;
    no main-body absence claim and no broad archive search.
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/snippet-audit.json
  locator: All11 canonical excerpt placements
  summary: Eight match raw fresh MED and three require explicit CO subscript rendering
    to CO2; all11 match the cache. Text matching does not establish causal entailment.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855092Z'
  snapshot_sha256: 7af8baf0c71d5211af65ac595c541c9fd4639e047db89f13dda158fa32591c38
- evidence_id: rendering
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/snippet-rendering-projection.json
  locator: Exact source superscript/subscript rendering
  summary: The three CO2 projections preserve source wording while removing HTML subscript
    markup; they are not raw-string matches.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855128Z'
  snapshot_sha256: 928e96ab806a79d96c17b040c850020f4afe7c171dfe3d62e4607033a2114bf0
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-14/000297/provenance-audit.json
  locator: Whole history/cache, exact batch28records[3], cohort and current issues
  summary: Prior graph repairs and open issue1373 remain context. Fresh supplementary
    recovery updates present access without rewriting the dated historical limitation.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855157Z'
  snapshot_sha256: 5bae697a1408771b0185dc8e920516b71fdc44b34313fa4948806df700781a3b
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/inspect.json
  locator: 30 immutable official inputs
  summary: Ignored-inclusive discovery bound eight focal contexts plus21authorities
    and the target; generic corpus/build mentions were discovery-only.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855190Z'
  snapshot_sha256: 744cb6ba80d02b4ead1486dca7c5060191cd1ef5e749a72d3cb6a8b1e3f91290
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/lead-source-assets.json
  locator: Actual access attempts and recovered assets
  summary: Main body unavailable; full matched supplementary DOCX, four SI figures
    and graphical abstract recovered and read. Original failed requests remain preserved.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855212Z'
  snapshot_sha256: 5b8ed39e2761d2019d2593bdb6828f40b4e75bd076047896f8995ad5272061c1
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/lead-primary-read-scope.json
  locator: Actual whole and bounded source reading
  summary: Whole supplement text/tables and all four figures were read. S1/S3/S4 used
    a white display canvas for transparent labels; no data reanalysis or image-value
    change.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855244Z'
  snapshot_sha256: aa9df18b9fec63593f04f23d66ca8a73cb182016b05524748baa39c5261ac74c
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/source-locator-verification.json
  locator: Direct MED sentence and DOCX heading/table checks
  summary: Every candidate source locator refers to inspected Abstract text or actual
    supplementary labels, not invented main section numbers.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855271Z'
  snapshot_sha256: 55c906919a981eb7799b32341b7a22ae1c9bf825abe06f37435f69c8ad6c3d56
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/source-audit.json
  locator: Final lead findings
  summary: Two major findings concern non-graph mechanism scope and performance-versus-protocol;
    one minor concerns GTDB provenance. Main-body access remains incomplete.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855298Z'
  snapshot_sha256: 773d02c7c997f40846aea5186d1d4812e2c2ecd04f3ab9c82aad582f45816474
- evidence_id: selector-clarification
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/source-selector-clarification.json
  locator: Exact frozen scratch selector erratum
  summary: The canonical field is growth_media[0].preparation_notes; the original
    source audit is preserved and this candidate uses the actual selector.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855325Z'
  snapshot_sha256: d5632e2e701e1f989a38cd7007ac4002cf4128f48922cc0c16c2d69c480c40bd
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/root-independent-source-audit.json
  locator: Independent root source judgment
  summary: Root independently read the available sources and figures and agreed the
    final scope/findings.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855350Z'
  snapshot_sha256: f1b0b88b44d0acc6803b8dc7221d29efa74c7247f896f4293d8a50e8e7990504
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/support-final-audit.json
  locator: Final support and native arithmetic
  summary: Completeness80; base128.33333333333331 minus20 for two major and2 for one
    minor equals106.33333333333331 raw, capped100. Scores do not certify scientific
    completion.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855384Z'
  snapshot_sha256: 53c30a3e9226ecfad8b2174577c6d75585d2b3fc525e2e17c3ba56f1111e915f
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/supporting-artifact-manifest.json
  locator: Frozen supporting inputs
  summary: Final support follows independent source, authority and provenance reconciliation;
    preliminary receipts remain unchanged.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855407Z'
  snapshot_sha256: 613add7907f5448795d5ba920cde3197c121d5470026fd03a990ffcb076ea0f5
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/auxiliary-frozen-manifest.json
  locator: Frozen authority/native outputs
  summary: Eight focused checks pass and all30 official inputs remain unchanged.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855434Z'
  snapshot_sha256: 1b99351fccac9dcc1f3e2a65cb2fb77a45a1dbc6cbc133687e903c9a28f911e0
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/final-validator-summary.json
  locator: Eight actual command/stdout/stderr outcomes
  summary: Focused checks pass; zero reference issues is a native diagnostic, not
    a measure of mechanistic certainty.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855460Z'
  snapshot_sha256: 0cfc0e045c96bfe7d55b073f06b271791c10f935a6a18d442509f407f9f9d5be
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/child-current-corpus-context.json
  locator: Actual batch14 corpus baseline
  summary: Both corpus commands exited1 with44warnings across16/477records and zero
    errors; nonrequired context.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855486Z'
  snapshot_sha256: 54b98519b92c9d1a0e0005f20bc72b45bb6193104a93543fea35ce5c81349366
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/adapter-check.json
  locator: Optional adapter in owned runtime
  summary: Unavailable; no external-checkout adapter was executed.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855512Z'
  snapshot_sha256: fb8486799a2bd6bb8d028d05f7452f9caab477ff573e5214dd94d409c3f3c06b
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/validate.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855702Z'
  snapshot_sha256: 4aa720fc2057991622ede0102c1c686dfcb35d5a715974699f48c853cb0a5705
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/validate-strict.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855753Z'
  snapshot_sha256: 66daceb5f2c815ef299f8f2cdc505f3195a99c1d3070c6fbc5ea7c6c2891f8f8
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/validate-terms.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855799Z'
  snapshot_sha256: ea061cfb607cbcd9b06199f079616ae0d13417512d78cbf1407ea0c0dfedcbe7
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/validate-references-explained.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855844Z'
  snapshot_sha256: 14d1d61e92818e7cbc6733cea92f929c415edf1f34d07ef36f0be42129c02676
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/validate-gtdb.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855887Z'
  snapshot_sha256: 4b36d67482c372bfc6980f5f02f1e3ae54c942ea02f0a66f03b6fdc121443c05
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/validate-gtdb-domain.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855931Z'
  snapshot_sha256: 5e2231e02733cb03b96b60df11238b9333fc4b86b28e38f730f3ec33b6b36515
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/validate-history.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:21:58.855976Z'
  snapshot_sha256: 5cd6ab898e27f671e47417f223d52d086fbab8d585bd4aa28c377699bddd4679
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000297/normalize-cache-names-check.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:21:58.856021Z'
  snapshot_sha256: 4fe66e737bd14ee431ef8166cdb97d92f6717fcde5ed6f9d59cc41d449068f7f
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/audit-network.json
  locator: Actual batch14 corpus baseline
  summary: Exit1,44warnings across16/477records and zero errors.
  support: supports
  accessed_at: '2026-10-22T03:21:58.856093Z'
  snapshot_sha256: 3110e0bb1dbe3ea63b81aea82871ac4adb2915c8fce1d15249422d0f5db266c6
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/check-network-quality.json
  locator: Actual batch14 corpus baseline
  summary: Exit1,44warnings across16/477records and zero errors.
  support: supports
  accessed_at: '2026-10-22T03:21:58.856147Z'
  snapshot_sha256: 18896ef4136601b37550cb5612abc06784abcbf982e4778cbf2b9c10368cb66a
assessments:
- assessment_id: identity
  area: identity
  topic: Two enriched consortia and prominent taxa
  outcome: supported
  summary: Retain the two top-down consortia, engineered origin/state and source-attributed
    prominent species.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - record
  - publication
  - ontology
  - genes
  dimensions:
  - name: community_scope
    value: CMPS and CMMS enriched consortia
    definition: Different soil/sediment mixtures with manure; three encoded taxa are
      prominent members, not exhaustive isolated strains.
    evidence_ids:
    - performance
    - genes
  - name: source_access
    value: Full Abstract and supplement; partial main preview
    definition: Complete main Methods/Results/Discussion and ordinary main figures
      remain unavailable.
    evidence_ids:
    - assets
    - lead-read
  details: CMPS and CMMS are distinct inoculum-derived communities, not an exactly
    three-member isolated co-culture. Preserve source C.aceticum/current Andreesenella
    acetica synonym grounding. Additional annotated taxa and the graphical-abstract
    D.desulfuricans example do not automatically redefine the roster.
- assessment_id: node-0
  area: graph
  topic: Proposed S. globosa to M. mazei DIET Syntrophy
  outcome: supported
  summary: Retain proposed S.globosa-to-M.mazei syntrophy with PARTIAL/OTHER support.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - pathway
  - electrochemistry
  - genes
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[0]; name Proposed S. globosa to
    M. mazei DIET Syntrophy; scope PAIRWISE; interaction_type SYNTROPHY. Encoded taxa:
    {"source": {"preferred_term": "Sphaerochaeta globosa", "term": {"id": "NCBITaxon:1131703",
    "label": "Sphaerochaeta globosa"}}, "target": {"preferred_term": "Methanosarcina
    mazei", "term": {"id": "NCBITaxon:2209", "label": "Methanosarcina mazei"}}, "participants":
    []}. Canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "a36d934591136cfd8acc085985cbdb3444198b922b2ba40d4dc41f64c8ba4204",
    "reference": "PMID:42229598", "supports": "PARTIAL", "evidence_source": "OTHER"}].
    Snippet audit SHA256 7af8baf0c71d5211af65ac595c541c9fd4639e047db89f13dda158fa32591c38.
    PMID:42229598 Abstract eighth sentence; supplementary TextsS1–S3 and TablesS4/S5.
    Intermediate-metabolism assignments and community electrochemistry support plausibility,
    not donor-specific electrons or exclusion of hydrogen/formate.'
- assessment_id: edge-0-0
  area: graph
  topic: Proposed donor contribution to intrinsic methanogenesis
  outcome: supported
  summary: Retain this parallel HYPOTHESIZED arrow at its existing qualified tier.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - pathway
  - electrochemistry
  - genes
  - schema
  details: 'Exact selector ecological_interactions[0].downstream[0]; source node Proposed
    S. globosa to M. mazei DIET Syntrophy; actual target Proposed M. mazei CO2 Reduction
    to Methane; description HYPOTHESIZED - direct electron delivery by Sphaerochaeta
    globosa could supply reducing equivalents for the proposed M. mazei CO2-to-methane
    step. The available abstract proposes this contribution but does not trace donor-specific
    electrons, establish the carrier, or selectively perturb that route; this arrow
    does not assert a dependency between the two bacterial donors.; description SHA256
    0b2aa63dfefe501e7ac6e6f31f967a3e6f9f2c3daabd15f361bc3bba5dfabd69. Supporting source:
    PMID:42229598 Abstract eighth sentence, with whole-community support in TextsS1–S3.
    No separate edge experiment or donor-to-donor dependency is asserted.'
- assessment_id: node-1
  area: graph
  topic: Proposed C. aceticum to M. mazei DIET Syntrophy
  outcome: supported
  summary: Retain proposed C.aceticum-to-M.mazei syntrophy with PARTIAL/OTHER support.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - pathway
  - electrochemistry
  - genes
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[1]; name Proposed C. aceticum to
    M. mazei DIET Syntrophy; scope PAIRWISE; interaction_type SYNTROPHY. Encoded taxa:
    {"source": {"preferred_term": "Clostridium aceticum", "term": {"id": "NCBITaxon:84022",
    "label": "Andreesenella acetica"}}, "target": {"preferred_term": "Methanosarcina
    mazei", "term": {"id": "NCBITaxon:2209", "label": "Methanosarcina mazei"}}, "participants":
    []}. Canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "a36d934591136cfd8acc085985cbdb3444198b922b2ba40d4dc41f64c8ba4204",
    "reference": "PMID:42229598", "supports": "PARTIAL", "evidence_source": "OTHER"}].
    Snippet audit SHA256 7af8baf0c71d5211af65ac595c541c9fd4639e047db89f13dda158fa32591c38.
    PMID:42229598 Abstract eighth sentence; supplementary TextsS1–S3 and TablesS4/S5.
    C.aceticum CAZyme potential strengthens capability evidence but does not trace
    electron transfer to the methanogen.'
- assessment_id: edge-1-0
  area: graph
  topic: Proposed donor contribution to intrinsic methanogenesis
  outcome: supported
  summary: Retain this parallel HYPOTHESIZED arrow at its existing qualified tier.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - pathway
  - electrochemistry
  - genes
  - schema
  details: 'Exact selector ecological_interactions[1].downstream[0]; source node Proposed
    C. aceticum to M. mazei DIET Syntrophy; actual target Proposed M. mazei CO2 Reduction
    to Methane; description HYPOTHESIZED - direct electron delivery by Clostridium
    aceticum (Andreesenella acetica) could supply reducing equivalents for the proposed
    M. mazei CO2-to-methane step. The available abstract proposes this contribution
    but does not trace donor-specific electrons, establish the carrier, or selectively
    perturb that route; this arrow does not assert a dependency between the two bacterial
    donors.; description SHA256 2b30b019cf0f111074e53c826ff2e54572c9a22011b4d938cd20d1b29b537b3f.
    Supporting source: PMID:42229598 Abstract eighth sentence, with whole-community
    support in TextsS1–S3. No separate edge experiment or donor-to-donor dependency
    is asserted.'
- assessment_id: node-2
  area: graph
  topic: Proposed M. mazei CO2 Reduction to Methane
  outcome: supported
  summary: Retain the untyped intrinsic M.mazei CO2-to-methane step and separate community
    conductivity evidence.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - pathway
  - electrochemistry
  - genes
  - snippets
  - schema
  - performance
  details: 'Exact selector ecological_interactions[2]; name Proposed M. mazei CO2
    Reduction to Methane; scope PAIRWISE; interaction_type untyped. Encoded taxa:
    {"source": {"preferred_term": "Methanosarcina mazei", "term": {"id": "NCBITaxon:2209",
    "label": "Methanosarcina mazei"}}, "target": null, "participants": []}. Canonical
    snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet",
    "sha256": "049bbe2ee2ba55e5a6091167223e5de21ec80291f13963acf536c3361074d372",
    "reference": "PMID:42229598", "supports": "PARTIAL", "evidence_source": "OTHER"},
    {"selector": "ecological_interactions[2].evidence[1].snippet", "sha256": "b23ad9cfd37391de3577b6370d39ae9f53640e43945e9c0c536bd04f587c5848",
    "reference": "PMID:42229598", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 7af8baf0c71d5211af65ac595c541c9fd4639e047db89f13dda158fa32591c38.
    PMID:42229598 Abstract fifth sentence (conductivity) and eighth sentence (proposed
    pathway); supplementary Texts S1–S3 and Tables S4/S5. Retain PARTIAL/OTHER for
    the proposed pathway and PARTIAL/IN_VITRO for whole-community conductivity. The
    source-only PAIRWISE node is valid; no artificial target or syntrophic interaction
    type is needed.'
- assessment_id: mechanism
  area: evidence
  topic: Non-graph claims and member-role support
  outcome: concern
  summary: Description, taxon notes and hard roles need the same proposed/potential
    scope already present in the graph.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - pathway
  - electrochemistry
  - genes
  - schema
  - semantics
  details: Distinguish taxonomy abundance from role evidence. C.aceticum degradation
    potential is supported by annotation; S.globosa complex-substrate degradation
    needs claim-local support. Do not convert community electrode observations into
    individual ELECTROGEN assays, or require universal obligacy to retain a proposed
    syntrophy.
- assessment_id: cultivation
  area: completeness
  topic: Performance endpoint and optimization stages
  outcome: concern
  summary: The15–16day performance period is not a universal incubation setting; actual
    stage conditions are recoverable.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - performance
  - culture
  - optimization
  details: Keep100mL as working volume,37°C/120rpm within the optimization arm, and
    initial pH as a measurement. The existing abstract-access note is historically
    scoped but current curation can now incorporate the supplement. No complete basal
    recipe, headspace composition or original selection protocol is inferred.
- assessment_id: grounding
  area: grounding
  topic: Stable identities and mapping provenance
  outcome: concern
  summary: All current ontology labels and GTDB cores reproduce; latest/build-date
    provenance does not.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - ontology
  - gtdb
  - semantics
  details: Qualitative dominance remains source-attributed without invented percentages.
    No forced isolate/strain inference, chemical stereoform replacement or named-species
    expansion.
- assessment_id: resources
  area: provenance
  topic: Available source traceability
  outcome: supported
  summary: Publication and supplement identities agree; no distinct resource defect
    was established.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - publication
  - resources
  - assets
  details: Collection locations are preview-only enrichment leads. EC/KO identifiers
    and supplement bibliography are background/annotation classes, not verified focal
    sequence deposits.
- assessment_id: ownership
  area: ownership
  topic: Maintained record and preserved history
  outcome: supported
  summary: All repairs belong to the focal maintained YAML.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - inspection
  - provenance
  details: Preserve prior graph edits, source/cache bytes and dated histories. Open
    issue1373 is context for the two major findings; no issue mutation or source-status
    promotion is performed.
- assessment_id: native
  area: schema
  topic: Focused checks and source limits
  outcome: supported
  summary: All eight focused checks pass; corpus failures and adapter limits remain
    explicit.
  target_ids:
  - CommunityMech:000297
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
  summary: Completeness80; raw quality106.33333333333331, capped100.
  target_ids:
  - CommunityMech:000297
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields/roles50 + environment5 + at least3nodes10 + growth_media10
      + node metabolites5; no factors threshold, external_resources or associated_datasets
      awards.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 -2major*10 -1minor*2 +20*min(((4evidence/3nodes)/2),1) +15 COMPLETE
      =106.33333333333331 raw, capped100. Two typed nodes and two arrows. Scores do
      not certify scientific completion.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 2
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 1
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
findings:
- finding_id: mechanism-scope
  issue_key: cm-000297-mechanism-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material mismatch between encoded mechanism/protocol and the
    available source evidence.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Qualify non-graph mechanism and role assertions
  description: The opening DIET claim, taxon notes and hard functional roles imply
    stronger member-specific mechanism support than the proposed pathway. Whole-community
    electrochemistry and pooled metagenomic annotations are positive but do not independently
    resolve each species’ electron flux. Preserve the qualified graph and supported
    gene potential.
  target_ids:
  - CommunityMech:000297
  field_paths:
  - description
  - taxonomy[0].functional_role
  - taxonomy[0].taxon_term.notes
  - taxonomy[0].evidence
  - taxonomy[1].functional_role
  - taxonomy[1].taxon_term.notes
  - taxonomy[1].evidence
  - taxonomy[2].functional_role
  - taxonomy[2].taxon_term.notes
  - taxonomy[2].evidence
  evidence_ids:
  - pathway
  - electrochemistry
  - genes
  - schema
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns repair; current issue1373 and historical reports
    remain contextual.
- finding_id: performance-protocol
  issue_key: cm-000297-performance-protocol
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material mismatch between encoded mechanism/protocol and the
    available source evidence.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Separate methane performance from incubation protocol
  description: growth_media encodes15–16days and explicitly calls that an incubation
    period, although the Abstract reports a performance endpoint and supplement TextS4
    tests distinct durations and optimization stages. Recover available settings with
    their stage-specific scope.
  target_ids:
  - CommunityMech:000297
  field_paths:
  - growth_media[0].incubation_time
  - growth_media[0].incubation_time_unit
  - growth_media[0].preparation_notes
  - growth_media[0].evidence[1]
  evidence_ids:
  - performance
  - culture
  - optimization
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns repair; current issue1373 and historical reports
    remain contextual.
- finding_id: gtdb-provenance
  issue_key: cm-000297-gtdb-provenance
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Valid mapping cores retain a bounded provenance defect.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Correct release and build-date provenance
  description: All three mapping_source strings call the snapshot latest and use its
    filesystem modification date as a build date. Exact species mappings are valid;
    those provenance claims are not established.
  target_ids:
  - CommunityMech:000297
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  - taxonomy[2].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns repair; current issue1373 and historical reports
    remain contextual.
actions:
- action_id: qualify-mechanism
  description: Align non-graph assertions with the supported proposed model.
  finding_ids:
  - mechanism-scope
  target_ids:
  - CommunityMech:000297
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
    role: canonical_record
  acceptance_checks:
  - Qualify the opening DIET mechanism and each taxon note as proposed/inferred. Preserve
    measured methane performance, community conductivity and cytochrome-associated
    spectra; do not present gene abundance as measured activity or flux.
  - Attach member-specific evidence to each retained functional_role. Preserve C.aceticum
    degradation potential from TextS3/TablesS4–S5 as computational annotation; S.globosa
    has intermediate-metabolism support but its optional complex-substrate role needs
    source-local justification or qualification. Do not require polymer-only degradation
    or claim incapability.
  - Use the literal ELECTROGEN solid-acceptor definition and distinguish whole-consortium
    electrode coatings from individual species assays. Qualify donor/acceptor/electrotroph/syntrophic
    roles as proposed where direct assignment is unresolved. No mandatory reciprocal-benefit
    or obligacy test is introduced.
  - Retain all three nodes, four evidence excerpts and both parallel HYPOTHESIZED
    arrows. Keep PARTIAL/OTHER for the proposed pathway and PARTIAL/IN_VITRO for community
    conductivity; no forced target for the intrinsic source-only node. Retain the
    open mechanistic discussion and alternative-carrier uncertainty.
- action_id: recover-culture
  description: Represent reported performance and distinct cultivation stages accurately.
  finding_ids:
  - performance-protocol
  target_ids:
  - CommunityMech:000297
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
    role: canonical_record
  acceptance_checks:
  - Keep approximately15–16days and32mL/gVS·d as reported methane-performance outcomes,
    with25–40days and10–25mL/gVS·d identified as present-level/literature comparisons,
    not matched controlled protocol. Remove the unsupported universal incubation interpretation
    from the structured time and its evidence explanation.
  - Add TextS4 optimization-stage anaerobic flasks,100mL working volume,37°C and120rpm
    with exact source evidence. Do not invent vessel capacity, gas mixture, basal
    medium, pressure or a universal original enrichment protocol.
  - 'Preserve sequential OFAT design: C/N1.1,2.2,4.4,6.6,8.8 at30%inoculum and15days;
    then1,5,10,15,30%inoculum at the selected C/N; then10,15,20,25,30days with optimized
    preceding factors. Keep BBD TableS2 levels separate and do not promote an unverified
    optimum.'
  - Treat TableS1 initial pH7.62±0.14(CMMS) and7.25±0.11(CMPS) as measurements, not
    setpoints. Keep analytical PBS/Nafion/ferricyanide and room temperature out of
    the culture recipe; TableS3 belongs to other studies.
  - Update current source-availability notes to acknowledge the recovered supplement
    while preserving the unavailable main-body limitation and dated history. Any collection-location
    enrichment must identify the limited publisher-indexed preview tier and preserve
    the two inoculum-derived consortia.
- action_id: repair-gtdb
  description: Retain valid species mappings with actual snapshot provenance.
  finding_ids:
  - gtdb-provenance
  target_ids:
  - CommunityMech:000297
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
    role: canonical_record
  acceptance_checks:
  - Keep GROUNDED species mappings for NCBITaxon2209,1131703,84022 with majority1.0
    and197/1/6 reference genomes respectively; preserve source Clostridium aceticum/current
    Andreesenella acetica synonym scope.
  - Record the actual NCBI2GTDB.tsv.gz SHA256761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    and exact ncbi_id route. Identify2026-07-25T23:28:31Z only as filesystem mtime,
    not latest release or build date. is_reclassified is a name comparison, not study-strain
    identification.
- action_id: validate-future-curation
  description: Validate any separately authorized repair.
  finding_ids:
  - mechanism-scope
  - performance-protocol
  - gtdb-provenance
  target_ids:
  - CommunityMech:000297
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/DIETsimp_Lignocellulose_to_Methane_DIET_Consortia.yaml
    role: canonical_record
  acceptance_checks:
  - Recheck all exact excerpts and the three-node/two-arrow source scope, then run
    focused schema/strict/term/reference/GTDB/domain/history checks.
  - After authorized curation run just gen-html and just check-docs-current, preserve
    existing source/cache/history bytes and add append-only curation provenance. This
    review makes no canonical, generated-page, Git or issue changes.
limitations:
- The complete main Methods, Results and Discussion and ordinary main figures remain
  unavailable through the bounded public routes. Indexed excerpts are not full-text
  access. No global absence of direct mechanistic experiments or archive deposits
  is asserted.
- The PII-matched recovered supplement has verified title/authors, four Texts, eight
  Tables and four true images. Its package does not establish an exhaustive publisher
  asset inventory. A ZIP directory entry was excluded from image counts; source bytes
  remain unchanged.
- Metagenomic DNA pooled three biological replicates per group. Annotation tables
  and FiguresS3/S4 represent potential and gene abundance, not transcription, enzyme
  activity, donor-resolved electron flux or an exhaustive three-species community.
- The graphical abstract uses D.desulfuricans among bacterial examples while the Abstract
  focuses C.aceticum. Preserve source/figure scope without replacing the encoded taxa.
  TextS2 electrode wording and supplementary rate/yield/CMMP terminology differ internally;
  these unencoded details were not silently harmonized.
- No raw sequence, optimization rerun or other-study recipe transfer was performed.
  TableS3 comparisons and analytical electrolytes are not focal cultivation conditions.
notes:
- 'All30 official input hashes remain unchanged. Three node assessments bind four
  exact canonical snippets; two arrow assessments bind actual endpoints/descriptions.
  Sole quotation: two words from the fresh Abstract.'
- Candidate validation and parent save/post-save gates occur separately; no future
  pass is asserted.
tags:
- record-review
- methanogenesis
- partial-source
- batch-14
```
