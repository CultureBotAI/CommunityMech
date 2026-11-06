# Cyprus copper sulphide bioleaching record review

- Review: 20261022T025653Z-cyprus-copper-bioleaching-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T02:46:38.133713Z
- Finished UTC: 2026-10-22T02:56:53.348870Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The complete paper and declared supplements support the SC3 enrichment identity and three qualified graph nodes. One major finding addresses nongraph mineral chemistry and Fe-only attribution; three minor findings concern cultivation, GTDB provenance and study-resource traceability. Eight focused checks pass. Literal completeness 25 and raw quality 109 (capped 100) remain separate from the scientific verdict.

## Scope And Provenance

Whole target and fresh primary manuscript, all main/SI figures and all nonempty cells of the five supplementary workbook sheets, with current authority and bounded direct resource verification.

Selection: Only released CommunityMech:000217 in owned batch14.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e117e3d37c65bfad2e04af53ab34e1325d8d7f98.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000217 | kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml | maintained | Cyprus Copper Sulphide Bioleaching Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000217 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000217 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000217 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000217 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000217 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000217 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000217 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000217 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000217 | Actual corpus exit 1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000217 | Actual corpus exit 1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000217 | Unavailable in owned runtime. |

## Scientific And Domain Assessments

### SC3 enrichment and aggregate members

identity: supported. Targets: CommunityMech:000217.

The record denotes the laboratory SC3 mineral-transfer community, with valid natural origin and engineered state.

The four descriptors aggregate multiple recovered organisms, not four isolates. Keep physical laboratory environment and broad modeled acid-mine-drainage analogy separate from the originating column. No mandatory species split, missing-role invention or quantitative abundance threshold follows.

### Mineral- and Fraction-Associated Community Profiles

graph: supported. Targets: CommunityMech:000217.

Retain observed mineral/fraction-associated profiles with the existing Fe-only and pooled-DNA limits.

Exact selector ecological_interactions[0]; name Mineral- and Fraction-Associated Community Profiles; scope COMMUNITY_LEVEL; interaction_type absent. Encoded taxa: {"source": null, "target": null, "participants": [{"id": "NCBITaxon:119977", "label": "Acidithiobacillus"}, {"id": "NCBITaxon:412449", "label": "Leptospirillum ferrodiazotrophum"}, {"id": "NCBITaxon:204441", "label": "Rhodospirillales"}, {"id": "NCBITaxon:2301", "label": "Thermoplasmatales"}]}. Canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "42d5ef20c7d70c738e760e8b4027475f2e0ad0d1dcd1f305416458c33df056d2", "reference": "PMID:41381092", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 d6dcd2f92cba07f0ca08bd64a285c4c5ea2dfc60e2eb98979369eccbfde7bad8. PMID:41381092 locator: Fresh MED Abstract abundance-trend sentence; Methods 2.4; Results 3.2; Figure 2 and Table S2. Retain SUPPORT/IN_VITRO. Different minerals co-vary in structure, sulfur chemistry, kinetics and iron; relative DNA profiles from pooled samples are not member-specific metabolic flux.

### Plasmid-Encoded Functional Potential

graph: supported. Targets: CommunityMech:000217.

Retain computational plasmid-encoded potential for the explicitly named host subset.

Exact selector ecological_interactions[1]; name Plasmid-Encoded Functional Potential; scope COMMUNITY_LEVEL; interaction_type absent. Encoded taxa: {"source": null, "target": null, "participants": [{"id": "NCBITaxon:119977", "label": "Acidithiobacillus"}, {"id": "NCBITaxon:412449", "label": "Leptospirillum ferrodiazotrophum"}]}. Canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "b0bc2430c05c462e1dda5b079b916189258a38a78ff90c7b337af0bf801442fb", "reference": "PMID:41381092", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}]. Snippet audit SHA256 d6dcd2f92cba07f0ca08bd64a285c4c5ea2dfc60e2eb98979369eccbfde7bad8. PMID:41381092 locator: Fresh MED Abstract plasmid-functions sentence; Methods 2.5; Results 3.3 paragraph 1 and Table 2. Retain SUPPORT/COMPUTATIONAL. Acidithiobacillus and Leptospirillum represent only the associated subset; the Alphaproteobacteria copper-resistance plasmid is not assigned to canonical Rhodospirillales or archaea.

### Putative Acidithiobacillus Plasmid CRISPR Interference

graph: supported. Targets: CommunityMech:000217.

Retain source-only, hypothesized plasmid interference without a measured competitive interaction.

Exact selector ecological_interactions[2]; name Putative Acidithiobacillus Plasmid CRISPR Interference; scope PAIRWISE; interaction_type absent. Encoded taxa: {"source": {"id": "NCBITaxon:119977", "label": "Acidithiobacillus"}, "target": null, "participants": []}. Canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "be67eda95c87ff94159f3f71cf6101deda8331a52032c3dcfdc01623ff14a4fa", "reference": "PMID:41381092", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"}]. Snippet audit SHA256 d6dcd2f92cba07f0ca08bd64a285c4c5ea2dfc60e2eb98979369eccbfde7bad8. PMID:41381092 locator: Fresh MED Abstract CRISPR-spacer sentence; Methods 2.8; Results 3.3 paragraph 2 and Table 3. Retain PARTIAL/COMPUTATIONAL and HYPOTHESIZED. Plasmid_56_509 matches two unbinned Acidithiobacillus-like contigs; no target cleavage, exclusion, co-residence or reciprocal harm is measured.

### Zero downstream arrows

graph: supported. Targets: CommunityMech:000217.

The three contextual findings do not require causal arrows between them.

Preserve three untyped nodes and the source-only third node. Characterization/repertoire-to-example relationships do not establish a downstream dependency. No forced COMPETITION or reciprocal benefit tag.

### Mineral identity and nongraph causal wording

grounding: concern. Targets: CommunityMech:000217.

Valid mineral identifiers coexist with unsupported oxidation-state and surrogate/Fe-only explanations.

Apply the same co-varying mineral boundary already present in node 0 to related_ingredients. Fe(II) cycling is not the entire released iron pool; the two minerals are alternative treatments, not a simultaneously required mixture.

### Recoverable MAM and staged protocol

completeness: concern. Targets: CommunityMech:000217.

The source supplies a recipe and additional preparation details missing from the structured record.

Keep 28°C, no agitation, serial transfers and source-specified sampling. Replace unsupported exposure/settled-surface design rationale and unrelated-record commentary. No vessel capacity, working volume, gas regime or complete Atlas trace stock is inferred.

### Current aggregate mappings versus study MAGs

grounding: concern. Targets: CommunityMech:000217.

Reference-wide cores reproduce, but their provenance and source-MAG distinction need clarification.

Table S2 names historical and GTDB-Tk classifications separately. Its Leptospirillum MAG maps to UBA4572 sp002387725 and Rhodospirillales MAG to Acidibrevibacterium fodinaquatile/Acetobacterales. These are original study-MAG results, not automatic replacements for current broad NCBI descriptors.

### Source-declared project and genome resources

provenance: concern. Targets: CommunityMech:000217.

Empty associated_datasets omits a verifiable source project and six pooled metagenomic samples.

Add exact run/BioSample/MAG scope and ggKbase provenance; distinguish six runs from three pooled replicates per condition and from other-enrichment transcriptomes. Publication links remain valid.

### Observations, potential and source conflicts

scope: supported. Targets: CommunityMech:000217.

Measured chemistry and relative composition remain distinct from proposed organism and mobile-element mechanisms.

Figure 4 is explicitly genetic potential and Figure 5 literature-based mechanism. Unencoded value/fraction/quality inconsistencies are retained as limitations, not extra record defects. Existing description identifies spacer evidence; optional inferential wording can be harmonized without another finding.

### Maintained input and historical context

ownership: supported. Targets: CommunityMech:000217.

Future repairs belong to the canonical YAML; prior graph corrections and dated access notes remain preserved.

The review does not close 1372, reopen 1369, overwrite the history or claim that old reviewers inspected today’s recovered SI.

### Focused validity and source support

schema: supported. Targets: CommunityMech:000217.

Eight focused checks pass; contextual corpus failures and optional adapter limits remain explicit.

### Two literal native scores

completeness: supported. Targets: CommunityMech:000217.

Completeness 25; raw quality 109, capped 100.

## Findings

### mineral-chemistry: Correct mineral chemistry and Fe-only attribution

major / open / confirmed; issue key: cm-000217-mineral-chemistry.

The source describes Cu(I)/Fe(III) in chalcopyrite and primarily ferric soluble iron. It does not test a soluble Cu(II)/Fe(II)/sulfide equivalent or independently manipulate Fe while holding mineral structure and kinetics constant. Existing nongraph wording exceeds that evidence.

### culture-protocol: Recover MAM and remove invented design rationale

minor / open / confirmed; issue key: cm-000217-culture-protocol.

The structured medium is empty despite a source recipe; setup notes infer a microbial-exposure and settled-surface purpose not stated by the authors. The mineral-specific passage stage is also recoverable.

### gtdb-provenance: Separate snapshot provenance from study MAG classifications

minor / open / confirmed; issue key: cm-000217-gtdb-provenance.

Three mapping_source strings claim latest release/build metadata unsupported by filesystem mtime. Table S2 supplies relevant original MAG classifications that must remain distinguishable from rank-aggregate RF32/Acidithiobacillus/Thermoplasmatales mappings.

### study-resources: Add declared project and genome-resource traceability

minor / open / confirmed; issue key: cm-000217-study-resources.

The paper and supplements identify raw metagenomes and derived genomes/plasmids, while associated_datasets is empty and external resources list only the publication.

## Recommended Actions And Acceptance Checks

### repair-chemistry

Align nongraph chemistry with the actual mineral comparison.

- Retain CHEBI86202 chalcopyrite, CHEBI51114 copper(I) sulfide and CHEBI29033 iron(2+). Explain the source Cu(I)/Fe(III) mineral description separately from ChEBI’s disconnected-ion representation and dissolved Cu(II)/Fe cycling.
- Remove the untested soluble-surrogate equivalence and claim that Fe(II) alone was manipulated. Describe co-varying mineral structure, sulfur chemistry, dissolution kinetics and mineral-derived iron, matching node 0.
- Describe alternative chalcopyrite and chalcocite treatment arms, not simultaneous addition of both phases. Preserve measured community/chemistry outcomes and all three qualified nodes, without adding causal arrows.

### recover-culture

Encode the reported MAM and staged enrichment with unresolved details explicit.

- Use Methods 2.1 paragraph 3: per litre 0.4 g(NH4)2SO4,0.4 g KH2PO4,0.4 g MgSO4·7H2O,1 mL trace stock including W/Se cited to Atlas 2004, pH 1.5 adjusted with H2SO4. Preserve the heptahydrate and do not invent the trace-stock formulation.
- Separate approximately 0.5 g source slurry, ten initial 28°C/no-agitation transfers with 5% inoculum every 2 months, and five subsequent same-mineral passages stated in Figure 1. Preserve three biotic and three abiotic replicates per mineral and six pooled sequencing samples.
- Keep the source 0.25 g mineral wording and its per-litre/per-enrichment ambiguity; do not derive a one-litre working volume, vessel capacity or supplied-gas regime. State BATCH at the individual incubation stage with transfers separately.
- Replace exposure and agitation-purpose conjecture with the authors’ mineral integrity/oxidation-state rationale, maximum 50 µm particles, XRD check and no microbes observed in abiotic controls. Remove unrelated-record/editorial notes.
- Keep exact source conflicts visible: chemical 0/4/6 caption versus 0/4/8 Methods/S3, and week 4 mixed caption versus liquid Methods. Do not silently harmonize.

### repair-gtdb

Preserve valid reference mappings and add accurate source-MAG provenance.

- Retain current reference aggregate cores: Acidithiobacillus 158/212 with four total destinations, Rhodospirillales→RF32 1269/1802 with 15 total destinations, Thermoplasmatales 63/63 with one. is_reclassified is a name comparison, not proof of study-organism reclassification.
- Record actual snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd and rank routes. Do not turn observed filesystem mtime into release latest or build date.
- Document Table S2 Organisms row 3 SAMN44253046 as original GTDB-Tk v1.3.0 UBA4572 sp002387725 and row 9 SAMN44253047 as Acidibrevibacterium fodinaquatile in Acetobacterales. Preserve source historical names and distinguish these MAG-specific results from current rank mappings; do not blanket-replace the NCBI descriptors or invent strain identity.
- The current exact Leptospirillum species lookup remains unresolved; a source-MAG classification is separate evidence, not proof of a universal species-level crosswalk.

### add-resources

Link source-specific sequencing and derived genome resources.

- Add PRJNA1170356 and the six exact Table S1 run mappings SRR30914516 through SRR30914511, preserving 4/8-week/mineral/fraction and pooled-replicate scope. These are metagenomes; project-level transcriptome remarks concern other enrichments.
- Link https://ggkbase.berkeley.edu/cu_bioleaching_organisms_and_plasmids and Table S2’s twelve MAG BioSample identities SAMN44253036–SAMN44253047 with exact row labels. BioSamples are not assemblies or isolate genome_accession values. Preserve the 12 putative plasmid context without inventing separate accession assignments.
- Use registry and source evidence at each added resource. Do not promote S1 phylogeny reference genomes or generic analysis tools to focal study deposits.

### validate-future-curation

Run required validation after separately authorized repair.

- Recheck exact source snippets and narrow assertion support, taxonomy/chemical labels, all node selectors and graph directions. Run focused schema, strict, terms, explained references, GTDB/domain and history gates.
- After authorized record changes run just gen-html and just check-docs-current. Preserve original history/source/caches and record append-only curation provenance; this review itself performs no canonical repair, Git operation, issue mutation or status promotion.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml; Whole maintained YAML | supports | Natural-origin SC3 enrichment, four aggregate member descriptors, three qualified untyped nodes and zero arrows. The record owns future repairs. |
| publication | PMID:41381092; DOI:10.1111/1758-2229.70261; Fresh MED identity fields and JATS article metadata | supports | PMID, DOI, title and PMC12698208 agree; the complete open-access manuscript and all declared supplements were recovered. |
| culture | PMID:41381092; DOI:10.1111/1758-2229.70261; Materials and Methods / Sample Collection and Enrichments (2.1), direct paragraphs 1–3 (quoted words in paragraph 3); Figure 1 caption | supports | Source column, MAM formulation, pH 1.5, 28°C, initial ten serial transfers and subsequent mineral-specific treatments are described. Figure 1 adds five further same-mineral passages. The authors left minerals unsterilised to preserve integrity and oxidation states; no laboratory fill volume is stated. |
| sampling | PMID:41381092; DOI:10.1111/1758-2229.70261; Materials and Methods / Chemical Analyses (2.2), sole paragraph; DNA Extraction and Sequencing (2.4), sole paragraph; Figure 1 and Figure 2 captions | supports | ICP-OES and colorimetric iron assays assess solution chemistry. Six sequencing samples represent mineral/time/fraction conditions, each pooling three biological replicates; this is not replicated organism-resolved flux measurement. Week 4 fraction wording differs between Methods 2.4 and Figure 2 caption. |
| chemistry | PMID:41381092; DOI:10.1111/1758-2229.70261; Results and Discussion / Cu Bioleaching by SC3 Microbial Consortium (3.1), all three direct paragraphs and equations; Figure 2B; Table S3 | supports | The focal mineral description assigns monovalent copper and trivalent iron to chalcopyrite. Solution iron is primarily ferric, with ferrous cycling discussed separately. Mineral structure, sulfur chemistry, kinetics and iron availability change together. Neither a soluble Cu(II)/Fe(II)/sulfide substitute nor an isolated iron perturbation was tested. |
| community | PMID:41381092; DOI:10.1111/1758-2229.70261; Results and Discussion / Microbial Community Composition and Metabolism (3.2), entire section; Figures 2–5; Table 1 | supports | Relative mapped-DNA profiles differ by mineral and fraction. The authors retain historical organism names and explicitly distinguish Figure 4 gene potential from activity; Figure 5 is a proposed literature-based mechanism. These data support the existing qualified community observation. |
| plasmids | PMID:41381092; DOI:10.1111/1758-2229.70261; Materials and Methods / Metagenomic Assembly, Annotation and Binning (2.5), paragraphs 2–3; CRISPR Analysis (2.8), sole paragraph; Results and Discussion / Mobile Elements in SC3 Bioleaching Community (3.3), both paragraphs; Tables 2–3 | supports | Twelve dereplicated putative plasmids include predicted functions. Plasmid_56_509 spacers match two unbinned Acidithiobacillus-like contigs with conjugation-related annotations. Host association, gene content and spacer matches do not prove expression, host benefit, cleavage, exclusion or reciprocal taxon harm. |
| si-runs | PMID:41381092; DOI:10.1111/1758-2229.70261; Table S1 DNA, all nonempty cells A1:K8 | supports | Six exact run identifiers are associated with mineral, time and fraction labels. Three biological replicates were pooled per sequencing sample. |
| si-samples | PMID:41381092; DOI:10.1111/1758-2229.70261; Table S2 Organisms, A1:M14; Plasmids, A1:I14; Organisms_in_samples, all nonempty A1:C56 | supports | Twelve MAG BioSamples and organism/plasmid identifiers are provided. Original GTDB-Tk results are study-MAG assignments, distinct from the record’s reference-wide rank mappings. All nonempty cells in these sheets were read without recomputing coverage or taxonomy. |
| si-chemistry | PMID:41381092; DOI:10.1111/1758-2229.70261; Table S3 Sheet1, all nonempty cells A1:G16; Figure 2B | supports | The table and plot assign the eight-week copper values to chalcopyrite 0.93 and chalcocite 2.108 g/L; the main sentence reverses its parenthetic labels. A separate time-zero table cell gives 90 g/L, inconsistent with the plot. These source conflicts are retained, not introduced as new canonical numeric findings. |
| si-figures | PMID:41381092; DOI:10.1111/1758-2229.70261; Figure S1 whole phylogenies; Figure S2 whole single-page GC-skew plot | supports | Phylogenies distinguish source MAG labels from reference accessions. Low/noisy GC skew is only suggestive of replication mode. No new isolate identity or demonstrated plasmid competition is inferred. |
| ontology | /private/tmp/cm-review-session/batch-14/000217/ontology-authority.json; All 10 ID-label definitions and 20 placements | supports | All labels match. CHEBI86202 identifies chalcopyrite but its disconnected Cu(II)/Fe(II) representation differs from the focal mineral-state description. |
| chemical-authority | /private/tmp/cm-review-session/batch-14/000217/child-mineral-chemical-scope.json; Exact mineral and ion semantics | supports | Keep correct CHEBI identifiers. Chemical identity does not validate a soluble surrogate, dissolved-iron speciation or Fe-only causality. |
| schema | /private/tmp/cm-review-session/batch-14/000217/child-schema-semantics.json; Literal roles, abundance, origin, state, modes and evidence | supports | Broad mineral-degrader roles are not restricted to polymers; ordinal abundance does not require a percentage threshold. BATCH can describe individual incubations with serial passages stated separately. |
| gtdb | /private/tmp/cm-review-session/batch-14/000217/child-gtdb-crosswalk.json; Three rank aggregates, one unresolved species and snapshot provenance | supports | Current cores reproduce: Acidithiobacillus 158/212, Rhodospirillales→RF32 1269/1802 and Thermoplasmatales 63/63. Local mtime does not establish release/build metadata; these aggregates are not study-MAG assignments. |
| semantics | /private/tmp/cm-review-session/batch-14/000217/ontology-semantic-notes.json; Final child semantic scope | supports | Four broad descriptors, mineral context and three qualified nodes are retained. Source-specific MAG enrichment must preserve study naming and original classification provenance. |
| resources | /private/tmp/cm-review-session/batch-14/000217/dataset-verification.json; Direct project/run and genome-resource metadata plus Table S1/S2 mapping | supports | Project and ggKbase traceability are verified within declared scope. Six metagenomic runs are distinct from other-enrichment transcriptomes mentioned in project context; no raw datasets were downloaded. |
| resource-correction | /private/tmp/cm-review-session/batch-14/000217/dataset-project-projection-correction.json; Exact project TITLE/DESCRIPTION display correction | supports | Two null display fields in the preserved resource receipt are corrected from the original PROJECT XML. Resource identities, mappings and conclusions are unchanged. |
| snippets | /private/tmp/cm-review-session/batch-14/000217/snippet-audit.json; Every canonical excerpt occurrence | supports | All 17 occurrences match fresh sources and the MD cache: 11 JATS placements plus six additional exact MED Abstract placements. The TXT cache contains 15 matches. Lexical support is separate from entailment. Exact node snippets are bound below by canonical selectors and SHA256. |
| provenance | /private/tmp/cm-review-session/batch-14/000217/provenance-audit.json; Sole history, exact batch28 row, current issues and four cohort contexts | supports | Prior graph corrections remain dated context. Open 1372 concerns nongraph chemistry; closed 1369 does not establish every nongraph claim. No issue is closed or historical event rewritten. |
| inspection | /private/tmp/cm-review-session/batch-14/000217/inspect.json; 31 immutable official inputs | supports | Ignored-inclusive discovery covered exact ID, filename, PMID and DOI in cache/history/reports/reviews; nine focal files plus 21 authorities and target are pinned. Generic corpus hits remained discovery-only. |
| assets | /private/tmp/cm-review-session/batch-14/000217/lead-source-assets.json; Complete primary and declared asset inventory | supports | Five main figures, graphical abstract, two SI figures and three workbooks are available. Failed normal attachment/CDN responses remain distinct from the MD5-verified EPMC package. |
| lead-read | /private/tmp/cm-review-session/batch-14/000217/lead-primary-read-scope.json; Actual full-source reading and bounded reanalysis | supports | Whole 75,665-character main including 89 references, all tables/captions, six JPEGs, two SI figures and all nonempty cells of five workbook sheets were read. No sequence, phylogenetic or statistical reanalysis. |
| sections | /private/tmp/cm-review-session/batch-14/000217/source-section-projection.json; Direct fresh-JATS heading/paragraph inventory | supports | All candidate locators are checked against actual section labels and direct paragraph counts; the sole quote occurs in Methods 2.1 paragraph 3. |
| source-scope | /private/tmp/cm-review-session/batch-14/000217/source-audit.json; Final lead scientific assessment | supports | One major chemistry/causality finding and three minor cultivation, GTDB-provenance and resource findings; all scientific source material needed for this scope is available. |
| root-source | /private/tmp/cm-review-session/batch-14/000217/root-independent-source-audit.json; Independent root scientific assessment | supports | Root independently reconciles source text, figures, all SI sheets, source conflicts and final finding groups. |
| metrics | /private/tmp/cm-review-session/batch-14/000217/support-final-audit.json; Distinct final support and literal arithmetic | supports | Completeness 25; quality 125 base minus 10 for one P2 and 6 for three P3 gives 109 raw, capped 100. Scores do not establish scientific truth. |
| support-manifest | /private/tmp/cm-review-session/batch-14/000217/supporting-artifact-manifest.json; Frozen supporting inputs | supports | Final support follows source/authority reconciliation and preserves preliminary receipts. |
| auxiliary | /private/tmp/cm-review-session/batch-14/000217/auxiliary-frozen-manifest.json; Frozen native/authority outputs | supports | Eight focused checks pass; all 31 inspected inputs remain unchanged. |
| final-native | /private/tmp/cm-review-session/batch-14/000217/final-validator-summary.json; Eight actual command/stdout/stderr outcomes | supports | Focused checks pass; zero reported reference issues does not replace independent snippet and source review. |
| corpus-context | /private/tmp/cm-review-session/batch-14/000217/child-current-corpus-context.json; Actual batch14 baseline | supports | Both corpus commands exited 1 with 44 warnings across 16 of 477 records and zero errors; these are nonrequired context. |
| adapter | /private/tmp/cm-review-session/batch-14/000217/adapter-check.json; Owned runtime optional structured adapter | supports | The optional adapter was unavailable; no external-checkout adapter was executed. |
| check-validate | /private/tmp/cm-review-session/batch-14/000217/validate.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment reviewed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-14/000217/validate-strict.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment reviewed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-14/000217/validate-terms.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment reviewed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-14/000217/validate-references-explained.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment reviewed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-14/000217/validate-gtdb.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment reviewed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-14/000217/validate-gtdb-domain.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment reviewed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-14/000217/validate-history.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment reviewed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-14/000217/normalize-cache-names-check.json; Actual current command/stdout/stderr | supports | Native exit 0; scientific entailment reviewed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-14/audit-network.json; Fresh batch14 corpus baseline | supports | Actual exit 1 with 44 warnings across 16 of 477 records and zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-14/check-network-quality.json; Fresh batch14 corpus baseline | supports | Actual exit 1 with 44 warnings across 16 of 477 records and zero errors. |

## Limits And Additional Notes

- No raw sequencing, read-mapping, phylogenetic or statistical reanalysis was performed. Source gene and spacer annotations remain potential and association.
- The source reverses 0.93/2.1g/L parenthetic mineral labels, and S3 time-zero Cu cell E5 says 90 g/L unlike the plot. Figure 1 chemical sampling 0/4/6 conflicts Methods/S3 0/4/8; Figure 2 week 4 mixed-fraction caption conflicts Methods liquid sampling. These unencoded inconsistencies are not new record findings.
- Methods says all downstream MAGs pass 10% contamination, but Table S2 Organisms M8 is 13.48%. Preserve that source-quality limitation when reusing its classifications.
- The complete Atlas trace-stock formulation and laboratory working volume are not supplied by the inspected focal material. Figure flask cartoons do not establish a numerical fill or explicit vessel specification.
- Reference-wide GTDB mappings, original study GTDB-Tk assignments and phylogenetic comparator accessions have separate scope. No new modern classification or isolate identity is certified.
- Three node assessments bind all three canonical snippet hashes and exact participants; the record has zero arrows. The sole direct quotation is two words from Methods 2.1 paragraph 3.
- All 31 inspected inputs are unchanged. Parent-owned candidate validation, saving and post-save gates follow this source assessment; no future success is asserted.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T025653Z-cyprus-copper-bioleaching-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Cyprus copper sulphide bioleaching record review
started_at: '2026-10-22T02:46:38.133713Z'
finished_at: '2026-10-22T02:56:53.348870Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, supporting and auxiliary reviewers; no
    person-level independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The complete paper and declared supplements support the SC3 enrichment identity
  and three qualified graph nodes. One major finding addresses nongraph mineral chemistry
  and Fe-only attribution; three minor findings concern cultivation, GTDB provenance
  and study-resource traceability. Eight focused checks pass. Literal completeness
  25 and raw quality 109 (capped 100) remain separate from the scientific verdict.
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
  - path: history/records/Cyprus_Copper_Sulphide_Bioleaching_Consortium/2026-10-06T045256Z-codex-f71387.yaml
    sha256: e42a22dcd9b2b38ae0c7b98a39f3de887c6b07589924465bb1af06c2008c92b6
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    sha256: c914e6ebd91d24dbb0b18b48b2aff7979e6528900cc282824d40b8da8afb29c8
    role: target
  - path: references_cache/PMID_41381092.md
    sha256: b1305170302d2a3241a7fbce156d9c0c8054bf257cf308810b34a66baecd2710
    role: context
  - path: references_cache/PMID_41381092.txt
    sha256: 8d157568486d11ca3c30eeb232590a5d513e9ef90de8bac2340deab82b70f00a
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
- target_id: CommunityMech:000217
  path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
  label: Cyprus Copper Sulphide Bioleaching Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    role: canonical_record
scope:
  description: Whole target and fresh primary manuscript, all main/SI figures and
    all nonempty cells of the five supplementary workbook sheets, with current authority
    and bounded direct resource verification.
  selection: Only released CommunityMech:000217 in owned batch14.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000217
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000217
  command: just --no-dotenv validate kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
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
  - CommunityMech:000217
  command: just --no-dotenv validate-strict kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-14/000217/strict-report.tsv
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
  - CommunityMech:000217
  command: just --no-dotenv validate-terms kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
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
  - CommunityMech:000217
  command: just --no-dotenv validate-references-explained kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
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
  - CommunityMech:000217
  command: just --no-dotenv validate-gtdb kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
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
  - CommunityMech:000217
  command: just --no-dotenv validate-gtdb-domain kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
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
  - CommunityMech:000217
  command: just --no-dotenv validate-history history/records/Cyprus_Copper_Sulphide_Bioleaching_Consortium
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
  - CommunityMech:000217
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
  - CommunityMech:000217
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, not attributed wholly to this target.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1 retained.
  target_ids:
  - CommunityMech:000217
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, not attributed wholly to this target.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in owned runtime.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - adapter
  scope_note: No external-checkout adapter executed.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
  locator: Whole maintained YAML
  summary: Natural-origin SC3 enrichment, four aggregate member descriptors, three
    qualified untyped nodes and zero arrows. The record owns future repairs.
  support: supports
  accessed_at: '2026-10-22T02:55:49.512251Z'
- evidence_id: publication
  kind: database
  reference: PMID:41381092; DOI:10.1111/1758-2229.70261
  locator: Fresh MED identity fields and JATS article metadata
  summary: PMID, DOI, title and PMC12698208 agree; the complete open-access manuscript
    and all declared supplements were recovered.
  support: supports
  accessed_at: '2026-10-22T02:55:49.512338Z'
  snapshot_sha256: 37c23b242f9f62f4362ea98fbac911a120a39848d414a968af5e6af48b210313
- evidence_id: culture
  kind: primary_source
  reference: PMID:41381092; DOI:10.1111/1758-2229.70261
  locator: Materials and Methods / Sample Collection and Enrichments (2.1), direct
    paragraphs 1–3 (quoted words in paragraph 3); Figure 1 caption
  summary: Source column, MAM formulation, pH 1.5, 28°C, initial ten serial transfers
    and subsequent mineral-specific treatments are described. Figure 1 adds five further
    same-mineral passages. The authors left minerals unsterilised to preserve integrity
    and oxidation states; no laboratory fill volume is stated.
  support: supports
  accessed_at: '2026-10-22T02:55:49.512493Z'
  snapshot_sha256: 53b73bc09fed7487ee2ed5f232e3c32830bc8693956976d32a51a1bdc96b99a8
  quote: without agitation
- evidence_id: sampling
  kind: primary_source
  reference: PMID:41381092; DOI:10.1111/1758-2229.70261
  locator: Materials and Methods / Chemical Analyses (2.2), sole paragraph; DNA Extraction
    and Sequencing (2.4), sole paragraph; Figure 1 and Figure 2 captions
  summary: ICP-OES and colorimetric iron assays assess solution chemistry. Six sequencing
    samples represent mineral/time/fraction conditions, each pooling three biological
    replicates; this is not replicated organism-resolved flux measurement. Week 4
    fraction wording differs between Methods 2.4 and Figure 2 caption.
  support: supports
  accessed_at: '2026-10-22T02:55:49.512979Z'
  snapshot_sha256: 53b73bc09fed7487ee2ed5f232e3c32830bc8693956976d32a51a1bdc96b99a8
- evidence_id: chemistry
  kind: primary_source
  reference: PMID:41381092; DOI:10.1111/1758-2229.70261
  locator: Results and Discussion / Cu Bioleaching by SC3 Microbial Consortium (3.1),
    all three direct paragraphs and equations; Figure 2B; Table S3
  summary: The focal mineral description assigns monovalent copper and trivalent iron
    to chalcopyrite. Solution iron is primarily ferric, with ferrous cycling discussed
    separately. Mineral structure, sulfur chemistry, kinetics and iron availability
    change together. Neither a soluble Cu(II)/Fe(II)/sulfide substitute nor an isolated
    iron perturbation was tested.
  support: supports
  accessed_at: '2026-10-22T02:55:49.513101Z'
  snapshot_sha256: 53b73bc09fed7487ee2ed5f232e3c32830bc8693956976d32a51a1bdc96b99a8
- evidence_id: community
  kind: primary_source
  reference: PMID:41381092; DOI:10.1111/1758-2229.70261
  locator: Results and Discussion / Microbial Community Composition and Metabolism
    (3.2), entire section; Figures 2–5; Table 1
  summary: Relative mapped-DNA profiles differ by mineral and fraction. The authors
    retain historical organism names and explicitly distinguish Figure 4 gene potential
    from activity; Figure 5 is a proposed literature-based mechanism. These data support
    the existing qualified community observation.
  support: supports
  accessed_at: '2026-10-22T02:55:49.513211Z'
  snapshot_sha256: 53b73bc09fed7487ee2ed5f232e3c32830bc8693956976d32a51a1bdc96b99a8
- evidence_id: plasmids
  kind: primary_source
  reference: PMID:41381092; DOI:10.1111/1758-2229.70261
  locator: Materials and Methods / Metagenomic Assembly, Annotation and Binning (2.5),
    paragraphs 2–3; CRISPR Analysis (2.8), sole paragraph; Results and Discussion
    / Mobile Elements in SC3 Bioleaching Community (3.3), both paragraphs; Tables
    2–3
  summary: Twelve dereplicated putative plasmids include predicted functions. Plasmid_56_509
    spacers match two unbinned Acidithiobacillus-like contigs with conjugation-related
    annotations. Host association, gene content and spacer matches do not prove expression,
    host benefit, cleavage, exclusion or reciprocal taxon harm.
  support: supports
  accessed_at: '2026-10-22T02:55:49.513324Z'
  snapshot_sha256: 53b73bc09fed7487ee2ed5f232e3c32830bc8693956976d32a51a1bdc96b99a8
- evidence_id: si-runs
  kind: primary_source
  reference: PMID:41381092; DOI:10.1111/1758-2229.70261
  locator: Table S1 DNA, all nonempty cells A1:K8
  summary: Six exact run identifiers are associated with mineral, time and fraction
    labels. Three biological replicates were pooled per sequencing sample.
  support: supports
  accessed_at: '2026-10-22T02:55:49.513430Z'
  snapshot_sha256: 0191712e6b72ef7fe3c5786bdd124f18a7b94b653903d07bb718e365c5747604
- evidence_id: si-samples
  kind: primary_source
  reference: PMID:41381092; DOI:10.1111/1758-2229.70261
  locator: Table S2 Organisms, A1:M14; Plasmids, A1:I14; Organisms_in_samples, all
    nonempty A1:C56
  summary: Twelve MAG BioSamples and organism/plasmid identifiers are provided. Original
    GTDB-Tk results are study-MAG assignments, distinct from the record’s reference-wide
    rank mappings. All nonempty cells in these sheets were read without recomputing
    coverage or taxonomy.
  support: supports
  accessed_at: '2026-10-22T02:55:49.513654Z'
  snapshot_sha256: d53e45d005817a754f067dd843ebdb6437c440aea311681659e84c6235a7d762
- evidence_id: si-chemistry
  kind: primary_source
  reference: PMID:41381092; DOI:10.1111/1758-2229.70261
  locator: Table S3 Sheet1, all nonempty cells A1:G16; Figure 2B
  summary: The table and plot assign the eight-week copper values to chalcopyrite
    0.93 and chalcocite 2.108 g/L; the main sentence reverses its parenthetic labels.
    A separate time-zero table cell gives 90 g/L, inconsistent with the plot. These
    source conflicts are retained, not introduced as new canonical numeric findings.
  support: supports
  accessed_at: '2026-10-22T02:55:49.513828Z'
  snapshot_sha256: 7c05923e9051760df61b255436834a4ef5ef59d7136e43232570bb38d8df5a91
- evidence_id: si-figures
  kind: primary_source
  reference: PMID:41381092; DOI:10.1111/1758-2229.70261
  locator: Figure S1 whole phylogenies; Figure S2 whole single-page GC-skew plot
  summary: Phylogenies distinguish source MAG labels from reference accessions. Low/noisy
    GC skew is only suggestive of replication mode. No new isolate identity or demonstrated
    plasmid competition is inferred.
  support: supports
  accessed_at: '2026-10-22T02:55:49.513993Z'
  snapshot_sha256: f5813bd209b34da2ce0287cfdde81a71d6b85736f46aa7ca105ab4054f5ef209
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000217/ontology-authority.json
  locator: All 10 ID-label definitions and 20 placements
  summary: All labels match. CHEBI86202 identifies chalcopyrite but its disconnected
    Cu(II)/Fe(II) representation differs from the focal mineral-state description.
  support: supports
  accessed_at: '2026-10-22T02:55:49.514151Z'
  snapshot_sha256: b9030b792d1724d568274df5a72c118e6320e6887b1ef20b0a8f468b3c98ef97
- evidence_id: chemical-authority
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000217/child-mineral-chemical-scope.json
  locator: Exact mineral and ion semantics
  summary: Keep correct CHEBI identifiers. Chemical identity does not validate a soluble
    surrogate, dissolved-iron speciation or Fe-only causality.
  support: supports
  accessed_at: '2026-10-22T02:55:49.514308Z'
  snapshot_sha256: 7e7c6ea4c1df0799582d768043fbe98f09d422ecad7385d7a13ec901a2cecd32
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000217/child-schema-semantics.json
  locator: Literal roles, abundance, origin, state, modes and evidence
  summary: Broad mineral-degrader roles are not restricted to polymers; ordinal abundance
    does not require a percentage threshold. BATCH can describe individual incubations
    with serial passages stated separately.
  support: supports
  accessed_at: '2026-10-22T02:55:49.514451Z'
  snapshot_sha256: 4b0bf31da7f956144ef09e33e1eea8fb52517b9b4e60f20829f57322631421db
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000217/child-gtdb-crosswalk.json
  locator: Three rank aggregates, one unresolved species and snapshot provenance
  summary: 'Current cores reproduce: Acidithiobacillus 158/212, Rhodospirillales→RF32
    1269/1802 and Thermoplasmatales 63/63. Local mtime does not establish release/build
    metadata; these aggregates are not study-MAG assignments.'
  support: supports
  accessed_at: '2026-10-22T02:55:49.514616Z'
  snapshot_sha256: a83f6c87c40816bd040e541ea69bde8f9ba2120c0c4ba5f7a1e5af2ec94ea1fe
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000217/ontology-semantic-notes.json
  locator: Final child semantic scope
  summary: Four broad descriptors, mineral context and three qualified nodes are retained.
    Source-specific MAG enrichment must preserve study naming and original classification
    provenance.
  support: supports
  accessed_at: '2026-10-22T02:55:49.514764Z'
  snapshot_sha256: 3ad0ec1c86b10f827e2ea9622e172627580b6db6e1a267b2136cfd7f52b28838
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/dataset-verification.json
  locator: Direct project/run and genome-resource metadata plus Table S1/S2 mapping
  summary: Project and ggKbase traceability are verified within declared scope. Six
    metagenomic runs are distinct from other-enrichment transcriptomes mentioned in
    project context; no raw datasets were downloaded.
  support: supports
  accessed_at: '2026-10-22T02:55:49.514906Z'
  snapshot_sha256: d42b3b6e1497c1d98a6156562fa5573c39e248b05b45eefaede5f7010330e44f
- evidence_id: resource-correction
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/dataset-project-projection-correction.json
  locator: Exact project TITLE/DESCRIPTION display correction
  summary: Two null display fields in the preserved resource receipt are corrected
    from the original PROJECT XML. Resource identities, mappings and conclusions are
    unchanged.
  support: supports
  accessed_at: '2026-10-22T02:55:49.515129Z'
  snapshot_sha256: 7feb46e7ea9865b7a38c508f7f9fd38fa667a6f96144bda054d5fbf3a1f27ca6
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/snippet-audit.json
  locator: Every canonical excerpt occurrence
  summary: 'All 17 occurrences match fresh sources and the MD cache: 11 JATS placements
    plus six additional exact MED Abstract placements. The TXT cache contains 15 matches.
    Lexical support is separate from entailment. Exact node snippets are bound below
    by canonical selectors and SHA256.'
  support: supports
  accessed_at: '2026-10-22T02:55:49.515173Z'
  snapshot_sha256: d6dcd2f92cba07f0ca08bd64a285c4c5ea2dfc60e2eb98979369eccbfde7bad8
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-14/000217/provenance-audit.json
  locator: Sole history, exact batch28 row, current issues and four cohort contexts
  summary: Prior graph corrections remain dated context. Open 1372 concerns nongraph
    chemistry; closed 1369 does not establish every nongraph claim. No issue is closed
    or historical event rewritten.
  support: supports
  accessed_at: '2026-10-22T02:55:49.515310Z'
  snapshot_sha256: 2f745d7475f0b8052760c96638e0371f2fa9faba43f047a80233346488c0d82a
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/inspect.json
  locator: 31 immutable official inputs
  summary: Ignored-inclusive discovery covered exact ID, filename, PMID and DOI in
    cache/history/reports/reviews; nine focal files plus 21 authorities and target
    are pinned. Generic corpus hits remained discovery-only.
  support: supports
  accessed_at: '2026-10-22T02:55:49.515449Z'
  snapshot_sha256: d37700617a8f9b7b74a66f2be221bce099439ff1982bed1755ac525bd2522cc5
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/lead-source-assets.json
  locator: Complete primary and declared asset inventory
  summary: Five main figures, graphical abstract, two SI figures and three workbooks
    are available. Failed normal attachment/CDN responses remain distinct from the
    MD5-verified EPMC package.
  support: supports
  accessed_at: '2026-10-22T02:55:49.515488Z'
  snapshot_sha256: f5813bd209b34da2ce0287cfdde81a71d6b85736f46aa7ca105ab4054f5ef209
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/lead-primary-read-scope.json
  locator: Actual full-source reading and bounded reanalysis
  summary: Whole 75,665-character main including 89 references, all tables/captions,
    six JPEGs, two SI figures and all nonempty cells of five workbook sheets were
    read. No sequence, phylogenetic or statistical reanalysis.
  support: supports
  accessed_at: '2026-10-22T02:55:49.515520Z'
  snapshot_sha256: c174ea15394eaeff8100263bc167353d338287e1246d68bb1829046e6e03164f
- evidence_id: sections
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/source-section-projection.json
  locator: Direct fresh-JATS heading/paragraph inventory
  summary: All candidate locators are checked against actual section labels and direct
    paragraph counts; the sole quote occurs in Methods 2.1 paragraph 3.
  support: supports
  accessed_at: '2026-10-22T02:55:49.515654Z'
  snapshot_sha256: 6b831bf8ec489946e3fac3510682c83999bf163dcfaff98b4f71ad1b3b6d0a4e
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/source-audit.json
  locator: Final lead scientific assessment
  summary: One major chemistry/causality finding and three minor cultivation, GTDB-provenance
    and resource findings; all scientific source material needed for this scope is
    available.
  support: supports
  accessed_at: '2026-10-22T02:55:49.515830Z'
  snapshot_sha256: ae1e181b9d0759ba8660ebcd4b7d9895d02b7d6e850ced85a67e6dd9031ac70c
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/root-independent-source-audit.json
  locator: Independent root scientific assessment
  summary: Root independently reconciles source text, figures, all SI sheets, source
    conflicts and final finding groups.
  support: supports
  accessed_at: '2026-10-22T02:55:49.515991Z'
  snapshot_sha256: a518b23d28bf211962f5d9495d78a8fc5eda89ce75657901acc5b73bbd0258be
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/support-final-audit.json
  locator: Distinct final support and literal arithmetic
  summary: Completeness 25; quality 125 base minus 10 for one P2 and 6 for three P3
    gives 109 raw, capped 100. Scores do not establish scientific truth.
  support: supports
  accessed_at: '2026-10-22T02:55:49.516035Z'
  snapshot_sha256: 58ee55f6ce09a9a39c0f103cb9ee817cbf973d76ab124d01f39a44a80fa0b176
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/supporting-artifact-manifest.json
  locator: Frozen supporting inputs
  summary: Final support follows source/authority reconciliation and preserves preliminary
    receipts.
  support: supports
  accessed_at: '2026-10-22T02:55:49.516065Z'
  snapshot_sha256: 91b450929be19a64cdeb0d49330edb168a10ae130be3af462f456a58eb39009f
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/auxiliary-frozen-manifest.json
  locator: Frozen native/authority outputs
  summary: Eight focused checks pass; all 31 inspected inputs remain unchanged.
  support: supports
  accessed_at: '2026-10-22T02:55:49.516194Z'
  snapshot_sha256: 1cd2458b858564dc17e58d0758a9c4b28c5c53105d916269f1b362d06fe62d97
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/final-validator-summary.json
  locator: Eight actual command/stdout/stderr outcomes
  summary: Focused checks pass; zero reported reference issues does not replace independent
    snippet and source review.
  support: supports
  accessed_at: '2026-10-22T02:55:49.516297Z'
  snapshot_sha256: a071f117c8e3c61eb22f759256003c9663edd660c6e876a61d5db7b3fd7d9e4d
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/child-current-corpus-context.json
  locator: Actual batch14 baseline
  summary: Both corpus commands exited 1 with 44 warnings across 16 of 477 records
    and zero errors; these are nonrequired context.
  support: supports
  accessed_at: '2026-10-22T02:55:49.516427Z'
  snapshot_sha256: b2f180af9d321c6ab29194c6df98d81025fc045a5a89aeb952ddc5e3e9a60d97
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/adapter-check.json
  locator: Owned runtime optional structured adapter
  summary: The optional adapter was unavailable; no external-checkout adapter was
    executed.
  support: supports
  accessed_at: '2026-10-22T02:55:49.516561Z'
  snapshot_sha256: 4db0dcb3997b4f0e063df042a8ea5f5cf10f4707212d1e06060c969a20ba4bd3
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/validate.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment reviewed separately.
  support: supports
  accessed_at: '2026-10-22T02:55:49.516952Z'
  snapshot_sha256: da62c406fa67a7b2f5228fdbedd668382dc49da82d097ecc63c2374fdb5ad077
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/validate-strict.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment reviewed separately.
  support: supports
  accessed_at: '2026-10-22T02:55:49.517140Z'
  snapshot_sha256: a5a9bc2c65857eca96d76dbde37fe6d2eff46f8171403589d4f4f7870cb48269
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/validate-terms.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment reviewed separately.
  support: supports
  accessed_at: '2026-10-22T02:55:49.517265Z'
  snapshot_sha256: 0803559aa3f60584f22cf2c7c97f522e80c170cfaa1f94cb69b50b6ab8736ce1
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/validate-references-explained.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment reviewed separately.
  support: supports
  accessed_at: '2026-10-22T02:55:49.517451Z'
  snapshot_sha256: 3d320e6c5917afcbea8d933c243d4994000ea3cd4c44b053405a8aea62cd0830
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/validate-gtdb.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment reviewed separately.
  support: supports
  accessed_at: '2026-10-22T02:55:49.517629Z'
  snapshot_sha256: 4a4cd5aea8deb3209a39c076126eac7f7ddcd10cc7adf2190b57730fdc65cc40
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/validate-gtdb-domain.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment reviewed separately.
  support: supports
  accessed_at: '2026-10-22T02:55:49.517794Z'
  snapshot_sha256: d5ce07578c6bf8deb825f4c0d3d843faad59eccc4f5d56f151292567972c574b
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/validate-history.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment reviewed separately.
  support: supports
  accessed_at: '2026-10-22T02:55:49.517968Z'
  snapshot_sha256: a3957d4394b69bb824100263d46d587c5477e78b1ceb9e552a101201649db996
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000217/normalize-cache-names-check.json
  locator: Actual current command/stdout/stderr
  summary: Native exit 0; scientific entailment reviewed separately.
  support: supports
  accessed_at: '2026-10-22T02:55:49.518123Z'
  snapshot_sha256: d5bf9c973e67ed557f8cada70bbaf2ac4fcd20ac16aae34f6c7843b850f3e3f2
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/audit-network.json
  locator: Fresh batch14 corpus baseline
  summary: Actual exit 1 with 44 warnings across 16 of 477 records and zero errors.
  support: supports
  accessed_at: '2026-10-22T02:55:49.518354Z'
  snapshot_sha256: 3110e0bb1dbe3ea63b81aea82871ac4adb2915c8fce1d15249422d0f5db266c6
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/check-network-quality.json
  locator: Fresh batch14 corpus baseline
  summary: Actual exit 1 with 44 warnings across 16 of 477 records and zero errors.
  support: supports
  accessed_at: '2026-10-22T02:55:49.518533Z'
  snapshot_sha256: 18896ef4136601b37550cb5612abc06784abcbf982e4778cbf2b9c10368cb66a
assessments:
- assessment_id: identity
  area: identity
  topic: SC3 enrichment and aggregate members
  outcome: supported
  summary: The record denotes the laboratory SC3 mineral-transfer community, with
    valid natural origin and engineered state.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - record
  - culture
  - community
  - schema
  dimensions:
  - name: member_scope
    value: One genus, one species and two order-level descriptors
    definition: NCBITaxon:119977, NCBITaxon:412449, NCBITaxon:204441, NCBITaxon:2301;
      broader than the 12 source MAGs.
    evidence_ids:
    - ontology
    - community
  - name: setting
    value: Laboratory mineral enrichments from SC3 mine column
    definition: Natural provenance with serial experimental propagation; no defined-isolate
      assembly.
    evidence_ids:
    - culture
    - schema
  details: The four descriptors aggregate multiple recovered organisms, not four isolates.
    Keep physical laboratory environment and broad modeled acid-mine-drainage analogy
    separate from the originating column. No mandatory species split, missing-role
    invention or quantitative abundance threshold follows.
- assessment_id: node-0
  area: graph
  topic: Mineral- and Fraction-Associated Community Profiles
  outcome: supported
  summary: Retain observed mineral/fraction-associated profiles with the existing
    Fe-only and pooled-DNA limits.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - community
  - sampling
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[0]; name Mineral- and Fraction-Associated
    Community Profiles; scope COMMUNITY_LEVEL; interaction_type absent. Encoded taxa:
    {"source": null, "target": null, "participants": [{"id": "NCBITaxon:119977", "label":
    "Acidithiobacillus"}, {"id": "NCBITaxon:412449", "label": "Leptospirillum ferrodiazotrophum"},
    {"id": "NCBITaxon:204441", "label": "Rhodospirillales"}, {"id": "NCBITaxon:2301",
    "label": "Thermoplasmatales"}]}. Canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "42d5ef20c7d70c738e760e8b4027475f2e0ad0d1dcd1f305416458c33df056d2",
    "reference": "PMID:41381092", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 d6dcd2f92cba07f0ca08bd64a285c4c5ea2dfc60e2eb98979369eccbfde7bad8.
    PMID:41381092 locator: Fresh MED Abstract abundance-trend sentence; Methods 2.4;
    Results 3.2; Figure 2 and Table S2. Retain SUPPORT/IN_VITRO. Different minerals
    co-vary in structure, sulfur chemistry, kinetics and iron; relative DNA profiles
    from pooled samples are not member-specific metabolic flux.'
- assessment_id: node-1
  area: graph
  topic: Plasmid-Encoded Functional Potential
  outcome: supported
  summary: Retain computational plasmid-encoded potential for the explicitly named
    host subset.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - plasmids
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[1]; name Plasmid-Encoded Functional
    Potential; scope COMMUNITY_LEVEL; interaction_type absent. Encoded taxa: {"source":
    null, "target": null, "participants": [{"id": "NCBITaxon:119977", "label": "Acidithiobacillus"},
    {"id": "NCBITaxon:412449", "label": "Leptospirillum ferrodiazotrophum"}]}. Canonical
    snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "b0bc2430c05c462e1dda5b079b916189258a38a78ff90c7b337af0bf801442fb",
    "reference": "PMID:41381092", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}].
    Snippet audit SHA256 d6dcd2f92cba07f0ca08bd64a285c4c5ea2dfc60e2eb98979369eccbfde7bad8.
    PMID:41381092 locator: Fresh MED Abstract plasmid-functions sentence; Methods
    2.5; Results 3.3 paragraph 1 and Table 2. Retain SUPPORT/COMPUTATIONAL. Acidithiobacillus
    and Leptospirillum represent only the associated subset; the Alphaproteobacteria
    copper-resistance plasmid is not assigned to canonical Rhodospirillales or archaea.'
- assessment_id: node-2
  area: graph
  topic: Putative Acidithiobacillus Plasmid CRISPR Interference
  outcome: supported
  summary: Retain source-only, hypothesized plasmid interference without a measured
    competitive interaction.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - plasmids
  - snippets
  - schema
  details: 'Exact selector ecological_interactions[2]; name Putative Acidithiobacillus
    Plasmid CRISPR Interference; scope PAIRWISE; interaction_type absent. Encoded
    taxa: {"source": {"id": "NCBITaxon:119977", "label": "Acidithiobacillus"}, "target":
    null, "participants": []}. Canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet",
    "sha256": "be67eda95c87ff94159f3f71cf6101deda8331a52032c3dcfdc01623ff14a4fa",
    "reference": "PMID:41381092", "supports": "PARTIAL", "evidence_source": "COMPUTATIONAL"}].
    Snippet audit SHA256 d6dcd2f92cba07f0ca08bd64a285c4c5ea2dfc60e2eb98979369eccbfde7bad8.
    PMID:41381092 locator: Fresh MED Abstract CRISPR-spacer sentence; Methods 2.8;
    Results 3.3 paragraph 2 and Table 3. Retain PARTIAL/COMPUTATIONAL and HYPOTHESIZED.
    Plasmid_56_509 matches two unbinned Acidithiobacillus-like contigs; no target
    cleavage, exclusion, co-residence or reciprocal harm is measured.'
- assessment_id: topology
  area: graph
  topic: Zero downstream arrows
  outcome: supported
  summary: The three contextual findings do not require causal arrows between them.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - record
  - plasmids
  - provenance
  details: Preserve three untyped nodes and the source-only third node. Characterization/repertoire-to-example
    relationships do not establish a downstream dependency. No forced COMPETITION
    or reciprocal benefit tag.
- assessment_id: chemistry
  area: grounding
  topic: Mineral identity and nongraph causal wording
  outcome: concern
  summary: Valid mineral identifiers coexist with unsupported oxidation-state and
    surrogate/Fe-only explanations.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - chemistry
  - chemical-authority
  - ontology
  details: Apply the same co-varying mineral boundary already present in node 0 to
    related_ingredients. Fe(II) cycling is not the entire released iron pool; the
    two minerals are alternative treatments, not a simultaneously required mixture.
- assessment_id: cultivation
  area: completeness
  topic: Recoverable MAM and staged protocol
  outcome: concern
  summary: The source supplies a recipe and additional preparation details missing
    from the structured record.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - culture
  - sampling
  - schema
  details: Keep 28°C, no agitation, serial transfers and source-specified sampling.
    Replace unsupported exposure/settled-surface design rationale and unrelated-record
    commentary. No vessel capacity, working volume, gas regime or complete Atlas trace
    stock is inferred.
- assessment_id: taxonomy
  area: grounding
  topic: Current aggregate mappings versus study MAGs
  outcome: concern
  summary: Reference-wide cores reproduce, but their provenance and source-MAG distinction
    need clarification.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - gtdb
  - si-samples
  - semantics
  details: Table S2 names historical and GTDB-Tk classifications separately. Its Leptospirillum
    MAG maps to UBA4572 sp002387725 and Rhodospirillales MAG to Acidibrevibacterium
    fodinaquatile/Acetobacterales. These are original study-MAG results, not automatic
    replacements for current broad NCBI descriptors.
- assessment_id: resource-traceability
  area: provenance
  topic: Source-declared project and genome resources
  outcome: concern
  summary: Empty associated_datasets omits a verifiable source project and six pooled
    metagenomic samples.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - resources
  - resource-correction
  - si-runs
  - si-samples
  details: Add exact run/BioSample/MAG scope and ggKbase provenance; distinguish six
    runs from three pooled replicates per condition and from other-enrichment transcriptomes.
    Publication links remain valid.
- assessment_id: source-boundaries
  area: scope
  topic: Observations, potential and source conflicts
  outcome: supported
  summary: Measured chemistry and relative composition remain distinct from proposed
    organism and mobile-element mechanisms.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - community
  - plasmids
  - si-chemistry
  - si-figures
  - source-scope
  details: Figure 4 is explicitly genetic potential and Figure 5 literature-based
    mechanism. Unencoded value/fraction/quality inconsistencies are retained as limitations,
    not extra record defects. Existing description identifies spacer evidence; optional
    inferential wording can be harmonized without another finding.
- assessment_id: ownership
  area: ownership
  topic: Maintained input and historical context
  outcome: supported
  summary: Future repairs belong to the canonical YAML; prior graph corrections and
    dated access notes remain preserved.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - inspection
  - provenance
  details: The review does not close 1372, reopen 1369, overwrite the history or claim
    that old reviewers inspected today’s recovered SI.
- assessment_id: native
  area: schema
  topic: Focused validity and source support
  outcome: supported
  summary: Eight focused checks pass; contextual corpus failures and optional adapter
    limits remain explicit.
  target_ids:
  - CommunityMech:000217
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
  summary: Completeness 25; raw quality 109, capped 100.
  target_ids:
  - CommunityMech:000217
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 25
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields/roles block 0 because two members lack optional roles;
      environment 5 + three nodes 10 + external resources 5 + node metabolites 5.
      Two factors give 0; empty media/datasets give 0. Low score does not justify
      inventing roles.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 - 1 major*10 - 3 minor*2 + 20*min((3 evidence/3 nodes)/2,1) +
      15 COMPLETE = 109 raw, capped 100. Three untyped nodes, zero arrows; scoring
      is separate from source truth.
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
- finding_id: mineral-chemistry
  issue_key: cm-000217-mineral-chemistry
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material chemical/causal scope error outside the already qualified
    graph.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Correct mineral chemistry and Fe-only attribution
  description: The source describes Cu(I)/Fe(III) in chalcopyrite and primarily ferric
    soluble iron. It does not test a soluble Cu(II)/Fe(II)/sulfide equivalent or independently
    manipulate Fe while holding mineral structure and kinetics constant. Existing
    nongraph wording exceeds that evidence.
  target_ids:
  - CommunityMech:000217
  field_paths:
  - related_ingredients[0].relevance
  - related_ingredients[0].evidence[0].explanation
  - related_ingredients[1].relevance
  - related_ingredients[1].evidence[0].explanation
  - related_ingredients[2].relevance
  - related_ingredients[2].evidence[0].explanation
  evidence_ids:
  - chemistry
  - chemical-authority
  - community
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    role: canonical_record
  ownership_note: Maintained focal record owns repair. Historical/shared issues are
    context, not superseded or closed.
- finding_id: culture-protocol
  issue_key: cm-000217-culture-protocol
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable protocol, provenance or traceability gap;
    current community identity and qualified graph remain valid.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Recover MAM and remove invented design rationale
  description: The structured medium is empty despite a source recipe; setup notes
    infer a microbial-exposure and settled-surface purpose not stated by the authors.
    The mineral-specific passage stage is also recoverable.
  target_ids:
  - CommunityMech:000217
  field_paths:
  - growth_media
  - cultivation_setup[0].instrument_detail
  - cultivation_setup[0].notes
  evidence_ids:
  - culture
  - sampling
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    role: canonical_record
  ownership_note: Maintained focal record owns repair. Historical/shared issues are
    context, not superseded or closed.
- finding_id: gtdb-provenance
  issue_key: cm-000217-gtdb-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable protocol, provenance or traceability gap;
    current community identity and qualified graph remain valid.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Separate snapshot provenance from study MAG classifications
  description: Three mapping_source strings claim latest release/build metadata unsupported
    by filesystem mtime. Table S2 supplies relevant original MAG classifications that
    must remain distinguishable from rank-aggregate RF32/Acidithiobacillus/Thermoplasmatales
    mappings.
  target_ids:
  - CommunityMech:000217
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term
  - taxonomy[2].taxon_term.gtdb_classification
  - taxonomy[3].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - si-samples
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    role: canonical_record
  ownership_note: Maintained focal record owns repair. Historical/shared issues are
    context, not superseded or closed.
- finding_id: study-resources
  issue_key: cm-000217-study-resources
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: Bounded recoverable protocol, provenance or traceability gap;
    current community identity and qualified graph remain valid.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Add declared project and genome-resource traceability
  description: The paper and supplements identify raw metagenomes and derived genomes/plasmids,
    while associated_datasets is empty and external resources list only the publication.
  target_ids:
  - CommunityMech:000217
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - resources
  - resource-correction
  - si-runs
  - si-samples
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    role: canonical_record
  ownership_note: Maintained focal record owns repair. Historical/shared issues are
    context, not superseded or closed.
actions:
- action_id: repair-chemistry
  description: Align nongraph chemistry with the actual mineral comparison.
  finding_ids:
  - mineral-chemistry
  target_ids:
  - CommunityMech:000217
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Retain CHEBI86202 chalcopyrite, CHEBI51114 copper(I) sulfide and CHEBI29033 iron(2+).
    Explain the source Cu(I)/Fe(III) mineral description separately from ChEBI’s disconnected-ion
    representation and dissolved Cu(II)/Fe cycling.
  - Remove the untested soluble-surrogate equivalence and claim that Fe(II) alone
    was manipulated. Describe co-varying mineral structure, sulfur chemistry, dissolution
    kinetics and mineral-derived iron, matching node 0.
  - Describe alternative chalcopyrite and chalcocite treatment arms, not simultaneous
    addition of both phases. Preserve measured community/chemistry outcomes and all
    three qualified nodes, without adding causal arrows.
- action_id: recover-culture
  description: Encode the reported MAM and staged enrichment with unresolved details
    explicit.
  finding_ids:
  - culture-protocol
  target_ids:
  - CommunityMech:000217
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - 'Use Methods 2.1 paragraph 3: per litre 0.4 g(NH4)2SO4,0.4 g KH2PO4,0.4 g MgSO4·7H2O,1
    mL trace stock including W/Se cited to Atlas 2004, pH 1.5 adjusted with H2SO4.
    Preserve the heptahydrate and do not invent the trace-stock formulation.'
  - Separate approximately 0.5 g source slurry, ten initial 28°C/no-agitation transfers
    with 5% inoculum every 2 months, and five subsequent same-mineral passages stated
    in Figure 1. Preserve three biotic and three abiotic replicates per mineral and
    six pooled sequencing samples.
  - Keep the source 0.25 g mineral wording and its per-litre/per-enrichment ambiguity;
    do not derive a one-litre working volume, vessel capacity or supplied-gas regime.
    State BATCH at the individual incubation stage with transfers separately.
  - Replace exposure and agitation-purpose conjecture with the authors’ mineral integrity/oxidation-state
    rationale, maximum 50 µm particles, XRD check and no microbes observed in abiotic
    controls. Remove unrelated-record/editorial notes.
  - 'Keep exact source conflicts visible: chemical 0/4/6 caption versus 0/4/8 Methods/S3,
    and week 4 mixed caption versus liquid Methods. Do not silently harmonize.'
- action_id: repair-gtdb
  description: Preserve valid reference mappings and add accurate source-MAG provenance.
  finding_ids:
  - gtdb-provenance
  target_ids:
  - CommunityMech:000217
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - 'Retain current reference aggregate cores: Acidithiobacillus 158/212 with four
    total destinations, Rhodospirillales→RF32 1269/1802 with 15 total destinations,
    Thermoplasmatales 63/63 with one. is_reclassified is a name comparison, not proof
    of study-organism reclassification.'
  - Record actual snapshot SHA256 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    and rank routes. Do not turn observed filesystem mtime into release latest or
    build date.
  - Document Table S2 Organisms row 3 SAMN44253046 as original GTDB-Tk v1.3.0 UBA4572
    sp002387725 and row 9 SAMN44253047 as Acidibrevibacterium fodinaquatile in Acetobacterales.
    Preserve source historical names and distinguish these MAG-specific results from
    current rank mappings; do not blanket-replace the NCBI descriptors or invent strain
    identity.
  - The current exact Leptospirillum species lookup remains unresolved; a source-MAG
    classification is separate evidence, not proof of a universal species-level crosswalk.
- action_id: add-resources
  description: Link source-specific sequencing and derived genome resources.
  finding_ids:
  - study-resources
  target_ids:
  - CommunityMech:000217
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Add PRJNA1170356 and the six exact Table S1 run mappings SRR30914516 through SRR30914511,
    preserving 4/8-week/mineral/fraction and pooled-replicate scope. These are metagenomes;
    project-level transcriptome remarks concern other enrichments.
  - Link https://ggkbase.berkeley.edu/cu_bioleaching_organisms_and_plasmids and Table
    S2’s twelve MAG BioSample identities SAMN44253036–SAMN44253047 with exact row
    labels. BioSamples are not assemblies or isolate genome_accession values. Preserve
    the 12 putative plasmid context without inventing separate accession assignments.
  - Use registry and source evidence at each added resource. Do not promote S1 phylogeny
    reference genomes or generic analysis tools to focal study deposits.
- action_id: validate-future-curation
  description: Run required validation after separately authorized repair.
  finding_ids:
  - mineral-chemistry
  - culture-protocol
  - gtdb-provenance
  - study-resources
  target_ids:
  - CommunityMech:000217
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cyprus_Copper_Sulphide_Bioleaching_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Recheck exact source snippets and narrow assertion support, taxonomy/chemical
    labels, all node selectors and graph directions. Run focused schema, strict, terms,
    explained references, GTDB/domain and history gates.
  - After authorized record changes run just gen-html and just check-docs-current.
    Preserve original history/source/caches and record append-only curation provenance;
    this review itself performs no canonical repair, Git operation, issue mutation
    or status promotion.
limitations:
- No raw sequencing, read-mapping, phylogenetic or statistical reanalysis was performed.
  Source gene and spacer annotations remain potential and association.
- The source reverses 0.93/2.1g/L parenthetic mineral labels, and S3 time-zero Cu
  cell E5 says 90 g/L unlike the plot. Figure 1 chemical sampling 0/4/6 conflicts
  Methods/S3 0/4/8; Figure 2 week 4 mixed-fraction caption conflicts Methods liquid
  sampling. These unencoded inconsistencies are not new record findings.
- Methods says all downstream MAGs pass 10% contamination, but Table S2 Organisms
  M8 is 13.48%. Preserve that source-quality limitation when reusing its classifications.
- The complete Atlas trace-stock formulation and laboratory working volume are not
  supplied by the inspected focal material. Figure flask cartoons do not establish
  a numerical fill or explicit vessel specification.
- Reference-wide GTDB mappings, original study GTDB-Tk assignments and phylogenetic
  comparator accessions have separate scope. No new modern classification or isolate
  identity is certified.
notes:
- Three node assessments bind all three canonical snippet hashes and exact participants;
  the record has zero arrows. The sole direct quotation is two words from Methods
  2.1 paragraph 3.
- All 31 inspected inputs are unchanged. Parent-owned candidate validation, saving
  and post-save gates follow this source assessment; no future success is asserted.
tags:
- record-review
- biomining
- full-source
- batch-14
```
