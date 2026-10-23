# Bay Area sewage SARS-CoV-2 surveillance: record review

- Review: 20261021T103643Z-bay-area-sewage-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T10:30:09.499789Z
- Finished UTC: 2026-10-21T10:36:43.063695Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review finds one major issue (unsupported stable equilibrium) and two minor issues (sampling/sequence-comparison qualification and missing public resources). Preserve the three qualified surveillance nodes and zero arrows. Published S3 conflicts with universal exact-identity prose for two samples; broad regional concordance remains supported.

## Scope And Provenance

All record fields and three nodes assessed against fresh complete scientific main, all three main figures, bounded supplementary comparisons, ontology and current public metadata/provenance.

Selection: Next assigned maintained path after 000428 was saved and both mandatory post-save checks passed; only CommunityMech:000249 reviewed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000249 | kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml | maintained | San Francisco Bay Area Sewage SARS-CoV-2 Metagenomic Surveillance Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000249 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000249 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000249 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000249 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000249 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000249 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000249 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000249 | Target reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000249 | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; the target-native graph has no issue. |
| check-network-quality | failed | True | CommunityMech:000249 | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; the target-native graph has no issue. |
| Publication identity and scientific source assessment | passed | True | CommunityMech:000249 | Fresh main, all three figures and relevant supplemental comparisons support assessment of every current material assertion. |
| Project and repository identity | passed | True | CommunityMech:000249 | The paper-linked public project and immutable repository metadata/tree/README resolve with matching study scope. |
| Raw sequence and analysis reproduction | not_applicable | False | CommunityMech:000249 | No raw alignment, SNP-calling or notebook reproduction was needed or performed for this source-grounded record review. |
| Encoded medium/ingredient-Mech links | not_applicable | False | CommunityMech:000249 | No CultureMech or MediaIngredientMech identifier is encoded, and no cultivation medium is required by this surveillance study. |
| Optional structured source adapter | unavailable | False | CommunityMech:000249 | No runnable adapter was available in the owned task runtime. |

## Scientific And Domain Assessments

### Environmental viral population under surveillance

identity: supported. Targets: CommunityMech:000249.

The target is a defined surveillance population, with no claim to inventory the entire sewage community.

### Focal virus and environmental ontology

grounding: supported. Targets: CommunityMech:000249.

Retain the current viral identity and wastewater environment.

No reusable taxon, bacterial GTDB assignment, functional role or abundance label needs to be invented. Detection of plant viruses and bocaviruses by method-dependent panels does not require enlarging this focal SARS-CoV-2 record. OTHER category and NATURAL origin are compatible with the stated scope.

### Ecological equilibrium designation

evidence: concern. Targets: CommunityMech:000249.

The current STABLE value asserts an unsupported ecological property.

Neither repeated collections nor similar consensus sequences establish stable community equilibrium. The source assesses surveillance performance and variation, not an ecological stability endpoint; this is absence of support, not proof of instability.

### ecological_interactions[0]: Wastewater Minor SARS-CoV-2 Allele Profiling

graph: supported. Targets: CommunityMech:000249.

Retain the qualified community-level observation of sub-consensus alleles.

The participant is the sampled wastewater SARS-CoV-2 population. Computational calling identifies variation within mapped RNA reads, with some pair/triplet frequency concordance supporting linkage. This has no taxon-to-taxon causal direction and does not resolve every strain haplotype or demonstrate infectivity.

### ecological_interactions[1]: Regional Clinical Genotype Concordance

graph: concern. Targets: CommunityMech:000249.

Preserve broad sequence concordance while qualifying exact identity against the published comparison table.

The comparison is between wastewater consensus sequences and available regional clinical genomes, not transmission between named hosts. The main text claims universal exact matches, whereas two of seven S3 sample groups have minimum SNP distance one. Specify compared nongap/non-N positions and the clinical snapshot; retain the discrepancy rather than presenting all seven as identical or discarding regional concordance.

### ecological_interactions[2]: Preclinical Local Lineage-Introduction Signal

graph: supported. Targets: CommunityMech:000249.

Retain PARTIAL support and the current sampling-sensitive interpretation.

Recurrent wastewater variants absent from the available California clinical set but detected elsewhere support possible introductions. Absence from that clinical sample is not absence from California; the observation establishes neither a transmission event nor a precise introduction date. Figure 3 contains earlier outside-California points than the Results July-only narrative, so that unencoded date claim should not be imported. No downstream arrows are encoded or warranted by the analytical workflow.

### Sampling and measurement provenance

completeness: concern. Targets: CommunityMech:000249.

Recover bounded sample-processing context without adding cultivation or silently reconciling source counts.

The record currently names only the region. Methods supply interceptor and composite-sampling context, while respiratory-virus capture and extraction shape detection. S1 contains 27 processing/library rows dated 13 May–1 July; the main Results says 19 May–15 July and uses a 22-sample denominator. Preserve those source boundaries rather than converting table rows into independent biological samples or asserting an exact reconciled interval.

### Public sequencing and analysis resources

completeness: concern. Targets: CommunityMech:000249.

The empty dataset list and publication-only links omit recoverable source resources.

Add the verified study project and source-linked analysis repository with their appropriate data/code scope. Public metadata and an immutable README/tree establish availability, not a complete run inventory, reproducibility result or confirmation of clinical coverage.

### Evidence placement, cultivation and metal relevance

schema: supported. Targets: CommunityMech:000249.

The remaining fields are compatible with the defined environmental surveillance scope.

The field-study IN_VIVO evidence enum is allowed, while computational node evidence is appropriately scoped. Empty growth_media, metal lists and NOT_APPLICABLE metal relevance do not require invented media or metal-processing roles. There are no encoded CultureMech/MediaIngredientMech links. Current exact snippets are authentic even where broader source interpretation requires qualification.

### Cache boundaries and prior graph repairs

evidence: supported. Targets: CommunityMech:000249.

Preserve the prior workflow-edge removals and uncertainty discussion.

The TXT cache is abstract-level; the MD header says abstract_only despite appended main text and captions. Fresh XML independently verifies the source. Earlier history certifies a bounded graph repair, not the current ecological-state or resource completeness. No cache or append-only history is altered by this review.

### Native validity and scientific qualification

schema: supported. Targets: CommunityMech:000249.

Eight native checks pass; the findings concern state attribution and source/resource completeness.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000249.

Native scores do not certify equilibrium, exact haplotypes or transmission.

## Findings

### unsupported-stability: Remove or substantiate the stable-equilibrium designation

major / open / confirmed; issue key: cm-000249-unsupported-stability.

STABLE asserts stable ecological equilibrium without a corresponding source measurement or inference; surveillance success and genotype similarity do not support that property.

### sampling-measurement-scope: Qualify exact sequence identity and add bounded sampling context

minor / open / confirmed; issue key: cm-000249-sampling-measurement-scope.

The unqualified identical-genotype summary omits a main/S3 conflict, and sparse context obscures the comparison and analytical sampling boundaries.

### missing-public-resources: Link the verified sequencing project and analysis repository

minor / open / confirmed; issue key: cm-000249-missing-public-resources.

The source explicitly provides a public sequencing project and processed-data/code repository, but the record links only the publication and DOI.

## Recommended Actions And Acceptance Checks

### repair-unsupported-stability

Remove or substantiate the stable-equilibrium designation.

- Remove the optional STABLE value or provide specific evidence of equilibrium under the schema definition.
- Do not automatically replace it with TRANSIENT, infer instability from variation alone, or treat repeated sampling as evidence of equilibrium.

### repair-sampling-measurement-scope

Qualify exact sequence identity and add bounded sampling context.

- Retain broad regional concordance, but state that main universal identity wording conflicts with S3 minimum-one-SNP groups 5_28_S and 6_30_S_COL; five other groups include zero-distance California hits.
- State that comparisons exclude gaps/N positions and use the available clinical snapshot; do not infer specific transmission or complete local infection coverage.
- Add the four-interceptor, 24-hour composite sampling and capture-enrichment context with direct source evidence, keeping these separate from cultivation.
- Preserve the main/S1 date and sample-denominator differences rather than silently reconciling them; do not add the conflicting July-only emergence claim.

### repair-missing-public-resources

Link the verified sequencing project and analysis repository.

- Add PRJNA661613 with the source-supported enriched wastewater RNA scope and claim-level Data availability evidence.
- Add the paper-linked analysis repository and record immutable commit 0104c8431936374caaba5c93e809968d3496ed92 as inspected provenance, keeping data availability separate from successful reproduction.
- Do not invent sample/run counts, certify uninspected sequence or notebook contents, or treat the metadata-linked PRJEB40770 as independently verified.

### preserve-surveillance-graph

Preserve the three bounded surveillance observations and zero causal arrows during separately authorized curation.

- Do not restore sequencing/analysis workflow arrows or infer viral replication, infectivity, complete haplotypes, transmission or ecological interactions from these observations.
- Retain the PARTIAL introduction inference, broad clinical concordance and current uncertainty discussion with corrected source qualification.
- After authorized curation, preserve append-only history and rerun schema, strict, term, history, reference and target/corpus network checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml; Whole record: one focal viral population, three community-level nodes and zero arrows | supports | The record concerns environmental SARS-CoV-2 sequence surveillance, not the complete sewage microbiome or a cultured consortium. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=33468686&amp;retmode=xml; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=33468686&amp;retmode=xml | supports | PubMed verifies PMID:33468686, DOI:10.1128/mBio.02703-20, title and abstract. |
| crossref | https://api.crossref.org/works/10.1128/mBio.02703-20; https://api.crossref.org/works/10.1128/mBio.02703-20 | supports | Crossref verifies DOI/title metadata and the publisher route. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:33468686&amp;format=json&amp;resultType=core; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:33468686&amp;format=json&amp;resultType=core | supports | Europe PMC verifies article metadata and provides the full scientific XML for PMC7845645. |
| sampling | PMID:33468686; Full XML s3.1 and s3.3; Figure 1; Supplementary Tables S1/S2 | supports | Four Bay Area interceptors were sampled using 24-hour one-liter composites; extraction and respiratory-virus capture enrichment affect detection. These are sampling/analytical procedures, not cultivation. |
| minor-alleles | PMID:33468686; Abstract; full XML s2.3 and s3.5; Figures 2 and 3a/b | supports | Computational SNV calling identifies sub-consensus variation; co-varying frequencies support linkage for particular pairs/triplets, not universal complete haplotypes or infectious particles. |
| concordance | PMID:33468686; Full XML s2.2 and s3.5; Supplementary Table S3 | partial | The main text reports exact consensus matches at compared positions; the published comparison table requires qualification. Clinical alignments were downloaded on 23 August 2020, and comparisons exclude gaps and N positions. |
| consensus-table | PMID:33468686; Supplementary Table S3: all 1349 rows grouped by seven samples; supplement-focused-audit.json | partial | Five sample groups include zero-distance California hits; 5_28_S has eight rows all at distance one and 6_30_S_COL has 259 rows all at distance one. This conflicts with universal identity prose while retaining close regional concordance. |
| introduction | PMID:33468686; Full XML s2.4; Figure 3; Supplementary Table S4 focal loci | partial | Four recurrent variants absent from the available California clinical comparison but present elsewhere support the authors’ possible-introduction interpretation; incomplete clinical sampling prevents a confirmed or precisely dated introduction claim. |
| supplement-context | PMID:33468686; S1 all rows; S2 nineteen SARS-CoV-2 rows; S3 grouped comparisons; S4 ten focal-locus rows | supports | The tables distinguish library/extraction rows, genome breadth and consensus comparisons. S1 dates and row counts differ from the main narrative and cannot be silently treated as a corrected set of independent biological samples. |
| availability | PMID:33468686; Full XML s3.6 Data availability | supports | The publication explicitly names PRJNA661613 and the alexcritschristoph/wastewater_sarscov2 analysis repository. |
| archives | PRJNA661613 and https://github.com/alexcritschristoph/wastewater_sarscov2; dataset-verification.json: project metadata and immutable commit/tree/README | supports | The public project matches enriched Bay Area sewage RNA. Repository commit 0104c8431936374caaba5c93e809968d3496ed92 and README are verified; notebooks, clinical tables and sequence files were not analyzed or executed. |
| ontology | Local OAK NCBITaxon and ENVO snapshots; ontology-authority.json and viral-taxonomy-scope.json | supports | Both encoded ID/label pairs match. NCBITaxon:2697049 identifies SARS-CoV-2; its species-ranked parent does not justify replacing the encoded taxon or assuming that its own rank is species. Viral NO_GTDB_EQUIVALENT is appropriate. |
| viral-rank | NCBITaxon:2697049; viral-taxonomy-scope.json: label, parent and lineage | context_only | The local authority provides no explicit rank for the encoded virus taxon; parent NCBITaxon:3418604 is species-ranked Betacoronavirus pandemicum. |
| schema | src/communitymech/schema/communitymech.yaml; EcologicalStateEnum.STABLE; EvidenceSourceEnum.IN_VIVO; community-level interaction and taxonomy slots | supports | STABLE asserts stable equilibrium, which sequencing success and repeat sampling do not establish. IN_VIVO explicitly permits field studies; absent optional functional roles are not schema failures. |
| snippets | kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml; snippet-audit.json: six occurrence comparisons | supports | All six snippets match the cache and fresh XML; five also match the fresh abstract and the publication title is verified metadata. Exact wording does not resolve the main/S3 scientific discrepancy. |
| history | Two target history sidecars and exact batch7 decision; provenance-audit.json: prior target hash and current issue states | supports | Closed issue 1260 concerns preserved graph-scope repairs. Issue 1262 is open but its current body does not name this target; it is not claimed as an unresolved target-specific defect. |
| search | Owned maintained community, isolate and reusable-taxon roots; local-search.json: recorded ignored-inclusive searches | supports | No reusable target record was established within the bounded search scope; no global absence claim is made. |
| adapter | Optional structured source adapter; adapter-check.json: owned batch 06 runtime availability | supports | No runnable structured adapter was available; no external-checkout runner or paid provider was invoked. |
| native-target | NetworkIntegrityAuditor().audit_community(target); support-audit.json: target network, evidence counts and native metric components | supports | The three-node, zero-arrow graph is natively COMPLETE with no issues; absence of an optional viral functional role lowers completeness without requiring an invented role. |
| source-scope | PMID:33468686; source-audit.json: main, figures, supplements and explicit uninspected scope | context_only | The whole scientific main and all three figure pixels were read; supplements were inspected to the stated sample/table scope without raw sequence or alignment reanalysis. |
| independent-source | PMID:33468686; root-independent-source-audit.json: independent main, figure and supplement assessment | context_only | Independent source review supports the same three bounded findings and preservation of the qualified surveillance graph. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml; Actual execution 2026-10-21T10:30:40.597486+00:00 to 2026-10-21T10:30:41.422799+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-strict kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml --out /private/tmp/cm-review-session/batch-06/000249/strict-report.tsv; Actual execution 2026-10-21T10:30:40.597746+00:00 to 2026-10-21T10:30:42.874721+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-terms kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml; Actual execution 2026-10-21T10:30:40.597827+00:00 to 2026-10-21T10:30:42.444037+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-gtdb kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml; Actual execution 2026-10-21T10:30:41.423177+00:00 to 2026-10-21T10:30:41.493386+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-gtdb-domain kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml; Actual execution 2026-10-21T10:30:41.493643+00:00 to 2026-10-21T10:30:42.940998+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-history history/records/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community; Actual execution 2026-10-21T10:30:42.444290+00:00 to 2026-10-21T10:30:43.189044+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T10:30:43.190083+00:00 to 2026-10-21T10:30:43.246691+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-references-explained kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml; Actual execution 2026-10-21T10:30:43.246934+00:00 to 2026-10-21T10:30:44.248817+00:00 | supports | Target reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T10:06:35.990708+00:00 to 2026-10-21T10:06:41.713287+00:00 | supports | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; the target-native graph has no issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T10:06:35.990845+00:00 to 2026-10-21T10:06:41.708376+00:00 | supports | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; the target-native graph has no issue. |

## Limits And Additional Notes

- Whole scientific main and all three main figure pixels were inspected. S1 was read completely; S2 inspection covered all nineteen SARS-CoV-2 rows and selected measurement columns, not all other viruses; S3 comparisons were grouped across all 1349 rows with both one-distance groups checked; S4 review covered the four recurrent focal loci and representative rows.
- No raw reads, clinical sequence tables, consensus FASTA, alignment, variant calling, deposited notebooks or statistical pipeline was reanalyzed. Published table inspection is not independent sequence reproduction.
- Main and supplements disagree on universal exact identity, sample dates/count boundaries and July-only emergence. These discrepancies are retained rather than reconciled by assumption; the current node does not encode the conflicting emergence date.
- Public archive review covered project metadata and immutable repository metadata/tree/README only. No full run inventory or linked PRJEB40770 content was verified.
- ASM access returned 403 and the PMC browser response was a CAPTCHA; complete source assessment instead used successfully retrieved Europe PMC XML and supplements plus primary figure assets.
- The MD cache frontmatter is stale relative to its appended main text; both cache files were preserved unchanged. Corpus warning counts are distinct from the clean target-native graph.
- No canonical, cache, history or generated file was changed.
- All 25 repository inputs were pinned before assessment and rechecked.
- Quoted primary-source text totals 11 words across the publication, including all main/supplement evidence.
- Native quality 100 is capped from 111; absent optional roles and inapplicable cultivation are not invented to raise completeness.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103643Z-bay-area-sewage-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Bay Area sewage SARS-CoV-2 surveillance: record review'
started_at: '2026-10-21T10:30:09.499789Z'
finished_at: '2026-10-21T10:36:43.063695Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed source science/figures, ontology/native
    checks and supporting provenance/resource metadata; canonical inputs remain unchanged.
    No person-level independence is asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole-record review finds one major issue (unsupported stable equilibrium)
  and two minor issues (sampling/sequence-comparison qualification and missing public
  resources). Preserve the three qualified surveillance nodes and zero arrows. Published
  S3 conflicts with universal exact-identity prose for two samples; broad regional
  concordance remains supported.
source:
  git_revision: 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b
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
  - path: history/records/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community/2026-10-02T050543Z-codex-0b4c31.yaml
    sha256: 1e1e4d51f103296fbf6b64a60cbd8da1d1a89abb45c91acce307fc1a36f1c0ad
    role: context
  - path: history/records/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community/2026-10-05T124957Z-codex-fb11a1.yaml
    sha256: 31006bfa24ba00a49ec2087533ed19043a829f6b8b9e29ec154ef870502f8593
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    sha256: dd723b34a92aff159763e8ccfe3955ba829551f50127dc24130fc9e346c69c17
    role: target
  - path: references_cache/PMID_33468686.md
    sha256: 19369b4f9c4f4cf062b68d928f8fa556b162696aa13cbd0d68d952f464aea69d
    role: context
  - path: references_cache/PMID_33468686.txt
    sha256: eba75dd3b4f49429cb90667706c6f234bc274194457dfc3a89fe97092d6a27e6
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch7.yaml
    sha256: c96f00489d2ad14f63cd035adc778adbf72d7fe6a11c2dffd81cd1a904cc0a75
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
- target_id: CommunityMech:000249
  path: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  label: San Francisco Bay Area Sewage SARS-CoV-2 Metagenomic Surveillance Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    role: canonical_record
scope:
  description: All record fields and three nodes assessed against fresh complete scientific
    main, all three main figures, bounded supplementary comparisons, ontology and
    current public metadata/provenance.
  selection: Next assigned maintained path after 000428 was saved and both mandatory
    post-save checks passed; only CommunityMech:000249 reviewed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000249
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000249
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    source science assessed separately.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000249
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-strict kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    --out /private/tmp/cm-review-session/batch-06/000249/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    source science assessed separately.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000249
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-terms kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    source science assessed separately.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000249
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    source science assessed separately.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000249
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    source science assessed separately.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000249
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-history history/records/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    source science assessed separately.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000249
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    source science assessed separately.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000249
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-references-explained kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    source science assessed separately.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; the target-native graph has no issue.
  target_ids:
  - CommunityMech:000249
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Reused fresh full-corpus batch 06 execution, not a target-specific pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; the target-native graph has no issue.
  target_ids:
  - CommunityMech:000249
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Reused fresh full-corpus batch 06 execution, not a target-specific pass.
- check_id: publication-and-source
  name: Publication identity and scientific source assessment
  status: passed
  required: true
  summary: Fresh main, all three figures and relevant supplemental comparisons support
    assessment of every current material assertion.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - source-scope
  - independent-source
- check_id: public-resource-identity
  name: Project and repository identity
  status: passed
  required: true
  summary: The paper-linked public project and immutable repository metadata/tree/README
    resolve with matching study scope.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - availability
  - archives
- check_id: raw-reanalysis
  name: Raw sequence and analysis reproduction
  status: not_applicable
  required: false
  summary: No raw alignment, SNP-calling or notebook reproduction was needed or performed
    for this source-grounded record review.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - source-scope
  - archives
- check_id: cross-mech
  name: Encoded medium/ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech identifier is encoded, and no cultivation
    medium is required by this surveillance study.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - record
  - sampling
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No runnable adapter was available in the owned task runtime.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  locator: 'Whole record: one focal viral population, three community-level nodes
    and zero arrows'
  summary: The record concerns environmental SARS-CoV-2 sequence surveillance, not
    the complete sewage microbiome or a cultured consortium.
  support: supports
  accessed_at: '2026-10-21T10:36:43.060194Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=33468686&retmode=xml
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=33468686&retmode=xml
  summary: PubMed verifies PMID:33468686, DOI:10.1128/mBio.02703-20, title and abstract.
  support: supports
  accessed_at: '2026-10-21T10:30:26.810268Z'
  snapshot_sha256: 4d62e0a2218ffcf9fc54e62b95ec8bef5d0f89613d7ae2d022b8406e6e6e155c
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1128/mBio.02703-20
  locator: https://api.crossref.org/works/10.1128/mBio.02703-20
  summary: Crossref verifies DOI/title metadata and the publisher route.
  support: supports
  accessed_at: '2026-10-21T10:30:26.766077Z'
  snapshot_sha256: d27200af4d177ebe46597192b12b9365ba93c9d2e4d0c7cac3ed47aa307a6031
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:33468686&format=json&resultType=core
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:33468686&format=json&resultType=core
  summary: Europe PMC verifies article metadata and provides the full scientific XML
    for PMC7845645.
  support: supports
  accessed_at: '2026-10-21T10:30:27.173950Z'
  snapshot_sha256: 7c4a40ebdb674dbc453438a46ee051724f050d10878b93c8ed46e3b59a4bf26e
- evidence_id: sampling
  kind: primary_source
  reference: PMID:33468686
  locator: Full XML s3.1 and s3.3; Figure 1; Supplementary Tables S1/S2
  summary: Four Bay Area interceptors were sampled using 24-hour one-liter composites;
    extraction and respiratory-virus capture enrichment affect detection. These are
    sampling/analytical procedures, not cultivation.
  support: supports
  accessed_at: '2026-10-21T10:36:43.060396Z'
  quote: Twenty-four-hour 1-liter composite samples
  snapshot_sha256: a39a8d6d05cacb818271a1c52f84f7e96ff482c55011f22c110b4b24570af317
- evidence_id: minor-alleles
  kind: primary_source
  reference: PMID:33468686
  locator: Abstract; full XML s2.3 and s3.5; Figures 2 and 3a/b
  summary: Computational SNV calling identifies sub-consensus variation; co-varying
    frequencies support linkage for particular pairs/triplets, not universal complete
    haplotypes or infectious particles.
  support: supports
  accessed_at: '2026-10-21T10:36:43.060398Z'
  quote: minor SARS-CoV-2 alleles
  snapshot_sha256: a39a8d6d05cacb818271a1c52f84f7e96ff482c55011f22c110b4b24570af317
- evidence_id: concordance
  kind: primary_source
  reference: PMID:33468686
  locator: Full XML s2.2 and s3.5; Supplementary Table S3
  summary: The main text reports exact consensus matches at compared positions; the
    published comparison table requires qualification. Clinical alignments were downloaded
    on 23 August 2020, and comparisons exclude gaps and N positions.
  support: partial
  accessed_at: '2026-10-21T10:36:43.060399Z'
  quote: nongapped positions
  snapshot_sha256: a39a8d6d05cacb818271a1c52f84f7e96ff482c55011f22c110b4b24570af317
- evidence_id: consensus-table
  kind: primary_source
  reference: PMID:33468686
  locator: 'Supplementary Table S3: all 1349 rows grouped by seven samples; supplement-focused-audit.json'
  summary: Five sample groups include zero-distance California hits; 5_28_S has eight
    rows all at distance one and 6_30_S_COL has 259 rows all at distance one. This
    conflicts with universal identity prose while retaining close regional concordance.
  support: partial
  accessed_at: '2026-10-21T10:36:43.060443Z'
  snapshot_sha256: 5a4001540ceb5ee3581c0baa493c2c8e964ecc10e5a8da252530504eb0b3aaca
- evidence_id: introduction
  kind: primary_source
  reference: PMID:33468686
  locator: Full XML s2.4; Figure 3; Supplementary Table S4 focal loci
  summary: Four recurrent variants absent from the available California clinical comparison
    but present elsewhere support the authors’ possible-introduction interpretation;
    incomplete clinical sampling prevents a confirmed or precisely dated introduction
    claim.
  support: partial
  accessed_at: '2026-10-21T10:36:43.060445Z'
  quote: recent introductions
  snapshot_sha256: a39a8d6d05cacb818271a1c52f84f7e96ff482c55011f22c110b4b24570af317
- evidence_id: supplement-context
  kind: primary_source
  reference: PMID:33468686
  locator: S1 all rows; S2 nineteen SARS-CoV-2 rows; S3 grouped comparisons; S4 ten
    focal-locus rows
  summary: The tables distinguish library/extraction rows, genome breadth and consensus
    comparisons. S1 dates and row counts differ from the main narrative and cannot
    be silently treated as a corrected set of independent biological samples.
  support: supports
  accessed_at: '2026-10-21T10:36:43.060484Z'
  snapshot_sha256: b6665aa68b14bf85cf2f62d46622b06079fa5b52baea72ddedf9769258a651ee
- evidence_id: availability
  kind: primary_source
  reference: PMID:33468686
  locator: Full XML s3.6 Data availability
  summary: The publication explicitly names PRJNA661613 and the alexcritschristoph/wastewater_sarscov2
    analysis repository.
  support: supports
  accessed_at: '2026-10-21T10:36:43.060486Z'
  snapshot_sha256: a39a8d6d05cacb818271a1c52f84f7e96ff482c55011f22c110b4b24570af317
- evidence_id: archives
  kind: database
  reference: PRJNA661613 and https://github.com/alexcritschristoph/wastewater_sarscov2
  locator: 'dataset-verification.json: project metadata and immutable commit/tree/README'
  summary: The public project matches enriched Bay Area sewage RNA. Repository commit
    0104c8431936374caaba5c93e809968d3496ed92 and README are verified; notebooks, clinical
    tables and sequence files were not analyzed or executed.
  support: supports
  accessed_at: '2026-10-21T10:36:43.060517Z'
  snapshot_sha256: 18b16c70666cdce76b808f39f91ec0e8c98adc01b8863ed76fbffb1ffe1d95a5
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon and ENVO snapshots
  locator: ontology-authority.json and viral-taxonomy-scope.json
  summary: Both encoded ID/label pairs match. NCBITaxon:2697049 identifies SARS-CoV-2;
    its species-ranked parent does not justify replacing the encoded taxon or assuming
    that its own rank is species. Viral NO_GTDB_EQUIVALENT is appropriate.
  support: supports
  accessed_at: '2026-10-21T10:36:43.060549Z'
  snapshot_sha256: 5ebbc343ceea03b3561470eac5c83687f2261db8752696c9273469deec5081ed
- evidence_id: viral-rank
  kind: authority
  reference: NCBITaxon:2697049
  locator: 'viral-taxonomy-scope.json: label, parent and lineage'
  summary: The local authority provides no explicit rank for the encoded virus taxon;
    parent NCBITaxon:3418604 is species-ranked Betacoronavirus pandemicum.
  support: context_only
  accessed_at: '2026-10-21T10:36:43.060579Z'
  snapshot_sha256: a20d676b316e6be0cd62587f7233a825ea1d3a611965cbeceb9dd2e41e8bdd8f
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: EcologicalStateEnum.STABLE; EvidenceSourceEnum.IN_VIVO; community-level
    interaction and taxonomy slots
  summary: STABLE asserts stable equilibrium, which sequencing success and repeat
    sampling do not establish. IN_VIVO explicitly permits field studies; absent optional
    functional roles are not schema failures.
  support: supports
  accessed_at: '2026-10-21T10:36:43.060580Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  locator: 'snippet-audit.json: six occurrence comparisons'
  summary: All six snippets match the cache and fresh XML; five also match the fresh
    abstract and the publication title is verified metadata. Exact wording does not
    resolve the main/S3 scientific discrepancy.
  support: supports
  accessed_at: '2026-10-21T10:36:43.060609Z'
  snapshot_sha256: cfd5459b270baa842f605292b3c8bd042652ac826ea460e7a23abab89b3d064c
- evidence_id: history
  kind: record_content
  reference: Two target history sidecars and exact batch7 decision
  locator: 'provenance-audit.json: prior target hash and current issue states'
  summary: Closed issue 1260 concerns preserved graph-scope repairs. Issue 1262 is
    open but its current body does not name this target; it is not claimed as an unresolved
    target-specific defect.
  support: supports
  accessed_at: '2026-10-21T10:36:43.062397Z'
  snapshot_sha256: fc5498cefcb054416651ab9ed1ddea50e60eb31fcaeb14edbdccddc7c88e3339
- evidence_id: search
  kind: search
  reference: Owned maintained community, isolate and reusable-taxon roots
  locator: 'local-search.json: recorded ignored-inclusive searches'
  summary: No reusable target record was established within the bounded search scope;
    no global absence claim is made.
  support: supports
  accessed_at: '2026-10-21T10:36:43.062511Z'
  snapshot_sha256: 1a9397961060fb17b40b56e96b6467c74c62a950d0c2435ba5328167f479abff
  search_scope: Recorded rg --no-ignore --hidden searches in the owned maintained
    roots and bounded mapping discovery.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: 'adapter-check.json: owned batch 06 runtime availability'
  summary: No runnable structured adapter was available; no external-checkout runner
    or paid provider was invoked.
  support: supports
  accessed_at: '2026-10-21T10:36:43.062557Z'
  snapshot_sha256: 7aa4f714e88b8ccc2f0a81fa690811de2ff26f5de0b44a6826f50420e77e7a95
  search_scope: Fresh batch 06 PATH, owned venv/module and ignored-inclusive worktree
    discovery, reused with provenance.
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: 'support-audit.json: target network, evidence counts and native metric
    components'
  summary: The three-node, zero-arrow graph is natively COMPLETE with no issues; absence
    of an optional viral functional role lowers completeness without requiring an
    invented role.
  support: supports
  accessed_at: '2026-10-21T10:36:43.062624Z'
  snapshot_sha256: b65d97c0d2f2065f916c9b10d617cec96d4c6bd531e7a7441fa83a95f0d2162f
- evidence_id: source-scope
  kind: validation
  reference: PMID:33468686
  locator: 'source-audit.json: main, figures, supplements and explicit uninspected
    scope'
  summary: The whole scientific main and all three figure pixels were read; supplements
    were inspected to the stated sample/table scope without raw sequence or alignment
    reanalysis.
  support: context_only
  accessed_at: '2026-10-21T10:36:43.062665Z'
  snapshot_sha256: ecb8a1888d74837cf73c26fcc5639e66a1ffc891895fb491209b60edd3bdda2d
- evidence_id: independent-source
  kind: validation
  reference: PMID:33468686
  locator: 'root-independent-source-audit.json: independent main, figure and supplement
    assessment'
  summary: Independent source review supports the same three bounded findings and
    preservation of the qualified surveillance graph.
  support: context_only
  accessed_at: '2026-10-21T10:36:43.062703Z'
  snapshot_sha256: ffcc9f22e76bdc74b14b135d95e173e1885b28a50889ce306b30fd855fd9bc79
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  locator: Actual execution 2026-10-21T10:30:40.597486+00:00 to 2026-10-21T10:30:41.422799+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T10:30:41.422799Z'
  snapshot_sha256: b9f650f88309c8e07161e838f8d9ca568bdffc4173bfb797ccc02915dbd1e7de
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-strict kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    --out /private/tmp/cm-review-session/batch-06/000249/strict-report.tsv
  locator: Actual execution 2026-10-21T10:30:40.597746+00:00 to 2026-10-21T10:30:42.874721+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T10:30:42.874721Z'
  snapshot_sha256: ffffb9d73130ce115dc1168aea52d9863a2e3750c1adb8d412e66294913baa1d
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-terms kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  locator: Actual execution 2026-10-21T10:30:40.597827+00:00 to 2026-10-21T10:30:42.444037+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T10:30:42.444037Z'
  snapshot_sha256: 647b209f594e70a19b8b56e2276585907413a95fc3ddf4fc2daf4c3501ce4aa2
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  locator: Actual execution 2026-10-21T10:30:41.423177+00:00 to 2026-10-21T10:30:41.493386+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T10:30:41.493386Z'
  snapshot_sha256: 24f0be203ded8f91a3e26758a8cf0ae21954c16c9458c2b5c674fca22fdd0310
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  locator: Actual execution 2026-10-21T10:30:41.493643+00:00 to 2026-10-21T10:30:42.940998+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T10:30:42.940998Z'
  snapshot_sha256: c7d5332462be73f810e7e7befca08ff5dee308ef82e4a0428a219b0c8b363a7d
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-history history/records/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community
  locator: Actual execution 2026-10-21T10:30:42.444290+00:00 to 2026-10-21T10:30:43.189044+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T10:30:43.189044Z'
  snapshot_sha256: 695614d166c215e6d27a0f9cd150f99c694cf83cf22c3e7287045c17880ce8fb
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T10:30:43.190083+00:00 to 2026-10-21T10:30:43.246691+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T10:30:43.246691Z'
  snapshot_sha256: f37f5bbf038931ba7b62ecb00b12575affb48a443edef379ea6a8affcbf83c8c
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-references-explained kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
  locator: Actual execution 2026-10-21T10:30:43.246934+00:00 to 2026-10-21T10:30:44.248817+00:00
  summary: Target reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T10:30:44.248817Z'
  snapshot_sha256: d90564e0511697bffaf65a52c06c56b4c59de33907e3cd9a74c9e6337e6eb0ae
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T10:06:35.990708+00:00 to 2026-10-21T10:06:41.713287+00:00
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; the target-native graph has no issue.
  support: supports
  accessed_at: '2026-10-21T10:06:41.713287Z'
  snapshot_sha256: 330e4d9c9367a126afe7da9d93d310348e0ba6cc1289d806f4ff8df350be9620
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T10:06:35.990845+00:00 to 2026-10-21T10:06:41.708376+00:00
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; the target-native graph has no issue.
  support: supports
  accessed_at: '2026-10-21T10:06:41.708376Z'
  snapshot_sha256: 0420f90879ef008b71c8bfcfe444d05d2c030519aca57834b4e2587766c5b854
assessments:
- assessment_id: identity
  area: identity
  topic: Environmental viral population under surveillance
  outcome: supported
  summary: The target is a defined surveillance population, with no claim to inventory
    the entire sewage community.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - record
  - sampling
  - ontology
  dimensions:
  - name: community_scope
    value: SARS-CoV-2 RNA population sampled from Bay Area municipal sewage
    definition: Other detected viruses and organisms are outside the focal target;
      clinical comparators are separate sampled populations.
    evidence_ids:
    - record
    - sampling
  - name: source_strain
    value: Mixed viral population and sample consensus sequences
    definition: No cultured strain, fully resolved set of haplotypes, viability or
      infectious isolate is established.
    evidence_ids:
    - minor-alleles
    - concordance
  - name: environment
    value: Municipal wastewater from four Bay Area interceptors
    definition: The four source labels are Berkeley, Berkeley Hills, Oakland and Marin;
      natural environmental origin is compatible with engineered sewer infrastructure.
    evidence_ids:
    - sampling
    - ontology
  - name: medium
    value: No cultivation medium
    definition: Extraction, heat inactivation, capture enrichment and sequencing are
      analytical operations, not growth conditions.
    evidence_ids:
    - sampling
  - name: experimental_setting
    value: Environmental sequencing with clinical-genome comparison
    definition: Sampling/library processing and a dated clinical comparison snapshot
      constrain detection and inferred geographic concordance.
    evidence_ids:
    - sampling
    - concordance
    - supplement-context
  - name: evidence_tier
    value: Computational sequence observation and qualified epidemiological inference
    definition: No ecological causal interaction, sewage replication, transmission
      event or stable equilibrium follows from these measurements.
    evidence_ids:
    - minor-alleles
    - introduction
    - schema
  - name: grounding_status
    value: Two valid encoded ontology pairs; no GTDB equivalent for the virus
    definition: Ontology identity is verified without assuming species rank or replacing
      the virus with its parent taxon.
    evidence_ids:
    - ontology
    - viral-rank
- assessment_id: taxonomy
  area: grounding
  topic: Focal virus and environmental ontology
  outcome: supported
  summary: Retain the current viral identity and wastewater environment.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - ontology
  - viral-rank
  - sampling
  details: No reusable taxon, bacterial GTDB assignment, functional role or abundance
    label needs to be invented. Detection of plant viruses and bocaviruses by method-dependent
    panels does not require enlarging this focal SARS-CoV-2 record. OTHER category
    and NATURAL origin are compatible with the stated scope.
- assessment_id: state
  area: evidence
  topic: Ecological equilibrium designation
  outcome: concern
  summary: The current STABLE value asserts an unsupported ecological property.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - schema
  - sampling
  - minor-alleles
  - concordance
  details: Neither repeated collections nor similar consensus sequences establish
    stable community equilibrium. The source assesses surveillance performance and
    variation, not an ecological stability endpoint; this is absence of support, not
    proof of instability.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Wastewater Minor SARS-CoV-2 Allele Profiling'
  outcome: supported
  summary: Retain the qualified community-level observation of sub-consensus alleles.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - minor-alleles
  - supplement-context
  details: The participant is the sampled wastewater SARS-CoV-2 population. Computational
    calling identifies variation within mapped RNA reads, with some pair/triplet frequency
    concordance supporting linkage. This has no taxon-to-taxon causal direction and
    does not resolve every strain haplotype or demonstrate infectivity.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Regional Clinical Genotype Concordance'
  outcome: concern
  summary: Preserve broad sequence concordance while qualifying exact identity against
    the published comparison table.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - concordance
  - consensus-table
  details: The comparison is between wastewater consensus sequences and available
    regional clinical genomes, not transmission between named hosts. The main text
    claims universal exact matches, whereas two of seven S3 sample groups have minimum
    SNP distance one. Specify compared nongap/non-N positions and the clinical snapshot;
    retain the discrepancy rather than presenting all seven as identical or discarding
    regional concordance.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Preclinical Local Lineage-Introduction Signal'
  outcome: supported
  summary: Retain PARTIAL support and the current sampling-sensitive interpretation.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - introduction
  - supplement-context
  details: Recurrent wastewater variants absent from the available California clinical
    set but detected elsewhere support possible introductions. Absence from that clinical
    sample is not absence from California; the observation establishes neither a transmission
    event nor a precise introduction date. Figure 3 contains earlier outside-California
    points than the Results July-only narrative, so that unencoded date claim should
    not be imported. No downstream arrows are encoded or warranted by the analytical
    workflow.
- assessment_id: context
  area: completeness
  topic: Sampling and measurement provenance
  outcome: concern
  summary: Recover bounded sample-processing context without adding cultivation or
    silently reconciling source counts.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - sampling
  - supplement-context
  - concordance
  details: The record currently names only the region. Methods supply interceptor
    and composite-sampling context, while respiratory-virus capture and extraction
    shape detection. S1 contains 27 processing/library rows dated 13 May–1 July; the
    main Results says 19 May–15 July and uses a 22-sample denominator. Preserve those
    source boundaries rather than converting table rows into independent biological
    samples or asserting an exact reconciled interval.
- assessment_id: resources
  area: completeness
  topic: Public sequencing and analysis resources
  outcome: concern
  summary: The empty dataset list and publication-only links omit recoverable source
    resources.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - availability
  - archives
  details: Add the verified study project and source-linked analysis repository with
    their appropriate data/code scope. Public metadata and an immutable README/tree
    establish availability, not a complete run inventory, reproducibility result or
    confirmation of clinical coverage.
- assessment_id: remaining-fields
  area: schema
  topic: Evidence placement, cultivation and metal relevance
  outcome: supported
  summary: The remaining fields are compatible with the defined environmental surveillance
    scope.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - record
  - sampling
  - schema
  - snippets
  details: The field-study IN_VIVO evidence enum is allowed, while computational node
    evidence is appropriately scoped. Empty growth_media, metal lists and NOT_APPLICABLE
    metal relevance do not require invented media or metal-processing roles. There
    are no encoded CultureMech/MediaIngredientMech links. Current exact snippets are
    authentic even where broader source interpretation requires qualification.
- assessment_id: provenance
  area: evidence
  topic: Cache boundaries and prior graph repairs
  outcome: supported
  summary: Preserve the prior workflow-edge removals and uncertainty discussion.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - history
  - snippets
  - source-scope
  details: The TXT cache is abstract-level; the MD header says abstract_only despite
    appended main text and captions. Fresh XML independently verifies the source.
    Earlier history certifies a bounded graph repair, not the current ecological-state
    or resource completeness. No cache or append-only history is altered by this review.
- assessment_id: validation
  area: schema
  topic: Native validity and scientific qualification
  outcome: supported
  summary: Eight native checks pass; the findings concern state attribution and source/resource
    completeness.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - check-validate
  - check-validate-strict
  - check-validate-references-explained
  - ontology
  - source-scope
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality
  outcome: supported
  summary: Native scores do not certify equilibrium, exact haplotypes or transmission.
  target_ids:
  - CommunityMech:000249
  evidence_ids:
  - native-target
  - record
  metrics:
  - name: completeness
    value: 20
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata including all roles +5 environment +10
      at least 3 factors +10 at least 3 nodes +5 resources +10 media +5 datasets +5
      node metabolites). 0+5+0+10+5+0+0+0=20; absent optional roles withhold the native
      50 component without creating a schema defect.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50P1-10P2-2P3+20 min(mean node evidence/2,1)+15 if native
      COMPLETE,0,100). P1=0,P2=1,P3=2,P4=0; 3 evidence items / 3 nodes = 1; 100-10-4+10+15=111
      before capping.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count.
  - name: P2
    value: 1
    unit: findings
    definition: Observed native severity count.
  - name: P3
    value: 2
    unit: findings
    definition: Observed native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count.
findings:
- finding_id: unsupported-stability
  issue_key: cm-000249-unsupported-stability
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: unsupported ecological-state attribution adds a
    substantive biological claim beyond the surveillance evidence.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Remove or substantiate the stable-equilibrium designation
  description: STABLE asserts stable ecological equilibrium without a corresponding
    source measurement or inference; surveillance success and genotype similarity
    do not support that property.
  target_ids:
  - CommunityMech:000249
  field_paths:
  - ecological_state
  evidence_ids:
  - schema
  - sampling
  - minor-alleles
  - concordance
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    role: canonical_record
- finding_id: sampling-measurement-scope
  issue_key: cm-000249-sampling-measurement-scope
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: broad regional concordance and target identity
    remain supported; precise source qualification and sampling provenance need correction.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Qualify exact sequence identity and add bounded sampling context
  description: The unqualified identical-genotype summary omits a main/S3 conflict,
    and sparse context obscures the comparison and analytical sampling boundaries.
  target_ids:
  - CommunityMech:000249
  field_paths:
  - description
  - ecological_interactions[1].description
  - ecological_interactions[1].evidence[0].explanation
  - environmental_factors
  evidence_ids:
  - sampling
  - concordance
  - consensus-table
  - supplement-context
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    role: canonical_record
- finding_id: missing-public-resources
  issue_key: cm-000249-missing-public-resources
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: recoverable public resource provenance is missing
    without invalidating the supported observations.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Link the verified sequencing project and analysis repository
  description: The source explicitly provides a public sequencing project and processed-data/code
    repository, but the record links only the publication and DOI.
  target_ids:
  - CommunityMech:000249
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - availability
  - archives
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    role: canonical_record
actions:
- action_id: repair-unsupported-stability
  description: Remove or substantiate the stable-equilibrium designation.
  finding_ids:
  - unsupported-stability
  target_ids:
  - CommunityMech:000249
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Remove the optional STABLE value or provide specific evidence of equilibrium under
    the schema definition.
  - Do not automatically replace it with TRANSIENT, infer instability from variation
    alone, or treat repeated sampling as evidence of equilibrium.
- action_id: repair-sampling-measurement-scope
  description: Qualify exact sequence identity and add bounded sampling context.
  finding_ids:
  - sampling-measurement-scope
  target_ids:
  - CommunityMech:000249
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Retain broad regional concordance, but state that main universal identity wording
    conflicts with S3 minimum-one-SNP groups 5_28_S and 6_30_S_COL; five other groups
    include zero-distance California hits.
  - State that comparisons exclude gaps/N positions and use the available clinical
    snapshot; do not infer specific transmission or complete local infection coverage.
  - Add the four-interceptor, 24-hour composite sampling and capture-enrichment context
    with direct source evidence, keeping these separate from cultivation.
  - Preserve the main/S1 date and sample-denominator differences rather than silently
    reconciling them; do not add the conflicting July-only emergence claim.
- action_id: repair-missing-public-resources
  description: Link the verified sequencing project and analysis repository.
  finding_ids:
  - missing-public-resources
  target_ids:
  - CommunityMech:000249
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Add PRJNA661613 with the source-supported enriched wastewater RNA scope and claim-level
    Data availability evidence.
  - Add the paper-linked analysis repository and record immutable commit 0104c8431936374caaba5c93e809968d3496ed92
    as inspected provenance, keeping data availability separate from successful reproduction.
  - Do not invent sample/run counts, certify uninspected sequence or notebook contents,
    or treat the metadata-linked PRJEB40770 as independently verified.
- action_id: preserve-surveillance-graph
  description: Preserve the three bounded surveillance observations and zero causal
    arrows during separately authorized curation.
  finding_ids:
  - unsupported-stability
  - sampling-measurement-scope
  - missing-public-resources
  target_ids:
  - CommunityMech:000249
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bay_Area_Sewage_SARS_CoV2_Surveillance_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Do not restore sequencing/analysis workflow arrows or infer viral replication,
    infectivity, complete haplotypes, transmission or ecological interactions from
    these observations.
  - Retain the PARTIAL introduction inference, broad clinical concordance and current
    uncertainty discussion with corrected source qualification.
  - After authorized curation, preserve append-only history and rerun schema, strict,
    term, history, reference and target/corpus network checks.
limitations:
- Whole scientific main and all three main figure pixels were inspected. S1 was read
  completely; S2 inspection covered all nineteen SARS-CoV-2 rows and selected measurement
  columns, not all other viruses; S3 comparisons were grouped across all 1349 rows
  with both one-distance groups checked; S4 review covered the four recurrent focal
  loci and representative rows.
- No raw reads, clinical sequence tables, consensus FASTA, alignment, variant calling,
  deposited notebooks or statistical pipeline was reanalyzed. Published table inspection
  is not independent sequence reproduction.
- Main and supplements disagree on universal exact identity, sample dates/count boundaries
  and July-only emergence. These discrepancies are retained rather than reconciled
  by assumption; the current node does not encode the conflicting emergence date.
- Public archive review covered project metadata and immutable repository metadata/tree/README
  only. No full run inventory or linked PRJEB40770 content was verified.
- ASM access returned 403 and the PMC browser response was a CAPTCHA; complete source
  assessment instead used successfully retrieved Europe PMC XML and supplements plus
  primary figure assets.
- The MD cache frontmatter is stale relative to its appended main text; both cache
  files were preserved unchanged. Corpus warning counts are distinct from the clean
  target-native graph.
notes:
- No canonical, cache, history or generated file was changed.
- All 25 repository inputs were pinned before assessment and rechecked.
- Quoted primary-source text totals 11 words across the publication, including all
  main/supplement evidence.
- Native quality 100 is capped from 111; absent optional roles and inapplicable cultivation
  are not invented to raise completeness.
tags:
- record-review
- wastewater
- viral-surveillance
- batch-06
```
