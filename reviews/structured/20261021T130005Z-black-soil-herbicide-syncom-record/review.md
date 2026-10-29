# Black-soil herbicide SynCom record review

- Review: 20261021T130005Z-black-soil-herbicide-syncom-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T12:56:25.885854Z
- Finished UTC: 2026-10-21T13:00:05.041357Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Three major findings concern NMC-to-SynCom result attribution, unresolved four-isolate/genus-complex grounding, and mechanistic/causal overreach. The qualitative SynCom advantage and engineered synthetic origin are supported. Full main and supplements remain unavailable, so this is not a completed scientific certification.

## Scope And Provenance

Entire record and all three nodes/two arrows against direct abstract, current schema/ontology, history and bounded access/resource evidence.

Selection: Only released CommunityMech:000482 after 000303 save and both mandatory gates.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000482 | kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml | maintained | Black-Soil Glucose-Activated Herbicide-Mixture Degrading Synthetic Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000482 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000482 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000482 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000482 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000482 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000482 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000482 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000482 | Reference validation passed against pinned caches. |
| audit-network | failed | True | CommunityMech:000482 | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; the target-native graph is COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000482 | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; the target-native graph is COMPLETE. |
| Primary bibliographic identity | passed | True | CommunityMech:000482 | Exact DOI/PMID/title and direct abstract identity agree. |
| Full primary source and critical supplemental verification | unavailable | True | CommunityMech:000482 | Direct abstract is available, but critical full Methods/Results, figures and supplements remain unavailable in inspected public routes. |
| Medium, strain and data resource correspondence | not_applicable | False | CommunityMech:000482 | No encoded CultureMech/archive/strain accession and no exact recipe established; no omission finding inferred. |
| Optional structured source adapter | unavailable | False | CommunityMech:000482 | No applicable runnable adapter established in stable batch 07 runtime discovery; no strain/locus identity to substitute. |

## Scientific And Domain Assessments

### Natural consortium and constructed SynCom

identity: concern. Targets: CommunityMech:000482.

The four-isolate SynCom is a real source entity, but its record conflates natural-consortium outcomes and unresolved member identities.

### Four isolates, genus complex, abundance and roles

grounding: concern. Targets: CommunityMech:000482.

The current three-genus roster and keystone-derived DOMINANT labels are not fully established for the constructed community.

Do not assert that Burkholderia is absent; it may occur among the four isolates. Verify the actual roster before using one genus as the whole complex. Keystone importance is not ordinal abundance evidence, and no percentage cutoff is required. atzF/gst associations do not establish every gene or primary-degrader role in each cultured isolate; syntrophic roles require a separate metabolic basis.

### ecological_interactions[0]

graph: concern. Targets: CommunityMech:000482.

Retain the reported glucose-associated interpretation with NMC and evidence qualifiers; SYNTROPHY is not demonstrated by the cited abstract.

Glucose metabolism is a suitable broad process label, but metagenomic potential and authors' activation interpretation do not establish direct flux, acidification necessity or partner-product removal in each SynCom strain.

### ecological_interactions[0].downstream[0]

graph: concern. Targets: CommunityMech:000482.

The asserted central-carbon activation → keystone gene enrichment direction is not established by the inspected text.

Glucose is a shared experimental input linked to community shifts and metabolic potential. The abstract does not show that the first endpoint causes the second; qualify or remove this arrow unless the full source supplies directional support. A directly implied edge need not require a mediation experiment, but it must express the source's actual causal claim.

### ecological_interactions[1]

graph: concern. Targets: CommunityMech:000482.

Retain candidate keystone-associated functional-gene enrichment as association/potential, not syntrophy or universal strain functions.

RF/co-occurrence plus metagenomic screening can identify candidate taxa/functions. They do not alone establish partner-metabolite transfer or the exact four-isolate gene inventory. Do not replace the valid broad glucose GO term with an unverified enzyme/process identifier.

### ecological_interactions[1].downstream[0]

graph: concern. Targets: CommunityMech:000482.

Selection of isolates using functional associations is a construction workflow, not itself a demonstrated biological causal mediator.

The source supports testing a constructed SynCom and its improved degradation. It does not establish that atzF/gst enrichment or the three named taxonomic signals mechanistically cause the performance difference. Preserve the assay endpoint without promoting selection rationale to causal physiology.

### ecological_interactions[2]

graph: concern. Targets: CommunityMech:000482.

Improved mixture degradation is supported; mineralization, formal synergism and syntrophy are stronger than the accessible result.

The abstract compares the SynCom with isolates and NMC but provides no complete carbon-balance/mineralization endpoint, factorial synergy basis or producer-benefiting product-removal mechanism. Use the reported degradation endpoint and preserve the unresolved exact strain/protocol scope.

### Environment, conditions and quantitative attribution

scope: concern. Targets: CommunityMech:000482.

Move the NMC percentages and eight-day duration to their exact experiment and distinguish soil origin from liquid cultivation.

Glucose was required for significant degradation in the tested MSM/GSM NMC comparison; this does not establish an unrestricted requirement across all substrates or conditions. Preserve a qualitative GSM context without inventing a recipe, temperature, pH or precise SynCom endpoint.

### Access, reusable resources and datasets

provenance: unknown. Targets: CommunityMech:000482.

No exact strain/medium/archive resource can be certified from the accessible abstract alone.

No independent dataset omission or complete-source absence is inferred. A future curator should verify the exact source roster, medium, assay endpoints and any data statement after legitimate main/SI access.

### Historical review and snippet support

provenance: supported. Targets: CommunityMech:000482.

All nine snippets are exact; historical abstract-based node/arrow acceptance is not inherited as whole-source certification.

The earlier retained causal chain is reassessed against actual semantic support. No history, cache or public issue state is changed.

### Native checks and ontology labels

schema: supported. Targets: CommunityMech:000482.

Eight native checks and all seven current ID/label pairs pass; source-scope conclusions remain separate.

### Native mechanical scores

completeness: supported. Targets: CommunityMech:000482.

Mechanical scores do not certify the three unresolved source-scope findings.

## Findings

### experiment-attribution: Separate NMC results from SynCom performance

major / open / confirmed; issue key: cm-000482-experiment-attribution.

The description assigns the NMC eight-day percentages to the four-isolate SynCom, while environment/context prose implies broader glucose necessity and soil-versus-broth scope than the available comparison.

### four-isolate-grounding: Resolve the four-isolate roster without collapsing a genus complex

major / open / confirmed; issue key: cm-000482-four-isolate-grounding.

The record uses three keystone signals as if they resolve the four cultured members, and narrows the Burkholderia-Caballeronia-Paraburkholderia complex to Burkholderia while treating keystone status as dominance.

### mechanism-and-edges: Bound metabolic mechanisms and both causal arrows

major / open / confirmed; issue key: cm-000482-mechanism-and-edges.

Syntrophic roles/types, mineralization, unqualified metabolic certainty and the two causal links exceed what the inspected abstract demonstrates.

## Recommended Actions And Acceptance Checks

### repair-experiment-attribution

Separate NMC results from SynCom performance.

- Attribute 97.27% nicosulfuron, 68.00% mesotrione and 22.91% atrazine after 8 days to the NMC GSM experiment. Give only the accessible qualitative SynCom comparison until its exact results and duration are verified.
- Limit glucose dependence to the tested comparison; distinguish soil isolation/bioremediation context from liquid MSM/GSM cultivation. Use a verified physical-environment term and modeled/source habitat notes rather than treating contaminated soil as the tested broth.
- Before adding numeric culture conditions, inspect the exact primary Methods/SI and attach claim-level evidence. Do not import protocol from a similar black-soil study.

### repair-four-isolate-grounding

Resolve the four-isolate roster without collapsing a genus complex.

- Recover exact four-isolate identities and source labels from Methods/SI before changing the roster or participant assignments. Preserve uncertainty if access remains blocked; do not invent a fourth strain or assume all three complex genera are present.
- Distinguish the multigenus amplicon signal from a verified Burkholderia isolate. Retain valid NCBI/GTDB labels only for the biological entity actually supported.
- Justify each abundance category from community-specific ordinal evidence, or remove/qualify it. Keystone network importance alone is insufficient; no arbitrary percentage threshold is imposed. Verify strain-specific functional claims rather than assuming every taxon carries both genes.

### repair-mechanism-and-edges

Bound metabolic mechanisms and both causal arrows.

- Retain source-reported improved degradation and the authors' glucose/metagenomic interpretation with appropriate NMC/SynCom qualifiers. Do not call degradation mineralization or formal synergism without a corresponding assay.
- Remove or explicitly support SYNTROPHY and SYNTROPHIC_PARTNER using actual partner-product utilization/removal that favors producer metabolism; do not impose an obligacy requirement or substitute another interaction type without evidence.
- Review each arrow independently: glucose-associated changes do not by themselves establish metabolic activation→gene enrichment, and functional selection→SynCom construction is a workflow rather than a biological causal edge. Retain only source-supported directions with the appropriate evidence qualifier.
- Verify expression/flux, acidification necessity, gene-to-isolate mapping and mineralization claims against full Methods/Results/SI before certifying them. Do not fabricate protein accessions or restore unsupported mechanistic specificity to preserve node count.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml; Entire record: three genus entries, three nodes and two arrows | supports | The record denotes a four-isolate SynCom but attaches natural-consortium statistics and mechanistic claims to its current genus-level roster. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=41762466&amp;retmode=xml; Article-level metadata/abstract where supplied | supports | Article-level PMID 41762466, DOI/title and complete abstract identify the focal study. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41762466%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article-level metadata/abstract where supplied | supports | The same abstract and DOI agree; access metadata supplies no PMCID and a subscription DOI route. |
| crossref | https://api.crossref.org/works/10.1016/j.jhazmat.2026.141615; Article-level metadata/abstract where supplied | supports | DOI/title bibliographic identity agrees; metadata does not certify full Methods or the inferred mechanism. |
| nmc-results | PMID:41762466; Abstract: NMC inoculation into MSM/GSM and following eight-day result sentences | supports | The percentages 97.27/68.00/22.91 refer to the natural-consortium GSM experiment; the four-isolate experiment is introduced later. |
| syncom | PMID:41762466; Abstract: final SynCom result sentence | supports | The constructed four-isolate community performs better than individual isolates and the NMC in GSM; exact members and treatment-specific yields are not given. |
| keystones | PMID:41762466; Abstract: RF/co-occurrence and metagenomic screening sentences | supports | The source identifies a Burkholderia-Caballeronia-Paraburkholderia complex plus Rhodanobacter and Achromobacter as keystone signals; this does not resolve four cultured isolates or establish ordinal dominance. |
| carbon | PMID:41762466; Abstract: integrated 16S/metagenomic interpretation | supports | The authors link glucose to community shifts and central-carbon activation. Preserve this as a source interpretation at the assay/evidence level, not direct measured flux in every named SynCom member. |
| schema | src/communitymech/schema/communitymech.yaml; InteractionTypeEnum.SYNTROPHY; FunctionalRoleEnum.SYNTROPHIC_PARTNER; AbundanceEnum; MicrobialCommunity.environment_term/modeled_environment | supports | Syntrophy requires partner-product utilization/removal making producer metabolism favorable; it does not require obligacy. DOMINANT is ordinal prominence, not a percentage threshold. Physical environment and modeled/source habitat are distinct. |
| ontology | ontology-authority.json; Whole bounded receipt | supports | All seven distinct ontology pairs across 22 occurrences have correct labels; Burkholderia is one genus rather than the entire three-genus complex. |
| complex-authority | complex-authority-scope.json; Whole bounded receipt | supports | Burkholderia, Caballeronia and Paraburkholderia are distinct verified genera under Burkholderiaceae; this is not evidence that all three occur in the four isolates. |
| resources | dataset-verification.json; Whole bounded receipt | supports | No exact strain or archive accession was established from the accessible source; no global absence or dataset-omission inference. |
| snippets | snippet-audit.json; Whole bounded receipt | supports | All nine quoted occurrences match direct PubMed abstract and pinned cache; lexical validity does not establish their broader interpretation. |
| history | provenance-audit.json; Whole bounded receipt | supports | Both histories and exact batch 133 row were read. The historical graph assessment used abstract/cache scope; no directly linked issue status was available to refresh. |
| native-target | support-audit.json; Whole bounded receipt | supports | Mechanical completeness/network/quality scores do not certify source causality or exact strain composition. |
| source-scope | source-audit.json; Whole bounded receipt | supports | Direct abstract/metadata and actual access receipts support a partial review; no full-main/SI certification. |
| independent-source | root-independent-source-audit.json; Whole bounded receipt | supports | Independent root assessment agrees on the bounded source findings and current-access limitation. |
| access-doi | https://doi.org/10.1016/j.jhazmat.2026.141615; Inspected response body and retrieval receipt | context_only | HTTP200 serves only a redirect shell. |
| access-article-api | https://api.elsevier.com/content/article/doi/10.1016/j.jhazmat.2026.141615?httpAccept=text/xml; Inspected response body and retrieval receipt | context_only | HTTP200 serves coredata only, without full article text. |
| access-publisher | https://www.sciencedirect.com/science/article/pii/S0304389426005935; Inspected response body and retrieval receipt | context_only | HTTP403 serves a visible access-error page, not the primary paper. |
| access-openalex | https://api.openalex.org/works/https://doi.org/10.1016/j.jhazmat.2026.141615; Inspected response body and retrieval receipt | context_only | Current metadata reports closed access and no open PDF location; this is not proof of global unavailability. |
| search-leads | Exact DOI/title public discovery; indexed-search-leads.json | context_only | Search-indexed primary excerpts and abstract mirrors are leads only; no main-text claims are certified from them. |
| local-search | Maintained local corpus; local-search.json | supports | Ignored-inclusive local discovery records the inspected source/history boundaries. |
| adapter | Optional structured source adapter; adapter-check.json | supports | Stable batch 07 runtime discovery reused explicitly; no applicable runnable adapter established or external-checkout execution. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml; Actual execution 2026-10-21T12:56:52.615679+00:00 to 2026-10-21T12:56:55.203468+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-strict kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml --out /private/tmp/cm-review-session/batch-07/000482/strict-report.tsv; Actual execution 2026-10-21T12:56:52.616250+00:00 to 2026-10-21T12:56:59.787672+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-terms kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml; Actual execution 2026-10-21T12:56:52.616487+00:00 to 2026-10-21T12:56:57.921396+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-gtdb kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml; Actual execution 2026-10-21T12:56:55.203984+00:00 to 2026-10-21T12:56:55.378020+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-gtdb-domain kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml; Actual execution 2026-10-21T12:56:55.378408+00:00 to 2026-10-21T12:56:59.900586+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-history history/records/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom; Actual execution 2026-10-21T12:56:57.922479+00:00 to 2026-10-21T12:57:00.158642+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T12:57:00.163702+00:00 to 2026-10-21T12:57:00.325366+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src just --no-dotenv validate-references-explained kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml; Actual execution 2026-10-21T12:57:00.331710+00:00 to 2026-10-21T12:57:01.701215+00:00 | supports | Reference validation passed against pinned caches. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T11:32:06.425768+00:00 to 2026-10-21T11:32:16.427975+00:00 | supports | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; the target-native graph is COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T11:32:06.426382+00:00 to 2026-10-21T11:32:14.966232+00:00 | supports | Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records; the target-native graph is COMPLETE. |

## Limits And Additional Notes

- Full primary Methods, Results, figures, supplements, exact four-isolate roster, culture recipe and raw data were not accessible in the inspected routes. This prevents whole-source scientific certification.
- The natural microbial consortium (NMC) and the constructed four-isolate SynCom are distinct experimental populations. The abstract reports the eight-day percentages in the NMC comparison; it separately reports better SynCom performance without giving those SynCom percentages.
- RF/co-occurrence keystone identification and metagenomic gene enrichment are association/potential evidence. They do not independently establish isotope-resolved flux, gene expression, enzyme activity, partner-product removal, mineralization or each isolate carrying every named gene.
- Publisher indexed excerpts remain search leads. OpenAlex/EPMC access flags and bounded failed routes do not prove that no public copy, supplement or dataset exists globally. No authentication bypass, paid provider, author contact or alternate-paper substitution.
- No strain aliases, exact GSM recipe, unreported accessions, raw sequence analysis or causal mechanisms were invented. The similarly themed 2025 eight-herbicide study is a different source.
- No canonical, cache, history, generated or saved-review files changed; all 24 inspected inputs remain pinned.
- All nine quotations match direct source/cache. Exact matching does not validate the inferred cause, strain identity or experimental population.
- Native completeness 70 and capped quality 100/raw 101.6666667 remain separate from partial source access and unresolved findings.
- ENGINEERED/SYNTHETIC is appropriate for the constructed SynCom; this review does not invent a different origin, missing strain or recipe.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T130005Z-black-soil-herbicide-syncom-record
kind: record
repository: CultureBotAI/CommunityMech
title: Black-soil herbicide SynCom record review
started_at: '2026-10-21T12:56:25.885854Z'
finished_at: '2026-10-21T13:00:05.041357Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed direct source scope, native/ontology
    checks and supporting provenance; no person-level independence asserted.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: Three major findings concern NMC-to-SynCom result attribution, unresolved
  four-isolate/genus-complex grounding, and mechanistic/causal overreach. The qualitative
  SynCom advantage and engineered synthetic origin are supported. Full main and supplements
  remain unavailable, so this is not a completed scientific certification.
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
  - path: history/records/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom/2026-10-19T053000Z-antigravity-cc0d.yaml
    sha256: 0fca4521b941a5eaa723e13e7d2f7664c2329a0eb61ea80213882111ba3229f7
    role: context
  - path: history/records/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom/2026-10-20T041800Z-antigravity-8da2f3.yaml
    sha256: b48309d668f8f35fba5a5f678b32bfb03c7aa4175ae22f8f24d4d558de8f2f09
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
    sha256: 8da2f35995f5bde8cb1a9af16a1fa460d66f8a27d6b30e8ccd08b9c42263dc9a
    role: target
  - path: references_cache/PMID_41762466.txt
    sha256: 3a5145b825f62744b99c373cf18c10a27ff0daf6c7ac7c2f608d439a665462fd
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
- target_id: CommunityMech:000482
  path: kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  label: Black-Soil Glucose-Activated Herbicide-Mixture Degrading Synthetic Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
    role: canonical_record
scope:
  description: Entire record and all three nodes/two arrows against direct abstract,
    current schema/ontology, history and bounded access/resource evidence.
  selection: Only released CommunityMech:000482 after 000303 save and both mandatory
    gates.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000482
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000482
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh target/history checks and corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000482
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-strict kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-07/000482/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh target/history checks and corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000482
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-terms kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh target/history checks and corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000482
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh target/history checks and corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000482
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb-domain kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh target/history checks and corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000482
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-history history/records/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh target/history checks and corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000482
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh target/history checks and corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against pinned caches.
  target_ids:
  - CommunityMech:000482
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-references-explained kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh target/history checks and corpus cache-filename preflight; structural
    success does not certify scientific scope.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records;
    the target-native graph is COMPLETE.
  target_ids:
  - CommunityMech:000482
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit reuse of fresh batch 07 corpus receipts, not a target-specific
    pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records;
    the target-native graph is COMPLETE.
  target_ids:
  - CommunityMech:000482
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit reuse of fresh batch 07 corpus receipts, not a target-specific
    pass.
- check_id: source-identity
  name: Primary bibliographic identity
  status: passed
  required: true
  summary: Exact DOI/PMID/title and direct abstract identity agree.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - pubmed
  - epmc
  - crossref
- check_id: scientific-source
  name: Full primary source and critical supplemental verification
  status: unavailable
  required: true
  summary: Direct abstract is available, but critical full Methods/Results, figures
    and supplements remain unavailable in inspected public routes.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - source-scope
  - independent-source
  - access-publisher
  - access-article-api
- check_id: cross-mech
  name: Medium, strain and data resource correspondence
  status: not_applicable
  required: false
  summary: No encoded CultureMech/archive/strain accession and no exact recipe established;
    no omission finding inferred.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - resources
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No applicable runnable adapter established in stable batch 07 runtime discovery;
    no strain/locus identity to substitute.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  locator: 'Entire record: three genus entries, three nodes and two arrows'
  summary: The record denotes a four-isolate SynCom but attaches natural-consortium
    statistics and mechanistic claims to its current genus-level roster.
  support: supports
  accessed_at: '2026-10-21T13:00:05.038819Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41762466&retmode=xml
  locator: Article-level metadata/abstract where supplied
  summary: Article-level PMID 41762466, DOI/title and complete abstract identify the
    focal study.
  support: supports
  accessed_at: '2026-10-21T12:56:58.314993Z'
  snapshot_sha256: 7894e9d55542a816208ef76486e4a101405a3009862fce2ad90f2aec352273f8
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:41762466%20AND%20SRC:MED&format=json&resultType=core
  locator: Article-level metadata/abstract where supplied
  summary: The same abstract and DOI agree; access metadata supplies no PMCID and
    a subscription DOI route.
  support: supports
  accessed_at: '2026-10-21T12:56:58.877219Z'
  snapshot_sha256: bd3553f847449f510cf867b16642f83e75e7bee67d3bcfd2c22f26f219ef39a3
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.jhazmat.2026.141615
  locator: Article-level metadata/abstract where supplied
  summary: DOI/title bibliographic identity agrees; metadata does not certify full
    Methods or the inferred mechanism.
  support: supports
  accessed_at: '2026-10-21T12:56:58.370814Z'
  snapshot_sha256: 534bf1d0f0483400f7a18057cf48c858da4fd12ff3e79673a61ebaae94b8385f
- evidence_id: nmc-results
  kind: primary_source
  reference: PMID:41762466
  locator: 'Abstract: NMC inoculation into MSM/GSM and following eight-day result
    sentences'
  summary: The percentages 97.27/68.00/22.91 refer to the natural-consortium GSM experiment;
    the four-isolate experiment is introduced later.
  support: supports
  accessed_at: '2026-10-21T13:00:05.038933Z'
  snapshot_sha256: 7894e9d55542a816208ef76486e4a101405a3009862fce2ad90f2aec352273f8
  quote: An NMC enriched
- evidence_id: syncom
  kind: primary_source
  reference: PMID:41762466
  locator: 'Abstract: final SynCom result sentence'
  summary: The constructed four-isolate community performs better than individual
    isolates and the NMC in GSM; exact members and treatment-specific yields are not
    given.
  support: supports
  accessed_at: '2026-10-21T13:00:05.038956Z'
  snapshot_sha256: 7894e9d55542a816208ef76486e4a101405a3009862fce2ad90f2aec352273f8
  quote: four-isolate SynCom
- evidence_id: keystones
  kind: primary_source
  reference: PMID:41762466
  locator: 'Abstract: RF/co-occurrence and metagenomic screening sentences'
  summary: The source identifies a Burkholderia-Caballeronia-Paraburkholderia complex
    plus Rhodanobacter and Achromobacter as keystone signals; this does not resolve
    four cultured isolates or establish ordinal dominance.
  support: supports
  accessed_at: '2026-10-21T13:00:05.038978Z'
  snapshot_sha256: 7894e9d55542a816208ef76486e4a101405a3009862fce2ad90f2aec352273f8
  quote: functional genes associated with herbicide degradation
- evidence_id: carbon
  kind: primary_source
  reference: PMID:41762466
  locator: 'Abstract: integrated 16S/metagenomic interpretation'
  summary: The authors link glucose to community shifts and central-carbon activation.
    Preserve this as a source interpretation at the assay/evidence level, not direct
    measured flux in every named SynCom member.
  support: supports
  accessed_at: '2026-10-21T13:00:05.038999Z'
  snapshot_sha256: 7894e9d55542a816208ef76486e4a101405a3009862fce2ad90f2aec352273f8
  quote: activation of central carbon metabolism
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: InteractionTypeEnum.SYNTROPHY; FunctionalRoleEnum.SYNTROPHIC_PARTNER; AbundanceEnum;
    MicrobialCommunity.environment_term/modeled_environment
  summary: Syntrophy requires partner-product utilization/removal making producer
    metabolism favorable; it does not require obligacy. DOMINANT is ordinal prominence,
    not a percentage threshold. Physical environment and modeled/source habitat are
    distinct.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039055Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded receipt
  summary: All seven distinct ontology pairs across 22 occurrences have correct labels;
    Burkholderia is one genus rather than the entire three-genus complex.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039083Z'
  snapshot_sha256: d280b48ee51f775759e944fe2aae4807ecb9dc54303d15c3bb968095845b1ab9
- evidence_id: complex-authority
  kind: authority
  reference: complex-authority-scope.json
  locator: Whole bounded receipt
  summary: Burkholderia, Caballeronia and Paraburkholderia are distinct verified genera
    under Burkholderiaceae; this is not evidence that all three occur in the four
    isolates.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039253Z'
  snapshot_sha256: b02e9d7b7f3f33cac949d28748518468a97c33307893abfa526a8112ad94a783
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded receipt
  summary: No exact strain or archive accession was established from the accessible
    source; no global absence or dataset-omission inference.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039279Z'
  snapshot_sha256: 8278f6042fdc0d3ca23a0dba04a7fe6cb9b5403b7ec52eead6e85a3aa68df66b
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded receipt
  summary: All nine quoted occurrences match direct PubMed abstract and pinned cache;
    lexical validity does not establish their broader interpretation.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039305Z'
  snapshot_sha256: 108d9cbf1ce60f565816f4d5c2075b9ce9bada72a00db1d7dca77116b436afda
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded receipt
  summary: Both histories and exact batch 133 row were read. The historical graph
    assessment used abstract/cache scope; no directly linked issue status was available
    to refresh.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039332Z'
  snapshot_sha256: 08afd829af49f72f91e5392f66aa8d9acf62ccdb9448bfe8e1b037b53e15f1d2
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded receipt
  summary: Mechanical completeness/network/quality scores do not certify source causality
    or exact strain composition.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039351Z'
  snapshot_sha256: a1a84c01686d0774e019d2932ff6305f8aeb4d63e96f1059272122b6aaf717c1
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded receipt
  summary: Direct abstract/metadata and actual access receipts support a partial review;
    no full-main/SI certification.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039369Z'
  snapshot_sha256: 625866564fbb77e836b37cb62c329d87300cd1ce80becafaae402d97f793300c
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded receipt
  summary: Independent root assessment agrees on the bounded source findings and current-access
    limitation.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039387Z'
  snapshot_sha256: c8b63ea128d1b0440fe701097e6704ca825b43a60a7f72569ee8b9472d3203df
- evidence_id: access-doi
  kind: database
  reference: https://doi.org/10.1016/j.jhazmat.2026.141615
  locator: Inspected response body and retrieval receipt
  summary: HTTP200 serves only a redirect shell.
  support: context_only
  accessed_at: '2026-10-21T12:56:58.819734Z'
  snapshot_sha256: f3d816703ddd948e679145fd96075f3079b0147d2bbce3341837b0c2b714faea
- evidence_id: access-article-api
  kind: database
  reference: https://api.elsevier.com/content/article/doi/10.1016/j.jhazmat.2026.141615?httpAccept=text/xml
  locator: Inspected response body and retrieval receipt
  summary: HTTP200 serves coredata only, without full article text.
  support: context_only
  accessed_at: '2026-10-21T12:56:58.812381Z'
  snapshot_sha256: 8691eec515b23bcfcbb7d53976461af50d44f8b20effad01d2d325c4cc65f941
- evidence_id: access-publisher
  kind: database
  reference: https://www.sciencedirect.com/science/article/pii/S0304389426005935
  locator: Inspected response body and retrieval receipt
  summary: HTTP403 serves a visible access-error page, not the primary paper.
  support: context_only
  accessed_at: '2026-10-21T12:56:58.970644Z'
  snapshot_sha256: 2f198bc8040e29eeadee2c1603ec311fa9922dba4af31eb36f0be422a927a3ef
- evidence_id: access-openalex
  kind: database
  reference: https://api.openalex.org/works/https://doi.org/10.1016/j.jhazmat.2026.141615
  locator: Inspected response body and retrieval receipt
  summary: Current metadata reports closed access and no open PDF location; this is
    not proof of global unavailability.
  support: context_only
  accessed_at: '2026-10-21T12:57:37.995729Z'
  snapshot_sha256: 273f42bba8c80c1f9c76d7108da46ea39b74bba3baa6d4eec87927aa8095573e
- evidence_id: search-leads
  kind: search
  reference: Exact DOI/title public discovery
  locator: indexed-search-leads.json
  summary: Search-indexed primary excerpts and abstract mirrors are leads only; no
    main-text claims are certified from them.
  support: context_only
  accessed_at: '2026-10-21T13:00:05.039498Z'
  snapshot_sha256: 7a6e4f429e87a558fe4e15e392f7e333b55372052cbc19ba809544ec80d81209
  search_scope: Exact DOI/title plus public repository/Almeria terms; bounded search,
    no global absence claim.
- evidence_id: local-search
  kind: search
  reference: Maintained local corpus
  locator: local-search.json
  summary: Ignored-inclusive local discovery records the inspected source/history
    boundaries.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039518Z'
  snapshot_sha256: c4cff31181d6ee1a329ff62ad312e64422a2ddd3846425ac83ecdcbda8d1bc26
  search_scope: Maintained record/taxon/mapping roots including ignored files, as
    recorded.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: adapter-check.json
  summary: Stable batch 07 runtime discovery reused explicitly; no applicable runnable
    adapter established or external-checkout execution.
  support: supports
  accessed_at: '2026-10-21T13:00:05.039688Z'
  snapshot_sha256: 890acdaa4cb3c073a027c078300a6e46cbf076dd663dd5a98f35b78f2ab419da
  search_scope: Pinned batch 07 runtime discovery; no paid provider or expression-module
    inference.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  locator: Actual execution 2026-10-21T12:56:52.615679+00:00 to 2026-10-21T12:56:55.203468+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T12:56:55.203468Z'
  snapshot_sha256: 598191c08792f0d7157be5211d6559e88ba351672016c2af7ae9e848cca625a6
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-strict kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-07/000482/strict-report.tsv
  locator: Actual execution 2026-10-21T12:56:52.616250+00:00 to 2026-10-21T12:56:59.787672+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T12:56:59.787672Z'
  snapshot_sha256: 5ca460e3a6d51730235f7ff6ce2fed47a1fea3b73ad4886cf66924d310d6124d
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-terms kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  locator: Actual execution 2026-10-21T12:56:52.616487+00:00 to 2026-10-21T12:56:57.921396+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T12:56:57.921396Z'
  snapshot_sha256: 066c92faa2466fed034f2d896415f4867563d352582f0623223e25e143284a4c
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  locator: Actual execution 2026-10-21T12:56:55.203984+00:00 to 2026-10-21T12:56:55.378020+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T12:56:55.378020Z'
  snapshot_sha256: c03e19a9ac7b02cc2328514c9366032473e9803b3774023432fa8c5cf584032e
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-gtdb-domain kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  locator: Actual execution 2026-10-21T12:56:55.378408+00:00 to 2026-10-21T12:56:59.900586+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T12:56:59.900586Z'
  snapshot_sha256: 653a3fe346d45973449a56c3b8c6f83c97f7c01110a38918f3e40b6d628687b5
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-history history/records/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom
  locator: Actual execution 2026-10-21T12:56:57.922479+00:00 to 2026-10-21T12:57:00.158642+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T12:57:00.158642Z'
  snapshot_sha256: 4aac1b852c2ae517ef8e4a5e69d9ebbf906338e58889f5527fc4bbc9241153df
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T12:57:00.163702+00:00 to 2026-10-21T12:57:00.325366+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T12:57:00.325366Z'
  snapshot_sha256: c844524a482a135d1255f0148716d3ce2e69212f2c1ea57bec1d360765575e8a
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src
    just --no-dotenv validate-references-explained kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
  locator: Actual execution 2026-10-21T12:57:00.331710+00:00 to 2026-10-21T12:57:01.701215+00:00
  summary: Reference validation passed against pinned caches.
  support: supports
  accessed_at: '2026-10-21T12:57:01.701215Z'
  snapshot_sha256: b1c6618a1d814b828de9ae6331f6ea6214f4b214c52a6d0d162b5e13a19f4785
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T11:32:06.425768+00:00 to 2026-10-21T11:32:16.427975+00:00
  summary: Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records;
    the target-native graph is COMPLETE.
  support: supports
  accessed_at: '2026-10-21T11:32:16.427975Z'
  snapshot_sha256: c16b3a28b790e90191e9c5fb067c97a8038a813593fbfbe1796bf78d116abafb
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-07/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T11:32:06.426382+00:00 to 2026-10-21T11:32:14.966232+00:00
  summary: Fresh batch 07 corpus execution returned 57 warnings across 21 of 477 records;
    the target-native graph is COMPLETE.
  support: supports
  accessed_at: '2026-10-21T11:32:14.966232Z'
  snapshot_sha256: 6a321df993e978ed76cacc843bf792ecb9969ab237ca14c6e8575723ee3410f3
assessments:
- assessment_id: identity
  area: identity
  topic: Natural consortium and constructed SynCom
  outcome: concern
  summary: The four-isolate SynCom is a real source entity, but its record conflates
    natural-consortium outcomes and unresolved member identities.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - nmc-results
  - syncom
  - keystones
  dimensions:
  - name: community_scope
    value: Four-isolate synthetic community derived from an enriched NMC
    definition: Separate natural-consortium screening, network inference and subsequent
      constructed-community validation.
    evidence_ids:
    - nmc-results
    - syncom
  - name: source_strain
    value: Exact four-isolate roster unresolved at accessible scope
    definition: Three keystone taxonomic signals are not a complete cultured-strain
      inventory.
    evidence_ids:
    - keystones
    - syncom
  - name: environment
    value: Liquid mineral-salt experiments derived from contaminated black soil
    definition: Soil is origin/bioremediation context; do not present a broth assay
      as an in-soil SynCom trial.
    evidence_ids:
    - nmc-results
    - schema
  - name: medium
    value: MSM versus glucose-supplemented GSM
    definition: Only qualitative medium comparison is accessible; exact concentrations,
      inocula and incubation parameters require Methods.
    evidence_ids:
    - nmc-results
  - name: experimental_setting
    value: NMC comparison followed by designed SynCom evaluation
    definition: The eight-day NMC result cannot be automatically assigned to the subsequent
      SynCom.
    evidence_ids:
    - nmc-results
    - syncom
  - name: evidence_tier
    value: Direct abstract with experiment and metagenomic association summaries
    definition: No independently inspected full Methods, figures or supplements.
    evidence_ids:
    - source-scope
    - carbon
  - name: grounding_status
    value: Valid current labels, unresolved biological scope
    definition: Burkholderia 32008 is valid but does not stand for the whole reported
      complex.
    evidence_ids:
    - ontology
    - keystones
- assessment_id: taxonomy
  area: grounding
  topic: Four isolates, genus complex, abundance and roles
  outcome: concern
  summary: The current three-genus roster and keystone-derived DOMINANT labels are
    not fully established for the constructed community.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - keystones
  - syncom
  - ontology
  - complex-authority
  - schema
  details: Do not assert that Burkholderia is absent; it may occur among the four
    isolates. Verify the actual roster before using one genus as the whole complex.
    Keystone importance is not ordinal abundance evidence, and no percentage cutoff
    is required. atzF/gst associations do not establish every gene or primary-degrader
    role in each cultured isolate; syntrophic roles require a separate metabolic basis.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: concern
  summary: Retain the reported glucose-associated interpretation with NMC and evidence
    qualifiers; SYNTROPHY is not demonstrated by the cited abstract.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - carbon
  - nmc-results
  - schema
  details: Glucose metabolism is a suitable broad process label, but metagenomic potential
    and authors' activation interpretation do not establish direct flux, acidification
    necessity or partner-product removal in each SynCom strain.
- assessment_id: arrow-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: concern
  summary: The asserted central-carbon activation → keystone gene enrichment direction
    is not established by the inspected text.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - carbon
  - keystones
  details: Glucose is a shared experimental input linked to community shifts and metabolic
    potential. The abstract does not show that the first endpoint causes the second;
    qualify or remove this arrow unless the full source supplies directional support.
    A directly implied edge need not require a mediation experiment, but it must express
    the source's actual causal claim.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: concern
  summary: Retain candidate keystone-associated functional-gene enrichment as association/potential,
    not syntrophy or universal strain functions.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - keystones
  - schema
  details: RF/co-occurrence plus metagenomic screening can identify candidate taxa/functions.
    They do not alone establish partner-metabolite transfer or the exact four-isolate
    gene inventory. Do not replace the valid broad glucose GO term with an unverified
    enzyme/process identifier.
- assessment_id: arrow-1
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: concern
  summary: Selection of isolates using functional associations is a construction workflow,
    not itself a demonstrated biological causal mediator.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - keystones
  - syncom
  details: The source supports testing a constructed SynCom and its improved degradation.
    It does not establish that atzF/gst enrichment or the three named taxonomic signals
    mechanistically cause the performance difference. Preserve the assay endpoint
    without promoting selection rationale to causal physiology.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: concern
  summary: Improved mixture degradation is supported; mineralization, formal synergism
    and syntrophy are stronger than the accessible result.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - syncom
  - schema
  details: The abstract compares the SynCom with isolates and NMC but provides no
    complete carbon-balance/mineralization endpoint, factorial synergy basis or producer-benefiting
    product-removal mechanism. Use the reported degradation endpoint and preserve
    the unresolved exact strain/protocol scope.
- assessment_id: context
  area: scope
  topic: Environment, conditions and quantitative attribution
  outcome: concern
  summary: Move the NMC percentages and eight-day duration to their exact experiment
    and distinguish soil origin from liquid cultivation.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - nmc-results
  - syncom
  - schema
  details: Glucose was required for significant degradation in the tested MSM/GSM
    NMC comparison; this does not establish an unrestricted requirement across all
    substrates or conditions. Preserve a qualitative GSM context without inventing
    a recipe, temperature, pH or precise SynCom endpoint.
- assessment_id: resources
  area: provenance
  topic: Access, reusable resources and datasets
  outcome: unknown
  summary: No exact strain/medium/archive resource can be certified from the accessible
    abstract alone.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - resources
  - source-scope
  details: No independent dataset omission or complete-source absence is inferred.
    A future curator should verify the exact source roster, medium, assay endpoints
    and any data statement after legitimate main/SI access.
- assessment_id: history
  area: provenance
  topic: Historical review and snippet support
  outcome: supported
  summary: All nine snippets are exact; historical abstract-based node/arrow acceptance
    is not inherited as whole-source certification.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - history
  - snippets
  details: The earlier retained causal chain is reassessed against actual semantic
    support. No history, cache or public issue state is changed.
- assessment_id: validation
  area: schema
  topic: Native checks and ontology labels
  outcome: supported
  summary: Eight native checks and all seven current ID/label pairs pass; source-scope
    conclusions remain separate.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - schema
- assessment_id: metrics
  area: completeness
  topic: Native mechanical scores
  outcome: supported
  summary: Mechanical scores do not certify the three unresolved source-scope findings.
  target_ids:
  - CommunityMech:000482
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 70
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-fields/taxon-role component +5 environment +10 interaction
      nodes +5 node metabolites. No media, data, external-resource or three-factor
      bonus.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      P1=0/P2=3/P3=0/P4=0; evidence 5/3 gives 16.6667 bonus; network 15; raw 101.6666667,
      capped 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 3
    unit: findings
    definition: Native severity count.
  - name: P3
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count.
findings:
- finding_id: experiment-attribution
  issue_key: cm-000482-experiment-attribution
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: 'P2: material population, grounding or mechanistic scope inflation;
    not a lexical snippet error.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Separate NMC results from SynCom performance
  description: The description assigns the NMC eight-day percentages to the four-isolate
    SynCom, while environment/context prose implies broader glucose necessity and
    soil-versus-broth scope than the available comparison.
  target_ids:
  - CommunityMech:000482
  field_paths:
  - description
  - environment_term
  - environmental_factors[0]
  evidence_ids:
  - nmc-results
  - syncom
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
    role: canonical_record
- finding_id: four-isolate-grounding
  issue_key: cm-000482-four-isolate-grounding
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: 'P2: material population, grounding or mechanistic scope inflation;
    not a lexical snippet error.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Resolve the four-isolate roster without collapsing a genus complex
  description: The record uses three keystone signals as if they resolve the four
    cultured members, and narrows the Burkholderia-Caballeronia-Paraburkholderia complex
    to Burkholderia while treating keystone status as dominance.
  target_ids:
  - CommunityMech:000482
  field_paths:
  - taxonomy
  - ecological_interactions[0].participating_taxa
  - ecological_interactions[1].participating_taxa
  - ecological_interactions[2].participating_taxa
  evidence_ids:
  - keystones
  - syncom
  - ontology
  - complex-authority
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
    role: canonical_record
- finding_id: mechanism-and-edges
  issue_key: cm-000482-mechanism-and-edges
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: material population, grounding or mechanistic scope inflation;
    not a lexical snippet error.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Bound metabolic mechanisms and both causal arrows
  description: Syntrophic roles/types, mineralization, unqualified metabolic certainty
    and the two causal links exceed what the inspected abstract demonstrates.
  target_ids:
  - CommunityMech:000482
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  - taxonomy[2].functional_role
  - description
  - environmental_factors[0].description
  - ecological_interactions[0]
  - ecological_interactions[1]
  - ecological_interactions[2]
  evidence_ids:
  - carbon
  - keystones
  - syncom
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
    role: canonical_record
actions:
- action_id: repair-experiment-attribution
  description: Separate NMC results from SynCom performance.
  finding_ids:
  - experiment-attribution
  target_ids:
  - CommunityMech:000482
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Attribute 97.27% nicosulfuron, 68.00% mesotrione and 22.91% atrazine after 8 days
    to the NMC GSM experiment. Give only the accessible qualitative SynCom comparison
    until its exact results and duration are verified.
  - Limit glucose dependence to the tested comparison; distinguish soil isolation/bioremediation
    context from liquid MSM/GSM cultivation. Use a verified physical-environment term
    and modeled/source habitat notes rather than treating contaminated soil as the
    tested broth.
  - Before adding numeric culture conditions, inspect the exact primary Methods/SI
    and attach claim-level evidence. Do not import protocol from a similar black-soil
    study.
- action_id: repair-four-isolate-grounding
  description: Resolve the four-isolate roster without collapsing a genus complex.
  finding_ids:
  - four-isolate-grounding
  target_ids:
  - CommunityMech:000482
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Recover exact four-isolate identities and source labels from Methods/SI before
    changing the roster or participant assignments. Preserve uncertainty if access
    remains blocked; do not invent a fourth strain or assume all three complex genera
    are present.
  - Distinguish the multigenus amplicon signal from a verified Burkholderia isolate.
    Retain valid NCBI/GTDB labels only for the biological entity actually supported.
  - Justify each abundance category from community-specific ordinal evidence, or remove/qualify
    it. Keystone network importance alone is insufficient; no arbitrary percentage
    threshold is imposed. Verify strain-specific functional claims rather than assuming
    every taxon carries both genes.
- action_id: repair-mechanism-and-edges
  description: Bound metabolic mechanisms and both causal arrows.
  finding_ids:
  - mechanism-and-edges
  target_ids:
  - CommunityMech:000482
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Black_Soil_Glucose_Activated_Herbicide_Mixture_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Retain source-reported improved degradation and the authors' glucose/metagenomic
    interpretation with appropriate NMC/SynCom qualifiers. Do not call degradation
    mineralization or formal synergism without a corresponding assay.
  - Remove or explicitly support SYNTROPHY and SYNTROPHIC_PARTNER using actual partner-product
    utilization/removal that favors producer metabolism; do not impose an obligacy
    requirement or substitute another interaction type without evidence.
  - 'Review each arrow independently: glucose-associated changes do not by themselves
    establish metabolic activation→gene enrichment, and functional selection→SynCom
    construction is a workflow rather than a biological causal edge. Retain only source-supported
    directions with the appropriate evidence qualifier.'
  - Verify expression/flux, acidification necessity, gene-to-isolate mapping and mineralization
    claims against full Methods/Results/SI before certifying them. Do not fabricate
    protein accessions or restore unsupported mechanistic specificity to preserve
    node count.
limitations:
- Full primary Methods, Results, figures, supplements, exact four-isolate roster,
  culture recipe and raw data were not accessible in the inspected routes. This prevents
  whole-source scientific certification.
- The natural microbial consortium (NMC) and the constructed four-isolate SynCom are
  distinct experimental populations. The abstract reports the eight-day percentages
  in the NMC comparison; it separately reports better SynCom performance without giving
  those SynCom percentages.
- RF/co-occurrence keystone identification and metagenomic gene enrichment are association/potential
  evidence. They do not independently establish isotope-resolved flux, gene expression,
  enzyme activity, partner-product removal, mineralization or each isolate carrying
  every named gene.
- Publisher indexed excerpts remain search leads. OpenAlex/EPMC access flags and bounded
  failed routes do not prove that no public copy, supplement or dataset exists globally.
  No authentication bypass, paid provider, author contact or alternate-paper substitution.
- No strain aliases, exact GSM recipe, unreported accessions, raw sequence analysis
  or causal mechanisms were invented. The similarly themed 2025 eight-herbicide study
  is a different source.
notes:
- No canonical, cache, history, generated or saved-review files changed; all 24 inspected
  inputs remain pinned.
- All nine quotations match direct source/cache. Exact matching does not validate
  the inferred cause, strain identity or experimental population.
- Native completeness 70 and capped quality 100/raw 101.6666667 remain separate from
  partial source access and unresolved findings.
- ENGINEERED/SYNTHETIC is appropriate for the constructed SynCom; this review does
  not invent a different origin, missing strain or recipe.
tags:
- record-review
- herbicide
- synthetic-community
- partial-source
- batch-07
```
