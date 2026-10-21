# Cellulose methane coculture roles, cultivation and provenance review

- Review: 20261021T214532Z-cellulose-methane-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T21:39:46.683653Z
- Finished UTC: 2026-10-21T21:45:32.806061Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full-source review identifies one major unsupported donor CROSS_FEEDER annotation and two minor cultivation-context and GTDB-provenance issues. Retain both strain identities, ordinal abundance and the qualified three-node/two-arrow graph. Eight focused native checks pass; completeness 95, raw quality 121/capped 100.

## Scope And Provenance

Whole maintained record, fresh focal main and complete declared SI, all main/SI figures, current authority and provenance assessed.

Selection: Only released CommunityMech:000174 in owned batch 12.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95812d3412d5aab41fd03422340cf736ac7b56f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000174 | kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml | maintained | Clostridium cellulovorans-Methanosarcina barkeri Cellulose Methane Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000174 | Focused native command exit 0. |
| validate-strict | passed | True | CommunityMech:000174 | Focused native command exit 0. |
| validate-terms | passed | True | CommunityMech:000174 | Focused native command exit 0. |
| validate-references-explained | passed | True | CommunityMech:000174 | Focused native command exit 0. |
| validate-gtdb | passed | True | CommunityMech:000174 | Focused native command exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000174 | Focused native command exit 0. |
| validate-history | passed | True | CommunityMech:000174 | Focused native command exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000174 | Focused native command exit 0. |
| audit-network | failed | True | CommunityMech:000174 | Same-batch corpus diagnostic retained. |
| check-network-quality | failed | True | CommunityMech:000174 | Same-batch corpus diagnostic retained. |
| Claim-critical source assessment | passed | True | CommunityMech:000174 | Whole focal main and declared supplement, all figures, table and equations assessed. |
| Reference-specific excerpt verification | passed | True | CommunityMech:000174 | 28 strict fresh/MD matches: 24 abstract and four body-only. |
| Ontology and schema semantics | passed | True | CommunityMech:000174 | 13 pairs/33 occurrences match; source-specific roles and mappings assessed. |
| Optional structured adapter | unavailable | False | CommunityMech:000174 | Fresh owned-runtime availability plus explicit prior discovery reuse. |
| Raw-data or experimental reproduction | skipped | False | CommunityMech:000174 | No raw assay, genome, image or biological reanalysis. |

## Scientific And Domain Assessments

### Focal membership, origin and environment

identity: supported. Targets: CommunityMech:000174.

The record denotes the intended defined laboratory pair.

Keep both exact strain terms, SYNTHETIC origin, ENGINEERED state and the laboratory environment. Exclude the separately tested M. mazei comparator, monoculture controls and catalogue media from focal membership/protocol.

### Strain mappings and provenance

grounding: concern. Targets: CommunityMech:000174.

Core taxonomy and GTDB values are sound; release/build wording is not verified.

Retain both exact-ID classifications and four/one genome counts. Correct snapshot provenance without replacing strain descriptors or interpreting is_reclassified as a new genomic result.

### Donor and recipient functional roles

scope: concern. Targets: CommunityMech:000174.

Donor CROSS_FEEDER lacks local recipient evidence.

The bacterium releases precursors and benefits functionally from a proposed product-removal feedback. Neither establishes a metabolite supplied by the methanogen that the bacterium utilizes. Retain donor PRIMARY_DEGRADER and the methanogen’s broad recipient roles; no obligatory dependence or nutrient-only criterion applies.

### ecological_interactions[0] and its downstream arrow

graph: supported. Targets: CommunityMech:000174.

Precursor provision is supported with unresolved individual contributions.

Keep C. cellulovorans-to-M. barkeri CROSS_FEEDING and the arrow to coculture-associated methanogenesis. Undetectable hydrogen is not a quantified gross transfer flux; formate use remains conditional. Other VFA products are not automatically methanogen substrates.

### ecological_interactions[1] and its downstream arrow

graph: supported. Targets: CommunityMech:000174.

The PARTIAL pathway node and HYPOTHESIZED feedback remain appropriate.

Retain the negative and mixed-substrate controls and source conceptual acetoclastic/CO2-reduction interpretation. The reverse taxon direction denotes proposed product-removal feedback, not reciprocal nutrient donation. No unique pH mediator, obligatory syntrophy or electron-contribution partition is established.

### ecological_interactions[2] and discussions[0]

graph: supported. Targets: CommunityMech:000174.

The untyped outcome node preserves functional improvement without reciprocal-growth inflation.

Keep measured improved degradation and smaller pH decline, unchanged fermenter growth, changed acid-production patterns and the existing mechanism discussion. No extra nodes or arrows are required.

### Description, taxon notes and related ingredients

consistency: supported. Targets: CommunityMech:000174.

Existing formate wording is scoped to the coculture and follows the source interpretation.

The graph/discussion already supplies the negative-control and unresolved-flux boundaries. Do not characterize current notes as proof of formate-only growth. Glucose-equivalent yield is not glucose feeding, and supplied CO2/bicarbonate is distinct from donor-derived carbon.

### Medium, atmosphere and preparation stages

scope: concern. Targets: CommunityMech:000174.

Stored setup numbers are correct, but explanatory notes and medium context need repair.

Remove unsupported claims about agitation impairing transfer and the supply-versus-atmosphere dichotomy. Recover explicit DCB-1 modifications and focal inoculation context. Preserve the unrecovered base recipe boundary; do not import revival or high-salt preculture concentrations into production without source support.

### Duration, pH and inoculum basis

quantity: supported. Targets: CommunityMech:000174.

Source values can be added only with their original measurement basis.

The 1.4:1 cell ratio differs from preculture transfer percentages. Main sampling through day 20 differs from 17 days of methane production, six months of acclimation and nine months of formate-only observation. Initial/endpoint pH values do not establish active pH control.

### Cell counts, gene expression and conceptual pathways

evidence: supported. Targets: CommunityMech:000174.

Genomic-DNA population qPCR and selected-gene RT-qPCR are distinct experiments.

Retain IN_VITRO assay provenance and conceptual-model qualifications. Ordinal ABUNDANT does not require equal fractions or a universal numerical threshold; it is not a substitute for source-specific measured abundance.

### CHEBI/GO scope and metal relevance

grounding: supported. Targets: CommunityMech:000174.

Terms correctly identify the stated substrate, products and processes.

Cellulose catabolism belongs to the bacterium and methanogenesis to the archaeon. Chemical co-listing does not establish transfer direction. Salts or trace constituents do not establish a metal-processing purpose; keep NOT_APPLICABLE.

### Reference identity and exact text

evidence: supported. Targets: CommunityMech:000174.

All 28 excerpt occurrences strictly match fresh source and the MD cache.

Twenty-four occur in the abstract and four only in the body. The MD header says abstract_only despite appended full main, while TXT is short abstract text. This is a cache-provenance boundary, not a failed snippet or a claim that caches were refreshed.

### Publication, declared supplement and datasets

representation: supported. Targets: CommunityMech:000174.

The publication link and accessible supplement have verified identities.

Primer and processed RT-qPCR tables are source supplemental data; assay Gene IDs and prior genomes are background context. Empty associated_datasets does not establish a missing mandatory deposit. No cross-Mech medium equivalence is asserted.

### Historical repair and current follow-up

provenance: supported. Targets: CommunityMech:000174.

The prior graph repair is preserved and shared non-graph ownership remains open.

Current 1326 is closed and 1327 is open. This single-record review neither closes shared findings for other records nor repeats older numerical-abundance assumptions against the current ordinal schema.

### Native results and scientific completion

schema: supported. Targets: CommunityMech:000174.

Eight focused checks pass; current-claim scientific review is completed.

Actual corpus diagnostic outcomes are retained separately. Native checks do not certify scientific interpretation; all current claim-critical focal sources were assessed. The inherited base-medium access limit is explicit.

### Native scores and finding counts

completeness: supported. Targets: CommunityMech:000174.

Completeness 95; raw quality 121, capped 100.

## Findings

### support-donor-recipient-role: Support or omit the donor recipient role

major / open / confirmed; issue key: cm-000174-support-donor-recipient-role.

C. cellulovorans carries CROSS_FEEDER, but the source establishes its metabolite donation and a proposed benefit from product removal rather than utilization of a partner-derived metabolite. Identify a provider, metabolite and source-local utilization evidence before retaining this optional recipient role; otherwise omit CROSS_FEEDER for this donor. Retain PRIMARY_DEGRADER, methanogen roles and the qualified graph. Do not claim reciprocal utilization is impossible.

### separate-culture-stages: Clarify focal medium and culture stages

minor / open / confirmed; issue key: cm-000174-separate-culture-stages.

Correct stored bottle/volume/temperature/static values coexist with an unsupported agitation rationale, a false distinction between gas supply and atmosphere, and an incomplete abstract-tier medium description despite available full Methods. Document focal DCB-1 modifications, initial cellulose, gas/bicarbonate and inoculum cell ratio with exact Methods evidence; separate revival, precultures, formate controls and production. Remove the unsupported agitation explanation and workflow clutter, retain both atmosphere and resource scope, and mark the inherited base recipe unresolved rather than import unrelated conditions.

### document-gtdb-snapshot: Document the verified GTDB snapshot

minor / open / confirmed; issue key: cm-000174-document-gtdb-snapshot.

Both valid exact-strain GTDB blocks describe the mapping as latest and built on a date that is only the checked local file mtime. Record verified crosswalk SHA and exact-ID method, labeling mtime only as snapshot metadata unless independent release/build evidence is available. Retain the current taxa, lineages, majority fractions and four/one genome counts.

## Recommended Actions And Acceptance Checks

### resolve-donor-role

Attach recipient evidence or omit the unsupported optional donor role.

- For taxonomy[0].functional_role CROSS_FEEDER, identify the partner provider, metabolite and source-local utilization evidence before retention; otherwise omit this role. Product donation, improved degradation, aggregation and relief from product accumulation alone do not establish utilization of another taxon metabolite.
- Retain donor PRIMARY_DEGRADER and M. barkeri CROSS_FEEDER/SYNTROPHIC_PARTNER, the three existing nodes, both qualified arrows and the open mechanism discussion. Do not impose obligacy or a nutrient-only criterion, and do not claim reciprocal utilization is biologically impossible.
- Preserve the source’s coculture-specific formate interpretation, nine-month formate-only failure, limited mixed-substrate monoculture consumption, unresolved individual flux and non-unique pH mediation. Current non-graph formate statements already name this coculture; do not falsely reclassify them as unconditional formate-growth claims.

### clarify-cultivation

Represent source-specific medium, gas and inoculation context.

- Retain 160-mL serum bottles, 100-mL working volume, 35°C and no shaking. Remove the unsupported claim that agitation opposes gas balance or interspecies transfer. Headspace CO2/N2 20:80 is both gas composition and a supplied resource, not mutually exclusive categories. Do not invent pressure, flow or continuous feed.
- Recover the focal 3 g/L cellulose and stated DCB-1 modifications: yeast extract 2 g/L, sodium chloride 10 g/L and magnesium sulfate 9.5 g/L, preserving the reported chemical form without inventing a hydrate. Include sodium bicarbonate 2.5 g/L with exact Analytical analyses evidence. Full inherited reference-23 formulation remains unresolved; do not silently reconstruct it from another study or catalogue.
- Keep the authors’ only-substrate designation scoped to the cellulose amendment while recording yeast extract, supplied CO2 and bicarbonate. Do not claim chemically exclusive carbon. Replace stale abstract-tier preparation prose with precise Methods evidence and remove cross-record workflow/issue narration from biological notes.
- Separate collection revival, C. cellulovorans 5% v/v preculture transfer, methanogen 10% v/v transfer to high-salt medium with 50 mM acetate, six-month initial acclimation and routine two-week propagation from the focal production assay. Use the focal 1.4:1 cell ratio in suitable setup notes; do not insert it as a transfer percentage or absolute inoculum density, and do not use the comparator 1.7:1 ratio.
- Keep genomic-DNA cell counting separate from selected-gene RNA/RT-qPCR. Initial pH 7.5 ± 0.02 and endpoint 6.7 ± 0.06 are observations, not active pH-control settings. Main trajectories extend 20 days; 17 days is the reported methane-production duration. Formate-only nine-month observation and mixed-substrate controls are separate arms.

### document-mapping

Replace unsupported release/build wording with verified mapping provenance.

- Preserve exact NCBITaxon:573061 and 269797, their current lineages, majority fractions 1.0 and genome counts four/one. Both resolve via ncbi_id; no species/strain replacement or count transfer is required.
- Record crosswalk SHA 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd and exact lookup method. Label the July 25 local mtime as file snapshot metadata, not a verified release named latest or a build date. Keep is_reclassified as the helper’s name-comparison flag.
- Keep identity support distinct from access: direct DSM 3052 confirms 743B/ATCC 35296; DSM 804 direct access failed, but source Methods and current NCBI related synonym support Fusaro/DSM 804. Do not import catalogue maintenance media or the M. mazei comparator.

### verify-future-curation

Validate separately authorized repairs without altering existing evidence scope.

- Attach exact source-local evidence to each changed claim. Preserve the qualified graph, ordinal ABUNDANT and current strain identities. Optional SI links may identify processed expression/control data, but no mandatory raw-deposit omission is established.
- Any future cache metadata or Methods enrichment must preserve source/version boundaries and both existing cache files through the authorized workflow. The MD contains appended full main despite its abstract_only header; the TXT is short abstract text. Do not move supplement text into the article cache.
- After authorized canonical changes, append required history and run schema, strict, terms, references, GTDB, domain and history checks, then regenerate and check HTML. This review changes no canonical record, cache, history or generated output; parent persistence is limited to the new review bundle after whole-candidate audits.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml; Whole maintained record | supports | The defined cellulose-to-methane pair has three nodes and two qualified arrows. Graph interpretation already distinguishes measurements, negative controls and proposed mediation. |
| identity | PMID:28191038; DOI:10.1186/s13068-017-0719-y; Abstract Background; Methods: Cultures and growth conditions, paragraphs 1–2 | supports | The focal pair is C. cellulovorans 743B/ATCC 35296 and M. barkeri Fusaro/DSM 804. M. mazei DSM 3647 is a separately tested comparator. The laboratory assembly supports SYNTHETIC origin and ENGINEERED state, without implying genetic modification. |
| medium | PMID:28191038; DOI:10.1186/s13068-017-0719-y; Methods: Cultures and growth conditions, paragraphs 1–2; Analytical analyses | supports | The focal medium uses 3 g/L cellulose and DCB-1 with stated modifications of 2 g/L yeast extract, 10 g/L sodium chloride and 9.5 g/L magnesium sulfate. CO2/N2 20:80 fills the headspace; sodium bicarbonate 2.5 g/L supplies additional inorganic carbon. The source calls cellulose the only amended substrate, which does not establish chemical carbon exclusivity. Inherited base formulations in references 23–24 were not recovered. |
| stages | PMID:28191038; DOI:10.1186/s13068-017-0719-y; Methods: Cultures and growth conditions, paragraphs 1–2 | supports | Revival uses collection-recommended media. C. cellulovorans preculture transfers 5% v/v to modified DCB-1; methanogens transfer 10% v/v to high-salt medium with 50 mM acetate. Their initial six-month acclimation and subsequent two-week propagation are separate from focal production. Mid-exponential monocultures supply the focal 1.4:1 C. cellulovorans:M. barkeri cell ratio; the comparator uses 1.7:1. |
| operation | PMID:28191038; DOI:10.1186/s13068-017-0719-y; Methods: Cultures and growth conditions, paragraph 2; Analytical analyses | supports | Experiments use 160-mL serum bottles, 100-mL medium and 35°C without shaking. These stored numeric conditions are correct. The paper does not compare agitation treatments or establish that agitation impairs transfer. Gas composition is both a headspace atmosphere and a deliberately supplied resource; a supply-versus-atmosphere exclusion is unwarranted. |
| sampling | PMID:28191038; DOI:10.1186/s13068-017-0719-y; Methods: Analytical analyses; Results: Methanogenesis and cellulose utilization; Fermentation products and pH; Figures 1–3 | supports | Gas concentrations are measured by GC and converted to total moles with gas/liquid volumes and Henry constants. Two-mL samples support pH, product, cellulose and density assays. CO2 production is not quantified because external CO2 and bicarbonate are supplied. Main trajectories extend 20 days; the text separately reports a 17-day methane-production duration. Initial pH 7.5 ± 0.02 and focal endpoint 6.7 ± 0.06 are observed values, not an actively maintained pH setpoint. |
| precursors | PMID:28191038; DOI:10.1186/s13068-017-0719-y; Results: Methanogenesis and cellulose utilization; Fermentation products and pH; Figures 1–2; Table 1 | supports | Coculture produces methane, has no detected hydrogen accumulation and shows transient accumulation followed by formate depletion and acetate near-depletion. The focal pair consumes 267 ± 16 mg cellulose and yields 0.87 ± 0.02 mol methane per mol glucose equivalent. These observations support the authors’ precursor-exchange interpretation, but pools combine production and consumption and do not resolve each transferred substrate or electron contribution. |
| controls | PMID:28191038; DOI:10.1186/s13068-017-0719-y; Methods: Cultures and growth conditions; Discussion: Coculturing C. cellulovorans with M. barkeri or M. mazei enabled direct conversion of cellulose to CH4, paragraph 1; Additional file 1: Figures S1–S4 | supports | No growth on 50 mM formate alone was observed after nine months. A mixed-substrate M. barkeri monoculture supplied with 10 mM formate, 3 mM acetate and 0.95 mmol H2 consumed only about 1.5 mM formate and little acetate. Its methane production and cell increase were lower than in coculture. These controls bound the conceptual formate pathway; the record’s non-graph statements already specify the coculture and do not assert formate-only growth. |
| feedback | PMID:28191038; DOI:10.1186/s13068-017-0719-y; Results: Fermentation products and pH; Cell growth and culture morphology; Discussion: Stabilization of pH by methanogens enhanced cellulose degradation; Figures 2–4 | supports | The focal coculture improves cellulose degradation by 13.8% and has a smaller pH decline. Lower butyrate/lactate accumulation is not net depletion by the methanogen. Altered production and consumption jointly support the proposed feedback. C. cellulovorans growth and yield do not significantly improve. Product-removal benefit does not identify a partner metabolite utilized by the donor. |
| expression | PMID:28191038; DOI:10.1186/s13068-017-0719-y; Methods: RNA extraction; Reverse transcription (RT)-qPCR; Results: Expression of genes in pathways; Discussion: Metabolic shifts in C. cellulovorans in cocultures; Figures 5–6 | supports | Separate RNA experiments examine 37 selected genes: 17 C. cellulovorans, 13 M. barkeri and seven comparator genes. Two biological cultures and two technical replicates per biological replicate support relative RT-qPCR; absolute fold-change ≥1.2 and p&lt;0.05 define differential expression. Figures 5–6 combine conceptual pathways with selected expression, not a whole-transcriptome experiment or direct flux measurement. |
| population | PMID:28191038; DOI:10.1186/s13068-017-0719-y; Methods: Cell density analysis; Results: Cell growth and culture morphology; Figure 4A; Additional file 1: Figure S4 | supports | Population estimates use genomic DNA qPCR against one-copy targets in each genome; this is distinct from RNA/RT-qPCR. C. cellulovorans reaches higher final density, while the focal methanogen grows with a shorter lag than acetate monocultures. The 1.4:1 inoculum ratio is not a persistent population fraction. Ordinal ABUNDANT remains valid and need not be replaced by a fixed percentage. |
| supplement | PMID:28191038, Additional file 1; Published Tables S1–S6 and Figures S1–S4; actual DOC internal Additional files 1–10 | supports | All six tables and four figure captions were read, and all four plots were viewed. Tables S1–S2 give target/control primers; S3 gives monoculture product yields; S4–S6 give selected-gene fold changes and p-values. Figures S1–S3 distinguish acetate and mixed-substrate monocultures; S4 compares cell-density increase. The source DOC uses a different internal sequence of labels, explicitly mapped in the asset receipt. |
| ontology | /private/tmp/cm-review-session/batch-12/000174/ontology-authority.json; Thirteen ID-label/definition/location pairs across 33 occurrences | supports | All encoded labels match. Seven CHEBI identities represent cellulose, hydrogen, formate, acetate, methane, carbon dioxide and glucose; identity does not establish transfer direction or source. Glucose is a yield-equivalent basis, not a supplied feed. |
| schema | /private/tmp/cm-review-session/batch-12/000174/child-schema-semantics.json; FunctionalRoleEnum, InteractionTypeEnum, AbundanceEnum and cultivation definitions | supports | CROSS_FEEDER means utilization of metabolites from other taxa. Broad SYNTROPHIC_PARTNER and the more specific product-removal SYNTROPHY interaction are distinct; no obligacy or nutrient-only test is imposed. ABUNDANT is ordinal. |
| gtdb | /private/tmp/cm-review-session/batch-12/000174/child-gtdb-crosswalk.json; Exact encoded strain rows 573061 and 269797, routes and snapshot | supports | Both mappings reproduce via ncbi_id: Clostridium_K cellulovorans at 1.0/four genomes and Methanosarcina barkeri_B at 1.0/one genome. Their classifications and lineages are valid. Local mtime does not verify a GTDB release called latest or its build date. |
| strain | /private/tmp/cm-review-session/batch-12/000174/child-strain-authority.json; Focal Methods, current NCBI ranks/parents and catalogue identity blocks | supports | Both terms are strain descriptors. Direct DSM 3052 catalogue links 743B and ATCC 35296. DSM 804 direct catalogue access failed, but the current NCBI authority explicitly lists DSM 804 as a related synonym of Fusaro 269797, agreeing with focal Methods. No alternate strain or catalogue medium is substituted. |
| semantics | /private/tmp/cm-review-session/batch-12/000174/ontology-semantic-notes.json; Final source-specific roles, graph, chemistry and cultivation boundaries | supports | Retain donor PRIMARY_DEGRADER, recipient CROSS_FEEDER/SYNTROPHIC_PARTNER, ordinal ABUNDANT and the qualified three-node/two-arrow graph. Donor CROSS_FEEDER needs actual utilization evidence or omission of the optional role. |
| base-medium | /private/tmp/cm-review-session/batch-12/000174/root-medium-reference-scope.json; Scoped public access attempts for references 23 and 24 | supports | Metadata verifies DCB-1 reference DOI 10.1128/AEM.02574-06 and high-salt reference DOI 10.1128/AEM.02680-08. Full recipes were not recovered after EPMC errors and blocked alternate routes. Focal modifications are directly supported; no inherited concentrations or other-study substrates are imported. |
| resources | /private/tmp/cm-review-session/batch-12/000174/dataset-verification.json; Publication identity, exact legacy DOC/package and data-availability statements | supports | The PMID identifies the primary publication. The article points to its own text and SI; exact DOC/ZIP identity and six-table/four-figure mapping are verified. Source gene IDs are assay targets, not new deposits. A bounded article/SI scan found no named archive identifier; no mandatory dataset omission finding is inferred. |
| snippets | /private/tmp/cm-review-session/batch-12/000174/snippet-audit.json; Twenty-eight reference-specific excerpt occurrences | supports | All 28 occurrences strictly match fresh XML and the MD cache: 24 abstract and four body-only. The short TXT cache supports 24. Literal matching verifies text, not donor recipient-role support or causal mediation. |
| history | /private/tmp/cm-review-session/batch-12/000174/provenance-audit.json; Whole history, exact batch 19 row/adversarial context and current 1326/1327/529 bodies/comments | supports | Issue 1326 is closed after graph qualification; shared 1327 remains open and owns non-graph follow-up; 529 is closed contextual provenance. All comments were read. The older quantitative-abundance request is assessed against the current ordinal schema rather than automatically repeated. This review does not close shared issues or reassess their other records. |
| historical-source | /private/tmp/cm-review-session/batch-12/000174/historical-source-byte-comparison.json; Prior XML digest versus fresh bytes | supports | Fresh main XML equals the prior recorded digest. The old path is inert historical metadata, not an active pin exception or a reconstructed source. |
| inspect | /private/tmp/cm-review-session/batch-12/000174/inspect.json; Fresh official 27-input inspection | supports | The target, both cache extensions, sole history, exact batch 19 decision/adversarial and 21 authorities were inspected before assessment. Ignored-inclusive bounded discovery found no other focal prior review; broad corpus logs were not treated as scientific evidence. |
| assets | /private/tmp/cm-review-session/batch-12/000174/lead-source-assets.json; Seventeen package members and local legacy-DOC rendering | supports | Six main JPEGs, six thumbnails, four equation GIFs and one DOC were acquired. All six main figures and four SI figures were viewed. The original DOC is preserved; text conversion omitted images, so a separate local PDF render supplied the pixels. Initial acquisition/rendering failures are retained as scratch attempts, not native validation failures. |
| lead-read | /private/tmp/cm-review-session/batch-12/000174/lead-primary-read-scope.json; Whole main, 41 references, Table 1, four equations and complete declared SI | supports | Lead read all main scientific sections and references, all six supplementary tables and captions, and all ten main/SI figures. Full source and authority scopes are explicit; no raw assay reanalysis or model execution occurred. |
| source-scope | /private/tmp/cm-review-session/batch-12/000174/source-audit.json; Final three finding groups and completion | supports | Completed scientific assessment finds one major donor-role support issue and two minor cultivation/provenance issues. Formate claims remain author-supported and coculture-scoped; they are not graded as unconditional formate-growth claims. |
| root-source | /private/tmp/cm-review-session/batch-12/000174/root-independent-source-audit.json; Independent primary, supplement, authority and provenance assessment | supports | Root independently assessed the current scientific claims and agrees with the final three groups and completion. Its actual reading and bounded base-recipe access are recorded separately. |
| metrics | /private/tmp/cm-review-session/batch-12/000174/support-final-audit.json; Distinct final support, counts and native arithmetic | supports | Completeness 95. Eight evidence occurrences across three nodes give mean 8/3. With COMPLETE network and one major/two minor findings, raw quality is 121, capped at 100. All 27 inspected input bytes remain unchanged. |
| support-manifest | /private/tmp/cm-review-session/batch-12/000174/supporting-artifact-manifest.json; Final support artifacts and exact hashes | supports | Final provenance, resource, snippet and source scopes are pinned. Preliminary support remains immutable. |
| auxiliary | /private/tmp/cm-review-session/batch-12/000174/auxiliary-frozen-manifest.json; Final native and authority receipts | supports | Eight focused native checks pass; all 13 ontology pairs across 33 occurrences match. Core strain mappings are retained. No canonical/cache mutation occurred. |
| final-native | /private/tmp/cm-review-session/batch-12/000174/final-validator-summary.json; Actual eight command outcomes and final input integrity | supports | Schema, strict, term, reference, GTDB, domain, history and cache-name checks pass. Initial validator summary remains unchanged. Native success does not establish scientific entailment. |
| adapter | /private/tmp/cm-review-session/batch-12/000174/adapter-check.json; Fresh batch 12 runtime checks; explicit batch 11 record 403 discovery reuse at 2026-10-21T19:20:45.556660+00:00 | supports | PATH/module/owned-venv availability was freshly checked. The ignored-inclusive filename search is explicitly the prior batch 11 search, not a new batch 12 search. The other-checkout runner was not executed; no global absence or installation is claimed. |
| check-validate | /private/tmp/cm-review-session/batch-12/000174/validate.json; Actual focused command and output | supports | Recorded native outcome; biological entailment independently assessed. |
| check-validate-strict | /private/tmp/cm-review-session/batch-12/000174/validate-strict.json; Actual focused command and output | supports | Recorded native outcome; biological entailment independently assessed. |
| check-validate-terms | /private/tmp/cm-review-session/batch-12/000174/validate-terms.json; Actual focused command and output | supports | Recorded native outcome; biological entailment independently assessed. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-12/000174/validate-references-explained.json; Actual focused command and output | supports | Recorded native outcome; biological entailment independently assessed. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-12/000174/validate-gtdb.json; Actual focused command and output | supports | Recorded native outcome; biological entailment independently assessed. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-12/000174/validate-gtdb-domain.json; Actual focused command and output | supports | Recorded native outcome; biological entailment independently assessed. |
| check-validate-history | /private/tmp/cm-review-session/batch-12/000174/validate-history.json; Actual focused command and output | supports | Recorded native outcome; biological entailment independently assessed. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-12/000174/normalize-cache-names-check.json; Actual focused command and output | supports | Recorded native outcome; biological entailment independently assessed. |
| check-audit-network | /private/tmp/cm-review-session/batch-12/audit-network.json; Same-batch corpus diagnostic | supports | Actual corpus result retained; later records are not assessed. |
| check-check-network-quality | /private/tmp/cm-review-session/batch-12/check-network-quality.json; Same-batch corpus diagnostic | supports | Actual corpus result retained; later records are not assessed. |

## Limits And Additional Notes

- Full focal main, all six main figures, Table 1, four equations, 41 references, all six SI tables and four SI figures were assessed. The original legacy DOC was locally rendered; its internal Additional file labels differ from the published S-table/S-figure labels, with the mapping preserved.
- Inherited DCB-1 and high-salt reference formulations were not recovered after bounded public attempts. Focal modifications are directly supported; no unrelated-study substrates or catalogue recipes are imported. This does not prevent assessment of current focal claims.
- No raw assay reanalysis, image digitization, gene-database reannotation, genome classification or biological experiment was performed. Metabolite pools and selected expression do not resolve every transferred molecule or isolate unique pH mediation.
- All 28 field excerpt occurrences strictly match fresh source and MD cache, partitioned 24 abstract/four body-only; TXT supports 24. Matching is not scientific entailment. Both caches remain unchanged, including the MD abstract_only metadata/full-main boundary.
- Direct DSM 804 catalogue access failed; source Methods and current NCBI synonym support the identity. Current mappings are exact local snapshot evidence, not a new genome analysis or verified release/build date.
- Optional adapter availability was freshly checked in batch 12 while filename-search discovery is explicitly reused from batch 11 record 403. No other-checkout runner or paid source was used. Historical XML paths remain inert metadata, and initial support/validator receipts are immutable.
- Completed scientific review; one major/two minor findings; completeness 95, raw quality 121/capped 100.
- No unconditional formate-growth, mandatory dataset or fixed-percentage abundance finding.
- No canonical changes or save by lead; parent persistence follows independent whole-candidate acceptance.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T214532Z-cellulose-methane-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Cellulose methane coculture roles, cultivation and provenance review
started_at: '2026-10-21T21:39:46.683653Z'
finished_at: '2026-10-21T21:45:32.806061Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed science, authority and support; no
    person-level independence asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Full-source review identifies one major unsupported donor CROSS_FEEDER annotation
  and two minor cultivation-context and GTDB-provenance issues. Retain both strain
  identities, ordinal abundance and the qualified three-node/two-arrow graph. Eight
  focused native checks pass; completeness 95, raw quality 121/capped 100.
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
  - path: history/records/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture/2026-10-05T234231Z-codex-aa4e0f.yaml
    sha256: 605c4bed76e99cfdc79dd6c76147abd0c1a836a9402e96348755019a35eb8883
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
    sha256: c6b526dc6a76ffb307bdd56cc43df3b3365fc2def4fe027d53924869f5746d78
    role: target
  - path: references_cache/PMID_28191038.md
    sha256: fb32f16dc75d0e39eee473d5d206a61e8a3e704b92311d465041f84559684043
    role: context
  - path: references_cache/PMID_28191038.txt
    sha256: 49ca6d1ea53da6637ee0f6d52d7b4f6489dbef5e67007f12a1759b8ad4fd4b5e
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
- target_id: CommunityMech:000174
  path: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
  label: Clostridium cellulovorans-Methanosarcina barkeri Cellulose Methane Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
    role: canonical_record
scope:
  description: Whole maintained record, fresh focal main and complete declared SI,
    all main/SI figures, current authority and provenance assessed.
  selection: Only released CommunityMech:000174 in owned batch 12.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000174
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000174
  command: just --no-dotenv validate kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Owned batch 12 runtime; unchanged canonical inputs.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000174
  command: just --no-dotenv validate-strict kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-12/000174/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Owned batch 12 runtime; unchanged canonical inputs.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000174
  command: just --no-dotenv validate-terms kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Owned batch 12 runtime; unchanged canonical inputs.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000174
  command: just --no-dotenv validate-references-explained kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Owned batch 12 runtime; unchanged canonical inputs.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000174
  command: just --no-dotenv validate-gtdb kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Owned batch 12 runtime; unchanged canonical inputs.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000174
  command: just --no-dotenv validate-gtdb-domain kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Owned batch 12 runtime; unchanged canonical inputs.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000174
  command: just --no-dotenv validate-history history/records/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Owned batch 12 runtime; unchanged canonical inputs.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000174
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Owned batch 12 runtime; unchanged canonical inputs.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Same-batch corpus diagnostic retained.
  target_ids:
  - CommunityMech:000174
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-12/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - metrics
  scope_note: Explicit batch 12 diagnostic reuse; focused target checks pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Same-batch corpus diagnostic retained.
  target_ids:
  - CommunityMech:000174
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-12/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - metrics
  scope_note: Explicit batch 12 diagnostic reuse; focused target checks pass.
- check_id: scientific-source
  name: Claim-critical source assessment
  status: passed
  required: true
  summary: Whole focal main and declared supplement, all figures, table and equations
    assessed.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - lead-read
  - source-scope
  - root-source
- check_id: direct-excerpts
  name: Reference-specific excerpt verification
  status: passed
  required: true
  summary: '28 strict fresh/MD matches: 24 abstract and four body-only.'
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - snippets
- check_id: authority-review
  name: Ontology and schema semantics
  status: passed
  required: true
  summary: 13 pairs/33 occurrences match; source-specific roles and mappings assessed.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - ontology
  - schema
  - strain
  - gtdb
- check_id: adapter
  name: Optional structured adapter
  status: unavailable
  required: false
  summary: Fresh owned-runtime availability plus explicit prior discovery reuse.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - adapter
- check_id: reanalysis
  name: Raw-data or experimental reproduction
  status: skipped
  required: false
  summary: No raw assay, genome, image or biological reanalysis.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - lead-read
  - resources
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
  locator: Whole maintained record
  summary: The defined cellulose-to-methane pair has three nodes and two qualified
    arrows. Graph interpretation already distinguishes measurements, negative controls
    and proposed mediation.
  support: supports
  accessed_at: '2026-10-21T21:45:32.802702Z'
- evidence_id: identity
  kind: primary_source
  reference: PMID:28191038; DOI:10.1186/s13068-017-0719-y
  locator: 'Abstract Background; Methods: Cultures and growth conditions, paragraphs
    1–2'
  summary: The focal pair is C. cellulovorans 743B/ATCC 35296 and M. barkeri Fusaro/DSM
    804. M. mazei DSM 3647 is a separately tested comparator. The laboratory assembly
    supports SYNTHETIC origin and ENGINEERED state, without implying genetic modification.
  support: supports
  accessed_at: '2026-10-21T21:45:32.802764Z'
  snapshot_sha256: 341b838b72428a0cbc581db1acb8df23054e24ec8eddfdd8ca653d353f77bc16
- evidence_id: medium
  kind: primary_source
  reference: PMID:28191038; DOI:10.1186/s13068-017-0719-y
  locator: 'Methods: Cultures and growth conditions, paragraphs 1–2; Analytical analyses'
  summary: The focal medium uses 3 g/L cellulose and DCB-1 with stated modifications
    of 2 g/L yeast extract, 10 g/L sodium chloride and 9.5 g/L magnesium sulfate.
    CO2/N2 20:80 fills the headspace; sodium bicarbonate 2.5 g/L supplies additional
    inorganic carbon. The source calls cellulose the only amended substrate, which
    does not establish chemical carbon exclusivity. Inherited base formulations in
    references 23–24 were not recovered.
  support: supports
  accessed_at: '2026-10-21T21:45:32.802842Z'
  snapshot_sha256: 341b838b72428a0cbc581db1acb8df23054e24ec8eddfdd8ca653d353f77bc16
- evidence_id: stages
  kind: primary_source
  reference: PMID:28191038; DOI:10.1186/s13068-017-0719-y
  locator: 'Methods: Cultures and growth conditions, paragraphs 1–2'
  summary: Revival uses collection-recommended media. C. cellulovorans preculture
    transfers 5% v/v to modified DCB-1; methanogens transfer 10% v/v to high-salt
    medium with 50 mM acetate. Their initial six-month acclimation and subsequent
    two-week propagation are separate from focal production. Mid-exponential monocultures
    supply the focal 1.4:1 C. cellulovorans:M. barkeri cell ratio; the comparator
    uses 1.7:1.
  support: supports
  accessed_at: '2026-10-21T21:45:32.802905Z'
  snapshot_sha256: 341b838b72428a0cbc581db1acb8df23054e24ec8eddfdd8ca653d353f77bc16
- evidence_id: operation
  kind: primary_source
  reference: PMID:28191038; DOI:10.1186/s13068-017-0719-y
  locator: 'Methods: Cultures and growth conditions, paragraph 2; Analytical analyses'
  summary: Experiments use 160-mL serum bottles, 100-mL medium and 35°C without shaking.
    These stored numeric conditions are correct. The paper does not compare agitation
    treatments or establish that agitation impairs transfer. Gas composition is both
    a headspace atmosphere and a deliberately supplied resource; a supply-versus-atmosphere
    exclusion is unwarranted.
  support: supports
  accessed_at: '2026-10-21T21:45:32.802965Z'
  snapshot_sha256: 341b838b72428a0cbc581db1acb8df23054e24ec8eddfdd8ca653d353f77bc16
  quote: without shaking
- evidence_id: sampling
  kind: primary_source
  reference: PMID:28191038; DOI:10.1186/s13068-017-0719-y
  locator: 'Methods: Analytical analyses; Results: Methanogenesis and cellulose utilization;
    Fermentation products and pH; Figures 1–3'
  summary: Gas concentrations are measured by GC and converted to total moles with
    gas/liquid volumes and Henry constants. Two-mL samples support pH, product, cellulose
    and density assays. CO2 production is not quantified because external CO2 and
    bicarbonate are supplied. Main trajectories extend 20 days; the text separately
    reports a 17-day methane-production duration. Initial pH 7.5 ± 0.02 and focal
    endpoint 6.7 ± 0.06 are observed values, not an actively maintained pH setpoint.
  support: supports
  accessed_at: '2026-10-21T21:45:32.803029Z'
  snapshot_sha256: 341b838b72428a0cbc581db1acb8df23054e24ec8eddfdd8ca653d353f77bc16
- evidence_id: precursors
  kind: primary_source
  reference: PMID:28191038; DOI:10.1186/s13068-017-0719-y
  locator: 'Results: Methanogenesis and cellulose utilization; Fermentation products
    and pH; Figures 1–2; Table 1'
  summary: Coculture produces methane, has no detected hydrogen accumulation and shows
    transient accumulation followed by formate depletion and acetate near-depletion.
    The focal pair consumes 267 ± 16 mg cellulose and yields 0.87 ± 0.02 mol methane
    per mol glucose equivalent. These observations support the authors’ precursor-exchange
    interpretation, but pools combine production and consumption and do not resolve
    each transferred substrate or electron contribution.
  support: supports
  accessed_at: '2026-10-21T21:45:32.803095Z'
  snapshot_sha256: 341b838b72428a0cbc581db1acb8df23054e24ec8eddfdd8ca653d353f77bc16
- evidence_id: controls
  kind: primary_source
  reference: PMID:28191038; DOI:10.1186/s13068-017-0719-y
  locator: 'Methods: Cultures and growth conditions; Discussion: Coculturing C. cellulovorans
    with M. barkeri or M. mazei enabled direct conversion of cellulose to CH4, paragraph
    1; Additional file 1: Figures S1–S4'
  summary: No growth on 50 mM formate alone was observed after nine months. A mixed-substrate
    M. barkeri monoculture supplied with 10 mM formate, 3 mM acetate and 0.95 mmol
    H2 consumed only about 1.5 mM formate and little acetate. Its methane production
    and cell increase were lower than in coculture. These controls bound the conceptual
    formate pathway; the record’s non-graph statements already specify the coculture
    and do not assert formate-only growth.
  support: supports
  accessed_at: '2026-10-21T21:45:32.803156Z'
  snapshot_sha256: 341b838b72428a0cbc581db1acb8df23054e24ec8eddfdd8ca653d353f77bc16
- evidence_id: feedback
  kind: primary_source
  reference: PMID:28191038; DOI:10.1186/s13068-017-0719-y
  locator: 'Results: Fermentation products and pH; Cell growth and culture morphology;
    Discussion: Stabilization of pH by methanogens enhanced cellulose degradation;
    Figures 2–4'
  summary: The focal coculture improves cellulose degradation by 13.8% and has a smaller
    pH decline. Lower butyrate/lactate accumulation is not net depletion by the methanogen.
    Altered production and consumption jointly support the proposed feedback. C. cellulovorans
    growth and yield do not significantly improve. Product-removal benefit does not
    identify a partner metabolite utilized by the donor.
  support: supports
  accessed_at: '2026-10-21T21:45:32.803215Z'
  snapshot_sha256: 341b838b72428a0cbc581db1acb8df23054e24ec8eddfdd8ca653d353f77bc16
- evidence_id: expression
  kind: primary_source
  reference: PMID:28191038; DOI:10.1186/s13068-017-0719-y
  locator: 'Methods: RNA extraction; Reverse transcription (RT)-qPCR; Results: Expression
    of genes in pathways; Discussion: Metabolic shifts in C. cellulovorans in cocultures;
    Figures 5–6'
  summary: 'Separate RNA experiments examine 37 selected genes: 17 C. cellulovorans,
    13 M. barkeri and seven comparator genes. Two biological cultures and two technical
    replicates per biological replicate support relative RT-qPCR; absolute fold-change
    ≥1.2 and p<0.05 define differential expression. Figures 5–6 combine conceptual
    pathways with selected expression, not a whole-transcriptome experiment or direct
    flux measurement.'
  support: supports
  accessed_at: '2026-10-21T21:45:32.803277Z'
  snapshot_sha256: 341b838b72428a0cbc581db1acb8df23054e24ec8eddfdd8ca653d353f77bc16
- evidence_id: population
  kind: primary_source
  reference: PMID:28191038; DOI:10.1186/s13068-017-0719-y
  locator: 'Methods: Cell density analysis; Results: Cell growth and culture morphology;
    Figure 4A; Additional file 1: Figure S4'
  summary: Population estimates use genomic DNA qPCR against one-copy targets in each
    genome; this is distinct from RNA/RT-qPCR. C. cellulovorans reaches higher final
    density, while the focal methanogen grows with a shorter lag than acetate monocultures.
    The 1.4:1 inoculum ratio is not a persistent population fraction. Ordinal ABUNDANT
    remains valid and need not be replaced by a fixed percentage.
  support: supports
  accessed_at: '2026-10-21T21:45:32.803335Z'
  snapshot_sha256: 341b838b72428a0cbc581db1acb8df23054e24ec8eddfdd8ca653d353f77bc16
- evidence_id: supplement
  kind: primary_source
  reference: PMID:28191038, Additional file 1
  locator: Published Tables S1–S6 and Figures S1–S4; actual DOC internal Additional
    files 1–10
  summary: All six tables and four figure captions were read, and all four plots were
    viewed. Tables S1–S2 give target/control primers; S3 gives monoculture product
    yields; S4–S6 give selected-gene fold changes and p-values. Figures S1–S3 distinguish
    acetate and mixed-substrate monocultures; S4 compares cell-density increase. The
    source DOC uses a different internal sequence of labels, explicitly mapped in
    the asset receipt.
  support: supports
  accessed_at: '2026-10-21T21:45:32.803393Z'
  snapshot_sha256: 381ea3379eed71918b2ad0260ddb3feac747dc909df1a9f2ab93fbe6b2816d20
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000174/ontology-authority.json
  locator: Thirteen ID-label/definition/location pairs across 33 occurrences
  summary: All encoded labels match. Seven CHEBI identities represent cellulose, hydrogen,
    formate, acetate, methane, carbon dioxide and glucose; identity does not establish
    transfer direction or source. Glucose is a yield-equivalent basis, not a supplied
    feed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804450Z'
  snapshot_sha256: f0fb1c38c7cf013f66e3bb3c0343510b62d0b494694fb37b2ee0cd9befc3e7c2
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000174/child-schema-semantics.json
  locator: FunctionalRoleEnum, InteractionTypeEnum, AbundanceEnum and cultivation
    definitions
  summary: CROSS_FEEDER means utilization of metabolites from other taxa. Broad SYNTROPHIC_PARTNER
    and the more specific product-removal SYNTROPHY interaction are distinct; no obligacy
    or nutrient-only test is imposed. ABUNDANT is ordinal.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804494Z'
  snapshot_sha256: 9f0d3b826d072f1d7389eb8b511f4e02638acc9953642cc48fc52119fb858076
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000174/child-gtdb-crosswalk.json
  locator: Exact encoded strain rows 573061 and 269797, routes and snapshot
  summary: 'Both mappings reproduce via ncbi_id: Clostridium_K cellulovorans at 1.0/four
    genomes and Methanosarcina barkeri_B at 1.0/one genome. Their classifications
    and lineages are valid. Local mtime does not verify a GTDB release called latest
    or its build date.'
  support: supports
  accessed_at: '2026-10-21T21:45:32.804529Z'
  snapshot_sha256: fce8b9b237b77c7531b141b217867d866ec3a4d6bd8171a7e86c823d3113351b
- evidence_id: strain
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000174/child-strain-authority.json
  locator: Focal Methods, current NCBI ranks/parents and catalogue identity blocks
  summary: Both terms are strain descriptors. Direct DSM 3052 catalogue links 743B
    and ATCC 35296. DSM 804 direct catalogue access failed, but the current NCBI authority
    explicitly lists DSM 804 as a related synonym of Fusaro 269797, agreeing with
    focal Methods. No alternate strain or catalogue medium is substituted.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804558Z'
  snapshot_sha256: f7f2289ee8608a510fffa98ee8a89c67018ae7ed4d831f8cf9950a52f738860f
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000174/ontology-semantic-notes.json
  locator: Final source-specific roles, graph, chemistry and cultivation boundaries
  summary: Retain donor PRIMARY_DEGRADER, recipient CROSS_FEEDER/SYNTROPHIC_PARTNER,
    ordinal ABUNDANT and the qualified three-node/two-arrow graph. Donor CROSS_FEEDER
    needs actual utilization evidence or omission of the optional role.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804586Z'
  snapshot_sha256: e1c2dedd520ff894353aca4efbfe86c8abfe5590d1d4f6ad1399fdba2cb360f6
- evidence_id: base-medium
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/root-medium-reference-scope.json
  locator: Scoped public access attempts for references 23 and 24
  summary: Metadata verifies DCB-1 reference DOI 10.1128/AEM.02574-06 and high-salt
    reference DOI 10.1128/AEM.02680-08. Full recipes were not recovered after EPMC
    errors and blocked alternate routes. Focal modifications are directly supported;
    no inherited concentrations or other-study substrates are imported.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804617Z'
  snapshot_sha256: f3bd531898f61c72141335350ee6a0c79d3f312b943756fe30ecd62b33182c5f
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/dataset-verification.json
  locator: Publication identity, exact legacy DOC/package and data-availability statements
  summary: The PMID identifies the primary publication. The article points to its
    own text and SI; exact DOC/ZIP identity and six-table/four-figure mapping are
    verified. Source gene IDs are assay targets, not new deposits. A bounded article/SI
    scan found no named archive identifier; no mandatory dataset omission finding
    is inferred.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804645Z'
  snapshot_sha256: 6b3a4c367fad55de80699247507f00fc184813e37533fcd0bb74e5a620f659d1
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/snippet-audit.json
  locator: Twenty-eight reference-specific excerpt occurrences
  summary: 'All 28 occurrences strictly match fresh XML and the MD cache: 24 abstract
    and four body-only. The short TXT cache supports 24. Literal matching verifies
    text, not donor recipient-role support or causal mediation.'
  support: supports
  accessed_at: '2026-10-21T21:45:32.804673Z'
  snapshot_sha256: cf73ecf3e36622bc3a2c873760262ba3036d0632612dbc6a26b65586133178f8
- evidence_id: history
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-12/000174/provenance-audit.json
  locator: Whole history, exact batch 19 row/adversarial context and current 1326/1327/529
    bodies/comments
  summary: Issue 1326 is closed after graph qualification; shared 1327 remains open
    and owns non-graph follow-up; 529 is closed contextual provenance. All comments
    were read. The older quantitative-abundance request is assessed against the current
    ordinal schema rather than automatically repeated. This review does not close
    shared issues or reassess their other records.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804719Z'
  snapshot_sha256: 54507de71d6e114834eb30843e587ef3f521dcc7e1d2760a94af1ec7134cdbe4
- evidence_id: historical-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/historical-source-byte-comparison.json
  locator: Prior XML digest versus fresh bytes
  summary: Fresh main XML equals the prior recorded digest. The old path is inert
    historical metadata, not an active pin exception or a reconstructed source.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804748Z'
  snapshot_sha256: d88a4405eac7979dca624a06fa351d2eb37ce8e9cef0883cb8e52e526b33c153
- evidence_id: inspect
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/inspect.json
  locator: Fresh official 27-input inspection
  summary: The target, both cache extensions, sole history, exact batch 19 decision/adversarial
    and 21 authorities were inspected before assessment. Ignored-inclusive bounded
    discovery found no other focal prior review; broad corpus logs were not treated
    as scientific evidence.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804776Z'
  snapshot_sha256: 6063e2ca1e10fe15aab7d140a9b1e47ddf75926facfb4fc046f98fa40af8fd63
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/lead-source-assets.json
  locator: Seventeen package members and local legacy-DOC rendering
  summary: Six main JPEGs, six thumbnails, four equation GIFs and one DOC were acquired.
    All six main figures and four SI figures were viewed. The original DOC is preserved;
    text conversion omitted images, so a separate local PDF render supplied the pixels.
    Initial acquisition/rendering failures are retained as scratch attempts, not native
    validation failures.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804797Z'
  snapshot_sha256: 8f0be4f529e26bc566adcb05c23566663ce424da8c9b9e8ca7b6582ffe824cce
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/lead-primary-read-scope.json
  locator: Whole main, 41 references, Table 1, four equations and complete declared
    SI
  summary: Lead read all main scientific sections and references, all six supplementary
    tables and captions, and all ten main/SI figures. Full source and authority scopes
    are explicit; no raw assay reanalysis or model execution occurred.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804825Z'
  snapshot_sha256: 18bfcf08288062530f731494837044765c17a53003f6e442791d35a4b43c2954
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/source-audit.json
  locator: Final three finding groups and completion
  summary: Completed scientific assessment finds one major donor-role support issue
    and two minor cultivation/provenance issues. Formate claims remain author-supported
    and coculture-scoped; they are not graded as unconditional formate-growth claims.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804852Z'
  snapshot_sha256: ad88faf2f062b0c674e4052530bb9dfddeafe1a8d8f8ce0873b506531609ddda
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/root-independent-source-audit.json
  locator: Independent primary, supplement, authority and provenance assessment
  summary: Root independently assessed the current scientific claims and agrees with
    the final three groups and completion. Its actual reading and bounded base-recipe
    access are recorded separately.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804882Z'
  snapshot_sha256: 55c7e976b1e72223b09b719250e22585a2f9789be25a6b0baf452b5910d130bd
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/support-final-audit.json
  locator: Distinct final support, counts and native arithmetic
  summary: Completeness 95. Eight evidence occurrences across three nodes give mean
    8/3. With COMPLETE network and one major/two minor findings, raw quality is 121,
    capped at 100. All 27 inspected input bytes remain unchanged.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804906Z'
  snapshot_sha256: 42fe8b512b3b94b3d9fb03ef670ef42851e390aeb2ddd09d591dc9084466f624
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/supporting-artifact-manifest.json
  locator: Final support artifacts and exact hashes
  summary: Final provenance, resource, snippet and source scopes are pinned. Preliminary
    support remains immutable.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804930Z'
  snapshot_sha256: 1747a22036c56e005338dc9d47d78284db84b204f16eb9ac352037f7ea9136c0
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/auxiliary-frozen-manifest.json
  locator: Final native and authority receipts
  summary: Eight focused native checks pass; all 13 ontology pairs across 33 occurrences
    match. Core strain mappings are retained. No canonical/cache mutation occurred.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804952Z'
  snapshot_sha256: d17ebccccf9c2b3dcf348f5444c3861701af600b94a6259263723bb0d46c5cdd
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/final-validator-summary.json
  locator: Actual eight command outcomes and final input integrity
  summary: Schema, strict, term, reference, GTDB, domain, history and cache-name checks
    pass. Initial validator summary remains unchanged. Native success does not establish
    scientific entailment.
  support: supports
  accessed_at: '2026-10-21T21:45:32.804992Z'
  snapshot_sha256: 06515a3331cce48f26c25e32a8ea5066ae71536257d657b25bb953b837a01116
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/adapter-check.json
  locator: Fresh batch 12 runtime checks; explicit batch 11 record 403 discovery reuse
    at 2026-10-21T19:20:45.556660+00:00
  summary: PATH/module/owned-venv availability was freshly checked. The ignored-inclusive
    filename search is explicitly the prior batch 11 search, not a new batch 12 search.
    The other-checkout runner was not executed; no global absence or installation
    is claimed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805019Z'
  snapshot_sha256: 356a49ec78798be7b9a9e5f44e09b8b8d62d94325d19788b4602ab9a0b966b5e
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/validate.json
  locator: Actual focused command and output
  summary: Recorded native outcome; biological entailment independently assessed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805095Z'
  snapshot_sha256: 0b1af662239407dd4af3b1669504a8b3ed5bdd244d45555392751ae3bea3c98a
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/validate-strict.json
  locator: Actual focused command and output
  summary: Recorded native outcome; biological entailment independently assessed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805156Z'
  snapshot_sha256: 12b570f815ad1e6053d13d89da63970e14fdd860d21c8976812348ddb267cf5e
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/validate-terms.json
  locator: Actual focused command and output
  summary: Recorded native outcome; biological entailment independently assessed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805205Z'
  snapshot_sha256: 30bd0bd502b06a4035f59e19f759b5d98128dd75ca4e99ea8e49388bed41fa76
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/validate-references-explained.json
  locator: Actual focused command and output
  summary: Recorded native outcome; biological entailment independently assessed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805256Z'
  snapshot_sha256: 4ff289f65b516f5883ba21d73f01ccdb4ec9b52171eead87ad3eb131f1687c6a
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/validate-gtdb.json
  locator: Actual focused command and output
  summary: Recorded native outcome; biological entailment independently assessed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805317Z'
  snapshot_sha256: 39f2c87762a372bd8d325dea27fbe18ee50f13a02be1bdd7fc42959dab9d9ae1
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/validate-gtdb-domain.json
  locator: Actual focused command and output
  summary: Recorded native outcome; biological entailment independently assessed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805366Z'
  snapshot_sha256: c44111cd18fb98eb6a684731f72181dafcd1091723db0efbb12dc8424e701cb2
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/validate-history.json
  locator: Actual focused command and output
  summary: Recorded native outcome; biological entailment independently assessed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805530Z'
  snapshot_sha256: bb10eab45fbf74ed25eafd63cd779df6459ed40dc1eab1c349f0cfe50fe527f4
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000174/normalize-cache-names-check.json
  locator: Actual focused command and output
  summary: Recorded native outcome; biological entailment independently assessed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805589Z'
  snapshot_sha256: b214cb884ef7e5ac75f28ee76c6bf7ae08ef7067ad91717e67de3aa2249453ea
- evidence_id: check-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/audit-network.json
  locator: Same-batch corpus diagnostic
  summary: Actual corpus result retained; later records are not assessed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805819Z'
  snapshot_sha256: 1621a1dd35060a1052cf4669f27e9a936a82f4759be38e4f39a9a4a1a73a14b8
- evidence_id: check-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/check-network-quality.json
  locator: Same-batch corpus diagnostic
  summary: Actual corpus result retained; later records are not assessed.
  support: supports
  accessed_at: '2026-10-21T21:45:32.805983Z'
  snapshot_sha256: 34467f31f8dad2a00579e8350771795ee0f769be41af2e9435c88b603ec9fa1e
assessments:
- assessment_id: identity
  area: identity
  topic: Focal membership, origin and environment
  outcome: supported
  summary: The record denotes the intended defined laboratory pair.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - identity
  - strain
  - ontology
  details: Keep both exact strain terms, SYNTHETIC origin, ENGINEERED state and the
    laboratory environment. Exclude the separately tested M. mazei comparator, monoculture
    controls and catalogue media from focal membership/protocol.
- assessment_id: taxonomy
  area: grounding
  topic: Strain mappings and provenance
  outcome: concern
  summary: Core taxonomy and GTDB values are sound; release/build wording is not verified.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - strain
  - gtdb
  details: Retain both exact-ID classifications and four/one genome counts. Correct
    snapshot provenance without replacing strain descriptors or interpreting is_reclassified
    as a new genomic result.
- assessment_id: roles
  area: scope
  topic: Donor and recipient functional roles
  outcome: concern
  summary: Donor CROSS_FEEDER lacks local recipient evidence.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - feedback
  - schema
  - semantics
  details: The bacterium releases precursors and benefits functionally from a proposed
    product-removal feedback. Neither establishes a metabolite supplied by the methanogen
    that the bacterium utilizes. Retain donor PRIMARY_DEGRADER and the methanogen’s
    broad recipient roles; no obligatory dependence or nutrient-only criterion applies.
- assessment_id: supply-node
  area: graph
  topic: ecological_interactions[0] and its downstream arrow
  outcome: supported
  summary: Precursor provision is supported with unresolved individual contributions.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - precursors
  - controls
  - expression
  details: Keep C. cellulovorans-to-M. barkeri CROSS_FEEDING and the arrow to coculture-associated
    methanogenesis. Undetectable hydrogen is not a quantified gross transfer flux;
    formate use remains conditional. Other VFA products are not automatically methanogen
    substrates.
- assessment_id: methane-node
  area: graph
  topic: ecological_interactions[1] and its downstream arrow
  outcome: supported
  summary: The PARTIAL pathway node and HYPOTHESIZED feedback remain appropriate.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - controls
  - expression
  - feedback
  - schema
  details: Retain the negative and mixed-substrate controls and source conceptual
    acetoclastic/CO2-reduction interpretation. The reverse taxon direction denotes
    proposed product-removal feedback, not reciprocal nutrient donation. No unique
    pH mediator, obligatory syntrophy or electron-contribution partition is established.
- assessment_id: outcome-node
  area: graph
  topic: ecological_interactions[2] and discussions[0]
  outcome: supported
  summary: The untyped outcome node preserves functional improvement without reciprocal-growth
    inflation.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - feedback
  - population
  details: Keep measured improved degradation and smaller pH decline, unchanged fermenter
    growth, changed acid-production patterns and the existing mechanism discussion.
    No extra nodes or arrows are required.
- assessment_id: non-graph-claims
  area: consistency
  topic: Description, taxon notes and related ingredients
  outcome: supported
  summary: Existing formate wording is scoped to the coculture and follows the source
    interpretation.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - controls
  - precursors
  - expression
  details: The graph/discussion already supplies the negative-control and unresolved-flux
    boundaries. Do not characterize current notes as proof of formate-only growth.
    Glucose-equivalent yield is not glucose feeding, and supplied CO2/bicarbonate
    is distinct from donor-derived carbon.
- assessment_id: cultivation
  area: scope
  topic: Medium, atmosphere and preparation stages
  outcome: concern
  summary: Stored setup numbers are correct, but explanatory notes and medium context
    need repair.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - medium
  - stages
  - operation
  - base-medium
  details: Remove unsupported claims about agitation impairing transfer and the supply-versus-atmosphere
    dichotomy. Recover explicit DCB-1 modifications and focal inoculation context.
    Preserve the unrecovered base recipe boundary; do not import revival or high-salt
    preculture concentrations into production without source support.
- assessment_id: time-ph
  area: quantity
  topic: Duration, pH and inoculum basis
  outcome: supported
  summary: Source values can be added only with their original measurement basis.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - sampling
  - stages
  - population
  details: The 1.4:1 cell ratio differs from preculture transfer percentages. Main
    sampling through day 20 differs from 17 days of methane production, six months
    of acclimation and nine months of formate-only observation. Initial/endpoint pH
    values do not establish active pH control.
- assessment_id: assays
  area: evidence
  topic: Cell counts, gene expression and conceptual pathways
  outcome: supported
  summary: Genomic-DNA population qPCR and selected-gene RT-qPCR are distinct experiments.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - population
  - expression
  - supplement
  details: Retain IN_VITRO assay provenance and conceptual-model qualifications. Ordinal
    ABUNDANT does not require equal fractions or a universal numerical threshold;
    it is not a substitute for source-specific measured abundance.
- assessment_id: chemistry
  area: grounding
  topic: CHEBI/GO scope and metal relevance
  outcome: supported
  summary: Terms correctly identify the stated substrate, products and processes.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - ontology
  - medium
  - semantics
  details: Cellulose catabolism belongs to the bacterium and methanogenesis to the
    archaeon. Chemical co-listing does not establish transfer direction. Salts or
    trace constituents do not establish a metal-processing purpose; keep NOT_APPLICABLE.
- assessment_id: excerpts
  area: evidence
  topic: Reference identity and exact text
  outcome: supported
  summary: All 28 excerpt occurrences strictly match fresh source and the MD cache.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - snippets
  - history
  details: Twenty-four occur in the abstract and four only in the body. The MD header
    says abstract_only despite appended full main, while TXT is short abstract text.
    This is a cache-provenance boundary, not a failed snippet or a claim that caches
    were refreshed.
- assessment_id: resources
  area: representation
  topic: Publication, declared supplement and datasets
  outcome: supported
  summary: The publication link and accessible supplement have verified identities.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - resources
  - assets
  - base-medium
  details: Primer and processed RT-qPCR tables are source supplemental data; assay
    Gene IDs and prior genomes are background context. Empty associated_datasets does
    not establish a missing mandatory deposit. No cross-Mech medium equivalence is
    asserted.
- assessment_id: provenance
  area: provenance
  topic: Historical repair and current follow-up
  outcome: supported
  summary: The prior graph repair is preserved and shared non-graph ownership remains
    open.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - history
  - historical-source
  - inspect
  details: Current 1326 is closed and 1327 is open. This single-record review neither
    closes shared findings for other records nor repeats older numerical-abundance
    assumptions against the current ordinal schema.
- assessment_id: validation
  area: schema
  topic: Native results and scientific completion
  outcome: supported
  summary: Eight focused checks pass; current-claim scientific review is completed.
  target_ids:
  - CommunityMech:000174
  evidence_ids:
  - final-native
  - auxiliary
  - source-scope
  - root-source
  details: Actual corpus diagnostic outcomes are retained separately. Native checks
    do not certify scientific interpretation; all current claim-critical focal sources
    were assessed. The inherited base-medium access limit is explicit.
- assessment_id: metrics
  area: completeness
  topic: Native scores and finding counts
  outcome: supported
  summary: Completeness 95; raw quality 121, capped 100.
  target_ids:
  - CommunityMech:000174
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
      earns no bonus. Presence is not scientific support.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 − 50P1 − 10P2 − 2P3 + 20min(mean node evidence/2,1) + 15
      if COMPLETE,0,100). P1=0, P2=1, P3=2, P4=0; eight node-evidence occurrences/three
      nodes give mean 8/3 and bonus 20; COMPLETE adds 15. Raw 121 caps at 100.
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
- finding_id: support-donor-recipient-role
  issue_key: cm-000174-support-donor-recipient-role
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: An unsupported recipient metabolism materially changes the
    donor functional annotation.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Support or omit the donor recipient role
  description: C. cellulovorans carries CROSS_FEEDER, but the source establishes its
    metabolite donation and a proposed benefit from product removal rather than utilization
    of a partner-derived metabolite. Identify a provider, metabolite and source-local
    utilization evidence before retaining this optional recipient role; otherwise
    omit CROSS_FEEDER for this donor. Retain PRIMARY_DEGRADER, methanogen roles and
    the qualified graph. Do not claim reciprocal utilization is impossible.
  target_ids:
  - CommunityMech:000174
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].evidence
  evidence_ids:
  - feedback
  - schema
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate with existing shared
    non-graph issue 1327; do not reopen the closed 1326 graph repair or close other
    targets. No issue mutation.
- finding_id: separate-culture-stages
  issue_key: cm-000174-separate-culture-stages
  category: scope
  severity: minor
  native_severity: P3
  normalization_reason: The numeric setup remains correct; gaps and unsupported explanatory
    prose are bounded context issues.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Clarify focal medium and culture stages
  description: Correct stored bottle/volume/temperature/static values coexist with
    an unsupported agitation rationale, a false distinction between gas supply and
    atmosphere, and an incomplete abstract-tier medium description despite available
    full Methods. Document focal DCB-1 modifications, initial cellulose, gas/bicarbonate
    and inoculum cell ratio with exact Methods evidence; separate revival, precultures,
    formate controls and production. Remove the unsupported agitation explanation
    and workflow clutter, retain both atmosphere and resource scope, and mark the
    inherited base recipe unresolved rather than import unrelated conditions.
  target_ids:
  - CommunityMech:000174
  field_paths:
  - cultivation_setup[0].notes
  - cultivation_setup[0].instrument_detail
  - growth_media[0].composition
  - growth_media[0].preparation_notes
  - growth_media[0].evidence
  evidence_ids:
  - medium
  - stages
  - operation
  - sampling
  - base-medium
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate with existing shared
    non-graph issue 1327; do not reopen the closed 1326 graph repair or close other
    targets. No issue mutation.
- finding_id: document-gtdb-snapshot
  issue_key: cm-000174-document-gtdb-snapshot
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Both mapping cores are valid; the defect is unsupported release/build
    provenance.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Document the verified GTDB snapshot
  description: Both valid exact-strain GTDB blocks describe the mapping as latest
    and built on a date that is only the checked local file mtime. Record verified
    crosswalk SHA and exact-ID method, labeling mtime only as snapshot metadata unless
    independent release/build evidence is available. Retain the current taxa, lineages,
    majority fractions and four/one genome counts.
  target_ids:
  - CommunityMech:000174
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - strain
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate with existing shared
    non-graph issue 1327; do not reopen the closed 1326 graph repair or close other
    targets. No issue mutation.
actions:
- action_id: resolve-donor-role
  description: Attach recipient evidence or omit the unsupported optional donor role.
  finding_ids:
  - support-donor-recipient-role
  target_ids:
  - CommunityMech:000174
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - For taxonomy[0].functional_role CROSS_FEEDER, identify the partner provider, metabolite
    and source-local utilization evidence before retention; otherwise omit this role.
    Product donation, improved degradation, aggregation and relief from product accumulation
    alone do not establish utilization of another taxon metabolite.
  - Retain donor PRIMARY_DEGRADER and M. barkeri CROSS_FEEDER/SYNTROPHIC_PARTNER,
    the three existing nodes, both qualified arrows and the open mechanism discussion.
    Do not impose obligacy or a nutrient-only criterion, and do not claim reciprocal
    utilization is biologically impossible.
  - Preserve the source’s coculture-specific formate interpretation, nine-month formate-only
    failure, limited mixed-substrate monoculture consumption, unresolved individual
    flux and non-unique pH mediation. Current non-graph formate statements already
    name this coculture; do not falsely reclassify them as unconditional formate-growth
    claims.
- action_id: clarify-cultivation
  description: Represent source-specific medium, gas and inoculation context.
  finding_ids:
  - separate-culture-stages
  target_ids:
  - CommunityMech:000174
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Retain 160-mL serum bottles, 100-mL working volume, 35°C and no shaking. Remove
    the unsupported claim that agitation opposes gas balance or interspecies transfer.
    Headspace CO2/N2 20:80 is both gas composition and a supplied resource, not mutually
    exclusive categories. Do not invent pressure, flow or continuous feed.
  - 'Recover the focal 3 g/L cellulose and stated DCB-1 modifications: yeast extract
    2 g/L, sodium chloride 10 g/L and magnesium sulfate 9.5 g/L, preserving the reported
    chemical form without inventing a hydrate. Include sodium bicarbonate 2.5 g/L
    with exact Analytical analyses evidence. Full inherited reference-23 formulation
    remains unresolved; do not silently reconstruct it from another study or catalogue.'
  - Keep the authors’ only-substrate designation scoped to the cellulose amendment
    while recording yeast extract, supplied CO2 and bicarbonate. Do not claim chemically
    exclusive carbon. Replace stale abstract-tier preparation prose with precise Methods
    evidence and remove cross-record workflow/issue narration from biological notes.
  - Separate collection revival, C. cellulovorans 5% v/v preculture transfer, methanogen
    10% v/v transfer to high-salt medium with 50 mM acetate, six-month initial acclimation
    and routine two-week propagation from the focal production assay. Use the focal
    1.4:1 cell ratio in suitable setup notes; do not insert it as a transfer percentage
    or absolute inoculum density, and do not use the comparator 1.7:1 ratio.
  - Keep genomic-DNA cell counting separate from selected-gene RNA/RT-qPCR. Initial
    pH 7.5 ± 0.02 and endpoint 6.7 ± 0.06 are observations, not active pH-control
    settings. Main trajectories extend 20 days; 17 days is the reported methane-production
    duration. Formate-only nine-month observation and mixed-substrate controls are
    separate arms.
- action_id: document-mapping
  description: Replace unsupported release/build wording with verified mapping provenance.
  finding_ids:
  - document-gtdb-snapshot
  target_ids:
  - CommunityMech:000174
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve exact NCBITaxon:573061 and 269797, their current lineages, majority fractions
    1.0 and genome counts four/one. Both resolve via ncbi_id; no species/strain replacement
    or count transfer is required.
  - Record crosswalk SHA 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    and exact lookup method. Label the July 25 local mtime as file snapshot metadata,
    not a verified release named latest or a build date. Keep is_reclassified as the
    helper’s name-comparison flag.
  - 'Keep identity support distinct from access: direct DSM 3052 confirms 743B/ATCC
    35296; DSM 804 direct access failed, but source Methods and current NCBI related
    synonym support Fusaro/DSM 804. Do not import catalogue maintenance media or the
    M. mazei comparator.'
- action_id: verify-future-curation
  description: Validate separately authorized repairs without altering existing evidence
    scope.
  finding_ids:
  - support-donor-recipient-role
  - separate-culture-stages
  - document-gtdb-snapshot
  target_ids:
  - CommunityMech:000174
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Methanosarcina_Cellulose_Methane_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Attach exact source-local evidence to each changed claim. Preserve the qualified
    graph, ordinal ABUNDANT and current strain identities. Optional SI links may identify
    processed expression/control data, but no mandatory raw-deposit omission is established.
  - Any future cache metadata or Methods enrichment must preserve source/version boundaries
    and both existing cache files through the authorized workflow. The MD contains
    appended full main despite its abstract_only header; the TXT is short abstract
    text. Do not move supplement text into the article cache.
  - After authorized canonical changes, append required history and run schema, strict,
    terms, references, GTDB, domain and history checks, then regenerate and check
    HTML. This review changes no canonical record, cache, history or generated output;
    parent persistence is limited to the new review bundle after whole-candidate audits.
limitations:
- Full focal main, all six main figures, Table 1, four equations, 41 references, all
  six SI tables and four SI figures were assessed. The original legacy DOC was locally
  rendered; its internal Additional file labels differ from the published S-table/S-figure
  labels, with the mapping preserved.
- Inherited DCB-1 and high-salt reference formulations were not recovered after bounded
  public attempts. Focal modifications are directly supported; no unrelated-study
  substrates or catalogue recipes are imported. This does not prevent assessment of
  current focal claims.
- No raw assay reanalysis, image digitization, gene-database reannotation, genome
  classification or biological experiment was performed. Metabolite pools and selected
  expression do not resolve every transferred molecule or isolate unique pH mediation.
- All 28 field excerpt occurrences strictly match fresh source and MD cache, partitioned
  24 abstract/four body-only; TXT supports 24. Matching is not scientific entailment.
  Both caches remain unchanged, including the MD abstract_only metadata/full-main
  boundary.
- Direct DSM 804 catalogue access failed; source Methods and current NCBI synonym
  support the identity. Current mappings are exact local snapshot evidence, not a
  new genome analysis or verified release/build date.
- Optional adapter availability was freshly checked in batch 12 while filename-search
  discovery is explicitly reused from batch 11 record 403. No other-checkout runner
  or paid source was used. Historical XML paths remain inert metadata, and initial
  support/validator receipts are immutable.
notes:
- Completed scientific review; one major/two minor findings; completeness 95, raw
  quality 121/capped 100.
- No unconditional formate-growth, mandatory dataset or fixed-percentage abundance
  finding.
- No canonical changes or save by lead; parent persistence follows independent whole-candidate
  acceptance.
tags:
- record-review
- cellulose
- methanogenesis
- batch-12
```
