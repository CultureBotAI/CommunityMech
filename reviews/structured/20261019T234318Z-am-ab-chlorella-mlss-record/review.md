# AM-AB Chlorella-MLSS consortium: source, control and completeness review

- Review: 20261019T234318Z-am-ab-chlorella-mlss-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-19T23:36:14.964665Z
- Finished UTC: 2026-10-19T23:43:18.444139Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Identity, assembly and all five recorded endpoints/conditions are supported within the primary study. One major gap is the empty functional graph; one minor gap is unrepresented full-text cultivation context. Controls preclude universal synergy claims. Focused gates pass; corpus warning failures remain explicit.

## Scope And Provenance

Entire canonical record, zero interaction nodes and arrows, both member descriptors, all conditions, cultivation, resources, discussions and history.

Selection: Seventh initially uncovered path in the declared sorted isolate/community corpus; one record per bundle. Saved only after preceding paths.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a4611c913c8da9619673df63a0c2cce3aa206a83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000444 | kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml | maintained | AM-AB Chlorella-MLSS Wastewater Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000444 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml |
| validate-terms | passed | True | CommunityMech:000444 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000444 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000444 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml |
| validate-strict | passed | True | CommunityMech:000444 | uv run python scripts/validate_strict.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml --out /private/tmp/cm-review-session/000444/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/000444/strict-report.tsv |
| validate-history | passed | True | CommunityMech:000444 | No issues found |
| normalize-cache-names | passed | True | CommunityMech:000444 | Command completed without output or reported issues. |
| validate-references-explained | passed | True | CommunityMech:000444 | Validating kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000444 | Same-session corpus result: exit 1; 462 records, 57 warnings in 21 records, zero errors. No target finding. Reused at identical base and unchanged record bytes; no new execution claimed. |
| check-network-quality | failed | True | CommunityMech:000444 | Same-session corpus result: exit 1; 462 records, 57 warnings in 21 records, zero errors. No target finding. Reused at identical base and unchanged record bytes; no new execution claimed. |
| Structured-source applicability | not_applicable | False | CommunityMech:000444 | No resolvable gene/transcriptomic source key is present. |

## Scientific And Domain Assessments

### Experimental identity and biological scope

identity: supported. Targets: CommunityMech:000444.

AM-AB denotes the combined activated C. vulgaris and MLSS treatment; it is distinct from each algae-only activation control. ENGINEERED origin and BIOREMEDIATION category fit that design. No genetic engineering is implied.

### Taxonomic resolution and roles

grounding: supported. Targets: CommunityMech:000444.

Species-level Chlorella and domain-level bacterial partner match the source’s resolution. PRIMARY_PRODUCER fits the phototrophic algal context. The MLSS entry has no functional_role, and no unmeasured bacterial function should be invented to improve a score. GTDB domain mapping is coherent but its historical 1,603,049-genome aggregate was not independently rebuilt.

### Assembly, perturbation and endpoints

evidence: supported. Targets: CommunityMech:000444.

Separate activation and subsequent mixing match Methods. Reported endpoints correspond to nitrogen/phosphate removal, BOD, biomass and kinetic fitting. Comparative claims require the algae-only controls; the design does not demonstrate a particular bacterial-to-algal transfer mechanism.

### ecological_interactions: complete zero-node, zero-arrow inventory

graph: concern. Targets: CommunityMech:000444.

The exact maintained list is empty: no interaction or arrow requires a fabricated edge assessment. Source-supported consortium performance is absent from graph products. The existing open discussion documents this substantive extension gap and correctly cautions against universal synergy or inferred substrate transfer.

### Physical and modeled environment

grounding: supported. Targets: CommunityMech:000444.

The wastewater-treatment facility class and separate waste-water material fit the outdoor HRAP study at the declared resolution. The exact wastewater source is now available in full Methods; the note about the abstract’s limited detail is accurate but leaves the maintained record incomplete.

### environmental_factors[0]: Chlorella nutrient activation

evidence: supported. Targets: CommunityMech:000444.

0.1-times commercial medium for two days matches the selected algal activation condition. Name the source medium and keep bacterial activation separate.

### environmental_factors[1]: Nitrogen removal

evidence: supported. Targets: CommunityMech:000444.

99.9% after six hours is the total-nitrogen result for AM-AB, not a universal nitrogen-species efficiency or early advantage.

### environmental_factors[2]: Phosphate removal

evidence: supported. Targets: CommunityMech:000444.

The reported two-hour endpoint is below 0.01 mg/L. Both algae-only and combined treatments reached the detection limit; this is not unique consortium superiority.

### environmental_factors[3]: Total-nitrogen specific removal rate

evidence: supported. Targets: CommunityMech:000444.

49.81 mg/g/h is a fitted maximum specific removal parameter from the stated kinetic analysis, not a measured interspecies flux.

### environmental_factors[4]: BOD reduction

evidence: supported. Targets: CommunityMech:000444.

81.73% is the combined six-hour outcome. The selected algae-only control reached 83.75%, so that endpoint does not show a universal improvement.

### growth_media[0], cultivation_setup[0] and missing full-text context

completeness: concern. Targets: CommunityMech:000444.

The recorded activation/assembly sequence is supported. Methods additionally identify NMR medium, domestic wastewater and sludge origin, algal inoculum context, bacterial activation, pond dimensions/depth/mixing and initial chemistry. These details are not represented, although the discussion recognizes their availability. Indoor stock light/temperature must not be transferred to outdoor treatment; the sludge activation vessel is not the HRAP working volume.

### Control comparisons and limitations of mechanism

evidence: supported. Targets: CommunityMech:000444.

The article and existing discussion distinguish early delay from later total-nitrogen removal. Phosphate reaches the detection limit in both treatments, BOD is not uniformly better, and biomass correlations are not significant at the stated 0.05 threshold. Hypothesized metabolite exchange remains unmeasured.

### Resources, discussion and history

provenance: supported. Targets: CommunityMech:000444.

PMID/DOI resources identify the same article. Two open discussions capture condition curation and graph extension; all anchors resolve. The historical graph-gap decision remains context, not a structured finding superseded here. No metal processing role is asserted; NOT_APPLICABLE matches scope.

### Structured gene/expression adapter applicability

evidence: not_applicable. Targets: CommunityMech:000444.

No gene, locus, protein, defined bacterial strain or transcriptomic dataset is named. General activation and removal endpoints do not supply a matching source key; no expression-module inference is used.

### Deterministic gates and source retrieval

schema: supported. Targets: CommunityMech:000444.

All focused recipes passed without ontology skips and cache bytes were unchanged. Public PMC HTML and Europe PMC metadata were retrieved; an XML endpoint failed but was not needed. Corpus gate warning failures are retained and prevent a passing verdict.

### Native metrics

completeness: concern. Targets: CommunityMech:000444.

Completeness 30 and validation quality 88 are separate from scientific support. Missing MLSS role and graph reduce presence; neither should be fabricated. The empty graph has no dangling references but does not receive the native COMPLETE bonus because neither declared participant has represented interaction participation.

## Findings

### empty-functional-graph: Functional graph omits the observed consortium performance

major / open / confirmed; issue key: cm-000444-empty-functional-graph.

The record contains no interaction node even though a source-controlled consortium treatment is documented. This leaves the biological function absent from graph exports; it is a representation gap, not proof that any specific cross-feeding mechanism occurred.

### unrepresented-full-text-conditions: Available cultivation context has not reached the maintained fields

minor / open / confirmed; issue key: cm-000444-unrepresented-full-text-conditions.

The condition discussion acknowledges full Methods, but medium/setup and wastewater notes remain mostly abstract-level. Important stage-specific source information can now be represented without estimating unreported outdoor conditions.

## Recommended Actions And Acceptance Checks

### fix-empty-functional-graph

Prepare a separately authorized source-backed graph extension limited to measured community-level effects and explicit control comparisons. Preserve uncertain mechanisms and add no unsupported arrows.

- Each proposed node names the exact combined/control context and endpoint timing.
- No unqualified faster-removal, phosphate superiority, BOD superiority or traced metabolite exchange is asserted.
- Respect the record’s separate causal-graph research workflow before applying new nodes; this review itself performs no provider call.
- Validate new representation with strict, reference and network gates after authorized curation.

### fix-unrepresented-full-text-conditions

Curate the reported source, activation, inoculation, pond and starting-chemistry details into their proper stage-specific fields; keep genuinely unreported outdoor values unresolved.

- Separate stock culture, bacterial activation and mixed wastewater treatment.
- Do not transfer indoor temperature/light or activation-reactor volume to the outdoor pond.
- Attach exact Methods/Table locators and validate schema, terms and references.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml; Entire canonical record; two taxonomic descriptors, zero interaction nodes/arrows, five environmental factors, medium/setup/resources/discussions/history | supports | The record is a defined experimental assembly of activated Chlorella and a taxonomically unresolved activated sludge partner. Results remain in descriptive/condition fields while the functional graph is empty. |
| paper | https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/; PMID:42429207; DOI:10.1002/wer.70489; complete public article Introduction, Methods 2.1-2.9, Results 3.1-3.4, Tables 1-4, captions and Conclusion; snapshot hashes fetched HTML bytes | supports | Full primary text confirms the assembled culture and reported treatment endpoints. Tables distinguish algae-only controls, treatment timing and measured results from proposed mechanisms. |
| methods | https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/; Methods 2.4-2.5 | supports | The source identifies wastewater/sludge origin and separates algal activation, bacterial activation and mixed treatment. |
| assembly | https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/; Methods 2.5 | supports | The source specifies the initial microalgae:bacteria dry-mass mixing ratio; this is not a taxonomic abundance estimate. |
| controls | https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/; Results 3.2, nitrogen comparison | supports | Early nitrogen removal does not support universal synergy; the later endpoint must be compared at its actual time. |
| detection | https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/; Table 3 footnote | supports | Phosphate removal is a detection-limit endpoint, not proof of zero residual concentration. |
| model | https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/; Methods 2.7 | supports | Maximum specific removal rate and affinity are fitted kinetic parameters, not direct causal-transfer measurements. |
| identity-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A42429207%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Europe PMC core response result for EXT_ID:42429207, MED; PMID/PMCID/DOI/title/authors/journal | supports | Public metadata confirms the source identifiers and July 2026 Water Environment Research article. Failed browser/Europe PMC full-text attempts did not prevent ordinary public PMC HTML retrieval. |
| history | history/records/AM_AB_Chlorella_MLSS_Wastewater_Consortium; All three events and target row of reports/causal_graph_review/decisions/20261008-six-records-batch124.yaml | supports | Creation, environment repair and later graph-gap review are documented. The open discussion already recognizes full Methods availability and confines any future graph extension to controlled evidence. No issue-tracker status was checked. |
| search | PMID:42429207; doi:10.1002/wer.70489; AM_AB_Chlorella_MLSS_Wastewater_Consortium; Ignored-inclusive local source/history/decision search | context_only | The source cache contains the complete PubMed record plus one explicitly labeled primary excerpt; a full article was fetched separately. No undocumented local source absence is inferred. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity, TaxonomicComposition, CommunityEngineeringDesign, GrowthMedium and CultivationSetup | supports | The schema separates biological member resolution, engineered assembly, cultivation and interaction representation. An unresolved bacterial consortium must not be replaced by invented species. |
| check-validate | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml; Actual command output | context_only | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml |
| check-validate-terms | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-terms kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml; Actual command output | context_only | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-gtdb kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml; Actual command output | context_only | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-gtdb-domain kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml; Actual command output | context_only | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml |
| check-validate-strict | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-strict kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml --out /private/tmp/cm-review-session/000444/strict-report.tsv; Actual command output | context_only | uv run python scripts/validate_strict.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml --out /private/tmp/cm-review-session/000444/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/000444/strict-report.tsv |
| check-validate-history | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-history history/records/AM_AB_Chlorella_MLSS_Wastewater_Consortium; Actual command output | context_only | No issues found |
| check-normalize-cache-names | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true uv run python scripts/normalize_cache_names.py --check; Actual command output | context_only | Command completed without output or reported issues. |
| check-validate-references-explained | UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true JUST_NO_DOTENV=true just --no-dotenv validate-references-explained kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml; Actual command output | context_only | Validating kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | just --no-dotenv audit-network; Complete corpus log | context_only | Same-session corpus result: exit 1; 462 records, 57 warnings in 21 records, zero errors. No target finding. Reused at identical base and unchanged record bytes; no new execution claimed. |
| check-check-network-quality | just --no-dotenv check-network-quality; Complete corpus log | context_only | Same-session corpus result: exit 1; 462 records, 57 warnings in 21 records, zero errors. No target finding. Reused at identical base and unchanged record bytes; no new execution claimed. |

## Limits And Additional Notes

- No new causal node, arrow, condition or history event was added. Full text supports bounded outcomes; proposed mechanistic transfer remains unmeasured.
- Supplementary datasets and raw data were not independently reanalyzed; fitted kinetic parameters and statistical claims are reported at publication scope. Source numerical inconsistencies outside curated endpoints were not reconciled into new claims.
- Historical GTDB aggregate counts were not rebuilt. Public source retrieval improved accessible evidence without converting an abstract limitation into an invented protocol.
- Required corpus network checks fail on other-record warnings. The target itself passes focused gates; an empty graph is not certified complete by their silence.
- This reviewer did not author or change the record in this session; historical curation shares the codex identity, so person-level independence is unknown.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T234318Z-am-ab-chlorella-mlss-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'AM-AB Chlorella-MLSS consortium: source, control and completeness review'
started_at: '2026-10-19T23:36:14.964665Z'
finished_at: '2026-10-19T23:43:18.444139Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: This reviewer did not author or change the record in this session;
    historical curation shares the codex identity, so person-level independence is
    unknown.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Identity, assembly and all five recorded endpoints/conditions are supported
  within the primary study. One major gap is the empty functional graph; one minor
  gap is unrepresented full-text cultivation context. Controls preclude universal
  synergy claims. Focused gates pass; corpus warning failures remain explicit.
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
  - path: history/records/AM_AB_Chlorella_MLSS_Wastewater_Consortium/2026-09-27T012549Z-codex-42429207.yaml
    sha256: ee96c1f97632c5194015aea1b73b3a4b4b0135408aac2627439ba8518611608b
    role: context
  - path: history/records/AM_AB_Chlorella_MLSS_Wastewater_Consortium/2026-09-27T013247Z-codex-1130.yaml
    sha256: c158c39ea32a16bcd5ae18f88487a2c0d01e9f9a036a7acedd342a780fcd8720
    role: context
  - path: history/records/AM_AB_Chlorella_MLSS_Wastewater_Consortium/2026-10-08T175132Z-codex-665b31.yaml
    sha256: b38ec278e3b3a85d8ee7ca0d2b3f30dfe7cdf074fd2efad716e2fcf236bc7541
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    sha256: f3a69684e81df00ca791bfc61832141ad9048270f4b3ed476328b772d07604d2
    role: target
  - path: references_cache/PMID_42429207.txt
    sha256: eb80e76d862305f4031055915eb45a832b8f32de2d0bfe042eb9142c314f4c7a
    role: context
  - path: reports/causal_graph_review/decisions/20261008-six-records-batch124.yaml
    sha256: ac925b5b57d1e2d173d9e515d8b371b300b885f3fc06c473570ddce7e3a07c87
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
- target_id: CommunityMech:000444
  path: kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  label: AM-AB Chlorella-MLSS Wastewater Consortium
  record_class: MicrobialCommunity
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    role: canonical_record
scope:
  description: Entire canonical record, zero interaction nodes and arrows, both member
    descriptors, all conditions, cultivation, resources, discussions and history.
  selection: Seventh initially uncovered path in the declared sorted isolate/community
    corpus; one record per bundle. Saved only after preceding paths.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000444
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  locator: Entire canonical record; two taxonomic descriptors, zero interaction nodes/arrows,
    five environmental factors, medium/setup/resources/discussions/history
  summary: The record is a defined experimental assembly of activated Chlorella and
    a taxonomically unresolved activated sludge partner. Results remain in descriptive/condition
    fields while the functional graph is empty.
  support: supports
  accessed_at: '2026-10-19T23:40:38.139525Z'
- evidence_id: paper
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/
  locator: PMID:42429207; DOI:10.1002/wer.70489; complete public article Introduction,
    Methods 2.1-2.9, Results 3.1-3.4, Tables 1-4, captions and Conclusion; snapshot
    hashes fetched HTML bytes
  summary: Full primary text confirms the assembled culture and reported treatment
    endpoints. Tables distinguish algae-only controls, treatment timing and measured
    results from proposed mechanisms.
  support: supports
  accessed_at: '2026-10-19T23:36:48.787845Z'
  snapshot_sha256: 04e2d5135ffe3ef63e61df67f1c0db82928ee3898a862eb17ac9374bbba96a52
- evidence_id: methods
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/
  locator: Methods 2.4-2.5
  summary: The source identifies wastewater/sludge origin and separates algal activation,
    bacterial activation and mixed treatment.
  support: supports
  accessed_at: '2026-10-19T23:36:48.787845Z'
  quote: Raw domestic wastewater
- evidence_id: assembly
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/
  locator: Methods 2.5
  summary: The source specifies the initial microalgae:bacteria dry-mass mixing ratio;
    this is not a taxonomic abundance estimate.
  support: supports
  accessed_at: '2026-10-19T23:36:48.787845Z'
  quote: 3.84:1
- evidence_id: controls
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/
  locator: Results 3.2, nitrogen comparison
  summary: Early nitrogen removal does not support universal synergy; the later endpoint
    must be compared at its actual time.
  support: supports
  accessed_at: '2026-10-19T23:36:48.787845Z'
  quote: delayed the removal of nitrogen
- evidence_id: detection
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/
  locator: Table 3 footnote
  summary: Phosphate removal is a detection-limit endpoint, not proof of zero residual
    concentration.
  support: supports
  accessed_at: '2026-10-19T23:36:48.787845Z'
  quote: below the analytical detection level
- evidence_id: model
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13352569/
  locator: Methods 2.7
  summary: Maximum specific removal rate and affinity are fitted kinetic parameters,
    not direct causal-transfer measurements.
  support: supports
  accessed_at: '2026-10-19T23:36:48.787845Z'
  quote: Lineweaver–Burk linearization
- evidence_id: identity-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A42429207%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Europe PMC core response result for EXT_ID:42429207, MED; PMID/PMCID/DOI/title/authors/journal
  summary: Public metadata confirms the source identifiers and July 2026 Water Environment
    Research article. Failed browser/Europe PMC full-text attempts did not prevent
    ordinary public PMC HTML retrieval.
  support: supports
  accessed_at: '2026-10-19T23:36:48.788231Z'
  snapshot_sha256: 1ff09935a8a5371ce87d56dfcdad001f5b685e763e30bf97dfc1a073b305a6af
- evidence_id: history
  kind: record_content
  reference: history/records/AM_AB_Chlorella_MLSS_Wastewater_Consortium
  locator: All three events and target row of reports/causal_graph_review/decisions/20261008-six-records-batch124.yaml
  summary: Creation, environment repair and later graph-gap review are documented.
    The open discussion already recognizes full Methods availability and confines
    any future graph extension to controlled evidence. No issue-tracker status was
    checked.
  support: supports
  accessed_at: '2026-10-19T23:40:38.140096Z'
- evidence_id: search
  kind: search
  reference: PMID:42429207; doi:10.1002/wer.70489; AM_AB_Chlorella_MLSS_Wastewater_Consortium
  locator: Ignored-inclusive local source/history/decision search
  summary: The source cache contains the complete PubMed record plus one explicitly
    labeled primary excerpt; a full article was fetched separately. No undocumented
    local source absence is inferred.
  support: context_only
  accessed_at: '2026-10-19T23:40:38.140098Z'
  search_scope: rg --no-ignore --hidden searched references_cache, reports/causal_graph_review/decisions
    and the exact history directory for PMID, DOI suffix and slug, including ignored
    files. Full target inspection establishes its empty interaction list and unpopulated
    optional fields.
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity, TaxonomicComposition, CommunityEngineeringDesign, GrowthMedium
    and CultivationSetup
  summary: The schema separates biological member resolution, engineered assembly,
    cultivation and interaction representation. An unresolved bacterial consortium
    must not be replaced by invented species.
  support: supports
  accessed_at: '2026-10-19T23:40:38.140099Z'
- evidence_id: check-validate
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  locator: Actual command output
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml'
  support: context_only
  accessed_at: '2026-10-19T23:36:41.424959Z'
  snapshot_sha256: 2a41fc04ddb76b78dae0e857278b0d1f88ccff6387c9febccb3306fefaa33f11
- evidence_id: check-validate-terms
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-terms kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  locator: Actual command output
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: context_only
  accessed_at: '2026-10-19T23:36:42.438562Z'
  snapshot_sha256: ea8f28b3ba7a9b5cba284ca1db3387545812a130390438a786fe98c97b6de663
- evidence_id: check-validate-gtdb
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  locator: Actual command output
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: context_only
  accessed_at: '2026-10-19T23:36:40.615055Z'
  snapshot_sha256: df576d5b1947fb0ad82c0d631d762078bf64db9413a727ae1359089253f550e8
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb-domain kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  locator: Actual command output
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml'
  support: context_only
  accessed_at: '2026-10-19T23:36:42.347672Z'
  snapshot_sha256: 23ae8dce68472312046e1503c5a83a21c09203822991ca51ad58dea98fef904c
- evidence_id: check-validate-strict
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-strict kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    --out /private/tmp/cm-review-session/000444/strict-report.tsv
  locator: Actual command output
  summary: "uv run python scripts/validate_strict.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml\
    \ --out /private/tmp/cm-review-session/000444/strict-report.tsv\nValidating 1\
    \ files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/000444/strict-report.tsv"
  support: context_only
  accessed_at: '2026-10-19T23:36:43.730879Z'
  snapshot_sha256: cef46df5feea3c79719848f60381662014b9184baa9ca8286b694d6d161e5d8c
- evidence_id: check-validate-history
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-history history/records/AM_AB_Chlorella_MLSS_Wastewater_Consortium
  locator: Actual command output
  summary: No issues found
  support: context_only
  accessed_at: '2026-10-19T23:36:43.273131Z'
  snapshot_sha256: 56eb08ed8a389fe218ac63b890c5ff665015f5bc81c6308689173f7bcc20072c
- evidence_id: check-normalize-cache-names
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true uv run python scripts/normalize_cache_names.py --check
  locator: Actual command output
  summary: Command completed without output or reported issues.
  support: context_only
  accessed_at: '2026-10-19T23:36:43.788843Z'
  snapshot_sha256: d96841bf53defcb98eb90dbc11bc513438f9230a26aeff3b13e658cc66b4e61f
- evidence_id: check-validate-references-explained
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-references-explained kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  locator: Actual command output
  summary: "Validating kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: context_only
  accessed_at: '2026-10-19T23:36:45.642826Z'
  snapshot_sha256: f9ec8e2ad13b2adca5a11d4997458a6115930c2a2d05ddaf90f82e89443da921
- evidence_id: check-audit-network
  kind: validation
  reference: just --no-dotenv audit-network
  locator: Complete corpus log
  summary: 'Same-session corpus result: exit 1; 462 records, 57 warnings in 21 records,
    zero errors. No target finding. Reused at identical base and unchanged record
    bytes; no new execution claimed.'
  support: context_only
  accessed_at: '2026-10-19T07:30:27.845593Z'
  snapshot_sha256: bedf3fd18a964bda429f7c6b5feb01b8918e1440b48a4329664501161c80e3f4
- evidence_id: check-check-network-quality
  kind: validation
  reference: just --no-dotenv check-network-quality
  locator: Complete corpus log
  summary: 'Same-session corpus result: exit 1; 462 records, 57 warnings in 21 records,
    zero errors. No target finding. Reused at identical base and unchanged record
    bytes; no new execution claimed.'
  support: context_only
  accessed_at: '2026-10-19T07:30:43.193891Z'
  snapshot_sha256: 885e62e84ed8d3e69a6e5ef5be43f941ef64d756107c3b062846831f76e081aa
assessments:
- assessment_id: identity
  area: identity
  topic: Experimental identity and biological scope
  outcome: supported
  summary: AM-AB denotes the combined activated C. vulgaris and MLSS treatment; it
    is distinct from each algae-only activation control. ENGINEERED origin and BIOREMEDIATION
    category fit that design. No genetic engineering is implied.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - paper
  - identity-metadata
  dimensions:
  - name: source_strain
    value: C. vulgaris from Madras Christian College algal collection; no strain accession
      reported
    definition: Species identity is supported; no strain code was invented.
    evidence_ids:
    - methods
    - paper
  - name: taxon_rank
    value: NCBITaxon:3077 species and NCBITaxon:2 bacterial domain
    definition: MLSS composition remains unresolved below domain; the green alga has
      no GTDB equivalent.
    evidence_ids:
    - record
    - paper
  - name: community_scope
    value: Activated microalga plus activated mixed bacterial sludge
    definition: A mixed partner is not a single resolved bacterial species.
    evidence_ids:
    - assembly
    - paper
  - name: experimental_setting
    value: Outdoor pilot HRAP treating domestic wastewater
    definition: Indoor stock culture and bacterial activation are separate stages.
    evidence_ids:
    - methods
    - paper
  - name: medium
    value: NMR activation medium and raw domestic wastewater treatment matrix
    definition: Source-available context should be added with stage-specific provenance.
    evidence_ids:
    - methods
  - name: biomass_state
    value: Living activated cultures; dry-mass measurements after treatment
    definition: Final biomass and theoretical downstream methane estimates are distinct.
    evidence_ids:
    - paper
  - name: source_category
    value: Full primary experimental article with controls and fitted kinetics
    definition: Introduction hypotheses are not measured metabolite transfer.
    evidence_ids:
    - paper
    - model
- assessment_id: taxonomy
  area: grounding
  topic: Taxonomic resolution and roles
  outcome: supported
  summary: Species-level Chlorella and domain-level bacterial partner match the source’s
    resolution. PRIMARY_PRODUCER fits the phototrophic algal context. The MLSS entry
    has no functional_role, and no unmeasured bacterial function should be invented
    to improve a score. GTDB domain mapping is coherent but its historical 1,603,049-genome
    aggregate was not independently rebuilt.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - paper
  - schema
- assessment_id: engineering
  area: evidence
  topic: Assembly, perturbation and endpoints
  outcome: supported
  summary: Separate activation and subsequent mixing match Methods. Reported endpoints
    correspond to nitrogen/phosphate removal, BOD, biomass and kinetic fitting. Comparative
    claims require the algae-only controls; the design does not demonstrate a particular
    bacterial-to-algal transfer mechanism.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - assembly
  - controls
  - model
- assessment_id: graph
  area: graph
  topic: 'ecological_interactions: complete zero-node, zero-arrow inventory'
  outcome: concern
  summary: 'The exact maintained list is empty: no interaction or arrow requires a
    fabricated edge assessment. Source-supported consortium performance is absent
    from graph products. The existing open discussion documents this substantive extension
    gap and correctly cautions against universal synergy or inferred substrate transfer.'
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - paper
  - controls
  - history
- assessment_id: environment
  area: grounding
  topic: Physical and modeled environment
  outcome: supported
  summary: The wastewater-treatment facility class and separate waste-water material
    fit the outdoor HRAP study at the declared resolution. The exact wastewater source
    is now available in full Methods; the note about the abstract’s limited detail
    is accurate but leaves the maintained record incomplete.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - methods
  - paper
- assessment_id: factor-0
  area: evidence
  topic: 'environmental_factors[0]: Chlorella nutrient activation'
  outcome: supported
  summary: 0.1-times commercial medium for two days matches the selected algal activation
    condition. Name the source medium and keep bacterial activation separate.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - methods
  - paper
- assessment_id: factor-1
  area: evidence
  topic: 'environmental_factors[1]: Nitrogen removal'
  outcome: supported
  summary: 99.9% after six hours is the total-nitrogen result for AM-AB, not a universal
    nitrogen-species efficiency or early advantage.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - paper
  - controls
- assessment_id: factor-2
  area: evidence
  topic: 'environmental_factors[2]: Phosphate removal'
  outcome: supported
  summary: The reported two-hour endpoint is below 0.01 mg/L. Both algae-only and
    combined treatments reached the detection limit; this is not unique consortium
    superiority.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - paper
  - detection
- assessment_id: factor-3
  area: evidence
  topic: 'environmental_factors[3]: Total-nitrogen specific removal rate'
  outcome: supported
  summary: 49.81 mg/g/h is a fitted maximum specific removal parameter from the stated
    kinetic analysis, not a measured interspecies flux.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - paper
  - model
- assessment_id: factor-4
  area: evidence
  topic: 'environmental_factors[4]: BOD reduction'
  outcome: supported
  summary: 81.73% is the combined six-hour outcome. The selected algae-only control
    reached 83.75%, so that endpoint does not show a universal improvement.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - paper
  - controls
- assessment_id: cultivation
  area: completeness
  topic: growth_media[0], cultivation_setup[0] and missing full-text context
  outcome: concern
  summary: The recorded activation/assembly sequence is supported. Methods additionally
    identify NMR medium, domestic wastewater and sludge origin, algal inoculum context,
    bacterial activation, pond dimensions/depth/mixing and initial chemistry. These
    details are not represented, although the discussion recognizes their availability.
    Indoor stock light/temperature must not be transferred to outdoor treatment; the
    sludge activation vessel is not the HRAP working volume.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - methods
  - assembly
  - paper
  - history
- assessment_id: controls
  area: evidence
  topic: Control comparisons and limitations of mechanism
  outcome: supported
  summary: The article and existing discussion distinguish early delay from later
    total-nitrogen removal. Phosphate reaches the detection limit in both treatments,
    BOD is not uniformly better, and biomass correlations are not significant at the
    stated 0.05 threshold. Hypothesized metabolite exchange remains unmeasured.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - controls
  - paper
- assessment_id: resources
  area: provenance
  topic: Resources, discussion and history
  outcome: supported
  summary: PMID/DOI resources identify the same article. Two open discussions capture
    condition curation and graph extension; all anchors resolve. The historical graph-gap
    decision remains context, not a structured finding superseded here. No metal processing
    role is asserted; NOT_APPLICABLE matches scope.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - identity-metadata
  - history
- assessment_id: adapters
  area: evidence
  topic: Structured gene/expression adapter applicability
  outcome: not_applicable
  summary: No gene, locus, protein, defined bacterial strain or transcriptomic dataset
    is named. General activation and removal endpoints do not supply a matching source
    key; no expression-module inference is used.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - paper
- assessment_id: validation
  area: schema
  topic: Deterministic gates and source retrieval
  outcome: supported
  summary: All focused recipes passed without ontology skips and cache bytes were
    unchanged. Public PMC HTML and Europe PMC metadata were retrieved; an XML endpoint
    failed but was not needed. Corpus gate warning failures are retained and prevent
    a passing verdict.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - identity-metadata
  - paper
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-references-explained
  - check-validate-history
- assessment_id: scores
  area: completeness
  topic: Native metrics
  outcome: concern
  summary: Completeness 30 and validation quality 88 are separate from scientific
    support. Missing MLSS role and graph reduce presence; neither should be fabricated.
    The empty graph has no dangling references but does not receive the native COMPLETE
    bonus because neither declared participant has represented interaction participation.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
  - check-audit-network
  metrics:
  - name: completeness
    value: 30
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including taxonomy with roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 interactions + 5 resources + 10 growth_media
      + 5 datasets + 5 any metabolites). Required block = 0 because MLSS functional_role
      is absent; 0 + 5 + 10 + 0 + 5 + 10 + 0 + 0 = 30.
  - name: validation_quality
    value: 88
    unit: points
    minimum: 0
    maximum: 100
    definition: 'clamp(100 - 50*P1 - 10*P2 - 2*P3 + 20*min(mean interaction evidence/2,
      1) + 15 if COMPLETE network, 0, 100). P1=0, P2=1, P3=1. Zero interactions: mean
      evidence is treated as 0 solely for scoring, not a measured ratio. No COMPLETE
      participation bonus for an empty graph. 100 - 10 - 2 = 88.'
  - name: P1
    value: 0
    unit: findings
    definition: Target blocker count.
  - name: P2
    value: 1
    unit: findings
    definition: Target major count.
  - name: P3
    value: 1
    unit: findings
    definition: Target minor count.
  - name: interaction_evidence
    value: 0
    unit: evidence items
    definition: Zero evidence items attached to zero interactions; no biological mean
      is defined. Score uses 0 by explicit convention.
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml'
  target_ids:
  - CommunityMech:000444
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history; cache-name normalization checks the corpus without
    mutation.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000444
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-terms kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history; cache-name normalization checks the corpus without
    mutation.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000444
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history; cache-name normalization checks the corpus without
    mutation.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml'
  target_ids:
  - CommunityMech:000444
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-gtdb-domain kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history; cache-name normalization checks the corpus without
    mutation.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml\
    \ --out /private/tmp/cm-review-session/000444/strict-report.tsv\nValidating 1\
    \ files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/000444/strict-report.tsv"
  target_ids:
  - CommunityMech:000444
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-strict kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    --out /private/tmp/cm-review-session/000444/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history; cache-name normalization checks the corpus without
    mutation.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: No issues found
  target_ids:
  - CommunityMech:000444
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-history history/records/AM_AB_Chlorella_MLSS_Wastewater_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history; cache-name normalization checks the corpus without
    mutation.
- check_id: normalize-cache-names
  name: normalize-cache-names
  status: passed
  required: true
  summary: Command completed without output or reported issues.
  target_ids:
  - CommunityMech:000444
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names
  scope_note: Focused target/history; cache-name normalization checks the corpus without
    mutation.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: "Validating kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000444
  command: UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true
    JUST_NO_DOTENV=true just --no-dotenv validate-references-explained kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history; cache-name normalization checks the corpus without
    mutation.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Same-session corpus result: exit 1; 462 records, 57 warnings in 21 records,
    zero errors. No target finding. Reused at identical base and unchanged record
    bytes; no new execution claimed.'
  target_ids:
  - CommunityMech:000444
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Native auditor does not require a nonempty graph; absence of a target
    warning does not certify functional coverage.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Same-session corpus result: exit 1; 462 records, 57 warnings in 21 records,
    zero errors. No target finding. Reused at identical base and unchanged record
    bytes; no new execution claimed.'
  target_ids:
  - CommunityMech:000444
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Native auditor does not require a nonempty graph; absence of a target
    warning does not certify functional coverage.
- check_id: source-adapter-applicability
  name: Structured-source applicability
  status: not_applicable
  required: false
  summary: No resolvable gene/transcriptomic source key is present.
  target_ids:
  - CommunityMech:000444
  evidence_ids:
  - record
findings:
- finding_id: empty-functional-graph
  issue_key: cm-000444-empty-functional-graph
  category: completeness
  severity: major
  native_severity: P2
  rule_id: P2.3
  normalization_reason: 'P2 major: the entire functional graph is absent despite source-supported
    consortium outcomes.'
  status: open
  certainty: confirmed
  title: Functional graph omits the observed consortium performance
  description: The record contains no interaction node even though a source-controlled
    consortium treatment is documented. This leaves the biological function absent
    from graph exports; it is a representation gap, not proof that any specific cross-feeding
    mechanism occurred.
  target_ids:
  - CommunityMech:000444
  field_paths:
  - ecological_interactions
  evidence_ids:
  - record
  - paper
  - controls
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    role: canonical_record
- finding_id: unrepresented-full-text-conditions
  issue_key: cm-000444-unrepresented-full-text-conditions
  category: completeness
  severity: minor
  native_severity: P3
  rule_id: docs/record-review-profile.md:cultivation
  normalization_reason: 'P3 minor: supported identity and outcomes are retained, but
    source-available cultivation context is not represented.'
  status: open
  certainty: confirmed
  title: Available cultivation context has not reached the maintained fields
  description: The condition discussion acknowledges full Methods, but medium/setup
    and wastewater notes remain mostly abstract-level. Important stage-specific source
    information can now be represented without estimating unreported outdoor conditions.
  target_ids:
  - CommunityMech:000444
  field_paths:
  - modeled_environment[0].notes
  - growth_media[0]
  - cultivation_setup[0]
  - environmental_factors[0]
  evidence_ids:
  - record
  - methods
  - assembly
  - paper
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    role: canonical_record
actions:
- action_id: fix-empty-functional-graph
  description: Prepare a separately authorized source-backed graph extension limited
    to measured community-level effects and explicit control comparisons. Preserve
    uncertain mechanisms and add no unsupported arrows.
  finding_ids:
  - empty-functional-graph
  target_ids:
  - CommunityMech:000444
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Each proposed node names the exact combined/control context and endpoint timing.
  - No unqualified faster-removal, phosphate superiority, BOD superiority or traced
    metabolite exchange is asserted.
  - Respect the record’s separate causal-graph research workflow before applying new
    nodes; this review itself performs no provider call.
  - Validate new representation with strict, reference and network gates after authorized
    curation.
- action_id: fix-unrepresented-full-text-conditions
  description: Curate the reported source, activation, inoculation, pond and starting-chemistry
    details into their proper stage-specific fields; keep genuinely unreported outdoor
    values unresolved.
  finding_ids:
  - unrepresented-full-text-conditions
  target_ids:
  - CommunityMech:000444
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Separate stock culture, bacterial activation and mixed wastewater treatment.
  - Do not transfer indoor temperature/light or activation-reactor volume to the outdoor
    pond.
  - Attach exact Methods/Table locators and validate schema, terms and references.
limitations:
- No new causal node, arrow, condition or history event was added. Full text supports
  bounded outcomes; proposed mechanistic transfer remains unmeasured.
- Supplementary datasets and raw data were not independently reanalyzed; fitted kinetic
  parameters and statistical claims are reported at publication scope. Source numerical
  inconsistencies outside curated endpoints were not reconciled into new claims.
- Historical GTDB aggregate counts were not rebuilt. Public source retrieval improved
  accessible evidence without converting an abstract limitation into an invented protocol.
- Required corpus network checks fail on other-record warnings. The target itself
  passes focused gates; an empty graph is not certified complete by their silence.
- This reviewer did not author or change the record in this session; historical curation
  shares the codex identity, so person-level independence is unknown.
tags:
- record-review
- wastewater
- consortium
- batch-01
```
