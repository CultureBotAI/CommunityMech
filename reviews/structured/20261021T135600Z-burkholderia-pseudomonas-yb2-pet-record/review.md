# Burkholderia–Pseudomonas YB2 PET consortium record review

- Review: 20261021T135600Z-burkholderia-pseudomonas-yb2-pet-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T13:51:07.411402Z
- Finished UTC: 2026-10-21T13:56:00.062251Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Direct abstract evidence supports YB2 membership, relative functional differences, measured degradation endpoints and the two-node/one-PARTIAL-arrow graph. One major finding concerns the unqualified G1B recipient role; two minor findings concern outcomes stored as conditions and composition stored as inoculum amount. Full main, figures and SI remain unavailable through inspected routes.

## Scope And Provenance

Entire record, each node and the single arrow assessed against direct abstract/title, schema/ontology, history and bounded source-access/resource evidence.

Selection: Only released CommunityMech:000426 in the owned batch 08 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000426 | kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml | maintained | Burkholderia-Pseudomonas YB2 PET Degradation Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000426 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000426 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000426 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000426 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000426 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000426 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000426 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000426 | Reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000426 | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000426 | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| Primary bibliographic identity | passed | True | CommunityMech:000426 | Exact PMID, DOI, title and directly retrieved complete abstract agree. |
| Full main and critical supplemental verification | unavailable | True | CommunityMech:000426 | Main Methods/Results, figures and SI remain uninspected; direct access attempts returned errors or metadata only. |
| Medium and archive correspondence | not_applicable | False | CommunityMech:000426 | No exact recipe or archive accession established at direct abstract scope; no guessed link or omission finding. |
| Optional structured source adapter | unavailable | False | CommunityMech:000426 | No task-runtime adapter or relevant expression-module dataset established; discovery reuse is explicit. |

## Scientific And Domain Assessments

### Defined two-strain YB2 scope

identity: supported. Targets: CommunityMech:000426.

Retain B. cepacia ZY1 and P. harudinis G1B, SYNTHETIC origin, ENGINEERED state and BIOREMEDIATION category.

### taxonomy[0].functional_role and taxonomy[1].functional_role

evidence: concern. Targets: CommunityMech:000426.

ZY1 PRIMARY_DEGRADER is supported, while the unqualified G1B CROSS_FEEDER assignment exceeds demonstrated recipient evidence.

Greater growth in externally supplied hydrolysis products supports substrate-use capability, not their provenance from ZY1. Retain source-proposed cross-feeding/complementarity as a hypothesis with local PARTIAL evidence if represented, or omit the unsupported categorical role. This does not assert that cross-feeding is absent or require a particular tracer assay to retain a hypothesis. Both strains have overlapping functions; relative strengths do not imply exclusivity.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000426.

Retain the COMMUNITY_LEVEL complementarity node without imposing a stronger interaction type.

Its PARTIAL evidence and explicit exclusions correctly distinguish relative activity/growth differences from demonstrated resource partitioning, reciprocal benefit and donor-resolved exchange. Mainly cell-associated hydrolysis does not justify inventing a secreted-enzyme mechanism.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000426.

Retain the PARTIAL complementarity→enhanced film-loss explanation at the source hypothesis level.

The abstract proposes potential complementarity alongside enhanced consortium performance. It does not isolate necessary mediation or trace transfer, and the existing arrow already states those limits. No obligatory-dependence requirement or extra edge is added.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000426.

Retain the measured PET-film loss and physical/chemical alteration node.

The three-day film result is separate from two-day BHET/MHET and five-day TPA endpoints. The record correctly rejects interpreting mass loss as mineralization or proof of niche partitioning. Significance is source-reported against individual strains; no inaccessible figure or statistical reanalysis is claimed.

### environmental_factors[1] and [2]

representation: concern. Targets: CommunityMech:000426.

Film mass loss and product conversion are responses, not environmental conditions.

Keep the numerical results with outcome/process claims; pH and temperature can remain actual conditions. The starting ratio in environmental_factors[0] is an assembly parameter already captured in engineering_design and can be consolidated during this bounded cleanup without a separate finding.

### growth_media[0] inoculum and assay scope

representation: concern. Targets: CommunityMech:000426.

The 4:5 composition ratio is not the initial cell density or transfer amount required by inoculum_size.

Preserve 4:5 in assembly/composition notes and leave inoculum amount unresolved unless Methods supplies it. The source explicitly attaches pH 7.0 and 30 C to the PET-film assay; narrow the medium title/notes to that verified scope rather than implying every product assay shares those conditions. This is not a finding that the actual product-assay conditions differ. No specific basal recipe, agitation, vessel or culture volume is inferred.

### Chemical terms, related ingredients and GO process

grounding: supported. Targets: CommunityMech:000426.

Current PET, BHET, TPA, EG and broad xenobiotic-process annotations fit the stated abstract claims.

EG release/decline is retained without promoting possible utilization to measured assimilation. No acid/anion error is inferred solely from pH or nomenclature. MHET enrichment is optional and should distinguish neutral acid from anion if adopted; no full mineralization, enzyme identity or molecular flux is added.

### Publication, source access and unresolved datasets

provenance: supported. Targets: CommunityMech:000426.

The existing resource identifies the focal publication; unavailable main/SI prevents a complete resource or protocol assessment.

No exact sequence archive, strain-catalogue accession or recipe link is verified in the abstract. Do not infer its absence from the paper or add an omission finding. Indexed publisher snippets remain leads requiring direct primary verification.

### Prior repair and evidence matching

provenance: supported. Targets: CommunityMech:000426.

The two qualified nodes and PARTIAL arrow preserve the prior graph repair and current discussion.

Issue 1265 is freshly verified closed with no comments; its scope separates graph repair from non-graph follow-up. Issue 1268 is assessed through explicitly timestamped same-session receipt reuse. All 18 current excerpts match direct abstract/title, without extending that result to inaccessible full text.

### Native gates and authority labels

schema: supported. Targets: CommunityMech:000426.

Eight native checks and all eight ontology pairs pass; semantic and access limitations remain.

### Mechanical completeness and quality

completeness: supported. Targets: CommunityMech:000426.

Native scores do not certify the uninspected main/SI or resolve semantic overstatement.

## Findings

### recipient-role: Qualify the G1B recipient role as proposed complementarity

major / open / confirmed; issue key: cm-000426-recipient-role.

taxonomy[1].functional_role asserts CROSS_FEEDER without the uncertainty already preserved in the graph. Its local growth evidence concerns supplied BHET/MHET media and supports downstream substrate-use capacity; it does not establish that the utilized material came from ZY1.

### outcome-placement: Move degradation outcomes out of environmental conditions

minor / open / confirmed; issue key: cm-000426-outcome-placement.

environmental_factors[1] and [2] encode film mass loss and BHET/MHET conversion. These measured outcomes remain supported but are not environmental conditions; pH and temperature embedded in the first outcome are genuine assay conditions.

### inoculum-amount: Separate starting composition from inoculum amount

minor / open / confirmed; issue key: cm-000426-inoculum-amount.

growth_media[0].inoculum_size and inoculum_unit encode 4:5 ZY1:G1B. This specifies starting composition rather than initial density or transfer percentage. The medium title also combines assays for which the abstract only explicitly supplies PET-film pH/temperature.

## Recommended Actions And Acceptance Checks

### qualify-recipient-role

Align the G1B taxonomy role with the source-proposed complementarity and locally supported growth phenotype.

- Either retain CROSS_FEEDER only with explicit proposed/partial support and a local note distinguishing supplied-substrate growth from donor-resolved uptake, or omit the categorical role and retain the directly supported phenotype. Do not declare cross-feeding disproven.
- Use the source conclusion for potential complementarity and preserve overlapping functions. Neither greater substrate growth nor stable relative proportions establishes reciprocal benefit, obligatory dependence or transfer necessity.
- Retain ZY1 PRIMARY_DEGRADER, both exact source strains, current compatible taxon/chemical IDs and unresolved GTDB status. Preserve the two nodes and one PARTIAL downstream explanation. No particular tracer assay is a prerequisite for representing the source hypothesis.

### relocate-outcomes

Retain supported degradation results in endpoint/process context and reserve environmental fields for actual conditions.

- Preserve 4.30% ± 0.11% PET-film mass loss after 3 days, 96.4% BHET and 97.3% MHET conversion after 2 days, and the separate nearly complete TPA use after 5 days. Keep reported significance restricted to the film-loss comparison.
- Place pH 7.0 and 30 C as film-assay conditions; move response values out of environmental_factors[1] and [2]. Consolidate the starting ratio under engineering_design or composition notes as appropriate.
- Do not relabel polymer alteration as complete mineralization, or EG decline as demonstrated assimilation. No new node or arrow is needed to relocate supported outcomes.

### repair-inoculum-and-assay-scope

Represent 4:5 as composition, leave total inoculum unresolved and scope cultivation fields to direct evidence.

- Remove 4:5 from inoculum_size/inoculum_unit as an amount and preserve it as the source-defined ZY1:G1B starting ratio. Do not invent cell density, OD, transfer percentage or CFU.
- Narrow the medium name and notes so pH 7.0 and 30 C are explicitly verified for the three-day PET-film assay; retain the two-day product and five-day TPA endpoints separately. Do not assert their conditions differ.
- Resolve formulation, vessel, agitation, working volume and other assay conditions only from directly inspected main/SI. Indexed MSM/sole-carbon fragments remain leads, with no guessed CultureMech link or dataset omission.
- After separately authorized curation, run focused schema, strict, term, reference and history checks; preserve the existing qualified graph and record any new direct-source scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml; Entire record, two interaction nodes and one downstream link | supports | The graph explicitly separates relative functional differences and proposed complementarity from measured PET-film loss. The unqualified G1B role and several non-graph field placements remain inconsistent with that scope. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42664909&amp;retmode=xml; Article-level metadata and available abstract | supports | The complete direct abstract and exact title identify PMID:42664909 and DOI 10.1016/j.jenvman.2026.130823. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42664909%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article-level metadata and available abstract | supports | Matching abstract and access metadata report no PMCID and subscription access; this is not a global public-copy search. |
| crossref | https://api.crossref.org/works/10.1016/j.jenvman.2026.130823; Article-level metadata and available abstract | supports | Direct DOI metadata agrees with the focal article identity. |
| membership | PMID:42664909; Abstract: strain comparison and assembly sentence | supports | The study compared B. cepacia ZY1 and P. harudinis G1B and assembled YB2 at a ZY1:G1B ratio of 4:5. That ratio identifies starting composition, not total cell density or transfer amount. |
| functions | PMID:42664909; Abstract: relative strain activities and concluding interpretation | supports | ZY1 had stronger PET-depolymerization-related activity; G1B grew better in supplied BHET/MHET media, with a trend toward faster BHET conversion. The authors describe overlapping functions and potential complementarity, not demonstrated donor-specific uptake. |
| localization | PMID:42664909; Abstract: hydrolytic activity and cocultivation sentence | supports | Both strains had mainly cell-associated hydrolytic activities and remained culturable with stable relative proportions over 0–7 days. This does not establish secreted-enzyme cooperation, reciprocal benefit or necessary cross-feeding. |
| film | PMID:42664909; Abstract: PET film mass loss and surface-characterization sentences | supports | At pH 7.0 and 30 C, YB2 reached 4.30% ± 0.11% film mass loss after 3 days and exceeded the individual strains. Surface erosion, ester-related changes and residual crystallinity support polymer alteration, not complete mineralization. |
| products | PMID:42664909; Abstract: hydrolysis-product and conversion sentences | supports | BHET/MHET/TPA detection and EG release accompany depolymerization. The source reports 96.4% BHET and 97.3% MHET conversion at 2 days and nearly complete TPA use at 5 days. EG decline is interpreted as possible subsequent use, not tested assimilation. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum.CROSS_FEEDER/PRIMARY_DEGRADER; EnvironmentalFactor; GrowthMedia.inoculum_size/inoculum_unit; EcologicalStateEnum; CommunityOriginEnum | supports | CROSS_FEEDER denotes use of metabolites from another taxon, while PRIMARY_DEGRADER covers complex substrates. Environmental factors are conditions or parameters; inoculum_size is initial cell density or transfer percentage. ENGINEERED state and SYNTHETIC origin are compatible with deliberate assembly. |
| ontology | ontology-authority.json; Whole bounded receipt | supports | Eight encoded ontology pairs across 17 occurrences match canonical local labels. Both taxon IDs are species-ranked; separate ZY1/G1B designations do not imply unique strain-level taxonomy or genome mapping. |
| semantics | ontology-semantic-notes.json; Whole bounded receipt | supports | Exact role and field definitions support the recipient-evidence, outcome-placement and ratio-versus-amount distinctions while retaining the qualified graph. |
| mhet | mhet-grounding-candidates.json; Whole bounded receipt | supports | Optional MHET candidates distinguish neutral acid CHEBI:131735 and anion CHEBI:131704. This does not establish assay speciation or require a new annotation. |
| resources | dataset-verification.json; Whole bounded receipt | supports | The existing publication resource is verified. No concrete archive, culture accession or exact recipe is established at direct abstract scope; no omission or nonexistent-dataset conclusion follows. |
| snippets | snippet-audit.json; Whole bounded receipt | supports | All 18 excerpts match the pinned cache and directly retrieved source: 17 abstract passages and one article title. No full-text match is claimed. |
| history | provenance-audit.json; Whole bounded receipt | supports | Both sidecars, exact prior graph decision and linked issue provenance were reviewed. The prior graph repair remains intact; historical abstract review does not certify full Methods. |
| native-target | support-audit.json; Whole bounded receipt | supports | The target network is COMPLETE with two nodes, one arrow and three node-evidence items; native metrics are separate from scientific source coverage. |
| source-scope | source-audit.json; Whole bounded receipt | supports | Whole record review is partial because main Methods/Results, figures and SI remain uninspected. Only actual direct-source and authority scopes are certified. |
| independent-source | root-independent-source-audit.json; Whole bounded receipt | supports | Root independently concurs with the direct-abstract scope, retained graph and one major/two minor findings. |
| access-doi | https://doi.org/10.1016/j.jenvman.2026.130823; Inspected response and retrieval receipt | context_only | HTTP 200 returned a redirect shell without scientific article text. |
| access-article-api | https://api.elsevier.com/content/article/pii/S0301479726022838?httpAccept=text/xml; Inspected response and retrieval receipt | context_only | HTTP 200 returned 1856 bytes of bibliographic coredata, not full text. |
| access-publisher | https://www.sciencedirect.com/science/article/pii/S0301479726022838; Inspected response and retrieval receipt | context_only | HTTP 403 returned a visible access-error page. |
| access-openalex | https://api.openalex.org/works/https://doi.org/10.1016/j.jenvman.2026.130823; Inspected response and retrieval receipt | context_only | Closed-access metadata had no open PDF location; bounded metadata does not establish global absence. |
| search-leads | Exact DOI/title/PII public discovery; indexed-search-leads.json; direct-web-attempts.json | context_only | Indexed publisher methods and additional results are leads only because direct pages failed. No MSM recipe, sole-carbon condition or individual-strain numerical result is imported. |
| local-search | Maintained local corpus; local-search.json | supports | Ignored-inclusive local discovery establishes the scoped reuse/provenance search. |
| adapter | Optional structured source adapter; adapter-check.json | supports | Same-runtime batch 08 adapter discovery is explicitly reused with its original timestamp; no usable adapter or relevant expression-module dataset is asserted. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml; Actual execution 2026-10-21T13:51:32.577081+00:00 to 2026-10-21T13:51:33.434382+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-strict kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml --out /private/tmp/cm-review-session/batch-08/000426/strict-report.tsv; Actual execution 2026-10-21T13:51:32.577334+00:00 to 2026-10-21T13:51:34.884761+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-terms kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml; Actual execution 2026-10-21T13:51:32.577442+00:00 to 2026-10-21T13:51:34.423644+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml; Actual execution 2026-10-21T13:51:33.434641+00:00 to 2026-10-21T13:51:33.516731+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb-domain kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml; Actual execution 2026-10-21T13:51:33.516985+00:00 to 2026-10-21T13:51:34.937318+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-history history/records/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium; Actual execution 2026-10-21T13:51:34.424000+00:00 to 2026-10-21T13:51:35.167458+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T13:51:35.167954+00:00 to 2026-10-21T13:51:35.224320+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-references-explained kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml; Actual execution 2026-10-21T13:51:35.224563+00:00 to 2026-10-21T13:51:36.214124+00:00 | supports | Reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00 | supports | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00 | supports | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |

## Limits And Additional Notes

- Main Methods/Results, figures and supplementary files were not directly accessible through the inspected public routes. Whole-source scientific review remains incomplete; no full-text snippet verification or figure inspection is claimed.
- The direct abstract supports overlapping relative functions and potential complementarity. G1B growth in externally supplied BHET/MHET media does not itself establish uptake of metabolites supplied by ZY1; this is an evidence-scope distinction, not proof that cross-feeding is absent. Retain the explicitly proposed mechanism and qualified graph.
- The source explicitly attaches pH 7.0 and 30 C to three-day PET film mass loss. Two-day BHET/MHET and five-day TPA measurements are separate endpoints; full Methods is needed before extending all film-assay conditions to them. No claim is made that their actual conditions differ.
- Indexed MSM, sole-carbon wording and individual-strain quantitative results were not directly retrieved from article text and are not imported into the review as verified methods or outcomes. Bounded access failures do not establish global absence of public copies, datasets or protocols.
- No raw-data, enzyme, metabolite-flux or population-dynamics reanalysis was performed. No strain accession, recipe, reactor, culture-catalogue alias or exact medium linkage is guessed. No paid provider, contact or access-control bypass was used.
- No canonical, cache, history, generated or saved-review file changed; all 24 inspected inputs remain pinned.
- All 18 excerpts match directly retrieved source and cache: 17 abstract passages and one title. No full-text, figure or SI verification is claimed.
- Completeness 85 and quality 100/raw 116 are mechanical scores; review completion remains partial and scientific_review false.
- Optional MHET grounding is a bounded authority enrichment, not an extra finding. No exact strain genome, catalogue alias or recipe is inferred.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T135600Z-burkholderia-pseudomonas-yb2-pet-record
kind: record
repository: CultureBotAI/CommunityMech
title: Burkholderia–Pseudomonas YB2 PET consortium record review
started_at: '2026-10-21T13:51:07.411402Z'
finished_at: '2026-10-21T13:56:00.062251Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed source science, native/ontology checks
    and supporting provenance; no person-level independence asserted.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: Direct abstract evidence supports YB2 membership, relative functional differences,
  measured degradation endpoints and the two-node/one-PARTIAL-arrow graph. One major
  finding concerns the unqualified G1B recipient role; two minor findings concern
  outcomes stored as conditions and composition stored as inoculum amount. Full main,
  figures and SI remain unavailable through inspected routes.
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
  - path: history/records/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium/2026-09-22T213202Z-codex-426.yaml
    sha256: 4acf6e3ad7a72d265d90ec8c315e24151406e2b3f86e8e58e401fdaee910c262
    role: context
  - path: history/records/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium/2026-10-05T142601Z-codex-47e191.yaml
    sha256: 5f746825e2698995f733e12d9f69aafb56c6ff52f1fe896e575e610d7c2c9f74
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
    sha256: 8bfeed82fde64564ea0aeb64f142de29e051a643aafe17dcda5e1e45ea948e0b
    role: target
  - path: references_cache/PMID_42664909.txt
    sha256: 233f89810b1a1082f34803f7707bfe8cc42988b68b3b737329a89b13c2b8bb9b
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
- target_id: CommunityMech:000426
  path: kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  label: Burkholderia-Pseudomonas YB2 PET Degradation Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
    role: canonical_record
scope:
  description: Entire record, each node and the single arrow assessed against direct
    abstract/title, schema/ontology, history and bounded source-access/resource evidence.
  selection: Only released CommunityMech:000426 in the owned batch 08 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000426
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000426
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused native checks and cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000426
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-08/000426/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused native checks and cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000426
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused native checks and cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000426
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused native checks and cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000426
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused native checks and cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000426
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused native checks and cache-filename preflight; mechanical
    success does not certify source science.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000426
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused native checks and cache-filename preflight; mechanical
    success does not certify source science.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000426
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused native checks and cache-filename preflight; mechanical
    success does not certify source science.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000426
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit reuse of fresh batch 08 corpus receipts, not a target-specific
    pass or source certification.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000426
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit reuse of fresh batch 08 corpus receipts, not a target-specific
    pass or source certification.
- check_id: source-identity
  name: Primary bibliographic identity
  status: passed
  required: true
  summary: Exact PMID, DOI, title and directly retrieved complete abstract agree.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - pubmed
  - epmc
  - crossref
- check_id: scientific-source
  name: Full main and critical supplemental verification
  status: unavailable
  required: true
  summary: Main Methods/Results, figures and SI remain uninspected; direct access
    attempts returned errors or metadata only.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - source-scope
  - independent-source
  - access-publisher
  - access-article-api
- check_id: cross-mech
  name: Medium and archive correspondence
  status: not_applicable
  required: false
  summary: No exact recipe or archive accession established at direct abstract scope;
    no guessed link or omission finding.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - resources
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No task-runtime adapter or relevant expression-module dataset established;
    discovery reuse is explicit.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  locator: Entire record, two interaction nodes and one downstream link
  summary: The graph explicitly separates relative functional differences and proposed
    complementarity from measured PET-film loss. The unqualified G1B role and several
    non-graph field placements remain inconsistent with that scope.
  support: supports
  accessed_at: '2026-10-21T13:56:00.054574Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42664909&retmode=xml
  locator: Article-level metadata and available abstract
  summary: The complete direct abstract and exact title identify PMID:42664909 and
    DOI 10.1016/j.jenvman.2026.130823.
  support: supports
  accessed_at: '2026-10-21T13:51:37.592304Z'
  snapshot_sha256: 650248d727570787459aeb6496ca9c275952ef089e303e0a0d4effebed1d0d62
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42664909%20AND%20SRC:MED&format=json&resultType=core
  locator: Article-level metadata and available abstract
  summary: Matching abstract and access metadata report no PMCID and subscription
    access; this is not a global public-copy search.
  support: supports
  accessed_at: '2026-10-21T13:51:38.080575Z'
  snapshot_sha256: 70c54336e592fad36ef4ea6778d9866a27b75d1ca43ad16e4336bc9c64814237
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.jenvman.2026.130823
  locator: Article-level metadata and available abstract
  summary: Direct DOI metadata agrees with the focal article identity.
  support: supports
  accessed_at: '2026-10-21T13:51:37.666977Z'
  snapshot_sha256: cc608df0b74a1a1b2d7083c8b03df84052a90bc970150640ff305426382ec362
- evidence_id: membership
  kind: primary_source
  reference: PMID:42664909
  locator: 'Abstract: strain comparison and assembly sentence'
  summary: The study compared B. cepacia ZY1 and P. harudinis G1B and assembled YB2
    at a ZY1:G1B ratio of 4:5. That ratio identifies starting composition, not total
    cell density or transfer amount.
  support: supports
  accessed_at: '2026-10-21T13:56:00.055629Z'
  snapshot_sha256: 650248d727570787459aeb6496ca9c275952ef089e303e0a0d4effebed1d0d62
  quote: optimal inoculation ratio of 4:5
- evidence_id: functions
  kind: primary_source
  reference: PMID:42664909
  locator: 'Abstract: relative strain activities and concluding interpretation'
  summary: ZY1 had stronger PET-depolymerization-related activity; G1B grew better
    in supplied BHET/MHET media, with a trend toward faster BHET conversion. The authors
    describe overlapping functions and potential complementarity, not demonstrated
    donor-specific uptake.
  support: supports
  accessed_at: '2026-10-21T13:56:00.055664Z'
  snapshot_sha256: 650248d727570787459aeb6496ca9c275952ef089e303e0a0d4effebed1d0d62
  quote: potential complementarity
- evidence_id: localization
  kind: primary_source
  reference: PMID:42664909
  locator: 'Abstract: hydrolytic activity and cocultivation sentence'
  summary: Both strains had mainly cell-associated hydrolytic activities and remained
    culturable with stable relative proportions over 0–7 days. This does not establish
    secreted-enzyme cooperation, reciprocal benefit or necessary cross-feeding.
  support: supports
  accessed_at: '2026-10-21T13:56:00.055693Z'
  snapshot_sha256: 650248d727570787459aeb6496ca9c275952ef089e303e0a0d4effebed1d0d62
- evidence_id: film
  kind: primary_source
  reference: PMID:42664909
  locator: 'Abstract: PET film mass loss and surface-characterization sentences'
  summary: At pH 7.0 and 30 C, YB2 reached 4.30% ± 0.11% film mass loss after 3 days
    and exceeded the individual strains. Surface erosion, ester-related changes and
    residual crystallinity support polymer alteration, not complete mineralization.
  support: supports
  accessed_at: '2026-10-21T13:56:00.055719Z'
  snapshot_sha256: 650248d727570787459aeb6496ca9c275952ef089e303e0a0d4effebed1d0d62
- evidence_id: products
  kind: primary_source
  reference: PMID:42664909
  locator: 'Abstract: hydrolysis-product and conversion sentences'
  summary: BHET/MHET/TPA detection and EG release accompany depolymerization. The
    source reports 96.4% BHET and 97.3% MHET conversion at 2 days and nearly complete
    TPA use at 5 days. EG decline is interpreted as possible subsequent use, not tested
    assimilation.
  support: supports
  accessed_at: '2026-10-21T13:56:00.055740Z'
  snapshot_sha256: 650248d727570787459aeb6496ca9c275952ef089e303e0a0d4effebed1d0d62
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum.CROSS_FEEDER/PRIMARY_DEGRADER; EnvironmentalFactor;
    GrowthMedia.inoculum_size/inoculum_unit; EcologicalStateEnum; CommunityOriginEnum
  summary: CROSS_FEEDER denotes use of metabolites from another taxon, while PRIMARY_DEGRADER
    covers complex substrates. Environmental factors are conditions or parameters;
    inoculum_size is initial cell density or transfer percentage. ENGINEERED state
    and SYNTHETIC origin are compatible with deliberate assembly.
  support: supports
  accessed_at: '2026-10-21T13:56:00.055796Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded receipt
  summary: Eight encoded ontology pairs across 17 occurrences match canonical local
    labels. Both taxon IDs are species-ranked; separate ZY1/G1B designations do not
    imply unique strain-level taxonomy or genome mapping.
  support: supports
  accessed_at: '2026-10-21T13:56:00.056085Z'
  snapshot_sha256: bad1fc0460ed944925b004248e825ab89356176c110a9454b709d37c667086e8
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole bounded receipt
  summary: Exact role and field definitions support the recipient-evidence, outcome-placement
    and ratio-versus-amount distinctions while retaining the qualified graph.
  support: supports
  accessed_at: '2026-10-21T13:56:00.056463Z'
  snapshot_sha256: e461bae138187708255874be8f9d1a2d62f43f61d2ecaec9aeeb6343cc974240
- evidence_id: mhet
  kind: authority
  reference: mhet-grounding-candidates.json
  locator: Whole bounded receipt
  summary: Optional MHET candidates distinguish neutral acid CHEBI:131735 and anion
    CHEBI:131704. This does not establish assay speciation or require a new annotation.
  support: supports
  accessed_at: '2026-10-21T13:56:00.056767Z'
  snapshot_sha256: a25349617ec8b9fe94cb55ed7300c6f33dd69ff88b6adc93b1e8c07c914f04c7
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded receipt
  summary: The existing publication resource is verified. No concrete archive, culture
    accession or exact recipe is established at direct abstract scope; no omission
    or nonexistent-dataset conclusion follows.
  support: supports
  accessed_at: '2026-10-21T13:56:00.056902Z'
  snapshot_sha256: cc5d6d5d03e6b77aa9f5ea6a113b374987c1e75d95b5508e10b94d67c1107c62
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded receipt
  summary: 'All 18 excerpts match the pinned cache and directly retrieved source:
    17 abstract passages and one article title. No full-text match is claimed.'
  support: supports
  accessed_at: '2026-10-21T13:56:00.057111Z'
  snapshot_sha256: e84396777fc19e4a9ae5f2b639b4839cecd9bf6db46b40f89b652f18aca89a7d
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded receipt
  summary: Both sidecars, exact prior graph decision and linked issue provenance were
    reviewed. The prior graph repair remains intact; historical abstract review does
    not certify full Methods.
  support: supports
  accessed_at: '2026-10-21T13:56:00.057341Z'
  snapshot_sha256: a4809c9ee8eab163700a5600d488fd9391fc4c3fe658ba495a8bbdc8758b928d
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded receipt
  summary: The target network is COMPLETE with two nodes, one arrow and three node-evidence
    items; native metrics are separate from scientific source coverage.
  support: supports
  accessed_at: '2026-10-21T13:56:00.057382Z'
  snapshot_sha256: 277250ef65630a1e39b96d35d63eb3d4e2a547038805f911169a6ac9c662dc69
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded receipt
  summary: Whole record review is partial because main Methods/Results, figures and
    SI remain uninspected. Only actual direct-source and authority scopes are certified.
  support: supports
  accessed_at: '2026-10-21T13:56:00.057407Z'
  snapshot_sha256: 3f154858dd2e8a57082656cfdd4fc5df0dfe97cebc42ccb8753a3fe5e0bed065
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded receipt
  summary: Root independently concurs with the direct-abstract scope, retained graph
    and one major/two minor findings.
  support: supports
  accessed_at: '2026-10-21T13:56:00.057539Z'
  snapshot_sha256: e3ff0f79443ae40c873f18f1fd12186570c4d116e5b1fd21f67dca38567d29fa
- evidence_id: access-doi
  kind: database
  reference: https://doi.org/10.1016/j.jenvman.2026.130823
  locator: Inspected response and retrieval receipt
  summary: HTTP 200 returned a redirect shell without scientific article text.
  support: context_only
  accessed_at: '2026-10-21T13:51:38.032956Z'
  snapshot_sha256: 0a7a709e82e4c1da89916e8f0a1d02345153bd9793e3858d8d02dbbcf8458726
- evidence_id: access-article-api
  kind: database
  reference: https://api.elsevier.com/content/article/pii/S0301479726022838?httpAccept=text/xml
  locator: Inspected response and retrieval receipt
  summary: HTTP 200 returned 1856 bytes of bibliographic coredata, not full text.
  support: context_only
  accessed_at: '2026-10-21T13:51:46.000088Z'
  snapshot_sha256: 03bcea663e728dc8728cf8ae7f2324223800a1cbafffbd31201c828772d4994f
- evidence_id: access-publisher
  kind: database
  reference: https://www.sciencedirect.com/science/article/pii/S0301479726022838
  locator: Inspected response and retrieval receipt
  summary: HTTP 403 returned a visible access-error page.
  support: context_only
  accessed_at: '2026-10-21T13:51:45.722700Z'
  snapshot_sha256: dd9fec6af4a0c7d06dfa00a08caf33c54ebdd9aa9de8e967a2d530a03e8f1bdb
- evidence_id: access-openalex
  kind: database
  reference: https://api.openalex.org/works/https://doi.org/10.1016/j.jenvman.2026.130823
  locator: Inspected response and retrieval receipt
  summary: Closed-access metadata had no open PDF location; bounded metadata does
    not establish global absence.
  support: context_only
  accessed_at: '2026-10-21T13:51:45.904190Z'
  snapshot_sha256: 012caf55617ff15d2072411cfc4a6f1c562663bfefe729a90aa0c878c8d5f200
- evidence_id: search-leads
  kind: search
  reference: Exact DOI/title/PII public discovery
  locator: indexed-search-leads.json; direct-web-attempts.json
  summary: Indexed publisher methods and additional results are leads only because
    direct pages failed. No MSM recipe, sole-carbon condition or individual-strain
    numerical result is imported.
  support: context_only
  accessed_at: '2026-10-21T13:56:00.058679Z'
  snapshot_sha256: 5da6f99f3aa48d235888fce33d885422a467494d7abf4ee101af3af57440af21
  search_scope: Bounded exact DOI/title/PII and institutional/PDF queries; no global
    absence claim.
- evidence_id: local-search
  kind: search
  reference: Maintained local corpus
  locator: local-search.json
  summary: Ignored-inclusive local discovery establishes the scoped reuse/provenance
    search.
  support: supports
  accessed_at: '2026-10-21T13:56:00.058893Z'
  snapshot_sha256: 166a395600810cd06e00360599579e9a06d49cbc5e15b203e58629cb8cc8dcde
  search_scope: Maintained record, reusable taxon and mapping roots including ignored
    files, as recorded in the receipt.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: adapter-check.json
  summary: Same-runtime batch 08 adapter discovery is explicitly reused with its original
    timestamp; no usable adapter or relevant expression-module dataset is asserted.
  support: supports
  accessed_at: '2026-10-21T13:56:00.059029Z'
  snapshot_sha256: 2709b2aea7b8370b0d6434d6a0156553431a40fed8c0007dc1260c3e17c365d4
  search_scope: Bounded runtime/module and ignored-inclusive filename discovery; another
    checkout candidate was not executed.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  locator: Actual execution 2026-10-21T13:51:32.577081+00:00 to 2026-10-21T13:51:33.434382+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T13:51:33.434382Z'
  snapshot_sha256: e0a7f9badbd95ade822d427cb1529fcc6ee9f71ba2f650617716b9825a730dac
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-08/000426/strict-report.tsv
  locator: Actual execution 2026-10-21T13:51:32.577334+00:00 to 2026-10-21T13:51:34.884761+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T13:51:34.884761Z'
  snapshot_sha256: 76efd94aabbe14e2e3d600544247e62359fefd4fb1ce6c1ca9207ab665c48aad
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  locator: Actual execution 2026-10-21T13:51:32.577442+00:00 to 2026-10-21T13:51:34.423644+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T13:51:34.423644Z'
  snapshot_sha256: d44ff365fb8479c8d9d87cff5555eee9de6392fbd007065c513e32bd17b37487
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  locator: Actual execution 2026-10-21T13:51:33.434641+00:00 to 2026-10-21T13:51:33.516731+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T13:51:33.516731Z'
  snapshot_sha256: 0ad8152cf7b67c562894842e757271ea5a6158431c04a978a2d4eb38469bd6d7
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  locator: Actual execution 2026-10-21T13:51:33.516985+00:00 to 2026-10-21T13:51:34.937318+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T13:51:34.937318Z'
  snapshot_sha256: 78f4a09270fa49fb8eccfff3a30e1ffc7ba6f2100bb6108ba5f2c5541838399c
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium
  locator: Actual execution 2026-10-21T13:51:34.424000+00:00 to 2026-10-21T13:51:35.167458+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T13:51:35.167458Z'
  snapshot_sha256: ba75cd4a1c59d44464230e23e9d0b8c6a6d27c6b1cb3198f7d471d78754e2cbf
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T13:51:35.167954+00:00 to 2026-10-21T13:51:35.224320+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T13:51:35.224320Z'
  snapshot_sha256: 6147e68e4f618c8313321edfbaa9118e46179657b72b4e89db45870354f134ec
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
  locator: Actual execution 2026-10-21T13:51:35.224563+00:00 to 2026-10-21T13:51:36.214124+00:00
  summary: Reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T13:51:36.214124Z'
  snapshot_sha256: ff0cb2c2640fcb3dd0f82c41841afe84545cfdaf1399a39775870128ac716e83
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:11.311177Z'
  snapshot_sha256: 2d17097db768619fa7fea156f7c37781fa9cd463a6abdce6f529112518848cf0
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:15.408522Z'
  snapshot_sha256: 1332cfd7980ec54d517d625aff43fa6328c1a19fd405a7aef071f78af9774f3f
assessments:
- assessment_id: identity
  area: identity
  topic: Defined two-strain YB2 scope
  outcome: supported
  summary: Retain B. cepacia ZY1 and P. harudinis G1B, SYNTHETIC origin, ENGINEERED
    state and BIOREMEDIATION category.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - membership
  - schema
  - ontology
  dimensions:
  - name: community_scope
    value: Defined two-strain laboratory consortium
    definition: The optimized ratio belongs to assembly; it is not a natural community
      census.
    evidence_ids:
    - membership
  - name: taxon_rank
    value: Two species IDs with explicit strain designations
    definition: Neither species ID identifies a unique genome or validates an undisclosed
      strain alias.
    evidence_ids:
    - ontology
  - name: grounding_status
    value: UNRESOLVED GTDB for both members
    definition: No genome-based mapping is invented from species labels.
    evidence_ids:
    - ontology
  - name: environment
    value: Controlled laboratory environment
    definition: The source describes in-vitro PET and hydrolysis-product assays, not
      field remediation.
    evidence_ids:
    - membership
    - film
  - name: medium
    value: PET-assay pH/temperature verified; basal formulation unresolved
    definition: Direct abstract scope does not provide a complete recipe, vessel or
      total inoculum amount.
    evidence_ids:
    - film
    - source-scope
  - name: evidence_tier
    value: Direct abstract and bibliographic metadata
    definition: Critical main Methods, figures and SI remain inaccessible.
    evidence_ids:
    - source-scope
- assessment_id: roles
  area: evidence
  topic: taxonomy[0].functional_role and taxonomy[1].functional_role
  outcome: concern
  summary: ZY1 PRIMARY_DEGRADER is supported, while the unqualified G1B CROSS_FEEDER
    assignment exceeds demonstrated recipient evidence.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - functions
  - schema
  - semantics
  details: Greater growth in externally supplied hydrolysis products supports substrate-use
    capability, not their provenance from ZY1. Retain source-proposed cross-feeding/complementarity
    as a hypothesis with local PARTIAL evidence if represented, or omit the unsupported
    categorical role. This does not assert that cross-feeding is absent or require
    a particular tracer assay to retain a hypothesis. Both strains have overlapping
    functions; relative strengths do not imply exclusivity.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain the COMMUNITY_LEVEL complementarity node without imposing a stronger
    interaction type.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - functions
  - localization
  - record
  details: Its PARTIAL evidence and explicit exclusions correctly distinguish relative
    activity/growth differences from demonstrated resource partitioning, reciprocal
    benefit and donor-resolved exchange. Mainly cell-associated hydrolysis does not
    justify inventing a secreted-enzyme mechanism.
- assessment_id: arrow-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: Retain the PARTIAL complementarity→enhanced film-loss explanation at the
    source hypothesis level.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - functions
  - film
  details: The abstract proposes potential complementarity alongside enhanced consortium
    performance. It does not isolate necessary mediation or trace transfer, and the
    existing arrow already states those limits. No obligatory-dependence requirement
    or extra edge is added.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain the measured PET-film loss and physical/chemical alteration node.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - film
  - products
  details: The three-day film result is separate from two-day BHET/MHET and five-day
    TPA endpoints. The record correctly rejects interpreting mass loss as mineralization
    or proof of niche partitioning. Significance is source-reported against individual
    strains; no inaccessible figure or statistical reanalysis is claimed.
- assessment_id: outcome-placement
  area: representation
  topic: environmental_factors[1] and [2]
  outcome: concern
  summary: Film mass loss and product conversion are responses, not environmental
    conditions.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - film
  - products
  - schema
  details: Keep the numerical results with outcome/process claims; pH and temperature
    can remain actual conditions. The starting ratio in environmental_factors[0] is
    an assembly parameter already captured in engineering_design and can be consolidated
    during this bounded cleanup without a separate finding.
- assessment_id: cultivation
  area: representation
  topic: growth_media[0] inoculum and assay scope
  outcome: concern
  summary: The 4:5 composition ratio is not the initial cell density or transfer amount
    required by inoculum_size.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - membership
  - film
  - schema
  - semantics
  details: Preserve 4:5 in assembly/composition notes and leave inoculum amount unresolved
    unless Methods supplies it. The source explicitly attaches pH 7.0 and 30 C to
    the PET-film assay; narrow the medium title/notes to that verified scope rather
    than implying every product assay shares those conditions. This is not a finding
    that the actual product-assay conditions differ. No specific basal recipe, agitation,
    vessel or culture volume is inferred.
- assessment_id: chemistry
  area: grounding
  topic: Chemical terms, related ingredients and GO process
  outcome: supported
  summary: Current PET, BHET, TPA, EG and broad xenobiotic-process annotations fit
    the stated abstract claims.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - ontology
  - products
  - mhet
  details: EG release/decline is retained without promoting possible utilization to
    measured assimilation. No acid/anion error is inferred solely from pH or nomenclature.
    MHET enrichment is optional and should distinguish neutral acid from anion if
    adopted; no full mineralization, enzyme identity or molecular flux is added.
- assessment_id: resources
  area: provenance
  topic: Publication, source access and unresolved datasets
  outcome: supported
  summary: The existing resource identifies the focal publication; unavailable main/SI
    prevents a complete resource or protocol assessment.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - pubmed
  - epmc
  - crossref
  - resources
  - source-scope
  details: No exact sequence archive, strain-catalogue accession or recipe link is
    verified in the abstract. Do not infer its absence from the paper or add an omission
    finding. Indexed publisher snippets remain leads requiring direct primary verification.
- assessment_id: history
  area: provenance
  topic: Prior repair and evidence matching
  outcome: supported
  summary: The two qualified nodes and PARTIAL arrow preserve the prior graph repair
    and current discussion.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - history
  - snippets
  details: Issue 1265 is freshly verified closed with no comments; its scope separates
    graph repair from non-graph follow-up. Issue 1268 is assessed through explicitly
    timestamped same-session receipt reuse. All 18 current excerpts match direct abstract/title,
    without extending that result to inaccessible full text.
- assessment_id: validation
  area: schema
  topic: Native gates and authority labels
  outcome: supported
  summary: Eight native checks and all eight ontology pairs pass; semantic and access
    limitations remain.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - native-target
- assessment_id: metrics
  area: completeness
  topic: Mechanical completeness and quality
  outcome: supported
  summary: Native scores do not certify the uninspected main/SI or resolve semantic
    overstatement.
  target_ids:
  - CommunityMech:000426
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role component +5 environment +10 for three
      environmental factors +5 resource +10 growth medium +5 metabolites; no three-node
      or dataset bonus.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0/P2=1/P3=2/P4=0; three node evidence/two nodes gives15; COMPLETE adds15;
      raw116 capped100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 1
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 2
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
findings:
- finding_id: recipient-role
  issue_key: cm-000426-recipient-role
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: the categorical role asserts another-taxon metabolite
    use beyond the cited phenotype and source-proposed mechanism, despite the correctly
    qualified graph.'
  rule_id: review-checklist.claim-specific-evidence-and-placement
  status: open
  certainty: confirmed
  title: Qualify the G1B recipient role as proposed complementarity
  description: taxonomy[1].functional_role asserts CROSS_FEEDER without the uncertainty
    already preserved in the graph. Its local growth evidence concerns supplied BHET/MHET
    media and supports downstream substrate-use capacity; it does not establish that
    the utilized material came from ZY1.
  target_ids:
  - CommunityMech:000426
  field_paths:
  - taxonomy[1].functional_role
  - taxonomy[1].evidence[1]
  evidence_ids:
  - functions
  - schema
  - semantics
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
    role: canonical_record
- finding_id: outcome-placement
  issue_key: cm-000426-outcome-placement
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded field placement of supported observations, without
    changing the biological result.'
  rule_id: review-checklist.claim-specific-evidence-and-placement
  status: open
  certainty: confirmed
  title: Move degradation outcomes out of environmental conditions
  description: environmental_factors[1] and [2] encode film mass loss and BHET/MHET
    conversion. These measured outcomes remain supported but are not environmental
    conditions; pH and temperature embedded in the first outcome are genuine assay
    conditions.
  target_ids:
  - CommunityMech:000426
  field_paths:
  - environmental_factors[1]
  - environmental_factors[2]
  evidence_ids:
  - film
  - products
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
    role: canonical_record
- finding_id: inoculum-amount
  issue_key: cm-000426-inoculum-amount
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: semantic correction to inoculum amount and a bounded
    assay-scope clarification; no unsupported claim that actual assay conditions differ.'
  rule_id: review-checklist.claim-specific-evidence-and-placement
  status: open
  certainty: confirmed
  title: Separate starting composition from inoculum amount
  description: growth_media[0].inoculum_size and inoculum_unit encode 4:5 ZY1:G1B.
    This specifies starting composition rather than initial density or transfer percentage.
    The medium title also combines assays for which the abstract only explicitly supplies
    PET-film pH/temperature.
  target_ids:
  - CommunityMech:000426
  field_paths:
  - growth_media[0].inoculum_size
  - growth_media[0].inoculum_unit
  - growth_media[0].name
  - growth_media[0].preparation_notes
  evidence_ids:
  - membership
  - film
  - schema
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
    role: canonical_record
actions:
- action_id: qualify-recipient-role
  description: Align the G1B taxonomy role with the source-proposed complementarity
    and locally supported growth phenotype.
  finding_ids:
  - recipient-role
  target_ids:
  - CommunityMech:000426
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Either retain CROSS_FEEDER only with explicit proposed/partial support and a local
    note distinguishing supplied-substrate growth from donor-resolved uptake, or omit
    the categorical role and retain the directly supported phenotype. Do not declare
    cross-feeding disproven.
  - Use the source conclusion for potential complementarity and preserve overlapping
    functions. Neither greater substrate growth nor stable relative proportions establishes
    reciprocal benefit, obligatory dependence or transfer necessity.
  - Retain ZY1 PRIMARY_DEGRADER, both exact source strains, current compatible taxon/chemical
    IDs and unresolved GTDB status. Preserve the two nodes and one PARTIAL downstream
    explanation. No particular tracer assay is a prerequisite for representing the
    source hypothesis.
- action_id: relocate-outcomes
  description: Retain supported degradation results in endpoint/process context and
    reserve environmental fields for actual conditions.
  finding_ids:
  - outcome-placement
  target_ids:
  - CommunityMech:000426
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve 4.30% ± 0.11% PET-film mass loss after 3 days, 96.4% BHET and 97.3% MHET
    conversion after 2 days, and the separate nearly complete TPA use after 5 days.
    Keep reported significance restricted to the film-loss comparison.
  - Place pH 7.0 and 30 C as film-assay conditions; move response values out of environmental_factors[1]
    and [2]. Consolidate the starting ratio under engineering_design or composition
    notes as appropriate.
  - Do not relabel polymer alteration as complete mineralization, or EG decline as
    demonstrated assimilation. No new node or arrow is needed to relocate supported
    outcomes.
- action_id: repair-inoculum-and-assay-scope
  description: Represent 4:5 as composition, leave total inoculum unresolved and scope
    cultivation fields to direct evidence.
  finding_ids:
  - inoculum-amount
  target_ids:
  - CommunityMech:000426
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Burkholderia_Pseudomonas_YB2_PET_Degradation_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Remove 4:5 from inoculum_size/inoculum_unit as an amount and preserve it as the
    source-defined ZY1:G1B starting ratio. Do not invent cell density, OD, transfer
    percentage or CFU.
  - Narrow the medium name and notes so pH 7.0 and 30 C are explicitly verified for
    the three-day PET-film assay; retain the two-day product and five-day TPA endpoints
    separately. Do not assert their conditions differ.
  - Resolve formulation, vessel, agitation, working volume and other assay conditions
    only from directly inspected main/SI. Indexed MSM/sole-carbon fragments remain
    leads, with no guessed CultureMech link or dataset omission.
  - After separately authorized curation, run focused schema, strict, term, reference
    and history checks; preserve the existing qualified graph and record any new direct-source
    scope.
limitations:
- Main Methods/Results, figures and supplementary files were not directly accessible
  through the inspected public routes. Whole-source scientific review remains incomplete;
  no full-text snippet verification or figure inspection is claimed.
- The direct abstract supports overlapping relative functions and potential complementarity.
  G1B growth in externally supplied BHET/MHET media does not itself establish uptake
  of metabolites supplied by ZY1; this is an evidence-scope distinction, not proof
  that cross-feeding is absent. Retain the explicitly proposed mechanism and qualified
  graph.
- The source explicitly attaches pH 7.0 and 30 C to three-day PET film mass loss.
  Two-day BHET/MHET and five-day TPA measurements are separate endpoints; full Methods
  is needed before extending all film-assay conditions to them. No claim is made that
  their actual conditions differ.
- Indexed MSM, sole-carbon wording and individual-strain quantitative results were
  not directly retrieved from article text and are not imported into the review as
  verified methods or outcomes. Bounded access failures do not establish global absence
  of public copies, datasets or protocols.
- No raw-data, enzyme, metabolite-flux or population-dynamics reanalysis was performed.
  No strain accession, recipe, reactor, culture-catalogue alias or exact medium linkage
  is guessed. No paid provider, contact or access-control bypass was used.
notes:
- No canonical, cache, history, generated or saved-review file changed; all 24 inspected
  inputs remain pinned.
- 'All 18 excerpts match directly retrieved source and cache: 17 abstract passages
  and one title. No full-text, figure or SI verification is claimed.'
- Completeness 85 and quality 100/raw 116 are mechanical scores; review completion
  remains partial and scientific_review false.
- Optional MHET grounding is a bounded authority enrichment, not an extra finding.
  No exact strain genome, catalogue alias or recipe is inferred.
tags:
- record-review
- pet-degradation
- proposed-cross-feeding
- partial-source
- batch-08
```
