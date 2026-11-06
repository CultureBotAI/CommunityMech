# Bifidobacterium–Bacillus alginate coculture: record review

- Review: 20261021T105317Z-bifidobacterium-bacillus-alginate-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T10:48:50.776536Z
- Finished UTC: 2026-10-21T10:53:17.180420Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

The named pair and reported B. longum viability outcomes are supported at direct-abstract scope. Two major findings concern unsupported syntrophic roles and graph signs, beneficiary direction and causal links. Critical full scientific text remains unavailable, so the review is partial.

## Scope And Provenance

Every record field, all three nodes and both arrows assessed using direct abstract/metadata, current schema, catalogue identity, ontology and native checks; full scientific source assessment unavailable.

Selection: Next assigned maintained path after 000005 was saved and both mandatory post-save checks passed; only CommunityMech:000478 reviewed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000478 | kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml | maintained | Bifidobacterium longum DSM20219 and Bacillus subtilis SOM8 Alginate Biofilm Probiotic Co-Culture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000478 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000478 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000478 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000478 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000478 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000478 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000478 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000478 | Target reference validation passed against the pinned abstract cache. |
| audit-network | failed | True | CommunityMech:000478 | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; the target-native audit has no issue. |
| check-network-quality | failed | True | CommunityMech:000478 | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; the target-native audit has no issue. |
| Publication and strain identity | passed | True | CommunityMech:000478 | Fresh metadata and direct abstract verify the paper and pair; DSMZ verifies the named DSM culture at catalogue scope. |
| Full scientific source assessment | unavailable | True | CommunityMech:000478 | Critical full Methods/Results, figures and supplements remain unavailable; redirect/coredata responses do not complete scientific verification. |
| Encoded medium/ingredient-Mech links | not_applicable | False | CommunityMech:000478 | No CultureMech or MediaIngredientMech identifier is encoded. |
| Optional structured source adapter | unavailable | False | CommunityMech:000478 | No runnable adapter was available in the owned runtime. |

## Scientific And Domain Assessments

### Resolved alginate probiotic pair

identity: supported. Targets: CommunityMech:000478.

The intended members and synthetic laboratory formulation are supported; detailed source access remains incomplete.

### Both SYNTROPHIC_PARTNER assignments

evidence: concern. Targets: CommunityMech:000478.

Physical co-encapsulation and improved recipient survival do not establish syntrophic metabolism.

Both strains are supported members, but their attached evidence establishes composition or B. longum viability rather than metabolic cooperation. Source or remove the role assignments without inventing transferred metabolites, assuming oxygen consumption, or requiring obligate interdependence. Both DOMINANT labels can express coequal engineered prominence; they are not measured abundance fractions or proof of persistence.

### Node 0: biofilm/matrix formation, B. subtilis → B. longum

graph: concern. Targets: CommunityMech:000478.

The biofilm-associated formulation is supported, but COMMENSALISM and causal protection exceed the inspected evidence.

The pairwise node concerns aggregation and matrix within alginate. The abstract reports an association with recipient protection, without establishing that Bacillus is unaffected. GO:0042710 is relevant process context; retain the association without treating the label as evidence of a signed ecological effect or isolated protective mechanism.

### Node 1: SGF/SIF viability, B. subtilis → B. longum

graph: concern. Targets: CommunityMech:000478.

The B. longum viability comparison is supported at abstract scope; the partner-neutrality claim is not.

The reported CFU advantage concerns the biofilm-assisted formulation relative to alginate-only encapsulation after two hours in simulated fluids. It does not establish Bacillus neutrality or assign the entire effect to a single member or matrix component. Biofilm formation can be qualified mechanistic context, not an identity-equivalent annotation of survival.

### Node 2: storage viability, encoded B. longum → B. subtilis

graph: concern. Targets: CommunityMech:000478.

The measured B. longum beneficiary conflicts with the encoded target; MUTUALISM lacks reciprocal-benefit evidence.

Retain the reported aerobic-storage viability outcome, while correcting participant direction and withholding an unmeasured benefit to Bacillus. The abstract supplies no storage temperature; the word ambient must not be taken as a verified room-temperature condition. No temperature correction is inferred from indexed leads.

### Arrow 0 → 1: biofilm/matrix formation → GI survival

graph: concern. Targets: CommunityMech:000478.

The abstract suggests association, whereas the edge asserts directly implied protection.

The proposed mediator is biofilm/matrix in the SOM8–DSM20219 alginate formulation and the endpoint is B. longum viability in SGF/SIF. Preserve the source qualifier; full Methods and interventions remain uninspected. If retained, the causal interpretation needs appropriately partial or hypothesized wording and evidence, rather than a stronger label inferred from temporal co-culture observations.

### Arrow 1 → 2: GI survival → aerobic-storage viability

graph: concern. Targets: CommunityMech:000478.

Two improved endpoints do not establish that one causes the other.

The encoded source is GI survival and target is storage survival, but the edge description proposes shared matrix protection. These are different causal claims. Remove the unsupported endpoint-to-endpoint arrow; do not automatically substitute a new matrix-to-storage causal edge without source-specific support and qualification.

### Cultivation, environmental factors and optional enrichment

completeness: unknown. Targets: CommunityMech:000478.

Assay categories and reported durations are recoverable; exact culture and challenge protocols remain unresolved.

ENGINEERED/SYNTHETIC/BIOTECHNOLOGY and laboratory environment fit the formulation. No metal-processing phenotype is asserted. Retain the two-hour and 28-day scopes without inferring that SGF and SIF were sequential, or that ambient oxygen specifies temperature. Structured strain/catalogue links and source-backed medium/design fields are useful follow-up, not automatic defects or a license to import DSMZ maintenance conditions. No dataset absence is inferred from an abstract.

### Exact excerpts and prior graph curation

provenance: supported. Targets: CommunityMech:000478.

All eight snippets are authentic at abstract scope; their presence does not validate the prior causal interpretation.

The prior history/decision is preserved as provenance. The current review reassesses all three nodes and two arrows against actual source language and current schema semantics; no cache or saved history is changed.

### Native gates and scientific source boundary

schema: supported. Targets: CommunityMech:000478.

All eight native checks pass; critical source unavailability and corpus warnings remain explicit.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000478.

Mechanical scores do not certify ecological interpretation or overcome partial scientific status.

## Findings

### syntrophic-roles: Source or remove unsupported syntrophic roles

major / open / confirmed; issue key: cm-000478-syntrophic-roles.

Both members are assigned syntrophic metabolism using composition and survival evidence; the accessible source supports physical biofilm-associated protection, not this metabolic role.

### graph-effects-direction: Repair interaction signs, beneficiary direction and causal scope

major / open / confirmed; issue key: cm-000478-graph-effects-direction.

The graph infers partner neutrality or reciprocal benefit, reverses the storage beneficiary, and links parallel stress outcomes into a serial causal chain beyond the abstract.

## Recommended Actions And Acceptance Checks

### repair-syntrophic-roles

Source or remove unsupported syntrophic roles.

- Require source-specific evidence of syntrophic metabolism for each retained SYNTROPHIC_PARTNER assignment; otherwise remove or explicitly qualify the unsupported assignment.
- Do not invent exchanged metabolites, oxygen-consumption mechanisms, replacement roles or obligacy requirements; membership and recipient viability remain supported.
- Retain exact SOM8/DSM20219 identity and attach functional evidence to the narrow role it supports.

### repair-graph-effects-direction

Repair interaction signs, beneficiary direction and causal scope.

- Preserve B. longum viability outcomes and the alginate comparison while using an evidence-supported representation of participants and effects; do not assert Bacillus neutrality or benefit without a measured source basis.
- Correct the storage node so its encoded beneficiary and description agree; do not use B. longum-to-Bacillus MUTUALISM to represent B. longum survival.
- Qualify biofilm/matrix protection as the reported association unless full-source evidence justifies stronger causal wording; align description, taxon notes, GO context and node evidence.
- Remove GI-survival-to-storage causation unless an exact source establishes that direction; shared formulation effects do not by themselves warrant a replacement causal arrow.
- Inspect full Methods/Results before specifying assay sequence, storage temperature, exact media, matrix formulation or mechanisms beyond the abstract; retain separate GI and storage contexts.

### bounded-source-followup

Complete source verification before expanding protocol, strain mapping or mechanism claims.

- Keep the directly supported pair and viability outcomes; do not infer clinical efficacy, full source absence or missing archive deposition from the abstract.
- Optional DSMZ/subspecies enrichment may use the verified catalogue and NCBI candidate, with no automatic genome-to-GTDB reassignment or catalogue-medium transfer.
- After separately authorized curation, preserve append-only history and rerun schema, strict, term, reference, history and target/corpus network checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml; Whole record: two members, three nodes and two arrows | supports | The intended alginate-encapsulated pair is resolved; its biological interaction signs and mechanism require separate assessment from B. longum viability. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42372892&amp;retmode=xml; Article-level metadata and available abstract | supports | Direct PubMed verifies PMID, DOI, title and the complete abstract. |
| crossref | https://api.crossref.org/works/10.1016/j.ijbiomac.2026.153262; Article-level metadata and available abstract | supports | Crossref verifies the DOI/title and publisher identity; it is bibliographic metadata. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42372892&amp;format=json&amp;resultType=core; Article-level metadata and available abstract | supports | Europe PMC supplies the abstract and subscription/no-PMC metadata, not full scientific text. |
| access-publisher | https://doi.org/10.1016/j.ijbiomac.2026.153262; Actual request 2026-10-21T10:48:54.717023Z to 2026-10-21T10:48:55.108944Z | context_only | The DOI request returned a LinkingHub redirect shell despite HTTP 200. |
| access-article-api | https://api.elsevier.com/content/article/PII:S0141813026032022?httpAccept=text/xml; Actual request 2026-10-21T10:49:26.195233Z to 2026-10-21T10:49:26.560444Z | context_only | The public Elsevier API returned coredata only despite HTTP 200. |
| access-sciencedirect | https://www.sciencedirect.com/science/article/pii/S0141813026032022; Actual request 2026-10-21T10:49:26.194777Z to 2026-10-21T10:49:26.343374Z | context_only | The direct ScienceDirect request returned HTTP 403 and an error page. |
| pair | PMID:42372892; Fresh PubMed Abstract: system-development sentence | supports | The abstract identifies SOM8 and DSM20219 in the alginate co-encapsulation system; membership alone does not demonstrate syntrophic metabolism. |
| biofilm | PMID:42372892; Fresh PubMed Abstract: imaging/time-resolved analysis sentence | supports | Imaging and co-culture observations are described as suggested associations with protection, not isolated causal mediation. |
| gi | PMID:42372892; Fresh PubMed Abstract: viability comparison sentence | supports | B. longum survival exceeds 7-log CFU/g after two hours in SGF/SIF, with an approximately three-log advantage over alginate-only encapsulation. |
| storage | PMID:42372892; Fresh PubMed Abstract: sentence immediately after the SGF/SIF comparison | supports | B. longum remains above 6-log CFU/g after aerobic storage; the measured beneficiary is not Bacillus. |
| catalogue | https://www.dsmz.de/collection/catalogue/details/culture/DSM-20219; root-primary-web.json: DSMZ catalogue lines 158–213 | supports | DSM 20219 is B. longum subsp. longum, designation E194b (Variant a), with ATCC 15707/NCTC 11818/WDCM 00225 aliases; maintenance conditions are not the focal protocol. |
| ontology | Local OAK NCBITaxon, ENVO and GO snapshots; ontology-authority.json: four distinct encoded pairs across twelve occurrences | supports | All encoded labels match; biofilm formation is not identical to a CFU endpoint, and authority correspondence does not establish causal mediation. |
| subspecies | NCBITaxon:1679; subspecies-grounding-candidate.json: label, rank and parent | context_only | The optional subspecies candidate is Bifidobacterium longum subsp. longum, parent 216816; this does not invalidate the current species ID or resolve its GTDB mapping. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum, InteractionTypeEnum and AbundanceEnum | supports | SYNTROPHIC_PARTNER requires syntrophic metabolism; COMMENSALISM requires benefit/neutrality and MUTUALISM reciprocal benefit. DOMINANT permits coequal prominence; no obligacy or percentage threshold is imposed. |
| snippets | kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml; snippet-audit.json | supports | All eight excerpts match the pinned abstract cache and fresh direct PubMed abstract; lexical accuracy does not validate their ecological interpretation. |
| history | kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml; provenance-audit.json | supports | Both sidecars and the exact prior row match current target provenance; no directly linked issue or PR is present in that bounded scope. |
| resources | kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml; dataset-verification.json | supports | No target archive accession is established at accessible abstract scope; catalogue identity is distinguished from experiment-specific cultivation. |
| native-target | kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml; support-audit.json | supports | Native structure is COMPLETE with three nodes, two arrows and five node evidence items; this does not establish interaction signs or causal direction. |
| source-scope | PMID:42372892; source-audit.json | context_only | Whole-record assessment is bounded to the direct abstract and metadata because critical full scientific text is unavailable. |
| independent-source | PMID:42372892; root-independent-source-audit.json | context_only | Independent review agrees with two major findings and partial scientific status at the same source boundary. |
| search | Owned maintained roots; local-search.json: ignored-inclusive bounded searches | supports | No reusable taxon match was found within the recorded roots; filename-only mapping discovery is not a global absence claim. |
| adapter | Optional structured source adapter; adapter-check.json: fresh batch 06 owned runtime discovery reuse | supports | No runnable structured adapter was available; no external checkout runner or paid provider was used. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml; Actual execution 2026-10-21T10:49:34.957487+00:00 to 2026-10-21T10:49:35.779278+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-strict kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml --out /private/tmp/cm-review-session/batch-06/000478/strict-report.tsv; Actual execution 2026-10-21T10:49:34.957610+00:00 to 2026-10-21T10:49:37.239649+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-terms kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml; Actual execution 2026-10-21T10:49:34.957716+00:00 to 2026-10-21T10:49:36.750246+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-gtdb kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml; Actual execution 2026-10-21T10:49:35.779552+00:00 to 2026-10-21T10:49:35.862130+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-gtdb-domain kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml; Actual execution 2026-10-21T10:49:35.862525+00:00 to 2026-10-21T10:49:37.308472+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-history history/records/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture; Actual execution 2026-10-21T10:49:36.750617+00:00 to 2026-10-21T10:49:37.525044+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T10:49:37.525650+00:00 to 2026-10-21T10:49:37.589218+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-references-explained kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml; Actual execution 2026-10-21T10:49:37.589487+00:00 to 2026-10-21T10:49:38.574983+00:00 | supports | Target reference validation passed against the pinned abstract cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T10:06:35.990708+00:00 to 2026-10-21T10:06:41.713287+00:00 | supports | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; the target-native audit has no issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T10:06:35.990845+00:00 to 2026-10-21T10:06:41.708376+00:00 | supports | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; the target-native audit has no issue. |

## Limits And Additional Notes

- No full Methods, detailed Results, figure pixels or supplements were inspected. ScienceDirect returned 403; DOI HTTP 200 was a redirect shell and API HTTP 200 coredata only.
- The complete directly retrieved abstract supports reported outcomes and a suggested biofilm association; exact controls, replication, statistical tests, culture medium, matrix recipe, inoculum ratio, challenge sequence and storage temperature remain unverified.
- Search-indexed temperature/construct details are leads only and are not used as source-confirmed corrections. DSMZ catalogue conditions are maintenance information, not the focal protocol.
- No raw data, microbial genome mapping release or code was reanalyzed. Current GTDB coherence does not independently authenticate exact strains or resolve the Bifidobacterium candidate mapping.
- No dataset omission is inferred from abstract scope, and optional strain/design fields are not graded solely for being unpopulated. Native structural completeness does not demonstrate biological causality.
- No canonical, cache, history or generated file was changed.
- All 24 repository inputs were pinned before assessment and rechecked.
- Twelve quoted words from the primary publication; catalogue material is paraphrased.
- Native quality 100 is capped from 111.6667 and does not override partial scientific status.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T105317Z-bifidobacterium-bacillus-alginate-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Bifidobacterium–Bacillus alginate coculture: record review'
started_at: '2026-10-21T10:48:50.776536Z'
finished_at: '2026-10-21T10:53:17.180420Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed source scope, ontology/native checks
    and supporting citation/provenance metadata. Canonical inputs remain unchanged;
    no person-level independence is asserted.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: The named pair and reported B. longum viability outcomes are supported at
  direct-abstract scope. Two major findings concern unsupported syntrophic roles and
  graph signs, beneficiary direction and causal links. Critical full scientific text
  remains unavailable, so the review is partial.
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
  - path: history/records/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture/2026-10-19T053000Z-antigravity-4906.yaml
    sha256: 696c7cc7fe528fa11035cc1b3b4d2c736e80d63f69033004c0eadd3e673023ea
    role: context
  - path: history/records/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture/2026-10-20T041800Z-antigravity-6d6b41.yaml
    sha256: ea695d1afb3b5ef1f305f3c19c6c2d2be27635120ac0e52ba9f39cb56f46d112
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
    sha256: 6d6b41f26553059039d96bac4e4e4a4e3d080d95f4ae11cc852761f905655c47
    role: target
  - path: references_cache/PMID_42372892.txt
    sha256: 14692afedb5d69060ff15313bd24e0449c354a9d2544fc00e6a05a20f62de3bc
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
- target_id: CommunityMech:000478
  path: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  label: Bifidobacterium longum DSM20219 and Bacillus subtilis SOM8 Alginate Biofilm
    Probiotic Co-Culture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
    role: canonical_record
scope:
  description: Every record field, all three nodes and both arrows assessed using
    direct abstract/metadata, current schema, catalogue identity, ontology and native
    checks; full scientific source assessment unavailable.
  selection: Next assigned maintained path after 000005 was saved and both mandatory
    post-save checks passed; only CommunityMech:000478 reviewed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000478
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000478
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    a pass does not establish ecological causality.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000478
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-strict kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-06/000478/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    a pass does not establish ecological causality.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000478
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-terms kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    a pass does not establish ecological causality.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000478
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    a pass does not establish ecological causality.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000478
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    a pass does not establish ecological causality.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000478
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-history history/records/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    a pass does not establish ecological causality.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000478
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    a pass does not establish ecological causality.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target reference validation passed against the pinned abstract cache.
  target_ids:
  - CommunityMech:000478
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-references-explained kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    a pass does not establish ecological causality.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; the target-native audit has no issue.
  target_ids:
  - CommunityMech:000478
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
    and exit 1; the target-native audit has no issue.
  target_ids:
  - CommunityMech:000478
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Reused fresh full-corpus batch 06 execution, not a target-specific pass.
- check_id: publication-identity
  name: Publication and strain identity
  status: passed
  required: true
  summary: Fresh metadata and direct abstract verify the paper and pair; DSMZ verifies
    the named DSM culture at catalogue scope.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - pair
  - catalogue
- check_id: full-scientific-source
  name: Full scientific source assessment
  status: unavailable
  required: true
  summary: Critical full Methods/Results, figures and supplements remain unavailable;
    redirect/coredata responses do not complete scientific verification.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - access-publisher
  - access-article-api
  - access-sciencedirect
  - source-scope
  - independent-source
- check_id: cross-mech
  name: Encoded medium/ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech identifier is encoded.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - resources
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No runnable adapter was available in the owned runtime.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  locator: 'Whole record: two members, three nodes and two arrows'
  summary: The intended alginate-encapsulated pair is resolved; its biological interaction
    signs and mechanism require separate assessment from B. longum viability.
  support: supports
  accessed_at: '2026-10-21T10:53:17.175697Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42372892&retmode=xml
  locator: Article-level metadata and available abstract
  summary: Direct PubMed verifies PMID, DOI, title and the complete abstract.
  support: supports
  accessed_at: '2026-10-21T10:48:54.958946Z'
  snapshot_sha256: 46a046f408de3af4e36e42a85c2f6da559c3e0bfc364a048357340704b3d2fdc
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1016/j.ijbiomac.2026.153262
  locator: Article-level metadata and available abstract
  summary: Crossref verifies the DOI/title and publisher identity; it is bibliographic
    metadata.
  support: supports
  accessed_at: '2026-10-21T10:48:55.020975Z'
  snapshot_sha256: 0adbbdec8f934daaec76ccf67ee8b7025b1ba1c00b340e3bf80415db589a1385
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42372892&format=json&resultType=core
  locator: Article-level metadata and available abstract
  summary: Europe PMC supplies the abstract and subscription/no-PMC metadata, not
    full scientific text.
  support: supports
  accessed_at: '2026-10-21T10:48:55.457318Z'
  snapshot_sha256: 77c710041921b5e1504b6a8d18983c99c0f57704797bed0546bb758ce6517d15
- evidence_id: access-publisher
  kind: validation
  reference: https://doi.org/10.1016/j.ijbiomac.2026.153262
  locator: Actual request 2026-10-21T10:48:54.717023Z to 2026-10-21T10:48:55.108944Z
  summary: The DOI request returned a LinkingHub redirect shell despite HTTP 200.
  support: context_only
  accessed_at: '2026-10-21T10:48:55.108944Z'
  snapshot_sha256: fd5248544fb014d08829aaf429cfab8b824d357bfeaa360ef55037f1b957911a
- evidence_id: access-article-api
  kind: validation
  reference: https://api.elsevier.com/content/article/PII:S0141813026032022?httpAccept=text/xml
  locator: Actual request 2026-10-21T10:49:26.195233Z to 2026-10-21T10:49:26.560444Z
  summary: The public Elsevier API returned coredata only despite HTTP 200.
  support: context_only
  accessed_at: '2026-10-21T10:49:26.560444Z'
  snapshot_sha256: 2e3182222042152f235d73dc6468ebc4b569031d0c869edba55df3ca3e11cd7a
- evidence_id: access-sciencedirect
  kind: validation
  reference: https://www.sciencedirect.com/science/article/pii/S0141813026032022
  locator: Actual request 2026-10-21T10:49:26.194777Z to 2026-10-21T10:49:26.343374Z
  summary: The direct ScienceDirect request returned HTTP 403 and an error page.
  support: context_only
  accessed_at: '2026-10-21T10:49:26.343374Z'
  snapshot_sha256: d86ce84622a0e52d53815d0174355942db3826c26cf69a284c2dfd53fd086a9d
- evidence_id: pair
  kind: primary_source
  reference: PMID:42372892
  locator: 'Fresh PubMed Abstract: system-development sentence'
  summary: The abstract identifies SOM8 and DSM20219 in the alginate co-encapsulation
    system; membership alone does not demonstrate syntrophic metabolism.
  support: supports
  accessed_at: '2026-10-21T10:53:17.176573Z'
  snapshot_sha256: 46a046f408de3af4e36e42a85c2f6da559c3e0bfc364a048357340704b3d2fdc
- evidence_id: biofilm
  kind: primary_source
  reference: PMID:42372892
  locator: 'Fresh PubMed Abstract: imaging/time-resolved analysis sentence'
  summary: Imaging and co-culture observations are described as suggested associations
    with protection, not isolated causal mediation.
  support: supports
  accessed_at: '2026-10-21T10:53:17.176596Z'
  quote: associated with biofilm formation
  snapshot_sha256: 46a046f408de3af4e36e42a85c2f6da559c3e0bfc364a048357340704b3d2fdc
- evidence_id: gi
  kind: primary_source
  reference: PMID:42372892
  locator: 'Fresh PubMed Abstract: viability comparison sentence'
  summary: B. longum survival exceeds 7-log CFU/g after two hours in SGF/SIF, with
    an approximately three-log advantage over alginate-only encapsulation.
  support: supports
  accessed_at: '2026-10-21T10:53:17.176617Z'
  quote: approximately 3-log improvement
  snapshot_sha256: 46a046f408de3af4e36e42a85c2f6da559c3e0bfc364a048357340704b3d2fdc
- evidence_id: storage
  kind: primary_source
  reference: PMID:42372892
  locator: 'Fresh PubMed Abstract: sentence immediately after the SGF/SIF comparison'
  summary: B. longum remains above 6-log CFU/g after aerobic storage; the measured
    beneficiary is not Bacillus.
  support: supports
  accessed_at: '2026-10-21T10:53:17.176638Z'
  quote: 28 days of aerobic storage
  snapshot_sha256: 46a046f408de3af4e36e42a85c2f6da559c3e0bfc364a048357340704b3d2fdc
- evidence_id: catalogue
  kind: authority
  reference: https://www.dsmz.de/collection/catalogue/details/culture/DSM-20219
  locator: 'root-primary-web.json: DSMZ catalogue lines 158–213'
  summary: DSM 20219 is B. longum subsp. longum, designation E194b (Variant a), with
    ATCC 15707/NCTC 11818/WDCM 00225 aliases; maintenance conditions are not the focal
    protocol.
  support: supports
  accessed_at: '2026-10-21T10:53:17.176667Z'
  snapshot_sha256: e43bbadbe4202aa1e20680f624b8cdd1c5aed11e8a4e4478e8cd45926a756bde
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO and GO snapshots
  locator: 'ontology-authority.json: four distinct encoded pairs across twelve occurrences'
  summary: All encoded labels match; biofilm formation is not identical to a CFU endpoint,
    and authority correspondence does not establish causal mediation.
  support: supports
  accessed_at: '2026-10-21T10:53:17.176873Z'
  snapshot_sha256: 08f51aa08a3d7edad444fc6849011a294bea59f896b2b6c6646db3de32501646
- evidence_id: subspecies
  kind: authority
  reference: NCBITaxon:1679
  locator: 'subspecies-grounding-candidate.json: label, rank and parent'
  summary: The optional subspecies candidate is Bifidobacterium longum subsp. longum,
    parent 216816; this does not invalidate the current species ID or resolve its
    GTDB mapping.
  support: context_only
  accessed_at: '2026-10-21T10:53:17.177157Z'
  snapshot_sha256: ceaa31872c801ced18e85f3de1e7bbed37960a3b0e7bc7b0b5cbf164d05db341
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum, InteractionTypeEnum and AbundanceEnum
  summary: SYNTROPHIC_PARTNER requires syntrophic metabolism; COMMENSALISM requires
    benefit/neutrality and MUTUALISM reciprocal benefit. DOMINANT permits coequal
    prominence; no obligacy or percentage threshold is imposed.
  support: supports
  accessed_at: '2026-10-21T10:53:17.177161Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  locator: snippet-audit.json
  summary: All eight excerpts match the pinned abstract cache and fresh direct PubMed
    abstract; lexical accuracy does not validate their ecological interpretation.
  support: supports
  accessed_at: '2026-10-21T10:53:17.177365Z'
  snapshot_sha256: 5ff39af5a9d111b2b7b2df073f6f03aa32a28ce5ede455375e58609a3b3880d9
- evidence_id: history
  kind: record_content
  reference: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  locator: provenance-audit.json
  summary: Both sidecars and the exact prior row match current target provenance;
    no directly linked issue or PR is present in that bounded scope.
  support: supports
  accessed_at: '2026-10-21T10:53:17.177604Z'
  snapshot_sha256: 38c626ccfbabb454f4d79d6bd4129963282dd7675efdb7884056173041bcb017
- evidence_id: resources
  kind: validation
  reference: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  locator: dataset-verification.json
  summary: No target archive accession is established at accessible abstract scope;
    catalogue identity is distinguished from experiment-specific cultivation.
  support: supports
  accessed_at: '2026-10-21T10:53:17.177784Z'
  snapshot_sha256: f7f9ecf2d8485434455680c038c76ea7ea7c13489a1c03c7e9ffdb3e402b8c9e
- evidence_id: native-target
  kind: validation
  reference: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  locator: support-audit.json
  summary: Native structure is COMPLETE with three nodes, two arrows and five node
    evidence items; this does not establish interaction signs or causal direction.
  support: supports
  accessed_at: '2026-10-21T10:53:17.177986Z'
  snapshot_sha256: fe9714a7e0f398c460d07faddc2f89c45c9a2221fac39ae426c1b1fe0cd79e73
- evidence_id: source-scope
  kind: validation
  reference: PMID:42372892
  locator: source-audit.json
  summary: Whole-record assessment is bounded to the direct abstract and metadata
    because critical full scientific text is unavailable.
  support: context_only
  accessed_at: '2026-10-21T10:53:17.178020Z'
  snapshot_sha256: 44c5780b42b60df2d76c38498bcc3b543e09d43d65db505a4195eedbccc17932
- evidence_id: independent-source
  kind: validation
  reference: PMID:42372892
  locator: root-independent-source-audit.json
  summary: Independent review agrees with two major findings and partial scientific
    status at the same source boundary.
  support: context_only
  accessed_at: '2026-10-21T10:53:17.178046Z'
  snapshot_sha256: 467b2e6f69230daf3ea938187b8a125537c82665151647df2070661937d80c3a
- evidence_id: search
  kind: search
  reference: Owned maintained roots
  locator: 'local-search.json: ignored-inclusive bounded searches'
  summary: No reusable taxon match was found within the recorded roots; filename-only
    mapping discovery is not a global absence claim.
  support: supports
  accessed_at: '2026-10-21T10:53:17.178190Z'
  snapshot_sha256: 901d6278d9c6ddc815e0c3fe37d7af7cac8e86566e95a8d003ff45cec3a8dcc4
  search_scope: Recorded rg --no-ignore --hidden searches in kb/taxa and maintained
    community/isolate roots; bounded mapping filename search in data.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: 'adapter-check.json: fresh batch 06 owned runtime discovery reuse'
  summary: No runnable structured adapter was available; no external checkout runner
    or paid provider was used.
  support: supports
  accessed_at: '2026-10-21T10:53:17.178319Z'
  snapshot_sha256: 80e1299ef813dbae3485b4ab701f5be320f2bd259d682313f6bbfb2fdae77941
  search_scope: Explicitly reused same-runtime batch 06 PATH/venv/module and ignored-inclusive
    discovery.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  locator: Actual execution 2026-10-21T10:49:34.957487+00:00 to 2026-10-21T10:49:35.779278+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T10:49:35.779278Z'
  snapshot_sha256: 2ea08d60255eefc438c1626317c449931e38f5cc079c6715092bcf82535a731c
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-strict kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-06/000478/strict-report.tsv
  locator: Actual execution 2026-10-21T10:49:34.957610+00:00 to 2026-10-21T10:49:37.239649+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T10:49:37.239649Z'
  snapshot_sha256: 9891302742ac8a7f39e0680295a8544018be424964f73357d26bb61db40e73e9
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-terms kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  locator: Actual execution 2026-10-21T10:49:34.957716+00:00 to 2026-10-21T10:49:36.750246+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T10:49:36.750246Z'
  snapshot_sha256: 97eb7ad215814a6edad7a1e94009b2c9548329e991fd82295bafbcd1c4dd11cb
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  locator: Actual execution 2026-10-21T10:49:35.779552+00:00 to 2026-10-21T10:49:35.862130+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T10:49:35.862130Z'
  snapshot_sha256: 0864ae7eb5010a309a93e0679066b7aedfdd1b573942c383f1e036c9827287cc
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  locator: Actual execution 2026-10-21T10:49:35.862525+00:00 to 2026-10-21T10:49:37.308472+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T10:49:37.308472Z'
  snapshot_sha256: 0b4739e5390d2a9c9d9066cf6f3b4e8d1ec14a2d9bdb862bd95f898cef328eda
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-history history/records/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture
  locator: Actual execution 2026-10-21T10:49:36.750617+00:00 to 2026-10-21T10:49:37.525044+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T10:49:37.525044Z'
  snapshot_sha256: ccd732eb853a07d5405aed85cdb9b31c8b14ee4fd4883c8a26e3a83b312cdca8
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T10:49:37.525650+00:00 to 2026-10-21T10:49:37.589218+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T10:49:37.589218Z'
  snapshot_sha256: 0f81456385516e4679a6704b0f3892d0f8e36e06103d6396aba31c8046b75674
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-references-explained kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
  locator: Actual execution 2026-10-21T10:49:37.589487+00:00 to 2026-10-21T10:49:38.574983+00:00
  summary: Target reference validation passed against the pinned abstract cache.
  support: supports
  accessed_at: '2026-10-21T10:49:38.574983Z'
  snapshot_sha256: b1b0a0f407e09bed77cfabd8a951a41034f9a1ebdc17306b86984d2330b05fc5
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T10:06:35.990708+00:00 to 2026-10-21T10:06:41.713287+00:00
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; the target-native audit has no issue.
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
    and exit 1; the target-native audit has no issue.
  support: supports
  accessed_at: '2026-10-21T10:06:41.708376Z'
  snapshot_sha256: 0420f90879ef008b71c8bfcfe444d05d2c030519aca57834b4e2587766c5b854
assessments:
- assessment_id: identity
  area: identity
  topic: Resolved alginate probiotic pair
  outcome: supported
  summary: The intended members and synthetic laboratory formulation are supported;
    detailed source access remains incomplete.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - pair
  - pubmed
  - ontology
  - catalogue
  dimensions:
  - name: community_scope
    value: Defined two-member hydrogel formulation
    definition: B. subtilis SOM8 and B. longum DSM20219 are the focal pair; protection
      in simulated fluids is not demonstrated intestinal colonization or human clinical
      benefit.
    evidence_ids:
    - pair
    - gi
  - name: source_strain
    value: SOM8 and DSM20219 explicitly identified
    definition: DSMZ supplies bounded aliases and subspecies identity for DSM20219;
      no independent SOM8 archive or exact genome mapping was established.
    evidence_ids:
    - pair
    - catalogue
    - subspecies
  - name: environment
    value: Laboratory hydrogel, simulated fluids and aerobic storage
    definition: The ENVO label is coherent; the abstract establishes assay classes
      and durations but not exact recipes, pH or temperatures.
    evidence_ids:
    - ontology
    - gi
    - storage
  - name: medium
    value: Focal cultivation and encapsulation protocol unresolved
    definition: Sodium alginate is the matrix. Culture medium, bead formulation, inoculum
      ratio and atmosphere cannot be imported from catalogue maintenance instructions.
    evidence_ids:
    - pair
    - catalogue
    - source-scope
  - name: experimental_setting
    value: In-vitro formulation comparison and separate stress endpoints
    definition: The stated SGF/SIF and storage outcomes do not establish a serial
      challenge pathway or an in-vivo efficacy result.
    evidence_ids:
    - gi
    - storage
    - source-scope
  - name: evidence_tier
    value: Direct abstract outcomes and suggested mechanistic association
    definition: Critical full Methods, detailed Results, figures and supplements remain
      unavailable; this is a partial scientific review.
    evidence_ids:
    - biofilm
    - source-scope
  - name: grounding_status
    value: Four valid current ontology pairs; GTDB status preserved
    definition: Current species IDs are valid. Optional subspecies identity does not
      authorize automatic GTDB reassignment or validate historical mapping statistics.
    evidence_ids:
    - ontology
    - subspecies
- assessment_id: roles
  area: evidence
  topic: Both SYNTROPHIC_PARTNER assignments
  outcome: concern
  summary: Physical co-encapsulation and improved recipient survival do not establish
    syntrophic metabolism.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - pair
  - gi
  - biofilm
  - schema
  details: Both strains are supported members, but their attached evidence establishes
    composition or B. longum viability rather than metabolic cooperation. Source or
    remove the role assignments without inventing transferred metabolites, assuming
    oxygen consumption, or requiring obligate interdependence. Both DOMINANT labels
    can express coequal engineered prominence; they are not measured abundance fractions
    or proof of persistence.
- assessment_id: node-0
  area: graph
  topic: 'Node 0: biofilm/matrix formation, B. subtilis → B. longum'
  outcome: concern
  summary: The biofilm-associated formulation is supported, but COMMENSALISM and causal
    protection exceed the inspected evidence.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - biofilm
  - pair
  - schema
  - ontology
  details: The pairwise node concerns aggregation and matrix within alginate. The
    abstract reports an association with recipient protection, without establishing
    that Bacillus is unaffected. GO:0042710 is relevant process context; retain the
    association without treating the label as evidence of a signed ecological effect
    or isolated protective mechanism.
- assessment_id: node-1
  area: graph
  topic: 'Node 1: SGF/SIF viability, B. subtilis → B. longum'
  outcome: concern
  summary: The B. longum viability comparison is supported at abstract scope; the
    partner-neutrality claim is not.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - gi
  - biofilm
  - schema
  - source-scope
  details: The reported CFU advantage concerns the biofilm-assisted formulation relative
    to alginate-only encapsulation after two hours in simulated fluids. It does not
    establish Bacillus neutrality or assign the entire effect to a single member or
    matrix component. Biofilm formation can be qualified mechanistic context, not
    an identity-equivalent annotation of survival.
- assessment_id: node-2
  area: graph
  topic: 'Node 2: storage viability, encoded B. longum → B. subtilis'
  outcome: concern
  summary: The measured B. longum beneficiary conflicts with the encoded target; MUTUALISM
    lacks reciprocal-benefit evidence.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - storage
  - schema
  - ontology
  details: Retain the reported aerobic-storage viability outcome, while correcting
    participant direction and withholding an unmeasured benefit to Bacillus. The abstract
    supplies no storage temperature; the word ambient must not be taken as a verified
    room-temperature condition. No temperature correction is inferred from indexed
    leads.
- assessment_id: edge-0-1
  area: graph
  topic: 'Arrow 0 → 1: biofilm/matrix formation → GI survival'
  outcome: concern
  summary: The abstract suggests association, whereas the edge asserts directly implied
    protection.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - biofilm
  - gi
  - source-scope
  details: The proposed mediator is biofilm/matrix in the SOM8–DSM20219 alginate formulation
    and the endpoint is B. longum viability in SGF/SIF. Preserve the source qualifier;
    full Methods and interventions remain uninspected. If retained, the causal interpretation
    needs appropriately partial or hypothesized wording and evidence, rather than
    a stronger label inferred from temporal co-culture observations.
- assessment_id: edge-1-2
  area: graph
  topic: 'Arrow 1 → 2: GI survival → aerobic-storage viability'
  outcome: concern
  summary: Two improved endpoints do not establish that one causes the other.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - gi
  - storage
  - biofilm
  details: The encoded source is GI survival and target is storage survival, but the
    edge description proposes shared matrix protection. These are different causal
    claims. Remove the unsupported endpoint-to-endpoint arrow; do not automatically
    substitute a new matrix-to-storage causal edge without source-specific support
    and qualification.
- assessment_id: context
  area: completeness
  topic: Cultivation, environmental factors and optional enrichment
  outcome: unknown
  summary: Assay categories and reported durations are recoverable; exact culture
    and challenge protocols remain unresolved.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - gi
  - storage
  - catalogue
  - resources
  - source-scope
  details: ENGINEERED/SYNTHETIC/BIOTECHNOLOGY and laboratory environment fit the formulation.
    No metal-processing phenotype is asserted. Retain the two-hour and 28-day scopes
    without inferring that SGF and SIF were sequential, or that ambient oxygen specifies
    temperature. Structured strain/catalogue links and source-backed medium/design
    fields are useful follow-up, not automatic defects or a license to import DSMZ
    maintenance conditions. No dataset absence is inferred from an abstract.
- assessment_id: provenance
  area: provenance
  topic: Exact excerpts and prior graph curation
  outcome: supported
  summary: All eight snippets are authentic at abstract scope; their presence does
    not validate the prior causal interpretation.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - snippets
  - history
  - source-scope
  details: The prior history/decision is preserved as provenance. The current review
    reassesses all three nodes and two arrows against actual source language and current
    schema semantics; no cache or saved history is changed.
- assessment_id: validation
  area: schema
  topic: Native gates and scientific source boundary
  outcome: supported
  summary: All eight native checks pass; critical source unavailability and corpus
    warnings remain explicit.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - source-scope
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality
  outcome: supported
  summary: Mechanical scores do not certify ecological interpretation or overcome
    partial scientific status.
  target_ids:
  - CommunityMech:000478
  evidence_ids:
  - native-target
  - record
  metrics:
  - name: completeness
    value: 65
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata including all roles +5 environment +10
      at least 3 factors +10 at least 3 nodes +5 resources +10 media +5 datasets +5
      node metabolites). 50+5+0+10+0+0+0+0=65; populated roles are credited mechanically
      even when unsupported.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50P1-10P2-2P3+20 min(mean node evidence/2,1)+15 if native
      COMPLETE,0,100). P1=0,P2=2,P3=0,P4=0; 5 evidence items/3 nodes gives 16.6667
      evidence bonus; 100-20+16.6667+15=111.6667 before capping.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count.
  - name: P2
    value: 2
    unit: findings
    definition: Observed native severity count.
  - name: P3
    value: 0
    unit: findings
    definition: Observed native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count.
findings:
- finding_id: syntrophic-roles
  issue_key: cm-000478-syntrophic-roles
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: a substantive biological attribution exceeds the
    inspected source, rather than a label-format or optional-field defect.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Source or remove unsupported syntrophic roles
  description: Both members are assigned syntrophic metabolism using composition and
    survival evidence; the accessible source supports physical biofilm-associated
    protection, not this metabolic role.
  target_ids:
  - CommunityMech:000478
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  evidence_ids:
  - pair
  - gi
  - biofilm
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
    role: canonical_record
- finding_id: graph-effects-direction
  issue_key: cm-000478-graph-effects-direction
  category: graph
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: a substantive biological attribution exceeds the
    inspected source, rather than a label-format or optional-field defect.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Repair interaction signs, beneficiary direction and causal scope
  description: The graph infers partner neutrality or reciprocal benefit, reverses
    the storage beneficiary, and links parallel stress outcomes into a serial causal
    chain beyond the abstract.
  target_ids:
  - CommunityMech:000478
  field_paths:
  - description
  - taxonomy[0].taxon_term.notes
  - ecological_interactions[0]
  - ecological_interactions[1]
  - ecological_interactions[2]
  evidence_ids:
  - biofilm
  - gi
  - storage
  - schema
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
    role: canonical_record
actions:
- action_id: repair-syntrophic-roles
  description: Source or remove unsupported syntrophic roles.
  finding_ids:
  - syntrophic-roles
  target_ids:
  - CommunityMech:000478
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Require source-specific evidence of syntrophic metabolism for each retained SYNTROPHIC_PARTNER
    assignment; otherwise remove or explicitly qualify the unsupported assignment.
  - Do not invent exchanged metabolites, oxygen-consumption mechanisms, replacement
    roles or obligacy requirements; membership and recipient viability remain supported.
  - Retain exact SOM8/DSM20219 identity and attach functional evidence to the narrow
    role it supports.
- action_id: repair-graph-effects-direction
  description: Repair interaction signs, beneficiary direction and causal scope.
  finding_ids:
  - graph-effects-direction
  target_ids:
  - CommunityMech:000478
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve B. longum viability outcomes and the alginate comparison while using
    an evidence-supported representation of participants and effects; do not assert
    Bacillus neutrality or benefit without a measured source basis.
  - Correct the storage node so its encoded beneficiary and description agree; do
    not use B. longum-to-Bacillus MUTUALISM to represent B. longum survival.
  - Qualify biofilm/matrix protection as the reported association unless full-source
    evidence justifies stronger causal wording; align description, taxon notes, GO
    context and node evidence.
  - Remove GI-survival-to-storage causation unless an exact source establishes that
    direction; shared formulation effects do not by themselves warrant a replacement
    causal arrow.
  - Inspect full Methods/Results before specifying assay sequence, storage temperature,
    exact media, matrix formulation or mechanisms beyond the abstract; retain separate
    GI and storage contexts.
- action_id: bounded-source-followup
  description: Complete source verification before expanding protocol, strain mapping
    or mechanism claims.
  finding_ids:
  - syntrophic-roles
  - graph-effects-direction
  target_ids:
  - CommunityMech:000478
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Bacillus_Alginate_Biofilm_Probiotic_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Keep the directly supported pair and viability outcomes; do not infer clinical
    efficacy, full source absence or missing archive deposition from the abstract.
  - Optional DSMZ/subspecies enrichment may use the verified catalogue and NCBI candidate,
    with no automatic genome-to-GTDB reassignment or catalogue-medium transfer.
  - After separately authorized curation, preserve append-only history and rerun schema,
    strict, term, reference, history and target/corpus network checks.
limitations:
- No full Methods, detailed Results, figure pixels or supplements were inspected.
  ScienceDirect returned 403; DOI HTTP 200 was a redirect shell and API HTTP 200 coredata
  only.
- The complete directly retrieved abstract supports reported outcomes and a suggested
  biofilm association; exact controls, replication, statistical tests, culture medium,
  matrix recipe, inoculum ratio, challenge sequence and storage temperature remain
  unverified.
- Search-indexed temperature/construct details are leads only and are not used as
  source-confirmed corrections. DSMZ catalogue conditions are maintenance information,
  not the focal protocol.
- No raw data, microbial genome mapping release or code was reanalyzed. Current GTDB
  coherence does not independently authenticate exact strains or resolve the Bifidobacterium
  candidate mapping.
- No dataset omission is inferred from abstract scope, and optional strain/design
  fields are not graded solely for being unpopulated. Native structural completeness
  does not demonstrate biological causality.
notes:
- No canonical, cache, history or generated file was changed.
- All 24 repository inputs were pinned before assessment and rechecked.
- Twelve quoted words from the primary publication; catalogue material is paraphrased.
- Native quality 100 is capped from 111.6667 and does not override partial scientific
  status.
tags:
- record-review
- probiotic
- biofilm
- source-scope
- batch-06
```
