# Bifidobacterium–Faecalibacterium 2′-FL/FOS coculture: record review

- Review: 20261021T105953Z-bifidobacterium-faecalibacterium-2fl-fos-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T10:55:16.761476Z
- Finished UTC: 2026-10-21T10:59:53.226059Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Complete source review supports the bounded ratio-dependent butyrate endpoint and putative acetate-transfer graph. Two major findings concern current A2-165 species grounding and the DIET category; one minor finding concerns the B. bifidum consumer-role assignment. Preserve experimental qualifications and zero arrows.

## Scope And Provenance

Whole record, both nodes and absence of downstream arrows assessed against complete main text, all figures/S1, current culture catalogue/ontology and native checks.

Selection: Next assigned maintained path after 000478 was saved and both mandatory post-save checks passed; only CommunityMech:000401 reviewed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000401 | kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml | maintained | Bifidobacterium-Faecalibacterium 2′-FL/FOS Butyrate Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000401 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000401 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000401 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000401 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000401 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000401 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000401 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000401 | Target reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000401 | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |
| check-network-quality | failed | True | CommunityMech:000401 | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |
| Primary publication and strain authority | passed | True | CommunityMech:000401 | Direct metadata/full text and JCM/OAK identities were verified, revealing the current A2-165 nomenclature mismatch. |
| Full primary scientific assessment | passed | True | CommunityMech:000401 | Complete main text, four main figures and the full Supplementary S1 were inspected with experimental limits preserved. |
| Encoded medium/ingredient-Mech links | not_applicable | False | CommunityMech:000401 | No CultureMech or MediaIngredientMech identifier is encoded; exact recipe equivalence was not inferred. |
| Optional structured source adapter | unavailable | False | CommunityMech:000401 | No runnable adapter was available in the owned runtime. |

## Scientific And Domain Assessments

### Exact model and strain provenance

identity: concern. Targets: CommunityMech:000401.

The experiment is resolved, but its A2-165 current species grounding must be reconciled with the paper’s legacy name.

### taxonomy[0]: B. bifidum JCM1254

grounding: concern. Targets: CommunityMech:000401.

Species and collection identity are supported, but the recipient CROSS_FEEDER role lacks source support.

The substrate-response evidence supports degradation of the supplied oligosaccharide and a donor interpretation. The source does not show B. bifidum consuming Faecalibacterium metabolites. Its existing species 1681 ID is compatible with the named strain; optional strain 398514 enrichment is not required to fix a wrong identity.

### taxonomy[1]: A2-165/JCM31915

grounding: concern. Targets: CommunityMech:000401.

The named culture is current F. duncaniae, not species 853 F. prausnitzii.

This is a current grounding correction for the same biological isolate, not a different experiment or evidence fabrication. Preserve A2-165/JCM31915 and legacy source quotations; use verified current nomenclature consistently in taxonomy and graph participants. FOS utilization supports the substrate-degrader role; acetate uptake remains author-inferred and should retain its qualification. Catalogue identity alone does not resolve GTDB.

### community_category: DIET

evidence: concern. Targets: CommunityMech:000401.

A dietary-substrate experiment does not establish direct interspecies electron transfer.

No direct electrical coupling is measured or proposed in the inspected study. Choose a schema-valid category matching the verified gut-culture experiment, with rationale; do not infer a replacement category solely from the word diet or force a syntrophy classification.

### ecological_interactions[0]: ratio-dependent butyrate peak

graph: supported. Targets: CommunityMech:000401.

Retain the measured community-level endpoint with its present assay and mechanism limits.

Participants are JCM1254 and A2-165, whose current taxon annotation needs the separate correction. The node has no donor-to-recipient direction or downstream arrow. Its 10:90 maximum, growth/output distinction, fixed added carbohydrate and 24-hour endpoint are supported; Figure 3d separates the peak statistically. Preserve its warning against an in-vivo optimum or donor-resolved transfer claim.

### ecological_interactions[1]: putative JCM1254 → A2-165 acetate support

graph: supported. Targets: CommunityMech:000401.

Retain the explicitly PARTIAL cross-feeding interpretation, distinct from the measured acid endpoints.

The proposed donor is B. bifidum and recipient is A2-165/current F. duncaniae; acetate is the only encoded pairwise metabolite. Main Discussion proposes this direction while acknowledging absent flux, pH and residual-substrate measurements. qPCR and S1 are abundance estimates, not viable counts. Keep zero downstream arrows and do not convert this interpretation into demonstrated acetate transfer.

### Medium, design, factors and batch setup

completeness: supported. Targets: CommunityMech:000401.

The recorded perturbation, incubation and derived working volume agree with the focal Methods.

Monocultures receive one 8 µL standardized suspension; cocultures receive two into 800 µL medium, giving the explicitly modeled 816 µL. This arithmetic does not establish equal cell counts or biomass. Keep initial glucose-YCFA revival distinct from sugar/VFA-free YCFA− assays. Culture pH is unmeasured; chromatographic mobile-phase pH and column temperature are analytical settings, not culture conditions. Basal recipe expansion would require the cited formulation; no catalogue protocol is substituted.

### 2′-FL, FOS, acetate, butyrate and GO scope

grounding: supported. Targets: CommunityMech:000401.

The ingredients and broad carbohydrate-process grounding fit the bounded experiment.

FOS is the source preparation of kestose, nystose and fructofuranosylnystose, not an automatically interchangeable single compound. Acetate is measured and only a proposed contributor to butyrate; the ingredient prose preserves that distinction. No metal/REE phenotype is asserted. The broad GO label is valid without proving a unique enzymatic pathway.

### Source excerpts, prior repairs and resources

provenance: supported. Targets: CommunityMech:000401.

Exact snippets and current history support the existing graph qualifications while leaving non-graph taxonomy actionable.

Issues 991–994 and 1254 are closed and their repairs remain present; open 1256 names the current strain-taxonomy question. The publication links resolve. No absent external dataset is inferred when Data Availability points to the paper/SI; catalogue genome links are not newly generated data from this experiment.

### Native checks and current source assessment

schema: supported. Targets: CommunityMech:000401.

All eight native checks pass; the source audit identifies semantic issues beyond those gates.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000401.

Mechanical metrics remain distinct from experimental correctness and taxonomic attribution.

## Findings

### a2-165-current-taxon: Reconcile A2-165 with current F. duncaniae grounding

major / open / confirmed; issue key: cm-000401-a2-165-current-taxon.

The exact JCM culture is verified as F. duncaniae, while taxonomy and graph participants use the distinct current F. prausnitzii species ID.

### diet-category: Replace the unsupported electron-transfer category

major / open / confirmed; issue key: cm-000401-diet-category.

The record uses DIET for a dietary-substrate model even though the schema defines it as direct interspecies electron transfer and the source supplies no such evidence.

### donor-recipient-role: Qualify the B. bifidum recipient-role assignment

minor / open / confirmed; issue key: cm-000401-donor-recipient-role.

The source supports substrate use and a proposed metabolite-donor role, but not B. bifidum uptake of metabolites from its partner.

## Recommended Actions And Acceptance Checks

### repair-a2-165-current-taxon

Reconcile A2-165 with current F. duncaniae grounding.

- Ground A2-165/JCM31915 to verified NCBITaxon:411483 Faecalibacterium duncaniae consistently in taxonomy and graph participants, retaining the exact culture identity.
- Preserve literal source quotations and explain that the paper uses the legacy F. prausnitzii name; do not rewrite historical evidence or imply a different experimental isolate.
- Keep source naming, current nomenclature and exact strain distinct in prose and notes; reassess GTDB only with an applicable verified mapping, without forcing an assignment.
- Rerun term, GTDB/domain and network consistency checks after a separately authorized correction.

### repair-diet-category

Replace the unsupported electron-transfer category.

- Select a schema-valid category justified by the verified experiment, with an explicit rationale; OTHER is preferable to an unsupported mechanistic classification where no narrower category fits.
- Do not reinterpret DIET as dietary supplementation or infer electron transfer from fermentation/metabolite exchange.
- Preserve the bounded carbohydrate-ratio and putative acetate-transfer graph; category correction does not require new nodes or arrows.

### repair-donor-recipient-role

Qualify the B. bifidum recipient-role assignment.

- Remove or source-qualify B. bifidum CROSS_FEEDER under its consumer definition; donor secretion alone is insufficient.
- Attach role-specific substrate/fermentation evidence to retained roles, without inventing reverse transfer or a new replacement role.
- Retain Faecalibacterium recipient support as author-inferred and preserve the explicit unresolved flux, pH and substrate limitations.

### preserve-qualified-model

Preserve the two qualified nodes, zero arrows and experimental limitations during separately authorized follow-up.

- Do not convert acid pools, relative qPCR or estimated copies into donor-resolved flux, viable abundance or an in-vivo optimal formulation.
- Do not import catalogue growth conditions or reference-genome records as the focal study’s experimental data.
- Preserve append-only history and rerun schema, strict, term, reference, history and target/corpus network checks after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml; Whole record: exact two-strain model, two nodes and no arrows | supports | The experiment and strains are identifiable; category, current taxonomic grounding and one functional-role attribution require correction. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42655156&amp;retmode=xml; Article-level metadata | supports | PubMed verifies PMID, DOI, title and abstract. |
| crossref | https://api.crossref.org/works/10.3390/microorganisms14081812; Article-level metadata | supports | Crossref verifies the DOI/title and publisher identity. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42655156&amp;format=json&amp;resultType=core; Article-level metadata | supports | Europe PMC verifies the article metadata, PMC identifier and open full-text route. |
| methods | PMID:42655156; Fresh XML sec2dot1–sec2dot5: strains, growth, qPCR, acids and statistics | supports | Methods establish the exact JCM strains, 48-well anaerobic YCFA− experiment and distinct growth, qPCR and acid-concentration measurements. |
| peak | PMID:42655156; Fresh XML sec3dot3 and sec5; Figure 3d | supports | The tested 10:90 substrate ratio gives the maximal butyrate endpoint, distinct from the conditions maximizing total OD600. |
| transfer | PMID:42655156; Fresh XML sec4: acetate interpretation and five explicit limitations | supports | The authors propose a bifidobacterial contribution while acknowledging unmeasured flux, culture pH and residual substrates; they do not establish reciprocal uptake by B. bifidum. |
| mono | PMID:42655156; Fresh XML sec3dot1–sec3dot2 and Figures1–2 | supports | Monoculture substrate responses and acid endpoints support complementary substrate use; donor secretion alone does not establish a recipient functional role. |
| figure-1 | PMID:42655156; figure-1.body: all panels and caption inspected | supports | Faecalibacterium monoculture responds to FOS-containing conditions; endpoints remain concentrations and OD. |
| figure-2 | PMID:42655156; figure-2.body: all panels and caption inspected | supports | B. bifidum responds to increasing 2′-FL with lactate/acetate accumulation and no detected butyrate. |
| figure-3 | PMID:42655156; figure-3.body: all panels and caption inspected | supports | The 10% 2′-FL butyrate bar has a distinct significance letter; OD and other acid patterns differ. |
| figure-4 | PMID:42655156; figure-4.body: all panels and caption inspected | supports | Relative qPCR composition shifts with substrate ratio; it is not a viable-cell count or donor-resolved flux. |
| supplement | PMID:42655156; Supplementary Figure S1: entire one-page PDF and pixels | supports | Estimated genome-copy profiles provide an additional abundance measure; they do not demonstrate viable abundance, acetate transfer or the cause of the butyrate peak. |
| catalogues | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=31915; https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=1254; root-catalogue-web.json: JCM31915 lines4–35, JCM1254 lines4–31 and May 2022 announcement lines61–95 | supports | JCM identifies A2-165/JCM31915/DSM17677 as F. duncaniae after an explicit name change; JCM1254/DSM20082 remains B. bifidum. |
| strain-authority | NCBITaxon:411483; NCBITaxon:853; NCBITaxon:398514; jcm-strain-authority.json: canonical labels, ranks and asserted parent chains | supports | 411483 is species F. duncaniae, separate from species 853 F. prausnitzii; strain 398514 belongs to species 1681 B. bifidum. |
| ontology | Local OAK NCBITaxon, ENVO, CHEBI and GO; ontology-authority.json: eight encoded pairs across eighteen occurrences | supports | Current ID/label strings match authority labels; that lexical match does not make species 853 correct for the specifically named A2-165 culture. |
| schema | src/communitymech/schema/communitymech.yaml; CommunityCategoryEnum.DIET; FunctionalRoleEnum.CROSS_FEEDER and PRIMARY_DEGRADER | supports | DIET means direct interspecies electron transfer; CROSS_FEEDER denotes consumption of another taxon’s metabolites; substrate degradation and metabolite supply are distinct roles. |
| snippets | kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml; snippet-audit.json | supports | All 31 snippets match the fresh full XML and appended primary cache; main-text scope is distinct from abstract-only comparison. |
| history | kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml; provenance-audit.json | supports | Three histories and the exact graph-only row preserve prior repairs; current issue 1256 explicitly includes the A2-165 taxonomy follow-up. |
| resources | kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml; dataset-verification.json | supports | Data Availability points to article/SI and further inquiry without an accession; catalogue genomes are separate identity resources. |
| native-target | kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml; support-audit.json | supports | The target network is COMPLETE with two nodes, no arrows and six node evidence items; mechanical completeness does not validate roles or taxonomy. |
| source-scope | PMID:42655156; source-audit.json | supports | Complete scientific main, all four figures and Supplementary S1 were inspected; no raw-data or genome reanalysis was performed. |
| independent-source | PMID:42655156; root-independent-source-audit.json | context_only | Independent source assessment supplies a separate check of the study, current strain identity and bounded findings. |
| search | Owned maintained roots; local-search.json: ignored-inclusive bounded searches | supports | Recorded searches bound reusable identity/resource discovery without asserting global absence. |
| adapter | Optional structured source adapter; adapter-check.json: same-runtime batch 06 discovery reuse | supports | No runnable adapter was available in the owned runtime; no external runner or paid provider was used. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml; Actual execution 2026-10-21T10:55:51.940838+00:00 to 2026-10-21T10:55:52.751254+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-strict kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml --out /private/tmp/cm-review-session/batch-06/000401/strict-report.tsv; Actual execution 2026-10-21T10:55:51.940990+00:00 to 2026-10-21T10:55:54.185997+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-terms kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml; Actual execution 2026-10-21T10:55:51.941087+00:00 to 2026-10-21T10:55:53.798916+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-gtdb kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml; Actual execution 2026-10-21T10:55:52.751504+00:00 to 2026-10-21T10:55:52.837900+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-gtdb-domain kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml; Actual execution 2026-10-21T10:55:52.840862+00:00 to 2026-10-21T10:55:54.216505+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-history history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture; Actual execution 2026-10-21T10:55:53.799268+00:00 to 2026-10-21T10:55:54.516212+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T10:55:54.516782+00:00 to 2026-10-21T10:55:54.580601+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src just --no-dotenv validate-references-explained kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml; Actual execution 2026-10-21T10:55:54.590695+00:00 to 2026-10-21T10:55:55.651862+00:00 | supports | Target reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T10:06:35.990708+00:00 to 2026-10-21T10:06:41.713287+00:00 | supports | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T10:06:35.990845+00:00 to 2026-10-21T10:06:41.708376+00:00 | supports | Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records and exit 1; target-native structure has no issue. |

## Limits And Additional Notes

- No raw data, statistical analysis, genome sequence, isotope tracing or biochemical flux was reanalyzed. Figure inspection verifies reported patterns and scope, not a new quantitative reconstruction.
- Only one strain pair and a 24-hour batch endpoint are studied; pH, residual substrate and direct flux are explicitly unmeasured. The optimal tested ratio is not an established in-vivo optimum.
- Current catalogue identity does not alter literal source nomenclature, verify historical GTDB release statistics or authorize an inferred new GTDB mapping.
- The basal YCFA recipe cited to an earlier reference was not independently reconstructed; no CultureMech formulation or catalogue-maintenance transfer is certified.
- Data Availability points to article/SI and author inquiry; no unreported archive accession or dataset omission is inferred. Catalogue genome links were not fetched or analyzed.
- No canonical, cache, history or generated file changed.
- All 25 repository inputs were pinned before assessment and rechecked.
- Fifteen quoted words from the focal paper; catalogue/reclassification material is paraphrased.
- Native quality 100 is capped from 113; source findings remain actionable.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T105953Z-bifidobacterium-faecalibacterium-2fl-fos-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Bifidobacterium–Faecalibacterium 2′-FL/FOS coculture: record review'
started_at: '2026-10-21T10:55:16.761476Z'
finished_at: '2026-10-21T10:59:53.226059Z'
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
summary: Complete source review supports the bounded ratio-dependent butyrate endpoint
  and putative acetate-transfer graph. Two major findings concern current A2-165 species
  grounding and the DIET category; one minor finding concerns the B. bifidum consumer-role
  assignment. Preserve experimental qualifications and zero arrows.
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
  - path: history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-09-21T023720Z-codex-64dd83.yaml
    sha256: 39c5386f7abbed87c36316495f9b44c7f40ae157e77f2371fc43e0a3529e108f
    role: context
  - path: history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-09-21T024109Z-codex-f468fd.yaml
    sha256: ecd3755e9bfb361ff922f29791f7da2f4792c709ceb538b6a42e9f4bffd72a29
    role: context
  - path: history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture/2026-10-05T112950Z-codex-4bd70f.yaml
    sha256: 33d82b7786f0178a39bd4c9c935288511e7223b1ed85842764acf7a8a4532472
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    sha256: fb0edcb5af076a247ed278b42027f036f101484395333493653d4e6f75f8b319
    role: target
  - path: references_cache/PMID_42655156.txt
    sha256: f40ae202ccae35dad94ef7ed446f94adc2d089879ac64cec97302fc090b35e4c
    role: context
  - path: reports/causal_graph_review/decisions/20261005-eleven-records-batch6.yaml
    sha256: 23f5fa6fc197e020f7cb3469749ebe4aa78886f8973cb6ed63fde321470a7f96
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
- target_id: CommunityMech:000401
  path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  label: Bifidobacterium-Faecalibacterium 2′-FL/FOS Butyrate Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    role: canonical_record
scope:
  description: Whole record, both nodes and absence of downstream arrows assessed
    against complete main text, all figures/S1, current culture catalogue/ontology
    and native checks.
  selection: Next assigned maintained path after 000478 was saved and both mandatory
    post-save checks passed; only CommunityMech:000401 reviewed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000401
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000401
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    valid labels do not authenticate source strain grounding.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000401
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-strict kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-06/000401/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    valid labels do not authenticate source strain grounding.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000401
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-terms kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    valid labels do not authenticate source strain grounding.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000401
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    valid labels do not authenticate source strain grounding.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000401
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    valid labels do not authenticate source strain grounding.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000401
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-history history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    valid labels do not authenticate source strain grounding.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000401
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    valid labels do not authenticate source strain grounding.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000401
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-references-explained kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Seven focused target/history checks plus one corpus cache-filename preflight;
    valid labels do not authenticate source strain grounding.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 06 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; target-native structure has no issue.
  target_ids:
  - CommunityMech:000401
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
  - CommunityMech:000401
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
  name: Primary publication and strain authority
  status: passed
  required: true
  summary: Direct metadata/full text and JCM/OAK identities were verified, revealing
    the current A2-165 nomenclature mismatch.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - pubmed
  - crossref
  - methods
  - catalogues
  - strain-authority
- check_id: scientific-source
  name: Full primary scientific assessment
  status: passed
  required: true
  summary: Complete main text, four main figures and the full Supplementary S1 were
    inspected with experimental limits preserved.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - source-scope
  - independent-source
  - supplement
- check_id: cross-mech
  name: Encoded medium/ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech identifier is encoded; exact recipe
    equivalence was not inferred.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - record
  - resources
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: No runnable adapter was available in the owned runtime.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  locator: 'Whole record: exact two-strain model, two nodes and no arrows'
  summary: The experiment and strains are identifiable; category, current taxonomic
    grounding and one functional-role attribution require correction.
  support: supports
  accessed_at: '2026-10-21T10:59:53.223180Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42655156&retmode=xml
  locator: Article-level metadata
  summary: PubMed verifies PMID, DOI, title and abstract.
  support: supports
  accessed_at: '2026-10-21T10:55:35.402592Z'
  snapshot_sha256: 6e79683213ef0c5254dba123b5b1b1728afd00e49bd8b93ce2bc9c275ed0b7e8
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.3390/microorganisms14081812
  locator: Article-level metadata
  summary: Crossref verifies the DOI/title and publisher identity.
  support: supports
  accessed_at: '2026-10-21T10:55:35.454629Z'
  snapshot_sha256: 7e5fe42277634757c3787f44565c9113221e8080c9fde137992bb753d096a451
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42655156&format=json&resultType=core
  locator: Article-level metadata
  summary: Europe PMC verifies the article metadata, PMC identifier and open full-text
    route.
  support: supports
  accessed_at: '2026-10-21T10:55:35.888626Z'
  snapshot_sha256: 89aca0c0f36f41ed65ee9fe605ac4b07d26eda63c17ab164320124fcd92f703f
- evidence_id: methods
  kind: primary_source
  reference: PMID:42655156
  locator: 'Fresh XML sec2dot1–sec2dot5: strains, growth, qPCR, acids and statistics'
  summary: Methods establish the exact JCM strains, 48-well anaerobic YCFA− experiment
    and distinct growth, qPCR and acid-concentration measurements.
  support: supports
  accessed_at: '2026-10-21T10:59:53.223474Z'
  quote: A2-165 (JCM31915)
  snapshot_sha256: c5b4d94fcd98543be47d7eb623a69180ae15cc98dbe1a3b1ad772818f65d421e
- evidence_id: peak
  kind: primary_source
  reference: PMID:42655156
  locator: Fresh XML sec3dot3 and sec5; Figure 3d
  summary: The tested 10:90 substrate ratio gives the maximal butyrate endpoint, distinct
    from the conditions maximizing total OD600.
  support: supports
  accessed_at: '2026-10-21T10:59:53.223561Z'
  quote: butyrate production was highest at 10% 2′-FL and 90% FOS
  snapshot_sha256: c5b4d94fcd98543be47d7eb623a69180ae15cc98dbe1a3b1ad772818f65d421e
- evidence_id: transfer
  kind: primary_source
  reference: PMID:42655156
  locator: 'Fresh XML sec4: acetate interpretation and five explicit limitations'
  summary: The authors propose a bifidobacterial contribution while acknowledging
    unmeasured flux, culture pH and residual substrates; they do not establish reciprocal
    uptake by B. bifidum.
  support: supports
  accessed_at: '2026-10-21T10:59:53.223645Z'
  quote: may have contributed
  snapshot_sha256: c5b4d94fcd98543be47d7eb623a69180ae15cc98dbe1a3b1ad772818f65d421e
- evidence_id: mono
  kind: primary_source
  reference: PMID:42655156
  locator: Fresh XML sec3dot1–sec3dot2 and Figures1–2
  summary: Monoculture substrate responses and acid endpoints support complementary
    substrate use; donor secretion alone does not establish a recipient functional
    role.
  support: supports
  accessed_at: '2026-10-21T10:59:53.223728Z'
  snapshot_sha256: c5b4d94fcd98543be47d7eb623a69180ae15cc98dbe1a3b1ad772818f65d421e
- evidence_id: figure-1
  kind: primary_source
  reference: PMID:42655156
  locator: 'figure-1.body: all panels and caption inspected'
  summary: Faecalibacterium monoculture responds to FOS-containing conditions; endpoints
    remain concentrations and OD.
  support: supports
  accessed_at: '2026-10-21T10:59:53.223791Z'
  snapshot_sha256: e46a66bf27563bda2f8edb356d09102fd4eaf97528228c667517c0ee018d2448
- evidence_id: figure-2
  kind: primary_source
  reference: PMID:42655156
  locator: 'figure-2.body: all panels and caption inspected'
  summary: B. bifidum responds to increasing 2′-FL with lactate/acetate accumulation
    and no detected butyrate.
  support: supports
  accessed_at: '2026-10-21T10:59:53.223857Z'
  snapshot_sha256: 6cf48baf52a11315933c97e6dd6096ed2828ebde0810851682e17d7197863937
- evidence_id: figure-3
  kind: primary_source
  reference: PMID:42655156
  locator: 'figure-3.body: all panels and caption inspected'
  summary: The 10% 2′-FL butyrate bar has a distinct significance letter; OD and other
    acid patterns differ.
  support: supports
  accessed_at: '2026-10-21T10:59:53.223919Z'
  snapshot_sha256: 054d2ca9f5791622e172e859ce08157094e70a1d5de298db27b38163a74bd093
- evidence_id: figure-4
  kind: primary_source
  reference: PMID:42655156
  locator: 'figure-4.body: all panels and caption inspected'
  summary: Relative qPCR composition shifts with substrate ratio; it is not a viable-cell
    count or donor-resolved flux.
  support: supports
  accessed_at: '2026-10-21T10:59:53.223992Z'
  snapshot_sha256: 8810a3e762e33beceaa06a42389b2a2da573d6bb421783ab1de631cb39a6d2dd
- evidence_id: supplement
  kind: primary_source
  reference: PMID:42655156
  locator: 'Supplementary Figure S1: entire one-page PDF and pixels'
  summary: Estimated genome-copy profiles provide an additional abundance measure;
    they do not demonstrate viable abundance, acetate transfer or the cause of the
    butyrate peak.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224387Z'
  snapshot_sha256: 64dda1580ce88954d8a0c636014281b14542004e81cbc69abf10e0b7b27151c0
- evidence_id: catalogues
  kind: authority
  reference: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=31915; https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=1254
  locator: 'root-catalogue-web.json: JCM31915 lines4–35, JCM1254 lines4–31 and May
    2022 announcement lines61–95'
  summary: JCM identifies A2-165/JCM31915/DSM17677 as F. duncaniae after an explicit
    name change; JCM1254/DSM20082 remains B. bifidum.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224456Z'
  snapshot_sha256: eeba4f79434bd45610fd37f45b35b719d3acc61baf240da1eaed332840a3bf6d
- evidence_id: strain-authority
  kind: authority
  reference: NCBITaxon:411483; NCBITaxon:853; NCBITaxon:398514
  locator: 'jcm-strain-authority.json: canonical labels, ranks and asserted parent
    chains'
  summary: 411483 is species F. duncaniae, separate from species 853 F. prausnitzii;
    strain 398514 belongs to species 1681 B. bifidum.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224500Z'
  snapshot_sha256: 9c0b5fb07c3afe0783fc3ac4aa37c0d68e46405e9be2767df530b05259c3f586
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, CHEBI and GO
  locator: 'ontology-authority.json: eight encoded pairs across eighteen occurrences'
  summary: Current ID/label strings match authority labels; that lexical match does
    not make species 853 correct for the specifically named A2-165 culture.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224582Z'
  snapshot_sha256: 8131183f971a6af4c1f75c463e070c5c808124dfa26a9d9a259710a76bbbcac9
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: CommunityCategoryEnum.DIET; FunctionalRoleEnum.CROSS_FEEDER and PRIMARY_DEGRADER
  summary: DIET means direct interspecies electron transfer; CROSS_FEEDER denotes
    consumption of another taxon’s metabolites; substrate degradation and metabolite
    supply are distinct roles.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224584Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  locator: snippet-audit.json
  summary: All 31 snippets match the fresh full XML and appended primary cache; main-text
    scope is distinct from abstract-only comparison.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224653Z'
  snapshot_sha256: 54349cd2f4765d57f334ce1e323acbe6a9c059580ee4c773876761354b88568b
- evidence_id: history
  kind: record_content
  reference: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  locator: provenance-audit.json
  summary: Three histories and the exact graph-only row preserve prior repairs; current
    issue 1256 explicitly includes the A2-165 taxonomy follow-up.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224702Z'
  snapshot_sha256: e01ecf73e466354fbdf12803c9755d3bc0becc4e224fddd10bbc127c1f3c8566
- evidence_id: resources
  kind: validation
  reference: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  locator: dataset-verification.json
  summary: Data Availability points to article/SI and further inquiry without an accession;
    catalogue genomes are separate identity resources.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224744Z'
  snapshot_sha256: 1c7f25e7c39e87d61abe8e135809832e31cd44a35291b6ed2fee509086711814
- evidence_id: native-target
  kind: validation
  reference: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  locator: support-audit.json
  summary: The target network is COMPLETE with two nodes, no arrows and six node evidence
    items; mechanical completeness does not validate roles or taxonomy.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224786Z'
  snapshot_sha256: 4e72f9cf259e2b83c88b668bab8cc75f00e7624a7ced7c32ce56ddede85bf58f
- evidence_id: source-scope
  kind: validation
  reference: PMID:42655156
  locator: source-audit.json
  summary: Complete scientific main, all four figures and Supplementary S1 were inspected;
    no raw-data or genome reanalysis was performed.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224825Z'
  snapshot_sha256: 8f894f70e331f2e303660b38aec2ad3ddcea7184882e7c1fcc95add4d0dfc059
- evidence_id: independent-source
  kind: validation
  reference: PMID:42655156
  locator: root-independent-source-audit.json
  summary: Independent source assessment supplies a separate check of the study, current
    strain identity and bounded findings.
  support: context_only
  accessed_at: '2026-10-21T10:59:53.224888Z'
  snapshot_sha256: c4bcdb9328f4f1369081598d7a1790c9c1c3aa138995140e172c2ab122dd40fa
- evidence_id: search
  kind: search
  reference: Owned maintained roots
  locator: 'local-search.json: ignored-inclusive bounded searches'
  summary: Recorded searches bound reusable identity/resource discovery without asserting
    global absence.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224933Z'
  snapshot_sha256: 43a7ed133ebb2e79b56cb7072b2f5d9b2aa51d349b904dc01b97cb547623cd9e
  search_scope: Ignored-inclusive maintained community, isolate and reusable-taxon
    roots; bounded data/mapping discovery.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: 'adapter-check.json: same-runtime batch 06 discovery reuse'
  summary: No runnable adapter was available in the owned runtime; no external runner
    or paid provider was used.
  support: supports
  accessed_at: '2026-10-21T10:59:53.224991Z'
  snapshot_sha256: b6e96ba7211accd230a6c6a0ac4fea59fda8be6741b6dc2a75659da49110785a
  search_scope: Reused recorded fresh batch 06 PATH/venv/module and ignored-inclusive
    discovery.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  locator: Actual execution 2026-10-21T10:55:51.940838+00:00 to 2026-10-21T10:55:52.751254+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T10:55:52.751254Z'
  snapshot_sha256: 6ccd3196eaa4388f7e49d835a5c97a6afde3879ce79a65bacca32352b1514c06
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-strict kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    --out /private/tmp/cm-review-session/batch-06/000401/strict-report.tsv
  locator: Actual execution 2026-10-21T10:55:51.940990+00:00 to 2026-10-21T10:55:54.185997+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T10:55:54.185997Z'
  snapshot_sha256: d65811f58e3d7b56716faadfe0a3e50ebc6d77f2969ef2e98c665290b5a5aef5
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-terms kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  locator: Actual execution 2026-10-21T10:55:51.941087+00:00 to 2026-10-21T10:55:53.798916+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T10:55:53.798916Z'
  snapshot_sha256: fd84764a190fe495e653ffe69de466a35059dbe69e9a21f7697df80e88e90d58
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  locator: Actual execution 2026-10-21T10:55:52.751504+00:00 to 2026-10-21T10:55:52.837900+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T10:55:52.837900Z'
  snapshot_sha256: b9e91cacc32cb160097118a052cf0e168fa4e9ef9d30e58dc4fe13b5b8bda5e2
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  locator: Actual execution 2026-10-21T10:55:52.840862+00:00 to 2026-10-21T10:55:54.216505+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T10:55:54.216505Z'
  snapshot_sha256: e5cdc486300b75591b26567c64a4007e07ac828937e4b97554e5541404566393
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-history history/records/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture
  locator: Actual execution 2026-10-21T10:55:53.799268+00:00 to 2026-10-21T10:55:54.516212+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T10:55:54.516212Z'
  snapshot_sha256: 59e7160e7dafd132f7b8ec1afa09d8631b9f218f376a3fab3c3429873279a43a
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T10:55:54.516782+00:00 to 2026-10-21T10:55:54.580601+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T10:55:54.580601Z'
  snapshot_sha256: cca31a002050a4738ae291af240543b4ae3e26c69511513525a215a22a55bb6d
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-06/src
    just --no-dotenv validate-references-explained kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  locator: Actual execution 2026-10-21T10:55:54.590695+00:00 to 2026-10-21T10:55:55.651862+00:00
  summary: Target reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T10:55:55.651862Z'
  snapshot_sha256: 9034a2a8ca69828458277bc72b3b686aae7c390e44367cf2d6bbb22a1db9a5c7
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
  topic: Exact model and strain provenance
  outcome: concern
  summary: The experiment is resolved, but its A2-165 current species grounding must
    be reconciled with the paper’s legacy name.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - record
  - methods
  - catalogues
  - strain-authority
  dimensions:
  - name: community_scope
    value: Defined two-strain in-vitro prebiotic model
    definition: The 10:90 optimum is specific to the tested batch assay and is not
      an established adult-gut or clinical optimum.
    evidence_ids:
    - methods
    - peak
    - transfer
  - name: source_strain
    value: B. bifidum JCM1254 and A2-165/JCM31915
    definition: Retain exact strains and the paper’s historical name while grounding
      A2-165 to current F. duncaniae.
    evidence_ids:
    - methods
    - catalogues
    - strain-authority
  - name: environment
    value: Laboratory culture modeling adult intestinal metabolism
    definition: Laboratory ENVO and explicitly modeled intestine are distinct; the
      cultures are not an intact gut community.
    evidence_ids:
    - record
    - ontology
    - methods
  - name: medium
    value: Sugar- and volatile-fatty-acid-free YCFA with varied carbohydrate
    definition: The culture contains basal medium constituents; its 0.5% added 2′-FL/FOS
      series is not a chemically carbon-free formulation.
    evidence_ids:
    - methods
  - name: experimental_setting
    value: Anaerobic 48-well batch incubation at 37 °C for 24 h
    definition: OD-standardized inocula, monoculture controls and triplicate endpoint
      assays support a bounded formulation comparison.
    evidence_ids:
    - methods
  - name: evidence_tier
    value: Measured endpoints plus explicitly inferred acetate contribution
    definition: OD, acid pools and qPCR estimates do not establish direct transfer,
      metabolic flux or viable counts; no arrows are encoded.
    evidence_ids:
    - peak
    - transfer
    - figure-4
    - supplement
  - name: grounding_status
    value: Eight matched labels with one strain-to-species mismatch
    definition: Current nomenclature correction must propagate through the graph;
      no GTDB assignment follows automatically from a catalogue name.
    evidence_ids:
    - ontology
    - strain-authority
- assessment_id: taxon-bifidum
  area: grounding
  topic: 'taxonomy[0]: B. bifidum JCM1254'
  outcome: concern
  summary: Species and collection identity are supported, but the recipient CROSS_FEEDER
    role lacks source support.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - methods
  - catalogues
  - strain-authority
  - mono
  - transfer
  - schema
  details: The substrate-response evidence supports degradation of the supplied oligosaccharide
    and a donor interpretation. The source does not show B. bifidum consuming Faecalibacterium
    metabolites. Its existing species 1681 ID is compatible with the named strain;
    optional strain 398514 enrichment is not required to fix a wrong identity.
- assessment_id: taxon-faecalibacterium
  area: grounding
  topic: 'taxonomy[1]: A2-165/JCM31915'
  outcome: concern
  summary: The named culture is current F. duncaniae, not species 853 F. prausnitzii.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - methods
  - catalogues
  - strain-authority
  - ontology
  details: This is a current grounding correction for the same biological isolate,
    not a different experiment or evidence fabrication. Preserve A2-165/JCM31915 and
    legacy source quotations; use verified current nomenclature consistently in taxonomy
    and graph participants. FOS utilization supports the substrate-degrader role;
    acetate uptake remains author-inferred and should retain its qualification. Catalogue
    identity alone does not resolve GTDB.
- assessment_id: category
  area: evidence
  topic: 'community_category: DIET'
  outcome: concern
  summary: A dietary-substrate experiment does not establish direct interspecies electron
    transfer.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - schema
  - methods
  - transfer
  details: No direct electrical coupling is measured or proposed in the inspected
    study. Choose a schema-valid category matching the verified gut-culture experiment,
    with rationale; do not infer a replacement category solely from the word diet
    or force a syntrophy classification.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: ratio-dependent butyrate peak'
  outcome: supported
  summary: Retain the measured community-level endpoint with its present assay and
    mechanism limits.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - peak
  - figure-3
  - methods
  - transfer
  details: Participants are JCM1254 and A2-165, whose current taxon annotation needs
    the separate correction. The node has no donor-to-recipient direction or downstream
    arrow. Its 10:90 maximum, growth/output distinction, fixed added carbohydrate
    and 24-hour endpoint are supported; Figure 3d separates the peak statistically.
    Preserve its warning against an in-vivo optimum or donor-resolved transfer claim.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: putative JCM1254 → A2-165 acetate support'
  outcome: supported
  summary: Retain the explicitly PARTIAL cross-feeding interpretation, distinct from
    the measured acid endpoints.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - transfer
  - mono
  - peak
  - figure-4
  - supplement
  details: The proposed donor is B. bifidum and recipient is A2-165/current F. duncaniae;
    acetate is the only encoded pairwise metabolite. Main Discussion proposes this
    direction while acknowledging absent flux, pH and residual-substrate measurements.
    qPCR and S1 are abundance estimates, not viable counts. Keep zero downstream arrows
    and do not convert this interpretation into demonstrated acetate transfer.
- assessment_id: cultivation
  area: completeness
  topic: Medium, design, factors and batch setup
  outcome: supported
  summary: The recorded perturbation, incubation and derived working volume agree
    with the focal Methods.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - methods
  - record
  details: Monocultures receive one 8 µL standardized suspension; cocultures receive
    two into 800 µL medium, giving the explicitly modeled 816 µL. This arithmetic
    does not establish equal cell counts or biomass. Keep initial glucose-YCFA revival
    distinct from sugar/VFA-free YCFA− assays. Culture pH is unmeasured; chromatographic
    mobile-phase pH and column temperature are analytical settings, not culture conditions.
    Basal recipe expansion would require the cited formulation; no catalogue protocol
    is substituted.
- assessment_id: ingredients
  area: grounding
  topic: 2′-FL, FOS, acetate, butyrate and GO scope
  outcome: supported
  summary: The ingredients and broad carbohydrate-process grounding fit the bounded
    experiment.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - ontology
  - methods
  - mono
  - peak
  - transfer
  details: FOS is the source preparation of kestose, nystose and fructofuranosylnystose,
    not an automatically interchangeable single compound. Acetate is measured and
    only a proposed contributor to butyrate; the ingredient prose preserves that distinction.
    No metal/REE phenotype is asserted. The broad GO label is valid without proving
    a unique enzymatic pathway.
- assessment_id: provenance
  area: provenance
  topic: Source excerpts, prior repairs and resources
  outcome: supported
  summary: Exact snippets and current history support the existing graph qualifications
    while leaving non-graph taxonomy actionable.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - snippets
  - history
  - resources
  - source-scope
  details: Issues 991–994 and 1254 are closed and their repairs remain present; open
    1256 names the current strain-taxonomy question. The publication links resolve.
    No absent external dataset is inferred when Data Availability points to the paper/SI;
    catalogue genome links are not newly generated data from this experiment.
- assessment_id: validation
  area: schema
  topic: Native checks and current source assessment
  outcome: supported
  summary: All eight native checks pass; the source audit identifies semantic issues
    beyond those gates.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - strain-authority
  - source-scope
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality
  outcome: supported
  summary: Mechanical metrics remain distinct from experimental correctness and taxonomic
    attribution.
  target_ids:
  - CommunityMech:000401
  evidence_ids:
  - native-target
  - record
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata including all roles +5 environment +10
      at least 3 factors +10 at least 3 nodes +5 resources +10 media +5 datasets +5
      node metabolites). 50+5+0+0+5+10+0+5=75.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50P1-10P2-2P3+20 min(mean node evidence/2,1)+15 if native
      COMPLETE,0,100). P1=0, P2=2, P3=1, P4=0; 6 evidence items/2 nodes=3 gives 20
      evidence bonus; 100-20-2+20+15=113 before capping.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count.
  - name: P2
    value: 2
    unit: findings
    definition: Observed native severity count.
  - name: P3
    value: 1
    unit: findings
    definition: Observed native severity count.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count.
findings:
- finding_id: a2-165-current-taxon
  issue_key: cm-000401-a2-165-current-taxon
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: current species grounding attaches the known isolate
    and graph endpoints to a different species concept; the experiment and strain
    identity remain resolved.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Reconcile A2-165 with current F. duncaniae grounding
  description: The exact JCM culture is verified as F. duncaniae, while taxonomy and
    graph participants use the distinct current F. prausnitzii species ID.
  target_ids:
  - CommunityMech:000401
  field_paths:
  - taxonomy[1].taxon_term
  - ecological_interactions[0].participating_taxa[1]
  - ecological_interactions[1].target_taxon
  - description
  evidence_ids:
  - methods
  - catalogues
  - strain-authority
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    role: canonical_record
- finding_id: diet-category
  issue_key: cm-000401-diet-category
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: the category encodes an unsupported ecological
    mechanism and misclassifies the entire record.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Replace the unsupported electron-transfer category
  description: The record uses DIET for a dietary-substrate model even though the
    schema defines it as direct interspecies electron transfer and the source supplies
    no such evidence.
  target_ids:
  - CommunityMech:000401
  field_paths:
  - community_category
  evidence_ids:
  - schema
  - methods
  - transfer
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    role: canonical_record
- finding_id: donor-recipient-role
  issue_key: cm-000401-donor-recipient-role
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: one local functional-role attribution needs narrowing;
    the existing graph already encodes the donor-to-recipient direction cautiously.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Qualify the B. bifidum recipient-role assignment
  description: The source supports substrate use and a proposed metabolite-donor role,
    but not B. bifidum uptake of metabolites from its partner.
  target_ids:
  - CommunityMech:000401
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].evidence
  evidence_ids:
  - schema
  - mono
  - transfer
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    role: canonical_record
actions:
- action_id: repair-a2-165-current-taxon
  description: Reconcile A2-165 with current F. duncaniae grounding.
  finding_ids:
  - a2-165-current-taxon
  target_ids:
  - CommunityMech:000401
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Ground A2-165/JCM31915 to verified NCBITaxon:411483 Faecalibacterium duncaniae
    consistently in taxonomy and graph participants, retaining the exact culture identity.
  - Preserve literal source quotations and explain that the paper uses the legacy
    F. prausnitzii name; do not rewrite historical evidence or imply a different experimental
    isolate.
  - Keep source naming, current nomenclature and exact strain distinct in prose and
    notes; reassess GTDB only with an applicable verified mapping, without forcing
    an assignment.
  - Rerun term, GTDB/domain and network consistency checks after a separately authorized
    correction.
- action_id: repair-diet-category
  description: Replace the unsupported electron-transfer category.
  finding_ids:
  - diet-category
  target_ids:
  - CommunityMech:000401
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Select a schema-valid category justified by the verified experiment, with an explicit
    rationale; OTHER is preferable to an unsupported mechanistic classification where
    no narrower category fits.
  - Do not reinterpret DIET as dietary supplementation or infer electron transfer
    from fermentation/metabolite exchange.
  - Preserve the bounded carbohydrate-ratio and putative acetate-transfer graph; category
    correction does not require new nodes or arrows.
- action_id: repair-donor-recipient-role
  description: Qualify the B. bifidum recipient-role assignment.
  finding_ids:
  - donor-recipient-role
  target_ids:
  - CommunityMech:000401
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Remove or source-qualify B. bifidum CROSS_FEEDER under its consumer definition;
    donor secretion alone is insufficient.
  - Attach role-specific substrate/fermentation evidence to retained roles, without
    inventing reverse transfer or a new replacement role.
  - Retain Faecalibacterium recipient support as author-inferred and preserve the
    explicit unresolved flux, pH and substrate limitations.
- action_id: preserve-qualified-model
  description: Preserve the two qualified nodes, zero arrows and experimental limitations
    during separately authorized follow-up.
  finding_ids:
  - a2-165-current-taxon
  - diet-category
  - donor-recipient-role
  target_ids:
  - CommunityMech:000401
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Do not convert acid pools, relative qPCR or estimated copies into donor-resolved
    flux, viable abundance or an in-vivo optimal formulation.
  - Do not import catalogue growth conditions or reference-genome records as the focal
    study’s experimental data.
  - Preserve append-only history and rerun schema, strict, term, reference, history
    and target/corpus network checks after authorized curation.
limitations:
- No raw data, statistical analysis, genome sequence, isotope tracing or biochemical
  flux was reanalyzed. Figure inspection verifies reported patterns and scope, not
  a new quantitative reconstruction.
- Only one strain pair and a 24-hour batch endpoint are studied; pH, residual substrate
  and direct flux are explicitly unmeasured. The optimal tested ratio is not an established
  in-vivo optimum.
- Current catalogue identity does not alter literal source nomenclature, verify historical
  GTDB release statistics or authorize an inferred new GTDB mapping.
- The basal YCFA recipe cited to an earlier reference was not independently reconstructed;
  no CultureMech formulation or catalogue-maintenance transfer is certified.
- Data Availability points to article/SI and author inquiry; no unreported archive
  accession or dataset omission is inferred. Catalogue genome links were not fetched
  or analyzed.
notes:
- No canonical, cache, history or generated file changed.
- All 25 repository inputs were pinned before assessment and rechecked.
- Fifteen quoted words from the focal paper; catalogue/reclassification material is
  paraphrased.
- Native quality 100 is capped from 113; source findings remain actionable.
tags:
- record-review
- gut-coculture
- taxonomy
- prebiotic
- batch-06
```
