# Cellulose-to-methane quad-culture review

- Review: 20261021T171211Z-cellulose-methane-quad-culture-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T17:05:03.264919Z
- Finished UTC: 2026-10-21T17:12:11.313294Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The source supports the defined four-member culture and six qualified nodes/five arrows. Four minor findings address cultivation context, non-graph evidence scope, computational provenance and missing data/code resources. All eight focused checks pass; all 25 excerpts match fresh reference-specific sources. Critical SI is inspected with explicit limits on the large protein table.

## Scope And Provenance

Whole record and every node/arrow assessed against scientific main, all main/SI figures, complete Tables S1–S3, bounded S4 rows and static source-code/data inspection.

Selection: Only released CommunityMech:000089 in owned batch 10.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 95812d3412d5aab41fd03422340cf736ac7b56f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000089 | kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml | maintained | Cellulose-to-Methane Quad-Culture SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000089 | Schema passed. |
| validate-strict | passed | True | CommunityMech:000089 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000089 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000089 | GTDB validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000089 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000089 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000089 | Read-only cache naming passed. |
| validate-references-explained | passed | True | CommunityMech:000089 | Reference validation passed; independent fresh matching verifies all 25 excerpts with abstract, IMPORTANCE and body distinctions. |
| audit-network | failed | True | CommunityMech:000089 | Fresh batch 10 corpus diagnostics retain their nonzero exit and warnings; the focal graph separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000089 | Fresh batch 10 corpus diagnostics retain their nonzero exit and warnings; the focal graph separately reports COMPLETE. |
| Whole-record scientific review | passed | True | CommunityMech:000089 | Scientific main, all five main figures, both SI figures and complete Tables S1–S3 assessed; S4 protein payload read only at declared bounded scope. |
| Fresh source excerpt verification | passed | True | CommunityMech:000089 | All 25 fresh matches: nine main abstract, five PubMed/EPMC IMPORTANCE and eleven body; all 25 also match cache. XML alone matches 20. |
| Data, code and strain identity | passed | True | CommunityMech:000089 | Source-linked archive and immutable repository identities verified; source strains and valid current parents checked. |
| Critical supplementary source review | passed | True | CommunityMech:000089 | All six scientific supplementary assets obtained. S1–S3 tables and both figures fully read/viewed; S4 has explicitly bounded protein-row reading and no reanalysis. |
| Model or raw-data reproduction | skipped | False | CommunityMech:000089 | No MATLAB execution, model fitting, raw proteomics, new significance test or parameter estimation. |
| Optional structured adapter | unavailable | False | CommunityMech:000089 | Fresh bounded batch 10 task-runtime discovery; known executable in another checkout not run. No biological absence inference. |

## Scientific And Domain Assessments

### Four-member synthetic community and comparison panel

identity: supported. Targets: CommunityMech:000089.

Retain the defined quad-culture, its four members and source-specific subset comparisons.

The main Table 1 has thirteen conditions, including a sulfate-treated Rc/Mh/Mc comparison without Dv. Exact H10, Hildenborough, JF-1 and GP6 information can enrich the record without changing valid parent-species identities. No host or natural community membership is inferred.

### State, origin, category and environment

scope: supported. Targets: CommunityMech:000089.

ENGINEERED, SYNTHETIC and METHANOGENESIS fit this laboratory assembly.

The laboratory-environment term is correct; the source vessel is a serum bottle, not a reason to invent continuous bioreactor operation. No equilibrium or abundance claim is required. Functional guild roles are supported at their source level, without obligacy or reciprocal-fitness inflation.

### Current names and optional finer strain grounding

identity: supported. Targets: CommunityMech:000089.

Encoded NCBI concepts and exact GTDB mappings are compatible with source identities.

Historical Methanosaeta and Desulfovibrio names remain source aliases. Optional strain refinement must carry its own crosswalk provenance; current species parents are not wrong IDs. Exact strains can first be recorded in strain_designation without forcing term substitutions.

### Daily medium replacement and gas handling

scope: concern. Targets: CommunityMech:000089.

Replace closed BATCH with the reported draw-and-fill mode and recover protocol context.

Daily replenishment, pH adjustment and venting matter for interpretation of seven-day accumulated products. Chamber gas is not proof of a fixed bottle headspace throughout growth. Distinguish preparation, revival and storage from focal conditions, and record sulfate timing ambiguity without guessing.

### Measured versus fitted endpoints and condition placement

scope: concern. Targets: CommunityMech:000089.

Keep assembly design separate from environmental factors and distinguish measured outcomes from fitted cross-feeding.

Sulfate consumption supports inferred H2S. Cross-feeding fluxes are model endpoints, not direct tracer measurements. Label-free proteomics and inferred pathway changes should not be rewritten as the later paper’s workflow.

### Cellulose Cross-Feeding to Methane

evidence: supported. Targets: CommunityMech:000089.

Retain community-level cellulose conversion and distinct methane/cellulose synergy responses.

Community output changes do not prove reciprocal organism fitness or each organism-resolved transfer. Preserve these qualifications and membership context.

### Rc acetate cross-feeding to Mc

evidence: supported. Targets: CommunityMech:000089.

Retain directed acetate utilization and qualify sulfate-enhanced contribution as fitted.

Culture contrasts and acetoclastic markers support the route; increased handoff under sulfate is inferred. Downstream contribution to methane is a supported route, not proof of unique mediation or all carbon arriving by this path.

### Rc lactate cross-feeding to Dv

evidence: supported. Targets: CommunityMech:000089.

Retain the explicitly partial lactate or alternative-intermediate hypothesis.

The source admits lactate/H2 exchange is poorly constrained and alternative organic donors remain possible. Preserve the hypothesized downstream supply connection to Dv-derived hydrogen rather than assert a uniquely identified lactate-to-H2 chain.

### Proposed Dv H2 syntrophy to Mh

evidence: supported. Targets: CommunityMech:000089.

Retain conditional proposed hydrogen provision under limited sulfate.

No demonstrated obligate dependence is inferred. Under sulfate, Dv can instead consume H2. The downstream connection to methane remains HYPOTHESIZED because Dv-specific contribution and donor substrate are not uniquely resolved.

### Mh H2 removal and Rc product inhibition

evidence: supported. Targets: CommunityMech:000089.

Retain partial stoichiometric feedback inference.

The calculation uses methane stoichiometry and accumulated H2, not an imposed-pressure intervention. No acetate-specific downstream edge is warranted; preserve its previous removal.

### Dv–Mh hydrogen competition

evidence: supported. Targets: CommunityMech:000089.

Retain the partial sulfate-associated competition interpretation.

The two suppressive downstream connections remain qualified. Fitted zero hydrogenotrophic flux is not measured cessation; persistent Mh protein and alternative electron donors/transfer routes remain in scope. Competition is not a directly measured reciprocal-fitness result.

### All five directed causal connections

evidence: supported. Targets: CommunityMech:000089.

Retain the existing five arrows with their current strengths and mechanisms.

Acetate-route→community methane is supported at route level; lactate-handoff→Dv H2 and Dv H2→methane are hypothesized; competition→proposed H2 supply is hypothesized and competition→methane is partial. No new arrow or restored acetate-feedback edge is needed.

### Non-graph handoff and electron-flow wording

evidence: concern. Targets: CommunityMech:000089.

Bring ingredient relevance/explanations to the same measured-versus-fitted scope already present in the graph.

Acetate utilization is supported, but sulfate-strengthened transfers and electron redistribution are inferred from fits. Methane is directly measured, sulfide estimated from sulfate loss. Exact source quotations should remain unchanged while explanations identify their scope.

### Actual stoichiometric model and alternatives

provenance: concern. Targets: CommunityMech:000089.

Add structured provenance for the seven-reaction model and its alternative fits.

Separate glucose-equivalent model input from wet-culture cellulose, and GC CO2 measurements from the six-row fit. Do not add a genome-scale FBA objective, SMETANA or ATP/protein-rate assumptions. Equal-goodness language conflicts with displayed S2 errors; preserve uncertainty rather than certify uniqueness.

### Source-linked data and code

provenance: concern. Targets: CommunityMech:000089.

Add the verified focal proteomics deposit and versioned model repository.

Metadata and file inventory are verified; raw proteomics was not analyzed. Preserve Fusion Tribrid versus LTQ Orbitrap Elite attribution. Dataset file counts are not biological replicate counts; source triplicates derive from the actual experimental description.

### Native checks and write boundaries

schema: supported. Targets: CommunityMech:000089.

All eight focused checks pass; scientific follow-ups remain despite valid syntax.

Only a new immutable review bundle may be saved. No canonical, cache, history or generated artifact changes occur. Corpus warnings and source-specific scientific assessments remain separately reported.

### Native scoring

completeness: supported. Targets: CommunityMech:000089.

Mechanical scores do not replace evidence review.

## Findings

### cultivation-context: Recover actual draw-and-fill and source strain context

minor / open / confirmed; issue key: cm-000089-cultivation-context.

Closed BATCH and fixed headspace wording overcompress daily replacement/venting and chamber gas. Exact strain/preparation and sulfate-control details are recoverable.

### outcome-evidence: Scope non-graph endpoints and ingredient explanations

minor / open / confirmed; issue key: cm-000089-outcome-evidence.

The graph distinguishes fitted pathways from measured outcomes more carefully than design endpoints and ingredient explanations. Assembly design is duplicated as an environmental condition.

### model-provenance: Add structured provenance for the actual seven-reaction fit

minor / open / confirmed; issue key: cm-000089-model-provenance.

Computational evidence lacks the structured input/method/alternative-solution provenance supplied by this source and its model artifacts.

### resources: Link verified focal proteomics and code resources

minor / open / confirmed; issue key: cm-000089-resources.

The record omits the source-linked PXD035759 dataset and Community_stoichiometric_model repository.

## Recommended Actions And Acceptance Checks

### recover-cultivation

Correct mode and add exact preparation/control context.

- Set cultivation_setup[0].cultivation_mode to SEMI_CONTINUOUS for daily 2 mL withdrawal and 2 mL replacement with fresh VM containing 10 g/L cellulose. Remove closed-batch claims from notes/explanations. Preserve 160 mL vessel capacity, 20 mL working volume, 34 °C, 200 rpm and seven-day assay; do not infer continuous flow or a steady state.
- Record pH adjustment to 7.3 after sampling and venting to atmospheric pressure. Describe 3% H2/97% N2 as the reported chamber atmosphere, not a maintained measured bottle-headspace composition. Keep evolving gas pools and pressure measurements separate from the environmental supply.
- Record sulfate treatment as 2 mL of 100 mM K2SO4 stock daily with equal sterile-water controls; preserve the Methods from-first-day versus Results after-first-day conflict. Do not infer final sulfate concentration or silently resolve addition-volume accounting. State no-added-sulfate control with the source-reported trace sulfate from FeSO4·6H2O, not chemically sulfate-free.
- Recover H10/ATCC 35319, Hildenborough/ATCC 29579, JF-1 and GP6 in strain_designation or source notes. Valid parent NCBI IDs may remain. If adopting finer strain IDs, rerun exact-ID GTDB grounding and preserve their distinct denominators/provenance rather than copying the current species block.
- Separate revival and focal conditions: Rc modified VM plus 2 g/L yeast extract and Dv LS4D at 34 °C; methanogen RST/H2:CO2 80:20/50 mM acetate at 37 °C; Mc approximately five-week revival; active OD600 0.5 transfer and about 5 × 10^7 cells per species. Do not carry revival yeast extract, acetate or temperature into the experimental cellulose medium or infer a complete VM recipe without its source.

### scope-outcomes

Align design and ingredient wording with the established graph boundaries.

- Distinguish measured cellulose/acid/gas outcomes, sulfate consumption and relative protein abundance from fitted cross-feeding fluxes in engineering_design. H2S is estimated from sulfate consumption; do not call it a directly measured gas endpoint. Label-free ProRata/Sipros methods belong to this source, not TMT or the later paper’s model workflow.
- Move or consolidate environmental_factors[0] synthetic assembly content into engineering_design. Use actual chemical/physical context for environmental factors and preserve correct ENVO laboratory scope. Do not manufacture conditions to improve completeness.
- Keep acetate utilization and its methane-route contribution, but identify sulfate-strengthened handoffs and electron redistribution in related_ingredients as source interpretations from stoichiometric modeling. Preserve exact source excerpts; add or relabel narrow computational evidence where its explanation goes beyond observed pools.
- Retain all six nodes and five qualified arrows. Lactate-to-H2 handoff and Dv-derived H2 contribution remain hypotheses; product-inhibition relief remains a stoichiometric inference without an acetate-feedback edge. Fitted zero Mh flux is not eradication or direct pathway cessation. Neither positive methane synergy nor negative cellulose synergy establishes reciprocal organism fitness.
- Preserve the source’s thirteen condition columns, including sulfate-treated Rc/Mh/Mc without Dv, and keep quad-culture metaproteomics separate from subset metabolite comparisons. Do not generalize a route to a composition lacking the relevant methanogen.

### record-model-provenance

Represent the focal stoichiometric method, inputs and uncertainty.

- Populate computational_provenance for modeled evidence with the seven overall reactions: Rc lactate fermentation and hydrogenic acetogenesis; Dv hydrogenic lactate oxidation, sulfidogenic lactate oxidation and sulfidogenic hydrogen oxidation; Mh hydrogenotrophic and Mc acetoclastic methanogenesis. Distinguish glucose-equivalent model input from supplied cellulose and note omitted extracellular hydrolysis and low ethanol branch.
- Identify daily measured/inferred fitting inputs and the reaction-exclusion/nonnegative least-squares procedure. The supplied matrix fits glucose equivalents, acetate, lactate, H2, CH4 and sulfide; CO2 gas was measured but omitted from fitting because buffering/pH affect partitioning. Do not import SMETANA, CarveMe, a genome-scale objective or protein/ATP-rate weights.
- Record alternative fitted solutions and their limits. Preserve the source’s equal-goodness claim as attributed language while noting Table S2’s differing displayed errors; do not silently repair numbers or certify unique flux. Protein evidence and fitted flux can disagree, and selected S3/S4 marker values must not be harmonized without analysis.
- Pin code and small data to commit d8605d066e782ae5fec5c4fd985b5731684a0834 with exact artifact paths. State that this review read the script and CSVs statically only. No MATLAB import behavior, executable reproduction, fresh significance test or raw proteomics reanalysis is certified.

### link-resources

Add precise focal dataset and repository links.

- Add PRIDE PXD035759 using direct source Data availability and verified project identity. Preserve its proteomics scope and 145-entry inventory distinction: 48 RAW, 48 PEAK, 48 RESULT and one design file. File counts do not define biological replication; triplicates are supported by the experiment description.
- Add the author Community_stoichiometric_model repository and immutable commit d8605d066e782ae5fec5c4fd985b5731684a0834. Distinguish README/tree metadata from the three small script/data payloads inspected by lead and raw proteomics not analyzed. Do not substitute the later paper’s PXD or repository.
- Preserve the manuscript/protocol Orbitrap Fusion Tribrid versus structured PRIDE LTQ Orbitrap Elite discrepancy with attribution, rather than silently correcting either. Keep the exact focal publication reference alongside reusable resource links.

### validate-authorized-curation

Perform canonical remediation only in a separately authorized curation task.

- Append fresh curation history and run focused schema, strict, term, reference, GTDB/domain and history checks after authorized changes; then run just gen-html and just check-docs-current. No canonical, cache, history or generated artifact is changed by this review.
- Verify new snippets against exact source sections and maintain independent primary versus supplementary-source provenance. Preserve all prior frozen artifacts and issue ownership; do not create or close issues here. Review persistence is limited to a new immutable review bundle, not a native scientific-status transition.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml; Entire maintained YAML: four taxa, six nodes, five arrows and both discussions | supports | The focal object is the 2023 four-member cellulose-to-methane culture and its sulfate comparison, informed by subset cultures. The current graph carefully qualifies alternative transfers, inferred product inhibition and zero modeled flux; historical repairs are retained. |
| identity | PMID:36847519; MATERIALS AND METHODS: Strains.; RESULTS: Overview of the experimental design.; Figure 1A; Table 1 | supports | The source specifies Rc H10/ATCC 35319, Dv Hildenborough/ATCC 29579, Mh JF1/taxid 323259 and Mc/taxid 990316. Eight Rc-centered compositions and sulfate arms yield thirteen Table 1 conditions, including a sulfate-treated Rc/Mh/Mc culture without Dv. The quad-culture is the focal metaproteomic comparison; not every assay is four-member only. |
| culture | PMID:36847519; MATERIALS AND METHODS: Cultures, growth conditions, and experimental design. | supports | Experiments use 160 mL serum bottles with 20 mL modified VM and 10 g/L cellulose, 34 °C, 200 rpm and seven days. Daily withdrawal of 2 mL culture is followed by 2 mL fresh cellulose medium, pH adjustment to 7.3 and venting to atmospheric pressure. This contradicts closed BATCH and matches periodic draw-and-fill. The 3% H2/97% N2 value is explicitly chamber gas. |
| preparation | PMID:36847519; MATERIALS AND METHODS: Strains.; Cultures, growth conditions, and experimental design. | supports | Rc revival uses modified VM plus 2 g/L yeast extract; Dv uses LS4D, both at 34 °C. Methanogens use RST, H2/CO2 80:20 and 50 mM acetate at 37 °C; Mc takes about five weeks before noticeable growth. Active OD600 0.5 inocula transfer to experimental VM, with flow-cytometry-based inoculation of about 5 × 10^7 cells per species. These stages are distinct from focal growth and storage. |
| sulfate | PMID:36847519; MATERIALS AND METHODS: Cultures, growth conditions, and experimental design.; RESULTS: Overview of the experimental design.; Table 1 | supports | Sulfate arms receive 2 mL of 100 mM K2SO4 stock daily and controls equal sterile water. Methods says from the first day, whereas Results says after the first day. The source reports approximately 0.14 µmol background sulfate from 1.25 mg/L FeSO4·6H2O in modified VM. Preserve no-added-sulfate rather than sulfate-free control; stock concentration is not a universal final concentration. |
| measurements | PMID:36847519; MATERIALS AND METHODS: Chemical analysis.; Protein identification and quantification.; Statistical analysis. | supports | Daily pressure and GC determine gas pools; HPLC measures soluble sugars and acids. H2S production is estimated from sulfate consumption, not directly measured as gas. Quad-culture proteins are analyzed by label-free ProRata quantification following Sipros Ensemble identification against four genomes at 1% peptide FDR. Source Methods names Orbitrap Fusion Tribrid. Normalized protein fractions and peak heights are not cell abundance or enzyme flux. |
| community-output | PMID:36847519; RESULTS: Overview of the experimental design.; Metabolism of cellulolytic bacterium Ruminiclostridium cellulolyticum.; Metabolism of the sulfate-reducing bacterium Desulfovibrio vulgaris.; DISCUSSION; Figures 1–4; Table 1 | supports | Cellulose conversion and methane outputs vary across defined member additions. Methane shows positive and cellulose degradation negative higher-order synergy relative to specified additive comparisons. These community phenotypes do not establish reciprocal organism fitness. The main proteome fractions are Rc 68% to 59%, Dv 19% to 28%, with Mc 10% and Mh 3% under both conditions; they are relative protein contributions. |
| acetate-feedback | PMID:36847519; RESULTS: Metabolism of hydrogenotrophic methanogen Methanospirillum hungatei and acetoclastic methanogen Methanosaeta concilii.; Figures 3 and 5 | supports | Acetate trajectories, methane outcomes and methanogen markers support the Rc-to-Mc route. The sulfate-associated increase in its contribution comes from fitted fluxes. Rc/Mh H2 production is inferred from stoichiometry and net accumulation, supporting proposed product-inhibition relief without a direct pressure intervention or acetate-specific mediator. |
| dv-hydrogen | PMID:36847519; RESULTS: Metabolism of the sulfate-reducing bacterium Desulfovibrio vulgaris.; DISCUSSION; Figure 4 | supports | The authors propose Rc-derived lactate or another oxidizable intermediate as Dv substrate and possible Dv-derived H2 supply to Mh. Discussion says lactate-to-H2 oxidation is unfavorable at the studied pressures and allows pyruvate/alanine alternatives. Net gas and protein profiles do not uniquely resolve the donor substrate or hydrogen turnover. |
| model | PMID:36847519; RESULTS: Modeling of carbon and energy flow through the synthetic community.; MATERIALS AND METHODS: Construction of the stoichiometric model.; Figure 5 | supports | The seven overall reactions comprise two Rc, three Dv and one reaction per methanogen. Rc is modeled as glucose-consuming, omitting extracellular hydrolysis and a low ethanol branch. Nonnegative fits to daily metabolites are tested by excluding pathways, yielding alternative distributions. This is a simple stoichiometric fit without a genome-scale FBA objective; no CarveMe, SMETANA or protein/ATP-rate weighting from the later paper belongs here. |
| model-limits | PMID:36847519; DISCUSSION; Figure 5; RESULTS: Modeling of carbon and energy flow through the synthetic community. | supports | The source admits poorly constrained Dv exchange and alternate solutions. Zero fitted Mh hydrogenotrophic flux under sulfate is not measured shutdown: Mh retains a 3% protein fraction, and formate, timing or other electron transfer are discussed. Protein changes do not validate every flux direction, and methanogen protein/flux trends can differ. |
| resources-statement | PMID:36847519; MATERIALS AND METHODS: Data availability.; Construction of the stoichiometric model. | supports | The source names PRIDE PXD035759 and thepanlab/Community_stoichiometric_model. These exact focal resources are independently verified and distinct from the later study’s deposit and repository. |
| s1 | PMID:36847519 supplementary Table S1; mbio.03189-22-s0003.pdf, entire single-page control reaction matrix and two scenarios | supports | All reaction coefficients, measured data, fit columns and both control scenarios were read in text and pixels. Two different Rc/Dv reaction allocations have the same displayed error; this supports nonuniqueness, not measured directional flux. |
| s2 | PMID:36847519 supplementary Table S2; mbio.03189-22-s0004.pdf, entire sulfate matrix and three scenarios | supports | The whole layout was read. Three scenario rows retain zero modeled hydrogenotrophic methanogenesis and alternative Dv routes. Displayed fit errors 6.44, 2.93 and 4.38 differ despite main/README equal-goodness language. Preserve the discrepancy; do not certify equivalence or silently repair the table. |
| s3 | PMID:36847519 supplementary Table S3; mbio.03189-22-s0005.pdf, all seven reaction rows and marker columns | supports | Whole text/layout compares alternative fluxes with marker protein changes. The acetate methanogen modeled contribution increases while its marker decreases; these different evidence types cannot be treated as interchangeable. Selected marker statistics differ from other source displays and are not harmonized here. |
| s4 | PMID:36847519 supplementary Table S4; mbio.03189-22-s0006.pdf; initial header/first 30 protein rows, all 32 queried marker-name matches, final 10 rows | supports | The table contains 3,736 protein entries with triplicate control and sulfate peak-height columns, q values, fold changes and directional labels. The declared subset was read, not every entry. Protein identifiers are source annotations, not newly validated reusable gene assignments or direct flux observations. |
| figures | PMID:36847519; Main Figures 1–5 and supplementary Figures S1–S2, all viewed | supports | The main figures separate community phenotype/protein fractions from fitted networks. Supplementary figures show cellulose consumption and acetate accumulation across Rc-centered configurations. These figures do not identify a unique Dv donor substrate or independently validate every fitted edge. |
| code | thepanlab/Community_stoichiometric_model commit d8605d066e782ae5fec5c4fd985b5731684a0834; README.md; script&amp;data/Quad_model.m; matrix_1.csv; quad_dataset.csv | supports | All three small script/data payloads and README were read statically. The supplied six-by-seven matrix fits glucose equivalents, acetate, lactate, H2, CH4 and sulfide. README excludes CO2 because buffer/pH affect partitioning. Two conditions, seven days and three replicates appear in the written workflow. No MATLAB execution, import test or numerical reproduction. |
| schema | src/communitymech/schema/communitymech.yaml; CultivationModeEnum; EvidenceItem.computational_provenance; FunctionalRoleEnum; InteractionTypeEnum | supports | SEMI_CONTINUOUS describes periodic partial harvest/replacement. Functional guild roles and interaction mechanisms have distinct scopes; SYNTROPHY does not imply obligacy. Structured computational provenance is available, and environmental conditions are distinct from experimental design. |
| ontology | ontology-authority.json; Whole frozen receipt and its declared scope | supports | All fifteen encoded ID-label pairs match across thirty-three occurrences. Correct labels do not establish experimental mechanisms. |
| semantics | ontology-semantic-notes.json; Whole frozen receipt and its declared scope | supports | Child independently checked source-specific culture wording, roles and model boundaries. The valid species parents need no forced strain replacement; no 2025 methods are imported. |
| strain-authority | child-strain-authority.json; Whole frozen receipt and its declared scope | supports | Exact source strains are recoverable. Direct catalogue identity views are explicitly reused from frozen batch 09 with original provenance; current source and local authorities are checked for this target. No catalogue cultivation conditions are transferred. |
| gtdb | child-gtdb-mapping-check.json; Whole frozen receipt and its declared scope | supports | Current exact-ID mappings match denominators 1/5/9/6 for Rc/Mh/Mc/Dv. Optional finer H10/GP6/Hildenborough concepts use distinct 2/85/7 denominators and require matched grounding. |
| resources | dataset-verification.json; Whole frozen receipt and its declared scope | supports | PXD035759 metadata and 145 unique inventory entries are verified: 48 RAW, 48 PEAK, 48 RESULT and one design entry. The source-linked repository has six tree entries at the pinned commit. Instrument metadata says LTQ Orbitrap Elite while protocol/manuscript says Fusion Tribrid; preserve attribution. No raw payloads were analyzed. |
| snippet-partition | snippet-source-partition.json; Whole frozen receipt and its declared scope | supports | Exact fresh-source partition: nine main abstract excerpts, five PubMed/EPMC IMPORTANCE excerpts and eleven body excerpts; no wording drift. |
| snippets | snippet-audit.json; Whole frozen receipt and its declared scope | supports | All 25 excerpts match fresh reference-specific source and cache: nine main abstract, five PubMed/EPMC IMPORTANCE and eleven body excerpts. Fresh XML alone supports twenty; IMPORTANCE omission is not wording drift. |
| history | provenance-audit.json; Whole frozen receipt and its declared scope | supports | The sole history and exact prior target decision were read. Preserve six qualified nodes/five arrows and the removed unsupported acetate-feedback arrow. Issue 1272 was freshly retrieved for batch 10; historical non-graph preservation is not certification. |
| metrics | support-audit.json; Whole frozen receipt and its declared scope | supports | Native COMPLETE graph has six nodes, five arrows and nine node-evidence entries. Completeness 80; four minor findings give raw 122, capped 100. |
| lead-read | lead-primary-read-scope.json; Whole frozen receipt and its declared scope | supports | Whole canonical, complete scientific cached main, all main/SI figures and complete S1–S3 assessed. S4 is bounded to declared rows, not all 3,736. Root independently read fresh main. Small code/data files read statically only. |
| source-scope | source-audit.json; Whole frozen receipt and its declared scope | supports | Frozen lead source assessment records four minor groups and source-specific scope limits. |
| root-source | root-independent-source-audit.json; Whole frozen receipt and its declared scope | supports | Root independently assessed the complete fresh main and declared figures/tables/SI scope, agreeing the four minor findings and retained graph. |
| auxiliary | auxiliary-frozen-manifest.json; Whole frozen receipt and its declared scope | supports | All eight focused native checks pass, fifteen term pairs match and all twenty-three official inputs remain unchanged. Child artifacts are immutable. |
| adapter | adapter-check.json; Whole frozen receipt and its declared scope | supports | Fresh bounded batch 10 adapter discovery found no task-runtime runner/module. A known other-checkout executable was not run; this is not evidence against the biology. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml; Actual execution 2026-10-21T17:05:50.143335+00:00 to 2026-10-21T17:05:50.924433+00:00 | supports | Schema passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-strict kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml --out /private/tmp/cm-review-session/batch-10/000089/strict-report.tsv; Actual execution 2026-10-21T17:05:50.143543+00:00 to 2026-10-21T17:05:52.303214+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-terms kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml; Actual execution 2026-10-21T17:05:50.143599+00:00 to 2026-10-21T17:05:51.839603+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-gtdb kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml; Actual execution 2026-10-21T17:05:50.924693+00:00 to 2026-10-21T17:05:51.016619+00:00 | supports | GTDB validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-gtdb-domain kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml; Actual execution 2026-10-21T17:05:51.016986+00:00 to 2026-10-21T17:05:52.363376+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-history history/records/Cellulose_Methane_Quad_Culture_SynCom; Actual execution 2026-10-21T17:05:51.839961+00:00 to 2026-10-21T17:05:52.608230+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T17:05:52.608828+00:00 to 2026-10-21T17:05:52.664685+00:00 | supports | Read-only cache naming passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src just --no-dotenv validate-references-explained kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml; Actual execution 2026-10-21T17:05:52.664929+00:00 to 2026-10-21T17:05:53.647043+00:00 | supports | Reference validation passed; independent fresh matching verifies all 25 excerpts with abstract, IMPORTANCE and body distinctions. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T17:04:17.819938+00:00 to 2026-10-21T17:04:25.370848+00:00 | supports | Fresh batch 10 corpus diagnostics retain their nonzero exit and warnings; the focal graph separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T17:04:17.819995+00:00 to 2026-10-21T17:04:26.163649+00:00 | supports | Fresh batch 10 corpus diagnostics retain their nonzero exit and warnings; the focal graph separately reports COMPLETE. |

## Limits And Additional Notes

- This review concerns PMID 36847519 (2023 mBio), not the later combinatorial modeling paper. No later-study model, TMT workflow or protocol is imported.
- Complete scientific main, all five main figures, two SI figures and complete Tables S1–S3 were assessed. Table S4 has 3,736 protein entries; only initial header/first 30 rows, all 32 marker-name matches and final 10 rows were read. No exhaustive per-protein or raw-data certification.
- Table 1 has thirteen conditions including a sulfate-treated Rc/Mh/Mc culture without Dv. Community output contrasts and quad-culture proteomics have different scopes. Relative proteome fractions are not cell counts or viability measurements.
- Daily culture replacement, pH adjustment and gas venting are source-reported. Chamber gas is not a demonstrated fixed bottle-headspace composition. Sulfate onset differs between Methods and Results, and stock concentration/addition volume is not a resolved final concentration or fluid balance.
- Control contains trace sulfate according to the source; no added sulfate is not sulfate-free. Revival yeast extract, acetate and temperatures are not automatically focal medium constituents. No complete modified VM recipe or exact recipe cross-link was established.
- The model fits six measured/inferred quantities, including glucose equivalents, with seven overall reactions. GC CO2 was observed but excluded from supplied fits due to buffer/pH partitioning. Neither model input nor a fitted zero is a direct organism-specific flux measurement.
- Alternative fluxes and source fit-quality claims do not establish unique mediation. Table S2 displayed errors differ from equal-goodness language; S3/S4/Figure 3 marker summaries differ. These source inconsistencies are preserved without numerical repair or an extra canonical finding.
- Lactate oxidation to hydrogen is unfavorable at studied pressures according to the source; alternative organic intermediates remain possible. Keep partial donor/recipient hypotheses and the absence of direct pressure intervention or acetate-specific feedback evidence.
- H2S is inferred from sulfate loss. Net gas accumulation does not separate gross production/consumption. Positive methane and negative cellulose synergies concern community outputs, not reciprocal organism fitness.
- Existing species parents are valid. Finer H10/GP6/Hildenborough concepts would require their own GTDB mappings. Historical catalogue names and current authority labels remain distinct; catalogue growth conditions are not imported.
- PRIDE metadata/inventory and source code identity were checked. Three small code/data files were read statically; no model execution, MATLAB import test or raw proteomics reanalysis. Manuscript/protocol Fusion Tribrid and structured archive LTQ Orbitrap Elite are unresolved attributed values.
- All 25 snippets match fresh reference-specific sources and cache: nine main abstract, five IMPORTANCE, eleven body. XML alone contains twenty matches; PubMed/EPMC supplies IMPORTANCE. Source matching is not causal proof.
- All 23 official inspected inputs remain unchanged. Focused native checks pass; corpus-wide diagnostics remain separately reported. Only a new immutable review bundle may subsequently be saved.
- All 23 fresh official inputs remain unchanged. No canonical, cache, history, generated product or prior review is edited.
- Root independently read the complete fresh main and its declared figure/SI scope. Lead read complete cached main and all figures/S1–S3, with bounded S4 and full small static-code/data reading. Auxiliary and supporting scopes remain exactly as declared in their receipts.
- Completeness 80 and quality 100/raw 122 are mechanical values, not proof of unique modeled exchanges. Do not add unsupported roles or fields for points.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T171211Z-cellulose-methane-quad-culture-record
kind: record
repository: CultureBotAI/CommunityMech
title: Cellulose-to-methane quad-culture review
started_at: '2026-10-21T17:05:03.264919Z'
finished_at: '2026-10-21T17:12:11.313294Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, auxiliary validation
    and provenance; no person-level independence is asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The source supports the defined four-member culture and six qualified nodes/five
  arrows. Four minor findings address cultivation context, non-graph evidence scope,
  computational provenance and missing data/code resources. All eight focused checks
  pass; all 25 excerpts match fresh reference-specific sources. Critical SI is inspected
  with explicit limits on the large protein table.
source:
  git_revision: 95812d3412d5aab41fd03422340cf736ac7b56f3
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
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
  - path: history/records/Cellulose_Methane_Quad_Culture_SynCom/2026-10-05T173108Z-codex-e5c53b.yaml
    sha256: eee2aafcd7cde29e60fdaf767f87fb2c84f96df6a3d6c33f97201b0667f9f0fa
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    sha256: f6daf89ddcb52d344ccb2169c618bde2b7334e706c1143a2262bf95d54d9f645
    role: target
  - path: references_cache/PMID_36847519.txt
    sha256: 43968d3cc3801f1454458bad7e2b535aa97ced19763a724103e6ceb5ce0da448
    role: context
  - path: reports/causal_graph_review/decisions/20261005-ten-records-batch10.yaml
    sha256: 7149a6a81f091ff27d40deaf5bf99cb0a9b6486344db20009517f48652fe855d
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
- target_id: CommunityMech:000089
  path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  label: Cellulose-to-Methane Quad-Culture SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    role: canonical_record
scope:
  description: Whole record and every node/arrow assessed against scientific main,
    all main/SI figures, complete Tables S1–S3, bounded S4 rows and static source-code/data
    inspection.
  selection: Only released CommunityMech:000089 in owned batch 10.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000089
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema passed.
  target_ids:
  - CommunityMech:000089
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused execution in owned batch 10. Scientific support is assessed
    separately.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000089
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-strict kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-10/000089/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused execution in owned batch 10. Scientific support is assessed
    separately.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000089
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-terms kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused execution in owned batch 10. Scientific support is assessed
    separately.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB validation passed.
  target_ids:
  - CommunityMech:000089
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused execution in owned batch 10. Scientific support is assessed
    separately.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000089
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb-domain kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused execution in owned batch 10. Scientific support is assessed
    separately.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000089
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-history history/records/Cellulose_Methane_Quad_Culture_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused execution in owned batch 10. Scientific support is assessed
    separately.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache naming passed.
  target_ids:
  - CommunityMech:000089
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused execution in owned batch 10. Scientific support is assessed
    separately.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed; independent fresh matching verifies all 25
    excerpts with abstract, IMPORTANCE and body distinctions.
  target_ids:
  - CommunityMech:000089
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-references-explained kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused execution in owned batch 10. Scientific support is assessed
    separately.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 10 corpus diagnostics retain their nonzero exit and warnings;
    the focal graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000089
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - metrics
  scope_note: Explicit same-batch corpus reuse; unrelated warnings are not assigned
    to this target.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 10 corpus diagnostics retain their nonzero exit and warnings;
    the focal graph separately reports COMPLETE.
  target_ids:
  - CommunityMech:000089
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - metrics
  scope_note: Explicit same-batch corpus reuse; unrelated warnings are not assigned
    to this target.
- check_id: scientific-source
  name: Whole-record scientific review
  status: passed
  required: true
  summary: Scientific main, all five main figures, both SI figures and complete Tables
    S1–S3 assessed; S4 protein payload read only at declared bounded scope.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - lead-read
  - root-source
  - source-scope
- check_id: direct-snippets
  name: Fresh source excerpt verification
  status: passed
  required: true
  summary: 'All 25 fresh matches: nine main abstract, five PubMed/EPMC IMPORTANCE
    and eleven body; all 25 also match cache. XML alone matches 20.'
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - snippets
- check_id: resource-identity
  name: Data, code and strain identity
  status: passed
  required: true
  summary: Source-linked archive and immutable repository identities verified; source
    strains and valid current parents checked.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - resources
  - strain-authority
- check_id: supplements
  name: Critical supplementary source review
  status: passed
  required: true
  summary: All six scientific supplementary assets obtained. S1–S3 tables and both
    figures fully read/viewed; S4 has explicitly bounded protein-row reading and no
    reanalysis.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - s1
  - s2
  - s3
  - s4
  - figures
- check_id: reproduction
  name: Model or raw-data reproduction
  status: skipped
  required: false
  summary: No MATLAB execution, model fitting, raw proteomics, new significance test
    or parameter estimation.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - code
  - lead-read
- check_id: adapter
  name: Optional structured adapter
  status: unavailable
  required: false
  summary: Fresh bounded batch 10 task-runtime discovery; known executable in another
    checkout not run. No biological absence inference.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  locator: 'Entire maintained YAML: four taxa, six nodes, five arrows and both discussions'
  summary: The focal object is the 2023 four-member cellulose-to-methane culture and
    its sulfate comparison, informed by subset cultures. The current graph carefully
    qualifies alternative transfers, inferred product inhibition and zero modeled
    flux; historical repairs are retained.
  support: supports
  accessed_at: '2026-10-21T17:12:11.302760Z'
- evidence_id: identity
  kind: primary_source
  reference: PMID:36847519
  locator: 'MATERIALS AND METHODS: Strains.; RESULTS: Overview of the experimental
    design.; Figure 1A; Table 1'
  summary: The source specifies Rc H10/ATCC 35319, Dv Hildenborough/ATCC 29579, Mh
    JF1/taxid 323259 and Mc/taxid 990316. Eight Rc-centered compositions and sulfate
    arms yield thirteen Table 1 conditions, including a sulfate-treated Rc/Mh/Mc culture
    without Dv. The quad-culture is the focal metaproteomic comparison; not every
    assay is four-member only.
  support: supports
  accessed_at: '2026-10-21T17:12:11.302833Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
- evidence_id: culture
  kind: primary_source
  reference: PMID:36847519
  locator: 'MATERIALS AND METHODS: Cultures, growth conditions, and experimental design.'
  summary: Experiments use 160 mL serum bottles with 20 mL modified VM and 10 g/L
    cellulose, 34 °C, 200 rpm and seven days. Daily withdrawal of 2 mL culture is
    followed by 2 mL fresh cellulose medium, pH adjustment to 7.3 and venting to atmospheric
    pressure. This contradicts closed BATCH and matches periodic draw-and-fill. The
    3% H2/97% N2 value is explicitly chamber gas.
  support: supports
  accessed_at: '2026-10-21T17:12:11.303079Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
  quote: pH was adjusted to 7.3
- evidence_id: preparation
  kind: primary_source
  reference: PMID:36847519
  locator: 'MATERIALS AND METHODS: Strains.; Cultures, growth conditions, and experimental
    design.'
  summary: Rc revival uses modified VM plus 2 g/L yeast extract; Dv uses LS4D, both
    at 34 °C. Methanogens use RST, H2/CO2 80:20 and 50 mM acetate at 37 °C; Mc takes
    about five weeks before noticeable growth. Active OD600 0.5 inocula transfer to
    experimental VM, with flow-cytometry-based inoculation of about 5 × 10^7 cells
    per species. These stages are distinct from focal growth and storage.
  support: supports
  accessed_at: '2026-10-21T17:12:11.303159Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
- evidence_id: sulfate
  kind: primary_source
  reference: PMID:36847519
  locator: 'MATERIALS AND METHODS: Cultures, growth conditions, and experimental design.;
    RESULTS: Overview of the experimental design.; Table 1'
  summary: Sulfate arms receive 2 mL of 100 mM K2SO4 stock daily and controls equal
    sterile water. Methods says from the first day, whereas Results says after the
    first day. The source reports approximately 0.14 µmol background sulfate from
    1.25 mg/L FeSO4·6H2O in modified VM. Preserve no-added-sulfate rather than sulfate-free
    control; stock concentration is not a universal final concentration.
  support: supports
  accessed_at: '2026-10-21T17:12:11.303236Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
- evidence_id: measurements
  kind: primary_source
  reference: PMID:36847519
  locator: 'MATERIALS AND METHODS: Chemical analysis.; Protein identification and
    quantification.; Statistical analysis.'
  summary: Daily pressure and GC determine gas pools; HPLC measures soluble sugars
    and acids. H2S production is estimated from sulfate consumption, not directly
    measured as gas. Quad-culture proteins are analyzed by label-free ProRata quantification
    following Sipros Ensemble identification against four genomes at 1% peptide FDR.
    Source Methods names Orbitrap Fusion Tribrid. Normalized protein fractions and
    peak heights are not cell abundance or enzyme flux.
  support: supports
  accessed_at: '2026-10-21T17:12:11.303313Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
- evidence_id: community-output
  kind: primary_source
  reference: PMID:36847519
  locator: 'RESULTS: Overview of the experimental design.; Metabolism of cellulolytic
    bacterium Ruminiclostridium cellulolyticum.; Metabolism of the sulfate-reducing
    bacterium Desulfovibrio vulgaris.; DISCUSSION; Figures 1–4; Table 1'
  summary: Cellulose conversion and methane outputs vary across defined member additions.
    Methane shows positive and cellulose degradation negative higher-order synergy
    relative to specified additive comparisons. These community phenotypes do not
    establish reciprocal organism fitness. The main proteome fractions are Rc 68%
    to 59%, Dv 19% to 28%, with Mc 10% and Mh 3% under both conditions; they are relative
    protein contributions.
  support: supports
  accessed_at: '2026-10-21T17:12:11.303389Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
- evidence_id: acetate-feedback
  kind: primary_source
  reference: PMID:36847519
  locator: 'RESULTS: Metabolism of hydrogenotrophic methanogen Methanospirillum hungatei
    and acetoclastic methanogen Methanosaeta concilii.; Figures 3 and 5'
  summary: Acetate trajectories, methane outcomes and methanogen markers support the
    Rc-to-Mc route. The sulfate-associated increase in its contribution comes from
    fitted fluxes. Rc/Mh H2 production is inferred from stoichiometry and net accumulation,
    supporting proposed product-inhibition relief without a direct pressure intervention
    or acetate-specific mediator.
  support: supports
  accessed_at: '2026-10-21T17:12:11.303466Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
- evidence_id: dv-hydrogen
  kind: primary_source
  reference: PMID:36847519
  locator: 'RESULTS: Metabolism of the sulfate-reducing bacterium Desulfovibrio vulgaris.;
    DISCUSSION; Figure 4'
  summary: The authors propose Rc-derived lactate or another oxidizable intermediate
    as Dv substrate and possible Dv-derived H2 supply to Mh. Discussion says lactate-to-H2
    oxidation is unfavorable at the studied pressures and allows pyruvate/alanine
    alternatives. Net gas and protein profiles do not uniquely resolve the donor substrate
    or hydrogen turnover.
  support: supports
  accessed_at: '2026-10-21T17:12:11.303542Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
- evidence_id: model
  kind: primary_source
  reference: PMID:36847519
  locator: 'RESULTS: Modeling of carbon and energy flow through the synthetic community.;
    MATERIALS AND METHODS: Construction of the stoichiometric model.; Figure 5'
  summary: The seven overall reactions comprise two Rc, three Dv and one reaction
    per methanogen. Rc is modeled as glucose-consuming, omitting extracellular hydrolysis
    and a low ethanol branch. Nonnegative fits to daily metabolites are tested by
    excluding pathways, yielding alternative distributions. This is a simple stoichiometric
    fit without a genome-scale FBA objective; no CarveMe, SMETANA or protein/ATP-rate
    weighting from the later paper belongs here.
  support: supports
  accessed_at: '2026-10-21T17:12:11.303617Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
- evidence_id: model-limits
  kind: primary_source
  reference: PMID:36847519
  locator: 'DISCUSSION; Figure 5; RESULTS: Modeling of carbon and energy flow through
    the synthetic community.'
  summary: 'The source admits poorly constrained Dv exchange and alternate solutions.
    Zero fitted Mh hydrogenotrophic flux under sulfate is not measured shutdown: Mh
    retains a 3% protein fraction, and formate, timing or other electron transfer
    are discussed. Protein changes do not validate every flux direction, and methanogen
    protein/flux trends can differ.'
  support: supports
  accessed_at: '2026-10-21T17:12:11.303691Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
- evidence_id: resources-statement
  kind: primary_source
  reference: PMID:36847519
  locator: 'MATERIALS AND METHODS: Data availability.; Construction of the stoichiometric
    model.'
  summary: The source names PRIDE PXD035759 and thepanlab/Community_stoichiometric_model.
    These exact focal resources are independently verified and distinct from the later
    study’s deposit and repository.
  support: supports
  accessed_at: '2026-10-21T17:12:11.303767Z'
  snapshot_sha256: 71de6814fc3b5100f2cbea30df5c4c2c7c34136e463d31f4c96e8ea03a8acb4d
- evidence_id: s1
  kind: primary_source
  reference: PMID:36847519 supplementary Table S1
  locator: mbio.03189-22-s0003.pdf, entire single-page control reaction matrix and
    two scenarios
  summary: All reaction coefficients, measured data, fit columns and both control
    scenarios were read in text and pixels. Two different Rc/Dv reaction allocations
    have the same displayed error; this supports nonuniqueness, not measured directional
    flux.
  support: supports
  accessed_at: '2026-10-21T17:12:11.303842Z'
  snapshot_sha256: 1fd529d21a6461158ac39ad67c7020e115aefa25fe176dd45db399f95b10924e
- evidence_id: s2
  kind: primary_source
  reference: PMID:36847519 supplementary Table S2
  locator: mbio.03189-22-s0004.pdf, entire sulfate matrix and three scenarios
  summary: The whole layout was read. Three scenario rows retain zero modeled hydrogenotrophic
    methanogenesis and alternative Dv routes. Displayed fit errors 6.44, 2.93 and
    4.38 differ despite main/README equal-goodness language. Preserve the discrepancy;
    do not certify equivalence or silently repair the table.
  support: supports
  accessed_at: '2026-10-21T17:12:11.304239Z'
  snapshot_sha256: da4aca91f96ae9e8cfbf64f73362d78158abae590fcb1cd22996754b1945ed88
- evidence_id: s3
  kind: primary_source
  reference: PMID:36847519 supplementary Table S3
  locator: mbio.03189-22-s0005.pdf, all seven reaction rows and marker columns
  summary: Whole text/layout compares alternative fluxes with marker protein changes.
    The acetate methanogen modeled contribution increases while its marker decreases;
    these different evidence types cannot be treated as interchangeable. Selected
    marker statistics differ from other source displays and are not harmonized here.
  support: supports
  accessed_at: '2026-10-21T17:12:11.304644Z'
  snapshot_sha256: 571bfef99e6cf7534af59b973c91d497d8b97ed7af11208befeaa5733abd54b9
- evidence_id: s4
  kind: primary_source
  reference: PMID:36847519 supplementary Table S4
  locator: mbio.03189-22-s0006.pdf; initial header/first 30 protein rows, all 32 queried
    marker-name matches, final 10 rows
  summary: The table contains 3,736 protein entries with triplicate control and sulfate
    peak-height columns, q values, fold changes and directional labels. The declared
    subset was read, not every entry. Protein identifiers are source annotations,
    not newly validated reusable gene assignments or direct flux observations.
  support: supports
  accessed_at: '2026-10-21T17:12:11.305041Z'
  snapshot_sha256: 7772ff7d0c3f32149207513cf045b35072e5d52cdc55d9ca4413fbed46b6bfe0
- evidence_id: figures
  kind: primary_source
  reference: PMID:36847519
  locator: Main Figures 1–5 and supplementary Figures S1–S2, all viewed
  summary: The main figures separate community phenotype/protein fractions from fitted
    networks. Supplementary figures show cellulose consumption and acetate accumulation
    across Rc-centered configurations. These figures do not identify a unique Dv donor
    substrate or independently validate every fitted edge.
  support: supports
  accessed_at: '2026-10-21T17:12:11.305259Z'
  snapshot_sha256: fac6d1946d5be56ba0bf30814b5463746965946e6021fc83fff449b5068e9dda
- evidence_id: code
  kind: primary_source
  reference: thepanlab/Community_stoichiometric_model commit d8605d066e782ae5fec5c4fd985b5731684a0834
  locator: README.md; script&data/Quad_model.m; matrix_1.csv; quad_dataset.csv
  summary: All three small script/data payloads and README were read statically. The
    supplied six-by-seven matrix fits glucose equivalents, acetate, lactate, H2, CH4
    and sulfide. README excludes CO2 because buffer/pH affect partitioning. Two conditions,
    seven days and three replicates appear in the written workflow. No MATLAB execution,
    import test or numerical reproduction.
  support: supports
  accessed_at: '2026-10-21T17:12:11.305404Z'
  snapshot_sha256: 1659601070029e2e52eb4f2f9b6420b74c515e7822a7085a965c363737549309
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: CultivationModeEnum; EvidenceItem.computational_provenance; FunctionalRoleEnum;
    InteractionTypeEnum
  summary: SEMI_CONTINUOUS describes periodic partial harvest/replacement. Functional
    guild roles and interaction mechanisms have distinct scopes; SYNTROPHY does not
    imply obligacy. Structured computational provenance is available, and environmental
    conditions are distinct from experimental design.
  support: supports
  accessed_at: '2026-10-21T17:12:11.305533Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole frozen receipt and its declared scope
  summary: All fifteen encoded ID-label pairs match across thirty-three occurrences.
    Correct labels do not establish experimental mechanisms.
  support: supports
  accessed_at: '2026-10-21T17:12:11.305630Z'
  snapshot_sha256: e3d06430b5ce0311355efff723bd3c73a9957527e461cc7f27b7b54070af7e30
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole frozen receipt and its declared scope
  summary: Child independently checked source-specific culture wording, roles and
    model boundaries. The valid species parents need no forced strain replacement;
    no 2025 methods are imported.
  support: supports
  accessed_at: '2026-10-21T17:12:11.305794Z'
  snapshot_sha256: 58ccad1e7ab73547adc0c5c59656fdc851213ed7e66a1fdaa8ff9cde569bb62b
- evidence_id: strain-authority
  kind: authority
  reference: child-strain-authority.json
  locator: Whole frozen receipt and its declared scope
  summary: Exact source strains are recoverable. Direct catalogue identity views are
    explicitly reused from frozen batch 09 with original provenance; current source
    and local authorities are checked for this target. No catalogue cultivation conditions
    are transferred.
  support: supports
  accessed_at: '2026-10-21T17:12:11.305910Z'
  snapshot_sha256: dfcd94d552c96883ec362eb5dbe220aaddcbd510169ce747fd62071d1c290f37
- evidence_id: gtdb
  kind: authority
  reference: child-gtdb-mapping-check.json
  locator: Whole frozen receipt and its declared scope
  summary: Current exact-ID mappings match denominators 1/5/9/6 for Rc/Mh/Mc/Dv. Optional
    finer H10/GP6/Hildenborough concepts use distinct 2/85/7 denominators and require
    matched grounding.
  support: supports
  accessed_at: '2026-10-21T17:12:11.306057Z'
  snapshot_sha256: 658b78d5637b7d7c7d133bc9e97ea54a346240e9afd64201653a0de30a5f07e5
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole frozen receipt and its declared scope
  summary: 'PXD035759 metadata and 145 unique inventory entries are verified: 48 RAW,
    48 PEAK, 48 RESULT and one design entry. The source-linked repository has six
    tree entries at the pinned commit. Instrument metadata says LTQ Orbitrap Elite
    while protocol/manuscript says Fusion Tribrid; preserve attribution. No raw payloads
    were analyzed.'
  support: supports
  accessed_at: '2026-10-21T17:12:11.306273Z'
  snapshot_sha256: 923bf49b93d9fed9f831a627abd430d0af98809ca0b332c18fb93987fdcf35bf
- evidence_id: snippet-partition
  kind: validation
  reference: snippet-source-partition.json
  locator: Whole frozen receipt and its declared scope
  summary: 'Exact fresh-source partition: nine main abstract excerpts, five PubMed/EPMC
    IMPORTANCE excerpts and eleven body excerpts; no wording drift.'
  support: supports
  accessed_at: '2026-10-21T17:12:11.306473Z'
  snapshot_sha256: 2f26300653ec9e04a97bfac3f03c930fa2bf2e4b1fc24a8d1a588979b8935f56
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole frozen receipt and its declared scope
  summary: 'All 25 excerpts match fresh reference-specific source and cache: nine
    main abstract, five PubMed/EPMC IMPORTANCE and eleven body excerpts. Fresh XML
    alone supports twenty; IMPORTANCE omission is not wording drift.'
  support: supports
  accessed_at: '2026-10-21T17:12:11.307684Z'
  snapshot_sha256: fed55f743683d5aabd47ae4dbeb7ed750f39be540e2a5cf2b3293ee09555c4ae
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole frozen receipt and its declared scope
  summary: The sole history and exact prior target decision were read. Preserve six
    qualified nodes/five arrows and the removed unsupported acetate-feedback arrow.
    Issue 1272 was freshly retrieved for batch 10; historical non-graph preservation
    is not certification.
  support: supports
  accessed_at: '2026-10-21T17:12:11.308893Z'
  snapshot_sha256: cbc90c1ce6bc98dd5aa90ace3731371d57e0870927a875ce86189c3450fa9f37
- evidence_id: metrics
  kind: validation
  reference: support-audit.json
  locator: Whole frozen receipt and its declared scope
  summary: Native COMPLETE graph has six nodes, five arrows and nine node-evidence
    entries. Completeness 80; four minor findings give raw 122, capped 100.
  support: supports
  accessed_at: '2026-10-21T17:12:11.309988Z'
  snapshot_sha256: bec4b4c8b0612fed3be0521d085bff15c792215f15ee12bd57af100d3e620ec8
- evidence_id: lead-read
  kind: validation
  reference: lead-primary-read-scope.json
  locator: Whole frozen receipt and its declared scope
  summary: Whole canonical, complete scientific cached main, all main/SI figures and
    complete S1–S3 assessed. S4 is bounded to declared rows, not all 3,736. Root independently
    read fresh main. Small code/data files read statically only.
  support: supports
  accessed_at: '2026-10-21T17:12:11.310034Z'
  snapshot_sha256: fac6d1946d5be56ba0bf30814b5463746965946e6021fc83fff449b5068e9dda
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole frozen receipt and its declared scope
  summary: Frozen lead source assessment records four minor groups and source-specific
    scope limits.
  support: supports
  accessed_at: '2026-10-21T17:12:11.310060Z'
  snapshot_sha256: 3aa6ce923dfebad2949fb89f7f2f09d3738c497cc63e08af57e9f1ea87133240
- evidence_id: root-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole frozen receipt and its declared scope
  summary: Root independently assessed the complete fresh main and declared figures/tables/SI
    scope, agreeing the four minor findings and retained graph.
  support: supports
  accessed_at: '2026-10-21T17:12:11.310970Z'
  snapshot_sha256: c1f278515a42ba439fcfd9010f702d3e64e5294a1c1ce77f7d676796c13b48b6
- evidence_id: auxiliary
  kind: validation
  reference: auxiliary-frozen-manifest.json
  locator: Whole frozen receipt and its declared scope
  summary: All eight focused native checks pass, fifteen term pairs match and all
    twenty-three official inputs remain unchanged. Child artifacts are immutable.
  support: supports
  accessed_at: '2026-10-21T17:12:11.311127Z'
  snapshot_sha256: d643d8fd1b7d0da29404dd7733aa70305c6b5f963f8554aff9658e5beac7edd8
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Whole frozen receipt and its declared scope
  summary: Fresh bounded batch 10 adapter discovery found no task-runtime runner/module.
    A known other-checkout executable was not run; this is not evidence against the
    biology.
  support: supports
  accessed_at: '2026-10-21T17:12:11.311271Z'
  snapshot_sha256: eef91dd62ff54edfe162d1928e0ce49962624eed1bfa3ba4618ba8dc1f462773
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  locator: Actual execution 2026-10-21T17:05:50.143335+00:00 to 2026-10-21T17:05:50.924433+00:00
  summary: Schema passed.
  support: supports
  accessed_at: '2026-10-21T17:05:50.924433Z'
  snapshot_sha256: 51e513f2c32de4f607b6fab1b8e28ea15f7d9721d8e97917611560d2e4e0dbe8
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-strict kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-10/000089/strict-report.tsv
  locator: Actual execution 2026-10-21T17:05:50.143543+00:00 to 2026-10-21T17:05:52.303214+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T17:05:52.303214Z'
  snapshot_sha256: 9ec68b04769f20bdb8bb1184f00962d5592022bdce19a99634eeebb3d2cb6305
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-terms kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  locator: Actual execution 2026-10-21T17:05:50.143599+00:00 to 2026-10-21T17:05:51.839603+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T17:05:51.839603Z'
  snapshot_sha256: b1ea687e00aa301489c436041509b985ad2ed1b8122f5c3171983452435dbb7d
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  locator: Actual execution 2026-10-21T17:05:50.924693+00:00 to 2026-10-21T17:05:51.016619+00:00
  summary: GTDB validation passed.
  support: supports
  accessed_at: '2026-10-21T17:05:51.016619Z'
  snapshot_sha256: 22103e59397d33ba88f24a43cb4523639f90b7bbc96038f5cf16dd1f9d8a9168
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-gtdb-domain kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  locator: Actual execution 2026-10-21T17:05:51.016986+00:00 to 2026-10-21T17:05:52.363376+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T17:05:52.363376Z'
  snapshot_sha256: 9da4a28efd5e08c069dde0c6cfe787fd55f2e82e4dd30168f323b6252cb4be72
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-history history/records/Cellulose_Methane_Quad_Culture_SynCom
  locator: Actual execution 2026-10-21T17:05:51.839961+00:00 to 2026-10-21T17:05:52.608230+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T17:05:52.608230Z'
  snapshot_sha256: c9caab684f69965d29cfd217e9d6a9bf6b12b5600485f869c9c826b7df054097
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T17:05:52.608828+00:00 to 2026-10-21T17:05:52.664685+00:00
  summary: Read-only cache naming passed.
  support: supports
  accessed_at: '2026-10-21T17:05:52.664685Z'
  snapshot_sha256: d9afc08b574fdde566c8e46a18a6f00d45cd052bc990fc7f86d140b885ea46e5
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src
    just --no-dotenv validate-references-explained kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
  locator: Actual execution 2026-10-21T17:05:52.664929+00:00 to 2026-10-21T17:05:53.647043+00:00
  summary: Reference validation passed; independent fresh matching verifies all 25
    excerpts with abstract, IMPORTANCE and body distinctions.
  support: supports
  accessed_at: '2026-10-21T17:05:53.647043Z'
  snapshot_sha256: 8206fe15783c062f77ec4e778b92e1eb8e12c7d3c3688d7e6dc825814c494147
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T17:04:17.819938+00:00 to 2026-10-21T17:04:25.370848+00:00
  summary: Fresh batch 10 corpus diagnostics retain their nonzero exit and warnings;
    the focal graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T17:04:25.370848Z'
  snapshot_sha256: 301cbda477198c0cff0f38601fdb49af8d805cafa7da106733150d64786d987d
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-10/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T17:04:17.819995+00:00 to 2026-10-21T17:04:26.163649+00:00
  summary: Fresh batch 10 corpus diagnostics retain their nonzero exit and warnings;
    the focal graph separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T17:04:26.163649Z'
  snapshot_sha256: f8dae0e292e8e2f8c221450aacc2bb120abe0e3f32c16ed59f8406e8b859a895
assessments:
- assessment_id: identity
  area: identity
  topic: Four-member synthetic community and comparison panel
  outcome: supported
  summary: Retain the defined quad-culture, its four members and source-specific subset
    comparisons.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - identity
  - ontology
  - strain-authority
  details: The main Table 1 has thirteen conditions, including a sulfate-treated Rc/Mh/Mc
    comparison without Dv. Exact H10, Hildenborough, JF-1 and GP6 information can
    enrich the record without changing valid parent-species identities. No host or
    natural community membership is inferred.
- assessment_id: origin-state
  area: scope
  topic: State, origin, category and environment
  outcome: supported
  summary: ENGINEERED, SYNTHETIC and METHANOGENESIS fit this laboratory assembly.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - identity
  - schema
  details: The laboratory-environment term is correct; the source vessel is a serum
    bottle, not a reason to invent continuous bioreactor operation. No equilibrium
    or abundance claim is required. Functional guild roles are supported at their
    source level, without obligacy or reciprocal-fitness inflation.
- assessment_id: taxonomy
  area: identity
  topic: Current names and optional finer strain grounding
  outcome: supported
  summary: Encoded NCBI concepts and exact GTDB mappings are compatible with source
    identities.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - strain-authority
  - gtdb
  - semantics
  details: Historical Methanosaeta and Desulfovibrio names remain source aliases.
    Optional strain refinement must carry its own crosswalk provenance; current species
    parents are not wrong IDs. Exact strains can first be recorded in strain_designation
    without forcing term substitutions.
- assessment_id: cultivation
  area: scope
  topic: Daily medium replacement and gas handling
  outcome: concern
  summary: Replace closed BATCH with the reported draw-and-fill mode and recover protocol
    context.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - culture
  - preparation
  - sulfate
  - schema
  details: Daily replenishment, pH adjustment and venting matter for interpretation
    of seven-day accumulated products. Chamber gas is not proof of a fixed bottle
    headspace throughout growth. Distinguish preparation, revival and storage from
    focal conditions, and record sulfate timing ambiguity without guessing.
- assessment_id: design
  area: scope
  topic: Measured versus fitted endpoints and condition placement
  outcome: concern
  summary: Keep assembly design separate from environmental factors and distinguish
    measured outcomes from fitted cross-feeding.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - measurements
  - model
  - community-output
  details: Sulfate consumption supports inferred H2S. Cross-feeding fluxes are model
    endpoints, not direct tracer measurements. Label-free proteomics and inferred
    pathway changes should not be rewritten as the later paper’s workflow.
- assessment_id: node-0
  area: evidence
  topic: Cellulose Cross-Feeding to Methane
  outcome: supported
  summary: Retain community-level cellulose conversion and distinct methane/cellulose
    synergy responses.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - community-output
  - measurements
  details: Community output changes do not prove reciprocal organism fitness or each
    organism-resolved transfer. Preserve these qualifications and membership context.
- assessment_id: node-1
  area: evidence
  topic: Rc acetate cross-feeding to Mc
  outcome: supported
  summary: Retain directed acetate utilization and qualify sulfate-enhanced contribution
    as fitted.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - acetate-feedback
  - model
  - s1
  - s2
  details: Culture contrasts and acetoclastic markers support the route; increased
    handoff under sulfate is inferred. Downstream contribution to methane is a supported
    route, not proof of unique mediation or all carbon arriving by this path.
- assessment_id: node-2
  area: evidence
  topic: Rc lactate cross-feeding to Dv
  outcome: supported
  summary: Retain the explicitly partial lactate or alternative-intermediate hypothesis.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - dv-hydrogen
  - s3
  details: The source admits lactate/H2 exchange is poorly constrained and alternative
    organic donors remain possible. Preserve the hypothesized downstream supply connection
    to Dv-derived hydrogen rather than assert a uniquely identified lactate-to-H2
    chain.
- assessment_id: node-3
  area: evidence
  topic: Proposed Dv H2 syntrophy to Mh
  outcome: supported
  summary: Retain conditional proposed hydrogen provision under limited sulfate.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - dv-hydrogen
  - model-limits
  - s3
  details: No demonstrated obligate dependence is inferred. Under sulfate, Dv can
    instead consume H2. The downstream connection to methane remains HYPOTHESIZED
    because Dv-specific contribution and donor substrate are not uniquely resolved.
- assessment_id: node-4
  area: evidence
  topic: Mh H2 removal and Rc product inhibition
  outcome: supported
  summary: Retain partial stoichiometric feedback inference.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - acetate-feedback
  - model-limits
  details: The calculation uses methane stoichiometry and accumulated H2, not an imposed-pressure
    intervention. No acetate-specific downstream edge is warranted; preserve its previous
    removal.
- assessment_id: node-5
  area: evidence
  topic: Dv–Mh hydrogen competition
  outcome: supported
  summary: Retain the partial sulfate-associated competition interpretation.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - model-limits
  - s2
  - s3
  details: The two suppressive downstream connections remain qualified. Fitted zero
    hydrogenotrophic flux is not measured cessation; persistent Mh protein and alternative
    electron donors/transfer routes remain in scope. Competition is not a directly
    measured reciprocal-fitness result.
- assessment_id: arrows
  area: evidence
  topic: All five directed causal connections
  outcome: supported
  summary: Retain the existing five arrows with their current strengths and mechanisms.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - acetate-feedback
  - dv-hydrogen
  - model-limits
  - history
  details: Acetate-route→community methane is supported at route level; lactate-handoff→Dv
    H2 and Dv H2→methane are hypothesized; competition→proposed H2 supply is hypothesized
    and competition→methane is partial. No new arrow or restored acetate-feedback
    edge is needed.
- assessment_id: ingredients
  area: evidence
  topic: Non-graph handoff and electron-flow wording
  outcome: concern
  summary: Bring ingredient relevance/explanations to the same measured-versus-fitted
    scope already present in the graph.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - measurements
  - model
  - model-limits
  details: Acetate utilization is supported, but sulfate-strengthened transfers and
    electron redistribution are inferred from fits. Methane is directly measured,
    sulfide estimated from sulfate loss. Exact source quotations should remain unchanged
    while explanations identify their scope.
- assessment_id: provenance
  area: provenance
  topic: Actual stoichiometric model and alternatives
  outcome: concern
  summary: Add structured provenance for the seven-reaction model and its alternative
    fits.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - model
  - s1
  - s2
  - s3
  - code
  details: Separate glucose-equivalent model input from wet-culture cellulose, and
    GC CO2 measurements from the six-row fit. Do not add a genome-scale FBA objective,
    SMETANA or ATP/protein-rate assumptions. Equal-goodness language conflicts with
    displayed S2 errors; preserve uncertainty rather than certify uniqueness.
- assessment_id: resources
  area: provenance
  topic: Source-linked data and code
  outcome: concern
  summary: Add the verified focal proteomics deposit and versioned model repository.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - resources-statement
  - resources
  details: Metadata and file inventory are verified; raw proteomics was not analyzed.
    Preserve Fusion Tribrid versus LTQ Orbitrap Elite attribution. Dataset file counts
    are not biological replicate counts; source triplicates derive from the actual
    experimental description.
- assessment_id: validation
  area: schema
  topic: Native checks and write boundaries
  outcome: supported
  summary: All eight focused checks pass; scientific follow-ups remain despite valid
    syntax.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - auxiliary
  - ontology
  - snippets
  details: Only a new immutable review bundle may be saved. No canonical, cache, history
    or generated artifact changes occur. Corpus warnings and source-specific scientific
    assessments remain separately reported.
- assessment_id: metrics
  area: completeness
  topic: Native scoring
  outcome: supported
  summary: Mechanical scores do not replace evidence review.
  target_ids:
  - CommunityMech:000089
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: Required-field/taxon-role bundle 50 + environment term 5 + at least
      three interactions 10 + growth media 10 + metabolites 5. No external-resource/dataset
      bonus and fewer than three environmental factors. Do not add unsupported fields
      for scores.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0/P2=0/P3=4/P4=0; nine evidence entries/six nodes gives 15 evidence points;
      COMPLETE gives 15. Raw122 capped 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 4
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
findings:
- finding_id: cultivation-context
  issue_key: cm-000089-cultivation-context
  category: scope
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded cultivation, claim-placement or provenance repair
    while identity and qualified causal graph remain sound.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Recover actual draw-and-fill and source strain context
  description: Closed BATCH and fixed headspace wording overcompress daily replacement/venting
    and chamber gas. Exact strain/preparation and sulfate-control details are recoverable.
  target_ids:
  - CommunityMech:000089
  field_paths:
  - cultivation_setup[0]
  - growth_media[0]
  - taxonomy[*].strain_designation
  evidence_ids:
  - culture
  - preparation
  - sulfate
  - identity
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    role: canonical_record
- finding_id: outcome-evidence
  issue_key: cm-000089-outcome-evidence
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded cultivation, claim-placement or provenance repair
    while identity and qualified causal graph remain sound.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Scope non-graph endpoints and ingredient explanations
  description: The graph distinguishes fitted pathways from measured outcomes more
    carefully than design endpoints and ingredient explanations. Assembly design is
    duplicated as an environmental condition.
  target_ids:
  - CommunityMech:000089
  field_paths:
  - engineering_design.measurement_endpoints
  - engineering_design.evidence
  - environmental_factors[0]
  - related_ingredients[*].relevance
  - related_ingredients[*].evidence
  evidence_ids:
  - measurements
  - model
  - model-limits
  - community-output
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    role: canonical_record
- finding_id: model-provenance
  issue_key: cm-000089-model-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded cultivation, claim-placement or provenance repair
    while identity and qualified causal graph remain sound.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Add structured provenance for the actual seven-reaction fit
  description: Computational evidence lacks the structured input/method/alternative-solution
    provenance supplied by this source and its model artifacts.
  target_ids:
  - CommunityMech:000089
  field_paths:
  - ecological_interactions[*].evidence[*].computational_provenance
  - engineering_design.evidence
  evidence_ids:
  - model
  - s1
  - s2
  - s3
  - code
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    role: canonical_record
- finding_id: resources
  issue_key: cm-000089-resources
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded cultivation, claim-placement or provenance repair
    while identity and qualified causal graph remain sound.'
  rule_id: review-checklist.claim-specific-scope-and-evidence
  status: open
  certainty: confirmed
  title: Link verified focal proteomics and code resources
  description: The record omits the source-linked PXD035759 dataset and Community_stoichiometric_model
    repository.
  target_ids:
  - CommunityMech:000089
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - resources-statement
  - resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    role: canonical_record
actions:
- action_id: recover-cultivation
  description: Correct mode and add exact preparation/control context.
  finding_ids:
  - cultivation-context
  target_ids:
  - CommunityMech:000089
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Set cultivation_setup[0].cultivation_mode to SEMI_CONTINUOUS for daily 2 mL withdrawal
    and 2 mL replacement with fresh VM containing 10 g/L cellulose. Remove closed-batch
    claims from notes/explanations. Preserve 160 mL vessel capacity, 20 mL working
    volume, 34 °C, 200 rpm and seven-day assay; do not infer continuous flow or a
    steady state.
  - Record pH adjustment to 7.3 after sampling and venting to atmospheric pressure.
    Describe 3% H2/97% N2 as the reported chamber atmosphere, not a maintained measured
    bottle-headspace composition. Keep evolving gas pools and pressure measurements
    separate from the environmental supply.
  - Record sulfate treatment as 2 mL of 100 mM K2SO4 stock daily with equal sterile-water
    controls; preserve the Methods from-first-day versus Results after-first-day conflict.
    Do not infer final sulfate concentration or silently resolve addition-volume accounting.
    State no-added-sulfate control with the source-reported trace sulfate from FeSO4·6H2O,
    not chemically sulfate-free.
  - Recover H10/ATCC 35319, Hildenborough/ATCC 29579, JF-1 and GP6 in strain_designation
    or source notes. Valid parent NCBI IDs may remain. If adopting finer strain IDs,
    rerun exact-ID GTDB grounding and preserve their distinct denominators/provenance
    rather than copying the current species block.
  - 'Separate revival and focal conditions: Rc modified VM plus 2 g/L yeast extract
    and Dv LS4D at 34 °C; methanogen RST/H2:CO2 80:20/50 mM acetate at 37 °C; Mc approximately
    five-week revival; active OD600 0.5 transfer and about 5 × 10^7 cells per species.
    Do not carry revival yeast extract, acetate or temperature into the experimental
    cellulose medium or infer a complete VM recipe without its source.'
- action_id: scope-outcomes
  description: Align design and ingredient wording with the established graph boundaries.
  finding_ids:
  - outcome-evidence
  target_ids:
  - CommunityMech:000089
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Distinguish measured cellulose/acid/gas outcomes, sulfate consumption and relative
    protein abundance from fitted cross-feeding fluxes in engineering_design. H2S
    is estimated from sulfate consumption; do not call it a directly measured gas
    endpoint. Label-free ProRata/Sipros methods belong to this source, not TMT or
    the later paper’s model workflow.
  - Move or consolidate environmental_factors[0] synthetic assembly content into engineering_design.
    Use actual chemical/physical context for environmental factors and preserve correct
    ENVO laboratory scope. Do not manufacture conditions to improve completeness.
  - Keep acetate utilization and its methane-route contribution, but identify sulfate-strengthened
    handoffs and electron redistribution in related_ingredients as source interpretations
    from stoichiometric modeling. Preserve exact source excerpts; add or relabel narrow
    computational evidence where its explanation goes beyond observed pools.
  - Retain all six nodes and five qualified arrows. Lactate-to-H2 handoff and Dv-derived
    H2 contribution remain hypotheses; product-inhibition relief remains a stoichiometric
    inference without an acetate-feedback edge. Fitted zero Mh flux is not eradication
    or direct pathway cessation. Neither positive methane synergy nor negative cellulose
    synergy establishes reciprocal organism fitness.
  - Preserve the source’s thirteen condition columns, including sulfate-treated Rc/Mh/Mc
    without Dv, and keep quad-culture metaproteomics separate from subset metabolite
    comparisons. Do not generalize a route to a composition lacking the relevant methanogen.
- action_id: record-model-provenance
  description: Represent the focal stoichiometric method, inputs and uncertainty.
  finding_ids:
  - model-provenance
  target_ids:
  - CommunityMech:000089
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - 'Populate computational_provenance for modeled evidence with the seven overall
    reactions: Rc lactate fermentation and hydrogenic acetogenesis; Dv hydrogenic
    lactate oxidation, sulfidogenic lactate oxidation and sulfidogenic hydrogen oxidation;
    Mh hydrogenotrophic and Mc acetoclastic methanogenesis. Distinguish glucose-equivalent
    model input from supplied cellulose and note omitted extracellular hydrolysis
    and low ethanol branch.'
  - Identify daily measured/inferred fitting inputs and the reaction-exclusion/nonnegative
    least-squares procedure. The supplied matrix fits glucose equivalents, acetate,
    lactate, H2, CH4 and sulfide; CO2 gas was measured but omitted from fitting because
    buffering/pH affect partitioning. Do not import SMETANA, CarveMe, a genome-scale
    objective or protein/ATP-rate weights.
  - Record alternative fitted solutions and their limits. Preserve the source’s equal-goodness
    claim as attributed language while noting Table S2’s differing displayed errors;
    do not silently repair numbers or certify unique flux. Protein evidence and fitted
    flux can disagree, and selected S3/S4 marker values must not be harmonized without
    analysis.
  - Pin code and small data to commit d8605d066e782ae5fec5c4fd985b5731684a0834 with
    exact artifact paths. State that this review read the script and CSVs statically
    only. No MATLAB import behavior, executable reproduction, fresh significance test
    or raw proteomics reanalysis is certified.
- action_id: link-resources
  description: Add precise focal dataset and repository links.
  finding_ids:
  - resources
  target_ids:
  - CommunityMech:000089
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - 'Add PRIDE PXD035759 using direct source Data availability and verified project
    identity. Preserve its proteomics scope and 145-entry inventory distinction: 48
    RAW, 48 PEAK, 48 RESULT and one design file. File counts do not define biological
    replication; triplicates are supported by the experiment description.'
  - Add the author Community_stoichiometric_model repository and immutable commit
    d8605d066e782ae5fec5c4fd985b5731684a0834. Distinguish README/tree metadata from
    the three small script/data payloads inspected by lead and raw proteomics not
    analyzed. Do not substitute the later paper’s PXD or repository.
  - Preserve the manuscript/protocol Orbitrap Fusion Tribrid versus structured PRIDE
    LTQ Orbitrap Elite discrepancy with attribution, rather than silently correcting
    either. Keep the exact focal publication reference alongside reusable resource
    links.
- action_id: validate-authorized-curation
  description: Perform canonical remediation only in a separately authorized curation
    task.
  finding_ids:
  - cultivation-context
  - outcome-evidence
  - model-provenance
  - resources
  target_ids:
  - CommunityMech:000089
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cellulose_Methane_Quad_Culture_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Append fresh curation history and run focused schema, strict, term, reference,
    GTDB/domain and history checks after authorized changes; then run just gen-html
    and just check-docs-current. No canonical, cache, history or generated artifact
    is changed by this review.
  - Verify new snippets against exact source sections and maintain independent primary
    versus supplementary-source provenance. Preserve all prior frozen artifacts and
    issue ownership; do not create or close issues here. Review persistence is limited
    to a new immutable review bundle, not a native scientific-status transition.
limitations:
- This review concerns PMID 36847519 (2023 mBio), not the later combinatorial modeling
  paper. No later-study model, TMT workflow or protocol is imported.
- Complete scientific main, all five main figures, two SI figures and complete Tables
  S1–S3 were assessed. Table S4 has 3,736 protein entries; only initial header/first
  30 rows, all 32 marker-name matches and final 10 rows were read. No exhaustive per-protein
  or raw-data certification.
- Table 1 has thirteen conditions including a sulfate-treated Rc/Mh/Mc culture without
  Dv. Community output contrasts and quad-culture proteomics have different scopes.
  Relative proteome fractions are not cell counts or viability measurements.
- Daily culture replacement, pH adjustment and gas venting are source-reported. Chamber
  gas is not a demonstrated fixed bottle-headspace composition. Sulfate onset differs
  between Methods and Results, and stock concentration/addition volume is not a resolved
  final concentration or fluid balance.
- Control contains trace sulfate according to the source; no added sulfate is not
  sulfate-free. Revival yeast extract, acetate and temperatures are not automatically
  focal medium constituents. No complete modified VM recipe or exact recipe cross-link
  was established.
- The model fits six measured/inferred quantities, including glucose equivalents,
  with seven overall reactions. GC CO2 was observed but excluded from supplied fits
  due to buffer/pH partitioning. Neither model input nor a fitted zero is a direct
  organism-specific flux measurement.
- Alternative fluxes and source fit-quality claims do not establish unique mediation.
  Table S2 displayed errors differ from equal-goodness language; S3/S4/Figure 3 marker
  summaries differ. These source inconsistencies are preserved without numerical repair
  or an extra canonical finding.
- Lactate oxidation to hydrogen is unfavorable at studied pressures according to the
  source; alternative organic intermediates remain possible. Keep partial donor/recipient
  hypotheses and the absence of direct pressure intervention or acetate-specific feedback
  evidence.
- H2S is inferred from sulfate loss. Net gas accumulation does not separate gross
  production/consumption. Positive methane and negative cellulose synergies concern
  community outputs, not reciprocal organism fitness.
- Existing species parents are valid. Finer H10/GP6/Hildenborough concepts would require
  their own GTDB mappings. Historical catalogue names and current authority labels
  remain distinct; catalogue growth conditions are not imported.
- PRIDE metadata/inventory and source code identity were checked. Three small code/data
  files were read statically; no model execution, MATLAB import test or raw proteomics
  reanalysis. Manuscript/protocol Fusion Tribrid and structured archive LTQ Orbitrap
  Elite are unresolved attributed values.
- 'All 25 snippets match fresh reference-specific sources and cache: nine main abstract,
  five IMPORTANCE, eleven body. XML alone contains twenty matches; PubMed/EPMC supplies
  IMPORTANCE. Source matching is not causal proof.'
- All 23 official inspected inputs remain unchanged. Focused native checks pass; corpus-wide
  diagnostics remain separately reported. Only a new immutable review bundle may subsequently
  be saved.
notes:
- All 23 fresh official inputs remain unchanged. No canonical, cache, history, generated
  product or prior review is edited.
- Root independently read the complete fresh main and its declared figure/SI scope.
  Lead read complete cached main and all figures/S1–S3, with bounded S4 and full small
  static-code/data reading. Auxiliary and supporting scopes remain exactly as declared
  in their receipts.
- Completeness 80 and quality 100/raw 122 are mechanical values, not proof of unique
  modeled exchanges. Do not add unsupported roles or fields for points.
tags:
- record-review
- cellulose-methane
- main-and-critical-si-assessed
- batch-10
```
