# Acetobacterium–Clostridium electrolysis coculture: whole-record review

- Review: 20261020T034103Z-acetobacterium-clostridium-electrolysis-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-20T03:36:39.636260Z
- Finished UTC: 2026-10-20T03:41:03.531214Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The exact species pair, lactate-mediated chain elongation and both directed process edges are supported. Four major findings concern experimental context, donor role, carbon/energy wording and process grounding; two minor findings concern acid/anion naming and medium linkage. Focused gates pass; corpus warnings remain explicit.

## Scope And Provenance

Entire target, all material statements, two taxa, three nodes, two arrows and three cited primary papers.

Selection: First remaining path after the ten validated batch-01 targets; first record of batch 02 from freshly fetched origin/main. Coverage combines validated helper lists from the baseline and locally committed pending batch 01.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a4611c913c8da9619673df63a0c2cce3aa206a83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000173 | kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml | maintained | Acetobacterium woodii-Clostridium drakei CO2 Electrolysis Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000173 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml |
| validate-strict | passed | True | CommunityMech:000173 | uv run python scripts/validate_strict.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml --out /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000173 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000173 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000173 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml |
| validate-history | passed | True | CommunityMech:000173 | No issues found |
| normalize-cache-names-check | passed | True | CommunityMech:000173 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000173 | Validating kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000173 | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| check-network-quality | failed | True | CommunityMech:000173 | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| Optional structured-source adapter | unavailable | False | CommunityMech:000173 | Runner unavailable in isolated runtime; inspected public catalog fallback has no matching organism. |

## Scientific And Domain Assessments

### Species pair, source strains and study boundaries

identity: supported. Targets: CommunityMech:000173.

All three papers involve the same lactate-producing A. woodii and wild-type C. drakei species pair. The coculture producer is the plasmid-based P_bgaL_ldhD_NFP strain; the original paper also tests other producer strains separately. C. drakei SL1 is DSM 12750 and the A. woodii parental strain is DSM 1030. Species grounding is sound, but species-pair equivalence does not make all assays or reactors identical.

### taxonomy[0..1], NCBI/GTDB and functional roles

grounding: concern. Targets: CommunityMech:000173.

NCBITaxon:33952 and 332101 correctly identify the two species. Native GTDB coherence/domain gates pass; name differences and stored aggregate mapping counts are not independently reconstructed. A. woodii PRIMARY_PRODUCER is supported. C. drakei is the demonstrated lactate consumer; the donor A. woodii CROSS_FEEDER assignment has no demonstrated reverse transfer. SECONDARY_FERMENTER for C. drakei describes its secondary lactate-consuming context, but no complex-substrate primary degrader is identified. ABUNDANT values are ordinal and not measured fractions.

### ecological_interactions[0]: Acetogenic Lactate Production from CO2 and H2

graph: concern. Targets: CommunityMech:000173.

Producer A. woodii fixes carbon and supplies lactate to recipient C. drakei. Carbon dioxide, dihydrogen and lactate terms match substrates/intermediate, and GO:0015977 fits fixation. The generic fermentation annotation is more specific energetically than the gas-fermentation label warrants; it does not follow from this ATP-limited electron-transport-linked process. The biological transfer claim remains supported.

### ecological_interactions[0].downstream[0] -&gt; Lactate-Mediated Chain Elongation to Caproic Acid

graph: supported. Targets: CommunityMech:000173.

Direction is positive substrate provision: A. woodii lactate production feeds C. drakei lactate consumption and chain elongation. Original sequential inoculation and substrate/product trajectories support the link; later lactate-mediated/control comparisons strengthen process-level interpretation. No isotope-resolved carbon allocation or complete enzyme route is asserted.

Participants: NCBITaxon:33952 donor, NCBITaxon:332101 recipient. Mechanism: lactate-mediated cross-feeding. Exact primary quote and locator: transfer, original Results 3.3. Context: sequential AiO coculture; follow-up assays are separate.

### ecological_interactions[1]: Lactate-Mediated Chain Elongation to Caproic Acid

graph: concern. Targets: CommunityMech:000173.

Both partners are declared, with C. drakei as lactate-consuming chain elongator. Product formation and lactate use are supported by coculture and monoculture assays. Fermentative organic-substrate processing is compatible at this broad level, but exact ATP/enzyme pathways remain speculative in the follow-up. Preferred hexanoate is inconsistent with the acid-specific CHEBI identifier; the observed product class remains valid.

### ecological_interactions[2]: Electrolysis-Generated Hydrogen Supply

graph: supported. Targets: CommunityMech:000173.

Abiotic electrolysis supplies H2 for the A. woodii producer; no bacterial source or ecological niche-partitioning relation is invented. Hydrogen limitation is observed. The engineering intervention is represented at community level even though only its direct biological recipient is listed.

### ecological_interactions[2].downstream[0] -&gt; Acetogenic Lactate Production from CO2 and H2

graph: supported. Targets: CommunityMech:000173.

Positive enabling direction: electrode H2 supply to recombinant A. woodii lactate production. The original supply limitation and later current on/off responses support this process edge. This is neither direct electrode-to-cell electron uptake nor a measured causal claim about a particular intracellular protein.

Engineered source node to biological recipient NCBITaxon:33952, feeding the NCBITaxon:332101 partner indirectly. Exact source locators/quotes: hydrogen and feedback. Separate monoculture control and coculture experiments retain their distinct scope.

### description, engineering_design and external_resources[0..2]

scope: concern. Targets: CommunityMech:000173.

Synthetic origin, CO2 valorization objective, lactate-producing donor and wild-type consumer are supported. DOE relevance is a topical interpretation, not documented DOE funding. Carbon-negative production is a stated future potential, not a completed lifecycle analysis. Resource identifiers resolve, but the 2023 process-control paper is mislabeled as mixotrophic cocultivation and the 2024 flask study as bioreactor optimization.

### cultivation_setup[0..1] and growth_media[0]

evidence: concern. Targets: CommunityMech:000173.

The two setup entries correctly distinguish electrode versus external gas, but falsely imply the same vessel and comparable coculture arms. They attach producer-monoculture lactate endpoints to coculture behavior. The full source explicitly reports batch operation, temperature, pH, volumes and cell voltage; an abstract-only cache is not evidence these were unreported. Gas supply alone is not a complete medium. Full-text conditions should be scoped by study and assay, with voltage distinguished from reference potential.

### environment_term and environmental_factors[0..2]

grounding: supported. Targets: CommunityMech:000173.

Laboratory environment fits both tanks and flasks. CO2/H2 supply, alternative delivery and AiO hydrogen limitation are supported. The 0.5 g/L example in factor[1] needs explicit producer-monoculture scope under the experimental-context finding; no universal optimum or shared coculture yield is established.

### related_ingredients[0..6]

evidence: concern. Targets: CommunityMech:000173.

H2 donor, lactate transfer, acetate baseline and butyrate coproduct are supported. The roughly doubled butyrate result is specific to the 2024 matched control comparison, not every coculture. CO2 alone is incorrectly called an energy feedstock. Formate is produced/consumed in C. drakei monocultures and also observed in cocultures, where exact producer/consumer attribution can remain unresolved. Hexanoate/hexanoic-acid names need consistent chemical representation.

### All citations, evidence, history and omitted resources

provenance: supported. Targets: CommunityMech:000173.

All 34 evidence occurrences were checked; matching differences are typographic/indexing rather than invented quotations. Three resource DOIs/PMIDs resolve. The graph history agrees with retained arrows and does not certify reactor metadata. No discussion block or dataset entries are present in the whole record; the control paper advertises a Mendeley dataset, but its external availability was not checked and is not claimed here.

### Structured expression-module cross-check

evidence: not_applicable. Targets: CommunityMech:000173.

The public catalog has no matching organism/dataset. Broader related species modules cannot verify this engineered strain or its exact process phenotype.

### Focused native gates and graph integrity

schema: supported. Targets: CommunityMech:000173.

All focused gates pass and cache hashes remain unchanged. Both members participate, and both arrows target declared nodes. Semantic process/role defects survive these syntax/coherence gates. Required corpus warning failures remain explicit.

### Native completeness and validation quality

completeness: concern. Targets: CommunityMech:000173.

Completeness 95 and quality 91 do not imply scientific approval. Four major and two minor findings remain; all six directly attached node EvidenceItems derive from the original paper.

## Findings

### experimental-context: Monoculture endpoints and distinct apparatus are attributed to equivalent coculture arms

major / open / confirmed; issue key: cm-000173-experimental-context.

The 0.5/8.1 g/L comparison is a producer-monoculture comparison in different named tanks/working volumes. Setup notes imply two otherwise identical coculture arms and falsely state batch regime and voltage were not reported. The 2024 flask study is called bioreactor optimization, and the 2023 process-control resource is labeled as the mixotrophic follow-up.

### donor-role: The lactate donor is classified as a demonstrated cross-feeding consumer

major / open / confirmed; issue key: cm-000173-donor-role.

A. woodii supplies lactate, but CROSS_FEEDER means using metabolites from other taxa. The cited experiments do not demonstrate uptake of C. drakei-derived metabolites by that producer. A potential reverse formate interaction is not established by pooled concentrations.

### co2-energy: CO2 is incorrectly isolated as the energy feedstock

major / open / confirmed; issue key: cm-000173-co2-energy.

related_ingredients[0] calls CO2 the primary carbon and energy feedstock, while the study describes the H2 plus CO2 substrate pair and H2 as electron donor. CO2 fixation needs reducing power; removing H2 from the energy statement changes its biochemical meaning.

### fixation-process: Gas-fermentation wording does not establish the specific GO fermentation process

major / open / confirmed; issue key: cm-000173-fixation-process.

GO:0006113 entails organic-substrate redox and substrate-level ATP generation independent of electron transport. The autotrophic lactate-production node and original Rnf/hydrogenase/ATP-synthetase model do not establish that process merely because the reactor operation is called fermentation. Carbon fixation itself is correctly grounded.

### acid-anion: Hexanoate preferred wording is paired with a hexanoic-acid identifier

minor / open / confirmed; issue key: cm-000173-acid-anion.

CHEBI:30776 canonically denotes hexanoic acid, while preferred terms and relevance prose equate it with hexanoate. The product class is supported, but acid/anion distinction is lost in the structured descriptors.

### media-linkage: The described medium has no verified cross-repository linkage

minor / open / confirmed; issue key: cm-000173-media-linkage.

The record medium is a gas-supply summary without CultureMech/MediaIngredientMech identifiers; full papers identify modified DSM 135 formulations with study-specific differences.

## Recommended Actions And Acceptance Checks

### fix-experimental-context

Separate study, strain, monoculture/coculture and apparatus contexts; correct false source-absence statements using full Methods.

- 0.5/8.1 g/L lactate values are explicitly producer-monoculture endpoints.
- Each setup keeps its actual vessel, mode and measurement context; cell voltage is not an invented reference potential.
- 2023 feedback and 2024 flask experiments retain accurate titles/scope.
- Run focused strict, term and references-explained checks after authorized curation.

### fix-donor-role

Retain carbon-fixing producer function and qualify or remove the unsupported recipient role unless reverse uptake is evidenced.

- Role semantics match the direction supported by the graph and primary assays.
- Do not infer reciprocal benefit or uptake from proximity or shared metabolites.
- Run strict and network checks after authorized curation.

### fix-co2-energy

Distinguish fixed carbon from reductant/energy supply and preserve the full gas-pair context.

- CO2 carbon incorporation is separate from H2 electron donation.
- No carbon-negative lifecycle conclusion is inferred from carbon fixation alone.
- Run references-explained and strict validation.

### fix-fixation-process

Retain supported carbon fixation and remove or replace the unsupported fermentation annotation after definition-level review.

- A replacement term, if used, matches the demonstrated process rather than reactor jargon.
- No complete ATP pathway is promoted from a speculative model.
- Run term, strict and reference checks.

### fix-acid-anion

Align preferred wording and chemical grounding, preserving the publication endpoint and assay context.

- Every chemical descriptor denotes the same acid/base entity as its canonical term.
- Do not infer unmeasured speciation from analytical product naming.
- Run term and strict checks.

### fix-media-linkage

Check exact source-compatible medium/ingredient identifiers in future curation; preserve modified formulations rather than asserting identity to an unmodified base recipe.

- Any link resolves and matches the correct formulation/experiment.
- Unavailable exact matches are left explicitly unresolved.
- Run appropriate linkage, strict and evidence gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml; Entire record: two taxa, three nodes, two arrows, two setups, three environmental factors, one medium, seven related ingredients and three resources | supports | The target denotes an engineered lactate-mediated species pair across three studies; source conditions and comparator cultures must remain distinguishable. |
| original | PMID:36619880; 10.1002/elsc.202100169; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9815077/fullTextXML; Methods, Results, relevant Discussion and main figures/tables | supports | The primary study contains separate A. woodii monoculture gas-delivery comparisons and a sequential two-species AiO coculture. The comparative 0.5/8.1 g/L lactate endpoints belong to monocultures; the coculture produced caproate after C. drakei addition. |
| control | doi:10.3389/fbioe.2023.1212044; 10.3389/fbioe.2023.1212044; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10327822/fullTextXML; Methods, Results, relevant Discussion and main figures/tables | supports | The later study tests lactate-dependent electrode feedback, including distinct C. drakei monoculture and coculture experiments. The title is about process control, not the 2024 mixotrophic study. |
| followup | doi:10.1186/s12934-024-02481-3; 10.1186/s12934-024-02481-3; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11282840/fullTextXML; Methods, Results, relevant Discussion and main figures/tables | supports | The 2024 study compares lactate supplementation, lactate-producing versus control cocultures, concurrent/sequential inoculation and cell proximity in flask experiments. Bioreactor optimization is not its experimental vessel context. |
| transfer | PMID:36619880; Results 3.3, after C. drakei addition | supports | Lactate consumption follows recipient addition and caproate appears; supports donor-to-recipient process level transfer without resolving every intracellular reaction. |
| hydrogen | PMID:36619880; Abstract and Results 3.1–3.2 | supports | Electrolysis supplies hydrogen; its limitation explains the producer process comparison, not a biological niche-partitioning interaction. |
| batch | PMID:36619880; Methods 2.3 | supports | The source explicitly states batch operation; the record assertion that feeding regime is unreported is false. |
| feedback | doi:10.3389/fbioe.2023.1212044; Results 3.3 and Discussion | supports | Current switching responds to lactate and alters hydrogen supply; support for the substrate-supply edge remains at the engineering/process level. |
| flasks | doi:10.1186/s12934-024-02481-3; Methods: Strains and cultivation | supports | The 2024 cultures are flasks, not the original stirred-tank electrolysis apparatus. |
| pathway-limits | doi:10.1186/s12934-024-02481-3; Abstract conclusion | supports | The paper explicitly limits the C. drakei pathway interpretation; product and substrate observations do not identify a complete enzyme pathway. |
| identities | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=36619880,37425355,39061103&amp;retmode=xml; PubmedArticle identities for 36619880, 37425355 and 39061103 | supports | PMID/DOI and PMC identities agree for all three cited articles. Online 2022 versus issue-year 2023 for the first study is a publication-date distinction, not a reference mismatch. |
| setup-context | PMID:36619880; Methods 2.3–2.4; Table 1–2; Figures 1–3 | supports | AiO and direct-gas arms used different named 2-L stirred tanks with different working volumes. Methods identify batch operation and cell voltage; voltage is not a reference-electrode potential. Lactate comparison is A. woodii producer monoculture, while the two-species run is sequential AiO cultivation. |
| roles-energy | doi:10.1186/s12934-024-02481-3; Results monoculture and co-culture comparisons; Discussion proposed pathway | supports | H2 is the reductant/energy-bearing feed and CO2 the fixed carbon substrate. C. drakei consumes lactate and can co-utilize gas; A. woodii supplies lactate. Reciprocal uptake of a recipient-produced metabolite by the donor is not demonstrated. Formate behavior in monocultures is distinct from uncertain partner attribution in concurrent cocultures. |
| energetics | PMID:36619880; Methods 2.5, Results 3.4/Figure 4 and Discussion | supports | Autotrophic lactate production is modeled with Rnf, hydrogenase and ATP synthetase coupling; it is not established as organic-substrate fermentation independent of electron transport. The use of fermentation in reactor terminology cannot alone justify GO:0006113. |
| ontology | OAK local SemanticSQL CHEBI/GO/ENVO snapshots; Exact labels/definitions in /private/tmp/cm-review-session/batch-02/000173/ontology-authority.json | supports | All listed terms resolve. Carbon fixation fits CO2 incorporation. GO:0006113 requires organic-compound redox and substrate-level ATP independent of electron transport. Hexanoic acid and hexanoate are acid/conjugate-base representations, not identical preferred names. Laboratory environment fits controlled reactors and flasks. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum, AbundanceEnum and cultivation/chemical descriptors | supports | CROSS_FEEDER means utilizes metabolites from other taxa, not merely secretes a metabolite. PRIMARY_PRODUCER denotes carbon fixation. ABUNDANT is ordinal within the record, not a numeric abundance band. |
| history | history/records/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture/2026-10-05T055200Z-codex-928235.yaml; Entire history event and corresponding target row in reports/causal_graph_review/decisions/20261005-seven-records.yaml | supports | Prior review retained both process-level arrows and removed niche partitioning from engineered supply. It explicitly did not certify other metadata; that qualification is preserved. |
| snippets | kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml; All 34 EvidenceItem occurrences; full XML paragraphs plus matching primary PubMed abstracts/titles | supports | Thirty-three match after NFKC, whitespace/case and Unicode-dash normalization. The remaining CO(2)/H(2) title notation corresponds to CO2/H2 in current XML and is an indexing representation difference. Source matching does not validate experimental attribution. |
| local-search | references_cache; history/records; reports/causal_graph_review/decisions; kb/taxa; Ignored-inclusive record-ID/slug/citation search | supports | All three caches and the history/graph-decision entries were located; no reusable taxon match was returned for this bounded record/citation query. Exact medium identifiers are absent from the whole target, not asserted absent from every external registry. |
| adapter | https://imodulondb.org/api/datasets; Same-session complete catalog: 20 organisms, 28 datasets; optional runner absent in isolated runtime | context_only | No matching Acetobacterium woodii or Clostridium drakei dataset appears. An unrelated Clostridium dataset does not resolve strain-specific expression claims. No paid provider or other user checkout was used. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml; Actual execution 2026-10-20T03:36:40.179331+00:00 to 2026-10-20T03:36:40.888104+00:00 | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml --out /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv; Actual execution 2026-10-20T03:36:40.179575+00:00 to 2026-10-20T03:36:42.151074+00:00 | supports | uv run python scripts/validate_strict.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml --out /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml; Actual execution 2026-10-20T03:36:40.179675+00:00 to 2026-10-20T03:36:42.079906+00:00 | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml; Actual execution 2026-10-20T03:36:40.888370+00:00 to 2026-10-20T03:36:40.975138+00:00 | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml; Actual execution 2026-10-20T03:36:40.975387+00:00 to 2026-10-20T03:36:42.209600+00:00 | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-history history/records/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture; Actual execution 2026-10-20T03:36:42.080242+00:00 to 2026-10-20T03:36:42.788974+00:00 | supports | No issues found |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-20T03:36:42.790014+00:00 to 2026-10-20T03:36:42.851694+00:00 | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml; Actual execution 2026-10-20T03:36:42.851909+00:00 to 2026-10-20T03:36:43.773369+00:00 | supports | Validating kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | just --no-dotenv audit-network; Actual run finished 2026-10-19T07:30:27.845593+00:00 | supports | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| check-check-network-quality | just --no-dotenv check-network-quality; Actual run finished 2026-10-19T07:30:43.193891+00:00 | supports | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |

## Limits And Additional Notes

- Three main articles were inspected; linked supplementary files and raw assay datasets were not reanalyzed. Discussion inspection focused on experimental interpretation and stated pathway limitations.
- Initial and follow-up producer/recipient controls remain distinct from coculture outcomes; no complete intracellular pathway, reciprocal benefit or lifecycle carbon balance was established by this review.
- Historical GTDB mapping counts and release provenance were not reconstructed; canonical labels and native coherence/domain gates pass.
- Optional adapter unavailable in the isolated runtime; public catalog fallback has no matching organism. Required corpus network gates retain unrelated warning failures.
- A potential Mendeley dataset is advertised in the 2023 article; external dataset availability was not verified and no dataset is newly assigned.
- No record, cache, history, generated product or scientific status changed. Proposed actions are future curation only.
- Every original inspected local input hash remains unchanged; external primary bodies have exact response hashes.
- Exact short quotations are shared across assessments and total at most 25 words per publication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T034103Z-acetobacterium-clostridium-electrolysis-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Acetobacterium–Clostridium electrolysis coculture: whole-record review'
started_at: '2026-10-20T03:36:39.636260Z'
finished_at: '2026-10-20T03:41:03.531214Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: No target authored or modified this session; historical curation
    also used codex, so person-level independence is unknown.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The exact species pair, lactate-mediated chain elongation and both directed
  process edges are supported. Four major findings concern experimental context, donor
  role, carbon/energy wording and process grounding; two minor findings concern acid/anion
  naming and medium linkage. Focused gates pass; corpus warnings remain explicit.
source:
  git_revision: a4611c913c8da9619673df63a0c2cce3aa206a83
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
  - path: history/records/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture/2026-10-05T055200Z-codex-928235.yaml
    sha256: b3868ceebec7c942630c98bc707f844803d23e49dcdddcaf567a292855ab7a88
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    sha256: 4861dca464d4efcdf3db47d3dacb0480c77210c168b30d3aec613ee4cf3518cf
    role: target
  - path: references_cache/PMID_36619880.md
    sha256: de055ad95352c6a350c58bef946f9fd42d8b8f9c0fa0b3f4daf1638695878212
    role: context
  - path: references_cache/doi_10.1186_s12934-024-02481-3.md
    sha256: cc695181c06ce5fef78fdf8d9504e68c5b80f526ca07398b59b69a0b16b9c5f9
    role: context
  - path: references_cache/doi_10.3389_fbioe.2023.1212044.md
    sha256: dbf6bde393721896998b47cced40e6b6902320635a4b4fd3fcea03b91766c216
    role: context
  - path: reports/causal_graph_review/decisions/20261005-seven-records.yaml
    sha256: 064f7395bbb54d42023f3a0bceeb31a3dd990221e62094f6a51507fee81eea69
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000173
  path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  label: Acetobacterium woodii-Clostridium drakei CO2 Electrolysis Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
scope:
  description: Entire target, all material statements, two taxa, three nodes, two
    arrows and three cited primary papers.
  selection: First remaining path after the ten validated batch-01 targets; first
    record of batch 02 from freshly fetched origin/main. Coverage combines validated
    helper lists from the baseline and locally committed pending batch 01.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000173
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml'
  target_ids:
  - CommunityMech:000173
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml\
    \ --out /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv"
  target_ids:
  - CommunityMech:000173
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000173
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000173
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml'
  target_ids:
  - CommunityMech:000173
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: No issues found
  target_ids:
  - CommunityMech:000173
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-history history/records/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Command completed without reported issues.
  target_ids:
  - CommunityMech:000173
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: "Validating kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000173
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Reused complete corpus result at identical freshly fetched base and unchanged
    canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors.
    Target has no finding. No new execution is claimed.'
  target_ids:
  - CommunityMech:000173
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Corpus-wide warnings outside selected target, retained as actual required
    failures.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Reused complete corpus result at identical freshly fetched base and unchanged
    canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors.
    Target has no finding. No new execution is claimed.'
  target_ids:
  - CommunityMech:000173
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Corpus-wide warnings outside selected target, retained as actual required
    failures.
- check_id: optional-adapter
  name: Optional structured-source adapter
  status: unavailable
  required: false
  summary: Runner unavailable in isolated runtime; inspected public catalog fallback
    has no matching organism.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  locator: 'Entire record: two taxa, three nodes, two arrows, two setups, three environmental
    factors, one medium, seven related ingredients and three resources'
  summary: The target denotes an engineered lactate-mediated species pair across three
    studies; source conditions and comparator cultures must remain distinguishable.
  support: supports
  accessed_at: '2026-10-20T03:41:03.524040Z'
- evidence_id: original
  kind: primary_source
  reference: PMID:36619880
  locator: 10.1002/elsc.202100169; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC9815077/fullTextXML;
    Methods, Results, relevant Discussion and main figures/tables
  summary: The primary study contains separate A. woodii monoculture gas-delivery
    comparisons and a sequential two-species AiO coculture. The comparative 0.5/8.1
    g/L lactate endpoints belong to monocultures; the coculture produced caproate
    after C. drakei addition.
  support: supports
  accessed_at: '2026-10-20T03:37:05.808929Z'
  snapshot_sha256: ddc57d9db62df5e105f8e5397750129eb7fdf0fd3473350bae707eca20f0dfa3
- evidence_id: control
  kind: primary_source
  reference: doi:10.3389/fbioe.2023.1212044
  locator: 10.3389/fbioe.2023.1212044; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10327822/fullTextXML;
    Methods, Results, relevant Discussion and main figures/tables
  summary: The later study tests lactate-dependent electrode feedback, including distinct
    C. drakei monoculture and coculture experiments. The title is about process control,
    not the 2024 mixotrophic study.
  support: supports
  accessed_at: '2026-10-20T03:37:05.809328Z'
  snapshot_sha256: 122f00edec6923a2abe398eb58a6dd8d0e7c9966e9eb2fdb695b0a9d7784e426
- evidence_id: followup
  kind: primary_source
  reference: doi:10.1186/s12934-024-02481-3
  locator: 10.1186/s12934-024-02481-3; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11282840/fullTextXML;
    Methods, Results, relevant Discussion and main figures/tables
  summary: The 2024 study compares lactate supplementation, lactate-producing versus
    control cocultures, concurrent/sequential inoculation and cell proximity in flask
    experiments. Bioreactor optimization is not its experimental vessel context.
  support: supports
  accessed_at: '2026-10-20T03:37:05.809537Z'
  snapshot_sha256: 663d447647a33eee2959d41d1a8f18f1ecdd132151de77da6d7c885b4b5c0049
- evidence_id: transfer
  kind: primary_source
  reference: PMID:36619880
  locator: Results 3.3, after C. drakei addition
  summary: Lactate consumption follows recipient addition and caproate appears; supports
    donor-to-recipient process level transfer without resolving every intracellular
    reaction.
  support: supports
  accessed_at: '2026-10-20T03:37:05.808929Z'
  quote: lactate concentration started to decline
- evidence_id: hydrogen
  kind: primary_source
  reference: PMID:36619880
  locator: Abstract and Results 3.1–3.2
  summary: Electrolysis supplies hydrogen; its limitation explains the producer process
    comparison, not a biological niche-partitioning interaction.
  support: supports
  accessed_at: '2026-10-20T03:37:05.808929Z'
  quote: Hydrogen limitation was identified
- evidence_id: batch
  kind: primary_source
  reference: PMID:36619880
  locator: Methods 2.3
  summary: The source explicitly states batch operation; the record assertion that
    feeding regime is unreported is false.
  support: supports
  accessed_at: '2026-10-20T03:37:05.808929Z'
  quote: All batch fermentations
- evidence_id: feedback
  kind: primary_source
  reference: doi:10.3389/fbioe.2023.1212044
  locator: Results 3.3 and Discussion
  summary: Current switching responds to lactate and alters hydrogen supply; support
    for the substrate-supply edge remains at the engineering/process level.
  support: supports
  accessed_at: '2026-10-20T03:37:05.809328Z'
  quote: automated process control
- evidence_id: flasks
  kind: primary_source
  reference: doi:10.1186/s12934-024-02481-3
  locator: 'Methods: Strains and cultivation'
  summary: The 2024 cultures are flasks, not the original stirred-tank electrolysis
    apparatus.
  support: supports
  accessed_at: '2026-10-20T03:37:05.809537Z'
  quote: rubber-sealed 500-mL Müller-Krempel flasks
- evidence_id: pathway-limits
  kind: primary_source
  reference: doi:10.1186/s12934-024-02481-3
  locator: Abstract conclusion
  summary: The paper explicitly limits the C. drakei pathway interpretation; product
    and substrate observations do not identify a complete enzyme pathway.
  support: supports
  accessed_at: '2026-10-20T03:37:05.809537Z'
  quote: still speculatory
- evidence_id: identities
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=36619880,37425355,39061103&retmode=xml
  locator: PubmedArticle identities for 36619880, 37425355 and 39061103
  summary: PMID/DOI and PMC identities agree for all three cited articles. Online
    2022 versus issue-year 2023 for the first study is a publication-date distinction,
    not a reference mismatch.
  support: supports
  accessed_at: '2026-10-20T03:37:05.809847Z'
  snapshot_sha256: 681655a8d6f7b7114a7c2decc0ec09bda7d328e36bdd87b98d528b0533a066e1
- evidence_id: setup-context
  kind: primary_source
  reference: PMID:36619880
  locator: Methods 2.3–2.4; Table 1–2; Figures 1–3
  summary: AiO and direct-gas arms used different named 2-L stirred tanks with different
    working volumes. Methods identify batch operation and cell voltage; voltage is
    not a reference-electrode potential. Lactate comparison is A. woodii producer
    monoculture, while the two-species run is sequential AiO cultivation.
  support: supports
  accessed_at: '2026-10-20T03:37:05.808929Z'
- evidence_id: roles-energy
  kind: primary_source
  reference: doi:10.1186/s12934-024-02481-3
  locator: Results monoculture and co-culture comparisons; Discussion proposed pathway
  summary: H2 is the reductant/energy-bearing feed and CO2 the fixed carbon substrate.
    C. drakei consumes lactate and can co-utilize gas; A. woodii supplies lactate.
    Reciprocal uptake of a recipient-produced metabolite by the donor is not demonstrated.
    Formate behavior in monocultures is distinct from uncertain partner attribution
    in concurrent cocultures.
  support: supports
  accessed_at: '2026-10-20T03:37:05.809537Z'
- evidence_id: energetics
  kind: primary_source
  reference: PMID:36619880
  locator: Methods 2.5, Results 3.4/Figure 4 and Discussion
  summary: Autotrophic lactate production is modeled with Rnf, hydrogenase and ATP
    synthetase coupling; it is not established as organic-substrate fermentation independent
    of electron transport. The use of fermentation in reactor terminology cannot alone
    justify GO:0006113.
  support: supports
  accessed_at: '2026-10-20T03:37:05.808929Z'
- evidence_id: ontology
  kind: authority
  reference: OAK local SemanticSQL CHEBI/GO/ENVO snapshots
  locator: Exact labels/definitions in /private/tmp/cm-review-session/batch-02/000173/ontology-authority.json
  summary: All listed terms resolve. Carbon fixation fits CO2 incorporation. GO:0006113
    requires organic-compound redox and substrate-level ATP independent of electron
    transport. Hexanoic acid and hexanoate are acid/conjugate-base representations,
    not identical preferred names. Laboratory environment fits controlled reactors
    and flasks.
  support: supports
  accessed_at: '2026-10-20T03:38:14.143713Z'
  snapshot_sha256: f35d15bdb430500be51e48aca158a60b3d5f739e408223119a2d8ed951bd9356
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum, AbundanceEnum and cultivation/chemical descriptors
  summary: CROSS_FEEDER means utilizes metabolites from other taxa, not merely secretes
    a metabolite. PRIMARY_PRODUCER denotes carbon fixation. ABUNDANT is ordinal within
    the record, not a numeric abundance band.
  support: supports
  accessed_at: '2026-10-20T03:41:03.526154Z'
- evidence_id: history
  kind: record_content
  reference: history/records/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture/2026-10-05T055200Z-codex-928235.yaml
  locator: Entire history event and corresponding target row in reports/causal_graph_review/decisions/20261005-seven-records.yaml
  summary: Prior review retained both process-level arrows and removed niche partitioning
    from engineered supply. It explicitly did not certify other metadata; that qualification
    is preserved.
  support: supports
  accessed_at: '2026-10-20T03:41:03.526157Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  locator: All 34 EvidenceItem occurrences; full XML paragraphs plus matching primary
    PubMed abstracts/titles
  summary: Thirty-three match after NFKC, whitespace/case and Unicode-dash normalization.
    The remaining CO(2)/H(2) title notation corresponds to CO2/H2 in current XML and
    is an indexing representation difference. Source matching does not validate experimental
    attribution.
  support: supports
  accessed_at: '2026-10-20T03:41:03.526391Z'
  snapshot_sha256: 752b1f419d24239984fc6433d4b614be09c84bece07b40f4428a525c9753828e
- evidence_id: local-search
  kind: search
  reference: references_cache; history/records; reports/causal_graph_review/decisions;
    kb/taxa
  locator: Ignored-inclusive record-ID/slug/citation search
  summary: All three caches and the history/graph-decision entries were located; no
    reusable taxon match was returned for this bounded record/citation query. Exact
    medium identifiers are absent from the whole target, not asserted absent from
    every external registry.
  support: supports
  accessed_at: '2026-10-20T03:38:14.251109Z'
  search_scope: rg --no-ignore --hidden -l 'Acetobacterium_Clostridium_CO2_Electrolysis_Coculture|CommunityMech:000173|36619880|1212044|02481-3'
    references_cache history/records reports/causal_graph_review/decisions kb/taxa
  snapshot_sha256: 76d15aa313a87bacca9126b271c49c75abebedf6104999df32193d00220fb549
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Same-session complete catalog: 20 organisms, 28 datasets; optional runner
    absent in isolated runtime'
  summary: No matching Acetobacterium woodii or Clostridium drakei dataset appears.
    An unrelated Clostridium dataset does not resolve strain-specific expression claims.
    No paid provider or other user checkout was used.
  support: context_only
  accessed_at: '2026-10-19T23:31:07.726770Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  locator: Actual execution 2026-10-20T03:36:40.179331+00:00 to 2026-10-20T03:36:40.888104+00:00
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml'
  support: supports
  accessed_at: '2026-10-20T03:36:40.888104Z'
  snapshot_sha256: cb750c00d2fee1df27d7cc4850738bbbeb6a865fdeeefb982164d2af85d4d100
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv
  locator: Actual execution 2026-10-20T03:36:40.179575+00:00 to 2026-10-20T03:36:42.151074+00:00
  summary: "uv run python scripts/validate_strict.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml\
    \ --out /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-02/000173/strict-report.tsv"
  support: supports
  accessed_at: '2026-10-20T03:36:42.151074Z'
  snapshot_sha256: 3e0c2646a601d69228c4785e1edb0757cbf10b63e310c21ae874376129d341be
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  locator: Actual execution 2026-10-20T03:36:40.179675+00:00 to 2026-10-20T03:36:42.079906+00:00
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-10-20T03:36:42.079906Z'
  snapshot_sha256: acde93d588a646942f572394c2c3401a4e157d5b024421cf02419b0008e993f2
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  locator: Actual execution 2026-10-20T03:36:40.888370+00:00 to 2026-10-20T03:36:40.975138+00:00
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-10-20T03:36:40.975138Z'
  snapshot_sha256: 319f38f63ef633e8756dcf528147ee1e8d7a7306b13274f2b0d58dd06275c954
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  locator: Actual execution 2026-10-20T03:36:40.975387+00:00 to 2026-10-20T03:36:42.209600+00:00
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml'
  support: supports
  accessed_at: '2026-10-20T03:36:42.209600Z'
  snapshot_sha256: f2272714a1ddc6877f20a95a63c6aa28856234145dc98eebb9c4241f70ad5ff6
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-history history/records/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture
  locator: Actual execution 2026-10-20T03:36:42.080242+00:00 to 2026-10-20T03:36:42.788974+00:00
  summary: No issues found
  support: supports
  accessed_at: '2026-10-20T03:36:42.788974Z'
  snapshot_sha256: 015f4449e9cda30e595e15144543007dfdd42cb3c32e4960c9ec05e0e5b1863d
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-20T03:36:42.790014+00:00 to 2026-10-20T03:36:42.851694+00:00
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-10-20T03:36:42.851694Z'
  snapshot_sha256: 0b2023b62f0550d4a31a0dc2e2d539fd710f70e16d044e7f71ec3302b1454a61
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
  locator: Actual execution 2026-10-20T03:36:42.851909+00:00 to 2026-10-20T03:36:43.773369+00:00
  summary: "Validating kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-10-20T03:36:43.773369Z'
  snapshot_sha256: 4245c7384e7d99cf1348662fea5d86ad8047aa076208629cd693efac713e9671
- evidence_id: check-audit-network
  kind: validation
  reference: just --no-dotenv audit-network
  locator: Actual run finished 2026-10-19T07:30:27.845593+00:00
  summary: 'Reused complete corpus result at identical freshly fetched base and unchanged
    canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors.
    Target has no finding. No new execution is claimed.'
  support: supports
  accessed_at: '2026-10-19T07:30:27.845593Z'
  snapshot_sha256: bedf3fd18a964bda429f7c6b5feb01b8918e1440b48a4329664501161c80e3f4
- evidence_id: check-check-network-quality
  kind: validation
  reference: just --no-dotenv check-network-quality
  locator: Actual run finished 2026-10-19T07:30:43.193891+00:00
  summary: 'Reused complete corpus result at identical freshly fetched base and unchanged
    canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors.
    Target has no finding. No new execution is claimed.'
  support: supports
  accessed_at: '2026-10-19T07:30:43.193891Z'
  snapshot_sha256: 885e62e84ed8d3e69a6e5ef5be43f941ef64d756107c3b062846831f76e081aa
assessments:
- assessment_id: identity
  area: identity
  topic: Species pair, source strains and study boundaries
  outcome: supported
  summary: All three papers involve the same lactate-producing A. woodii and wild-type
    C. drakei species pair. The coculture producer is the plasmid-based P_bgaL_ldhD_NFP
    strain; the original paper also tests other producer strains separately. C. drakei
    SL1 is DSM 12750 and the A. woodii parental strain is DSM 1030. Species grounding
    is sound, but species-pair equivalence does not make all assays or reactors identical.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - original
  - control
  - followup
  - identities
  dimensions:
  - name: source_strain
    value: A. woodii P_bgaL_ldhD_NFP producer plus C. drakei SL1
    definition: Other A. woodii strains in comparisons are not interchangeable coculture
      producers.
    evidence_ids:
    - original
    - followup
  - name: community_scope
    value: Defined synthetic two-species lactate-mediated coculture
    definition: Separate producer and recipient monocultures supply controls, not
      community outcomes.
    evidence_ids:
    - original
    - control
    - followup
  - name: experimental_setting
    value: AiO stirred-tank cocultures; separate direct-gas producer controls; 2024
      flask cocultures
    definition: Individual study and assay settings remain separate.
    evidence_ids:
    - setup-context
    - flasks
  - name: medium
    value: Study-specific modified DSM 135 media
    definition: Main Methods describe formulations/conditions; serum precultures,
      stirred tanks and flasks are not one recipe.
    evidence_ids:
    - original
    - control
    - followup
  - name: source_category
    value: Three primary full-text experimental papers with modeled pathways
    definition: Measured products/consumption are distinct from proposed intracellular
      flux and carbon-negative potential.
    evidence_ids:
    - original
    - control
    - followup
- assessment_id: taxonomy
  area: grounding
  topic: taxonomy[0..1], NCBI/GTDB and functional roles
  outcome: concern
  summary: NCBITaxon:33952 and 332101 correctly identify the two species. Native GTDB
    coherence/domain gates pass; name differences and stored aggregate mapping counts
    are not independently reconstructed. A. woodii PRIMARY_PRODUCER is supported.
    C. drakei is the demonstrated lactate consumer; the donor A. woodii CROSS_FEEDER
    assignment has no demonstrated reverse transfer. SECONDARY_FERMENTER for C. drakei
    describes its secondary lactate-consuming context, but no complex-substrate primary
    degrader is identified. ABUNDANT values are ordinal and not measured fractions.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - schema
  - roles-energy
  - original
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Acetogenic Lactate Production from CO2 and H2'
  outcome: concern
  summary: Producer A. woodii fixes carbon and supplies lactate to recipient C. drakei.
    Carbon dioxide, dihydrogen and lactate terms match substrates/intermediate, and
    GO:0015977 fits fixation. The generic fermentation annotation is more specific
    energetically than the gas-fermentation label warrants; it does not follow from
    this ATP-limited electron-transport-linked process. The biological transfer claim
    remains supported.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - original
  - transfer
  - energetics
  - ontology
- assessment_id: edge-0
  area: graph
  topic: ecological_interactions[0].downstream[0] -> Lactate-Mediated Chain Elongation
    to Caproic Acid
  outcome: supported
  summary: 'Direction is positive substrate provision: A. woodii lactate production
    feeds C. drakei lactate consumption and chain elongation. Original sequential
    inoculation and substrate/product trajectories support the link; later lactate-mediated/control
    comparisons strengthen process-level interpretation. No isotope-resolved carbon
    allocation or complete enzyme route is asserted.'
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - transfer
  - original
  - followup
  details: 'Participants: NCBITaxon:33952 donor, NCBITaxon:332101 recipient. Mechanism:
    lactate-mediated cross-feeding. Exact primary quote and locator: transfer, original
    Results 3.3. Context: sequential AiO coculture; follow-up assays are separate.'
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Lactate-Mediated Chain Elongation to Caproic
    Acid'
  outcome: concern
  summary: Both partners are declared, with C. drakei as lactate-consuming chain elongator.
    Product formation and lactate use are supported by coculture and monoculture assays.
    Fermentative organic-substrate processing is compatible at this broad level, but
    exact ATP/enzyme pathways remain speculative in the follow-up. Preferred hexanoate
    is inconsistent with the acid-specific CHEBI identifier; the observed product
    class remains valid.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - original
  - followup
  - pathway-limits
  - ontology
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Electrolysis-Generated Hydrogen Supply'
  outcome: supported
  summary: Abiotic electrolysis supplies H2 for the A. woodii producer; no bacterial
    source or ecological niche-partitioning relation is invented. Hydrogen limitation
    is observed. The engineering intervention is represented at community level even
    though only its direct biological recipient is listed.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - hydrogen
  - original
  - control
- assessment_id: edge-2
  area: graph
  topic: ecological_interactions[2].downstream[0] -> Acetogenic Lactate Production
    from CO2 and H2
  outcome: supported
  summary: 'Positive enabling direction: electrode H2 supply to recombinant A. woodii
    lactate production. The original supply limitation and later current on/off responses
    support this process edge. This is neither direct electrode-to-cell electron uptake
    nor a measured causal claim about a particular intracellular protein.'
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - hydrogen
  - feedback
  - control
  details: 'Engineered source node to biological recipient NCBITaxon:33952, feeding
    the NCBITaxon:332101 partner indirectly. Exact source locators/quotes: hydrogen
    and feedback. Separate monoculture control and coculture experiments retain their
    distinct scope.'
- assessment_id: engineering
  area: scope
  topic: description, engineering_design and external_resources[0..2]
  outcome: concern
  summary: Synthetic origin, CO2 valorization objective, lactate-producing donor and
    wild-type consumer are supported. DOE relevance is a topical interpretation, not
    documented DOE funding. Carbon-negative production is a stated future potential,
    not a completed lifecycle analysis. Resource identifiers resolve, but the 2023
    process-control paper is mislabeled as mixotrophic cocultivation and the 2024
    flask study as bioreactor optimization.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - original
  - control
  - followup
- assessment_id: setup
  area: evidence
  topic: cultivation_setup[0..1] and growth_media[0]
  outcome: concern
  summary: The two setup entries correctly distinguish electrode versus external gas,
    but falsely imply the same vessel and comparable coculture arms. They attach producer-monoculture
    lactate endpoints to coculture behavior. The full source explicitly reports batch
    operation, temperature, pH, volumes and cell voltage; an abstract-only cache is
    not evidence these were unreported. Gas supply alone is not a complete medium.
    Full-text conditions should be scoped by study and assay, with voltage distinguished
    from reference potential.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - setup-context
  - batch
  - original
  - control
  - followup
- assessment_id: environment
  area: grounding
  topic: environment_term and environmental_factors[0..2]
  outcome: supported
  summary: Laboratory environment fits both tanks and flasks. CO2/H2 supply, alternative
    delivery and AiO hydrogen limitation are supported. The 0.5 g/L example in factor[1]
    needs explicit producer-monoculture scope under the experimental-context finding;
    no universal optimum or shared coculture yield is established.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - ontology
  - original
  - setup-context
- assessment_id: ingredients
  area: evidence
  topic: related_ingredients[0..6]
  outcome: concern
  summary: H2 donor, lactate transfer, acetate baseline and butyrate coproduct are
    supported. The roughly doubled butyrate result is specific to the 2024 matched
    control comparison, not every coculture. CO2 alone is incorrectly called an energy
    feedstock. Formate is produced/consumed in C. drakei monocultures and also observed
    in cocultures, where exact producer/consumer attribution can remain unresolved.
    Hexanoate/hexanoic-acid names need consistent chemical representation.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - roles-energy
  - followup
  - ontology
- assessment_id: evidence-history
  area: provenance
  topic: All citations, evidence, history and omitted resources
  outcome: supported
  summary: All 34 evidence occurrences were checked; matching differences are typographic/indexing
    rather than invented quotations. Three resource DOIs/PMIDs resolve. The graph
    history agrees with retained arrows and does not certify reactor metadata. No
    discussion block or dataset entries are present in the whole record; the control
    paper advertises a Mendeley dataset, but its external availability was not checked
    and is not claimed here.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - snippets
  - identities
  - history
  - control
- assessment_id: adapter-applicability
  area: evidence
  topic: Structured expression-module cross-check
  outcome: not_applicable
  summary: The public catalog has no matching organism/dataset. Broader related species
    modules cannot verify this engineered strain or its exact process phenotype.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - adapter
- assessment_id: validation
  area: schema
  topic: Focused native gates and graph integrity
  outcome: supported
  summary: All focused gates pass and cache hashes remain unchanged. Both members
    participate, and both arrows target declared nodes. Semantic process/role defects
    survive these syntax/coherence gates. Required corpus warning failures remain
    explicit.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-references-explained
  - check-audit-network
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: concern
  summary: Completeness 95 and quality 91 do not imply scientific approval. Four major
    and two minor findings remain; all six directly attached node EvidenceItems derive
    from the original paper.
  target_ids:
  - CommunityMech:000173
  evidence_ids:
  - record
  - check-audit-network
  metrics:
  - name: completeness
    value: 95
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata/taxonomy roles +5 environment +10 for
      at least 3 factors +10 for at least 3 nodes +5 external resources +10 growth_media
      +5 datasets +5 any node metabolites). Applied 50+5+10+10+5+10+0+5=95; presence
      only.
  - name: validation_quality
    value: 91
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50*P1-10*P2-2*P3+20*min(mean evidence/2,1)+15 if native
      network COMPLETE,0,100). P1=0,P2=4,P3=2; six EvidenceItems/three nodes=2; all
      participants/references intact. 100-40-4+20+15=91.
  - name: P1
    value: 0
    unit: findings
    definition: Target native severity count.
  - name: P2
    value: 4
    unit: findings
    definition: Target native severity count.
  - name: P3
    value: 2
    unit: findings
    definition: Target native severity count.
  - name: interaction_evidence
    value: 2
    unit: evidence items per interaction
    denominator: 3
    definition: Six directly attached entries over three nodes from one publication;
      not independent replication.
findings:
- finding_id: experimental-context
  issue_key: cm-000173-experimental-context
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: experimental attribution, biological role or process
    meaning materially exceeds the source.'
  rule_id: CLAUDE.claim-level-evidence
  status: open
  certainty: confirmed
  title: Monoculture endpoints and distinct apparatus are attributed to equivalent
    coculture arms
  description: The 0.5/8.1 g/L comparison is a producer-monoculture comparison in
    different named tanks/working volumes. Setup notes imply two otherwise identical
    coculture arms and falsely state batch regime and voltage were not reported. The
    2024 flask study is called bioreactor optimization, and the 2023 process-control
    resource is labeled as the mixotrophic follow-up.
  target_ids:
  - CommunityMech:000173
  field_paths:
  - engineering_design.perturbation_design
  - cultivation_setup[0]
  - cultivation_setup[1]
  - environmental_factors[1]
  - growth_media[0]
  - external_resources[1]
  - external_resources[2]
  evidence_ids:
  - original
  - control
  - followup
  - setup-context
  - batch
  - flasks
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
- finding_id: donor-role
  issue_key: cm-000173-donor-role
  category: consistency
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: experimental attribution, biological role or process
    meaning materially exceeds the source.'
  rule_id: P2.4
  status: open
  certainty: confirmed
  title: The lactate donor is classified as a demonstrated cross-feeding consumer
  description: A. woodii supplies lactate, but CROSS_FEEDER means using metabolites
    from other taxa. The cited experiments do not demonstrate uptake of C. drakei-derived
    metabolites by that producer. A potential reverse formate interaction is not established
    by pooled concentrations.
  target_ids:
  - CommunityMech:000173
  field_paths:
  - taxonomy[0].functional_role
  evidence_ids:
  - schema
  - roles-energy
  - original
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
- finding_id: co2-energy
  issue_key: cm-000173-co2-energy
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: experimental attribution, biological role or process
    meaning materially exceeds the source.'
  rule_id: CLAUDE.claim-level-evidence
  status: open
  certainty: confirmed
  title: CO2 is incorrectly isolated as the energy feedstock
  description: related_ingredients[0] calls CO2 the primary carbon and energy feedstock,
    while the study describes the H2 plus CO2 substrate pair and H2 as electron donor.
    CO2 fixation needs reducing power; removing H2 from the energy statement changes
    its biochemical meaning.
  target_ids:
  - CommunityMech:000173
  field_paths:
  - related_ingredients[0].relevance
  - growth_media[0].evidence[1].explanation
  evidence_ids:
  - roles-energy
  - original
  - followup
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
- finding_id: fixation-process
  issue_key: cm-000173-fixation-process
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: experimental attribution, biological role or process
    meaning materially exceeds the source.'
  rule_id: review-checklist.grounding
  status: open
  certainty: confirmed
  title: Gas-fermentation wording does not establish the specific GO fermentation
    process
  description: GO:0006113 entails organic-substrate redox and substrate-level ATP
    generation independent of electron transport. The autotrophic lactate-production
    node and original Rnf/hydrogenase/ATP-synthetase model do not establish that process
    merely because the reactor operation is called fermentation. Carbon fixation itself
    is correctly grounded.
  target_ids:
  - CommunityMech:000173
  field_paths:
  - ecological_interactions[0].biological_processes[1]
  evidence_ids:
  - ontology
  - energetics
  - original
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
- finding_id: acid-anion
  issue_key: cm-000173-acid-anion
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded chemical naming or resource-linkage defect;
    core community identity remains interpretable.'
  rule_id: review-checklist.grounding
  status: open
  certainty: confirmed
  title: Hexanoate preferred wording is paired with a hexanoic-acid identifier
  description: CHEBI:30776 canonically denotes hexanoic acid, while preferred terms
    and relevance prose equate it with hexanoate. The product class is supported,
    but acid/anion distinction is lost in the structured descriptors.
  target_ids:
  - CommunityMech:000173
  field_paths:
  - ecological_interactions[1].metabolites[1]
  - related_ingredients[5]
  evidence_ids:
  - record
  - ontology
  - original
  - followup
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
- finding_id: media-linkage
  issue_key: cm-000173-media-linkage
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded chemical naming or resource-linkage defect;
    core community identity remains interpretable.'
  rule_id: P3.1
  status: open
  certainty: confirmed
  title: The described medium has no verified cross-repository linkage
  description: The record medium is a gas-supply summary without CultureMech/MediaIngredientMech
    identifiers; full papers identify modified DSM 135 formulations with study-specific
    differences.
  target_ids:
  - CommunityMech:000173
  field_paths:
  - growth_media[0]
  evidence_ids:
  - record
  - original
  - control
  - followup
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
actions:
- action_id: fix-experimental-context
  description: Separate study, strain, monoculture/coculture and apparatus contexts;
    correct false source-absence statements using full Methods.
  finding_ids:
  - experimental-context
  target_ids:
  - CommunityMech:000173
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - 0.5/8.1 g/L lactate values are explicitly producer-monoculture endpoints.
  - Each setup keeps its actual vessel, mode and measurement context; cell voltage
    is not an invented reference potential.
  - 2023 feedback and 2024 flask experiments retain accurate titles/scope.
  - Run focused strict, term and references-explained checks after authorized curation.
- action_id: fix-donor-role
  description: Retain carbon-fixing producer function and qualify or remove the unsupported
    recipient role unless reverse uptake is evidenced.
  finding_ids:
  - donor-role
  target_ids:
  - CommunityMech:000173
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Role semantics match the direction supported by the graph and primary assays.
  - Do not infer reciprocal benefit or uptake from proximity or shared metabolites.
  - Run strict and network checks after authorized curation.
- action_id: fix-co2-energy
  description: Distinguish fixed carbon from reductant/energy supply and preserve
    the full gas-pair context.
  finding_ids:
  - co2-energy
  target_ids:
  - CommunityMech:000173
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - CO2 carbon incorporation is separate from H2 electron donation.
  - No carbon-negative lifecycle conclusion is inferred from carbon fixation alone.
  - Run references-explained and strict validation.
- action_id: fix-fixation-process
  description: Retain supported carbon fixation and remove or replace the unsupported
    fermentation annotation after definition-level review.
  finding_ids:
  - fixation-process
  target_ids:
  - CommunityMech:000173
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - A replacement term, if used, matches the demonstrated process rather than reactor
    jargon.
  - No complete ATP pathway is promoted from a speculative model.
  - Run term, strict and reference checks.
- action_id: fix-acid-anion
  description: Align preferred wording and chemical grounding, preserving the publication
    endpoint and assay context.
  finding_ids:
  - acid-anion
  target_ids:
  - CommunityMech:000173
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Every chemical descriptor denotes the same acid/base entity as its canonical term.
  - Do not infer unmeasured speciation from analytical product naming.
  - Run term and strict checks.
- action_id: fix-media-linkage
  description: Check exact source-compatible medium/ingredient identifiers in future
    curation; preserve modified formulations rather than asserting identity to an
    unmodified base recipe.
  finding_ids:
  - media-linkage
  target_ids:
  - CommunityMech:000173
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetobacterium_Clostridium_CO2_Electrolysis_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Any link resolves and matches the correct formulation/experiment.
  - Unavailable exact matches are left explicitly unresolved.
  - Run appropriate linkage, strict and evidence gates.
limitations:
- Three main articles were inspected; linked supplementary files and raw assay datasets
  were not reanalyzed. Discussion inspection focused on experimental interpretation
  and stated pathway limitations.
- Initial and follow-up producer/recipient controls remain distinct from coculture
  outcomes; no complete intracellular pathway, reciprocal benefit or lifecycle carbon
  balance was established by this review.
- Historical GTDB mapping counts and release provenance were not reconstructed; canonical
  labels and native coherence/domain gates pass.
- Optional adapter unavailable in the isolated runtime; public catalog fallback has
  no matching organism. Required corpus network gates retain unrelated warning failures.
- A potential Mendeley dataset is advertised in the 2023 article; external dataset
  availability was not verified and no dataset is newly assigned.
notes:
- No record, cache, history, generated product or scientific status changed. Proposed
  actions are future curation only.
- Every original inspected local input hash remains unchanged; external primary bodies
  have exact response hashes.
- Exact short quotations are shared across assessments and total at most 25 words
  per publication.
tags:
- record-review
- synthetic-coculture
- batch-02
```
