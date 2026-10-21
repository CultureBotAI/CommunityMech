# Bacillus G12-Y4-X25 tobacco SynCom: partial record review

- Review: 20261021T085942Z-bacillus-tobacco-syncom-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T08:54:08.307799Z
- Finished UTC: 2026-10-21T08:59:42.479935Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Partial review: complete critical source text and figures remain unavailable. Two minor findings concern local role evidence and experiment-specific cultivation/environment context. All five nodes and the absence of arrows were assessed; existing mechanistic limits remain appropriate. Seven focused gates and cache preflight pass; two host-target diagnostic warnings do not make tobacco a missing member.

## Scope And Provenance

Whole target reviewed using fresh abstract/metadata, complete selected-passage cache and indexed primary data statement/captions. Five nodes and no arrows assessed; full main Methods/Results and figure pixels, supplementary DOCX and raw datasets remain unreviewed.

Selection: Next assigned maintained path after CommunityMech:000120 in batch05; one resolved three-strain SynCom.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c6e5a9b9af2d05e12eaafb2555a53f3a079268f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000373 | kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml | maintained | Bacillus G12-Y4-X25 Tobacco Biocontrol SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000373 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000373 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000373 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000373 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000373 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000373 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000373 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000373 | Target reference validation passed against the pinned selected-passage cache. |
| audit-network | failed | True | CommunityMech:000373 | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1, including two external-host warnings for this target. |
| check-network-quality | failed | True | CommunityMech:000373 | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1, including two external-host warnings for this target. |
| Publication identity and accessible-source comparison | passed | True | CommunityMech:000373 | Fresh article identifiers and abstract agree with the record; selected cache passages were reviewed within their provenance scope. |
| Complete critical Methods, Results and figures | unavailable | True | CommunityMech:000373 | Complete main text and supplementary DOCX/figures were not recovered through the inspected public routes. |
| Encoded dataset accession and release boundary | not_applicable | False | CommunityMech:000373 | No accession is encoded; the public statement reports temporary sequencing restrictions and future deposition. |
| Encoded medium and ingredient-Mech links | not_applicable | False | CommunityMech:000373 | No CultureMech or MediaIngredientMech ID is encoded or uniquely inferred from the LB name. |
| Optional structured source adapter | unavailable | False | CommunityMech:000373 | Same-runtime batch05 discovery is reused; no external runner or strain-module query was executed. |

## Scientific And Domain Assessments

### Three-strain inoculant and plant-pathogen assay scope

identity: supported. Targets: CommunityMech:000373.

The source resolves G12/Y4/X25 and separates inoculum composition, host/pathogen targets and experimental endpoints.

### All three member roles, source strains and prominence

grounding: concern. Targets: CommunityMech:000373.

Identities, habitats and antagonist roles are supported, but nearest taxonomy snippets establish only identity/source.

Attach the explicit pathogen-specific antagonism evidence locally. DOMINANT may describe co-equal formulation members; it is not a percentage defect and does not certify abundance or persistence in field soil.

### ecological_interactions[0]: Mild-Inhibition Three-Strain SynCom Compatibility

graph: supported. Targets: CommunityMech:000373.

Reciprocal directional inhibition supports the existing COMPETITION label at plate-assay scope.

Participants are G12, Y4, X25 with each pair tested in both directions. Values below 25% define the source mild-inhibition class; this does not prove resource competition, reciprocal benefit or stable coexistence. Complete plate Methods/figures remain unreviewed.

### ecological_interactions[1]: SynCom Indole-3-Acetic Acid Enhancement

graph: supported. Targets: CommunityMech:000373.

The node preserves a per-volume colorimetric increase without claiming exchange or IAA-mediated plant protection.

Direction is three-strain co-culture versus constituent monocultures to measured supernatant output. The separate 25 C/48 h co-cultivation growth measurement is not assumed to define the IAA assay conditions. GO IAA biosynthesis and CHEBI identity are compatible subject annotations; no member-resolved flux or selective mediation is certified.

### ecological_interactions[2]: Tobacco FO/PN Glasshouse Disease Suppression

graph: supported. Targets: CommunityMech:000373.

Disease-index suppression is corroborated; the record does not convert it into a specific hormonal pathway.

The G12/Y4/X25 inoculant treats He Luo No. 1 tobacco challenged with F. oxysporum and P. nicotianae, under preventive and curative timing. Source defense-enzyme responses support broad protective-response context but do not distinguish every direct/host-mediated contribution.

### ecological_interactions[3]: Tobacco Root Activity Improvement

graph: supported. Targets: CommunityMech:000373.

The TTC-based endpoint is correctly limited to root metabolic activity.

Direction is SynCom treatment under FO/PN stress to tobacco root activity versus single-strain treatments. NCBITaxon:4097 is the external plant target, not a missing community member; the record correctly avoids direct biomass-growth and reciprocal microbial-benefit claims.

### ecological_interactions[4]: Two-Site Field Disease Suppression and Yield Increase

graph: supported. Targets: CommunityMech:000373.

Two-site outcomes retain the source estimated-yield and natural-disease scope.

G12/Y4/X25 is applied twice to tobacco under natural co-occurring root-rot/black-shank pressure. The target is host disease/estimated yield versus source controls; neither whole-plot harvested yield nor durable microbiome change is established. Figures remain uninspected.

### downstream inventory

graph: not_applicable. Targets: CommunityMech:000373.

No downstream arrows are encoded, so no additional mechanistic direction is certified.

### LB, glasshouse and field context

completeness: concern. Targets: CommunityMech:000373.

The record accurately captures 30 C stock preparation but omits the separate assay and plant-setting conditions present in selected cached Methods.

The environmental factor duplicates assembly strategy. Place source-backed conditions with their experiment rather than assigning the 30 C preparation temperature to all outcomes. Current full Methods/supplement access remains unavailable.

### IAA output and biological scope

grounding: supported. Targets: CommunityMech:000373.

The IAA entry is a measured potential growth-promoting output rather than a verified mediator of disease protection.

No metal-processing phenotype or specific additional metabolite is established by the accessible evidence. Names alone do not justify additional pathways or genes.

### Source/cache/history and resource boundaries

evidence: supported. Targets: CommunityMech:000373.

Fresh abstract identity is verified, while exact snippets remain cache-supported and complete article access is unresolved.

The record discussion already states that its cache is selected text. The PMID resource resolves; free-to-read PMC metadata does not establish open licensing or successful full-body retrieval. Source sequencing restrictions are retained without invented accession gaps.

### Native checks and incomplete scientific source assessment

schema: concern. Targets: CommunityMech:000373.

Seven focused gates and cache preflight pass; two host-target warnings and required full-source unavailability remain explicit.

### Native completeness and quality within partial review

completeness: supported. Targets: CommunityMech:000373.

Completeness is 85 and capped quality 100; neither score substitutes for the unavailable full-source assessment.

## Findings

### role-evidence-placement: Taxonomy role claims lack their narrow source evidence

minor / open / confirmed; issue key: cm-000373-role-evidence-placement.

Each PATHOGEN_ANTAGONIST entry cites taxonomic identity and isolation habitat, although the fresh abstract separately provides the relevant pathogen-specific prior-study attribution.

### cultivation-context: Preparation and outcome-assay contexts are incompletely represented

minor / open / confirmed; issue key: cm-000373-cultivation-context.

The LB block captures 30 C preparation but not the distinct 25 C/48 h co-cultivation assay; cached glasshouse and field conditions are also absent from structured context, while the environmental factor repeats the assembly design.

## Recommended Actions And Acceptance Checks

### fix-role-evidence-placement

Attach source-attributed antagonism evidence to each corresponding taxon role.

- Keep G12 linked to F. oxysporum and Y4/X25 to P. nicotianae, preserving attribution to the prior studies summarized by this article.
- Retain current species/strain/habitat evidence; do not generalize every strain to every pathogen or invent direct mechanisms.
- If original prior-study protocols are later cited, inspect them before adding stronger strain-specific claims.
- Run references, schema and strict validation after separately authorized curation.

### fix-cultivation-context

Treat the selected cached Methods as candidate context; independently verify complete primary Methods before adding numerical cultivation details.

- Verify complete main Methods before applying the numerical context expansions below; preserve the current correctly scoped preparation block until then.
- Keep 30 C/180 rpm inoculum preparation separate from 25 C/180 rpm/48 h co-cultivation measurement.
- Represent glasshouse 25 +/- 2 C, 12 h:12 h light/dark, 70-80% RH and 21-day experiments separately from field cultivation.
- Preserve field 10 mL per-plant root irrigation and two events seven days apart without extrapolating glasshouse conditions to field sites.
- Move duplicated assembly prose to engineering_design and use environmental fields for actual setting conditions.
- Do not fabricate LB formulation, exact CultureMech ID, assay inoculum details or unavailable field protocol information.
- Cite the selected-cache scope explicitly, then reassess against complete source Methods when accessible.

### complete-source-assessment

When authorized complete source text becomes available, review full assay/field Methods, all relevant figures and supplementary material, then issue a new immutable assessment.

- Verify detailed numeric comparisons and assay contexts against complete primary content while preserving current qualifiers.
- Do not convert transcriptomic associations, nonsignificant genus shifts or IAA output into hormone mediation or persistent colonization.
- Revisit sequencing-data release only when the source provides a real deposited accession.
- No purchase, author contact, canonical edit or status promotion is authorized by this review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; Entire target: three Bacillus strains, five nodes and no arrows | supports | The record separates microbial inoculant members from tobacco host/pathogens, source habitats and measured endpoints. |
| cache | PMID:42388034; references_cache/PMID_42388034.txt: complete cache, selected Methods/Results/Discussion | supports | The pinned cache contains selected primary passages despite its full-text separator. These support bounded assessment but are not independent verification of the complete main article. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42388034&amp;retmode=xml; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42388034&amp;retmode=xml | supports | Fresh article-level PubMed metadata verifies PMID 42388034, DOI 10.1002/ps.71069, PMC13569317 and the full abstract. |
| crossref | https://api.crossref.org/works/10.1002/ps.71069; https://api.crossref.org/works/10.1002/ps.71069 | supports | Fresh Crossref metadata verifies DOI/title and journal full-XML/PDF routes. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42388034&amp;format=json&amp;resultType=core; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42388034&amp;format=json&amp;resultType=core | supports | Fresh Europe PMC metadata links free PMC article routes but marks the record outside its open-access subset; current retrieval did not supply the body. |
| access | Public EPMC, PMC, BioC and Wiley routes; access-audit.json: individual request times, status, response and receipt hashes | context_only | XML returned 500 twice; HTML/PDF routes returned 403 or browser verification. PMC efetch supplied frontmatter only and BioC returned no result; none was counted as full text. |
| root-access | PMID:42388034; root-source-access.json: indexed primary abstract/data statement/captions and failed supplement retrieval | context_only | Independent public access supplied abstract, data availability and supplementary captions, but no complete main body, DOCX or figure pixels. |
| members | PMID:42388034; Fresh PubMed abstract; cached strain-source paragraph | supports | G12 is the tobacco-rhizosphere B. amyloliquefaciens isolate; Y4 and X25 are tobacco endophytes assigned to B. pumilus and B. velezensis. The abstract attributes prior F. oxysporum antagonism to G12 and P. nicotianae inhibition to Y4/X25. |
| compatibility | PMID:42388034; Cached pairwise-confrontation Results paragraph and Figure 1(A/B) reference; fresh abstract | supports | Six directional plate-inhibition values are below 25%; these support mild reciprocal antagonism under that assay without proving long-term coexistence. |
| iaa | PMID:42388034; Fresh PubMed abstract; cached Salkowski Results paragraph and Figure 1(D/E) reference | supports | The reported 11.57 +/- 0.24 mg/L output exceeds monocultures; the assay is colorimetric and per volume, without resolved metabolite exchange or demonstrated IAA-mediated protection. |
| glasshouse | PMID:42388034; Fresh PubMed abstract; cached glasshouse Methods and disease Results/Figure 4 reference | supports | Preventive and curative disease suppression is reported with defense-enzyme responses. The detailed 54.07-to-9.26 disease-index change is supported by selected cached Results, not independently read figure pixels. |
| root-activity | PMID:42388034; Fresh PubMed abstract; cached TTC/dehydrogenase Results and Figure 6 reference | supports | The detailed 20.27-45.38% preventive comparison is a root metabolic-activity endpoint, not direct biomass or reciprocal microbial fitness. |
| field | PMID:42388034; Fresh PubMed abstract; cached two-site field Methods/Discussion | supports | Field disease and yield effects are source-reported; yield is estimated from middle leaves rather than whole-plot harvested yield, and native-community abundance shifts were nonsignificant. |
| cultivation | PMID:42388034; Cached single-strain fermentation, co-cultivation, glasshouse and field Methods paragraphs | supports | Preparation uses 30 C/180 rpm, whereas co-cultivation measurement uses 25 C/180 rpm/48 h. Cached glasshouse conditions are 25 +/- 2 C, 12 h light, 70-80% RH and 21 days; field plants receive 10 mL twice, seven days apart. These contexts must remain separate. |
| limits | PMID:42388034; Cached Discussion paragraphs on colonization, microbiome sampling and future validation | supports | The source does not establish strain persistence, niche differentiation, hormonal mediation or long-term community stability. Endpoint genus-level shifts are not evidence of colonization; equal inoculation does not measure field dominance. |
| ontology | Local OAK NCBITaxon, ENVO, CHEBI and GO snapshots; Eleven unique ID/label pairs at fourteen occurrences | supports | All labels match. Species terms preserve isolate-name context, and broad defense/growth processes do not independently prove a specific hormonal mechanism. |
| schema | src/communitymech/schema/communitymech.yaml; InteractionTypeEnum.COMPETITION; FunctionalRoleEnum.PATHOGEN_ANTAGONIST; AbundanceEnum.DOMINANT; taxonomy host exclusion | supports | COMPETITION permits reciprocal negative effects without requiring resource depletion. DOMINANT is ordinal, and tobacco belongs as an external target rather than a microbial member. |
| snippets | kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; snippet-audit.json: eighteen occurrences | supports | All eighteen snippets match the selected-passage cache; none of those exact spans appears in the differently worded fresh abstract. Broad claims are corroborated, but full-text lexical freshness is unverified. |
| datasets | Publisher data availability and bounded accessible-source audit; dataset-verification.json; root-source-access.json | supports | The public statement describes temporary sequencing-data restrictions and future deposition, without a current accession. No arbitrary archive association or dataset-omission finding is made. |
| history | Two target history sidecars; 20261005-eleven-records-batch5.yaml; Target decision lines 531-575; live issues 1248 and 880 | supports | The prior hash matches. Issue 1248 is the closed graph repair; closed issue 880 concerned the already-present IAA process annotation, not a new repair claimed here. |
| search | Owned community/isolate/reusable-taxon roots; Ignored-inclusive bounded target, source and species lookup | supports | No reusable record authenticates these exact isolates; shared Bacillus species occurrences are not interchangeable source strains. |
| adapter | Optional kg-microbe-sources runner; Explicit same-batch05 runtime reuse of 000120 discovery at 08:47:38Z | supports | No callable owned-runtime adapter was available; the known external-checkout runner was not executed and no strain/module coverage was queried. |
| native-target | NetworkIntegrityAuditor().audit_community(target); support-audit.json: targeted API and native metrics | supports | The auditor reports two UNKNOWN_TARGET warnings for tobacco and marks INCOMPLETE. These are host-target limitations of the diagnostic, not evidence that tobacco should join the SynCom taxonomy. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; Actual execution 2026-10-21T08:54:24.561324+00:00 to 2026-10-21T08:54:25.311381+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-strict kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml --out /private/tmp/cm-review-session/batch-05/000373/strict-report.tsv; Actual execution 2026-10-21T08:54:24.561533+00:00 to 2026-10-21T08:54:26.930264+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-terms kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; Actual execution 2026-10-21T08:54:24.561638+00:00 to 2026-10-21T08:54:26.464400+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-gtdb kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; Actual execution 2026-10-21T08:54:25.311810+00:00 to 2026-10-21T08:54:25.397298+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; Actual execution 2026-10-21T08:54:25.397677+00:00 to 2026-10-21T08:54:27.017901+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-history history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom; Actual execution 2026-10-21T08:54:26.464685+00:00 to 2026-10-21T08:54:27.450444+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T08:54:27.451070+00:00 to 2026-10-21T08:54:27.519675+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-references-explained kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml; Actual execution 2026-10-21T08:54:27.519975+00:00 to 2026-10-21T08:54:29.383454+00:00 | supports | Target reference validation passed against the pinned selected-passage cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T08:44:47.720127+00:00 to 2026-10-21T08:45:04.195128+00:00 | supports | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1, including two external-host warnings for this target. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T08:44:47.737345+00:00 to 2026-10-21T08:45:04.925187+00:00 | supports | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1, including two external-host warnings for this target. |

## Limits And Additional Notes

- Required whole-source assessment is unavailable. EPMC XML failed twice; public HTML/PDF routes supplied 403, browser verification or frontmatter only, while BioC returned no result. No access-control bypass or paid retrieval was used.
- The cache contains selected passages, not complete full text. All 18 exact snippets match it, but none matches the differently worded fresh abstract verbatim; this is not a fabricated-snippet finding or independent full-text verification.
- The fresh abstract corroborates broad identity/antagonism, IAA, glasshouse disease/root and field yield outcomes. Detailed directional plate values, disease-index and root-activity comparisons remain supported through the provenance-marked cache only.
- Publisher supplementary captions were read by the independent reviewer, but no DOCX or main/supplementary figure pixels were recovered. Captions do not certify the underlying plots or complete protocols.
- Tobacco is an external host target under the current schema. Two native UNKNOWN_TARGET warnings are retained in the score with no network bonus, without adding the plant to microbial taxonomy or inventing graph edges.
- DOMINANT can describe co-equal formulation members; equal-volume inoculum, nonsignificant genus shifts and a single microbiome endpoint do not demonstrate persistent field dominance, resilience or colonization.
- Source sequencing data are temporarily restricted with future deposition described; no accession was inferred, no author contacted and no raw transcriptome/microbiome analysis performed.
- Historical GTDB statuses and X25 mapping counts/release were not recomputed; same-runtime optional adapter discovery was reused and the known external runner was not executed.
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 15 words for this publication; exact source spans are verified within fresh abstract or explicitly labeled selected cached Results.
- All 24 repository inputs were pinned before assessment and rechecked; quality 100 is capped from 106 and is not whole-source scientific certification.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T085942Z-bacillus-tobacco-syncom-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Bacillus G12-Y4-X25 tobacco SynCom: partial record review'
started_at: '2026-10-21T08:54:08.307799Z'
finished_at: '2026-10-21T08:59:42.479935Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Prior codex creation/graph review prevents person-level independence
    claims. Separate agents assessed available sources, ontology, native gates, snippets,
    provenance and metrics; canonical inputs remain unchanged.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: 'Partial review: complete critical source text and figures remain unavailable.
  Two minor findings concern local role evidence and experiment-specific cultivation/environment
  context. All five nodes and the absence of arrows were assessed; existing mechanistic
  limits remain appropriate. Seven focused gates and cache preflight pass; two host-target
  diagnostic warnings do not make tobacco a missing member.'
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
  - path: history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-09-14T042451Z-codex-bacillus-tobacco.yaml
    sha256: 5edbf58603e8088c5b05fabd4f028014cd0c76414cf477e622b1d5aba1d8d519
    role: context
  - path: history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom/2026-10-05T101150Z-codex-7933b3.yaml
    sha256: 1ee592e291879f3df8b0aae5f529d6b66e701f6c1d0ba9d784d2364a8a269d98
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    sha256: e0126b602878c9abada427f906334f6a059784e07b29c33b709c9a9549f0689f
    role: target
  - path: references_cache/PMID_42388034.txt
    sha256: 7c411b8884969706099963aa4cf8b7f6b1cda8810a8b38ca1dc392420d3dd393
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
- target_id: CommunityMech:000373
  path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  label: Bacillus G12-Y4-X25 Tobacco Biocontrol SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
scope:
  description: Whole target reviewed using fresh abstract/metadata, complete selected-passage
    cache and indexed primary data statement/captions. Five nodes and no arrows assessed;
    full main Methods/Results and figure pixels, supplementary DOCX and raw datasets
    remain unreviewed.
  selection: Next assigned maintained path after CommunityMech:000120 in batch05;
    one resolved three-strain SynCom.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000373
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000373
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
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
  - CommunityMech:000373
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-strict kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-05/000373/strict-report.tsv
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
  - CommunityMech:000373
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-terms kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
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
  - CommunityMech:000373
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
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
  - CommunityMech:000373
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
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
  - CommunityMech:000373
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-history history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom
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
  - CommunityMech:000373
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
  summary: Target reference validation passed against the pinned selected-passage
    cache.
  target_ids:
  - CommunityMech:000373
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-references-explained kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
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
    and exit 1, including two external-host warnings for this target.
  target_ids:
  - CommunityMech:000373
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  - schema
  scope_note: Reused fresh full-corpus batch05 execution, not a target-specific pass;
    host-target warnings do not authorize adding tobacco to microbial membership.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1, including two external-host warnings for this target.
  target_ids:
  - CommunityMech:000373
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  - schema
  scope_note: Reused fresh full-corpus batch05 execution, not a target-specific pass;
    host-target warnings do not authorize adding tobacco to microbial membership.
- check_id: publication-identity
  name: Publication identity and accessible-source comparison
  status: passed
  required: true
  summary: Fresh article identifiers and abstract agree with the record; selected
    cache passages were reviewed within their provenance scope.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - cache
  - snippets
- check_id: full-primary-source
  name: Complete critical Methods, Results and figures
  status: unavailable
  required: true
  summary: Complete main text and supplementary DOCX/figures were not recovered through
    the inspected public routes.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - access
  - root-access
  - cache
  scope_note: Fresh abstract plus selected cached Methods/Results/Discussion and indexed
    captions are not a completed whole-source review.
- check_id: source-data
  name: Encoded dataset accession and release boundary
  status: not_applicable
  required: false
  summary: No accession is encoded; the public statement reports temporary sequencing
    restrictions and future deposition.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - datasets
  - root-access
- check_id: cross-mech
  name: Encoded medium and ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech ID is encoded or uniquely inferred
    from the LB name.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - record
  - cultivation
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Same-runtime batch05 discovery is reused; no external runner or strain-module
    query was executed.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: 'Entire target: three Bacillus strains, five nodes and no arrows'
  summary: The record separates microbial inoculant members from tobacco host/pathogens,
    source habitats and measured endpoints.
  support: supports
  accessed_at: '2026-10-21T08:59:42.474991Z'
- evidence_id: cache
  kind: primary_source
  reference: PMID:42388034
  locator: 'references_cache/PMID_42388034.txt: complete cache, selected Methods/Results/Discussion'
  summary: The pinned cache contains selected primary passages despite its full-text
    separator. These support bounded assessment but are not independent verification
    of the complete main article.
  support: supports
  accessed_at: '2026-10-21T08:59:42.475124Z'
  snapshot_sha256: 7c411b8884969706099963aa4cf8b7f6b1cda8810a8b38ca1dc392420d3dd393
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42388034&retmode=xml
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42388034&retmode=xml
  summary: Fresh article-level PubMed metadata verifies PMID 42388034, DOI 10.1002/ps.71069,
    PMC13569317 and the full abstract.
  support: supports
  accessed_at: '2026-10-21T08:54:26.021925Z'
  snapshot_sha256: 103674cbfe03ac75435744f571fe47bf7eb86395ca6f9dc10afad731a6d1df26
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1002/ps.71069
  locator: https://api.crossref.org/works/10.1002/ps.71069
  summary: Fresh Crossref metadata verifies DOI/title and journal full-XML/PDF routes.
  support: supports
  accessed_at: '2026-10-21T08:54:26.034117Z'
  snapshot_sha256: 7088c862bf5b9e3049e1a38bc6db4a9c37cd8cc49437248e2a0c3b8a9d87f2ad
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42388034&format=json&resultType=core
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42388034&format=json&resultType=core
  summary: Fresh Europe PMC metadata links free PMC article routes but marks the record
    outside its open-access subset; current retrieval did not supply the body.
  support: supports
  accessed_at: '2026-10-21T08:54:26.417520Z'
  snapshot_sha256: 53381561c4d23ce8afb623942fd3d553f367565a89d902c5012954b109fc3780
- evidence_id: access
  kind: validation
  reference: Public EPMC, PMC, BioC and Wiley routes
  locator: 'access-audit.json: individual request times, status, response and receipt
    hashes'
  summary: XML returned 500 twice; HTML/PDF routes returned 403 or browser verification.
    PMC efetch supplied frontmatter only and BioC returned no result; none was counted
    as full text.
  support: context_only
  accessed_at: '2026-10-21T08:59:42.475918Z'
  snapshot_sha256: 1ddf146c4dba22bc8bdc770574575879fd45a9587efd37260d55c894d337c4f6
- evidence_id: root-access
  kind: validation
  reference: PMID:42388034
  locator: 'root-source-access.json: indexed primary abstract/data statement/captions
    and failed supplement retrieval'
  summary: Independent public access supplied abstract, data availability and supplementary
    captions, but no complete main body, DOCX or figure pixels.
  support: context_only
  accessed_at: '2026-10-21T08:59:42.476349Z'
  snapshot_sha256: df82c359e57a7113db82b00e62eec866747f0607416bff3b2795c5762a75947e
- evidence_id: members
  kind: primary_source
  reference: PMID:42388034
  locator: Fresh PubMed abstract; cached strain-source paragraph
  summary: G12 is the tobacco-rhizosphere B. amyloliquefaciens isolate; Y4 and X25
    are tobacco endophytes assigned to B. pumilus and B. velezensis. The abstract
    attributes prior F. oxysporum antagonism to G12 and P. nicotianae inhibition to
    Y4/X25.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476353Z'
- evidence_id: compatibility
  kind: primary_source
  reference: PMID:42388034
  locator: Cached pairwise-confrontation Results paragraph and Figure 1(A/B) reference;
    fresh abstract
  summary: Six directional plate-inhibition values are below 25%; these support mild
    reciprocal antagonism under that assay without proving long-term coexistence.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476355Z'
  quote: mild inhibition
- evidence_id: iaa
  kind: primary_source
  reference: PMID:42388034
  locator: Fresh PubMed abstract; cached Salkowski Results paragraph and Figure 1(D/E)
    reference
  summary: The reported 11.57 +/- 0.24 mg/L output exceeds monocultures; the assay
    is colorimetric and per volume, without resolved metabolite exchange or demonstrated
    IAA-mediated protection.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476357Z'
  quote: higher indole-3-acetic acid production
- evidence_id: glasshouse
  kind: primary_source
  reference: PMID:42388034
  locator: Fresh PubMed abstract; cached glasshouse Methods and disease Results/Figure
    4 reference
  summary: Preventive and curative disease suppression is reported with defense-enzyme
    responses. The detailed 54.07-to-9.26 disease-index change is supported by selected
    cached Results, not independently read figure pixels.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476359Z'
  quote: significant disease suppression
- evidence_id: root-activity
  kind: primary_source
  reference: PMID:42388034
  locator: Fresh PubMed abstract; cached TTC/dehydrogenase Results and Figure 6 reference
  summary: The detailed 20.27-45.38% preventive comparison is a root metabolic-activity
    endpoint, not direct biomass or reciprocal microbial fitness.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476360Z'
  quote: Root activity increased
- evidence_id: field
  kind: primary_source
  reference: PMID:42388034
  locator: Fresh PubMed abstract; cached two-site field Methods/Discussion
  summary: Field disease and yield effects are source-reported; yield is estimated
    from middle leaves rather than whole-plot harvested yield, and native-community
    abundance shifts were nonsignificant.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476361Z'
  quote: middle-leaf-based estimated yield
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:42388034
  locator: Cached single-strain fermentation, co-cultivation, glasshouse and field
    Methods paragraphs
  summary: Preparation uses 30 C/180 rpm, whereas co-cultivation measurement uses
    25 C/180 rpm/48 h. Cached glasshouse conditions are 25 +/- 2 C, 12 h light, 70-80%
    RH and 21 days; field plants receive 10 mL twice, seven days apart. These contexts
    must remain separate.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476363Z'
- evidence_id: limits
  kind: primary_source
  reference: PMID:42388034
  locator: Cached Discussion paragraphs on colonization, microbiome sampling and future
    validation
  summary: The source does not establish strain persistence, niche differentiation,
    hormonal mediation or long-term community stability. Endpoint genus-level shifts
    are not evidence of colonization; equal inoculation does not measure field dominance.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476364Z'
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, CHEBI and GO snapshots
  locator: Eleven unique ID/label pairs at fourteen occurrences
  summary: All labels match. Species terms preserve isolate-name context, and broad
    defense/growth processes do not independently prove a specific hormonal mechanism.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476552Z'
  snapshot_sha256: a88c344719e2a08faa9d08512ad2369507a59670b926968085751558b3913259
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: InteractionTypeEnum.COMPETITION; FunctionalRoleEnum.PATHOGEN_ANTAGONIST;
    AbundanceEnum.DOMINANT; taxonomy host exclusion
  summary: COMPETITION permits reciprocal negative effects without requiring resource
    depletion. DOMINANT is ordinal, and tobacco belongs as an external target rather
    than a microbial member.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476557Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: 'snippet-audit.json: eighteen occurrences'
  summary: All eighteen snippets match the selected-passage cache; none of those exact
    spans appears in the differently worded fresh abstract. Broad claims are corroborated,
    but full-text lexical freshness is unverified.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476717Z'
  snapshot_sha256: 8260279a6df0ba0aa09a773b957b097cc751a3cbc8b9004b65d34705bf04ab43
- evidence_id: datasets
  kind: validation
  reference: Publisher data availability and bounded accessible-source audit
  locator: dataset-verification.json; root-source-access.json
  summary: The public statement describes temporary sequencing-data restrictions and
    future deposition, without a current accession. No arbitrary archive association
    or dataset-omission finding is made.
  support: supports
  accessed_at: '2026-10-21T08:59:42.476877Z'
  snapshot_sha256: ca152edc2a88440243f8d26211cf5691ec8a53f6940e45c7a4df64443e43e01b
- evidence_id: history
  kind: record_content
  reference: Two target history sidecars; 20261005-eleven-records-batch5.yaml
  locator: Target decision lines 531-575; live issues 1248 and 880
  summary: The prior hash matches. Issue 1248 is the closed graph repair; closed issue
    880 concerned the already-present IAA process annotation, not a new repair claimed
    here.
  support: supports
  accessed_at: '2026-10-21T08:59:42.477035Z'
  snapshot_sha256: 5a027b242c5a35758a8247ad10e182896126ecbca80cddee83f3530ab4516a57
- evidence_id: search
  kind: search
  reference: Owned community/isolate/reusable-taxon roots
  locator: Ignored-inclusive bounded target, source and species lookup
  summary: No reusable record authenticates these exact isolates; shared Bacillus
    species occurrences are not interchangeable source strains.
  support: supports
  accessed_at: '2026-10-21T08:59:42.477184Z'
  snapshot_sha256: 0920d3df83795e66666e7f09719a5f5e766529e0658b847c8f34b56ceac61b80
  search_scope: rg --no-ignore --hidden for recorded species/strain/source identifiers
    in maintained roots; bounded synonym coverage.
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources runner
  locator: Explicit same-batch05 runtime reuse of 000120 discovery at 08:47:38Z
  summary: No callable owned-runtime adapter was available; the known external-checkout
    runner was not executed and no strain/module coverage was queried.
  support: supports
  accessed_at: '2026-10-21T08:59:42.477332Z'
  snapshot_sha256: 374bd4bf20a7cf8c9429cf9ea69cf445397f5d164acc613afb218910269c2e47
  search_scope: Original fresh batch05 discovery reused with its exact timestamp and
    external-path boundary.
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: 'support-audit.json: targeted API and native metrics'
  summary: The auditor reports two UNKNOWN_TARGET warnings for tobacco and marks INCOMPLETE.
    These are host-target limitations of the diagnostic, not evidence that tobacco
    should join the SynCom taxonomy.
  support: supports
  accessed_at: '2026-10-21T08:59:42.477454Z'
  snapshot_sha256: 28678f588e4b5ccb06f1b39c1bb3fa17f85652b7c75fbfd6326826afa5831cc6
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: Actual execution 2026-10-21T08:54:24.561324+00:00 to 2026-10-21T08:54:25.311381+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T08:54:25.311381Z'
  snapshot_sha256: 659b9da146e88f4d594578e20374b685286230dfdb41b89e2f6d5bde21c174cf
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-strict kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-05/000373/strict-report.tsv
  locator: Actual execution 2026-10-21T08:54:24.561533+00:00 to 2026-10-21T08:54:26.930264+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T08:54:26.930264Z'
  snapshot_sha256: f90fcc7d7a4861cbc2d59b2cd6e50175997459f824bebb68c646db889ed0bee1
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-terms kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: Actual execution 2026-10-21T08:54:24.561638+00:00 to 2026-10-21T08:54:26.464400+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T08:54:26.464400Z'
  snapshot_sha256: 46953a406ff9a5c56c0c7a7d5f8608c01b4e9709f29aee6e7f3cdd8f1c84ed9f
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: Actual execution 2026-10-21T08:54:25.311810+00:00 to 2026-10-21T08:54:25.397298+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T08:54:25.397298Z'
  snapshot_sha256: e0217930f9313f367925ed9bb52a67a0850a2bbfef9ac9ec6826eee4d3d9fab8
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: Actual execution 2026-10-21T08:54:25.397677+00:00 to 2026-10-21T08:54:27.017901+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T08:54:27.017901Z'
  snapshot_sha256: 1b1eab2edbf27e3f91a4e0b24041c3473d46a7bcee614c4aa4ba48fe07d8c642
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-history history/records/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom
  locator: Actual execution 2026-10-21T08:54:26.464685+00:00 to 2026-10-21T08:54:27.450444+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T08:54:27.450444Z'
  snapshot_sha256: ba20bd905870107d1ce9c0f44eb0c53e3646c7b4a21a5a1316e66dcf4c42106d
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T08:54:27.451070+00:00 to 2026-10-21T08:54:27.519675+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T08:54:27.519675Z'
  snapshot_sha256: 533a323bcd7c20fd03ced5cea1230edad68990a12cd7b6eb457dc9f90e420052
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-references-explained kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  locator: Actual execution 2026-10-21T08:54:27.519975+00:00 to 2026-10-21T08:54:29.383454+00:00
  summary: Target reference validation passed against the pinned selected-passage
    cache.
  support: supports
  accessed_at: '2026-10-21T08:54:29.383454Z'
  snapshot_sha256: b0230865dc0bcc5e1d55c87a88927d64cb97a282b6318f2294af80040d7b5366
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T08:44:47.720127+00:00 to 2026-10-21T08:45:04.195128+00:00
  summary: Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1, including two external-host warnings for this target.
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
    and exit 1, including two external-host warnings for this target.
  support: supports
  accessed_at: '2026-10-21T08:45:04.925187Z'
  snapshot_sha256: 8128f67a5d762dda726f1e6a0c0775a825d030d316c46765c08a359e6b621edb
assessments:
- assessment_id: identity
  area: identity
  topic: Three-strain inoculant and plant-pathogen assay scope
  outcome: supported
  summary: The source resolves G12/Y4/X25 and separates inoculum composition, host/pathogen
    targets and experimental endpoints.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - record
  - members
  - cultivation
  - schema
  - ontology
  dimensions:
  - name: community_scope
    value: Three-strain Bacillus SynCom tested on tobacco
    definition: ENGINEERED/SYNTHETIC/RHIZOSPHERE fit the function-guided inoculant;
      plant and challenge pathogens are not added microbial members.
    evidence_ids:
    - record
    - members
    - schema
  - name: source_strain
    value: B. amyloliquefaciens G12, B. pumilus Y4 and B. velezensis X25
    definition: Source names/habitats are explicit; species ontology anchors do not
      establish deposited isolate genomes or physiological equivalence to other strains.
    evidence_ids:
    - members
    - ontology
  - name: environment
    value: Tobacco-associated and rhizosphere contexts
    definition: The rhizosphere and plant-associated ENVO terms preserve different
      isolate habitats and application/sampling contexts.
    evidence_ids:
    - members
    - field
    - ontology
  - name: medium
    value: LB preparation and separate co-cultivation measurement
    definition: The encoded 30 C preparation is supported; the separate 25 C/48 h
      assay context is omitted. No exact CultureMech recipe is inferred from the LB
      name.
    evidence_ids:
    - cultivation
  - name: experimental_setting
    value: Plate and liquid assays, two glasshouse trials and two field sites
    definition: Glasshouse challenge and preventive/curative timing differ from field
      natural disease and repeat root irrigation.
    evidence_ids:
    - compatibility
    - glasshouse
    - field
    - cultivation
  - name: evidence_tier
    value: Measured endpoints and associated host responses
    definition: IAA, TTC root activity, defense enzymes and estimated yield remain
      separate; hormonal mediation and persistent strain colonization are not established.
    evidence_ids:
    - iaa
    - root-activity
    - limits
  - name: grounding_status
    value: Eleven canonical term pairs; historical GTDB blocks/statuses
    definition: G12/Y4 remain UNRESOLVED and X25 GROUNDED at species level; historical
      release/count provenance was not recomputed.
    evidence_ids:
    - ontology
    - adapter
- assessment_id: taxonomy
  area: grounding
  topic: All three member roles, source strains and prominence
  outcome: concern
  summary: Identities, habitats and antagonist roles are supported, but nearest taxonomy
    snippets establish only identity/source.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - members
  - schema
  - ontology
  - limits
  details: Attach the explicit pathogen-specific antagonism evidence locally. DOMINANT
    may describe co-equal formulation members; it is not a percentage defect and does
    not certify abundance or persistence in field soil.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Mild-Inhibition Three-Strain SynCom Compatibility'
  outcome: supported
  summary: Reciprocal directional inhibition supports the existing COMPETITION label
    at plate-assay scope.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - compatibility
  - members
  - schema
  - limits
  details: Participants are G12, Y4, X25 with each pair tested in both directions.
    Values below 25% define the source mild-inhibition class; this does not prove
    resource competition, reciprocal benefit or stable coexistence. Complete plate
    Methods/figures remain unreviewed.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: SynCom Indole-3-Acetic Acid Enhancement'
  outcome: supported
  summary: The node preserves a per-volume colorimetric increase without claiming
    exchange or IAA-mediated plant protection.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - iaa
  - cultivation
  - members
  - ontology
  details: Direction is three-strain co-culture versus constituent monocultures to
    measured supernatant output. The separate 25 C/48 h co-cultivation growth measurement
    is not assumed to define the IAA assay conditions. GO IAA biosynthesis and CHEBI
    identity are compatible subject annotations; no member-resolved flux or selective
    mediation is certified.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Tobacco FO/PN Glasshouse Disease Suppression'
  outcome: supported
  summary: Disease-index suppression is corroborated; the record does not convert
    it into a specific hormonal pathway.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - glasshouse
  - members
  - ontology
  - limits
  details: The G12/Y4/X25 inoculant treats He Luo No. 1 tobacco challenged with F.
    oxysporum and P. nicotianae, under preventive and curative timing. Source defense-enzyme
    responses support broad protective-response context but do not distinguish every
    direct/host-mediated contribution.
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Tobacco Root Activity Improvement'
  outcome: supported
  summary: The TTC-based endpoint is correctly limited to root metabolic activity.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - root-activity
  - members
  - schema
  details: Direction is SynCom treatment under FO/PN stress to tobacco root activity
    versus single-strain treatments. NCBITaxon:4097 is the external plant target,
    not a missing community member; the record correctly avoids direct biomass-growth
    and reciprocal microbial-benefit claims.
- assessment_id: node-4
  area: graph
  topic: 'ecological_interactions[4]: Two-Site Field Disease Suppression and Yield
    Increase'
  outcome: supported
  summary: Two-site outcomes retain the source estimated-yield and natural-disease
    scope.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - field
  - cultivation
  - members
  - limits
  - ontology
  details: G12/Y4/X25 is applied twice to tobacco under natural co-occurring root-rot/black-shank
    pressure. The target is host disease/estimated yield versus source controls; neither
    whole-plot harvested yield nor durable microbiome change is established. Figures
    remain uninspected.
- assessment_id: edges
  area: graph
  topic: downstream inventory
  outcome: not_applicable
  summary: No downstream arrows are encoded, so no additional mechanistic direction
    is certified.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - record
  - limits
- assessment_id: cultivation
  area: completeness
  topic: LB, glasshouse and field context
  outcome: concern
  summary: The record accurately captures 30 C stock preparation but omits the separate
    assay and plant-setting conditions present in selected cached Methods.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - cultivation
  - record
  details: The environmental factor duplicates assembly strategy. Place source-backed
    conditions with their experiment rather than assigning the 30 C preparation temperature
    to all outcomes. Current full Methods/supplement access remains unavailable.
- assessment_id: ingredients
  area: grounding
  topic: IAA output and biological scope
  outcome: supported
  summary: The IAA entry is a measured potential growth-promoting output rather than
    a verified mediator of disease protection.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - iaa
  - ontology
  - limits
  details: No metal-processing phenotype or specific additional metabolite is established
    by the accessible evidence. Names alone do not justify additional pathways or
    genes.
- assessment_id: provenance
  area: evidence
  topic: Source/cache/history and resource boundaries
  outcome: supported
  summary: Fresh abstract identity is verified, while exact snippets remain cache-supported
    and complete article access is unresolved.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - cache
  - snippets
  - history
  - datasets
  - root-access
  details: The record discussion already states that its cache is selected text. The
    PMID resource resolves; free-to-read PMC metadata does not establish open licensing
    or successful full-body retrieval. Source sequencing restrictions are retained
    without invented accession gaps.
- assessment_id: validation
  area: schema
  topic: Native checks and incomplete scientific source assessment
  outcome: concern
  summary: Seven focused gates and cache preflight pass; two host-target warnings
    and required full-source unavailability remain explicit.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - ontology
  - snippets
  - check-validate
  - check-validate-strict
  - check-audit-network
  - native-target
  - schema
  - access
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality within partial review
  outcome: supported
  summary: Completeness is 85 and capped quality 100; neither score substitutes for
    the unavailable full-source assessment.
  target_ids:
  - CommunityMech:000373
  evidence_ids:
  - record
  - native-target
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including all taxon roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). 50 + 5 + 0 + 10 + 5 + 10 + 0 + 5 = 85.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1=0, P2=0, P3=2, P4=0; 5 items / 5 nodes
      = 1; native INCOMPLETE due to 2 host warnings, so no network bonus. 100 - 4
      + 10 = 106 before capping; counts cover assessed material only.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count within this partial record review.
  - name: P2
    value: 0
    unit: findings
    definition: Observed native severity count within this partial record review.
  - name: P3
    value: 2
    unit: findings
    definition: Observed native severity count within this partial record review.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count within this partial record review.
findings:
- finding_id: role-evidence-placement
  issue_key: cm-000373-role-evidence-placement
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: source-supported roles or experimental context
    lack precise local evidence/representation; the three-strain identity and qualified
    graph remain intact.'
  rule_id: review-checklist.claim_evidence
  status: open
  certainty: confirmed
  title: Taxonomy role claims lack their narrow source evidence
  description: Each PATHOGEN_ANTAGONIST entry cites taxonomic identity and isolation
    habitat, although the fresh abstract separately provides the relevant pathogen-specific
    prior-study attribution.
  target_ids:
  - CommunityMech:000373
  field_paths:
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  - taxonomy[2].evidence
  evidence_ids:
  - members
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
- finding_id: cultivation-context
  issue_key: cm-000373-cultivation-context
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: source-supported roles or experimental context
    lack precise local evidence/representation; the three-strain identity and qualified
    graph remain intact.'
  rule_id: review-checklist.cultivation
  status: open
  certainty: confirmed
  title: Preparation and outcome-assay contexts are incompletely represented
  description: The LB block captures 30 C preparation but not the distinct 25 C/48
    h co-cultivation assay; cached glasshouse and field conditions are also absent
    from structured context, while the environmental factor repeats the assembly design.
  target_ids:
  - CommunityMech:000373
  field_paths:
  - growth_media
  - cultivation_setup
  - environmental_factors[0]
  evidence_ids:
  - cultivation
  - record
  - cache
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
actions:
- action_id: fix-role-evidence-placement
  description: Attach source-attributed antagonism evidence to each corresponding
    taxon role.
  finding_ids:
  - role-evidence-placement
  target_ids:
  - CommunityMech:000373
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Keep G12 linked to F. oxysporum and Y4/X25 to P. nicotianae, preserving attribution
    to the prior studies summarized by this article.
  - Retain current species/strain/habitat evidence; do not generalize every strain
    to every pathogen or invent direct mechanisms.
  - If original prior-study protocols are later cited, inspect them before adding
    stronger strain-specific claims.
  - Run references, schema and strict validation after separately authorized curation.
- action_id: fix-cultivation-context
  description: Treat the selected cached Methods as candidate context; independently
    verify complete primary Methods before adding numerical cultivation details.
  finding_ids:
  - cultivation-context
  target_ids:
  - CommunityMech:000373
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Verify complete main Methods before applying the numerical context expansions
    below; preserve the current correctly scoped preparation block until then.
  - Keep 30 C/180 rpm inoculum preparation separate from 25 C/180 rpm/48 h co-cultivation
    measurement.
  - Represent glasshouse 25 +/- 2 C, 12 h:12 h light/dark, 70-80% RH and 21-day experiments
    separately from field cultivation.
  - Preserve field 10 mL per-plant root irrigation and two events seven days apart
    without extrapolating glasshouse conditions to field sites.
  - Move duplicated assembly prose to engineering_design and use environmental fields
    for actual setting conditions.
  - Do not fabricate LB formulation, exact CultureMech ID, assay inoculum details
    or unavailable field protocol information.
  - Cite the selected-cache scope explicitly, then reassess against complete source
    Methods when accessible.
- action_id: complete-source-assessment
  description: When authorized complete source text becomes available, review full
    assay/field Methods, all relevant figures and supplementary material, then issue
    a new immutable assessment.
  finding_ids:
  - role-evidence-placement
  - cultivation-context
  target_ids:
  - CommunityMech:000373
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Verify detailed numeric comparisons and assay contexts against complete primary
    content while preserving current qualifiers.
  - Do not convert transcriptomic associations, nonsignificant genus shifts or IAA
    output into hormone mediation or persistent colonization.
  - Revisit sequencing-data release only when the source provides a real deposited
    accession.
  - No purchase, author contact, canonical edit or status promotion is authorized
    by this review.
limitations:
- Required whole-source assessment is unavailable. EPMC XML failed twice; public HTML/PDF
  routes supplied 403, browser verification or frontmatter only, while BioC returned
  no result. No access-control bypass or paid retrieval was used.
- The cache contains selected passages, not complete full text. All 18 exact snippets
  match it, but none matches the differently worded fresh abstract verbatim; this
  is not a fabricated-snippet finding or independent full-text verification.
- The fresh abstract corroborates broad identity/antagonism, IAA, glasshouse disease/root
  and field yield outcomes. Detailed directional plate values, disease-index and root-activity
  comparisons remain supported through the provenance-marked cache only.
- Publisher supplementary captions were read by the independent reviewer, but no DOCX
  or main/supplementary figure pixels were recovered. Captions do not certify the
  underlying plots or complete protocols.
- Tobacco is an external host target under the current schema. Two native UNKNOWN_TARGET
  warnings are retained in the score with no network bonus, without adding the plant
  to microbial taxonomy or inventing graph edges.
- DOMINANT can describe co-equal formulation members; equal-volume inoculum, nonsignificant
  genus shifts and a single microbiome endpoint do not demonstrate persistent field
  dominance, resilience or colonization.
- Source sequencing data are temporarily restricted with future deposition described;
  no accession was inferred, no author contacted and no raw transcriptome/microbiome
  analysis performed.
- Historical GTDB statuses and X25 mapping counts/release were not recomputed; same-runtime
  optional adapter discovery was reused and the known external runner was not executed.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 15 words for this publication; exact source spans are verified
  within fresh abstract or explicitly labeled selected cached Results.
- All 24 repository inputs were pinned before assessment and rechecked; quality 100
  is capped from 106 and is not whole-source scientific certification.
tags:
- record-review
- partial
- synthetic-community
- biocontrol
- batch-05
```
