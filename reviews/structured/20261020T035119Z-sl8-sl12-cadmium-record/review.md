# SL8–SL12 coculture: bounded evidence and metadata review

- Review: 20261020T035119Z-sl8-sl12-cadmium-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-20T03:47:18.943009Z
- Finished UTC: 2026-10-20T03:51:19.548422Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Genus-level identity, phenotype-level node and molecular-causality caveat are supported. Three minor metadata findings concern missing roles, combined sequence accessions and response values stored as environmental factors. iProX identity remains unverified. Cultivation optimization and genetic intervention details are excluded; this is not a completed full-scope review.

## Scope And Provenance

Entire record read; assessed identity, ontology labels, phenotype-level node, absence of arrows, evidence provenance, public metadata and native validation.

Selection: Third uncovered path of batch 02; baseline plus validated pending batch-01 coverage.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a4611c913c8da9619673df63a0c2cce3aa206a83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000374 | kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml | maintained | Achromobacter-Enterobacter SL8-SL12 Cadmium Immobilization Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000374 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml |
| validate-strict | passed | True | CommunityMech:000374 | uv run python scripts/validate_strict.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml --out /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000374 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000374 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000374 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml |
| validate-history | passed | True | CommunityMech:000374 | No issues found |
| normalize-cache-names-check | passed | True | CommunityMech:000374 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000374 | Validating kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000374 | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| check-network-quality | failed | True | CommunityMech:000374 | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| Optional structured-source adapter | unavailable | False | CommunityMech:000374 | Runner unavailable in isolated runtime; inspected public catalog fallback has no matching organism. |
| iProX public accession identity | unavailable | True | CommunityMech:000374 | HTTP response is a generic client application shell and does not verify the claimed accession. No scientific contradiction inferred. |

## Scientific And Domain Assessments

### Strain pair, source category and experimental setting

identity: supported. Targets: CommunityMech:000374.

The defined synthetic pair is distinguished from the soil microbiome in greenhouse observations. Genus-level grounding retains the reported identification limits despite species names in the title and GenBank submissions. No genome-backed species promotion is justified here.

### taxonomy, environment, process and chemical identifiers

grounding: supported. Targets: CommunityMech:000374.

The six curated identifiers resolve and native GTDB coherence/domain gates pass. DOMINANT reasonably describes the two defining members, with no quantitative abundance implied. Cadmium is represented by the ion descriptor; an empty metal enum list alongside SIGNIFICANT is explicitly explained by the vocabulary limitation.

### ecological_interactions[0]: SL8-SL12 cooperative cadmium immobilization

graph: supported. Targets: CommunityMech:000374.

This is a community phenotype, not a resolved directed interaction. Both listed strains are included by broad COMMUNITY_LEVEL scope. Experimental removal and material-characterization observations support the bounded summary. Possible EPS involvement and molecular causality remain uncertain. No obligate mutual benefit, exchanged substrate or gene-level cause is established.

Participants: NCBITaxon:222 SL8 and NCBITaxon:547 SL12. Direction: none asserted. Mechanism: phenotype-level immobilization with observed partitioning/spectroscopy, not a causal molecular route. Context: source laboratory comparison; separate greenhouse outcomes. Exact field locator ecological_interactions[0]; PMID:42307251; source limitations quote in causality.

### ecological_interactions[0].downstream

graph: not_applicable. Targets: CommunityMech:000374.

The whole target contains no downstream edges. Prior removal of dangling measured-outcome arrows is consistent with the current schema and does not leave a missing required causal graph.

### description and environmental_factors

evidence: concern. Targets: CommunityMech:000374.

Reported removal and greenhouse outcome claims are bounded to the studied contexts. Measured response values are mixed into environmental_factors, making experimental exposures and results difficult to distinguish in downstream queries. No field-scale efficacy or deployment recommendation is inferred.

### taxonomy[0..1].functional_role

completeness: concern. Targets: CommunityMech:000374.

Neither member has a functional_role entry. This affects the native completeness metric, but available enum choices must not force an unsupported donor/consumer or degradation relationship. The omission is a metadata gap, not a mandate to invent mechanism.

### associated_datasets and external_resources

provenance: concern. Targets: CommunityMech:000374.

Publication, GenBank, MetaboLights and supplemental metadata resolve. The sequence accession field combines two independent identifiers and should preserve independently resolvable entries. iProX remains unverified because its HTTP response is a generic shell. This is an access limitation, not evidence of a false citation.

### discussions and prior evidence boundaries

evidence: supported. Targets: CommunityMech:000374.

The open causality gap accurately reflects the primary source limitation. Proposed genetic interventions are not assessed or refined by this review. Evidence matching is positive but does not establish that those proposed interventions are warranted.

### engineering_design operational details and growth_media

scope: unknown. Targets: CommunityMech:000374.

Parameter-level cultivation, selection and stress-tolerance methods, medium optimization/linking, and proposed genetic perturbations are outside this bounded review. No corrected operational details are supplied.

### Structured expression-source applicability

evidence: not_applicable. Targets: CommunityMech:000374.

No exact strain dataset in the inspected public catalog; absence is not evidence against the phenotype.

### Native gates and graph references

schema: supported. Targets: CommunityMech:000374.

Focused gates pass; both defined members are credited by the unqualified community-level node. No downstream reference exists to dangle. These facts do not validate molecular causation or excluded operational details. Required corpus warning failures remain outside this target.

### Native presence and assessed-finding metrics

completeness: concern. Targets: CommunityMech:000374.

Completeness 40 reflects missing roles in the all-or-nothing required block and one node. Quality 100 is capped despite three minor findings and partial review; it is not approval of excluded or unverified claims.

## Findings

### role-metadata: Taxon functional roles are unrepresented

minor / open / confirmed; issue key: cm-000374-role-metadata.

Both taxonomy members lack functional_role entries. The native completeness rubric requires roles for its metadata block, although the schema permits their absence. A role should not be forced from coculture membership alone.

### combined-accession: Two independently resolvable sequence identifiers share one accession field

minor / open / confirmed; issue key: cm-000374-combined-accession.

associated_datasets[0].accession combines two GenBank accessions, obscuring individual identifier resolution and strain linkage. Both records independently resolve.

### outcome-factor: Measured outcomes are mixed with environmental exposures

minor / open / confirmed; issue key: cm-000374-outcome-factor.

Several environmental_factors entries contain removal percentages or plant/soil response endpoints. The values are source-backed, but their placement mixes results with experimental environmental context.

## Recommended Actions And Acceptance Checks

### fix-role-metadata

Clarify whether the existing vocabulary can express the already supported ecological role; otherwise preserve an explicit vocabulary gap.

- Do not add inferred reciprocal benefit or exchange.
- Any role annotation is evidence-backed and matches the schema definition.
- Run strict and network validation after authorized metadata curation.

### fix-combined-accession

Represent each accession distinctly while preserving the appropriate strain association and publication.

- Each identifier resolves to its own metadata record.
- Strain-to-accession correspondence remains unambiguous.
- Run strict and resource-reference checks.

### fix-outcome-factor

Distinguish measured responses from environmental inputs in supported metadata fields or retain an explicit schema gap.

- Do not silently change the numerical endpoint or comparison scope.
- No new cultivation or intervention design is introduced.
- Run strict and evidence checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml; Entire target read; annotation-level assessment of two taxa, one node, no downstream edges, resources and history | supports | The record denotes a defined SL8/SL12 coculture, with separate laboratory and greenhouse observations. Review output does not reproduce cultivation parameters, stress-tolerance optimization or proposed genetic interventions. |
| primary | PMID:42307251; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13340288/fullTextXML; title, abstract, Results and Discussion, figures, source identifiers | supports | The paper supports a coculture-associated cadmium-immobilization phenotype and separate greenhouse outcomes. It explicitly treats molecular omics interpretations as correlative. Genus-level identification in Results is more cautious than the title and submitted sequence labels. |
| causality | PMID:42307251; Results and Discussion, final molecular-interpretation limitations paragraph | supports | The source explicitly limits causal claims. Existing phenotype summary and open uncertainty are reasonable; no new gene-level causal claim follows. |
| phenotype | PMID:42307251; Results: Growth inhibition and cadmium removal efficiency; Cd stress response; greenhouse efficacy | supports | The matched high-stress comparison supports greater measured removal by the coculture. The lower-stress comparison is not a universal advantage over every monoculture. Cd-associated partitioning and spectroscopy support observed material changes; possible EPS involvement remains an interpretation. Greenhouse reductions in bioavailable soil fractions and aboveground plant content do not demonstrate field deployment or overall soil-cadmium disappearance. |
| publication | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42307251&amp;retmode=xml; PMID/DOI/PMCID metadata | supports | PMID 42307251, DOI 10.1128/spectrum.01081-26 and PMC13340288 identify the same 2026 Microbiology Spectrum paper. |
| genbank | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&amp;id=PZ429300,PZ429301&amp;retmode=json; Public metadata response; accession-specific verification where stated | supports | Both sequence accession summaries resolve to the correct SL8 and SL12 partial 16S records. Submitted species names match the record notes; a submitted name is not independent genome-level species validation. |
| metabolights | https://www.ebi.ac.uk/metabolights/ws/studies/MTBLS14477; Public metadata response; accession-specific verification where stated | supports | Public metadata resolve MTBLS14477 with the matching extracellular-metabolite study title and strain pair. Raw measurements and sample tables were not reanalyzed. |
| zenodo | https://zenodo.org/api/records/20263325; Public metadata response; accession-specific verification where stated | supports | DOI 10.5281/zenodo.20263325 resolves to supplementary-material metadata for this article. Supplementary operational protocols and candidate-target tables were not extracted. |
| iprox | https://www.iprox.cn/page/project.html?id=IPX0017179000; Public metadata response; accession-specific verification where stated | context_only | HTTP 200 returned a generic application shell without the requested accession or study title. Public dataset identity and availability remain unverified; no missing-dataset conclusion follows. |
| ontology | OAK local NCBITaxon/ENVO/GO/CHEBI snapshots; Six unique curated identifiers | supports | All six IDs have the stated canonical labels. Genus assignments, laboratory environment, contaminated soil, cadmium ion and response-to-metal process are semantically appropriate. |
| schema | src/communitymech/schema/communitymech.yaml; AbundanceEnum, TaxonDescriptor, AssociatedDataset and EnvironmentalFactor | supports | DOMINANT is ordinal prominence and permits co-equal prominent members, not a percentage claim. Taxon roles are absent. A single accession field currently combines two sequence identifiers; endpoint values and imposed environmental factors are mixed. |
| snippets | kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml; All 25 evidence occurrences compared with XML or metadata | supports | Twenty-four snippets match after NFKC normalization and markup-induced whitespace removal. One PMCID snippet matches article identifier metadata, not a scientific Results passage. This lexical audit does not validate protocol choices or molecular intervention design. |
| history | history/records/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture; Four whole history entries and target row in reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml | supports | History explains removal of unsupported niche partitioning, dangling outcome arrows and redundant participant narrowing. The later graph review retained the phenotype node and molecular-causality gap without certifying all metadata. |
| local-search | references_cache; history/records; reports/causal_graph_review/decisions; kb/taxa; Ignored-inclusive citation, slug and identifier search | supports | The full-text cache, supplemental cache, history and graph decisions were located. Claims of missing roles and split accession objects refer to the entire target file, not external database absence. |
| adapter | https://imodulondb.org/api/datasets; Same-session complete public catalog: 20 organisms, 28 datasets | context_only | No exact SL8/SL12 strain dataset appears. Expression modules from unrelated model organisms cannot establish causality in this pair. The optional runner is unavailable in the isolated runtime. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml; Actual execution 2026-10-20T03:47:19.696985+00:00 to 2026-10-20T03:47:20.405731+00:00 | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml --out /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv; Actual execution 2026-10-20T03:47:19.699059+00:00 to 2026-10-20T03:47:22.313615+00:00 | supports | uv run python scripts/validate_strict.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml --out /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml; Actual execution 2026-10-20T03:47:19.701344+00:00 to 2026-10-20T03:47:21.952665+00:00 | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml; Actual execution 2026-10-20T03:47:20.406030+00:00 to 2026-10-20T03:47:20.533681+00:00 | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml; Actual execution 2026-10-20T03:47:20.534013+00:00 to 2026-10-20T03:47:22.359837+00:00 | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-history history/records/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture; Actual execution 2026-10-20T03:47:21.953048+00:00 to 2026-10-20T03:47:22.646315+00:00 | supports | No issues found |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-20T03:47:22.646896+00:00 to 2026-10-20T03:47:22.720871+00:00 | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml; Actual execution 2026-10-20T03:47:22.722079+00:00 to 2026-10-20T03:47:23.684181+00:00 | supports | Validating kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | just --no-dotenv audit-network; Actual run finished 2026-10-19T07:30:27.845593+00:00 | supports | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| check-check-network-quality | just --no-dotenv check-network-quality; Actual run finished 2026-10-19T07:30:43.193891+00:00 | supports | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |

## Limits And Additional Notes

- Partial scope: cultivation/selection protocols, medium-linkage optimization and proposed genetic interventions were not assessed or refined.
- iProX page returned a generic application shell; source advertises the accession, but study identity and availability remain unverified.
- MetaboLights and GenBank checks covered public metadata only; raw omics and sequence data were not reanalyzed. Zenodo check covered supplementary metadata, not its operational contents.
- Historical GTDB mapping aggregate counts were not reconstructed.
- Optional structured-source runner unavailable; public catalog has no exact strain dataset. Required corpus checks retain unrelated warning failures.
- No canonical record, cache, history or generated output changed.
- Every inspected input hash is unchanged; local supplemental cache was inventoried but not used to derive operational findings.
- Presence/quality metrics do not certify excluded content.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T035119Z-sl8-sl12-cadmium-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'SL8–SL12 coculture: bounded evidence and metadata review'
started_at: '2026-10-20T03:47:18.943009Z'
finished_at: '2026-10-20T03:51:19.548422Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Target not changed this session; earlier codex curation prevents
    claiming person-level independence.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: Genus-level identity, phenotype-level node and molecular-causality caveat
  are supported. Three minor metadata findings concern missing roles, combined sequence
  accessions and response values stored as environmental factors. iProX identity remains
  unverified. Cultivation optimization and genetic intervention details are excluded;
  this is not a completed full-scope review.
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
  - path: history/records/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture/2026-09-14T063944Z-codex-review.yaml
    sha256: eebbcb58e03a3c5cae1fff4f2ae9745e3967e33bd10cd7aacfca8ea10b6c3cfa
    role: context
  - path: history/records/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture/2026-09-14T064354Z-codex-network.yaml
    sha256: c1bf458c1519e4bbb312671f034ce270fb1bbbae5467a652d5677c04a22836d0
    role: context
  - path: history/records/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture/2026-09-14T154255Z-codex-participating-taxa.yaml
    sha256: 09035d2e4561ad023a1e40db8b934791b2b7ff3671354b25cfc4bc74f34ccdd3
    role: context
  - path: history/records/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture/20260914T063411Z-codex-3604dc.yaml
    sha256: bf2a0663e7c0e1845cb256c20ae44d77344531b011b41ec78ce3f8509f48c235
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    sha256: eeef4a3c72f6660c2263fe91ec7858610797c19fa513bf641e2a6234ff4414d4
    role: target
  - path: references_cache/PMID_42307251.supplement.md
    sha256: 292f06d875760cea5d5ca2c659dae6a0f637d8cd98d297db2aaa635fdb3042b2
    role: context
  - path: references_cache/PMID_42307251.txt
    sha256: e0f0fee88ee885a2049f2f726e05f9b6ab816346dc5186e5f1fea325464aba4e
    role: context
  - path: reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml
    sha256: 3e0877c63e94f1c87d6c78b6d5480a0be07d80f1cd18f8db5efda4e8e2ea4d26
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
- target_id: CommunityMech:000374
  path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  label: Achromobacter-Enterobacter SL8-SL12 Cadmium Immobilization Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
scope:
  description: Entire record read; assessed identity, ontology labels, phenotype-level
    node, absence of arrows, evidence provenance, public metadata and native validation.
  selection: Third uncovered path of batch 02; baseline plus validated pending batch-01
    coverage.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000374
  exclusions:
  - target: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml#growth_media;engineering_design.inoculation_strategy;discussions.proposed_experiments
    reason: Parameter-level cultivation, stress-tolerance optimization and genetic
      intervention recommendations are not assessed or refined. Review is restricted
      to non-operational identity, provenance and claim boundaries.
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml'
  target_ids:
  - CommunityMech:000374
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
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
  summary: "uv run python scripts/validate_strict.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml\
    \ --out /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv"
  target_ids:
  - CommunityMech:000374
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv
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

    uv run linkml-term-validator validate-data kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000374
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
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
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000374
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
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

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml'
  target_ids:
  - CommunityMech:000374
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
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
  - CommunityMech:000374
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-history history/records/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture
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
  - CommunityMech:000374
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
  summary: "Validating kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000374
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
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
  - CommunityMech:000374
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
  - CommunityMech:000374
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
  - CommunityMech:000374
  evidence_ids:
  - adapter
- check_id: iprox-identity
  name: iProX public accession identity
  status: unavailable
  required: true
  summary: HTTP response is a generic client application shell and does not verify
    the claimed accession. No scientific contradiction inferred.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - iprox
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  locator: Entire target read; annotation-level assessment of two taxa, one node,
    no downstream edges, resources and history
  summary: The record denotes a defined SL8/SL12 coculture, with separate laboratory
    and greenhouse observations. Review output does not reproduce cultivation parameters,
    stress-tolerance optimization or proposed genetic interventions.
  support: supports
  accessed_at: '2026-10-20T03:51:19.539909Z'
- evidence_id: primary
  kind: primary_source
  reference: PMID:42307251
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13340288/fullTextXML;
    title, abstract, Results and Discussion, figures, source identifiers
  summary: The paper supports a coculture-associated cadmium-immobilization phenotype
    and separate greenhouse outcomes. It explicitly treats molecular omics interpretations
    as correlative. Genus-level identification in Results is more cautious than the
    title and submitted sequence labels.
  support: supports
  accessed_at: '2026-10-20T03:47:32.915893Z'
  snapshot_sha256: c5dd556551ae9aebd45c50367b6738c792fd6ee74ccbc5070c77c219167c5cbf
- evidence_id: causality
  kind: primary_source
  reference: PMID:42307251
  locator: Results and Discussion, final molecular-interpretation limitations paragraph
  summary: The source explicitly limits causal claims. Existing phenotype summary
    and open uncertainty are reasonable; no new gene-level causal claim follows.
  support: supports
  accessed_at: '2026-10-20T03:47:32.915893Z'
  quote: direct causal validation (e.g., gene knockout) was not performed.
- evidence_id: phenotype
  kind: primary_source
  reference: PMID:42307251
  locator: 'Results: Growth inhibition and cadmium removal efficiency; Cd stress response;
    greenhouse efficacy'
  summary: The matched high-stress comparison supports greater measured removal by
    the coculture. The lower-stress comparison is not a universal advantage over every
    monoculture. Cd-associated partitioning and spectroscopy support observed material
    changes; possible EPS involvement remains an interpretation. Greenhouse reductions
    in bioavailable soil fractions and aboveground plant content do not demonstrate
    field deployment or overall soil-cadmium disappearance.
  support: supports
  accessed_at: '2026-10-20T03:47:32.915893Z'
- evidence_id: publication
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42307251&retmode=xml
  locator: PMID/DOI/PMCID metadata
  summary: PMID 42307251, DOI 10.1128/spectrum.01081-26 and PMC13340288 identify the
    same 2026 Microbiology Spectrum paper.
  support: supports
  accessed_at: '2026-10-20T03:47:32.916266Z'
  snapshot_sha256: e59b362728162859908c4199bfb34d386024f368fe6849768212b8dc6487e05f
- evidence_id: genbank
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=nuccore&id=PZ429300,PZ429301&retmode=json
  locator: Public metadata response; accession-specific verification where stated
  summary: Both sequence accession summaries resolve to the correct SL8 and SL12 partial
    16S records. Submitted species names match the record notes; a submitted name
    is not independent genome-level species validation.
  support: supports
  accessed_at: '2026-10-20T03:48:34.967017Z'
  snapshot_sha256: bfc3efd8c5be77182d22584d3cbe70a233babd4ea513ab4c5bd1c152efb5d6b6
- evidence_id: metabolights
  kind: database
  reference: https://www.ebi.ac.uk/metabolights/ws/studies/MTBLS14477
  locator: Public metadata response; accession-specific verification where stated
  summary: Public metadata resolve MTBLS14477 with the matching extracellular-metabolite
    study title and strain pair. Raw measurements and sample tables were not reanalyzed.
  support: supports
  accessed_at: '2026-10-20T03:48:34.967451Z'
  snapshot_sha256: 224a19f555be4bd88cbe3ca561e6d6db5d0b360b3eca5a8edb36c2459ae9fece
- evidence_id: zenodo
  kind: database
  reference: https://zenodo.org/api/records/20263325
  locator: Public metadata response; accession-specific verification where stated
  summary: DOI 10.5281/zenodo.20263325 resolves to supplementary-material metadata
    for this article. Supplementary operational protocols and candidate-target tables
    were not extracted.
  support: supports
  accessed_at: '2026-10-20T03:48:34.967744Z'
  snapshot_sha256: dabcec2485f4c119f730884809d238721729c88f5961f0cead43bfb7dedd7c17
- evidence_id: iprox
  kind: database
  reference: https://www.iprox.cn/page/project.html?id=IPX0017179000
  locator: Public metadata response; accession-specific verification where stated
  summary: HTTP 200 returned a generic application shell without the requested accession
    or study title. Public dataset identity and availability remain unverified; no
    missing-dataset conclusion follows.
  support: context_only
  accessed_at: '2026-10-20T03:48:34.967601Z'
  snapshot_sha256: 999052c9982d313d1b25f98cb59fc830b9a4f0012b345d83bd21c7a03adf30ae
- evidence_id: ontology
  kind: authority
  reference: OAK local NCBITaxon/ENVO/GO/CHEBI snapshots
  locator: Six unique curated identifiers
  summary: All six IDs have the stated canonical labels. Genus assignments, laboratory
    environment, contaminated soil, cadmium ion and response-to-metal process are
    semantically appropriate.
  support: supports
  accessed_at: '2026-10-20T03:49:08.859567Z'
  snapshot_sha256: f06bdde6c192e2abcbf3cb15f51a67c3e6e868c035591d8abb17fc38c4e4e8ba
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: AbundanceEnum, TaxonDescriptor, AssociatedDataset and EnvironmentalFactor
  summary: DOMINANT is ordinal prominence and permits co-equal prominent members,
    not a percentage claim. Taxon roles are absent. A single accession field currently
    combines two sequence identifiers; endpoint values and imposed environmental factors
    are mixed.
  support: supports
  accessed_at: '2026-10-20T03:51:19.542351Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  locator: All 25 evidence occurrences compared with XML or metadata
  summary: Twenty-four snippets match after NFKC normalization and markup-induced
    whitespace removal. One PMCID snippet matches article identifier metadata, not
    a scientific Results passage. This lexical audit does not validate protocol choices
    or molecular intervention design.
  support: supports
  accessed_at: '2026-10-20T03:51:19.542699Z'
  snapshot_sha256: d41a4a9f9d3a3402c793614a9099c28d72000dd627bb351c5c5e01224e6c4e5a
- evidence_id: history
  kind: record_content
  reference: history/records/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture
  locator: Four whole history entries and target row in reports/causal_graph_review/decisions/20261005-six-records-batch3.yaml
  summary: History explains removal of unsupported niche partitioning, dangling outcome
    arrows and redundant participant narrowing. The later graph review retained the
    phenotype node and molecular-causality gap without certifying all metadata.
  support: supports
  accessed_at: '2026-10-20T03:51:19.542717Z'
- evidence_id: local-search
  kind: search
  reference: references_cache; history/records; reports/causal_graph_review/decisions;
    kb/taxa
  locator: Ignored-inclusive citation, slug and identifier search
  summary: The full-text cache, supplemental cache, history and graph decisions were
    located. Claims of missing roles and split accession objects refer to the entire
    target file, not external database absence.
  support: supports
  accessed_at: '2026-10-20T03:51:19.543228Z'
  search_scope: rg --no-ignore --hidden -l '42307251|Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture|spectrum.01081-26'
    references_cache history/records reports/causal_graph_review/decisions kb/taxa
  snapshot_sha256: 616eeb976a65bce919a9516432769e4a3c583c92f571018167cf86bff6fdcd48
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Same-session complete public catalog: 20 organisms, 28 datasets'
  summary: No exact SL8/SL12 strain dataset appears. Expression modules from unrelated
    model organisms cannot establish causality in this pair. The optional runner is
    unavailable in the isolated runtime.
  support: context_only
  accessed_at: '2026-10-19T23:31:07.726770Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  locator: Actual execution 2026-10-20T03:47:19.696985+00:00 to 2026-10-20T03:47:20.405731+00:00
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml'
  support: supports
  accessed_at: '2026-10-20T03:47:20.405731Z'
  snapshot_sha256: 6865e8f6f5cbe30a494357436954cc35e1e0aa32a682e30e36c703bf01884b22
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv
  locator: Actual execution 2026-10-20T03:47:19.699059+00:00 to 2026-10-20T03:47:22.313615+00:00
  summary: "uv run python scripts/validate_strict.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml\
    \ --out /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-02/000374/strict-report.tsv"
  support: supports
  accessed_at: '2026-10-20T03:47:22.313615Z'
  snapshot_sha256: b6469f149028aaaf5dc9dddced8e3c15c4df21efbff1820987fc1d95129f6ed1
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  locator: Actual execution 2026-10-20T03:47:19.701344+00:00 to 2026-10-20T03:47:21.952665+00:00
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-10-20T03:47:21.952665Z'
  snapshot_sha256: ccd0ad22337d99e05bec5a7fbd68e4bed3209d37d8e53b350c9933ef9331e7a5
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  locator: Actual execution 2026-10-20T03:47:20.406030+00:00 to 2026-10-20T03:47:20.533681+00:00
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-10-20T03:47:20.533681Z'
  snapshot_sha256: dd2c57271e99acdffa419b03189d543614aeecc1a41dc0c437613ef4aa148483
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  locator: Actual execution 2026-10-20T03:47:20.534013+00:00 to 2026-10-20T03:47:22.359837+00:00
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml'
  support: supports
  accessed_at: '2026-10-20T03:47:22.359837Z'
  snapshot_sha256: c91a6c3c263660b7432d153d13da3a7c8331e9c2f92de6bbb506cfee44df3f63
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-history history/records/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture
  locator: Actual execution 2026-10-20T03:47:21.953048+00:00 to 2026-10-20T03:47:22.646315+00:00
  summary: No issues found
  support: supports
  accessed_at: '2026-10-20T03:47:22.646315Z'
  snapshot_sha256: 7ce1c7db4dfb8a7d74dbee9ff0cb7e1cb2c44c18a3f79807def7b2d6d1894236
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-20T03:47:22.646896+00:00 to 2026-10-20T03:47:22.720871+00:00
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-10-20T03:47:22.720871Z'
  snapshot_sha256: 515d329c05a774feb63f0925417c2c633e1b54d8b120261347191c2a87a59149
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  locator: Actual execution 2026-10-20T03:47:22.722079+00:00 to 2026-10-20T03:47:23.684181+00:00
  summary: "Validating kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-10-20T03:47:23.684181Z'
  snapshot_sha256: d7fc209cf742bd06dcb3f65876d171cdfa7fa8a9c0b38f7776b0d0b4b4b535a8
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
  topic: Strain pair, source category and experimental setting
  outcome: supported
  summary: The defined synthetic pair is distinguished from the soil microbiome in
    greenhouse observations. Genus-level grounding retains the reported identification
    limits despite species names in the title and GenBank submissions. No genome-backed
    species promotion is justified here.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - record
  - primary
  - publication
  - genbank
  dimensions:
  - name: source_strain
    value: Achromobacter sp. SL8 and Enterobacter sp. SL12
    definition: Source strain labels are supported; submitted species names are provenance,
      not new genome verification.
    evidence_ids:
    - primary
    - genbank
  - name: community_scope
    value: Defined synthetic bacterial pair
    definition: The pot soil community is a distinct recipient ecosystem, not the
      same two-member community.
    evidence_ids:
    - primary
  - name: experimental_setting
    value: Laboratory assays and separate greenhouse pots
    definition: Observed pot outcomes do not establish field efficacy or safety.
    evidence_ids:
    - primary
    - phenotype
  - name: medium_context
    value: Source-reported laboratory medium, parameter-level review excluded
    definition: This review does not refine cultivation or stress-tolerance methods.
    evidence_ids:
    - record
- assessment_id: grounding
  area: grounding
  topic: taxonomy, environment, process and chemical identifiers
  outcome: supported
  summary: The six curated identifiers resolve and native GTDB coherence/domain gates
    pass. DOMINANT reasonably describes the two defining members, with no quantitative
    abundance implied. Cadmium is represented by the ion descriptor; an empty metal
    enum list alongside SIGNIFICANT is explicitly explained by the vocabulary limitation.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - record
  - ontology
  - schema
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: SL8-SL12 cooperative cadmium immobilization'
  outcome: supported
  summary: This is a community phenotype, not a resolved directed interaction. Both
    listed strains are included by broad COMMUNITY_LEVEL scope. Experimental removal
    and material-characterization observations support the bounded summary. Possible
    EPS involvement and molecular causality remain uncertain. No obligate mutual benefit,
    exchanged substrate or gene-level cause is established.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - record
  - primary
  - phenotype
  - causality
  details: 'Participants: NCBITaxon:222 SL8 and NCBITaxon:547 SL12. Direction: none
    asserted. Mechanism: phenotype-level immobilization with observed partitioning/spectroscopy,
    not a causal molecular route. Context: source laboratory comparison; separate
    greenhouse outcomes. Exact field locator ecological_interactions[0]; PMID:42307251;
    source limitations quote in causality.'
- assessment_id: edges
  area: graph
  topic: ecological_interactions[0].downstream
  outcome: not_applicable
  summary: The whole target contains no downstream edges. Prior removal of dangling
    measured-outcome arrows is consistent with the current schema and does not leave
    a missing required causal graph.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - record
  - history
- assessment_id: phenotypes
  area: evidence
  topic: description and environmental_factors
  outcome: concern
  summary: Reported removal and greenhouse outcome claims are bounded to the studied
    contexts. Measured response values are mixed into environmental_factors, making
    experimental exposures and results difficult to distinguish in downstream queries.
    No field-scale efficacy or deployment recommendation is inferred.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - record
  - phenotype
- assessment_id: roles
  area: completeness
  topic: taxonomy[0..1].functional_role
  outcome: concern
  summary: Neither member has a functional_role entry. This affects the native completeness
    metric, but available enum choices must not force an unsupported donor/consumer
    or degradation relationship. The omission is a metadata gap, not a mandate to
    invent mechanism.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - record
  - schema
- assessment_id: resources
  area: provenance
  topic: associated_datasets and external_resources
  outcome: concern
  summary: Publication, GenBank, MetaboLights and supplemental metadata resolve. The
    sequence accession field combines two independent identifiers and should preserve
    independently resolvable entries. iProX remains unverified because its HTTP response
    is a generic shell. This is an access limitation, not evidence of a false citation.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - publication
  - genbank
  - metabolights
  - zenodo
  - iprox
  - record
- assessment_id: uncertainty
  area: evidence
  topic: discussions and prior evidence boundaries
  outcome: supported
  summary: The open causality gap accurately reflects the primary source limitation.
    Proposed genetic interventions are not assessed or refined by this review. Evidence
    matching is positive but does not establish that those proposed interventions
    are warranted.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - causality
  - snippets
  - history
- assessment_id: cultivation
  area: scope
  topic: engineering_design operational details and growth_media
  outcome: unknown
  summary: Parameter-level cultivation, selection and stress-tolerance methods, medium
    optimization/linking, and proposed genetic perturbations are outside this bounded
    review. No corrected operational details are supplied.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - record
- assessment_id: adapter
  area: evidence
  topic: Structured expression-source applicability
  outcome: not_applicable
  summary: No exact strain dataset in the inspected public catalog; absence is not
    evidence against the phenotype.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - adapter
- assessment_id: validation
  area: schema
  topic: Native gates and graph references
  outcome: supported
  summary: Focused gates pass; both defined members are credited by the unqualified
    community-level node. No downstream reference exists to dangle. These facts do
    not validate molecular causation or excluded operational details. Required corpus
    warning failures remain outside this target.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - record
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-references-explained
  - check-audit-network
- assessment_id: metrics
  area: completeness
  topic: Native presence and assessed-finding metrics
  outcome: concern
  summary: Completeness 40 reflects missing roles in the all-or-nothing required block
    and one node. Quality 100 is capped despite three minor findings and partial review;
    it is not approval of excluded or unverified claims.
  target_ids:
  - CommunityMech:000374
  evidence_ids:
  - record
  - schema
  metrics:
  - name: completeness
    value: 40
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 if required metadata including all taxon roles present
      +5 environment +10 at least 3 factors +10 at least 3 nodes +5 external resources
      +10 media +5 datasets +5 node metabolites). 0+5+10+0+5+10+5+5=40.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 'clamp(100-50*P1-10*P2-2*P3+20*min(mean node evidence/2,1)+15 if native
      network COMPLETE,0,100). Assessed P1=0,P2=0,P3=3; 3 evidence items/1 node; broad
      community scope credits both members. clamp(100-6+20+15)=100. Partial review:
      excluded claims are not certified.'
  - name: P1
    value: 0
    unit: findings
    definition: Observed findings within assessed scope; not a full protocol audit.
  - name: P2
    value: 0
    unit: findings
    definition: Observed findings within assessed scope; not a full protocol audit.
  - name: P3
    value: 3
    unit: findings
    definition: Observed findings within assessed scope; not a full protocol audit.
  - name: interaction_evidence
    value: 3
    unit: evidence items per interaction
    denominator: 1
    definition: Three attached entries, all from one primary study; not independent
      replication.
findings:
- finding_id: role-metadata
  issue_key: cm-000374-role-metadata
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: missing structured linkage or metabolite representation;
    prose retains the supported process.'
  rule_id: review-checklist.taxonomy
  status: open
  certainty: confirmed
  title: Taxon functional roles are unrepresented
  description: Both taxonomy members lack functional_role entries. The native completeness
    rubric requires roles for its metadata block, although the schema permits their
    absence. A role should not be forced from coculture membership alone.
  target_ids:
  - CommunityMech:000374
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  evidence_ids:
  - record
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
- finding_id: combined-accession
  issue_key: cm-000374-combined-accession
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: missing structured linkage or metabolite representation;
    prose retains the supported process.'
  rule_id: review-checklist.external-resources
  status: open
  certainty: confirmed
  title: Two independently resolvable sequence identifiers share one accession field
  description: associated_datasets[0].accession combines two GenBank accessions, obscuring
    individual identifier resolution and strain linkage. Both records independently
    resolve.
  target_ids:
  - CommunityMech:000374
  field_paths:
  - associated_datasets[0].accession
  evidence_ids:
  - genbank
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
- finding_id: outcome-factor
  issue_key: cm-000374-outcome-factor
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: missing structured linkage or metabolite representation;
    prose retains the supported process.'
  rule_id: review-checklist.environment
  status: open
  certainty: confirmed
  title: Measured outcomes are mixed with environmental exposures
  description: Several environmental_factors entries contain removal percentages or
    plant/soil response endpoints. The values are source-backed, but their placement
    mixes results with experimental environmental context.
  target_ids:
  - CommunityMech:000374
  field_paths:
  - environmental_factors[1]
  - environmental_factors[3]
  - environmental_factors[4]
  evidence_ids:
  - record
  - phenotype
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
actions:
- action_id: fix-role-metadata
  description: Clarify whether the existing vocabulary can express the already supported
    ecological role; otherwise preserve an explicit vocabulary gap.
  finding_ids:
  - role-metadata
  target_ids:
  - CommunityMech:000374
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Do not add inferred reciprocal benefit or exchange.
  - Any role annotation is evidence-backed and matches the schema definition.
  - Run strict and network validation after authorized metadata curation.
- action_id: fix-combined-accession
  description: Represent each accession distinctly while preserving the appropriate
    strain association and publication.
  finding_ids:
  - combined-accession
  target_ids:
  - CommunityMech:000374
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Each identifier resolves to its own metadata record.
  - Strain-to-accession correspondence remains unambiguous.
  - Run strict and resource-reference checks.
- action_id: fix-outcome-factor
  description: Distinguish measured responses from environmental inputs in supported
    metadata fields or retain an explicit schema gap.
  finding_ids:
  - outcome-factor
  target_ids:
  - CommunityMech:000374
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Do not silently change the numerical endpoint or comparison scope.
  - No new cultivation or intervention design is introduced.
  - Run strict and evidence checks.
limitations:
- 'Partial scope: cultivation/selection protocols, medium-linkage optimization and
  proposed genetic interventions were not assessed or refined.'
- iProX page returned a generic application shell; source advertises the accession,
  but study identity and availability remain unverified.
- MetaboLights and GenBank checks covered public metadata only; raw omics and sequence
  data were not reanalyzed. Zenodo check covered supplementary metadata, not its operational
  contents.
- Historical GTDB mapping aggregate counts were not reconstructed.
- Optional structured-source runner unavailable; public catalog has no exact strain
  dataset. Required corpus checks retain unrelated warning failures.
notes:
- No canonical record, cache, history or generated output changed.
- Every inspected input hash is unchanged; local supplemental cache was inventoried
  but not used to derive operational findings.
- Presence/quality metrics do not certify excluded content.
tags:
- record-review
- bounded-evidence-review
- batch-02
```
