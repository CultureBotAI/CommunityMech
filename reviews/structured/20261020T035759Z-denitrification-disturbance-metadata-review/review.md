# Disturbance-stable denitrification record: bounded provenance review

- Review: 20261020T035759Z-denitrification-disturbance-metadata-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-20T03:55:46.603290Z
- Finished UTC: 2026-10-20T03:57:59.962044Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Citation identity, member names, ontology labels and structural gates were checked. One major finding concerns generic evidence reused for specific claims; two minor findings concern publication-resource and design-factor metadata. Mechanistic nodes/edges and operational details were not scientifically reviewed or refined.

## Scope And Provenance

Entire target read; identity/provenance, source matching, metadata placement and deterministic validation only. This is not a full scientific review.

Selection: Fifth uncovered path in batch 02; baseline plus validated pending batch-01 coverage.
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a4611c913c8da9619673df63a0c2cce3aa206a83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000116 | kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml | maintained | Aerobic Denitrification Disturbance-Stable SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000116 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml |
| validate-strict | passed | True | CommunityMech:000116 | uv run python scripts/validate_strict.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml --out /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000116 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000116 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000116 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml |
| validate-history | passed | True | CommunityMech:000116 | No issues found |
| normalize-cache-names-check | passed | True | CommunityMech:000116 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000116 | Validating kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000116 | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| check-network-quality | failed | True | CommunityMech:000116 | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| Mechanistic and operational source review | skipped | True | CommunityMech:000116 | Not performed: pathogen stress-tolerance mechanisms, antibiotic-response interventions and cultivation refinement are excluded. Source inspection is limited to metadata, identity and evidence placement. |
| Mechanism-oriented expression adapter | not_applicable | False | CommunityMech:000116 | No expression-module inference was pursued because mechanistic refinement is excluded from this bounded review. |

## Scientific And Domain Assessments

### Defined community and source strain labels

identity: supported. Targets: CommunityMech:000116.

The primary abstract names the same three species. Species-level ontology IDs are appropriate for the species labels; strain labels present in prose should remain distinguishable from species IDs. The source describes a synthetic community, not a naturally co-occurring field assemblage.

### Taxonomy and environment labels

grounding: supported. Targets: CommunityMech:000116.

NCBI species labels and laboratory-environment label agree with authority snapshots. GTDB coherence/domain validators pass. Stored historical genome counts and crosswalk provenance were not reconstructed.

### engineering_design.evidence and taxonomy[*].evidence

evidence: concern. Targets: CommunityMech:000116.

The repeated introductory sentence is source-authentic but does not identify specific organisms or establish their functional roles. Membership can be checked against another part of the same abstract. Role claims must remain unverified where claim-specific support is absent; no replacement functional mechanism is supplied.

### ecological_interactions[0]

graph: unknown. Targets: CommunityMech:000116.

This node was inventoried, including its participant references and source citation. Its stress-response mechanism, performance contribution and proposed refinements are outside the assessed scope. Structural validation is not scientific endorsement.

All listed participants are declared taxon descriptors. No new mechanistic statement, experimental condition or source-derived optimization is supplied.

### ecological_interactions[1]

graph: unknown. Targets: CommunityMech:000116.

This node was inventoried, including its participant references and source citation. Its stress-response mechanism, performance contribution and proposed refinements are outside the assessed scope. Structural validation is not scientific endorsement.

All listed participants are declared taxon descriptors. No new mechanistic statement, experimental condition or source-derived optimization is supplied.

### ecological_interactions[2]

graph: unknown. Targets: CommunityMech:000116.

This node was inventoried, including its participant references and source citation. Its stress-response mechanism, performance contribution and proposed refinements are outside the assessed scope. Structural validation is not scientific endorsement.

All listed participants are declared taxon descriptors. No new mechanistic statement, experimental condition or source-derived optimization is supplied.

### ecological_interactions[0].downstream[0]

graph: unknown. Targets: CommunityMech:000116.

The existing arrow targets a declared node. Its causal direction and mechanistic support were not adjudicated in this bounded review. Prior PARTIAL qualifications remain unchanged.

Exact path retained for auditability; no mediator-to-performance mapping is refined or endorsed.

### ecological_interactions[1].downstream[0]

graph: unknown. Targets: CommunityMech:000116.

The existing arrow targets a declared node. Its causal direction and mechanistic support were not adjudicated in this bounded review. Prior PARTIAL qualifications remain unchanged.

Exact path retained for auditability; no mediator-to-performance mapping is refined or endorsed.

### environmental_factors[0]

scope: concern. Targets: CommunityMech:000116.

This entry primarily repeats community design instead of a distinct environmental factor. That is a metadata-placement issue; this review does not expand the perturbation or exposure description.

### Publication and missing resource block

provenance: concern. Targets: CommunityMech:000116.

PMID and DOI identity are verified, but no structured external publication resource exists in the entire target. Adding a bibliographic entry would improve identifier resolution without changing scientific claims.

### growth_media, related_ingredients, mechanism descriptions and discussion

scope: unknown. Targets: CommunityMech:000116.

Cultivation, resistance/stress optimization, pathway-specific explanations and proposed intervention follow-up were not assessed or refined. Full-text source review was not performed. This limits completion and prevents a passing scientific verdict.

### Focused gates and structural references

schema: supported. Targets: CommunityMech:000116.

All eight focused/preflight checks pass; caches remain unchanged. Both arrows resolve to a declared node and all three taxa participate in the graph. No inference about stress-response effectiveness follows from these gates. Corpus network warnings remain failed outside this target.

### Native presence and observed-finding scores

completeness: concern. Targets: CommunityMech:000116.

Completeness 80 is a presence score. Capped quality 100 is based only on the assessed metadata findings and cannot certify excluded biological claims.

## Findings

### generic-evidence: Generic motivation is reused as member- and role-specific evidence

major / open / confirmed; issue key: cm-000116-generic-evidence.

The same introductory statement supports assembly, all three taxon entries and the design factor. It discusses why the topic matters rather than identifying the members or demonstrating their roles. Abstract membership is independently verifiable, but the attached evidence is not claim-specific.

### publication-resource: The verified publication lacks a structured resource entry

minor / open / confirmed; issue key: cm-000116-publication-resource.

References use the PMID, but external_resources is absent from the entire record. The DOI is verified from PubMed and Europe PMC.

### design-factor: Community design is stored as an environmental factor

minor / open / confirmed; issue key: cm-000116-design-factor.

environmental_factors[0] repeats the assembly description and generic evidence. Its label denotes study design rather than a specific environmental property.

## Recommended Actions And Acceptance Checks

### fix-generic-evidence

Separate bibliographic motivation from member-identification evidence, and mark unsupported role annotations as unresolved without adding mechanistic recommendations.

- Membership evidence identifies the stated species/strain labels.
- Generic motivation is not presented as role validation.
- Do not introduce stress-tolerance or antibiotic-response optimization.
- Run strict and reference checks after authorized metadata curation.

### fix-publication-resource

Add a bibliographic resource entry with the verified citation identifiers during authorized metadata curation.

- PMID/DOI identify the same article.
- Do not imply full-text inspection where only metadata/abstract were verified.
- Run strict and reference checks.

### fix-design-factor

Keep design metadata distinguishable from environmental metadata without expanding operational details.

- No duplication is needed to preserve community membership.
- The field label matches the information represented.
- Run strict validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml; Entire record read; bounded identity/provenance assessment; three taxa, three nodes, two arrows | supports | The maintained record describes a synthetic three-member community. This review inventories the graph but does not verify or refine pathogen stress-tolerance mechanisms, antibiotic-response interventions, cultivation methods or mediator-specific effects. |
| publication | PMID:40020349; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=40020349&amp;retmode=xml; article identity, abstract membership and introductory context | supports | PMID 40020349 resolves to the 2025 Water Research article with DOI 10.1016/j.watres.2025.123270. Its abstract explicitly names the three species and the two provided strain labels. The generic introductory sentence reused in the record does not itself establish those details. |
| intro | PMID:40020349; Abstract opening sentence | supports | This is a general motivation statement, not a member-specific observation. |
| access | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40020349&amp;format=json&amp;resultType=core; Europe PMC core metadata | supports | Article identity agrees with PubMed. Metadata report no PMCID and no open-access full text. No full article or supplements were inspected. |
| ontology | OAK local NCBITaxon and ENVO snapshots; Taxon and environment identifier lookup | supports | Species IDs 287, 470 and 644 and laboratory-environment ID resolve to the stated labels. Native term checking also passes, but semantic mechanisms and chemical pathway interpretation are outside this review. |
| schema | src/communitymech/schema/communitymech.yaml; EvidenceItem, taxon roles and external-resource representation | supports | A generic study-motivation snippet cannot serve as direct support for every attached membership or role claim. Valid syntax and identifier correspondence do not establish biological roles. |
| snippets | kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml; All 13 EvidenceItem occurrences, including repeated aliases | supports | All snippets match the PubMed abstract after NFKC and whitespace normalization. Lexical matches are not independent scientific validation of mechanisms or intervention effects. |
| history | history/records/Aerobic_Denitrification_Disturbance_SynCom; Three whole history events | supports | History retains qualified causal claims and removes unsupported categorical labels. A later append-only correction identifies the original actor; no history mutation is needed. This review does not promote prior mechanistic judgments. |
| local-search | references_cache; history/records; reports/causal_graph_review/decisions; kb/taxa; Ignored-inclusive identifier/slug search | supports | Located the source abstract and history/decision records. The entire target lacks external_resources and associated_datasets. No external dataset-absence claim is made. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml; Actual execution 2026-10-20T03:55:47.283760+00:00 to 2026-10-20T03:55:47.923328+00:00 | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml --out /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv; Actual execution 2026-10-20T03:55:47.283913+00:00 to 2026-10-20T03:55:49.179316+00:00 | supports | uv run python scripts/validate_strict.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml --out /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml; Actual execution 2026-10-20T03:55:47.283980+00:00 to 2026-10-20T03:55:49.184530+00:00 | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml; Actual execution 2026-10-20T03:55:47.923565+00:00 to 2026-10-20T03:55:47.997246+00:00 | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml; Actual execution 2026-10-20T03:55:47.997594+00:00 to 2026-10-20T03:55:49.233606+00:00 | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-history history/records/Aerobic_Denitrification_Disturbance_SynCom; Actual execution 2026-10-20T03:55:49.179595+00:00 to 2026-10-20T03:55:49.832619+00:00 | supports | No issues found |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-20T03:55:49.833088+00:00 to 2026-10-20T03:55:49.908644+00:00 | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml; Actual execution 2026-10-20T03:55:49.908864+00:00 to 2026-10-20T03:55:50.829263+00:00 | supports | Validating kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | just --no-dotenv audit-network; Actual run finished 2026-10-19T07:30:27.845593+00:00 | supports | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |
| check-check-network-quality | just --no-dotenv check-network-quality; Actual run finished 2026-10-19T07:30:43.193891+00:00 | supports | Reused complete corpus result at identical freshly fetched base and unchanged canonical corpus: exit 1; 462 records, 57 warnings in 21 records, zero errors. Target has no finding. No new execution is claimed. |

## Limits And Additional Notes

- Partial non-operational provenance review: no scientific endorsement of the mechanistic graph or stress-response claims.
- Full text, supplements and raw datasets were not inspected. Only primary abstract/metadata were used for identity and evidence placement.
- No expression-module inference, cultivation refinement, mediator-specific optimization or intervention guidance was supplied.
- Historical GTDB mapping aggregate counts were not reconstructed. Native coherence/domain gates pass.
- Required corpus network checks retain unrelated warning failures; the required mechanistic source review was intentionally skipped and is explicit.
- No canonical records, caches, histories or generated products changed.
- All inspected local input hashes are unchanged.
- Saved target coverage does not mean full scientific completion; completion=partial and scientific_review=false preserve that distinction.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T035759Z-denitrification-disturbance-metadata-review
kind: record
repository: CultureBotAI/CommunityMech
title: 'Disturbance-stable denitrification record: bounded provenance review'
started_at: '2026-10-20T03:55:46.603290Z'
finished_at: '2026-10-20T03:57:59.962044Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: No target edited this session; historical codex curation prevents
    person-level independence claim.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: Citation identity, member names, ontology labels and structural gates were
  checked. One major finding concerns generic evidence reused for specific claims;
  two minor findings concern publication-resource and design-factor metadata. Mechanistic
  nodes/edges and operational details were not scientifically reviewed or refined.
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
  - path: history/records/Aerobic_Denitrification_Disturbance_SynCom/2026-10-05T035546Z-claude-code-5feed8.yaml
    sha256: 977e8df6f8a2e2e965054c808b0b3545d9517a284ca61d760503e6f761fbf166
    role: context
  - path: history/records/Aerobic_Denitrification_Disturbance_SynCom/2026-10-05T035647Z-codex-1b36e6.yaml
    sha256: a82881d09aaca5f20408e93f506e688c8208378a1002883a79dc8d6e5376ac11
    role: context
  - path: history/records/Aerobic_Denitrification_Disturbance_SynCom/2026-10-05T040913Z-codex-f8fc9e.yaml
    sha256: e62874964195a97561578306d0dc19e03ca9ab93002fb1b00be367679a6b3bdc
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    sha256: c9cefea6036c2e4564079cfa0950e49c2282eff63dfe120835adb0c92fbbdbb0
    role: target
  - path: references_cache/PMID_40020349.txt
    sha256: ca2c553fe150cfa6d60c5c27666a269ce134b026e9fb23509e6b276a319e6643
    role: context
  - path: reports/causal_graph_review/decisions/20261004-four-records.yaml
    sha256: 78e90ab701090461d09df57d1fbc348e97676e4d96197f26f58fbe0427845f32
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
- target_id: CommunityMech:000116
  path: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
  label: Aerobic Denitrification Disturbance-Stable SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    role: canonical_record
scope:
  description: Entire target read; identity/provenance, source matching, metadata
    placement and deterministic validation only. This is not a full scientific review.
  selection: Fifth uncovered path in batch 02; baseline plus validated pending batch-01
    coverage.
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000116
  exclusions:
  - target: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml#ecological_interactions;related_ingredients;growth_media;discussions
    reason: Mechanistic causal adjudication, pathogen stress-tolerance/antibiotic-response
      optimization and cultivation/intervention details are excluded. Nodes and arrows
      are inventoried but scientifically unassessed.
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml'
  target_ids:
  - CommunityMech:000116
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
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
  summary: "uv run python scripts/validate_strict.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml\
    \ --out /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv"
  target_ids:
  - CommunityMech:000116
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv
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

    uv run linkml-term-validator validate-data kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000116
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
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
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000116
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
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

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml'
  target_ids:
  - CommunityMech:000116
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
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
  - CommunityMech:000116
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-history history/records/Aerobic_Denitrification_Disturbance_SynCom
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
  - CommunityMech:000116
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
  summary: "Validating kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000116
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
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
  - CommunityMech:000116
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
  - CommunityMech:000116
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Corpus-wide warnings outside selected target, retained as actual required
    failures.
- check_id: mechanistic-source-review
  name: Mechanistic and operational source review
  status: skipped
  required: true
  summary: 'Not performed: pathogen stress-tolerance mechanisms, antibiotic-response
    interventions and cultivation refinement are excluded. Source inspection is limited
    to metadata, identity and evidence placement.'
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - publication
- check_id: structured-expression-adapter
  name: Mechanism-oriented expression adapter
  status: not_applicable
  required: false
  summary: No expression-module inference was pursued because mechanistic refinement
    is excluded from this bounded review.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
  locator: Entire record read; bounded identity/provenance assessment; three taxa,
    three nodes, two arrows
  summary: The maintained record describes a synthetic three-member community. This
    review inventories the graph but does not verify or refine pathogen stress-tolerance
    mechanisms, antibiotic-response interventions, cultivation methods or mediator-specific
    effects.
  support: supports
  accessed_at: '2026-10-20T03:57:59.958344Z'
- evidence_id: publication
  kind: primary_source
  reference: PMID:40020349
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=40020349&retmode=xml;
    article identity, abstract membership and introductory context
  summary: PMID 40020349 resolves to the 2025 Water Research article with DOI 10.1016/j.watres.2025.123270.
    Its abstract explicitly names the three species and the two provided strain labels.
    The generic introductory sentence reused in the record does not itself establish
    those details.
  support: supports
  accessed_at: '2026-10-20T03:56:03.302855Z'
  snapshot_sha256: da0bdd2c7b4883bce5c4f567d7773f10acd0dc083d53db5d4a535cf104752d9c
- evidence_id: intro
  kind: primary_source
  reference: PMID:40020349
  locator: Abstract opening sentence
  summary: This is a general motivation statement, not a member-specific observation.
  support: supports
  accessed_at: '2026-10-20T03:56:03.302855Z'
  quote: Understanding how synthetic microbial community (SMC) respond to environmental
    disturbances
- evidence_id: access
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40020349&format=json&resultType=core
  locator: Europe PMC core metadata
  summary: Article identity agrees with PubMed. Metadata report no PMCID and no open-access
    full text. No full article or supplements were inspected.
  support: supports
  accessed_at: '2026-10-20T03:56:03.303175Z'
  snapshot_sha256: 3f9cdf124c61c098162f476e42af0aeb57970ed0f7bb8d198cab8307856b10d8
- evidence_id: ontology
  kind: authority
  reference: OAK local NCBITaxon and ENVO snapshots
  locator: Taxon and environment identifier lookup
  summary: Species IDs 287, 470 and 644 and laboratory-environment ID resolve to the
    stated labels. Native term checking also passes, but semantic mechanisms and chemical
    pathway interpretation are outside this review.
  support: supports
  accessed_at: '2026-10-20T03:56:37.011413Z'
  snapshot_sha256: 57847ae87b55cbda0174d1d96db844e7f1e226f91439d4fcda56a6339c20e425
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: EvidenceItem, taxon roles and external-resource representation
  summary: A generic study-motivation snippet cannot serve as direct support for every
    attached membership or role claim. Valid syntax and identifier correspondence
    do not establish biological roles.
  support: supports
  accessed_at: '2026-10-20T03:57:59.958754Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
  locator: All 13 EvidenceItem occurrences, including repeated aliases
  summary: All snippets match the PubMed abstract after NFKC and whitespace normalization.
    Lexical matches are not independent scientific validation of mechanisms or intervention
    effects.
  support: supports
  accessed_at: '2026-10-20T03:57:59.958897Z'
  snapshot_sha256: 25a95ff782f48782baad78c27d2deccea6187808b92d9ab595bbc273838c211d
- evidence_id: history
  kind: record_content
  reference: history/records/Aerobic_Denitrification_Disturbance_SynCom
  locator: Three whole history events
  summary: History retains qualified causal claims and removes unsupported categorical
    labels. A later append-only correction identifies the original actor; no history
    mutation is needed. This review does not promote prior mechanistic judgments.
  support: supports
  accessed_at: '2026-10-20T03:57:59.958903Z'
- evidence_id: local-search
  kind: search
  reference: references_cache; history/records; reports/causal_graph_review/decisions;
    kb/taxa
  locator: Ignored-inclusive identifier/slug search
  summary: Located the source abstract and history/decision records. The entire target
    lacks external_resources and associated_datasets. No external dataset-absence
    claim is made.
  support: supports
  accessed_at: '2026-10-20T03:57:59.959109Z'
  search_scope: rg --no-ignore --hidden -l '40020349|Aerobic_Denitrification_Disturbance_SynCom'
    references_cache history/records reports/causal_graph_review/decisions kb/taxa
  snapshot_sha256: e83507583047b160685396dfec59219270cc594bd6d8886f6797e3cbfc934947
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
  locator: Actual execution 2026-10-20T03:55:47.283760+00:00 to 2026-10-20T03:55:47.923328+00:00
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml'
  support: supports
  accessed_at: '2026-10-20T03:55:47.923328Z'
  snapshot_sha256: 649cea37474bf3b5e524d154ad9053154c31dd524599b8238e7206564ef09bbf
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv
  locator: Actual execution 2026-10-20T03:55:47.283913+00:00 to 2026-10-20T03:55:49.179316+00:00
  summary: "uv run python scripts/validate_strict.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml\
    \ --out /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-02/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-02/000116/strict-report.tsv"
  support: supports
  accessed_at: '2026-10-20T03:55:49.179316Z'
  snapshot_sha256: fca780233b22eed75856d4cd090684045f64180301304e0835d49d020721f532
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
  locator: Actual execution 2026-10-20T03:55:47.283980+00:00 to 2026-10-20T03:55:49.184530+00:00
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-10-20T03:55:49.184530Z'
  snapshot_sha256: 8bb0495744d7e14dc905bc561f41631e873897e5b23acb0189aaac0ec0240bfd
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
  locator: Actual execution 2026-10-20T03:55:47.923565+00:00 to 2026-10-20T03:55:47.997246+00:00
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-10-20T03:55:47.997246Z'
  snapshot_sha256: 34141e7c39769b94e64eaf46acb6a62020c997847a467e8e8d50c93962dd00a8
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
  locator: Actual execution 2026-10-20T03:55:47.997594+00:00 to 2026-10-20T03:55:49.233606+00:00
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml'
  support: supports
  accessed_at: '2026-10-20T03:55:49.233606Z'
  snapshot_sha256: 4845a8309357d865f9b5dbee46ad6cb00036390bcb1712d2d8fcdb0376535bac
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-history history/records/Aerobic_Denitrification_Disturbance_SynCom
  locator: Actual execution 2026-10-20T03:55:49.179595+00:00 to 2026-10-20T03:55:49.832619+00:00
  summary: No issues found
  support: supports
  accessed_at: '2026-10-20T03:55:49.832619Z'
  snapshot_sha256: 59814eb84aceb913810423a572ab45e6cdf15ff41226e4132379a4bc80daff96
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-20T03:55:49.833088+00:00 to 2026-10-20T03:55:49.908644+00:00
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-10-20T03:55:49.908644Z'
  snapshot_sha256: 0149bfaba7c99370d08a03c2c411f81863d49f5817b7bd5bd2c94c6c571f2ddc
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
  locator: Actual execution 2026-10-20T03:55:49.908864+00:00 to 2026-10-20T03:55:50.829263+00:00
  summary: "Validating kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-10-20T03:55:50.829263Z'
  snapshot_sha256: db63586747508fbd55dd0e44c61283b2c4e60741d26f0eb532c16b3141d6eb88
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
  topic: Defined community and source strain labels
  outcome: supported
  summary: The primary abstract names the same three species. Species-level ontology
    IDs are appropriate for the species labels; strain labels present in prose should
    remain distinguishable from species IDs. The source describes a synthetic community,
    not a naturally co-occurring field assemblage.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - publication
  - ontology
  dimensions:
  - name: community_scope
    value: Synthetic three-member community
    definition: Defined source assemblage; does not imply environmental co-occurrence
      or field safety.
    evidence_ids:
    - publication
  - name: source_strain
    value: Two source strain labels and one species-only member
    definition: No new genome or strain accession was inferred.
    evidence_ids:
    - publication
    - record
  - name: experimental_setting
    value: Laboratory study
    definition: No reactor hardware, method optimization or application protocol is
      assessed.
    evidence_ids:
    - record
  - name: medium_context
    value: Unspecified source-medium record
    definition: Composition and cultivation parameters are excluded from this review.
    evidence_ids:
    - record
- assessment_id: identifiers
  area: grounding
  topic: Taxonomy and environment labels
  outcome: supported
  summary: NCBI species labels and laboratory-environment label agree with authority
    snapshots. GTDB coherence/domain validators pass. Stored historical genome counts
    and crosswalk provenance were not reconstructed.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - ontology
- assessment_id: evidence
  area: evidence
  topic: engineering_design.evidence and taxonomy[*].evidence
  outcome: concern
  summary: The repeated introductory sentence is source-authentic but does not identify
    specific organisms or establish their functional roles. Membership can be checked
    against another part of the same abstract. Role claims must remain unverified
    where claim-specific support is absent; no replacement functional mechanism is
    supplied.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - publication
  - intro
  - schema
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: unknown
  summary: This node was inventoried, including its participant references and source
    citation. Its stress-response mechanism, performance contribution and proposed
    refinements are outside the assessed scope. Structural validation is not scientific
    endorsement.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - snippets
  details: All listed participants are declared taxon descriptors. No new mechanistic
    statement, experimental condition or source-derived optimization is supplied.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: unknown
  summary: This node was inventoried, including its participant references and source
    citation. Its stress-response mechanism, performance contribution and proposed
    refinements are outside the assessed scope. Structural validation is not scientific
    endorsement.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - snippets
  details: All listed participants are declared taxon descriptors. No new mechanistic
    statement, experimental condition or source-derived optimization is supplied.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: unknown
  summary: This node was inventoried, including its participant references and source
    citation. Its stress-response mechanism, performance contribution and proposed
    refinements are outside the assessed scope. Structural validation is not scientific
    endorsement.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - snippets
  details: All listed participants are declared taxon descriptors. No new mechanistic
    statement, experimental condition or source-derived optimization is supplied.
- assessment_id: edge-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: unknown
  summary: The existing arrow targets a declared node. Its causal direction and mechanistic
    support were not adjudicated in this bounded review. Prior PARTIAL qualifications
    remain unchanged.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - history
  details: Exact path retained for auditability; no mediator-to-performance mapping
    is refined or endorsed.
- assessment_id: edge-1
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: unknown
  summary: The existing arrow targets a declared node. Its causal direction and mechanistic
    support were not adjudicated in this bounded review. Prior PARTIAL qualifications
    remain unchanged.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - history
  details: Exact path retained for auditability; no mediator-to-performance mapping
    is refined or endorsed.
- assessment_id: environment
  area: scope
  topic: environmental_factors[0]
  outcome: concern
  summary: This entry primarily repeats community design instead of a distinct environmental
    factor. That is a metadata-placement issue; this review does not expand the perturbation
    or exposure description.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - schema
- assessment_id: resources
  area: provenance
  topic: Publication and missing resource block
  outcome: concern
  summary: PMID and DOI identity are verified, but no structured external publication
    resource exists in the entire target. Adding a bibliographic entry would improve
    identifier resolution without changing scientific claims.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - publication
  - access
- assessment_id: limitations
  area: scope
  topic: growth_media, related_ingredients, mechanism descriptions and discussion
  outcome: unknown
  summary: Cultivation, resistance/stress optimization, pathway-specific explanations
    and proposed intervention follow-up were not assessed or refined. Full-text source
    review was not performed. This limits completion and prevents a passing scientific
    verdict.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - access
- assessment_id: validation
  area: schema
  topic: Focused gates and structural references
  outcome: supported
  summary: All eight focused/preflight checks pass; caches remain unchanged. Both
    arrows resolve to a declared node and all three taxa participate in the graph.
    No inference about stress-response effectiveness follows from these gates. Corpus
    network warnings remain failed outside this target.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-references-explained
  - check-audit-network
- assessment_id: metrics
  area: completeness
  topic: Native presence and observed-finding scores
  outcome: concern
  summary: Completeness 80 is a presence score. Capped quality 100 is based only on
    the assessed metadata findings and cannot certify excluded biological claims.
  target_ids:
  - CommunityMech:000116
  evidence_ids:
  - record
  - schema
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata including roles +5 environment +10 at
      least 3 factors +10 at least 3 nodes +5 external resources +10 media +5 datasets
      +5 node metabolites). 50+5+0+10+0+10+0+5=80; placeholder media count as presence
      only.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50*P1-10*P2-2*P3+20*min(mean node evidence/2,1)+15 if native
      network COMPLETE,0,100). Observed P1=0,P2=1,P3=2; 3 items/3 nodes; participants
      and references intact. clamp(100-10-4+10+15)=100. Excluded scientific claims
      are unscored, not approved.
  - name: P1
    value: 0
    unit: findings
    definition: Observed bounded-review findings only.
  - name: P2
    value: 1
    unit: findings
    definition: Observed bounded-review findings only.
  - name: P3
    value: 2
    unit: findings
    definition: Observed bounded-review findings only.
  - name: interaction_evidence
    value: 1
    unit: evidence items per interaction
    denominator: 3
    definition: Three directly attached snippets across three nodes; all one source.
      Lexical evidence count only.
findings:
- finding_id: generic-evidence
  issue_key: cm-000116-generic-evidence
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material claim-level evidence attribution defect.'
  rule_id: CLAUDE.claim-level-evidence
  status: open
  certainty: confirmed
  title: Generic motivation is reused as member- and role-specific evidence
  description: The same introductory statement supports assembly, all three taxon
    entries and the design factor. It discusses why the topic matters rather than
    identifying the members or demonstrating their roles. Abstract membership is independently
    verifiable, but the attached evidence is not claim-specific.
  target_ids:
  - CommunityMech:000116
  field_paths:
  - engineering_design.evidence[0]
  - taxonomy[0].evidence[0]
  - taxonomy[1].evidence[0]
  - taxonomy[2].evidence[0]
  - environmental_factors[0].evidence[0]
  evidence_ids:
  - record
  - publication
  - intro
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    role: canonical_record
- finding_id: publication-resource
  issue_key: cm-000116-publication-resource
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: missing structured linkage or metabolite representation;
    prose retains the supported process.'
  rule_id: review-checklist.external-resources
  status: open
  certainty: confirmed
  title: The verified publication lacks a structured resource entry
  description: References use the PMID, but external_resources is absent from the
    entire record. The DOI is verified from PubMed and Europe PMC.
  target_ids:
  - CommunityMech:000116
  field_paths:
  - external_resources
  evidence_ids:
  - record
  - publication
  - access
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    role: canonical_record
- finding_id: design-factor
  issue_key: cm-000116-design-factor
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: missing structured linkage or metabolite representation;
    prose retains the supported process.'
  rule_id: review-checklist.environment
  status: open
  certainty: confirmed
  title: Community design is stored as an environmental factor
  description: environmental_factors[0] repeats the assembly description and generic
    evidence. Its label denotes study design rather than a specific environmental
    property.
  target_ids:
  - CommunityMech:000116
  field_paths:
  - environmental_factors[0]
  evidence_ids:
  - record
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    role: canonical_record
actions:
- action_id: fix-generic-evidence
  description: Separate bibliographic motivation from member-identification evidence,
    and mark unsupported role annotations as unresolved without adding mechanistic
    recommendations.
  finding_ids:
  - generic-evidence
  target_ids:
  - CommunityMech:000116
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Membership evidence identifies the stated species/strain labels.
  - Generic motivation is not presented as role validation.
  - Do not introduce stress-tolerance or antibiotic-response optimization.
  - Run strict and reference checks after authorized metadata curation.
- action_id: fix-publication-resource
  description: Add a bibliographic resource entry with the verified citation identifiers
    during authorized metadata curation.
  finding_ids:
  - publication-resource
  target_ids:
  - CommunityMech:000116
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - PMID/DOI identify the same article.
  - Do not imply full-text inspection where only metadata/abstract were verified.
  - Run strict and reference checks.
- action_id: fix-design-factor
  description: Keep design metadata distinguishable from environmental metadata without
    expanding operational details.
  finding_ids:
  - design-factor
  target_ids:
  - CommunityMech:000116
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aerobic_Denitrification_Disturbance_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - No duplication is needed to preserve community membership.
  - The field label matches the information represented.
  - Run strict validation.
limitations:
- 'Partial non-operational provenance review: no scientific endorsement of the mechanistic
  graph or stress-response claims.'
- Full text, supplements and raw datasets were not inspected. Only primary abstract/metadata
  were used for identity and evidence placement.
- No expression-module inference, cultivation refinement, mediator-specific optimization
  or intervention guidance was supplied.
- Historical GTDB mapping aggregate counts were not reconstructed. Native coherence/domain
  gates pass.
- Required corpus network checks retain unrelated warning failures; the required mechanistic
  source review was intentionally skipped and is explicit.
notes:
- No canonical records, caches, histories or generated products changed.
- All inspected local input hashes are unchanged.
- Saved target coverage does not mean full scientific completion; completion=partial
  and scientific_review=false preserve that distinction.
tags:
- record-review
- bounded-provenance
- batch-02
```
