# BioAsteroid ISS chondrite biomining consortium: record review

- Review: 20261021T112821Z-bioasteroid-iss-chondrite-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T11:22:47.142833Z
- Finished UTC: 2026-10-21T11:28:21.436721Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Complete source review supports the defined consortium and all three qualified graph nodes with no arrows. Three minor findings concern experimental/measurement qualifications, structured medium precision and the omitted public metabolomics deposit. The supplement limits contamination concerns to particular Earth fungal samples rather than invalidating the ISS model.

## Scope And Provenance

Whole record and three nodes assessed against complete scientific main, all main and supplementary figures, declared tables/statistics, public dataset metadata and strain/ontology authorities.

Selection: Next assigned maintained path after 000318 was saved and both mandatory post-save checks passed; only CommunityMech:000305 reviewed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000305 | kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml | maintained | BioAsteroid ISS Chondrite Biomining Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000305 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000305 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000305 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000305 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000305 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000305 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000305 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000305 | Target reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000305 | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |
| check-network-quality | failed | True | CommunityMech:000305 | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |
| Primary publication and resource identity | passed | True | CommunityMech:000305 | Direct final-publication metadata, full text, strain catalogue and study-deposit metadata were verified. |
| Full primary scientific assessment | passed | True | CommunityMech:000305 | Whole scientific main, six main figures, all eleven SI figures and declared supplement/statistics scopes were inspected. |
| Encoded medium/ingredient-Mech links | not_applicable | False | CommunityMech:000305 | No CultureMech or MediaIngredientMech identifier is encoded; no exact recipe equivalence was inferred. |
| Optional structured source adapter | unavailable | False | CommunityMech:000305 | No runnable adapter was available in the owned runtime. |

## Scientific And Domain Assessments

### Defined consortium, strain and experimental scope

identity: supported. Targets: CommunityMech:000305.

The two-member synthetic biomining model and its structured strain identities are supported.

### Membership, roles and strain authority

grounding: supported. Targets: CommunityMech:000305.

Retain the source-defined pair, current species names and broad degradation roles.

The roles are compatible with the schema’s broad complex-substrate definition and source biomining evidence, rather than proof that every treatment outperforms every abiotic control. The bacterial basalt/REE snippet is explicitly prior-study background, not a measurement from this chondrite assay. Fungal NO_GTDB_EQUIVALENT is appropriate; historical mapping-release statistics were not re-certified.

### ecological_interactions[0]: Fungal bioleaching

graph: supported. Targets: CommunityMech:000305.

Retain the element-specific means and PARTIAL chemistry interpretation.

P. simplicissimum DSM 1078 is the participating organism in monoculture-versus-control and between-organism comparisons, with ISS/ground conditions kept separate. The graph correctly limits most ISS contrasts to nonsignificant mean differences and singles out phosphorus. Carboxylic-acid features suggest chemistry without identifying a necessary mediator; bulk Pd/V measurements do not resolve ionic species.

### ecological_interactions[1]: Surface colonization

graph: supported. Targets: CommunityMech:000305.

Retain co-colonization without facilitation or biofilm-to-leaching causation.

S. desiccabilis CP1D and P. simplicissimum DSM 1078 appear together on the meteorite in consortium samples under both conditions. Morphology supports the source’s biofilm interpretation, not quantified growth/transcription kinetics, enhanced partner establishment or necessary contact mediation. The three-node graph correctly has no downstream arrows.

### ecological_interactions[2]: Candidate bacterial antagonism

graph: supported. Targets: CommunityMech:000305.

Retain the explicitly PARTIAL S. desiccabilis → P. simplicissimum interpretation.

The direction refers to lower mean palladium extraction by the mixture than the fungal monoculture. The ISS comparison is nonsignificant (published p≈0.863); it does not measure fungal suppression, reciprocal negative fitness or an upstream mediator. No edge to the leaching node should be restored from the same endpoint contrast.

### Comparators, measurements and source caveats

evidence: concern. Targets: CommunityMech:000305.

Non-graph summaries should inherit the graph’s statistical and mechanistic qualifications and the recovered control caveats.

Parallel treatment arms are not necessarily concurrent experiments: ISS samples ran in December 2020–January 2021, ground controls were prepared in March/April 2021, with n=3 flight and n=4 biological/n=6 non-biological ground samples. Possible Earth fungal contamination has unresolved origin and effect; it does not invalidate all ISS results. Relative metabolite features are not production-rate measurements. Liquid extraction used ICP-MS, whereas pristine-rock characterization also used ICP-OES.

### Medium formulation and cultivation representation

completeness: concern. Targets: CommunityMech:000305.

The core cultivation settings are supported, with bounded ingredient representation gaps.

Keep 5 mL, 19 days, 20 °C setpoint/19.5 °C logged flight temperature and initial pH 7.2. Gas-permeable BMR membranes support aerobic exchange; closed batch does not mean hermetically sealed. The 0.15 g/L reagent is sodium pyruvate, while CHEBI:15361 denotes its anion. K2HPO4 0.15 g/L and MgSO4·7H2O 0.025 g/L appear in correct notes but not the structured composition. Preculture, desiccation, fixation and analytical temperatures are distinct stages.

### Element inventory and measurement scope

grounding: supported. Targets: CommunityMech:000305.

Retain element-level grounding without inferring speciation or universal biological enhancement.

The source measures the listed metals and reports europium/lutetium bioleaching context. Platinum, ruthenium, molybdenum and manganese are source-reported but lack the current structured enum values, as the notes state. The inventory does not establish a particular oxidation state or that every element improved in the consortium under microgravity.

### Public metabolomics deposit

completeness: concern. Targets: CommunityMech:000305.

The empty associated_datasets list omits a directly reported public study deposit.

DataShare DOI 10.7488/ds/7828 and handle 10283/8889 resolve to BioAsteroid_metabolomics. Metadata and the complete small README describe prepared ISS/ground samples; its 1 mL volume is the recovered aliquot, not reactor working volume. The listed 4.05 GB archive was not downloaded or analyzed; preprint metadata are provenance, not interchangeable final-source evidence.

### Exact snippets and previous repairs

provenance: supported. Targets: CommunityMech:000305.

Fresh source evidence preserves the earlier qualified graph and canonical palladium labels.

The MD header remains abstract_only despite appended scientific main text. All 23 quotations match directly retrieved final-source text; the historical abstract-access mismatch backlog does not imply current fabrication. Prior unread-figure/SI statements describe that earlier review rather than the current inspection.

### Native checks and source assessment

schema: supported. Targets: CommunityMech:000305.

All eight native checks pass; source assessment supplies the bounded context and precision follow-up.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000305.

Mechanical scores do not certify statistical significance or molecular mediation.

## Findings

### experimental-context: Clarify comparator and measurement scope

minor / open / confirmed; issue key: cm-000305-experimental-context.

Non-graph summaries omit recoverable statistical/control caveats and conflate liquid-leachate with pristine-rock analytical methods.

### medium-representation: Match structured ingredients to the reported formulation

minor / open / confirmed; issue key: cm-000305-medium-representation.

The sodium-pyruvate reagent is mapped to its anion, and two correctly transcribed salts remain only in preparation notes.

### metabolomics-data: Link the public metabolomics dataset

minor / open / confirmed; issue key: cm-000305-metabolomics-data.

A source-reported, publicly resolvable metabolomics deposit is absent from the dataset/resource fields.

## Recommended Actions And Acceptance Checks

### repair-experimental-context

Clarify comparator and measurement scope.

- Use source-supported mean/trend wording and preserve element-specific significance; do not turn proposed bacterial antagonism or organic-acid mediation into demonstrated partner fitness or causal necessity.
- State the later ground-control timeline and unequal replication, without presenting it as an onboard 1g control or an isolated gravity intervention.
- Record the supplement’s sample-specific Earth fungal contamination caveat and unresolved timing/impact; do not add contaminants to intended membership or label all samples contaminated.
- Distinguish metabolite feature abundance from measured production rate, and liquid-leachate ICP-MS from ICP-MS/ICP-OES pristine-rock characterization.
- Keep initial pH 7.2 distinct from RNAlater-affected endpoint measurements; retain all three qualified nodes and zero arrows.

### repair-medium-representation

Match structured ingredients to the reported formulation.

- Use verified CHEBI:50144 sodium pyruvate for the weighed reagent, or explicitly distinguish reagent identity from the dissolved pyruvate moiety; preserve the source 0.15 g/L amount.
- Add source-backed structured entries for K2HPO4 0.15 g/L and MgSO4·7H2O 0.025 g/L, preserving hydration and not doubling the already half-strength formulation.
- Retain the valid 5 mL, initial pH and incubation context; do not import DSMZ maintenance conditions or an unverified CultureMech recipe equivalent.

### repair-metabolomics-data

Link the public metabolomics dataset.

- Add DataShare handle 10283/8889 and DOI 10.7488/ds/7828 with the BioAsteroid_metabolomics title and liquid-fraction ISS/ground scope.
- Distinguish prepared sample metadata from validated post-filtering analytical coverage; 1 mL README aliquots are not the 5 mL reactors.
- Do not certify uninspected archive payloads or equate preprint and final-publication results; no raw-data rerun is required for this linkage.

### preserve-qualified-graph

Retain all three qualified nodes and zero arrows during separately authorized follow-up.

- Keep mean leaching, statistical contrasts, biofilm observations and candidate mechanisms distinct.
- Do not restore biofilm-to-leaching or antagonism-to-leaching edges from observations of the same endpoint.
- Preserve append-only history and rerun schema, strict, term, reference, history and target/corpus network checks after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml; Whole record: two strains, three nodes, zero arrows, medium and source resources | supports | The intended experimental consortium and qualified graph are identifiable; bounded context, medium and resource follow-up remains. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=41617698&amp;retmode=xml; Article-level metadata | supports | PubMed verifies PMID, DOI, title and abstract. |
| crossref | https://api.crossref.org/works/10.1038/s41526-026-00567-3; Article-level metadata | supports | Crossref verifies the final DOI/title and publication metadata. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41617698&amp;format=json&amp;resultType=core; Article-level metadata | supports | Europe PMC verifies article-level identifiers and the available full-text route. |
| leaching | PMID:41617698; Fresh XML Sec5–Sec9; Figures 4–5; Supplementary Tables 2–5 | supports | Element-specific means, control normalizations and significance limits support the qualified extraction node; phosphorus is the significant fungal/non-biological ISS comparison. |
| colonization | PMID:41617698; Fresh XML Sec4 and Sec11; Figure 3; Supplementary Figures 1–3 | supports | SEM supports both organisms on meteorite surfaces and mixed colonization, without establishing enhanced partner establishment or a leaching requirement. |
| antagonism | PMID:41617698; Fresh XML Sec11; Figure 5; Supplementary Table 2 | partial | Lower mean consortium palladium extraction motivates a candidate bacterial effect, not demonstrated inhibition of fungal fitness. |
| metabolomics | PMID:41617698; Fresh XML Sec10–Sec11 and Sec24; Figure 6; Supplementary Figures 5–6/Table 6 | supports | Liquid-fraction feature annotations and abundance patterns motivate chemical hypotheses; common leaching acids were not detected and no mediator was selectively tested. |
| methods | PMID:41617698; Fresh XML Sec13–Sec21 and Sec26 | supports | Methods report exact strains, medium, desiccated inocula, gas-permeable reactors, 19-day cultivation and separate flight/ground timelines; leachates were measured by ICP-MS. |
| meteorite | PMID:41617698; Fresh XML Sec3/Table 1/Table 2 and Sec14; Figure 2 | supports | Pristine NWA 869 characterization supports the mineral/element inventory; ICP-MS/ICP-OES rock measurements are distinct from the liquid-leachate assay. |
| supplement | PMID:41617698; Supplementary Note 1 pp. 2–4; Figures 7–11; Tables 7–9 | supports | The authors infer clean original ISS samples and bound possible contamination to Earth fungal samples; post-fixation pH cannot reconstruct the culture pH trajectory. |
| statistics | PMID:41617698; Supplementary Data 1, TUKEY rows 10 and 22; all focal ISS comparison columns in scratch audit | supports | Published p values are 0.0498876 for fungal/non-biological phosphorus and 0.863164 for consortium/fungal palladium on ISS; no statistical model was rerun. |
| catalogue | https://www.dsmz.de/collection/catalogue/details/culture/DSM-1078; Direct DSMZ catalogue lines 159–209, preserved in root-catalogue-web.json | supports | DSM 1078 currently maps to P. simplicissimum, strain 5696 with collection aliases; historical naming and catalogue maintenance conditions do not replace the focal identity or protocol. |
| ontology | Local OAK NCBITaxon, ENVO, CHEBI and GO; ontology-authority.json and sodium-pyruvate assessment | supports | All encoded labels match; ingredient specificity must distinguish sodium pyruvate from its pyruvate anion, while element terms do not demonstrate ionic speciation. |
| salt-candidate | CHEBI:50144; sodium-pyruvate-candidate.json: local OAK label, formula, charge and synonyms | supports | Verified sodium pyruvate is the sodium salt with formula C3H3O3.Na, distinct from pyruvate anion CHEBI:15361. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum.PRIMARY_DEGRADER; MetalElementEnum and RareEarthElementEnum | supports | PRIMARY_DEGRADER means degradation of complex substrates without an organic-only restriction; the four metal names omitted from the structured lists are absent from the current metal enum. |
| snippets | kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml; snippet-audit.json | supports | All 23 snippets match the fresh direct XML and publisher text as well as the pinned appended-main cache. |
| history | kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml; provenance-audit.json | supports | Earlier label and graph repairs remain preserved; generic open backlog context is not evidence of a current snippet defect. |
| resources | kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml; dataset-verification.json | supports | DataShare handle 10283/8889 and DOI 10.7488/ds/7828 identify BioAsteroid metabolomics; the preprint identity is verified without equating all versions. |
| native-target | kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml; support-audit.json | supports | Target network and mechanical metrics are separately recorded; source assessment controls biological interpretation. |
| source-scope | PMID:41617698; source-audit.json | supports | Whole scientific main and all figure/caption scopes were inspected; large archive and sequence/statistical reanalysis remain excluded. |
| independent-source | PMID:41617698; root-independent-source-audit.json | context_only | Independent source, figure, supplement and authority review supports the bounded follow-up. |
| search | Owned maintained roots; local-search.json: ignored-inclusive bounded searches | supports | Reusable identity and mapping discovery was limited to the declared roots; no global absence is asserted. |
| adapter | Optional structured source adapter; adapter-check.json: same-runtime batch 06 discovery reuse | supports | No runnable adapter was available in the owned runtime; no paid provider or external runner was used. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml; Actual execution 2026-10-21T11:24:53.519237+00:00 to 2026-10-21T11:24:54.385735+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-strict kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml --out /private/tmp/cm-review-session/batch-06/000305/strict-report.tsv; Actual execution 2026-10-21T11:24:53.519527+00:00 to 2026-10-21T11:24:55.792366+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-terms kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml; Actual execution 2026-10-21T11:24:53.519663+00:00 to 2026-10-21T11:24:55.342801+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-gtdb kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml; Actual execution 2026-10-21T11:24:54.386064+00:00 to 2026-10-21T11:24:54.474336+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-gtdb-domain kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml; Actual execution 2026-10-21T11:24:54.474572+00:00 to 2026-10-21T11:24:55.852290+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-history history/records/BioAsteroid_ISS_Chondrite_Biomining_Consortium; Actual execution 2026-10-21T11:24:55.343038+00:00 to 2026-10-21T11:24:56.052796+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T11:24:56.053750+00:00 to 2026-10-21T11:24:56.111459+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-references-explained kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml; Actual execution 2026-10-21T11:24:56.111683+00:00 to 2026-10-21T11:24:57.109176+00:00 | supports | Target reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T10:06:35.990708+00:00 to 2026-10-21T10:06:41.713287+00:00 | supports | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T10:06:35.990845+00:00 to 2026-10-21T10:06:41.708376+00:00 | supports | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |

## Limits And Additional Notes

- No raw metabolomics archive, peak processing, statistical model or sequence alignment was rerun; the 4.05 GB deposit payload was not downloaded.
- Supplementary Data 1 inspection was bounded to workbook inventory/headers and published focal comparison columns; other raw-data rows were not exhaustively assessed. Table 8 sequences were not independently used to identify contaminants.
- Possible Earth fungal contamination has unresolved timing and influence. The authors infer original ISS samples were clean; this assessment does not establish absolute sterility or add contaminants as designed members.
- Separate Earth and ISS timelines, sample counts and processing caveats limit an isolated gravity-causation interpretation. Endpoint pH after RNAlater does not establish the culture pH trajectory.
- Broad biofilm and chemical annotations do not prove molecular mediation, partner fitness or ionic speciation. No exact CultureMech recipe equivalence was verified.
- Preprint bibliographic identity was verified; preprint scientific content was not substituted for the final publication. Catalogue maintenance conditions and historical GTDB-release statistics were not re-certified as experimental conditions.
- No canonical, cache, history or generated file changed.
- All 24 repository inputs were pinned before assessment and rechecked.
- Eleven quoted words from the focal publication, including the total budget for its supplements.
- Native quality 100 is capped from 129; source findings remain actionable.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T112821Z-bioasteroid-iss-chondrite-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'BioAsteroid ISS chondrite biomining consortium: record review'
started_at: '2026-10-21T11:22:47.142833Z'
finished_at: '2026-10-21T11:28:21.436721Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, native/ontology checks
    and supporting snippets/provenance; no person-level independence is asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Complete source review supports the defined consortium and all three qualified
  graph nodes with no arrows. Three minor findings concern experimental/measurement
  qualifications, structured medium precision and the omitted public metabolomics
  deposit. The supplement limits contamination concerns to particular Earth fungal
  samples rather than invalidating the ISS model.
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
  - path: history/records/BioAsteroid_ISS_Chondrite_Biomining_Consortium/2026-10-02T052502Z-codex-305ca1.yaml
    sha256: ca237a37aa7ffd2bd25d3c63969cb27c38cd3505686a16e128ca733a70e027db
    role: context
  - path: history/records/BioAsteroid_ISS_Chondrite_Biomining_Consortium/2026-10-05T124957Z-codex-30174b.yaml
    sha256: 910bd44af4f343980d4b43846cc11695262b2b49025ab1829b057393c57656d7
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    sha256: deca4ca6c9b101ed4fdd56d063fba994e7b88fbabe06a8e5c8a7f19b3165ef5b
    role: target
  - path: references_cache/PMID_41617698.md
    sha256: 019a43dfbb99934f1a5c72e50df30b7d0bafc026c04d999e12c7751a7ae2b437
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
- target_id: CommunityMech:000305
  path: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  label: BioAsteroid ISS Chondrite Biomining Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    role: canonical_record
scope:
  description: Whole record and three nodes assessed against complete scientific main,
    all main and supplementary figures, declared tables/statistics, public dataset
    metadata and strain/ontology authorities.
  selection: Next assigned maintained path after 000318 was saved and both mandatory
    post-save checks passed; only CommunityMech:000305 reviewed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000305
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000305
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify membership or ontology semantics.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000305
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-strict kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-06/000305/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify membership or ontology semantics.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000305
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-terms kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify membership or ontology semantics.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000305
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify membership or ontology semantics.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000305
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb-domain kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify membership or ontology semantics.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000305
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-history history/records/BioAsteroid_ISS_Chondrite_Biomining_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify membership or ontology semantics.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000305
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify membership or ontology semantics.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000305
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-references-explained kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    structural success does not certify membership or ontology semantics.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; target-native structure has no issue.
  target_ids:
  - CommunityMech:000305
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
    and exit 1; target-native structure has no issue.
  target_ids:
  - CommunityMech:000305
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Reused fresh full-corpus batch 06 execution, not a target-specific pass.
- check_id: source-identity
  name: Primary publication and resource identity
  status: passed
  required: true
  summary: Direct final-publication metadata, full text, strain catalogue and study-deposit
    metadata were verified.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - catalogue
  - resources
- check_id: scientific-source
  name: Full primary scientific assessment
  status: passed
  required: true
  summary: Whole scientific main, six main figures, all eleven SI figures and declared
    supplement/statistics scopes were inspected.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - source-scope
  - independent-source
  - supplement
  - statistics
- check_id: cross-mech
  name: Encoded medium/ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech identifier is encoded; no exact recipe
    equivalence was inferred.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - record
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No runnable adapter was available in the owned runtime.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  locator: 'Whole record: two strains, three nodes, zero arrows, medium and source
    resources'
  summary: The intended experimental consortium and qualified graph are identifiable;
    bounded context, medium and resource follow-up remains.
  support: supports
  accessed_at: '2026-10-21T11:28:21.429370Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41617698&retmode=xml
  locator: Article-level metadata
  summary: PubMed verifies PMID, DOI, title and abstract.
  support: supports
  accessed_at: '2026-10-21T11:22:53.424689Z'
  snapshot_sha256: 16a7f3d50bb3a20e2627761b2fc2a72c30160a560294c1687092c305353097d8
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1038/s41526-026-00567-3
  locator: Article-level metadata
  summary: Crossref verifies the final DOI/title and publication metadata.
  support: supports
  accessed_at: '2026-10-21T11:22:53.258906Z'
  snapshot_sha256: bbcd9ed92e7d02b918195f56f778ea256e72f95d687222a666a12be31e2f6f97
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41617698&format=json&resultType=core
  locator: Article-level metadata
  summary: Europe PMC verifies article-level identifiers and the available full-text
    route.
  support: supports
  accessed_at: '2026-10-21T11:22:53.655907Z'
  snapshot_sha256: 1042abdc59d0144f471a2c1dd50bdadfc088392cf910139921064eea0bd95ae6
- evidence_id: leaching
  kind: primary_source
  reference: PMID:41617698
  locator: Fresh XML Sec5–Sec9; Figures 4–5; Supplementary Tables 2–5
  summary: Element-specific means, control normalizations and significance limits
    support the qualified extraction node; phosphorus is the significant fungal/non-biological
    ISS comparison.
  support: supports
  accessed_at: '2026-10-21T11:28:21.429947Z'
  quote: enhanced mean leaching
  snapshot_sha256: d833c0e79dbe1b0485c0cf1a3cb90b851d0237feb62a61a823fecced7ec0deb9
- evidence_id: colonization
  kind: primary_source
  reference: PMID:41617698
  locator: Fresh XML Sec4 and Sec11; Figure 3; Supplementary Figures 1–3
  summary: SEM supports both organisms on meteorite surfaces and mixed colonization,
    without establishing enhanced partner establishment or a leaching requirement.
  support: supports
  accessed_at: '2026-10-21T11:28:21.430042Z'
  quote: mixed filamentous
  snapshot_sha256: d833c0e79dbe1b0485c0cf1a3cb90b851d0237feb62a61a823fecced7ec0deb9
- evidence_id: antagonism
  kind: primary_source
  reference: PMID:41617698
  locator: Fresh XML Sec11; Figure 5; Supplementary Table 2
  summary: Lower mean consortium palladium extraction motivates a candidate bacterial
    effect, not demonstrated inhibition of fungal fitness.
  support: partial
  accessed_at: '2026-10-21T11:28:21.430133Z'
  quote: possibly due to the antagonistic effects
  snapshot_sha256: d833c0e79dbe1b0485c0cf1a3cb90b851d0237feb62a61a823fecced7ec0deb9
- evidence_id: metabolomics
  kind: primary_source
  reference: PMID:41617698
  locator: Fresh XML Sec10–Sec11 and Sec24; Figure 6; Supplementary Figures 5–6/Table
    6
  summary: Liquid-fraction feature annotations and abundance patterns motivate chemical
    hypotheses; common leaching acids were not detected and no mediator was selectively
    tested.
  support: supports
  accessed_at: '2026-10-21T11:28:21.430225Z'
  snapshot_sha256: d833c0e79dbe1b0485c0cf1a3cb90b851d0237feb62a61a823fecced7ec0deb9
- evidence_id: methods
  kind: primary_source
  reference: PMID:41617698
  locator: Fresh XML Sec13–Sec21 and Sec26
  summary: Methods report exact strains, medium, desiccated inocula, gas-permeable
    reactors, 19-day cultivation and separate flight/ground timelines; leachates were
    measured by ICP-MS.
  support: supports
  accessed_at: '2026-10-21T11:28:21.430315Z'
  snapshot_sha256: d833c0e79dbe1b0485c0cf1a3cb90b851d0237feb62a61a823fecced7ec0deb9
- evidence_id: meteorite
  kind: primary_source
  reference: PMID:41617698
  locator: Fresh XML Sec3/Table 1/Table 2 and Sec14; Figure 2
  summary: Pristine NWA 869 characterization supports the mineral/element inventory;
    ICP-MS/ICP-OES rock measurements are distinct from the liquid-leachate assay.
  support: supports
  accessed_at: '2026-10-21T11:28:21.430407Z'
  snapshot_sha256: d833c0e79dbe1b0485c0cf1a3cb90b851d0237feb62a61a823fecced7ec0deb9
- evidence_id: supplement
  kind: primary_source
  reference: PMID:41617698
  locator: Supplementary Note 1 pp. 2–4; Figures 7–11; Tables 7–9
  summary: The authors infer clean original ISS samples and bound possible contamination
    to Earth fungal samples; post-fixation pH cannot reconstruct the culture pH trajectory.
  support: supports
  accessed_at: '2026-10-21T11:28:21.432046Z'
  snapshot_sha256: ba45d3d6c86298d395d6aec9138abf7689aaab03015fcdcf4b9a57c28d2b02a4
- evidence_id: statistics
  kind: primary_source
  reference: PMID:41617698
  locator: Supplementary Data 1, TUKEY rows 10 and 22; all focal ISS comparison columns
    in scratch audit
  summary: Published p values are 0.0498876 for fungal/non-biological phosphorus and
    0.863164 for consortium/fungal palladium on ISS; no statistical model was rerun.
  support: supports
  accessed_at: '2026-10-21T11:28:21.432134Z'
  snapshot_sha256: c3cc6075ecba1a587edf5b02fdf6d330ae03adeb9cf18f0dd834818080686d19
- evidence_id: catalogue
  kind: authority
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-1078
  locator: Direct DSMZ catalogue lines 159–209, preserved in root-catalogue-web.json
  summary: DSM 1078 currently maps to P. simplicissimum, strain 5696 with collection
    aliases; historical naming and catalogue maintenance conditions do not replace
    the focal identity or protocol.
  support: supports
  accessed_at: '2026-10-21T11:28:21.432176Z'
  snapshot_sha256: 83992cb7dfa498a36c8f03786d2aaa0110144d57f9a6896c88340fd28c446cbd
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, CHEBI and GO
  locator: ontology-authority.json and sodium-pyruvate assessment
  summary: All encoded labels match; ingredient specificity must distinguish sodium
    pyruvate from its pyruvate anion, while element terms do not demonstrate ionic
    speciation.
  support: supports
  accessed_at: '2026-10-21T11:28:21.432600Z'
  snapshot_sha256: 69da9e04a4b3df967bb81373b79136adf3677cf0dd0a26d4feabb9c435e565c3
- evidence_id: salt-candidate
  kind: authority
  reference: CHEBI:50144
  locator: 'sodium-pyruvate-candidate.json: local OAK label, formula, charge and synonyms'
  summary: Verified sodium pyruvate is the sodium salt with formula C3H3O3.Na, distinct
    from pyruvate anion CHEBI:15361.
  support: supports
  accessed_at: '2026-10-21T11:28:21.432869Z'
  snapshot_sha256: fb889c695f33c7e380fa4ad27db9dd82b7234260e8f14abf7e4b0df7f58d0704
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum.PRIMARY_DEGRADER; MetalElementEnum and RareEarthElementEnum
  summary: PRIMARY_DEGRADER means degradation of complex substrates without an organic-only
    restriction; the four metal names omitted from the structured lists are absent
    from the current metal enum.
  support: supports
  accessed_at: '2026-10-21T11:28:21.432872Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  locator: snippet-audit.json
  summary: All 23 snippets match the fresh direct XML and publisher text as well as
    the pinned appended-main cache.
  support: supports
  accessed_at: '2026-10-21T11:28:21.433257Z'
  snapshot_sha256: ed42e13d22c7682ee81873147ef9af9914695f30cf1933a11c5524285176844d
- evidence_id: history
  kind: record_content
  reference: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  locator: provenance-audit.json
  summary: Earlier label and graph repairs remain preserved; generic open backlog
    context is not evidence of a current snippet defect.
  support: supports
  accessed_at: '2026-10-21T11:28:21.433447Z'
  snapshot_sha256: 9db5e8613fc9e5b6b0135aa765c4e4b5f5fd2893eabc6ab1f5e34ce9c91c04af
- evidence_id: resources
  kind: database
  reference: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  locator: dataset-verification.json
  summary: DataShare handle 10283/8889 and DOI 10.7488/ds/7828 identify BioAsteroid
    metabolomics; the preprint identity is verified without equating all versions.
  support: supports
  accessed_at: '2026-10-21T11:28:21.433621Z'
  snapshot_sha256: 612c2bb7ce1e314a9544da0918c9990c14a397d171afe25eab4d966298fe63c8
- evidence_id: native-target
  kind: validation
  reference: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  locator: support-audit.json
  summary: Target network and mechanical metrics are separately recorded; source assessment
    controls biological interpretation.
  support: supports
  accessed_at: '2026-10-21T11:28:21.433769Z'
  snapshot_sha256: ed7948fa71572a3bc4e22dd5181dc330e33e2a271c3ed7e3a51391148fa59e9d
- evidence_id: source-scope
  kind: validation
  reference: PMID:41617698
  locator: source-audit.json
  summary: Whole scientific main and all figure/caption scopes were inspected; large
    archive and sequence/statistical reanalysis remain excluded.
  support: supports
  accessed_at: '2026-10-21T11:28:21.433805Z'
  snapshot_sha256: 851c92556fad00ae81ef2901d630a465957839198a651cf232190d5e2ec0f3ca
- evidence_id: independent-source
  kind: validation
  reference: PMID:41617698
  locator: root-independent-source-audit.json
  summary: Independent source, figure, supplement and authority review supports the
    bounded follow-up.
  support: context_only
  accessed_at: '2026-10-21T11:28:21.433961Z'
  snapshot_sha256: 82c2fcf588a3c7d5d45cd3099a02c3cc7c4d77af91c7f1bdbafbd822ad037294
- evidence_id: search
  kind: search
  reference: Owned maintained roots
  locator: 'local-search.json: ignored-inclusive bounded searches'
  summary: Reusable identity and mapping discovery was limited to the declared roots;
    no global absence is asserted.
  support: supports
  accessed_at: '2026-10-21T11:28:21.434113Z'
  snapshot_sha256: dcf4bb480011be01393cf46dbd1861db8837c40c624687d2722d3d8f6ebf8e70
  search_scope: Ignored-inclusive maintained community, isolate and reusable-taxon
    roots plus recorded mapping-file discovery.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: 'adapter-check.json: same-runtime batch 06 discovery reuse'
  summary: No runnable adapter was available in the owned runtime; no paid provider
    or external runner was used.
  support: supports
  accessed_at: '2026-10-21T11:28:21.434371Z'
  snapshot_sha256: ed8cfd14db32e2daa6cef99022edda6d36bfbe93f6767b0515cf39e22ad6373c
  search_scope: Recorded PATH/venv/module and ignored-inclusive discovery reused in
    the same runtime.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  locator: Actual execution 2026-10-21T11:24:53.519237+00:00 to 2026-10-21T11:24:54.385735+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T11:24:54.385735Z'
  snapshot_sha256: 65db48c1c0c9d2d6cb1d18472d7f8587ca519afef82762857c2038b943635d35
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-strict kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-06/000305/strict-report.tsv
  locator: Actual execution 2026-10-21T11:24:53.519527+00:00 to 2026-10-21T11:24:55.792366+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T11:24:55.792366Z'
  snapshot_sha256: cf2e89bd6bc997682ede68a7d9c1982531e1a58040d1e66d36ce300b3e1ef2e8
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-terms kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  locator: Actual execution 2026-10-21T11:24:53.519663+00:00 to 2026-10-21T11:24:55.342801+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T11:24:55.342801Z'
  snapshot_sha256: bfff938d9736abcb6c8184ee157d8249f8c404b2bb08194bc7905bc3602ce2b8
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  locator: Actual execution 2026-10-21T11:24:54.386064+00:00 to 2026-10-21T11:24:54.474336+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T11:24:54.474336Z'
  snapshot_sha256: 396bf8f91dc0ab28d15ef2d347987935df3a85f21c67dd67d40ac8dcc6a73e23
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb-domain kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  locator: Actual execution 2026-10-21T11:24:54.474572+00:00 to 2026-10-21T11:24:55.852290+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T11:24:55.852290Z'
  snapshot_sha256: 23bc3600b98317befa69b35f0eea84e93a31f2e86e1995fae1626011e0299da7
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-history history/records/BioAsteroid_ISS_Chondrite_Biomining_Consortium
  locator: Actual execution 2026-10-21T11:24:55.343038+00:00 to 2026-10-21T11:24:56.052796+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T11:24:56.052796Z'
  snapshot_sha256: e626dd055959699d12bb867ad46d707d44bc2f938384a6bf201876ef695ad9a3
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T11:24:56.053750+00:00 to 2026-10-21T11:24:56.111459+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T11:24:56.111459Z'
  snapshot_sha256: 2098d1737c723e1a7b7fd4b818272c91543e5de77ea48da6ed7c4711ced80949
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-references-explained kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
  locator: Actual execution 2026-10-21T11:24:56.111683+00:00 to 2026-10-21T11:24:57.109176+00:00
  summary: Target reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T11:24:57.109176Z'
  snapshot_sha256: 70547aba3b234596000221ca35d2fcf649c1e3088703b04d19c2883d2cd20d57
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T10:06:35.990708+00:00 to 2026-10-21T10:06:41.713287+00:00
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; target-native structure has no issue.
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
    and exit 1; target-native structure has no issue.
  support: supports
  accessed_at: '2026-10-21T10:06:41.708376Z'
  snapshot_sha256: 0420f90879ef008b71c8bfcfe444d05d2c030519aca57834b4e2587766c5b854
assessments:
- assessment_id: identity
  area: identity
  topic: Defined consortium, strain and experimental scope
  outcome: supported
  summary: The two-member synthetic biomining model and its structured strain identities
    are supported.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - record
  - methods
  - catalogue
  - ontology
  dimensions:
  - name: community_scope
    value: Defined bacterial–fungal pair with separate monocultures and non-biological
      controls
    definition: The intended roster remains two members; possible contaminants are
      sample-quality caveats, not additional designed members.
    evidence_ids:
    - methods
    - supplement
  - name: source_strain
    value: S. desiccabilis CP1D and P. simplicissimum DSM 1078
    definition: Both strains are source-explicit and structured; DSMZ confirms the
      fungal identity without a current species correction.
    evidence_ids:
    - methods
    - catalogue
  - name: environment
    value: Controlled ISS hardware with terrestrial laboratory comparators
    definition: Laboratory environment and modeled regolith are coherent; the actual
      substrate is crushed NWA 869 meteorite rather than an in-situ asteroid ecosystem.
    evidence_ids:
    - methods
    - meteorite
    - ontology
  - name: medium
    value: 50% v/v R2A, initial pH 7.2, 5 mL
    definition: The source formula and initial pH are valid; final pH after RNAlater
      cannot be substituted for the culture trajectory.
    evidence_ids:
    - methods
    - supplement
  - name: experimental_setting
    value: 19-day ISS and separate ground-control experiments
    definition: Flight incubation logged 19.5 °C versus 20 °C setpoint; Earth controls
      followed a later timeline and no onboard 1g comparison is reported.
    evidence_ids:
    - methods
  - name: evidence_tier
    value: Element concentrations, microscopy and metabolite-feature abundances
    definition: No specific acid necessity, biofilm mediation or bacterial inhibition
      of fungal fitness was selectively demonstrated.
    evidence_ids:
    - leaching
    - colonization
    - antagonism
    - metabolomics
  - name: grounding_status
    value: Valid species/element labels with a salt-versus-anion precision issue
    definition: Species-level taxon grounding remains appropriate; no ionic species
      or exact metabolite mechanism is inferred from elemental measurements.
    evidence_ids:
    - ontology
    - schema
- assessment_id: taxonomy
  area: grounding
  topic: Membership, roles and strain authority
  outcome: supported
  summary: Retain the source-defined pair, current species names and broad degradation
    roles.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - methods
  - catalogue
  - schema
  - ontology
  details: The roles are compatible with the schema’s broad complex-substrate definition
    and source biomining evidence, rather than proof that every treatment outperforms
    every abiotic control. The bacterial basalt/REE snippet is explicitly prior-study
    background, not a measurement from this chondrite assay. Fungal NO_GTDB_EQUIVALENT
    is appropriate; historical mapping-release statistics were not re-certified.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Fungal bioleaching'
  outcome: supported
  summary: Retain the element-specific means and PARTIAL chemistry interpretation.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - leaching
  - statistics
  - metabolomics
  - meteorite
  details: P. simplicissimum DSM 1078 is the participating organism in monoculture-versus-control
    and between-organism comparisons, with ISS/ground conditions kept separate. The
    graph correctly limits most ISS contrasts to nonsignificant mean differences and
    singles out phosphorus. Carboxylic-acid features suggest chemistry without identifying
    a necessary mediator; bulk Pd/V measurements do not resolve ionic species.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Surface colonization'
  outcome: supported
  summary: Retain co-colonization without facilitation or biofilm-to-leaching causation.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - colonization
  - supplement
  - ontology
  details: S. desiccabilis CP1D and P. simplicissimum DSM 1078 appear together on
    the meteorite in consortium samples under both conditions. Morphology supports
    the source’s biofilm interpretation, not quantified growth/transcription kinetics,
    enhanced partner establishment or necessary contact mediation. The three-node
    graph correctly has no downstream arrows.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Candidate bacterial antagonism'
  outcome: supported
  summary: Retain the explicitly PARTIAL S. desiccabilis → P. simplicissimum interpretation.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - antagonism
  - statistics
  - leaching
  details: The direction refers to lower mean palladium extraction by the mixture
    than the fungal monoculture. The ISS comparison is nonsignificant (published p≈0.863);
    it does not measure fungal suppression, reciprocal negative fitness or an upstream
    mediator. No edge to the leaching node should be restored from the same endpoint
    contrast.
- assessment_id: context
  area: evidence
  topic: Comparators, measurements and source caveats
  outcome: concern
  summary: Non-graph summaries should inherit the graph’s statistical and mechanistic
    qualifications and the recovered control caveats.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - methods
  - leaching
  - metabolomics
  - supplement
  - meteorite
  details: 'Parallel treatment arms are not necessarily concurrent experiments: ISS
    samples ran in December 2020–January 2021, ground controls were prepared in March/April
    2021, with n=3 flight and n=4 biological/n=6 non-biological ground samples. Possible
    Earth fungal contamination has unresolved origin and effect; it does not invalidate
    all ISS results. Relative metabolite features are not production-rate measurements.
    Liquid extraction used ICP-MS, whereas pristine-rock characterization also used
    ICP-OES.'
- assessment_id: medium
  area: completeness
  topic: Medium formulation and cultivation representation
  outcome: concern
  summary: The core cultivation settings are supported, with bounded ingredient representation
    gaps.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - methods
  - ontology
  - supplement
  details: Keep 5 mL, 19 days, 20 °C setpoint/19.5 °C logged flight temperature and
    initial pH 7.2. Gas-permeable BMR membranes support aerobic exchange; closed batch
    does not mean hermetically sealed. The 0.15 g/L reagent is sodium pyruvate, while
    CHEBI:15361 denotes its anion. K2HPO4 0.15 g/L and MgSO4·7H2O 0.025 g/L appear
    in correct notes but not the structured composition. Preculture, desiccation,
    fixation and analytical temperatures are distinct stages.
- assessment_id: metals
  area: grounding
  topic: Element inventory and measurement scope
  outcome: supported
  summary: Retain element-level grounding without inferring speciation or universal
    biological enhancement.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - meteorite
  - leaching
  - ontology
  - schema
  details: The source measures the listed metals and reports europium/lutetium bioleaching
    context. Platinum, ruthenium, molybdenum and manganese are source-reported but
    lack the current structured enum values, as the notes state. The inventory does
    not establish a particular oxidation state or that every element improved in the
    consortium under microgravity.
- assessment_id: resources
  area: completeness
  topic: Public metabolomics deposit
  outcome: concern
  summary: The empty associated_datasets list omits a directly reported public study
    deposit.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - resources
  - methods
  details: DataShare DOI 10.7488/ds/7828 and handle 10283/8889 resolve to BioAsteroid_metabolomics.
    Metadata and the complete small README describe prepared ISS/ground samples; its
    1 mL volume is the recovered aliquot, not reactor working volume. The listed 4.05
    GB archive was not downloaded or analyzed; preprint metadata are provenance, not
    interchangeable final-source evidence.
- assessment_id: provenance
  area: provenance
  topic: Exact snippets and previous repairs
  outcome: supported
  summary: Fresh source evidence preserves the earlier qualified graph and canonical
    palladium labels.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - snippets
  - history
  - source-scope
  details: The MD header remains abstract_only despite appended scientific main text.
    All 23 quotations match directly retrieved final-source text; the historical abstract-access
    mismatch backlog does not imply current fabrication. Prior unread-figure/SI statements
    describe that earlier review rather than the current inspection.
- assessment_id: validation
  area: schema
  topic: Native checks and source assessment
  outcome: supported
  summary: All eight native checks pass; source assessment supplies the bounded context
    and precision follow-up.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - source-scope
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality
  outcome: supported
  summary: Mechanical scores do not certify statistical significance or molecular
    mediation.
  target_ids:
  - CommunityMech:000305
  evidence_ids:
  - native-target
  - record
  metrics:
  - name: completeness
    value: 95
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata including all roles +5 environment +10
      at least 3 factors +10 at least 3 nodes +5 resources +10 media +5 datasets +5
      node metabolites). 50+5+10+10+5+10+0+5=95.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50P1-10P2-2P3+20 min(mean node evidence/2,1)+15 if native
      COMPLETE,0,100). P1=0, P2=0, P3=3, P4=0; 6 evidence items/3 nodes gives the
      capped 20 evidence bonus; 100-6+20+15=129 before capping.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count.
  - name: P2
    value: 0
    unit: findings
    definition: Observed native severity count.
  - name: P3
    value: 3
    unit: findings
    definition: Observed native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count.
findings:
- finding_id: experimental-context
  issue_key: cm-000305-experimental-context
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded precision/completeness follow-up preserves
    the identified experiment and qualified graph; it does not establish wrong community
    identity or a false central result.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Clarify comparator and measurement scope
  description: Non-graph summaries omit recoverable statistical/control caveats and
    conflate liquid-leachate with pristine-rock analytical methods.
  target_ids:
  - CommunityMech:000305
  field_paths:
  - description
  - engineering_design.assembly_strategy
  - engineering_design.perturbation_design
  - engineering_design.measurement_endpoints[0]
  - related_ingredients[0].relevance
  - related_ingredients[1].relevance
  - metal_notes
  evidence_ids:
  - methods
  - leaching
  - metabolomics
  - supplement
  - meteorite
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    role: canonical_record
- finding_id: medium-representation
  issue_key: cm-000305-medium-representation
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded precision/completeness follow-up preserves
    the identified experiment and qualified graph; it does not establish wrong community
    identity or a false central result.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Match structured ingredients to the reported formulation
  description: The sodium-pyruvate reagent is mapped to its anion, and two correctly
    transcribed salts remain only in preparation notes.
  target_ids:
  - CommunityMech:000305
  field_paths:
  - growth_media[0].composition[2].chebi_term
  - growth_media[0].composition
  evidence_ids:
  - methods
  - ontology
  - salt-candidate
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    role: canonical_record
- finding_id: metabolomics-data
  issue_key: cm-000305-metabolomics-data
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded precision/completeness follow-up preserves
    the identified experiment and qualified graph; it does not establish wrong community
    identity or a false central result.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Link the public metabolomics dataset
  description: A source-reported, publicly resolvable metabolomics deposit is absent
    from the dataset/resource fields.
  target_ids:
  - CommunityMech:000305
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    role: canonical_record
actions:
- action_id: repair-experimental-context
  description: Clarify comparator and measurement scope.
  finding_ids:
  - experimental-context
  target_ids:
  - CommunityMech:000305
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Use source-supported mean/trend wording and preserve element-specific significance;
    do not turn proposed bacterial antagonism or organic-acid mediation into demonstrated
    partner fitness or causal necessity.
  - State the later ground-control timeline and unequal replication, without presenting
    it as an onboard 1g control or an isolated gravity intervention.
  - Record the supplement’s sample-specific Earth fungal contamination caveat and
    unresolved timing/impact; do not add contaminants to intended membership or label
    all samples contaminated.
  - Distinguish metabolite feature abundance from measured production rate, and liquid-leachate
    ICP-MS from ICP-MS/ICP-OES pristine-rock characterization.
  - Keep initial pH 7.2 distinct from RNAlater-affected endpoint measurements; retain
    all three qualified nodes and zero arrows.
- action_id: repair-medium-representation
  description: Match structured ingredients to the reported formulation.
  finding_ids:
  - medium-representation
  target_ids:
  - CommunityMech:000305
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Use verified CHEBI:50144 sodium pyruvate for the weighed reagent, or explicitly
    distinguish reagent identity from the dissolved pyruvate moiety; preserve the
    source 0.15 g/L amount.
  - Add source-backed structured entries for K2HPO4 0.15 g/L and MgSO4·7H2O 0.025
    g/L, preserving hydration and not doubling the already half-strength formulation.
  - Retain the valid 5 mL, initial pH and incubation context; do not import DSMZ maintenance
    conditions or an unverified CultureMech recipe equivalent.
- action_id: repair-metabolomics-data
  description: Link the public metabolomics dataset.
  finding_ids:
  - metabolomics-data
  target_ids:
  - CommunityMech:000305
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Add DataShare handle 10283/8889 and DOI 10.7488/ds/7828 with the BioAsteroid_metabolomics
    title and liquid-fraction ISS/ground scope.
  - Distinguish prepared sample metadata from validated post-filtering analytical
    coverage; 1 mL README aliquots are not the 5 mL reactors.
  - Do not certify uninspected archive payloads or equate preprint and final-publication
    results; no raw-data rerun is required for this linkage.
- action_id: preserve-qualified-graph
  description: Retain all three qualified nodes and zero arrows during separately
    authorized follow-up.
  finding_ids:
  - experimental-context
  - medium-representation
  - metabolomics-data
  target_ids:
  - CommunityMech:000305
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioAsteroid_ISS_Chondrite_Biomining_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Keep mean leaching, statistical contrasts, biofilm observations and candidate
    mechanisms distinct.
  - Do not restore biofilm-to-leaching or antagonism-to-leaching edges from observations
    of the same endpoint.
  - Preserve append-only history and rerun schema, strict, term, reference, history
    and target/corpus network checks after authorized curation.
limitations:
- No raw metabolomics archive, peak processing, statistical model or sequence alignment
  was rerun; the 4.05 GB deposit payload was not downloaded.
- Supplementary Data 1 inspection was bounded to workbook inventory/headers and published
  focal comparison columns; other raw-data rows were not exhaustively assessed. Table
  8 sequences were not independently used to identify contaminants.
- Possible Earth fungal contamination has unresolved timing and influence. The authors
  infer original ISS samples were clean; this assessment does not establish absolute
  sterility or add contaminants as designed members.
- Separate Earth and ISS timelines, sample counts and processing caveats limit an
  isolated gravity-causation interpretation. Endpoint pH after RNAlater does not establish
  the culture pH trajectory.
- Broad biofilm and chemical annotations do not prove molecular mediation, partner
  fitness or ionic speciation. No exact CultureMech recipe equivalence was verified.
- Preprint bibliographic identity was verified; preprint scientific content was not
  substituted for the final publication. Catalogue maintenance conditions and historical
  GTDB-release statistics were not re-certified as experimental conditions.
notes:
- No canonical, cache, history or generated file changed.
- All 24 repository inputs were pinned before assessment and rechecked.
- Eleven quoted words from the focal publication, including the total budget for its
  supplements.
- Native quality 100 is capped from 129; source findings remain actionable.
tags:
- record-review
- biomining
- spaceflight
- batch-06
```
