# Methylobacterium REE platform: source-scoped whole-record review

- Review: 20261019T233756Z-methylobacterium-ree-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-19T23:31:30.659610Z
- Finished UTC: 2026-10-19T23:37:56.327595Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Four nodes and two explicitly partial arrows retain experimental support. Five major findings concern environment and dysprosium grounding, functional role, non-graph operating claims, and product/scale extrapolation. Focused gates pass; unrelated corpus warning failures remain explicit.

## Scope And Provenance

Entire target including 4 nodes, 2 arrows, 9 environmental factors, engineering, taxonomy, claim evidence and history.

Selection: Fourth initially uncovered record path in the declared isolate/community corpus; one record per bundle, saved in path order by parent.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a4611c913c8da9619673df63a0c2cce3aa206a83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000322 | data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml | maintained | Methylobacterium REE E-waste Platform |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000322 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml |
| validate-strict | passed | True | CommunityMech:000322 | uv run python scripts/validate_strict.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml --out /private/tmp/cm-review-session/000322/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/000322/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000322 | ✅ Validation passed<br>uv run linkml-term-validator validate-data data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000322 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000322 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml |
| validate-history | passed | True | CommunityMech:000322 | No issues found |
| normalize-cache-names | passed | True | CommunityMech:000322 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000322 | Validating data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000322 | Same-session corpus execution: exit 1, 462 records, 57 warnings in 21 records, zeroerrors. No target-specific finding. Reused at unchanged Git base and record bytes, not rerun for this record. |
| check-network-quality | failed | True | CommunityMech:000322 | Same-session corpus execution: exit 1, 462 records, 57 warnings in 21 records, zeroerrors. No target-specific finding. Reused at unchanged Git base and record bytes, not rerun for this record. |
| iModulonDB organism coverage | not_applicable | False | CommunityMech:000322 | No matching organism in inspected public catalogue; no gene/module query is applicable. |

## Scientific And Domain Assessments

### Identity, experimental scope and source strata

identity: supported. Targets: CommunityMech:000322.

Stable identity is an engineered AM1 single-member platform with separately tested chemical and genetic interventions. The primary PMID/DOI and strain nomenclature align; no natural consortium is implied.

### Taxonomy, strain, functional role and abundance

grounding: concern. Targets: CommunityMech:000322.

Taxon and GTDB/domain gates pass; species nomenclature differs explicitly. AM1 and mutant details are central but not structured in strain_designation. Dominant monoculture representation is plausible;202 mg/g DW is loading, not abundance. PRIMARY_DEGRADER is unsupported by simple C1 growth and REE uptake evidence.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000322.

Citrate-Supplemented REE Leaching: supplied reagent -&gt; greater abiotic leaching and cellular accumulation; no secreting source or recipient taxon asserted. 5/15 mM citrate, 55 mM gluconate and 5 mM oxalate are distinguished. The description preserves concentration/scale limitations and total REE rather than Nd-only values.

### ecological_interactions[1]

graph: concern. Targets: CommunityMech:000322.

Lanthanophore-Mediated REE Bioaccumulation: AM1 delta-mxaF/pAZ1 mll expression -&gt; increased cellular Nd/Pr/Dy, compared with delta-mxaF.80/15/8 mg/g DW are supported and assay-specific. Biological direction is sound; dysprosium(3+) preferred wording is incorrectly grounded to an atom.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000322.

Polyphosphate Granule REE Sequestration: AM1 ppx deletion -&gt; higher Nd accumulation, 202 mg/g DW relative to its assay comparator. Storage context and exopolyphosphatase mechanism are supported; no irreversible retention, covalent bonding or rescue is claimed. Exact ppx construction remains supplement-limited.

### ecological_interactions[3]

graph: supported. Targets: CommunityMech:000322.

Methanol-Powered REE Acquisition Metabolism: AM1 delta-mxaF deletion -&gt; REE dependency for methanol growth through alternative dehydrogenases. The record correctly avoids obligate wild-type REE dependence and an unmeasured uptake-energy gradient.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000322.

Direction: citrate-associated supply -&gt; lanthanophore-associated accumulation node. The source measures increased leaching and uptake but does not isolate mll mediation of the citrate increment. The edge explicitly says PARTIAL and states that limit; this review supports the qualified representation, not fully established mediation.

### ecological_interactions[1].downstream[0]

graph: supported. Targets: CommunityMech:000322.

Direction: uptake -&gt; polyphosphate storage. Separate mll and ppx perturbations and storage context support a proposed relationship; no traced mll-delivered metal or combined mediation is established. Existing PARTIAL wording correctly preserves uncertainty.

### Entire graph and discussion references

graph: supported. Targets: CommunityMech:000322.

All 4 nodes and 2 arrows were assessed, including their participants, metabolite/process descriptors and all 6 direct EvidenceItems. Arrow targets and all 4 discussion anchors resolve. No interspecies mechanism or extra causal arrow was inferred.

### engineering_design

evidence: concern. Targets: CommunityMech:000322.

Platform objective and deliberate monoculture representation are supported. The cited organic-acid sentence does not demonstrate member persistence tracking or pH/temperature perturbation designs: those reported values are fixed operating setpoints. Growth curves support growth/biomass measurements but do not establish the separate persistence endpoint.

### environment_term

grounding: concern. Targets: CommunityMech:000322.

The ontology ID/label pair is valid but denotes contaminated soil; controlled liquid culture with supplied magnet swarf is not soil. Notes correctly say engineered conditions while retaining contradictory gluconate-leaching and broader feedstock wording.

### environmental_factors[0]: pH

evidence: concern. Targets: CommunityMech:000322.

pH 6.9 and 1 M NaOH control are measured Methods conditions. The attached snippet does not establish a physiological optimum, elimination of corrosion or comparative energy/waste benefits.

### environmental_factors[1]: Temperature

evidence: concern. Targets: CommunityMech:000322.

29.5 C bioreactor setting and 29-30 C routine cultivation are supported. An optimum and energy/economic advantages are not measured by this temperature statement.

### environmental_factors[2]: Bioreactor Scale

evidence: concern. Targets: CommunityMech:000322.

10 L demonstration is supported; successful pilot 100-1000 L or industrial &gt;10, 000 L scaling and commercial feasibility are not demonstrated. Keep strain/condition-specific loading separate.

### environmental_factors[3]: Medium Composition

evidence: concern. Targets: CommunityMech:000322.

HyphoMOD phosphate recipe and methanol support are established; reduced phosphate improves growth/uptake. Characterizing gluconate as an effective REE leaching additive conflicts with the tested negative result. Routine succinate precultures and methanol REE assays should be distinguished.

### environmental_factors[4]: REE Bioaccumulation Capacity

evidence: supported. Targets: CommunityMech:000322.

202 mg Nd/g DW and approximately 5.5-fold increase are supported for the separate ppx test and its comparison; they are not the 10 L baseline yield.

### environmental_factors[5]: REE Selectivity and Purity

evidence: concern. Targets: CommunityMech:000322.

98% REE and the source-reported 96.8%Nd refer to measured cellular metals in a particular batch culture. They do not establish magnet-grade metal, no further purification, or mll-mediated selectivity in that experiment.

### environmental_factors[6]: Substrate E-waste Composition

evidence: concern. Targets: CommunityMech:000322.

NdFeB magnet swarf is supported. Source measurements are 68%Fe, 26.7%Nd, 4.35%Pr, 3.34%Dy; prose gives~1%Dy. Phosphor powder processing and universal substrate performance are not established by the inspected experiment; other ores/smartphones are discussed as growth sources.

### environmental_factors[7]: Citrate Leaching Efficiency

evidence: concern. Targets: CommunityMech:000322.

5/15 mM citrate chemical leaching gives 8.2/58.7 ppm total REE after 28 h, supported. Biological uptake is condition-specific and 15 mM inhibits 100 mL growth; comparative economic/environmental claims are not measured by the leaching endpoint.

### environmental_factors[8]: Genetic Engineering Strategy

evidence: supported. Targets: CommunityMech:000322.

ppx deletion is directly linked to 202 mg/g DW and~5.5-fold increase. Existing wording does not assert an unverified double mutant, retention kinetics or combined mll phenotype.

### Structured growth conditions and external resources

completeness: concern. Targets: CommunityMech:000322.

All target bytes were inspected: growth_media, cultivation_setup, associated_datasets and external_resources blocks are not populated. Detailed Methods provide actionable source-backed cultivation information; current environmental-factor prose is not a fully normalized condition-specific protocol. Optional omissions are not schema failures.

### History and unresolved scientific questions

provenance: supported. Targets: CommunityMech:000322.

Two append-only history events, embedded events and prior graph decisions agree. The current discussion appropriately distinguishes separate interventions and unproven combined mediation. This review extends to non-graph claims without changing history, closing the discussion or claiming an earlier structured finding was resolved.

### Structured transcriptomic-source applicability

evidence: not_applicable. Targets: CommunityMech:000322.

The inspected 20 organism public iModulonDB catalogue contains no matching Methylobacterium/Methylorubrum dataset. No related-organism module was substituted for gene or phenotype support.

### Focused validators and corpus scope

schema: supported. Targets: CommunityMech:000322.

Focused schema, strict, terms, references, GTDB coherence/domain and history pass with no ontology skips. Cited cache bytes remain unchanged. Corpus network failures are retained as unrelated warnings; validation does not substantiate the scientific claims.

### Native completeness and validation quality

completeness: concern. Targets: CommunityMech:000322.

Completeness 80 and validation quality 80 do not establish scientific correctness; five major findings remain. Native participant/reference network has no target finding, even though two mechanistic arrows correctly remain partial.

## Findings

### soil-environment-misgrounding: Contaminated-soil grounding contradicts the engineered study setting

major / open / confirmed; issue key: CommunityMech.000322.soil-environment-misgrounding.

ENVO:00002116 requires soil, whereas source experiments use controlled liquid cultures with magnet swarf. A correct canonical label cannot validate the biological setting.

### dysprosium-chemical-identity: Dysprosium cation is represented by an atom ontology class

major / open / confirmed; issue key: CommunityMech.000322.dysprosium-chemical-identity.

The preferred term asserts dysprosium(3+) but CHEBI:33377 is dysprosium atom, not a parent of the cation. The note acknowledges that distinction and selects the atom for enum/export consistency; consistency does not establish chemical identity.

### functional-role-mismatch: Primary-degrader role is not supported by methanol growth and REE uptake

major / open / confirmed; issue key: CommunityMech.000322.functional-role-mismatch.

PRIMARY_DEGRADER means degradation of complex substrates. The demonstrated processes are methylotrophic growth, chemical leaching and metal accumulation; these do not by themselves show degradation of a complex substrate.

### operating-and-engineering-claims: Non-graph operating and engineering claims exceed or conflict with measured conditions

major / open / confirmed; issue key: CommunityMech.000322.operating-and-engineering-claims.

Outside the corrected graph, gluconate is presented as promoting REE leaching despite the negative result; fixed pH/temperature settings become a perturbation design or optimum; persistence is an unsupported endpoint; substrate composition gives~1%Dy versus measured 3.34%. Broader feedstock and economic/physiological assertions lack claim-specific evidence in the inspected source.

### product-purity-and-scale-overstatement: Cellular composition and laboratory scale are inflated to commercial product performance

major / open / confirmed; issue key: CommunityMech.000322.product-purity-and-scale-overstatement.

Measured cellular-metal selectivity is described as magnet-grade product purity eliminating downstream purification. 10 L proof of principle becomes industrial feasibility and larger-scale performance; high ppx/mll shake-flask yields and selectivity from other conditions are presented as integrated strain attributes. The paper explicitly leaves end-to-end rare-earth oxide production to future work.

## Recommended Actions And Acceptance Checks

### fix-soil-environment-misgrounding

Ground the physical culture environment to a verified source-compatible class and retain waste feedstock separately.

- Verify replacement ID, label and definition against the actual setting.
- Run focused terms/strict validation and inspect rendered environment after separately authorized curation.

### fix-dysprosium-chemical-identity

Use a source-appropriate chemical identity and verify its ontology semantics. Trace downstream enum/extraction/export assumptions before changing the mapping; coordinate separately authorized maintained schema/export changes if needed.

- No 3+ cation is asserted as an atom or falsely called its child.
- Verify any broader molecular-entity mapping and preserve explicit measurement/speciation limits.
- Recheck all consumers named in the existing note, ontology validation and affected KG exports after authorized implementation.

### fix-functional-role-mismatch

Remove or replace the unsupported role using an evidenced biological function and schema meaning.

- Do not infer complex-substrate degradation from metal leaching or growth on methanol.
- Any replacement role has exact source support and passes strict/network gates.

### fix-operating-and-engineering-claims

Reconcile all descriptive and condition fields with exact assay contexts; preserve negatives, fixed-setpoint distinctions and measured composition, and remove or separately substantiate extrapolations.

- All 9 environmental factors retain exact strain, medium, scale and endpoint context.
- Gluconate is not said to enhance REE leaching in the tested condition.
- Growth observations are not relabeled persistence, and fixed setpoints are not a tested optimum or perturbation series.
- Run source/snippet, strict and term checks after separately authorized curation.

### fix-product-purity-and-scale-overstatement

Keep measured cell-associated metal proportions separate from recovered-product purity, and distinguish each genotype/scale result from proposed integration or commercialization.

- No magnet-grade metal or elimination of downstream purification is claimed without a demonstrated product-analysis source.
- 10 L demonstration, baseline 3.2 mg/g, mll 80 mg/g and ppx 202 mg/g remain tied to their own contexts.
- Pilot/industrial scale and commercial feasibility are explicitly prospective or removed.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml; Entire maintained YAML; four interaction nodes, two downstream arrows, nine environmental factors, taxonomy, engineering, discussion and embedded history | supports | Engineered AM1 platform with distinct chemical/genetic perturbation studies. Graph prose limits causal interpretation, while surrounding claims overstate physiological and commercial conclusions. |
| article | PMID:38150661; DOI:10.1021/acs.est.3c06775; entire article body in references_cache/PMID_38150661.txt, including Methods, Results, Figures1-8, Table1 and Environmental Implications | supports | Full article text was inspected. PubMed primary metadata independently resolves PMID, PMCID:PMC10785750, DOI, title and figure captions. The published study is a proof of principle for AM1 recovery from solid feedstocks; supplements were not retrieved. |
| pubmed | https://pubmed.ncbi.nlm.nih.gov/38150661/; Bibliographic metadata, abstract and Figures1-8 captions | supports | PMID:38150661 and DOI:10.1021/acs.est. 3 c 06775 correspond to the named primary study, published January 2024 with December 2023 online date. Online figure captions preserve delta-mxaF/pAZ1 and ppx experimental distinctions. |
| methods | PMID:38150661; Cached article lines182-279: Bacterial Strains and Growth Conditions, Growth Analysis with Organic Acids, Bioreactor Cultivation, Metal Quantification and Mutagenesis | supports | All growth studies used AM1 delta-mxaF. Succinate precultures differ from methanol/REE assays. HyphoMOD contains reduced phosphate; bioreactor setpoints were 29.5 C, pH 6.9, 500 rpm, 200-2000 sccm. Acid digestion/ICP-MS measures biomass-associated metals; exact ppx construction is delegated to the supplement. |
| scale | PMID:38150661; Cached article Table1 and Results Scalable REE Bioleaching, lines279-345; Environmental Implications lines578-598 | refutes | Baseline 3.2 mg Nd/g DW differs from HyphoMOD/10 L endpoints; Table 1 gives 10 L13.2 mg Nd/g DW. The authors describe end-to-end oxide products as future work and report the high-engineering-loading potential separately. |
| selectivity | PMID:38150661; Cached article Selective Bioaccumulation, lines345-401; Figure3B | supports | Measured cellular metal composition in 0.75 L cultures was 98% REE with the source-described 96.8%Nd selectivity. This is not analysis of a purified magnet-grade product. Swarf measured 68.0%Fe, 26.7%Nd, 4.35%Pr, 3.34%Dy. |
| organic-acids | PMID:38150661; Cached article Chemical Strategies, lines405-485; Figures4-5 and referenced TablesS1/S3 | supports | Supplied citrate increases nonspecific leaching;55 mM gluconate and 5 mM oxalate did not increaseREE leaching. 5 mMand 15 mM citrate have different uptake effects;15 mM inhibited growth upon 100 mL scale-up. Numbers 58.7 ppm and 8.2 ppm denote total REE in chemical leachate, not Nd-only recovery. |
| genetics | PMID:38150661; Cached article Approaches for Enhanced REE-Specific Bioleaching, lines510-574; Figure7A-B | supports | Separate mll expression and ppx deletion experiments increase uptake. Figure 7 A compares delta-mxaF with delta-mxaF/pAZ1; Figure 7 B compares delta-mxaF and delta-ppx. 80 mg Nd/g DW and 202 mg Nd/g DW are shake-flask genetic endpoints, not one demonstrated combined 10 L strain. |
| citrate-quote | PMID:38150661; Chemical Strategies/Figure5; exact excerpt from inspected article | supports | Exact short excerpt; interpretation retains its assay/strain context. |
| mll-quote | PMID:38150661; Approaches for Enhanced REE-Specific Bioleaching/Figure7A; exact excerpt from inspected article | supports | Exact short excerpt; interpretation retains its assay/strain context. |
| ppx-quote | PMID:38150661; Abstract and ppx results/Figure7B; exact excerpt from inspected article | supports | Exact short excerpt; interpretation retains its assay/strain context. |
| mxaF-quote | PMID:38150661; Methods/Bacterial Strains and Growth Conditions; exact excerpt from inspected article | supports | Exact short excerpt; interpretation retains its assay/strain context. |
| ontology | OAK SemanticSQL ENVO and CHEBI local adapters; ENVO:00002116, CHEBI:33377 and CHEBI:37295 labels/definitions; extracted query results hashed separately | refutes | ENVO:00002116 denotes contaminated soil; its definition requires soil. CHEBI:33377 is dysprosium atom;37295 is dysprosium molecular entity. An atom does not denote a 3+ cation. The record itself acknowledges that the chosen atom does not subsume its preferred cation. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum.PRIMARY_DEGRADER; TaxonomicComposition.strain_designation; environment_term/modeled_environment | supports | PRIMARY_DEGRADER means degradation of complex substrates. Methanol growth and metal-ion uptake do not alone demonstrate that role. The schema supports explicit strain and genetic modification context and distinguishes physical study setting from modeled environment. |
| history | history/records/Methylobacterium_REE_Ewaste_Platform; Both append-only events, embedded curation_history and matching target row in reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml | supports | The earlier graph repair explicitly excluded non-graph environmental/commercial claims and unread ppx supplement. Its bounded graph decisions and current knowledge-gap discussion agree. |
| local-search | CommunityMech:000322; Ignored-inclusive search for exact slug and Methylobacterium/Methylorubrum extorquens/NCBITaxon408 in kb/taxa, target history and prior graph decision | context_only | Target identity and two history records are resolved. No matching reusable taxon entry was returned in the explicitly searched kb/taxa files; no external absence is inferred. |
| imodulondb | https://imodulondb.org/api/datasets; Same-session public catalogue response, all20 organisms/28 datasets, independently inspected for this target | context_only | No Methylobacterium or Methylorubrum organism is in the fetched catalogue. No applicable gene/module search exists for this target in that bounded response; absence is not negative biological evidence. |
| check-validate | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml; Actual command output; start 2026-10-19T23:31:38.504210+00:00; finish 2026-10-19T23:31:42.954964+00:00 | context_only | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml |
| check-validate-strict | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-strict data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml --out /private/tmp/cm-review-session/000322/strict-report.tsv; Actual command output; start 2026-10-19T23:31:38.507249+00:00; finish 2026-10-19T23:31:46.151394+00:00 | context_only | uv run python scripts/validate_strict.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml --out /private/tmp/cm-review-session/000322/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/000322/strict-report.tsv |
| check-validate-terms | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-terms data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml; Actual command output; start 2026-10-19T23:31:38.511429+00:00; finish 2026-10-19T23:31:45.265354+00:00 | context_only | ✅ Validation passed<br>uv run linkml-term-validator validate-data data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-gtdb data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml; Actual command output; start 2026-10-19T23:31:42.955847+00:00; finish 2026-10-19T23:31:43.230634+00:00 | context_only | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-gtdb-domain data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml; Actual command output; start 2026-10-19T23:31:43.231172+00:00; finish 2026-10-19T23:31:46.351855+00:00 | context_only | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml |
| check-validate-history | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-history history/records/Methylobacterium_REE_Ewaste_Platform; Actual command output; start 2026-10-19T23:31:45.265654+00:00; finish 2026-10-19T23:31:46.524146+00:00 | context_only | No issues found |
| check-normalize-cache-names | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true uv run python scripts/normalize_cache_names.py --check; Actual command output; start 2026-10-19T23:31:46.524704+00:00; finish 2026-10-19T23:31:46.624733+00:00 | context_only | Command completed without reported issues. |
| check-validate-references-explained | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-references-explained data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml; Actual command output; start 2026-10-19T23:31:46.625378+00:00; finish 2026-10-19T23:31:49.276882+00:00 | context_only | Validating data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | just --no-dotenv audit-network; Complete corpus output, executed 2026-10-19T07:30:27.845593+00:00 | context_only | Same-session corpus execution: exit 1, 462 records, 57 warnings in 21 records, zeroerrors. No target-specific finding. Reused at unchanged Git base and record bytes, not rerun for this record. |
| check-check-network-quality | just --no-dotenv check-network-quality; Complete corpus output, executed 2026-10-19T07:30:43.193891+00:00 | context_only | Same-session corpus execution: exit 1, 462 records, 57 warnings in 21 records, zeroerrors. No target-specific finding. Reused at unchanged Git base and record bytes, not rerun for this record. |

## Limits And Additional Notes

- The primary article full text was assessed through the committed EuropePMC-derived cache; PubMed metadata/abstract/figure captions were independently inspected online. Supplemental Methods were not retrieved, so exact ppx construction remains limited.
- No independent reconstruction of the historical 42-genome GTDB mapping was attempted; documented validators cover canonical terms, coherence and domain.
- Corpus network checks failed on warnings elsewhere; no target finding was found. Required failures are explicit and the verdict is needs_curation.
- Local ontology meanings use available SemanticSQL snapshots. Dysprosium mapping needs chemically correct semantics and coordinated consumer review, not a new nearby identifier assumed equivalent.
- The review did not author/edit the record during this session; earlier curation shares the codex identity, so person-level reviewer independence is unknown.
- No canonical record, cache, history, generated product or scientific status was changed. Proposed curation remains separate authorized work.
- No current issue-tracker disposition is inferred from historical links; no paid provider or outbound communication was used.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233756Z-methylobacterium-ree-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Methylobacterium REE platform: source-scoped whole-record review'
started_at: '2026-10-19T23:31:30.659610Z'
finished_at: '2026-10-19T23:37:56.327595Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: The review did not author/edit the record during this session;
    earlier curation shares the codex identity, so person-level reviewer independence
    is unknown.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Four nodes and two explicitly partial arrows retain experimental support.
  Five major findings concern environment and dysprosium grounding, functional role,
  non-graph operating claims, and product/scale extrapolation. Focused gates pass;
  unrelated corpus warning failures remain explicit.
source:
  git_revision: a4611c913c8da9619673df63a0c2cce3aa206a83
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/evidence-curation/SKILL.md
    sha256: 5c5e3c62dc733c762afbf790b270b978b5c523930dbe6c74a88beda81007f396
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
  - path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    sha256: 70d9761a556a3e744eb81c26f1906bb0ce697b3d64be526ecaafddea7404f978
    role: target
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/Methylobacterium_REE_Ewaste_Platform/2026-10-02T045300Z-codex-68c801.yaml
    sha256: c59dd7ec198cefc89c8cbfc7b37d7716cd619248554dd37dd1e04262f4a3f0fa
    role: context
  - path: history/records/Methylobacterium_REE_Ewaste_Platform/2026-10-05T071441Z-codex-ba09e4.yaml
    sha256: 3108e184702daf68c070ef6613661b1d027c7437d2845b5ffe89b41850c4d09b
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: references_cache/PMID_38150661.txt
    sha256: 4217f047487f44565514f5233ebca2fc656245f3356588f3bf66ae58d2f8a272
    role: context
  - path: reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml
    sha256: 3e0877c63e94f1c87d6c78b6d5480a0be07d80f1cd18f8db5efda4e8e2ea4d26
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
- target_id: CommunityMech:000322
  path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  label: Methylobacterium REE E-waste Platform
  record_class: MicrobialCommunity
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
scope:
  description: Entire target including 4 nodes, 2 arrows, 9 environmental factors,
    engineering, taxonomy, claim evidence and history.
  selection: Fourth initially uncovered record path in the declared isolate/community
    corpus; one record per bundle, saved in path order by parent.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000322
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml'
  target_ids:
  - CommunityMech:000322
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history directory; normalization is a read-only corpus
    cache-name check. Offline uv environment, no dependency fetch.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml\
    \ --out /private/tmp/cm-review-session/000322/strict-report.tsv\nValidating 1\
    \ files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/000322/strict-report.tsv"
  target_ids:
  - CommunityMech:000322
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-strict data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    --out /private/tmp/cm-review-session/000322/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history directory; normalization is a read-only corpus
    cache-name check. Offline uv environment, no dependency fetch.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000322
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-terms data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history directory; normalization is a read-only corpus
    cache-name check. Offline uv environment, no dependency fetch.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000322
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history directory; normalization is a read-only corpus
    cache-name check. Offline uv environment, no dependency fetch.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml'
  target_ids:
  - CommunityMech:000322
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb-domain data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history directory; normalization is a read-only corpus
    cache-name check. Offline uv environment, no dependency fetch.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: No issues found
  target_ids:
  - CommunityMech:000322
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-history history/records/Methylobacterium_REE_Ewaste_Platform
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history directory; normalization is a read-only corpus
    cache-name check. Offline uv environment, no dependency fetch.
- check_id: normalize-cache-names
  name: normalize-cache-names
  status: passed
  required: true
  summary: Command completed without reported issues.
  target_ids:
  - CommunityMech:000322
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names
  scope_note: Focused target/history directory; normalization is a read-only corpus
    cache-name check. Offline uv environment, no dependency fetch.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: "Validating data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml against\
    \ schema src/communitymech/schema/communitymech.yaml\nCache directory: references_cache\n\
    \nValidation Summary:\n  Reported validation issues: 0\n  All validations passed!\n\
    \n[annotate] This is not a count of checked excerpts (#1469). Native Discussion\
    \ evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000322
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-references-explained data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history directory; normalization is a read-only corpus
    cache-name check. Offline uv environment, no dependency fetch.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Same-session corpus execution: exit 1, 462 records, 57 warnings in 21
    records, zeroerrors. No target-specific finding. Reused at unchanged Git base
    and record bytes, not rerun for this record.'
  target_ids:
  - CommunityMech:000322
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Complete corpus; warnings elsewhere are not attributed to selected record.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Same-session corpus execution: exit 1, 462 records, 57 warnings in 21
    records, zeroerrors. No target-specific finding. Reused at unchanged Git base
    and record bytes, not rerun for this record.'
  target_ids:
  - CommunityMech:000322
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Complete corpus; warnings elsewhere are not attributed to selected record.
- check_id: imodulondb-applicability
  name: iModulonDB organism coverage
  status: not_applicable
  required: false
  summary: No matching organism in inspected public catalogue; no gene/module query
    is applicable.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - imodulondb
evidence:
- evidence_id: record
  kind: record_content
  reference: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  locator: Entire maintained YAML; four interaction nodes, two downstream arrows,
    nine environmental factors, taxonomy, engineering, discussion and embedded history
  summary: Engineered AM1 platform with distinct chemical/genetic perturbation studies.
    Graph prose limits causal interpretation, while surrounding claims overstate physiological
    and commercial conclusions.
  support: supports
  accessed_at: '2026-10-19T23:36:33.761696Z'
- evidence_id: article
  kind: primary_source
  reference: PMID:38150661
  locator: DOI:10.1021/acs.est.3c06775; entire article body in references_cache/PMID_38150661.txt,
    including Methods, Results, Figures1-8, Table1 and Environmental Implications
  summary: Full article text was inspected. PubMed primary metadata independently
    resolves PMID, PMCID:PMC10785750, DOI, title and figure captions. The published
    study is a proof of principle for AM1 recovery from solid feedstocks; supplements
    were not retrieved.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762156Z'
- evidence_id: pubmed
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/38150661/
  locator: Bibliographic metadata, abstract and Figures1-8 captions
  summary: PMID:38150661 and DOI:10.1021/acs.est. 3 c 06775 correspond to the named
    primary study, published January 2024 with December 2023 online date. Online figure
    captions preserve delta-mxaF/pAZ1 and ppx experimental distinctions.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762159Z'
- evidence_id: methods
  kind: primary_source
  reference: PMID:38150661
  locator: 'Cached article lines182-279: Bacterial Strains and Growth Conditions,
    Growth Analysis with Organic Acids, Bioreactor Cultivation, Metal Quantification
    and Mutagenesis'
  summary: All growth studies used AM1 delta-mxaF. Succinate precultures differ from
    methanol/REE assays. HyphoMOD contains reduced phosphate; bioreactor setpoints
    were 29.5 C, pH 6.9, 500 rpm, 200-2000 sccm. Acid digestion/ICP-MS measures biomass-associated
    metals; exact ppx construction is delegated to the supplement.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762160Z'
- evidence_id: scale
  kind: primary_source
  reference: PMID:38150661
  locator: Cached article Table1 and Results Scalable REE Bioleaching, lines279-345;
    Environmental Implications lines578-598
  summary: Baseline 3.2 mg Nd/g DW differs from HyphoMOD/10 L endpoints; Table 1 gives
    10 L13.2 mg Nd/g DW. The authors describe end-to-end oxide products as future
    work and report the high-engineering-loading potential separately.
  support: refutes
  accessed_at: '2026-10-19T23:36:33.762162Z'
- evidence_id: selectivity
  kind: primary_source
  reference: PMID:38150661
  locator: Cached article Selective Bioaccumulation, lines345-401; Figure3B
  summary: Measured cellular metal composition in 0.75 L cultures was 98% REE with
    the source-described 96.8%Nd selectivity. This is not analysis of a purified magnet-grade
    product. Swarf measured 68.0%Fe, 26.7%Nd, 4.35%Pr, 3.34%Dy.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762163Z'
- evidence_id: organic-acids
  kind: primary_source
  reference: PMID:38150661
  locator: Cached article Chemical Strategies, lines405-485; Figures4-5 and referenced
    TablesS1/S3
  summary: Supplied citrate increases nonspecific leaching;55 mM gluconate and 5 mM
    oxalate did not increaseREE leaching. 5 mMand 15 mM citrate have different uptake
    effects;15 mM inhibited growth upon 100 mL scale-up. Numbers 58.7 ppm and 8.2
    ppm denote total REE in chemical leachate, not Nd-only recovery.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762164Z'
- evidence_id: genetics
  kind: primary_source
  reference: PMID:38150661
  locator: Cached article Approaches for Enhanced REE-Specific Bioleaching, lines510-574;
    Figure7A-B
  summary: Separate mll expression and ppx deletion experiments increase uptake. Figure
    7 A compares delta-mxaF with delta-mxaF/pAZ1; Figure 7 B compares delta-mxaF and
    delta-ppx. 80 mg Nd/g DW and 202 mg Nd/g DW are shake-flask genetic endpoints,
    not one demonstrated combined 10 L strain.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762165Z'
- evidence_id: citrate-quote
  kind: primary_source
  reference: PMID:38150661
  locator: Chemical Strategies/Figure5; exact excerpt from inspected article
  summary: Exact short excerpt; interpretation retains its assay/strain context.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762172Z'
  quote: addition of citrate greatly improved REE leaching
- evidence_id: mll-quote
  kind: primary_source
  reference: PMID:38150661
  locator: Approaches for Enhanced REE-Specific Bioleaching/Figure7A; exact excerpt
    from inspected article
  summary: Exact short excerpt; interpretation retains its assay/strain context.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762174Z'
  quote: accumulation increased by more than 3-fold
- evidence_id: ppx-quote
  kind: primary_source
  reference: PMID:38150661
  locator: Abstract and ppx results/Figure7B; exact excerpt from inspected article
  summary: Exact short excerpt; interpretation retains its assay/strain context.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762175Z'
  quote: activity increases metal accumulation
- evidence_id: mxaF-quote
  kind: primary_source
  reference: PMID:38150661
  locator: Methods/Bacterial Strains and Growth Conditions; exact excerpt from inspected
    article
  summary: Exact short excerpt; interpretation retains its assay/strain context.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762176Z'
  quote: ensures REE dependency
- evidence_id: ontology
  kind: authority
  reference: OAK SemanticSQL ENVO and CHEBI local adapters
  locator: ENVO:00002116, CHEBI:33377 and CHEBI:37295 labels/definitions; extracted
    query results hashed separately
  summary: ENVO:00002116 denotes contaminated soil; its definition requires soil.
    CHEBI:33377 is dysprosium atom;37295 is dysprosium molecular entity. An atom does
    not denote a 3+ cation. The record itself acknowledges that the chosen atom does
    not subsume its preferred cation.
  support: refutes
  accessed_at: '2026-10-19T23:32:25.683285Z'
  snapshot_sha256: 87781b539fced37a83c3746340718f0c30f168171fe59674fef812ca0774ec97
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum.PRIMARY_DEGRADER; TaxonomicComposition.strain_designation;
    environment_term/modeled_environment
  summary: PRIMARY_DEGRADER means degradation of complex substrates. Methanol growth
    and metal-ion uptake do not alone demonstrate that role. The schema supports explicit
    strain and genetic modification context and distinguishes physical study setting
    from modeled environment.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762793Z'
- evidence_id: history
  kind: record_content
  reference: history/records/Methylobacterium_REE_Ewaste_Platform
  locator: Both append-only events, embedded curation_history and matching target
    row in reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml
  summary: The earlier graph repair explicitly excluded non-graph environmental/commercial
    claims and unread ppx supplement. Its bounded graph decisions and current knowledge-gap
    discussion agree.
  support: supports
  accessed_at: '2026-10-19T23:36:33.762796Z'
- evidence_id: local-search
  kind: search
  reference: CommunityMech:000322
  locator: Ignored-inclusive search for exact slug and Methylobacterium/Methylorubrum
    extorquens/NCBITaxon408 in kb/taxa, target history and prior graph decision
  summary: Target identity and two history records are resolved. No matching reusable
    taxon entry was returned in the explicitly searched kb/taxa files; no external
    absence is inferred.
  support: context_only
  accessed_at: '2026-10-19T23:36:33.762798Z'
  search_scope: rg --no-ignore --hidden in kb/taxa, history/records/Methylobacterium_REE_Ewaste_Platform
    and reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml; all
    target bytes also read.
- evidence_id: imodulondb
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Same-session public catalogue response, all20 organisms/28 datasets, independently
    inspected for this target
  summary: No Methylobacterium or Methylorubrum organism is in the fetched catalogue.
    No applicable gene/module search exists for this target in that bounded response;
    absence is not negative biological evidence.
  support: context_only
  accessed_at: '2026-10-19T23:31:07.726770Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: check-validate
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  locator: Actual command output; start 2026-10-19T23:31:38.504210+00:00; finish 2026-10-19T23:31:42.954964+00:00
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml'
  support: context_only
  accessed_at: '2026-10-19T23:31:42.954964Z'
  snapshot_sha256: e7ccbd040d5a1d8fc3759f35a8cd660e74ea1cb1542bda6c7cab1de1abd912ca
- evidence_id: check-validate-strict
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-strict data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    --out /private/tmp/cm-review-session/000322/strict-report.tsv
  locator: Actual command output; start 2026-10-19T23:31:38.507249+00:00; finish 2026-10-19T23:31:46.151394+00:00
  summary: "uv run python scripts/validate_strict.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml\
    \ --out /private/tmp/cm-review-session/000322/strict-report.tsv\nValidating 1\
    \ files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/000322/strict-report.tsv"
  support: context_only
  accessed_at: '2026-10-19T23:31:46.151394Z'
  snapshot_sha256: fabc8f9ec6dccb69bb2346219e9bdfda3be826afcf75cb8213e3e12dfbed8154
- evidence_id: check-validate-terms
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-terms data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  locator: Actual command output; start 2026-10-19T23:31:38.511429+00:00; finish 2026-10-19T23:31:45.265354+00:00
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: context_only
  accessed_at: '2026-10-19T23:31:45.265354Z'
  snapshot_sha256: 37427f9459a2fad9f59f23d09e9c78889b2ed4570aef79160ad6c9082c152dee
- evidence_id: check-validate-gtdb
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  locator: Actual command output; start 2026-10-19T23:31:42.955847+00:00; finish 2026-10-19T23:31:43.230634+00:00
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: context_only
  accessed_at: '2026-10-19T23:31:43.230634Z'
  snapshot_sha256: 59376bf1ad177ac6de8198f5f96e174ea90e3f3993ec208e095582fac84206b3
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb-domain data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  locator: Actual command output; start 2026-10-19T23:31:43.231172+00:00; finish 2026-10-19T23:31:46.351855+00:00
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml'
  support: context_only
  accessed_at: '2026-10-19T23:31:46.351855Z'
  snapshot_sha256: 32ab58daa72fd1b22d87fb0f3c7a77d01f8ebab1934e5231dc71278c83ecc3ae
- evidence_id: check-validate-history
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-history history/records/Methylobacterium_REE_Ewaste_Platform
  locator: Actual command output; start 2026-10-19T23:31:45.265654+00:00; finish 2026-10-19T23:31:46.524146+00:00
  summary: No issues found
  support: context_only
  accessed_at: '2026-10-19T23:31:46.524146Z'
  snapshot_sha256: a2536e66eca96bec5253181694df781977adb744456f422c976352e98ee3c502
- evidence_id: check-normalize-cache-names
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true uv run python scripts/normalize_cache_names.py --check
  locator: Actual command output; start 2026-10-19T23:31:46.524704+00:00; finish 2026-10-19T23:31:46.624733+00:00
  summary: Command completed without reported issues.
  support: context_only
  accessed_at: '2026-10-19T23:31:46.624733Z'
  snapshot_sha256: f9cfe4d6cebcf83e317c180c901fcb2a75bca0cd7f23b3ed4393d5a688eefb3b
- evidence_id: check-validate-references-explained
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-references-explained data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
  locator: Actual command output; start 2026-10-19T23:31:46.625378+00:00; finish 2026-10-19T23:31:49.276882+00:00
  summary: "Validating data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml against\
    \ schema src/communitymech/schema/communitymech.yaml\nCache directory: references_cache\n\
    \nValidation Summary:\n  Reported validation issues: 0\n  All validations passed!\n\
    \n[annotate] This is not a count of checked excerpts (#1469). Native Discussion\
    \ evidence coverage remains incomplete (#476)."
  support: context_only
  accessed_at: '2026-10-19T23:31:49.276882Z'
  snapshot_sha256: 71b25fb8d91eee7469dc74764cc559f2e09a046f8a2e5cb750ddf364ee3abd02
- evidence_id: check-audit-network
  kind: validation
  reference: just --no-dotenv audit-network
  locator: Complete corpus output, executed 2026-10-19T07:30:27.845593+00:00
  summary: 'Same-session corpus execution: exit 1, 462 records, 57 warnings in 21
    records, zeroerrors. No target-specific finding. Reused at unchanged Git base
    and record bytes, not rerun for this record.'
  support: context_only
  accessed_at: '2026-10-19T07:30:27.845593Z'
  snapshot_sha256: bedf3fd18a964bda429f7c6b5feb01b8918e1440b48a4329664501161c80e3f4
- evidence_id: check-check-network-quality
  kind: validation
  reference: just --no-dotenv check-network-quality
  locator: Complete corpus output, executed 2026-10-19T07:30:43.193891+00:00
  summary: 'Same-session corpus execution: exit 1, 462 records, 57 warnings in 21
    records, zeroerrors. No target-specific finding. Reused at unchanged Git base
    and record bytes, not rerun for this record.'
  support: context_only
  accessed_at: '2026-10-19T07:30:43.193891Z'
  snapshot_sha256: 885e62e84ed8d3e69a6e5ef5be43f941ef64d756107c3b062846831f76e081aa
assessments:
- assessment_id: identity
  area: identity
  topic: Identity, experimental scope and source strata
  outcome: supported
  summary: Stable identity is an engineered AM1 single-member platform with separately
    tested chemical and genetic interventions. The primary PMID/DOI and strain nomenclature
    align; no natural consortium is implied.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - article
  - pubmed
  - methods
  dimensions:
  - name: source_strain
    value: M. extorquens AM1 delta-mxaF; mll test delta-mxaF/pAZ1; ppx mutant separately
      tested
    definition: Genotypes are condition-specific; unread supplement prevents asserting
      an unverified combined mutant.
    evidence_ids:
    - methods
    - genetics
  - name: taxon_rank
    value: Species NCBITaxon 408; AM1 named in prose
    definition: The current term label is Methylorubrum extorquens; GTDB uses Methylobacterium
      extorquens. Canonical validators accept this explicitly represented naming difference.
    evidence_ids:
    - record
  - name: community_scope
    value: Engineered monoculture assay platform
    definition: Single-member schema representation across multiple experiments.
    evidence_ids:
    - record
    - methods
  - name: experimental_setting
    value: Liquid laboratory cultures with NdFeB magnet swarf
    definition: Study environment is distinct from the incorrect contaminated-soil
      term.
    evidence_ids:
    - methods
  - name: medium
    value: HyphoMOD with reduced phosphate; methanol assays and succinate precultures
    definition: Citrate is a supplied reagent; assay format and concentration matter.
    evidence_ids:
    - methods
    - organic-acids
  - name: source_category
    value: Primary experimental article full text in committed cache; live PubMed
      metadata
    definition: Supplemental Methods were not inspected.
    evidence_ids:
    - article
    - pubmed
  - name: biomass_state
    value: Growing cultures; harvested biomass acid-digested for ICP-MS
    definition: Metal loading per dry biomass and elemental proportions do not establish
      purified product grade.
    evidence_ids:
    - methods
    - selectivity
- assessment_id: taxonomy
  area: grounding
  topic: Taxonomy, strain, functional role and abundance
  outcome: concern
  summary: Taxon and GTDB/domain gates pass; species nomenclature differs explicitly.
    AM1 and mutant details are central but not structured in strain_designation. Dominant
    monoculture representation is plausible;202 mg/g DW is loading, not abundance.
    PRIMARY_DEGRADER is unsupported by simple C1 growth and REE uptake evidence.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - methods
  - schema
  - genetics
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: 'Citrate-Supplemented REE Leaching: supplied reagent -> greater abiotic
    leaching and cellular accumulation; no secreting source or recipient taxon asserted.
    5/15 mM citrate, 55 mM gluconate and 5 mM oxalate are distinguished. The description
    preserves concentration/scale limitations and total REE rather than Nd-only values.'
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - organic-acids
  - citrate-quote
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: concern
  summary: 'Lanthanophore-Mediated REE Bioaccumulation: AM1 delta-mxaF/pAZ1 mll expression
    -> increased cellular Nd/Pr/Dy, compared with delta-mxaF.80/15/8 mg/g DW are supported
    and assay-specific. Biological direction is sound; dysprosium(3+) preferred wording
    is incorrectly grounded to an atom.'
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - genetics
  - mll-quote
  - ontology
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: 'Polyphosphate Granule REE Sequestration: AM1 ppx deletion -> higher Nd
    accumulation, 202 mg/g DW relative to its assay comparator. Storage context and
    exopolyphosphatase mechanism are supported; no irreversible retention, covalent
    bonding or rescue is claimed. Exact ppx construction remains supplement-limited.'
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - genetics
  - ppx-quote
- assessment_id: node-3
  area: graph
  topic: ecological_interactions[3]
  outcome: supported
  summary: 'Methanol-Powered REE Acquisition Metabolism: AM1 delta-mxaF deletion ->
    REE dependency for methanol growth through alternative dehydrogenases. The record
    correctly avoids obligate wild-type REE dependence and an unmeasured uptake-energy
    gradient.'
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - methods
  - mxaF-quote
- assessment_id: edge-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: 'Direction: citrate-associated supply -> lanthanophore-associated accumulation
    node. The source measures increased leaching and uptake but does not isolate mll
    mediation of the citrate increment. The edge explicitly says PARTIAL and states
    that limit; this review supports the qualified representation, not fully established
    mediation.'
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - organic-acids
  - citrate-quote
- assessment_id: edge-1
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: supported
  summary: 'Direction: uptake -> polyphosphate storage. Separate mll and ppx perturbations
    and storage context support a proposed relationship; no traced mll-delivered metal
    or combined mediation is established. Existing PARTIAL wording correctly preserves
    uncertainty.'
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - genetics
  - mll-quote
  - ppx-quote
- assessment_id: graph-inventory
  area: graph
  topic: Entire graph and discussion references
  outcome: supported
  summary: All 4 nodes and 2 arrows were assessed, including their participants, metabolite/process
    descriptors and all 6 direct EvidenceItems. Arrow targets and all 4 discussion
    anchors resolve. No interspecies mechanism or extra causal arrow was inferred.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - history
- assessment_id: engineering
  area: evidence
  topic: engineering_design
  outcome: concern
  summary: 'Platform objective and deliberate monoculture representation are supported.
    The cited organic-acid sentence does not demonstrate member persistence tracking
    or pH/temperature perturbation designs: those reported values are fixed operating
    setpoints. Growth curves support growth/biomass measurements but do not establish
    the separate persistence endpoint.'
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - methods
  - article
- assessment_id: environment
  area: grounding
  topic: environment_term
  outcome: concern
  summary: The ontology ID/label pair is valid but denotes contaminated soil; controlled
    liquid culture with supplied magnet swarf is not soil. Notes correctly say engineered
    conditions while retaining contradictory gluconate-leaching and broader feedstock
    wording.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - ontology
  - methods
  - organic-acids
- assessment_id: factor-0
  area: evidence
  topic: 'environmental_factors[0]: pH'
  outcome: concern
  summary: pH 6.9 and 1 M NaOH control are measured Methods conditions. The attached
    snippet does not establish a physiological optimum, elimination of corrosion or
    comparative energy/waste benefits.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - methods
- assessment_id: factor-1
  area: evidence
  topic: 'environmental_factors[1]: Temperature'
  outcome: concern
  summary: 29.5 C bioreactor setting and 29-30 C routine cultivation are supported.
    An optimum and energy/economic advantages are not measured by this temperature
    statement.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - methods
- assessment_id: factor-2
  area: evidence
  topic: 'environmental_factors[2]: Bioreactor Scale'
  outcome: concern
  summary: 10 L demonstration is supported; successful pilot 100-1000 L or industrial
    >10, 000 L scaling and commercial feasibility are not demonstrated. Keep strain/condition-specific
    loading separate.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - scale
  - methods
- assessment_id: factor-3
  area: evidence
  topic: 'environmental_factors[3]: Medium Composition'
  outcome: concern
  summary: HyphoMOD phosphate recipe and methanol support are established; reduced
    phosphate improves growth/uptake. Characterizing gluconate as an effective REE
    leaching additive conflicts with the tested negative result. Routine succinate
    precultures and methanol REE assays should be distinguished.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - methods
  - organic-acids
- assessment_id: factor-4
  area: evidence
  topic: 'environmental_factors[4]: REE Bioaccumulation Capacity'
  outcome: supported
  summary: 202 mg Nd/g DW and approximately 5.5-fold increase are supported for the
    separate ppx test and its comparison; they are not the 10 L baseline yield.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - genetics
  - scale
- assessment_id: factor-5
  area: evidence
  topic: 'environmental_factors[5]: REE Selectivity and Purity'
  outcome: concern
  summary: 98% REE and the source-reported 96.8%Nd refer to measured cellular metals
    in a particular batch culture. They do not establish magnet-grade metal, no further
    purification, or mll-mediated selectivity in that experiment.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - selectivity
  - scale
  - genetics
- assessment_id: factor-6
  area: evidence
  topic: 'environmental_factors[6]: Substrate E-waste Composition'
  outcome: concern
  summary: NdFeB magnet swarf is supported. Source measurements are 68%Fe, 26.7%Nd,
    4.35%Pr, 3.34%Dy; prose gives~1%Dy. Phosphor powder processing and universal substrate
    performance are not established by the inspected experiment; other ores/smartphones
    are discussed as growth sources.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - selectivity
  - article
- assessment_id: factor-7
  area: evidence
  topic: 'environmental_factors[7]: Citrate Leaching Efficiency'
  outcome: concern
  summary: 5/15 mM citrate chemical leaching gives 8.2/58.7 ppm total REE after 28
    h, supported. Biological uptake is condition-specific and 15 mM inhibits 100 mL
    growth; comparative economic/environmental claims are not measured by the leaching
    endpoint.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - organic-acids
- assessment_id: factor-8
  area: evidence
  topic: 'environmental_factors[8]: Genetic Engineering Strategy'
  outcome: supported
  summary: ppx deletion is directly linked to 202 mg/g DW and~5.5-fold increase. Existing
    wording does not assert an unverified double mutant, retention kinetics or combined
    mll phenotype.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - genetics
- assessment_id: cultivation
  area: completeness
  topic: Structured growth conditions and external resources
  outcome: concern
  summary: 'All target bytes were inspected: growth_media, cultivation_setup, associated_datasets
    and external_resources blocks are not populated. Detailed Methods provide actionable
    source-backed cultivation information; current environmental-factor prose is not
    a fully normalized condition-specific protocol. Optional omissions are not schema
    failures.'
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - methods
- assessment_id: history-discussion
  area: provenance
  topic: History and unresolved scientific questions
  outcome: supported
  summary: Two append-only history events, embedded events and prior graph decisions
    agree. The current discussion appropriately distinguishes separate interventions
    and unproven combined mediation. This review extends to non-graph claims without
    changing history, closing the discussion or claiming an earlier structured finding
    was resolved.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - history
- assessment_id: adapters
  area: evidence
  topic: Structured transcriptomic-source applicability
  outcome: not_applicable
  summary: The inspected 20 organism public iModulonDB catalogue contains no matching
    Methylobacterium/Methylorubrum dataset. No related-organism module was substituted
    for gene or phenotype support.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - imodulondb
- assessment_id: validation
  area: schema
  topic: Focused validators and corpus scope
  outcome: supported
  summary: Focused schema, strict, terms, references, GTDB coherence/domain and history
    pass with no ontology skips. Cited cache bytes remain unchanged. Corpus network
    failures are retained as unrelated warnings; validation does not substantiate
    the scientific claims.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-references-explained
  - check-validate-gtdb
  - check-validate-gtdb-domain
  - check-validate-history
  - record
- assessment_id: scores
  area: completeness
  topic: Native completeness and validation quality
  outcome: concern
  summary: Completeness 80 and validation quality 80 do not establish scientific correctness;
    five major findings remain. Native participant/reference network has no target
    finding, even though two mechanistic arrows correctly remain partial.
  target_ids:
  - CommunityMech:000322
  evidence_ids:
  - record
  - check-audit-network
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required+5 environment+10 for at least 3 environmental
      factors+10 for at least 3 interactions+5 external_resources+10 growth_media+5
      associated_datasets+5 any metabolites). Applied 50+5+10+10+0+0+0+5=80; presence
      is not correctness.
  - name: validation_quality
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50*P1-10*P2-2*P3+20*min(mean interaction evidence/2, 1)+15
      if native network COMPLETE, 0, 100). P1=0, P2=5, P3=0, 6 EvidenceItems/4 nodes=1.5,
      network COMPLETE.100-50+15+15=80.
  - name: P1
    value: 0
    unit: findings
    definition: Target-specific blocker findings.
  - name: P2
    value: 5
    unit: findings
    definition: Target-specific major findings.
  - name: P3
    value: 0
    unit: findings
    definition: Target-specific minor findings.
  - name: interaction_evidence
    value: 1.5
    unit: evidence items per interaction
    denominator: 4
    definition: Six directly attached EvidenceItems across four nodes, all from one
      publication; not independent replication.
findings:
- finding_id: soil-environment-misgrounding
  issue_key: CommunityMech.000322.soil-environment-misgrounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Contaminated-soil grounding contradicts the engineered study setting
  description: ENVO:00002116 requires soil, whereas source experiments use controlled
    liquid cultures with magnet swarf. A correct canonical label cannot validate the
    biological setting.
  target_ids:
  - CommunityMech:000322
  field_paths:
  - environment_term.term
  - environment_term.preferred_term
  evidence_ids:
  - record
  - ontology
  - methods
  rule_id: docs/record-review-profile.md:grounding
  native_severity: P2
  normalization_reason: 'P2 major: materially incorrect grounding or unsupported scientific/experimental
    interpretation, rather than a formatting defect.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
- finding_id: dysprosium-chemical-identity
  issue_key: CommunityMech.000322.dysprosium-chemical-identity
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Dysprosium cation is represented by an atom ontology class
  description: The preferred term asserts dysprosium(3+) but CHEBI:33377 is dysprosium
    atom, not a parent of the cation. The note acknowledges that distinction and selects
    the atom for enum/export consistency; consistency does not establish chemical
    identity.
  target_ids:
  - CommunityMech:000322
  field_paths:
  - ecological_interactions[1].metabolites[2].term
  - ecological_interactions[1].metabolites[2].preferred_term
  - ecological_interactions[1].metabolites[2].notes
  evidence_ids:
  - record
  - ontology
  rule_id: docs/record-review-profile.md:grounding
  native_severity: P2
  normalization_reason: 'P2 major: materially incorrect grounding or unsupported scientific/experimental
    interpretation, rather than a formatting defect.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
- finding_id: functional-role-mismatch
  issue_key: CommunityMech.000322.functional-role-mismatch
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Primary-degrader role is not supported by methanol growth and REE uptake
  description: PRIMARY_DEGRADER means degradation of complex substrates. The demonstrated
    processes are methylotrophic growth, chemical leaching and metal accumulation;
    these do not by themselves show degradation of a complex substrate.
  target_ids:
  - CommunityMech:000322
  field_paths:
  - taxonomy[0].functional_role
  evidence_ids:
  - record
  - schema
  - methods
  rule_id: P2.4
  native_severity: P2
  normalization_reason: 'P2 major: materially incorrect grounding or unsupported scientific/experimental
    interpretation, rather than a formatting defect.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
- finding_id: operating-and-engineering-claims
  issue_key: CommunityMech.000322.operating-and-engineering-claims
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Non-graph operating and engineering claims exceed or conflict with measured
    conditions
  description: Outside the corrected graph, gluconate is presented as promoting REE
    leaching despite the negative result; fixed pH/temperature settings become a perturbation
    design or optimum; persistence is an unsupported endpoint; substrate composition
    gives~1%Dy versus measured 3.34%. Broader feedstock and economic/physiological
    assertions lack claim-specific evidence in the inspected source.
  target_ids:
  - CommunityMech:000322
  field_paths:
  - engineering_design.measurement_endpoints
  - engineering_design.perturbation_design
  - environment_term.notes
  - taxonomy[0].taxon_term.notes
  - environmental_factors[0].description
  - environmental_factors[1].description
  - environmental_factors[3].description
  - environmental_factors[6].description
  - environmental_factors[7].description
  evidence_ids:
  - record
  - methods
  - organic-acids
  - selectivity
  rule_id: CLAUDE.md:claim-level-evidence
  native_severity: P2
  normalization_reason: 'P2 major: materially incorrect grounding or unsupported scientific/experimental
    interpretation, rather than a formatting defect.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
- finding_id: product-purity-and-scale-overstatement
  issue_key: CommunityMech.000322.product-purity-and-scale-overstatement
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Cellular composition and laboratory scale are inflated to commercial product
    performance
  description: Measured cellular-metal selectivity is described as magnet-grade product
    purity eliminating downstream purification. 10 L proof of principle becomes industrial
    feasibility and larger-scale performance; high ppx/mll shake-flask yields and
    selectivity from other conditions are presented as integrated strain attributes.
    The paper explicitly leaves end-to-end rare-earth oxide production to future work.
  target_ids:
  - CommunityMech:000322
  field_paths:
  - description
  - taxonomy[0].taxon_term.notes
  - environmental_factors[2].description
  - environmental_factors[5].description
  evidence_ids:
  - record
  - methods
  - scale
  - selectivity
  - genetics
  rule_id: CLAUDE.md:claim-level-evidence
  native_severity: P2
  normalization_reason: 'P2 major: materially incorrect grounding or unsupported scientific/experimental
    interpretation, rather than a formatting defect.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
actions:
- action_id: fix-soil-environment-misgrounding
  description: Ground the physical culture environment to a verified source-compatible
    class and retain waste feedstock separately.
  finding_ids:
  - soil-environment-misgrounding
  target_ids:
  - CommunityMech:000322
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
  acceptance_checks:
  - Verify replacement ID, label and definition against the actual setting.
  - Run focused terms/strict validation and inspect rendered environment after separately
    authorized curation.
- action_id: fix-dysprosium-chemical-identity
  description: Use a source-appropriate chemical identity and verify its ontology
    semantics. Trace downstream enum/extraction/export assumptions before changing
    the mapping; coordinate separately authorized maintained schema/export changes
    if needed.
  finding_ids:
  - dysprosium-chemical-identity
  target_ids:
  - CommunityMech:000322
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
  acceptance_checks:
  - No 3+ cation is asserted as an atom or falsely called its child.
  - Verify any broader molecular-entity mapping and preserve explicit measurement/speciation
    limits.
  - Recheck all consumers named in the existing note, ontology validation and affected
    KG exports after authorized implementation.
- action_id: fix-functional-role-mismatch
  description: Remove or replace the unsupported role using an evidenced biological
    function and schema meaning.
  finding_ids:
  - functional-role-mismatch
  target_ids:
  - CommunityMech:000322
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
  acceptance_checks:
  - Do not infer complex-substrate degradation from metal leaching or growth on methanol.
  - Any replacement role has exact source support and passes strict/network gates.
- action_id: fix-operating-and-engineering-claims
  description: Reconcile all descriptive and condition fields with exact assay contexts;
    preserve negatives, fixed-setpoint distinctions and measured composition, and
    remove or separately substantiate extrapolations.
  finding_ids:
  - operating-and-engineering-claims
  target_ids:
  - CommunityMech:000322
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
  acceptance_checks:
  - All 9 environmental factors retain exact strain, medium, scale and endpoint context.
  - Gluconate is not said to enhance REE leaching in the tested condition.
  - Growth observations are not relabeled persistence, and fixed setpoints are not
    a tested optimum or perturbation series.
  - Run source/snippet, strict and term checks after separately authorized curation.
- action_id: fix-product-purity-and-scale-overstatement
  description: Keep measured cell-associated metal proportions separate from recovered-product
    purity, and distinguish each genotype/scale result from proposed integration or
    commercialization.
  finding_ids:
  - product-purity-and-scale-overstatement
  target_ids:
  - CommunityMech:000322
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Methylobacterium_REE_Ewaste_Platform.yaml
    role: canonical_record
  acceptance_checks:
  - No magnet-grade metal or elimination of downstream purification is claimed without
    a demonstrated product-analysis source.
  - 10 L demonstration, baseline 3.2 mg/g, mll 80 mg/g and ppx 202 mg/g remain tied
    to their own contexts.
  - Pilot/industrial scale and commercial feasibility are explicitly prospective or
    removed.
limitations:
- The primary article full text was assessed through the committed EuropePMC-derived
  cache; PubMed metadata/abstract/figure captions were independently inspected online.
  Supplemental Methods were not retrieved, so exact ppx construction remains limited.
- No independent reconstruction of the historical 42-genome GTDB mapping was attempted;
  documented validators cover canonical terms, coherence and domain.
- Corpus network checks failed on warnings elsewhere; no target finding was found.
  Required failures are explicit and the verdict is needs_curation.
- Local ontology meanings use available SemanticSQL snapshots. Dysprosium mapping
  needs chemically correct semantics and coordinated consumer review, not a new nearby
  identifier assumed equivalent.
- The review did not author/edit the record during this session; earlier curation
  shares the codex identity, so person-level reviewer independence is unknown.
notes:
- No canonical record, cache, history, generated product or scientific status was
  changed. Proposed curation remains separate authorized work.
- No current issue-tracker disposition is inferred from historical links; no paid
  provider or outbound communication was used.
tags:
- record-review
- isolate
- ree-biomining
- batch-01
```
