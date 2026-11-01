# Arabidopsis SynCom150: whole-record source review

- Review: 20261021T065013Z-arabidopsis-syncom150-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T06:46:04.244519Z
- Finished UTC: 2026-10-21T06:50:13.400918Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major finding concerns the description omitting the immune-mechanism limitation preserved by the full Discussion and current graph. Two minor findings concern external media identifiers and typed dataset representation. All five nodes retain source-supported, qualified phenotypes; no causal arrows are warranted. Eight focused gates pass, seven ontology pairs match and twenty-nine snippets verify.

## Scope And Provenance

Entire record, nested aggregate taxonomy, all five nodes and no arrows, all metadata and twenty-nine evidence occurrences, primary main article and public sequencing metadata. Exact strain roster, supplements, raw data and figure geometry were not audited.

Selection: Next uncovered path after Apple Fire Blight ANP in batch03; one resolved maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ade4a9acdc245e1090522bb4f6ec5fe82ee88689.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000368 | kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml | maintained | Arabidopsis Bacillus Biocontrol SynCom150 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000368 | Schema validation passed for the target. |
| validate-strict | passed | True | CommunityMech:000368 | Strict closed-schema and cross-field validation passed for the target. |
| validate-terms | passed | True | CommunityMech:000368 | Native ontology-term validation passed for the target. |
| validate-gtdb | passed | True | CommunityMech:000368 | GTDB structural grounding validation passed; this is not an isolate-level crosswalk audit. |
| validate-gtdb-domain | passed | True | CommunityMech:000368 | GTDB domain validation passed for the target. |
| validate-history | passed | True | CommunityMech:000368 | All three target history sidecars passed native validation. |
| normalize-cache-names-check | passed | True | CommunityMech:000368 | Read-only reference-cache filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000368 | Native reference validation passed; committed cache hashes remained unchanged. |
| audit-network | failed | True | CommunityMech:000368 | Earlier correct-runtime corpus run retained: 477 records, 57 warnings across 21 records, zero errors and exit 1; this target was not listed. |
| check-network-quality | failed | True | CommunityMech:000368 | Earlier correct-runtime corpus run retained: 477 records, 57 warnings across 21 records, zero errors and exit 1; this target was not listed. |
| Optional structured source adapter availability | unavailable | False | CommunityMech:000368 | No runner in the owned runtime; an external candidate was not executed, and no catalog coverage was established. |

## Scientific And Domain Assessments

### SynCom150 and nested protective subsets

identity: supported. Targets: CommunityMech:000368.

The source and target are resolved. Aggregate Bacteria and nested protective subsets are clearly labeled. The review does not treat these descriptors as three independent members or certify the full strain inventory.

### taxonomy[0:3], rank and GTDB scope

grounding: supported. Targets: CommunityMech:000368.

Encoded IDs and labels are correct at their stated ranks. Source-supported subset roles should not be generalized to all members of Bacillus or Pseudomonadota outside this inoculum. No functional role need be invented for the heterogeneous whole-community aggregate.

### Description immune-activation interpretation

evidence: concern. Targets: CommunityMech:000368.

The description follows the abstract interpretation but omits the Discussion limitation retained by node 4 and open discussions. Protection despite the tested co-receptor defect and lower marker expression does not exclude every induced-resistance contribution.

### ecological_interactions[0]: SynCom Colonization and Partial Growth Rescue in Irradiated Coir

graph: supported. Targets: CommunityMech:000368.

Aggregate colonization and partial growth rescue are supported.

Participants: full SynCom150 and Arabidopsis in irradiated coir. Direction: inoculation toward recovered aggregate bacterial communities and partial host growth improvement; individual strain establishment and reciprocal fitness benefits are not resolved. Linked primary evidence provides the exact source locator and a bounded verbatim excerpt.

### ecological_interactions[1]: Bacillus-Dependent Pto Leaf-Pathogen Suppression

graph: supported. Targets: CommunityMech:000368.

Dropout/add-in and diversity interventions support Bacillus-subset protection.

Participants: the source Bacillus subset and challenged Arabidopsis, with external Pto DC3000 as pathogen. Direction: Bacillus inclusion toward reduced pathogen leaf colonization. Coir and agar diversity tests must not be collapsed into one protocol. Linked primary evidence provides the exact source locator and a bounded verbatim excerpt.

### ecological_interactions[2]: Diverse Bacillus In Vitro Pto Antagonism

graph: supported. Targets: CommunityMech:000368.

Observed agar inhibition and the qualified BGC result are supported.

Participants: individual screened Bacillus isolates and Pto in vitro. Direction: isolate presence toward lower spatial luminescence. A diffusible antagonist is inferred; no single molecule, reciprocal competition or ecological transition to later assays is established. Linked primary evidence provides the exact source locator and a bounded verbatim excerpt.

### ecological_interactions[3]: Pseudomonadota Multi-Class Pto Protection

graph: supported. Targets: CommunityMech:000368.

Multi-class protection is supported without one resolved focal class.

Participants: Pseudomonadota subsets, challenged Arabidopsis and Pto. Direction: combined inoculum toward protection; class dropouts/add-ins do not isolate resource competition. Linked primary evidence provides the exact source locator and a bounded verbatim excerpt.

### ecological_interactions[4]: Bacillus Protection in bbc1 Immune-Impaired Arabidopsis

graph: supported. Targets: CommunityMech:000368.

Protection despite the specified immune defect is supported.

Participants: 22-strain Bacillus inoculum, wild-type or bbc1 Arabidopsis and Pto in open unsterilized coir. Direction: inoculation toward reduced pathogen counts. This does not eliminate all immunity or establish mutualistic bacterial benefit. Linked primary evidence provides the exact source locator and a bounded verbatim excerpt.

### ecological_interactions[*].downstream

graph: not_applicable. Targets: CommunityMech:000368.

No downstream arrows remain. Source-to-follow-up experiment order is not ecological causation.

### Node biological_processes

grounding: supported. Targets: CommunityMech:000368.

Canonical process labels resolve. Broad defense-response mapping must not be read as proof of activated host immunity or an induced self-defense mechanism in the halo bacterium; the source-specific phenotypes remain in the descriptions.

### engineering_design and intervention contexts

scope: supported. Targets: CommunityMech:000368.

Top-down assembly/deconstruction, pathogen readouts, host expression and biosynthetic prediction endpoints match the main article. The GFP reporter strain used separately for leaf localization must not be added to SynCom150 membership from that assay alone.

### Laboratory and modeled rhizosphere environments

grounding: supported. Targets: CommunityMech:000368.

The formal laboratory environment and modeled rhizosphere distinguish controlled study setting from natural source habitat. Notes retain the open-coir validation system rather than claiming all assays are gnotobiotic.

### Growth media, environmental factors and cultivation_setup

scope: concern. Targets: CommunityMech:000368.

Source-backed LB and MS contexts are represented. Culture-age and system-specific inoculum details must remain qualified; the seedling light/temperature evidence is not a numeric chamber profile for every later assay. Exact external medium linkages are missing.

### External resources and associated_datasets

completeness: concern. Targets: CommunityMech:000368.

Both resource accessions verify and remain relevant. They are represented only as generic external resources; no associated_datasets entries expose their sequencing/transcriptomic roles for structured retrieval.

### History, cache and open scientific questions

provenance: supported. Targets: CommunityMech:000368.

Three valid sidecars and the prior graph decision preserve experimental scope and unresolved mechanism. All snippets verify against current primary XML, with only a cache text-node spacing difference for one accession sentence.

### Metal and REE fields

scope: supported. Targets: CommunityMech:000368.

No metal or rare-earth-processing mechanism is asserted; media salts or predicted clusters do not establish one.

### Native gates and independent source checks

schema: supported. Targets: CommunityMech:000368.

Eight focused checks passed, seven ontology pairs match and twenty-nine snippets verify against primary XML. Corpus failures are retained; these deterministic checks do not decide mechanism scope.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000368.

Completeness 30 reflects aggregate representation and field placement, not a need to invent a whole-community role; quality 100 is not scientific approval.

## Findings

### immune-qualification: Description omits the source immune-mechanism qualification

major / open / confirmed; issue key: cm-000368-immune-qualification.

The abstract supports an immune-independence interpretation, which the description repeats. The full Discussion and existing node 4/discussions retain unresolved induced-resistance contributions. The summary can be read more broadly than the actual bbc1 and expression tests establish; this is a qualification inconsistency, not a claim that the source contains no supporting statement.

### media-linkage: LB and MS media have no external identifiers

minor / open / confirmed; issue key: cm-000368-media-linkage.

The two growth-media entries carry source-supported preparation context but lack CultureMech or MediaIngredientMech identifiers.

### typed-datasets: Verified sequencing resources are not typed as associated datasets

minor / open / confirmed; issue key: cm-000368-typed-datasets.

PRJNA1175571 and GSE285599 resolve and are linked as external resources, but associated_datasets is absent. This is a structured representation gap, not missing source accessions.

## Recommended Actions And Acceptance Checks

### fix-immune-qualification

Carry the specific co-receptor-defect and unresolved induced-resistance qualification into the description while retaining the demonstrated protection phenotype.

- Description agrees with node 4 and existing open discussions.
- No test of bbc1 is described as removal of all host immune function.
- Source abstract and Discussion interpretations are both represented fairly.
- Run strict and reference checks.

### fix-media-linkage

Link exact compatible external medium or ingredient entries where available without collapsing distinct source preparations.

- Any linked recipe matches the formulation and assay context.
- No unreported ingredient or growth condition is inferred.
- Run focused medium/linkage validation appropriate to the curated change.

### fix-typed-datasets

Represent the existing source-relevant accessions with accurate dataset types while preserving their current links and evidence.

- Amplicon data and host RNA-seq are distinguished.
- GEO is not misrepresented as Bacillus transcriptomics.
- No raw-data or strain-level validation is implied by project metadata.
- Run strict and reference checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml; Whole record: three nested aggregate descriptors, five nodes, no downstream arrows, twenty-nine evidence occurrences | supports | The target is SynCom150 with Bacillus and Pseudomonadota protective subsets. The descriptors are explicitly nested aggregates, not three disjoint members or a complete strain roster. |
| primary | PMID:40590505; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13235741/fullTextXML; abstract, full Methods, Results, Discussion, figure captions and supplement inventory | supports | Independent full article inspected. Main-text experiments distinguish the full SynCom, taxonomic dropout/add-in arms, Bacillus-only subsets, individual isolates and a separate reporter strain. Supplementary data files and figure geometry were not inspected. |
| identity | PMID:40590505; Methods: Bacterial culture and plant inoculation; Results: system establishment; Discussion: amplicon resolution | supports | The inoculum contains 150 genome-sequenced root isolates, nearly all from Arabidopsis. Supplementary Dataset S1 is cited for membership; the archive is listed in XML but was not retrieved. The authors did not track individual strain establishment and report sequencing resolution limits, which the node correctly preserves. |
| colonization | PMID:40590505; Results: Establishment of a plant-microbiome model system; Supplementary Fig S1 discussed in main text | supports | Aggregate inoculum-derived communities were recovered from rhizosphere, roots and shoots and plant growth improved partially relative to irradiated coir. This does not establish every strain in every compartment. |
| bacillus | PMID:40590505; Abstract; Results: focal taxon deconstruction and Bacillus strain diversity; Figs 1 and 4 captions | supports | Bacillus dropout/add-in interventions support protective inoculum effects. The diversity experiments distinguish growth-limited single-strain coir assays from subsequent agar tests; combinations protect more completely than single strains. |
| halo | PMID:40590505; Methods: Halo assay; Results: All Bacillus strains inhibit Pto in vitro; BGC analysis | supports | Individual isolates inhibited the luminescent pathogen readout in agar assays. Spatial inhibition supports diffusible antagonism but does not identify the active molecule; computational BGC analysis did not find one shared Bacillus-specific cluster. |
| pseudomonadota | PMID:40590505; Results: second deconstruction within Pseudomonadota; Fig 1D caption; Discussion final paragraph | supports | Class-level dropouts did not identify one necessary class; combinations protected more effectively than isolated classes. Niche overlap remains a hypothesis rather than demonstrated resource competition. |
| bbc1 | PMID:40590505; Results: immune gene expression and bbc1 intervention; Fig 5 caption; Discussion | supports | Bacillus inoculation protected both wild type and the specified co-receptor-deficient mutant in the open-coir assay. The intervention does not disable every immune pathway. RNA-seq describes host expression and is not a direct assay excluding all immune contributions. |
| immune-qualification | PMID:40590505; Abstract contrasted with Discussion paragraphs on direct and systemic effects | supports | The abstract uses a strong immune-independence interpretation, reflected in the description. Discussion explicitly leaves induced-resistance involvement unresolved, and the current graph preserves this caveat. The review identifies an inconsistency in qualification, not absence of any supporting source wording. |
| culture | PMID:40590505; Methods: Bacterial culture and plant inoculation; seed growth; closed/agar/open systems | supports | LB revival and MS inoculation conditions are source-backed. The preparation includes two culture ages rather than one homogeneous culture. Inoculum normalization differs among experimental systems; the MS evidence explanation specifically limits its value to the closed system. The light/temperature excerpt concerns seedling plates before transfer. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity, functional-role, evidence and cultivation definitions | supports | The schema permits aggregate taxa and optional role/dataset fields. A missing role on heterogeneous Bacteria is not permission to invent a common function. Dataset typing and external medium links improve retrieval without changing measured biology. |
| ontology | Local OAK NCBITaxon, ENVO and GO snapshots; Seven distinct ID-label pairs across fifteen occurrences; rank and GO definition checks | supports | All pairs match. Bacteria/domain, Bacillus/genus and Pseudomonadota/phylum signal nested scope. GO0042742 is broader than host immunity, so its use does not alone contradict immune-impaired protection. Halo inhibition does not independently establish a triggered bacterial defensive response. The Bacillus GTDB majority mapping does not prove all 22 isolates have that GTDB genus. |
| snippets | kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml; Twenty-nine evidence occurrences against independently fetched main article XML and committed cache | supports | All 29 match fresh XML after NFKC/whitespace normalization. The cache has one normalized miss caused solely by a separator before the GEO accession period, rather than absent supporting text. No source quote was repaired or canonical cache changed. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=40590505&amp;retmode=xml; Independent public metadata | supports | PMID40590505 identifies the cited SynCom150 paper. |
| crossref | https://api.crossref.org/works/10.1093/ismejo/wraf134; Independent public metadata | supports | DOI10.1093/ismejo/wraf134 identifies the same paper; publication metadata is independently verified. |
| bioproject | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&amp;id=1175571&amp;retmode=xml; Independent public metadata | supports | PRJNA1175571 is public and corresponds to the source sequencing project; metadata does not verify each strain or raw read. |
| geo | https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE285599&amp;targ=self&amp;form=text&amp;view=full; Independent public metadata | supports | GSE285599 is public Arabidopsis expression profiling, directly links the source PMID and BioProject, and lists 18 sample accessions. It is host RNA-seq, not a Bacillus expression dataset. |
| history | history/records/Arabidopsis_Bacillus_Biocontrol_SynCom150; reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml; Three sidecars, inline history and exact target decision row | supports | Later graph curation removed workflow arrows and unsupported interaction labels. Earlier mutualism wording in append-only history is superseded, not a current graph assertion. Existing immune and focal-taxon discussions are preserved. |
| local-search | references_cache; history; reports/causal_graph_review/decisions; kb/taxa; Source PMID and record ID/slug search including hidden and ignored files | supports | Located the primary cache, three history sidecars and prior graph decision. No assertion of globally absent taxon or source data is based on this identifier search. |
| adapter | Optional kg-microbe-sources runner discovery; Reused bounded task-runtime and sibling discovery receipt from the preceding record | supports | No runner in the owned runtime; a candidate in another task checkout was not executed. No expression catalog coverage was queried. GEO and primary Methods supply host RNA-seq context; no iModulon membership is claimed. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml; Actual execution 2026-10-21T06:46:04.910083+00:00 to 2026-10-21T06:46:05.711539+00:00 | supports | Schema validation passed for the target. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-strict kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml --out /private/tmp/cm-review-session/batch-03/000368/strict-report.tsv; Actual execution 2026-10-21T06:46:04.910312+00:00 to 2026-10-21T06:46:07.458542+00:00 | supports | Strict closed-schema and cross-field validation passed for the target. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-terms kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml; Actual execution 2026-10-21T06:46:04.910414+00:00 to 2026-10-21T06:46:07.428024+00:00 | supports | Native ontology-term validation passed for the target. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml; Actual execution 2026-10-21T06:46:05.711917+00:00 to 2026-10-21T06:46:05.818249+00:00 | supports | GTDB structural grounding validation passed; this is not an isolate-level crosswalk audit. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb-domain kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml; Actual execution 2026-10-21T06:46:05.818548+00:00 to 2026-10-21T06:46:07.468750+00:00 | supports | GTDB domain validation passed for the target. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-history history/records/Arabidopsis_Bacillus_Biocontrol_SynCom150; Actual execution 2026-10-21T06:46:07.428491+00:00 to 2026-10-21T06:46:08.269665+00:00 | supports | All three target history sidecars passed native validation. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T06:46:08.270988+00:00 to 2026-10-21T06:46:08.342614+00:00 | supports | Read-only reference-cache filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-references-explained kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml; Actual execution 2026-10-21T06:46:08.342989+00:00 to 2026-10-21T06:46:09.902430+00:00 | supports | Native reference validation passed; committed cache hashes remained unchanged. |
| check-audit-network | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv audit-network; Actual finish 2026-10-20T07:08:14.467705+00:00 | supports | Earlier correct-runtime corpus run retained: 477 records, 57 warnings across 21 records, zero errors and exit 1; this target was not listed. |
| check-check-network-quality | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv check-network-quality; Actual finish 2026-10-20T07:08:13.673449+00:00 | supports | Earlier correct-runtime corpus run retained: 477 records, 57 warnings across 21 records, zero errors and exit 1; this target was not listed. |
| native-target | NetworkIntegrityAuditor().audit_community(target); Fresh independent read-only API check and native metric components in support-audit.json | supports | No target network issue returned; eleven evidence items across five nodes give mean 2.2 and all three aggregate descriptors participate. |

## Limits And Additional Notes

- Supplementary Dataset S1 and the supplement archive are cited/listed but were not retrieved; all 150 individual strain identities and their current taxonomy are not certified. The record intentionally uses aggregate membership.
- Figure captions and reported main-text results were read, but figure geometry, raw sequencing/host-expression data and supplement-only measurements were not independently reanalyzed.
- GTDB validation checks the encoded grounding structure/domain; this review does not independently reproduce the historical crosswalk counts or assign all 22 isolates to a present-day GTDB genus.
- Host immune contribution, active antagonistic molecules and bacterial fitness benefits remain unresolved. The source abstract supports a stronger interpretation than the Discussion and bounded current graph.
- Optional structured-expression adapter was not available in the owned runtime; a candidate in another checkout was not executed. Public GEO metadata supplies host RNA-seq context, not a functional proof.
- Required corpus gates retain actual warning failures; field-completeness and network scores do not establish scientific truth.
- Canonical records, caches, history and generated outputs remain unchanged.
- Short quotations from the single source total 24 words.
- A one-snippet cache mismatch is solely whitespace before a punctuation mark; fresh primary XML supports the exact evidence text.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T065013Z-arabidopsis-syncom150-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Arabidopsis SynCom150: whole-record source review'
started_at: '2026-10-21T06:46:04.244519Z'
finished_at: '2026-10-21T06:50:13.400918Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Canonical target unchanged in this session; prior codex curation
    prevents person-level independence claim. Separate agents checked ontology, snippets,
    resources, history and native metrics; root also inspected the primary source.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: One major finding concerns the description omitting the immune-mechanism
  limitation preserved by the full Discussion and current graph. Two minor findings
  concern external media identifiers and typed dataset representation. All five nodes
  retain source-supported, qualified phenotypes; no causal arrows are warranted. Eight
  focused gates pass, seven ontology pairs match and twenty-nine snippets verify.
source:
  git_revision: ade4a9acdc245e1090522bb4f6ec5fe82ee88689
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
  - path: history/README.md
    sha256: 86c0347d77402bcecdec466b01974ad53beddb9cf1bd17cf085674970542a101
    role: context
  - path: history/records/Arabidopsis_Bacillus_Biocontrol_SynCom150/2026-09-13T215632Z-codex-6d974c.yaml
    sha256: 13d222e09b7b76c7333c934c17e21125c7023da3995d5108da1fa57a9bb9887a
    role: context
  - path: history/records/Arabidopsis_Bacillus_Biocontrol_SynCom150/2026-09-13T220136Z-codex-ebffcc.yaml
    sha256: db9b2eba8e2eeabba0c9923dbcf455cd47c2ec6a8f435e4708217bfe6c62f2b8
    role: context
  - path: history/records/Arabidopsis_Bacillus_Biocontrol_SynCom150/2026-10-05T084410Z-codex-ba9883.yaml
    sha256: 17d61436e3544c923218e976c75fa5d82e0ad6722f61c5b2f6cf02bf789cfa70
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
    sha256: c487e5ae123f7515fa5060e82625f5c89dd336284107fc94755552b620cabb98
    role: target
  - path: references_cache/PMID_40590505.txt
    sha256: c41b282736b88ca0034cc3d05e01f041691652e1f51958c61fad8fc960da4ea3
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
    sha256: e21a355f676730e8e7e6de6ea663017c9b09e05a824ff383a272ab9f1399fd70
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
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
- target_id: CommunityMech:000368
  path: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  label: Arabidopsis Bacillus Biocontrol SynCom150
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
    role: canonical_record
scope:
  description: Entire record, nested aggregate taxonomy, all five nodes and no arrows,
    all metadata and twenty-nine evidence occurrences, primary main article and public
    sequencing metadata. Exact strain roster, supplements, raw data and figure geometry
    were not audited.
  selection: Next uncovered path after Apple Fire Blight ANP in batch03; one resolved
    maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000368
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed for the target.
  target_ids:
  - CommunityMech:000368
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history check or read-only cache-name preflight; no canonical
    cache changes.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict closed-schema and cross-field validation passed for the target.
  target_ids:
  - CommunityMech:000368
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
    --out /private/tmp/cm-review-session/batch-03/000368/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history check or read-only cache-name preflight; no canonical
    cache changes.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Native ontology-term validation passed for the target.
  target_ids:
  - CommunityMech:000368
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history check or read-only cache-name preflight; no canonical
    cache changes.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB structural grounding validation passed; this is not an isolate-level
    crosswalk audit.
  target_ids:
  - CommunityMech:000368
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history check or read-only cache-name preflight; no canonical
    cache changes.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed for the target.
  target_ids:
  - CommunityMech:000368
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history check or read-only cache-name preflight; no canonical
    cache changes.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: All three target history sidecars passed native validation.
  target_ids:
  - CommunityMech:000368
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Arabidopsis_Bacillus_Biocontrol_SynCom150
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history check or read-only cache-name preflight; no canonical
    cache changes.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only reference-cache filename preflight passed.
  target_ids:
  - CommunityMech:000368
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history check or read-only cache-name preflight; no canonical
    cache changes.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Native reference validation passed; committed cache hashes remained unchanged.
  target_ids:
  - CommunityMech:000368
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history check or read-only cache-name preflight; no canonical
    cache changes.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Earlier correct-runtime corpus run retained: 477 records, 57 warnings
    across 21 records, zero errors and exit 1; this target was not listed.'
  target_ids:
  - CommunityMech:000368
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Actual earlier batch03 corpus gate reused with unchanged canonical inputs;
    fresh target API diagnostics do not replace it.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Earlier correct-runtime corpus run retained: 477 records, 57 warnings
    across 21 records, zero errors and exit 1; this target was not listed.'
  target_ids:
  - CommunityMech:000368
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Actual earlier batch03 corpus gate reused with unchanged canonical inputs;
    fresh target API diagnostics do not replace it.
- check_id: structured-expression-adapter
  name: Optional structured source adapter availability
  status: unavailable
  required: false
  summary: No runner in the owned runtime; an external candidate was not executed,
    and no catalog coverage was established.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - adapter
  - geo
  - primary
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  locator: 'Whole record: three nested aggregate descriptors, five nodes, no downstream
    arrows, twenty-nine evidence occurrences'
  summary: The target is SynCom150 with Bacillus and Pseudomonadota protective subsets.
    The descriptors are explicitly nested aggregates, not three disjoint members or
    a complete strain roster.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392264Z'
- evidence_id: primary
  kind: primary_source
  reference: PMID:40590505
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13235741/fullTextXML;
    abstract, full Methods, Results, Discussion, figure captions and supplement inventory
  summary: Independent full article inspected. Main-text experiments distinguish the
    full SynCom, taxonomic dropout/add-in arms, Bacillus-only subsets, individual
    isolates and a separate reporter strain. Supplementary data files and figure geometry
    were not inspected.
  support: supports
  accessed_at: '2026-10-21T06:46:26.093174Z'
  snapshot_sha256: b34ecbc6f6fec18b7c18ac85f558bdc338f0e4dece16a5286454168c6ee3b208
- evidence_id: identity
  kind: primary_source
  reference: PMID:40590505
  locator: 'Methods: Bacterial culture and plant inoculation; Results: system establishment;
    Discussion: amplicon resolution'
  summary: The inoculum contains 150 genome-sequenced root isolates, nearly all from
    Arabidopsis. Supplementary Dataset S1 is cited for membership; the archive is
    listed in XML but was not retrieved. The authors did not track individual strain
    establishment and report sequencing resolution limits, which the node correctly
    preserves.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392381Z'
- evidence_id: colonization
  kind: primary_source
  reference: PMID:40590505
  locator: 'Results: Establishment of a plant-microbiome model system; Supplementary
    Fig S1 discussed in main text'
  summary: Aggregate inoculum-derived communities were recovered from rhizosphere,
    roots and shoots and plant growth improved partially relative to irradiated coir.
    This does not establish every strain in every compartment.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392384Z'
  quote: partially restored plant growth
- evidence_id: bacillus
  kind: primary_source
  reference: PMID:40590505
  locator: 'Abstract; Results: focal taxon deconstruction and Bacillus strain diversity;
    Figs 1 and 4 captions'
  summary: Bacillus dropout/add-in interventions support protective inoculum effects.
    The diversity experiments distinguish growth-limited single-strain coir assays
    from subsequent agar tests; combinations protect more completely than single strains.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392386Z'
  quote: critical role for the genus Bacillus
- evidence_id: halo
  kind: primary_source
  reference: PMID:40590505
  locator: 'Methods: Halo assay; Results: All Bacillus strains inhibit Pto in vitro;
    BGC analysis'
  summary: Individual isolates inhibited the luminescent pathogen readout in agar
    assays. Spatial inhibition supports diffusible antagonism but does not identify
    the active molecule; computational BGC analysis did not find one shared Bacillus-specific
    cluster.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392388Z'
  quote: inhibition halo
- evidence_id: pseudomonadota
  kind: primary_source
  reference: PMID:40590505
  locator: 'Results: second deconstruction within Pseudomonadota; Fig 1D caption;
    Discussion final paragraph'
  summary: Class-level dropouts did not identify one necessary class; combinations
    protected more effectively than isolated classes. Niche overlap remains a hypothesis
    rather than demonstrated resource competition.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392389Z'
  quote: could not identify a focal taxon
- evidence_id: bbc1
  kind: primary_source
  reference: PMID:40590505
  locator: 'Results: immune gene expression and bbc1 intervention; Fig 5 caption;
    Discussion'
  summary: Bacillus inoculation protected both wild type and the specified co-receptor-deficient
    mutant in the open-coir assay. The intervention does not disable every immune
    pathway. RNA-seq describes host expression and is not a direct assay excluding
    all immune contributions.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392390Z'
  quote: fully functional immune system
- evidence_id: immune-qualification
  kind: primary_source
  reference: PMID:40590505
  locator: Abstract contrasted with Discussion paragraphs on direct and systemic effects
  summary: The abstract uses a strong immune-independence interpretation, reflected
    in the description. Discussion explicitly leaves induced-resistance involvement
    unresolved, and the current graph preserves this caveat. The review identifies
    an inconsistency in qualification, not absence of any supporting source wording.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392392Z'
  quote: induced resistance
- evidence_id: culture
  kind: primary_source
  reference: PMID:40590505
  locator: 'Methods: Bacterial culture and plant inoculation; seed growth; closed/agar/open
    systems'
  summary: LB revival and MS inoculation conditions are source-backed. The preparation
    includes two culture ages rather than one homogeneous culture. Inoculum normalization
    differs among experimental systems; the MS evidence explanation specifically limits
    its value to the closed system. The light/temperature excerpt concerns seedling
    plates before transfer.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392393Z'
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity, functional-role, evidence and cultivation definitions
  summary: The schema permits aggregate taxa and optional role/dataset fields. A missing
    role on heterogeneous Bacteria is not permission to invent a common function.
    Dataset typing and external medium links improve retrieval without changing measured
    biology.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392395Z'
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO and GO snapshots
  locator: Seven distinct ID-label pairs across fifteen occurrences; rank and GO definition
    checks
  summary: All pairs match. Bacteria/domain, Bacillus/genus and Pseudomonadota/phylum
    signal nested scope. GO0042742 is broader than host immunity, so its use does
    not alone contradict immune-impaired protection. Halo inhibition does not independently
    establish a triggered bacterial defensive response. The Bacillus GTDB majority
    mapping does not prove all 22 isolates have that GTDB genus.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392640Z'
  snapshot_sha256: 4190998e0e329fc3044901cb50262db262ea257086ff7a30ab7bcbd19c1d64de
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  locator: Twenty-nine evidence occurrences against independently fetched main article
    XML and committed cache
  summary: All 29 match fresh XML after NFKC/whitespace normalization. The cache has
    one normalized miss caused solely by a separator before the GEO accession period,
    rather than absent supporting text. No source quote was repaired or canonical
    cache changed.
  support: supports
  accessed_at: '2026-10-21T06:50:13.392897Z'
  snapshot_sha256: 1859d103547218226adab36080fc9ea978888a12cbcc8f03ccdf196e7e30da78
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=40590505&retmode=xml
  locator: Independent public metadata
  summary: PMID40590505 identifies the cited SynCom150 paper.
  support: supports
  accessed_at: '2026-10-21T06:46:26.093596Z'
  snapshot_sha256: a7de33756e697acacfa82e24fecfd941559e0569a15b83e12588293ee92e20f7
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1093/ismejo/wraf134
  locator: Independent public metadata
  summary: DOI10.1093/ismejo/wraf134 identifies the same paper; publication metadata
    is independently verified.
  support: supports
  accessed_at: '2026-10-21T06:46:26.093720Z'
  snapshot_sha256: 8fe631faf3338daf587e12de96bd318028956655fcec25f340f414377f71d39d
- evidence_id: bioproject
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=1175571&retmode=xml
  locator: Independent public metadata
  summary: PRJNA1175571 is public and corresponds to the source sequencing project;
    metadata does not verify each strain or raw read.
  support: supports
  accessed_at: '2026-10-21T06:46:26.094009Z'
  snapshot_sha256: 6ccc4ca4ea50f7d41d280ce0e57a962d28e57ebb91d56a698de842833cecfb46
- evidence_id: geo
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE285599&targ=self&form=text&view=full
  locator: Independent public metadata
  summary: GSE285599 is public Arabidopsis expression profiling, directly links the
    source PMID and BioProject, and lists 18 sample accessions. It is host RNA-seq,
    not a Bacillus expression dataset.
  support: supports
  accessed_at: '2026-10-21T06:46:26.094159Z'
  snapshot_sha256: 070a72f71e228b4d19eabaeb50af51373ec6311ed182cc233b8ff29878fc2d83
- evidence_id: history
  kind: record_content
  reference: history/records/Arabidopsis_Bacillus_Biocontrol_SynCom150; reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
  locator: Three sidecars, inline history and exact target decision row
  summary: Later graph curation removed workflow arrows and unsupported interaction
    labels. Earlier mutualism wording in append-only history is superseded, not a
    current graph assertion. Existing immune and focal-taxon discussions are preserved.
  support: supports
  accessed_at: '2026-10-21T06:50:13.393638Z'
- evidence_id: local-search
  kind: search
  reference: references_cache; history; reports/causal_graph_review/decisions; kb/taxa
  locator: Source PMID and record ID/slug search including hidden and ignored files
  summary: Located the primary cache, three history sidecars and prior graph decision.
    No assertion of globally absent taxon or source data is based on this identifier
    search.
  support: supports
  accessed_at: '2026-10-21T06:50:13.393641Z'
  search_scope: rg --no-ignore --hidden -l for 40590505, Arabidopsis_Bacillus_Biocontrol_SynCom150
    and CommunityMech:000368 in the four named trees.
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources runner discovery
  locator: Reused bounded task-runtime and sibling discovery receipt from the preceding
    record
  summary: No runner in the owned runtime; a candidate in another task checkout was
    not executed. No expression catalog coverage was queried. GEO and primary Methods
    supply host RNA-seq context; no iModulon membership is claimed.
  support: supports
  accessed_at: '2026-10-21T06:50:13.393820Z'
  snapshot_sha256: ad01c2d3ebb0536fec73f2e2ce83629e45b9e1a30a0c8d1575de49795aa9225a
  search_scope: Prior exact PATH/module resolution and ignored-inclusive bounded filename
    search, reused explicitly; no execution in another checkout.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  locator: Actual execution 2026-10-21T06:46:04.910083+00:00 to 2026-10-21T06:46:05.711539+00:00
  summary: Schema validation passed for the target.
  support: supports
  accessed_at: '2026-10-21T06:46:05.711539Z'
  snapshot_sha256: 2b2b7c1ab16307f994426941408a55241afacab82ee475eb57ca43f5a90e3280
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
    --out /private/tmp/cm-review-session/batch-03/000368/strict-report.tsv
  locator: Actual execution 2026-10-21T06:46:04.910312+00:00 to 2026-10-21T06:46:07.458542+00:00
  summary: Strict closed-schema and cross-field validation passed for the target.
  support: supports
  accessed_at: '2026-10-21T06:46:07.458542Z'
  snapshot_sha256: 91b592ee9efbae3e8b35f2125bf2f5c164f44e542021376aa47b1f2ddad06d0c
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  locator: Actual execution 2026-10-21T06:46:04.910414+00:00 to 2026-10-21T06:46:07.428024+00:00
  summary: Native ontology-term validation passed for the target.
  support: supports
  accessed_at: '2026-10-21T06:46:07.428024Z'
  snapshot_sha256: 390aee71fae5a0b644d0eb997b78aaf4589ad4a30fa6fcb5a08032f87e1143bf
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  locator: Actual execution 2026-10-21T06:46:05.711917+00:00 to 2026-10-21T06:46:05.818249+00:00
  summary: GTDB structural grounding validation passed; this is not an isolate-level
    crosswalk audit.
  support: supports
  accessed_at: '2026-10-21T06:46:05.818249Z'
  snapshot_sha256: 01902e6636830941234621bc258d43e5b5ea0b8b4c6edb3a6f9e36deafac5e9a
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  locator: Actual execution 2026-10-21T06:46:05.818548+00:00 to 2026-10-21T06:46:07.468750+00:00
  summary: GTDB domain validation passed for the target.
  support: supports
  accessed_at: '2026-10-21T06:46:07.468750Z'
  snapshot_sha256: e8de640c31d0279d64004a0d061b1e45de9b447eb72f3684f11f9db8c47261e4
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Arabidopsis_Bacillus_Biocontrol_SynCom150
  locator: Actual execution 2026-10-21T06:46:07.428491+00:00 to 2026-10-21T06:46:08.269665+00:00
  summary: All three target history sidecars passed native validation.
  support: supports
  accessed_at: '2026-10-21T06:46:08.269665Z'
  snapshot_sha256: 1d7a8bef2d7b6f7ea56f19579ec95cf4523f647829278cd2ca8e5500780f8247
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T06:46:08.270988+00:00 to 2026-10-21T06:46:08.342614+00:00
  summary: Read-only reference-cache filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T06:46:08.342614Z'
  snapshot_sha256: c00bbe687944f721bbbc36a252bec641b536057812ba2d4c24e8de9e11b17a7a
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
  locator: Actual execution 2026-10-21T06:46:08.342989+00:00 to 2026-10-21T06:46:09.902430+00:00
  summary: Native reference validation passed; committed cache hashes remained unchanged.
  support: supports
  accessed_at: '2026-10-21T06:46:09.902430Z'
  snapshot_sha256: d415f7a59ee4b9d7fb261e80700c4130f3005608bab0927188be3b621d11411f
- evidence_id: check-audit-network
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  locator: Actual finish 2026-10-20T07:08:14.467705+00:00
  summary: 'Earlier correct-runtime corpus run retained: 477 records, 57 warnings
    across 21 records, zero errors and exit 1; this target was not listed.'
  support: supports
  accessed_at: '2026-10-20T07:08:14.467705Z'
  snapshot_sha256: e2122e512641be2226ad12ab146b2c8f7d1e153f1211745e4816457834a42667
- evidence_id: check-check-network-quality
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  locator: Actual finish 2026-10-20T07:08:13.673449+00:00
  summary: 'Earlier correct-runtime corpus run retained: 477 records, 57 warnings
    across 21 records, zero errors and exit 1; this target was not listed.'
  support: supports
  accessed_at: '2026-10-20T07:08:13.673449Z'
  snapshot_sha256: b0cb58371a5a771dcbd671952ee68dfe5f26169d08240b66162aa83580fb5229
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: Fresh independent read-only API check and native metric components in support-audit.json
  summary: No target network issue returned; eleven evidence items across five nodes
    give mean 2.2 and all three aggregate descriptors participate.
  support: supports
  accessed_at: '2026-10-21T06:50:13.400873Z'
  snapshot_sha256: 6aa2524e447f1f4e470223edacb4587a717ff157084097bfc324f0a33fb90b1c
assessments:
- assessment_id: identity
  area: identity
  topic: SynCom150 and nested protective subsets
  outcome: supported
  summary: The source and target are resolved. Aggregate Bacteria and nested protective
    subsets are clearly labeled. The review does not treat these descriptors as three
    independent members or certify the full strain inventory.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - identity
  - primary
  - pubmed
  - crossref
  dimensions:
  - name: community_scope
    value: 150-member root-derived SynCom with nested protective subsets
    definition: Full SynCom, taxonomic dropouts/add-ins and Bacillus-only arms remain
      distinct.
    evidence_ids:
    - identity
    - bacillus
    - pseudomonadota
  - name: source_strain
    value: 150 genome-sequenced isolates; 22 Bacillus subset
    definition: Exact isolate roster remains in cited Supplementary Dataset S1, not
      independently audited here.
    evidence_ids:
    - identity
    - bacillus
  - name: experimental_setting
    value: Closed irradiated-coir, agar and open unsterilized-coir systems
    definition: Assays differ in background community, inoculation and readout; no
      universal field outcome is implied.
    evidence_ids:
    - primary
    - culture
  - name: evidence_tier
    value: Controlled protection interventions, halo inhibition, host RNA-seq and
      genomic prediction
    definition: Molecular antagonists, induced-resistance contribution and microbial
      fitness effects remain unresolved.
    evidence_ids:
    - halo
    - bbc1
    - immune-qualification
  - name: medium
    value: Source-specific LB preparation and MS inoculation
    definition: Two culture ages and system-specific inoculum dilutions must remain
      distinct.
    evidence_ids:
    - culture
- assessment_id: taxonomy
  area: grounding
  topic: taxonomy[0:3], rank and GTDB scope
  outcome: supported
  summary: Encoded IDs and labels are correct at their stated ranks. Source-supported
    subset roles should not be generalized to all members of Bacillus or Pseudomonadota
    outside this inoculum. No functional role need be invented for the heterogeneous
    whole-community aggregate.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - identity
  - ontology
  - schema
  - bacillus
  - pseudomonadota
- assessment_id: description
  area: evidence
  topic: Description immune-activation interpretation
  outcome: concern
  summary: The description follows the abstract interpretation but omits the Discussion
    limitation retained by node 4 and open discussions. Protection despite the tested
    co-receptor defect and lower marker expression does not exclude every induced-resistance
    contribution.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - bbc1
  - immune-qualification
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: SynCom Colonization and Partial Growth Rescue
    in Irradiated Coir'
  outcome: supported
  summary: Aggregate colonization and partial growth rescue are supported.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - colonization
  - primary
  details: 'Participants: full SynCom150 and Arabidopsis in irradiated coir. Direction:
    inoculation toward recovered aggregate bacterial communities and partial host
    growth improvement; individual strain establishment and reciprocal fitness benefits
    are not resolved. Linked primary evidence provides the exact source locator and
    a bounded verbatim excerpt.'
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Bacillus-Dependent Pto Leaf-Pathogen Suppression'
  outcome: supported
  summary: Dropout/add-in and diversity interventions support Bacillus-subset protection.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - bacillus
  - primary
  details: 'Participants: the source Bacillus subset and challenged Arabidopsis, with
    external Pto DC3000 as pathogen. Direction: Bacillus inclusion toward reduced
    pathogen leaf colonization. Coir and agar diversity tests must not be collapsed
    into one protocol. Linked primary evidence provides the exact source locator and
    a bounded verbatim excerpt.'
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Diverse Bacillus In Vitro Pto Antagonism'
  outcome: supported
  summary: Observed agar inhibition and the qualified BGC result are supported.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - halo
  - primary
  details: 'Participants: individual screened Bacillus isolates and Pto in vitro.
    Direction: isolate presence toward lower spatial luminescence. A diffusible antagonist
    is inferred; no single molecule, reciprocal competition or ecological transition
    to later assays is established. Linked primary evidence provides the exact source
    locator and a bounded verbatim excerpt.'
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Pseudomonadota Multi-Class Pto Protection'
  outcome: supported
  summary: Multi-class protection is supported without one resolved focal class.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - pseudomonadota
  - primary
  details: 'Participants: Pseudomonadota subsets, challenged Arabidopsis and Pto.
    Direction: combined inoculum toward protection; class dropouts/add-ins do not
    isolate resource competition. Linked primary evidence provides the exact source
    locator and a bounded verbatim excerpt.'
- assessment_id: node-4
  area: graph
  topic: 'ecological_interactions[4]: Bacillus Protection in bbc1 Immune-Impaired
    Arabidopsis'
  outcome: supported
  summary: Protection despite the specified immune defect is supported.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - bbc1
  - primary
  details: 'Participants: 22-strain Bacillus inoculum, wild-type or bbc1 Arabidopsis
    and Pto in open unsterilized coir. Direction: inoculation toward reduced pathogen
    counts. This does not eliminate all immunity or establish mutualistic bacterial
    benefit. Linked primary evidence provides the exact source locator and a bounded
    verbatim excerpt.'
- assessment_id: arrows
  area: graph
  topic: ecological_interactions[*].downstream
  outcome: not_applicable
  summary: No downstream arrows remain. Source-to-follow-up experiment order is not
    ecological causation.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - history
- assessment_id: process-terms
  area: grounding
  topic: Node biological_processes
  outcome: supported
  summary: Canonical process labels resolve. Broad defense-response mapping must not
    be read as proof of activated host immunity or an induced self-defense mechanism
    in the halo bacterium; the source-specific phenotypes remain in the descriptions.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - ontology
  - halo
  - bbc1
- assessment_id: engineering
  area: scope
  topic: engineering_design and intervention contexts
  outcome: supported
  summary: Top-down assembly/deconstruction, pathogen readouts, host expression and
    biosynthetic prediction endpoints match the main article. The GFP reporter strain
    used separately for leaf localization must not be added to SynCom150 membership
    from that assay alone.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - primary
  - identity
  - bacillus
  - culture
- assessment_id: environment
  area: grounding
  topic: Laboratory and modeled rhizosphere environments
  outcome: supported
  summary: The formal laboratory environment and modeled rhizosphere distinguish controlled
    study setting from natural source habitat. Notes retain the open-coir validation
    system rather than claiming all assays are gnotobiotic.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - ontology
  - culture
- assessment_id: cultivation
  area: scope
  topic: Growth media, environmental factors and cultivation_setup
  outcome: concern
  summary: Source-backed LB and MS contexts are represented. Culture-age and system-specific
    inoculum details must remain qualified; the seedling light/temperature evidence
    is not a numeric chamber profile for every later assay. Exact external medium
    linkages are missing.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - culture
  - schema
- assessment_id: datasets
  area: completeness
  topic: External resources and associated_datasets
  outcome: concern
  summary: Both resource accessions verify and remain relevant. They are represented
    only as generic external resources; no associated_datasets entries expose their
    sequencing/transcriptomic roles for structured retrieval.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - bioproject
  - geo
  - schema
- assessment_id: history
  area: provenance
  topic: History, cache and open scientific questions
  outcome: supported
  summary: Three valid sidecars and the prior graph decision preserve experimental
    scope and unresolved mechanism. All snippets verify against current primary XML,
    with only a cache text-node spacing difference for one accession sentence.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - history
  - snippets
  - immune-qualification
- assessment_id: metals
  area: scope
  topic: Metal and REE fields
  outcome: supported
  summary: No metal or rare-earth-processing mechanism is asserted; media salts or
    predicted clusters do not establish one.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - primary
- assessment_id: validation
  area: schema
  topic: Native gates and independent source checks
  outcome: supported
  summary: Eight focused checks passed, seven ontology pairs match and twenty-nine
    snippets verify against primary XML. Corpus failures are retained; these deterministic
    checks do not decide mechanism scope.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - ontology
  - snippets
  - check-validate
  - check-validate-strict
  - check-validate-history
  - check-audit-network
  - native-target
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Completeness 30 reflects aggregate representation and field placement,
    not a need to invent a whole-community role; quality 100 is not scientific approval.
  target_ids:
  - CommunityMech:000368
  evidence_ids:
  - record
  - schema
  - native-target
  metrics:
  - name: completeness
    value: 30
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including all roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). Aggregate Bacteria lacks a role, so 0 + 5 + 0 + 10 +
      5 + 10 + 0 + 0 = 30. Missing heterogeneous-aggregate role is not itself a defect.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1 = 0, P2 = 1, P3 = 2, P4 = 0; 11 items /
      5 nodes = 2.2; native COMPLETE. 100 - 10 - 4 + 20 + 15 = 121, clamped to 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P2
    value: 1
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P3
    value: 2
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
findings:
- finding_id: immune-qualification
  issue_key: cm-000368-immune-qualification
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: interpretation scope affects the stated protective
    mechanism.'
  rule_id: review-checklist.causal_claims
  status: open
  certainty: confirmed
  title: Description omits the source immune-mechanism qualification
  description: The abstract supports an immune-independence interpretation, which
    the description repeats. The full Discussion and existing node 4/discussions retain
    unresolved induced-resistance contributions. The summary can be read more broadly
    than the actual bbc1 and expression tests establish; this is a qualification inconsistency,
    not a claim that the source contains no supporting statement.
  target_ids:
  - CommunityMech:000368
  field_paths:
  - description
  evidence_ids:
  - record
  - bbc1
  - immune-qualification
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
    role: canonical_record
- finding_id: media-linkage
  issue_key: cm-000368-media-linkage
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded provenance, identity qualification or cultivation-linkage
    gap; source-supported endpoint claims remain recoverable.'
  rule_id: P3.1
  status: open
  certainty: confirmed
  title: LB and MS media have no external identifiers
  description: The two growth-media entries carry source-supported preparation context
    but lack CultureMech or MediaIngredientMech identifiers.
  target_ids:
  - CommunityMech:000368
  field_paths:
  - growth_media[0]
  - growth_media[1]
  evidence_ids:
  - record
  - culture
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
    role: canonical_record
- finding_id: typed-datasets
  issue_key: cm-000368-typed-datasets
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded provenance, identity qualification or cultivation-linkage
    gap; source-supported endpoint claims remain recoverable.'
  rule_id: review-checklist.datasets
  status: open
  certainty: confirmed
  title: Verified sequencing resources are not typed as associated datasets
  description: PRJNA1175571 and GSE285599 resolve and are linked as external resources,
    but associated_datasets is absent. This is a structured representation gap, not
    missing source accessions.
  target_ids:
  - CommunityMech:000368
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - record
  - bioproject
  - geo
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
    role: canonical_record
actions:
- action_id: fix-immune-qualification
  description: Carry the specific co-receptor-defect and unresolved induced-resistance
    qualification into the description while retaining the demonstrated protection
    phenotype.
  finding_ids:
  - immune-qualification
  target_ids:
  - CommunityMech:000368
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
    role: canonical_record
  acceptance_checks:
  - Description agrees with node 4 and existing open discussions.
  - No test of bbc1 is described as removal of all host immune function.
  - Source abstract and Discussion interpretations are both represented fairly.
  - Run strict and reference checks.
- action_id: fix-media-linkage
  description: Link exact compatible external medium or ingredient entries where available
    without collapsing distinct source preparations.
  finding_ids:
  - media-linkage
  target_ids:
  - CommunityMech:000368
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
    role: canonical_record
  acceptance_checks:
  - Any linked recipe matches the formulation and assay context.
  - No unreported ingredient or growth condition is inferred.
  - Run focused medium/linkage validation appropriate to the curated change.
- action_id: fix-typed-datasets
  description: Represent the existing source-relevant accessions with accurate dataset
    types while preserving their current links and evidence.
  finding_ids:
  - typed-datasets
  target_ids:
  - CommunityMech:000368
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Bacillus_Biocontrol_SynCom150.yaml
    role: canonical_record
  acceptance_checks:
  - Amplicon data and host RNA-seq are distinguished.
  - GEO is not misrepresented as Bacillus transcriptomics.
  - No raw-data or strain-level validation is implied by project metadata.
  - Run strict and reference checks.
limitations:
- Supplementary Dataset S1 and the supplement archive are cited/listed but were not
  retrieved; all 150 individual strain identities and their current taxonomy are not
  certified. The record intentionally uses aggregate membership.
- Figure captions and reported main-text results were read, but figure geometry, raw
  sequencing/host-expression data and supplement-only measurements were not independently
  reanalyzed.
- GTDB validation checks the encoded grounding structure/domain; this review does
  not independently reproduce the historical crosswalk counts or assign all 22 isolates
  to a present-day GTDB genus.
- Host immune contribution, active antagonistic molecules and bacterial fitness benefits
  remain unresolved. The source abstract supports a stronger interpretation than the
  Discussion and bounded current graph.
- Optional structured-expression adapter was not available in the owned runtime; a
  candidate in another checkout was not executed. Public GEO metadata supplies host
  RNA-seq context, not a functional proof.
- Required corpus gates retain actual warning failures; field-completeness and network
  scores do not establish scientific truth.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Short quotations from the single source total 24 words.
- A one-snippet cache mismatch is solely whitespace before a punctuation mark; fresh
  primary XML supports the exact evidence text.
tags:
- record-review
- syncom
- rhizosphere
- batch-03
```
