# Apple fire blight ANP SynCom: whole-record source review

- Review: 20261021T064512Z-apple-fire-blight-anp-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T06:39:54.731640Z
- Finished UTC: 2026-10-21T06:45:12.289489Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major finding concerns unqualified member-specific antagonist roles. Three minor findings concern the unresolved cross-paper strain correspondence, media identifiers and missing dataset evidence provenance. The two measured endpoint nodes remain sound with existing mechanism qualifications; no causal arrows are warranted. Eight focused checks pass, twelve ontology pairs and thirty snippets verify.

## Scope And Provenance

Entire maintained record, all nine taxa, two endpoint nodes and no arrows, all metadata and thirty evidence occurrences; independent full main articles and public project metadata. Separate supplementary figures/raw data are excluded.

Selection: Next uncovered path after Angelarchaeales in batch03; one resolved maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ade4a9acdc245e1090522bb4f6ec5fe82ee88689.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000377 | kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml | maintained | Apple Fire Blight A+N+P SynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000377 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml |
| validate-strict | passed | True | CommunityMech:000377 | uv run python scripts/validate_strict.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml --out /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000377 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000377 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000377 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml |
| validate-history | passed | True | CommunityMech:000377 | No issues found |
| normalize-cache-names-check | passed | True | CommunityMech:000377 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000377 | Validating kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000377 | Correct batch03 PYTHONPATH corpus run: 477 records, 57 warnings in 21 records, zero errors; exit 1. Target not listed among warnings. Actual earlier execution reused with unchanged canonical inputs. |
| check-network-quality | failed | True | CommunityMech:000377 | Correct batch03 PYTHONPATH corpus run: 477 records, 57 warnings in 21 records, zero errors; exit 1. Target not listed among warnings. Actual earlier execution reused with unchanged canonical inputs. |
| Optional structured source adapter availability | unavailable | False | CommunityMech:000377 | No own-runtime runner. Another checkout has a candidate, which was not executed under isolation. No catalog query occurred; primary-source Methods and genomic interpretation supply the scientific fallback. |

## Scientific And Domain Assessments

### Full ANP formulation and comparator boundaries

identity: supported. Targets: CommunityMech:000377.

The nine-member formulation is resolved from the construction paper. Two A, five N and two P strains define this target; challenge Erwinia and separate tissue/plant/exudate arms are not additional formulation members.

### All nine members, strain descriptors and GTDB status

grounding: supported. Targets: CommunityMech:000377.

Species names and strain designations agree with construction Table 1 and current local NCBI authority. All nine GTDB states are explicitly unresolved; passing GTDB gates do not constitute successful grounding. The 03SUJ4/TAH1 link remains unverified.

### taxonomy[*].functional_role

evidence: concern. Targets: CommunityMech:000377.

All members carry the same antagonist role, but membership snippets support their identity and group selection. Direct inhibition is demonstrated for A members and weakly Kitasatospora; indirect contributions of the other members remain group-level or candidate interpretations.

### taxonomy[*].abundance_level

scope: supported. Targets: CommunityMech:000377.

All DOMINANT values can be read as qualitative prominence in the designed formulation under the current schema. They are not measured abundance or proof of equal cell fractions, and no percentage is inferred.

### ecological_interactions[0]: A+N+P Fire-Blight Severity Reduction in Rosaceae Tissue

graph: supported. Targets: CommunityMech:000377.

Both source-specific disease endpoints support the qualified node. The full ANP arm had the stated fruit and rose disease scores; pathogen eradication or a defined mechanism is not established.

Participants: all nine formulation members plus external E. amylovora TS3128. Direction: ANP treatment toward reduced host-tissue disease score after challenge. Mechanism unresolved. Context and exact source locators are in linked evidence; numerical equality to the chemical control does not prove general equivalence.

### ecological_interactions[1]: A+N+P Erwinia Density Suppression in Flower Exudate

graph: supported. Targets: CommunityMech:000377.

The follow-up supports the ANP-associated decrease in pathogen density. PARTIAL wording correctly leaves resource competition and antibiosis unresolved; retain the separate strain-alias limitation.

Participants: follow-up A/N/P formulation and external E. amylovora TS3128. Direction: treatment-associated reduction of pathogen counts. There is no demonstrated reciprocal cost or isolated metabolite-transfer mechanism. No universal equivalence of Terriglobus 03SUJ4 and TAH1 is inferred.

### ecological_interactions[*].downstream

graph: not_applicable. Targets: CommunityMech:000377.

No downstream arrows exist. The second assay is not causally downstream of the first merely because it was a follow-up study.

### engineering_design and description

scope: supported. Targets: CommunityMech:000377.

Assembly groups and tissue-specific endpoint distinctions are supported. The note correctly separates the ANP plant value from the P-only abstract highlight; source inconsistency for the second plant protocol remains un-reconciled and is not silently propagated.

### Environment, origin, state and category

grounding: supported. Targets: CommunityMech:000377.

SYNTHETIC and ENGINEERED match a designed formulation. Broad plant-associated environment is compatible with multiple Rosaceae tissues, and notes retain the exudate assay. OTHER is not an erroneous rhizosphere assignment.

### growth_media[0:2] and environmental_factors[0]

scope: concern. Targets: CommunityMech:000377.

Source-context conditions and exudate preparation are represented. The first paper also reports R2A with mannitol for member assays; the follow-up preparation note is not a demonstrated contradiction. Keep genome preparation, nutrient-use work and exudate co-culture scoped separately. Named media lack external CultureMech or ingredient linkages.

### associated_datasets and external_resources

provenance: concern. Targets: CommunityMech:000377.

Both PMID/DOI identities and the public source BioProject verify. The dataset evidence object omits evidence_source despite the claim-level curation policy. Project data are endophyte community reads rather than verified strain-genome identities.

### discussions, history and reference caches

provenance: supported. Targets: CommunityMech:000377.

The existing alias and mechanism gaps are concrete and remain unresolved. Four sidecars and inline events preserve prior work; both caches correctly distinguish appended full text and match current primary article snippets.

### metals_present, metal_relevance and metal_notes

scope: supported. Targets: CommunityMech:000377.

No metal-processing function is asserted. Peripheral siderophore screens and predicted biosynthetic clusters do not establish an ecosystem metal/REE mechanism.

### Native and independent checks

schema: supported. Targets: CommunityMech:000377.

Eight focused/history/preflight commands pass, twelve ontology pairs match and thirty snippets verify independently. Corpus warning failures remain actual failures; they are not silently recoded as target scientific success.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000377.

Completeness 75 and quality 100 are mechanical metadata/network scores, not certification of individual roles, strain equivalence or mechanism.

## Findings

### member-role-evidence: Common antagonist role exceeds member-specific evidence

major / open / confirmed; issue key: cm-000377-member-role-evidence.

The record assigns PATHOGEN_ANTAGONIST to all nine members without distinguishing demonstrated direct antagonism, group-level protective performance and the inferred network/pathway roles of individual strains. A positive whole-mixture or group result does not establish every member's causal contribution; absence of direct plate inhibition does not disprove indirect protection.

### alias-qualification: Strain correspondence remains unresolved

minor / open / confirmed; issue key: cm-000377-alias-qualification.

The taxonomy note calls the follow-up Terriglobus genome corresponding while the open discussion correctly asks whether TAH1 and 03SUJ4 are the same strain. The two source names are verified but their equivalence is not.

### media-linkage: Cultivation media lack external identifiers

minor / open / confirmed; issue key: cm-000377-media-linkage.

Two named growth-media entries are present without CultureMech or MediaIngredientMech identifiers. Their evidence and source context remain available.

### dataset-evidence-source: Dataset evidence omits its provenance type

minor / open / confirmed; issue key: cm-000377-dataset-evidence-source.

associated_datasets[0].evidence[0] contains a valid reference and exact matching data-availability excerpt but omits evidence_source. Native schema/reference validation passes; the local claim-level evidence policy still asks for this field.

## Recommended Actions And Acceptance Checks

### fix-member-role-evidence

Attach role-specific evidence and distinguish intended/candidate biocontrol roles from demonstrated member-specific effects; retain supported indirect or collective roles with explicit scope.

- Identity snippets are not the sole support for functional roles.
- Direct antagonism is distinguished from group-level disease protection and inferred ecological contribution.
- No negative plate assay is treated as proof of no possible indirect role.
- Run strict, reference and network checks.

### fix-alias-qualification

Keep both source-specific names and qualify their correspondence explicitly; verify publicly available culture or assembly identifiers before transferring strain-specific follow-up claims.

- No alias is treated as proven without a resolving source.
- The construction formulation remains defined by 03SUJ4.
- The follow-up endpoint retains the unresolved member-provenance limitation.

### fix-media-linkage

Resolve exact compatible medium or ingredient identifiers where available, retaining custom exudate provenance when no exact external recipe exists.

- No approximate recipe is substituted for the actual source preparation.
- Any accepted external identifier resolves to matching formulation/context.
- Leave genuinely unmatched custom media explicit.

### fix-dataset-evidence-source

Add an accurate provenance classification for the source data-availability assertion, retaining the verified accession and exact snippet.

- Evidence-source classification reflects bibliographic/data provenance rather than an invented experiment.
- Schema and reference checks continue to pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml; Entire record: nine member taxa, two endpoint nodes, no downstream arrows, thirty evidence occurrences | supports | The target is the full A+N+P biocontrol formulation, with A-only, N-only and P-only arms retained as experimental comparators. Erwinia is a challenged external participant, not a tenth formulation member. |
| paper-40223277 | PMID:40223277; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12010091/fullTextXML; independently retrieved main article XML, complete Methods, Results and Discussion, table text and figure captions | supports | Primary source inspected for the source-specific formulation, endpoints, interpretation and experimental context. Separate supplementary figures and underlying raw data were not audited. |
| paper-40468884 | PMID:40468884; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12146627/fullTextXML; independently retrieved main article XML, complete Methods, Results and Discussion, table text and figure captions | supports | Primary source inspected for the source-specific formulation, endpoints, interpretation and experimental context. Separate supplementary figures and underlying raw data were not audited. |
| membership | PMID:40223277; Table 1; Results: SynCom Members Acquisition through Microbiome Analysis; Methods: SynCom preparation | supports | The construction paper identifies all nine species/strain combinations and their A/N/P selection groups. N strains are culture-collection proxies selected by microbiome sequence similarity, not demonstrated recovery of those exact strains from every healthy apple. Equal group mixing is not equal dosage of every strain across groups. |
| roles | PMID:40223277; Results: The Varying Anti-E. amylovora Effects of SynCom Member Strains; Discussion | supports | Direct plate inhibition is shown for the two A strains and more weakly Kitasatospora; N/P group biocontrol or network/pathway selection does not identify each member's individual causal contribution. Antagonism can be indirect, but a common unqualified role for all members needs this distinction. |
| fruit | PMID:40223277; Results: SynCom Inhibited the Fire Blight Disease in Apple Fruits; corresponding Methods and Fig 1 caption | supports | The full ANP arm has zero measured disease severity in the stated fruit assay. This is a disease score and not proof that no viable pathogen remained. |
| rose | PMID:40223277; Results: Fire Blight Disease on Flower Was Controlled by the SynCom; corresponding Methods and Fig 2 caption | supports | The full ANP arm and chemical positive control have the same reported disease-severity value in the rose model. Numerical equality here does not establish universal efficacy equivalence. |
| plant | PMID:40223277; Results: SynCom Can Suppress Fire Blight Disease That Occurs in Apple Plants; Discussion; Fig 3 caption | supports | The full ANP value reported in the text is 33.4 percent; 5.4 percent belongs to P alone. The record correctly preserves that distinction. Source prose repeats one numerical vector for the second plant assay while describing contrasting rankings, so the second protocol must not inherit those values as independently reconciled measurements. |
| exudate | PMID:40468884; Methods section 5; Results section 11; Fig 4 caption; Discussion section 12 | supports | The ANP arm shows a negative pathogen-density trajectory during the exudate assay. Substrate use overlap and co-culture counts do not isolate resource depletion from antibiosis or prove reciprocal fitness costs. |
| alias | PMID:40468884; Methods section 2; Table 1; Results section 7 and section 9; compare construction PMID40223277 Table 1 | supports | The follow-up calls Terriglobus aquaticus TAH1 whereas the construction paper names 03SUJ4. These inspected articles do not explicitly establish a strain alias. Existing discussion correctly leaves the question open; taxonomy notes should avoid presenting correspondence as verified. |
| culture | PMID:40468884; Methods section 2 Whole genome sequencing of SynCom strains; section 4 Nutrient utilization assay; section 5 Apple flower exudate nutrient competition assay | supports | The follow-up separates seven N/P genome subjects from previously sequenced A strains, nutrient-use assay preparation and exudate competition. The curated R2A and exudate entries match their source contexts; the broad preparation note should identify the relevant strain set and should not turn one preparation into a universal protocol. |
| mechanism | PMID:40468884; Results sections 8-11; Discussion section 12 | supports | Genome-mined biosynthetic clusters and EC annotations remain candidate functions. The main-text discussion distinguishes direct inhibition from plausible indirect protection; no chemically validated member-level effector or resolved resource-competition mechanism is established. |
| schema | src/communitymech/schema/communitymech.yaml; AbundanceEnum, FunctionalRoleEnum, EvidenceSourceEnum, community and cultivation slots | supports | DOMINANT is ordinal prominence and can denote co-equal members; it is not a measured percentage. PATHOGEN_ANTAGONIST concerns biocontrol and need not mean direct killing. Evidence-source completeness is also a curation-policy requirement in CLAUDE.md. |
| ontology | Local OAK NCBITaxon, ENVO and GO snapshots; Twelve distinct ID-label pairs across 33 occurrences; species-rank metadata | supports | All twelve canonical pairs match. The nine member terms and external Erwinia term denote species; strain resolution is provided by strain_designation and source Table 1,  not species CURIEs. GO0044419 is broad and marked gocheck_do_not_annotate in the source ontology; its use here does not establish a particular mechanism. |
| snippets | kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml; All thirty evidence occurrences against independent article XML and committed source caches | supports | All thirty snippets match both the corresponding cache and independently fetched main article after NFKC/whitespace normalization. No supplement-only evidence was substituted into an article source. Matching words do not validate causal role attribution. |
| 40223277-pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=40223277&amp;retmode=xml; Independent citation metadata | supports | The identifier resolves to the same cited construction paper. |
| 40223277-crossref | https://api.crossref.org/works/10.4014/jmb.2501.01047; Independent citation metadata | supports | The identifier resolves to the same cited construction paper. |
| 40468884-pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=40468884&amp;retmode=xml; Independent citation metadata | supports | The identifier resolves to the same cited follow-up paper. |
| 40468884-crossref | https://api.crossref.org/works/10.5423/PPJ.OA.03.2025.0040; Independent citation metadata | supports | The identifier resolves to the same cited follow-up paper. |
| dataset | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&amp;id=1144217&amp;retmode=xml; BioProject 1144217 title, description, access and data type | supports | Public project metadata concerns endophytic communities in SynCom-treated apple seedlings and raw sequence reads. It supports the record's source-project link, not an assertion that this project contains assemblies of all nine strains. |
| history | history/records/Apple_Fire_Blight_ANP_SynCom; reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml; Four sidecars, inline history, exact target decision row 172-215 | supports | Previous edits separated tissue scores from exudate counts, removed a workflow arrow and retained the strain-alias and effector gaps. Sidecars pass validation. Historical graph review is context rather than independent source support. |
| local-search | references_cache; history; reports/causal_graph_review/decisions; kb/taxa; Identifier/slug search plus separate species-ID/name search, both including hidden and ignored files | supports | The initial bounded search located both article caches, four target history files and a prior decision row. A separate root-agent search of kb/taxa for every member species ID and full species label returned no matches; ignored files were included. No machine-wide absence claim is made. |
| adapter | Optional kg-microbe-sources runner discovery; PATH, task virtualenv/module, named siblings and ignored-inclusive filenames | supports | No runner was available in this task runtime. A candidate in another task checkout was found but not executed under checkout isolation; no iModulon catalog or organism coverage was established. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml; Actual execution 2026-10-21T06:39:56.208924+00:00 to 2026-10-21T06:39:58.202481+00:00 | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-strict kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml --out /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv; Actual execution 2026-10-21T06:39:56.209116+00:00 to 2026-10-21T06:40:02.350636+00:00 | supports | uv run python scripts/validate_strict.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml --out /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-terms kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml; Actual execution 2026-10-21T06:39:56.209192+00:00 to 2026-10-21T06:40:01.014987+00:00 | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml; Actual execution 2026-10-21T06:39:58.202879+00:00 to 2026-10-21T06:39:58.350897+00:00 | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb-domain kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml; Actual execution 2026-10-21T06:39:58.351244+00:00 to 2026-10-21T06:40:02.492449+00:00 | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-history history/records/Apple_Fire_Blight_ANP_SynCom; Actual execution 2026-10-21T06:40:01.015355+00:00 to 2026-10-21T06:40:02.842737+00:00 | supports | No issues found |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T06:40:02.847564+00:00 to 2026-10-21T06:40:02.918242+00:00 | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-references-explained kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml; Actual execution 2026-10-21T06:40:02.919820+00:00 to 2026-10-21T06:40:06.148299+00:00 | supports | Validating kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv audit-network; Actual finish 2026-10-20T07:08:14.467705+00:00 | supports | Correct batch03 PYTHONPATH corpus run: 477 records, 57 warnings in 21 records, zero errors; exit 1. Target not listed among warnings. Actual earlier execution reused with unchanged canonical inputs. |
| check-check-network-quality | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv check-network-quality; Actual finish 2026-10-20T07:08:13.673449+00:00 | supports | Correct batch03 PYTHONPATH corpus run: 477 records, 57 warnings in 21 records, zero errors; exit 1. Target not listed among warnings. Actual earlier execution reused with unchanged canonical inputs. |
| native-target | NetworkIntegrityAuditor().audit_community(target); Independent read-only native API check recorded in support-audit.json | supports | No target network issue returned; all nine formulation members are represented and external challenged Erwinia is not required in membership. Four node evidence items across two nodes give mean 2. |

## Limits And Additional Notes

- The construction target is resolved, but public main-text evidence does not resolve Terriglobus 03SUJ4 versus TAH1; follow-up strain equivalence remains an open question.
- Separate supplementary figures, Table 2 image geometry, raw sequencing reads, assemblies and sample-to-strain reconciliation were not independently audited. Main-text Results supplied the reported inhibition and endpoint interpretations.
- The second plant-assay numerical vector conflicts with the narrative ranking in the source; no reconstruction or new source-specific quantitative assertion is made.
- Member-wise causal contributions, active effectors and resource-competition discrimination remain unresolved; this review is not a cultivation optimization or field-efficacy claim.
- Optional expression adapter was unavailable in the owned runtime; a candidate in another checkout was not executed. No catalog coverage or gene-expression evidence is claimed.
- Required corpus gates retain actual warning failures, with no target issue; metric scores are not scientific approval.
- Canonical records, caches, history and generated outputs remain unchanged.
- Short quotations total 10 words from PMID40223277 and 3 from PMID40468884.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T064512Z-apple-fire-blight-anp-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Apple fire blight ANP SynCom: whole-record source review'
started_at: '2026-10-21T06:39:54.731640Z'
finished_at: '2026-10-21T06:45:12.289489Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Canonical target unchanged in this session; prior codex curation
    prevents person-level independence claim. Separate agents checked ontology/runner
    availability and snippets/dataset/history/native metrics.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: One major finding concerns unqualified member-specific antagonist roles.
  Three minor findings concern the unresolved cross-paper strain correspondence, media
  identifiers and missing dataset evidence provenance. The two measured endpoint nodes
  remain sound with existing mechanism qualifications; no causal arrows are warranted.
  Eight focused checks pass, twelve ontology pairs and thirty snippets verify.
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
  - path: history/records/Apple_Fire_Blight_ANP_SynCom/2026-09-14T214500Z-codex-apple-fire-blight-anp-syncom.yaml
    sha256: 90cff7f1166dcfd260e3450cffadcc72564bb030690a3d8af6c573be6a6ca344
    role: context
  - path: history/records/Apple_Fire_Blight_ANP_SynCom/2026-09-14T215800Z-codex-review.yaml
    sha256: 8faf51de812d3678e62b2e147e914febf5374e756d179d51f9e267af5e942e0a
    role: context
  - path: history/records/Apple_Fire_Blight_ANP_SynCom/2026-10-02T055533Z-codex-afb402.yaml
    sha256: a0fadad8dc11d6ef38d9b62b8c984284b3f00a0e5373272e3b6d84e8b93e4da3
    role: context
  - path: history/records/Apple_Fire_Blight_ANP_SynCom/2026-10-05T084242Z-codex-4f54a1.yaml
    sha256: 070a6795214a7a1f935e84f230b2c4fd11e057587c25417453455920ea604591
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    sha256: 1f2e836d0bcd5ff68622188aa5eff6d82b0d7c30d9c1a0b6191ea52f0a8e0a94
    role: target
  - path: references_cache/PMID_40223277.txt
    sha256: 6da021c7eb122c88477dd4283bcc25f8fb06c31864bb59870bf9ca20d9310e5f
    role: context
  - path: references_cache/PMID_40468884.txt
    sha256: e8c83245e26f3c46555f7b1fc6bf144a343002e791e3321c06c1e2f56d0532aa
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
- target_id: CommunityMech:000377
  path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  label: Apple Fire Blight A+N+P SynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    role: canonical_record
scope:
  description: Entire maintained record, all nine taxa, two endpoint nodes and no
    arrows, all metadata and thirty evidence occurrences; independent full main articles
    and public project metadata. Separate supplementary figures/raw data are excluded.
  selection: Next uncovered path after Angelarchaeales in batch03; one resolved maintained
    record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000377
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml'
  target_ids:
  - CommunityMech:000377
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history or read-only cache-name preflight. Both cache
    hashes unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml\
    \ --out /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv"
  target_ids:
  - CommunityMech:000377
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history or read-only cache-name preflight. Both cache
    hashes unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000377
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history or read-only cache-name preflight. Both cache
    hashes unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000377
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history or read-only cache-name preflight. Both cache
    hashes unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml'
  target_ids:
  - CommunityMech:000377
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history or read-only cache-name preflight. Both cache
    hashes unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: No issues found
  target_ids:
  - CommunityMech:000377
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Apple_Fire_Blight_ANP_SynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history or read-only cache-name preflight. Both cache
    hashes unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Command completed without reported issues.
  target_ids:
  - CommunityMech:000377
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history or read-only cache-name preflight. Both cache
    hashes unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: "Validating kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml against schema\
    \ src/communitymech/schema/communitymech.yaml\nCache directory: references_cache\n\
    \nValidation Summary:\n  Reported validation issues: 0\n  All validations passed!\n\
    \n[annotate] This is not a count of checked excerpts (#1469). Native Discussion\
    \ evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000377
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history or read-only cache-name preflight. Both cache
    hashes unchanged.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Correct batch03 PYTHONPATH corpus run: 477 records, 57 warnings in 21
    records, zero errors; exit 1. Target not listed among warnings. Actual earlier
    execution reused with unchanged canonical inputs.'
  target_ids:
  - CommunityMech:000377
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Corpus-only documented gate; warnings preserved. A separate read-only
    native API audit also found no target issues; it does not replace this corpus
    result.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Correct batch03 PYTHONPATH corpus run: 477 records, 57 warnings in 21
    records, zero errors; exit 1. Target not listed among warnings. Actual earlier
    execution reused with unchanged canonical inputs.'
  target_ids:
  - CommunityMech:000377
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Corpus-only documented gate; warnings preserved. A separate read-only
    native API audit also found no target issues; it does not replace this corpus
    result.
- check_id: structured-expression-adapter
  name: Optional structured source adapter availability
  status: unavailable
  required: false
  summary: No own-runtime runner. Another checkout has a candidate, which was not
    executed under isolation. No catalog query occurred; primary-source Methods and
    genomic interpretation supply the scientific fallback.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - adapter
  - mechanism
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  locator: 'Entire record: nine member taxa, two endpoint nodes, no downstream arrows,
    thirty evidence occurrences'
  summary: The target is the full A+N+P biocontrol formulation, with A-only, N-only
    and P-only arms retained as experimental comparators. Erwinia is a challenged
    external participant, not a tenth formulation member.
  support: supports
  accessed_at: '2026-10-21T06:45:12.285514Z'
- evidence_id: paper-40223277
  kind: primary_source
  reference: PMID:40223277
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12010091/fullTextXML;
    independently retrieved main article XML, complete Methods, Results and Discussion,
    table text and figure captions
  summary: Primary source inspected for the source-specific formulation, endpoints,
    interpretation and experimental context. Separate supplementary figures and underlying
    raw data were not audited.
  support: supports
  accessed_at: '2026-10-21T06:40:17.137531Z'
  snapshot_sha256: 93334f74ec8ab3daa37a025494cdfd65a98601a13a6c83e6d8ea2cd0d7e4da45
- evidence_id: paper-40468884
  kind: primary_source
  reference: PMID:40468884
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC12146627/fullTextXML;
    independently retrieved main article XML, complete Methods, Results and Discussion,
    table text and figure captions
  summary: Primary source inspected for the source-specific formulation, endpoints,
    interpretation and experimental context. Separate supplementary figures and underlying
    raw data were not audited.
  support: supports
  accessed_at: '2026-10-21T06:40:17.138707Z'
  snapshot_sha256: 569d0f4ef25292c97db1bf0a6fb3e54413034686efc5e956f6d9fe763d3c9d3a
- evidence_id: membership
  kind: primary_source
  reference: PMID:40223277
  locator: 'Table 1; Results: SynCom Members Acquisition through Microbiome Analysis;
    Methods: SynCom preparation'
  summary: The construction paper identifies all nine species/strain combinations
    and their A/N/P selection groups. N strains are culture-collection proxies selected
    by microbiome sequence similarity, not demonstrated recovery of those exact strains
    from every healthy apple. Equal group mixing is not equal dosage of every strain
    across groups.
  support: supports
  accessed_at: '2026-10-21T06:40:17.137531Z'
- evidence_id: roles
  kind: primary_source
  reference: PMID:40223277
  locator: 'Results: The Varying Anti-E. amylovora Effects of SynCom Member Strains;
    Discussion'
  summary: Direct plate inhibition is shown for the two A strains and more weakly
    Kitasatospora; N/P group biocontrol or network/pathway selection does not identify
    each member's individual causal contribution. Antagonism can be indirect, but
    a common unqualified role for all members needs this distinction.
  support: supports
  accessed_at: '2026-10-21T06:40:17.137531Z'
  quote: negligible anti-EA activity
- evidence_id: fruit
  kind: primary_source
  reference: PMID:40223277
  locator: 'Results: SynCom Inhibited the Fire Blight Disease in Apple Fruits; corresponding
    Methods and Fig 1 caption'
  summary: The full ANP arm has zero measured disease severity in the stated fruit
    assay. This is a disease score and not proof that no viable pathogen remained.
  support: supports
  accessed_at: '2026-10-21T06:40:17.137531Z'
  quote: EA+A+N+P at 0% severity
- evidence_id: rose
  kind: primary_source
  reference: PMID:40223277
  locator: 'Results: Fire Blight Disease on Flower Was Controlled by the SynCom; corresponding
    Methods and Fig 2 caption'
  summary: The full ANP arm and chemical positive control have the same reported disease-severity
    value in the rose model. Numerical equality here does not establish universal
    efficacy equivalence.
  support: supports
  accessed_at: '2026-10-21T06:40:17.137531Z'
  quote: EA+A+N+P at 1.67%
- evidence_id: plant
  kind: primary_source
  reference: PMID:40223277
  locator: 'Results: SynCom Can Suppress Fire Blight Disease That Occurs in Apple
    Plants; Discussion; Fig 3 caption'
  summary: The full ANP value reported in the text is 33.4 percent; 5.4 percent belongs
    to P alone. The record correctly preserves that distinction. Source prose repeats
    one numerical vector for the second plant assay while describing contrasting rankings,
    so the second protocol must not inherit those values as independently reconciled
    measurements.
  support: supports
  accessed_at: '2026-10-21T06:40:17.137531Z'
- evidence_id: exudate
  kind: primary_source
  reference: PMID:40468884
  locator: Methods section 5; Results section 11; Fig 4 caption; Discussion section
    12
  summary: The ANP arm shows a negative pathogen-density trajectory during the exudate
    assay. Substrate use overlap and co-culture counts do not isolate resource depletion
    from antibiosis or prove reciprocal fitness costs.
  support: supports
  accessed_at: '2026-10-21T06:40:17.138707Z'
  quote: ANP was 0.506
- evidence_id: alias
  kind: primary_source
  reference: PMID:40468884
  locator: Methods section 2; Table 1; Results section 7 and section 9; compare construction
    PMID40223277 Table 1
  summary: The follow-up calls Terriglobus aquaticus TAH1 whereas the construction
    paper names 03SUJ4. These inspected articles do not explicitly establish a strain
    alias. Existing discussion correctly leaves the question open; taxonomy notes
    should avoid presenting correspondence as verified.
  support: supports
  accessed_at: '2026-10-21T06:40:17.138707Z'
- evidence_id: culture
  kind: primary_source
  reference: PMID:40468884
  locator: Methods section 2 Whole genome sequencing of SynCom strains; section 4
    Nutrient utilization assay; section 5 Apple flower exudate nutrient competition
    assay
  summary: The follow-up separates seven N/P genome subjects from previously sequenced
    A strains, nutrient-use assay preparation and exudate competition. The curated
    R2A and exudate entries match their source contexts; the broad preparation note
    should identify the relevant strain set and should not turn one preparation into
    a universal protocol.
  support: supports
  accessed_at: '2026-10-21T06:40:17.138707Z'
- evidence_id: mechanism
  kind: primary_source
  reference: PMID:40468884
  locator: Results sections 8-11; Discussion section 12
  summary: Genome-mined biosynthetic clusters and EC annotations remain candidate
    functions. The main-text discussion distinguishes direct inhibition from plausible
    indirect protection; no chemically validated member-level effector or resolved
    resource-competition mechanism is established.
  support: supports
  accessed_at: '2026-10-21T06:40:17.138707Z'
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: AbundanceEnum, FunctionalRoleEnum, EvidenceSourceEnum, community and cultivation
    slots
  summary: DOMINANT is ordinal prominence and can denote co-equal members; it is not
    a measured percentage. PATHOGEN_ANTAGONIST concerns biocontrol and need not mean
    direct killing. Evidence-source completeness is also a curation-policy requirement
    in CLAUDE.md.
  support: supports
  accessed_at: '2026-10-21T06:45:12.285617Z'
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO and GO snapshots
  locator: Twelve distinct ID-label pairs across 33 occurrences; species-rank metadata
  summary: All twelve canonical pairs match. The nine member terms and external Erwinia
    term denote species; strain resolution is provided by strain_designation and source
    Table 1,  not species CURIEs. GO0044419 is broad and marked gocheck_do_not_annotate
    in the source ontology; its use here does not establish a particular mechanism.
  support: supports
  accessed_at: '2026-10-21T06:45:12.285811Z'
  snapshot_sha256: 5aa6e4f6e89792f336d137ec2aa27dc99f2e5bd91412110e9862de0351090e09
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  locator: All thirty evidence occurrences against independent article XML and committed
    source caches
  summary: All thirty snippets match both the corresponding cache and independently
    fetched main article after NFKC/whitespace normalization. No supplement-only evidence
    was substituted into an article source. Matching words do not validate causal
    role attribution.
  support: supports
  accessed_at: '2026-10-21T06:45:12.286047Z'
  snapshot_sha256: aba318494c213624969244845d4f3cc8997ca6b6048d3723e72e9aa4c131935f
- evidence_id: 40223277-pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=40223277&retmode=xml
  locator: Independent citation metadata
  summary: The identifier resolves to the same cited construction paper.
  support: supports
  accessed_at: '2026-10-21T06:40:17.138030Z'
  snapshot_sha256: 561bc0776f73e03c0e5692dace497534a5c7a9064fe318b8bb9e6639bdb61762
- evidence_id: 40223277-crossref
  kind: database
  reference: https://api.crossref.org/works/10.4014/jmb.2501.01047
  locator: Independent citation metadata
  summary: The identifier resolves to the same cited construction paper.
  support: supports
  accessed_at: '2026-10-21T06:40:17.138261Z'
  snapshot_sha256: 29cadeaa2b8bb2e4866b1bdefe55c42af96f96fdd61fa65a21a424c5a59add89
- evidence_id: 40468884-pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=40468884&retmode=xml
  locator: Independent citation metadata
  summary: The identifier resolves to the same cited follow-up paper.
  support: supports
  accessed_at: '2026-10-21T06:40:17.138892Z'
  snapshot_sha256: f40231cee25280b5582fc94ffa087531b5c8240adae30e2172edbe2b31495a57
- evidence_id: 40468884-crossref
  kind: database
  reference: https://api.crossref.org/works/10.5423/PPJ.OA.03.2025.0040
  locator: Independent citation metadata
  summary: The identifier resolves to the same cited follow-up paper.
  support: supports
  accessed_at: '2026-10-21T06:40:17.139261Z'
  snapshot_sha256: 898c9295bd8b6c7efa2eb85f5d5478e309fe9c78997b4849ac569265be51c5ae
- evidence_id: dataset
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=1144217&retmode=xml
  locator: BioProject 1144217 title, description, access and data type
  summary: Public project metadata concerns endophytic communities in SynCom-treated
    apple seedlings and raw sequence reads. It supports the record's source-project
    link, not an assertion that this project contains assemblies of all nine strains.
  support: supports
  accessed_at: '2026-10-21T06:40:17.139488Z'
  snapshot_sha256: 34cc6090c6d97a7e4ef4102bf4f4a36890952f6ebc0b9b6c7058614bf9813344
- evidence_id: history
  kind: record_content
  reference: history/records/Apple_Fire_Blight_ANP_SynCom; reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
  locator: Four sidecars, inline history, exact target decision row 172-215
  summary: Previous edits separated tissue scores from exudate counts, removed a workflow
    arrow and retained the strain-alias and effector gaps. Sidecars pass validation.
    Historical graph review is context rather than independent source support.
  support: supports
  accessed_at: '2026-10-21T06:45:12.286890Z'
- evidence_id: local-search
  kind: search
  reference: references_cache; history; reports/causal_graph_review/decisions; kb/taxa
  locator: Identifier/slug search plus separate species-ID/name search, both including
    hidden and ignored files
  summary: The initial bounded search located both article caches, four target history
    files and a prior decision row. A separate root-agent search of kb/taxa for every
    member species ID and full species label returned no matches; ignored files were
    included. No machine-wide absence claim is made.
  support: supports
  accessed_at: '2026-10-21T06:45:12.286892Z'
  search_scope: Initial rg --no-ignore --hidden -l for the two PMIDs and record slug/ID
    in the four named trees; separate rg --no-ignore --hidden -l across kb/taxa for
    all nine full species labels and NCBITaxon IDs 67355, 1406, 346912, 346911, 428990,
    1955250, 940139, 1464011, 86185 (exit 1, no matches).
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources runner discovery
  locator: PATH, task virtualenv/module, named siblings and ignored-inclusive filenames
  summary: No runner was available in this task runtime. A candidate in another task
    checkout was found but not executed under checkout isolation; no iModulon catalog
    or organism coverage was established.
  support: supports
  accessed_at: '2026-10-21T06:45:12.287057Z'
  search_scope: Exact PATH/module resolution plus bounded ignored-inclusive task and
    sibling filename search; no credentials read or installation performed.
  snapshot_sha256: b9f8b032eb8790220cb4eacbcdece697b778bd640778c6f70c6db6f6acba8c14
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  locator: Actual execution 2026-10-21T06:39:56.208924+00:00 to 2026-10-21T06:39:58.202481+00:00
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml'
  support: supports
  accessed_at: '2026-10-21T06:39:58.202481Z'
  snapshot_sha256: 1a41053ddefce8eeea95da15417ad1582ecac06d38c3a02978ac0e22226287ca
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    --out /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv
  locator: Actual execution 2026-10-21T06:39:56.209116+00:00 to 2026-10-21T06:40:02.350636+00:00
  summary: "uv run python scripts/validate_strict.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml\
    \ --out /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-03/000377/strict-report.tsv"
  support: supports
  accessed_at: '2026-10-21T06:40:02.350636Z'
  snapshot_sha256: 57c42f04dd87d121e09020b695be2cc6eb5384ae3c6a71da27a4282a42e63ce7
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  locator: Actual execution 2026-10-21T06:39:56.209192+00:00 to 2026-10-21T06:40:01.014987+00:00
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-10-21T06:40:01.014987Z'
  snapshot_sha256: e4230f14c0102b4ad7a21bb9e7fb065444b059ec321ea0e3758becdcc0a3fe65
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  locator: Actual execution 2026-10-21T06:39:58.202879+00:00 to 2026-10-21T06:39:58.350897+00:00
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-10-21T06:39:58.350897Z'
  snapshot_sha256: e4d32e7708f1f8642105d1890e78254fdfb0aca02e73b0305322f4d277b58820
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  locator: Actual execution 2026-10-21T06:39:58.351244+00:00 to 2026-10-21T06:40:02.492449+00:00
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml'
  support: supports
  accessed_at: '2026-10-21T06:40:02.492449Z'
  snapshot_sha256: d1e8bee03878c10fe643fdb6f4034f7d71a292feae7f1e849eaa57a8aef0c74f
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Apple_Fire_Blight_ANP_SynCom
  locator: Actual execution 2026-10-21T06:40:01.015355+00:00 to 2026-10-21T06:40:02.842737+00:00
  summary: No issues found
  support: supports
  accessed_at: '2026-10-21T06:40:02.842737Z'
  snapshot_sha256: e65c120958492e7853d33aee16bca2cc83b5cc0f292bfa443b8000e55b3a72e0
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T06:40:02.847564+00:00 to 2026-10-21T06:40:02.918242+00:00
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-10-21T06:40:02.918242Z'
  snapshot_sha256: 88728dfc5a6b0989092dd7ef834fdbde87a4fc2789ba67a57a44dbf9ab190dfa
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
  locator: Actual execution 2026-10-21T06:40:02.919820+00:00 to 2026-10-21T06:40:06.148299+00:00
  summary: "Validating kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml against schema\
    \ src/communitymech/schema/communitymech.yaml\nCache directory: references_cache\n\
    \nValidation Summary:\n  Reported validation issues: 0\n  All validations passed!\n\
    \n[annotate] This is not a count of checked excerpts (#1469). Native Discussion\
    \ evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-10-21T06:40:06.148299Z'
  snapshot_sha256: b854b44ee2b77a74b3bc0ed2e73d67c7dcc8ced6e3fc2ae320f820b4d755c917
- evidence_id: check-audit-network
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  locator: Actual finish 2026-10-20T07:08:14.467705+00:00
  summary: 'Correct batch03 PYTHONPATH corpus run: 477 records, 57 warnings in 21
    records, zero errors; exit 1. Target not listed among warnings. Actual earlier
    execution reused with unchanged canonical inputs.'
  support: supports
  accessed_at: '2026-10-20T07:08:14.467705Z'
  snapshot_sha256: e2122e512641be2226ad12ab146b2c8f7d1e153f1211745e4816457834a42667
- evidence_id: check-check-network-quality
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  locator: Actual finish 2026-10-20T07:08:13.673449+00:00
  summary: 'Correct batch03 PYTHONPATH corpus run: 477 records, 57 warnings in 21
    records, zero errors; exit 1. Target not listed among warnings. Actual earlier
    execution reused with unchanged canonical inputs.'
  support: supports
  accessed_at: '2026-10-20T07:08:13.673449Z'
  snapshot_sha256: b0cb58371a5a771dcbd671952ee68dfe5f26169d08240b66162aa83580fb5229
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: Independent read-only native API check recorded in support-audit.json
  summary: No target network issue returned; all nine formulation members are represented
    and external challenged Erwinia is not required in membership. Four node evidence
    items across two nodes give mean 2.
  support: supports
  accessed_at: '2026-10-21T06:45:12.289453Z'
  snapshot_sha256: 4b1727a93d747bd1e120216b3b149ec33c098dad26ad91f10fe5890a6cb6498a
assessments:
- assessment_id: identity
  area: identity
  topic: Full ANP formulation and comparator boundaries
  outcome: supported
  summary: The nine-member formulation is resolved from the construction paper. Two
    A, five N and two P strains define this target; challenge Erwinia and separate
    tissue/plant/exudate arms are not additional formulation members.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - membership
  - paper-40223277
  - paper-40468884
  dimensions:
  - name: community_scope
    value: Defined nine-member A+N+P formulation
    definition: A-only, N-only, P-only and two-group mixtures are comparators, not
      interchangeable target communities.
    evidence_ids:
    - membership
  - name: source_strain
    value: Nine named bacterial strains from construction Table 1
    definition: Species identifiers do not prove exact strains; Terriglobus cross-paper
      alias remains unresolved.
    evidence_ids:
    - membership
    - alias
  - name: experimental_setting
    value: Controlled fruit, flower, plant and exudate biocontrol assays
    definition: Distinct endpoints and protocols are retained; no field-wide efficacy
      inference.
    evidence_ids:
    - fruit
    - rose
    - plant
    - exudate
  - name: evidence_tier
    value: Measured disease severity and pathogen counts; candidate mechanisms
    definition: Group-level outcomes do not establish every member contribution or
      the active molecular mechanism.
    evidence_ids:
    - roles
    - mechanism
  - name: cultivation_scope
    value: Source-specific strain preparation and exudate co-culture
    definition: Follow-up genome preparation, N/P nutrient-use assays and community
      competition have different scopes.
    evidence_ids:
    - culture
- assessment_id: taxonomy
  area: grounding
  topic: All nine members, strain descriptors and GTDB status
  outcome: supported
  summary: Species names and strain designations agree with construction Table 1 and
    current local NCBI authority. All nine GTDB states are explicitly unresolved;
    passing GTDB gates do not constitute successful grounding. The 03SUJ4/TAH1 link
    remains unverified.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - membership
  - ontology
  - alias
- assessment_id: roles
  area: evidence
  topic: taxonomy[*].functional_role
  outcome: concern
  summary: All members carry the same antagonist role, but membership snippets support
    their identity and group selection. Direct inhibition is demonstrated for A members
    and weakly Kitasatospora; indirect contributions of the other members remain group-level
    or candidate interpretations.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - roles
  - mechanism
  - schema
- assessment_id: abundance
  area: scope
  topic: taxonomy[*].abundance_level
  outcome: supported
  summary: All DOMINANT values can be read as qualitative prominence in the designed
    formulation under the current schema. They are not measured abundance or proof
    of equal cell fractions, and no percentage is inferred.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - membership
  - schema
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: A+N+P Fire-Blight Severity Reduction in Rosaceae
    Tissue'
  outcome: supported
  summary: Both source-specific disease endpoints support the qualified node. The
    full ANP arm had the stated fruit and rose disease scores; pathogen eradication
    or a defined mechanism is not established.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - fruit
  - rose
  details: 'Participants: all nine formulation members plus external E. amylovora
    TS3128. Direction: ANP treatment toward reduced host-tissue disease score after
    challenge. Mechanism unresolved. Context and exact source locators are in linked
    evidence; numerical equality to the chemical control does not prove general equivalence.'
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: A+N+P Erwinia Density Suppression in Flower
    Exudate'
  outcome: supported
  summary: The follow-up supports the ANP-associated decrease in pathogen density.
    PARTIAL wording correctly leaves resource competition and antibiosis unresolved;
    retain the separate strain-alias limitation.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - exudate
  - alias
  - mechanism
  details: 'Participants: follow-up A/N/P formulation and external E. amylovora TS3128.
    Direction: treatment-associated reduction of pathogen counts. There is no demonstrated
    reciprocal cost or isolated metabolite-transfer mechanism. No universal equivalence
    of Terriglobus 03SUJ4 and TAH1 is inferred.'
- assessment_id: arrows
  area: graph
  topic: ecological_interactions[*].downstream
  outcome: not_applicable
  summary: No downstream arrows exist. The second assay is not causally downstream
    of the first merely because it was a follow-up study.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - history
  - exudate
- assessment_id: engineering
  area: scope
  topic: engineering_design and description
  outcome: supported
  summary: Assembly groups and tissue-specific endpoint distinctions are supported.
    The note correctly separates the ANP plant value from the P-only abstract highlight;
    source inconsistency for the second plant protocol remains un-reconciled and is
    not silently propagated.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - membership
  - fruit
  - rose
  - plant
  - exudate
- assessment_id: environment
  area: grounding
  topic: Environment, origin, state and category
  outcome: supported
  summary: SYNTHETIC and ENGINEERED match a designed formulation. Broad plant-associated
    environment is compatible with multiple Rosaceae tissues, and notes retain the
    exudate assay. OTHER is not an erroneous rhizosphere assignment.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - membership
  - ontology
  - culture
- assessment_id: cultivation
  area: scope
  topic: growth_media[0:2] and environmental_factors[0]
  outcome: concern
  summary: Source-context conditions and exudate preparation are represented. The
    first paper also reports R2A with mannitol for member assays; the follow-up preparation
    note is not a demonstrated contradiction. Keep genome preparation, nutrient-use
    work and exudate co-culture scoped separately. Named media lack external CultureMech
    or ingredient linkages.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - culture
  - paper-40223277
  - paper-40468884
- assessment_id: resources
  area: provenance
  topic: associated_datasets and external_resources
  outcome: concern
  summary: Both PMID/DOI identities and the public source BioProject verify. The dataset
    evidence object omits evidence_source despite the claim-level curation policy.
    Project data are endophyte community reads rather than verified strain-genome
    identities.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - dataset
  - schema
  - 40223277-pubmed
  - 40223277-crossref
  - 40468884-pubmed
  - 40468884-crossref
- assessment_id: history
  area: provenance
  topic: discussions, history and reference caches
  outcome: supported
  summary: The existing alias and mechanism gaps are concrete and remain unresolved.
    Four sidecars and inline events preserve prior work; both caches correctly distinguish
    appended full text and match current primary article snippets.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - history
  - snippets
  - alias
  - mechanism
- assessment_id: metals
  area: scope
  topic: metals_present, metal_relevance and metal_notes
  outcome: supported
  summary: No metal-processing function is asserted. Peripheral siderophore screens
    and predicted biosynthetic clusters do not establish an ecosystem metal/REE mechanism.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - paper-40223277
  - mechanism
- assessment_id: validation
  area: schema
  topic: Native and independent checks
  outcome: supported
  summary: Eight focused/history/preflight commands pass, twelve ontology pairs match
    and thirty snippets verify independently. Corpus warning failures remain actual
    failures; they are not silently recoded as target scientific success.
  target_ids:
  - CommunityMech:000377
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
  summary: Completeness 75 and quality 100 are mechanical metadata/network scores,
    not certification of individual roles, strain equivalence or mechanism.
  target_ids:
  - CommunityMech:000377
  evidence_ids:
  - record
  - schema
  - native-target
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including all roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 external resources + 10 media
      + 5 datasets + 5 node metabolites). 50 + 5 + 0 + 0 + 5 + 10 + 5 + 0 = 75.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1 = 0, P2 = 1, P3 = 3, P4 = 0; 4 evidence
      items / 2 nodes = 2; native COMPLETE. 100 - 10 - 6 + 20 + 15 = 119, clamped
      to 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P2
    value: 1
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
- finding_id: member-role-evidence
  issue_key: cm-000377-member-role-evidence
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: claim-level member role attribution exceeds direct
    evidence and affects functional interpretation.'
  rule_id: P2.4
  status: open
  certainty: confirmed
  title: Common antagonist role exceeds member-specific evidence
  description: The record assigns PATHOGEN_ANTAGONIST to all nine members without
    distinguishing demonstrated direct antagonism, group-level protective performance
    and the inferred network/pathway roles of individual strains. A positive whole-mixture
    or group result does not establish every member's causal contribution; absence
    of direct plate inhibition does not disprove indirect protection.
  target_ids:
  - CommunityMech:000377
  field_paths:
  - taxonomy[*].functional_role
  - taxonomy[*].evidence
  evidence_ids:
  - record
  - roles
  - mechanism
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    role: canonical_record
- finding_id: alias-qualification
  issue_key: cm-000377-alias-qualification
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded provenance, identity qualification or cultivation-linkage
    gap; source-supported endpoint claims remain recoverable.'
  rule_id: review-checklist.taxonomy
  status: open
  certainty: confirmed
  title: Strain correspondence remains unresolved
  description: The taxonomy note calls the follow-up Terriglobus genome corresponding
    while the open discussion correctly asks whether TAH1 and 03SUJ4 are the same
    strain. The two source names are verified but their equivalence is not.
  target_ids:
  - CommunityMech:000377
  field_paths:
  - taxonomy[6].taxon_term.notes
  - ecological_interactions[1].participating_taxa[6]
  - discussions[0]
  evidence_ids:
  - record
  - membership
  - alias
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    role: canonical_record
- finding_id: media-linkage
  issue_key: cm-000377-media-linkage
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded provenance, identity qualification or cultivation-linkage
    gap; source-supported endpoint claims remain recoverable.'
  rule_id: P3.1
  status: open
  certainty: confirmed
  title: Cultivation media lack external identifiers
  description: Two named growth-media entries are present without CultureMech or MediaIngredientMech
    identifiers. Their evidence and source context remain available.
  target_ids:
  - CommunityMech:000377
  field_paths:
  - growth_media[0]
  - growth_media[1]
  evidence_ids:
  - record
  - culture
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    role: canonical_record
- finding_id: dataset-evidence-source
  issue_key: cm-000377-dataset-evidence-source
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded provenance, identity qualification or cultivation-linkage
    gap; source-supported endpoint claims remain recoverable.'
  rule_id: review-checklist.evidence
  status: open
  certainty: confirmed
  title: Dataset evidence omits its provenance type
  description: associated_datasets[0].evidence[0] contains a valid reference and exact
    matching data-availability excerpt but omits evidence_source. Native schema/reference
    validation passes; the local claim-level evidence policy still asks for this field.
  target_ids:
  - CommunityMech:000377
  field_paths:
  - associated_datasets[0].evidence[0].evidence_source
  evidence_ids:
  - record
  - dataset
  - snippets
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    role: canonical_record
actions:
- action_id: fix-member-role-evidence
  description: Attach role-specific evidence and distinguish intended/candidate biocontrol
    roles from demonstrated member-specific effects; retain supported indirect or
    collective roles with explicit scope.
  finding_ids:
  - member-role-evidence
  target_ids:
  - CommunityMech:000377
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Identity snippets are not the sole support for functional roles.
  - Direct antagonism is distinguished from group-level disease protection and inferred
    ecological contribution.
  - No negative plate assay is treated as proof of no possible indirect role.
  - Run strict, reference and network checks.
- action_id: fix-alias-qualification
  description: Keep both source-specific names and qualify their correspondence explicitly;
    verify publicly available culture or assembly identifiers before transferring
    strain-specific follow-up claims.
  finding_ids:
  - alias-qualification
  target_ids:
  - CommunityMech:000377
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - No alias is treated as proven without a resolving source.
  - The construction formulation remains defined by 03SUJ4.
  - The follow-up endpoint retains the unresolved member-provenance limitation.
- action_id: fix-media-linkage
  description: Resolve exact compatible medium or ingredient identifiers where available,
    retaining custom exudate provenance when no exact external recipe exists.
  finding_ids:
  - media-linkage
  target_ids:
  - CommunityMech:000377
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - No approximate recipe is substituted for the actual source preparation.
  - Any accepted external identifier resolves to matching formulation/context.
  - Leave genuinely unmatched custom media explicit.
- action_id: fix-dataset-evidence-source
  description: Add an accurate provenance classification for the source data-availability
    assertion, retaining the verified accession and exact snippet.
  finding_ids:
  - dataset-evidence-source
  target_ids:
  - CommunityMech:000377
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Apple_Fire_Blight_ANP_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Evidence-source classification reflects bibliographic/data provenance rather than
    an invented experiment.
  - Schema and reference checks continue to pass.
limitations:
- The construction target is resolved, but public main-text evidence does not resolve
  Terriglobus 03SUJ4 versus TAH1; follow-up strain equivalence remains an open question.
- Separate supplementary figures, Table 2 image geometry, raw sequencing reads, assemblies
  and sample-to-strain reconciliation were not independently audited. Main-text Results
  supplied the reported inhibition and endpoint interpretations.
- The second plant-assay numerical vector conflicts with the narrative ranking in
  the source; no reconstruction or new source-specific quantitative assertion is made.
- Member-wise causal contributions, active effectors and resource-competition discrimination
  remain unresolved; this review is not a cultivation optimization or field-efficacy
  claim.
- Optional expression adapter was unavailable in the owned runtime; a candidate in
  another checkout was not executed. No catalog coverage or gene-expression evidence
  is claimed.
- Required corpus gates retain actual warning failures, with no target issue; metric
  scores are not scientific approval.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Short quotations total 10 words from PMID40223277 and 3 from PMID40468884.
tags:
- record-review
- syncom
- biocontrol
- batch-03
```
