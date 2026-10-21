# Arabidopsis Coumarin Root SynCom: whole-record source review

- Review: 20261021T065553Z-arabidopsis-coumarin-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T06:51:11.765264Z
- Finished UTC: 2026-10-21T06:55:53.017700Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two major findings concern the parent-coumarin ingredient identity and an unqualified description of root peroxide mediation. Three minor findings concern environment fields, live-host evidence types and medium identifiers. All four nodes and three qualified arrows are supported. Eight focused gates pass and seventeen snippets match the primary cache; fresh metadata verifies source identity, while complete full-text freshness remains unverified.

## Scope And Provenance

Entire record, nested taxonomy, four nodes and three arrows, all metadata and seventeen evidence occurrences, cached main primary article and fresh publication metadata. Complete strain inventory, supplements, raw data and figure geometry were not audited.

Selection: Next uncovered path after Arabidopsis Bacillus Biocontrol SynCom150 in batch03; one resolved maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ade4a9acdc245e1090522bb4f6ec5fe82ee88689.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000094 | kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml | maintained | Arabidopsis Coumarin Root SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000094 | Schema validation passed for the target. |
| validate-strict | passed | True | CommunityMech:000094 | Strict closed-schema and cross-field validation passed for the target. |
| validate-terms | passed | True | CommunityMech:000094 | Native ontology-term validation passed for the target. |
| validate-gtdb | passed | True | CommunityMech:000094 | GTDB structural validation passed without certifying an isolate-level crosswalk. |
| validate-gtdb-domain | passed | True | CommunityMech:000094 | GTDB domain validation passed for the target. |
| validate-history | passed | True | CommunityMech:000094 | The target history sidecar passed native validation. |
| normalize-cache-names-check | passed | True | CommunityMech:000094 | Read-only reference-cache filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000094 | Native reference validation passed with committed cache hashes unchanged. |
| audit-network | failed | True | CommunityMech:000094 | Earlier correct-runtime corpus run retained: 477 records, 57 warnings across 21 records, zero errors and exit 1; this target was not listed. |
| check-network-quality | failed | True | CommunityMech:000094 | Earlier correct-runtime corpus run retained: 477 records, 57 warnings across 21 records, zero errors and exit 1; this target was not listed. |
| Independent publication identity | passed | True | CommunityMech:000094 | Fresh PubMed and Crossref metadata confirm the cited article and identifiers. |
| Independent complete full-text retrieval | unavailable | False | CommunityMech:000094 | Fresh complete article retrieval was unavailable, so scientific assessment uses the intact provenance-marked primary cache. |
| Optional structured source adapter availability | unavailable | False | CommunityMech:000094 | No runner was available in the owned runtime, and no expression-module catalog coverage was established. |

## Scientific And Domain Assessments

### Hydroponic 22-member SynCom and focal Root329 strain

identity: supported. Targets: CommunityMech:000094.

The source and experimental community are resolved. Bacteria is an aggregate and Root329 is a focal member; neither the whole roster nor a two-member community is asserted.

### Taxonomy, strain designation and GTDB scope

grounding: supported. Targets: CommunityMech:000094.

NCBI domain and genus IDs fit the explicitly nested descriptors; no functional role is invented for the heterogeneous aggregate or coumarin-sensitive focal strain. Genus-level GTDB majority mapping is not an isolate-genome crosswalk.

### Description peroxide-mediation claim

evidence: concern. Targets: CommunityMech:000094.

The description presents peroxide-linked suppression as contributing to the root profile without carrying the candidate-mechanism and relative-abundance limits already preserved in the graph and discussion.

### ecological_interactions[0]: Iron-Limited Catecholic Coumarin Exudation

graph: supported. Targets: CommunityMech:000094.

Root catecholic-coumarin release is supported.

Participants: Arabidopsis roots and downstream microbial community; direction: iron limitation and plant biosynthesis/export toward compound release, without implying reciprocal competition. Linked primary evidence supplies the source locator and bounded excerpt.

### ecological_interactions[1]: Catecholic Coumarin Peroxide Generation

graph: supported. Targets: CommunityMech:000094.

Cell-free peroxide production is supported.

Participants: purified catecholic coumarins in iron-deficient MS; direction: chemical redox activity toward peroxide generation. COMMUNITY_LEVEL is a graph grouping, not evidence that bacteria catalyze this chemistry. Linked primary evidence supplies the source locator and bounded excerpt.

### ecological_interactions[2]: Pseudomonas Root329 Coumarin Sensitivity

graph: supported. Targets: CommunityMech:000094.

Strain-specific inhibition and rescue are supported.

Participants: Root329 and tested compounds on nutrient agar; direction: compound exposure toward inhibited growth, modified by catalase and soluble iron. Neither a genus-wide response nor a specific bacterial regulator is established. Linked primary evidence supplies the source locator and bounded excerpt.

### ecological_interactions[3]: Pseudomonas-Weighted Coumarin Community Shift

graph: supported. Targets: CommunityMech:000094.

Qualified root-community compositional response is supported.

Participants: hydroponic Arabidopsis, full or experimentally reduced SynComs and Root329; direction: host coumarin perturbation/supplementation toward relative-abundance changes. In-silico rescaling is not physical dropout or proof of absolute depletion. Linked primary evidence supplies the source locator and bounded excerpt.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000094.

Exudation supplies the chemical species tested separately.

Source roots release the named catechols, which generate peroxide in cell-free MS. The edge explicitly does not claim a root-local peroxide measurement. Direction and context remain bounded by the current edge wording.

### ecological_interactions[1].downstream[0]

graph: supported. Targets: CommunityMech:000094.

The partial peroxide-to-inhibition link is supported.

Peroxide production and catalase rescue support involvement in Root329 inhibition across separate assays; a direct chemical flux at roots is not established. Direction and context remain bounded by the current edge wording.

### ecological_interactions[2].downstream[0]

graph: supported. Targets: CommunityMech:000094.

The partial sensitivity-to-community link is supported as a candidate explanation.

Root329 inhibition in vitro and its host-associated relative-abundance response are consistent with the proposed mechanism. The edge explicitly preserves unresolved intact-root peroxide mediation and absolute depletion. Direction and context remain bounded by the current edge wording.

### All graph metabolites, related ingredients and GO process

grounding: concern. Targets: CommunityMech:000094.

Graph coumarins use the correct class with named-compound limits; peroxide and oxidative-stress response fit the assays. Ferric iron fits source mobilization and FeCl3/Fe-EDTA manipulations without proving every iron pool. Only the separate parent-coumarin ingredient conflates molecule and class.

### Ecological state, category, engineering design and environment

scope: concern. Targets: CommunityMech:000094.

ENGINEERED, SYNTHETIC and root-associated category fit the design; soil rhizosphere should be separated from the physical hydroponic setting. The assembly-design factor is metadata duplicated from engineering_design rather than a measured environmental condition.

### Non-graph evidence_source values

provenance: concern. Targets: CommunityMech:000094.

Several snippets explicitly describe living plant roots but are typed IN_VITRO, unlike the correctly typed root-response graph nodes; cultured-inoculum, cell-free and agar evidence remain IN_VITRO.

### Growth media and experimental conditions

completeness: concern. Targets: CommunityMech:000094.

The combined entry distinguishes bacterial TSB preparation from plant hydroponics in its notes, and its reported timing is source-backed. External recipe identifiers remain absent; uninspected supplement details should not be inferred.

### Plant genes, microbial roles and expression-module applicability

scope: supported. Targets: CommunityMech:000094.

F6-prime-H1 and other plant mutants define host perturbations, not identified bacterial effectors. No bacterial transcriptomic module or protein-level mechanism is asserted.

### External resources and datasets

completeness: supported. Targets: CommunityMech:000094.

No dataset accession is encoded; the bounded cached-text search found no common BioProject/GEO/SRA-style accession, which does not establish global absence. Supplementary materials and full strain identities were not independently audited.

### History, cache and open discussion

provenance: supported. Targets: CommunityMech:000094.

The valid target sidecar and prior decision preserve qualified causal interpretation; all snippets match cache, with fresh abstract confirmation for six occurrences and explicit full-text access limitations.

### Iron and metal-related assertions

scope: supported. Targets: CommunityMech:000094.

Iron availability and ferric-iron mobilization are relevant context for coumarin chemistry; the record does not establish microbial iron uptake, siderophore exchange, metal recovery or rare-earth processing.

### Native gates and independent checks

schema: supported. Targets: CommunityMech:000094.

Eight focused checks passed, eight ID-label pairs match and seventeen snippets match cached primary text; corpus warning failures and fresh full-text unavailability remain explicit.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000094.

Completeness 30 reflects sparse structured metadata and absent roles; quality 100 is not scientific approval.

## Findings

### parent-coumarin: Parent coumarin is substituted for the coumarins class

major / open / confirmed; issue key: cm-000094-parent-coumarin.

CHEBI:28794 correctly labels the specific molecule coumarin, but related_ingredients[0] uses it for class-wide biosynthesis and named substituted compounds. This differs from the graph's correct CHEBI:23403 class and can create a wrong compound join.

### root-mediation: Description omits the root-mediation qualification

major / open / confirmed; issue key: cm-000094-root-mediation.

The description turns the cross-assay peroxide-linked explanation into an unqualified contribution to the root community profile. Source interpretation and current arrows distinguish relative abundance, in-vitro inhibition and unresolved peroxide mediation in the intact community.

### experimental-environment: Actual hydroponic environment and modeled rhizosphere are conflated

minor / open / confirmed; issue key: cm-000094-experimental-environment.

The formal environment is root-influenced soil even though the studied community is hydroponic. A separate factor records assembly design rather than an environmental parameter. Source habitat and experimental design remain clear in prose but are misplaced in structured fields.

### host-evidence-source: Live-host root evidence is labeled IN_VITRO outside the graph

minor / open / confirmed; issue key: cm-000094-host-evidence-source.

Explicit root-community responses and hydroponic seedling inoculation are host-associated experiments under the schema, yet their non-graph evidence uses IN_VITRO. The corresponding graph correctly distinguishes IN_VIVO and COMPUTATIONAL evidence.

### media-linkage: Source-supported media lack external identifiers

minor / open / confirmed; issue key: cm-000094-media-linkage.

The growth entry records TSB preparation and hydroponic MS context but provides no CultureMech or MediaIngredientMech identifier.

## Recommended Actions And Acceptance Checks

### fix-parent-coumarin

Ground the maintained class assertion as coumarins, or separately verify the named compounds and represent them at their actual chemical identities.

- No parent molecule is treated as equivalent to the whole class or its derivatives.
- Relevance, evidence and chemical ID share the same scope.
- Run strict, term and reference checks.

### fix-root-mediation

Carry the candidate-mechanism and relative-abundance qualifications into the description while preserving demonstrated chemistry, inhibition and root-composition effects.

- Description agrees with the three qualified arrows and open discussion.
- No absolute depletion or measured root-local peroxide mediation is asserted.
- Run strict and reference checks.

### fix-experimental-environment

Represent the physical study setting and modeled rhizosphere distinctly, and keep assembly metadata in engineering_design.

- The actual study setting does not imply soil cultivation.
- Root-isolate origin and modeled habitat are retained.
- Iron-deficiency context is preserved.
- Run strict and term checks.

### fix-host-evidence-source

Use IN_VIVO for the explicit living-host observations and review shared design snippets in context; retain IN_VITRO for bacterial preparation, cell-free chemistry and agar inhibition.

- Each evidence type follows its actual experiment rather than the laboratory location.
- Computational rescaling remains COMPUTATIONAL.
- Quoted text and source boundaries remain intact.
- Run strict and reference checks.

### fix-media-linkage

Link exact compatible medium or ingredient entries where available, retaining separate inoculum and host-cultivation contexts.

- Linked formulations match the reported preparation and assay.
- No missing supplement recipe or growth condition is invented.
- Run focused medium/linkage checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml; Whole record: two nested taxonomic descriptors, four nodes, three arrows and seventeen evidence occurrences | supports | The target represents a 22-member hydroponic root SynCom with a focal Root329 isolate, not a two-member assembly. |
| primary | PMID:31152139; https://pmc.ncbi.nlm.nih.gov/articles/PMC6589675/; committed references_cache/PMID_31152139.txt, full-text section attributed to PMC6589675.html | supports | The intact cached primary main text, Methods, Results, Discussion and figure captions were read. Fresh metadata confirms identity, but independent full-text freshness was not verified; supplements, raw data and figure geometry were not inspected. |
| identity | PMID:31152139; Cached Results: initial SynCom design and strain establishment; Fig. 1 caption | supports | The source designed 22 distinguishable root-endophyte isolates from Cologne loamy soil and inoculated hydroponic Arabidopsis seedlings. Members establish unevenly; the aggregate descriptor does not claim equal abundance or list all isolates. |
| exudation | PMID:31152139; Cached Results: iron-deficiency community shifts; Fig. 3A caption | supports | Iron-deficient roots release sideretin, fraxetin and esculetin. Biosynthesis and export mutants implicate catecholic coumarins; fro2 controls distinguish the community effect from generic host iron deficiency. |
| chemistry | PMID:31152139; Cached Results: Pseudomonas Root329 growth inhibition, peroxide paragraph; Fig. 4C caption | supports | The named catecholic compounds generate peroxide over 24 hours in iron-deficient MS medium. Cell-free chemistry and the separate agar-rescue assays do not directly measure peroxide at colonized roots. |
| sensitivity | PMID:31152139; Cached Results: purified-compound halo inhibition and catalase/soluble-iron rescue; Fig. 4B-D captions | supports | Sideretin strongly and fraxetin more weakly inhibit Root329; catalase abolishes sideretin inhibition and soluble iron reduces it. Responses vary among closely related pseudomonads, so no genus-wide susceptibility follows. |
| composition | PMID:31152139; Cached Results: robustness across community compositions and chemical complementation; Fig. 4A caption | supports | Root329 relative abundance responds to plant coumarin production and supplementation. Computational omission reduces the profile difference, while distinct reduced-community experiments retain the response. Scopoletin supplementation can be converted by the plant. |
| mediation | PMID:31152139; Cached Significance, Abstract and Discussion, second paragraph; current graph and open discussion | supports | The authors propose a redox mechanism and interpret root relative-abundance shifts through the separate inhibition results. They do not establish root-local peroxide mediation or absolute Root329 depletion; the graph explicitly preserves these limits. |
| chemical-scope | PMID:31152139; Cached Results: Fig. 3A and purified-compound/peroxide paragraphs | supports | Activity concerns specific substituted coumarins. The source contrasts peroxide-generating catechols with compounds lacking the relevant redox functionality; unsubstituted parent coumarin is not interchangeable with this class. |
| culture | PMID:31152139; Cached Results: hydroponic design and Fig. 1 caption; final Materials and Methods; Fig. 4 assay captions | supports | Quarter-strength TSB and a PBS wash prepare the bacterial inoculum; 13-day hydroponic seedlings are inoculated and root communities profiled around day 20. Plant-associated assays, cell-free MS chemistry and nutrient-agar inhibition are separate contexts. Detailed recipes and the complete strain roster are delegated to the uninspected supplement. |
| schema | src/communitymech/schema/communitymech.yaml; EvidenceSourceEnum, environment_term/modeled_environment and RelatedIngredient definitions | supports | IN_VIVO includes host-associated experiments, while IN_VITRO includes culture assays. The physical study environment differs from the modeled habitat. CHEBI ingredient identity serves an equivalence-safe compound join. |
| ontology | Local OAK NCBITaxon, ENVO, GO and CHEBI snapshots; Eight distinct ID-label pairs across seventeen occurrences; compound identity, rank and definition checks | supports | Every label matches its ID. CHEBI:28794 denotes the specific parent molecule and is not equivalent to the CHEBI:23403 class; ENVO rhizosphere denotes root-influenced soil. Root329 remains genus-grounded, and a genus-level GTDB majority does not independently assign its genome. |
| snippets | kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml; Seventeen evidence field occurrences against the committed cache and fresh PubMed abstract | supports | All seventeen match cached primary text after NFKC/whitespace normalization; six also match the independently retrieved abstract. No fresh complete article body was obtained, so cache matches are not reported as fresh full-text verification. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=31152139&amp;retmode=xml; Independent public metadata | supports | PMID 31152139 and DOI 10.1073/pnas.1820691116 identify the cited Voges et al. PNAS article on plant-derived coumarins and the Arabidopsis synthetic root microbiome. |
| crossref | https://api.crossref.org/works/10.1073/pnas.1820691116; Independent public metadata | supports | PMID 31152139 and DOI 10.1073/pnas.1820691116 identify the cited Voges et al. PNAS article on plant-derived coumarins and the Arabidopsis synthetic root microbiome. |
| access-fulltext | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6589675/fullTextXML; Actual public full-text access attempt | supports | Europe PMC returned HTTP 500. |
| access-fulltext-europe-retry | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6589675/fullTextXML; Actual public full-text access attempt | supports | Europe PMC returned HTTP 500. |
| access-fulltext-ncbi | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&amp;id=6589675; Actual public full-text access attempt | supports | NCBI returned HTTP 200 front matter and abstract with an explicit full-text XML restriction, not an article body. |
| history | history/records/Arabidopsis_Coumarin_Root_SynCom/2026-10-05T101148Z-codex-29d547.yaml; reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml; One target sidecar and target decision at lines 99-163, independently inspected | supports | Prior curation separates cell-free chemistry, agar inhibition, plant composition and computational rescaling; the current graph retains its partial-mediation qualifications and open question. |
| local-search | references_cache; history; reports/causal_graph_review/decisions; kb/taxa; Record slug, PMID and ID search including ignored and hidden files | supports | The bounded search located the cache, target history and prior decision; it does not establish absence of all reusable taxon records or public datasets. |
| adapter | Optional kg-microbe-sources runner discovery; Same-runtime discovery receipt reused with its original timestamp | supports | No runner was available in the owned runtime; a candidate in another checkout was not executed. No expression-module coverage was queried or inferred for Root329. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml; Actual execution 2026-10-21T06:51:12.913100+00:00 to 2026-10-21T06:51:15.654893+00:00 | supports | Schema validation passed for the target. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-strict kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml --out /private/tmp/cm-review-session/batch-03/000094/strict-report.tsv; Actual execution 2026-10-21T06:51:12.916140+00:00 to 2026-10-21T06:51:17.818877+00:00 | supports | Strict closed-schema and cross-field validation passed for the target. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-terms kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml; Actual execution 2026-10-21T06:51:12.918334+00:00 to 2026-10-21T06:51:17.218902+00:00 | supports | Native ontology-term validation passed for the target. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml; Actual execution 2026-10-21T06:51:15.655322+00:00 to 2026-10-21T06:51:15.784627+00:00 | supports | GTDB structural validation passed without certifying an isolate-level crosswalk. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb-domain kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml; Actual execution 2026-10-21T06:51:15.784902+00:00 to 2026-10-21T06:51:17.882731+00:00 | supports | GTDB domain validation passed for the target. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-history history/records/Arabidopsis_Coumarin_Root_SynCom; Actual execution 2026-10-21T06:51:17.219238+00:00 to 2026-10-21T06:51:18.127210+00:00 | supports | The target history sidecar passed native validation. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T06:51:18.128428+00:00 to 2026-10-21T06:51:18.211945+00:00 | supports | Read-only reference-cache filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-references-explained kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml; Actual execution 2026-10-21T06:51:18.212398+00:00 to 2026-10-21T06:51:19.438121+00:00 | supports | Native reference validation passed with committed cache hashes unchanged. |
| check-audit-network | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv audit-network; Actual finish 2026-10-20T07:08:14.467705+00:00 | supports | Earlier correct-runtime corpus run retained: 477 records, 57 warnings across 21 records, zero errors and exit 1; this target was not listed. |
| check-check-network-quality | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv check-network-quality; Actual finish 2026-10-20T07:08:13.673449+00:00 | supports | Earlier correct-runtime corpus run retained: 477 records, 57 warnings across 21 records, zero errors and exit 1; this target was not listed. |
| native-target | NetworkIntegrityAuditor().audit_community(target); Independent fresh read-only API check and native metric components in support-audit.json | supports | No target issue returned; six interaction evidence items across four nodes yield mean 1.5, and three arrows remain qualified. |

## Limits And Additional Notes

- Primary full-text assessment uses the intact committed cache attributed to PMC HTML. Europe PMC returned HTTP 500; NCBI supplied restricted front matter without an article body. Fresh PubMed/Crossref identity and abstract verification do not establish independent full-text freshness.
- The source supplement and spreadsheet were listed but not retrieved; the complete 22-isolate inventory, detailed recipes and supplement-only measurements are not certified. Main-text claims in the current aggregate representation remain assessable.
- Figure captions and main-text results were read, but figure geometry, raw counts and chemical measurements were not independently reanalyzed.
- GTDB validators check structural grounding and domain; historical crosswalk counts and the precise genome assignment of Root329 were not independently reproduced.
- The mechanism remains qualified across cell-free, agar, live-host and computational contexts; root-local peroxide mediation and absolute Root329 depletion remain unresolved.
- Optional structured-expression adapter discovery was reused with its original timestamp; another checkout candidate was not executed and no expression-module coverage was established.
- Required corpus checks retain their actual warning failures; clean target diagnostics and numeric scores do not establish scientific truth.
- Canonical records, caches, history and generated outputs remain unchanged.
- Source quotations total 21 words.
- No complete fresh full-text retrieval or supplement inspection is claimed.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T065553Z-arabidopsis-coumarin-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Arabidopsis Coumarin Root SynCom: whole-record source review'
started_at: '2026-10-21T06:51:11.765264Z'
finished_at: '2026-10-21T06:55:53.017700Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Canonical target unchanged in this session; prior codex curation
    prevents person-level independence claims. Separate agents checked ontology, cache
    boundaries, snippets, history and native metrics; root also inspected the primary
    text.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Two major findings concern the parent-coumarin ingredient identity and an
  unqualified description of root peroxide mediation. Three minor findings concern
  environment fields, live-host evidence types and medium identifiers. All four nodes
  and three qualified arrows are supported. Eight focused gates pass and seventeen
  snippets match the primary cache; fresh metadata verifies source identity, while
  complete full-text freshness remains unverified.
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
  - path: history/records/Arabidopsis_Coumarin_Root_SynCom/2026-10-05T101148Z-codex-29d547.yaml
    sha256: 7b7ad37c44aa8060027c333b70943eb8648ab365d1c72b362e600c3f70136131
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    sha256: 5886a0fe0ac3d47e69b0e2f0c0875e551446aa459b079dd8270d1ebcb6188f13
    role: target
  - path: references_cache/PMID_31152139.txt
    sha256: cd070a870cadc9e56af1f97b8d2fbc9f37f061d0cf51d87e186ff0febeb9be07
    role: context
  - path: reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml
    sha256: 5076ec8295dacfaae0ae1d829836e4380a312a702c4a43df5f604c3b1b1e0ad3
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
- target_id: CommunityMech:000094
  path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  label: Arabidopsis Coumarin Root SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
scope:
  description: Entire record, nested taxonomy, four nodes and three arrows, all metadata
    and seventeen evidence occurrences, cached main primary article and fresh publication
    metadata. Complete strain inventory, supplements, raw data and figure geometry
    were not audited.
  selection: Next uncovered path after Arabidopsis Bacillus Biocontrol SynCom150 in
    batch03; one resolved maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000094
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed for the target.
  target_ids:
  - CommunityMech:000094
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history check or read-only cache preflight; no canonical
    cache changes.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict closed-schema and cross-field validation passed for the target.
  target_ids:
  - CommunityMech:000094
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-03/000094/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history check or read-only cache preflight; no canonical
    cache changes.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Native ontology-term validation passed for the target.
  target_ids:
  - CommunityMech:000094
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history check or read-only cache preflight; no canonical
    cache changes.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB structural validation passed without certifying an isolate-level crosswalk.
  target_ids:
  - CommunityMech:000094
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history check or read-only cache preflight; no canonical
    cache changes.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed for the target.
  target_ids:
  - CommunityMech:000094
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history check or read-only cache preflight; no canonical
    cache changes.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: The target history sidecar passed native validation.
  target_ids:
  - CommunityMech:000094
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Arabidopsis_Coumarin_Root_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history check or read-only cache preflight; no canonical
    cache changes.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only reference-cache filename preflight passed.
  target_ids:
  - CommunityMech:000094
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history check or read-only cache preflight; no canonical
    cache changes.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Native reference validation passed with committed cache hashes unchanged.
  target_ids:
  - CommunityMech:000094
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history check or read-only cache preflight; no canonical
    cache changes.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Earlier correct-runtime corpus run retained: 477 records, 57 warnings
    across 21 records, zero errors and exit 1; this target was not listed.'
  target_ids:
  - CommunityMech:000094
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Actual earlier batch03 corpus gate reused with unchanged canonical inputs;
    a fresh target API diagnostic does not replace it.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Earlier correct-runtime corpus run retained: 477 records, 57 warnings
    across 21 records, zero errors and exit 1; this target was not listed.'
  target_ids:
  - CommunityMech:000094
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Actual earlier batch03 corpus gate reused with unchanged canonical inputs;
    a fresh target API diagnostic does not replace it.
- check_id: public-source-identity
  name: Independent publication identity
  status: passed
  required: true
  summary: Fresh PubMed and Crossref metadata confirm the cited article and identifiers.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - pubmed
  - crossref
- check_id: fresh-fulltext
  name: Independent complete full-text retrieval
  status: unavailable
  required: false
  summary: Fresh complete article retrieval was unavailable, so scientific assessment
    uses the intact provenance-marked primary cache.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - primary
  - access-fulltext
  - access-fulltext-europe-retry
  - access-fulltext-ncbi
- check_id: structured-expression-adapter
  name: Optional structured source adapter availability
  status: unavailable
  required: false
  summary: No runner was available in the owned runtime, and no expression-module
    catalog coverage was established.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  locator: 'Whole record: two nested taxonomic descriptors, four nodes, three arrows
    and seventeen evidence occurrences'
  summary: The target represents a 22-member hydroponic root SynCom with a focal Root329
    isolate, not a two-member assembly.
  support: supports
  accessed_at: '2026-10-21T06:55:53.012900Z'
- evidence_id: primary
  kind: primary_source
  reference: PMID:31152139
  locator: https://pmc.ncbi.nlm.nih.gov/articles/PMC6589675/; committed references_cache/PMID_31152139.txt,
    full-text section attributed to PMC6589675.html
  summary: The intact cached primary main text, Methods, Results, Discussion and figure
    captions were read. Fresh metadata confirms identity, but independent full-text
    freshness was not verified; supplements, raw data and figure geometry were not
    inspected.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013137Z'
  snapshot_sha256: cd070a870cadc9e56af1f97b8d2fbc9f37f061d0cf51d87e186ff0febeb9be07
- evidence_id: identity
  kind: primary_source
  reference: PMID:31152139
  locator: 'Cached Results: initial SynCom design and strain establishment; Fig. 1
    caption'
  summary: The source designed 22 distinguishable root-endophyte isolates from Cologne
    loamy soil and inoculated hydroponic Arabidopsis seedlings. Members establish
    unevenly; the aggregate descriptor does not claim equal abundance or list all
    isolates.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013146Z'
  quote: 22-member SynCom
- evidence_id: exudation
  kind: primary_source
  reference: PMID:31152139
  locator: 'Cached Results: iron-deficiency community shifts; Fig. 3A caption'
  summary: Iron-deficient roots release sideretin, fraxetin and esculetin. Biosynthesis
    and export mutants implicate catecholic coumarins; fro2 controls distinguish the
    community effect from generic host iron deficiency.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013148Z'
  quote: major coumarins exuded
- evidence_id: chemistry
  kind: primary_source
  reference: PMID:31152139
  locator: 'Cached Results: Pseudomonas Root329 growth inhibition, peroxide paragraph;
    Fig. 4C caption'
  summary: The named catecholic compounds generate peroxide over 24 hours in iron-deficient
    MS medium. Cell-free chemistry and the separate agar-rescue assays do not directly
    measure peroxide at colonized roots.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013150Z'
  quote: Hydrogen peroxide was generated
- evidence_id: sensitivity
  kind: primary_source
  reference: PMID:31152139
  locator: 'Cached Results: purified-compound halo inhibition and catalase/soluble-iron
    rescue; Fig. 4B-D captions'
  summary: Sideretin strongly and fraxetin more weakly inhibit Root329; catalase abolishes
    sideretin inhibition and soluble iron reduces it. Responses vary among closely
    related pseudomonads, so no genus-wide susceptibility follows.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013151Z'
  quote: addition of catalase
- evidence_id: composition
  kind: primary_source
  reference: PMID:31152139
  locator: 'Cached Results: robustness across community compositions and chemical
    complementation; Fig. 4A caption'
  summary: Root329 relative abundance responds to plant coumarin production and supplementation.
    Computational omission reduces the profile difference, while distinct reduced-community
    experiments retain the response. Scopoletin supplementation can be converted by
    the plant.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013152Z'
  quote: in silico rescaling
- evidence_id: mediation
  kind: primary_source
  reference: PMID:31152139
  locator: Cached Significance, Abstract and Discussion, second paragraph; current
    graph and open discussion
  summary: The authors propose a redox mechanism and interpret root relative-abundance
    shifts through the separate inhibition results. They do not establish root-local
    peroxide mediation or absolute Root329 depletion; the graph explicitly preserves
    these limits.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013153Z'
  quote: could be due
- evidence_id: chemical-scope
  kind: primary_source
  reference: PMID:31152139
  locator: 'Cached Results: Fig. 3A and purified-compound/peroxide paragraphs'
  summary: Activity concerns specific substituted coumarins. The source contrasts
    peroxide-generating catechols with compounds lacking the relevant redox functionality;
    unsubstituted parent coumarin is not interchangeable with this class.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013154Z'
  quote: scopoletin or isofraxidin
- evidence_id: culture
  kind: primary_source
  reference: PMID:31152139
  locator: 'Cached Results: hydroponic design and Fig. 1 caption; final Materials
    and Methods; Fig. 4 assay captions'
  summary: Quarter-strength TSB and a PBS wash prepare the bacterial inoculum; 13-day
    hydroponic seedlings are inoculated and root communities profiled around day 20.
    Plant-associated assays, cell-free MS chemistry and nutrient-agar inhibition are
    separate contexts. Detailed recipes and the complete strain roster are delegated
    to the uninspected supplement.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013155Z'
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: EvidenceSourceEnum, environment_term/modeled_environment and RelatedIngredient
    definitions
  summary: IN_VIVO includes host-associated experiments, while IN_VITRO includes culture
    assays. The physical study environment differs from the modeled habitat. CHEBI
    ingredient identity serves an equivalence-safe compound join.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013156Z'
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, GO and CHEBI snapshots
  locator: Eight distinct ID-label pairs across seventeen occurrences; compound identity,
    rank and definition checks
  summary: Every label matches its ID. CHEBI:28794 denotes the specific parent molecule
    and is not equivalent to the CHEBI:23403 class; ENVO rhizosphere denotes root-influenced
    soil. Root329 remains genus-grounded, and a genus-level GTDB majority does not
    independently assign its genome.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013473Z'
  snapshot_sha256: 1a3ac600c2c380dd2530d17da60f021e23cfc3966b752ef76afa16a58197fbca
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  locator: Seventeen evidence field occurrences against the committed cache and fresh
    PubMed abstract
  summary: All seventeen match cached primary text after NFKC/whitespace normalization;
    six also match the independently retrieved abstract. No fresh complete article
    body was obtained, so cache matches are not reported as fresh full-text verification.
  support: supports
  accessed_at: '2026-10-21T06:55:53.013702Z'
  snapshot_sha256: d5ee23aa85b86ff9a0258c237b6cf50794a7a12ec2be3ef549e8d0e70346ab44
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=31152139&retmode=xml
  locator: Independent public metadata
  summary: PMID 31152139 and DOI 10.1073/pnas.1820691116 identify the cited Voges
    et al. PNAS article on plant-derived coumarins and the Arabidopsis synthetic root
    microbiome.
  support: supports
  accessed_at: '2026-10-21T06:51:32.808334Z'
  snapshot_sha256: 2d01687e9f336bc95c72b3edb413be13ebaf573cfd91a0b8ed7da633cdba9ed9
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1073/pnas.1820691116
  locator: Independent public metadata
  summary: PMID 31152139 and DOI 10.1073/pnas.1820691116 identify the cited Voges
    et al. PNAS article on plant-derived coumarins and the Arabidopsis synthetic root
    microbiome.
  support: supports
  accessed_at: '2026-10-21T06:51:32.808880Z'
  snapshot_sha256: 5583aced346a220a03467b480fed1faf5e18603feb29139e67726009d11d6bf7
- evidence_id: access-fulltext
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6589675/fullTextXML
  locator: Actual public full-text access attempt
  summary: Europe PMC returned HTTP 500.
  support: supports
  accessed_at: '2026-10-21T06:51:32.806846Z'
  snapshot_sha256: 1194a6053c9c25d2866da7bd5164f2f72e3f206f73146ba7e76545421566f2ae
- evidence_id: access-fulltext-europe-retry
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6589675/fullTextXML
  locator: Actual public full-text access attempt
  summary: Europe PMC returned HTTP 500.
  support: supports
  accessed_at: '2026-10-21T06:51:51.989335Z'
  snapshot_sha256: fc5ff9bfde2604f803d2f96aa1a1166aff5abafd15f7a530975566b4257ae90f
- evidence_id: access-fulltext-ncbi
  kind: validation
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=6589675
  locator: Actual public full-text access attempt
  summary: NCBI returned HTTP 200 front matter and abstract with an explicit full-text
    XML restriction, not an article body.
  support: supports
  accessed_at: '2026-10-21T06:51:51.988226Z'
  snapshot_sha256: ed3d1245205768ce3bd5a9d26decbad8d00dbc077fc8775a37679e24ee9459b5
- evidence_id: history
  kind: record_content
  reference: history/records/Arabidopsis_Coumarin_Root_SynCom/2026-10-05T101148Z-codex-29d547.yaml;
    reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml
  locator: One target sidecar and target decision at lines 99-163, independently inspected
  summary: Prior curation separates cell-free chemistry, agar inhibition, plant composition
    and computational rescaling; the current graph retains its partial-mediation qualifications
    and open question.
  support: supports
  accessed_at: '2026-10-21T06:55:53.014700Z'
- evidence_id: local-search
  kind: search
  reference: references_cache; history; reports/causal_graph_review/decisions; kb/taxa
  locator: Record slug, PMID and ID search including ignored and hidden files
  summary: The bounded search located the cache, target history and prior decision;
    it does not establish absence of all reusable taxon records or public datasets.
  support: supports
  accessed_at: '2026-10-21T06:55:53.014703Z'
  search_scope: rg --no-ignore --hidden -l for 31152139, Arabidopsis_Coumarin_Root_SynCom
    and CommunityMech:000094 in the named trees.
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources runner discovery
  locator: Same-runtime discovery receipt reused with its original timestamp
  summary: No runner was available in the owned runtime; a candidate in another checkout
    was not executed. No expression-module coverage was queried or inferred for Root329.
  support: supports
  accessed_at: '2026-10-21T06:55:53.014894Z'
  snapshot_sha256: 3a73ceebdf482a2cf5f18bd7e2c70fa1d8e0b9f057fad0e8f756450ca1075786
  search_scope: Prior PATH/module resolution and bounded ignored-inclusive filename
    search; explicit reuse, not a fresh search.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  locator: Actual execution 2026-10-21T06:51:12.913100+00:00 to 2026-10-21T06:51:15.654893+00:00
  summary: Schema validation passed for the target.
  support: supports
  accessed_at: '2026-10-21T06:51:15.654893Z'
  snapshot_sha256: 68b537c5a5e98a913140bd468fd354e57e2268f35773f7dd4f2d7d087d80684b
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-03/000094/strict-report.tsv
  locator: Actual execution 2026-10-21T06:51:12.916140+00:00 to 2026-10-21T06:51:17.818877+00:00
  summary: Strict closed-schema and cross-field validation passed for the target.
  support: supports
  accessed_at: '2026-10-21T06:51:17.818877Z'
  snapshot_sha256: 9c9fcdf84db1c519d2d7186f973d82dee4c336c08f8c2c4ff0745f9224f43600
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  locator: Actual execution 2026-10-21T06:51:12.918334+00:00 to 2026-10-21T06:51:17.218902+00:00
  summary: Native ontology-term validation passed for the target.
  support: supports
  accessed_at: '2026-10-21T06:51:17.218902Z'
  snapshot_sha256: ab005e7d2f46ee58df643ce5a053b65d70b084957e134d8e469cb85e11a9e843
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  locator: Actual execution 2026-10-21T06:51:15.655322+00:00 to 2026-10-21T06:51:15.784627+00:00
  summary: GTDB structural validation passed without certifying an isolate-level crosswalk.
  support: supports
  accessed_at: '2026-10-21T06:51:15.784627Z'
  snapshot_sha256: f1261645a0ccede44d74b2189c399ed9e868876b6d07c4acc36f6497ab1dfd3a
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  locator: Actual execution 2026-10-21T06:51:15.784902+00:00 to 2026-10-21T06:51:17.882731+00:00
  summary: GTDB domain validation passed for the target.
  support: supports
  accessed_at: '2026-10-21T06:51:17.882731Z'
  snapshot_sha256: f8637414cabf526d26ced2bd43c4a61791f3ca275c3e845db968e1feff23ac63
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Arabidopsis_Coumarin_Root_SynCom
  locator: Actual execution 2026-10-21T06:51:17.219238+00:00 to 2026-10-21T06:51:18.127210+00:00
  summary: The target history sidecar passed native validation.
  support: supports
  accessed_at: '2026-10-21T06:51:18.127210Z'
  snapshot_sha256: dcd197fd94312a1f6edb535d1a12a4ce4f1b538b6e9ad70d8e0bd2e8ebd57313
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T06:51:18.128428+00:00 to 2026-10-21T06:51:18.211945+00:00
  summary: Read-only reference-cache filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T06:51:18.211945Z'
  snapshot_sha256: 5afa918d36b92ef458e148429e2b7ba6e3e534156b927a6c97bb73d143b348a6
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
  locator: Actual execution 2026-10-21T06:51:18.212398+00:00 to 2026-10-21T06:51:19.438121+00:00
  summary: Native reference validation passed with committed cache hashes unchanged.
  support: supports
  accessed_at: '2026-10-21T06:51:19.438121Z'
  snapshot_sha256: ac2c74bbe848426e0026bb1337f8f934d4c67c7411d1efed3ed5d5ec2de8ebae
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
  locator: Independent fresh read-only API check and native metric components in support-audit.json
  summary: No target issue returned; six interaction evidence items across four nodes
    yield mean 1.5, and three arrows remain qualified.
  support: supports
  accessed_at: '2026-10-21T06:55:53.017665Z'
  snapshot_sha256: b9efdeedb39a8fc0082c011afbf8aa4ec9cfd546c3a7482e3fec148a2c54c548
assessments:
- assessment_id: identity
  area: identity
  topic: Hydroponic 22-member SynCom and focal Root329 strain
  outcome: supported
  summary: The source and experimental community are resolved. Bacteria is an aggregate
    and Root329 is a focal member; neither the whole roster nor a two-member community
    is asserted.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - identity
  - primary
  - pubmed
  - crossref
  dimensions:
  - name: community_scope
    value: 22-member Arabidopsis root-isolate SynCom
    definition: Full community, reduced communities, individual isolates and computational
      omission are separate experimental objects.
    evidence_ids:
    - identity
    - composition
  - name: source_strain
    value: Pseudomonas sp. Root329 within a broader root-isolate aggregate
    definition: Genus grounding preserves the source designation without inventing
      a species or certifying every strain.
    evidence_ids:
    - identity
    - ontology
  - name: experimental_setting
    value: Controlled hydroponic live plants plus cell-free and agar assays
    definition: Root relative abundance is not a direct readout of bacterial absolute
      growth or local peroxide concentration.
    evidence_ids:
    - culture
    - mediation
  - name: evidence_tier
    value: Host interventions, purified chemistry, inhibition/rescue and computational
      rescaling
    definition: The combined experiments support a candidate mechanism, with intact-community
      mediation unresolved.
    evidence_ids:
    - chemistry
    - sensitivity
    - composition
  - name: medium
    value: Quarter-strength TSB preparation and hydroponic MS
    definition: Bacterial preparation and plant cultivation are distinct; no complete
      supplement recipe is certified.
    evidence_ids:
    - culture
- assessment_id: taxonomy
  area: grounding
  topic: Taxonomy, strain designation and GTDB scope
  outcome: supported
  summary: NCBI domain and genus IDs fit the explicitly nested descriptors; no functional
    role is invented for the heterogeneous aggregate or coumarin-sensitive focal strain.
    Genus-level GTDB majority mapping is not an isolate-genome crosswalk.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - ontology
  - identity
- assessment_id: description
  area: evidence
  topic: Description peroxide-mediation claim
  outcome: concern
  summary: The description presents peroxide-linked suppression as contributing to
    the root profile without carrying the candidate-mechanism and relative-abundance
    limits already preserved in the graph and discussion.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - mediation
  - composition
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Iron-Limited Catecholic Coumarin Exudation'
  outcome: supported
  summary: Root catecholic-coumarin release is supported.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - exudation
  - primary
  details: 'Participants: Arabidopsis roots and downstream microbial community; direction:
    iron limitation and plant biosynthesis/export toward compound release, without
    implying reciprocal competition. Linked primary evidence supplies the source locator
    and bounded excerpt.'
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Catecholic Coumarin Peroxide Generation'
  outcome: supported
  summary: Cell-free peroxide production is supported.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - chemistry
  - primary
  details: 'Participants: purified catecholic coumarins in iron-deficient MS; direction:
    chemical redox activity toward peroxide generation. COMMUNITY_LEVEL is a graph
    grouping, not evidence that bacteria catalyze this chemistry. Linked primary evidence
    supplies the source locator and bounded excerpt.'
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Pseudomonas Root329 Coumarin Sensitivity'
  outcome: supported
  summary: Strain-specific inhibition and rescue are supported.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - sensitivity
  - primary
  details: 'Participants: Root329 and tested compounds on nutrient agar; direction:
    compound exposure toward inhibited growth, modified by catalase and soluble iron.
    Neither a genus-wide response nor a specific bacterial regulator is established.
    Linked primary evidence supplies the source locator and bounded excerpt.'
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Pseudomonas-Weighted Coumarin Community Shift'
  outcome: supported
  summary: Qualified root-community compositional response is supported.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - composition
  - primary
  details: 'Participants: hydroponic Arabidopsis, full or experimentally reduced SynComs
    and Root329; direction: host coumarin perturbation/supplementation toward relative-abundance
    changes. In-silico rescaling is not physical dropout or proof of absolute depletion.
    Linked primary evidence supplies the source locator and bounded excerpt.'
- assessment_id: arrow-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: Exudation supplies the chemical species tested separately.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - exudation
  - chemistry
  details: Source roots release the named catechols, which generate peroxide in cell-free
    MS. The edge explicitly does not claim a root-local peroxide measurement. Direction
    and context remain bounded by the current edge wording.
- assessment_id: arrow-1
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: supported
  summary: The partial peroxide-to-inhibition link is supported.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - chemistry
  - sensitivity
  details: Peroxide production and catalase rescue support involvement in Root329
    inhibition across separate assays; a direct chemical flux at roots is not established.
    Direction and context remain bounded by the current edge wording.
- assessment_id: arrow-2
  area: graph
  topic: ecological_interactions[2].downstream[0]
  outcome: supported
  summary: The partial sensitivity-to-community link is supported as a candidate explanation.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - sensitivity
  - composition
  - mediation
  details: Root329 inhibition in vitro and its host-associated relative-abundance
    response are consistent with the proposed mechanism. The edge explicitly preserves
    unresolved intact-root peroxide mediation and absolute depletion. Direction and
    context remain bounded by the current edge wording.
- assessment_id: chemicals
  area: grounding
  topic: All graph metabolites, related ingredients and GO process
  outcome: concern
  summary: Graph coumarins use the correct class with named-compound limits; peroxide
    and oxidative-stress response fit the assays. Ferric iron fits source mobilization
    and FeCl3/Fe-EDTA manipulations without proving every iron pool. Only the separate
    parent-coumarin ingredient conflates molecule and class.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - ontology
  - chemical-scope
  - chemistry
  - sensitivity
- assessment_id: environment
  area: scope
  topic: Ecological state, category, engineering design and environment
  outcome: concern
  summary: ENGINEERED, SYNTHETIC and root-associated category fit the design; soil
    rhizosphere should be separated from the physical hydroponic setting. The assembly-design
    factor is metadata duplicated from engineering_design rather than a measured environmental
    condition.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - schema
  - culture
  - ontology
- assessment_id: evidence-context
  area: provenance
  topic: Non-graph evidence_source values
  outcome: concern
  summary: Several snippets explicitly describe living plant roots but are typed IN_VITRO,
    unlike the correctly typed root-response graph nodes; cultured-inoculum, cell-free
    and agar evidence remain IN_VITRO.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - schema
  - culture
  - composition
- assessment_id: cultivation
  area: completeness
  topic: Growth media and experimental conditions
  outcome: concern
  summary: The combined entry distinguishes bacterial TSB preparation from plant hydroponics
    in its notes, and its reported timing is source-backed. External recipe identifiers
    remain absent; uninspected supplement details should not be inferred.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - culture
  - schema
- assessment_id: genes
  area: scope
  topic: Plant genes, microbial roles and expression-module applicability
  outcome: supported
  summary: F6-prime-H1 and other plant mutants define host perturbations, not identified
    bacterial effectors. No bacterial transcriptomic module or protein-level mechanism
    is asserted.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - exudation
  - sensitivity
  - adapter
- assessment_id: resources
  area: completeness
  topic: External resources and datasets
  outcome: supported
  summary: No dataset accession is encoded; the bounded cached-text search found no
    common BioProject/GEO/SRA-style accession, which does not establish global absence.
    Supplementary materials and full strain identities were not independently audited.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - primary
  - local-search
- assessment_id: history
  area: provenance
  topic: History, cache and open discussion
  outcome: supported
  summary: The valid target sidecar and prior decision preserve qualified causal interpretation;
    all snippets match cache, with fresh abstract confirmation for six occurrences
    and explicit full-text access limitations.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - history
  - snippets
  - mediation
- assessment_id: metals
  area: scope
  topic: Iron and metal-related assertions
  outcome: supported
  summary: Iron availability and ferric-iron mobilization are relevant context for
    coumarin chemistry; the record does not establish microbial iron uptake, siderophore
    exchange, metal recovery or rare-earth processing.
  target_ids:
  - CommunityMech:000094
  evidence_ids:
  - record
  - chemical-scope
  - chemistry
  - ontology
- assessment_id: validation
  area: schema
  topic: Native gates and independent checks
  outcome: supported
  summary: Eight focused checks passed, eight ID-label pairs match and seventeen snippets
    match cached primary text; corpus warning failures and fresh full-text unavailability
    remain explicit.
  target_ids:
  - CommunityMech:000094
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
  summary: Completeness 30 reflects sparse structured metadata and absent roles; quality
    100 is not scientific approval.
  target_ids:
  - CommunityMech:000094
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
    definition: 'min(100, 50 required metadata including all roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). Both taxon roles are absent: 0 + 5 + 0 + 10 + 0 + 10
      + 0 + 5 = 30; no unsupported role should be invented to raise the score.'
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1 = 0, P2 = 2, P3 = 3, P4 = 0; 6 items /
      4 nodes = 1.5; native COMPLETE. 100 - 20 - 6 + 15 + 15 = 104, clamped to 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P2
    value: 2
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P3
    value: 3
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
findings:
- finding_id: parent-coumarin
  issue_key: cm-000094-parent-coumarin
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: chemical identity or causal scope changes the biological
    assertion.'
  rule_id: review-checklist.ontology_grounding
  status: open
  certainty: confirmed
  title: Parent coumarin is substituted for the coumarins class
  description: CHEBI:28794 correctly labels the specific molecule coumarin, but related_ingredients[0]
    uses it for class-wide biosynthesis and named substituted compounds. This differs
    from the graph's correct CHEBI:23403 class and can create a wrong compound join.
  target_ids:
  - CommunityMech:000094
  field_paths:
  - related_ingredients[0]
  evidence_ids:
  - record
  - ontology
  - chemical-scope
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
- finding_id: root-mediation
  issue_key: cm-000094-root-mediation
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: chemical identity or causal scope changes the biological
    assertion.'
  rule_id: review-checklist.causal_claims
  status: open
  certainty: confirmed
  title: Description omits the root-mediation qualification
  description: The description turns the cross-assay peroxide-linked explanation into
    an unqualified contribution to the root community profile. Source interpretation
    and current arrows distinguish relative abundance, in-vitro inhibition and unresolved
    peroxide mediation in the intact community.
  target_ids:
  - CommunityMech:000094
  field_paths:
  - description
  evidence_ids:
  - record
  - mediation
  - composition
  - sensitivity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
- finding_id: experimental-environment
  issue_key: cm-000094-experimental-environment
  category: scope
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded evidence-context, environment or cultivation-linkage
    gap; source-supported endpoints remain recoverable.'
  rule_id: review-checklist.environment
  status: open
  certainty: confirmed
  title: Actual hydroponic environment and modeled rhizosphere are conflated
  description: The formal environment is root-influenced soil even though the studied
    community is hydroponic. A separate factor records assembly design rather than
    an environmental parameter. Source habitat and experimental design remain clear
    in prose but are misplaced in structured fields.
  target_ids:
  - CommunityMech:000094
  field_paths:
  - environment_term
  - modeled_environment
  - environmental_factors[0]
  evidence_ids:
  - record
  - ontology
  - schema
  - culture
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
- finding_id: host-evidence-source
  issue_key: cm-000094-host-evidence-source
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded evidence-context, environment or cultivation-linkage
    gap; source-supported endpoints remain recoverable.'
  rule_id: review-checklist.evidence_type
  status: open
  certainty: confirmed
  title: Live-host root evidence is labeled IN_VITRO outside the graph
  description: Explicit root-community responses and hydroponic seedling inoculation
    are host-associated experiments under the schema, yet their non-graph evidence
    uses IN_VITRO. The corresponding graph correctly distinguishes IN_VIVO and COMPUTATIONAL
    evidence.
  target_ids:
  - CommunityMech:000094
  field_paths:
  - taxonomy[1].evidence[0].evidence_source
  - environmental_factors[1].evidence[0].evidence_source
  - related_ingredients[0].evidence[0].evidence_source
  - growth_media[0].evidence[1].evidence_source
  evidence_ids:
  - record
  - schema
  - culture
  - composition
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
- finding_id: media-linkage
  issue_key: cm-000094-media-linkage
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded evidence-context, environment or cultivation-linkage
    gap; source-supported endpoints remain recoverable.'
  rule_id: P3.1
  status: open
  certainty: confirmed
  title: Source-supported media lack external identifiers
  description: The growth entry records TSB preparation and hydroponic MS context
    but provides no CultureMech or MediaIngredientMech identifier.
  target_ids:
  - CommunityMech:000094
  field_paths:
  - growth_media[0]
  evidence_ids:
  - record
  - culture
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
actions:
- action_id: fix-parent-coumarin
  description: Ground the maintained class assertion as coumarins, or separately verify
    the named compounds and represent them at their actual chemical identities.
  finding_ids:
  - parent-coumarin
  target_ids:
  - CommunityMech:000094
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - No parent molecule is treated as equivalent to the whole class or its derivatives.
  - Relevance, evidence and chemical ID share the same scope.
  - Run strict, term and reference checks.
- action_id: fix-root-mediation
  description: Carry the candidate-mechanism and relative-abundance qualifications
    into the description while preserving demonstrated chemistry, inhibition and root-composition
    effects.
  finding_ids:
  - root-mediation
  target_ids:
  - CommunityMech:000094
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Description agrees with the three qualified arrows and open discussion.
  - No absolute depletion or measured root-local peroxide mediation is asserted.
  - Run strict and reference checks.
- action_id: fix-experimental-environment
  description: Represent the physical study setting and modeled rhizosphere distinctly,
    and keep assembly metadata in engineering_design.
  finding_ids:
  - experimental-environment
  target_ids:
  - CommunityMech:000094
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - The actual study setting does not imply soil cultivation.
  - Root-isolate origin and modeled habitat are retained.
  - Iron-deficiency context is preserved.
  - Run strict and term checks.
- action_id: fix-host-evidence-source
  description: Use IN_VIVO for the explicit living-host observations and review shared
    design snippets in context; retain IN_VITRO for bacterial preparation, cell-free
    chemistry and agar inhibition.
  finding_ids:
  - host-evidence-source
  target_ids:
  - CommunityMech:000094
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Each evidence type follows its actual experiment rather than the laboratory location.
  - Computational rescaling remains COMPUTATIONAL.
  - Quoted text and source boundaries remain intact.
  - Run strict and reference checks.
- action_id: fix-media-linkage
  description: Link exact compatible medium or ingredient entries where available,
    retaining separate inoculum and host-cultivation contexts.
  finding_ids:
  - media-linkage
  target_ids:
  - CommunityMech:000094
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Arabidopsis_Coumarin_Root_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Linked formulations match the reported preparation and assay.
  - No missing supplement recipe or growth condition is invented.
  - Run focused medium/linkage checks.
limitations:
- Primary full-text assessment uses the intact committed cache attributed to PMC HTML.
  Europe PMC returned HTTP 500; NCBI supplied restricted front matter without an article
  body. Fresh PubMed/Crossref identity and abstract verification do not establish
  independent full-text freshness.
- The source supplement and spreadsheet were listed but not retrieved; the complete
  22-isolate inventory, detailed recipes and supplement-only measurements are not
  certified. Main-text claims in the current aggregate representation remain assessable.
- Figure captions and main-text results were read, but figure geometry, raw counts
  and chemical measurements were not independently reanalyzed.
- GTDB validators check structural grounding and domain; historical crosswalk counts
  and the precise genome assignment of Root329 were not independently reproduced.
- The mechanism remains qualified across cell-free, agar, live-host and computational
  contexts; root-local peroxide mediation and absolute Root329 depletion remain unresolved.
- Optional structured-expression adapter discovery was reused with its original timestamp;
  another checkout candidate was not executed and no expression-module coverage was
  established.
- Required corpus checks retain their actual warning failures; clean target diagnostics
  and numeric scores do not establish scientific truth.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Source quotations total 21 words.
- No complete fresh full-text retrieval or supplement inspection is claimed.
tags:
- record-review
- syncom
- rhizosphere
- coumarins
- batch-03
```
