# Cellulose biohydrogen roles, medium and inference review

- Review: 20261021T215825Z-cellulose-biohydrogen-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T21:47:43.236946Z
- Finished UTC: 2026-10-21T21:58:25.716894Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Partial source review finds three major role/process, acetate-feed and non-graph attribution issues, plus two minor project-link and GTDB-provenance issues. The complete 2016 reader text supports these findings; the 2015 body and claim-relevant SI remain unavailable. Preserve the qualified three-node/one-arrow graph. Native checks pass; completeness 85 and quality 97.6666666667.

## Scope And Provenance

Whole maintained record and all available focal source text assessed, with explicit missing main/SI/visual coverage.

Selection: Only released CommunityMech:000264 in owned batch 12.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95812d3412d5aab41fd03422340cf736ac7b56f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000264 | kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml | maintained | Clostridium cellulovorans-Rhodopseudomonas palustris Cellulose Biohydrogen Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000264 | Focused native command exit 0. |
| validate-strict | passed | True | CommunityMech:000264 | Focused native command exit 0. |
| validate-terms | passed | True | CommunityMech:000264 | Focused native command exit 0. |
| validate-references-explained | passed | True | CommunityMech:000264 | Focused native command exit 0. |
| validate-gtdb | passed | True | CommunityMech:000264 | Focused native command exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000264 | Focused native command exit 0. |
| validate-history | passed | True | CommunityMech:000264 | Focused native command exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000264 | Focused native command exit 0. |
| audit-network | failed | True | CommunityMech:000264 | Same-batch corpus diagnostic retained. |
| check-network-quality | failed | True | CommunityMech:000264 | Same-batch corpus diagnostic retained. |
| Claim-critical source assessment | unavailable | True | CommunityMech:000264 | Whole 2016 reader text available; 2015 body, most images and SI unavailable, so scientific review remains partial. |
| Reference-specific excerpt verification | passed | True | CommunityMech:000264 | 18 strict fresh plus two explicit H2-spacing projections; all 20 cache matches. |
| Ontology and schema semantics | passed | True | CommunityMech:000264 | Eleven pairs/19 occurrences match; literal roles and source support assessed. |
| Optional structured adapter | unavailable | False | CommunityMech:000264 | Fresh runtime availability with explicit earlier filename-discovery reuse. |
| Raw-data or experimental reproduction | skipped | False | CommunityMech:000264 | No raw reads, flux analysis, genome reclassification or biological experiment. |

## Scientific And Domain Assessments

### Membership, origin and ecological setting

identity: supported. Targets: CommunityMech:000264.

The exact 743B/CGA009 pair is the intended laboratory coculture.

Retain both strain terms, ENGINEERED/SYNTHETIC, LIGNOCELLULOSE and laboratory setting. Do not substitute the CGA001 ancestor, constitutive-nitrogenase mutant, monoculture or catalogue protocol.

### Taxon functions and carbon-fixation grounding

scope: concern. Targets: CommunityMech:000264.

Donor recipient metabolism and focal autotrophy are not established.

Require utilized partner-metabolite evidence for donor CROSS_FEEDER. Require focal CO2 fixation for recipient PRIMARY_PRODUCER and GO:0015979, or omit these optional assertions. Keep donor PRIMARY_DEGRADER and recipient CROSS_FEEDER; no claim of intrinsic inability is made.

### Exact strain GTDB assignments

grounding: concern. Targets: CommunityMech:000264.

Core mappings are valid; release/build provenance is overstated.

Preserve exact-ID routes, classifications, lineages and four/two genome counts. File mtime is snapshot metadata, not proof of a release named latest.

### ecological_interactions[0] and downstream[0]

graph: supported. Targets: CommunityMech:000264.

VFA supply and the qualified link to hydrogen remain appropriate.

Keep the pairwise CROSS_FEEDING node and one downstream arrow. Cellulose is upstream feed, not a directly donated recipient substrate. Pool and pH changes do not resolve all partner flux or isolate pH as the only mediator.

### ecological_interactions[1]

graph: concern. Targets: CommunityMech:000264.

Measured output and nitrogenase-control bounds are sound; the optional GO annotation is not.

Preserve the untyped community endpoint, ammonium intervention and distinction between enhanced hydrogen and all-flux partition. Correct GO:0015979 within the role/process finding; do not restore N2 fixation under argon or add obligatory syntrophy.

### ecological_interactions[2] and discussions[0]

graph: supported. Targets: CommunityMech:000264.

Expression is measured while mediation remains an open question.

Keep the untyped transcriptomic response node and the existing mechanistic discussion. Do not restore the removed expression-to-output arrow or treat a conceptual model as direct metabolite transfer.

### Related ingredient claims and gradient evidence

consistency: concern. Targets: CommunityMech:000264.

Bulk-H2 attribution and causal explanations exceed the qualified graph.

Limit partner attribution to the authors’ inferred enhancement and control support. Qualify expression/chemotaxis explanations. The environmental-factor description already says implicated and thiamine relevance says likely; those are not separate categorical defects.

### Medium input versus intermediate and culture stages

scope: concern. Targets: CommunityMech:000264.

Acetate is incorrectly represented as a focal coculture feed.

Separate 20 mM acetate monocultures from 3 g/L cellulose coculture, secreted VFAs and ammonium intervention. Replace abstract-tier prose with recoverable 2016 Methods while preserving the unavailable inherited recipe and 2015 concentration-series boundary.

### Culture conditions and abundance basis

quantity: supported. Targets: CommunityMech:000264.

Recovered quantities require their source-specific bases.

A 1:4 cell ratio is not a transfer percentage or persistent abundance fraction; initial pH 7.2 is not a controlled setpoint. Keep ordinal ABUNDANT. Glutamate concentration, absolute inoculum density and full basal recipe remain unstated/unrecovered.

### RNA-seq, RT-qPCR and physiological comparisons

evidence: supported. Targets: CommunityMech:000264.

Experimental measurements and inferential models are distinct.

Retain IN_VITRO for measured expression and controls. NOIseq q is differential-expression probability, not an invented FDR threshold. Do not infer quantitative pathway flux from transcript changes or replace experimental provenance solely because analysis is computational.

### Chemical terms and metal relevance

grounding: supported. Targets: CommunityMech:000264.

Identifiers match, with class/form and placement limits.

Organic acid is broader than a VFA mixture; keep that breadth explicit. Thiamine(1+) is an expression-context chemical, not evidence of secretion. No medium salts or nitrogenase cofactor establish metal-processing relevance; retain NOT_APPLICABLE.

### Publication context and actual transcriptome deposit

representation: concern. Targets: CommunityMech:000264.

The verified study accession can be added with exact assay scope.

Retain clearly labeled DOI publications and add PRJNA280696/SRP057083. Nine archive samples have 18 runs; specific attributes distinguish arms despite inconsistent top-level organism labels. No raw read analysis or arbitrary archive omission is asserted.

### Reference identity and literal excerpt support

evidence: supported. Targets: CommunityMech:000264.

All 20 excerpts are supported with explicit formatting limits.

Eighteen strict fresh Abstract/IMPORTANCE matches plus two H2 inline-spacing projections; all 20 cache matches. The 2015 cache is bibliographic/unavailable, and the two 2016 caches are short abstract material. No cache was refreshed or treated as full body.

### Prior repairs and current issue ownership

provenance: supported. Targets: CommunityMech:000264.

Closed graph work and open shared non-graph follow-up are separated.

Coordinate with 1333 without closing its other records or reopening resolved 1330 automatically. Exact prior scopes were selected sections, not whole body/SI. This review adds a broader but still incomplete scientific read.

### Native gates and scientific completion

schema: supported. Targets: CommunityMech:000264.

Eight focused native gates pass; source review remains partial.

Native validity does not replace current-claim scientific support. Preserve all failed source-response payloads and explicit unread asset limits. The scratch asset-label correction is separate from candidate/native validation.

### Native rubric and final finding counts

completeness: supported. Targets: CommunityMech:000264.

Completeness 85; raw and capped quality 97.6666666667.

## Findings

### bound-functional-roles: Bound recipient and autotrophic role assertions

major / open / confirmed; issue key: cm-000264-bound-functional-roles.

Donor CROSS_FEEDER has no identified partner-derived metabolite utilization evidence. Recipient PRIMARY_PRODUCER and GO:0015979 require carbon fixation, while the focal Methods specify light energy and organic VFA carbon. Require source-local support or omit these optional assertions; retain donor PRIMARY_DEGRADER, recipient CROSS_FEEDER and the qualified output node.

### separate-feed-and-products: Separate coculture feed from monoculture and metabolic products

major / open / confirmed; issue key: cm-000264-separate-feed-and-products.

The focal medium lists acetate although 20 mM acetate belongs to R. palustris monocultures and coculture VFAs initially equal zero. Remove unsupported acetate feed, preserve it as an exchanged intermediate, and replace abstract-tier preparation prose with the recoverable 2016 protocol. Keep the unavailable 2015 concentration series and inherited recipe separate.

### qualify-hydrogen-and-mechanism: Qualify hydrogen attribution and mechanistic explanations

major / open / confirmed; issue key: cm-000264-qualify-hydrogen-and-mechanism.

The hydrogen ingredient attributes the bulk of total hydrogen to R. palustris, while the source supports an inferred enhanced component and nitrogenase involvement. Other ingredient explanations promote expression and inferred chemotaxis to established mediation. Align them with the qualified graph; preserve already-qualified gradient and thiamine descriptions.

### link-declared-transcriptome: Link the declared transcriptome project

minor / open / confirmed; issue key: cm-000264-link-declared-transcriptome.

The publication-context entries omit explicitly declared and verified PRJNA280696/SRP057083. Add the RNA-seq project with exact culture-arm/sample/run scope. Existing DOI publications may remain as clearly labeled publication context.

### document-gtdb-snapshot: Document the verified GTDB snapshot

minor / open / confirmed; issue key: cm-000264-document-gtdb-snapshot.

Both exact-ID GTDB cores are valid; latest-release/build wording is not established by local mtime. Retain classifications, lineages and four/two counts while reporting actual snapshot digest and lookup method.

## Recommended Actions And Acceptance Checks

### bound-roles

Support or omit optional recipient/autotrophy annotations.

- For donor CROSS_FEEDER, identify the provider, metabolite and local utilization evidence; product donation, pH relief and increased cellulose degradation alone do not establish receipt of partner metabolites. Otherwise omit that optional role. Retain donor PRIMARY_DEGRADER and recipient CROSS_FEEDER without an obligacy or nutrient-only criterion.
- For R. palustris PRIMARY_PRODUCER and ecological_interactions[1].biological_processes[0] GO:0015979, require focal CO2-to-organic-carbon evidence or omit the optional annotations. Light energy plus organic VFA use does not establish this fixation claim. Do not assert CGA009 is incapable of fixation in other conditions.
- Retain all three nodes and the one qualified arrow. A narrower process term is optional only with verified definition and source support: GO:0009765 concerns light harvesting, while GO:0019684 is not a generic anoxygenic-photofermentation replacement. Preserve ordinal ABUNDANT; do not demand an invented percentage.

### repair-medium

Separate focal feed, monoculture controls and recoverable protocol.

- Remove the unsupported acetate input from the focal coculture composition. Retain acetate/VFAs as fermentation intermediates; 20 mM acetate belongs to R. palustris monocultures. The 2016 coculture has 3 g/L cellulose and initially zero VFAs. Attach exact Culture experimental conditions and Bacterial chemotaxis evidence, not merely a VFA-expression excerpt.
- Recover 100 mL medium in 160-mL serum bottles, 30°C, 100 rpm, 6,000 lx from six 15-W Grolux tubes, argon headspace, 30 mM bicarbonate and 10 mM TES. Initial pH 7.2 is not an actively maintained setpoint. Record glutamate as nitrogen source with concentration unresolved; do not import another record or catalogue recipe.
- Place the 1:4 C. cellulovorans:R. palustris cell ratio in suitable setup context; do not relabel it as transfer percentage, absolute density or persistent abundance. Separate the 11.2 mM ammonium intervention, culture-specific substrates and early/mid/late sampling. Preserve source replication rather than inferring it from run counts.
- Replace abstract-only workflow prose with source-specific Methods evidence while preserving the unavailable inherited recipe and 2015 concentration-series details. The authors’ only-exogenous-substrate wording concerns designated cellulose feed; supplied bicarbonate and glutamate preclude an unqualified chemical carbon-exclusivity claim.

### qualify-mechanism

Align stronger ingredient explanations with measured and inferred scope.

- Replace bulk-of-total-hydrogen attribution with the authors’ inference about the enhanced component. Preserve the ammonium intervention as evidence of nitrogenase involvement, without directly allocating all gas to a partner or inferring N2 fixation under argon.
- Keep the physiological VFA-exchange interpretation and smaller pH decline, but qualify gene-expression/chemotaxis explanations as model support. Distinguish inferred spatial gradients from measured chemotaxis, pools from flux and correlated stress responses from selective mediation. Do not restore the removed expression-to-output arrow.
- Keep environmental_factors[1].description implicated wording and thiamine likely wording; their evidence explanations can explicitly retain inference. No separate categorical gradient or thiamine-secretion defect is asserted. Preserve the open mechanism discussion and state unavailable 2015/SI limits.

### link-project

Add the verified transcriptome resource with submission boundaries.

- Add PRJNA280696, secondary SRP057083, as the source-declared SRA/ENA RNA-seq resource. Link the exact project; retain clearly identified DOI publication contexts if useful. Reference genomes NC_014393.1 and NC_005296.1 are background alignment resources, not new deposits.
- Describe CC, Co and RP early/mid/late sample attributes, 18 paired runs and nine BioSamples, two runs per sample. Do not equate these counts to independent biological replication. Preserve the top-level archive label conflict for Co/RP; do not change membership or taxonomy from those labels alone.
- Identify the three declared SI files as unavailable inventory only until real payloads are recovered. Main references call CC DEGs Table S1, RP DEGs Table S2 and RT-qPCR Figure S3; do not certify unread worksheet structure or figures.

### document-mapping

Record reproducible GTDB mapping provenance.

- Preserve exact NCBITaxon:573061 and 258594, current GTDB lineages, fractions 1.0 and counts four/two. Both resolve through ncbi_id; no name-only fallback or strain/species substitution is needed.
- Record crosswalk SHA 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd and the exact lookup route. Label July 25 mtime as local file metadata, not a verified release named latest or build date. is_reclassified remains the helper’s name-comparison flag.
- Keep CGA009/BAA-98 and 743B/DSM 3052/ATCC 35296 identity support separate from stock purchase and culture conditions. Do not substitute CGA001 or import the prior 174 protocol.

### verify-future-curation

Validate separately authorized repairs and retain source limits.

- Attach exact source-local evidence to changed fields. Preserve all existing graph bounds, ordinal semantics and declared source versions; complete the 2015 body and claim-relevant SI assessment before claiming a full scientific review.
- Any authorized cache enrichment must preserve the three present caches and avoid treating supplement text as article text. This review leaves canonical records, caches, history and generated output unchanged. Coordinate current 1333 follow-up without closing other records.
- After separately authorized canonical repair, append required history, run focused schema/strict/terms/reference/GTDB/domain/history checks, and regenerate/check derived output. Parent may persist only this review bundle after independent candidate acceptance.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml; Whole maintained record | supports | The exact two-strain coculture has three nodes and one qualified arrow. Stronger non-graph annotations and medium placement require repair; native validity does not establish biological entailment. |
| identity | PMID:27208134; DOI:10.1128/AEM.00789-16; Abstract; Introduction, displayed lines 125–128; Materials and Methods: Culture experimental conditions., lines 130–136 | supports | The focal pair is C. cellulovorans 743B and R. palustris CGA009. The earlier physiology study and later transcriptomic experiments use this pair, but the 2015 full body remains unavailable. A constitutive-nitrogenase mutant is explicitly excluded. Laboratory assembly supports SYNTHETIC and ENGINEERED without implying a new genetic construct. |
| feed | PMID:27208134; DOI:10.1128/AEM.00789-16; Materials and Methods: Culture experimental conditions., lines 131–134; Results and Discussion: Bacterial chemotaxis., lines 404–408 | supports | The coculture receives 3 g/L cellulose; 20 mM acetate is the R. palustris monoculture substrate. Coculture VFAs begin at zero and accumulate through fermentation. Acetate in the coculture composition therefore confuses a produced intermediate with an added feed. The source separates light energy from VFA carbon for R. palustris. |
| operation | PMID:27208134; DOI:10.1128/AEM.00789-16; Materials and Methods: Culture experimental conditions., lines 131–136 | supports | The 2016 assay uses 100 mL medium in 160-mL serum bottles, 30°C, 100 rpm and 6,000 lx from six 15-W Grolux tubes. Argon fills the headspace; glutamate replaces ammonium as nitrogen source, without a stated concentration. Buffers are 30 mM sodium bicarbonate and 10 mM TES; initial pH is 7.2 and subsequently changes. Coculture inoculation is a 1:4 C. cellulovorans:R. palustris cell ratio, not a transfer percentage or absolute density. |
| assays | PMID:27208134; DOI:10.1128/AEM.00789-16; Materials and Methods: RNA extraction and sequencing.; RNA-sequencing data analysis.; RT-qPCR.; Table 1 | supports | Three culture arms and three growth phases have two biological cultures per arm/phase, yielding 18 RNA samples. RNA-seq uses HiSeq 2000 and named reference genomes. NOIseq probability q ≥0.8 and absolute log2 fold change ≥1 define differential expression. RT-qPCR checks 16 genes, eight per organism, with two biological and two technical replicates. This experimental evidence is not automatically COMPUTATIONAL because analysis uses software. |
| hydrogen | PMID:27208134; DOI:10.1128/AEM.00789-16; Results and Discussion: H2 production., displayed lines 230–231 and 379–388; Materials and Methods: Culture experimental conditions., lines 135–136 | supports | Ammonium at 11.2 mM reduces coculture hydrogen to 46 mL, 20 mL below the unamended coculture and 6 mL above amended C. cellulovorans monoculture; amended R. palustris monocultures produce no hydrogen. Together with nitrogenase expression, this supports involvement in the enhanced component. It does not directly partition all gas between partners or establish N2 fixation under argon. SI Figures S6–S7 are referenced by the main but unread. |
| exchange | PMID:27208134; DOI:10.1128/AEM.00789-16; Results and Discussion: Cellulose degradation.; Fatty acid metabolism.; Bacterial chemotaxis.; Figure 2 caption; Figure 5 caption and concluding paragraphs | supports | VFA profiles, pH and expression support the authors’ exchange model. The 2016 Figure 2 caption identifies a 3 g/L comparison modified from the 2015 source, with biological triplicates. Chemotaxis and a spatial gradient remain inferred from expression and feeding context. The final conceptual model is based on transcript levels, not measured partner flux or selective proof that expression causes output. |
| light-carbon | PMID:27208134; DOI:10.1128/AEM.00789-16; Materials and Methods: Culture experimental conditions., lines 133–134; Results and Discussion: Photosynthesis., lines 446–451 | supports | R. palustris uses light as energy and organic VFA carbon in coculture. Increased photosynthesis-gene expression accompanies this physiology. These observations do not establish focal inorganic-to-organic carbon fixation, even though the organism may have that capability in other conditions. |
| stress-population | PMID:27208134; DOI:10.1128/AEM.00789-16; Results and Discussion: Sulfur metabolism.; Thiamine metabolism.; Other genes and pathways of significance. | supports | Sulfur/thiamine transcription is correlated with pH and interpreted as stress response. It is not evidence of thiamine supplementation, transfer or quantified secretion. C. cellulovorans has no significant cell-density difference between mono- and coculture in the reported comparison. The initial 1:4 ratio is not a persistent abundance fraction; ordinal ABUNDANT remains permissible. |
| main-tables | PMID:27208134; DOI:10.1128/AEM.00789-16; Table 1; Table 2; Table 3; Figure 1 | supports | All three complete main tables were read: primers and selected expression results. Only Figure 1 pixels were recovered and viewed; it shows early/mid/late DEG counts for both taxa. The other four main figure captions were read, but their pixels and the supplementary PDF/workbooks were not recovered. |
| deposit-declaration | PMID:27208134; DOI:10.1128/AEM.00789-16; Materials and Methods: Accession number(s)., displayed lines 200–202 | supports | The article explicitly deposits RNA-sequencing data under PRJNA280696. This is a study resource distinct from the two publication-context DOI entries and from the prior genomes used for alignment. |
| ontology | /private/tmp/cm-review-session/batch-12/000264/ontology-authority.json; Eleven encoded ID-label/definition pairs across 19 occurrences | supports | All encoded labels match their identifiers. Label correctness does not establish donor recipient metabolism, focal carbon fixation, chemical supply or direct transfer. |
| schema | /private/tmp/cm-review-session/batch-12/000264/child-schema-semantics.json; FunctionalRoleEnum; cultivation, abundance and evidence definitions | supports | CROSS_FEEDER utilizes metabolites from other taxa; PRIMARY_PRODUCER fixes carbon as an autotroph. Ordinal ABUNDANT has no required fixed percentage. Roles and interaction mechanisms must be assessed under their actual definitions. |
| go-options | /private/tmp/cm-review-session/batch-12/000264/child-go-light-process-candidates.json; Exact bounded label/synonym query and OAK definitions for GO:0009765 and GO:0019684 | supports | GO:0009765 describes light-energy absorption/transfer and is only an optional source-supported candidate. GO:0019684 includes oxygenic photosystems and water oxidation, so it is unsuitable as a generic replacement. Omission of unsupported GO:0015979 is acceptable; this bounded lookup does not prove no other suitable term exists. |
| gtdb | /private/tmp/cm-review-session/batch-12/000264/child-gtdb-crosswalk.json; Exact rows and ncbi_id resolution for 573061 and 258594 | supports | Current strain descriptors map exactly to Clostridium_K cellulovorans at 1.0/four genomes and Rhodopseudomonas palustris_F at 1.0/two. Both lineages and core counts are valid. Local mtime does not establish a GTDB release named latest or its build date. |
| strain | /private/tmp/cm-review-session/batch-12/000264/child-strain-authority.json; Current NCBI strain ranks/parents; fresh ATCC BAA-98 and explicit recent DSM 3052 reuse | supports | CGA009 is ATCC BAA-98, a chloramphenicol-resistant derivative of CGA001; the two designations are not interchangeable. Recent 174 catalogue identity alone is reused for 743B/DSM 3052/ATCC 35296. No prior-record protocol or catalogue maintenance medium is imported. |
| semantics | /private/tmp/cm-review-session/batch-12/000264/ontology-semantic-notes.json; Final source-specific roles, chemistry, graph and cultivation assessment | supports | Retain donor PRIMARY_DEGRADER, recipient CROSS_FEEDER, ordinals and the three-node/one-arrow qualified graph. Narrow unsupported recipient/autotrophy assertions and distinguish fermentation intermediates from medium inputs. |
| resources | /private/tmp/cm-review-session/batch-12/000264/dataset-verification.json; Verified publication identities, declared project and bounded SI inventory | supports | Both DOI entries are correctly identified publications and may remain explicit publication context. Add the verified transcriptome deposit. SI filenames are declaration-only; original asset-label error is superseded by the separately pinned correction. No arbitrary archive absence finding is made. |
| project | /private/tmp/cm-review-session/batch-12/000264/declared-project-verification.json; Whole official project XML, 18 run rows and nine BioSample attribute projections | supports | PRJNA280696/SRP057083 contains 18 paired RNA-Seq runs across nine samples: CC, Co and RP at early/mid/late phases, two runs per sample. Specific source_name/sample_type/strain attributes identify arms. Co top-level taxon labels say C. cellulovorans and RP labels say mixed culture, contrary to their specific attributes. Preserve the metadata discrepancy; do not infer biological membership or independent replicate counts from broad labels/runs. |
| snippets | /private/tmp/cm-review-session/batch-12/000264/snippet-audit.json; Twenty reference-specific Abstract/IMPORTANCE excerpt occurrences | supports | Eighteen match fresh NCBI text strictly; two require explicitly documented H2 inline-spacing projections. All 20 match their selected caches. The direct NCBI response is front matter only, while the separate PMC reader supplies the main body. Excerpt matching alone is not source support. |
| history | /private/tmp/cm-review-session/batch-12/000264/provenance-audit.json; Whole sole history, exact batch 20 row/adversarial context and current 1330/1333 bodies/comments | supports | The prior graph repair is retained. Current 1330 is closed with one comment; shared non-graph 1333 remains open with no comments. Its older abundance request is assessed against current ordinal semantics. Issue 746 concerns another record. No issue is changed or closed by this review. |
| inspect | /private/tmp/cm-review-session/batch-12/000264/inspect.json; Fresh official 28-input inspection | supports | Canonical record, three focal caches, sole history, exact decision/adversarial context and 21 authorities are pinned. Ignored-inclusive focal discovery found no additional review within the searched scope; broad logs and prior-record citation-only sources were not used as new science. |
| assets | /private/tmp/cm-review-session/batch-12/000264/source-assets-corrected.json; Complete 2016 reader coverage; only Figure 1 pixels; declared unavailable SI and 2015 access routes | supports | Reader lines 105–551 cover all scientific text, three tables, five captions and 70 references; 552–565 identify supplements. Duplicate formatting conflicts concern citation markers, not scientific content. EPMC package returned a non-OA XML error, PMC files captcha HTML and publisher SI 403 HTML. None are misrepresented as PDF/XLSX/ZIP payloads. |
| asset-correction | /private/tmp/cm-review-session/batch-12/000264/source-assets-label-correction.json; Exact one-field SI-label correction and downstream pointer-only variants | supports | Main references identify Table S1 as C. cellulovorans DEGs, Table S2 as R. palustris DEGs and Figure S3 as RT-qPCR comparison. Frozen original asset/read/source receipts and dataset pins remain intact; corrected variants supersede only the label/pointers, with unchanged findings and timestamps. |
| lead-read | /private/tmp/cm-review-session/batch-12/000264/lead-primary-read-scope-final.json; Whole 2016 scientific reader text, tables/references and one visual; bounded 2015/SI scope | supports | Lead read the complete available 2016 main and viewed Figure 1. The founding main, remaining images and SI payloads remain unavailable. Authority, provenance and archive-reading boundaries are explicit; no raw reanalysis or experiment was performed. |
| source-scope | /private/tmp/cm-review-session/batch-12/000264/source-audit-final.json; Five final findings and partial scientific completion | supports | Three major findings address roles/process grounding, acetate feed placement and stronger non-graph claims. Two minor findings address the verified project link and GTDB provenance. Current gradient implicated wording and thiamine likely wording are preserved as qualified. |
| root-source | /private/tmp/cm-review-session/batch-12/000264/root-independent-source-audit.json; Independent complete available main, authority and supporting-source assessment | supports | Root independently read all recovered main text and references, the main tables, only Figure 1 pixels, and exact authority/provenance/resource scopes. It agrees with partial scientific status and the five groups. |
| metrics | /private/tmp/cm-review-session/batch-12/000264/support-final-audit.json; Distinct final support and native score arithmetic | supports | Completeness 85. Five evidence occurrences over three nodes give mean 5/3 and bonus 16.6667; COMPLETE adds 15. Three major and two minor findings produce raw and capped quality 97.6666666667. All 28 inspected input bytes remain unchanged. |
| support-manifest | /private/tmp/cm-review-session/batch-12/000264/supporting-artifact-manifest.json; Final frozen supporting receipts | supports | Final support pins actual source, resource, snippet, provenance and correction scopes. Preliminary support remains immutable. |
| auxiliary | /private/tmp/cm-review-session/batch-12/000264/auxiliary-frozen-manifest.json; Final native and authority receipts | supports | Eight native checks pass; 11 pairs across 19 occurrences match. Initial validator remains unchanged. Scratch helper preparation errors are disclosed separately and are not record-validation failures. |
| final-native | /private/tmp/cm-review-session/batch-12/000264/final-validator-summary.json; Eight focused command results and unchanged input/cache checks | supports | Schema, strict, term, reference, GTDB, domain, history and cache-name checks pass. Native zero reference issues is not an excerpt count and does not certify scientific entailment. |
| adapter | /private/tmp/cm-review-session/batch-12/000264/adapter-check.json; Fresh batch 12 runtime checks and explicit batch 11 discovery reuse at 2026-10-21T19:20:45.556660+00:00 | supports | Runtime/PATH/module availability was freshly checked. Filename-search discovery is explicitly reused from batch 11 record 403, not a fresh batch 12 search. The other-checkout runner was not executed; no global absence or installation is claimed. |
| check-validate | /private/tmp/cm-review-session/batch-12/000264/validate.json; Actual focused command and output | supports | Native command outcome; scientific support assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-12/000264/validate-strict.json; Actual focused command and output | supports | Native command outcome; scientific support assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-12/000264/validate-terms.json; Actual focused command and output | supports | Native command outcome; scientific support assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-12/000264/validate-references-explained.json; Actual focused command and output | supports | Native command outcome; scientific support assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-12/000264/validate-gtdb.json; Actual focused command and output | supports | Native command outcome; scientific support assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-12/000264/validate-gtdb-domain.json; Actual focused command and output | supports | Native command outcome; scientific support assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-12/000264/validate-history.json; Actual focused command and output | supports | Native command outcome; scientific support assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-12/000264/normalize-cache-names-check.json; Actual focused command and output | supports | Native command outcome; scientific support assessed separately. |
| check-audit-network | /private/tmp/cm-review-session/batch-12/audit-network.json; Same-batch corpus diagnostic | supports | Actual corpus result retained; later records are not assessed. |
| check-check-network-quality | /private/tmp/cm-review-session/batch-12/check-network-quality.json; Same-batch corpus diagnostic | supports | Actual corpus result retained; later records are not assessed. |

## Limits And Additional Notes

- Whole 2016 reader text, all three tables, five captions and 70 references were read. Only Figure 1 pixels were viewed. Figures 2–5 and SI PDF/workbooks were not recovered; their captions/references do not certify the images or internal data.
- The 2015 physiology paper is bibliographically verified but its main body and concentration-series/recipe details remain unavailable. Reprinted 3 g/L physiology in the 2016 text does not replace full original-paper assessment. Overall scientific completion remains partial/false.
- Failed EPMC/PMC/publisher responses are preserved with actual signatures; HTTP 200 captcha/error bodies are not PDFs, spreadsheets or ZIPs. Corrected asset metadata supersedes a Table S1/Figure S3 labeling error without altering frozen original receipts or grades.
- The 20 field excerpt occurrences have 18 strict fresh matches and two explicit H2-spacing projections; all match selected caches. None of the small caches is a verified full article. Literal matching does not establish mechanism or role entailment.
- No raw RNA-seq reanalysis, image digitization, flux calculation, genome reclassification or biological experiment was performed. Archive top-level organism labels conflict with specific sample attributes and are not promoted to biological conclusions.
- Optional adapter availability is fresh batch 12 runtime scope with explicitly reused batch 11 discovery. Initial validator/support and all source corrections remain immutable. No canonical change, external message, paid access or save by lead.
- Three major/two minor findings; completeness 85; raw/capped quality 97.6666666667.
- Whole-record coverage describes target selection, not complete source access; scientific_review remains false.
- Coordinate existing shared 1333; retain closed graph repair 1330 and all current qualified graph boundaries.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T215825Z-cellulose-biohydrogen-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Cellulose biohydrogen roles, medium and inference review
started_at: '2026-10-21T21:47:43.236946Z'
finished_at: '2026-10-21T21:58:25.716894Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed science, authorities and support; no
    person-level independence asserted.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: Partial source review finds three major role/process, acetate-feed and non-graph
  attribution issues, plus two minor project-link and GTDB-provenance issues. The
  complete 2016 reader text supports these findings; the 2015 body and claim-relevant
  SI remain unavailable. Preserve the qualified three-node/one-arrow graph. Native
  checks pass; completeness 85 and quality 97.6666666667.
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
  - path: history/records/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture/2026-10-06T002338Z-codex-e65507.yaml
    sha256: 398d34ea4df685e394e2b1cea9c9453e629bedf8543b61fc2c7fde2fdc1d5a1c
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    sha256: 609d1b7276a71d3a613fe7ffc299e75b6e4862e12c8057e6edf87822ff2816cb
    role: target
  - path: references_cache/PMID_27208134.txt
    sha256: 9d217a9411ef01ac74c463007b02d481416dddf69e9bec7f3e787eb1afd85030
    role: context
  - path: references_cache/doi_10.1016_j.ijhydene.2015.05.135.md
    sha256: 01532520b45cb0bd05fa687240e472da0ce62c716a1a39c17114101dc9c02b8c
    role: context
  - path: references_cache/doi_10.1128_AEM.00789-16.md
    sha256: 472f88aa5a51f01cec1bd55f0c241f1a048b0ce5301f211c31b5812cea0f229d
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261005-batch20.yaml
    sha256: a75fc7a6bce8c3b04e20b5a5b9e061b503e803bc312fbf6c5dcb49e6cfc3032b
    role: context
  - path: reports/causal_graph_review/decisions/20261005-three-records-batch20.yaml
    sha256: febd25cb92f04767991d8f3e54abf8e636a17c04b2cf97d5bd61ba9b6b400a45
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
- target_id: CommunityMech:000264
  path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
  label: Clostridium cellulovorans-Rhodopseudomonas palustris Cellulose Biohydrogen
    Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
scope:
  description: Whole maintained record and all available focal source text assessed,
    with explicit missing main/SI/visual coverage.
  selection: Only released CommunityMech:000264 in owned batch 12.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000264
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000264
  command: just --no-dotenv validate kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Owned batch 12; unchanged canonical inputs.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000264
  command: just --no-dotenv validate-strict kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-12/000264/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Owned batch 12; unchanged canonical inputs.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000264
  command: just --no-dotenv validate-terms kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Owned batch 12; unchanged canonical inputs.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000264
  command: just --no-dotenv validate-references-explained kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Owned batch 12; unchanged canonical inputs.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000264
  command: just --no-dotenv validate-gtdb kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Owned batch 12; unchanged canonical inputs.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000264
  command: just --no-dotenv validate-gtdb-domain kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Owned batch 12; unchanged canonical inputs.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000264
  command: just --no-dotenv validate-history history/records/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Owned batch 12; unchanged canonical inputs.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Focused native command exit 0.
  target_ids:
  - CommunityMech:000264
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Owned batch 12; unchanged canonical inputs.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Same-batch corpus diagnostic retained.
  target_ids:
  - CommunityMech:000264
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
  - CommunityMech:000264
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
  status: unavailable
  required: true
  summary: Whole 2016 reader text available; 2015 body, most images and SI unavailable,
    so scientific review remains partial.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - assets
  - lead-read
  - source-scope
  - root-source
- check_id: direct-excerpts
  name: Reference-specific excerpt verification
  status: passed
  required: true
  summary: 18 strict fresh plus two explicit H2-spacing projections; all 20 cache
    matches.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - snippets
- check_id: authority-review
  name: Ontology and schema semantics
  status: passed
  required: true
  summary: Eleven pairs/19 occurrences match; literal roles and source support assessed.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - ontology
  - schema
  - gtdb
  - strain
- check_id: adapter
  name: Optional structured adapter
  status: unavailable
  required: false
  summary: Fresh runtime availability with explicit earlier filename-discovery reuse.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - adapter
- check_id: reanalysis
  name: Raw-data or experimental reproduction
  status: skipped
  required: false
  summary: No raw reads, flux analysis, genome reclassification or biological experiment.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - lead-read
  - project
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
  locator: Whole maintained record
  summary: The exact two-strain coculture has three nodes and one qualified arrow.
    Stronger non-graph annotations and medium placement require repair; native validity
    does not establish biological entailment.
  support: supports
  accessed_at: '2026-10-21T21:58:25.701915Z'
- evidence_id: identity
  kind: primary_source
  reference: PMID:27208134; DOI:10.1128/AEM.00789-16
  locator: 'Abstract; Introduction, displayed lines 125–128; Materials and Methods:
    Culture experimental conditions., lines 130–136'
  summary: The focal pair is C. cellulovorans 743B and R. palustris CGA009. The earlier
    physiology study and later transcriptomic experiments use this pair, but the 2015
    full body remains unavailable. A constitutive-nitrogenase mutant is explicitly
    excluded. Laboratory assembly supports SYNTHETIC and ENGINEERED without implying
    a new genetic construct.
  support: supports
  accessed_at: '2026-10-21T21:58:25.702146Z'
  snapshot_sha256: cc44e73308beb79139665512e745a2f36ac7caa3c383fcb0cf86da88e9950c57
- evidence_id: feed
  kind: primary_source
  reference: PMID:27208134; DOI:10.1128/AEM.00789-16
  locator: 'Materials and Methods: Culture experimental conditions., lines 131–134;
    Results and Discussion: Bacterial chemotaxis., lines 404–408'
  summary: The coculture receives 3 g/L cellulose; 20 mM acetate is the R. palustris
    monoculture substrate. Coculture VFAs begin at zero and accumulate through fermentation.
    Acetate in the coculture composition therefore confuses a produced intermediate
    with an added feed. The source separates light energy from VFA carbon for R. palustris.
  support: supports
  accessed_at: '2026-10-21T21:58:25.702369Z'
  snapshot_sha256: cc44e73308beb79139665512e745a2f36ac7caa3c383fcb0cf86da88e9950c57
  quote: began at zero
- evidence_id: operation
  kind: primary_source
  reference: PMID:27208134; DOI:10.1128/AEM.00789-16
  locator: 'Materials and Methods: Culture experimental conditions., lines 131–136'
  summary: The 2016 assay uses 100 mL medium in 160-mL serum bottles, 30°C, 100 rpm
    and 6,000 lx from six 15-W Grolux tubes. Argon fills the headspace; glutamate
    replaces ammonium as nitrogen source, without a stated concentration. Buffers
    are 30 mM sodium bicarbonate and 10 mM TES; initial pH is 7.2 and subsequently
    changes. Coculture inoculation is a 1:4 C. cellulovorans:R. palustris cell ratio,
    not a transfer percentage or absolute density.
  support: supports
  accessed_at: '2026-10-21T21:58:25.702613Z'
  snapshot_sha256: cc44e73308beb79139665512e745a2f36ac7caa3c383fcb0cf86da88e9950c57
- evidence_id: assays
  kind: primary_source
  reference: PMID:27208134; DOI:10.1128/AEM.00789-16
  locator: 'Materials and Methods: RNA extraction and sequencing.; RNA-sequencing
    data analysis.; RT-qPCR.; Table 1'
  summary: Three culture arms and three growth phases have two biological cultures
    per arm/phase, yielding 18 RNA samples. RNA-seq uses HiSeq 2000 and named reference
    genomes. NOIseq probability q ≥0.8 and absolute log2 fold change ≥1 define differential
    expression. RT-qPCR checks 16 genes, eight per organism, with two biological and
    two technical replicates. This experimental evidence is not automatically COMPUTATIONAL
    because analysis uses software.
  support: supports
  accessed_at: '2026-10-21T21:58:25.702830Z'
  snapshot_sha256: cc44e73308beb79139665512e745a2f36ac7caa3c383fcb0cf86da88e9950c57
- evidence_id: hydrogen
  kind: primary_source
  reference: PMID:27208134; DOI:10.1128/AEM.00789-16
  locator: 'Results and Discussion: H2 production., displayed lines 230–231 and 379–388;
    Materials and Methods: Culture experimental conditions., lines 135–136'
  summary: Ammonium at 11.2 mM reduces coculture hydrogen to 46 mL, 20 mL below the
    unamended coculture and 6 mL above amended C. cellulovorans monoculture; amended
    R. palustris monocultures produce no hydrogen. Together with nitrogenase expression,
    this supports involvement in the enhanced component. It does not directly partition
    all gas between partners or establish N2 fixation under argon. SI Figures S6–S7
    are referenced by the main but unread.
  support: supports
  accessed_at: '2026-10-21T21:58:25.703149Z'
  snapshot_sha256: cc44e73308beb79139665512e745a2f36ac7caa3c383fcb0cf86da88e9950c57
- evidence_id: exchange
  kind: primary_source
  reference: PMID:27208134; DOI:10.1128/AEM.00789-16
  locator: 'Results and Discussion: Cellulose degradation.; Fatty acid metabolism.;
    Bacterial chemotaxis.; Figure 2 caption; Figure 5 caption and concluding paragraphs'
  summary: VFA profiles, pH and expression support the authors’ exchange model. The
    2016 Figure 2 caption identifies a 3 g/L comparison modified from the 2015 source,
    with biological triplicates. Chemotaxis and a spatial gradient remain inferred
    from expression and feeding context. The final conceptual model is based on transcript
    levels, not measured partner flux or selective proof that expression causes output.
  support: supports
  accessed_at: '2026-10-21T21:58:25.703421Z'
  snapshot_sha256: cc44e73308beb79139665512e745a2f36ac7caa3c383fcb0cf86da88e9950c57
- evidence_id: light-carbon
  kind: primary_source
  reference: PMID:27208134; DOI:10.1128/AEM.00789-16
  locator: 'Materials and Methods: Culture experimental conditions., lines 133–134;
    Results and Discussion: Photosynthesis., lines 446–451'
  summary: R. palustris uses light as energy and organic VFA carbon in coculture.
    Increased photosynthesis-gene expression accompanies this physiology. These observations
    do not establish focal inorganic-to-organic carbon fixation, even though the organism
    may have that capability in other conditions.
  support: supports
  accessed_at: '2026-10-21T21:58:25.703523Z'
  snapshot_sha256: cc44e73308beb79139665512e745a2f36ac7caa3c383fcb0cf86da88e9950c57
- evidence_id: stress-population
  kind: primary_source
  reference: PMID:27208134; DOI:10.1128/AEM.00789-16
  locator: 'Results and Discussion: Sulfur metabolism.; Thiamine metabolism.; Other
    genes and pathways of significance.'
  summary: Sulfur/thiamine transcription is correlated with pH and interpreted as
    stress response. It is not evidence of thiamine supplementation, transfer or quantified
    secretion. C. cellulovorans has no significant cell-density difference between
    mono- and coculture in the reported comparison. The initial 1:4 ratio is not a
    persistent abundance fraction; ordinal ABUNDANT remains permissible.
  support: supports
  accessed_at: '2026-10-21T21:58:25.703594Z'
  snapshot_sha256: cc44e73308beb79139665512e745a2f36ac7caa3c383fcb0cf86da88e9950c57
- evidence_id: main-tables
  kind: primary_source
  reference: PMID:27208134; DOI:10.1128/AEM.00789-16
  locator: Table 1; Table 2; Table 3; Figure 1
  summary: 'All three complete main tables were read: primers and selected expression
    results. Only Figure 1 pixels were recovered and viewed; it shows early/mid/late
    DEG counts for both taxa. The other four main figure captions were read, but their
    pixels and the supplementary PDF/workbooks were not recovered.'
  support: supports
  accessed_at: '2026-10-21T21:58:25.703665Z'
  snapshot_sha256: cc44e73308beb79139665512e745a2f36ac7caa3c383fcb0cf86da88e9950c57
- evidence_id: deposit-declaration
  kind: primary_source
  reference: PMID:27208134; DOI:10.1128/AEM.00789-16
  locator: 'Materials and Methods: Accession number(s)., displayed lines 200–202'
  summary: The article explicitly deposits RNA-sequencing data under PRJNA280696.
    This is a study resource distinct from the two publication-context DOI entries
    and from the prior genomes used for alignment.
  support: supports
  accessed_at: '2026-10-21T21:58:25.704004Z'
  snapshot_sha256: cc44e73308beb79139665512e745a2f36ac7caa3c383fcb0cf86da88e9950c57
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000264/ontology-authority.json
  locator: Eleven encoded ID-label/definition pairs across 19 occurrences
  summary: All encoded labels match their identifiers. Label correctness does not
    establish donor recipient metabolism, focal carbon fixation, chemical supply or
    direct transfer.
  support: supports
  accessed_at: '2026-10-21T21:58:25.704285Z'
  snapshot_sha256: 0e31078f18084bc39b0687e9ea8e785e74d7654f9d1f5584da572d1eef65da4b
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000264/child-schema-semantics.json
  locator: FunctionalRoleEnum; cultivation, abundance and evidence definitions
  summary: CROSS_FEEDER utilizes metabolites from other taxa; PRIMARY_PRODUCER fixes
    carbon as an autotroph. Ordinal ABUNDANT has no required fixed percentage. Roles
    and interaction mechanisms must be assessed under their actual definitions.
  support: supports
  accessed_at: '2026-10-21T21:58:25.704569Z'
  snapshot_sha256: de8496089c7901bb4ba1b2917133cd15cda62fe3ae3892999000e8387f6def59
- evidence_id: go-options
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000264/child-go-light-process-candidates.json
  locator: Exact bounded label/synonym query and OAK definitions for GO:0009765 and
    GO:0019684
  summary: GO:0009765 describes light-energy absorption/transfer and is only an optional
    source-supported candidate. GO:0019684 includes oxygenic photosystems and water
    oxidation, so it is unsuitable as a generic replacement. Omission of unsupported
    GO:0015979 is acceptable; this bounded lookup does not prove no other suitable
    term exists.
  support: supports
  accessed_at: '2026-10-21T21:58:25.705122Z'
  snapshot_sha256: 3cdf25d4a58bfde3fc8fde5640cb4da788005f59ac07632e566d2c619e2e5a9d
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000264/child-gtdb-crosswalk.json
  locator: Exact rows and ncbi_id resolution for 573061 and 258594
  summary: Current strain descriptors map exactly to Clostridium_K cellulovorans at
    1.0/four genomes and Rhodopseudomonas palustris_F at 1.0/two. Both lineages and
    core counts are valid. Local mtime does not establish a GTDB release named latest
    or its build date.
  support: supports
  accessed_at: '2026-10-21T21:58:25.705571Z'
  snapshot_sha256: 9a82ee6f7b4c1fd07445c05238264baca4cf312365dc07b07f8415515bb46048
- evidence_id: strain
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000264/child-strain-authority.json
  locator: Current NCBI strain ranks/parents; fresh ATCC BAA-98 and explicit recent
    DSM 3052 reuse
  summary: CGA009 is ATCC BAA-98, a chloramphenicol-resistant derivative of CGA001;
    the two designations are not interchangeable. Recent 174 catalogue identity alone
    is reused for 743B/DSM 3052/ATCC 35296. No prior-record protocol or catalogue
    maintenance medium is imported.
  support: supports
  accessed_at: '2026-10-21T21:58:25.706013Z'
  snapshot_sha256: 6b83cb020d80b0fe7f48a02e908a562658108a72d67825f61bc00709e9238279
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-12/000264/ontology-semantic-notes.json
  locator: Final source-specific roles, chemistry, graph and cultivation assessment
  summary: Retain donor PRIMARY_DEGRADER, recipient CROSS_FEEDER, ordinals and the
    three-node/one-arrow qualified graph. Narrow unsupported recipient/autotrophy
    assertions and distinguish fermentation intermediates from medium inputs.
  support: supports
  accessed_at: '2026-10-21T21:58:25.706437Z'
  snapshot_sha256: 55b4413ef83012c134feff4926048738659e2c52416663bccdccd213d2340290
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/dataset-verification.json
  locator: Verified publication identities, declared project and bounded SI inventory
  summary: Both DOI entries are correctly identified publications and may remain explicit
    publication context. Add the verified transcriptome deposit. SI filenames are
    declaration-only; original asset-label error is superseded by the separately pinned
    correction. No arbitrary archive absence finding is made.
  support: supports
  accessed_at: '2026-10-21T21:58:25.706895Z'
  snapshot_sha256: 5983eb4b87fd61f1ab56a223cad2077ad8ad4227a24927440404d8ccff6bc61f
- evidence_id: project
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/declared-project-verification.json
  locator: Whole official project XML, 18 run rows and nine BioSample attribute projections
  summary: 'PRJNA280696/SRP057083 contains 18 paired RNA-Seq runs across nine samples:
    CC, Co and RP at early/mid/late phases, two runs per sample. Specific source_name/sample_type/strain
    attributes identify arms. Co top-level taxon labels say C. cellulovorans and RP
    labels say mixed culture, contrary to their specific attributes. Preserve the
    metadata discrepancy; do not infer biological membership or independent replicate
    counts from broad labels/runs.'
  support: supports
  accessed_at: '2026-10-21T21:58:25.707252Z'
  snapshot_sha256: e76a2186e8627efc6b0619156fb151fa43b67d9db2df6aef1f229b7dd127c2dc
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/snippet-audit.json
  locator: Twenty reference-specific Abstract/IMPORTANCE excerpt occurrences
  summary: Eighteen match fresh NCBI text strictly; two require explicitly documented
    H2 inline-spacing projections. All 20 match their selected caches. The direct
    NCBI response is front matter only, while the separate PMC reader supplies the
    main body. Excerpt matching alone is not source support.
  support: supports
  accessed_at: '2026-10-21T21:58:25.707576Z'
  snapshot_sha256: d06fbb891bde24f3e27c2c07c821d3564b37eea8b7af575b3986e6882f7989a3
- evidence_id: history
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-12/000264/provenance-audit.json
  locator: Whole sole history, exact batch 20 row/adversarial context and current
    1330/1333 bodies/comments
  summary: The prior graph repair is retained. Current 1330 is closed with one comment;
    shared non-graph 1333 remains open with no comments. Its older abundance request
    is assessed against current ordinal semantics. Issue 746 concerns another record.
    No issue is changed or closed by this review.
  support: supports
  accessed_at: '2026-10-21T21:58:25.707859Z'
  snapshot_sha256: 8ad4879d5678138c06981ef37ef57edba7f3f614682bdea2a01affe89907962f
- evidence_id: inspect
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/inspect.json
  locator: Fresh official 28-input inspection
  summary: Canonical record, three focal caches, sole history, exact decision/adversarial
    context and 21 authorities are pinned. Ignored-inclusive focal discovery found
    no additional review within the searched scope; broad logs and prior-record citation-only
    sources were not used as new science.
  support: supports
  accessed_at: '2026-10-21T21:58:25.708283Z'
  snapshot_sha256: 82cb2d9b52c8d51f16a9334bf93293d78d80409dcc5094e444c74780f67bbeb2
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/source-assets-corrected.json
  locator: Complete 2016 reader coverage; only Figure 1 pixels; declared unavailable
    SI and 2015 access routes
  summary: Reader lines 105–551 cover all scientific text, three tables, five captions
    and 70 references; 552–565 identify supplements. Duplicate formatting conflicts
    concern citation markers, not scientific content. EPMC package returned a non-OA
    XML error, PMC files captcha HTML and publisher SI 403 HTML. None are misrepresented
    as PDF/XLSX/ZIP payloads.
  support: supports
  accessed_at: '2026-10-21T21:58:25.708448Z'
  snapshot_sha256: cd631b69da459fc7f63195432db130440aa77c594da68e6b1c1b63cd37934277
- evidence_id: asset-correction
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/source-assets-label-correction.json
  locator: Exact one-field SI-label correction and downstream pointer-only variants
  summary: Main references identify Table S1 as C. cellulovorans DEGs, Table S2 as
    R. palustris DEGs and Figure S3 as RT-qPCR comparison. Frozen original asset/read/source
    receipts and dataset pins remain intact; corrected variants supersede only the
    label/pointers, with unchanged findings and timestamps.
  support: supports
  accessed_at: '2026-10-21T21:58:25.708698Z'
  snapshot_sha256: a33627ce20721dfde812f6885e484f2d243fde6cc0741ae14119e99fab2be147
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/lead-primary-read-scope-final.json
  locator: Whole 2016 scientific reader text, tables/references and one visual; bounded
    2015/SI scope
  summary: Lead read the complete available 2016 main and viewed Figure 1. The founding
    main, remaining images and SI payloads remain unavailable. Authority, provenance
    and archive-reading boundaries are explicit; no raw reanalysis or experiment was
    performed.
  support: supports
  accessed_at: '2026-10-21T21:58:25.708985Z'
  snapshot_sha256: 71073ff0992bf8f8dbe39dd2f366728f9c5a177d9388ab33ce46f040d64d8850
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/source-audit-final.json
  locator: Five final findings and partial scientific completion
  summary: Three major findings address roles/process grounding, acetate feed placement
    and stronger non-graph claims. Two minor findings address the verified project
    link and GTDB provenance. Current gradient implicated wording and thiamine likely
    wording are preserved as qualified.
  support: supports
  accessed_at: '2026-10-21T21:58:25.709223Z'
  snapshot_sha256: cbcece0dec8d16adb82c8b427115d09b7ba926ef8bc5089a9873ee0bb28e77df
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/root-independent-source-audit.json
  locator: Independent complete available main, authority and supporting-source assessment
  summary: Root independently read all recovered main text and references, the main
    tables, only Figure 1 pixels, and exact authority/provenance/resource scopes.
    It agrees with partial scientific status and the five groups.
  support: supports
  accessed_at: '2026-10-21T21:58:25.709480Z'
  snapshot_sha256: fa54c290e304bd52845ec0938e6b446a5cf31a7a72c290ef9cd87b9202e74660
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/support-final-audit.json
  locator: Distinct final support and native score arithmetic
  summary: Completeness 85. Five evidence occurrences over three nodes give mean 5/3
    and bonus 16.6667; COMPLETE adds 15. Three major and two minor findings produce
    raw and capped quality 97.6666666667. All 28 inspected input bytes remain unchanged.
  support: supports
  accessed_at: '2026-10-21T21:58:25.709919Z'
  snapshot_sha256: 1fff73c21bb718bfe701f3c02d4809a3f57cf8f0a31d7934079289b845dde9e4
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/supporting-artifact-manifest.json
  locator: Final frozen supporting receipts
  summary: Final support pins actual source, resource, snippet, provenance and correction
    scopes. Preliminary support remains immutable.
  support: supports
  accessed_at: '2026-10-21T21:58:25.710089Z'
  snapshot_sha256: 74b714335e920249a919086564ec4704b08d2d23243d46b9405aec19de57253b
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/auxiliary-frozen-manifest.json
  locator: Final native and authority receipts
  summary: Eight native checks pass; 11 pairs across 19 occurrences match. Initial
    validator remains unchanged. Scratch helper preparation errors are disclosed separately
    and are not record-validation failures.
  support: supports
  accessed_at: '2026-10-21T21:58:25.710324Z'
  snapshot_sha256: 3dd2b81c0b43fda28a7cfa93b02b38d6e501b7bc7e87a1bc371a4357f7740d8b
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/final-validator-summary.json
  locator: Eight focused command results and unchanged input/cache checks
  summary: Schema, strict, term, reference, GTDB, domain, history and cache-name checks
    pass. Native zero reference issues is not an excerpt count and does not certify
    scientific entailment.
  support: supports
  accessed_at: '2026-10-21T21:58:25.710965Z'
  snapshot_sha256: 98dbf8f01c17f8388c8dcdb5fe600865b5a1583f996b34aac0e32f9d1e72ae3e
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/adapter-check.json
  locator: Fresh batch 12 runtime checks and explicit batch 11 discovery reuse at
    2026-10-21T19:20:45.556660+00:00
  summary: Runtime/PATH/module availability was freshly checked. Filename-search discovery
    is explicitly reused from batch 11 record 403, not a fresh batch 12 search. The
    other-checkout runner was not executed; no global absence or installation is claimed.
  support: supports
  accessed_at: '2026-10-21T21:58:25.711267Z'
  snapshot_sha256: bdee7f946fc732e1d423ca169b5cf91e52151a54c991bfd2bd917887415f5ee6
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/validate.json
  locator: Actual focused command and output
  summary: Native command outcome; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:58:25.711834Z'
  snapshot_sha256: 63b642038c4123d71fa2a3c302e1c6e6b90e71af22d25a4e3749734095e95cec
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/validate-strict.json
  locator: Actual focused command and output
  summary: Native command outcome; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:58:25.712455Z'
  snapshot_sha256: c2f79e8b305f7baed66f68d4f95639e690cbdefdca5cc8f3ccc3fe922cc41bed
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/validate-terms.json
  locator: Actual focused command and output
  summary: Native command outcome; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:58:25.712948Z'
  snapshot_sha256: f9b0fb1a349132d19619c5958ffae467b6382242fdd31fcf0c98414bd0e9b50b
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/validate-references-explained.json
  locator: Actual focused command and output
  summary: Native command outcome; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:58:25.713421Z'
  snapshot_sha256: bfd0616387480d6c275bb378db8bd4685bac5200de635c9e25403a0689b1c230
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/validate-gtdb.json
  locator: Actual focused command and output
  summary: Native command outcome; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:58:25.713909Z'
  snapshot_sha256: e7df188536d73bebe2a264fa14be7a82e8c290c60d6a8080a3e809f549c82bea
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/validate-gtdb-domain.json
  locator: Actual focused command and output
  summary: Native command outcome; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:58:25.714305Z'
  snapshot_sha256: 8ba3837092ff19d9e49b0e91606ee27536ea10826ef11277c20a595aa5255a7a
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/validate-history.json
  locator: Actual focused command and output
  summary: Native command outcome; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:58:25.714568Z'
  snapshot_sha256: 5040dd8ad4a4a44bfb2a6237cdc50f7bd98c088c9e33f46ae9203c170fbc1845
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/000264/normalize-cache-names-check.json
  locator: Actual focused command and output
  summary: Native command outcome; scientific support assessed separately.
  support: supports
  accessed_at: '2026-10-21T21:58:25.714967Z'
  snapshot_sha256: b78284b0148f50a5f14681d42a7ff00ebb67842fdb79285824c86b53ef8a685f
- evidence_id: check-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/audit-network.json
  locator: Same-batch corpus diagnostic
  summary: Actual corpus result retained; later records are not assessed.
  support: supports
  accessed_at: '2026-10-21T21:58:25.716190Z'
  snapshot_sha256: 1621a1dd35060a1052cf4669f27e9a936a82f4759be38e4f39a9a4a1a73a14b8
- evidence_id: check-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-12/check-network-quality.json
  locator: Same-batch corpus diagnostic
  summary: Actual corpus result retained; later records are not assessed.
  support: supports
  accessed_at: '2026-10-21T21:58:25.716813Z'
  snapshot_sha256: 34467f31f8dad2a00579e8350771795ee0f769be41af2e9435c88b603ec9fa1e
assessments:
- assessment_id: identity
  area: identity
  topic: Membership, origin and ecological setting
  outcome: supported
  summary: The exact 743B/CGA009 pair is the intended laboratory coculture.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - identity
  - strain
  details: Retain both strain terms, ENGINEERED/SYNTHETIC, LIGNOCELLULOSE and laboratory
    setting. Do not substitute the CGA001 ancestor, constitutive-nitrogenase mutant,
    monoculture or catalogue protocol.
- assessment_id: roles
  area: scope
  topic: Taxon functions and carbon-fixation grounding
  outcome: concern
  summary: Donor recipient metabolism and focal autotrophy are not established.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - feed
  - light-carbon
  - schema
  - ontology
  - go-options
  - semantics
  details: Require utilized partner-metabolite evidence for donor CROSS_FEEDER. Require
    focal CO2 fixation for recipient PRIMARY_PRODUCER and GO:0015979, or omit these
    optional assertions. Keep donor PRIMARY_DEGRADER and recipient CROSS_FEEDER; no
    claim of intrinsic inability is made.
- assessment_id: taxonomy
  area: grounding
  topic: Exact strain GTDB assignments
  outcome: concern
  summary: Core mappings are valid; release/build provenance is overstated.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - gtdb
  - strain
  details: Preserve exact-ID routes, classifications, lineages and four/two genome
    counts. File mtime is snapshot metadata, not proof of a release named latest.
- assessment_id: exchange-node
  area: graph
  topic: ecological_interactions[0] and downstream[0]
  outcome: supported
  summary: VFA supply and the qualified link to hydrogen remain appropriate.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - exchange
  - feed
  details: Keep the pairwise CROSS_FEEDING node and one downstream arrow. Cellulose
    is upstream feed, not a directly donated recipient substrate. Pool and pH changes
    do not resolve all partner flux or isolate pH as the only mediator.
- assessment_id: hydrogen-node
  area: graph
  topic: ecological_interactions[1]
  outcome: concern
  summary: Measured output and nitrogenase-control bounds are sound; the optional
    GO annotation is not.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - hydrogen
  - light-carbon
  - go-options
  details: Preserve the untyped community endpoint, ammonium intervention and distinction
    between enhanced hydrogen and all-flux partition. Correct GO:0015979 within the
    role/process finding; do not restore N2 fixation under argon or add obligatory
    syntrophy.
- assessment_id: transcript-node
  area: graph
  topic: ecological_interactions[2] and discussions[0]
  outcome: supported
  summary: Expression is measured while mediation remains an open question.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - assays
  - exchange
  details: Keep the untyped transcriptomic response node and the existing mechanistic
    discussion. Do not restore the removed expression-to-output arrow or treat a conceptual
    model as direct metabolite transfer.
- assessment_id: non-graph
  area: consistency
  topic: Related ingredient claims and gradient evidence
  outcome: concern
  summary: Bulk-H2 attribution and causal explanations exceed the qualified graph.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - hydrogen
  - exchange
  - stress-population
  details: Limit partner attribution to the authors’ inferred enhancement and control
    support. Qualify expression/chemotaxis explanations. The environmental-factor
    description already says implicated and thiamine relevance says likely; those
    are not separate categorical defects.
- assessment_id: cultivation
  area: scope
  topic: Medium input versus intermediate and culture stages
  outcome: concern
  summary: Acetate is incorrectly represented as a focal coculture feed.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - feed
  - operation
  details: Separate 20 mM acetate monocultures from 3 g/L cellulose coculture, secreted
    VFAs and ammonium intervention. Replace abstract-tier prose with recoverable 2016
    Methods while preserving the unavailable inherited recipe and 2015 concentration-series
    boundary.
- assessment_id: quantities
  area: quantity
  topic: Culture conditions and abundance basis
  outcome: supported
  summary: Recovered quantities require their source-specific bases.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - operation
  - stress-population
  details: A 1:4 cell ratio is not a transfer percentage or persistent abundance fraction;
    initial pH 7.2 is not a controlled setpoint. Keep ordinal ABUNDANT. Glutamate
    concentration, absolute inoculum density and full basal recipe remain unstated/unrecovered.
- assessment_id: assay-mode
  area: evidence
  topic: RNA-seq, RT-qPCR and physiological comparisons
  outcome: supported
  summary: Experimental measurements and inferential models are distinct.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - assays
  - hydrogen
  - main-tables
  details: Retain IN_VITRO for measured expression and controls. NOIseq q is differential-expression
    probability, not an invented FDR threshold. Do not infer quantitative pathway
    flux from transcript changes or replace experimental provenance solely because
    analysis is computational.
- assessment_id: chemistry
  area: grounding
  topic: Chemical terms and metal relevance
  outcome: supported
  summary: Identifiers match, with class/form and placement limits.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - ontology
  - semantics
  - feed
  details: Organic acid is broader than a VFA mixture; keep that breadth explicit.
    Thiamine(1+) is an expression-context chemical, not evidence of secretion. No
    medium salts or nitrogenase cofactor establish metal-processing relevance; retain
    NOT_APPLICABLE.
- assessment_id: resources
  area: representation
  topic: Publication context and actual transcriptome deposit
  outcome: concern
  summary: The verified study accession can be added with exact assay scope.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - deposit-declaration
  - project
  - resources
  details: Retain clearly labeled DOI publications and add PRJNA280696/SRP057083.
    Nine archive samples have 18 runs; specific attributes distinguish arms despite
    inconsistent top-level organism labels. No raw read analysis or arbitrary archive
    omission is asserted.
- assessment_id: excerpts
  area: evidence
  topic: Reference identity and literal excerpt support
  outcome: supported
  summary: All 20 excerpts are supported with explicit formatting limits.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - snippets
  details: Eighteen strict fresh Abstract/IMPORTANCE matches plus two H2 inline-spacing
    projections; all 20 cache matches. The 2015 cache is bibliographic/unavailable,
    and the two 2016 caches are short abstract material. No cache was refreshed or
    treated as full body.
- assessment_id: provenance
  area: provenance
  topic: Prior repairs and current issue ownership
  outcome: supported
  summary: Closed graph work and open shared non-graph follow-up are separated.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - history
  - inspect
  details: Coordinate with 1333 without closing its other records or reopening resolved
    1330 automatically. Exact prior scopes were selected sections, not whole body/SI.
    This review adds a broader but still incomplete scientific read.
- assessment_id: validation
  area: schema
  topic: Native gates and scientific completion
  outcome: supported
  summary: Eight focused native gates pass; source review remains partial.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - final-native
  - auxiliary
  - source-scope
  - root-source
  details: Native validity does not replace current-claim scientific support. Preserve
    all failed source-response payloads and explicit unread asset limits. The scratch
    asset-label correction is separate from candidate/native validation.
- assessment_id: metrics
  area: completeness
  topic: Native rubric and final finding counts
  outcome: supported
  summary: Completeness 85; raw and capped quality 97.6666666667.
  target_ids:
  - CommunityMech:000264
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: Required fields with roles 50 + environment term 5 + at least three
      interaction nodes 10 + growth media 10 + associated datasets 5 + node metabolites
      5. Two environmental factors and absent external_resources earn no bonus. Presence
      is not source support.
  - name: validation_quality
    value: 97.66666666666667
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 −50P1 −10P2 −2P3 +20min(mean node evidence/2,1) +15 if COMPLETE,0,100).
      P1=0, P2=3, P3=2, P4=0; five evidence occurrences/three nodes give mean 5/3
      and bonus 16.6666666667. COMPLETE adds 15. Raw and capped 97.6666666667.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 3
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
- finding_id: bound-functional-roles
  issue_key: cm-000264-bound-functional-roles
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Unsupported recipient and autotrophic functions materially
    alter biological interpretation.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Bound recipient and autotrophic role assertions
  description: Donor CROSS_FEEDER has no identified partner-derived metabolite utilization
    evidence. Recipient PRIMARY_PRODUCER and GO:0015979 require carbon fixation, while
    the focal Methods specify light energy and organic VFA carbon. Require source-local
    support or omit these optional assertions; retain donor PRIMARY_DEGRADER, recipient
    CROSS_FEEDER and the qualified output node.
  target_ids:
  - CommunityMech:000264
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  - ecological_interactions[1].biological_processes[0]
  evidence_ids:
  - feed
  - light-carbon
  - schema
  - ontology
  - go-options
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate with shared open
    issue 1333; retain resolved 1330 graph boundaries and do not close other targets.
    No issue mutation.
- finding_id: separate-feed-and-products
  issue_key: cm-000264-separate-feed-and-products
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: A product/control substrate is represented as a focal feed
    and could misdirect cultivation.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Separate coculture feed from monoculture and metabolic products
  description: The focal medium lists acetate although 20 mM acetate belongs to R.
    palustris monocultures and coculture VFAs initially equal zero. Remove unsupported
    acetate feed, preserve it as an exchanged intermediate, and replace abstract-tier
    preparation prose with the recoverable 2016 protocol. Keep the unavailable 2015
    concentration series and inherited recipe separate.
  target_ids:
  - CommunityMech:000264
  field_paths:
  - growth_media[0].composition[1]
  - growth_media[0].preparation_notes
  - growth_media[0].evidence[1]
  - growth_media[0]
  - engineering_design.perturbation_design
  evidence_ids:
  - feed
  - operation
  - identity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate with shared open
    issue 1333; retain resolved 1330 graph boundaries and do not close other targets.
    No issue mutation.
- finding_id: qualify-hydrogen-and-mechanism
  issue_key: cm-000264-qualify-hydrogen-and-mechanism
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: The stronger total-output and causal claims exceed the measurements
    and existing qualified graph.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Qualify hydrogen attribution and mechanistic explanations
  description: The hydrogen ingredient attributes the bulk of total hydrogen to R.
    palustris, while the source supports an inferred enhanced component and nitrogenase
    involvement. Other ingredient explanations promote expression and inferred chemotaxis
    to established mediation. Align them with the qualified graph; preserve already-qualified
    gradient and thiamine descriptions.
  target_ids:
  - CommunityMech:000264
  field_paths:
  - related_ingredients[0].relevance
  - related_ingredients[0].evidence[0].explanation
  - related_ingredients[1].relevance
  - related_ingredients[2].relevance
  - related_ingredients[2].evidence[0].explanation
  - environmental_factors[1].evidence[0].explanation
  evidence_ids:
  - hydrogen
  - exchange
  - stress-population
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate with shared open
    issue 1333; retain resolved 1330 graph boundaries and do not close other targets.
    No issue mutation.
- finding_id: link-declared-transcriptome
  issue_key: cm-000264-link-declared-transcriptome
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: The exact public study deposit is a recoverable resource omission.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Link the declared transcriptome project
  description: The publication-context entries omit explicitly declared and verified
    PRJNA280696/SRP057083. Add the RNA-seq project with exact culture-arm/sample/run
    scope. Existing DOI publications may remain as clearly labeled publication context.
  target_ids:
  - CommunityMech:000264
  field_paths:
  - associated_datasets
  evidence_ids:
  - deposit-declaration
  - project
  - resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate with shared open
    issue 1333; retain resolved 1330 graph boundaries and do not close other targets.
    No issue mutation.
- finding_id: document-gtdb-snapshot
  issue_key: cm-000264-document-gtdb-snapshot
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Mapping cores remain valid; the defect is unsupported provenance
    wording.
  rule_id: review-checklist.claim-specific-scope-and-grounding
  status: open
  certainty: confirmed
  title: Document the verified GTDB snapshot
  description: Both exact-ID GTDB cores are valid; latest-release/build wording is
    not established by local mtime. Retain classifications, lineages and four/two
    counts while reporting actual snapshot digest and lookup method.
  target_ids:
  - CommunityMech:000264
  field_paths:
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - strain
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  ownership_note: Maintained YAML owns future repair. Coordinate with shared open
    issue 1333; retain resolved 1330 graph boundaries and do not close other targets.
    No issue mutation.
actions:
- action_id: bound-roles
  description: Support or omit optional recipient/autotrophy annotations.
  finding_ids:
  - bound-functional-roles
  target_ids:
  - CommunityMech:000264
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - For donor CROSS_FEEDER, identify the provider, metabolite and local utilization
    evidence; product donation, pH relief and increased cellulose degradation alone
    do not establish receipt of partner metabolites. Otherwise omit that optional
    role. Retain donor PRIMARY_DEGRADER and recipient CROSS_FEEDER without an obligacy
    or nutrient-only criterion.
  - For R. palustris PRIMARY_PRODUCER and ecological_interactions[1].biological_processes[0]
    GO:0015979, require focal CO2-to-organic-carbon evidence or omit the optional
    annotations. Light energy plus organic VFA use does not establish this fixation
    claim. Do not assert CGA009 is incapable of fixation in other conditions.
  - 'Retain all three nodes and the one qualified arrow. A narrower process term is
    optional only with verified definition and source support: GO:0009765 concerns
    light harvesting, while GO:0019684 is not a generic anoxygenic-photofermentation
    replacement. Preserve ordinal ABUNDANT; do not demand an invented percentage.'
- action_id: repair-medium
  description: Separate focal feed, monoculture controls and recoverable protocol.
  finding_ids:
  - separate-feed-and-products
  target_ids:
  - CommunityMech:000264
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Remove the unsupported acetate input from the focal coculture composition. Retain
    acetate/VFAs as fermentation intermediates; 20 mM acetate belongs to R. palustris
    monocultures. The 2016 coculture has 3 g/L cellulose and initially zero VFAs.
    Attach exact Culture experimental conditions and Bacterial chemotaxis evidence,
    not merely a VFA-expression excerpt.
  - Recover 100 mL medium in 160-mL serum bottles, 30°C, 100 rpm, 6,000 lx from six
    15-W Grolux tubes, argon headspace, 30 mM bicarbonate and 10 mM TES. Initial pH
    7.2 is not an actively maintained setpoint. Record glutamate as nitrogen source
    with concentration unresolved; do not import another record or catalogue recipe.
  - Place the 1:4 C. cellulovorans:R. palustris cell ratio in suitable setup context;
    do not relabel it as transfer percentage, absolute density or persistent abundance.
    Separate the 11.2 mM ammonium intervention, culture-specific substrates and early/mid/late
    sampling. Preserve source replication rather than inferring it from run counts.
  - Replace abstract-only workflow prose with source-specific Methods evidence while
    preserving the unavailable inherited recipe and 2015 concentration-series details.
    The authors’ only-exogenous-substrate wording concerns designated cellulose feed;
    supplied bicarbonate and glutamate preclude an unqualified chemical carbon-exclusivity
    claim.
- action_id: qualify-mechanism
  description: Align stronger ingredient explanations with measured and inferred scope.
  finding_ids:
  - qualify-hydrogen-and-mechanism
  target_ids:
  - CommunityMech:000264
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Replace bulk-of-total-hydrogen attribution with the authors’ inference about the
    enhanced component. Preserve the ammonium intervention as evidence of nitrogenase
    involvement, without directly allocating all gas to a partner or inferring N2
    fixation under argon.
  - Keep the physiological VFA-exchange interpretation and smaller pH decline, but
    qualify gene-expression/chemotaxis explanations as model support. Distinguish
    inferred spatial gradients from measured chemotaxis, pools from flux and correlated
    stress responses from selective mediation. Do not restore the removed expression-to-output
    arrow.
  - Keep environmental_factors[1].description implicated wording and thiamine likely
    wording; their evidence explanations can explicitly retain inference. No separate
    categorical gradient or thiamine-secretion defect is asserted. Preserve the open
    mechanism discussion and state unavailable 2015/SI limits.
- action_id: link-project
  description: Add the verified transcriptome resource with submission boundaries.
  finding_ids:
  - link-declared-transcriptome
  target_ids:
  - CommunityMech:000264
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Add PRJNA280696, secondary SRP057083, as the source-declared SRA/ENA RNA-seq resource.
    Link the exact project; retain clearly identified DOI publication contexts if
    useful. Reference genomes NC_014393.1 and NC_005296.1 are background alignment
    resources, not new deposits.
  - Describe CC, Co and RP early/mid/late sample attributes, 18 paired runs and nine
    BioSamples, two runs per sample. Do not equate these counts to independent biological
    replication. Preserve the top-level archive label conflict for Co/RP; do not change
    membership or taxonomy from those labels alone.
  - Identify the three declared SI files as unavailable inventory only until real
    payloads are recovered. Main references call CC DEGs Table S1, RP DEGs Table S2
    and RT-qPCR Figure S3; do not certify unread worksheet structure or figures.
- action_id: document-mapping
  description: Record reproducible GTDB mapping provenance.
  finding_ids:
  - document-gtdb-snapshot
  target_ids:
  - CommunityMech:000264
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve exact NCBITaxon:573061 and 258594, current GTDB lineages, fractions 1.0
    and counts four/two. Both resolve through ncbi_id; no name-only fallback or strain/species
    substitution is needed.
  - Record crosswalk SHA 761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    and the exact lookup route. Label July 25 mtime as local file metadata, not a
    verified release named latest or build date. is_reclassified remains the helper’s
    name-comparison flag.
  - Keep CGA009/BAA-98 and 743B/DSM 3052/ATCC 35296 identity support separate from
    stock purchase and culture conditions. Do not substitute CGA001 or import the
    prior 174 protocol.
- action_id: verify-future-curation
  description: Validate separately authorized repairs and retain source limits.
  finding_ids:
  - bound-functional-roles
  - separate-feed-and-products
  - qualify-hydrogen-and-mechanism
  - link-declared-transcriptome
  - document-gtdb-snapshot
  target_ids:
  - CommunityMech:000264
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulovorans_Rhodopseudomonas_Cellulose_Biohydrogen_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Attach exact source-local evidence to changed fields. Preserve all existing graph
    bounds, ordinal semantics and declared source versions; complete the 2015 body
    and claim-relevant SI assessment before claiming a full scientific review.
  - Any authorized cache enrichment must preserve the three present caches and avoid
    treating supplement text as article text. This review leaves canonical records,
    caches, history and generated output unchanged. Coordinate current 1333 follow-up
    without closing other records.
  - After separately authorized canonical repair, append required history, run focused
    schema/strict/terms/reference/GTDB/domain/history checks, and regenerate/check
    derived output. Parent may persist only this review bundle after independent candidate
    acceptance.
limitations:
- Whole 2016 reader text, all three tables, five captions and 70 references were read.
  Only Figure 1 pixels were viewed. Figures 2–5 and SI PDF/workbooks were not recovered;
  their captions/references do not certify the images or internal data.
- The 2015 physiology paper is bibliographically verified but its main body and concentration-series/recipe
  details remain unavailable. Reprinted 3 g/L physiology in the 2016 text does not
  replace full original-paper assessment. Overall scientific completion remains partial/false.
- Failed EPMC/PMC/publisher responses are preserved with actual signatures; HTTP 200
  captcha/error bodies are not PDFs, spreadsheets or ZIPs. Corrected asset metadata
  supersedes a Table S1/Figure S3 labeling error without altering frozen original
  receipts or grades.
- The 20 field excerpt occurrences have 18 strict fresh matches and two explicit H2-spacing
  projections; all match selected caches. None of the small caches is a verified full
  article. Literal matching does not establish mechanism or role entailment.
- No raw RNA-seq reanalysis, image digitization, flux calculation, genome reclassification
  or biological experiment was performed. Archive top-level organism labels conflict
  with specific sample attributes and are not promoted to biological conclusions.
- Optional adapter availability is fresh batch 12 runtime scope with explicitly reused
  batch 11 discovery. Initial validator/support and all source corrections remain
  immutable. No canonical change, external message, paid access or save by lead.
notes:
- Three major/two minor findings; completeness 85; raw/capped quality 97.6666666667.
- Whole-record coverage describes target selection, not complete source access; scientific_review
  remains false.
- Coordinate existing shared 1333; retain closed graph repair 1330 and all current
  qualified graph boundaries.
tags:
- record-review
- cellulose
- biohydrogen
- batch-12
```
