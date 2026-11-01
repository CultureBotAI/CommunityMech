# Bacillus-Pseudomonas chili SynCom T7: partial record review

- Review: 20261021T090637Z-bacillus-pseudomonas-chili-t7-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T09:02:10.677254Z
- Finished UTC: 2026-10-21T09:06:37.212111Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Partial review: critical main text and exact T7 formulation remain unavailable. One major finding groups unsupported mutualism/syntrophic roles, incorrect bacterial participants and two causal arrows while preserving reported biocontrol and plant-response outcomes. Three nodes and both arrows were individually assessed; native checks pass but do not establish those mechanisms.

## Scope And Provenance

Entire canonical record and all three nodes/two arrows assessed against fresh abstract/metadata, abstract-only cache, actual schema and native/OAK diagnostics. Full main/supplementary Methods, T7 strain formulation, figures and raw data remain unreviewed.

Selection: Next assigned maintained path after CommunityMech:000373 in batch05; the source treatment T7 is uniquely resolved while exact composition remains uncertain.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c6e5a9b9af2d05e12eaafb2555a53f3a079268f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000483 | kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml | maintained | Bacillus and Pseudomonas Antagonistic Synthetic Community T7 Against Chili Root Rot |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000483 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000483 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000483 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000483 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000483 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000483 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000483 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000483 | Target reference validation passed against the abstract cache. |
| audit-network | failed | True | CommunityMech:000483 | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-network-quality | failed | True | CommunityMech:000483 | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| Publication identifiers and fresh abstract | passed | True | CommunityMech:000483 | Fresh bibliographic metadata and abstract identify the study and support its reported outcomes. |
| Complete critical Methods, formulation and causal evidence | unavailable | True | CommunityMech:000483 | Main text, T7 formulation, assay details and supplementary figures remain unavailable through inspected public routes. |
| Encoded dataset accessions | not_applicable | False | CommunityMech:000483 | No dataset accession is encoded or established in the bounded accessible material. |
| Encoded medium/ingredient-Mech links | not_applicable | False | CommunityMech:000483 | No CultureMech or MediaIngredientMech ID is encoded; no recipe equivalence was inferred. |
| Optional structured source adapter | unavailable | False | CommunityMech:000483 | Same-runtime batch05 discovery is reused; no external runner or strain-module query was executed. |

## Scientific And Domain Assessments

### Source T7 treatment versus genus candidate pool

identity: unknown. Targets: CommunityMech:000483.

The named T7 study is resolved, but its precise isolate roster and formulation cannot be certified from the abstract.

### Both genus entries and functional roles

grounding: concern. Targets: CommunityMech:000483.

Antagonist-pool attribution is supported; syntrophic roles are unsupported by the attached evidence.

Bacillus and Pseudomonas are source biomarker genera, but actual T7 roster and prominence remain unverified. DOMINANT is ordinal, not a percentage violation; LEfSe biomarker status alone does not certify composition within the engineered formulation.

### ecological_interactions[0]: Cooperative Bacillus-Pseudomonas Antagonism Against Rhizosphere Fusarium solani

graph: concern. Targets: CommunityMech:000483.

Antagonism toward the pathogen does not support Bacillus-to-Pseudomonas PAIRWISE MUTUALISM.

Encoded source Bacillus and target Pseudomonas are possible inoculant components, whereas the reported negative effect is on F. solani. Reframe at the verified antagonist/community-to-pathogen scope; no reciprocal member fitness or T7-specific cooperative mechanism is certified.

### ecological_interactions[1]: Pathogen Suppression and Reduction of Chili Root Rot Incidence by SynCom T7

graph: concern. Targets: CommunityMech:000483.

Retain source-reported efficacy while correcting bacterial recipient and mutualism semantics.

The encoded Bacillus-to-Pseudomonas direction denotes neither the suppressed pathogen nor the chili disease endpoint. T7 treatment, F. solani suppression and host incidence must be represented at distinct correct scopes; detailed efficacy assay conditions remain unknown.

### ecological_interactions[2]: Activation of Plant MAPK, Ethylene, Jasmonic Acid, and Salicylic Acid Systemic Resistance

graph: concern. Targets: CommunityMech:000483.

The pathway statement concerns the plant, not Pseudomonas-to-Bacillus mutualism.

Encoded source Pseudomonas and target Bacillus are wrong participants for the stated host process. Preserve the article interpretation with an appropriate community/host scope and unresolved assay tier; do not claim specific hormones were measured or pathways selectively perturbed without Methods.

### ecological_interactions[0].downstream[0]: antagonism -&gt; root-rot suppression

graph: concern. Targets: CommunityMech:000483.

A bounded T7-application-to-efficacy link is source-implied, but the current reciprocal-benefit framing needs repair.

The abstract explicitly links use of the antagonist pool to effective T7 treatment. After correcting node and participant scope, an appropriately bounded source-implied application-to-outcome edge may remain; this does not establish reciprocal bacterial benefit or every specific mediator. Exact formulation and assay context remain unverified.

### ecological_interactions[1].downstream[0]: suppression -&gt; host immune activation

graph: concern. Targets: CommunityMech:000483.

Concurrent outcomes do not entail the asserted suppression/colonization-to-immune direction.

The source names T7 efficacy and induced resistance; the edge adds rhizosphere colonization and places pathogen suppression upstream of plant pathways. Neither that direction nor bacterial-recipient mutualism follows from the inspected abstract; causal orientation requires targeted source assessment.

### Cropping conditions, metabolites, cultivation and resources

completeness: unknown. Targets: CommunityMech:000483.

Rhizosphere context is supported; exact cultivation, strain and deposited-data details remain unavailable.

Cropping-associated sequencing shifts do not prove absolute population loss or T7 abundance. Named plant hormone pathways do not warrant metabolite-exchange fields. No metal/rare-earth processing role is supported; no omission finding is invented from inaccessible Methods.

### Identifiers, cache, history and access boundaries

evidence: supported. Targets: CommunityMech:000483.

Publication identity and snippet text verify, while the earlier mechanistic interpretation needs reassessment.

The cache is abstract-only. Open-license wording and EPMC access flags conflict, so the limitation is unsuccessful retrieval rather than proven paywall status. Prior review hashes are preserved without endorsing their causal judgment.

### Native diagnostics versus scientific support

schema: concern. Targets: CommunityMech:000483.

All eight native checks pass, but required full-source access is unavailable and the semantic graph finding remains.

### Native completeness and quality within partial review

completeness: supported. Targets: CommunityMech:000483.

Completeness is 65 and capped quality 100; structural scores do not certify the bacterial mechanisms.

## Findings

### interaction-scope-and-causality: Pathogen and plant outcomes are encoded as reciprocal bacterial mechanisms

major / open / confirmed; issue key: cm-000483-interaction-scope-and-causality.

All three nodes use PAIRWISE MUTUALISM between the bacterial genera, both taxa carry SYNTROPHIC_PARTNER, and both arrows inherit that misframing; the suppression-to-immunity direction additionally exceeds the attached abstract. The evidence reports antagonist selection, T7 efficacy and plant pathways, without establishing member benefit, product-consuming cooperation, colonization or the suppression-to-immunity direction.

## Recommended Actions And Acceptance Checks

### repair-interaction-scope

Retain reported T7 phenotypes while correcting participant scope and removing unsupported bacterial mechanisms.

- Remove or qualify MUTUALISM and SYNTROPHIC_PARTNER unless inspected member-level evidence establishes their actual schema meanings; obligacy is not required.
- Represent pathogen antagonism and chili responses at appropriate community/target scope instead of Bacillus-Pseudomonas reciprocal benefit.
- Fusarium solani NCBITaxon:169388 is a verified species-label candidate; Capsicum annuum NCBITaxon:4072 matches the record name but needs full-source host-species confirmation. These targets need not join microbial taxonomy.
- Keep T7 exact strain roster/proportions unresolved until primary formulation tables/Methods are inspected; do not infer two strains from two genus entries.
- After scope correction, a bounded source-implied T7-application-to-efficacy link may remain; do not infer a selective bacterial mechanism from it.
- Remove or explicitly source-qualify suppression-to-immune direction and unsupported colonization; simultaneous outcomes alone do not entail that arrow.
- Retain immune-pathway statements as source-reported until their assay modality and selective causality are verified.
- Add a concrete discussion documenting unavailable source context; rerun schema, strict, references and network gates after separately authorized curation, with a new history event.

### complete-source-assessment

When the publicly licensed main article and supplement are accessible, inspect T7 composition, cultivation, controls, immune measurements and data availability before a new scientific review.

- Preserve genus-pool versus T7 roster uncertainty until exact source tables/Methods are read.
- Verify causal intervention/measurement scope rather than infer it from the abstract pathway names.
- Record actual source strain/data identifiers only when resolved; no invented media, metabolites or missing-dataset claim.
- No purchase, author contact, canonical edit or status promotion is authorized by this review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml; Entire target: two genus entries, three nodes and two arrows | supports | The record denotes source treatment T7 but models pathogen/plant endpoints as reciprocal interactions between Bacillus and Pseudomonas. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42693392&amp;retmode=xml; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42693392&amp;retmode=xml | supports | Fresh article-level PubMed metadata verifies PMID 42693392, DOI 10.1094/PDIS-06-25-1298-RE, title and abstract; the abstract explicitly states CC BY 4.0. |
| crossref | https://api.crossref.org/works/10.1094/PDIS-06-25-1298-RE; https://api.crossref.org/works/10.1094/PDIS-06-25-1298-RE | supports | Fresh Crossref DOI/title metadata identifies the same APS article and its tested PDF route. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42693392&amp;format=json&amp;resultType=core; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42693392&amp;format=json&amp;resultType=core | supports | Fresh Europe PMC metadata supplies the matching abstract, no PMC identifier and a subscription flag; that flag does not override the abstract open-license statement. |
| access | Public APS full HTML and Crossref-linked PDF; access-audit.json: exact request timestamps, HTTP status and body hashes | context_only | Both public requests returned 403 challenge pages; the review has no main Methods/Results or figures. Access failure is not proof that this openly licensed article is paywalled. |
| antagonism | PMID:42693392; Fresh PubMed abstract: LEfSe/isolated-antagonist statement | supports | The source links the two biomarker genera to isolates antagonistic to F. solani, not to reciprocal bacterial benefit or partner-product consumption. |
| design | PMID:42693392; Fresh PubMed abstract: nine candidate SynComs and selected T7 | supports | The abstract names the selected treatment but does not enumerate T7 strain identities, counts, proportions or each candidate combination. |
| efficacy | PMID:42693392; Fresh PubMed abstract: T7 efficacy statement | supports | T7 pathogen suppression and lower root-rot incidence are source-reported; their detailed protocol, comparator and quantitative magnitude remain unreviewed. |
| host-response | PMID:42693392; Fresh PubMed abstract: MAPK/ethylene/JA/SA statement | supports | The stated pathways concern the plant response. They are not Pseudomonas-to-Bacillus signaling or evidence that both bacterial partners benefit. |
| direction | PMID:42693392; Fresh PubMed abstract: concurrent efficacy and induced-resistance outcomes | supports | The source attributes resistance to T7 but does not specify suppression/colonization as the upstream cause of immune activation; exact assay modality and selective pathway mediation remain unverified. |
| environment | PMID:42693392; Fresh PubMed abstract: continuous-cropping microbiome comparison | supports | Sequencing reports increased Fusarium abundance and declining Bacillus/Pseudomonas representation under prolonged cropping. These are ecological associations distinct from the defined T7 intervention. |
| ontology | Local OAK NCBITaxon, ENVO and GO snapshots; Five unique ID/label pairs at fourteen occurrences | supports | All canonical labels match, including Bacillus &lt;firmicutes&gt;; both bacterial IDs are genus-ranked. Defense GO terms are compatible with plant processes but do not authenticate the encoded bacterial recipients. |
| participant-candidates | Local OAK NCBITaxon snapshot; participant-grounding-candidates.json: optional external targets | supports | Fusarium solani matches NCBITaxon:169388; the record-named Capsicum annuum matches NCBITaxon:4072, both species. The abstract names only chili for the host, so verify its species in the full source before applying that candidate; no isolate or species-complex identity is inferred. |
| schema | src/communitymech/schema/communitymech.yaml; InteractionTypeEnum.MUTUALISM/SYNTROPHY; FunctionalRoleEnum.SYNTROPHIC_PARTNER/PATHOGEN_ANTAGONIST; AbundanceEnum.DOMINANT | supports | MUTUALISM requires benefit to both organisms. Syntrophic cooperation involves partner-product consumption/removal making metabolism favorable, without an obligacy requirement. Collective pathogen control alone establishes neither relation. |
| snippets | kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml; snippet-audit.json: all current evidence occurrences | supports | Current snippets match the pinned abstract cache and fresh abstract; exact words do not establish the added participant directions or causal mediation. |
| datasets | Accessible abstract and metadata; dataset-verification.json: bounded accession/resource scope | supports | No encoded dataset accession is available for validation; inaccessible main/supplementary data statements are not treated as evidence of absent data. |
| history | Two target sidecars; 20261020-stage2-fifteen-records-batch133.yaml; Target decision lines 2101-2246 | supports | The prior hash matches. The previous abstract-based certification of pairwise mutualism and both directions is reassessed against the same source meaning; historical files remain unchanged. |
| search | Owned maintained community/isolate/reusable-taxon roots; Ignored-inclusive bounded record/source/taxon lookup | supports | Genus-level occurrences elsewhere cannot supply T7 isolate membership; exact roster remains unresolved from accessible source content. |
| adapter | Optional kg-microbe-sources runner; Explicit same-batch05 runtime reuse of 000120 discovery at 08:47:38Z | supports | No callable owned-runtime adapter was available; no external runner or strain/module coverage query was executed. |
| native-target | NetworkIntegrityAuditor().audit_community(target); support-audit.json: targeted API and native score components | supports | The native graph is structurally COMPLETE; five evidence items across three nodes give mean 5/3. It does not validate reciprocal benefit or causal entailment. |
| independent-source | PMID:42693392; root-source-access.json: independent abstract/access and graph assessment | supports | Independent source review preserves the reported efficacy while identifying unsupported bacterial mechanisms and inaccessible critical main context. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml; Actual execution 2026-10-21T09:02:19.920746+00:00 to 2026-10-21T09:02:21.125934+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-strict kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml --out /private/tmp/cm-review-session/batch-05/000483/strict-report.tsv; Actual execution 2026-10-21T09:02:19.923780+00:00 to 2026-10-21T09:02:23.377011+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-terms kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml; Actual execution 2026-10-21T09:02:19.926815+00:00 to 2026-10-21T09:02:22.825915+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-gtdb kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml; Actual execution 2026-10-21T09:02:21.126307+00:00 to 2026-10-21T09:02:21.246478+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml; Actual execution 2026-10-21T09:02:21.246785+00:00 to 2026-10-21T09:02:23.619606+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-history history/records/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7; Actual execution 2026-10-21T09:02:22.826334+00:00 to 2026-10-21T09:02:23.906071+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T09:02:23.907997+00:00 to 2026-10-21T09:02:24.002283+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-references-explained kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml; Actual execution 2026-10-21T09:02:24.002595+00:00 to 2026-10-21T09:02:25.318375+00:00 | supports | Target reference validation passed against the abstract cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T08:44:47.720127+00:00 to 2026-10-21T08:45:04.195128+00:00 | supports | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T08:44:47.737345+00:00 to 2026-10-21T08:45:04.925187+00:00 | supports | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |

## Limits And Additional Notes

- The abstract explicitly states CC BY 4.0, while EPMC marks subscription access and no PMC record. Public APS HTML/PDF retrieval failed 403; the report records unsuccessful access rather than declaring a paywall.
- The exact T7 strain roster, proportions, preparation, dose, controls, timing and experimental vessels are unavailable. Two genus entries do not establish a two-strain community or prove both genera occur in every candidate SynCom.
- The abstract reports plant pathway activation and induced resistance; its assay modality, causal perturbations and spatial/systemic design were not independently assessed. Missing accessible evidence is not proof that experiments were absent.
- Biomarker abundance shifts, antagonist activity, community efficacy and plant signaling are distinct scopes. No partner-fitness, syntrophic transfer, rhizosphere colonization or selective suppression-to-immunity pathway was verified.
- Current snippets match abstract evidence, but exact lexical support does not entail the encoded mutualism or directed mediation. Prior history is retained unchanged and its scientific interpretation reassessed.
- No dataset or cultivation omission is inferred from inaccessible main/supplementary text. No raw community, sequence, metabolite or plant-pathway data were analyzed.
- Historical GTDB genus mapping fractions/counts/releases were not recomputed; optional adapter discovery was explicitly reused in the same batch05 runtime without executing an external checkout.
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 23 words for this publication, all from the fresh abstract.
- All 24 repository inputs were pinned before assessment and rechecked; quality 100 is capped from 121.6666667 and is not scientific certification.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T090637Z-bacillus-pseudomonas-chili-t7-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Bacillus-Pseudomonas chili SynCom T7: partial record review'
started_at: '2026-10-21T09:02:10.677254Z'
finished_at: '2026-10-21T09:06:37.212111Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Canonical inputs unchanged; separate agents assessed available
    sources, ontology, native gates, snippets, history and metrics. No person-level
    independence beyond task roles is claimed.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: 'Partial review: critical main text and exact T7 formulation remain unavailable.
  One major finding groups unsupported mutualism/syntrophic roles, incorrect bacterial
  participants and two causal arrows while preserving reported biocontrol and plant-response
  outcomes. Three nodes and both arrows were individually assessed; native checks
  pass but do not establish those mechanisms.'
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
  - path: history/records/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7/2026-10-19T053000Z-antigravity-4b3e.yaml
    sha256: d748e29a6b21faf6bdc9a37f17390a49f38a8dc400c46375db756bbde918e7c1
    role: context
  - path: history/records/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7/2026-10-20T041800Z-antigravity-99f70a.yaml
    sha256: 30299ecfd3c414ea7ae3d99e943f1e97e94b5ebe98cd8a4c0545a3e28658c3b3
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
    sha256: 99f70a387a6393d7fb059eeb8d2294c590e32ee7503a78a5e68866c3dfe545ff
    role: target
  - path: references_cache/PMID_42693392.txt
    sha256: a0c9e8567d9a2c123794102ccbcae5fbcac6796fb57c160ab193aac7783284fb
    role: context
  - path: reports/causal_graph_review/decisions/20261020-stage2-fifteen-records-batch133.yaml
    sha256: e9ded35a2333f9994869573f9f952b3af3191ab55528813a7f2c03639a362d3f
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
- target_id: CommunityMech:000483
  path: kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  label: Bacillus and Pseudomonas Antagonistic Synthetic Community T7 Against Chili
    Root Rot
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
    role: canonical_record
scope:
  description: Entire canonical record and all three nodes/two arrows assessed against
    fresh abstract/metadata, abstract-only cache, actual schema and native/OAK diagnostics.
    Full main/supplementary Methods, T7 strain formulation, figures and raw data remain
    unreviewed.
  selection: Next assigned maintained path after CommunityMech:000373 in batch05;
    the source treatment T7 is uniquely resolved while exact composition remains uncertain.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000483
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000483
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight
    in the owned batch05 runtime.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000483
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-strict kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
    --out /private/tmp/cm-review-session/batch-05/000483/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight
    in the owned batch05 runtime.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000483
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-terms kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight
    in the owned batch05 runtime.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000483
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight
    in the owned batch05 runtime.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000483
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight
    in the owned batch05 runtime.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000483
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-history history/records/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight
    in the owned batch05 runtime.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000483
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight
    in the owned batch05 runtime.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target reference validation passed against the abstract cache.
  target_ids:
  - CommunityMech:000483
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-references-explained kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight
    in the owned batch05 runtime.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000483
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Reused fresh full-corpus batch05 execution, not a target-specific pass
    or scientific certification.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000483
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Reused fresh full-corpus batch05 execution, not a target-specific pass
    or scientific certification.
- check_id: publication-identity
  name: Publication identifiers and fresh abstract
  status: passed
  required: true
  summary: Fresh bibliographic metadata and abstract identify the study and support
    its reported outcomes.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - snippets
- check_id: full-primary-source
  name: Complete critical Methods, formulation and causal evidence
  status: unavailable
  required: true
  summary: Main text, T7 formulation, assay details and supplementary figures remain
    unavailable through inspected public routes.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - access
  - independent-source
  - design
  scope_note: Abstract assessment does not certify exact T7 membership, experimental
    conditions or selective mechanisms.
- check_id: source-data
  name: Encoded dataset accessions
  status: not_applicable
  required: false
  summary: No dataset accession is encoded or established in the bounded accessible
    material.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - datasets
- check_id: cross-mech
  name: Encoded medium/ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech ID is encoded; no recipe equivalence
    was inferred.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - record
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Same-runtime batch05 discovery is reused; no external runner or strain-module
    query was executed.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  locator: 'Entire target: two genus entries, three nodes and two arrows'
  summary: The record denotes source treatment T7 but models pathogen/plant endpoints
    as reciprocal interactions between Bacillus and Pseudomonas.
  support: supports
  accessed_at: '2026-10-21T09:06:37.201079Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42693392&retmode=xml
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42693392&retmode=xml
  summary: Fresh article-level PubMed metadata verifies PMID 42693392, DOI 10.1094/PDIS-06-25-1298-RE,
    title and abstract; the abstract explicitly states CC BY 4.0.
  support: supports
  accessed_at: '2026-10-21T09:02:25.501716Z'
  snapshot_sha256: 502347de07b8b6a5406a0b1d28032ab89d90dedc52a1a31a0d62c69265d35699
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1094/PDIS-06-25-1298-RE
  locator: https://api.crossref.org/works/10.1094/PDIS-06-25-1298-RE
  summary: Fresh Crossref DOI/title metadata identifies the same APS article and its
    tested PDF route.
  support: supports
  accessed_at: '2026-10-21T09:02:37.752573Z'
  snapshot_sha256: ae723648e7cdc14f6ebae77e365a27e1b7091262ef76e8a667f0a4a0ab58554f
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42693392&format=json&resultType=core
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42693392&format=json&resultType=core
  summary: Fresh Europe PMC metadata supplies the matching abstract, no PMC identifier
    and a subscription flag; that flag does not override the abstract open-license
    statement.
  support: supports
  accessed_at: '2026-10-21T09:02:25.819449Z'
  snapshot_sha256: 22d9d999b652cf17970ecc61d5c7d4d2d93917f61d97390b4fdc3730672c8f5c
- evidence_id: access
  kind: validation
  reference: Public APS full HTML and Crossref-linked PDF
  locator: 'access-audit.json: exact request timestamps, HTTP status and body hashes'
  summary: Both public requests returned 403 challenge pages; the review has no main
    Methods/Results or figures. Access failure is not proof that this openly licensed
    article is paywalled.
  support: context_only
  accessed_at: '2026-10-21T09:06:37.202038Z'
  snapshot_sha256: 85e0b1e577b837cc72f6171faf3a723e64e7ac63050cc535f386ad85f9a6f8af
- evidence_id: antagonism
  kind: primary_source
  reference: PMID:42693392
  locator: 'Fresh PubMed abstract: LEfSe/isolated-antagonist statement'
  summary: The source links the two biomarker genera to isolates antagonistic to F.
    solani, not to reciprocal bacterial benefit or partner-product consumption.
  support: supports
  accessed_at: '2026-10-21T09:06:37.203532Z'
  quote: significant antagonistic effects against Fusarium solani
  snapshot_sha256: 502347de07b8b6a5406a0b1d28032ab89d90dedc52a1a31a0d62c69265d35699
- evidence_id: design
  kind: primary_source
  reference: PMID:42693392
  locator: 'Fresh PubMed abstract: nine candidate SynComs and selected T7'
  summary: The abstract names the selected treatment but does not enumerate T7 strain
    identities, counts, proportions or each candidate combination.
  support: supports
  accessed_at: '2026-10-21T09:06:37.203544Z'
  quote: nine different synthetic communities
- evidence_id: efficacy
  kind: primary_source
  reference: PMID:42693392
  locator: 'Fresh PubMed abstract: T7 efficacy statement'
  summary: T7 pathogen suppression and lower root-rot incidence are source-reported;
    their detailed protocol, comparator and quantitative magnitude remain unreviewed.
  support: supports
  accessed_at: '2026-10-21T09:06:37.203547Z'
  quote: reduced the incidence of root rot
- evidence_id: host-response
  kind: primary_source
  reference: PMID:42693392
  locator: 'Fresh PubMed abstract: MAPK/ethylene/JA/SA statement'
  summary: The stated pathways concern the plant response. They are not Pseudomonas-to-Bacillus
    signaling or evidence that both bacterial partners benefit.
  support: supports
  accessed_at: '2026-10-21T09:06:37.203548Z'
  quote: plant immune-associated pathways
- evidence_id: direction
  kind: primary_source
  reference: PMID:42693392
  locator: 'Fresh PubMed abstract: concurrent efficacy and induced-resistance outcomes'
  summary: The source attributes resistance to T7 but does not specify suppression/colonization
    as the upstream cause of immune activation; exact assay modality and selective
    pathway mediation remain unverified.
  support: supports
  accessed_at: '2026-10-21T09:06:37.203550Z'
  quote: enhanced systemic induced resistance
- evidence_id: environment
  kind: primary_source
  reference: PMID:42693392
  locator: 'Fresh PubMed abstract: continuous-cropping microbiome comparison'
  summary: Sequencing reports increased Fusarium abundance and declining Bacillus/Pseudomonas
    representation under prolonged cropping. These are ecological associations distinct
    from the defined T7 intervention.
  support: supports
  accessed_at: '2026-10-21T09:06:37.203552Z'
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO and GO snapshots
  locator: Five unique ID/label pairs at fourteen occurrences
  summary: All canonical labels match, including Bacillus <firmicutes>; both bacterial
    IDs are genus-ranked. Defense GO terms are compatible with plant processes but
    do not authenticate the encoded bacterial recipients.
  support: supports
  accessed_at: '2026-10-21T09:06:37.204520Z'
  snapshot_sha256: 1a2dc12e550b5abd4bf7ae231182c478606ead2acd357f466d0c03c1d7561dd8
- evidence_id: participant-candidates
  kind: authority
  reference: Local OAK NCBITaxon snapshot
  locator: 'participant-grounding-candidates.json: optional external targets'
  summary: Fusarium solani matches NCBITaxon:169388; the record-named Capsicum annuum
    matches NCBITaxon:4072, both species. The abstract names only chili for the host,
    so verify its species in the full source before applying that candidate; no isolate
    or species-complex identity is inferred.
  support: supports
  accessed_at: '2026-10-21T09:06:37.204757Z'
  snapshot_sha256: 0dc72b88ec4772c0a633c366de3fe786a5c5c8b24c2b3d5cd8abed07f10054ec
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: InteractionTypeEnum.MUTUALISM/SYNTROPHY; FunctionalRoleEnum.SYNTROPHIC_PARTNER/PATHOGEN_ANTAGONIST;
    AbundanceEnum.DOMINANT
  summary: MUTUALISM requires benefit to both organisms. Syntrophic cooperation involves
    partner-product consumption/removal making metabolism favorable, without an obligacy
    requirement. Collective pathogen control alone establishes neither relation.
  support: supports
  accessed_at: '2026-10-21T09:06:37.204762Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  locator: 'snippet-audit.json: all current evidence occurrences'
  summary: Current snippets match the pinned abstract cache and fresh abstract; exact
    words do not establish the added participant directions or causal mediation.
  support: supports
  accessed_at: '2026-10-21T09:06:37.204917Z'
  snapshot_sha256: 589fffe5a9a35a12241fe8917f1ff27a281bdafa40b43cb367478a6a4aac13f4
- evidence_id: datasets
  kind: validation
  reference: Accessible abstract and metadata
  locator: 'dataset-verification.json: bounded accession/resource scope'
  summary: No encoded dataset accession is available for validation; inaccessible
    main/supplementary data statements are not treated as evidence of absent data.
  support: supports
  accessed_at: '2026-10-21T09:06:37.205401Z'
  snapshot_sha256: ad8b6a4df2dd71d601ba1b9d723b82d2005b2f03612adf38037ebb3ab25392c9
- evidence_id: history
  kind: record_content
  reference: Two target sidecars; 20261020-stage2-fifteen-records-batch133.yaml
  locator: Target decision lines 2101-2246
  summary: The prior hash matches. The previous abstract-based certification of pairwise
    mutualism and both directions is reassessed against the same source meaning; historical
    files remain unchanged.
  support: supports
  accessed_at: '2026-10-21T09:06:37.205685Z'
  snapshot_sha256: 1bde007f8a03a5f3f8115fad5280627f1b32057bb54580a720824103bcfe04a8
- evidence_id: search
  kind: search
  reference: Owned maintained community/isolate/reusable-taxon roots
  locator: Ignored-inclusive bounded record/source/taxon lookup
  summary: Genus-level occurrences elsewhere cannot supply T7 isolate membership;
    exact roster remains unresolved from accessible source content.
  support: supports
  accessed_at: '2026-10-21T09:06:37.205831Z'
  snapshot_sha256: b6658129d4f00f6119dc1a749cf1472b2186b4dcd0ce2d41469bf21521a9da78
  search_scope: Stored rg --no-ignore --hidden searches of maintained roots for target/source/genus
    identifiers; bounded, not an exhaustive synonym search.
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources runner
  locator: Explicit same-batch05 runtime reuse of 000120 discovery at 08:47:38Z
  summary: No callable owned-runtime adapter was available; no external runner or
    strain/module coverage query was executed.
  support: supports
  accessed_at: '2026-10-21T09:06:37.205987Z'
  snapshot_sha256: 46fcd75f26a0ce8b1c982b4bc7e1a43fe69ca7347426e23735986a007a1c2668
  search_scope: Original fresh batch05 discovery retained with its timestamp and external-checkout
    boundary.
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: 'support-audit.json: targeted API and native score components'
  summary: The native graph is structurally COMPLETE; five evidence items across three
    nodes give mean 5/3. It does not validate reciprocal benefit or causal entailment.
  support: supports
  accessed_at: '2026-10-21T09:06:37.206148Z'
  snapshot_sha256: c3462f123326f570a65e1a2c1b5a12434536a048a67f5abab8853ff73b7f89e2
- evidence_id: independent-source
  kind: validation
  reference: PMID:42693392
  locator: 'root-source-access.json: independent abstract/access and graph assessment'
  summary: Independent source review preserves the reported efficacy while identifying
    unsupported bacterial mechanisms and inaccessible critical main context.
  support: supports
  accessed_at: '2026-10-21T09:06:37.206350Z'
  snapshot_sha256: 1f289edd1248d9f7a3a7d82132cd6a142136f1fddb1f45c11b2be261a2676fbb
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  locator: Actual execution 2026-10-21T09:02:19.920746+00:00 to 2026-10-21T09:02:21.125934+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T09:02:21.125934Z'
  snapshot_sha256: 3ed661f03af1268970c4c8c9fbcb465363f52bc8d1e8721f5b4e28204ef5a252
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-strict kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
    --out /private/tmp/cm-review-session/batch-05/000483/strict-report.tsv
  locator: Actual execution 2026-10-21T09:02:19.923780+00:00 to 2026-10-21T09:02:23.377011+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T09:02:23.377011Z'
  snapshot_sha256: 4d34c14660426ec7228532d1795fe41ce3acbb516e354816655da331c0107bbc
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-terms kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  locator: Actual execution 2026-10-21T09:02:19.926815+00:00 to 2026-10-21T09:02:22.825915+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T09:02:22.825915Z'
  snapshot_sha256: 4b922e5ff476283c934c8b1284e86c5ecce818bad03467833ae531493e9a2b84
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  locator: Actual execution 2026-10-21T09:02:21.126307+00:00 to 2026-10-21T09:02:21.246478+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T09:02:21.246478Z'
  snapshot_sha256: 8da301fc6b1c9a11e0043d54c6aeba4a56d1c30295d52846e60b9b22f45a7ca3
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  locator: Actual execution 2026-10-21T09:02:21.246785+00:00 to 2026-10-21T09:02:23.619606+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T09:02:23.619606Z'
  snapshot_sha256: ec25c96e8e3f6947caedd61ad1feda28d06845bb647e96812ea179c80bafb3c8
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-history history/records/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7
  locator: Actual execution 2026-10-21T09:02:22.826334+00:00 to 2026-10-21T09:02:23.906071+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T09:02:23.906071Z'
  snapshot_sha256: 289d76e5e892600fee62f91cde4790b98d52baac63e5f78fe7ab1c10e03b28e2
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T09:02:23.907997+00:00 to 2026-10-21T09:02:24.002283+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T09:02:24.002283Z'
  snapshot_sha256: 510c824700cfc230add678428b36a44b8555f5df29ca506d15bee84752af41bb
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-references-explained kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
  locator: Actual execution 2026-10-21T09:02:24.002595+00:00 to 2026-10-21T09:02:25.318375+00:00
  summary: Target reference validation passed against the abstract cache.
  support: supports
  accessed_at: '2026-10-21T09:02:25.318375Z'
  snapshot_sha256: d27a3ed9434855267d9a3453c657df1026f042c2b1e154e1b3c73ee5c5b2f8f7
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T08:44:47.720127+00:00 to 2026-10-21T08:45:04.195128+00:00
  summary: Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  support: supports
  accessed_at: '2026-10-21T08:45:04.195128Z'
  snapshot_sha256: 83a73a6ead4c57534fef4ad456dae148cc75d2127e568a1d0815abaa8cf1b47b
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T08:44:47.737345+00:00 to 2026-10-21T08:45:04.925187+00:00
  summary: Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  support: supports
  accessed_at: '2026-10-21T08:45:04.925187Z'
  snapshot_sha256: 8128f67a5d762dda726f1e6a0c0775a825d030d316c46765c08a359e6b621edb
assessments:
- assessment_id: identity
  area: identity
  topic: Source T7 treatment versus genus candidate pool
  outcome: unknown
  summary: The named T7 study is resolved, but its precise isolate roster and formulation
    cannot be certified from the abstract.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - record
  - design
  - antagonism
  - pubmed
  - ontology
  dimensions:
  - name: community_scope
    value: Engineered rhizosphere SynCom treatment T7
    definition: The two entries are genus aggregates, not proof of a two-strain roster;
      source isolates were used to construct nine candidates.
    evidence_ids:
    - record
    - design
  - name: source_strain
    value: T7 isolate identities/counts/proportions unresolved
    definition: Accessible text names the antagonist pool at genus level but does
      not establish the exact T7 combination or deposited strain identity.
    evidence_ids:
    - antagonism
    - design
    - datasets
  - name: environment
    value: Continuous-cropping chili rhizosphere
    definition: ENVO rhizosphere is compatible; microbiome association and inoculated-treatment
      outcomes must remain distinct.
    evidence_ids:
    - environment
    - ontology
  - name: medium
    value: Unresolved from accessible source
    definition: No medium is encoded; absence of a retrieved protocol is not evidence
      that no cultivation conditions were reported.
    evidence_ids:
    - access
    - record
  - name: experimental_setting
    value: Cropping comparison plus candidate-community biocontrol evaluation
    definition: The abstract reports T7 efficacy but does not resolve vessels, doses,
      controls, timing or immune-assay modality.
    evidence_ids:
    - design
    - efficacy
    - direction
  - name: evidence_tier
    value: Abstract-reported antagonism, disease outcome and plant pathways
    definition: No member-fitness, syntrophic transfer, colonization or selective
      causal mediation is demonstrated in the inspected material.
    evidence_ids:
    - antagonism
    - host-response
    - direction
  - name: grounding_status
    value: Five canonical term pairs; inherited genus GTDB mappings
    definition: Genus-level historical crosswalk counts/fractions/releases were not
      recomputed and cannot identify exact T7 strains.
    evidence_ids:
    - ontology
    - adapter
- assessment_id: taxonomy
  area: grounding
  topic: Both genus entries and functional roles
  outcome: concern
  summary: Antagonist-pool attribution is supported; syntrophic roles are unsupported
    by the attached evidence.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - antagonism
  - design
  - schema
  - ontology
  details: Bacillus and Pseudomonas are source biomarker genera, but actual T7 roster
    and prominence remain unverified. DOMINANT is ordinal, not a percentage violation;
    LEfSe biomarker status alone does not certify composition within the engineered
    formulation.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Cooperative Bacillus-Pseudomonas Antagonism
    Against Rhizosphere Fusarium solani'
  outcome: concern
  summary: Antagonism toward the pathogen does not support Bacillus-to-Pseudomonas
    PAIRWISE MUTUALISM.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - antagonism
  - design
  - schema
  - ontology
  details: Encoded source Bacillus and target Pseudomonas are possible inoculant components,
    whereas the reported negative effect is on F. solani. Reframe at the verified
    antagonist/community-to-pathogen scope; no reciprocal member fitness or T7-specific
    cooperative mechanism is certified.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Pathogen Suppression and Reduction of Chili
    Root Rot Incidence by SynCom T7'
  outcome: concern
  summary: Retain source-reported efficacy while correcting bacterial recipient and
    mutualism semantics.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - efficacy
  - design
  - schema
  details: The encoded Bacillus-to-Pseudomonas direction denotes neither the suppressed
    pathogen nor the chili disease endpoint. T7 treatment, F. solani suppression and
    host incidence must be represented at distinct correct scopes; detailed efficacy
    assay conditions remain unknown.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Activation of Plant MAPK, Ethylene, Jasmonic
    Acid, and Salicylic Acid Systemic Resistance'
  outcome: concern
  summary: The pathway statement concerns the plant, not Pseudomonas-to-Bacillus mutualism.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - host-response
  - direction
  - schema
  - ontology
  details: Encoded source Pseudomonas and target Bacillus are wrong participants for
    the stated host process. Preserve the article interpretation with an appropriate
    community/host scope and unresolved assay tier; do not claim specific hormones
    were measured or pathways selectively perturbed without Methods.
- assessment_id: edge-0-1
  area: graph
  topic: 'ecological_interactions[0].downstream[0]: antagonism -> root-rot suppression'
  outcome: concern
  summary: A bounded T7-application-to-efficacy link is source-implied, but the current
    reciprocal-benefit framing needs repair.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - antagonism
  - design
  - efficacy
  - schema
  details: The abstract explicitly links use of the antagonist pool to effective T7
    treatment. After correcting node and participant scope, an appropriately bounded
    source-implied application-to-outcome edge may remain; this does not establish
    reciprocal bacterial benefit or every specific mediator. Exact formulation and
    assay context remain unverified.
- assessment_id: edge-1-2
  area: graph
  topic: 'ecological_interactions[1].downstream[0]: suppression -> host immune activation'
  outcome: concern
  summary: Concurrent outcomes do not entail the asserted suppression/colonization-to-immune
    direction.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - efficacy
  - host-response
  - direction
  - schema
  details: The source names T7 efficacy and induced resistance; the edge adds rhizosphere
    colonization and places pathogen suppression upstream of plant pathways. Neither
    that direction nor bacterial-recipient mutualism follows from the inspected abstract;
    causal orientation requires targeted source assessment.
- assessment_id: context
  area: completeness
  topic: Cropping conditions, metabolites, cultivation and resources
  outcome: unknown
  summary: Rhizosphere context is supported; exact cultivation, strain and deposited-data
    details remain unavailable.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - environment
  - access
  - datasets
  - record
  details: Cropping-associated sequencing shifts do not prove absolute population
    loss or T7 abundance. Named plant hormone pathways do not warrant metabolite-exchange
    fields. No metal/rare-earth processing role is supported; no omission finding
    is invented from inaccessible Methods.
- assessment_id: provenance
  area: evidence
  topic: Identifiers, cache, history and access boundaries
  outcome: supported
  summary: Publication identity and snippet text verify, while the earlier mechanistic
    interpretation needs reassessment.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - snippets
  - history
  - access
  - independent-source
  details: The cache is abstract-only. Open-license wording and EPMC access flags
    conflict, so the limitation is unsuccessful retrieval rather than proven paywall
    status. Prior review hashes are preserved without endorsing their causal judgment.
- assessment_id: validation
  area: schema
  topic: Native diagnostics versus scientific support
  outcome: concern
  summary: All eight native checks pass, but required full-source access is unavailable
    and the semantic graph finding remains.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - ontology
  - snippets
  - check-validate
  - check-validate-strict
  - native-target
  - schema
  - access
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality within partial review
  outcome: supported
  summary: Completeness is 65 and capped quality 100; structural scores do not certify
    the bacterial mechanisms.
  target_ids:
  - CommunityMech:000483
  evidence_ids:
  - record
  - native-target
  metrics:
  - name: completeness
    value: 65
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including all taxon roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). 50 + 5 + 0 + 10 + 0 + 0 + 0 + 0 = 65.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1=0, P2=1, P3=0, P4=0; 5 items / 3 nodes
      = 1.6666667; native COMPLETE. 100 - 10 + 16.6666667 + 15 = 121.6666667 before
      capping; observed counts cover assessed material only.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count within this partial record review.
  - name: P2
    value: 1
    unit: findings
    definition: Observed native severity count within this partial record review.
  - name: P3
    value: 0
    unit: findings
    definition: Observed native severity count within this partial record review.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count within this partial record review.
findings:
- finding_id: interaction-scope-and-causality
  issue_key: cm-000483-interaction-scope-and-causality
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: collective pathogen/host outcomes are promoted
    to unsupported reciprocal bacterial benefit, syntrophic roles and directed mediation,
    changing the biological meaning of the graph.'
  rule_id: review-checklist.interactions-and-causal-claims
  status: open
  certainty: confirmed
  title: Pathogen and plant outcomes are encoded as reciprocal bacterial mechanisms
  description: All three nodes use PAIRWISE MUTUALISM between the bacterial genera,
    both taxa carry SYNTROPHIC_PARTNER, and both arrows inherit that misframing; the
    suppression-to-immunity direction additionally exceeds the attached abstract.
    The evidence reports antagonist selection, T7 efficacy and plant pathways, without
    establishing member benefit, product-consuming cooperation, colonization or the
    suppression-to-immunity direction.
  target_ids:
  - CommunityMech:000483
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  - ecological_interactions[0]
  - ecological_interactions[1]
  - ecological_interactions[2]
  - ecological_interactions[0].downstream[0]
  - ecological_interactions[1].downstream[0]
  evidence_ids:
  - antagonism
  - design
  - efficacy
  - host-response
  - direction
  - schema
  - ontology
  - participant-candidates
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
    role: canonical_record
actions:
- action_id: repair-interaction-scope
  description: Retain reported T7 phenotypes while correcting participant scope and
    removing unsupported bacterial mechanisms.
  finding_ids:
  - interaction-scope-and-causality
  target_ids:
  - CommunityMech:000483
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
    role: canonical_record
  acceptance_checks:
  - Remove or qualify MUTUALISM and SYNTROPHIC_PARTNER unless inspected member-level
    evidence establishes their actual schema meanings; obligacy is not required.
  - Represent pathogen antagonism and chili responses at appropriate community/target
    scope instead of Bacillus-Pseudomonas reciprocal benefit.
  - Fusarium solani NCBITaxon:169388 is a verified species-label candidate; Capsicum
    annuum NCBITaxon:4072 matches the record name but needs full-source host-species
    confirmation. These targets need not join microbial taxonomy.
  - Keep T7 exact strain roster/proportions unresolved until primary formulation tables/Methods
    are inspected; do not infer two strains from two genus entries.
  - After scope correction, a bounded source-implied T7-application-to-efficacy link
    may remain; do not infer a selective bacterial mechanism from it.
  - Remove or explicitly source-qualify suppression-to-immune direction and unsupported
    colonization; simultaneous outcomes alone do not entail that arrow.
  - Retain immune-pathway statements as source-reported until their assay modality
    and selective causality are verified.
  - Add a concrete discussion documenting unavailable source context; rerun schema,
    strict, references and network gates after separately authorized curation, with
    a new history event.
- action_id: complete-source-assessment
  description: When the publicly licensed main article and supplement are accessible,
    inspect T7 composition, cultivation, controls, immune measurements and data availability
    before a new scientific review.
  finding_ids:
  - interaction-scope-and-causality
  target_ids:
  - CommunityMech:000483
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Chili_Root_Rot_Antagonistic_SynCom_T7.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve genus-pool versus T7 roster uncertainty until exact source tables/Methods
    are read.
  - Verify causal intervention/measurement scope rather than infer it from the abstract
    pathway names.
  - Record actual source strain/data identifiers only when resolved; no invented media,
    metabolites or missing-dataset claim.
  - No purchase, author contact, canonical edit or status promotion is authorized
    by this review.
limitations:
- The abstract explicitly states CC BY 4.0, while EPMC marks subscription access and
  no PMC record. Public APS HTML/PDF retrieval failed 403; the report records unsuccessful
  access rather than declaring a paywall.
- The exact T7 strain roster, proportions, preparation, dose, controls, timing and
  experimental vessels are unavailable. Two genus entries do not establish a two-strain
  community or prove both genera occur in every candidate SynCom.
- The abstract reports plant pathway activation and induced resistance; its assay
  modality, causal perturbations and spatial/systemic design were not independently
  assessed. Missing accessible evidence is not proof that experiments were absent.
- Biomarker abundance shifts, antagonist activity, community efficacy and plant signaling
  are distinct scopes. No partner-fitness, syntrophic transfer, rhizosphere colonization
  or selective suppression-to-immunity pathway was verified.
- Current snippets match abstract evidence, but exact lexical support does not entail
  the encoded mutualism or directed mediation. Prior history is retained unchanged
  and its scientific interpretation reassessed.
- No dataset or cultivation omission is inferred from inaccessible main/supplementary
  text. No raw community, sequence, metabolite or plant-pathway data were analyzed.
- Historical GTDB genus mapping fractions/counts/releases were not recomputed; optional
  adapter discovery was explicitly reused in the same batch05 runtime without executing
  an external checkout.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 23 words for this publication, all from the fresh abstract.
- All 24 repository inputs were pinned before assessment and rechecked; quality 100
  is capped from 121.6666667 and is not scientific certification.
tags:
- record-review
- partial
- synthetic-community
- biocontrol
- batch-05
```
