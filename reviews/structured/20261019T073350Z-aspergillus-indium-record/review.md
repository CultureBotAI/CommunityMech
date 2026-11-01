# Aspergillus indium LCD recovery: whole-record source review

- Review: 20261019T073350Z-aspergillus-indium-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-19T07:29:02.918763Z
- Finished UTC: 2026-10-19T07:33:50.881008Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The fungal LCD bioleaching identity and five-node/four-arrow mechanism are supported at abstract resolution. Two major findings concern unsupported functional roles and population-tracking readouts; one minor finding concerns environmental specificity and outcome placement. No record edits were made.

## Scope And Provenance

Whole canonical isolate record; every current interaction and downstream edge assessed against the primary abstract, with full-text limitations explicit.

Selection: First unreviewed path in the skill corpus kb/communities/*.yaml and data/isolates/*.yaml after validated record_review.py list. Initial corpus:462 records,9 targeted by existing valid bundles,453 unreviewed. One target in this bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a4611c913c8da9619673df63a0c2cce3aa206a83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000320 | data/isolates/Aspergillus_Indium_LED_Recovery.yaml | maintained | Aspergillus Indium LCD Recovery Platform |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000320 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml data/isolates/Aspergillus_Indium_LED_Recovery.yaml |
| validate-strict | passed | True | CommunityMech:000320 | uv run python scripts/validate_strict.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/communitymech-record-reviews-20261019/reports/instance_validation_failures.tsv |
| validate-terms | passed | True | CommunityMech:000320 | ✅ Validation passed<br>uv run linkml-term-validator validate-data data/isolates/Aspergillus_Indium_LED_Recovery.yaml -s src/communitymech/schema/communitymech.yaml --labels<br><br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 0.00/2.20G [00:00&lt;?, ?B/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 128k/2.20G [00:00&lt;33:07, 1.19MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 384k/2.20G [00:00&lt;20:07, 1.96MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 1.50M/2.20G [00:00&lt;06:17, 6.27MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 3.31M/2.20G [00:00&lt;03:31, 11.2MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 6.12M/2.20G [00:00&lt;02:14, 17.6MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 9.88M/2.20G [00:00&lt;01:37, 24.1MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 15.2M/2.20G [00:00&lt;01:08, 34.2MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 16.4M/2.20G [00:00&lt;01:28, 26.6MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 18.5M/2.20G [00:00&lt;01:32, 25.3MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 24.1M/2.20G [00:01&lt;01:23, 28.1MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 25.2M/2.20G [00:01&lt;01:38, 23.8MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;▏         &#124; 30.2M/2.20G [00:01&lt;01:17, 30.2MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 37.6M/2.20G [00:01&lt;00:54, 42.8MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 40.6M/2.20G [00:01&lt;01:03, 36.7MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 42.2M/2.20G [00:01&lt;01:16, 30.2MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 49.2M/2.20G [00:01&lt;00:56, 41.1MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 52.9M/2.20G [00:01&lt;00:57, 40.3MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 56.9M/2.20G [00:01&lt;00:57, 40.4MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 62.3M/2.20G [00:02&lt;00:51, 44.9MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 64.3M/2.20G [00:02&lt;01:01, 37.2MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 65.6M/2.20G [00:02&lt;01:17, 29.8MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 67.1M/2.20G [00:02&lt;01:29, 25.7MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 71.7M/2.20G [00:02&lt;01:11, 31.8MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 76.3M/2.20G [00:02&lt;01:03, 36.1MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 78.8M/2.20G [00:02&lt;01:09, 33.1MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 85.7M/2.20G [00:02&lt;00:51, 44.4MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 93.6M/2.20G [00:02&lt;00:40, 55.6MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 100M/2.20G [00:03&lt;00:38, 59.0MB/s] <br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 109M/2.20G [00:03&lt;00:32, 69.3MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 116M/2.20G [00:03&lt;00:32, 69.0MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 120M/2.20G [00:03&lt;00:48, 46.4MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 122M/2.20G [00:03&lt;00:55, 40.6MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 125M/2.20G [00:03&lt;00:58, 38.0MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 129M/2.20G [00:03&lt;01:00, 37.1MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 136M/2.20G [00:03&lt;00:45, 48.7MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 141M/2.20G [00:03&lt;00:44, 49.4MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 144M/2.20G [00:04&lt;00:51, 43.2MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 145M/2.20G [00:04&lt;01:10, 31.5MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 146M/2.20G [00:04&lt;01:26, 25.6MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 146M/2.20G [00:04&lt;01:56, 19.0MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 147M/2.20G [00:04&lt;02:22, 15.5MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 148M/2.20G [00:04&lt;02:54, 12.7MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 148M/2.20G [00:04&lt;03:41, 9.99MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 149M/2.20G [00:04&lt;04:30, 8.18MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 149M/2.20G [00:04&lt;05:00, 7.34MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 150M/2.20G [00:05&lt;05:37, 6.54MB/s]<br>Down |
| validate-gtdb | passed | True | CommunityMech:000320 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000320 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml |
| validate-references-explained | passed | True | CommunityMech:000320 | Validating data/isolates/Aspergillus_Indium_LED_Recovery.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| validate-history | passed | True | CommunityMech:000320 | No issues found |
| audit-network | failed | True | CommunityMech:000320 | Full-corpus command returned 1: 462 records, 57 warnings in 21 records, zero errors. The target record has no reported network finding; these corpus warnings are not attributed to it. |
| check-network-quality | failed | True | CommunityMech:000320 | Full-corpus command returned 1: 462 records, 57 warnings in 21 records, zero errors. The target record has no reported network finding; these corpus warnings are not attributed to it. |
| validate-strict initial dependency attempt | failed | False | CommunityMech:000320 | Initial restricted execution could not access the ontology dependency. This attempt was superseded by the successful retry retained above; it is not a biological record failure. |
| validate-terms initial dependency attempt | failed | False | CommunityMech:000320 | Initial restricted execution could not access the ontology dependency. This attempt was superseded by the successful retry retained above; it is not a biological record failure. |
| validate-gtdb-domain initial dependency attempt | failed | False | CommunityMech:000320 | Initial restricted execution could not access the ontology dependency. This attempt was superseded by the successful retry retained above; it is not a biological record failure. |

## Scientific And Domain Assessments

### Isolate platform identity and experimental scope

identity: supported. Targets: CommunityMech:000320.

The identity is a laboratory A. niger fermentation-broth platform for indium recovery from LCD waste. ENGINEERED origin/state and BIOMINING category agree with that scope. The legacy filename contains LED but the name, source and current claims consistently specify LCD; this is not mistaken biological identity.

### Taxonomy, functional roles and abundance scope

grounding: concern. Targets: CommunityMech:000320.

A. niger is the reported fermentation organism and its sole-member representation is explicit. Monoculture abundance wording does not assert a measured relative abundance. However PRIMARY_PRODUCER asserts autotrophy under the schema, and PRIMARY_DEGRADER asserts complex-substrate degradation; neither is established by the cited organic-acid bioleaching experiment. NO_GTDB_EQUIVALENT is appropriate in scope for this fungal taxon.

### Engineering design and measured endpoints

scope: concern. Targets: CommunityMech:000320.

The objective, three-approach perturbation and recovery/mechanism characterization match the abstract. Member-level abundance and persistence tracking is an unsupported added readout; the attached carboxyl-group snippet does not establish it.

### Environment, cultivation and outcome fields

representation: concern. Targets: CommunityMech:000320.

Laboratory setting is supported but the preferred wording laboratory bioreactor is more specific than the inspected source. The record appropriately withholds numerical medium/temperature/pulp-density claims. EnvironmentalFactor[0] is a recovery outcome rather than an environmental condition; entries [1–3] describe process chemistry, tunability and biomass inhibition. Their prose is abstract-supported, but should not be treated as a reproducible growth protocol.

### ecological_interactions[0]: Optimization

graph: supported. Targets: CommunityMech:000320.

Participant/source: A. niger (NCBITaxon:5061); no second microbial target; COMMUNITY_LEVEL process in the engineered LCD-waste fermentation system. Fermentation optimization increases proton concentration, effective carboxyl groups and oxalic acid output. GO:0019752 is consistent with the described acid chemistry at this broad level; no specific pathway or enzyme is demonstrated.

### ecological_interactions[1]: Proton release

graph: supported. Targets: CommunityMech:000320.

Participant/source: A. niger (NCBITaxon:5061); no second microbial target; COMMUNITY_LEVEL process in the engineered LCD-waste fermentation system. Acid/protein carboxyl groups supply protons for indium leaching. This is extracellular chemical dissolution, not cellular metal transport.

### ecological_interactions[2]: Dissolution

graph: supported. Targets: CommunityMech:000320.

Participant/source: A. niger (NCBITaxon:5061); no second microbial target; COMMUNITY_LEVEL process in the engineered LCD-waste fermentation system. The oxide-bearing LCD material is leached by fermentation broth. Indium(3+) denotes the released/adsorbed ion. The source supports a leaching mechanism, with no cellular uptake claim.

### ecological_interactions[3]: Biomass inhibition

graph: supported. Targets: CommunityMech:000320.

Participant/source: A. niger (NCBITaxon:5061); no second microbial target; COMMUNITY_LEVEL process in the engineered LCD-waste fermentation system. A. niger biomass blocks proton contact and adsorbs released indium; the effect on recovery is negative.

### ecological_interactions[4]: Recovery

graph: supported. Targets: CommunityMech:000320.

Participant/source: A. niger (NCBITaxon:5061); no second microbial target; COMMUNITY_LEVEL process in the engineered LCD-waste fermentation system. The observed optimized recovery rises from 12.3% to 100%; the abstract also supports further process-parameter tuning without giving settings.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000320.

From node [0] to named node [1], within the same A. niger broth/LCD process; no interspecies target. Positive: optimized chemistry supplies the proton-donating groups used for leaching. This joins the abstract component and mechanism statements; it is not proof of separately controlled causal intermediates.

### ecological_interactions[1].downstream[0]

graph: supported. Targets: CommunityMech:000320.

From node [1] to named node [2], within the same A. niger broth/LCD process; no interspecies target. Positive: carboxyl-group proton donation enables metal-oxide leaching. Abstract-level chemical causal interpretation is supported.

### ecological_interactions[2].downstream[0]

graph: supported. Targets: CommunityMech:000320.

From node [2] to named node [4], within the same A. niger broth/LCD process; no interspecies target. Positive: mobilization by oxide leaching produces recovered indium in broth. The abstract supports recovery but does not give a separate mass-balance experiment for this arrow.

### ecological_interactions[3].downstream[0]

graph: supported. Targets: CommunityMech:000320.

From node [3] to named node [4], within the same A. niger broth/LCD process; no interspecies target. Negative: biomass prevents proton contact and adsorbs indium, reducing recovery. The description correctly preserves inhibition.

### Chemicals, metals, environmental evidence and resource scope

evidence: supported. Targets: CommunityMech:000320.

Oxalic acid, proton/hydron, protein and indium(3+) are assigned roles matching the abstract. Related ingredients are process products/reactants, not a fabricated medium recipe. All four environmental statements and all three ingredient snippets are supported at abstract resolution. The recovered metal is indium; iron is competition context rather than an asserted second target. No genomic dataset, accession or external-resource assertion is present to certify.

### Curation history and unresolved discussion

provenance: supported. Targets: CommunityMech:000320.

Embedded and append-only history describe the GO cleanup and graph scope repair. The open discussion explicitly asks for condition-specific controls and acknowledges abstract-level evidence. The complete methods remain unresolved; this review does not declare the reported mechanism false.

### Structured transcriptomics source applicability

evidence: not_applicable. Targets: CommunityMech:000320.

No gene, locus tag, UniProt accession, regulator or transcriptomics dataset is asserted, and no source strain is identified. The single broad GO process is chemical/metabolic context rather than a specific expression-module claim; no iModulonDB cross-check would establish this extracellular fungal bioleaching experiment.

### Ontology and GTDB verification

grounding: supported. Targets: CommunityMech:000320.

NCBITaxon:5061 represents the reported A. niger; ENVO:01001405 is laboratory environment. Chemistry descriptors are CHEBI:16995 oxalic acid, CHEBI:15378 hydron, CHEBI:36080 protein, CHEBI:49664 indium(3+), with GO:0019752 carboxylic acid metabolic process. Validator evidence below determines identifier/label verification coverage; ontology validity alone does not establish the experimental role.

### Native completeness and validation-quality scores

completeness: concern. Targets: CommunityMech:000320.

The rubric yields completeness 80 and validation quality 100 despite two major and one minor finding; capped scores do not constitute scientific approval. Required metadata earns the 50-point block. There are four environmental entries, five interactions, six interaction-level evidence items, no growth-medium block, no associated dataset and no external resource. The five-node/four-arrow graph is connected and has no network-audit finding for this target.

## Findings

### roles: Functional roles assert metabolism unsupported by the cited experiment

major / open / confirmed; issue key: cm-000320-functional-role-scope.

PRIMARY_PRODUCER explicitly means carbon-fixing autotroph in the maintained schema. PRIMARY_DEGRADER means complex-substrate degradation. The inspected source supports fungal organic-acid fermentation and extracellular leaching, not these ecological roles. Producing an acid does not establish autotrophy, and dissolving metal oxide is not evidence of degrading complex organic substrate.

### readout: Member abundance and persistence tracking is not supported by inspected evidence

major / open / confirmed; issue key: cm-000320-unsubstantiated-population-readout.

engineering_design.measurement_endpoints[1] asserts member-level abundance and persistence tracking. The complete inspected abstract reports indium leaching efficiency, broth chemistry and biomass inhibition, but no population-tracking assay. The nearest cited snippet describes carboxyl-group proton donation. This is a bounded evidence gap, not a claim that full methods exclude every growth measurement.

### environment: Environment wording and outcome placement imply more protocol detail than supported

minor / open / confirmed; issue key: cm-000320-environment-outcome-placement.

environment_term.preferred_term says laboratory bioreactor although the inspected abstract identifies fermentation systems without a vessel. environmental_factors[0] stores 100% indium recovery as an environmental parameter, whereas it is a measured outcome. The value is sourced correctly; the concern is representation and specificity.

## Recommended Actions And Acceptance Checks

### fix-roles

Curate the role list against the actual fermentation experiment; remove unsupported roles or replace them only with a directly evidenced role.

- Each retained role must have a precise source passage supporting its schema definition for this experiment.
- just validate data/isolates/Aspergillus_Indium_LED_Recovery.yaml; just validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml; just validate-references-explained data/isolates/Aspergillus_Indium_LED_Recovery.yaml
- If curation is separately authorized, append history and regenerate/check affected docs using just gen-html and just check-docs-current.

### fix-readout

Replace the unsupported population-tracking endpoint with source-backed reported readouts, or retain it only after obtaining direct methods/results evidence.

- Every measurement endpoint must be supported by a source passage identifying that assay/readout in this experiment.
- just validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml; just validate-references-explained data/isolates/Aspergillus_Indium_LED_Recovery.yaml
- Re-review the engineering-design evidence at assertion level; do not infer abundance tracking from the mere presence of biomass.

### fix-environment

Use source-supported laboratory-setting wording and represent indium-recovery efficiency as an experimental outcome rather than a growth condition.

- A bioreactor/vessel claim requires a direct methods passage; otherwise retain laboratory-environment scope.
- The reported 12.3% to 100% recovery result remains preserved in an outcome context.
- just validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml; just validate-terms data/isolates/Aspergillus_Indium_LED_Recovery.yaml; just validate-references-explained data/isolates/Aspergillus_Indium_LED_Recovery.yaml

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/isolates/Aspergillus_Indium_LED_Recovery.yaml; Entire record, including five interaction nodes, four downstream arrows, four environmental factors and embedded history | supports | Read the complete canonical MicrobialCommunity record. One fungal monoculture is explicitly represented for interoperability; it is not a natural multi-member community. |
| source | https://pubmed.ncbi.nlm.nih.gov/34111782/; PMID:34111782; DOI:10.1016/j.scitotenv.2021.148151; Abstract sentences 1–7; matching cached text references_cache/PMID_34111782.txt | supports | The inspected abstract identifies A. niger fermentation broth and waste LCD panels; three bioleaching approaches, optimized acid/carboxyl chemistry, increased indium recovery, and inhibitory biomass. It does not report the strain, medium, vessel, numerical cultivation conditions, or population tracking. |
| acid | PMID:34111782; Abstract sentences 4–5; references_cache/PMID_34111782.txt | supports | Carboxyl groups from acids and proteins donate protons for leaching; optimization increases proton concentration, effective carboxyl groups and oxalic acid. |
| biomass | PMID:34111782; Abstract sentence 6; references_cache/PMID_34111782.txt | supports | Biomass prevents proton contact with the oxide and adsorbs released indium, decreasing recovery. |
| recovery | PMID:34111782; Abstract sentence 3; references_cache/PMID_34111782.txt | supports | Fermentation-method optimization improves the reported recovery endpoint from 12.3% to 100%. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum.PRIMARY_PRODUCER / PRIMARY_DEGRADER; EngineeringDesign.measurement_endpoints; EnvironmentalFactor; InteractionDownstream | supports | PRIMARY_PRODUCER means carbon-fixing autotroph; PRIMARY_DEGRADER means complex-substrate degrader. Measurement endpoints are primary experimental readouts. Downstream schema stores target and description, with source support located on the interaction. |
| history | history/records/Aspergillus_Indium_LED_Recovery/; 2026-10-02T045300Z-codex-d1d786.yaml and 2026-10-05T071439Z-codex-eb16f5.yaml; reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml records[0] | supports | Two append-only history records disclose AI assistance; the earlier graph review removed obsolete/cellular transport mappings and explicitly did not certify all other metadata. This review makes no new history event or status promotion. |
| source-access | https://www.sciencedirect.com/science/article/pii/S0048969721032228; Publisher full-text attempt and PubMed abstract, accessed during this review | unknown | Publisher access returned HTTP 403. Full methods and supplement content were not inspected. No claim is made that protocol details are absent from the publication. |
| check-validate | just --no-dotenv validate data/isolates/Aspergillus_Indium_LED_Recovery.yaml; Exit code 0 | context_only | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml data/isolates/Aspergillus_Indium_LED_Recovery.yaml |
| check-validate-strict | just --no-dotenv validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml; Exit code 0 | context_only | uv run python scripts/validate_strict.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/communitymech-record-reviews-20261019/reports/instance_validation_failures.tsv |
| check-validate-terms | just --no-dotenv validate-terms data/isolates/Aspergillus_Indium_LED_Recovery.yaml; Exit code 0 | context_only | ✅ Validation passed<br>uv run linkml-term-validator validate-data data/isolates/Aspergillus_Indium_LED_Recovery.yaml -s src/communitymech/schema/communitymech.yaml --labels<br><br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 0.00/2.20G [00:00&lt;?, ?B/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 128k/2.20G [00:00&lt;33:07, 1.19MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 384k/2.20G [00:00&lt;20:07, 1.96MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 1.50M/2.20G [00:00&lt;06:17, 6.27MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 3.31M/2.20G [00:00&lt;03:31, 11.2MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 6.12M/2.20G [00:00&lt;02:14, 17.6MB/s]<br>Downloading ncbitaxon.db.gz:   0%&#124;          &#124; 9.88M/2.20G [00:00&lt;01:37, 24.1MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 15.2M/2.20G [00:00&lt;01:08, 34.2MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 16.4M/2.20G [00:00&lt;01:28, 26.6MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 18.5M/2.20G [00:00&lt;01:32, 25.3MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 24.1M/2.20G [00:01&lt;01:23, 28.1MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;          &#124; 25.2M/2.20G [00:01&lt;01:38, 23.8MB/s]<br>Downloading ncbitaxon.db.gz:   1%&#124;▏         &#124; 30.2M/2.20G [00:01&lt;01:17, 30.2MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 37.6M/2.20G [00:01&lt;00:54, 42.8MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 40.6M/2.20G [00:01&lt;01:03, 36.7MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 42.2M/2.20G [00:01&lt;01:16, 30.2MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 49.2M/2.20G [00:01&lt;00:56, 41.1MB/s]<br>Downloading ncbitaxon.db.gz:   2%&#124;▏         &#124; 52.9M/2.20G [00:01&lt;00:57, 40.3MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 56.9M/2.20G [00:01&lt;00:57, 40.4MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 62.3M/2.20G [00:02&lt;00:51, 44.9MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 64.3M/2.20G [00:02&lt;01:01, 37.2MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 65.6M/2.20G [00:02&lt;01:17, 29.8MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 67.1M/2.20G [00:02&lt;01:29, 25.7MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 71.7M/2.20G [00:02&lt;01:11, 31.8MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 76.3M/2.20G [00:02&lt;01:03, 36.1MB/s]<br>Downloading ncbitaxon.db.gz:   3%&#124;▎         &#124; 78.8M/2.20G [00:02&lt;01:09, 33.1MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 85.7M/2.20G [00:02&lt;00:51, 44.4MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 93.6M/2.20G [00:02&lt;00:40, 55.6MB/s]<br>Downloading ncbitaxon.db.gz:   4%&#124;▍         &#124; 100M/2.20G [00:03&lt;00:38, 59.0MB/s] <br>Downloading ncbitaxon.db.gz:   5%&#124;▍         &#124; 109M/2.20G [00:03&lt;00:32, 69.3MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 116M/2.20G [00:03&lt;00:32, 69.0MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 120M/2.20G [00:03&lt;00:48, 46.4MB/s]<br>Downloading ncbitaxon.db.gz:   5%&#124;▌         &#124; 122M/2.20G [00:03&lt;00:55, 40.6MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 125M/2.20G [00:03&lt;00:58, 38.0MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 129M/2.20G [00:03&lt;01:00, 37.1MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▌         &#124; 136M/2.20G [00:03&lt;00:45, 48.7MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 141M/2.20G [00:03&lt;00:44, 49.4MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 144M/2.20G [00:04&lt;00:51, 43.2MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 145M/2.20G [00:04&lt;01:10, 31.5MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 146M/2.20G [00:04&lt;01:26, 25.6MB/s]<br>Downloading ncbitaxon.db.gz:   6%&#124;▋         &#124; 146M/2.20G [00:04&lt;01:56, 19.0MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 147M/2.20G [00:04&lt;02:22, 15.5MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 148M/2.20G [00:04&lt;02:54, 12.7MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 148M/2.20G [00:04&lt;03:41, 9.99MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 149M/2.20G [00:04&lt;04:30, 8.18MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 149M/2.20G [00:04&lt;05:00, 7.34MB/s]<br>Downloading ncbitaxon.db.gz:   7%&#124;▋         &#124; 150M/2.20G [00:05&lt;05:37, 6.54MB/s]<br>Down |
| check-validate-gtdb | just --no-dotenv validate-gtdb data/isolates/Aspergillus_Indium_LED_Recovery.yaml; Exit code 0 | context_only | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | just --no-dotenv validate-gtdb-domain data/isolates/Aspergillus_Indium_LED_Recovery.yaml; Exit code 0 | context_only | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml |
| check-validate-references-explained | just --no-dotenv validate-references-explained data/isolates/Aspergillus_Indium_LED_Recovery.yaml; Exit code 0 | context_only | Validating data/isolates/Aspergillus_Indium_LED_Recovery.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-validate-history | just --no-dotenv validate-history history/records/Aspergillus_Indium_LED_Recovery; Exit code 0 | context_only | No issues found |
| check-audit-network | just --no-dotenv audit-network; Exit code 1 | context_only | Full-corpus command returned 1: 462 records, 57 warnings in 21 records, zero errors. The target record has no reported network finding; these corpus warnings are not attributed to it. |
| check-check-network-quality | just --no-dotenv check-network-quality; Exit code 1 | context_only | Full-corpus command returned 1: 462 records, 57 warnings in 21 records, zero errors. The target record has no reported network finding; these corpus warnings are not attributed to it. |
| check-validate-strict-initial | just --no-dotenv validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml; Initial attempt; exit 0 | context_only | Initial restricted execution could not access the ontology dependency. This attempt was superseded by the successful retry retained above; it is not a biological record failure. |
| check-validate-terms-initial | just --no-dotenv validate-terms data/isolates/Aspergillus_Indium_LED_Recovery.yaml; Initial attempt; exit 1 | context_only | Initial restricted execution could not access the ontology dependency. This attempt was superseded by the successful retry retained above; it is not a biological record failure. |
| check-validate-gtdb-domain-initial | just --no-dotenv validate-gtdb-domain data/isolates/Aspergillus_Indium_LED_Recovery.yaml; Initial attempt; exit 0 | context_only | Initial restricted execution could not access the ontology dependency. This attempt was superseded by the successful retry retained above; it is not a biological record failure. |

## Limits And Additional Notes

- Scientific source assessment is limited to the complete primary abstract and matching committed cache. Publisher full text returned HTTP 403; methods and supplementary evidence were not inspected.
- Source strain, cultivation medium, vessel, temperature, pH and pulp density remain unresolved at this source tier; their omission is not an instruction to fabricate details.
- Graph arrows retain abstract-level causal interpretations, without claiming separately isolated experimental controls for every intermediate.
- The native full-corpus network recipes fail on warnings elsewhere; this target has no reported network finding. The corpus warning count is not a target-specific curation finding.
- This agent did not author or modify the current record during this task, but historical record authors also used the codex identity; institutional/person-level independence is not established.
- The review changes no record, history, generated product or scientific-status flag. Proposed actions require separate curation authorization.
- All five nodes and four arrows link to source locators and source-based interpretation. The fifteen record EvidenceItems cite the same article; their count is not independent replication.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T073350Z-aspergillus-indium-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Aspergillus indium LCD recovery: whole-record source review'
started_at: '2026-10-19T07:29:02.918763Z'
finished_at: '2026-10-19T07:33:50.881008Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: This agent did not author or modify the current record during
    this task, but historical record authors also used the codex identity; institutional/person-level
    independence is not established.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The fungal LCD bioleaching identity and five-node/four-arrow mechanism are
  supported at abstract resolution. Two major findings concern unsupported functional
  roles and population-tracking readouts; one minor finding concerns environmental
  specificity and outcome placement. No record edits were made.
source:
  git_revision: a4611c913c8da9619673df63a0c2cce3aa206a83
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
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
  - path: conf/reference_validator.yaml
    sha256: 5cd4781c7e15b7c5472f0b008e41764842cc023a7ba99f4273298f421be36652
    role: context
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    sha256: c9ebc23ad2748751ae6a42fbc2340c5f7524a7aa38185bcad4602b7e56734d9d
    role: target
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/records/Aspergillus_Indium_LED_Recovery/2026-10-02T045300Z-codex-d1d786.yaml
    sha256: 5e8e5373813152ec5477702a7ab6669b4370aa3d6265688f41f9cb96129feab0
    role: context
  - path: history/records/Aspergillus_Indium_LED_Recovery/2026-10-05T071439Z-codex-eb16f5.yaml
    sha256: 113610ac109bff59e8ab2f4516023725aa54090b9ab041123c3469b6e18ae36c
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: references_cache/PMID_34111782.txt
    sha256: fc6ad8cf199cbb5c0b6cf7c2607bc953a97f17db3949342e15b472b9e712d85b
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
- kind: maintained
  label: Aspergillus Indium LCD Recovery Platform
  owner_paths:
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  record_class: MicrobialCommunity
  target_id: CommunityMech:000320
scope:
  description: Whole canonical isolate record; every current interaction and downstream
    edge assessed against the primary abstract, with full-text limitations explicit.
  selection: First unreviewed path in the skill corpus kb/communities/*.yaml and data/isolates/*.yaml
    after validated record_review.py list. Initial corpus:462 records,9 targeted by
    existing valid bundles,453 unreviewed. One target in this bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000320
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  command: just --no-dotenv validate data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml data/isolates/Aspergillus_Indium_LED_Recovery.yaml'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-validate
  scope_note: Resolved record and its exact history directory where applicable.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  command: just --no-dotenv validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "uv run python scripts/validate_strict.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml\n\
    Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/communitymech-record-reviews-20261019/reports/instance_validation_failures.tsv"
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-validate-strict
  scope_note: Resolved record and its exact history directory where applicable.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  command: just --no-dotenv validate-terms data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "✅ Validation passed\nuv run linkml-term-validator validate-data data/isolates/Aspergillus_Indium_LED_Recovery.yaml\
    \ -s src/communitymech/schema/communitymech.yaml --labels\n\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 0.00/2.20G [00:00<?, ?B/s]\nDownloading ncbitaxon.db.gz:  \
    \ 0%|          | 128k/2.20G [00:00<33:07, 1.19MB/s]\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 384k/2.20G [00:00<20:07, 1.96MB/s]\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 1.50M/2.20G [00:00<06:17, 6.27MB/s]\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 3.31M/2.20G [00:00<03:31, 11.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 6.12M/2.20G [00:00<02:14, 17.6MB/s]\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 9.88M/2.20G [00:00<01:37, 24.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|          | 15.2M/2.20G [00:00<01:08, 34.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|          | 16.4M/2.20G [00:00<01:28, 26.6MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|          | 18.5M/2.20G [00:00<01:32, 25.3MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|          | 24.1M/2.20G [00:01<01:23, 28.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|          | 25.2M/2.20G [00:01<01:38, 23.8MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|▏         | 30.2M/2.20G [00:01<01:17, 30.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   2%|▏         | 37.6M/2.20G [00:01<00:54, 42.8MB/s]\nDownloading ncbitaxon.db.gz:\
    \   2%|▏         | 40.6M/2.20G [00:01<01:03, 36.7MB/s]\nDownloading ncbitaxon.db.gz:\
    \   2%|▏         | 42.2M/2.20G [00:01<01:16, 30.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   2%|▏         | 49.2M/2.20G [00:01<00:56, 41.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   2%|▏         | 52.9M/2.20G [00:01<00:57, 40.3MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 56.9M/2.20G [00:01<00:57, 40.4MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 62.3M/2.20G [00:02<00:51, 44.9MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 64.3M/2.20G [00:02<01:01, 37.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 65.6M/2.20G [00:02<01:17, 29.8MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 67.1M/2.20G [00:02<01:29, 25.7MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 71.7M/2.20G [00:02<01:11, 31.8MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 76.3M/2.20G [00:02<01:03, 36.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 78.8M/2.20G [00:02<01:09, 33.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   4%|▍         | 85.7M/2.20G [00:02<00:51, 44.4MB/s]\nDownloading ncbitaxon.db.gz:\
    \   4%|▍         | 93.6M/2.20G [00:02<00:40, 55.6MB/s]\nDownloading ncbitaxon.db.gz:\
    \   4%|▍         | 100M/2.20G [00:03<00:38, 59.0MB/s] \nDownloading ncbitaxon.db.gz:\
    \   5%|▍         | 109M/2.20G [00:03<00:32, 69.3MB/s]\nDownloading ncbitaxon.db.gz:\
    \   5%|▌         | 116M/2.20G [00:03<00:32, 69.0MB/s]\nDownloading ncbitaxon.db.gz:\
    \   5%|▌         | 120M/2.20G [00:03<00:48, 46.4MB/s]\nDownloading ncbitaxon.db.gz:\
    \   5%|▌         | 122M/2.20G [00:03<00:55, 40.6MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▌         | 125M/2.20G [00:03<00:58, 38.0MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▌         | 129M/2.20G [00:03<01:00, 37.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▌         | 136M/2.20G [00:03<00:45, 48.7MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▋         | 141M/2.20G [00:03<00:44, 49.4MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▋         | 144M/2.20G [00:04<00:51, 43.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▋         | 145M/2.20G [00:04<01:10, 31.5MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▋         | 146M/2.20G [00:04<01:26, 25.6MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▋         | 146M/2.20G [00:04<01:56, 19.0MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 147M/2.20G [00:04<02:22, 15.5MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 148M/2.20G [00:04<02:54, 12.7MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 148M/2.20G [00:04<03:41, 9.99MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 149M/2.20G [00:04<04:30, 8.18MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 149M/2.20G [00:04<05:00, 7.34MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 150M/2.20G [00:05<05:37, 6.54MB/s]\nDown"
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-validate-terms
  scope_note: Resolved record and its exact history directory where applicable.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  command: just --no-dotenv validate-gtdb data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-validate-gtdb
  scope_note: Resolved record and its exact history directory where applicable.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  command: just --no-dotenv validate-gtdb-domain data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Resolved record and its exact history directory where applicable.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  command: just --no-dotenv validate-references-explained data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "Validating data/isolates/Aspergillus_Indium_LED_Recovery.yaml against\
    \ schema src/communitymech/schema/communitymech.yaml\nCache directory: references_cache\n\
    \nValidation Summary:\n  Reported validation issues: 0\n  All validations passed!\n\
    \n[annotate] This is not a count of checked excerpts (#1469). Native Discussion\
    \ evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-validate-references-explained
  scope_note: Resolved record and its exact history directory where applicable.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  command: just --no-dotenv validate-history history/records/Aspergillus_Indium_LED_Recovery
  exit_code: 0
  expected_exit_code: 0
  summary: No issues found
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-validate-history
  scope_note: Resolved record and its exact history directory where applicable.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  summary: 'Full-corpus command returned 1: 462 records, 57 warnings in 21 records,
    zero errors. The target record has no reported network finding; these corpus warnings
    are not attributed to it.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-audit-network
  scope_note: Repository corpus; target-specific finding count zero.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  summary: 'Full-corpus command returned 1: 462 records, 57 warnings in 21 records,
    zero errors. The target record has no reported network finding; these corpus warnings
    are not attributed to it.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-check-network-quality
  scope_note: Repository corpus; target-specific finding count zero.
- check_id: validate-strict-initial
  name: validate-strict initial dependency attempt
  status: failed
  required: false
  command: just --no-dotenv validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  exit_code: 0
  summary: Initial restricted execution could not access the ontology dependency.
    This attempt was superseded by the successful retry retained above; it is not
    a biological record failure.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-validate-strict-initial
- check_id: validate-terms-initial
  name: validate-terms initial dependency attempt
  status: failed
  required: false
  command: just --no-dotenv validate-terms data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  exit_code: 1
  summary: Initial restricted execution could not access the ontology dependency.
    This attempt was superseded by the successful retry retained above; it is not
    a biological record failure.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-validate-terms-initial
- check_id: validate-gtdb-domain-initial
  name: validate-gtdb-domain initial dependency attempt
  status: failed
  required: false
  command: just --no-dotenv validate-gtdb-domain data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  exit_code: 0
  summary: Initial restricted execution could not access the ontology dependency.
    This attempt was superseded by the successful retry retained above; it is not
    a biological record failure.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - check-validate-gtdb-domain-initial
evidence:
- evidence_id: record
  kind: record_content
  reference: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  locator: Entire record, including five interaction nodes, four downstream arrows,
    four environmental factors and embedded history
  accessed_at: '2026-10-19T07:33:50.878043Z'
  support: supports
  summary: Read the complete canonical MicrobialCommunity record. One fungal monoculture
    is explicitly represented for interoperability; it is not a natural multi-member
    community.
- evidence_id: source
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/34111782/
  locator: PMID:34111782; DOI:10.1016/j.scitotenv.2021.148151; Abstract sentences
    1–7; matching cached text references_cache/PMID_34111782.txt
  accessed_at: '2026-10-19T07:30:31Z'
  support: supports
  summary: The inspected abstract identifies A. niger fermentation broth and waste
    LCD panels; three bioleaching approaches, optimized acid/carboxyl chemistry, increased
    indium recovery, and inhibitory biomass. It does not report the strain, medium,
    vessel, numerical cultivation conditions, or population tracking.
- evidence_id: acid
  kind: primary_source
  reference: PMID:34111782
  locator: Abstract sentences 4–5; references_cache/PMID_34111782.txt
  accessed_at: '2026-10-19T07:30:31Z'
  support: supports
  summary: Carboxyl groups from acids and proteins donate protons for leaching; optimization
    increases proton concentration, effective carboxyl groups and oxalic acid.
  quote: Carboxy groups from organic acids and proteins
- evidence_id: biomass
  kind: primary_source
  reference: PMID:34111782
  locator: Abstract sentence 6; references_cache/PMID_34111782.txt
  accessed_at: '2026-10-19T07:30:31Z'
  support: supports
  summary: Biomass prevents proton contact with the oxide and adsorbs released indium,
    decreasing recovery.
  quote: adsorbed In3+ adverse to indium recovery
- evidence_id: recovery
  kind: primary_source
  reference: PMID:34111782
  locator: Abstract sentence 3; references_cache/PMID_34111782.txt
  accessed_at: '2026-10-19T07:30:31Z'
  support: supports
  summary: Fermentation-method optimization improves the reported recovery endpoint
    from 12.3% to 100%.
  quote: from 12.3% to 100%
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum.PRIMARY_PRODUCER / PRIMARY_DEGRADER; EngineeringDesign.measurement_endpoints;
    EnvironmentalFactor; InteractionDownstream
  accessed_at: '2026-10-19T07:33:50.878043Z'
  support: supports
  summary: PRIMARY_PRODUCER means carbon-fixing autotroph; PRIMARY_DEGRADER means
    complex-substrate degrader. Measurement endpoints are primary experimental readouts.
    Downstream schema stores target and description, with source support located on
    the interaction.
- evidence_id: history
  kind: record_content
  reference: history/records/Aspergillus_Indium_LED_Recovery/
  locator: 2026-10-02T045300Z-codex-d1d786.yaml and 2026-10-05T071439Z-codex-eb16f5.yaml;
    reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml records[0]
  accessed_at: '2026-10-19T07:33:50.878043Z'
  support: supports
  summary: Two append-only history records disclose AI assistance; the earlier graph
    review removed obsolete/cellular transport mappings and explicitly did not certify
    all other metadata. This review makes no new history event or status promotion.
- evidence_id: source-access
  kind: search
  reference: https://www.sciencedirect.com/science/article/pii/S0048969721032228
  locator: Publisher full-text attempt and PubMed abstract, accessed during this review
  accessed_at: '2026-10-19T07:30:09Z'
  support: unknown
  summary: Publisher access returned HTTP 403. Full methods and supplement content
    were not inspected. No claim is made that protocol details are absent from the
    publication.
  search_scope: PubMed PMID 34111782 abstract and publisher URL. Local reference cache,
    history, reports, scripts, kb, data and reviews were searched with rg --no-ignore
    --hidden for PMID 34111782, record slug and label, excluding credential files;
    ignored files included within these named directories.
- evidence_id: check-validate
  kind: validation
  reference: just --no-dotenv validate data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  locator: Exit code 0
  accessed_at: '2026-10-19T07:30:03.931582Z'
  support: context_only
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml data/isolates/Aspergillus_Indium_LED_Recovery.yaml'
- evidence_id: check-validate-strict
  kind: validation
  reference: just --no-dotenv validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  locator: Exit code 0
  accessed_at: '2026-10-19T07:33:07.505264Z'
  support: context_only
  summary: "uv run python scripts/validate_strict.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml\n\
    Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/communitymech-record-reviews-20261019/reports/instance_validation_failures.tsv"
- evidence_id: check-validate-terms
  kind: validation
  reference: just --no-dotenv validate-terms data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  locator: Exit code 0
  accessed_at: '2026-10-19T07:32:35.920504Z'
  support: context_only
  summary: "✅ Validation passed\nuv run linkml-term-validator validate-data data/isolates/Aspergillus_Indium_LED_Recovery.yaml\
    \ -s src/communitymech/schema/communitymech.yaml --labels\n\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 0.00/2.20G [00:00<?, ?B/s]\nDownloading ncbitaxon.db.gz:  \
    \ 0%|          | 128k/2.20G [00:00<33:07, 1.19MB/s]\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 384k/2.20G [00:00<20:07, 1.96MB/s]\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 1.50M/2.20G [00:00<06:17, 6.27MB/s]\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 3.31M/2.20G [00:00<03:31, 11.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 6.12M/2.20G [00:00<02:14, 17.6MB/s]\nDownloading ncbitaxon.db.gz:\
    \   0%|          | 9.88M/2.20G [00:00<01:37, 24.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|          | 15.2M/2.20G [00:00<01:08, 34.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|          | 16.4M/2.20G [00:00<01:28, 26.6MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|          | 18.5M/2.20G [00:00<01:32, 25.3MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|          | 24.1M/2.20G [00:01<01:23, 28.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|          | 25.2M/2.20G [00:01<01:38, 23.8MB/s]\nDownloading ncbitaxon.db.gz:\
    \   1%|▏         | 30.2M/2.20G [00:01<01:17, 30.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   2%|▏         | 37.6M/2.20G [00:01<00:54, 42.8MB/s]\nDownloading ncbitaxon.db.gz:\
    \   2%|▏         | 40.6M/2.20G [00:01<01:03, 36.7MB/s]\nDownloading ncbitaxon.db.gz:\
    \   2%|▏         | 42.2M/2.20G [00:01<01:16, 30.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   2%|▏         | 49.2M/2.20G [00:01<00:56, 41.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   2%|▏         | 52.9M/2.20G [00:01<00:57, 40.3MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 56.9M/2.20G [00:01<00:57, 40.4MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 62.3M/2.20G [00:02<00:51, 44.9MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 64.3M/2.20G [00:02<01:01, 37.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 65.6M/2.20G [00:02<01:17, 29.8MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 67.1M/2.20G [00:02<01:29, 25.7MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 71.7M/2.20G [00:02<01:11, 31.8MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 76.3M/2.20G [00:02<01:03, 36.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   3%|▎         | 78.8M/2.20G [00:02<01:09, 33.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   4%|▍         | 85.7M/2.20G [00:02<00:51, 44.4MB/s]\nDownloading ncbitaxon.db.gz:\
    \   4%|▍         | 93.6M/2.20G [00:02<00:40, 55.6MB/s]\nDownloading ncbitaxon.db.gz:\
    \   4%|▍         | 100M/2.20G [00:03<00:38, 59.0MB/s] \nDownloading ncbitaxon.db.gz:\
    \   5%|▍         | 109M/2.20G [00:03<00:32, 69.3MB/s]\nDownloading ncbitaxon.db.gz:\
    \   5%|▌         | 116M/2.20G [00:03<00:32, 69.0MB/s]\nDownloading ncbitaxon.db.gz:\
    \   5%|▌         | 120M/2.20G [00:03<00:48, 46.4MB/s]\nDownloading ncbitaxon.db.gz:\
    \   5%|▌         | 122M/2.20G [00:03<00:55, 40.6MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▌         | 125M/2.20G [00:03<00:58, 38.0MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▌         | 129M/2.20G [00:03<01:00, 37.1MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▌         | 136M/2.20G [00:03<00:45, 48.7MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▋         | 141M/2.20G [00:03<00:44, 49.4MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▋         | 144M/2.20G [00:04<00:51, 43.2MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▋         | 145M/2.20G [00:04<01:10, 31.5MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▋         | 146M/2.20G [00:04<01:26, 25.6MB/s]\nDownloading ncbitaxon.db.gz:\
    \   6%|▋         | 146M/2.20G [00:04<01:56, 19.0MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 147M/2.20G [00:04<02:22, 15.5MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 148M/2.20G [00:04<02:54, 12.7MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 148M/2.20G [00:04<03:41, 9.99MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 149M/2.20G [00:04<04:30, 8.18MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 149M/2.20G [00:04<05:00, 7.34MB/s]\nDownloading ncbitaxon.db.gz:\
    \   7%|▋         | 150M/2.20G [00:05<05:37, 6.54MB/s]\nDown"
- evidence_id: check-validate-gtdb
  kind: validation
  reference: just --no-dotenv validate-gtdb data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  locator: Exit code 0
  accessed_at: '2026-10-19T07:30:01.566509Z'
  support: context_only
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: just --no-dotenv validate-gtdb-domain data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  locator: Exit code 0
  accessed_at: '2026-10-19T07:32:41.711022Z'
  support: context_only
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py data/isolates/Aspergillus_Indium_LED_Recovery.yaml'
- evidence_id: check-validate-references-explained
  kind: validation
  reference: just --no-dotenv validate-references-explained data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  locator: Exit code 0
  accessed_at: '2026-10-19T07:30:19.710022Z'
  support: context_only
  summary: "Validating data/isolates/Aspergillus_Indium_LED_Recovery.yaml against\
    \ schema src/communitymech/schema/communitymech.yaml\nCache directory: references_cache\n\
    \nValidation Summary:\n  Reported validation issues: 0\n  All validations passed!\n\
    \n[annotate] This is not a count of checked excerpts (#1469). Native Discussion\
    \ evidence coverage remains incomplete (#476)."
- evidence_id: check-validate-history
  kind: validation
  reference: just --no-dotenv validate-history history/records/Aspergillus_Indium_LED_Recovery
  locator: Exit code 0
  accessed_at: '2026-10-19T07:30:05.774660Z'
  support: context_only
  summary: No issues found
- evidence_id: check-audit-network
  kind: validation
  reference: just --no-dotenv audit-network
  locator: Exit code 1
  accessed_at: '2026-10-19T07:30:27.845593Z'
  support: context_only
  summary: 'Full-corpus command returned 1: 462 records, 57 warnings in 21 records,
    zero errors. The target record has no reported network finding; these corpus warnings
    are not attributed to it.'
- evidence_id: check-check-network-quality
  kind: validation
  reference: just --no-dotenv check-network-quality
  locator: Exit code 1
  accessed_at: '2026-10-19T07:30:43.193891Z'
  support: context_only
  summary: 'Full-corpus command returned 1: 462 records, 57 warnings in 21 records,
    zero errors. The target record has no reported network finding; these corpus warnings
    are not attributed to it.'
- evidence_id: check-validate-strict-initial
  kind: validation
  reference: just --no-dotenv validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  locator: Initial attempt; exit 0
  accessed_at: '2026-10-19T07:30:15.013723Z'
  support: context_only
  summary: Initial restricted execution could not access the ontology dependency.
    This attempt was superseded by the successful retry retained above; it is not
    a biological record failure.
- evidence_id: check-validate-terms-initial
  kind: validation
  reference: just --no-dotenv validate-terms data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  locator: Initial attempt; exit 1
  accessed_at: '2026-10-19T07:30:15.537445Z'
  support: context_only
  summary: Initial restricted execution could not access the ontology dependency.
    This attempt was superseded by the successful retry retained above; it is not
    a biological record failure.
- evidence_id: check-validate-gtdb-domain-initial
  kind: validation
  reference: just --no-dotenv validate-gtdb-domain data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  locator: Initial attempt; exit 0
  accessed_at: '2026-10-19T07:30:13.938385Z'
  support: context_only
  summary: Initial restricted execution could not access the ontology dependency.
    This attempt was superseded by the successful retry retained above; it is not
    a biological record failure.
assessments:
- assessment_id: identity
  area: identity
  topic: Isolate platform identity and experimental scope
  outcome: supported
  summary: The identity is a laboratory A. niger fermentation-broth platform for indium
    recovery from LCD waste. ENGINEERED origin/state and BIOMINING category agree
    with that scope. The legacy filename contains LED but the name, source and current
    claims consistently specify LCD; this is not mistaken biological identity.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - source
  dimensions:
  - name: source_strain
    value: Aspergillus niger; strain not specified in inspected abstract
    definition: Source resolution retained without inventing a strain accession.
    evidence_ids:
    - source
  - name: community_scope
    value: Engineered single-member fungal platform
    definition: Explicit monoculture represented using MicrobialCommunity; no interspecies
      interaction inferred.
    evidence_ids:
    - record
    - source
  - name: experimental_setting
    value: Laboratory fermentation broth applied to waste LCD panels
    definition: Experimental material and process inspected at abstract resolution.
    evidence_ids:
    - source
  - name: medium_environment
    value: Laboratory environment; cultivation recipe and vessel unresolved
    definition: No numerical cultivation conditions inferred from the abstract.
    evidence_ids:
    - record
    - source
  - name: source_category
    value: Primary experimental article abstract
    definition: Current review did not inspect full methods or supplements.
    evidence_ids:
    - source
    - source-access
- assessment_id: composition
  area: grounding
  topic: Taxonomy, functional roles and abundance scope
  outcome: concern
  summary: A. niger is the reported fermentation organism and its sole-member representation
    is explicit. Monoculture abundance wording does not assert a measured relative
    abundance. However PRIMARY_PRODUCER asserts autotrophy under the schema, and PRIMARY_DEGRADER
    asserts complex-substrate degradation; neither is established by the cited organic-acid
    bioleaching experiment. NO_GTDB_EQUIVALENT is appropriate in scope for this fungal
    taxon.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - source
  - schema
- assessment_id: engineering
  area: scope
  topic: Engineering design and measured endpoints
  outcome: concern
  summary: The objective, three-approach perturbation and recovery/mechanism characterization
    match the abstract. Member-level abundance and persistence tracking is an unsupported
    added readout; the attached carboxyl-group snippet does not establish it.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - source
  - schema
- assessment_id: environment
  area: representation
  topic: Environment, cultivation and outcome fields
  outcome: concern
  summary: Laboratory setting is supported but the preferred wording laboratory bioreactor
    is more specific than the inspected source. The record appropriately withholds
    numerical medium/temperature/pulp-density claims. EnvironmentalFactor[0] is a
    recovery outcome rather than an environmental condition; entries [1–3] describe
    process chemistry, tunability and biomass inhibition. Their prose is abstract-supported,
    but should not be treated as a reproducible growth protocol.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - source
  - schema
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Optimization'
  outcome: supported
  summary: 'Participant/source: A. niger (NCBITaxon:5061); no second microbial target;
    COMMUNITY_LEVEL process in the engineered LCD-waste fermentation system. Fermentation
    optimization increases proton concentration, effective carboxyl groups and oxalic
    acid output. GO:0019752 is consistent with the described acid chemistry at this
    broad level; no specific pathway or enzyme is demonstrated.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - acid
  - source
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Proton release'
  outcome: supported
  summary: 'Participant/source: A. niger (NCBITaxon:5061); no second microbial target;
    COMMUNITY_LEVEL process in the engineered LCD-waste fermentation system. Acid/protein
    carboxyl groups supply protons for indium leaching. This is extracellular chemical
    dissolution, not cellular metal transport.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - acid
  - source
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Dissolution'
  outcome: supported
  summary: 'Participant/source: A. niger (NCBITaxon:5061); no second microbial target;
    COMMUNITY_LEVEL process in the engineered LCD-waste fermentation system. The oxide-bearing
    LCD material is leached by fermentation broth. Indium(3+) denotes the released/adsorbed
    ion. The source supports a leaching mechanism, with no cellular uptake claim.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - acid
  - source
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Biomass inhibition'
  outcome: supported
  summary: 'Participant/source: A. niger (NCBITaxon:5061); no second microbial target;
    COMMUNITY_LEVEL process in the engineered LCD-waste fermentation system. A. niger
    biomass blocks proton contact and adsorbs released indium; the effect on recovery
    is negative.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - biomass
  - source
- assessment_id: node-4
  area: graph
  topic: 'ecological_interactions[4]: Recovery'
  outcome: supported
  summary: 'Participant/source: A. niger (NCBITaxon:5061); no second microbial target;
    COMMUNITY_LEVEL process in the engineered LCD-waste fermentation system. The observed
    optimized recovery rises from 12.3% to 100%; the abstract also supports further
    process-parameter tuning without giving settings.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - recovery
  - source
- assessment_id: edge-0-1
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: 'From node [0] to named node [1], within the same A. niger broth/LCD process;
    no interspecies target. Positive: optimized chemistry supplies the proton-donating
    groups used for leaching. This joins the abstract component and mechanism statements;
    it is not proof of separately controlled causal intermediates.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - acid
  - source
- assessment_id: edge-1-2
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: supported
  summary: 'From node [1] to named node [2], within the same A. niger broth/LCD process;
    no interspecies target. Positive: carboxyl-group proton donation enables metal-oxide
    leaching. Abstract-level chemical causal interpretation is supported.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - acid
  - source
- assessment_id: edge-2-4
  area: graph
  topic: ecological_interactions[2].downstream[0]
  outcome: supported
  summary: 'From node [2] to named node [4], within the same A. niger broth/LCD process;
    no interspecies target. Positive: mobilization by oxide leaching produces recovered
    indium in broth. The abstract supports recovery but does not give a separate mass-balance
    experiment for this arrow.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - recovery
  - source
- assessment_id: edge-3-4
  area: graph
  topic: ecological_interactions[3].downstream[0]
  outcome: supported
  summary: 'From node [3] to named node [4], within the same A. niger broth/LCD process;
    no interspecies target. Negative: biomass prevents proton contact and adsorbs
    indium, reducing recovery. The description correctly preserves inhibition.'
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - biomass
  - source
- assessment_id: ingredients
  area: evidence
  topic: Chemicals, metals, environmental evidence and resource scope
  outcome: supported
  summary: Oxalic acid, proton/hydron, protein and indium(3+) are assigned roles matching
    the abstract. Related ingredients are process products/reactants, not a fabricated
    medium recipe. All four environmental statements and all three ingredient snippets
    are supported at abstract resolution. The recovered metal is indium; iron is competition
    context rather than an asserted second target. No genomic dataset, accession or
    external-resource assertion is present to certify.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - source
  - acid
  - biomass
  - recovery
- assessment_id: provenance
  area: provenance
  topic: Curation history and unresolved discussion
  outcome: supported
  summary: Embedded and append-only history describe the GO cleanup and graph scope
    repair. The open discussion explicitly asks for condition-specific controls and
    acknowledges abstract-level evidence. The complete methods remain unresolved;
    this review does not declare the reported mechanism false.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - history
  - source-access
- assessment_id: imodulondb
  area: evidence
  topic: Structured transcriptomics source applicability
  outcome: not_applicable
  summary: No gene, locus tag, UniProt accession, regulator or transcriptomics dataset
    is asserted, and no source strain is identified. The single broad GO process is
    chemical/metabolic context rather than a specific expression-module claim; no
    iModulonDB cross-check would establish this extracellular fungal bioleaching experiment.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - source
- assessment_id: grounding
  area: grounding
  topic: Ontology and GTDB verification
  outcome: supported
  summary: NCBITaxon:5061 represents the reported A. niger; ENVO:01001405 is laboratory
    environment. Chemistry descriptors are CHEBI:16995 oxalic acid, CHEBI:15378 hydron,
    CHEBI:36080 protein, CHEBI:49664 indium(3+), with GO:0019752 carboxylic acid metabolic
    process. Validator evidence below determines identifier/label verification coverage;
    ontology validity alone does not establish the experimental role.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - check-validate-terms
  - check-validate-gtdb
  - check-validate-gtdb-domain
  dimensions:
  - name: taxon_grounding
    value: NCBITaxon:5061; NO_GTDB_EQUIVALENT
    definition: Species-level fungal identity; no GTDB strain genome mapping claimed.
    evidence_ids:
    - record
    - check-validate-gtdb-domain
- assessment_id: scores
  area: completeness
  topic: Native completeness and validation-quality scores
  outcome: concern
  summary: The rubric yields completeness 80 and validation quality 100 despite two
    major and one minor finding; capped scores do not constitute scientific approval.
    Required metadata earns the 50-point block. There are four environmental entries,
    five interactions, six interaction-level evidence items, no growth-medium block,
    no associated dataset and no external resource. The five-node/four-arrow graph
    is connected and has no network-audit finding for this target.
  target_ids:
  - CommunityMech:000320
  evidence_ids:
  - record
  - schema
  - check-audit-network
  - source
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 for id/name/description/taxonomy-with-roles/ecological_state/community_category
      +5 environment +10 at least three environmental factors +10 at least three interactions
      +5 external resources +10 growth_media +5 associated_datasets +5 any interaction
      metabolites). Applied:50+5+10+10+0+0+0+5=80.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 -50*P1 -10*P2 -2*P3 +20*min(mean_interaction_evidence/2,1)
      +15 for COMPLETE network,0,100). P1=0; P2=2; P3=1; evidence=6/5=1.2; COMPLETE
      target graph. Raw105, capped100. Unavailable checks, if any, are explicit limitations
      rather than assumed passing evidence.
  - name: P1
    value: 0
    unit: findings
    definition: Normalized blocker findings for this target.
  - name: P2
    value: 2
    unit: findings
    definition: Normalized major findings for this target.
  - name: P3
    value: 1
    unit: findings
    definition: Normalized minor findings for this target.
  - name: interaction_evidence
    value: 1.2
    unit: evidence items per interaction
    denominator: 5
    definition: Six EvidenceItem entries directly attached to five interaction nodes;
      repeated citation counts as separate assertion evidence, not independent publications.
findings:
- finding_id: roles
  issue_key: cm-000320-functional-role-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Functional roles assert metabolism unsupported by the cited experiment
  description: PRIMARY_PRODUCER explicitly means carbon-fixing autotroph in the maintained
    schema. PRIMARY_DEGRADER means complex-substrate degradation. The inspected source
    supports fungal organic-acid fermentation and extracellular leaching, not these
    ecological roles. Producing an acid does not establish autotrophy, and dissolving
    metal oxide is not evidence of degrading complex organic substrate.
  target_ids:
  - CommunityMech:000320
  field_paths:
  - taxonomy[0].functional_role
  evidence_ids:
  - record
  - schema
  - source
  rule_id: P2.4
  native_severity: P2
  normalization_reason: 'P2 major: the annotation asserts a materially unsupported
    biological or experimental property.'
  owner_paths:
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
- finding_id: readout
  issue_key: cm-000320-unsubstantiated-population-readout
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Member abundance and persistence tracking is not supported by inspected evidence
  description: engineering_design.measurement_endpoints[1] asserts member-level abundance
    and persistence tracking. The complete inspected abstract reports indium leaching
    efficiency, broth chemistry and biomass inhibition, but no population-tracking
    assay. The nearest cited snippet describes carboxyl-group proton donation. This
    is a bounded evidence gap, not a claim that full methods exclude every growth
    measurement.
  target_ids:
  - CommunityMech:000320
  field_paths:
  - engineering_design.measurement_endpoints[1]
  - engineering_design.evidence[0]
  evidence_ids:
  - record
  - source
  - source-access
  rule_id: CLAUDE.claim-level-evidence
  native_severity: P2
  normalization_reason: 'P2 major: the annotation asserts a materially unsupported
    biological or experimental property.'
  owner_paths:
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
- finding_id: environment
  issue_key: cm-000320-environment-outcome-placement
  category: representation
  severity: minor
  status: open
  certainty: confirmed
  title: Environment wording and outcome placement imply more protocol detail than
    supported
  description: environment_term.preferred_term says laboratory bioreactor although
    the inspected abstract identifies fermentation systems without a vessel. environmental_factors[0]
    stores 100% indium recovery as an environmental parameter, whereas it is a measured
    outcome. The value is sourced correctly; the concern is representation and specificity.
  target_ids:
  - CommunityMech:000320
  field_paths:
  - environment_term.preferred_term
  - environmental_factors[0]
  evidence_ids:
  - record
  - schema
  - source
  rule_id: review-checklist.environment-cultivation
  native_severity: P3
  normalization_reason: 'P3 minor: the issue affects field meaning without changing
    platform identity.'
  owner_paths:
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
actions:
- action_id: fix-roles
  description: Curate the role list against the actual fermentation experiment; remove
    unsupported roles or replace them only with a directly evidenced role.
  finding_ids:
  - roles
  target_ids:
  - CommunityMech:000320
  owner_paths:
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  acceptance_checks:
  - Each retained role must have a precise source passage supporting its schema definition
    for this experiment.
  - just validate data/isolates/Aspergillus_Indium_LED_Recovery.yaml; just validate-strict
    data/isolates/Aspergillus_Indium_LED_Recovery.yaml; just validate-references-explained
    data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  - If curation is separately authorized, append history and regenerate/check affected
    docs using just gen-html and just check-docs-current.
- action_id: fix-readout
  description: Replace the unsupported population-tracking endpoint with source-backed
    reported readouts, or retain it only after obtaining direct methods/results evidence.
  finding_ids:
  - readout
  target_ids:
  - CommunityMech:000320
  owner_paths:
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  acceptance_checks:
  - Every measurement endpoint must be supported by a source passage identifying that
    assay/readout in this experiment.
  - just validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml; just
    validate-references-explained data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  - Re-review the engineering-design evidence at assertion level; do not infer abundance
    tracking from the mere presence of biomass.
- action_id: fix-environment
  description: Use source-supported laboratory-setting wording and represent indium-recovery
    efficiency as an experimental outcome rather than a growth condition.
  finding_ids:
  - environment
  target_ids:
  - CommunityMech:000320
  owner_paths:
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  acceptance_checks:
  - A bioreactor/vessel claim requires a direct methods passage; otherwise retain
    laboratory-environment scope.
  - The reported 12.3% to 100% recovery result remains preserved in an outcome context.
  - just validate-strict data/isolates/Aspergillus_Indium_LED_Recovery.yaml; just
    validate-terms data/isolates/Aspergillus_Indium_LED_Recovery.yaml; just validate-references-explained
    data/isolates/Aspergillus_Indium_LED_Recovery.yaml
limitations:
- Scientific source assessment is limited to the complete primary abstract and matching
  committed cache. Publisher full text returned HTTP 403; methods and supplementary
  evidence were not inspected.
- Source strain, cultivation medium, vessel, temperature, pH and pulp density remain
  unresolved at this source tier; their omission is not an instruction to fabricate
  details.
- Graph arrows retain abstract-level causal interpretations, without claiming separately
  isolated experimental controls for every intermediate.
- The native full-corpus network recipes fail on warnings elsewhere; this target has
  no reported network finding. The corpus warning count is not a target-specific curation
  finding.
- This agent did not author or modify the current record during this task, but historical
  record authors also used the codex identity; institutional/person-level independence
  is not established.
notes:
- The review changes no record, history, generated product or scientific-status flag.
  Proposed actions require separate curation authorization.
- All five nodes and four arrows link to source locators and source-based interpretation.
  The fifteen record EvidenceItems cite the same article; their count is not independent
  replication.
tags:
- record-review
- isolate
- abstract-evidence
- batch-01
```
