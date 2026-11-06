# BSFL gut SynCom: partial record review

- Review: 20261021T081345Z-bsfl-gut-syncom-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T08:08:12.320018Z
- Finished UTC: 2026-10-21T08:13:45.647587Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Partial review: critical full Methods/Results remain unavailable. One major finding concerns merged cultivation contexts; two minor findings concern proteolysis modality and unbounded source/ontology notes. Five nodes and no arrows are consistent with accessible abstract/highlight scope. Seven focused gates and cache preflight pass; the required source check is unavailable and corpus network warning failures remain explicit.

## Scope And Provenance

Whole target read and every current claim/node assessed to accessible-source limits: complete fresh abstracts, indexed primary Introduction and truncated Methods/Results/Discussion/Conclusions, metadata, local ontology and native gates. Full critical protocols, figures and supplements remain unreviewed.

Selection: Next uncovered maintained path after CommunityMech:000245 in batch04; one resolved three-member SynCom.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c6e5a9b9af2d05e12eaafb2555a53f3a079268f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000284 | kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml | maintained | Black Soldier Fly Larvae Gut SynCom (Bacillus + Lactobacillus + Issatchenkia) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000284 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000284 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000284 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000284 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000284 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000284 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000284 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000284 | Target native reference validation passed; scientific meaning was assessed separately. |
| audit-network | failed | True | CommunityMech:000284 | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-network-quality | failed | True | CommunityMech:000284 | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| Publication identity and accessible text | passed | True | CommunityMech:000284 | Fresh PMID/DOI metadata and complete abstracts agree; indexed primary preview was inspected within its visible boundaries. |
| Complete critical Methods and Results assessment | unavailable | True | CommunityMech:000284 | Critical full Methods/Results, strain protocols and supplements remain unavailable through the inspected public routes. |
| Encoded source accessions | not_applicable | False | CommunityMech:000284 | No accession is encoded or identified in the bounded accessible source text; uninspected sections are not certified. |
| Encoded medium and ingredient-Mech linkages | not_applicable | False | CommunityMech:000284 | No CultureMech or MediaIngredientMech ID is encoded, and the feedstock formulation remains unresolved. |
| Optional structured source adapter | unavailable | False | CommunityMech:000284 | Same-runtime discovery was reused; no strain/module coverage was queried. |

## Scientific And Domain Assessments

### SynCom identity and experimental boundary

identity: supported. Targets: CommunityMech:000284.

The cited abstract resolves the requested bacterial/yeast SynCom, while exact strains and stage-specific protocols remain unverified.

### All three taxa, membership and functional roles

grounding: concern. Targets: CommunityMech:000284.

Genus-level membership and Bacillus degradation are abstract-supported; exact strains and proteolysis assay provenance remain unresolved.

The two absent functional roles reduce native completeness but should not be invented. Membership abundance text is not a numerical abundance measurement. Genus-only statements should describe inspected text, not unreviewed full-paper contents.

### ecological_interactions[0]: Bacillus Direct Proteolysis

graph: supported. Targets: CommunityMech:000284.

Consistent with accessible abstract and publisher-highlight scope; full experimental certification remains pending.

Bacillus is the explicit participant and protein breakdown the reported endpoint. The node correctly uses OTHER for unresolved assay modality and does not infer cross-feeding to the other two members.

### ecological_interactions[1]: Lactobacillus-Issatchenkia Protein-Conversion Association

graph: supported. Targets: CommunityMech:000284.

Consistent with accessible abstract and publisher-highlight scope; full experimental certification remains pending.

Lactobacillus and source-named Issatchenkia/Pichia are participants associated with host protein conversion and amino-acid responses; the direction is microbial treatment toward host outcome, not proven microbial metabolite exchange.

### ecological_interactions[2]: Tripartite Gut-pH Niche Partitioning

graph: supported. Targets: CommunityMech:000284.

Consistent with accessible abstract and publisher-highlight scope; full experimental certification remains pending.

The three-member consortium is associated with gut distribution and host protein endpoints. The node treats niche partitioning as proposed; pH intervention, the 63% comparator and measured protein denominator remain unverified.

### ecological_interactions[3]: ALDH-TOR Amino-Acid Host Response

graph: supported. Targets: CommunityMech:000284.

Consistent with accessible abstract and publisher-highlight scope; full experimental certification remains pending.

The host ALDH/TOR context is associated with microbiota-responsive amino-acid changes. PARTIAL support correctly avoids certifying necessary mediation or reciprocal microbial fitness; no absence of unreviewed perturbation experiments is inferred.

### ecological_interactions[4]: Organic-Waste SynCom-BSFL Proof of Concept

graph: supported. Targets: CommunityMech:000284.

Consistent with accessible abstract and publisher-highlight scope; full experimental certification remains pending.

The SynCom-host system is applied to chicken manure and kitchen waste with reported selected performance gains. Direction is treatment toward application outcomes; the abstract does not establish a combined feed recipe or all host-rearing conditions. The primary highlight specifically reports waste protein degradation, supporting GO:0030163 context; the current vague performance snippet should be supplemented with claim-level evidence when Methods is available.

### Current downstream graph

graph: supported. Targets: CommunityMech:000284.

No downstream arrows remain; workflow, pH mediation and metabolite-transfer edges should not be invented.

### Origin, category, state and environmental context

scope: supported. Targets: CommunityMech:000284.

SYNTHETIC, ENGINEERED and BIOTECHNOLOGY are consistent with deliberate assembly; the digestive-tract anchor is appropriately broad.

The global absence claim about insect-gut ENVO terms requires narrower wording; it is not a defect in the chosen valid parent term.

### One growth-media entry with two feedstocks

scope: concern. Targets: CommunityMech:000284.

The entry merges contexts that the accessible evidence does not establish as one recipe or gnotobiotic baseline protocol.

Do not infer a growth temperature, numerical gut pH, diet composition, oxygen regime or duration from inaccessible Methods. The preview's 0/12/24-day omics context is not automatically the duration of every SynCom or waste assay.

### Datasets, cross-Mech links, chemicals and proteins

completeness: unknown. Targets: CommunityMech:000284.

No encoded dataset or cross-Mech ID requires verification; inaccessible details prevent a concrete missing-resource or exact-protein finding.

ALDH and TOR name host functions without verified gene/protein identifiers. Do not assign a microbial protein accession, fabricate exchanged amino acids or infer metal relevance from unrelated bibliography.

### Snippet fidelity, graph repair and source limits

provenance: supported. Targets: CommunityMech:000284.

The eleven snippets match fresh abstracts and the prior graph repair preserves the unresolved Methods boundary.

### Native gates and incomplete source certification

schema: concern. Targets: CommunityMech:000284.

Seven focused gates and cache preflight pass; the required full-source check remains unavailable and corpus network failures remain explicit.

### Native completeness and quality within partial review

completeness: supported. Targets: CommunityMech:000284.

Completeness is 25 and native quality caps at 100; these scores cannot certify the unavailable whole-source assessment.

## Findings

### cultivation-context: The growth-medium entry transfers conditions between experimental contexts

major / open / confirmed; issue key: cm-000284-cultivation-context.

The composition lists chicken manure and kitchen waste together, and preparation notes connect these feedstocks to germ-free baseline rearing. Accessible abstract and preview support controlled gnotobiotic work followed by short-term waste applications, but not a single mixed recipe or identical cultivation conditions across stages. This is unsupported protocol attribution, not proof that the opposite protocol was used.

### proteolysis-tier: Taxonomy assigns a specific proteolysis modality that remains unverified

minor / open / confirmed; issue key: cm-000284-proteolysis-tier.

The Bacillus taxonomy evidence is tagged IN_VIVO while its explanation asserts direct protein degradation. The same record correctly leaves this measurement's format unspecified and uses OTHER in node 0. The abstract reports activity but does not resolve whether its direct assay was isolated culture or living gut.

### source-scope-notes: Notes generalize beyond the inspected sources and ontology search

minor / open / confirmed; issue key: cm-000284-source-scope-notes.

Taxonomy notes say the paper names the relevant members only at genus rank although full Methods was not accessed; environment notes assert no insect-gut-specific ENVO term without a documented exhaustive ontology claim. These broad absence statements exceed the verified scope, even though the current genus and parent-environment anchors are valid.

## Recommended Actions And Acceptance Checks

### fix-cultivation-context

Separate controlled host-model cultivation from waste-application contexts and retain unresolved assay-specific conditions pending full Methods.

- Do not present the two named wastes as one verified mixture.
- Attach evidence to each stage and avoid transferring germ-free status, diet or incubation between stages without source support.
- Do not reconstruct the truncated diet ratio or use omics timepoints as every assay duration.
- Revisit full Methods when accessible, then run strict/reference checks.

### fix-proteolysis-tier

Align claim-specific assay provenance with the graph's unresolved modality until the relevant Methods is inspected.

- Keep the source-supported Bacillus role and activity report.
- Do not equate an in-vivo SynCom experiment with an in-vivo assay for every member phenotype.
- Use OTHER or separate membership from activity evidence as supported by schema; do not declare an in-vitro assay without evidence.
- Reference validation passes.

### fix-source-scope-notes

Scope the notes to the accessible abstract and the verified broad ontology anchors, preserving unresolved species/strain and environment specificity.

- Do not claim full-paper absence of strain names or global ontology absence.
- Retain Pichia/Issatchenkia as broad related-synonym correspondence, not an authenticated strain match.
- Any more specific future grounding must be separately source-verified.
- Term and reference checks pass.

### complete-source-assessment

When authorized full text becomes available, review critical Methods/Results and relevant supplements for exact member strains, proteolysis modality, baseline versus waste protocols, 63% endpoint/comparator, and ALDH/pH perturbations; then reassess the record in a new immutable review.

- Preserve current uncertainty until inspected primary evidence supports narrower claims.
- Do not purchase access, contact authors or infer missing experiments from this review.
- Attach claim-level evidence and rerun native gates before any separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml; Whole target: three genus-level members, five nodes, no arrows and one growth-medium entry | supports | The target is a three-member bacterial/yeast SynCom tested in a BSFL host, with separate waste-application claims. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42167379&amp;retmode=xml; PubmedArticle: PMID, ArticleTitle, Abstract and ArticleIdList | supports | Fresh PubMed record confirms PMID, DOI, title and the complete abstract. |
| crossref | https://api.crossref.org/works/10.1016/j.biortech.2026.134927; Crossref message: DOI, title, resource and link metadata | supports | Fresh Crossref metadata confirms DOI and title; no PMID or EPMC-access assertion is attributed to this payload. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42167379%20AND%20SRC:MED&amp;format=json&amp;resultType=core; EPMC result: identifiers, abstractText, fullTextUrlList and PMC/OA availability fields | supports | Fresh EPMC abstract/identifier metadata agrees and reports a subscription DOI route without PMC full text. |
| abstract | PMID:42167379; Complete fresh PubMed/EPMC abstract | supports | The abstract identifies three genera, reported proteolysis and host responses, a 63% final-protein increase and preliminary waste application; assay details and effect denominator are not supplied. |
| preview | PMID:42167379; Primary publisher indexed Introduction and truncated Methods/Results/Discussion/Conclusions | supports | The indexed preview provides additional context but not complete experimental protocols. Its Conclusions distinguish controlled gnotobiotic work from short-term waste assays; a truncated diet ratio cannot establish a formulation. |
| access-publisher | https://doi.org/10.1016/j.biortech.2026.134927; Actual public retrieval 2026-10-21T08:08:34.202664Z to 2026-10-21T08:08:34.716732Z | supports | DOI resolves to a LinkingHub redirect shell, not full text. |
| access-publisher-direct | https://www.sciencedirect.com/science/article/pii/S0960852426010096; Actual public retrieval 2026-10-21T08:08:50.190190Z to 2026-10-21T08:08:50.406287Z | supports | Direct public publisher retrieval returned HTTP 403 without article content. |
| access-publisher-tdm | https://api.elsevier.com/content/article/PII:S0960852426010096?httpAccept=text/xml; Actual public retrieval 2026-10-21T08:09:38.634837Z to 2026-10-21T08:09:39.026645Z | supports | Crossref-listed public text-mining endpoint returned HTTP 200 core metadata only, without Methods or article body. |
| access-root-wur | https://research.wur.nl/en/publications/engineering-a-gut-synthetic-microbial-community-to-enhance-protei/; Actual public retrieval 2026-10-21T08:08:20.387524+00:00 to 2026-10-21T08:08:21.497371+00:00 | supports | The author repository contains the complete abstract and DOI access links, not an inspected manuscript file. |
| access-root-openalex | https://api.openalex.org/works/https://doi.org/10.1016/j.biortech.2026.134927; Actual public retrieval 2026-10-21T08:08:20.387963+00:00 to 2026-10-21T08:08:20.780905+00:00 | supports | An OA metadata flag points to the author landing page with no PDF URL; the flag does not establish accessible full text. |
| wur-links | Author repository public landing page; All inspected content hrefs | supports | The bounded access-link inspection finds DOI links only; no global claim of manuscript or supplement absence is made. |
| proteolysis | PMID:42167379; Abstract, sentence beginning Bacillus | supports | Bacillus activity is reported, but the accessible abstract does not identify its assay modality. |
| association | PMID:42167379; Abstract, Bacillus/Lactobacillus/Issatchenkia comparison | supports | The latter two members are associated with host performance; specific exchanged metabolites and reciprocal benefits are not established by this text. |
| distribution | PMID:42167379; Abstract, tripartite-inoculum comparison | supports | The tripartite treatment is highest among tested schemes and associated with gut distribution patterns and a 63% final-protein increase; comparator and measurement basis require Methods. |
| host-response | PMID:42167379; Abstract, host ALDH and TOR sentence | supports | ALDH and amino-acid/TOR-related responses are presented as candidate host mechanisms; necessity or absent perturbations cannot be decided from the abstract. |
| waste | PMID:42167379; Abstract, final sentence; indexed Conclusions | supports | Chicken manure and kitchen waste are application feedstocks; accessible text does not establish one mixed recipe or its identity with the controlled rearing diet. |
| waste-highlight | PMID:42167379; Indexed primary publisher Highlights, final item | supports | The highlight specifically reports waste protein degradation, providing broader catabolic context absent from the vague performance snippet; exact assays remain unavailable. |
| ontology-search | Local ENVO snapshot; Bounded labels and synonyms search for insect-associated gut environments | supports | No matching terms were found in this bounded search; this does not justify a global absence statement or invalidate the current broad anchor. |
| ontology | Local OAK NCBITaxon, ENVO and GO snapshots; Seven unique ID/label pairs across twelve occurrences | supports | All canonical labels match. The three anchors are genera; Pichia lists Issatchenkia as a related synonym, supporting broad correspondence without authenticating a yeast species or strain. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum; evidence and cultivation definitions | supports | PRIMARY_DEGRADER is compatible with reported proteolysis; missing optional roles are not defects. Evidence type and cultivation context must remain specific to the supported assay. |
| snippets | kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml; Eleven snippet occurrences, ten unique, against pinned cache and fresh PubMed/EPMC | supports | All occurrences match the fresh abstracts; lexical correctness does not certify assay modality or transfer conditions between experiments. |
| history | history/records/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia; reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml; Two sidecars and exact current target decision, lines 327-376 | supports | The current record hash matches the graph repair, which explicitly left full Methods and non-graph metadata uncertified. |
| issue-1250 | https://github.com/CultureBotAI/CommunityMech/issues/1250; Fresh public issue body and status | supports | The graph-related issue is closed; this does not resolve current source-access limits or certify cultivation metadata. |
| search | Owned-worktree record/taxon/cache/history roots; Ignored-inclusive exact ID, genus and source lookup | supports | The bounded lookup finds no reusable target genus record and locates this source in the current community record. |
| datasets | Encoded resources and accessible source text; dataset-verification.json | supports | No dataset identifiers are encoded or identified in the inspected abstract material; inaccessible sections may contain them, so no dataset-omission finding is made. |
| adapter | Optional kg-microbe-sources adapter; Explicit same-batch04-runtime discovery reuse | supports | No installed runtime runner/module was available; no strain-level transcriptomic-module coverage was queried. |
| native-target | NetworkIntegrityAuditor().audit_community(target); support-audit.json: native diagnostic and scoring | supports | All three taxa are covered by five nodes, with no arrows or native warnings; five node evidence items give mean evidence one. |
| independent-source | PMID:42167379; root-source-audit.json | supports | Independent source assessment agrees with the three evidence-scope concerns and the need for a partial review. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml; Actual execution 2026-10-21T08:08:28.762097+00:00 to 2026-10-21T08:08:30.452917+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-strict kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml --out /private/tmp/cm-review-session/batch-04/000284/strict-report.tsv; Actual execution 2026-10-21T08:08:28.764338+00:00 to 2026-10-21T08:08:32.447784+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-terms kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml; Actual execution 2026-10-21T08:08:28.766483+00:00 to 2026-10-21T08:08:31.971395+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-gtdb kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml; Actual execution 2026-10-21T08:08:30.457679+00:00 to 2026-10-21T08:08:30.605237+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-gtdb-domain kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml; Actual execution 2026-10-21T08:08:30.605548+00:00 to 2026-10-21T08:08:32.716780+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-history history/records/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia; Actual execution 2026-10-21T08:08:31.971819+00:00 to 2026-10-21T08:08:33.000961+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T08:08:33.001738+00:00 to 2026-10-21T08:08:33.090023+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-references-explained kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml; Actual execution 2026-10-21T08:08:33.094256+00:00 to 2026-10-21T08:08:36.165917+00:00 | supports | Target native reference validation passed; scientific meaning was assessed separately. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T07:06:05.543108+00:00 to 2026-10-21T07:06:16.498440+00:00 | supports | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T07:06:16.498920+00:00 to 2026-10-21T07:06:23.361213+00:00 | supports | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |

## Limits And Additional Notes

- This is not a completed scientific record certification: required critical full Methods/Results remain unavailable. The available primary preview contains some Methods and Results, so no global absence claim is made.
- DOI retrieval yields a redirect shell, direct publisher access returns HTTP 403, and public TDM returns metadata only. The author repository has an abstract/DOI link; an OA flag does not supply a verified manuscript. No credentials, purchase or access-control bypass was used.
- Exact microbial species/strains, inoculum doses, culture media, gut-pH values, baseline diet, waste-assay microbial status and assay durations remain unresolved. A truncated diet ratio and introductory omics timepoints were not imported as complete protocols.
- The 63% final-larval-protein statement is retained as source-reported, without an inferred comparator, denominator or identity with conversion efficiency.
- ALDH/TOR and pH distribution remain candidate/associated host contexts. No absence of perturbation experiments, metabolite transfer or deposited datasets is inferred from inaccessible sections.
- Genus-level ontology anchors and Pichia related-synonym metadata do not authenticate isolate identities. The bounded ENVO search does not prove global absence of an insect-specific term.
- Historical GTDB mapping counts were not recomputed; optional structured-adapter discovery was reused and no external-checkout runner or strain/module query was executed.
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 23 words for Yu 2026, including primary highlights.
- Native quality 100 is capped from 111 and is not a substitute for the unavailable scientific-source assessment.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T081345Z-bsfl-gut-syncom-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'BSFL gut SynCom: partial record review'
started_at: '2026-10-21T08:08:12.320018Z'
finished_at: '2026-10-21T08:13:45.647587Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Canonical target unchanged; prior codex graph curation prevents
    person-level independence claims. Separate agents assessed accessible primary
    text, ontology, native gates, snippets, history and metrics.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: 'Partial review: critical full Methods/Results remain unavailable. One major
  finding concerns merged cultivation contexts; two minor findings concern proteolysis
  modality and unbounded source/ontology notes. Five nodes and no arrows are consistent
  with accessible abstract/highlight scope. Seven focused gates and cache preflight
  pass; the required source check is unavailable and corpus network warning failures
  remain explicit.'
source:
  git_revision: c6e5a9b9af2d05e12eaafb2555a53f3a079268f3
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
  - path: history/records/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia/2026-10-02T051251Z-codex-58578e.yaml
    sha256: 1abe7da267a56deeedf25468510e26467b618fe108da66b755d2d0ae6e5e161c
    role: context
  - path: history/records/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia/2026-10-05T101149Z-codex-3d53f1.yaml
    sha256: eb3090661a8c6224558c1eefae7de2bb39d2ba8be83fb134adadc770cf7a3a1b
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    sha256: b531d14963595ee4927d169e209b574bd3c4a57ba8eb8891f0e6668a558297d7
    role: target
  - path: references_cache/PMID_42167379.md
    sha256: c24fe40d023634b2b82a26e64d111c04629fa1dda71aed60645b766a46cb7df7
    role: context
  - path: reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml
    sha256: 5076ec8295dacfaae0ae1d829836e4380a312a702c4a43df5f604c3b1b1e0ad3
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
- target_id: CommunityMech:000284
  path: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  label: Black Soldier Fly Larvae Gut SynCom (Bacillus + Lactobacillus + Issatchenkia)
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    role: canonical_record
scope:
  description: 'Whole target read and every current claim/node assessed to accessible-source
    limits: complete fresh abstracts, indexed primary Introduction and truncated Methods/Results/Discussion/Conclusions,
    metadata, local ontology and native gates. Full critical protocols, figures and
    supplements remain unreviewed.'
  selection: Next uncovered maintained path after CommunityMech:000245 in batch04;
    one resolved three-member SynCom.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000284
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000284
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000284
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-strict kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    --out /private/tmp/cm-review-session/batch-04/000284/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000284
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-terms kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000284
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000284
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb-domain kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000284
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-history history/records/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000284
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target native reference validation passed; scientific meaning was assessed
    separately.
  target_ids:
  - CommunityMech:000284
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-references-explained kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    pinned inputs and both caches unchanged.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000284
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Reused fresh full-corpus batch04 execution; neither a target-specific
    failure nor a pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000284
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Reused fresh full-corpus batch04 execution; neither a target-specific
    failure nor a pass.
- check_id: publication-identity
  name: Publication identity and accessible text
  status: passed
  required: true
  summary: Fresh PMID/DOI metadata and complete abstracts agree; indexed primary preview
    was inspected within its visible boundaries.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - abstract
  - preview
- check_id: full-primary-source
  name: Complete critical Methods and Results assessment
  status: unavailable
  required: true
  summary: Critical full Methods/Results, strain protocols and supplements remain
    unavailable through the inspected public routes.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - access-publisher
  - access-publisher-direct
  - access-publisher-tdm
  - access-root-wur
  - access-root-openalex
  - wur-links
  - preview
  - independent-source
  scope_note: Some Methods/Results/Conclusions snippets are visible; unavailable complete
    critical sections require partial completion and scientific_review false, not
    a claim that experiments or datasets are absent.
- check_id: source-data
  name: Encoded source accessions
  status: not_applicable
  required: false
  summary: No accession is encoded or identified in the bounded accessible source
    text; uninspected sections are not certified.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - datasets
- check_id: cross-mech
  name: Encoded medium and ingredient-Mech linkages
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech ID is encoded, and the feedstock
    formulation remains unresolved.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - waste
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Same-runtime discovery was reused; no strain/module coverage was queried.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  locator: 'Whole target: three genus-level members, five nodes, no arrows and one
    growth-medium entry'
  summary: The target is a three-member bacterial/yeast SynCom tested in a BSFL host,
    with separate waste-application claims.
  support: supports
  accessed_at: '2026-10-21T08:13:45.641498Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42167379&retmode=xml
  locator: 'PubmedArticle: PMID, ArticleTitle, Abstract and ArticleIdList'
  summary: Fresh PubMed record confirms PMID, DOI, title and the complete abstract.
  support: supports
  accessed_at: '2026-10-21T08:08:34.201929Z'
  snapshot_sha256: d6a0d6932e169795c6f2d7faffd79c117049e3f52b904838cff2096949c2b987
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.biortech.2026.134927
  locator: 'Crossref message: DOI, title, resource and link metadata'
  summary: Fresh Crossref metadata confirms DOI and title; no PMID or EPMC-access
    assertion is attributed to this payload.
  support: supports
  accessed_at: '2026-10-21T08:08:34.265988Z'
  snapshot_sha256: 6a5e2ef3cbd034426b21ef5bee42354523518ba81f48bb9a260636d89715597f
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42167379%20AND%20SRC:MED&format=json&resultType=core
  locator: 'EPMC result: identifiers, abstractText, fullTextUrlList and PMC/OA availability
    fields'
  summary: Fresh EPMC abstract/identifier metadata agrees and reports a subscription
    DOI route without PMC full text.
  support: supports
  accessed_at: '2026-10-21T08:08:34.794272Z'
  snapshot_sha256: fe46c763c464e262e649658b5ec620bab981b2ba22ce83efc07782c1b9d47631
- evidence_id: abstract
  kind: primary_source
  reference: PMID:42167379
  locator: Complete fresh PubMed/EPMC abstract
  summary: The abstract identifies three genera, reported proteolysis and host responses,
    a 63% final-protein increase and preliminary waste application; assay details
    and effect denominator are not supplied.
  support: supports
  accessed_at: '2026-10-21T08:13:45.642283Z'
  snapshot_sha256: d6a0d6932e169795c6f2d7faffd79c117049e3f52b904838cff2096949c2b987
- evidence_id: preview
  kind: primary_source
  reference: PMID:42167379
  locator: Primary publisher indexed Introduction and truncated Methods/Results/Discussion/Conclusions
  summary: The indexed preview provides additional context but not complete experimental
    protocols. Its Conclusions distinguish controlled gnotobiotic work from short-term
    waste assays; a truncated diet ratio cannot establish a formulation.
  support: supports
  accessed_at: '2026-10-21T08:13:45.642494Z'
  snapshot_sha256: 523db861e50941f352aa335ff386f43eff6a5ae58b1b19f69b8eb6d3e206bc20
- evidence_id: access-publisher
  kind: validation
  reference: https://doi.org/10.1016/j.biortech.2026.134927
  locator: Actual public retrieval 2026-10-21T08:08:34.202664Z to 2026-10-21T08:08:34.716732Z
  summary: DOI resolves to a LinkingHub redirect shell, not full text.
  support: supports
  accessed_at: '2026-10-21T08:08:34.716732Z'
  snapshot_sha256: 102d400ffc8636e382ec5034ec5bb835c9dbd8389578b79d5e47aff98900bb03
- evidence_id: access-publisher-direct
  kind: validation
  reference: https://www.sciencedirect.com/science/article/pii/S0960852426010096
  locator: Actual public retrieval 2026-10-21T08:08:50.190190Z to 2026-10-21T08:08:50.406287Z
  summary: Direct public publisher retrieval returned HTTP 403 without article content.
  support: supports
  accessed_at: '2026-10-21T08:08:50.406287Z'
  snapshot_sha256: 16a2de802ceeabbe1b1dd95b67ce1971d6fc7d0cce550c9a4ee48b555229e663
- evidence_id: access-publisher-tdm
  kind: validation
  reference: https://api.elsevier.com/content/article/PII:S0960852426010096?httpAccept=text/xml
  locator: Actual public retrieval 2026-10-21T08:09:38.634837Z to 2026-10-21T08:09:39.026645Z
  summary: Crossref-listed public text-mining endpoint returned HTTP 200 core metadata
    only, without Methods or article body.
  support: supports
  accessed_at: '2026-10-21T08:09:39.026645Z'
  snapshot_sha256: 67e109b1d30230b794bb9e4c681133a833020e3ad11f7de145650846d0d32d33
- evidence_id: access-root-wur
  kind: validation
  reference: https://research.wur.nl/en/publications/engineering-a-gut-synthetic-microbial-community-to-enhance-protei/
  locator: Actual public retrieval 2026-10-21T08:08:20.387524+00:00 to 2026-10-21T08:08:21.497371+00:00
  summary: The author repository contains the complete abstract and DOI access links,
    not an inspected manuscript file.
  support: supports
  accessed_at: '2026-10-21T08:08:21.497371Z'
  snapshot_sha256: d752438c8156738570a23a5e63692ad6512381588fbf3ea5211763a4c6dd98b9
- evidence_id: access-root-openalex
  kind: validation
  reference: https://api.openalex.org/works/https://doi.org/10.1016/j.biortech.2026.134927
  locator: Actual public retrieval 2026-10-21T08:08:20.387963+00:00 to 2026-10-21T08:08:20.780905+00:00
  summary: An OA metadata flag points to the author landing page with no PDF URL;
    the flag does not establish accessible full text.
  support: supports
  accessed_at: '2026-10-21T08:08:20.780905Z'
  snapshot_sha256: 902d1e327629491f7e0f7ceca971fe5156deca63fd999496ce84441245b05ecd
- evidence_id: wur-links
  kind: search
  reference: Author repository public landing page
  locator: All inspected content hrefs
  summary: The bounded access-link inspection finds DOI links only; no global claim
    of manuscript or supplement absence is made.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643455Z'
  snapshot_sha256: 435d41cccd83f6e922f930d9963a3ec25ff5a0804b1e8da0ea9f14cbfdd81559
  search_scope: All hrefs in the retrieved author-repository page, not other repositories
    or private holdings.
- evidence_id: proteolysis
  kind: primary_source
  reference: PMID:42167379
  locator: Abstract, sentence beginning Bacillus
  summary: Bacillus activity is reported, but the accessible abstract does not identify
    its assay modality.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643458Z'
  quote: direct proteolytic activity
- evidence_id: association
  kind: primary_source
  reference: PMID:42167379
  locator: Abstract, Bacillus/Lactobacillus/Issatchenkia comparison
  summary: The latter two members are associated with host performance; specific exchanged
    metabolites and reciprocal benefits are not established by this text.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643460Z'
  quote: associated with improved protein conversion performance
- evidence_id: distribution
  kind: primary_source
  reference: PMID:42167379
  locator: Abstract, tripartite-inoculum comparison
  summary: The tripartite treatment is highest among tested schemes and associated
    with gut distribution patterns and a 63% final-protein increase; comparator and
    measurement basis require Methods.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643461Z'
  quote: distinct spatiotemporal distribution patterns
- evidence_id: host-response
  kind: primary_source
  reference: PMID:42167379
  locator: Abstract, host ALDH and TOR sentence
  summary: ALDH and amino-acid/TOR-related responses are presented as candidate host
    mechanisms; necessity or absent perturbations cannot be decided from the abstract.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643462Z'
  quote: candidate host node
- evidence_id: waste
  kind: primary_source
  reference: PMID:42167379
  locator: Abstract, final sentence; indexed Conclusions
  summary: Chicken manure and kitchen waste are application feedstocks; accessible
    text does not establish one mixed recipe or its identity with the controlled rearing
    diet.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643463Z'
  quote: selected performance metrics
- evidence_id: waste-highlight
  kind: primary_source
  reference: PMID:42167379
  locator: Indexed primary publisher Highlights, final item
  summary: The highlight specifically reports waste protein degradation, providing
    broader catabolic context absent from the vague performance snippet; exact assays
    remain unavailable.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643465Z'
  quote: protein degradation in wastes
- evidence_id: ontology-search
  kind: search
  reference: Local ENVO snapshot
  locator: Bounded labels and synonyms search for insect-associated gut environments
  summary: No matching terms were found in this bounded search; this does not justify
    a global absence statement or invalidate the current broad anchor.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643661Z'
  snapshot_sha256: 477ab914026567a47bcad5b53f320a68537711d5b2ec59c29c05b7d3d8d60bd4
  search_scope: Exact documented label/synonym patterns in the local ENVO snapshot;
    no exhaustive conceptual or external ontology search.
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO and GO snapshots
  locator: Seven unique ID/label pairs across twelve occurrences
  summary: All canonical labels match. The three anchors are genera; Pichia lists
    Issatchenkia as a related synonym, supporting broad correspondence without authenticating
    a yeast species or strain.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643827Z'
  snapshot_sha256: 0e34c649a6588d17c49c04efac14c1980360d6e930ada54567cb0f7e5e528ea9
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum; evidence and cultivation definitions
  summary: PRIMARY_DEGRADER is compatible with reported proteolysis; missing optional
    roles are not defects. Evidence type and cultivation context must remain specific
    to the supported assay.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643831Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  locator: Eleven snippet occurrences, ten unique, against pinned cache and fresh
    PubMed/EPMC
  summary: All occurrences match the fresh abstracts; lexical correctness does not
    certify assay modality or transfer conditions between experiments.
  support: supports
  accessed_at: '2026-10-21T08:13:45.643974Z'
  snapshot_sha256: fce778bd49791dc5fd00d6f44f3ff2634ede6e7e8462c2507cfade428e7f440c
- evidence_id: history
  kind: record_content
  reference: history/records/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia;
    reports/causal_graph_review/decisions/20261005-eleven-records-batch5.yaml
  locator: Two sidecars and exact current target decision, lines 327-376
  summary: The current record hash matches the graph repair, which explicitly left
    full Methods and non-graph metadata uncertified.
  support: supports
  accessed_at: '2026-10-21T08:13:45.644194Z'
  snapshot_sha256: 00ab120a9e56b507764631640f2c88a496cff128b4e2fc6a5aef94b54ba9551d
- evidence_id: issue-1250
  kind: database
  reference: https://github.com/CultureBotAI/CommunityMech/issues/1250
  locator: Fresh public issue body and status
  summary: The graph-related issue is closed; this does not resolve current source-access
    limits or certify cultivation metadata.
  support: supports
  accessed_at: '2026-10-21T08:08:04.923022Z'
  snapshot_sha256: 0d543a02d638c65140c89a475b97dcd986a75f56de5e0c9e6fd4018d811b3b64
- evidence_id: search
  kind: search
  reference: Owned-worktree record/taxon/cache/history roots
  locator: Ignored-inclusive exact ID, genus and source lookup
  summary: The bounded lookup finds no reusable target genus record and locates this
    source in the current community record.
  support: supports
  accessed_at: '2026-10-21T08:13:45.644628Z'
  snapshot_sha256: 0987480cf80ceecf878d129e47b2044f2a00db27c3079738ee6d6f6a618bbd02
  search_scope: rg --no-ignore --hidden over the declared roots; exact NCBITaxon IDs,
    Issatchenkia, PMID, DOI and slug, not global synonym coverage.
- evidence_id: datasets
  kind: search
  reference: Encoded resources and accessible source text
  locator: dataset-verification.json
  summary: No dataset identifiers are encoded or identified in the inspected abstract
    material; inaccessible sections may contain them, so no dataset-omission finding
    is made.
  support: supports
  accessed_at: '2026-10-21T08:13:45.644776Z'
  snapshot_sha256: b8282ff8f7fdc6cc7f3404d39a67580be631ee5b7cab2a0472c76910f4432a11
  search_scope: Bounded current record, pinned abstract and fresh PubMed/EPMC text
    only.
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources adapter
  locator: Explicit same-batch04-runtime discovery reuse
  summary: No installed runtime runner/module was available; no strain-level transcriptomic-module
    coverage was queried.
  support: supports
  accessed_at: '2026-10-21T08:13:45.644927Z'
  snapshot_sha256: f5ff6b896aa0c3ea8abbc6ea604196961ad912d9c71d9090903e3a66b9e45db4
  search_scope: Prior recorded batch04 PATH, virtualenv/module and bounded ignored-inclusive
    discovery, explicitly reused; external-checkout runner not executed.
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: 'support-audit.json: native diagnostic and scoring'
  summary: All three taxa are covered by five nodes, with no arrows or native warnings;
    five node evidence items give mean evidence one.
  support: supports
  accessed_at: '2026-10-21T08:13:45.645044Z'
  snapshot_sha256: a2a9295885a2603c08111f18c6e15069a2216382bf7b557fe59ed974adfc608d
- evidence_id: independent-source
  kind: validation
  reference: PMID:42167379
  locator: root-source-audit.json
  summary: Independent source assessment agrees with the three evidence-scope concerns
    and the need for a partial review.
  support: supports
  accessed_at: '2026-10-21T08:13:45.645359Z'
  snapshot_sha256: c66bba99c38a1d719abffa5a003ea1f2cc6a898b229da9767b875306ef44c13d
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  locator: Actual execution 2026-10-21T08:08:28.762097+00:00 to 2026-10-21T08:08:30.452917+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T08:08:30.452917Z'
  snapshot_sha256: 3ec60940a1b04d1144410d592c340e26b1c1a31690ee37ea5ad4a41575c4980f
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-strict kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    --out /private/tmp/cm-review-session/batch-04/000284/strict-report.tsv
  locator: Actual execution 2026-10-21T08:08:28.764338+00:00 to 2026-10-21T08:08:32.447784+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T08:08:32.447784Z'
  snapshot_sha256: 7f1ac8d83d17b426a3a053a9c4c1de1bd30a7009f1545426afe6c5bf96f07e0f
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-terms kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  locator: Actual execution 2026-10-21T08:08:28.766483+00:00 to 2026-10-21T08:08:31.971395+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T08:08:31.971395Z'
  snapshot_sha256: ec51c6eeb328113992c30f9b65f52c59fa56e1a56fd4c4d9e70dc3bbcdc04c59
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  locator: Actual execution 2026-10-21T08:08:30.457679+00:00 to 2026-10-21T08:08:30.605237+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T08:08:30.605237Z'
  snapshot_sha256: 4bc78932cfc821840b9a55ef2097aa86b834fcaaebde0c7c586887dad00768f4
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb-domain kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  locator: Actual execution 2026-10-21T08:08:30.605548+00:00 to 2026-10-21T08:08:32.716780+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T08:08:32.716780Z'
  snapshot_sha256: c023eaea2be9b31b2fe81b70e556a4944bbac95c4732bb89083ddc746d680ce5
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-history history/records/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia
  locator: Actual execution 2026-10-21T08:08:31.971819+00:00 to 2026-10-21T08:08:33.000961+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T08:08:33.000961Z'
  snapshot_sha256: 152c6eb4fe2f989a1918f0eb32bdbd2a0883e14327e1fcea008fbd44ee9e02d3
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T08:08:33.001738+00:00 to 2026-10-21T08:08:33.090023+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T08:08:33.090023Z'
  snapshot_sha256: c6ac21555dde32b717b167b832de492634d235439849208305374c43ec62789a
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-references-explained kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
  locator: Actual execution 2026-10-21T08:08:33.094256+00:00 to 2026-10-21T08:08:36.165917+00:00
  summary: Target native reference validation passed; scientific meaning was assessed
    separately.
  support: supports
  accessed_at: '2026-10-21T08:08:36.165917Z'
  snapshot_sha256: a9ba3049fb5cb17435ee36f163e033d6e8a475ebb6cda37889c69935c0007d8f
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T07:06:05.543108+00:00 to 2026-10-21T07:06:16.498440+00:00
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  support: supports
  accessed_at: '2026-10-21T07:06:16.498440Z'
  snapshot_sha256: 7e9c998a5a9fe2b1a28c809bd5eb651205b3256dd64666ef7a9ca6fbde7504fa
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T07:06:16.498920+00:00 to 2026-10-21T07:06:23.361213+00:00
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  support: supports
  accessed_at: '2026-10-21T07:06:23.361213Z'
  snapshot_sha256: 5ba6a0b7c789574c80df1b60d81f0e54454b66e4f919949ad352cff92dd9744e
assessments:
- assessment_id: identity
  area: identity
  topic: SynCom identity and experimental boundary
  outcome: supported
  summary: The cited abstract resolves the requested bacterial/yeast SynCom, while
    exact strains and stage-specific protocols remain unverified.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - abstract
  - ontology
  dimensions:
  - name: community_scope
    value: Tripartite synthetic gut community associated with BSFL protein conversion
    definition: Two bacterial genera and a yeast genus are represented; the host is
      context, not a fourth microbial member.
    evidence_ids:
    - record
    - abstract
  - name: source_strain
    value: Bacillus, Lactobacillus and source-named Issatchenkia at genus rank
    definition: Accessible text does not establish exact species, isolates or strain
      accessions; broad Pichia correspondence does not resolve the yeast isolate.
    evidence_ids:
    - abstract
    - ontology
  - name: environment
    value: Digestive tract of a controlled BSFL host model
    definition: The broad ENVO anchor is valid; gut pH distribution does not establish
      numerical growth pH or causal niche mediation.
    evidence_ids:
    - distribution
    - ontology
  - name: medium
    value: Controlled host diet and waste-application feedstocks require separation
    definition: Chicken manure and kitchen waste are reported applications; no mixed
      formulation or transfer of all baseline rearing conditions is verified.
    evidence_ids:
    - waste
    - preview
  - name: experimental_setting
    value: Controlled gnotobiotic testing plus preliminary waste assays
    definition: The available preview does not resolve microbial status, doses, incubation
      or diet details for each stage.
    evidence_ids:
    - abstract
    - preview
  - name: evidence_tier
    value: Complete abstract plus indexed Introduction and section previews
    definition: The required complete Methods/Results assessment remains unavailable;
      direct proteolysis is reported but its modality is unresolved.
    evidence_ids:
    - abstract
    - preview
    - proteolysis
  - name: grounding_status
    value: Seven correct canonical pairs with genus-level limits
    definition: GTDB checks cover syntax/domain, not fresh reconstruction of historical
      mapping counts.
    evidence_ids:
    - ontology
- assessment_id: taxonomy
  area: grounding
  topic: All three taxa, membership and functional roles
  outcome: concern
  summary: Genus-level membership and Bacillus degradation are abstract-supported;
    exact strains and proteolysis assay provenance remain unresolved.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - abstract
  - ontology
  - proteolysis
  - schema
  details: The two absent functional roles reduce native completeness but should not
    be invented. Membership abundance text is not a numerical abundance measurement.
    Genus-only statements should describe inspected text, not unreviewed full-paper
    contents.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Bacillus Direct Proteolysis'
  outcome: supported
  summary: Consistent with accessible abstract and publisher-highlight scope; full
    experimental certification remains pending.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - proteolysis
  - ontology
  details: Bacillus is the explicit participant and protein breakdown the reported
    endpoint. The node correctly uses OTHER for unresolved assay modality and does
    not infer cross-feeding to the other two members.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Lactobacillus-Issatchenkia Protein-Conversion
    Association'
  outcome: supported
  summary: Consistent with accessible abstract and publisher-highlight scope; full
    experimental certification remains pending.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - association
  - ontology
  details: Lactobacillus and source-named Issatchenkia/Pichia are participants associated
    with host protein conversion and amino-acid responses; the direction is microbial
    treatment toward host outcome, not proven microbial metabolite exchange.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Tripartite Gut-pH Niche Partitioning'
  outcome: supported
  summary: Consistent with accessible abstract and publisher-highlight scope; full
    experimental certification remains pending.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - distribution
  - ontology
  details: The three-member consortium is associated with gut distribution and host
    protein endpoints. The node treats niche partitioning as proposed; pH intervention,
    the 63% comparator and measured protein denominator remain unverified.
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: ALDH-TOR Amino-Acid Host Response'
  outcome: supported
  summary: Consistent with accessible abstract and publisher-highlight scope; full
    experimental certification remains pending.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - host-response
  - ontology
  details: The host ALDH/TOR context is associated with microbiota-responsive amino-acid
    changes. PARTIAL support correctly avoids certifying necessary mediation or reciprocal
    microbial fitness; no absence of unreviewed perturbation experiments is inferred.
- assessment_id: node-4
  area: graph
  topic: 'ecological_interactions[4]: Organic-Waste SynCom-BSFL Proof of Concept'
  outcome: supported
  summary: Consistent with accessible abstract and publisher-highlight scope; full
    experimental certification remains pending.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - waste
  - ontology
  - waste-highlight
  details: The SynCom-host system is applied to chicken manure and kitchen waste with
    reported selected performance gains. Direction is treatment toward application
    outcomes; the abstract does not establish a combined feed recipe or all host-rearing
    conditions. The primary highlight specifically reports waste protein degradation,
    supporting GO:0030163 context; the current vague performance snippet should be
    supplemented with claim-level evidence when Methods is available.
- assessment_id: arrows
  area: graph
  topic: Current downstream graph
  outcome: supported
  summary: No downstream arrows remain; workflow, pH mediation and metabolite-transfer
    edges should not be invented.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - history
  - abstract
- assessment_id: environment
  area: scope
  topic: Origin, category, state and environmental context
  outcome: supported
  summary: SYNTHETIC, ENGINEERED and BIOTECHNOLOGY are consistent with deliberate
    assembly; the digestive-tract anchor is appropriately broad.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - abstract
  - ontology
  details: The global absence claim about insect-gut ENVO terms requires narrower
    wording; it is not a defect in the chosen valid parent term.
- assessment_id: cultivation
  area: scope
  topic: One growth-media entry with two feedstocks
  outcome: concern
  summary: The entry merges contexts that the accessible evidence does not establish
    as one recipe or gnotobiotic baseline protocol.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - waste
  - preview
  details: Do not infer a growth temperature, numerical gut pH, diet composition,
    oxygen regime or duration from inaccessible Methods. The preview's 0/12/24-day
    omics context is not automatically the duration of every SynCom or waste assay.
- assessment_id: resources
  area: completeness
  topic: Datasets, cross-Mech links, chemicals and proteins
  outcome: unknown
  summary: No encoded dataset or cross-Mech ID requires verification; inaccessible
    details prevent a concrete missing-resource or exact-protein finding.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - datasets
  - preview
  - adapter
  details: ALDH and TOR name host functions without verified gene/protein identifiers.
    Do not assign a microbial protein accession, fabricate exchanged amino acids or
    infer metal relevance from unrelated bibliography.
- assessment_id: provenance
  area: provenance
  topic: Snippet fidelity, graph repair and source limits
  outcome: supported
  summary: The eleven snippets match fresh abstracts and the prior graph repair preserves
    the unresolved Methods boundary.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - snippets
  - history
  - issue-1250
  - independent-source
- assessment_id: validation
  area: schema
  topic: Native gates and incomplete source certification
  outcome: concern
  summary: Seven focused gates and cache preflight pass; the required full-source
    check remains unavailable and corpus network failures remain explicit.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - ontology
  - snippets
  - check-validate
  - check-validate-strict
  - check-audit-network
  - native-target
  - independent-source
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality within partial review
  outcome: supported
  summary: Completeness is 25 and native quality caps at 100; these scores cannot
    certify the unavailable whole-source assessment.
  target_ids:
  - CommunityMech:000284
  evidence_ids:
  - record
  - schema
  - native-target
  metrics:
  - name: completeness
    value: 25
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including all taxon roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). 0 + 5 + 0 + 10 + 0 + 10 + 0 + 0 = 25; absent optional
      Lactobacillus/yeast roles withhold the required-field component but are not
      schema defects.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). Observed P1=0, P2=1, P3=2, P4=0; 5 items /
      5 nodes = 1; native COMPLETE. 100 - 10 - 4 + 10 + 15 = 111 before capping. Counts
      cover assessed material only; this is not a completed scientific-source pass.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count within this partial review.
  - name: P2
    value: 1
    unit: findings
    definition: Observed native severity count within this partial review.
  - name: P3
    value: 2
    unit: findings
    definition: Observed native severity count within this partial review.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count within this partial review.
findings:
- finding_id: cultivation-context
  issue_key: cm-000284-cultivation-context
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: unsupported transfer between experimental contexts
    changes the represented cultivation protocol.'
  rule_id: review-checklist.cultivation
  status: open
  certainty: confirmed
  title: The growth-medium entry transfers conditions between experimental contexts
  description: The composition lists chicken manure and kitchen waste together, and
    preparation notes connect these feedstocks to germ-free baseline rearing. Accessible
    abstract and preview support controlled gnotobiotic work followed by short-term
    waste applications, but not a single mixed recipe or identical cultivation conditions
    across stages. This is unsupported protocol attribution, not proof that the opposite
    protocol was used.
  target_ids:
  - CommunityMech:000284
  field_paths:
  - growth_media[0].name
  - growth_media[0].composition
  - growth_media[0].preparation_notes
  - growth_media[0].evidence
  evidence_ids:
  - record
  - abstract
  - waste
  - preview
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    role: canonical_record
- finding_id: proteolysis-tier
  issue_key: cm-000284-proteolysis-tier
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded assay-provenance or source-scope wording
    defect; identity and cautious abstract-level graph remain intact.'
  rule_id: review-checklist.evidence_placement
  status: open
  certainty: confirmed
  title: Taxonomy assigns a specific proteolysis modality that remains unverified
  description: The Bacillus taxonomy evidence is tagged IN_VIVO while its explanation
    asserts direct protein degradation. The same record correctly leaves this measurement's
    format unspecified and uses OTHER in node 0. The abstract reports activity but
    does not resolve whether its direct assay was isolated culture or living gut.
  target_ids:
  - CommunityMech:000284
  field_paths:
  - taxonomy[0].evidence[0].evidence_source
  - taxonomy[0].evidence[0].explanation
  evidence_ids:
  - record
  - proteolysis
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    role: canonical_record
- finding_id: source-scope-notes
  issue_key: cm-000284-source-scope-notes
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded assay-provenance or source-scope wording
    defect; identity and cautious abstract-level graph remain intact.'
  rule_id: review-checklist.source_scope
  status: open
  certainty: confirmed
  title: Notes generalize beyond the inspected sources and ontology search
  description: Taxonomy notes say the paper names the relevant members only at genus
    rank although full Methods was not accessed; environment notes assert no insect-gut-specific
    ENVO term without a documented exhaustive ontology claim. These broad absence
    statements exceed the verified scope, even though the current genus and parent-environment
    anchors are valid.
  target_ids:
  - CommunityMech:000284
  field_paths:
  - taxonomy[0].taxon_term.notes
  - taxonomy[1].taxon_term.notes
  - environment_term.notes
  evidence_ids:
  - ontology
  - ontology-search
  - abstract
  - preview
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    role: canonical_record
actions:
- action_id: fix-cultivation-context
  description: Separate controlled host-model cultivation from waste-application contexts
    and retain unresolved assay-specific conditions pending full Methods.
  finding_ids:
  - cultivation-context
  target_ids:
  - CommunityMech:000284
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    role: canonical_record
  acceptance_checks:
  - Do not present the two named wastes as one verified mixture.
  - Attach evidence to each stage and avoid transferring germ-free status, diet or
    incubation between stages without source support.
  - Do not reconstruct the truncated diet ratio or use omics timepoints as every assay
    duration.
  - Revisit full Methods when accessible, then run strict/reference checks.
- action_id: fix-proteolysis-tier
  description: Align claim-specific assay provenance with the graph's unresolved modality
    until the relevant Methods is inspected.
  finding_ids:
  - proteolysis-tier
  target_ids:
  - CommunityMech:000284
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    role: canonical_record
  acceptance_checks:
  - Keep the source-supported Bacillus role and activity report.
  - Do not equate an in-vivo SynCom experiment with an in-vivo assay for every member
    phenotype.
  - Use OTHER or separate membership from activity evidence as supported by schema;
    do not declare an in-vitro assay without evidence.
  - Reference validation passes.
- action_id: fix-source-scope-notes
  description: Scope the notes to the accessible abstract and the verified broad ontology
    anchors, preserving unresolved species/strain and environment specificity.
  finding_ids:
  - source-scope-notes
  target_ids:
  - CommunityMech:000284
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    role: canonical_record
  acceptance_checks:
  - Do not claim full-paper absence of strain names or global ontology absence.
  - Retain Pichia/Issatchenkia as broad related-synonym correspondence, not an authenticated
    strain match.
  - Any more specific future grounding must be separately source-verified.
  - Term and reference checks pass.
- action_id: complete-source-assessment
  description: When authorized full text becomes available, review critical Methods/Results
    and relevant supplements for exact member strains, proteolysis modality, baseline
    versus waste protocols, 63% endpoint/comparator, and ALDH/pH perturbations; then
    reassess the record in a new immutable review.
  finding_ids:
  - cultivation-context
  - proteolysis-tier
  - source-scope-notes
  target_ids:
  - CommunityMech:000284
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BSFL_Gut_SynCom_Bacillus_Lactobacillus_Issatchenkia.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve current uncertainty until inspected primary evidence supports narrower
    claims.
  - Do not purchase access, contact authors or infer missing experiments from this
    review.
  - Attach claim-level evidence and rerun native gates before any separately authorized
    curation.
limitations:
- 'This is not a completed scientific record certification: required critical full
  Methods/Results remain unavailable. The available primary preview contains some
  Methods and Results, so no global absence claim is made.'
- DOI retrieval yields a redirect shell, direct publisher access returns HTTP 403,
  and public TDM returns metadata only. The author repository has an abstract/DOI
  link; an OA flag does not supply a verified manuscript. No credentials, purchase
  or access-control bypass was used.
- Exact microbial species/strains, inoculum doses, culture media, gut-pH values, baseline
  diet, waste-assay microbial status and assay durations remain unresolved. A truncated
  diet ratio and introductory omics timepoints were not imported as complete protocols.
- The 63% final-larval-protein statement is retained as source-reported, without an
  inferred comparator, denominator or identity with conversion efficiency.
- ALDH/TOR and pH distribution remain candidate/associated host contexts. No absence
  of perturbation experiments, metabolite transfer or deposited datasets is inferred
  from inaccessible sections.
- Genus-level ontology anchors and Pichia related-synonym metadata do not authenticate
  isolate identities. The bounded ENVO search does not prove global absence of an
  insect-specific term.
- Historical GTDB mapping counts were not recomputed; optional structured-adapter
  discovery was reused and no external-checkout runner or strain/module query was
  executed.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 23 words for Yu 2026, including primary highlights.
- Native quality 100 is capped from 111 and is not a substitute for the unavailable
  scientific-source assessment.
tags:
- record-review
- partial
- gut
- synthetic-community
- batch-04
```
