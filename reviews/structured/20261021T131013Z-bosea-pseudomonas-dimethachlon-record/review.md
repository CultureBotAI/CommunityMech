# Bosea–Pseudomonas dimethachlon consortium record review

- Review: 20261021T131013Z-bosea-pseudomonas-dimethachlon-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T13:07:09.360665Z
- Finished UTC: 2026-10-21T13:10:13.731852Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

The exact two-strain identity, reported intermediate handoff, three qualified nodes and single PARTIAL soil-removal edge are supported at abstract scope. One minor finding concerns outcome placement and inconsistent unresolved zebrafish evidence classification. Critical full Methods and supplements remain inaccessible.

## Scope And Provenance

Entire record and each of its three nodes/one arrow assessed against direct abstract, schema/ontology, history and bounded source-access/resource evidence.

Selection: Only released CommunityMech:000334, first target of the fresh batch08 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000334 | kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml | maintained | Bosea-Pseudomonas Dimethachlon-Degradation Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000334 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000334 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000334 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000334 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000334 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000334 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000334 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000334 | Reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000334 | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000334 | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |
| Primary bibliographic identity | passed | True | CommunityMech:000334 | Exact DOI, PMID, title and complete direct abstract agree. |
| Full primary source and critical supplemental verification | unavailable | True | CommunityMech:000334 | Critical main Methods/Results and assay details remain unavailable in inspected public routes; abstract support is preserved. |
| Medium and archive correspondence | not_applicable | False | CommunityMech:000334 | No exact medium or archive accession established; no omission finding or guessed linkage. |
| Optional structured source adapter | unavailable | False | CommunityMech:000334 | No runnable adapter established in fresh batch08 runtime; no expression-module or exact-strain inference. |

## Scientific And Domain Assessments

### Defined S6/KH-1 consortium and enrichment boundary

identity: supported. Targets: CommunityMech:000334.

The record correctly denotes the constructed two-strain consortium rather than the broader JHJ-2 enrichment. ENGINEERED, SYNTHETIC and BIOREMEDIATION are appropriate.

### Exact strains, names, roles and metabolite

grounding: supported. Targets: CommunityMech:000334.

The source supports S6 as upstream degrader and KH-1 as recipient/intermediate degrader. Existing canonical labels and 3,5-dichloroaniline grounding are valid.

Preserve Allobosea as canonical NCBI label, Bosea as the paper name and curated GTDB Bosea lineage as its separately documented mapping. Do not substitute a species, infer exact genomes from bin labels or impose a polymer-only restriction on PRIMARY_DEGRADER.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000334.

Retain the reported S6 → KH-1 intermediate handoff as CROSS_FEEDING with its existing mechanism limits.

The source explicitly assigns intermediate production to S6 and degradation to KH-1. The node does not assert mineralization, reciprocal fitness benefit or enzyme necessity.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000334.

Retain the PARTIAL handoff → soil-removal contribution; the existing qualification distinguishes plausible mechanism from unresolved in-soil flux and necessity.

Both strain functions and soil removal are reported. The edge appropriately avoids claiming measured in-soil transfer or a strain/mediator perturbation. No soil-removal → zebrafish arrow should be restored without sample linkage.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000334.

Retain the source-reported removal endpoint under the tested conditions, without a mineralization or soil-sample toxicity inference.

The node expressly excludes enrichment JHJ-2 kinetics from the pair. Exact soil protocol, detection limit, dose and duration remain unavailable; this review does not supply them.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000334.

Retain the bounded zebrafish result and OTHER classification while stage, dose and endpoint remain unresolved.

The current node limits the statement to the reported assay and does not claim universal safety, a separate cross-feeding event or linkage to the remediated soil samples.

### Environmental factors versus outcome observations

representation: concern. Targets: CommunityMech:000334.

Both environmental_factors entries repeat endpoints rather than environmental conditions; the toxicity evidence also contradicts the graph’s explicit unresolved-context treatment.

Preserve the supported removal and toxicity observations in their existing outcome nodes or appropriate design summary. Do not infer IN_VIVO merely from the word zebrafish or fill environmental fields with guessed conditions.

### Cultivation, datasets and source access

provenance: unknown. Targets: CommunityMech:000334.

The directly retrieved abstract provides no exact recipe or archive identifiers suitable for further grounding.

The metagenomic-bin statement is a lead for later full-source verification, not a verified deposited genome or absence finding. Keep growth_media and cultivation_setup unfilled until exact pair-specific conditions are recovered. The primary publication resource remains valid.

### Prior repairs, discussion and exact excerpts

provenance: supported. Targets: CommunityMech:000334.

The three nodes and single qualified edge preserve the previous repair, and the open discussion accurately identifies the missing assay details.

Issue 1266 is closed; issue 1268 remains open with its comment explicitly withholding certification of non-graph blocks. Current review does not close or supersede unrelated targets in those issues.

### Native checks and ontology labels

schema: supported. Targets: CommunityMech:000334.

Eight native checks and four current ID/label pairs pass; source access remains a separate limitation.

### Native mechanical scores

completeness: supported. Targets: CommunityMech:000334.

Native scores measure structural completeness and validation, not completed scientific review.

## Findings

### outcome-context: Separate assay outcomes from environmental conditions

minor / open / confirmed; issue key: cm-000334-outcome-context.

environmental_factors[0] and [1] encode removal and toxicity results rather than conditions. The zebrafish evidence in environmental_factors[1] is labeled IN_VITRO even though ecological_interactions[2] correctly preserves its unresolved assay context as OTHER.

## Recommended Actions And Acceptance Checks

### repair-outcome-context

Move or remove redundant outcome-valued environmental factors and align the retained zebrafish evidence with the verified assay scope.

- Keep supported removal and zebrafish outcomes in their existing bounded nodes or design summary; environmental_factors should contain actual measured or specified conditions, not endpoint duplicates.
- Until the primary Methods resolves the assay, preserve an explicitly unresolved evidence classification consistent with the existing OTHER node. Do not replace it automatically with IN_VIVO or infer organism stage, dose or endpoint.
- When full Methods/SI becomes legitimately available, verify toxicity exposure details and soil-sample linkage before adding conditions or causal edges; do not transfer enrichment JHJ-2 protocol or kinetics to the pair.
- Preserve exact strains, canonical Allobosea/GTDB source-name distinction, three qualified nodes and the PARTIAL handoff-to-soil edge. Run focused schema, strict, terms, reference and history checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml; Entire record, including three nodes and one arrow | supports | The maintained record distinguishes the reconstructed strain pair, enrichment origin and separate removal/toxicity endpoints; non-graph outcome placement and assay classification remain inconsistent. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=41326129&amp;retmode=xml; Article-level metadata and abstract where supplied | supports | Article-level PMID, DOI, title and complete abstract identify the focal two-strain study. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41326129%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article-level metadata and abstract where supplied | supports | The same abstract and DOI agree; there is no PMCID and the only full-text route is subscription DOI access. |
| crossref | https://api.crossref.org/works/10.1016/j.pestbp.2025.106807; Article-level metadata and abstract where supplied | supports | Bibliographic identity agrees; metadata is not full Methods or independent mechanistic confirmation. |
| pair | PMID:41326129; Abstract: reconstructed consortium and strain-function sentence | supports | S6 transforms the parent fungicide to 3,5-dichloroaniline; KH-1 degrades that intermediate. Both isolates originate from JHJ-2. |
| soil | PMID:41326129; Abstract: soil bioaugmentation sentence | supports | The pair is reported to remove both parent and intermediate from contaminated soil. This is not a mineralization measurement or proof of the in-soil mediator. |
| toxicity | PMID:41326129; Abstract: zebrafish toxicity sentence | supports | The source reports non-toxic transformation products in a zebrafish assay but does not specify organism stage, exposure, endpoint or linkage to the soil samples. |
| bins | PMID:41326129; Abstract: final metagenomic-binning sentences | supports | The 16 recovered bins and proposed enzymes concern metagenomic inference; direct bin-to-isolate identity and enzyme necessity are not certified. |
| schema | src/communitymech/schema/communitymech.yaml; EnvironmentalFactor; MicrobialCommunity.environmental_factors; EvidenceSourceEnum; FunctionalRoleEnum; InteractionTypeEnum.CROSS_FEEDING | supports | Environmental factors are conditions or parameters. IN_VITRO requires a known in-vitro context; the record already preserves unresolved zebrafish context with OTHER in its graph. CROSS_FEEDER means using metabolites from other taxa; PRIMARY_DEGRADER has no polymer-only restriction. |
| ontology | ontology-authority.json; Whole bounded receipt | supports | Four unique ontology pairs across 12 occurrences match current local OAK authorities; Allobosea is the current genus label for 85413, with the paper Bosea name retained separately. |
| resources | dataset-verification.json; Whole bounded receipt | supports | No exact genome/strain accession or cultivation recipe is established from the accessible abstract. No dataset-absence or missing-medium-link finding is inferred. |
| snippets | snippet-audit.json; Whole bounded receipt | supports | All nine evidence excerpts match direct PubMed abstract and the pinned cache; exact quotation does not establish unavailable assay details. |
| history | provenance-audit.json; Whole bounded receipt | supports | The exact prior decision and history were inspected; closed issue 1266 repairs remain present, while open 1268 retains the target-specific non-graph source-method follow-up. |
| native-target | support-audit.json; Whole bounded receipt | supports | Native scores and graph completeness are mechanical diagnostics separate from source access and scientific certification. |
| source-scope | source-audit.json; Whole bounded receipt | supports | The accessible abstract and actual access receipts support a partial review; no full-main, figure or supplement inspection is claimed. |
| independent-source | root-independent-source-audit.json; Whole bounded receipt | supports | Root independently agrees with the retained graph and one bounded non-graph finding at abstract scope. |
| access-doi | https://doi.org/10.1016/j.pestbp.2025.106807; Inspected response body and retrieval receipt | context_only | HTTP 200 is only a redirect shell. |
| access-article-api | https://api.elsevier.com/content/article/doi/10.1016/j.pestbp.2025.106807?httpAccept=text/xml; Inspected response body and retrieval receipt | context_only | HTTP 200 provides coredata without full article text. |
| access-publisher | https://www.sciencedirect.com/science/article/pii/S0048357525005206; Inspected response body and retrieval receipt | context_only | HTTP 403 is a visible access-error page. |
| access-openalex | https://api.openalex.org/works/https://doi.org/10.1016/j.pestbp.2025.106807; Inspected response body and retrieval receipt | context_only | Metadata reports closed access and no open PDF location, without establishing global unavailability. |
| search-leads | Exact focal DOI/title/PII discovery; indexed-search-leads.json; direct-web-attempts.json | context_only | Indexed publisher sections and mirrors are leads only; no recipe or JHJ-2 kinetics are imported. |
| local-search | Maintained local corpus; local-search.json | supports | Ignored-inclusive local searches define the record/resource reuse and provenance boundaries. |
| adapter | Optional structured source adapter; adapter-check.json | supports | Fresh batch08 runtime discovery did not establish a usable local adapter. An external task checkout was not executed. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml; Actual execution 2026-10-21T13:07:54.223810+00:00 to 2026-10-21T13:07:55.050435+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-strict kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml --out /private/tmp/cm-review-session/batch-08/000334/strict-report.tsv; Actual execution 2026-10-21T13:07:54.224165+00:00 to 2026-10-21T13:07:56.480490+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-terms kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml; Actual execution 2026-10-21T13:07:54.224243+00:00 to 2026-10-21T13:07:56.021267+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml; Actual execution 2026-10-21T13:07:55.050812+00:00 to 2026-10-21T13:07:55.130169+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb-domain kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml; Actual execution 2026-10-21T13:07:55.130455+00:00 to 2026-10-21T13:07:56.556898+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-history history/records/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium; Actual execution 2026-10-21T13:07:56.021705+00:00 to 2026-10-21T13:07:56.836130+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T13:07:56.836692+00:00 to 2026-10-21T13:07:56.902239+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-references-explained kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml; Actual execution 2026-10-21T13:07:56.929295+00:00 to 2026-10-21T13:07:58.217681+00:00 | supports | Reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00 | supports | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00 | supports | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |

## Limits And Additional Notes

- Full primary Methods/Results, figures, supplements, culture conditions and zebrafish stage/dose/endpoints were not accessible through the inspected routes. Whole-source scientific certification remains incomplete.
- The enriched consortium JHJ-2 and reconstructed S6/KH-1 pair are distinct. No enrichment kinetics, dose or incubation duration is assigned to the pair from indexed section leads.
- The abstract supports strain-specific production/consumption of 3,5-dichloroaniline and reported removal/toxicity endpoints. It does not establish mineralization, universal safety, in-soil flux, enzyme necessity or linkage between soil and zebrafish samples.
- Sixteen metagenomic bins, including Bosea bin 12 and Pseudomonas bin 15, are not automatically exact isolate genomes. Potential enzymes remain hypotheses; no genome accession, protein identity or sequence analysis was inferred.
- Access flags and bounded unsuccessful discovery do not establish global absence of public source material or datasets. No paid provider, authentication bypass, author contact, raw-data reanalysis or substitution of another consortium.
- No canonical, cache, history, generated or saved-review file changed; all 23 inspected inputs remain pinned.
- All nine evidence occurrences match the direct abstract and cache. Exact matching does not resolve missing culture or toxicity Methods.
- Completeness75 and quality100/raw123 are mechanical metrics; the review remains partial and scientific_review false.
- No new graph node, arrow, recipe, strain accession or dataset is required solely to fill optional fields.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T131013Z-bosea-pseudomonas-dimethachlon-record
kind: record
repository: CultureBotAI/CommunityMech
title: Bosea–Pseudomonas dimethachlon consortium record review
started_at: '2026-10-21T13:07:09.360665Z'
finished_at: '2026-10-21T13:10:13.731852Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary source scope, local native/ontology
    checks and supporting provenance; no person-level independence asserted.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: The exact two-strain identity, reported intermediate handoff, three qualified
  nodes and single PARTIAL soil-removal edge are supported at abstract scope. One
  minor finding concerns outcome placement and inconsistent unresolved zebrafish evidence
  classification. Critical full Methods and supplements remain inaccessible.
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
  - path: history/records/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium/2026-10-05T142559Z-codex-058c2b.yaml
    sha256: 90d1bb9d4597326605f25a54a7bd5b3f754cb1361a0478841342b78f8057f4bf
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
    sha256: 8c5570c61580e4a5c7232402076c0e47bc73c8b5aabe6a8fb1394b625eeee074
    role: target
  - path: references_cache/PMID_41326129.md
    sha256: 8791b0c27f83a1cb926b0f40cf1cd8c4ea012c6aad6c1695c2cb2ff692d6672b
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch8.yaml
    sha256: a03eceb4ca205fdd9092a4f18c0fa4c068e8ec91ee5a62d09da97b87a4f50a25
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
- target_id: CommunityMech:000334
  path: kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  label: Bosea-Pseudomonas Dimethachlon-Degradation Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
    role: canonical_record
scope:
  description: Entire record and each of its three nodes/one arrow assessed against
    direct abstract, schema/ontology, history and bounded source-access/resource evidence.
  selection: Only released CommunityMech:000334, first target of the fresh batch08
    checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000334
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000334
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000334
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-08/000334/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000334
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000334
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000334
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000334
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000334
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000334
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused checks and corpus cache-filename preflight; mechanical
    success does not certify source science.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  target_ids:
  - CommunityMech:000334
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit reuse of fresh batch08 corpus receipts, not a target-specific
    pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  target_ids:
  - CommunityMech:000334
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit reuse of fresh batch08 corpus receipts, not a target-specific
    pass.
- check_id: source-identity
  name: Primary bibliographic identity
  status: passed
  required: true
  summary: Exact DOI, PMID, title and complete direct abstract agree.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - pubmed
  - epmc
  - crossref
- check_id: scientific-source
  name: Full primary source and critical supplemental verification
  status: unavailable
  required: true
  summary: Critical main Methods/Results and assay details remain unavailable in inspected
    public routes; abstract support is preserved.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - source-scope
  - independent-source
  - access-publisher
  - access-article-api
- check_id: cross-mech
  name: Medium and archive correspondence
  status: not_applicable
  required: false
  summary: No exact medium or archive accession established; no omission finding or
    guessed linkage.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - resources
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No runnable adapter established in fresh batch08 runtime; no expression-module
    or exact-strain inference.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  locator: Entire record, including three nodes and one arrow
  summary: The maintained record distinguishes the reconstructed strain pair, enrichment
    origin and separate removal/toxicity endpoints; non-graph outcome placement and
    assay classification remain inconsistent.
  support: supports
  accessed_at: '2026-10-21T13:10:13.721653Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41326129&retmode=xml
  locator: Article-level metadata and abstract where supplied
  summary: Article-level PMID, DOI, title and complete abstract identify the focal
    two-strain study.
  support: supports
  accessed_at: '2026-10-21T13:07:37.287523Z'
  snapshot_sha256: 55a20d097a044cab2fb7b7fb7c29446f5e7c4170da9b103288a00e946944368a
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41326129%20AND%20SRC:MED&format=json&resultType=core
  locator: Article-level metadata and abstract where supplied
  summary: The same abstract and DOI agree; there is no PMCID and the only full-text
    route is subscription DOI access.
  support: supports
  accessed_at: '2026-10-21T13:07:37.729256Z'
  snapshot_sha256: 7bc39e5cbd47858779153e3df816d884d1186c89e0d5e0e56d149b37b1ba5045
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.pestbp.2025.106807
  locator: Article-level metadata and abstract where supplied
  summary: Bibliographic identity agrees; metadata is not full Methods or independent
    mechanistic confirmation.
  support: supports
  accessed_at: '2026-10-21T13:07:37.378516Z'
  snapshot_sha256: 6f2a86c876ebf4c17bc82abf34bf8f28911af130205a4f6bea897408736d1bc2
- evidence_id: pair
  kind: primary_source
  reference: PMID:41326129
  locator: 'Abstract: reconstructed consortium and strain-function sentence'
  summary: S6 transforms the parent fungicide to 3,5-dichloroaniline; KH-1 degrades
    that intermediate. Both isolates originate from JHJ-2.
  support: supports
  accessed_at: '2026-10-21T13:10:13.721956Z'
  snapshot_sha256: 55a20d097a044cab2fb7b7fb7c29446f5e7c4170da9b103288a00e946944368a
  quote: Bosea sp. S6
- evidence_id: soil
  kind: primary_source
  reference: PMID:41326129
  locator: 'Abstract: soil bioaugmentation sentence'
  summary: The pair is reported to remove both parent and intermediate from contaminated
    soil. This is not a mineralization measurement or proof of the in-soil mediator.
  support: supports
  accessed_at: '2026-10-21T13:10:13.722194Z'
  snapshot_sha256: 55a20d097a044cab2fb7b7fb7c29446f5e7c4170da9b103288a00e946944368a
  quote: complete removal
- evidence_id: toxicity
  kind: primary_source
  reference: PMID:41326129
  locator: 'Abstract: zebrafish toxicity sentence'
  summary: The source reports non-toxic transformation products in a zebrafish assay
    but does not specify organism stage, exposure, endpoint or linkage to the soil
    samples.
  support: supports
  accessed_at: '2026-10-21T13:10:13.722276Z'
  snapshot_sha256: 55a20d097a044cab2fb7b7fb7c29446f5e7c4170da9b103288a00e946944368a
  quote: Toxicity assays using the zebrafish
- evidence_id: bins
  kind: primary_source
  reference: PMID:41326129
  locator: 'Abstract: final metagenomic-binning sentences'
  summary: The 16 recovered bins and proposed enzymes concern metagenomic inference;
    direct bin-to-isolate identity and enzyme necessity are not certified.
  support: supports
  accessed_at: '2026-10-21T13:10:13.722316Z'
  snapshot_sha256: 55a20d097a044cab2fb7b7fb7c29446f5e7c4170da9b103288a00e946944368a
  quote: potential degradation enzymes were hypothesized
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: EnvironmentalFactor; MicrobialCommunity.environmental_factors; EvidenceSourceEnum;
    FunctionalRoleEnum; InteractionTypeEnum.CROSS_FEEDING
  summary: Environmental factors are conditions or parameters. IN_VITRO requires a
    known in-vitro context; the record already preserves unresolved zebrafish context
    with OTHER in its graph. CROSS_FEEDER means using metabolites from other taxa;
    PRIMARY_DEGRADER has no polymer-only restriction.
  support: supports
  accessed_at: '2026-10-21T13:10:13.722488Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded receipt
  summary: Four unique ontology pairs across 12 occurrences match current local OAK
    authorities; Allobosea is the current genus label for 85413, with the paper Bosea
    name retained separately.
  support: supports
  accessed_at: '2026-10-21T13:10:13.722778Z'
  snapshot_sha256: 46cc9ce2d22044fa48957eb30d1196f266be44795a91128d83ca514e01d5798a
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded receipt
  summary: No exact genome/strain accession or cultivation recipe is established from
    the accessible abstract. No dataset-absence or missing-medium-link finding is
    inferred.
  support: supports
  accessed_at: '2026-10-21T13:10:13.723130Z'
  snapshot_sha256: a8d3d6cf15dcda32b51c07e99417cd449b1f8ed1470c125ccf582d9a91e9c847
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded receipt
  summary: All nine evidence excerpts match direct PubMed abstract and the pinned
    cache; exact quotation does not establish unavailable assay details.
  support: supports
  accessed_at: '2026-10-21T13:10:13.723567Z'
  snapshot_sha256: 825bc08e6f854facc8ae9c1bf80339414712b441a71ed339f5896bfb3cf47250
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded receipt
  summary: The exact prior decision and history were inspected; closed issue 1266
    repairs remain present, while open 1268 retains the target-specific non-graph
    source-method follow-up.
  support: supports
  accessed_at: '2026-10-21T13:10:13.724007Z'
  snapshot_sha256: 9b4afee59179c756b6ce6c42fc3147f7228fea0c1d8bc1426cd897e41b87fc63
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded receipt
  summary: Native scores and graph completeness are mechanical diagnostics separate
    from source access and scientific certification.
  support: supports
  accessed_at: '2026-10-21T13:10:13.724254Z'
  snapshot_sha256: 9c44551b4e2e9be633572b5e7f5f88731dfca1f10e611b6338ea452416659269
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded receipt
  summary: The accessible abstract and actual access receipts support a partial review;
    no full-main, figure or supplement inspection is claimed.
  support: supports
  accessed_at: '2026-10-21T13:10:13.724312Z'
  snapshot_sha256: 1e62080d84dd4f5da52cb71485f65ae0d018d67c300e73c082ed476163f21e73
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded receipt
  summary: Root independently agrees with the retained graph and one bounded non-graph
    finding at abstract scope.
  support: supports
  accessed_at: '2026-10-21T13:10:13.724353Z'
  snapshot_sha256: 9fadf554d90985af19602368649c00a2b3d3953418df6637c7247031a5484a8e
- evidence_id: access-doi
  kind: database
  reference: https://doi.org/10.1016/j.pestbp.2025.106807
  locator: Inspected response body and retrieval receipt
  summary: HTTP 200 is only a redirect shell.
  support: context_only
  accessed_at: '2026-10-21T13:07:37.683258Z'
  snapshot_sha256: 519b8d9f327d2a26c9eecc4c2f9b9533f40e97923d5f30ae7b847ed3436130e2
- evidence_id: access-article-api
  kind: database
  reference: https://api.elsevier.com/content/article/doi/10.1016/j.pestbp.2025.106807?httpAccept=text/xml
  locator: Inspected response body and retrieval receipt
  summary: HTTP 200 provides coredata without full article text.
  support: context_only
  accessed_at: '2026-10-21T13:07:37.702048Z'
  snapshot_sha256: f7131a4dc52706c3e301eee66733dcc5156cff9b7d9b31ed98e6380720a96a49
- evidence_id: access-publisher
  kind: database
  reference: https://www.sciencedirect.com/science/article/pii/S0048357525005206
  locator: Inspected response body and retrieval receipt
  summary: HTTP 403 is a visible access-error page.
  support: context_only
  accessed_at: '2026-10-21T13:07:37.816699Z'
  snapshot_sha256: bd88be94cbedfc768f92a016544c08a84709c24e56092e8ffcfa7ecf1bc27a5e
- evidence_id: access-openalex
  kind: database
  reference: https://api.openalex.org/works/https://doi.org/10.1016/j.pestbp.2025.106807
  locator: Inspected response body and retrieval receipt
  summary: Metadata reports closed access and no open PDF location, without establishing
    global unavailability.
  support: context_only
  accessed_at: '2026-10-21T13:08:17.690521Z'
  snapshot_sha256: 50a5df6b72c1ebb072da4a337e1fc8a3920f4fcb1b278d2d7a73a75d7e21124d
- evidence_id: search-leads
  kind: search
  reference: Exact focal DOI/title/PII discovery
  locator: indexed-search-leads.json; direct-web-attempts.json
  summary: Indexed publisher sections and mirrors are leads only; no recipe or JHJ-2
    kinetics are imported.
  support: context_only
  accessed_at: '2026-10-21T13:10:13.724691Z'
  snapshot_sha256: 8a435f46eda44b0991752c3be315cf66159a4e21c15835388117919b496c837e
  search_scope: Exact focal DOI/title plus PII PDF and author-institution terms; bounded
    public search, no global absence claim.
- evidence_id: local-search
  kind: search
  reference: Maintained local corpus
  locator: local-search.json
  summary: Ignored-inclusive local searches define the record/resource reuse and provenance
    boundaries.
  support: supports
  accessed_at: '2026-10-21T13:10:13.724928Z'
  snapshot_sha256: 3fef059f97512f84390f1e4c016208e52427040c22f35008c6e846248211de0c
  search_scope: Maintained record/taxon/mapping roots, including ignored files, as
    recorded in the receipt.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: adapter-check.json
  summary: Fresh batch08 runtime discovery did not establish a usable local adapter.
    An external task checkout was not executed.
  support: supports
  accessed_at: '2026-10-21T13:10:13.725449Z'
  snapshot_sha256: 6bed01f5679a1193735ea7c7920ede239f75012c1f4bdfe6f37dad26ffd12c1e
  search_scope: Task runtime PATH, venv/module and ignored-inclusive filenames; not
    a global absence claim.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  locator: Actual execution 2026-10-21T13:07:54.223810+00:00 to 2026-10-21T13:07:55.050435+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T13:07:55.050435Z'
  snapshot_sha256: 0e25b0fe8bf99cee88394796920645b1c9a5b1484422f17106ab21ef12d36ddc
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-08/000334/strict-report.tsv
  locator: Actual execution 2026-10-21T13:07:54.224165+00:00 to 2026-10-21T13:07:56.480490+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T13:07:56.480490Z'
  snapshot_sha256: a13628741d539c4e5f6a8ecb7be6e8421f5ddd9de511350b4f178addcf2eecfe
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  locator: Actual execution 2026-10-21T13:07:54.224243+00:00 to 2026-10-21T13:07:56.021267+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T13:07:56.021267Z'
  snapshot_sha256: 2926d15ed8a444fff6434eafc9f07f1528e5f4f7899a2240c1235b39b0a66c01
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  locator: Actual execution 2026-10-21T13:07:55.050812+00:00 to 2026-10-21T13:07:55.130169+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T13:07:55.130169Z'
  snapshot_sha256: 57aab5636799223520fddcbec7d0e253a9c8437115c3f4d3f0360666d439aef8
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  locator: Actual execution 2026-10-21T13:07:55.130455+00:00 to 2026-10-21T13:07:56.556898+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T13:07:56.556898Z'
  snapshot_sha256: 4151b69833f14ef40a02fffb5e1e61703e0c80b7be8e3a9c0a2602e7aefb349c
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium
  locator: Actual execution 2026-10-21T13:07:56.021705+00:00 to 2026-10-21T13:07:56.836130+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T13:07:56.836130Z'
  snapshot_sha256: 20f1030ad545df56e04a90256ace809793ec4f0fc3173433ff8de26bff3366ea
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T13:07:56.836692+00:00 to 2026-10-21T13:07:56.902239+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T13:07:56.902239Z'
  snapshot_sha256: 699c7f4cf153de8eef780bc6ebea2ba1b47768ec6ded14de3f0c3b20ee5fa2cf
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
  locator: Actual execution 2026-10-21T13:07:56.929295+00:00 to 2026-10-21T13:07:58.217681+00:00
  summary: Reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T13:07:58.217681Z'
  snapshot_sha256: 9c011d67169cb7986429ae0b7b98adb6faa11a2f25b1651cd738a20350928aea
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:11.311177Z'
  snapshot_sha256: 2d17097db768619fa7fea156f7c37781fa9cd463a6abdce6f529112518848cf0
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:15.408522Z'
  snapshot_sha256: 1332cfd7980ec54d517d625aff43fa6328c1a19fd405a7aef071f78af9774f3f
assessments:
- assessment_id: identity
  area: identity
  topic: Defined S6/KH-1 consortium and enrichment boundary
  outcome: supported
  summary: The record correctly denotes the constructed two-strain consortium rather
    than the broader JHJ-2 enrichment. ENGINEERED, SYNTHETIC and BIOREMEDIATION are
    appropriate.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - pair
  - soil
  - record
  dimensions:
  - name: community_scope
    value: Defined pair reconstructed from enrichment JHJ-2
    definition: Keep the pair distinct from the source enrichment and metagenomic
      bins.
    evidence_ids:
    - pair
    - bins
  - name: source_strain
    value: Bosea sp. S6; Pseudomonas sp. KH-1
    definition: Exact source strain designations, without invented deposit aliases.
    evidence_ids:
    - pair
  - name: taxon_rank
    value: Genus grounding with strain designation
    definition: Current Allobosea 85413 and Pseudomonas 286 do not assert a resolved
      species identity.
    evidence_ids:
    - ontology
  - name: grounding_status
    value: GROUNDED for both taxa
    definition: Retain curated GTDB Bosea mapping independently of the current NCBI
      genus spelling.
    evidence_ids:
    - ontology
    - record
  - name: environment
    value: Contaminated-soil bioaugmentation endpoint
    definition: The soil annotation is supported for the reported application; other
      assays need their own conditions.
    evidence_ids:
    - soil
  - name: medium
    value: Unresolved at directly inspected abstract scope
    definition: No precise medium recipe, inoculum, duration or temperature is invented.
    evidence_ids:
    - source-scope
  - name: experimental_setting
    value: Strain transformation, soil bioaugmentation and zebrafish toxicity assays
    definition: Do not assume all endpoints use the same material or exposure.
    evidence_ids:
    - pair
    - soil
    - toxicity
  - name: evidence_tier
    value: Direct primary abstract
    definition: Full Methods, figures and supplements remain unavailable.
    evidence_ids:
    - source-scope
- assessment_id: taxonomy
  area: grounding
  topic: Exact strains, names, roles and metabolite
  outcome: supported
  summary: The source supports S6 as upstream degrader and KH-1 as recipient/intermediate
    degrader. Existing canonical labels and 3,5-dichloroaniline grounding are valid.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - pair
  - ontology
  - schema
  details: Preserve Allobosea as canonical NCBI label, Bosea as the paper name and
    curated GTDB Bosea lineage as its separately documented mapping. Do not substitute
    a species, infer exact genomes from bin labels or impose a polymer-only restriction
    on PRIMARY_DEGRADER.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain the reported S6 → KH-1 intermediate handoff as CROSS_FEEDING with
    its existing mechanism limits.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - pair
  - schema
  details: The source explicitly assigns intermediate production to S6 and degradation
    to KH-1. The node does not assert mineralization, reciprocal fitness benefit or
    enzyme necessity.
- assessment_id: arrow-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: Retain the PARTIAL handoff → soil-removal contribution; the existing qualification
    distinguishes plausible mechanism from unresolved in-soil flux and necessity.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - pair
  - soil
  details: Both strain functions and soil removal are reported. The edge appropriately
    avoids claiming measured in-soil transfer or a strain/mediator perturbation. No
    soil-removal → zebrafish arrow should be restored without sample linkage.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain the source-reported removal endpoint under the tested conditions,
    without a mineralization or soil-sample toxicity inference.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - soil
  details: The node expressly excludes enrichment JHJ-2 kinetics from the pair. Exact
    soil protocol, detection limit, dose and duration remain unavailable; this review
    does not supply them.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: Retain the bounded zebrafish result and OTHER classification while stage,
    dose and endpoint remain unresolved.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - toxicity
  details: The current node limits the statement to the reported assay and does not
    claim universal safety, a separate cross-feeding event or linkage to the remediated
    soil samples.
- assessment_id: context
  area: representation
  topic: Environmental factors versus outcome observations
  outcome: concern
  summary: Both environmental_factors entries repeat endpoints rather than environmental
    conditions; the toxicity evidence also contradicts the graph’s explicit unresolved-context
    treatment.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - schema
  - record
  - soil
  - toxicity
  details: Preserve the supported removal and toxicity observations in their existing
    outcome nodes or appropriate design summary. Do not infer IN_VIVO merely from
    the word zebrafish or fill environmental fields with guessed conditions.
- assessment_id: resources
  area: provenance
  topic: Cultivation, datasets and source access
  outcome: unknown
  summary: The directly retrieved abstract provides no exact recipe or archive identifiers
    suitable for further grounding.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - resources
  - source-scope
  - bins
  details: The metagenomic-bin statement is a lead for later full-source verification,
    not a verified deposited genome or absence finding. Keep growth_media and cultivation_setup
    unfilled until exact pair-specific conditions are recovered. The primary publication
    resource remains valid.
- assessment_id: history
  area: provenance
  topic: Prior repairs, discussion and exact excerpts
  outcome: supported
  summary: The three nodes and single qualified edge preserve the previous repair,
    and the open discussion accurately identifies the missing assay details.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - history
  - snippets
  details: Issue 1266 is closed; issue 1268 remains open with its comment explicitly
    withholding certification of non-graph blocks. Current review does not close or
    supersede unrelated targets in those issues.
- assessment_id: validation
  area: schema
  topic: Native checks and ontology labels
  outcome: supported
  summary: Eight native checks and four current ID/label pairs pass; source access
    remains a separate limitation.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - schema
- assessment_id: metrics
  area: completeness
  topic: Native mechanical scores
  outcome: supported
  summary: Native scores measure structural completeness and validation, not completed
    scientific review.
  target_ids:
  - CommunityMech:000334
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-fields/taxon-role component +5 environment +10 interaction
      count +5 external resource +5 node metabolites. No three-factor, medium or dataset
      bonus.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0/P2=0/P3=1/P4=0; three node evidence/three nodes gives10 bonus; COMPLETE
      gives15; raw123, capped100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 1
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
findings:
- finding_id: outcome-context
  issue_key: cm-000334-outcome-context
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded placement and evidence-context inconsistency;
    the underlying assay outcomes and qualified graph remain supported.'
  rule_id: review-checklist.environment-and-claim-evidence
  status: open
  certainty: confirmed
  title: Separate assay outcomes from environmental conditions
  description: environmental_factors[0] and [1] encode removal and toxicity results
    rather than conditions. The zebrafish evidence in environmental_factors[1] is
    labeled IN_VITRO even though ecological_interactions[2] correctly preserves its
    unresolved assay context as OTHER.
  target_ids:
  - CommunityMech:000334
  field_paths:
  - environmental_factors[0]
  - environmental_factors[1]
  - environmental_factors[1].evidence[0].evidence_source
  evidence_ids:
  - record
  - schema
  - soil
  - toxicity
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
    role: canonical_record
actions:
- action_id: repair-outcome-context
  description: Move or remove redundant outcome-valued environmental factors and align
    the retained zebrafish evidence with the verified assay scope.
  finding_ids:
  - outcome-context
  target_ids:
  - CommunityMech:000334
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bosea_Pseudomonas_Dimethachlon_Degradation_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Keep supported removal and zebrafish outcomes in their existing bounded nodes
    or design summary; environmental_factors should contain actual measured or specified
    conditions, not endpoint duplicates.
  - Until the primary Methods resolves the assay, preserve an explicitly unresolved
    evidence classification consistent with the existing OTHER node. Do not replace
    it automatically with IN_VIVO or infer organism stage, dose or endpoint.
  - When full Methods/SI becomes legitimately available, verify toxicity exposure
    details and soil-sample linkage before adding conditions or causal edges; do not
    transfer enrichment JHJ-2 protocol or kinetics to the pair.
  - Preserve exact strains, canonical Allobosea/GTDB source-name distinction, three
    qualified nodes and the PARTIAL handoff-to-soil edge. Run focused schema, strict,
    terms, reference and history checks after separately authorized curation.
limitations:
- Full primary Methods/Results, figures, supplements, culture conditions and zebrafish
  stage/dose/endpoints were not accessible through the inspected routes. Whole-source
  scientific certification remains incomplete.
- The enriched consortium JHJ-2 and reconstructed S6/KH-1 pair are distinct. No enrichment
  kinetics, dose or incubation duration is assigned to the pair from indexed section
  leads.
- The abstract supports strain-specific production/consumption of 3,5-dichloroaniline
  and reported removal/toxicity endpoints. It does not establish mineralization, universal
  safety, in-soil flux, enzyme necessity or linkage between soil and zebrafish samples.
- Sixteen metagenomic bins, including Bosea bin 12 and Pseudomonas bin 15, are not
  automatically exact isolate genomes. Potential enzymes remain hypotheses; no genome
  accession, protein identity or sequence analysis was inferred.
- Access flags and bounded unsuccessful discovery do not establish global absence
  of public source material or datasets. No paid provider, authentication bypass,
  author contact, raw-data reanalysis or substitution of another consortium.
notes:
- No canonical, cache, history, generated or saved-review file changed; all 23 inspected
  inputs remain pinned.
- All nine evidence occurrences match the direct abstract and cache. Exact matching
  does not resolve missing culture or toxicity Methods.
- Completeness75 and quality100/raw123 are mechanical metrics; the review remains
  partial and scientific_review false.
- No new graph node, arrow, recipe, strain accession or dataset is required solely
  to fill optional fields.
tags:
- record-review
- bioremediation
- cross-feeding
- partial-source
- batch-08
```
