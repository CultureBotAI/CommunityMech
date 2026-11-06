# Brachypodium young-root rhizosphere EcoFAB record review

- Review: 20261021T133158Z-brachypodium-young-root-ecofab-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T13:27:03.606118Z
- Finished UTC: 2026-10-21T13:31:58.218977Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full-source review retains three qualified nodes and two hypothetical arrows. Three major findings address unsupported exudate/medium prescriptions, phylum-wide degrader roles and equilibrium state. Two minor findings qualify the container-effect summary and recover verified sequencing provenance.

## Scope And Provenance

Whole record, all three nodes and two arrows assessed against full main, critical supplements/figures, native ontology/schema, current provenance and bounded archive metadata.

Selection: Only released CommunityMech:000225 in the owned batch08 checkout.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000225 | kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml | maintained | Brachypodium Young Root Rhizosphere EcoFAB Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000225 | Schema validation passed. |
| validate-strict | passed | True | CommunityMech:000225 | Strict validation passed. |
| validate-terms | passed | True | CommunityMech:000225 | Term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000225 | GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000225 | GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000225 | History validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000225 | Read-only cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000225 | Reference validation passed against the pinned cache. |
| audit-network | failed | True | CommunityMech:000225 | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |
| check-network-quality | failed | True | CommunityMech:000225 | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |
| Primary identity and exact excerpts | passed | True | CommunityMech:000225 | Exact identifiers agree; all 23 excerpts match direct full XML. |
| Whole scientific main and critical supplemental assessment | passed | True | CommunityMech:000225 | Full scientific main/SI text, all four main/four SI figures and declared workbook scopes inspected; no raw analysis rerun. |
| Source-linked project and archive scope | passed | True | CommunityMech:000225 | Project and 80 amplicon metadata records verified; exact MAG payload and focal ggKbase project remain unresolved. |
| Exact medium and ingredient correspondence | not_applicable | False | CommunityMech:000225 | Natural soil is the culture substrate/inoculum. No exact formulated medium or characterized exudate mixture supports an additional link. |
| Optional structured source adapter | unavailable | False | CommunityMech:000225 | Same-runtime fresh batch08 discovery explicitly reused; no runnable adapter established or external checkout executed. |

## Scientific And Domain Assessments

### Natural young-root community and selected phylum affiliations

identity: supported. Targets: CommunityMech:000225.

Retain NATURAL origin, RHIZOSPHERE category, real-soil environment and host outside microbial membership. The four phyla are selected observed affiliations, not a complete isolate roster.

### taxonomy[0] through taxonomy[3].functional_role

evidence: concern. Targets: CommunityMech:000225.

Membership/enrichment evidence does not support PRIMARY_DEGRADER for each whole phylum in this community.

The source discusses prior genus/strain examples and community-level genetic potential. Neither attaches degradation of complex substrates to all focal OTUs in each phylum. Remove unsupported optional roles or supply narrower, claim-specific evidence; do not invent replacement roles to preserve a score.

### ecological_state

evidence: concern. Targets: CommunityMech:000225.

A single juvenile-plant harvest and broad spatial similarity do not establish a stable equilibrium community.

The optional STABLE field lacks temporal or equilibrium support. Omission is valid if no defensible state is established; do not automatically replace it with TRANSIENT or ENGINEERED. NATURAL origin remains supported independently.

### ecological_interactions[0]

graph: supported. Targets: CommunityMech:000225.

Retain combined exudate/edaphic selection as a source-proposed hypothesis.

The explicit HYPOTHESIZED description and PARTIAL evidence distinguish the authors’ interpretation from exudate perturbation, chemical measurements or absolute growth.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000225.

Retain the hypothetical selection-to-rhizosphere-OTU direction with its present qualifications.

This is a proposed explanation of relative abundance patterns, not demonstrated exudate necessity or isolated facilitation.

### ecological_interactions[0].downstream[1]

graph: supported. Targets: CommunityMech:000225.

Retain the hypothetical resource-selection-to-KO-repertoire direction.

The edge appropriately avoids treating KO abundance as gene expression, substrate turnover or a measured tip/base exudate gradient.

### ecological_interactions[1]

graph: supported. Targets: CommunityMech:000225.

Retain relative OTU enrichment with mixed within-phylum trends and broadly similar tip/base composition.

Broad participants denote OTU affiliations, not uniform enrichment or greater absolute population growth. Do not turn broadly similar into equivalence of every OTU or every diversity measure.

### ecological_interactions[2]

graph: supported. Targets: CommunityMech:000225.

Retain the tip-versus-bulk KO pattern and existing pooled-library, gene-abundance and no-tip/base-differential-KO limits.

No demonstrated niche partitioning, metabolite use or taxon-specific degradation should be added from the annotation table.

### related_ingredients[0] and [1]

evidence: concern. Targets: CommunityMech:000225.

The ingredient prose asserts an unmeasured spatial chemical gradient and compulsory analog-medium design beyond the source.

Generic exudate/labile-carbon context may be retained as hypothesis. CHEBI:50860 cannot identify composition, concentration or a particular substrate mixture. Soil was the actual medium and inoculum; no necessity test supports either medium prescription.

### description

consistency: concern. Targets: CommunityMech:000225.

The categorical absence of container differences conflicts with the smaller significant container term in Results.

Use mostly similar or smaller container effects while retaining strong location effects. Attribute labile-carbon interpretation as an inference, consistent with the graph; spatial similarity does not establish equivalence or temporal stability.

### environmental_factors, growth_media and cultivation_setup

representation: supported. Targets: CommunityMech:000225.

Retain the detailed soil, host-growth, sampling and container context; no new broth recipe is required.

Soil remains nonsterile under both open and closed secondary containment. The paper’s sterile-closed shorthand does not mean a sterile rhizosphere. Mean day/night temperatures should remain reported greenhouse conditions rather than a new precision/control claim.

### associated_datasets and external_resources

completeness: concern. Targets: CommunityMech:000225.

The empty dataset list omits a directly identified, independently verified sequencing project.

Add the exact project at verified scope. Do not label the 80 observed amplicon records as shotgun libraries, infer all MAG accessions from the project alone or promote generic ggKbase to a resolved focal assembly dataset.

### Prior repairs and current issue scope

provenance: supported. Targets: CommunityMech:000225.

The graph repairs and open ingredient questions remain intact; this whole-record review extends their bounded scope without editing history.

The MD cache contains appended full text despite its abstract_only frontmatter. Exact snippet matching validates wording, not the broader claims attached to that wording.

### Native checks and ontology labels

schema: supported. Targets: CommunityMech:000225.

All eight native checks and six ontology ID/label pairs pass; this does not certify functional-role or state assertions.

### Native mechanical scores

completeness: supported. Targets: CommunityMech:000225.

Scores describe the current record before curation and retain the penalties for all five findings.

## Findings

### ingredient-inference: Keep inferred carbon context separate from measured chemistry and medium requirements

major / open / confirmed; issue key: cm-000225-ingredient-inference.

Both ingredient entries turn general biology or gene-profile interpretation into established spatial chemistry and mandatory analog-medium design. The focal study neither measured a tip/base exudate mixture nor tested either prescription.

### phylum-roles: Do not infer four phylum-wide degrader roles from enrichment

major / open / confirmed; issue key: cm-000225-phylum-roles.

All four PRIMARY_DEGRADER assignments are attached to taxonomic-enrichment excerpts. The primary and supplemental data do not identify degradation of complex substrates by each curated phylum in this system.

### equilibrium-state: Do not represent the 14-day snapshot as ecological equilibrium

major / open / confirmed; issue key: cm-000225-equilibrium-state.

STABLE implies equilibrium under the schema, but the study compares one harvest across spatial locations and containers rather than establishing temporal stability.

### container-summary: Qualify the summary of container effects

minor / open / confirmed; issue key: cm-000225-container-summary.

The description repeats an abstract-level no-container-effect statement while Results reports a statistically significant, smaller container contribution. The graph/discussion already preserve the more nuanced interpretation.

### dataset-provenance: Link the source-identified sequencing project

minor / open / confirmed; issue key: cm-000225-dataset-provenance.

associated_datasets is empty despite explicit PRJNA902408 in Data Availability and matching public project metadata.

## Recommended Actions And Acceptance Checks

### qualify-ingredients

Rewrite ingredient relevance and evidence interpretation at the measured or explicitly hypothetical level.

- Remove assertions that this experiment established distinct tip/base chemistry or that any medium must provide specified spatial/labile-carbon phases.
- If retaining root exudates/labile carbon, label them general context or author-inferred candidate resources; keep CHEBI:50860 generic and do not invent compounds, concentrations or a replacement recipe.
- Preserve actual natural-soil cultivation and all three nodes/two hypothetical arrows. Align description language with the same inference boundary.

### repair-roles

Remove unsupported optional degrader assignments or attach genuinely scoped role evidence.

- Keep supported phylum membership and canonical labels; do not mistake removal of an unsupported role for removal of a member.
- Require exact focal-organism or appropriately scoped community evidence for any retained role. Literature examples from other isolates and relative enrichment alone are insufficient.
- Do not replace with equally unverified roles or infer every member’s function from 3% MAG coverage. Recompute native completeness honestly if optional role removal changes its score.

### repair-state

Omit unsupported STABLE or justify a bounded state with appropriate evidence.

- ecological_state is optional: omit it when no supported state is available; do not invent a required-state schema limitation.
- Do not automatically substitute TRANSIENT or ENGINEERED or infer instability merely from the absence of a time series. Preserve NATURAL origin and the 14-day sampling context.

### qualify-container-summary

Describe predominantly similar profiles with smaller container effects.

- Acknowledge source-reported container R² 0.06336, p 0.00069 relative to location R² 0.10934, p 9.99e−05, or provide an accurate qualitative summary.
- Preserve the distinction among ordination overlap, relative OTU profiles, alpha diversity and KO comparisons. Do not claim every tip/base or container comparison is null.

### add-sequencing-project

Add the verified project with bounded assay and archive scope.

- Add PRJNA902408 with its official project URL, publication and source-grounded description; distinguish experimentally described pooled shotgun metagenomes/MAGs from independently observed amplicon metadata.
- Do not claim that the empty bounded Assembly search proves MAG absence or that all 80 ENA records are shotgun. Keep generic ggKbase as a platform-level lead unless an exact focal project is resolved.
- Run schema, strict, term, reference and history checks after separately authorized curation; preserve current history and immutable review files.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml; Entire canonical record | supports | The natural-soil EcoFAB/container comparison retains three observational/hypothesis nodes and two hypothetical arrows. Non-graph roles, state and ingredient assertions exceed that careful scope. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=37280433&amp;retmode=xml; Article-level identifiers and metadata | supports | PMID 37280433, DOI 10.1038/s43705-023-00265-1 and PMC10244434 identify the focal 2023 paper. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:37280433%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Article-level identifiers and metadata | supports | PMID 37280433, DOI 10.1038/s43705-023-00265-1 and PMC10244434 identify the focal 2023 paper. |
| crossref | https://api.crossref.org/works/10.1038/s43705-023-00265-1; Article-level identifiers and metadata | supports | PMID 37280433, DOI 10.1038/s43705-023-00265-1 and PMC10244434 identify the focal 2023 paper. |
| design | PMID:37280433; Methods: Soil and plant growth conditions; Plant phenotypic measurements; Rhizosphere and bulk soil collection | supports | Bd21-3 plants grew in nonsterile natural soil in EcoFABs, tubes and pots with open/closed secondary containment; rhizosphere and bulk soil were sampled at one 14-day harvest. |
| selection | PMID:37280433; Introduction and Discussion: root exudation and combined selection | supports | The Introduction describes general root-exudation biology. Discussion proposes combined exudate and edaphic selection; this experiment did not measure exudate chemistry, spatial carbon flux or a selective exudate intervention. |
| phyla | PMID:37280433; Results: differentially abundant OTUs; Discussion: phylum patterns | supports | Individual OTUs have varying relative abundance responses. General examples of Mucilaginibacter/Bacillus/Paenibacillus physiology concern prior studies, not demonstrated degradation by all members of the four curated phyla. |
| container | PMID:37280433; Results: Microbiomes in root tips and root base are largely similar yet distinct from bulk soil | supports | MANOVA/adonis reports a smaller but significant container contribution (R² 0.06336, p 0.00069) than location (R² 0.10934, p 9.99e−05). The abstract no-container shorthand is not an accurate universal null result. |
| functional | PMID:37280433; Methods: sequencing and bulk metagenome analysis; Results: KO differences; Discussion: limitations | supports | Biological samples were pooled into nine container-by-location metagenomes. Relative KO abundance differed mainly between tip and bulk, not tip and base; 32 representative MAGs covered approximately 3% of reads. Gene abundance is not expression, degradation flux or phylum-resolved function. |
| cultivation | PMID:37280433; Methods: Soil and plant growth conditions | supports | Natural 0–10 cm grassland soil was sieved at 2 mm; soil was not sterilized. Source conditions support the encoded soil masses, seed preparation, watering schedules, 16-hour photoperiod, humidity and day/night temperatures. Closed Microboxes restrict external exposure; they do not sterilize the soil. |
| data-availability | PMID:37280433; Data availability | supports | The source identifies the sequencing project and generic ggKbase platform; exact focal assembly access remains separately bounded. |
| figures | PMID:37280433; Figures 1–4; supplementary Figures S1–S4 | supports | All eight figures were viewed. They show relative abundance, diversity, MAG associations and KO patterns, not exudate measurements, temporal equilibrium or degradation assays. |
| supplement | PMID:37280433; Supplementary Methods, all captions and Table S4 | supports | Full supplemental text explains MAG phylogeny/abundance methods and cross-container correlations; these do not establish uniform phylum function or a required analog medium. |
| supp-taxa | PMID:37280433; Table S5: four focal phyla rows; Table S6: all 32 MAG rows; workbook-focal-read.json | supports | OTU effects vary within broad phyla. The selected MAGs and their differential abundance are distinct from the whole rhizosphere community; no automatic member expansion or phylum-wide role follows. |
| supp-ko | PMID:37280433; Table S7: all 55 KO rows | supports | KO descriptions, comparisons and statistics contain no taxon attribution column and do not resolve complex-substrate degradation for each curated phylum. |
| schema | src/communitymech/schema/communitymech.yaml; MicrobialCommunity.ecological_state; EcologicalStateEnum.STABLE; FunctionalRoleEnum.PRIMARY_DEGRADER; RelatedIngredient | supports | STABLE denotes equilibrium and ecological_state is optional. PRIMARY_DEGRADER means degradation of complex substrates, without a polymer-only restriction. Ingredient relevance does not authorize unmeasured recipes. |
| ontology | ontology-authority.json; Whole bounded receipt | supports | Six unique ontology pairs across 11 occurrences match current canonical labels. Four membership terms are phyla; CHEBI:50860 is a broad organic-entity concept, not an exact exudate-mixture identity. |
| resources | dataset-verification.json; Whole bounded receipt | supports | Public project metadata agrees with the focal source. ENA metadata lists 80 amplicon runs/samples; the bounded Assembly query and generic ggKbase page do not independently verify focal MAG accession records or establish their global absence. |
| snippets | snippet-audit.json; Whole bounded receipt | supports | All 23 excerpts match direct full XML and the full Markdown cache; 12 also match the abstract/TXT. The MD abstract_only header does not describe its appended full text. |
| history | provenance-audit.json; Whole bounded receipt | supports | The history and exact prior row preserve graph-only repair under closed issue 1264; open issue 1268 retains non-graph follow-up. Recent same-batch issue bodies/comments are reused explicitly. |
| native-target | support-audit.json; Whole bounded receipt | supports | Native graph COMPLETE, three nodes/two arrows/four node evidence. Completeness 80; quality 94.3333333333 after three major and two minor findings. |
| support-manifest | supporting-artifact-manifest.json; Whole bounded receipt | supports | Frozen hashes preserve supporting source, archive, provenance, native metric and input-integrity boundaries. |
| source-scope | lead-source-audit.json; Whole bounded receipt | supports | Lead read the entire scientific main and critical supplemental scopes, viewed four main/four SI figures and preserved all coverage limits. |
| independent-source | root-independent-source-audit.json; Whole bounded receipt | supports | Root independently assessed source science and agreed with the final finding scopes. |
| local-search | Maintained corpus and mappings; local-search.json | supports | Ignored-inclusive bounded searches assessed reusable identity, history and resource context without a global absence claim. |
| adapter | Optional structured source adapter; adapter-check.json | supports | Explicit same-runtime reuse of batch08 discovery establishes no runnable local adapter; another task checkout was not executed. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml; Actual execution 2026-10-21T13:27:31.229124+00:00 to 2026-10-21T13:27:32.194635+00:00 | supports | Schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-strict kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml --out /private/tmp/cm-review-session/batch-08/000225/strict-report.tsv; Actual execution 2026-10-21T13:27:31.229331+00:00 to 2026-10-21T13:27:33.706619+00:00 | supports | Strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-terms kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml; Actual execution 2026-10-21T13:27:31.229491+00:00 to 2026-10-21T13:27:33.225200+00:00 | supports | Term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml; Actual execution 2026-10-21T13:27:32.194974+00:00 to 2026-10-21T13:27:32.281998+00:00 | supports | GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-gtdb-domain kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml; Actual execution 2026-10-21T13:27:32.282260+00:00 to 2026-10-21T13:27:33.747880+00:00 | supports | GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-history history/records/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community; Actual execution 2026-10-21T13:27:33.225618+00:00 to 2026-10-21T13:27:33.997579+00:00 | supports | History validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T13:27:33.998203+00:00 to 2026-10-21T13:27:34.063020+00:00 | supports | Read-only cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src just --no-dotenv validate-references-explained kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml; Actual execution 2026-10-21T13:27:34.063244+00:00 to 2026-10-21T13:27:35.171217+00:00 | supports | Reference validation passed against the pinned cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00 | supports | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00 | supports | Fresh batch08 corpus check reports 57 warnings across 21 of 477 records; the focal graph is natively COMPLETE. |

## Limits And Additional Notes

- No raw sequence processing, new differential-abundance statistics, substrate degradation assay, measured exudate chemistry/flux or temporal stability analysis. Prior-literature physiology was not independently certified for focal organisms.
- Tables S1–S3 were inventoried with headers rather than read row by row. Table S5 reading covered the four curated phyla; all populated Table S6 MAG and Table S7 KO entries and Table S4 cells were read. Dense OTU tree labels were not independently reidentified from pixels.
- The nine shotgun libraries pooled biological samples; the 32 representative MAGs cover approximately 3% of reads. These limits prevent extrapolating gene capacity to all phylum members or measured activity.
- The main container-conditioned two-OTU tip/base statement and reduced-model Table S5 effects have different scopes; no unqualified exact count is imported. Broadly similar composition does not mean all diversity/OTU comparisons are null.
- Archive inspection is metadata only. The bounded Assembly query returned no hits with a phrase-not-found warning; it does not prove global MAG absence. Generic ggKbase access is not a resolved focal project or downloaded assembly.
- CHEBI:50860 is generic organic-entity grounding, not exact mixture chemistry. Seed-preparation agar/ethanol/bleach are not added as rhizosphere medium ingredients.
- All 24 official input pins remain unchanged; no canonical, cache, history, generated or saved-review edits.
- All 23 quotations match direct full XML and appended full MD; only 12 occur in the abstract-only TXT. Cache frontmatter is explicitly distinguished from body scope.
- Native completeness 80 and quality 94.3333 are mechanical diagnostics and do not justify unsupported role restoration.
- Natural soil cultivation and host context are already detailed; no new formulated medium, host membership or causal graph extension is required.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T133158Z-brachypodium-young-root-ecofab-record
kind: record
repository: CultureBotAI/CommunityMech
title: Brachypodium young-root rhizosphere EcoFAB record review
started_at: '2026-10-21T13:27:03.606118Z'
finished_at: '2026-10-21T13:31:58.218977Z'
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
summary: Full-source review retains three qualified nodes and two hypothetical arrows.
  Three major findings address unsupported exudate/medium prescriptions, phylum-wide
  degrader roles and equilibrium state. Two minor findings qualify the container-effect
  summary and recover verified sequencing provenance.
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
  - path: history/records/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community/2026-10-05T142600Z-codex-05415e.yaml
    sha256: 9d3bdf480e775dc4213f099697fc2d29b6c123b1a7053a6b2a8e14b5834ddacb
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    sha256: 674632b452d9a13cb3c42dddd5432e24ecb395b066c03c3e396fe91f89744b04
    role: target
  - path: references_cache/PMID_37280433.md
    sha256: d8146cb62d08544791d04d3394d387434fc56f4fc0489f54d74adec81d188136
    role: context
  - path: references_cache/PMID_37280433.txt
    sha256: 7c6e645a324bd1d64eaaf18b66945ff1c2e5b9a95267ba79c7ca6859c4786093
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
- target_id: CommunityMech:000225
  path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  label: Brachypodium Young Root Rhizosphere EcoFAB Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
scope:
  description: Whole record, all three nodes and two arrows assessed against full
    main, critical supplements/figures, native ontology/schema, current provenance
    and bounded archive metadata.
  selection: Only released CommunityMech:000225 in the owned batch08 checkout.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000225
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Schema validation passed.
  target_ids:
  - CommunityMech:000225
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Strict validation passed.
  target_ids:
  - CommunityMech:000225
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    --out /private/tmp/cm-review-session/batch-08/000225/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Term validation passed.
  target_ids:
  - CommunityMech:000225
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000225
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: GTDB domain validation passed.
  target_ids:
  - CommunityMech:000225
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: History validation passed.
  target_ids:
  - CommunityMech:000225
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only cache-filename preflight passed.
  target_ids:
  - CommunityMech:000225
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Reference validation passed against the pinned cache.
  target_ids:
  - CommunityMech:000225
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Native deterministic checks do not establish adequate taxonomic resolution
    or scientific support.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  target_ids:
  - CommunityMech:000225
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Explicit reuse of fresh batch08 corpus receipts, not a target-specific
    pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  target_ids:
  - CommunityMech:000225
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Explicit reuse of fresh batch08 corpus receipts, not a target-specific
    pass.
- check_id: source-identity
  name: Primary identity and exact excerpts
  status: passed
  required: true
  summary: Exact identifiers agree; all 23 excerpts match direct full XML.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - pubmed
  - epmc
  - crossref
  - snippets
- check_id: scientific-source
  name: Whole scientific main and critical supplemental assessment
  status: passed
  required: true
  summary: Full scientific main/SI text, all four main/four SI figures and declared
    workbook scopes inspected; no raw analysis rerun.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - source-scope
  - independent-source
  - figures
  - supplement
  - supp-ko
- check_id: resource-identity
  name: Source-linked project and archive scope
  status: passed
  required: true
  summary: Project and 80 amplicon metadata records verified; exact MAG payload and
    focal ggKbase project remain unresolved.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - resources
  - data-availability
- check_id: cross-mech
  name: Exact medium and ingredient correspondence
  status: not_applicable
  required: false
  summary: Natural soil is the culture substrate/inoculum. No exact formulated medium
    or characterized exudate mixture supports an additional link.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - cultivation
  - selection
  - ontology
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Same-runtime fresh batch08 discovery explicitly reused; no runnable adapter
    established or external checkout executed.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  locator: Entire canonical record
  summary: The natural-soil EcoFAB/container comparison retains three observational/hypothesis
    nodes and two hypothetical arrows. Non-graph roles, state and ingredient assertions
    exceed that careful scope.
  support: supports
  accessed_at: '2026-10-21T13:31:58.210788Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=37280433&retmode=xml
  locator: Article-level identifiers and metadata
  summary: PMID 37280433, DOI 10.1038/s43705-023-00265-1 and PMC10244434 identify
    the focal 2023 paper.
  support: supports
  accessed_at: '2026-10-21T13:27:31.646317Z'
  snapshot_sha256: e5214f03a0485b908a718b1581e63b738efaab3c3331042ef1451445c74a0c1d
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:37280433%20AND%20SRC:MED&format=json&resultType=core
  locator: Article-level identifiers and metadata
  summary: PMID 37280433, DOI 10.1038/s43705-023-00265-1 and PMC10244434 identify
    the focal 2023 paper.
  support: supports
  accessed_at: '2026-10-21T13:27:32.096216Z'
  snapshot_sha256: df8f7536ee5231e827de63a3fbf45b75183c1178369364174f6c5b1f971cf762
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1038/s43705-023-00265-1
  locator: Article-level identifiers and metadata
  summary: PMID 37280433, DOI 10.1038/s43705-023-00265-1 and PMC10244434 identify
    the focal 2023 paper.
  support: supports
  accessed_at: '2026-10-21T13:27:31.685279Z'
  snapshot_sha256: 30697445e42368bc2147630ee207d57d81530ad5eb5e2e915636e4c4c513192e
- evidence_id: design
  kind: primary_source
  reference: PMID:37280433
  locator: 'Methods: Soil and plant growth conditions; Plant phenotypic measurements;
    Rhizosphere and bulk soil collection'
  summary: Bd21-3 plants grew in nonsterile natural soil in EcoFABs, tubes and pots
    with open/closed secondary containment; rhizosphere and bulk soil were sampled
    at one 14-day harvest.
  support: supports
  accessed_at: '2026-10-21T13:31:58.211803Z'
  snapshot_sha256: 752c270723ee796dd29924e2a09c625e9f4c881aee473893331d73b6bc57f5dc
  quote: 14 days after sowing
- evidence_id: selection
  kind: primary_source
  reference: PMID:37280433
  locator: 'Introduction and Discussion: root exudation and combined selection'
  summary: The Introduction describes general root-exudation biology. Discussion proposes
    combined exudate and edaphic selection; this experiment did not measure exudate
    chemistry, spatial carbon flux or a selective exudate intervention.
  support: supports
  accessed_at: '2026-10-21T13:31:58.211897Z'
  snapshot_sha256: 752c270723ee796dd29924e2a09c625e9f4c881aee473893331d73b6bc57f5dc
  quote: our data also suggests
- evidence_id: phyla
  kind: primary_source
  reference: PMID:37280433
  locator: 'Results: differentially abundant OTUs; Discussion: phylum patterns'
  summary: Individual OTUs have varying relative abundance responses. General examples
    of Mucilaginibacter/Bacillus/Paenibacillus physiology concern prior studies, not
    demonstrated degradation by all members of the four curated phyla.
  support: supports
  accessed_at: '2026-10-21T13:31:58.211982Z'
  snapshot_sha256: 752c270723ee796dd29924e2a09c625e9f4c881aee473893331d73b6bc57f5dc
  quote: showed no clear trends
- evidence_id: container
  kind: primary_source
  reference: PMID:37280433
  locator: 'Results: Microbiomes in root tips and root base are largely similar yet
    distinct from bulk soil'
  summary: MANOVA/adonis reports a smaller but significant container contribution
    (R² 0.06336, p 0.00069) than location (R² 0.10934, p 9.99e−05). The abstract no-container
    shorthand is not an accurate universal null result.
  support: supports
  accessed_at: '2026-10-21T13:31:58.212077Z'
  snapshot_sha256: 752c270723ee796dd29924e2a09c625e9f4c881aee473893331d73b6bc57f5dc
- evidence_id: functional
  kind: primary_source
  reference: PMID:37280433
  locator: 'Methods: sequencing and bulk metagenome analysis; Results: KO differences;
    Discussion: limitations'
  summary: Biological samples were pooled into nine container-by-location metagenomes.
    Relative KO abundance differed mainly between tip and bulk, not tip and base;
    32 representative MAGs covered approximately 3% of reads. Gene abundance is not
    expression, degradation flux or phylum-resolved function.
  support: supports
  accessed_at: '2026-10-21T13:31:58.212178Z'
  snapshot_sha256: 752c270723ee796dd29924e2a09c625e9f4c881aee473893331d73b6bc57f5dc
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:37280433
  locator: 'Methods: Soil and plant growth conditions'
  summary: Natural 0–10 cm grassland soil was sieved at 2 mm; soil was not sterilized.
    Source conditions support the encoded soil masses, seed preparation, watering
    schedules, 16-hour photoperiod, humidity and day/night temperatures. Closed Microboxes
    restrict external exposure; they do not sterilize the soil.
  support: supports
  accessed_at: '2026-10-21T13:31:58.212263Z'
  snapshot_sha256: 752c270723ee796dd29924e2a09c625e9f4c881aee473893331d73b6bc57f5dc
- evidence_id: data-availability
  kind: primary_source
  reference: PMID:37280433
  locator: Data availability
  summary: The source identifies the sequencing project and generic ggKbase platform;
    exact focal assembly access remains separately bounded.
  support: supports
  accessed_at: '2026-10-21T13:31:58.212345Z'
  snapshot_sha256: 752c270723ee796dd29924e2a09c625e9f4c881aee473893331d73b6bc57f5dc
  quote: PRJNA902408
- evidence_id: figures
  kind: primary_source
  reference: PMID:37280433
  locator: Figures 1–4; supplementary Figures S1–S4
  summary: All eight figures were viewed. They show relative abundance, diversity,
    MAG associations and KO patterns, not exudate measurements, temporal equilibrium
    or degradation assays.
  support: supports
  accessed_at: '2026-10-21T13:31:58.212523Z'
  snapshot_sha256: 01a5805fe1bb9dde6af6aa35fee36cb275a6b2a253c7003ed7d4b471744487f6
- evidence_id: supplement
  kind: primary_source
  reference: PMID:37280433
  locator: Supplementary Methods, all captions and Table S4
  summary: Full supplemental text explains MAG phylogeny/abundance methods and cross-container
    correlations; these do not establish uniform phylum function or a required analog
    medium.
  support: supports
  accessed_at: '2026-10-21T13:31:58.212972Z'
  snapshot_sha256: 7bee161549f19d322b9a5d652e4f43428e7e8b89ddaf0c9b4b9de0e5ba8fe047
- evidence_id: supp-taxa
  kind: primary_source
  reference: PMID:37280433
  locator: 'Table S5: four focal phyla rows; Table S6: all 32 MAG rows; workbook-focal-read.json'
  summary: OTU effects vary within broad phyla. The selected MAGs and their differential
    abundance are distinct from the whole rhizosphere community; no automatic member
    expansion or phylum-wide role follows.
  support: supports
  accessed_at: '2026-10-21T13:31:58.213401Z'
  snapshot_sha256: 92d6e4ee79bde5a7c63efb3e73776049761e440419b2092caeb7d128fcb9066a
- evidence_id: supp-ko
  kind: primary_source
  reference: PMID:37280433
  locator: 'Table S7: all 55 KO rows'
  summary: KO descriptions, comparisons and statistics contain no taxon attribution
    column and do not resolve complex-substrate degradation for each curated phylum.
  support: supports
  accessed_at: '2026-10-21T13:31:58.213569Z'
  snapshot_sha256: aed3f8d75dc90872ebd851e53267f89cb52e0ef6ddbd682643b185a73ff12600
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity.ecological_state; EcologicalStateEnum.STABLE; FunctionalRoleEnum.PRIMARY_DEGRADER;
    RelatedIngredient
  summary: STABLE denotes equilibrium and ecological_state is optional. PRIMARY_DEGRADER
    means degradation of complex substrates, without a polymer-only restriction. Ingredient
    relevance does not authorize unmeasured recipes.
  support: supports
  accessed_at: '2026-10-21T13:31:58.213648Z'
  snapshot_sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
- evidence_id: ontology
  kind: authority
  reference: ontology-authority.json
  locator: Whole bounded receipt
  summary: Six unique ontology pairs across 11 occurrences match current canonical
    labels. Four membership terms are phyla; CHEBI:50860 is a broad organic-entity
    concept, not an exact exudate-mixture identity.
  support: supports
  accessed_at: '2026-10-21T13:31:58.213783Z'
  snapshot_sha256: 31a5dc5b97b680aec0e6b73fa9cf164de52f6fbe59bd1ed9ed1eb3073a0b01ae
- evidence_id: resources
  kind: database
  reference: dataset-verification.json
  locator: Whole bounded receipt
  summary: Public project metadata agrees with the focal source. ENA metadata lists
    80 amplicon runs/samples; the bounded Assembly query and generic ggKbase page
    do not independently verify focal MAG accession records or establish their global
    absence.
  support: supports
  accessed_at: '2026-10-21T13:31:58.213971Z'
  snapshot_sha256: f028a1a388e5f2fb7034902b33a321da5d828e41c9d4c5ac6d77154bb419fd47
- evidence_id: snippets
  kind: validation
  reference: snippet-audit.json
  locator: Whole bounded receipt
  summary: All 23 excerpts match direct full XML and the full Markdown cache; 12 also
    match the abstract/TXT. The MD abstract_only header does not describe its appended
    full text.
  support: supports
  accessed_at: '2026-10-21T13:31:58.214137Z'
  snapshot_sha256: 2dc52f3a041f5686cebcfcdbc72267f5ffcf7ea67968e85c0d2a0e4df7bfd95b
- evidence_id: history
  kind: record_content
  reference: provenance-audit.json
  locator: Whole bounded receipt
  summary: The history and exact prior row preserve graph-only repair under closed
    issue 1264; open issue 1268 retains non-graph follow-up. Recent same-batch issue
    bodies/comments are reused explicitly.
  support: supports
  accessed_at: '2026-10-21T13:31:58.214305Z'
  snapshot_sha256: 8f7921325dbc05361d3af508e74a8def1e93c0c6cb05741931e6ba715ad33315
- evidence_id: native-target
  kind: validation
  reference: support-audit.json
  locator: Whole bounded receipt
  summary: Native graph COMPLETE, three nodes/two arrows/four node evidence. Completeness
    80; quality 94.3333333333 after three major and two minor findings.
  support: supports
  accessed_at: '2026-10-21T13:31:58.214353Z'
  snapshot_sha256: f873d14c26b2b4d6671b8fdb72f908c50e16bf258e1f79590420591603b8dfd1
- evidence_id: support-manifest
  kind: validation
  reference: supporting-artifact-manifest.json
  locator: Whole bounded receipt
  summary: Frozen hashes preserve supporting source, archive, provenance, native metric
    and input-integrity boundaries.
  support: supports
  accessed_at: '2026-10-21T13:31:58.214492Z'
  snapshot_sha256: cdd18dbceb04caceca4d6db3dbe9a9a629757786cd17bf009d0277e26a28fe51
- evidence_id: source-scope
  kind: validation
  reference: lead-source-audit.json
  locator: Whole bounded receipt
  summary: Lead read the entire scientific main and critical supplemental scopes,
    viewed four main/four SI figures and preserved all coverage limits.
  support: supports
  accessed_at: '2026-10-21T13:31:58.214677Z'
  snapshot_sha256: 385b670e1f928d6b172e771786639e4eedc4910e708e3328bac575e225a9070b
- evidence_id: independent-source
  kind: validation
  reference: root-independent-source-audit.json
  locator: Whole bounded receipt
  summary: Root independently assessed source science and agreed with the final finding
    scopes.
  support: supports
  accessed_at: '2026-10-21T13:31:58.214716Z'
  snapshot_sha256: 125b5513f0041c2b746fc5080dcd89d6439ff48db119a2eee66c515f6c1ace5a
- evidence_id: local-search
  kind: search
  reference: Maintained corpus and mappings
  locator: local-search.json
  summary: Ignored-inclusive bounded searches assessed reusable identity, history
    and resource context without a global absence claim.
  support: supports
  accessed_at: '2026-10-21T13:31:58.214859Z'
  snapshot_sha256: 6a102b1d135e6df8314b69a4e66d886f5d5a5b83a80ec7c3e4708647de2a487d
  search_scope: Exact focal identity and relevant terms within maintained record/taxon/mapping
    roots, including ignored files.
- evidence_id: adapter
  kind: search
  reference: Optional structured source adapter
  locator: adapter-check.json
  summary: Explicit same-runtime reuse of batch08 discovery establishes no runnable
    local adapter; another task checkout was not executed.
  support: supports
  accessed_at: '2026-10-21T13:31:58.214913Z'
  snapshot_sha256: c467b20ca44c2d36df9bede1d61d5ebed01efd47b32eb904afdf021b76a7b9fe
  search_scope: Original batch08 PATH, venv/module and ignored-inclusive filenames
    plus current runtime verification; no new global search.
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  locator: Actual execution 2026-10-21T13:27:31.229124+00:00 to 2026-10-21T13:27:32.194635+00:00
  summary: Schema validation passed.
  support: supports
  accessed_at: '2026-10-21T13:27:32.194635Z'
  snapshot_sha256: 3b99593876a250ae9bbba7e37c188a09102da7685b0dc1d1911165beea901729
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-strict kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    --out /private/tmp/cm-review-session/batch-08/000225/strict-report.tsv
  locator: Actual execution 2026-10-21T13:27:31.229331+00:00 to 2026-10-21T13:27:33.706619+00:00
  summary: Strict validation passed.
  support: supports
  accessed_at: '2026-10-21T13:27:33.706619Z'
  snapshot_sha256: cd28c87fb700aedda9800957f8e877b712dfea2787fd960323c8f0f69ae64c5c
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-terms kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  locator: Actual execution 2026-10-21T13:27:31.229491+00:00 to 2026-10-21T13:27:33.225200+00:00
  summary: Term validation passed.
  support: supports
  accessed_at: '2026-10-21T13:27:33.225200Z'
  snapshot_sha256: 83676631651951c4f39fbe33da3a06b263e94d610152cee64cd6f7e865a2c490
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  locator: Actual execution 2026-10-21T13:27:32.194974+00:00 to 2026-10-21T13:27:32.281998+00:00
  summary: GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T13:27:32.281998Z'
  snapshot_sha256: 671fa25054df159b5ef8093a6e1c06e60d47a23122404bf4e4297b03acec87d0
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-gtdb-domain kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  locator: Actual execution 2026-10-21T13:27:32.282260+00:00 to 2026-10-21T13:27:33.747880+00:00
  summary: GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T13:27:33.747880Z'
  snapshot_sha256: bd70245bed9814a7cfc16e498dfdc60f284254f45e2c363087372da5360216bc
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-history history/records/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community
  locator: Actual execution 2026-10-21T13:27:33.225618+00:00 to 2026-10-21T13:27:33.997579+00:00
  summary: History validation passed.
  support: supports
  accessed_at: '2026-10-21T13:27:33.997579Z'
  snapshot_sha256: 160f30ad7780fff279aa66a2788ad488d091b050e6933111fe700d77294e73e0
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T13:27:33.998203+00:00 to 2026-10-21T13:27:34.063020+00:00
  summary: Read-only cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T13:27:34.063020Z'
  snapshot_sha256: c677af6cdca87cfbc5ec03fae63654fc9f0ade853b70d7e8befb7973e5ba0407
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src
    just --no-dotenv validate-references-explained kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
  locator: Actual execution 2026-10-21T13:27:34.063244+00:00 to 2026-10-21T13:27:35.171217+00:00
  summary: Reference validation passed against the pinned cache.
  support: supports
  accessed_at: '2026-10-21T13:27:35.171217Z'
  snapshot_sha256: 371ef4ed54d77a4c8c5512710e92fbf843d323e60c16bb1aa22774ba6c85b23a
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T13:06:00.734617+00:00 to 2026-10-21T13:06:11.311177+00:00
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:11.311177Z'
  snapshot_sha256: 2d17097db768619fa7fea156f7c37781fa9cd463a6abdce6f529112518848cf0
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-08/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T13:06:00.741568+00:00 to 2026-10-21T13:06:15.408522+00:00
  summary: Fresh batch08 corpus check reports 57 warnings across 21 of 477 records;
    the focal graph is natively COMPLETE.
  support: supports
  accessed_at: '2026-10-21T13:06:15.408522Z'
  snapshot_sha256: 1332cfd7980ec54d517d625aff43fa6328c1a19fd405a7aef071f78af9774f3f
assessments:
- assessment_id: identity
  area: identity
  topic: Natural young-root community and selected phylum affiliations
  outcome: supported
  summary: Retain NATURAL origin, RHIZOSPHERE category, real-soil environment and
    host outside microbial membership. The four phyla are selected observed affiliations,
    not a complete isolate roster.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - design
  - phyla
  - record
  - ontology
  dimensions:
  - name: community_scope
    value: Young Brachypodium rhizosphere from natural soil
    definition: Root-tip/base and bulk-soil comparisons across three containers; not
      a defined SynCom.
    evidence_ids:
    - design
  - name: source_strain
    value: Brachypodium Bd21-3 is host context
    definition: No microbial strain identity follows from broad phylum OTUs or selected
      MAGs.
    evidence_ids:
    - design
    - supp-taxa
  - name: taxon_rank
    value: Four bacterial phyla
    definition: Canonical names and curated GTDB summaries are broad affiliations,
      not every member or individual MAG identity.
    evidence_ids:
    - ontology
  - name: grounding_status
    value: Existing GROUNDED phylum mappings pass native checks
    definition: The Bacillota majority mapping is not a complete classification of
      all source OTUs.
    evidence_ids:
    - ontology
  - name: environment
    value: Young root rhizosphere in natural grassland soil
    definition: Physical environment and inoculum source are already explicit.
    evidence_ids:
    - design
    - cultivation
  - name: medium
    value: Nonsterile natural soil
    definition: A formulated medium or required exudate analog was not tested.
    evidence_ids:
    - cultivation
    - selection
  - name: experimental_setting
    value: Single 14-day harvest; pooled shotgun libraries
    definition: Separate biological replication of 16S from nine pooled metagenome
      libraries.
    evidence_ids:
    - design
    - functional
  - name: evidence_tier
    value: Community profiles plus author hypothesis
    definition: Relative 16S/KO associations do not measure carbon flux or temporal
      stability.
    evidence_ids:
    - selection
    - functional
- assessment_id: roles
  area: evidence
  topic: taxonomy[0] through taxonomy[3].functional_role
  outcome: concern
  summary: Membership/enrichment evidence does not support PRIMARY_DEGRADER for each
    whole phylum in this community.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - phyla
  - functional
  - supp-taxa
  - supp-ko
  - schema
  details: The source discusses prior genus/strain examples and community-level genetic
    potential. Neither attaches degradation of complex substrates to all focal OTUs
    in each phylum. Remove unsupported optional roles or supply narrower, claim-specific
    evidence; do not invent replacement roles to preserve a score.
- assessment_id: state
  area: evidence
  topic: ecological_state
  outcome: concern
  summary: A single juvenile-plant harvest and broad spatial similarity do not establish
    a stable equilibrium community.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - design
  - schema
  - figures
  details: The optional STABLE field lacks temporal or equilibrium support. Omission
    is valid if no defensible state is established; do not automatically replace it
    with TRANSIENT or ENGINEERED. NATURAL origin remains supported independently.
- assessment_id: node-0
  area: graph
  topic: ecological_interactions[0]
  outcome: supported
  summary: Retain combined exudate/edaphic selection as a source-proposed hypothesis.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - selection
  - functional
  details: The explicit HYPOTHESIZED description and PARTIAL evidence distinguish
    the authors’ interpretation from exudate perturbation, chemical measurements or
    absolute growth.
- assessment_id: arrow-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: Retain the hypothetical selection-to-rhizosphere-OTU direction with its
    present qualifications.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - selection
  - phyla
  details: This is a proposed explanation of relative abundance patterns, not demonstrated
    exudate necessity or isolated facilitation.
- assessment_id: arrow-1
  area: graph
  topic: ecological_interactions[0].downstream[1]
  outcome: supported
  summary: Retain the hypothetical resource-selection-to-KO-repertoire direction.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - selection
  - functional
  - supp-ko
  details: The edge appropriately avoids treating KO abundance as gene expression,
    substrate turnover or a measured tip/base exudate gradient.
- assessment_id: node-1
  area: graph
  topic: ecological_interactions[1]
  outcome: supported
  summary: Retain relative OTU enrichment with mixed within-phylum trends and broadly
    similar tip/base composition.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - phyla
  - container
  - figures
  - supp-taxa
  details: Broad participants denote OTU affiliations, not uniform enrichment or greater
    absolute population growth. Do not turn broadly similar into equivalence of every
    OTU or every diversity measure.
- assessment_id: node-2
  area: graph
  topic: ecological_interactions[2]
  outcome: supported
  summary: Retain the tip-versus-bulk KO pattern and existing pooled-library, gene-abundance
    and no-tip/base-differential-KO limits.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - functional
  - supp-ko
  - figures
  details: No demonstrated niche partitioning, metabolite use or taxon-specific degradation
    should be added from the annotation table.
- assessment_id: ingredients
  area: evidence
  topic: related_ingredients[0] and [1]
  outcome: concern
  summary: The ingredient prose asserts an unmeasured spatial chemical gradient and
    compulsory analog-medium design beyond the source.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - selection
  - functional
  - cultivation
  - schema
  details: Generic exudate/labile-carbon context may be retained as hypothesis. CHEBI:50860
    cannot identify composition, concentration or a particular substrate mixture.
    Soil was the actual medium and inoculum; no necessity test supports either medium
    prescription.
- assessment_id: summary
  area: consistency
  topic: description
  outcome: concern
  summary: The categorical absence of container differences conflicts with the smaller
    significant container term in Results.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - container
  - record
  details: Use mostly similar or smaller container effects while retaining strong
    location effects. Attribute labile-carbon interpretation as an inference, consistent
    with the graph; spatial similarity does not establish equivalence or temporal
    stability.
- assessment_id: cultivation
  area: representation
  topic: environmental_factors, growth_media and cultivation_setup
  outcome: supported
  summary: Retain the detailed soil, host-growth, sampling and container context;
    no new broth recipe is required.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - cultivation
  - design
  details: Soil remains nonsterile under both open and closed secondary containment.
    The paper’s sterile-closed shorthand does not mean a sterile rhizosphere. Mean
    day/night temperatures should remain reported greenhouse conditions rather than
    a new precision/control claim.
- assessment_id: resources
  area: completeness
  topic: associated_datasets and external_resources
  outcome: concern
  summary: The empty dataset list omits a directly identified, independently verified
    sequencing project.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - data-availability
  - resources
  - record
  details: Add the exact project at verified scope. Do not label the 80 observed amplicon
    records as shotgun libraries, infer all MAG accessions from the project alone
    or promote generic ggKbase to a resolved focal assembly dataset.
- assessment_id: history
  area: provenance
  topic: Prior repairs and current issue scope
  outcome: supported
  summary: The graph repairs and open ingredient questions remain intact; this whole-record
    review extends their bounded scope without editing history.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - history
  - snippets
  details: The MD cache contains appended full text despite its abstract_only frontmatter.
    Exact snippet matching validates wording, not the broader claims attached to that
    wording.
- assessment_id: validation
  area: schema
  topic: Native checks and ontology labels
  outcome: supported
  summary: All eight native checks and six ontology ID/label pairs pass; this does
    not certify functional-role or state assertions.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - check-validate
  - check-validate-references-explained
  - ontology
  - schema
- assessment_id: metrics
  area: completeness
  topic: Native mechanical scores
  outcome: supported
  summary: Scores describe the current record before curation and retain the penalties
    for all five findings.
  target_ids:
  - CommunityMech:000225
  evidence_ids:
  - native-target
  metrics:
  - name: completeness
    value: 80
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required-field/taxon-role component +5 environment +10 interaction
      count +5 resources +10 media; no three-factor, dataset or node-metabolite bonus.
  - name: validation_quality
    value: 94.33333333333333
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100−50P1−10P2−2P3+20min(mean node evidence/2,1)+15 if COMPLETE,0,100).
      Counts 0/3/2/0; four node evidence/three nodes gives 13.3333 bonus; COMPLETE
      adds 15; final 94.3333.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 3
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
- finding_id: ingredient-inference
  issue_key: cm-000225-ingredient-inference
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: material mechanistic and experimental-scope inflation
    outside an otherwise qualified graph.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Keep inferred carbon context separate from measured chemistry and medium
    requirements
  description: Both ingredient entries turn general biology or gene-profile interpretation
    into established spatial chemistry and mandatory analog-medium design. The focal
    study neither measured a tip/base exudate mixture nor tested either prescription.
  target_ids:
  - CommunityMech:000225
  field_paths:
  - related_ingredients[0].relevance
  - related_ingredients[0].evidence[0].explanation
  - related_ingredients[1].relevance
  - related_ingredients[1].evidence[0].explanation
  evidence_ids:
  - selection
  - functional
  - cultivation
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
- finding_id: phylum-roles
  issue_key: cm-000225-phylum-roles
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: repeated unsupported functional attribution across the
    entire encoded roster, distinct from valid membership evidence.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Do not infer four phylum-wide degrader roles from enrichment
  description: All four PRIMARY_DEGRADER assignments are attached to taxonomic-enrichment
    excerpts. The primary and supplemental data do not identify degradation of complex
    substrates by each curated phylum in this system.
  target_ids:
  - CommunityMech:000225
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  - taxonomy[2].functional_role
  - taxonomy[3].functional_role
  evidence_ids:
  - phyla
  - functional
  - supp-taxa
  - supp-ko
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
- finding_id: equilibrium-state
  issue_key: cm-000225-equilibrium-state
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2: unsupported whole-community state claim; spatial similarity
    and ecological equilibrium are different assertions.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Do not represent the 14-day snapshot as ecological equilibrium
  description: STABLE implies equilibrium under the schema, but the study compares
    one harvest across spatial locations and containers rather than establishing temporal
    stability.
  target_ids:
  - CommunityMech:000225
  field_paths:
  - ecological_state
  evidence_ids:
  - design
  - schema
  - figures
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
- finding_id: container-summary
  issue_key: cm-000225-container-summary
  category: consistency
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: bounded summary inconsistency; the main spatial result
    and cautious graph remain valid.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Qualify the summary of container effects
  description: The description repeats an abstract-level no-container-effect statement
    while Results reports a statistically significant, smaller container contribution.
    The graph/discussion already preserve the more nuanced interpretation.
  target_ids:
  - CommunityMech:000225
  field_paths:
  - description
  evidence_ids:
  - container
  - record
  - figures
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
- finding_id: dataset-provenance
  issue_key: cm-000225-dataset-provenance
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3: recoverable provenance gap; it does not invalidate the
    scientific results.'
  rule_id: review-checklist.claim-scope-and-completeness
  status: open
  certainty: confirmed
  title: Link the source-identified sequencing project
  description: associated_datasets is empty despite explicit PRJNA902408 in Data Availability
    and matching public project metadata.
  target_ids:
  - CommunityMech:000225
  field_paths:
  - associated_datasets
  evidence_ids:
  - data-availability
  - resources
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
actions:
- action_id: qualify-ingredients
  description: Rewrite ingredient relevance and evidence interpretation at the measured
    or explicitly hypothetical level.
  finding_ids:
  - ingredient-inference
  target_ids:
  - CommunityMech:000225
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Remove assertions that this experiment established distinct tip/base chemistry
    or that any medium must provide specified spatial/labile-carbon phases.
  - If retaining root exudates/labile carbon, label them general context or author-inferred
    candidate resources; keep CHEBI:50860 generic and do not invent compounds, concentrations
    or a replacement recipe.
  - Preserve actual natural-soil cultivation and all three nodes/two hypothetical
    arrows. Align description language with the same inference boundary.
- action_id: repair-roles
  description: Remove unsupported optional degrader assignments or attach genuinely
    scoped role evidence.
  finding_ids:
  - phylum-roles
  target_ids:
  - CommunityMech:000225
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Keep supported phylum membership and canonical labels; do not mistake removal
    of an unsupported role for removal of a member.
  - Require exact focal-organism or appropriately scoped community evidence for any
    retained role. Literature examples from other isolates and relative enrichment
    alone are insufficient.
  - Do not replace with equally unverified roles or infer every member’s function
    from 3% MAG coverage. Recompute native completeness honestly if optional role
    removal changes its score.
- action_id: repair-state
  description: Omit unsupported STABLE or justify a bounded state with appropriate
    evidence.
  finding_ids:
  - equilibrium-state
  target_ids:
  - CommunityMech:000225
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
  acceptance_checks:
  - 'ecological_state is optional: omit it when no supported state is available; do
    not invent a required-state schema limitation.'
  - Do not automatically substitute TRANSIENT or ENGINEERED or infer instability merely
    from the absence of a time series. Preserve NATURAL origin and the 14-day sampling
    context.
- action_id: qualify-container-summary
  description: Describe predominantly similar profiles with smaller container effects.
  finding_ids:
  - container-summary
  target_ids:
  - CommunityMech:000225
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Acknowledge source-reported container R² 0.06336, p 0.00069 relative to location
    R² 0.10934, p 9.99e−05, or provide an accurate qualitative summary.
  - Preserve the distinction among ordination overlap, relative OTU profiles, alpha
    diversity and KO comparisons. Do not claim every tip/base or container comparison
    is null.
- action_id: add-sequencing-project
  description: Add the verified project with bounded assay and archive scope.
  finding_ids:
  - dataset-provenance
  target_ids:
  - CommunityMech:000225
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brachypodium_Young_Root_Rhizosphere_EcoFAB_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Add PRJNA902408 with its official project URL, publication and source-grounded
    description; distinguish experimentally described pooled shotgun metagenomes/MAGs
    from independently observed amplicon metadata.
  - Do not claim that the empty bounded Assembly search proves MAG absence or that
    all 80 ENA records are shotgun. Keep generic ggKbase as a platform-level lead
    unless an exact focal project is resolved.
  - Run schema, strict, term, reference and history checks after separately authorized
    curation; preserve current history and immutable review files.
limitations:
- No raw sequence processing, new differential-abundance statistics, substrate degradation
  assay, measured exudate chemistry/flux or temporal stability analysis. Prior-literature
  physiology was not independently certified for focal organisms.
- Tables S1–S3 were inventoried with headers rather than read row by row. Table S5
  reading covered the four curated phyla; all populated Table S6 MAG and Table S7
  KO entries and Table S4 cells were read. Dense OTU tree labels were not independently
  reidentified from pixels.
- The nine shotgun libraries pooled biological samples; the 32 representative MAGs
  cover approximately 3% of reads. These limits prevent extrapolating gene capacity
  to all phylum members or measured activity.
- The main container-conditioned two-OTU tip/base statement and reduced-model Table
  S5 effects have different scopes; no unqualified exact count is imported. Broadly
  similar composition does not mean all diversity/OTU comparisons are null.
- Archive inspection is metadata only. The bounded Assembly query returned no hits
  with a phrase-not-found warning; it does not prove global MAG absence. Generic ggKbase
  access is not a resolved focal project or downloaded assembly.
- CHEBI:50860 is generic organic-entity grounding, not exact mixture chemistry. Seed-preparation
  agar/ethanol/bleach are not added as rhizosphere medium ingredients.
notes:
- All 24 official input pins remain unchanged; no canonical, cache, history, generated
  or saved-review edits.
- All 23 quotations match direct full XML and appended full MD; only 12 occur in the
  abstract-only TXT. Cache frontmatter is explicitly distinguished from body scope.
- Native completeness 80 and quality 94.3333 are mechanical diagnostics and do not
  justify unsupported role restoration.
- Natural soil cultivation and host context are already detailed; no new formulated
  medium, host membership or causal graph extension is required.
tags:
- record-review
- rhizosphere
- ecofab
- full-source
- batch-08
```
