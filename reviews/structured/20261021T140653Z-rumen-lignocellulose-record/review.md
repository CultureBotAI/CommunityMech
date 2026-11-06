# Rumen lignocellulolytic pair and three-member consortium review

- Review: 20261021T140653Z-rumen-lignocellulose-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T13:58:02.847365Z
- Finished UTC: 2026-10-21T14:06:53.749882Z
- Reviewer: codex (unknown)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

The direct abstract and public supplements support the selected pair/trio enzyme endpoints and retained two-node graph. Two major findings concern exact SR strain taxonomy and conflation of modeled cooperation with empirical activity; two minors concern recovered context and public source-data resources. Complete main Methods/Results remain uninspected.

## Scope And Provenance

Entire record, both nodes and absence of arrows assessed against direct abstract, critical SI, strain authority, schema, history and native checks.

Selection: Only released CommunityMech:000275 in the owned batch 08 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000275 | kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml | maintained | Butyrivibrio fibrisolvens + Selenomonas ruminantium + Ruminococcus albus Lignocellulolytic Rumen Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000275 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000275 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000275 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000275 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000275 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000275 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000275 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000275 | Reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000275 | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000275 | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| Primary and supplement identity | passed | True | CommunityMech:000275 | Direct abstract metadata and both public supplement DOI/file identities agree. |
| Complete main and critical supplemental verification | unavailable | True | CommunityMech:000275 | Critical supplemental claims were inspected, but complete main Methods/Results and main figures remain unavailable. |
| Exact growth-recipe correspondence | not_applicable | False | CommunityMech:000275 | No full focal bench recipe is verified; no catalogue medium or model bound is transferred into a CultureMech link. |
| Optional structured expression adapter | unavailable | False | CommunityMech:000275 | No relevant expression-module dataset established; bounded runtime discovery is preserved. |

## Scientific And Domain Assessments

### Selected pair/trio, source strains and current taxonomy

identity: concern. Targets: CommunityMech:000275.

The constructed three-member scope is valid, but the SR source strain maps to a different current species from the encoded taxon.

### State, origin and category

scope: supported. Targets: CommunityMech:000275.

Retain ENGINEERED, SYNTHETIC and LIGNOCELLULOSE for the deliberately assembled experimental/model system.

No equilibrium or genetic-engineering claim is inferred. The current category does not require full lignin mineralization, and the primary-degrader definition is not limited to any narrower arbitrary substrate class.

### Taxonomy role evidence and overview validation language

evidence: concern. Targets: CommunityMech:000275.

Preserve model-supported nutritional roles with computational qualifiers; do not present them as empirically validated by pair enzyme activity.

BF and RA have relevant individual enzyme activity in the supplement. The SR secondary-fermentation and recipient roles need their own source-specific model evidence and qualifiers. The current local IN_VITRO excerpt establishes pair membership/activity, not product provenance. The overview similarly links predicted mutualistic pairs to coculture validation without explaining that the observations are aggregate growth/enzyme endpoints. No particular tracer experiment is required to retain a hypothesis, and the roles are not declared biologically absent.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000275.

Retain the pair enzyme-synergy endpoint without a reciprocal-fitness interaction type, while correcting its SR identity and adding the recovered denominator.

The approximately 41% result is supported and is now traceable to the ratio of pair maximum activity to summed individual maxima. The existing statement that the abstract does not define the denominator remains historically accurate, but the current discussion should acknowledge the accessible source table. Do not describe it as growth gain or a time-matched comparison.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000275.

Retain the community-level three-substrate activity endpoint and qualified metabolic-interplay interpretation.

Correct the SR participant identifier but preserve three-member scope. The table supports bulk enzymatic synergy; no resolved exchange, reciprocal benefit or causal mediation is added. The focal triple model labels BF positive and SR/RA neutral, so pairwise model mutualism is not generalized to the trio. The small source xylan summary/time-course discrepancy does not overturn the bounded direction-of-effect claim.

### No downstream links

graph: supported. Targets: CommunityMech:000275.

Keep both endpoint nodes without workflow-derived causal arrows.

Model screening, correlation with enzyme assays and selection of a triple are analytical/design steps. The recovered supplements do not require converting them into ecological causal transitions.

### Structured model and assay context

provenance: concern. Targets: CommunityMech:000275.

Recover source-specific computational and assay provenance without inventing a bench recipe.

Record strain-linked draft/refined model context, PMA/PGSI and the inspected model-medium scope as computational provenance. Separate glucose validation from CMC growth and CMC/filter-paper/xylan enzyme assays. S1 lists basic 37 C/anaerobic strain attributes; catalogue conditions and model bounds must not become claimed focal cultivation conditions. Public supplementary data resolve the denominator even though full Methods remain unavailable.

### Physical and modeled environment

grounding: supported. Targets: CommunityMech:000275.

Laboratory environment is appropriate; digestive-tract context should remain explicitly tied to strain origin.

The bounded local ENVO query found no rumen-specific label/synonym match, which does not justify a global claim that no such term exists in every release or authority. Narrow or remove that incidental absence statement during curation; no replacement environment is invented and no separate finding is counted.

### Missing public source-data and supplement links

provenance: concern. Targets: CommunityMech:000275.

The two verified public supplements are usable, specific resources missing from the record.

Link the XLSX DOI 10.1021/acssynbio.6c00072.s001 as source data and the PDF DOI 10.1021/acssynbio.6c00072.s002 as supplementary figures. The workbook is not an executable genome-scale model archive. A bounded S1/S2 string scan found no concrete archive accession; this does not establish absence from the unavailable main.

### Prior repairs, authority chronology and snippets

provenance: supported. Targets: CommunityMech:000275.

Preserve earlier graph pruning and source-name history while applying the newly verified strain identity.

Issue 1217 repaired the label attached to 971; that label is still canonical for 971, but the newly recovered JCM 6582 mapping identifies sibling species 114197. Do not erase history or claim that the old label validator malfunctioned. The author-request text is local historical context only; no outreach occurred.

### Native checks and semantic source review

schema: supported. Targets: CommunityMech:000275.

Eight focused native gates pass; exact strain identity and evidence scope require the separate scientific findings.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000275.

Scores describe encoded fields and diagnostics, not full-main source coverage.

## Findings

### source-strain-taxonomy: Ground JCM 6582 to its current species

major / open / confirmed; issue key: cm-000275-source-strain-taxonomy.

S1 identifies the SR strain as JCM 6582. The direct culture catalogue and local taxonomy map it to Pseudoselenomonas lactilytica, NCBITaxon:114197, a sibling species of encoded Pseudoselenomonas ruminantium, NCBITaxon:971. The current ID/label match therefore denotes the wrong current species for this source strain.

### model-empirical-scope: Separate modeled cooperation from empirical enzyme validation

major / open / confirmed; issue key: cm-000275-model-empirical-scope.

The overview presents predicted mutualistic pairs as validated in cocultures, and the SR recipient/secondary-fermentation roles have only IN_VITRO pair-synergy evidence. The supplements support model-predicted cooperation and aggregate experimental activity, which do not establish measured partner-specific fitness or product transfer.

### recoverable-provenance: Add recovered assay comparison and computational context

minor / open / confirmed; issue key: cm-000275-recoverable-provenance.

The record omits available strain-linked model context and still leaves the 41% comparison denominator unresolved. S15 resolves the comparison as pair maximum divided by summed individual maxima; S2 and the SI figures distinguish model constraints, glucose validation and substrate-specific enzyme assays.

### public-si-resources: Link the verified public source-data supplements

minor / open / confirmed; issue key: cm-000275-public-si-resources.

The record has no associated dataset or external-resource link for the directly verified XLSX data and PDF figures, despite their exact parent DOI and downloadable file identities.

## Recommended Actions And Acceptance Checks

### repair-strain-grounding

Use the exact source strain to correct all SR taxon descriptors while preserving legacy source terminology.

- Record JCM 6582 and its source name/subspecies context; use NCBITaxon:114197 with canonical label Pseudoselenomonas lactilytica in taxonomy[1], ecological_interactions[0].target_taxon and ecological_interactions[1].participating_taxa[1]. Preserve the paper’s Selenomonas ruminantium wording as attributed source terminology.
- Re-ground GTDB against the corrected NCBI identity and exact strain/genome evidence. Do not automatically inherit the current 971 candidate list or guess a unique mapping.
- Record BF JCM 6563 and RA JCM 14654 with direct source support; their current species IDs remain compatible. Do not add the other screened strains or the bovine host as focal members.
- Re-run focused term, GTDB/domain, schema, strict and reference checks after separately authorized curation; retain append-only history and correct the stale instruction in discussions[0] to preserve the old species grounding.

### separate-evidence-types

Align the overview and local role evidence with the distinction between model prediction and measured aggregate activity.

- State that models predict partner cooperation, while experimental cocultures validate aggregate growth/enzyme performance at the reported assay scope. Do not claim experimental reciprocal fitness or donor-resolved uptake from these measurements.
- For each SR role, attach the relevant computational source with an explicit inferred/partial qualifier and model context, or omit the unsupported categorical role if its specific definition cannot be supported. Do not declare cross-feeding absent or require a particular tracer assay to retain the hypothesis.
- Retain two bounded activity nodes, zero workflow arrows and no empirical MUTUALISM type. Keep BF/RA degradation roles tied to their relevant individual enzyme evidence rather than only membership snippets.

### recover-context

Update the resolved denominator and source-specific model/assay provenance without inventing missing Methods.

- Explain that approximately 41% refers to the BF/SR maximum activity relative to the sum of the individual maxima, using S15 AQ80:AW81 and the maximum-activity source ranges. Do not imply matched timepoints, biomass gain or statistical significance beyond inspected evidence.
- Separate glucose growth/model validation, CMC coculture growth and CMC/filter-paper/xylan enzyme assays. Add available strain-linked model/provenance information to computational evidence; model-medium bounds are not bench concentrations.
- Update the current knowledge-gap discussion to acknowledge the inspected SI while preserving unavailable main Methods and unresolved mechanistic questions. Source-only compatibility-count and small xylan-summary differences remain explicitly bounded.
- Do not transfer S1 basic strain temperature/oxygen attributes or catalogue media into focal culture conditions. Narrow the unsupported global ENVO-absence statement to the actual bounded lookup or remove it; keep laboratory and rumen-origin contexts distinct.

### link-supplements

Add the exact public source-data and figure resources with their verified scope.

- Link DOI 10.1021/acssynbio.6c00072.s001 / Figshare 32788865 as the XLSX source-data resource containing S1–S21, and DOI 10.1021/acssynbio.6c00072.s002 / Figshare 32788868 as the PDF with Figures S1–S9.
- Preserve parent-publication identity and file version/type. Do not label the tables as executable GEM files, claim model reruns, or infer a sequence/archive accession not directly verified.
- Validate the resource and reference fields after separately authorized curation. A future full-main check remains necessary for a complete scientific review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml; Entire record, both interaction nodes and empty downstream graph | supports | The maintained record selects a three-member community and its strongest pair from a six-strain screen. Its graph distinguishes aggregate enzyme synergy from reciprocal fitness, but the overview and local role evidence do not consistently preserve that distinction. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42343824&amp;retmode=xml; Article metadata and available abstract | supports | The complete direct abstract and title establish the focal 2026 article and its enzyme/model claims. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42343824%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article metadata and available abstract | supports | Direct abstract/access metadata agree with the focal identity and do not supply a PMC full-text copy. |
| crossref | https://api.crossref.org/works/10.1021/acssynbio.6c00072; Article metadata and available abstract | supports | Direct DOI metadata identifies the focal article; metadata are not full Methods. |
| abstract | PMID:42343824; Abstract: model screening, pair enzyme endpoint and selected three-member combination | supports | Six rumen strains were screened; the BF/SR pair had about 41% higher endoglucanase activity and the BF/SR/RA combination showed activity synergy across the tested substrates. These are selected combinations, not all six organisms as one community. |
| strains | PMID:42343824; Supplementary workbook S1, rows 6, 7 and 9; S2 focal strain headings | supports | The source identifies BF as JCM 6563, SR as JCM 6582 (source subspecies lactilytica), and RA as JCM 14654. Basic strain attributes in S1 are distinct from a verified assay recipe or incubation protocol. |
| model-predictions | PMID:42343824; S7 focal BF/SR PMA/PGSI rows; S11 BF and SR normalized transport columns | supports | The model predicts positive partner responses for BF/SR and reports transport-associated flux changes. S11 gives normalized transport quantities without sufficient directional context to infer a specific donated metabolite from positive values alone. This is computational evidence, not measured transfer. |
| model-figures | PMID:42343824; Figures S5 and S6, pages 6–7; Figure S7, page 8 | supports | S5 describes cross-feeding inferred from modeled transport alterations; S6 classifies model interactions. S7 reports aggregate coculture growth compatibility on CMC. These analyses do not experimentally resolve each partner fitness response or donor-specific substrate uptake. |
| pair-denominator | PMID:42343824; S15 AQ80:AW81; AQ109:AT116; H102 and H106:H121 | supports | The pair maximum is 0.2865112101 U/ml; individual maxima are 0.1561040950 and 0.0472460223 U/ml. Their sum is 0.2033501173, and the source formula divides pair maximum by that sum to give DES 1.4089552. The approximately 41% enhancement is therefore relative to summed individual maxima, not necessarily matched timepoints. |
| triple-activity | PMID:42343824; S21 AG18:AL20; Figure S8 substrate context in the separate PDF | supports | The selected triple has reported DES above one for filter paper, CMC and xylan. These are aggregate enzyme assays. The source summary supports the bounded three-substrate claim without demonstrating reciprocal partner fitness, complete substrate mineralization or a necessary exchange mechanism. |
| model-context | PMID:42343824; S2 rows 2–48; workbook Index; Figures S1–S2 captions | supports | The supplement distinguishes draft/refined strain models and model-medium exchange bounds, with experimental glucose/growth comparisons used for model validation. Numeric exchange bounds are not culture concentrations. Software, full reconstruction methods and complete experimental recipes remain unavailable at the inspected main-source scope. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum; InteractionTypeEnum.MUTUALISM; EvidenceSourceEnum; ComputationalProvenance; MicrobialCommunity strain/resource slots | supports | Recipient and secondary-fermentation roles concern use of another taxon’s products. Mutualism requires both organisms to benefit; aggregate enzyme activity alone does not establish that. Computational evidence/provenance is distinct from IN_VITRO support. State and origin describe the engineered assembly, not genetic modification. |
| ontology | ontology-authority.json; Whole bounded receipt | supports | All six encoded ID/label pairs match local canonical labels. This mechanical pass does not resolve the later source-strain-specific discrepancy. |
| semantics | ontology-semantic-notes.json; Whole bounded receipt | supports | The initial schema/ontology audit separates broad degradation roles, modeled recipient roles and experimental enzyme endpoints. Its initial abstract-only scope is supplemented by the separate strain and SI receipts. |
| strain-authority | jcm-strain-authority.json; Whole bounded receipt | supports | Direct JCM catalogues and local taxonomy identify JCM 6582 as Pseudoselenomonas lactilytica, NCBITaxon:114197. This species is a sibling of encoded NCBITaxon:971. JCM 6563 and JCM 14654 agree with the other current species mappings. |
| supplement-read | lead-supplement-audit.json; Whole bounded receipt | supports | The lead inspected all SI captions, selected critical figure pixels and exact focal workbook cells/formulas. No model execution, statistical rerun or full-workbook certification is claimed. |
| supplement-clarification | lead-supplement-clarification.json; Whole bounded receipt | supports | This receipt corrects a compressed S6 branch-count sentence in the earlier lead audit and confirms the focal triple model labels: BF positive, SR and RA neutral. It adds no canonical finding. |
| resources | dataset-verification.json; Whole bounded receipt | supports | Both public Figshare supplements have matching parent DOI, size and MD5. The XLSX contains strain/model and assay data; the PDF has nine figures. Neither is a verified executable model deposit. |
| snippets | snippet-audit.json; Whole bounded receipt | supports | All five existing excerpts match the directly retrieved abstract and pinned cache; they do not alone support every attached role. |
| history | provenance-audit.json; Whole bounded receipt | supports | Both sidecars, exact prior graph decision, author-request draft and current linked issue provenance were reviewed. The draft was not sent. Earlier label repair and graph pruning are preserved as historical decisions, not certification of the newly recovered strain identity. |
| native-target | support-audit.json; Whole bounded receipt | supports | The native network is COMPLETE with two nodes, no arrows and two node-evidence entries. Mechanical metrics remain separate from source coverage. |
| source-scope | source-audit.json; Whole bounded receipt | supports | The whole record was assessed using the direct abstract, public supplements and authority records. Unavailable complete main Methods/Results and main figures require a partial review. |
| independent-source | root-independent-source-audit.json; Whole bounded receipt | supports | Root independently assessed the focal source, all nine supplemental figures and critical workbook/authority evidence, agreeing with the bounded findings and partial source scope. |
| access-doi | https://doi.org/10.1021/acssynbio.6c00072; Actual bounded access request | supports | The normal DOI route returned an HTTP 403 access page. |
| access-publisher | https://pubs.acs.org/doi/10.1021/acssynbio.6c00072; Actual bounded access request | supports | The direct ACS article route returned HTTP 403; the full main was not inspected. |
| access-openalex | https://api.openalex.org/works/https://doi.org/10.1021/acssynbio.6c00072; Actual bounded access request | supports | Closed-access metadata provides no open full-text location in this response; this is not proof of global absence. |
| adapter | adapter-check.json; Actual optional adapter/runtime discovery | supports | No relevant expression-module dataset is asserted; no paid provider or alternate checkout execution was used. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml; Actual execution 2026-10-21T13:58:24.095460+00:00 to 2026-10-21T13:58:24.885178+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-strict kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml --out /private/tmp/cm-review-session/batch-08/000275/strict-report.tsv; Actual execution 2026-10-21T13:58:24.095674+00:00 to 2026-10-21T13:58:26.267132+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-terms kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml; Actual execution 2026-10-21T13:58:24.095790+00:00 to 2026-10-21T13:58:25.873637+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml; Actual execution 2026-10-21T13:58:24.885438+00:00 to 2026-10-21T13:58:24.959028+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb-domain kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml; Actual execution 2026-10-21T13:58:24.959270+00:00 to 2026-10-21T13:58:26.311728+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-history history/records/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium; Actual execution 2026-10-21T13:58:25.873964+00:00 to 2026-10-21T13:58:26.529062+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T13:58:26.529482+00:00 to 2026-10-21T13:58:26.575349+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-references-explained kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml; Actual execution 2026-10-21T13:58:26.575565+00:00 to 2026-10-21T13:58:27.402856+00:00 | supports | Reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00 | supports | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00 | supports | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |

## Limits And Additional Notes

- Full main Methods/Results and main figures remain uninspected after direct ACS/DOI HTTP403 and metadata-only routes. No global absence of a public copy is asserted.
- The supplementary XLSX and PDF are directly inspected primary materials with verified identity. Reading selected tables does not certify all source calculations, model reconstruction or experimental protocols.
- No model execution, raw genome retrieval, statistical reanalysis, author contact or paid provider was used. Historical author-request text was not sent.
- Model exchange bounds and basic catalogue/strain attributes are not actual culture concentrations or a full focal cultivation regime. No exact recipe or executable model accession is invented.
- S6 versus S7 compatibility-count differences and the small S21 xylan summary/time-course discrepancy are source-only limits, not additional canonical defects. The corrected S6 branch interpretation is recorded separately.
- All existing snippets match direct abstract/cache; lexical matching alone does not validate the attached functional roles.
- Native corpus warnings remain existing batch-scoped diagnostics; passing focal checks do not certify source identity or complete science.
- No canonical, cache, history, generated or saved-review file changed; all 25 inspected inputs remain pinned.
- All five existing snippets match direct abstract/cache. Supplement-derived scientific judgments have separate source locators and read scopes.
- Completeness 55 and quality 100/raw 101 are mechanical scores; completion remains partial and scientific_review false.
- No model execution, raw genome download, statistical reanalysis, author contact or paid provider was used. Historical author-request text was read only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T140653Z-rumen-lignocellulose-record
kind: record
repository: CultureBotAI/CommunityMech
title: Rumen lignocellulolytic pair and three-member consortium review
started_at: '2026-10-21T13:58:02.847365Z'
finished_at: '2026-10-21T14:06:53.749882Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, native/ontology checks
    and supporting provenance; no person-level independence asserted.
skill: review-yaml-record
completion: partial
verdict: needs_curation
scientific_review: false
summary: The direct abstract and public supplements support the selected pair/trio
  enzyme endpoints and retained two-node graph. Two major findings concern exact SR
  strain taxonomy and conflation of modeled cooperation with empirical activity; two
  minors concern recovered context and public source-data resources. Complete main
  Methods/Results remain uninspected.
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
  - path: history/records/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium/2026-10-02T053348Z-codex-275ca3.yaml
    sha256: 3c96c6a99765542fdf0b38c6c7998d0c4798949795f6d811fa4484e679043616
    role: context
  - path: history/records/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium/2026-10-05T142601Z-codex-560f30.yaml
    sha256: 6e44e2aad957cfcebae23663169c10105467e94ef134605387de2f5458b44893
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    sha256: f9ad860387600c64fa0ba428afdfd9fa4cc0e960097b445b5253eb953ed1336e
    role: target
  - path: references_cache/PMID_42343824.md
    sha256: 25fba74703f690463be6b91ebe6ef2e712b29709eebf141dcea19e94eb64ce41
    role: context
  - path: reports/author_requests/000275_Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.txt
    sha256: 8cd5397eb3b005316ed296ae6409996021c65644df66bdcf3252d2e9b9472856
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
- target_id: CommunityMech:000275
  path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  label: Butyrivibrio fibrisolvens + Selenomonas ruminantium + Ruminococcus albus
    Lignocellulolytic Rumen Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    role: canonical_record
scope:
  description: Entire record, both nodes and absence of arrows assessed against direct
    abstract, critical SI, strain authority, schema, history and native checks.
  selection: Only released CommunityMech:000275 in the owned batch 08 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000275
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000275
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused native checks; a label match does not resolve exact source-strain
    identity or scientific support.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000275
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-08/000275/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused native checks; a label match does not resolve exact source-strain
    identity or scientific support.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000275
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused native checks; a label match does not resolve exact source-strain
    identity or scientific support.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000275
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused native checks; a label match does not resolve exact source-strain
    identity or scientific support.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000275
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused native checks; a label match does not resolve exact source-strain
    identity or scientific support.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000275
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused native checks; a label match does not resolve exact source-strain
    identity or scientific support.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000275
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused native checks; a label match does not resolve exact source-strain
    identity or scientific support.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000275
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused native checks; a label match does not resolve exact source-strain
    identity or scientific support.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000275
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse, not a focal scientific failure
    or source certification.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000275
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit same-batch corpus receipt reuse, not a focal scientific failure
    or source certification.
- check_id: source-identity
  name: Primary and supplement identity
  status: passed
  required: true
  summary: Direct abstract metadata and both public supplement DOI/file identities
    agree.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - pubmed
  - crossref
  - resources
- check_id: scientific-source
  name: Complete main and critical supplemental verification
  status: unavailable
  required: true
  summary: Critical supplemental claims were inspected, but complete main Methods/Results
    and main figures remain unavailable.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - source-scope
  - independent-source
  - access-publisher
- check_id: cross-mech
  name: Exact growth-recipe correspondence
  status: not_applicable
  required: false
  summary: No full focal bench recipe is verified; no catalogue medium or model bound
    is transferred into a CultureMech link.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - model-context
  - resources
- check_id: structured-adapter
  name: Optional structured expression adapter
  status: unavailable
  required: false
  summary: No relevant expression-module dataset established; bounded runtime discovery
    is preserved.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  locator: Entire record, both interaction nodes and empty downstream graph
  summary: The maintained record selects a three-member community and its strongest
    pair from a six-strain screen. Its graph distinguishes aggregate enzyme synergy
    from reciprocal fitness, but the overview and local role evidence do not consistently
    preserve that distinction.
  support: supports
  accessed_at: '2026-10-21T14:06:53.743198Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42343824&retmode=xml
  locator: Article metadata and available abstract
  summary: The complete direct abstract and title establish the focal 2026 article
    and its enzyme/model claims.
  support: supports
  accessed_at: '2026-10-21T13:58:40.213967Z'
  snapshot_sha256: a51b69f36f016946a5b98848a9a36a9341a74c9acfb54807792c17dee9034db2
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42343824%20AND%20SRC:MED&format=json&resultType=core
  locator: Article metadata and available abstract
  summary: Direct abstract/access metadata agree with the focal identity and do not
    supply a PMC full-text copy.
  support: supports
  accessed_at: '2026-10-21T13:58:40.568849Z'
  snapshot_sha256: 29998eb0fb207064b80283b792b30f6026ab26d248490f816db8e4c32cf9276e
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1021/acssynbio.6c00072
  locator: Article metadata and available abstract
  summary: Direct DOI metadata identifies the focal article; metadata are not full
    Methods.
  support: supports
  accessed_at: '2026-10-21T13:58:40.198727Z'
  snapshot_sha256: 614a7021bbe1302dd88fa674f9660b3cdf0c99c1c7145c8f75c9292024c86134
- evidence_id: abstract
  kind: primary_source
  reference: PMID:42343824
  locator: 'Abstract: model screening, pair enzyme endpoint and selected three-member
    combination'
  summary: Six rumen strains were screened; the BF/SR pair had about 41% higher endoglucanase
    activity and the BF/SR/RA combination showed activity synergy across the tested
    substrates. These are selected combinations, not all six organisms as one community.
  support: supports
  accessed_at: '2026-10-21T14:06:53.743807Z'
  snapshot_sha256: a51b69f36f016946a5b98848a9a36a9341a74c9acfb54807792c17dee9034db2
  quote: 41% increase in the endoglucanase activity
- evidence_id: strains
  kind: primary_source
  reference: PMID:42343824
  locator: Supplementary workbook S1, rows 6, 7 and 9; S2 focal strain headings
  summary: The source identifies BF as JCM 6563, SR as JCM 6582 (source subspecies
    lactilytica), and RA as JCM 14654. Basic strain attributes in S1 are distinct
    from a verified assay recipe or incubation protocol.
  support: supports
  accessed_at: '2026-10-21T14:06:53.744283Z'
  snapshot_sha256: 96ae86983d48ab54d984540057899fe33e02911a56d1875fc710c865776dbe20
- evidence_id: model-predictions
  kind: primary_source
  reference: PMID:42343824
  locator: S7 focal BF/SR PMA/PGSI rows; S11 BF and SR normalized transport columns
  summary: The model predicts positive partner responses for BF/SR and reports transport-associated
    flux changes. S11 gives normalized transport quantities without sufficient directional
    context to infer a specific donated metabolite from positive values alone. This
    is computational evidence, not measured transfer.
  support: supports
  accessed_at: '2026-10-21T14:06:53.744538Z'
  snapshot_sha256: 96ae86983d48ab54d984540057899fe33e02911a56d1875fc710c865776dbe20
- evidence_id: model-figures
  kind: primary_source
  reference: PMID:42343824
  locator: Figures S5 and S6, pages 6–7; Figure S7, page 8
  summary: S5 describes cross-feeding inferred from modeled transport alterations;
    S6 classifies model interactions. S7 reports aggregate coculture growth compatibility
    on CMC. These analyses do not experimentally resolve each partner fitness response
    or donor-specific substrate uptake.
  support: supports
  accessed_at: '2026-10-21T14:06:53.744948Z'
  snapshot_sha256: 133482702cf102b53980be4fdd47ece299ad641c5bb5970c9b45e95a5f967980
- evidence_id: pair-denominator
  kind: primary_source
  reference: PMID:42343824
  locator: S15 AQ80:AW81; AQ109:AT116; H102 and H106:H121
  summary: The pair maximum is 0.2865112101 U/ml; individual maxima are 0.1561040950
    and 0.0472460223 U/ml. Their sum is 0.2033501173, and the source formula divides
    pair maximum by that sum to give DES 1.4089552. The approximately 41% enhancement
    is therefore relative to summed individual maxima, not necessarily matched timepoints.
  support: supports
  accessed_at: '2026-10-21T14:06:53.745198Z'
  snapshot_sha256: 96ae86983d48ab54d984540057899fe33e02911a56d1875fc710c865776dbe20
- evidence_id: triple-activity
  kind: primary_source
  reference: PMID:42343824
  locator: S21 AG18:AL20; Figure S8 substrate context in the separate PDF
  summary: The selected triple has reported DES above one for filter paper, CMC and
    xylan. These are aggregate enzyme assays. The source summary supports the bounded
    three-substrate claim without demonstrating reciprocal partner fitness, complete
    substrate mineralization or a necessary exchange mechanism.
  support: supports
  accessed_at: '2026-10-21T14:06:53.745449Z'
  snapshot_sha256: 96ae86983d48ab54d984540057899fe33e02911a56d1875fc710c865776dbe20
- evidence_id: model-context
  kind: primary_source
  reference: PMID:42343824
  locator: S2 rows 2–48; workbook Index; Figures S1–S2 captions
  summary: The supplement distinguishes draft/refined strain models and model-medium
    exchange bounds, with experimental glucose/growth comparisons used for model validation.
    Numeric exchange bounds are not culture concentrations. Software, full reconstruction
    methods and complete experimental recipes remain unavailable at the inspected
    main-source scope.
  support: supports
  accessed_at: '2026-10-21T14:06:53.745702Z'
  snapshot_sha256: 96ae86983d48ab54d984540057899fe33e02911a56d1875fc710c865776dbe20
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum; InteractionTypeEnum.MUTUALISM; EvidenceSourceEnum;
    ComputationalProvenance; MicrobialCommunity strain/resource slots
  summary: Recipient and secondary-fermentation roles concern use of another taxon’s
    products. Mutualism requires both organisms to benefit; aggregate enzyme activity
    alone does not establish that. Computational evidence/provenance is distinct from
    IN_VITRO support. State and origin describe the engineered assembly, not genetic
    modification.
  support: supports
  accessed_at: '2026-10-21T14:06:53.745766Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded receipt
  summary: All six encoded ID/label pairs match local canonical labels. This mechanical
    pass does not resolve the later source-strain-specific discrepancy.
  support: supports
  accessed_at: '2026-10-21T14:06:53.745891Z'
  snapshot_sha256: 47b7ba2e2cb20a961d768a65f6650cc5bff341ca705503f1cfd30c73f5f82e7d
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole bounded receipt
  summary: The initial schema/ontology audit separates broad degradation roles, modeled
    recipient roles and experimental enzyme endpoints. Its initial abstract-only scope
    is supplemented by the separate strain and SI receipts.
  support: supports
  accessed_at: '2026-10-21T14:06:53.746014Z'
  snapshot_sha256: f27378e58339d15eed8283f1e97b2966c9b92f7b134c982d868473ec8829979c
- evidence_id: strain-authority
  kind: authority
  reference: jcm-strain-authority.json
  locator: Whole bounded receipt
  summary: Direct JCM catalogues and local taxonomy identify JCM 6582 as Pseudoselenomonas
    lactilytica, NCBITaxon:114197. This species is a sibling of encoded NCBITaxon:971.
    JCM 6563 and JCM 14654 agree with the other current species mappings.
  support: supports
  accessed_at: '2026-10-21T14:06:53.746162Z'
  snapshot_sha256: f478f45108eb50bb56334e407e9b67489afb88228c68bab6941b2c430dc21a87
- evidence_id: supplement-read
  kind: validation
  reference: lead-supplement-audit.json
  locator: Whole bounded receipt
  summary: The lead inspected all SI captions, selected critical figure pixels and
    exact focal workbook cells/formulas. No model execution, statistical rerun or
    full-workbook certification is claimed.
  support: supports
  accessed_at: '2026-10-21T14:06:53.746386Z'
  snapshot_sha256: f6a10447b817158d2f75c40e006fd76dcf2ac36d498b309da231d50a6cc4a1a5
- evidence_id: supplement-clarification
  kind: validation
  reference: lead-supplement-clarification.json
  locator: Whole bounded receipt
  summary: 'This receipt corrects a compressed S6 branch-count sentence in the earlier
    lead audit and confirms the focal triple model labels: BF positive, SR and RA
    neutral. It adds no canonical finding.'
  support: supports
  accessed_at: '2026-10-21T14:06:53.746569Z'
  snapshot_sha256: 92a5299331a2449c4d443a5f9318d0f504df2f37f56db987aea5ac19cfc5748d
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded receipt
  summary: Both public Figshare supplements have matching parent DOI, size and MD5.
    The XLSX contains strain/model and assay data; the PDF has nine figures. Neither
    is a verified executable model deposit.
  support: supports
  accessed_at: '2026-10-21T14:06:53.746614Z'
  snapshot_sha256: 4aafe0b743110923a3fcf11a3d71a3737cc7bdc6af4329b842a6477019c8e2fe
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded receipt
  summary: All five existing excerpts match the directly retrieved abstract and pinned
    cache; they do not alone support every attached role.
  support: supports
  accessed_at: '2026-10-21T14:06:53.746741Z'
  snapshot_sha256: 063d9cfe0384fa410f666814b5acdf29eca2ecfd4bd3d06002913a98692fdf36
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded receipt
  summary: Both sidecars, exact prior graph decision, author-request draft and current
    linked issue provenance were reviewed. The draft was not sent. Earlier label repair
    and graph pruning are preserved as historical decisions, not certification of
    the newly recovered strain identity.
  support: supports
  accessed_at: '2026-10-21T14:06:53.746867Z'
  snapshot_sha256: a83dcc80807e4dc882bce6541b445e00d6dd17c548748e7009ce5fdd3d16dacd
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded receipt
  summary: The native network is COMPLETE with two nodes, no arrows and two node-evidence
    entries. Mechanical metrics remain separate from source coverage.
  support: supports
  accessed_at: '2026-10-21T14:06:53.746903Z'
  snapshot_sha256: 5495864434294c5096d24f5e79b3674481f9145e147cf6d7a8c8f624951c7723
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded receipt
  summary: The whole record was assessed using the direct abstract, public supplements
    and authority records. Unavailable complete main Methods/Results and main figures
    require a partial review.
  support: supports
  accessed_at: '2026-10-21T14:06:53.746927Z'
  snapshot_sha256: 09712828253f332491c942050974b92c3631d19e093d4675875642419cdd5b93
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded receipt
  summary: Root independently assessed the focal source, all nine supplemental figures
    and critical workbook/authority evidence, agreeing with the bounded findings and
    partial source scope.
  support: supports
  accessed_at: '2026-10-21T14:06:53.747041Z'
  snapshot_sha256: 1f4ba4315c444ab637469b2976c8a9ee592a64abd53a80cc41b9572440c73aa7
- evidence_id: access-doi
  kind: validation
  reference: https://doi.org/10.1021/acssynbio.6c00072
  locator: Actual bounded access request
  summary: The normal DOI route returned an HTTP 403 access page.
  support: supports
  accessed_at: '2026-10-21T13:58:40.352637Z'
  snapshot_sha256: 925affd6cbd99c0ce0458dcd5dd82ba8a6f0eeff95fdbced0fe7ddae8dc60a80
- evidence_id: access-publisher
  kind: validation
  reference: https://pubs.acs.org/doi/10.1021/acssynbio.6c00072
  locator: Actual bounded access request
  summary: The direct ACS article route returned HTTP 403; the full main was not inspected.
  support: supports
  accessed_at: '2026-10-21T13:58:40.275729Z'
  snapshot_sha256: d6590620f89e242acebf8883b82422afec95e5d0c90ab8b4059751b79355a23f
- evidence_id: access-openalex
  kind: validation
  reference: https://api.openalex.org/works/https://doi.org/10.1021/acssynbio.6c00072
  locator: Actual bounded access request
  summary: Closed-access metadata provides no open full-text location in this response;
    this is not proof of global absence.
  support: supports
  accessed_at: '2026-10-21T13:59:23.833414Z'
  snapshot_sha256: d3570f90d412b2d62b18b9cf80b94c069fffdaf8c3dcd4cf0087fb82f4892be7
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Actual optional adapter/runtime discovery
  summary: No relevant expression-module dataset is asserted; no paid provider or
    alternate checkout execution was used.
  support: supports
  accessed_at: '2026-10-21T14:06:53.747640Z'
  snapshot_sha256: 6bb4a7cddef12bd10a1dc624d876666f1c7f7d16fbfa39318ad65b92a956cf6c
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  locator: Actual execution 2026-10-21T13:58:24.095460+00:00 to 2026-10-21T13:58:24.885178+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T13:58:24.885178Z'
  snapshot_sha256: 89bd0c9719ed4278d0cb2952877596b23d9562953201616f0bdfb9a850af9935
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-08/000275/strict-report.tsv
  locator: Actual execution 2026-10-21T13:58:24.095674+00:00 to 2026-10-21T13:58:26.267132+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T13:58:26.267132Z'
  snapshot_sha256: ba7e4414ed37b1e77b0c450f2d3da965d24601cbdda2876d88c51efe43600494
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  locator: Actual execution 2026-10-21T13:58:24.095790+00:00 to 2026-10-21T13:58:25.873637+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T13:58:25.873637Z'
  snapshot_sha256: 1b7c8f82559a1750126e73b965ddf76c4ae279ca24466975b784a01ab93c2827
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  locator: Actual execution 2026-10-21T13:58:24.885438+00:00 to 2026-10-21T13:58:24.959028+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T13:58:24.959028Z'
  snapshot_sha256: 65df601a3ba0d01ec9d89f6c65171bd1424797953c73aa6fb3d5c06ff5bee847
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  locator: Actual execution 2026-10-21T13:58:24.959270+00:00 to 2026-10-21T13:58:26.311728+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T13:58:26.311728Z'
  snapshot_sha256: 52cbd5e4acd357607188e8bed00d92ffcbbda542ba6d74b63d98b545ba028f0e
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium
  locator: Actual execution 2026-10-21T13:58:25.873964+00:00 to 2026-10-21T13:58:26.529062+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T13:58:26.529062Z'
  snapshot_sha256: 988b9cb459a8dc3ff05da9c2eccaf251522cf844545dbc4da78b4a96ea29e9bf
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T13:58:26.529482+00:00 to 2026-10-21T13:58:26.575349+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T13:58:26.575349Z'
  snapshot_sha256: b3b8ebc4ef248c84d58127c05c956470960274c7e063105ff52a6d623d2f313e
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
  locator: Actual execution 2026-10-21T13:58:26.575565+00:00 to 2026-10-21T13:58:27.402856+00:00
  summary: Reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T13:58:27.402856Z'
  snapshot_sha256: 95ea3adbbd0aea0fa9cd1f22d48c152becb93637c80bef2a140e89ae63ce153e
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
  topic: Selected pair/trio, source strains and current taxonomy
  outcome: concern
  summary: The constructed three-member scope is valid, but the SR source strain maps
    to a different current species from the encoded taxon.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - abstract
  - strains
  - strain-authority
  - ontology
  dimensions:
  - name: community_scope
    value: Three selected strains and one nested pair
    definition: Six strains formed the screening panel; the other three are not automatically
      community members.
    evidence_ids:
    - abstract
    - strains
  - name: taxon_rank
    value: Three species descriptors; one source-strain mismatch
    definition: JCM 6582 maps to NCBITaxon:114197, not sibling species 971.
    evidence_ids:
    - strain-authority
  - name: strain
    value: BF JCM 6563; SR JCM 6582; RA JCM 14654
    definition: Direct source table identities with catalogue confirmation; aliases
      do not substitute for an experimental genome accession.
    evidence_ids:
    - strains
    - strain-authority
  - name: grounding_status
    value: Re-ground SR after correcting its NCBI identity
    definition: Do not reuse the current 971-derived GTDB candidates automatically.
    evidence_ids:
    - ontology
    - strain-authority
  - name: environment
    value: Laboratory cultures and computational models of rumen-derived organisms
    definition: Digestive-tract context denotes provenance, not a verified intact-rumen
      simulation.
    evidence_ids:
    - semantics
    - model-context
  - name: medium
    value: CMC, filter-paper and xylan assay contexts; glucose-based model validation
    definition: Complete culture formulation, volume and incubation protocol remain
      unresolved.
    evidence_ids:
    - model-figures
    - model-context
  - name: evidence_tier
    value: Direct abstract, public SI and strain authority
    definition: Full main Methods/Results and main figures remain uninspected.
    evidence_ids:
    - source-scope
- assessment_id: state
  area: scope
  topic: State, origin and category
  outcome: supported
  summary: Retain ENGINEERED, SYNTHETIC and LIGNOCELLULOSE for the deliberately assembled
    experimental/model system.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - abstract
  - schema
  - semantics
  details: No equilibrium or genetic-engineering claim is inferred. The current category
    does not require full lignin mineralization, and the primary-degrader definition
    is not limited to any narrower arbitrary substrate class.
- assessment_id: roles
  area: evidence
  topic: Taxonomy role evidence and overview validation language
  outcome: concern
  summary: Preserve model-supported nutritional roles with computational qualifiers;
    do not present them as empirically validated by pair enzyme activity.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - model-predictions
  - model-figures
  - schema
  - record
  details: BF and RA have relevant individual enzyme activity in the supplement. The
    SR secondary-fermentation and recipient roles need their own source-specific model
    evidence and qualifiers. The current local IN_VITRO excerpt establishes pair membership/activity,
    not product provenance. The overview similarly links predicted mutualistic pairs
    to coculture validation without explaining that the observations are aggregate
    growth/enzyme endpoints. No particular tracer experiment is required to retain
    a hypothesis, and the roles are not declared biologically absent.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain the pair enzyme-synergy endpoint without a reciprocal-fitness interaction
    type, while correcting its SR identity and adding the recovered denominator.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - abstract
  - pair-denominator
  - model-figures
  - strain-authority
  details: The approximately 41% result is supported and is now traceable to the ratio
    of pair maximum activity to summed individual maxima. The existing statement that
    the abstract does not define the denominator remains historically accurate, but
    the current discussion should acknowledge the accessible source table. Do not
    describe it as growth gain or a time-matched comparison.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain the community-level three-substrate activity endpoint and qualified
    metabolic-interplay interpretation.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - triple-activity
  - abstract
  - strain-authority
  - supplement-clarification
  details: Correct the SR participant identifier but preserve three-member scope.
    The table supports bulk enzymatic synergy; no resolved exchange, reciprocal benefit
    or causal mediation is added. The focal triple model labels BF positive and SR/RA
    neutral, so pairwise model mutualism is not generalized to the trio. The small
    source xylan summary/time-course discrepancy does not overturn the bounded direction-of-effect
    claim.
- assessment_id: arrows
  area: graph
  topic: No downstream links
  outcome: supported
  summary: Keep both endpoint nodes without workflow-derived causal arrows.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - record
  - history
  - model-figures
  details: Model screening, correlation with enzyme assays and selection of a triple
    are analytical/design steps. The recovered supplements do not require converting
    them into ecological causal transitions.
- assessment_id: context
  area: provenance
  topic: Structured model and assay context
  outcome: concern
  summary: Recover source-specific computational and assay provenance without inventing
    a bench recipe.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - model-context
  - pair-denominator
  - strains
  - resources
  details: Record strain-linked draft/refined model context, PMA/PGSI and the inspected
    model-medium scope as computational provenance. Separate glucose validation from
    CMC growth and CMC/filter-paper/xylan enzyme assays. S1 lists basic 37 C/anaerobic
    strain attributes; catalogue conditions and model bounds must not become claimed
    focal cultivation conditions. Public supplementary data resolve the denominator
    even though full Methods remain unavailable.
- assessment_id: environment
  area: grounding
  topic: Physical and modeled environment
  outcome: supported
  summary: Laboratory environment is appropriate; digestive-tract context should remain
    explicitly tied to strain origin.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - semantics
  details: The bounded local ENVO query found no rumen-specific label/synonym match,
    which does not justify a global claim that no such term exists in every release
    or authority. Narrow or remove that incidental absence statement during curation;
    no replacement environment is invented and no separate finding is counted.
- assessment_id: resources
  area: provenance
  topic: Missing public source-data and supplement links
  outcome: concern
  summary: The two verified public supplements are usable, specific resources missing
    from the record.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - resources
  details: Link the XLSX DOI 10.1021/acssynbio.6c00072.s001 as source data and the
    PDF DOI 10.1021/acssynbio.6c00072.s002 as supplementary figures. The workbook
    is not an executable genome-scale model archive. A bounded S1/S2 string scan found
    no concrete archive accession; this does not establish absence from the unavailable
    main.
- assessment_id: history
  area: provenance
  topic: Prior repairs, authority chronology and snippets
  outcome: supported
  summary: Preserve earlier graph pruning and source-name history while applying the
    newly verified strain identity.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - history
  - snippets
  - strain-authority
  details: Issue 1217 repaired the label attached to 971; that label is still canonical
    for 971, but the newly recovered JCM 6582 mapping identifies sibling species 114197.
    Do not erase history or claim that the old label validator malfunctioned. The
    author-request text is local historical context only; no outreach occurred.
- assessment_id: validation
  area: schema
  topic: Native checks and semantic source review
  outcome: supported
  summary: Eight focused native gates pass; exact strain identity and evidence scope
    require the separate scientific findings.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - ontology
  - check-validate
  - check-validate-references-explained
  - strain-authority
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Scores describe encoded fields and diagnostics, not full-main source coverage.
  target_ids:
  - CommunityMech:000275
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 55
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role component + 5 environment; no three-node,
      environmental-factor, growth-medium, resource, dataset or metabolite bonus.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 − 50P1 − 10P2 − 2P3 + 20min(mean node evidence/2,1) + 15
      if COMPLETE,0,100). P1=0/P2=2/P3=2/P4=0; two evidence/two nodes gives 10; COMPLETE
      adds 15; raw 101 capped 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 2
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
- finding_id: source-strain-taxonomy
  issue_key: cm-000275-source-strain-taxonomy
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: 'P2: verified strain-to-species grounding mismatch affects
    membership and both graph participant descriptors, while the intended experimental
    community remains identifiable.'
  rule_id: review-checklist.claim-specific-identity-evidence-and-provenance
  status: open
  certainty: confirmed
  title: Ground JCM 6582 to its current species
  description: S1 identifies the SR strain as JCM 6582. The direct culture catalogue
    and local taxonomy map it to Pseudoselenomonas lactilytica, NCBITaxon:114197,
    a sibling species of encoded Pseudoselenomonas ruminantium, NCBITaxon:971. The
    current ID/label match therefore denotes the wrong current species for this source
    strain.
  target_ids:
  - CommunityMech:000275
  field_paths:
  - taxonomy[1].taxon_term
  - ecological_interactions[0].target_taxon
  - ecological_interactions[1].participating_taxa[1]
  evidence_ids:
  - strains
  - strain-authority
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    role: canonical_record
- finding_id: model-empirical-scope
  issue_key: cm-000275-model-empirical-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: evidence-type and causal-scope inflation remains outside
    a correctly qualified graph. Model-supported hypotheses can be retained with accurate
    qualifiers rather than deleted.'
  rule_id: review-checklist.claim-specific-identity-evidence-and-provenance
  status: open
  certainty: confirmed
  title: Separate modeled cooperation from empirical enzyme validation
  description: The overview presents predicted mutualistic pairs as validated in cocultures,
    and the SR recipient/secondary-fermentation roles have only IN_VITRO pair-synergy
    evidence. The supplements support model-predicted cooperation and aggregate experimental
    activity, which do not establish measured partner-specific fitness or product
    transfer.
  target_ids:
  - CommunityMech:000275
  field_paths:
  - description
  - taxonomy[1].functional_role
  - taxonomy[1].evidence
  evidence_ids:
  - model-predictions
  - model-figures
  - schema
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    role: canonical_record
- finding_id: recoverable-provenance
  issue_key: cm-000275-recoverable-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded recoverable context improves reproducibility
    and the existing correct endpoint without requiring a fabricated culture recipe
    or complete model reproduction.'
  rule_id: review-checklist.claim-specific-identity-evidence-and-provenance
  status: open
  certainty: confirmed
  title: Add recovered assay comparison and computational context
  description: The record omits available strain-linked model context and still leaves
    the 41% comparison denominator unresolved. S15 resolves the comparison as pair
    maximum divided by summed individual maxima; S2 and the SI figures distinguish
    model constraints, glucose validation and substrate-specific enzyme assays.
  target_ids:
  - CommunityMech:000275
  field_paths:
  - ecological_interactions[0].description
  - discussions[0].rationale
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  - taxonomy[2].evidence
  evidence_ids:
  - pair-denominator
  - model-context
  - strains
  - supplement-read
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    role: canonical_record
- finding_id: public-si-resources
  issue_key: cm-000275-public-si-resources
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: specific traceable public resource omission; no unverified
    genome, executable model or recipe deposit is inferred.'
  rule_id: review-checklist.claim-specific-identity-evidence-and-provenance
  status: open
  certainty: confirmed
  title: Link the verified public source-data supplements
  description: The record has no associated dataset or external-resource link for
    the directly verified XLSX data and PDF figures, despite their exact parent DOI
    and downloadable file identities.
  target_ids:
  - CommunityMech:000275
  field_paths:
  - associated_datasets
  - external_resources
  evidence_ids:
  - resources
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    role: canonical_record
actions:
- action_id: repair-strain-grounding
  description: Use the exact source strain to correct all SR taxon descriptors while
    preserving legacy source terminology.
  finding_ids:
  - source-strain-taxonomy
  target_ids:
  - CommunityMech:000275
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Record JCM 6582 and its source name/subspecies context; use NCBITaxon:114197 with
    canonical label Pseudoselenomonas lactilytica in taxonomy[1], ecological_interactions[0].target_taxon
    and ecological_interactions[1].participating_taxa[1]. Preserve the paper’s Selenomonas
    ruminantium wording as attributed source terminology.
  - Re-ground GTDB against the corrected NCBI identity and exact strain/genome evidence.
    Do not automatically inherit the current 971 candidate list or guess a unique
    mapping.
  - Record BF JCM 6563 and RA JCM 14654 with direct source support; their current
    species IDs remain compatible. Do not add the other screened strains or the bovine
    host as focal members.
  - Re-run focused term, GTDB/domain, schema, strict and reference checks after separately
    authorized curation; retain append-only history and correct the stale instruction
    in discussions[0] to preserve the old species grounding.
- action_id: separate-evidence-types
  description: Align the overview and local role evidence with the distinction between
    model prediction and measured aggregate activity.
  finding_ids:
  - model-empirical-scope
  target_ids:
  - CommunityMech:000275
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - State that models predict partner cooperation, while experimental cocultures validate
    aggregate growth/enzyme performance at the reported assay scope. Do not claim
    experimental reciprocal fitness or donor-resolved uptake from these measurements.
  - For each SR role, attach the relevant computational source with an explicit inferred/partial
    qualifier and model context, or omit the unsupported categorical role if its specific
    definition cannot be supported. Do not declare cross-feeding absent or require
    a particular tracer assay to retain the hypothesis.
  - Retain two bounded activity nodes, zero workflow arrows and no empirical MUTUALISM
    type. Keep BF/RA degradation roles tied to their relevant individual enzyme evidence
    rather than only membership snippets.
- action_id: recover-context
  description: Update the resolved denominator and source-specific model/assay provenance
    without inventing missing Methods.
  finding_ids:
  - recoverable-provenance
  target_ids:
  - CommunityMech:000275
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Explain that approximately 41% refers to the BF/SR maximum activity relative to
    the sum of the individual maxima, using S15 AQ80:AW81 and the maximum-activity
    source ranges. Do not imply matched timepoints, biomass gain or statistical significance
    beyond inspected evidence.
  - Separate glucose growth/model validation, CMC coculture growth and CMC/filter-paper/xylan
    enzyme assays. Add available strain-linked model/provenance information to computational
    evidence; model-medium bounds are not bench concentrations.
  - Update the current knowledge-gap discussion to acknowledge the inspected SI while
    preserving unavailable main Methods and unresolved mechanistic questions. Source-only
    compatibility-count and small xylan-summary differences remain explicitly bounded.
  - Do not transfer S1 basic strain temperature/oxygen attributes or catalogue media
    into focal culture conditions. Narrow the unsupported global ENVO-absence statement
    to the actual bounded lookup or remove it; keep laboratory and rumen-origin contexts
    distinct.
- action_id: link-supplements
  description: Add the exact public source-data and figure resources with their verified
    scope.
  finding_ids:
  - public-si-resources
  target_ids:
  - CommunityMech:000275
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Butyrivibrio_Selenomonas_Ruminococcus_Lignocellulolytic_Rumen_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Link DOI 10.1021/acssynbio.6c00072.s001 / Figshare 32788865 as the XLSX source-data
    resource containing S1–S21, and DOI 10.1021/acssynbio.6c00072.s002 / Figshare
    32788868 as the PDF with Figures S1–S9.
  - Preserve parent-publication identity and file version/type. Do not label the tables
    as executable GEM files, claim model reruns, or infer a sequence/archive accession
    not directly verified.
  - Validate the resource and reference fields after separately authorized curation.
    A future full-main check remains necessary for a complete scientific review.
limitations:
- Full main Methods/Results and main figures remain uninspected after direct ACS/DOI
  HTTP403 and metadata-only routes. No global absence of a public copy is asserted.
- The supplementary XLSX and PDF are directly inspected primary materials with verified
  identity. Reading selected tables does not certify all source calculations, model
  reconstruction or experimental protocols.
- No model execution, raw genome retrieval, statistical reanalysis, author contact
  or paid provider was used. Historical author-request text was not sent.
- Model exchange bounds and basic catalogue/strain attributes are not actual culture
  concentrations or a full focal cultivation regime. No exact recipe or executable
  model accession is invented.
- S6 versus S7 compatibility-count differences and the small S21 xylan summary/time-course
  discrepancy are source-only limits, not additional canonical defects. The corrected
  S6 branch interpretation is recorded separately.
- All existing snippets match direct abstract/cache; lexical matching alone does not
  validate the attached functional roles.
- Native corpus warnings remain existing batch-scoped diagnostics; passing focal checks
  do not certify source identity or complete science.
notes:
- No canonical, cache, history, generated or saved-review file changed; all 25 inspected
  inputs remain pinned.
- All five existing snippets match direct abstract/cache. Supplement-derived scientific
  judgments have separate source locators and read scopes.
- Completeness 55 and quality 100/raw 101 are mechanical scores; completion remains
  partial and scientific_review false.
- No model execution, raw genome download, statistical reanalysis, author contact
  or paid provider was used. Historical author-request text was read only.
tags:
- record-review
- rumen
- lignocellulose
- model-evidence
- partial-source
- batch-08
```
