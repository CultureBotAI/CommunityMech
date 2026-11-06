# Anammox DNRA community: whole-record source review

- Review: 20261020T073134Z-anammox-dnra-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-20T07:26:41.223800Z
- Finished UTC: 2026-10-20T07:31:34.589617Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full primary-source review supports the qualified five-node/three-arrow graph but identifies one major summary-level causal overstatement and six minor completeness/provenance issues. All eight focused checks pass;11 ontology labels and23 snippets verify. Corpus warnings and optional adapter unavailability remain explicit.

## Scope And Provenance

Whole record, all five nodes and three arrows, taxonomy, environment/cultivation,23 snippets, resources, history and discussion. Main-text source review; no supplementary-file or image-geometry certification.

Selection: Fourth uncovered record in batch03 path order after excluding validated baseline and pending batches01/02.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ade4a9acdc245e1090522bb4f6ec5fe82ee88689.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000244 | kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml | maintained | Anammox Bioreactor DNRA Destabilization Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000244 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml |
| validate-strict | passed | True | CommunityMech:000244 | uv run python scripts/validate_strict.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml --out /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000244 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000244 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000244 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml |
| validate-history | passed | True | CommunityMech:000244 | No issues found |
| normalize-cache-names-check | passed | True | CommunityMech:000244 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000244 | Validating kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000244 | Correct batch03 PYTHONPATH corpus run:477 records,57 warnings in21 records,zero errors;exit1. Selected target has no reported warning. Reused actual run; canonical inputs unchanged. |
| check-network-quality | failed | True | CommunityMech:000244 | Correct batch03 PYTHONPATH corpus run:477 records,57 warnings in21 records,zero errors;exit1. Selected target has no reported warning. Reused actual run; canonical inputs unchanged. |
| Structured expression adapter availability | unavailable | False | CommunityMech:000244 | command -v kg-microbe-sources returned no executable; ignored-inclusive search of /Users/marcin/Documents/VIMSS/ontology/culturebotai-claw and /Users/marcin/Documents/VIMSS/ontology/Mechs/culturebotai-claw found both expected roots absent. This bounded runner search does not establish machine-wide absence. Primary Methods and Results supply the nrfAH computational-capacity evidence; no expression-module claim is made. |

## Scientific And Domain Assessments

### Study population, setting and source identity

identity: supported. Targets: CommunityMech:000244.

The record denotes the laboratory anammox enrichment in the verified publication. Its provenance from a natural inoculum does not make this a survey of an undisturbed habitat. The perturbation/recovery trajectory and engineered setting are clear.

### Two broad taxonomic entries

grounding: concern. Targets: CommunityMech:000244.

Encoded NCBI labels and GTDB ranks are coherent. The primary source supplies more precise Brocadia/MAG identities than the phylum/domain placeholders, and functional role lists are absent. Genus/species or MAG promotion requires exact source-supported mapping.

### ecological_interactions[0]: Nutrient-Acquisition Core Selection

graph: supported. Targets: CommunityMech:000244.

Transporter enrichment is retained as inferred nutrient-acquisition potential. No complementary partitioning is asserted.

Unrestricted community scope; implicitly includes both declared groups. No pairwise direction. Source: metabolic selection results. Exact short source quotation/locator is preserved in the linked evidence item.

### ecological_interactions[1]: Brocadia Ammonium-Nitrite Anammox

graph: supported. Targets: CommunityMech:000244.

The qualified Brocadia pathway and measured reactor phenotype are supported.

Participating taxon NCBITaxon203682 is a broad placeholder for Brocadia; direction ammonium/nitrite use in nitrogen removal. Source: metabolic profiles and Figure8. Exact short source quotation/locator is preserved in the linked evidence item.

### ecological_interactions[2]: Core DNRA Nitrite Reduction Capacity

graph: supported. Targets: CommunityMech:000244.

nrfAH-based potential is appropriately distinguished from realized flux.

Participating taxon NCBITaxon2 denotes the DNRA guild broadly; direction nitrite to ammonium. Source: metabolic-analysis Methods. Exact short source quotation/locator is preserved in the linked evidence item.

### ecological_interactions[3]: Pre-Crash DNRA Bacterial Replication

graph: supported. Targets: CommunityMech:000244.

PARTIAL computational evidence correctly describes candidate influences from iRep and abundance estimates.

Source taxon Bacteria guild toward target Planctomycetota/Brocadia. This is inferential competitive direction, not demonstrated antagonism. Source: Table2 and destabilization results. Exact short source quotation/locator is preserved in the linked evidence item.

### ecological_interactions[4]: Candidate DNRA Competition During Anammox Destabilization

graph: supported. Targets: CommunityMech:000244.

The candidate competition node preserves the pathway assumption and alternative mechanism.

Source DNRA guild toward target Brocadia, competition for nitrite proposed within this reactor. Source: destabilization results and Discussion. Exact short source quotation/locator is preserved in the linked evidence item.

### ecological_interactions[1].downstream[0]

graph: supported. Targets: CommunityMech:000244.

The arrow remains a qualified hypothesis or partial inference; it does not establish the cause of the crash.

From Brocadia Ammonium-Nitrite Anammox to Candidate DNRA Competition During Anammox Destabilization. HYPOTHESIZED - anammox depends on nitrite, so a guild diverting nitrite could limit its substrate supply; this vulnerability does not by itself establish the cause of the observed crash. Participants: DNRA guild and Brocadia represented at domain/phylum rank. Direction is a proposed upstream vulnerability/capacity/replication association leading to candidate competition in this reactor, not a workflow edge. Source locators and short verbatim snippets in linked evidence.

### ecological_interactions[2].downstream[0]

graph: supported. Targets: CommunityMech:000244.

The arrow remains a qualified hypothesis or partial inference; it does not establish the cause of the crash.

From Core DNRA Nitrite Reduction Capacity to Candidate DNRA Competition During Anammox Destabilization. HYPOTHESIZED - if nrfAH-bearing bacteria use the DNRA route, their nitrite consumption could divert substrate from anammox while retaining fixed nitrogen as ammonium. Alternative partial-denitrification routes remain possible. Participants: DNRA guild and Brocadia represented at domain/phylum rank. Direction is a proposed upstream vulnerability/capacity/replication association leading to candidate competition in this reactor, not a workflow edge. Source locators and short verbatim snippets in linked evidence.

### ecological_interactions[3].downstream[0]

graph: supported. Targets: CommunityMech:000244.

The arrow remains a qualified hypothesis or partial inference; it does not establish the cause of the crash.

From Pre-Crash DNRA Bacterial Replication to Candidate DNRA Competition During Anammox Destabilization. PARTIAL - inferred replication and abundance changes preceding collapse support candidate competitors, but do not demonstrate that their growth caused the loss of anammox performance. Participants: DNRA guild and Brocadia represented at domain/phylum rank. Direction is a proposed upstream vulnerability/capacity/replication association leading to candidate competition in this reactor, not a workflow edge. Source locators and short verbatim snippets in linked evidence.

### Description, taxon notes and nitrate relevance

evidence: concern. Targets: CommunityMech:000244.

Unqualified outcompetition/cause statements and characterization of DNRA as nitrogen removal overstate the full-text interpretation and conflict with the carefully qualified graph. DNRA retains fixed nitrogen.

### Medium, reactor and operating history

scope: concern. Targets: CommunityMech:000244.

Parameters agree with Methods, but the source itself conflicts on the HRT-change and first reseeding dates. The record should identify the chosen source section and retain both alternatives. No media formulation is inferred from uninspected supplements.

### Environment, performance factor and metals

representation: concern. Targets: CommunityMech:000244.

Laboratory/bioreactor grounding is appropriate. The single factor is a performance trajectory rather than an environmental condition. Absence of a metal-processing role does not assert that trace metals were absent; the record already describes their adjustment.

### associated_datasets and media linkages

completeness: concern. Targets: CommunityMech:000244.

Verified publication-linked BioProject and Figshare resources are absent from the target dataset list. Media components have CHEBI grounding but no CultureMech/MediaIngredientMech links. Missing links must not be replaced with approximate formulations.

### History, discussion and reference cache

provenance: concern. Targets: CommunityMech:000244.

The existing discussion preserves a meaningful pathway-choice question. Sidecars pass and graph decisions explain prior qualification. Cache frontmatter incorrectly describes the appended full-text content.

### Focused native validation and limitations

schema: supported. Targets: CommunityMech:000244.

All eight focused/history/preflight commands pass.11 ontology labels and23 snippets verify. Required corpus checks retain their real warning exits; optional expression adapter is unavailable and primary-source fallback is explicit.

### Native metrics

completeness: concern. Targets: CommunityMech:000244.

Completeness35 and capped validation quality100 quantify representation only. They do not override the major causal-summary finding.

## Findings

### causal-overstatement: Summary overstates DNRA causation

major / open / confirmed; issue key: cm-000244-causal-overstatement.

The top-level description and ancillary notes state established outcompetition and causation, while the full text conditions DNRA dominance on pathway preference and retains an alternative. Calling DNRA nitrogen removal also obscures nitrogen retention.

### member-resolution: Source member identities and roles are incompletely represented

minor / open / confirmed; issue key: cm-000244-member-resolution.

The broad placeholders omit source-reported Brocadia/MAG distinctions and both role lists. Their labels are valid; this is incomplete identity resolution, not an ontology label error.

### operating-date-conflict: Source operating dates conflict

minor / open / confirmed; issue key: cm-000244-operating-date-conflict.

The target silently follows Methods for two dates that disagree with Results. The earlier graph decision already acknowledges this unresolved conflict.

### missing-datasets: Verified source datasets are not linked

minor / open / confirmed; issue key: cm-000244-missing-datasets.

associated_datasets is empty although the source explicitly links PRJNA511011 and Figshare59324, both independently resolved.

### media-linkages: Media lacks external linkage identifiers

minor / open / confirmed; issue key: cm-000244-media-linkages.

CHEBI-grounded components are present but external media/ingredient linkage IDs are absent.

### outcome-factor: Performance trajectory is encoded as an environmental factor

minor / open / confirmed; issue key: cm-000244-outcome-factor.

The sole factor describes stable/destabilized/recovered performance rather than a supplied condition. Existing cultivation fields already hold operating context.

### cache-content-type: Cache content-type metadata is stale

minor / open / confirmed; issue key: cm-000244-cache-content-type.

The Markdown cache declares abstract_only although full text is appended. This can mislead future evidence routing; independently retrieved full text verifies the source.

## Recommended Actions And Acceptance Checks

### fix-causal-overstatement

Align summary and ancillary claims with the graph’s conditional interpretation and distinguish nitrogen retention from removal.

- No unqualified causal competition claim remains.
- Alternative pathway explanation and evidence tier are retained.
- Run strict and reference validation.

### fix-member-resolution

Reconcile exact study genome identities and justified roles while preserving MAG uncertainty and source-specific membership.

- Do not map all Bacteria or Planctomycetota to the guild function.
- Any narrower NCBI/GTDB mapping is independently verified.
- Run ontology, GTDB and evidence gates.

### fix-operating-date-conflict

State the selected section and both conflicting source dates without inventing a resolution.

- Both HRT-change and reseeding discrepancies are explicit.
- No unsupported corrected date is introduced.

### fix-missing-datasets

Add source-matched dataset records after confirming the appropriate schema representation.

- Project identities and study relevance remain explicit.
- Do not claim individual sample/file reconciliation unless performed.
- Run strict and reference checks.

### fix-media-linkages

Assess exact existing media/ingredient matches; retain unmatched state where no exact identity is supported.

- No approximate medium is assigned an exact identifier.
- Any accepted cross-reference resolves and matches composition.

### fix-outcome-factor

Represent the trajectory with the study outcome/temporal context and avoid conflating it with environmental inputs.

- Supported temporal sequence is retained.
- No unreported environmental parameter is invented.
- Run strict validation.

### fix-cache-content-type

Reconcile cache metadata with the actual content while preserving source boundaries.

- Abstract/full-text provenance is accurate.
- No supplement is inserted into the article cache.
- Reference validation still passes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml; Whole target, five nodes and three downstream arrows | supports | Laboratory enrichment followed across destabilization and recovery. Two broad taxonomy entries stand for the anammox organism and DNRA guild; no defined isolate mixture is claimed. |
| primary | PMID:31980038; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6982389/fullTextXML; Results, Discussion, Conclusions, Methods and data availability | supports | Primary article read in full for these sections, including table text and figure captions. Conditional genomic explanation of instability is distinguished from measured reactor performance. Figures and supplements themselves were not inspected. |
| conditional | PMID:31980038; Discussion: two alternative nitrogen-metabolism scenarios; Results: investigating performance destabilization | supports | DNRA dominance depends on inferred pathway choice. Partial denitrification with nitric-oxide loss is an alternative; replication and compositional trends do not isolate causation. |
| members | PMID:31980038; Results: metagenomic sequencing, destabilization analysis, Table 2 and core anammox community | supports | The source identifies Brocadia LAC_PLT02 and multiple candidate Chloroflexi/ Ignavibacteria genomes. The current broad phylum/domain terms are incomplete member descriptors, not evidence that all members of those taxa have the assigned functions. |
| timing | PMID:31980038; Results: Bioreactor performance versus Methods: Bioreactor operation | supports | Results places the HRT change after day103 and first reseeding on day145; Methods gives day145 for HRT change and day147 for reseeding. The target follows Methods but does not retain this conflict. |
| operation | PMID:31980038; Methods: Bioreactor operation | supports | Recorded reactor type, medium components, operating parameters, inoculum source and retention regimes match Methods. Temperature control is distinct from the passive pH outcome. Conflicting event dates require qualification. |
| genes | PMID:31980038; Methods: Metabolic analysis and Results: investigating performance destabilization | supports | nrfAH annotations define potential nitrite-to-ammonium capacity. They are computational pathway evidence, not expression, direct flux, or necessity measurements. |
| selection | PMID:31980038; Results: Analysis of metabolic selection | supports | Transporter module enrichment supports inferred acquisition potential in the mature community; it does not demonstrate niche partitioning or transfer. |
| replication | PMID:31980038; Results: investigating performance destabilization, Figure8 caption and Table2; Methods: post-binning analysis | supports | Two genomes satisfy changes consistently across reference frames; three additional genomes satisfy some comparisons. iRep and log-ratio evidence support candidate influences, not an intervention establishing cause. |
| anammox | PMID:31980038; Results: metabolic profiles and Figure8 caption; Background | supports | Measured reactor nitrogen removal and recovered Brocadia pathway capacity support the qualified anammox node. They do not assign every unit of reactor flux to a fully resolved strain. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=31980038&amp;retmode=xml; Independently retrieved primary metadata | supports | PMID and DOI identify the cited article. |
| crossref | https://api.crossref.org/works/10.1186/s40168-020-0786-3; Independently retrieved primary metadata | supports | PMID and DOI identify the cited article. |
| bioproject | https://www.ncbi.nlm.nih.gov/bioproject/PRJNA511011; Independently retrieved primary metadata | supports | PRJNA511011 resolves to the anammox anaerobic membrane bioreactor study. |
| figshare | https://api.figshare.com/v2/projects/59324; Independently retrieved primary metadata | supports | Figshare project59324 resolves to Anammox Bioreactor data from the Alvarez-Cohen group. Individual deposited files were not audited. |
| ontology | OAK local NCBITaxon, ENVO, CHEBI and GO SQLite snapshots; All11 unique curated ontology pairs | supports | Every encoded identifier resolves with its canonical label. Rank-level GTDB checks pass but do not identify exact study genomes. |
| snippets | kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml; All23 evidence snippets | supports | All23 match independently fetched full text or PubMed after NFKC/whitespace normalization with inline XML text joined correctly. The initial naive XML joining caused four artificial misses; corrected paragraph checks resolve them. |
| history | reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml; Target row plus two history/records/Anammox_Bioreactor_DNRA_Destabilization_Community sidecars | supports | Prior graph curation qualified the five nodes and three arrows and noted the source date conflict. It expressly excluded non-graph metadata from certification. Both sidecars validate; this review changes no history. |
| local-search | references_cache; history; reports/causal_graph_review/decisions; kb/taxa; PMID and filename search, including ignored/hidden files | supports | Located both article caches, two sidecars and prior decision. No matching reusable taxon entry was returned in the searched taxon tree; no universal absence claim is made. |
| cache | references_cache/PMID_31980038.md; Frontmatter and appended full-text marker | supports | The cache header says abstract_only despite containing appended Europe PMC full text. The TXT sibling contains the abstract. Review support uses independently fetched primary XML; caches remain unchanged. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml; Actual execution 2026-10-20T07:26:44.883879+00:00 to 2026-10-20T07:26:45.645572+00:00 | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-strict kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml --out /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv; Actual execution 2026-10-20T07:26:44.884070+00:00 to 2026-10-20T07:26:47.730292+00:00 | supports | uv run python scripts/validate_strict.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml --out /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-terms kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml; Actual execution 2026-10-20T07:26:44.884170+00:00 to 2026-10-20T07:26:47.224452+00:00 | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml; Actual execution 2026-10-20T07:26:45.645901+00:00 to 2026-10-20T07:26:45.747185+00:00 | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb-domain kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml; Actual execution 2026-10-20T07:26:45.747571+00:00 to 2026-10-20T07:26:47.929695+00:00 | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-history history/records/Anammox_Bioreactor_DNRA_Destabilization_Community; Actual execution 2026-10-20T07:26:47.224717+00:00 to 2026-10-20T07:26:48.432386+00:00 | supports | No issues found |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-20T07:26:48.432974+00:00 to 2026-10-20T07:26:48.494492+00:00 | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-references-explained kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml; Actual execution 2026-10-20T07:26:48.494708+00:00 to 2026-10-20T07:26:50.343964+00:00 | supports | Validating kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv audit-network; Actual finish 2026-10-20T07:08:14.467705+00:00 | supports | Correct batch03 PYTHONPATH corpus run:477 records,57 warnings in21 records,zero errors;exit1. Selected target has no reported warning. Reused actual run; canonical inputs unchanged. |
| check-check-network-quality | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv check-network-quality; Actual finish 2026-10-20T07:08:13.673449+00:00 | supports | Correct batch03 PYTHONPATH corpus run:477 records,57 warnings in21 records,zero errors;exit1. Selected target has no reported warning. Reused actual run; canonical inputs unchanged. |

## Limits And Additional Notes

- Supplementary files, rendered figure images and raw genomic data were not audited; no complete study reproduction is claimed.
- BioProject and Figshare project identity verified; individual files and sample-to-MAG mappings were not reconciled.
- Structured expression runner unavailable in bounded search; source gene annotations support computational capacity only.
- Source Results/Methods date conflict remains unresolved.
- Corpus network gates exited1 with warnings; selected target is not listed among warnings.
- Broad ontology/GTDB labels are valid but do not identify exact study organisms.
- Canonical records,caches,history and generated outputs unchanged.
- Original naive XML snippet scan retained; corrected inline paragraph joining and PubMed punctuation resolve all23 snippets.
- Short verbatim source quotes total22 words across the primary article.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T073134Z-anammox-dnra-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Anammox DNRA community: whole-record source review'
started_at: '2026-10-20T07:26:41.223800Z'
finished_at: '2026-10-20T07:31:34.589617Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: No target changes this session; prior codex curation prevents
    a person-level independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Full primary-source review supports the qualified five-node/three-arrow graph
  but identifies one major summary-level causal overstatement and six minor completeness/provenance
  issues. All eight focused checks pass;11 ontology labels and23 snippets verify.
  Corpus warnings and optional adapter unavailability remain explicit.
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
  - path: history/records/Anammox_Bioreactor_DNRA_Destabilization_Community/2026-10-02T051803Z-codex-2e76f3.yaml
    sha256: 89e6283370f35408bb949542aa6ddde2cc62348cac52d912a9583e7891623ea0
    role: context
  - path: history/records/Anammox_Bioreactor_DNRA_Destabilization_Community/2026-10-05T084244Z-codex-9efb26.yaml
    sha256: 30c7490ea84166122ff71efbce1b8663ed0493445c49028319aab5e25774aaf0
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    sha256: 7fbf28a70189f8d6c53903fc8b618889fd2c31cfa8e5f79246a9fc22e108978b
    role: target
  - path: references_cache/PMID_31980038.md
    sha256: 7e94ca9771c243435559d8009126e13b591052232555dc699fe80a5ad6e9d410
    role: context
  - path: references_cache/PMID_31980038.txt
    sha256: e6b08bee2033c4f53d37b77eaed904b8c68eec06fea3d4093015ec841c3b2e90
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
    sha256: e21a355f676730e8e7e6de6ea663017c9b09e05a824ff383a272ab9f1399fd70
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
- target_id: CommunityMech:000244
  path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  label: Anammox Bioreactor DNRA Destabilization Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
scope:
  description: Whole record, all five nodes and three arrows, taxonomy, environment/cultivation,23
    snippets, resources, history and discussion. Main-text source review; no supplementary-file
    or image-geometry certification.
  selection: Fourth uncovered record in batch03 path order after excluding validated
    baseline and pending batches01/02.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000244
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml'
  target_ids:
  - CommunityMech:000244
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history or read-only cache-name preflight; cache hashes
    unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml\
    \ --out /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv"
  target_ids:
  - CommunityMech:000244
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    --out /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history or read-only cache-name preflight; cache hashes
    unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000244
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history or read-only cache-name preflight; cache hashes
    unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000244
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history or read-only cache-name preflight; cache hashes
    unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml'
  target_ids:
  - CommunityMech:000244
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history or read-only cache-name preflight; cache hashes
    unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: No issues found
  target_ids:
  - CommunityMech:000244
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Anammox_Bioreactor_DNRA_Destabilization_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history or read-only cache-name preflight; cache hashes
    unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Command completed without reported issues.
  target_ids:
  - CommunityMech:000244
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history or read-only cache-name preflight; cache hashes
    unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: "Validating kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000244
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history or read-only cache-name preflight; cache hashes
    unchanged.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Correct batch03 PYTHONPATH corpus run:477 records,57 warnings in21 records,zero
    errors;exit1. Selected target has no reported warning. Reused actual run; canonical
    inputs unchanged.
  target_ids:
  - CommunityMech:000244
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Corpus warning result retained; not a target scientific approval.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Correct batch03 PYTHONPATH corpus run:477 records,57 warnings in21 records,zero
    errors;exit1. Selected target has no reported warning. Reused actual run; canonical
    inputs unchanged.
  target_ids:
  - CommunityMech:000244
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Corpus warning result retained; not a target scientific approval.
- check_id: structured-expression-adapter
  name: Structured expression adapter availability
  status: unavailable
  required: false
  summary: command -v kg-microbe-sources returned no executable; ignored-inclusive
    search of /Users/marcin/Documents/VIMSS/ontology/culturebotai-claw and /Users/marcin/Documents/VIMSS/ontology/Mechs/culturebotai-claw
    found both expected roots absent. This bounded runner search does not establish
    machine-wide absence. Primary Methods and Results supply the nrfAH computational-capacity
    evidence; no expression-module claim is made.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - genes
  - primary
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  locator: Whole target, five nodes and three downstream arrows
  summary: Laboratory enrichment followed across destabilization and recovery. Two
    broad taxonomy entries stand for the anammox organism and DNRA guild; no defined
    isolate mixture is claimed.
  support: supports
  accessed_at: '2026-10-20T07:31:34.588234Z'
- evidence_id: primary
  kind: primary_source
  reference: PMID:31980038
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6982389/fullTextXML;
    Results, Discussion, Conclusions, Methods and data availability
  summary: Primary article read in full for these sections, including table text and
    figure captions. Conditional genomic explanation of instability is distinguished
    from measured reactor performance. Figures and supplements themselves were not
    inspected.
  support: supports
  accessed_at: '2026-10-20T07:27:12.905939Z'
  snapshot_sha256: 3502acef5bc0a46ec820d0a955b82cb9f892ccaf2f0413da7a910de5434f7078
- evidence_id: conditional
  kind: primary_source
  reference: PMID:31980038
  locator: 'Discussion: two alternative nitrogen-metabolism scenarios; Results: investigating
    performance destabilization'
  summary: DNRA dominance depends on inferred pathway choice. Partial denitrification
    with nitric-oxide loss is an alternative; replication and compositional trends
    do not isolate causation.
  support: supports
  accessed_at: '2026-10-20T07:27:12.905939Z'
  quote: Under this assumption
- evidence_id: members
  kind: primary_source
  reference: PMID:31980038
  locator: 'Results: metagenomic sequencing, destabilization analysis, Table 2 and
    core anammox community'
  summary: The source identifies Brocadia LAC_PLT02 and multiple candidate Chloroflexi/
    Ignavibacteria genomes. The current broad phylum/domain terms are incomplete member
    descriptors, not evidence that all members of those taxa have the assigned functions.
  support: supports
  accessed_at: '2026-10-20T07:27:12.905939Z'
- evidence_id: timing
  kind: primary_source
  reference: PMID:31980038
  locator: 'Results: Bioreactor performance versus Methods: Bioreactor operation'
  summary: Results places the HRT change after day103 and first reseeding on day145;
    Methods gives day145 for HRT change and day147 for reseeding. The target follows
    Methods but does not retain this conflict.
  support: supports
  accessed_at: '2026-10-20T07:27:12.905939Z'
- evidence_id: operation
  kind: primary_source
  reference: PMID:31980038
  locator: 'Methods: Bioreactor operation'
  summary: Recorded reactor type, medium components, operating parameters, inoculum
    source and retention regimes match Methods. Temperature control is distinct from
    the passive pH outcome. Conflicting event dates require qualification.
  support: supports
  accessed_at: '2026-10-20T07:27:12.905939Z'
- evidence_id: genes
  kind: primary_source
  reference: PMID:31980038
  locator: 'Methods: Metabolic analysis and Results: investigating performance destabilization'
  summary: nrfAH annotations define potential nitrite-to-ammonium capacity. They are
    computational pathway evidence, not expression, direct flux, or necessity measurements.
  support: supports
  accessed_at: '2026-10-20T07:27:12.905939Z'
  quote: using the nrfAH enzymes
- evidence_id: selection
  kind: primary_source
  reference: PMID:31980038
  locator: 'Results: Analysis of metabolic selection'
  summary: Transporter module enrichment supports inferred acquisition potential in
    the mature community; it does not demonstrate niche partitioning or transfer.
  support: supports
  accessed_at: '2026-10-20T07:27:12.905939Z'
  quote: may be a selective driver
- evidence_id: replication
  kind: primary_source
  reference: PMID:31980038
  locator: 'Results: investigating performance destabilization, Figure8 caption and
    Table2; Methods: post-binning analysis'
  summary: Two genomes satisfy changes consistently across reference frames; three
    additional genomes satisfy some comparisons. iRep and log-ratio evidence support
    candidate influences, not an intervention establishing cause.
  support: supports
  accessed_at: '2026-10-20T07:27:12.905939Z'
  quote: likely influenced the destabilization event
- evidence_id: anammox
  kind: primary_source
  reference: PMID:31980038
  locator: 'Results: metabolic profiles and Figure8 caption; Background'
  summary: Measured reactor nitrogen removal and recovered Brocadia pathway capacity
    support the qualified anammox node. They do not assign every unit of reactor flux
    to a fully resolved strain.
  support: supports
  accessed_at: '2026-10-20T07:27:12.905939Z'
  quote: conversion of ammonium and nitrite
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=31980038&retmode=xml
  locator: Independently retrieved primary metadata
  summary: PMID and DOI identify the cited article.
  support: supports
  accessed_at: '2026-10-20T07:27:12.906518Z'
  snapshot_sha256: ce05e95a3c14beec939f0455f865cc28388f73a10475084af5236f769bc2c7fa
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1186/s40168-020-0786-3
  locator: Independently retrieved primary metadata
  summary: PMID and DOI identify the cited article.
  support: supports
  accessed_at: '2026-10-20T07:27:12.906638Z'
  snapshot_sha256: 107fa8f71b3357a3931284706b080debaf6b9fdcac6fa496ce54fe1038538471
- evidence_id: bioproject
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA511011
  locator: Independently retrieved primary metadata
  summary: PRJNA511011 resolves to the anammox anaerobic membrane bioreactor study.
  support: supports
  accessed_at: '2026-10-20T07:28:01.696416Z'
  snapshot_sha256: c523332efb8038a61170e608a1f51054ad3d9ad5104721390fb54edd17f3f921
- evidence_id: figshare
  kind: database
  reference: https://api.figshare.com/v2/projects/59324
  locator: Independently retrieved primary metadata
  summary: Figshare project59324 resolves to Anammox Bioreactor data from the Alvarez-Cohen
    group. Individual deposited files were not audited.
  support: supports
  accessed_at: '2026-10-20T07:28:01.699285Z'
  snapshot_sha256: 5fd74c2a37f7d9bb0a7f9456031a42f6c284d4cfa7bb1e7f8a45d486d7785e7f
- evidence_id: ontology
  kind: authority
  reference: OAK local NCBITaxon, ENVO, CHEBI and GO SQLite snapshots
  locator: All11 unique curated ontology pairs
  summary: Every encoded identifier resolves with its canonical label. Rank-level
    GTDB checks pass but do not identify exact study genomes.
  support: supports
  accessed_at: '2026-10-20T07:31:34.588558Z'
  snapshot_sha256: 79938e6bc4d41b00542db441f47d1698e2c7ec4554a75aa62c90e46d2ffdcc33
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  locator: All23 evidence snippets
  summary: All23 match independently fetched full text or PubMed after NFKC/whitespace
    normalization with inline XML text joined correctly. The initial naive XML joining
    caused four artificial misses; corrected paragraph checks resolve them.
  support: supports
  accessed_at: '2026-10-20T07:31:34.588598Z'
  snapshot_sha256: ec0075e5f0d56298377acc85b6be6053410b91a4db420b22c8221df72bf79a6f
- evidence_id: history
  kind: record_content
  reference: reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
  locator: Target row plus two history/records/Anammox_Bioreactor_DNRA_Destabilization_Community
    sidecars
  summary: Prior graph curation qualified the five nodes and three arrows and noted
    the source date conflict. It expressly excluded non-graph metadata from certification.
    Both sidecars validate; this review changes no history.
  support: supports
  accessed_at: '2026-10-20T07:31:34.588599Z'
- evidence_id: local-search
  kind: search
  reference: references_cache; history; reports/causal_graph_review/decisions; kb/taxa
  locator: PMID and filename search, including ignored/hidden files
  summary: Located both article caches, two sidecars and prior decision. No matching
    reusable taxon entry was returned in the searched taxon tree; no universal absence
    claim is made.
  support: supports
  accessed_at: '2026-10-20T07:31:34.588639Z'
  search_scope: rg --no-ignore --hidden -l with PMID31980038 and target filename across
    the four named trees
  snapshot_sha256: a29ffc2958a1caf24e5cdd4792345c7330644eda1b02ab57809fc063d4af3d7b
- evidence_id: cache
  kind: record_content
  reference: references_cache/PMID_31980038.md
  locator: Frontmatter and appended full-text marker
  summary: The cache header says abstract_only despite containing appended Europe
    PMC full text. The TXT sibling contains the abstract. Review support uses independently
    fetched primary XML; caches remain unchanged.
  support: supports
  accessed_at: '2026-10-20T07:31:34.588641Z'
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  locator: Actual execution 2026-10-20T07:26:44.883879+00:00 to 2026-10-20T07:26:45.645572+00:00
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml'
  support: supports
  accessed_at: '2026-10-20T07:26:45.645572Z'
  snapshot_sha256: 108b87b1e5ac0eebf0f2ba8c6cb886f045fb2202724e02f63c555ea0d77cdf05
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    --out /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv
  locator: Actual execution 2026-10-20T07:26:44.884070+00:00 to 2026-10-20T07:26:47.730292+00:00
  summary: "uv run python scripts/validate_strict.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml\
    \ --out /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-03/000244/strict-report.tsv"
  support: supports
  accessed_at: '2026-10-20T07:26:47.730292Z'
  snapshot_sha256: 1a9a3e5f50205e4056443604b00ae20e516034d6fe76944c4a26a8d1a31c75e6
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  locator: Actual execution 2026-10-20T07:26:44.884170+00:00 to 2026-10-20T07:26:47.224452+00:00
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-10-20T07:26:47.224452Z'
  snapshot_sha256: b63432443988e849d52a46e561f7415bf01a3f75d3bb57f587ff1758019ebca2
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  locator: Actual execution 2026-10-20T07:26:45.645901+00:00 to 2026-10-20T07:26:45.747185+00:00
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-10-20T07:26:45.747185Z'
  snapshot_sha256: 03adc8a9881f5b7e8f2e0caa1740a6153830c9c57abed2d19dbea99d6b38db3b
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  locator: Actual execution 2026-10-20T07:26:45.747571+00:00 to 2026-10-20T07:26:47.929695+00:00
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml'
  support: supports
  accessed_at: '2026-10-20T07:26:47.929695Z'
  snapshot_sha256: 6848083b0bc6a3bc9febf944877de4be9b29d651736ed02fc523d3992a9590a1
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Anammox_Bioreactor_DNRA_Destabilization_Community
  locator: Actual execution 2026-10-20T07:26:47.224717+00:00 to 2026-10-20T07:26:48.432386+00:00
  summary: No issues found
  support: supports
  accessed_at: '2026-10-20T07:26:48.432386Z'
  snapshot_sha256: aac9dc34eda558730eeaa8268aa80633d8b9bcf0e7c5be2be19716b036b17d1c
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-20T07:26:48.432974+00:00 to 2026-10-20T07:26:48.494492+00:00
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-10-20T07:26:48.494492Z'
  snapshot_sha256: a86d79f4da9f604294afc7b618cab105f7d8b86c845340088ea27276cf328c3d
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
  locator: Actual execution 2026-10-20T07:26:48.494708+00:00 to 2026-10-20T07:26:50.343964+00:00
  summary: "Validating kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-10-20T07:26:50.343964Z'
  snapshot_sha256: 8ef4da2f530840fcb0fe2eb44b884ed6c29bce2536220706b6c2e39b9bd84b82
- evidence_id: check-audit-network
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  locator: Actual finish 2026-10-20T07:08:14.467705+00:00
  summary: Correct batch03 PYTHONPATH corpus run:477 records,57 warnings in21 records,zero
    errors;exit1. Selected target has no reported warning. Reused actual run; canonical
    inputs unchanged.
  support: supports
  accessed_at: '2026-10-20T07:08:14.467705Z'
  snapshot_sha256: e2122e512641be2226ad12ab146b2c8f7d1e153f1211745e4816457834a42667
- evidence_id: check-check-network-quality
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  locator: Actual finish 2026-10-20T07:08:13.673449+00:00
  summary: Correct batch03 PYTHONPATH corpus run:477 records,57 warnings in21 records,zero
    errors;exit1. Selected target has no reported warning. Reused actual run; canonical
    inputs unchanged.
  support: supports
  accessed_at: '2026-10-20T07:08:13.673449Z'
  snapshot_sha256: b0cb58371a5a771dcbd671952ee68dfe5f26169d08240b66162aa83580fb5229
assessments:
- assessment_id: identity
  area: identity
  topic: Study population, setting and source identity
  outcome: supported
  summary: The record denotes the laboratory anammox enrichment in the verified publication.
    Its provenance from a natural inoculum does not make this a survey of an undisturbed
    habitat. The perturbation/recovery trajectory and engineered setting are clear.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - primary
  - pubmed
  - crossref
  dimensions:
  - name: source_strain
    value: Brocadia study genome LAC_PLT02; other candidate MAGs
    definition: MAG identities are not cultured-isolate identities.
    evidence_ids:
    - members
  - name: community_scope
    value: Time-series laboratory enrichment
    definition: Not a defined two-organism mixture or pooled unrelated reactor studies.
    evidence_ids:
    - record
    - primary
  - name: experimental_setting
    value: Anaerobic membrane bioreactor
    definition: Laboratory reactor context must accompany claims.
    evidence_ids:
    - operation
  - name: medium
    value: Synthetic wastewater-like medium
    definition: Recorded components and operating conditions refer to this study.
    evidence_ids:
    - operation
  - name: evidence_tier
    value: Measured reactor phenotype plus computational genomic interpretation
    definition: Pathway capacity and replication inference do not establish isolated
      causal effects.
    evidence_ids:
    - primary
    - conditional
    - genes
- assessment_id: taxonomy
  area: grounding
  topic: Two broad taxonomic entries
  outcome: concern
  summary: Encoded NCBI labels and GTDB ranks are coherent. The primary source supplies
    more precise Brocadia/MAG identities than the phylum/domain placeholders, and
    functional role lists are absent. Genus/species or MAG promotion requires exact
    source-supported mapping.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - members
  - ontology
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Nutrient-Acquisition Core Selection'
  outcome: supported
  summary: Transporter enrichment is retained as inferred nutrient-acquisition potential.
    No complementary partitioning is asserted.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - selection
  - primary
  details: 'Unrestricted community scope; implicitly includes both declared groups.
    No pairwise direction. Source: metabolic selection results. Exact short source
    quotation/locator is preserved in the linked evidence item.'
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Brocadia Ammonium-Nitrite Anammox'
  outcome: supported
  summary: The qualified Brocadia pathway and measured reactor phenotype are supported.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - anammox
  - primary
  details: 'Participating taxon NCBITaxon203682 is a broad placeholder for Brocadia;
    direction ammonium/nitrite use in nitrogen removal. Source: metabolic profiles
    and Figure8. Exact short source quotation/locator is preserved in the linked evidence
    item.'
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Core DNRA Nitrite Reduction Capacity'
  outcome: supported
  summary: nrfAH-based potential is appropriately distinguished from realized flux.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - genes
  - primary
  details: 'Participating taxon NCBITaxon2 denotes the DNRA guild broadly; direction
    nitrite to ammonium. Source: metabolic-analysis Methods. Exact short source quotation/locator
    is preserved in the linked evidence item.'
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Pre-Crash DNRA Bacterial Replication'
  outcome: supported
  summary: PARTIAL computational evidence correctly describes candidate influences
    from iRep and abundance estimates.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - replication
  - primary
  details: 'Source taxon Bacteria guild toward target Planctomycetota/Brocadia. This
    is inferential competitive direction, not demonstrated antagonism. Source: Table2
    and destabilization results. Exact short source quotation/locator is preserved
    in the linked evidence item.'
- assessment_id: node-4
  area: graph
  topic: 'ecological_interactions[4]: Candidate DNRA Competition During Anammox Destabilization'
  outcome: supported
  summary: The candidate competition node preserves the pathway assumption and alternative
    mechanism.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - conditional
  - primary
  details: 'Source DNRA guild toward target Brocadia, competition for nitrite proposed
    within this reactor. Source: destabilization results and Discussion. Exact short
    source quotation/locator is preserved in the linked evidence item.'
- assessment_id: edge-1
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: supported
  summary: The arrow remains a qualified hypothesis or partial inference; it does
    not establish the cause of the crash.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - anammox
  - conditional
  details: 'From Brocadia Ammonium-Nitrite Anammox to Candidate DNRA Competition During
    Anammox Destabilization. HYPOTHESIZED - anammox depends on nitrite, so a guild
    diverting nitrite could limit its substrate supply; this vulnerability does not
    by itself establish the cause of the observed crash. Participants: DNRA guild
    and Brocadia represented at domain/phylum rank. Direction is a proposed upstream
    vulnerability/capacity/replication association leading to candidate competition
    in this reactor, not a workflow edge. Source locators and short verbatim snippets
    in linked evidence.'
- assessment_id: edge-2
  area: graph
  topic: ecological_interactions[2].downstream[0]
  outcome: supported
  summary: The arrow remains a qualified hypothesis or partial inference; it does
    not establish the cause of the crash.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - genes
  - conditional
  details: 'From Core DNRA Nitrite Reduction Capacity to Candidate DNRA Competition
    During Anammox Destabilization. HYPOTHESIZED - if nrfAH-bearing bacteria use the
    DNRA route, their nitrite consumption could divert substrate from anammox while
    retaining fixed nitrogen as ammonium. Alternative partial-denitrification routes
    remain possible. Participants: DNRA guild and Brocadia represented at domain/phylum
    rank. Direction is a proposed upstream vulnerability/capacity/replication association
    leading to candidate competition in this reactor, not a workflow edge. Source
    locators and short verbatim snippets in linked evidence.'
- assessment_id: edge-3
  area: graph
  topic: ecological_interactions[3].downstream[0]
  outcome: supported
  summary: The arrow remains a qualified hypothesis or partial inference; it does
    not establish the cause of the crash.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - replication
  - conditional
  details: 'From Pre-Crash DNRA Bacterial Replication to Candidate DNRA Competition
    During Anammox Destabilization. PARTIAL - inferred replication and abundance changes
    preceding collapse support candidate competitors, but do not demonstrate that
    their growth caused the loss of anammox performance. Participants: DNRA guild
    and Brocadia represented at domain/phylum rank. Direction is a proposed upstream
    vulnerability/capacity/replication association leading to candidate competition
    in this reactor, not a workflow edge. Source locators and short verbatim snippets
    in linked evidence.'
- assessment_id: causal-summary
  area: evidence
  topic: Description, taxon notes and nitrate relevance
  outcome: concern
  summary: Unqualified outcompetition/cause statements and characterization of DNRA
    as nitrogen removal overstate the full-text interpretation and conflict with the
    carefully qualified graph. DNRA retains fixed nitrogen.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - conditional
  - genes
  - primary
- assessment_id: cultivation
  area: scope
  topic: Medium, reactor and operating history
  outcome: concern
  summary: Parameters agree with Methods, but the source itself conflicts on the HRT-change
    and first reseeding dates. The record should identify the chosen source section
    and retain both alternatives. No media formulation is inferred from uninspected
    supplements.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - operation
  - timing
  - history
- assessment_id: environment
  area: representation
  topic: Environment, performance factor and metals
  outcome: concern
  summary: Laboratory/bioreactor grounding is appropriate. The single factor is a
    performance trajectory rather than an environmental condition. Absence of a metal-processing
    role does not assert that trace metals were absent; the record already describes
    their adjustment.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - ontology
  - operation
- assessment_id: datasets
  area: completeness
  topic: associated_datasets and media linkages
  outcome: concern
  summary: Verified publication-linked BioProject and Figshare resources are absent
    from the target dataset list. Media components have CHEBI grounding but no CultureMech/MediaIngredientMech
    links. Missing links must not be replaced with approximate formulations.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - bioproject
  - figshare
  - operation
- assessment_id: history
  area: provenance
  topic: History, discussion and reference cache
  outcome: concern
  summary: The existing discussion preserves a meaningful pathway-choice question.
    Sidecars pass and graph decisions explain prior qualification. Cache frontmatter
    incorrectly describes the appended full-text content.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - history
  - cache
- assessment_id: validation
  area: schema
  topic: Focused native validation and limitations
  outcome: supported
  summary: All eight focused/history/preflight commands pass.11 ontology labels and23
    snippets verify. Required corpus checks retain their real warning exits; optional
    expression adapter is unavailable and primary-source fallback is explicit.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - ontology
  - snippets
  - check-validate
  - check-validate-strict
  - check-validate-history
  - check-audit-network
- assessment_id: metrics
  area: completeness
  topic: Native metrics
  outcome: concern
  summary: Completeness35 and capped validation quality100 quantify representation
    only. They do not override the major causal-summary finding.
  target_ids:
  - CommunityMech:000244
  evidence_ids:
  - record
  - check-audit-network
  metrics:
  - name: completeness
    value: 35
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 if all required metadata including every taxon role +5
      environment +10>=3factors +10>=3nodes +5resources +10media +5datasets +5node
      metabolites). Roles absent,one factor,five nodes,resources/media present,datasets
      empty:0+5+0+10+5+10+0+5=35.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50P1-10P2-2P3+20min(mean node evidence/2,1)+15 if native
      COMPLETE,0,100). P1=0,P2=1,P3=6,P4=0;7 items/5 nodes=1.4;both declared taxa
      structurally participate.100-10-12+14+15=107,clamped100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count for this target review.
  - name: P2
    value: 1
    unit: findings
    definition: Native severity count for this target review.
  - name: P3
    value: 6
    unit: findings
    definition: Native severity count for this target review.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count for this target review.
findings:
- finding_id: causal-overstatement
  issue_key: cm-000244-causal-overstatement
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: review-checklist.causal
  status: open
  certainty: confirmed
  title: Summary overstates DNRA causation
  description: The top-level description and ancillary notes state established outcompetition
    and causation, while the full text conditions DNRA dominance on pathway preference
    and retains an alternative. Calling DNRA nitrogen removal also obscures nitrogen
    retention.
  target_ids:
  - CommunityMech:000244
  field_paths:
  - description
  - taxonomy[*].taxon_term.notes
  - related_ingredients[1].relevance
  evidence_ids:
  - record
  - conditional
  - genes
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
- finding_id: member-resolution
  issue_key: cm-000244-member-resolution
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded completeness, representation or provenance
    issue; study identity and qualified graph remain recoverable.'
  rule_id: review-checklist.taxonomy
  status: open
  certainty: confirmed
  title: Source member identities and roles are incompletely represented
  description: The broad placeholders omit source-reported Brocadia/MAG distinctions
    and both role lists. Their labels are valid; this is incomplete identity resolution,
    not an ontology label error.
  target_ids:
  - CommunityMech:000244
  field_paths:
  - taxonomy
  evidence_ids:
  - record
  - members
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
- finding_id: operating-date-conflict
  issue_key: cm-000244-operating-date-conflict
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded completeness, representation or provenance
    issue; study identity and qualified graph remain recoverable.'
  rule_id: review-checklist.cultivation
  status: open
  certainty: confirmed
  title: Source operating dates conflict
  description: The target silently follows Methods for two dates that disagree with
    Results. The earlier graph decision already acknowledges this unresolved conflict.
  target_ids:
  - CommunityMech:000244
  field_paths:
  - growth_media[0].preparation_notes
  - cultivation_setup[0].notes
  evidence_ids:
  - timing
  - history
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
- finding_id: missing-datasets
  issue_key: cm-000244-missing-datasets
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded completeness, representation or provenance
    issue; study identity and qualified graph remain recoverable.'
  rule_id: review-checklist.datasets
  status: open
  certainty: confirmed
  title: Verified source datasets are not linked
  description: associated_datasets is empty although the source explicitly links PRJNA511011
    and Figshare59324, both independently resolved.
  target_ids:
  - CommunityMech:000244
  field_paths:
  - associated_datasets
  evidence_ids:
  - record
  - bioproject
  - figshare
  - primary
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
- finding_id: media-linkages
  issue_key: cm-000244-media-linkages
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded completeness, representation or provenance
    issue; study identity and qualified graph remain recoverable.'
  rule_id: P3.1
  status: open
  certainty: confirmed
  title: Media lacks external linkage identifiers
  description: CHEBI-grounded components are present but external media/ingredient
    linkage IDs are absent.
  target_ids:
  - CommunityMech:000244
  field_paths:
  - growth_media
  evidence_ids:
  - record
  - operation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
- finding_id: outcome-factor
  issue_key: cm-000244-outcome-factor
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded completeness, representation or provenance
    issue; study identity and qualified graph remain recoverable.'
  rule_id: review-checklist.environment
  status: open
  certainty: confirmed
  title: Performance trajectory is encoded as an environmental factor
  description: The sole factor describes stable/destabilized/recovered performance
    rather than a supplied condition. Existing cultivation fields already hold operating
    context.
  target_ids:
  - CommunityMech:000244
  field_paths:
  - environmental_factors[0]
  evidence_ids:
  - record
  - operation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
- finding_id: cache-content-type
  issue_key: cm-000244-cache-content-type
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded completeness, representation or provenance
    issue; study identity and qualified graph remain recoverable.'
  rule_id: review-checklist.audit
  status: open
  certainty: confirmed
  title: Cache content-type metadata is stale
  description: The Markdown cache declares abstract_only although full text is appended.
    This can mislead future evidence routing; independently retrieved full text verifies
    the source.
  target_ids:
  - CommunityMech:000244
  field_paths:
  - references_cache/PMID_31980038.md:content_type
  evidence_ids:
  - cache
  - primary
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_31980038.md
    role: reference_cache
actions:
- action_id: fix-causal-overstatement
  description: Align summary and ancillary claims with the graph’s conditional interpretation
    and distinguish nitrogen retention from removal.
  finding_ids:
  - causal-overstatement
  target_ids:
  - CommunityMech:000244
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
  acceptance_checks:
  - No unqualified causal competition claim remains.
  - Alternative pathway explanation and evidence tier are retained.
  - Run strict and reference validation.
- action_id: fix-member-resolution
  description: Reconcile exact study genome identities and justified roles while preserving
    MAG uncertainty and source-specific membership.
  finding_ids:
  - member-resolution
  target_ids:
  - CommunityMech:000244
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Do not map all Bacteria or Planctomycetota to the guild function.
  - Any narrower NCBI/GTDB mapping is independently verified.
  - Run ontology, GTDB and evidence gates.
- action_id: fix-operating-date-conflict
  description: State the selected section and both conflicting source dates without
    inventing a resolution.
  finding_ids:
  - operating-date-conflict
  target_ids:
  - CommunityMech:000244
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Both HRT-change and reseeding discrepancies are explicit.
  - No unsupported corrected date is introduced.
- action_id: fix-missing-datasets
  description: Add source-matched dataset records after confirming the appropriate
    schema representation.
  finding_ids:
  - missing-datasets
  target_ids:
  - CommunityMech:000244
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Project identities and study relevance remain explicit.
  - Do not claim individual sample/file reconciliation unless performed.
  - Run strict and reference checks.
- action_id: fix-media-linkages
  description: Assess exact existing media/ingredient matches; retain unmatched state
    where no exact identity is supported.
  finding_ids:
  - media-linkages
  target_ids:
  - CommunityMech:000244
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
  acceptance_checks:
  - No approximate medium is assigned an exact identifier.
  - Any accepted cross-reference resolves and matches composition.
- action_id: fix-outcome-factor
  description: Represent the trajectory with the study outcome/temporal context and
    avoid conflating it with environmental inputs.
  finding_ids:
  - outcome-factor
  target_ids:
  - CommunityMech:000244
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Bioreactor_DNRA_Destabilization_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Supported temporal sequence is retained.
  - No unreported environmental parameter is invented.
  - Run strict validation.
- action_id: fix-cache-content-type
  description: Reconcile cache metadata with the actual content while preserving source
    boundaries.
  finding_ids:
  - cache-content-type
  target_ids:
  - CommunityMech:000244
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: references_cache/PMID_31980038.md
    role: reference_cache
  acceptance_checks:
  - Abstract/full-text provenance is accurate.
  - No supplement is inserted into the article cache.
  - Reference validation still passes.
limitations:
- Supplementary files, rendered figure images and raw genomic data were not audited;
  no complete study reproduction is claimed.
- BioProject and Figshare project identity verified; individual files and sample-to-MAG
  mappings were not reconciled.
- Structured expression runner unavailable in bounded search; source gene annotations
  support computational capacity only.
- Source Results/Methods date conflict remains unresolved.
- Corpus network gates exited1 with warnings; selected target is not listed among
  warnings.
- Broad ontology/GTDB labels are valid but do not identify exact study organisms.
notes:
- Canonical records,caches,history and generated outputs unchanged.
- Original naive XML snippet scan retained; corrected inline paragraph joining and
  PubMed punctuation resolve all23 snippets.
- Short verbatim source quotes total22 words across the primary article.
tags:
- record-review
- anammox
- batch-03
```
