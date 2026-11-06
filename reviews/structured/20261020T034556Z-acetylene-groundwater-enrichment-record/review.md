# Acetylene-fueled groundwater enrichment: whole-record review

- Review: 20261020T034556Z-acetylene-groundwater-enrichment-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-20T03:43:12.793406Z
- Finished UTC: 2026-10-20T03:45:56.542534Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Community hydrogen transfer and both process arrows are supported, with genomic producer uncertainty retained. Four major findings concern cultivation-stage scope, member resolution, functional roles and evidence type. Two minor findings concern the missing structured hydrogen and dataset links. Focused gates pass; corpus warning failures remain explicit.

## Scope And Provenance

Whole target: two taxa, three nodes, two arrows, all 16 evidence items and primary full-text article.

Selection: Second remaining record of batch 02 in path order, using baseline plus validated pending batch-01 coverage.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a4611c913c8da9619673df63a0c2cce3aa206a83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000238 | kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml | maintained | Acetylene-Fueled Trichloroethene Dechlorination Groundwater Enrichment |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000238 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml |
| validate-strict | passed | True | CommunityMech:000238 | uv run python scripts/validate_strict.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml --out /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000238 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000238 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000238 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml |
| validate-history | passed | True | CommunityMech:000238 | No issues found |
| normalize-cache-names-check | passed | True | CommunityMech:000238 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000238 | Validating kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000238 | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| check-network-quality | failed | True | CommunityMech:000238 | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| Optional structured-source adapter | unavailable | False | CommunityMech:000238 | Runner unavailable in isolated runtime; inspected public catalog fallback has no matching organism. |

## Scientific And Domain Assessments

### Community identity and provenance

identity: supported. Targets: CommunityMech:000238.

This is the stable native-groundwater-derived enrichment 36BR-A-TCE, selected in the laboratory, not a defined two-isolate synthetic culture. NATURAL origin and ENGINEERED state distinguish origin from manipulation. The source site had historical bioaugmentation; native-population attribution is argued from composition/phylogenetic comparisons, not direct field proof of active coupling. Earlier synthetic Pelobacter SFB93/strain 195 or BAV1 pairs remain background comparators.

### taxonomy[0..1], taxon roles and resolution

grounding: concern. Targets: CommunityMech:000238.

Existing NCBI/GTDB broad ranks resolve and coherence gates pass, but full text identifies the dechlorinator more precisely than Bacteria and the candidate producer as Coriobacteriales. The source does not establish a cultured producer isolate. Both PRIMARY_DEGRADER assignments exceed the complex-substrate definition; donor CROSS_FEEDER lacks demonstrated incoming cross-fed substrate. Other detected taxa are not an obligatory minimal consortium.

### ecological_interactions[0]: Acetylenotrophy Provides Reductant for Dechlorination

graph: concern. Targets: CommunityMech:000238.

Community-level cross-feeding is supported by hydrogen balance and solvent reduction. Producer Actinomycetota/Coriobacteriales attribution is correctly qualified as genomic, and the recipient broad Bacteria guild is structurally declared but unnecessarily vague. Acetylene/TCE/PCE are valid substrates; the transferred hydrogen is missing from structured metabolites. Anaerobic respiration describes the recipient process, not the donor fermentation.

### ecological_interactions[0].downstream[0] -&gt; Reductive Dechlorination of TCE and PCE

graph: supported. Targets: CommunityMech:000238.

Positive enabling direction from acetylene-fermenting community to dechlorination via hydrogen. Mass balances and concentration trajectories support this enrichment-level edge. Exact isolated donor/recipient attribution, reciprocal benefit and thermodynamic product-removal dependence remain unproven.

Declared donor NCBITaxon:201174; declared recipient NCBITaxon:2. Mechanism: hydrogen cross-feeding. Context: stable 36BR-A-TCE, differentiated TCE/PCE assays. Exact shared quotation and locator: transfer.

### ecological_interactions[1]: Reductive Dechlorination of TCE and PCE

graph: supported. Targets: CommunityMech:000238.

COMMUNITY_LEVEL with no specific participant is allowed. Measured endpoints are chiefly vinyl chloride, with limited ethene in some conditions; the record appropriately avoids complete detoxification. TCE/PCE chemicals and anaerobic respiration are valid. A future more resolved participant can follow the source genome evidence without claiming a purified isolate experiment.

### ecological_interactions[2]: Acetylene as Sole Electron Donor and Carbon Source

graph: supported. Targets: CommunityMech:000238.

The sole organic-donor amendment is supported. The participating producer is inferred genomically; the node is a community substrate condition, not proof of a producer-only isolate phenotype. Inorganic CO2 and mineral/vitamin nutrients remain compatible with sole organic carbon wording.

### ecological_interactions[2].downstream[0] -&gt; Acetylenotrophy Provides Reductant for Dechlorination

graph: supported. Targets: CommunityMech:000238.

Positive substrate-supply direction: acetylene amendment enables community fermentation and downstream reductant supply. No niche partitioning is inferred. Candidate Coriobacteriales assignment remains genomic while community consumption is experimentally observed.

Upstream condition lists NCBITaxon:201174; transfer node addresses NCBITaxon:2 recipient. Mechanism and context: acetylene-supported stable enrichment, with measured consumption/hydrogen balance. Exact short source quotations: sole and transfer.

### cultivation_setup[0], engineering_design, growth_media and environmental_factors

scope: concern. Targets: CommunityMech:000238.

The recorded setup belongs to the initial acetylenotrophic enrichment, not the full stable dechlorinating system. The claim that the larger format appears only in captions is contradicted by Methods. Source medium and incubation information exist, but growth_media is empty. Engineering objectives and two environmental factors are supported when source-field mineral chemistry is distinguished from laboratory amendment. The setup problem includes the missing stage-specific medium representation.

### Environment, ingredients and metal scope

grounding: supported. Targets: CommunityMech:000238.

Laboratory environment and modeled groundwater are correctly separate. Acetylene, trichloroethene and tetrachloroethene match their curated IDs and functional substrate roles. Mineral-mediated abiotic acetylene formation is source background, not a demonstrated metal-processing function of the enrichment; NOT_APPLICABLE metal relevance is reasonable. No abundance score is asserted in this record.

### All 16 evidence snippets, provenance and uncertainty

evidence: concern. Targets: CommunityMech:000238.

All snippets match; the taxon-identification snippet explicitly describes metagenomic analysis yet is tagged IN_VITRO. That overstates the assignment method even though the community itself was grown experimentally. The open producer-validation discussion accurately preserves unisolated-organism and enzyme uncertainty. Citations resolve; source-advertised datasets remain unrepresented.

### Structured source cross-check

evidence: not_applicable. Targets: CommunityMech:000238.

No matching public expression-module dataset is available in the inspected catalog. This does not count against the genomic or experimental evidence.

### Native focused validation and graph integrity

schema: supported. Targets: CommunityMech:000238.

All eight focused/preflight checks pass and cache bytes remain unchanged. Two arrows target declared nodes; both listed taxa participate somewhere in the graph. The community-level dechlorination node can omit participants. Native COMPLETE is structural, not proof of exact organism attribution. Required corpus warning failures remain explicit.

### Native completeness and validation quality

completeness: concern. Targets: CommunityMech:000238.

Completeness is 75 and quality approximately 87.67; neither score removes four major and two minor findings. Five directly attached node EvidenceItems derive from one paper.

## Findings

### cultivation-context: Initial microcosm setup substitutes for the stable dechlorinating enrichment

major / open / confirmed; issue key: cm-000238-cultivation-context.

The record omits the stable 36BR-A-TCE setup and falsely says its vessel format appears only in table captions. Methods explicitly distinguish the successive enrichment stages and their media. An empty growth_media list loses source-reported medium context.

### member-resolution: Full-text member assignments remain hidden behind broad guilds

major / open / confirmed; issue key: cm-000238-member-resolution.

The Bacteria dechlorinating guild is justified only by abstract limitations although Results identify a D. mccartyi genome and its likely role. The candidate acetylene producer can be represented at Coriobacteriales order while preserving inference. Neither update licenses an exact reference-isolate substitution.

### functional-roles: Taxon roles do not match the schema definitions

major / open / confirmed; issue key: cm-000238-functional-roles.

PRIMARY_DEGRADER requires complex-substrate degradation, which is not established by acetylene fermentation or chlorinated-solvent respiration. The candidate acetylene donor is CROSS_FEEDER although no incoming partner-derived metabolite use is demonstrated.

### evidence-type: Genomic producer identification is labeled as an in-vitro assignment

major / open / confirmed; issue key: cm-000238-evidence-type.

taxonomy[0].evidence[0] supports producer identity through metagenomic analysis, not isolation or biochemical testing. IN_VITRO conflates the experimental cultivation setting with the taxon-attribution method.

### hydrogen-metabolite: The exchanged hydrogen is missing from structured metabolites

minor / open / confirmed; issue key: cm-000238-hydrogen-metabolite.

The transfer node describes and evidences hydrogen exchange but lists only acetylene and chlorinated substrates. The supported exchanged molecule is unavailable to structured metabolite queries.

### dataset-links: Source-advertised datasets are not represented

minor / open / confirmed; issue key: cm-000238-dataset-links.

The paper names BioProject/SRA, genome collection and USGS cultivation data, while associated_datasets is empty. External availability was not independently checked, so only a source-backed linkage follow-up is asserted.

## Recommended Actions And Acceptance Checks

### fix-cultivation-context

Separate initial acetylenotrophic enrichment from stable dechlorination characterization, retaining source-specific medium and incubation context.

- Stable-community setup is traceable to the correct Methods passage.
- Remove the false caption-only assertion and avoid mixing stages into one recipe.
- Use exact verified medium links only where available.
- Run strict, term and reference validation after authorized curation.

### fix-member-resolution

Represent the source-supported member resolution and propagate consistent participant descriptors, retaining genome-based uncertainty.

- Dechlorinator and candidate producer are distinguished at source-supported ranks with authority-verified IDs.
- No inference of an obligatory two-member minimal community.
- Reference-strain similarity remains distinct from environmental genome identity.
- Run GTDB, term, strict and network gates.

### fix-functional-roles

Choose supported role semantics or document an unresolved vocabulary gap; do not turn hydrogen donation into proven consumption.

- Every role matches a defined activity supported by the correct source context.
- No unsupported reciprocal transfer is inferred.
- Run strict and network gates.

### fix-evidence-type

Use the schema-supported evidence classification for genomic/computational attribution and preserve partial organism-level certainty.

- Evidence type describes the actual identification method.
- Measured community function remains distinct from inferred producer identity.
- Run strict and reference checks.

### fix-hydrogen-metabolite

Represent the directly supported exchange molecule with a verified chemical identifier and claim-level evidence.

- Chemical identity matches molecular hydrogen, not a different hydrogen species.
- Do not add acetate transfer as measured merely because it is biologically plausible.
- Run term, strict and reference checks.

### fix-dataset-links

Verify the primary advertised accessions and add only resolved links with the correct dataset scope.

- Accessions resolve and distinguish amplicon, metagenome and cultivation data.
- Do not treat advertised availability as verified retrieval.
- Run strict and resource-reference checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml; Entire record, two taxa, three nodes and two arrows | supports | The record denotes groundwater-derived stable enrichment 36BR-A-TCE, not the preceding synthetic Pelobacter/Dehalococcoides cocultures. Canonical record remains unchanged. |
| primary | PMID:33531396; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7858054/fullTextXML; Abstract, Results, Discussion, Materials and Methods, main figures and data availability | supports | Measured acetylene consumption, hydrogen balance and chlorinated-solvent reduction support community coupling. Metagenomics identifies candidate Coriobacteriales and a D. mccartyi genome; biochemical producer validation remains open. Initial acetylenotrophic microcosms and stable TCE enrichment are separate experimental stages. |
| transfer | PMID:33531396; Results: C2H2 fuels PCE and TCE dechlorination | supports | Hydrogen measurements and mass balance support community-level transfer, without isolating an exact donor-recipient pair. |
| sole | PMID:33531396; Discussion opening | supports | Acetylene supply supports the upstream substrate edge; sole organic substrate does not mean absence of inorganic carbon or nutrients. |
| methods | PMID:33531396; Materials and Methods: Bacterial cultures and growth conditions | supports | Stable 36BR-A-TCE used a different medium and vessel context from initial SeFr1 microcosms. |
| identity-source | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=33531396&amp;retmode=xml; PMID, DOI, PMCID and article title | supports | PMID 33531396, DOI 10.1128/mBio.02724-20 and PMC7858054 identify the cited Gushgari-Doyle et al. 2021 mBio paper. |
| composition | PMID:33531396; Results: Composition of acetylenotrophic enrichment cultures; Discussion paragraphs 2–6 | supports | D. mccartyi is the presumed dechlorinator, with a recovered genome and reductive-dehalogenase evidence. Coriobacteriales is the candidate acetylene-fermenting population. Genome-derived relative abundance differs from 16S estimates and must retain method context. Methanosaeta concilii and Methanobacterium are also detected; methane production is condition-specific. A genome closest to DCMB5 is not permission to substitute a reference isolate without retaining the actual environmental genome identity. |
| setup | PMID:33531396; Methods: Bacterial cultures and growth conditions; Results/Figure 1 | supports | The initial groundwater/SeFr1 microcosms and the stable BAV1-medium TCE enrichment are explicitly distinguished in Methods. The larger stable-enrichment vessel is described in prose as well as the figure caption; the record says it occurs only in table captions. A documented incubation context and serial enrichment history are omitted. This review identifies the mismatch without converting it into an operational protocol. |
| datasets | PMID:33531396; Methods: Data availability; reference 89 | supports | The source advertises BioProject PRJNA615907, SRA SRX8026671–SRX8026678, a ggKbase LAC_acetylene_final collection and USGS data release DOI 10.5066/P9BF8LM4. These are source-advertised candidate links, not independently verified dataset availability. |
| ontology | OAK local SemanticSQL NCBITaxon, CHEBI, ENVO and GO snapshots; All seven unique IDs; ontology-authority.json | supports | All curated IDs have matching canonical labels. Laboratory environment and groundwater fit separate experimental/source contexts. Anaerobic respiration fits organohalide respiration; acetylene fermentation should not be described as respiration merely because the recipient respires. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum and evidence definitions | supports | PRIMARY_DEGRADER means degradation of complex substrates; CROSS_FEEDER means utilization of metabolites from other taxa. Acetylene consumption and organohalide respiration do not establish complex-substrate degradation, and a donor is not automatically a consumer. |
| snippets | kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml; Every one of 16 EvidenceItem occurrences; paragraph-aware XML extraction | supports | All 16 snippets match the primary source after NFKC and whitespace normalization, preserving chemical subscripts without inserted spaces. Exact matches do not establish correct evidence type or experimental scope. |
| history | history/records/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment/2026-10-05T055201Z-codex-fdadde.yaml; Whole history event and corresponding seven-record graph decision | supports | Prior graph review retained community transfer and sole-substrate arrows, bounded the endpoint to vinyl chloride and preserved producer uncertainty. It explicitly did not certify other metadata. |
| local-search | references_cache; history/records; reports/causal_graph_review/decisions; kb/taxa; Ignored-inclusive identifier/slug/citation search | supports | Located both cache forms, history and prior graph decision. The Markdown cache includes appended full text despite its abstract_only front matter. No medium/dataset entries are present in the whole target; no global external-registry absence is claimed. |
| adapter | https://imodulondb.org/api/datasets; Same-session public catalog, 20 organisms and 28 datasets | context_only | No matching environmental Coriobacteriales population or D. mccartyi dataset appears. An unrelated model-organism expression module cannot validate the candidate acetylene hydratase. Optional runner remains unavailable in the isolated runtime. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml; Actual execution 2026-10-20T03:43:17.311796+00:00 to 2026-10-20T03:43:17.927918+00:00 | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml --out /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv; Actual execution 2026-10-20T03:43:17.311956+00:00 to 2026-10-20T03:43:19.063574+00:00 | supports | uv run python scripts/validate_strict.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml --out /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml; Actual execution 2026-10-20T03:43:17.312142+00:00 to 2026-10-20T03:43:18.993879+00:00 | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml; Actual execution 2026-10-20T03:43:17.928216+00:00 to 2026-10-20T03:43:18.000725+00:00 | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml; Actual execution 2026-10-20T03:43:18.000981+00:00 to 2026-10-20T03:43:19.130597+00:00 | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-history history/records/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment; Actual execution 2026-10-20T03:43:18.994212+00:00 to 2026-10-20T03:43:19.579294+00:00 | supports | No issues found |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-20T03:43:19.579952+00:00 to 2026-10-20T03:43:19.641128+00:00 | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml; Actual execution 2026-10-20T03:43:19.641362+00:00 to 2026-10-20T03:43:20.510047+00:00 | supports | Validating kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | just --no-dotenv audit-network; Actual run finished 2026-10-19T07:30:27.845593+00:00 | supports | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| check-check-network-quality | just --no-dotenv check-network-quality; Actual run finished 2026-10-19T07:30:43.193891+00:00 | supports | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |

## Limits And Additional Notes

- Main article and embedded figure/table captions were inspected. Separate supplementary downloads, raw sequence reads and cultivation data were not reanalyzed.
- Source-advertised dataset accessions and genome collection were not independently retrieved; proposed linkages require verification.
- No isolate biochemical validation of the candidate producer was available; source uncertainty is preserved.
- Historical GTDB mapping aggregate counts were not rebuilt. Canonical broad-rank labels and native coherence/domain gates pass.
- Optional structured-source runner unavailable in the isolated runtime; inspected public catalog has no matching dataset. Required corpus network warnings concern other records.
- Only this immutable review bundle is saved; no canonical record, cache, history or generated product changes.
- All inspected input hashes remain unchanged. Evidence snippets match after documented XML/Unicode normalization.
- Short quotations total at most 25 words for the primary article and are shared across node/edge assessments.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T034556Z-acetylene-groundwater-enrichment-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Acetylene-fueled groundwater enrichment: whole-record review'
started_at: '2026-10-20T03:43:12.793406Z'
finished_at: '2026-10-20T03:45:56.542534Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Target unchanged this session; historical curation also used
    codex, so person-level independence is unknown.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Community hydrogen transfer and both process arrows are supported, with genomic
  producer uncertainty retained. Four major findings concern cultivation-stage scope,
  member resolution, functional roles and evidence type. Two minor findings concern
  the missing structured hydrogen and dataset links. Focused gates pass; corpus warning
  failures remain explicit.
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
  - path: history/records/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment/2026-10-05T055201Z-codex-fdadde.yaml
    sha256: d768d9eddc29e49e1fc836357e400cd5e781257883add61eade1b28adbd8b0d9
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    sha256: 31523009e0251f141c60c284424806a2289381b68f4bd125e3bea33046c8f755
    role: target
  - path: references_cache/PMID_33531396.md
    sha256: b9bfe13123b31f59fb468556209a69662ceba4ea6d98eca82482e9e06194750d
    role: context
  - path: references_cache/PMID_33531396.txt
    sha256: 436bc03b7f404050a0574d4c72dd744dece1785a209582b6aafce858104f6f57
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
- target_id: CommunityMech:000238
  path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
  label: Acetylene-Fueled Trichloroethene Dechlorination Groundwater Enrichment
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
scope:
  description: 'Whole target: two taxa, three nodes, two arrows, all 16 evidence items
    and primary full-text article.'
  selection: Second remaining record of batch 02 in path order, using baseline plus
    validated pending batch-01 coverage.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000238
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml'
  target_ids:
  - CommunityMech:000238
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
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
  summary: "uv run python scripts/validate_strict.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml\
    \ --out /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv"
  target_ids:
  - CommunityMech:000238
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    --out /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv
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

    uv run linkml-term-validator validate-data kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000238
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
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
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000238
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
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

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml'
  target_ids:
  - CommunityMech:000238
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
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
  - CommunityMech:000238
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-history history/records/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment
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
  - CommunityMech:000238
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
  summary: "Validating kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000238
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
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
  - CommunityMech:000238
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
  - CommunityMech:000238
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
  - CommunityMech:000238
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
  locator: Entire record, two taxa, three nodes and two arrows
  summary: The record denotes groundwater-derived stable enrichment 36BR-A-TCE, not
    the preceding synthetic Pelobacter/Dehalococcoides cocultures. Canonical record
    remains unchanged.
  support: supports
  accessed_at: '2026-10-20T03:45:56.538365Z'
- evidence_id: primary
  kind: primary_source
  reference: PMID:33531396
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7858054/fullTextXML;
    Abstract, Results, Discussion, Materials and Methods, main figures and data availability
  summary: Measured acetylene consumption, hydrogen balance and chlorinated-solvent
    reduction support community coupling. Metagenomics identifies candidate Coriobacteriales
    and a D. mccartyi genome; biochemical producer validation remains open. Initial
    acetylenotrophic microcosms and stable TCE enrichment are separate experimental
    stages.
  support: supports
  accessed_at: '2026-10-20T03:43:29.820793Z'
  snapshot_sha256: 065bb28d9f29e1b01a53779c90379f71295449f4430678bdbcb78597d820c378
- evidence_id: transfer
  kind: primary_source
  reference: PMID:33531396
  locator: 'Results: C2H2 fuels PCE and TCE dechlorination'
  summary: Hydrogen measurements and mass balance support community-level transfer,
    without isolating an exact donor-recipient pair.
  support: supports
  accessed_at: '2026-10-20T03:43:29.820793Z'
  quote: interspecies hydrogen transfer occurred in the enrichment
- evidence_id: sole
  kind: primary_source
  reference: PMID:33531396
  locator: Discussion opening
  summary: Acetylene supply supports the upstream substrate edge; sole organic substrate
    does not mean absence of inorganic carbon or nutrients.
  support: supports
  accessed_at: '2026-10-20T03:43:29.820793Z'
  quote: sole electron donor and organic carbon source
- evidence_id: methods
  kind: primary_source
  reference: PMID:33531396
  locator: 'Materials and Methods: Bacterial cultures and growth conditions'
  summary: Stable 36BR-A-TCE used a different medium and vessel context from initial
    SeFr1 microcosms.
  support: supports
  accessed_at: '2026-10-20T03:43:29.820793Z'
  quote: BAV1 defined mineral salts medium
- evidence_id: identity-source
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=33531396&retmode=xml
  locator: PMID, DOI, PMCID and article title
  summary: PMID 33531396, DOI 10.1128/mBio.02724-20 and PMC7858054 identify the cited
    Gushgari-Doyle et al. 2021 mBio paper.
  support: supports
  accessed_at: '2026-10-20T03:43:29.821211Z'
  snapshot_sha256: 23619828cbe416797a6aed6c2250c1693fd4934c1f1379f0dd3eaf82238fc2df
- evidence_id: composition
  kind: primary_source
  reference: PMID:33531396
  locator: 'Results: Composition of acetylenotrophic enrichment cultures; Discussion
    paragraphs 2–6'
  summary: D. mccartyi is the presumed dechlorinator, with a recovered genome and
    reductive-dehalogenase evidence. Coriobacteriales is the candidate acetylene-fermenting
    population. Genome-derived relative abundance differs from 16S estimates and must
    retain method context. Methanosaeta concilii and Methanobacterium are also detected;
    methane production is condition-specific. A genome closest to DCMB5 is not permission
    to substitute a reference isolate without retaining the actual environmental genome
    identity.
  support: supports
  accessed_at: '2026-10-20T03:43:29.820793Z'
- evidence_id: setup
  kind: primary_source
  reference: PMID:33531396
  locator: 'Methods: Bacterial cultures and growth conditions; Results/Figure 1'
  summary: The initial groundwater/SeFr1 microcosms and the stable BAV1-medium TCE
    enrichment are explicitly distinguished in Methods. The larger stable-enrichment
    vessel is described in prose as well as the figure caption; the record says it
    occurs only in table captions. A documented incubation context and serial enrichment
    history are omitted. This review identifies the mismatch without converting it
    into an operational protocol.
  support: supports
  accessed_at: '2026-10-20T03:43:29.820793Z'
- evidence_id: datasets
  kind: primary_source
  reference: PMID:33531396
  locator: 'Methods: Data availability; reference 89'
  summary: The source advertises BioProject PRJNA615907, SRA SRX8026671–SRX8026678,
    a ggKbase LAC_acetylene_final collection and USGS data release DOI 10.5066/P9BF8LM4.
    These are source-advertised candidate links, not independently verified dataset
    availability.
  support: supports
  accessed_at: '2026-10-20T03:43:29.820793Z'
- evidence_id: ontology
  kind: authority
  reference: OAK local SemanticSQL NCBITaxon, CHEBI, ENVO and GO snapshots
  locator: All seven unique IDs; ontology-authority.json
  summary: All curated IDs have matching canonical labels. Laboratory environment
    and groundwater fit separate experimental/source contexts. Anaerobic respiration
    fits organohalide respiration; acetylene fermentation should not be described
    as respiration merely because the recipient respires.
  support: supports
  accessed_at: '2026-10-20T03:44:01.556537Z'
  snapshot_sha256: cfa50c015dca940b151a6d9d1f779da1426612e2f980b3280fec67463e6d5f0a
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum and evidence definitions
  summary: PRIMARY_DEGRADER means degradation of complex substrates; CROSS_FEEDER
    means utilization of metabolites from other taxa. Acetylene consumption and organohalide
    respiration do not establish complex-substrate degradation, and a donor is not
    automatically a consumer.
  support: supports
  accessed_at: '2026-10-20T03:45:56.538839Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
  locator: Every one of 16 EvidenceItem occurrences; paragraph-aware XML extraction
  summary: All 16 snippets match the primary source after NFKC and whitespace normalization,
    preserving chemical subscripts without inserted spaces. Exact matches do not establish
    correct evidence type or experimental scope.
  support: supports
  accessed_at: '2026-10-20T03:45:56.538985Z'
  snapshot_sha256: bfed1e1da5b30551de077f3908c2737308ee2646b405e921d1883311f6967bb7
- evidence_id: history
  kind: record_content
  reference: history/records/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment/2026-10-05T055201Z-codex-fdadde.yaml
  locator: Whole history event and corresponding seven-record graph decision
  summary: Prior graph review retained community transfer and sole-substrate arrows,
    bounded the endpoint to vinyl chloride and preserved producer uncertainty. It
    explicitly did not certify other metadata.
  support: supports
  accessed_at: '2026-10-20T03:45:56.538990Z'
- evidence_id: local-search
  kind: search
  reference: references_cache; history/records; reports/causal_graph_review/decisions;
    kb/taxa
  locator: Ignored-inclusive identifier/slug/citation search
  summary: Located both cache forms, history and prior graph decision. The Markdown
    cache includes appended full text despite its abstract_only front matter. No medium/dataset
    entries are present in the whole target; no global external-registry absence is
    claimed.
  support: supports
  accessed_at: '2026-10-20T03:45:56.539179Z'
  search_scope: rg --no-ignore --hidden -l '33531396|Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment|10.1128/mBio.02724-20'
    references_cache history/records reports/causal_graph_review/decisions kb/taxa
  snapshot_sha256: 9d013f4af0a7b936993dd8c614df4a54bad30d02239398d0c73da2399949633d
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Same-session public catalog, 20 organisms and 28 datasets
  summary: No matching environmental Coriobacteriales population or D. mccartyi dataset
    appears. An unrelated model-organism expression module cannot validate the candidate
    acetylene hydratase. Optional runner remains unavailable in the isolated runtime.
  support: context_only
  accessed_at: '2026-10-19T23:31:07.726770Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
  locator: Actual execution 2026-10-20T03:43:17.311796+00:00 to 2026-10-20T03:43:17.927918+00:00
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml'
  support: supports
  accessed_at: '2026-10-20T03:43:17.927918Z'
  snapshot_sha256: 8e1bed3d5cea4938b88459e6f90cd2cfdd9d78724ee6ac901870c9a06a34829b
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    --out /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv
  locator: Actual execution 2026-10-20T03:43:17.311956+00:00 to 2026-10-20T03:43:19.063574+00:00
  summary: "uv run python scripts/validate_strict.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml\
    \ --out /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-02/000238/strict-report.tsv"
  support: supports
  accessed_at: '2026-10-20T03:43:19.063574Z'
  snapshot_sha256: 5474705e116a9974964fa780326527082fcf1043f18aad440757553de16c5464
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
  locator: Actual execution 2026-10-20T03:43:17.312142+00:00 to 2026-10-20T03:43:18.993879+00:00
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-10-20T03:43:18.993879Z'
  snapshot_sha256: e4a81d1a9b3be3cd1c0d5e12292c53af11c1b14612f3ad89cb94c027edb9697e
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
  locator: Actual execution 2026-10-20T03:43:17.928216+00:00 to 2026-10-20T03:43:18.000725+00:00
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-10-20T03:43:18.000725Z'
  snapshot_sha256: d78358325b2e47d2f8ec1766a6c1acb6e016400bc5d107b9fea54c3926b4738f
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
  locator: Actual execution 2026-10-20T03:43:18.000981+00:00 to 2026-10-20T03:43:19.130597+00:00
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml'
  support: supports
  accessed_at: '2026-10-20T03:43:19.130597Z'
  snapshot_sha256: daea60aaf55de8c2fa85db7a986b4aba8b64758187b6d9eeb46e7b1857134ee4
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-history history/records/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment
  locator: Actual execution 2026-10-20T03:43:18.994212+00:00 to 2026-10-20T03:43:19.579294+00:00
  summary: No issues found
  support: supports
  accessed_at: '2026-10-20T03:43:19.579294Z'
  snapshot_sha256: 850e7a63d7372e0c6448107197d9bff5b5acd791d563833d20be1e06ba15f235
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-20T03:43:19.579952+00:00 to 2026-10-20T03:43:19.641128+00:00
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-10-20T03:43:19.641128Z'
  snapshot_sha256: e059017911865916a4be9e1d9cf70f108dc8b5521722aec1f3ce66908612f6a9
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
  locator: Actual execution 2026-10-20T03:43:19.641362+00:00 to 2026-10-20T03:43:20.510047+00:00
  summary: "Validating kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-10-20T03:43:20.510047Z'
  snapshot_sha256: 4f3dc0733ac916a9198f345bfac82a93ec404d0376074f1c4bad4b247447b988
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
  topic: Community identity and provenance
  outcome: supported
  summary: This is the stable native-groundwater-derived enrichment 36BR-A-TCE, selected
    in the laboratory, not a defined two-isolate synthetic culture. NATURAL origin
    and ENGINEERED state distinguish origin from manipulation. The source site had
    historical bioaugmentation; native-population attribution is argued from composition/phylogenetic
    comparisons, not direct field proof of active coupling. Earlier synthetic Pelobacter
    SFB93/strain 195 or BAV1 pairs remain background comparators.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - primary
  - identity-source
  - composition
  dimensions:
  - name: source_population
    value: 36BR-A-TCE from NAWC groundwater
    definition: Stable laboratory enrichment distinct from initial acetylenotrophic
      cultures and earlier synthetic consortia.
    evidence_ids:
    - primary
    - setup
  - name: source_category
    value: Primary experiments plus genome-resolved inference
    definition: Community measurements and putative producer assignment are not equivalent
      evidence.
    evidence_ids:
    - primary
    - composition
- assessment_id: taxonomy
  area: grounding
  topic: taxonomy[0..1], taxon roles and resolution
  outcome: concern
  summary: Existing NCBI/GTDB broad ranks resolve and coherence gates pass, but full
    text identifies the dechlorinator more precisely than Bacteria and the candidate
    producer as Coriobacteriales. The source does not establish a cultured producer
    isolate. Both PRIMARY_DEGRADER assignments exceed the complex-substrate definition;
    donor CROSS_FEEDER lacks demonstrated incoming cross-fed substrate. Other detected
    taxa are not an obligatory minimal consortium.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - composition
  - ontology
  - schema
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Acetylenotrophy Provides Reductant for Dechlorination'
  outcome: concern
  summary: Community-level cross-feeding is supported by hydrogen balance and solvent
    reduction. Producer Actinomycetota/Coriobacteriales attribution is correctly qualified
    as genomic, and the recipient broad Bacteria guild is structurally declared but
    unnecessarily vague. Acetylene/TCE/PCE are valid substrates; the transferred hydrogen
    is missing from structured metabolites. Anaerobic respiration describes the recipient
    process, not the donor fermentation.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - transfer
  - composition
  - ontology
- assessment_id: edge-0
  area: graph
  topic: ecological_interactions[0].downstream[0] -> Reductive Dechlorination of TCE
    and PCE
  outcome: supported
  summary: Positive enabling direction from acetylene-fermenting community to dechlorination
    via hydrogen. Mass balances and concentration trajectories support this enrichment-level
    edge. Exact isolated donor/recipient attribution, reciprocal benefit and thermodynamic
    product-removal dependence remain unproven.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - transfer
  - primary
  details: 'Declared donor NCBITaxon:201174; declared recipient NCBITaxon:2. Mechanism:
    hydrogen cross-feeding. Context: stable 36BR-A-TCE, differentiated TCE/PCE assays.
    Exact shared quotation and locator: transfer.'
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Reductive Dechlorination of TCE and PCE'
  outcome: supported
  summary: COMMUNITY_LEVEL with no specific participant is allowed. Measured endpoints
    are chiefly vinyl chloride, with limited ethene in some conditions; the record
    appropriately avoids complete detoxification. TCE/PCE chemicals and anaerobic
    respiration are valid. A future more resolved participant can follow the source
    genome evidence without claiming a purified isolate experiment.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - primary
  - composition
  - ontology
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Acetylene as Sole Electron Donor and Carbon
    Source'
  outcome: supported
  summary: The sole organic-donor amendment is supported. The participating producer
    is inferred genomically; the node is a community substrate condition, not proof
    of a producer-only isolate phenotype. Inorganic CO2 and mineral/vitamin nutrients
    remain compatible with sole organic carbon wording.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - sole
  - primary
- assessment_id: edge-2
  area: graph
  topic: ecological_interactions[2].downstream[0] -> Acetylenotrophy Provides Reductant
    for Dechlorination
  outcome: supported
  summary: 'Positive substrate-supply direction: acetylene amendment enables community
    fermentation and downstream reductant supply. No niche partitioning is inferred.
    Candidate Coriobacteriales assignment remains genomic while community consumption
    is experimentally observed.'
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - sole
  - transfer
  - primary
  details: 'Upstream condition lists NCBITaxon:201174; transfer node addresses NCBITaxon:2
    recipient. Mechanism and context: acetylene-supported stable enrichment, with
    measured consumption/hydrogen balance. Exact short source quotations: sole and
    transfer.'
- assessment_id: cultivation
  area: scope
  topic: cultivation_setup[0], engineering_design, growth_media and environmental_factors
  outcome: concern
  summary: The recorded setup belongs to the initial acetylenotrophic enrichment,
    not the full stable dechlorinating system. The claim that the larger format appears
    only in captions is contradicted by Methods. Source medium and incubation information
    exist, but growth_media is empty. Engineering objectives and two environmental
    factors are supported when source-field mineral chemistry is distinguished from
    laboratory amendment. The setup problem includes the missing stage-specific medium
    representation.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - setup
  - methods
  - primary
- assessment_id: environment
  area: grounding
  topic: Environment, ingredients and metal scope
  outcome: supported
  summary: Laboratory environment and modeled groundwater are correctly separate.
    Acetylene, trichloroethene and tetrachloroethene match their curated IDs and functional
    substrate roles. Mineral-mediated abiotic acetylene formation is source background,
    not a demonstrated metal-processing function of the enrichment; NOT_APPLICABLE
    metal relevance is reasonable. No abundance score is asserted in this record.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - primary
  - ontology
- assessment_id: evidence
  area: evidence
  topic: All 16 evidence snippets, provenance and uncertainty
  outcome: concern
  summary: All snippets match; the taxon-identification snippet explicitly describes
    metagenomic analysis yet is tagged IN_VITRO. That overstates the assignment method
    even though the community itself was grown experimentally. The open producer-validation
    discussion accurately preserves unisolated-organism and enzyme uncertainty. Citations
    resolve; source-advertised datasets remain unrepresented.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - primary
  - snippets
  - datasets
  - history
- assessment_id: adapter
  area: evidence
  topic: Structured source cross-check
  outcome: not_applicable
  summary: No matching public expression-module dataset is available in the inspected
    catalog. This does not count against the genomic or experimental evidence.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - adapter
- assessment_id: validation
  area: schema
  topic: Native focused validation and graph integrity
  outcome: supported
  summary: All eight focused/preflight checks pass and cache bytes remain unchanged.
    Two arrows target declared nodes; both listed taxa participate somewhere in the
    graph. The community-level dechlorination node can omit participants. Native COMPLETE
    is structural, not proof of exact organism attribution. Required corpus warning
    failures remain explicit.
  target_ids:
  - CommunityMech:000238
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
  summary: Completeness is 75 and quality approximately 87.67; neither score removes
    four major and two minor findings. Five directly attached node EvidenceItems derive
    from one paper.
  target_ids:
  - CommunityMech:000238
  evidence_ids:
  - record
  - check-audit-network
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata/taxonomy roles +5 environment +10 for
      at least 3 factors +10 for at least 3 nodes +5 external resources +10 growth_media
      +5 datasets +5 any node metabolites). Applied 50+5+0+10+5+0+0+5=75; presence
      only.
  - name: validation_quality
    value: 87.6666666667
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50*P1-10*P2-2*P3+20*min(mean evidence/2,1)+15 if native
      network COMPLETE,0,100). P1=0,P2=4,P3=2; five EvidenceItems/three nodes; declared
      participants and references intact. 100-40-4+16.6666666667+15=87.6666666667.
  - name: P1
    value: 0
    unit: findings
    definition: Native target severity count.
  - name: P2
    value: 4
    unit: findings
    definition: Native target severity count.
  - name: P3
    value: 2
    unit: findings
    definition: Native target severity count.
  - name: interaction_evidence
    value: 1.6666666666666667
    unit: evidence items per interaction
    denominator: 3
    definition: Five directly attached entries across three nodes; all one primary
      publication, not independent replication.
findings:
- finding_id: cultivation-context
  issue_key: cm-000238-cultivation-context
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: CLAUDE.claim-level-evidence
  status: open
  certainty: confirmed
  title: Initial microcosm setup substitutes for the stable dechlorinating enrichment
  description: The record omits the stable 36BR-A-TCE setup and falsely says its vessel
    format appears only in table captions. Methods explicitly distinguish the successive
    enrichment stages and their media. An empty growth_media list loses source-reported
    medium context.
  target_ids:
  - CommunityMech:000238
  field_paths:
  - cultivation_setup[0]
  - growth_media
  evidence_ids:
  - setup
  - methods
  - primary
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
- finding_id: member-resolution
  issue_key: cm-000238-member-resolution
  category: completeness
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: review-checklist.taxonomy
  status: open
  certainty: confirmed
  title: Full-text member assignments remain hidden behind broad guilds
  description: The Bacteria dechlorinating guild is justified only by abstract limitations
    although Results identify a D. mccartyi genome and its likely role. The candidate
    acetylene producer can be represented at Coriobacteriales order while preserving
    inference. Neither update licenses an exact reference-isolate substitution.
  target_ids:
  - CommunityMech:000238
  field_paths:
  - taxonomy[0].taxon_term
  - taxonomy[1].taxon_term
  - ecological_interactions[0].source_taxon
  - ecological_interactions[0].target_taxon
  evidence_ids:
  - composition
  - primary
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
- finding_id: functional-roles
  issue_key: cm-000238-functional-roles
  category: consistency
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: P2.4
  status: open
  certainty: confirmed
  title: Taxon roles do not match the schema definitions
  description: PRIMARY_DEGRADER requires complex-substrate degradation, which is not
    established by acetylene fermentation or chlorinated-solvent respiration. The
    candidate acetylene donor is CROSS_FEEDER although no incoming partner-derived
    metabolite use is demonstrated.
  target_ids:
  - CommunityMech:000238
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  evidence_ids:
  - schema
  - primary
  - transfer
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
- finding_id: evidence-type
  issue_key: cm-000238-evidence-type
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: CLAUDE.claim-level-evidence
  status: open
  certainty: confirmed
  title: Genomic producer identification is labeled as an in-vitro assignment
  description: taxonomy[0].evidence[0] supports producer identity through metagenomic
    analysis, not isolation or biochemical testing. IN_VITRO conflates the experimental
    cultivation setting with the taxon-attribution method.
  target_ids:
  - CommunityMech:000238
  field_paths:
  - taxonomy[0].evidence[0].evidence_source
  evidence_ids:
  - record
  - composition
  - primary
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
- finding_id: hydrogen-metabolite
  issue_key: cm-000238-hydrogen-metabolite
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: missing structured linkage or metabolite representation;
    prose retains the supported process.'
  rule_id: review-checklist.interactions
  status: open
  certainty: confirmed
  title: The exchanged hydrogen is missing from structured metabolites
  description: The transfer node describes and evidences hydrogen exchange but lists
    only acetylene and chlorinated substrates. The supported exchanged molecule is
    unavailable to structured metabolite queries.
  target_ids:
  - CommunityMech:000238
  field_paths:
  - ecological_interactions[0].metabolites
  evidence_ids:
  - record
  - transfer
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
- finding_id: dataset-links
  issue_key: cm-000238-dataset-links
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: missing structured linkage or metabolite representation;
    prose retains the supported process.'
  rule_id: P3.1
  status: open
  certainty: confirmed
  title: Source-advertised datasets are not represented
  description: The paper names BioProject/SRA, genome collection and USGS cultivation
    data, while associated_datasets is empty. External availability was not independently
    checked, so only a source-backed linkage follow-up is asserted.
  target_ids:
  - CommunityMech:000238
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - datasets
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
actions:
- action_id: fix-cultivation-context
  description: Separate initial acetylenotrophic enrichment from stable dechlorination
    characterization, retaining source-specific medium and incubation context.
  finding_ids:
  - cultivation-context
  target_ids:
  - CommunityMech:000238
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
  acceptance_checks:
  - Stable-community setup is traceable to the correct Methods passage.
  - Remove the false caption-only assertion and avoid mixing stages into one recipe.
  - Use exact verified medium links only where available.
  - Run strict, term and reference validation after authorized curation.
- action_id: fix-member-resolution
  description: Represent the source-supported member resolution and propagate consistent
    participant descriptors, retaining genome-based uncertainty.
  finding_ids:
  - member-resolution
  target_ids:
  - CommunityMech:000238
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
  acceptance_checks:
  - Dechlorinator and candidate producer are distinguished at source-supported ranks
    with authority-verified IDs.
  - No inference of an obligatory two-member minimal community.
  - Reference-strain similarity remains distinct from environmental genome identity.
  - Run GTDB, term, strict and network gates.
- action_id: fix-functional-roles
  description: Choose supported role semantics or document an unresolved vocabulary
    gap; do not turn hydrogen donation into proven consumption.
  finding_ids:
  - functional-roles
  target_ids:
  - CommunityMech:000238
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
  acceptance_checks:
  - Every role matches a defined activity supported by the correct source context.
  - No unsupported reciprocal transfer is inferred.
  - Run strict and network gates.
- action_id: fix-evidence-type
  description: Use the schema-supported evidence classification for genomic/computational
    attribution and preserve partial organism-level certainty.
  finding_ids:
  - evidence-type
  target_ids:
  - CommunityMech:000238
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
  acceptance_checks:
  - Evidence type describes the actual identification method.
  - Measured community function remains distinct from inferred producer identity.
  - Run strict and reference checks.
- action_id: fix-hydrogen-metabolite
  description: Represent the directly supported exchange molecule with a verified
    chemical identifier and claim-level evidence.
  finding_ids:
  - hydrogen-metabolite
  target_ids:
  - CommunityMech:000238
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
  acceptance_checks:
  - Chemical identity matches molecular hydrogen, not a different hydrogen species.
  - Do not add acetate transfer as measured merely because it is biologically plausible.
  - Run term, strict and reference checks.
- action_id: fix-dataset-links
  description: Verify the primary advertised accessions and add only resolved links
    with the correct dataset scope.
  finding_ids:
  - dataset-links
  target_ids:
  - CommunityMech:000238
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acetylene_Fueled_TCE_Dechlorination_Groundwater_Enrichment.yaml
    role: canonical_record
  acceptance_checks:
  - Accessions resolve and distinguish amplicon, metagenome and cultivation data.
  - Do not treat advertised availability as verified retrieval.
  - Run strict and resource-reference checks.
limitations:
- Main article and embedded figure/table captions were inspected. Separate supplementary
  downloads, raw sequence reads and cultivation data were not reanalyzed.
- Source-advertised dataset accessions and genome collection were not independently
  retrieved; proposed linkages require verification.
- No isolate biochemical validation of the candidate producer was available; source
  uncertainty is preserved.
- Historical GTDB mapping aggregate counts were not rebuilt. Canonical broad-rank
  labels and native coherence/domain gates pass.
- Optional structured-source runner unavailable in the isolated runtime; inspected
  public catalog has no matching dataset. Required corpus network warnings concern
  other records.
notes:
- Only this immutable review bundle is saved; no canonical record, cache, history
  or generated product changes.
- All inspected input hashes remain unchanged. Evidence snippets match after documented
  XML/Unicode normalization.
- Short quotations total at most 25 words for the primary article and are shared across
  node/edge assessments.
tags:
- record-review
- groundwater-enrichment
- batch-02
```
