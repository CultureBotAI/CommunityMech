# Cable-bacteria photosynthetic biofilm sediment review

- Review: 20261021T143024Z-cable-biofilm-sediment-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T14:23:28.633512Z
- Finished UTC: 2026-10-21T14:30:24.736153Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The primary main, Table 1 and six figures support the broad community identity and qualified three-node, two-arrow graph. Two minor findings concern recoverable experiment/role context and the primary article being classified as phenotype data. The linked theoretical supplement remains unread and its quantitative derivation is not certified.

## Scope And Provenance

Entire record and every node/arrow assessed against direct primary main/figures, authority, history and native checks, with explicit unread theoretical-SI limits.

Selection: Only released CommunityMech:000145 in the owned batch 08 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000145 | kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml | maintained | Cable Bacteria beneath Photosynthetic Biofilm Sediment Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000145 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000145 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000145 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000145 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000145 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000145 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000145 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000145 | Reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000145 | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000145 | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| Primary article identity | passed | True | CommunityMech:000145 | Direct PubMed/Crossref metadata and actual PMC main HTML agree on article identity. |
| Current claim verification | passed | True | CommunityMech:000145 | Entire scientific main, Table 1 and all six main figures support assessment of the current qualified claims; no SI-only quantitative derivation is encoded or certified. |
| Theoretical supplement access | unavailable | False | CommunityMech:000145 | Ordinary public routes did not yield the theoretical PDF. Its constant-flux justification and quantitative derivation remain unverified. |
| Exact cultivation-recipe correspondence | not_applicable | False | CommunityMech:000145 | Natural sediment and filtered seawater are specified; no exact defined medium formulation or unique CultureMech link is established. |
| Optional structured expression adapter | unavailable | False | CommunityMech:000145 | No applicable expression-module dataset established; bounded runtime discovery is preserved. |

## Scientific And Domain Assessments

### Natural sediment assemblage and supported taxonomic resolution

identity: supported. Targets: CommunityMech:000145.

Retain the family-level cable bacteria and phylum-level diatom biofilm as the resolved focal groups.

### State, origin and category

scope: supported. Targets: CommunityMech:000145.

Retain TRANSIENT, NATURAL and OTHER for the developing sediment incubation community.

New biofilm development and cable-bacteria growth over days support the developing/transient context. Rapid chemical responses alone would not establish community transience. Laboratory conditioning of a natural assemblage does not automatically make origin ENGINEERED; ecological state is a separate optional field.

### Taxonomy functional-role support

evidence: concern. Targets: CommunityMech:000145.

The roles are supported by the full source, but their local excerpts establish identity only.

Retain cable-bacteria CROSS_FEEDER for phototroph-derived oxygen use and diatom PRIMARY_PRODUCER for photosynthesis/carbon assimilation. Add narrow role evidence rather than treating family affiliation or diatom dominance alone as functional proof. No reciprocal syntrophy, organic-only substrate restriction or obligacy is imposed.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000145.

Retain photosynthetic oxygen cross-feeding at the current community-level scope.

The source perturbs light, verifies oxygen production and follows sulfide responses. The graph does not claim reciprocal benefit or species-resolved interaction. The broad roster is appropriate to the observed biofilm and cable filaments.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000145.

Retain oxygen supply as the supported surface electron-acceptor link to deeper sulfide oxidation.

The source supports coupled responses, while exact redox-site allocation remains an interpretation. No need to turn this qualified physiological link into a claim of an isolated molecular mechanism.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000145.

Retain interpreted electrogenic sulfide oxidation with the current conduction and mechanism limits.

Conduction along a multicellular filament is not separately classified as exchange between organisms. The observed geochemical fingerprint and filaments support the interpretation; the main presents spatial regulation and motility as proposals.

### ecological_interactions[1].downstream[0]

graph: supported. Targets: CommunityMech:000145.

Retain electrical coupling as the source interpretation for rapid deep sulfide responses.

Minute-scale responses support coupling relative to slow diffusion. They do not uniquely distinguish biochemical regulation from movement or validate the unread SI constant-flux derivation.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000145.

Retain rapid repeatable redox responses without inflating replication or significance.

Four light/dark cycles are repeated observations, not four independent cores. Experiment 2 has separate baseline and treatment/control sample counts. Existing current-density and sulfide-depth significance caveats are source-faithful.

### Metabolites and related ingredients

grounding: supported. Targets: CommunityMech:000145.

Retain neutral H2S for measured free sulfide and O2 for the electron acceptor.

The ingredient note correctly distinguishes H2S from calculated H2S plus HS− and from sulfide(2−). No exclusive uptake form, fixed dissolved concentration or universally oxic sediment is inferred. The O2 ingredient description is consistent with the source.

### Sediment incubation and local evidence context

completeness: concern. Targets: CommunityMech:000145.

Recover available phase-specific setup, conditions and role evidence.

The record currently gives generic light/dark and sulfide context but omits temperature, salinity, core preparation, staged conditioning and the two experimental schedules. Preserve layered redox conditions, shared-water flow and measurement timing; no unreported working volume or full medium formulation is supplied.

### associated_datasets[0]

representation: concern. Targets: CommunityMech:000145.

The PMID/PMC entry denotes the publication rather than a distinct phenotype collection.

Keep a traceable article link as an external narrative/publication resource. A data object would require its own specific identity and scope; do not infer that no study data exist or create a new accession from the PMID.

### Previous repairs and current source boundary

provenance: supported. Targets: CommunityMech:000145.

Retain the later taxonomic/chemical repair and existing graph limits.

Earlier ledger certification was limited to its stated fields and access scope. The present review adds complete main/figure assessment and narrower context/resource findings. The SI is still uninspected; no prior decision substitutes for reading its model derivation.

### Native checks and source-specific review

schema: supported. Targets: CommunityMech:000145.

All eight focused native gates pass; two bounded context/resource findings remain.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000145.

Scores describe current encoded fields and diagnostics, including the misclassified article item.

## Findings

### recover-context: Recover incubation context and narrow role evidence

minor / open / confirmed; issue key: cm-000145-recover-context.

The record omits available temperature, salinity, sediment-core preparation and separate incubation schedules. Its local taxonomy excerpts establish family/phylum identity rather than the supported oxygen-recipient and primary-production functions. Recover these details from the actual main Methods and functional discussion without changing the valid broad roster or graph.

### article-as-dataset: Represent the primary article as a publication resource

minor / open / confirmed; issue key: cm-000145-article-as-dataset.

associated_datasets[0] uses PMID-25416774 and a PMC article URL for a PHENOTYPE dataset. The identifier resolves to the publication, not an independently identified collection of measurements. Preserve the source link in a publication/narrative-resource representation.

## Recommended Actions And Acceptance Checks

### recover-experimental-context

Add source-specific sediment incubation and functional evidence while preserving phase and redox boundaries.

- Describe natural Rattekaai sediment preparation: top 8 cm, 500 micrometre sieve, homogenization and 4 cm diameter Plexiglas core liners. Keep collection dates as provenance; do not assign collection years to individual experiments without explicit source support or infer a working volume from diameter.
- Record 16 ± approximately 1 C and filtered aerated Oosterschelde seawater at salinity 28 ± 1 per mille. Preserve oxygenated overlying water and suboxic/anoxic sediment layers; do not label the entire sediment uniformly aerobic or invent a defined recipe.
- Separate experiment 1’s 20-day dark conditioning, seven-day indirect-sunlight biofilm development and four-day 12 h light/12 h dark assay from experiment 2’s one-week preincubation and seven-day treatment. Include the approximately 300 micromol photons m−2 s−1 lighting with its experiment-specific fluorescent/LED source.
- Keep experiment 2 baseline n=3 and treatment/control n=2 distinct from repeated light/dark cycles in experiment 1. Shared water recirculation of 20 litres/h is not a core feed/dilution rate; the four-hour dark wait is measurement timing. Observed pH profiles are responses, not prescribed setpoints.
- Attach narrow evidence for phototrophic carbon assimilation/oxygen production and cable-bacteria oxygen use in addition to the current identity snippets. Retain CROSS_FEEDER and PRIMARY_PRODUCER at the resolved group level; do not add reciprocal benefit, species/strain identities or an obligatory syntrophic mechanism.
- Retain all three nodes, both qualified arrows and existing significance/replication caveats. Treat the unread SI derivation as unresolved, not as a verified model. Validate schema, terms, references, GTDB/domain and history after separately authorized curation.

### reclassify-publication-resource

Keep the primary source discoverable without treating its publication identifier as a dataset accession.

- Move the article link to external_resources with the verified PMID/DOI/PMC identity and a description of its sediment microsensor/light-perturbation study. Use a valid repository value and actual article URL rather than inventing a dataset accession.
- Remove the bibliographic item from associated_datasets when moving it to external_resources. Add a replacement dataset only if a specific data collection, table or archive asset is independently identified with accurate scope.
- Keep source citations/evidence and the historical repair record intact. An unread theoretical supplement should not be relabeled as a phenotype dataset or a verified executable model. Re-run resource/reference validation after curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml; Entire record, three nodes and two downstream arrows | supports | The record represents laboratory sediment incubations containing cable bacteria and a diatom-dominated surface biofilm. Prior repairs preserve broad identity, measured sulfide chemistry and explicit mechanistic/statistical limits. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=25416774&amp;retmode=xml; Article identity and available abstract | supports | Direct title, abstract and article identifiers agree with the focal sediment study. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:25416774%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article identity and available abstract | supports | Metadata agrees with the primary identity; the separate full-text API did not provide article XML. |
| crossref | https://api.crossref.org/works/10.1128/AEM.02682-14; Article identity and available abstract | supports | Direct DOI metadata identifies the focal article; a publication identifier is not by itself a dataset accession. |
| identity | PMID:25416774; Methods: Study site and sediment collection; Experiment 1; Figure 1 | supports | Rattekaai salt-marsh sediment was sieved, homogenized and repacked. Microscopy supports a diatom-dominated biofilm, and CARD-FISH with DSB706 supports the cable-bacteria family attribution. No species-resolved two-member culture or exhaustive sediment roster is identified. |
| setup | PMID:25416774; Methods: Study site and sediment collection; Experiment 1 pre-experimental steps | supports | Top 8 cm of sediment was sieved at 500 micrometres and placed in 4 cm diameter Plexiglas liners. Aerated filtered Oosterschelde seawater had salinity 28 ± 1 per mille, and the room was 16 ± approximately 1 C. These describe layered sediment with oxygenated overlying water, not a uniformly aerobic culture or a defined medium recipe. |
| experiment-1 | PMID:25416774; Methods: Experiment 1; Results/Figures 2–4 | supports | After 20 days dark preincubation and 7 days of indirect sunlight/biofilm development, cores experienced a four-day assay with 12 h light/12 h dark and approximately 300 micromol photons m−2 s−1 from cool-white fluorescent lighting. Repeated cycles are not independent sediment-core replicates. |
| experiment-2 | PMID:25416774; Methods: Experiment 2; Table 1 and footnote; Figure 5 | supports | The second experiment used one week of dark preincubation, baseline measurements in three cores, and seven days of light/dark or dark treatment with two cores per group. Shared water recirculated at 20 litres/h. Profiling followed at least four hours of darkness. This is not an individual-core dilution rate or the first experiment’s conditioning schedule. |
| roles | PMID:25416774; Introduction; Methods background theory; Discussion: rapid response of deep porewater sulfide | supports | Photosynthetic carbon assimilation and oxygen production support the phototroph role; the light perturbation and oxygen/sulfide responses support cable-bacteria use of the oxygen supply. Reciprocal benefit to diatoms remains unresolved. Identity-only taxonomy snippets should be supplemented with this role-specific source context. |
| oxygen-coupling | PMID:25416774; Results: Experiment 1; Discussion: rapid response of deep porewater sulfide | supports | Light transitions change near-surface oxygen and deep sulfide on a timescale much faster than the source’s estimated diffusion timescale. This supports the retained oxygen-supply and electrogenic-coupling interpretation without proving the detailed redox-site mechanism. |
| mechanistic-limits | PMID:25416774; Discussion: responses on minutes and hours timescales; Figure 6 and equation 1 | supports | The source presents an electrical analogy with a constant-flux assumption and proposes regulation or motility for the slower response. Figure 6 is a conceptual model, not a molecular perturbation assay. The quantitative justification delegated to SI was not inspected. |
| statistics | PMID:25416774; Results: Experiment 2; Table 1 and footnote | supports | Current-density and oxygen-penetration contrasts are nonsignificant. The table marks sulfide depth significant while Results reports P = .082; the record already preserves that inconsistency. No significance is recomputed from rounded summary values. |
| chemistry | PMID:25416774; Methods: Microsensor profiling and geochemical rate estimation | supports | Experiment 1 reports measured free H2S. Experiment 2 calculates total sulfide as H2S plus HS− from measured H2S and depth-matched pH. This supports the corrected H2S term without equating all dissolved sulfide with one species or proving an exclusive uptake mechanism. |
| resource-identity | PMID:25416774; Article title/identifiers; Associated Data and Supplementary Material sections | supports | PMID 25416774 and PMC4292484 identify the primary article. Associated Data lists a supplement index and theoretical PDF; the encoded PMID-based item does not identify a distinct phenotype collection. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum; EcologicalStateEnum; MicrobialCommunity; GrowthMedia; CultivationSetup; ExternalResource | supports | Oxygen can be a product used by another taxon; recipient roles do not require an organic-only substrate or reciprocal benefit. TRANSIENT can describe a developing community. Cultivation setup and ecological state are optional; source-supported context can still improve completeness. |
| dataset-schema | src/communitymech/schema/mech_shared.yaml; Dataset and DatasetTypeEnum | supports | Dataset describes a public data collection with a repository-accession reference. A publication about phenotype measurements is not automatically a PHENOTYPE dataset. |
| ontology | ontology-authority.json; Whole bounded receipt | supports | Six encoded ontology pairs across eleven occurrences match local canonical labels, including family/phylum taxonomy, sediment, photosynthesis, O2 and neutral H2S. |
| semantics | ontology-semantic-notes.json; Whole bounded receipt | supports | The repaired taxonomic and chemical scope is coherent. Role definitions permit oxygen use, and publication-as-data is a representation issue rather than a broken article identifier. |
| resources | dataset-verification.json; Whole bounded receipt | supports | Direct metadata establishes publication identity. Supplement links and failed access routes are inventoried; no independently identified study archive or exact cultivation recipe is asserted. |
| snippets | snippet-audit.json; Whole bounded receipt | supports | All eleven excerpts match the direct article/PubMed union and pinned cache. Identity-only excerpts do not establish every local functional-role claim. |
| history | provenance-audit.json; Whole bounded receipt | supports | Both histories and exact batch8/batch125 decisions were read. The later repair supersedes earlier diatom/sulfide uncertainty and preserves the three nodes/two arrows. Current issue 1267 status/comments are documented. |
| native-target | support-audit.json; Whole bounded receipt | supports | The native network is COMPLETE with three nodes, two arrows and four node-evidence entries. Scores reflect encoded fields, including the current dataset item, not the validity of its classification. |
| source-scope | source-audit.json; Whole bounded receipt | supports | Complete assessment of current claims uses the entire primary main, Table 1 and six figures. The linked theoretical supplement remains unread and its derivation is explicitly unverified. |
| independent-source | root-independent-source-audit.json; Whole bounded receipt | supports | Root independently assessed the full main, six figures, current record and authority/provenance boundaries, agreeing with two minor findings and the bounded completion status. |
| access-fulltext | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4292484/fullTextXML; Actual preserved access request | supports | The Europe PMC XML route returned an error; it is not the source used for main-text assessment. |
| access-supplement-zip | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4292484/supplementaryFiles; Actual preserved access request | supports | The supplementary endpoint returned a non-open-access error document, not a ZIP archive. |
| access-supp-pdf | https://pmc.ncbi.nlm.nih.gov/articles/instance/4292484/bin/AEM.02682-14_zam999105982so1.pdf; Actual preserved access request | supports | The linked PMC PDF request returned an HTML challenge, not supplemental content. |
| access-publisher-supp | https://journals.asm.org/doi/suppl/10.1128/AEM.02682-14/suppl_file/zam999105982so1.pdf; Actual preserved access request | supports | The ordinary publisher supplement request returned 403; no supplemental PDF was read. |
| adapter | adapter-check.json; Actual optional adapter/runtime discovery | supports | No applicable expression-module dataset was established; no paid provider or model execution was used. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml; Actual execution 2026-10-21T14:23:53.836945+00:00 to 2026-10-21T14:23:54.710155+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-strict kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml --out /private/tmp/cm-review-session/batch-08/000145/strict-report.tsv; Actual execution 2026-10-21T14:23:53.837119+00:00 to 2026-10-21T14:23:56.298988+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-terms kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml; Actual execution 2026-10-21T14:23:53.837190+00:00 to 2026-10-21T14:23:55.791025+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml; Actual execution 2026-10-21T14:23:54.710590+00:00 to 2026-10-21T14:23:54.792059+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb-domain kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml; Actual execution 2026-10-21T14:23:54.792469+00:00 to 2026-10-21T14:23:56.432686+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-history history/records/Cable_Bacteria_Photosynthetic_Biofilm_Sediment; Actual execution 2026-10-21T14:23:55.791453+00:00 to 2026-10-21T14:23:56.657245+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T14:23:56.658038+00:00 to 2026-10-21T14:23:56.719719+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-references-explained kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml; Actual execution 2026-10-21T14:23:56.720002+00:00 to 2026-10-21T14:23:58.058529+00:00 | supports | Reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00 | supports | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00 | supports | Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records; the focal network separately reports COMPLETE. |

## Limits And Additional Notes

- The linked theoretical supplement remains unread. Its constant-flux justification and redox-site quantitative derivation are unverified; this review does not certify the model beyond the explicit proposal described in main text/Figure6.
- Scientific completion concerns current main-supported record claims and bounded follow-up, not full source-package accessibility or model/statistical reproduction.
- No raw sensor traces were downloaded or reanalysed; no previous study was independently reread for methods transferred by citation. Existing main Methods are sufficient for the stated cultivation follow-up.
- Six main figures were inspected at available display resolution; no counts or numerical values were inferred from pixels in place of reported text/table measurements.
- No defined medium recipe, working volume, species/strain resolution, exact CultureMech linkage or deposited dataset accession was invented. No data-existence absence claim follows from the article-only resource.
- All11 canonical excerpts are supported by direct article/PubMed union and the pinned cache. Literal identity snippets alone do not establish a functional role.
- No canonical/cache/history/saved-review edits, model execution, author contact or paid provider use occurred.
- No canonical, cache, history, generated or saved-review file changed; all 25 inspected inputs remain pinned.
- Eleven existing snippets match the direct article/PubMed union and cache. Main Methods supplement the brief cached excerpts without changing cache bytes.
- Completeness 75 and quality 100/raw 124.3333333333 are mechanical scores. Completed assessment concerns current bounded claims, not complete source-package accessibility or verification of the theoretical SI.
- No raw-data or statistical reanalysis, model execution, author contact, paid provider or later-target work.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T143024Z-cable-biofilm-sediment-record
kind: record
repository: CultureBotAI/CommunityMech
title: Cable-bacteria photosynthetic biofilm sediment review
started_at: '2026-10-21T14:23:28.633512Z'
finished_at: '2026-10-21T14:30:24.736153Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate agents assessed primary science, native/ontology checks
    and supporting provenance; no person-level independence asserted.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The primary main, Table 1 and six figures support the broad community identity
  and qualified three-node, two-arrow graph. Two minor findings concern recoverable
  experiment/role context and the primary article being classified as phenotype data.
  The linked theoretical supplement remains unread and its quantitative derivation
  is not certified.
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
  - path: history/records/Cable_Bacteria_Photosynthetic_Biofilm_Sediment/2026-10-05T142600Z-codex-6e7ba0.yaml
    sha256: e32b0babe5a1216a2f36b1d798591210bbb64851890182e6c7089c99003c18f5
    role: context
  - path: history/records/Cable_Bacteria_Photosynthetic_Biofilm_Sediment/2026-10-08T194617Z-codex-d8c9fa.yaml
    sha256: b9579a45ffef217a8d510dad062da82a92adf48f0f227bfe4d7be9ca5fff522a
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
    sha256: 79a9597722d1caa4abad454a53464a9671801ec4d52d5b809a42ec003e90fd79
    role: target
  - path: references_cache/PMID_25416774.txt
    sha256: 686490fadcc5e7864de153e175e00dafdb40b8977465517dccc761c2551e5ddc
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch8.yaml
    sha256: a03eceb4ca205fdd9092a4f18c0fa4c068e8ec91ee5a62d09da97b87a4f50a25
    role: context
  - path: reports/causal_graph_review/decisions/20261008-cable-biofilm-batch125.yaml
    sha256: b753d01726b8c230018a13e2462eff8f394959b347a4324f92ef0db2857d79ca
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
- target_id: CommunityMech:000145
  path: kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  label: Cable Bacteria beneath Photosynthetic Biofilm Sediment Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
    role: canonical_record
scope:
  description: Entire record and every node/arrow assessed against direct primary
    main/figures, authority, history and native checks, with explicit unread theoretical-SI
    limits.
  selection: Only released CommunityMech:000145 in the owned batch 08 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000145
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000145
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support or correct resource classification.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000145
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
    --out /private/tmp/cm-review-session/batch-08/000145/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support or correct resource classification.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000145
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support or correct resource classification.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000145
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support or correct resource classification.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000145
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support or correct resource classification.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000145
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Cable_Bacteria_Photosynthetic_Biofilm_Sediment
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support or correct resource classification.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000145
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support or correct resource classification.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000145
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Fresh focused native checks; mechanical validity does not establish
    source-specific support or correct resource classification.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch 08 corpus check reports 57 warnings across 21 of 477 records;
    the focal network separately reports COMPLETE.
  target_ids:
  - CommunityMech:000145
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
  - CommunityMech:000145
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
  name: Primary article identity
  status: passed
  required: true
  summary: Direct PubMed/Crossref metadata and actual PMC main HTML agree on article
    identity.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - pubmed
  - crossref
  - resource-identity
- check_id: scientific-source
  name: Current claim verification
  status: passed
  required: true
  summary: Entire scientific main, Table 1 and all six main figures support assessment
    of the current qualified claims; no SI-only quantitative derivation is encoded
    or certified.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - source-scope
  - independent-source
  - mechanistic-limits
- check_id: supplement
  name: Theoretical supplement access
  status: unavailable
  required: false
  summary: Ordinary public routes did not yield the theoretical PDF. Its constant-flux
    justification and quantitative derivation remain unverified.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - access-supplement-zip
  - access-supp-pdf
  - access-publisher-supp
  - source-scope
- check_id: cross-mech
  name: Exact cultivation-recipe correspondence
  status: not_applicable
  required: false
  summary: Natural sediment and filtered seawater are specified; no exact defined
    medium formulation or unique CultureMech link is established.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - setup
  - resources
- check_id: structured-adapter
  name: Optional structured expression adapter
  status: unavailable
  required: false
  summary: No applicable expression-module dataset established; bounded runtime discovery
    is preserved.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  locator: Entire record, three nodes and two downstream arrows
  summary: The record represents laboratory sediment incubations containing cable
    bacteria and a diatom-dominated surface biofilm. Prior repairs preserve broad
    identity, measured sulfide chemistry and explicit mechanistic/statistical limits.
  support: supports
  accessed_at: '2026-10-21T14:29:23.220308Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=25416774&retmode=xml
  locator: Article identity and available abstract
  summary: Direct title, abstract and article identifiers agree with the focal sediment
    study.
  support: supports
  accessed_at: '2026-10-21T14:23:57.465288Z'
  snapshot_sha256: ca444a3425c13115b6ee85483c49be05e5b934e8e53f2ab0a1dbcf3994ae72d1
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:25416774%20AND%20SRC:MED&format=json&resultType=core
  locator: Article identity and available abstract
  summary: Metadata agrees with the primary identity; the separate full-text API did
    not provide article XML.
  support: supports
  accessed_at: '2026-10-21T14:23:57.890878Z'
  snapshot_sha256: fdb574d81139a2c122ac565d4f196f77b9146883e04d63d038351a0a27197032
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1128/AEM.02682-14
  locator: Article identity and available abstract
  summary: Direct DOI metadata identifies the focal article; a publication identifier
    is not by itself a dataset accession.
  support: supports
  accessed_at: '2026-10-21T14:24:37.036660Z'
  snapshot_sha256: 811d86f3040c95f9372799ddca891e2e71639e84fec577173c76f79a776c5620
- evidence_id: identity
  kind: primary_source
  reference: PMID:25416774
  locator: 'Methods: Study site and sediment collection; Experiment 1; Figure 1'
  summary: Rattekaai salt-marsh sediment was sieved, homogenized and repacked. Microscopy
    supports a diatom-dominated biofilm, and CARD-FISH with DSB706 supports the cable-bacteria
    family attribution. No species-resolved two-member culture or exhaustive sediment
    roster is identified.
  support: supports
  accessed_at: '2026-10-21T14:29:23.221628Z'
  snapshot_sha256: 52df8383273b4df901bcaf54632cb9650a0d551cb8d52b411b20aa3cf49a7427
  quote: dominated by diatoms
- evidence_id: setup
  kind: primary_source
  reference: PMID:25416774
  locator: 'Methods: Study site and sediment collection; Experiment 1 pre-experimental
    steps'
  summary: Top 8 cm of sediment was sieved at 500 micrometres and placed in 4 cm diameter
    Plexiglas liners. Aerated filtered Oosterschelde seawater had salinity 28 ± 1
    per mille, and the room was 16 ± approximately 1 C. These describe layered sediment
    with oxygenated overlying water, not a uniformly aerobic culture or a defined
    medium recipe.
  support: supports
  accessed_at: '2026-10-21T14:29:23.221793Z'
  snapshot_sha256: 52df8383273b4df901bcaf54632cb9650a0d551cb8d52b411b20aa3cf49a7427
- evidence_id: experiment-1
  kind: primary_source
  reference: PMID:25416774
  locator: 'Methods: Experiment 1; Results/Figures 2–4'
  summary: After 20 days dark preincubation and 7 days of indirect sunlight/biofilm
    development, cores experienced a four-day assay with 12 h light/12 h dark and
    approximately 300 micromol photons m−2 s−1 from cool-white fluorescent lighting.
    Repeated cycles are not independent sediment-core replicates.
  support: supports
  accessed_at: '2026-10-21T14:29:23.221904Z'
  snapshot_sha256: 52df8383273b4df901bcaf54632cb9650a0d551cb8d52b411b20aa3cf49a7427
- evidence_id: experiment-2
  kind: primary_source
  reference: PMID:25416774
  locator: 'Methods: Experiment 2; Table 1 and footnote; Figure 5'
  summary: The second experiment used one week of dark preincubation, baseline measurements
    in three cores, and seven days of light/dark or dark treatment with two cores
    per group. Shared water recirculated at 20 litres/h. Profiling followed at least
    four hours of darkness. This is not an individual-core dilution rate or the first
    experiment’s conditioning schedule.
  support: supports
  accessed_at: '2026-10-21T14:29:23.221996Z'
  snapshot_sha256: 52df8383273b4df901bcaf54632cb9650a0d551cb8d52b411b20aa3cf49a7427
- evidence_id: roles
  kind: primary_source
  reference: PMID:25416774
  locator: 'Introduction; Methods background theory; Discussion: rapid response of
    deep porewater sulfide'
  summary: Photosynthetic carbon assimilation and oxygen production support the phototroph
    role; the light perturbation and oxygen/sulfide responses support cable-bacteria
    use of the oxygen supply. Reciprocal benefit to diatoms remains unresolved. Identity-only
    taxonomy snippets should be supplemented with this role-specific source context.
  support: supports
  accessed_at: '2026-10-21T14:29:23.222082Z'
  snapshot_sha256: 52df8383273b4df901bcaf54632cb9650a0d551cb8d52b411b20aa3cf49a7427
- evidence_id: oxygen-coupling
  kind: primary_source
  reference: PMID:25416774
  locator: 'Results: Experiment 1; Discussion: rapid response of deep porewater sulfide'
  summary: Light transitions change near-surface oxygen and deep sulfide on a timescale
    much faster than the source’s estimated diffusion timescale. This supports the
    retained oxygen-supply and electrogenic-coupling interpretation without proving
    the detailed redox-site mechanism.
  support: supports
  accessed_at: '2026-10-21T14:29:23.222172Z'
  snapshot_sha256: 52df8383273b4df901bcaf54632cb9650a0d551cb8d52b411b20aa3cf49a7427
- evidence_id: mechanistic-limits
  kind: primary_source
  reference: PMID:25416774
  locator: 'Discussion: responses on minutes and hours timescales; Figure 6 and equation
    1'
  summary: The source presents an electrical analogy with a constant-flux assumption
    and proposes regulation or motility for the slower response. Figure 6 is a conceptual
    model, not a molecular perturbation assay. The quantitative justification delegated
    to SI was not inspected.
  support: supports
  accessed_at: '2026-10-21T14:29:23.222265Z'
  snapshot_sha256: 52df8383273b4df901bcaf54632cb9650a0d551cb8d52b411b20aa3cf49a7427
  quote: a regulatory or a behavioral response
- evidence_id: statistics
  kind: primary_source
  reference: PMID:25416774
  locator: 'Results: Experiment 2; Table 1 and footnote'
  summary: Current-density and oxygen-penetration contrasts are nonsignificant. The
    table marks sulfide depth significant while Results reports P = .082; the record
    already preserves that inconsistency. No significance is recomputed from rounded
    summary values.
  support: supports
  accessed_at: '2026-10-21T14:29:23.222402Z'
  snapshot_sha256: 52df8383273b4df901bcaf54632cb9650a0d551cb8d52b411b20aa3cf49a7427
- evidence_id: chemistry
  kind: primary_source
  reference: PMID:25416774
  locator: 'Methods: Microsensor profiling and geochemical rate estimation'
  summary: Experiment 1 reports measured free H2S. Experiment 2 calculates total sulfide
    as H2S plus HS− from measured H2S and depth-matched pH. This supports the corrected
    H2S term without equating all dissolved sulfide with one species or proving an
    exclusive uptake mechanism.
  support: supports
  accessed_at: '2026-10-21T14:29:23.222637Z'
  snapshot_sha256: 52df8383273b4df901bcaf54632cb9650a0d551cb8d52b411b20aa3cf49a7427
- evidence_id: resource-identity
  kind: primary_source
  reference: PMID:25416774
  locator: Article title/identifiers; Associated Data and Supplementary Material sections
  summary: PMID 25416774 and PMC4292484 identify the primary article. Associated Data
    lists a supplement index and theoretical PDF; the encoded PMID-based item does
    not identify a distinct phenotype collection.
  support: supports
  accessed_at: '2026-10-21T14:29:23.222825Z'
  snapshot_sha256: 52df8383273b4df901bcaf54632cb9650a0d551cb8d52b411b20aa3cf49a7427
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum; EcologicalStateEnum; MicrobialCommunity; GrowthMedia;
    CultivationSetup; ExternalResource
  summary: Oxygen can be a product used by another taxon; recipient roles do not require
    an organic-only substrate or reciprocal benefit. TRANSIENT can describe a developing
    community. Cultivation setup and ecological state are optional; source-supported
    context can still improve completeness.
  support: supports
  accessed_at: '2026-10-21T14:29:23.222924Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: dataset-schema
  kind: authority
  reference: src/communitymech/schema/mech_shared.yaml
  locator: Dataset and DatasetTypeEnum
  summary: Dataset describes a public data collection with a repository-accession
    reference. A publication about phenotype measurements is not automatically a PHENOTYPE
    dataset.
  support: supports
  accessed_at: '2026-10-21T14:29:23.222973Z'
  snapshot_sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded receipt
  summary: Six encoded ontology pairs across eleven occurrences match local canonical
    labels, including family/phylum taxonomy, sediment, photosynthesis, O2 and neutral
    H2S.
  support: supports
  accessed_at: '2026-10-21T14:29:23.223512Z'
  snapshot_sha256: b542c92a8061202a509b5efd456beb90a213bc0bfbbd87ca453b74776b575bea
- evidence_id: semantics
  kind: authority
  reference: ontology-semantic-notes.json
  locator: Whole bounded receipt
  summary: The repaired taxonomic and chemical scope is coherent. Role definitions
    permit oxygen use, and publication-as-data is a representation issue rather than
    a broken article identifier.
  support: supports
  accessed_at: '2026-10-21T14:29:23.223819Z'
  snapshot_sha256: b9bb1d6502274dc5e38675bb832094cb6f5eebfed47eb92eeb6533b6c04ba299
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded receipt
  summary: Direct metadata establishes publication identity. Supplement links and
    failed access routes are inventoried; no independently identified study archive
    or exact cultivation recipe is asserted.
  support: supports
  accessed_at: '2026-10-21T14:29:23.224145Z'
  snapshot_sha256: 95c2b3be4137698ca69879d25fd7065b0d82e11e37e4c902ef5abf6a454df123
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded receipt
  summary: All eleven excerpts match the direct article/PubMed union and pinned cache.
    Identity-only excerpts do not establish every local functional-role claim.
  support: supports
  accessed_at: '2026-10-21T14:29:23.224478Z'
  snapshot_sha256: 6b266c16560314d93b1a309a9090c94cce70a6b8deac4078bc373ca05b1c2147
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded receipt
  summary: Both histories and exact batch8/batch125 decisions were read. The later
    repair supersedes earlier diatom/sulfide uncertainty and preserves the three nodes/two
    arrows. Current issue 1267 status/comments are documented.
  support: supports
  accessed_at: '2026-10-21T14:29:23.224755Z'
  snapshot_sha256: 0364e8899b482910745831bd818724849ea94a5aaf111bd0e9e519e322f9b631
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded receipt
  summary: The native network is COMPLETE with three nodes, two arrows and four node-evidence
    entries. Scores reflect encoded fields, including the current dataset item, not
    the validity of its classification.
  support: supports
  accessed_at: '2026-10-21T14:29:23.224825Z'
  snapshot_sha256: f66a228f3015439ab5860ec169c6de795510e2224b7564818aac9dc51cd56307
- evidence_id: source-scope
  kind: validation
  reference: source-audit.json
  locator: Whole bounded receipt
  summary: Complete assessment of current claims uses the entire primary main, Table
    1 and six figures. The linked theoretical supplement remains unread and its derivation
    is explicitly unverified.
  support: supports
  accessed_at: '2026-10-21T14:29:23.224872Z'
  snapshot_sha256: 7648fa042ea54685ef2207b6dcfa99756e66643f6873e4c74f00ce03eb333640
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded receipt
  summary: Root independently assessed the full main, six figures, current record
    and authority/provenance boundaries, agreeing with two minor findings and the
    bounded completion status.
  support: supports
  accessed_at: '2026-10-21T14:29:23.225129Z'
  snapshot_sha256: 066a52362d50a0c743fe2e66921896a3d81566a9f4bb53c255ff6f3509d84deb
- evidence_id: access-fulltext
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4292484/fullTextXML
  locator: Actual preserved access request
  summary: The Europe PMC XML route returned an error; it is not the source used for
    main-text assessment.
  support: supports
  accessed_at: '2026-10-21T14:23:57.948874Z'
  snapshot_sha256: 4fb1643bfc2e009bc75f4e0ccc77173c300d77405892d133650b2c5b5a256833
- evidence_id: access-supplement-zip
  kind: validation
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4292484/supplementaryFiles
  locator: Actual preserved access request
  summary: The supplementary endpoint returned a non-open-access error document, not
    a ZIP archive.
  support: supports
  accessed_at: '2026-10-21T14:23:58.534905Z'
  snapshot_sha256: cbd6d47c589b534d02f628f9f7d6ad89a4e4a0bf5c4316a10fb1bfe37746cf28
- evidence_id: access-supp-pdf
  kind: validation
  reference: https://pmc.ncbi.nlm.nih.gov/articles/instance/4292484/bin/AEM.02682-14_zam999105982so1.pdf
  locator: Actual preserved access request
  summary: The linked PMC PDF request returned an HTML challenge, not supplemental
    content.
  support: supports
  accessed_at: '2026-10-21T14:24:36.753992Z'
  snapshot_sha256: 7411465f0fcbc0dd8d2260ac56a2d496a488ce5f03d8a72ea3d679363ae5d7dc
- evidence_id: access-publisher-supp
  kind: validation
  reference: https://journals.asm.org/doi/suppl/10.1128/AEM.02682-14/suppl_file/zam999105982so1.pdf
  locator: Actual preserved access request
  summary: The ordinary publisher supplement request returned 403; no supplemental
    PDF was read.
  support: supports
  accessed_at: '2026-10-21T14:25:01.126378Z'
  snapshot_sha256: 0f8cc9458c3522be8738227107144aeb52a804258fd86f086e4e2e1bf5834b45
- evidence_id: adapter
  kind: validation
  reference: adapter-check.json
  locator: Actual optional adapter/runtime discovery
  summary: No applicable expression-module dataset was established; no paid provider
    or model execution was used.
  support: supports
  accessed_at: '2026-10-21T14:29:23.226616Z'
  snapshot_sha256: 3e1dc441401d944def5adf089389c831f4a8170d466c957d2fa224dec73c4774
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  locator: Actual execution 2026-10-21T14:23:53.836945+00:00 to 2026-10-21T14:23:54.710155+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T14:23:54.710155Z'
  snapshot_sha256: e4a92b83c33612a2aedd676cc85f8970d9cf6289aff1fcbfc8df7b6ff2c0032d
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
    --out /private/tmp/cm-review-session/batch-08/000145/strict-report.tsv
  locator: Actual execution 2026-10-21T14:23:53.837119+00:00 to 2026-10-21T14:23:56.298988+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T14:23:56.298988Z'
  snapshot_sha256: ed6bf230918455ee79db567e455f9fc792f6771fc3da290d21b0a72997e842eb
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  locator: Actual execution 2026-10-21T14:23:53.837190+00:00 to 2026-10-21T14:23:55.791025+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T14:23:55.791025Z'
  snapshot_sha256: 0e9196d783e31b17c31b5ca48829a3ed27128eaa81719a048dc8452b8b244527
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  locator: Actual execution 2026-10-21T14:23:54.710590+00:00 to 2026-10-21T14:23:54.792059+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T14:23:54.792059Z'
  snapshot_sha256: 7616909fc3cbd569b5ddcd98aee68b0c9000b4be6d7ff0737e2d758718258418
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  locator: Actual execution 2026-10-21T14:23:54.792469+00:00 to 2026-10-21T14:23:56.432686+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T14:23:56.432686Z'
  snapshot_sha256: 99d60d3b748ae2d7f07c3ed39b32c13ddbb59589f2ac7f992806ad963405aa73
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Cable_Bacteria_Photosynthetic_Biofilm_Sediment
  locator: Actual execution 2026-10-21T14:23:55.791453+00:00 to 2026-10-21T14:23:56.657245+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T14:23:56.657245Z'
  snapshot_sha256: a6a9a7a249608b628901ebfe9be56c35563328904f16e3c0b583e4c9648d3625
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T14:23:56.658038+00:00 to 2026-10-21T14:23:56.719719+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T14:23:56.719719Z'
  snapshot_sha256: 93dd221091b3a9e50ad3b5d63550d134aacd40c42b884f0bd0094c4d12e5f589
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
  locator: Actual execution 2026-10-21T14:23:56.720002+00:00 to 2026-10-21T14:23:58.058529+00:00
  summary: Reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T14:23:58.058529Z'
  snapshot_sha256: 2acc5d4201254cff4e703129281b30432755f7faaabb227e9c6b7d9c883d000c
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
  topic: Natural sediment assemblage and supported taxonomic resolution
  outcome: supported
  summary: Retain the family-level cable bacteria and phylum-level diatom biofilm
    as the resolved focal groups.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - identity
  - ontology
  - history
  dimensions:
  - name: community_scope
    value: Sediment community with cable bacteria and photosynthetic biofilm
    definition: Not an isolated defined two-member culture or exhaustive sediment
      membership list.
    evidence_ids:
    - identity
  - name: taxon_rank
    value: Desulfobulbaceae family; Bacillariophyta phylum
    definition: The source supports broad groups, not a species or strain assignment.
    evidence_ids:
    - identity
    - ontology
  - name: strain
    value: Unresolved and not required by the source
    definition: No invented cultured strain or sequence accession.
    evidence_ids:
    - identity
  - name: grounding_status
    value: Family GTDB mapping and diatom no-equivalent status retained
    definition: Local labels agree; no forced species-level or prokaryotic classification
      of diatoms.
    evidence_ids:
    - ontology
    - semantics
  - name: environment
    value: Coastal sediment incubated under overlying seawater
    definition: ENVO sediment is broad but compatible; natural provenance and laboratory
      treatment are distinguished.
    evidence_ids:
    - setup
  - name: medium
    value: Source sediment plus aerated filtered seawater
    definition: No defined recipe or exact cross-Mech medium link is established.
    evidence_ids:
    - setup
    - resources
  - name: evidence_tier
    value: Direct full main and six figures; theoretical SI unread
    definition: Current mechanism is explicitly qualified, so missing SI does not
      require certifying its derivation.
    evidence_ids:
    - source-scope
    - independent-source
- assessment_id: state
  area: scope
  topic: State, origin and category
  outcome: supported
  summary: Retain TRANSIENT, NATURAL and OTHER for the developing sediment incubation
    community.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - identity
  - experiment-1
  - experiment-2
  - schema
  details: New biofilm development and cable-bacteria growth over days support the
    developing/transient context. Rapid chemical responses alone would not establish
    community transience. Laboratory conditioning of a natural assemblage does not
    automatically make origin ENGINEERED; ecological state is a separate optional
    field.
- assessment_id: roles
  area: evidence
  topic: Taxonomy functional-role support
  outcome: concern
  summary: The roles are supported by the full source, but their local excerpts establish
    identity only.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - roles
  - identity
  - schema
  - record
  details: Retain cable-bacteria CROSS_FEEDER for phototroph-derived oxygen use and
    diatom PRIMARY_PRODUCER for photosynthesis/carbon assimilation. Add narrow role
    evidence rather than treating family affiliation or diatom dominance alone as
    functional proof. No reciprocal syntrophy, organic-only substrate restriction
    or obligacy is imposed.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain photosynthetic oxygen cross-feeding at the current community-level
    scope.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - oxygen-coupling
  - roles
  details: The source perturbs light, verifies oxygen production and follows sulfide
    responses. The graph does not claim reciprocal benefit or species-resolved interaction.
    The broad roster is appropriate to the observed biofilm and cable filaments.
- assessment_id: arrow-0-1
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: Retain oxygen supply as the supported surface electron-acceptor link to
    deeper sulfide oxidation.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - oxygen-coupling
  - chemistry
  - mechanistic-limits
  details: The source supports coupled responses, while exact redox-site allocation
    remains an interpretation. No need to turn this qualified physiological link into
    a claim of an isolated molecular mechanism.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain interpreted electrogenic sulfide oxidation with the current conduction
    and mechanism limits.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - oxygen-coupling
  - chemistry
  - mechanistic-limits
  details: Conduction along a multicellular filament is not separately classified
    as exchange between organisms. The observed geochemical fingerprint and filaments
    support the interpretation; the main presents spatial regulation and motility
    as proposals.
- assessment_id: arrow-1-2
  area: graph
  topic: ecological_interactions[1].downstream[0]
  outcome: supported
  summary: Retain electrical coupling as the source interpretation for rapid deep
    sulfide responses.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - oxygen-coupling
  - experiment-1
  - mechanistic-limits
  details: Minute-scale responses support coupling relative to slow diffusion. They
    do not uniquely distinguish biochemical regulation from movement or validate the
    unread SI constant-flux derivation.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: Retain rapid repeatable redox responses without inflating replication or
    significance.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - experiment-1
  - experiment-2
  - statistics
  details: Four light/dark cycles are repeated observations, not four independent
    cores. Experiment 2 has separate baseline and treatment/control sample counts.
    Existing current-density and sulfide-depth significance caveats are source-faithful.
- assessment_id: chemicals
  area: grounding
  topic: Metabolites and related ingredients
  outcome: supported
  summary: Retain neutral H2S for measured free sulfide and O2 for the electron acceptor.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - chemistry
  - ontology
  details: The ingredient note correctly distinguishes H2S from calculated H2S plus
    HS− and from sulfide(2−). No exclusive uptake form, fixed dissolved concentration
    or universally oxic sediment is inferred. The O2 ingredient description is consistent
    with the source.
- assessment_id: context
  area: completeness
  topic: Sediment incubation and local evidence context
  outcome: concern
  summary: Recover available phase-specific setup, conditions and role evidence.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - setup
  - experiment-1
  - experiment-2
  - roles
  details: The record currently gives generic light/dark and sulfide context but omits
    temperature, salinity, core preparation, staged conditioning and the two experimental
    schedules. Preserve layered redox conditions, shared-water flow and measurement
    timing; no unreported working volume or full medium formulation is supplied.
- assessment_id: resource
  area: representation
  topic: associated_datasets[0]
  outcome: concern
  summary: The PMID/PMC entry denotes the publication rather than a distinct phenotype
    collection.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - resource-identity
  - resources
  - dataset-schema
  details: Keep a traceable article link as an external narrative/publication resource.
    A data object would require its own specific identity and scope; do not infer
    that no study data exist or create a new accession from the PMID.
- assessment_id: provenance
  area: provenance
  topic: Previous repairs and current source boundary
  outcome: supported
  summary: Retain the later taxonomic/chemical repair and existing graph limits.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - history
  - snippets
  - source-scope
  details: Earlier ledger certification was limited to its stated fields and access
    scope. The present review adds complete main/figure assessment and narrower context/resource
    findings. The SI is still uninspected; no prior decision substitutes for reading
    its model derivation.
- assessment_id: validation
  area: schema
  topic: Native checks and source-specific review
  outcome: supported
  summary: All eight focused native gates pass; two bounded context/resource findings
    remain.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - ontology
  - check-validate
  - check-validate-references-explained
  - source-scope
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Scores describe current encoded fields and diagnostics, including the misclassified
    article item.
  target_ids:
  - CommunityMech:000145
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 75
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role score + 5 environment + 10 for at least
      three interaction nodes + 5 associated dataset + 5 metabolites. No three-factor,
      growth-medium or external-resource bonus.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 − 50P1 − 10P2 − 2P3 + 20min(mean node evidence/2,1) + 15
      if COMPLETE,0,100). P1=0/P2=0/P3=2/P4=0; four evidence/three nodes gives 13.3333333333;
      COMPLETE adds 15; raw 124.3333333333 capped 100.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 0
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
- finding_id: recover-context
  issue_key: cm-000145-recover-context
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: source-supported completeness and evidence placement
    can be improved; no role is shown false and no mandatory cultivation field is
    missing.'
  rule_id: review-checklist.claim-specific-context-and-resource-representation
  status: open
  certainty: confirmed
  title: Recover incubation context and narrow role evidence
  description: The record omits available temperature, salinity, sediment-core preparation
    and separate incubation schedules. Its local taxonomy excerpts establish family/phylum
    identity rather than the supported oxygen-recipient and primary-production functions.
    Recover these details from the actual main Methods and functional discussion without
    changing the valid broad roster or graph.
  target_ids:
  - CommunityMech:000145
  field_paths:
  - growth_media
  - cultivation_setup
  - environmental_factors[0]
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  evidence_ids:
  - setup
  - experiment-1
  - experiment-2
  - roles
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
    role: canonical_record
- finding_id: article-as-dataset
  issue_key: cm-000145-article-as-dataset
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: a valid source identifier has the wrong resource role;
    no broken citation or global absence of study data is inferred.'
  rule_id: review-checklist.claim-specific-context-and-resource-representation
  status: open
  certainty: confirmed
  title: Represent the primary article as a publication resource
  description: associated_datasets[0] uses PMID-25416774 and a PMC article URL for
    a PHENOTYPE dataset. The identifier resolves to the publication, not an independently
    identified collection of measurements. Preserve the source link in a publication/narrative-resource
    representation.
  target_ids:
  - CommunityMech:000145
  field_paths:
  - associated_datasets[0]
  - external_resources
  evidence_ids:
  - resource-identity
  - resources
  - dataset-schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
    role: canonical_record
actions:
- action_id: recover-experimental-context
  description: Add source-specific sediment incubation and functional evidence while
    preserving phase and redox boundaries.
  finding_ids:
  - recover-context
  target_ids:
  - CommunityMech:000145
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
    role: canonical_record
  acceptance_checks:
  - 'Describe natural Rattekaai sediment preparation: top 8 cm, 500 micrometre sieve,
    homogenization and 4 cm diameter Plexiglas core liners. Keep collection dates
    as provenance; do not assign collection years to individual experiments without
    explicit source support or infer a working volume from diameter.'
  - Record 16 ± approximately 1 C and filtered aerated Oosterschelde seawater at salinity
    28 ± 1 per mille. Preserve oxygenated overlying water and suboxic/anoxic sediment
    layers; do not label the entire sediment uniformly aerobic or invent a defined
    recipe.
  - Separate experiment 1’s 20-day dark conditioning, seven-day indirect-sunlight
    biofilm development and four-day 12 h light/12 h dark assay from experiment 2’s
    one-week preincubation and seven-day treatment. Include the approximately 300
    micromol photons m−2 s−1 lighting with its experiment-specific fluorescent/LED
    source.
  - Keep experiment 2 baseline n=3 and treatment/control n=2 distinct from repeated
    light/dark cycles in experiment 1. Shared water recirculation of 20 litres/h is
    not a core feed/dilution rate; the four-hour dark wait is measurement timing.
    Observed pH profiles are responses, not prescribed setpoints.
  - Attach narrow evidence for phototrophic carbon assimilation/oxygen production
    and cable-bacteria oxygen use in addition to the current identity snippets. Retain
    CROSS_FEEDER and PRIMARY_PRODUCER at the resolved group level; do not add reciprocal
    benefit, species/strain identities or an obligatory syntrophic mechanism.
  - Retain all three nodes, both qualified arrows and existing significance/replication
    caveats. Treat the unread SI derivation as unresolved, not as a verified model.
    Validate schema, terms, references, GTDB/domain and history after separately authorized
    curation.
- action_id: reclassify-publication-resource
  description: Keep the primary source discoverable without treating its publication
    identifier as a dataset accession.
  finding_ids:
  - article-as-dataset
  target_ids:
  - CommunityMech:000145
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cable_Bacteria_Photosynthetic_Biofilm_Sediment.yaml
    role: canonical_record
  acceptance_checks:
  - Move the article link to external_resources with the verified PMID/DOI/PMC identity
    and a description of its sediment microsensor/light-perturbation study. Use a
    valid repository value and actual article URL rather than inventing a dataset
    accession.
  - Remove the bibliographic item from associated_datasets when moving it to external_resources.
    Add a replacement dataset only if a specific data collection, table or archive
    asset is independently identified with accurate scope.
  - Keep source citations/evidence and the historical repair record intact. An unread
    theoretical supplement should not be relabeled as a phenotype dataset or a verified
    executable model. Re-run resource/reference validation after curation.
limitations:
- The linked theoretical supplement remains unread. Its constant-flux justification
  and redox-site quantitative derivation are unverified; this review does not certify
  the model beyond the explicit proposal described in main text/Figure6.
- Scientific completion concerns current main-supported record claims and bounded
  follow-up, not full source-package accessibility or model/statistical reproduction.
- No raw sensor traces were downloaded or reanalysed; no previous study was independently
  reread for methods transferred by citation. Existing main Methods are sufficient
  for the stated cultivation follow-up.
- Six main figures were inspected at available display resolution; no counts or numerical
  values were inferred from pixels in place of reported text/table measurements.
- No defined medium recipe, working volume, species/strain resolution, exact CultureMech
  linkage or deposited dataset accession was invented. No data-existence absence claim
  follows from the article-only resource.
- All11 canonical excerpts are supported by direct article/PubMed union and the pinned
  cache. Literal identity snippets alone do not establish a functional role.
- No canonical/cache/history/saved-review edits, model execution, author contact or
  paid provider use occurred.
notes:
- No canonical, cache, history, generated or saved-review file changed; all 25 inspected
  inputs remain pinned.
- Eleven existing snippets match the direct article/PubMed union and cache. Main Methods
  supplement the brief cached excerpts without changing cache bytes.
- Completeness 75 and quality 100/raw 124.3333333333 are mechanical scores. Completed
  assessment concerns current bounded claims, not complete source-package accessibility
  or verification of the theoretical SI.
- No raw-data or statistical reanalysis, model execution, author contact, paid provider
  or later-target work.
tags:
- record-review
- cable-bacteria
- photosynthetic-biofilm
- sediment
- bounded-source
- batch-08
```
