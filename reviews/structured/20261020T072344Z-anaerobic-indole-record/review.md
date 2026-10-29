# Anaerobic indole consortium: partial whole-record review

- Review: 20261020T072344Z-anaerobic-indole-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-20T07:20:37.517974Z
- Finished UTC: 2026-10-20T07:23:44.762952Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

Publication identities, all eight ontology labels and all eleven abstract snippets verify. The candidate interaction remains appropriately qualified. Two minor findings concern absent roles and outcomes typed as factors; two informational findings concern publication and intermediate representation. Full-text/member-level verification remains unavailable. Seven focused checks pass; the attempted history check targeted an absent advisory sidecar.

## Scope And Provenance

Entire record read and assessed at abstract/metadata level, including four lineage entries, one node, no arrows, all evidence and open gaps. Full primary detail is not certified.

Selection: Third uncovered record of batch 03 in path order, excluding validated baseline and pending batches 01/02.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ade4a9acdc245e1090522bb4f6ec5fe82ee88689.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000386 | kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml | maintained | Anaerobic Indole-Degrading Sludge Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000386 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml |
| validate-strict | passed | True | CommunityMech:000386 | uv run python scripts/validate_strict.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml --out /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000386 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000386 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000386 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml |
| validate-history | failed | False | CommunityMech:000386 | validate-history: 'history/records/Anaerobic_Indole_Degrading_Sludge_Consortium' does not exist.<br>error: recipe &#96;validate-history&#96; failed with exit code 2 |
| normalize-cache-names-check | passed | True | CommunityMech:000386 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000386 | Validating kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000386 | Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records, 57 warnings in 21 records, zero errors; exit 1. Selected target has no reported network warning. Canonical records unchanged since execution. |
| check-network-quality | failed | True | CommunityMech:000386 | Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records, 57 warnings in 21 records, zero errors; exit 1. Selected target has no reported network warning. Canonical records unchanged since execution. |
| Independent full-text and exact-member verification | unavailable | True | CommunityMech:000386 | The abstract and publisher-index excerpts are available, but full Methods, MAG tables, supplements and accessioned datasets were not inspected. The target’s explicit full-text curation gap remains unresolved. |
| History sidecar applicability | not_applicable | False | CommunityMech:000386 | Ignored-inclusive search found no matching sidecar. Presence is advisory under history/README.md; no history is created for this review. |
| Structured expression-source applicability | not_applicable | False | CommunityMech:000386 | The target has no strain-resolved gene/locus, regulator or expression-module identifier. Broad MAG affiliations cannot resolve an exact strain expression dataset; no unrelated module is substituted for primary evidence. |

## Scientific And Domain Assessments

### Enrichment versus defined community

identity: supported. Targets: CommunityMech:000386.

The record and cited publication describe the same anaerobic sludge enrichment. Its four entries denote broad affiliated populations, not four isolated species, and the text appropriately avoids exact MAG identifiers.

### taxonomy[0..3] and GTDB classifications

grounding: supported. Targets: CommunityMech:000386.

All taxon labels resolve and broad source affiliations are preserved. The NCBI/GTDB nomenclature difference is explained. Coherence/domain gates pass at the encoded ranks; no conclusion about every member of a phylum or genus, or an exact MAG, follows.

### ecological_interactions[0]: Candidate anaerobic indole-to-methanogenesis division of labor

graph: supported. Targets: CommunityMech:000386.

Candidate/inferred wording and PARTIAL computational evidence match the abstract’s proposed framework. The SYNTROPHY type must be read with that qualification; it is not proof of obligate cooperation, reciprocal benefit or measured interspecies flux. Full-text validation remains unresolved.

Participants: three bacterial phylum-level affiliations and one archaeal genus affiliation. Direction/mechanism: a proposed community functional relationship rather than identified donor/recipient pairs. Source PMID 42735627 abstract; exact short quote and locator in abstract. Methane/methanogenesis annotations represent the proposed process, not a quantitative gas measurement.

### ecological_interactions[*].downstream

graph: not_applicable. Targets: CommunityMech:000386.

No downstream arrows occur in the complete target. The source’s candidate framework does not justify inventing an ordered pairwise network from the accessible abstract.

### Engineering design and description

scope: supported. Targets: CommunityMech:000386.

Study design and endpoints agree with the abstract at the stated level. No exact biochemical attribution, gene necessity or organism-specific benefit is established by the summary. The enrichment origin/category and laboratory environment are coherent.

### taxonomy[*].functional_role

completeness: concern. Targets: CommunityMech:000386.

All four role lists are absent. The abstract’s candidate assignments should not be promoted into unqualified roles merely to fill these fields.

### environmental_factors[0..1]

representation: concern. Targets: CommunityMech:000386.

The two entries are degradation outcomes, not independent environmental conditions. Their evidence can remain useful at the relevant phenotype or endpoint assertions.

### ecological_interactions[0].metabolites

completeness: concern. Targets: CommunityMech:000386.

The structured list represents substrate and proposed final product but omits named detected intermediates already present in the record’s endpoints. This is a retrieval gap, not evidence that a particular exchange step has been demonstrated.

### Missing external resource and dataset blocks

provenance: concern. Targets: CommunityMech:000386.

The known publication DOI is not represented in external_resources. No verified public dataset accession was obtained; absence from the accessible abstract is not proof that none exists. The full-text discussion correctly keeps accession/MAG work open.

### Inline event and advisory sidecar history

provenance: supported. Targets: CommunityMech:000386.

Inline creation history and a no-change graph decision are present. No sidecar file was found, but the repository explicitly makes presence advisory. Its nonexistent-directory validation failure is retained as an inapplicable attempted check, not a record-schema defect.

### Native gates and full-source limitations

schema: concern. Targets: CommunityMech:000386.

Seven focused/preflight checks pass with unchanged caches. A separate attempted history command failed because the assumed sidecar directory is absent; its presence is advisory. Corpus warnings and unavailable full-source verification remain explicit.

### Native completeness and validation quality

completeness: concern. Targets: CommunityMech:000386.

Completeness 10 reflects an intentionally sparse abstract-grounded record. Quality 100 is capped despite minor findings and does not certify unavailable scientific detail.

## Findings

### role-metadata: Taxon roles are not represented

minor / open / confirmed; issue key: cm-000386-role-metadata.

All four role lists are absent. The existing source affiliations and candidate-function wording do not support invented definitive roles.

### outcomes-as-factors: Phenotype outcomes are stored as environmental factors

minor / open / confirmed; issue key: cm-000386-outcomes-as-factors.

Both factor entries describe removal performance rather than supplied environmental conditions. The same outcomes are already summarized in engineering endpoints.

### publication-link: Publication resource is not structured

informational / open / confirmed; issue key: cm-000386-publication-link.

The record cites the paper but has no external_resources entry for its verified DOI/PMID.

### intermediate-representation: Detected intermediates are prose-only

informational / open / confirmed; issue key: cm-000386-intermediate-representation.

Intermediate names occur in the endpoint list but not in the node’s metabolite list. Later chemical grounding must distinguish observed detection from hypothesized transfer.

## Recommended Actions And Acceptance Checks

### fix-role-metadata

Preserve unknown roles explicitly until member-specific support and an appropriate vocabulary term are available.

- Do not infer confirmed roles from phylum/genus affiliation alone.
- Candidate evidence remains qualified.
- Run strict/evidence checks for later metadata edits.

### fix-outcomes-as-factors

Place source-supported outcomes with phenotype/endpoints, maintaining the distinction from experimental conditions.

- Outcome evidence remains attached to the reported result.
- No unreported condition or operational parameter is invented.
- Run strict and reference checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml; Whole target: four broad lineage entries, one candidate node, no downstream arrows, two outcome factors and an explicit full-text curation gap | supports | This is an enrichment described through broad MAG affiliations, not a defined four-isolate assembly. Candidate functions and unresolved full-text detail are already explicitly qualified. |
| abstract | PMID:42735627; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42735627&amp;retmode=xml; complete independently retrieved abstract | supports | The abstract supports the study identity, reported degradation phenotype, detected intermediates and a proposed functional framework. It does not identify exact MAG accessions or establish a resolved partner-to-partner mechanism. |
| affiliations | PMID:42735627; PubMed abstract, MAG-resolved analysis sentence | supports | Lineage affiliations are stated at the same broad ranks used in the target. They do not authorize species or strain promotion. |
| metabolites | PMID:42735627; PubMed abstract, metabolite-profiling sentence | supports | Detected intermediate names occur in engineering endpoints but are absent from the node’s structured chemical list. Detection does not independently establish transfer between taxa. |
| publication | https://api.crossref.org/works/10.1016/j.jhazmat.2026.143606; Crossref DOI, title, article type and primary resource URL | supports | DOI 10.1016/j.jhazmat.2026.143606 and PMID 42735627 identify the same article. A DOI link could be represented without inventing a dataset accession. |
| preview | https://www.sciencedirect.com/science/article/pii/S0304389426025860; Publisher-index preview and direct-access attempts | supports | Publisher preview is an excerpt, not full text. Its access notice and failed direct opens leave full Methods, MAG tables, supplements and source data unavailable to this review. No complete-source claim is made. |
| ontology | OAK local NCBITaxon, ENVO, GO and CHEBI snapshots; Eight unique curated identifier/label pairs | supports | All labels resolve. The source wording Desulfobacterota is retained as preferred wording alongside canonical NCBI Thermodesulfobacteriota; this is not a label mismatch. Broad-rank GTDB coherence does not establish the placement of individual MAGs. |
| schema | src/communitymech/schema/communitymech.yaml; Role, evidence and environmental-factor representation | supports | All four taxon role lists are absent. The two environmental-factor entries describe observed outcomes. These are metadata distinctions, not grounds to infer missing biological roles. |
| history | history/README.md; reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml; Advisory history-presence rule, inline creation event and target decision row | supports | No target sidecar was located by the ignored-inclusive search. Presence is advisory. The prior graph decision records no change and an abstract-only assessment; it does not provide independent full-text verification. The failed directory command tested an assumed path, not malformed target history. |
| local-search | references_cache; history; reports/causal_graph_review/decisions; kb/taxa; Ignored-inclusive PMID, ID and filename search | supports | Found the abstract cache and graph decision; no matching history sidecar was found in the full history tree including ignored files. Missing roles/resource/metabolite statements refer to the complete target. |
| snippets | kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml; All 11 evidence occurrences, including native Discussion evidence | supports | Every snippet matches the independently retrieved abstract after NFKC/whitespace normalization. This lexical check does not verify full Methods or prove causal support. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml; Actual execution 2026-10-20T07:19:36.986473+00:00 to 2026-10-20T07:19:38.511702+00:00 | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-strict kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml --out /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv; Actual execution 2026-10-20T07:19:36.986708+00:00 to 2026-10-20T07:19:41.828479+00:00 | supports | uv run python scripts/validate_strict.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml --out /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-terms kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml; Actual execution 2026-10-20T07:19:36.986797+00:00 to 2026-10-20T07:19:40.478854+00:00 | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml; Actual execution 2026-10-20T07:19:38.512175+00:00 to 2026-10-20T07:19:38.641080+00:00 | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb-domain kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml; Actual execution 2026-10-20T07:19:38.641364+00:00 to 2026-10-20T07:19:42.063163+00:00 | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-history history/records/Anaerobic_Indole_Degrading_Sludge_Consortium; Actual execution 2026-10-20T07:19:40.479222+00:00 to 2026-10-20T07:19:40.590226+00:00 | supports | validate-history: 'history/records/Anaerobic_Indole_Degrading_Sludge_Consortium' does not exist.<br>error: recipe &#96;validate-history&#96; failed with exit code 2 |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-20T07:19:42.063832+00:00 to 2026-10-20T07:19:42.138220+00:00 | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-references-explained kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml; Actual execution 2026-10-20T07:19:42.138586+00:00 to 2026-10-20T07:19:44.726351+00:00 | supports | Validating kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv audit-network; Actual run finished 2026-10-20T07:08:14.467705+00:00 | supports | Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records, 57 warnings in 21 records, zero errors; exit 1. Selected target has no reported network warning. Canonical records unchanged since execution. |
| check-check-network-quality | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv check-network-quality; Actual run finished 2026-10-20T07:08:13.673449+00:00 | supports | Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records, 57 warnings in 21 records, zero errors; exit 1. Selected target has no reported network warning. Canonical records unchanged since execution. |

## Limits And Additional Notes

- Complete primary text, MAG tables, supplements and exact data accessions were unavailable; source absence is not evidence that an experiment or dataset does not exist.
- Publisher-index text was treated as preview only, not an independently inspected complete article. No paid access or correspondence was attempted.
- Broad lineage/GTDB mappings do not establish exact MAG identity, organism-specific pathway activity or measured partner exchange.
- No cultivation formulation is reconstructed from the truncated publisher preview.
- The failed history-directory attempt is retained with its actual exit code; sidecar absence is advisory and inline provenance is present.
- Required corpus warning results remain nonzero; full-source unavailability requires partial completion.
- No canonical records, caches, history or generated products changed.
- All inspected local input hashes remain unchanged; publication response hashes are retained.
- Short source quotations total 11 words.
- All batch-03 native commands use the new worktree via PYTHONPATH.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T072344Z-anaerobic-indole-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Anaerobic indole consortium: partial whole-record review'
started_at: '2026-10-20T07:20:37.517974Z'
finished_at: '2026-10-20T07:23:44.762952Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Target unchanged this session; historical codex curation prevents
    person-level independence claim.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: true
summary: Publication identities, all eight ontology labels and all eleven abstract
  snippets verify. The candidate interaction remains appropriately qualified. Two
  minor findings concern absent roles and outcomes typed as factors; two informational
  findings concern publication and intermediate representation. Full-text/member-level
  verification remains unavailable. Seven focused checks pass; the attempted history
  check targeted an absent advisory sidecar.
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
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    sha256: 9e6d7a0e292ea070a329c8fe3e064b5420631091482e6367297703e79f68df79
    role: target
  - path: references_cache/PMID_42735627.txt
    sha256: 5ad5152086f34be6987be6983a037ca36c2ea29537da95e73c4d0068e5a4943b
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
- target_id: CommunityMech:000386
  path: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
  label: Anaerobic Indole-Degrading Sludge Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    role: canonical_record
scope:
  description: Entire record read and assessed at abstract/metadata level, including
    four lineage entries, one node, no arrows, all evidence and open gaps. Full primary
    detail is not certified.
  selection: Third uncovered record of batch 03 in path order, excluding validated
    baseline and pending batches 01/02.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000386
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml'
  target_ids:
  - CommunityMech:000386
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
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
  summary: "uv run python scripts/validate_strict.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml\
    \ --out /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv"
  target_ids:
  - CommunityMech:000386
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv
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

    uv run linkml-term-validator validate-data kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000386
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
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
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000386
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
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

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml'
  target_ids:
  - CommunityMech:000386
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-history
  name: validate-history
  status: failed
  required: false
  summary: 'validate-history: ''history/records/Anaerobic_Indole_Degrading_Sludge_Consortium''
    does not exist.

    error: recipe `validate-history` failed with exit code 2'
  target_ids:
  - CommunityMech:000386
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Anaerobic_Indole_Degrading_Sludge_Consortium
  exit_code: 2
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Actual attempt against a presumed sidecar directory exited2 because
    it does not exist. Sidecar presence is advisory; validity checking is not applicable
    without a file. Inline event remains covered by record validation.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Command completed without reported issues.
  target_ids:
  - CommunityMech:000386
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
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
  summary: "Validating kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000386
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
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
  summary: 'Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records,
    57 warnings in 21 records, zero errors; exit 1. Selected target has no reported
    network warning. Canonical records unchanged since execution.'
  target_ids:
  - CommunityMech:000386
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Corpus-wide warning result, not a scientific pass; selected target has
    complete structural participation.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records,
    57 warnings in 21 records, zero errors; exit 1. Selected target has no reported
    network warning. Canonical records unchanged since execution.'
  target_ids:
  - CommunityMech:000386
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Corpus-wide warning result, not a scientific pass; selected target has
    complete structural participation.
- check_id: full-source-review
  name: Independent full-text and exact-member verification
  status: unavailable
  required: true
  summary: The abstract and publisher-index excerpts are available, but full Methods,
    MAG tables, supplements and accessioned datasets were not inspected. The target’s
    explicit full-text curation gap remains unresolved.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - abstract
  - publication
  - preview
- check_id: sidecar-applicability
  name: History sidecar applicability
  status: not_applicable
  required: false
  summary: Ignored-inclusive search found no matching sidecar. Presence is advisory
    under history/README.md; no history is created for this review.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - history
  - local-search
- check_id: structured-expression-adapter
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: The target has no strain-resolved gene/locus, regulator or expression-module
    identifier. Broad MAG affiliations cannot resolve an exact strain expression dataset;
    no unrelated module is substituted for primary evidence.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - affiliations
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
  locator: 'Whole target: four broad lineage entries, one candidate node, no downstream
    arrows, two outcome factors and an explicit full-text curation gap'
  summary: This is an enrichment described through broad MAG affiliations, not a defined
    four-isolate assembly. Candidate functions and unresolved full-text detail are
    already explicitly qualified.
  support: supports
  accessed_at: '2026-10-20T07:23:44.760114Z'
- evidence_id: abstract
  kind: primary_source
  reference: PMID:42735627
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42735627&retmode=xml;
    complete independently retrieved abstract
  summary: The abstract supports the study identity, reported degradation phenotype,
    detected intermediates and a proposed functional framework. It does not identify
    exact MAG accessions or establish a resolved partner-to-partner mechanism.
  support: supports
  accessed_at: '2026-10-20T07:21:02.116505Z'
  quote: testable functional framework
  snapshot_sha256: e9043520ad64296c3963c87b7b2affc576ac77ebbf12a20fb09f5f1db44a9a9c
- evidence_id: affiliations
  kind: primary_source
  reference: PMID:42735627
  locator: PubMed abstract, MAG-resolved analysis sentence
  summary: Lineage affiliations are stated at the same broad ranks used in the target.
    They do not authorize species or strain promotion.
  support: supports
  accessed_at: '2026-10-20T07:21:02.116505Z'
  quote: candidate functions may be distributed
- evidence_id: metabolites
  kind: primary_source
  reference: PMID:42735627
  locator: PubMed abstract, metabolite-profiling sentence
  summary: Detected intermediate names occur in engineering endpoints but are absent
    from the node’s structured chemical list. Detection does not independently establish
    transfer between taxa.
  support: supports
  accessed_at: '2026-10-20T07:21:02.116505Z'
  quote: Metabolite profiling detected
- evidence_id: publication
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.jhazmat.2026.143606
  locator: Crossref DOI, title, article type and primary resource URL
  summary: DOI 10.1016/j.jhazmat.2026.143606 and PMID 42735627 identify the same article.
    A DOI link could be represented without inventing a dataset accession.
  support: supports
  accessed_at: '2026-10-20T07:21:02.118347Z'
  snapshot_sha256: 53d95c06ca45feeabeac158674e21d20a5de01a58b2141ca52037c96baf16bec
- evidence_id: preview
  kind: search
  reference: https://www.sciencedirect.com/science/article/pii/S0304389426025860
  locator: Publisher-index preview and direct-access attempts
  summary: Publisher preview is an excerpt, not full text. Its access notice and failed
    direct opens leave full Methods, MAG tables, supplements and source data unavailable
    to this review. No complete-source claim is made.
  support: supports
  accessed_at: '2026-10-20T07:21:53.154860Z'
  search_scope: One exact-DOI search plus direct DOI, PubMed and ScienceDirect browser
    opens; public PubMed/Crossref API metadata retrieved. No claim that no public
    copy exists elsewhere.
- evidence_id: ontology
  kind: authority
  reference: OAK local NCBITaxon, ENVO, GO and CHEBI snapshots
  locator: Eight unique curated identifier/label pairs
  summary: All labels resolve. The source wording Desulfobacterota is retained as
    preferred wording alongside canonical NCBI Thermodesulfobacteriota; this is not
    a label mismatch. Broad-rank GTDB coherence does not establish the placement of
    individual MAGs.
  support: supports
  accessed_at: '2026-10-20T07:21:53.097027Z'
  snapshot_sha256: ca35d8671780e829e813b5c411a0cca4fad99dfbbbe37b6d6169cbffe9cd91a6
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: Role, evidence and environmental-factor representation
  summary: All four taxon role lists are absent. The two environmental-factor entries
    describe observed outcomes. These are metadata distinctions, not grounds to infer
    missing biological roles.
  support: supports
  accessed_at: '2026-10-20T07:23:44.760616Z'
- evidence_id: history
  kind: record_content
  reference: history/README.md; reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
  locator: Advisory history-presence rule, inline creation event and target decision
    row
  summary: No target sidecar was located by the ignored-inclusive search. Presence
    is advisory. The prior graph decision records no change and an abstract-only assessment;
    it does not provide independent full-text verification. The failed directory command
    tested an assumed path, not malformed target history.
  support: supports
  accessed_at: '2026-10-20T07:23:44.760617Z'
- evidence_id: local-search
  kind: search
  reference: references_cache; history; reports/causal_graph_review/decisions; kb/taxa
  locator: Ignored-inclusive PMID, ID and filename search
  summary: Found the abstract cache and graph decision; no matching history sidecar
    was found in the full history tree including ignored files. Missing roles/resource/metabolite
    statements refer to the complete target.
  support: supports
  accessed_at: '2026-10-20T07:23:44.760782Z'
  search_scope: rg --no-ignore --hidden -l '42735627|CommunityMech:000386|Anaerobic_Indole_Degrading_Sludge_Consortium'
    references_cache history reports/causal_graph_review/decisions kb/taxa
  snapshot_sha256: e3fae3fd847b83e702cd4f4e766b7f2ac69403391c72bfa340995e74b96319a0
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
  locator: All 11 evidence occurrences, including native Discussion evidence
  summary: Every snippet matches the independently retrieved abstract after NFKC/whitespace
    normalization. This lexical check does not verify full Methods or prove causal
    support.
  support: supports
  accessed_at: '2026-10-20T07:23:44.760922Z'
  snapshot_sha256: d5014a1270106fef04291d007a9f3baa0a0eec37c835a29daad345cdf983a842
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
  locator: Actual execution 2026-10-20T07:19:36.986473+00:00 to 2026-10-20T07:19:38.511702+00:00
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml'
  support: supports
  accessed_at: '2026-10-20T07:19:38.511702Z'
  snapshot_sha256: 06ae48df7a88956780480658e3042825ad9cbd93b5ac227ec367b807d76f0077
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv
  locator: Actual execution 2026-10-20T07:19:36.986708+00:00 to 2026-10-20T07:19:41.828479+00:00
  summary: "uv run python scripts/validate_strict.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml\
    \ --out /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-03/000386/strict-report.tsv"
  support: supports
  accessed_at: '2026-10-20T07:19:41.828479Z'
  snapshot_sha256: c0fc70f55ad2e46fa9c272dd83c396b940535f0c7054f56f8182a8b04368b113
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
  locator: Actual execution 2026-10-20T07:19:36.986797+00:00 to 2026-10-20T07:19:40.478854+00:00
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-10-20T07:19:40.478854Z'
  snapshot_sha256: f653f32313d033c71e15683212306c235bf2e8a63d13eac547812b8acaffc551
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
  locator: Actual execution 2026-10-20T07:19:38.512175+00:00 to 2026-10-20T07:19:38.641080+00:00
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-10-20T07:19:38.641080Z'
  snapshot_sha256: 43c3d27e1a0ea050a2ede909fb1741491327b025649e21fcf3e253015b6a1897
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
  locator: Actual execution 2026-10-20T07:19:38.641364+00:00 to 2026-10-20T07:19:42.063163+00:00
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml'
  support: supports
  accessed_at: '2026-10-20T07:19:42.063163Z'
  snapshot_sha256: 9e69c8823392eb05e3afc91bd4406b77bf61381403d4b930e5ca09d7d4424f54
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Anaerobic_Indole_Degrading_Sludge_Consortium
  locator: Actual execution 2026-10-20T07:19:40.479222+00:00 to 2026-10-20T07:19:40.590226+00:00
  summary: 'validate-history: ''history/records/Anaerobic_Indole_Degrading_Sludge_Consortium''
    does not exist.

    error: recipe `validate-history` failed with exit code 2'
  support: supports
  accessed_at: '2026-10-20T07:19:40.590226Z'
  snapshot_sha256: e15964e362ef7a45ad52c6fa3b40e10a263ea79fac4bd4873849475f61993fa6
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-20T07:19:42.063832+00:00 to 2026-10-20T07:19:42.138220+00:00
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-10-20T07:19:42.138220Z'
  snapshot_sha256: 8cdf441eba47db75cf5b4063794897c083ef970edea9dce187f089c5be717ee6
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
  locator: Actual execution 2026-10-20T07:19:42.138586+00:00 to 2026-10-20T07:19:44.726351+00:00
  summary: "Validating kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-10-20T07:19:44.726351Z'
  snapshot_sha256: 09828c3b9f2f343228404e3ff06bea9cc604c8149625dc01009aff1bd2b68583
- evidence_id: check-audit-network
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  locator: Actual run finished 2026-10-20T07:08:14.467705+00:00
  summary: 'Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records,
    57 warnings in 21 records, zero errors; exit 1. Selected target has no reported
    network warning. Canonical records unchanged since execution.'
  support: supports
  accessed_at: '2026-10-20T07:08:14.467705Z'
  snapshot_sha256: e2122e512641be2226ad12ab146b2c8f7d1e153f1211745e4816457834a42667
- evidence_id: check-check-network-quality
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  locator: Actual run finished 2026-10-20T07:08:13.673449+00:00
  summary: 'Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records,
    57 warnings in 21 records, zero errors; exit 1. Selected target has no reported
    network warning. Canonical records unchanged since execution.'
  support: supports
  accessed_at: '2026-10-20T07:08:13.673449Z'
  snapshot_sha256: b0cb58371a5a771dcbd671952ee68dfe5f26169d08240b66162aa83580fb5229
assessments:
- assessment_id: identity
  area: identity
  topic: Enrichment versus defined community
  outcome: supported
  summary: The record and cited publication describe the same anaerobic sludge enrichment.
    Its four entries denote broad affiliated populations, not four isolated species,
    and the text appropriately avoids exact MAG identifiers.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - abstract
  - affiliations
  - publication
  dimensions:
  - name: source_strain
    value: No individual strain or exact MAG identifier curated
    definition: Broad affiliations are retained because exact accessioned members
      are unavailable in inspected evidence.
    evidence_ids:
    - record
    - affiliations
  - name: community_scope
    value: Laboratory-acclimated sludge enrichment
    definition: A study population is distinct from a defined isolate mixture.
    evidence_ids:
    - record
    - abstract
  - name: experimental_setting
    value: Laboratory phenotype and multi-omics study
    definition: Observed community phenotype is distinct from inferred assignment
      of functions to taxa.
    evidence_ids:
    - abstract
    - affiliations
  - name: medium
    value: No growth-media or cultivation-setup block
    definition: The existing discussion explicitly defers full Methods curation; no
      formulation is reconstructed from previews.
    evidence_ids:
    - record
    - preview
  - name: evidence_tier
    value: Independent abstract verification; incomplete full-source access
    definition: Source identity and bounded abstract support are verified, while exact
      mechanisms and data accessions remain unresolved.
    evidence_ids:
    - abstract
    - publication
    - preview
- assessment_id: taxonomy
  area: grounding
  topic: taxonomy[0..3] and GTDB classifications
  outcome: supported
  summary: All taxon labels resolve and broad source affiliations are preserved. The
    NCBI/GTDB nomenclature difference is explained. Coherence/domain gates pass at
    the encoded ranks; no conclusion about every member of a phylum or genus, or an
    exact MAG, follows.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - ontology
  - affiliations
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Candidate anaerobic indole-to-methanogenesis
    division of labor'
  outcome: supported
  summary: Candidate/inferred wording and PARTIAL computational evidence match the
    abstract’s proposed framework. The SYNTROPHY type must be read with that qualification;
    it is not proof of obligate cooperation, reciprocal benefit or measured interspecies
    flux. Full-text validation remains unresolved.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - abstract
  - affiliations
  - preview
  details: 'Participants: three bacterial phylum-level affiliations and one archaeal
    genus affiliation. Direction/mechanism: a proposed community functional relationship
    rather than identified donor/recipient pairs. Source PMID 42735627 abstract; exact
    short quote and locator in abstract. Methane/methanogenesis annotations represent
    the proposed process, not a quantitative gas measurement.'
- assessment_id: edges
  area: graph
  topic: ecological_interactions[*].downstream
  outcome: not_applicable
  summary: No downstream arrows occur in the complete target. The source’s candidate
    framework does not justify inventing an ordered pairwise network from the accessible
    abstract.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - abstract
  - history
- assessment_id: engineering
  area: scope
  topic: Engineering design and description
  outcome: supported
  summary: Study design and endpoints agree with the abstract at the stated level.
    No exact biochemical attribution, gene necessity or organism-specific benefit
    is established by the summary. The enrichment origin/category and laboratory environment
    are coherent.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - abstract
  - ontology
- assessment_id: roles
  area: completeness
  topic: taxonomy[*].functional_role
  outcome: concern
  summary: All four role lists are absent. The abstract’s candidate assignments should
    not be promoted into unqualified roles merely to fill these fields.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - schema
  - affiliations
- assessment_id: factors
  area: representation
  topic: environmental_factors[0..1]
  outcome: concern
  summary: The two entries are degradation outcomes, not independent environmental
    conditions. Their evidence can remain useful at the relevant phenotype or endpoint
    assertions.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - schema
  - abstract
- assessment_id: chemicals
  area: completeness
  topic: ecological_interactions[0].metabolites
  outcome: concern
  summary: The structured list represents substrate and proposed final product but
    omits named detected intermediates already present in the record’s endpoints.
    This is a retrieval gap, not evidence that a particular exchange step has been
    demonstrated.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - metabolites
  - ontology
- assessment_id: resources
  area: provenance
  topic: Missing external resource and dataset blocks
  outcome: concern
  summary: The known publication DOI is not represented in external_resources. No
    verified public dataset accession was obtained; absence from the accessible abstract
    is not proof that none exists. The full-text discussion correctly keeps accession/MAG
    work open.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - publication
  - preview
- assessment_id: history
  area: provenance
  topic: Inline event and advisory sidecar history
  outcome: supported
  summary: Inline creation history and a no-change graph decision are present. No
    sidecar file was found, but the repository explicitly makes presence advisory.
    Its nonexistent-directory validation failure is retained as an inapplicable attempted
    check, not a record-schema defect.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - history
  - local-search
- assessment_id: validation
  area: schema
  topic: Native gates and full-source limitations
  outcome: concern
  summary: Seven focused/preflight checks pass with unchanged caches. A separate attempted
    history command failed because the assumed sidecar directory is absent; its presence
    is advisory. Corpus warnings and unavailable full-source verification remain explicit.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-references-explained
  - check-validate-history
  - history
  - check-audit-network
  - preview
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: concern
  summary: Completeness 10 reflects an intentionally sparse abstract-grounded record.
    Quality 100 is capped despite minor findings and does not certify unavailable
    scientific detail.
  target_ids:
  - CommunityMech:000386
  evidence_ids:
  - record
  - schema
  - check-audit-network
  metrics:
  - name: completeness
    value: 10
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 if all required metadata including roles +5 environment
      +10 at least 3 factors +10 at least 3 nodes +5 external resources +10 media
      +5 datasets +5 node metabolites). 0+5+0+0+0+0+0+5=10; roles absent, two factors,
      one node, no media/resources/datasets.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50*P1-10*P2-2*P3+20*min(mean node evidence/2,1)+15 if native
      COMPLETE,0,100). P1=0,P2=0,P3=2,P4=2; 1 attached item/1 node; all four declared
      taxon groups included. clamp(100-4+10+15)=100.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native target severity count; unavailable full-source detail
      is not presumed error.
  - name: P2
    value: 0
    unit: findings
    definition: Observed native target severity count; unavailable full-source detail
      is not presumed error.
  - name: P3
    value: 2
    unit: findings
    definition: Observed native target severity count; unavailable full-source detail
      is not presumed error.
  - name: P4
    value: 2
    unit: findings
    definition: Observed native target severity count; unavailable full-source detail
      is not presumed error.
  - name: interaction_evidence
    value: 1
    unit: evidence items per interaction
    denominator: 1
    definition: One PARTIAL computational evidence item on one candidate node.
findings:
- finding_id: role-metadata
  issue_key: cm-000386-role-metadata
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded completeness or representation issue; study
    identity and cautious mechanistic qualification remain intact.'
  rule_id: review-checklist.taxonomy
  status: open
  certainty: confirmed
  title: Taxon roles are not represented
  description: All four role lists are absent. The existing source affiliations and
    candidate-function wording do not support invented definitive roles.
  target_ids:
  - CommunityMech:000386
  field_paths:
  - taxonomy[*].functional_role
  evidence_ids:
  - record
  - schema
  - affiliations
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    role: canonical_record
- finding_id: outcomes-as-factors
  issue_key: cm-000386-outcomes-as-factors
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded completeness or representation issue; study
    identity and cautious mechanistic qualification remain intact.'
  rule_id: review-checklist.environment
  status: open
  certainty: confirmed
  title: Phenotype outcomes are stored as environmental factors
  description: Both factor entries describe removal performance rather than supplied
    environmental conditions. The same outcomes are already summarized in engineering
    endpoints.
  target_ids:
  - CommunityMech:000386
  field_paths:
  - environmental_factors[0]
  - environmental_factors[1]
  evidence_ids:
  - record
  - schema
  - abstract
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    role: canonical_record
- finding_id: publication-link
  issue_key: cm-000386-publication-link
  category: completeness
  severity: informational
  native_severity: P4
  normalization_reason: 'P4 informational: optional structured enrichment; the existing
    prose/citations retain the underlying information.'
  rule_id: P4.1
  status: open
  certainty: confirmed
  title: Publication resource is not structured
  description: The record cites the paper but has no external_resources entry for
    its verified DOI/PMID.
  target_ids:
  - CommunityMech:000386
  field_paths:
  - external_resources
  evidence_ids:
  - record
  - publication
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    role: canonical_record
- finding_id: intermediate-representation
  issue_key: cm-000386-intermediate-representation
  category: completeness
  severity: informational
  native_severity: P4
  normalization_reason: 'P4 informational: optional structured enrichment; the existing
    prose/citations retain the underlying information.'
  rule_id: P4.2
  status: open
  certainty: confirmed
  title: Detected intermediates are prose-only
  description: Intermediate names occur in the endpoint list but not in the node’s
    metabolite list. Later chemical grounding must distinguish observed detection
    from hypothesized transfer.
  target_ids:
  - CommunityMech:000386
  field_paths:
  - ecological_interactions[0].metabolites
  evidence_ids:
  - record
  - metabolites
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    role: canonical_record
actions:
- action_id: fix-role-metadata
  description: Preserve unknown roles explicitly until member-specific support and
    an appropriate vocabulary term are available.
  finding_ids:
  - role-metadata
  target_ids:
  - CommunityMech:000386
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Do not infer confirmed roles from phylum/genus affiliation alone.
  - Candidate evidence remains qualified.
  - Run strict/evidence checks for later metadata edits.
- action_id: fix-outcomes-as-factors
  description: Place source-supported outcomes with phenotype/endpoints, maintaining
    the distinction from experimental conditions.
  finding_ids:
  - outcomes-as-factors
  target_ids:
  - CommunityMech:000386
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anaerobic_Indole_Degrading_Sludge_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Outcome evidence remains attached to the reported result.
  - No unreported condition or operational parameter is invented.
  - Run strict and reference checks.
limitations:
- Complete primary text, MAG tables, supplements and exact data accessions were unavailable;
  source absence is not evidence that an experiment or dataset does not exist.
- Publisher-index text was treated as preview only, not an independently inspected
  complete article. No paid access or correspondence was attempted.
- Broad lineage/GTDB mappings do not establish exact MAG identity, organism-specific
  pathway activity or measured partner exchange.
- No cultivation formulation is reconstructed from the truncated publisher preview.
- The failed history-directory attempt is retained with its actual exit code; sidecar
  absence is advisory and inline provenance is present.
- Required corpus warning results remain nonzero; full-source unavailability requires
  partial completion.
notes:
- No canonical records, caches, history or generated products changed.
- All inspected local input hashes remain unchanged; publication response hashes are
  retained.
- Short source quotations total 11 words.
- All batch-03 native commands use the new worktree via PYTHONPATH.
tags:
- record-review
- anaerobic-sludge
- batch-03
- partial-source-access
```
