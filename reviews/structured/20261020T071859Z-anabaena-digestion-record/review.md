# Anabaena digestion: whole-record review

- Review: 20261020T071859Z-anabaena-digestion-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-20T07:13:33.822756Z
- Finished UTC: 2026-10-20T07:18:59.043113Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The public primary source supports the study identity and the graph’s measured-versus-inferred distinctions. Two major findings concern feedstock encoded as the sole community member and overconfident non-graph claims. Four minor findings concern stale source-access statements, a missing declared dataset, an outcome stored as a factor and media linkage. One informational finding concerns phosphate representation. Focused checks pass; corpus warnings remain explicit.

## Scope And Provenance

Whole target: one declared taxon, five nodes, both arrows, all evidence, source context, cultivation representation, chemical/environment terms, dataset provenance and history.

Selection: Second uncovered record of batch 03 in path order, excluding validated baseline and pending batches 01/02.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base ade4a9acdc245e1090522bb4f6ec5fe82ee88689.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000307 | kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml | maintained | Anabaena / MGS-1 Anaerobic-Digestion Methanogen Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000307 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml |
| validate-strict | passed | True | CommunityMech:000307 | uv run python scripts/validate_strict.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml --out /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000307 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000307 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000307 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml |
| validate-history | passed | True | CommunityMech:000307 | No issues found |
| normalize-cache-names-check | passed | True | CommunityMech:000307 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000307 | Validating kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000307 | Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records, 57 warnings in 21 records, zero errors; exit 1. Selected target has no reported network warning. Canonical records are unchanged since this run. |
| check-network-quality | failed | True | CommunityMech:000307 | Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records, 57 warnings in 21 records, zero errors; exit 1. Selected target has no reported network warning. Canonical records are unchanged since this run. |
| Structured expression-source applicability | not_applicable | False | CommunityMech:000307 | No named regulatory gene, locus, transcriptomic module or strain expression dataset is curated. The cited amplicon project was checked through its public metadata; no expression-module claim is made. |

## Scientific And Domain Assessments

### Feedstock versus digesting community; experimental strata

identity: concern. Targets: CommunityMech:000307.

The record identifies the intended study, but its machine-readable membership contradicts its own feedstock exclusion. Three inocula and their matrix-specific outcomes must remain distinguishable during later curation.

### taxonomy[0] and implicit graph participants

grounding: concern. Targets: CommunityMech:000307.

The Anabaena ID/label is valid but is placed in the wrong semantic role. Actual digesting-community membership is unrepresented. The source offers composition at varying ranks; these should not be promoted to a single pooled species list.

### ecological_interactions[0]: Anabaena Biomass Anaerobic Digestion

graph: concern. Targets: CommunityMech:000307.

The process description and endpoint separation are supported. Participant representation is defective because broad scope currently resolves to the feedstock organism alone.

Participants: separate digestion communities acting on supplied biomass, not Anabaena as a live consortium member. Direction: substrate processing toward nutrient/carbon outcomes. Source PMID 40089033 Methods 2.3 and Results 3.2; exact excerpts/locators in feedstock and output.

### ecological_interactions[1]: Fermenter-to-methanogen syntrophy

graph: concern. Targets: CommunityMech:000307.

The HYPOTHESIZED wording appropriately limits the causal claim. It needs corrected community membership, not stronger certainty or an inferred pair of species.

Participants: candidate fermentative and methanogenic guilds in the minimal-medium branch; named partners are not resolved by this review. Direction: proposed donor-to-recipient exchange, without partner-resolved flux. Source locator and exact excerpt: guild, PMID 40089033 Results 3.2.4. Do not generalize across all matrices.

### ecological_interactions[2]: Candidate Sulfate-Reducer Competition in MGS-1 Regolith

graph: concern. Targets: CommunityMech:000307.

The node correctly retains competition as a hypothesis and distinguishes unsuccessful marker amplification from a measured zero product flux. The same participant defect applies.

Participants: proposed competing guilds, not the cyanobacterial substrate. Direction: candidate antagonistic influence, with alternative matrix effects retained. Source PMID 40089033 Results 3.2.4, guild locator/quote. This assessment does not establish exclusion through a single isolated causal mechanism.

### ecological_interactions[3]: Ammonium Production and Organic Carbon Removal

graph: concern. Targets: CommunityMech:000307.

The outcome node preserves the distinction between soluble and unmeasured total-carbon results. Its community scope remains incorrectly linked to the sole feedstock taxon.

Participants: digesting communities; direction: processing to measured nutrient/carbon outcomes. Exact source locators and excerpts: output and cod, PMID 40089033 Results 3.2.1–3.2.2. No specific microbial mediator is established.

### ecological_interactions[4]: MGS-1 Nutrient Recovery Penalty

graph: concern. Targets: CommunityMech:000307.

The PARTIAL description appropriately avoids attributing the recovery penalty solely to competition. It shares the participant defect and omits structured phosphate representation despite mentioning it in prose.

Participants/context: comparative community assays in the regolith matrix. Direction: matrix-associated change in recovered nutrients, not an established microbial donor-recipient edge. Source PMID 40089033 Results 3.2.2–3.2.3, exact excerpt in matrix.

### ecological_interactions[0].downstream[0]

graph: supported. Targets: CommunityMech:000307.

The retained digestion-to-syntrophy arrow is expressly hypothetical and context-limited. It must not be treated as measured transfer or as a process performed by Anabaena.

Source node: biomass digestion. Target node: candidate fermenter/methanogen relationship. Direction and mechanism are tentative; participant correction is handled in the membership finding. Source PMID 40089033 Results 3.2.4; quote/locator in guild.

### ecological_interactions[0].downstream[1]

graph: supported. Targets: CommunityMech:000307.

The digestion-to-outcome arrow is a process/result relation with the total-COD limitation retained. It does not isolate a taxon-specific causal contribution.

Source node: digestion; target node: ammonium/carbon endpoints. Direction: experimental process to reported outcomes. Exact source excerpts and locators in output/cod, PMID 40089033 Results 3.2.1–3.2.2. Other historical arrows remain removed.

### description, environmental_factors[0] and related_ingredients[1]

evidence: concern. Targets: CommunityMech:000307.

The graph preserves uncertainty, but summary and ingredient wording present inferred exchange, exclusion and methane output more definitively. Cross-field certainty should not depend on which part of the record a consumer reads.

### Environment terms, engineering context and metal relevance

grounding: supported. Targets: CommunityMech:000307.

The ontology labels fit laboratory/digester context. Mineral constituents do not by themselves establish a metal-extraction ecological role, so NOT_APPLICABLE is not contradicted by the matrix’s mineral content. The record is an experimental comparison rather than a natural community.

### growth_media[0] and source-access statements

provenance: concern. Targets: CommunityMech:000307.

The medium entry acknowledges alternative matrices, but its paywall rationale is stale. Public source access supports revisiting missing provenance and conditions while preserving assay distinctions; the supplement was not inspected and no complete formulation is certified.

### Publication, BioProject, snippets and history

provenance: concern. Targets: CommunityMech:000307.

Publication identity and all abstract snippets verify. The paper’s declared BioProject is missing from associated_datasets despite a resolvable project record. Sample-specific identity and raw-data quality were not reanalyzed.

### Focused checks and native network completeness

schema: concern. Targets: CommunityMech:000307.

All eight focused/preflight gates pass and cache bytes remain unchanged. Native network integrity is COMPLETE for the encoded taxon set, but broad scope gives credit to a substrate organism. That is why scientific membership review is needed despite green structural gates.

### Native completeness and validation quality

completeness: concern. Targets: CommunityMech:000307.

Completeness 85 and capped validation quality 100 are presence/integrity calculations; they do not resolve the feedstock-member contradiction or overconfident claims.

## Findings

### feedstock-membership: Feedstock is the sole declared community member

major / open / confirmed; issue key: cm-000307-feedstock-membership.

The target explicitly says Anabaena is not a live member but lists it as the only taxon with a producer role. Broad community-level nodes therefore inherit this substrate organism as their only structured participant, while the digesting communities are absent.

### cross-field-certainty: Non-graph fields overstate inferred processes

major / open / confirmed; issue key: cm-000307-cross-field-certainty.

The description and methane ingredient describe exchange, exclusion or product formation more definitively than the graph’s hypothetical/partial wording. Taxonomic guild inference and unsuccessful amplification do not establish partner flux or a measured gas-production endpoint.

### stale-source-access: Paywall and abstract-only rationales are stale

minor / open / confirmed; issue key: cm-000307-stale-source-access.

Several fields say source details cannot be represented because full text is paywalled. The public author copy is accessible and was already noted in the historical graph decision; its Methods name the biomass strain and assay context.

### dataset-linkage: Declared sequencing project is not represented

minor / open / confirmed; issue key: cm-000307-dataset-linkage.

associated_datasets is empty although Methods 2.4.5 cites PRJNA1219353. Public metadata resolves it as a broader Bremen Mars-bioproduction project; paper-specific sample membership has not been checked.

### output-as-factor: A process output is stored as an environmental factor

minor / open / confirmed; issue key: cm-000307-output-as-factor.

The second environmental_factors entry describes nutrient/carbon outcomes already represented by an outcome node. Its label and value describe a result, not an independently supplied condition.

### media-linkage: Alternative assay matrices lack verified resource links

minor / open / confirmed; issue key: cm-000307-media-linkage.

The combined media entry has no CultureMech/MediaIngredientMech linkage. A single generic label cannot establish exact equivalence of the alternatives.

### phosphate-representation: Phosphate is prose-only in the recovery node

informational / open / confirmed; issue key: cm-000307-phosphate-representation.

The recovery node mentions phosphate but has only ammonium in its metabolite list. Future chemical grounding should preserve the measured entity and the distinction between dissolved nutrient recovery and total phosphorus.

## Recommended Actions And Acceptance Checks

### fix-feedstock-membership

Represent feedstock separately from living community membership and preserve inoculum/matrix-specific identities at source-supported ranks.

- A substrate-only organism is not credited as a live participant in digestion interactions.
- Distinct experimental communities are not merged into one asserted member list.
- Unknown participants remain explicit rather than replaced by invented species.
- Run strict, term and network checks.

### fix-cross-field-certainty

Carry the graph’s evidence limits consistently into summaries, factors and ingredient relevance statements.

- Observed endpoints are separated from inferred microbial processes.
- No gas-production measurement is implied solely by identifying a methanogenic guild.
- No zero-flux claim is inferred from marker-amplification failure.
- Run reference and strict checks.

### fix-stale-source-access

Update source-access provenance and distinguish actually inspected primary passages from uninspected supplementary material.

- No categorical paywall assertion remains when a verified public author copy is available.
- Source strain naming remains attached to feedstock, not living digesting members.
- Do not claim complete supplement/formulation verification.

### fix-dataset-linkage

Add source-declared project provenance during curation, making the broader project scope and any unresolved sample mapping explicit.

- The accession resolves and is traceable to the cited paper.
- Do not claim every project sample belongs to this experiment.
- No raw sequence reanalysis is implied.
- Run strict/resource checks.

### fix-output-as-factor

Keep the outcome at its relevant result assertion instead of duplicating it as an environmental condition.

- Conditions and measured outcomes remain distinguishable.
- The source-supported outcome and evidence are preserved.
- Run strict and reference checks.

### fix-media-linkage

Assess exact formulation/resource matches separately when authorized curation revisits this field; retain unresolved matches explicitly.

- No link is inferred solely from a similar medium name.
- Alternative matrices remain distinct.
- Run applicable linkage and strict checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml; Entire target, including five nodes and both downstream arrows | supports | The record explicitly describes Anabaena as substrate, yet taxonomy contains only that organism with a producer role. Broad community-level nodes consequently inherit an inappropriate sole declared participant. |
| primary | PMID:40089033; https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars; author-uploaded article header, Methods 2.1/2.3/2.4.4–2.4.6, Results 3.2.1–3.2.4 and Outlook/Conclusions | supports | Public primary text was independently inspected. The study compares separate inocula across matrices; it is not one defined consortium. The source supplies composition and methodological context beyond the retained abstract. |
| feedstock | PMID:40089033; https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars; Methods 2.1 and 2.3; browser lines 338–412 and 540–749 | supports | The named cyanobacterium supplies biomass; the digesting inocula are distinct. The main text gives a strain designation omitted from the abstract-only rationale. |
| guild | PMID:40089033; https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars; Abstract and Results 3.2.4; lines 1499–1747 | supports | The guild relationship is inferred from taxonomic profiles, not partner-resolved transfer measurements. |
| output | PMID:40089033; https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars; Abstract; Results 3.2.1–3.2.2 | supports | Nutrient and carbon endpoints support an observed processing outcome, without identifying the responsible partner pair. |
| matrix | PMID:40089033; https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars; Abstract; Results 3.2.2–3.2.3 | supports | The nutrient-recovery observation does not isolate microbial competition as its cause. |
| cod | PMID:40089033; https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars; Methods 2.3.3 and Results 3.2.1; lines 734–742 and 1129–1137 | supports | The matrix constrains which carbon measurement can be claimed. |
| publication | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=40089033&amp;retmode=xml; PubMed title, DOI and complete abstract | supports | The DOI and PMID identify the same paper. All 18 target snippets match its retrieved abstract after NFKC/whitespace normalization; this is lexical verification, not proof of every explanation. |
| dataset | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=bioproject&amp;id=1219353&amp;retmode=json; BioProject PRJNA1219353 metadata | supports | The accession cited in Methods 2.4.5 resolves to BioProduction on Mars at Bremen. Its project description is broader than this article; project identity was verified, but individual sample assignments were not reanalyzed. |
| ontology | OAK local NCBITaxon, ENVO, GO and CHEBI snapshots; 11 unique curated identifiers | supports | All ID/label pairs resolve. This does not make feedstock a community member or prove pathway activity. Existing GTDB ambiguity is preserved; no new strain mapping is proposed. |
| schema | src/communitymech/schema/communitymech.yaml; src/communitymech/network/auditor.py; TaxonomicComposition and broad community-level participation semantics | supports | Taxonomy denotes organisms present in the community. A broad community-level interaction credits declared taxa structurally; a prose exclusion does not remove a feedstock entry from that participant set. |
| history | history/records/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium; Whole history event and target row in reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml | supports | Historical graph curation qualified guild claims and retained two arrows. It recorded public source availability while excluding non-graph metadata from certification; old abstract-only/paywall statements remain elsewhere. |
| local-search | references_cache; history/records; reports/causal_graph_review/decisions; kb/taxa; Ignored-inclusive PMID, accession and slug search | supports | The retained source is an abstract-only Markdown cache, not a missing TXT article. Missing dataset, participant and linkage observations concern the full target. External registries were not exhaustively searched for media equivalence. |
| snippets | kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml; All 18 attached snippets versus current PubMed abstract | supports | All normalize to exact abstract substrings. The small excerpts do not support detailed explanations merely because they match; current full-text context was independently checked where material. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml; Actual execution 2026-10-20T07:13:34.927873+00:00 to 2026-10-20T07:13:36.219589+00:00 | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-strict kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml --out /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv; Actual execution 2026-10-20T07:13:34.928585+00:00 to 2026-10-20T07:13:38.494027+00:00 | supports | uv run python scripts/validate_strict.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml --out /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-terms kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml; Actual execution 2026-10-20T07:13:34.936443+00:00 to 2026-10-20T07:13:37.596811+00:00 | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml; Actual execution 2026-10-20T07:13:36.219994+00:00 to 2026-10-20T07:13:36.364384+00:00 | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-gtdb-domain kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml; Actual execution 2026-10-20T07:13:36.364745+00:00 to 2026-10-20T07:13:39.172949+00:00 | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-history history/records/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium; Actual execution 2026-10-20T07:13:37.597509+00:00 to 2026-10-20T07:13:38.993644+00:00 | supports | No issues found |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-20T07:13:39.173565+00:00 to 2026-10-20T07:13:39.239610+00:00 | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv validate-references-explained kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml; Actual execution 2026-10-20T07:13:39.239885+00:00 to 2026-10-20T07:13:40.770884+00:00 | supports | Validating kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv audit-network; Actual run finished 2026-10-20T07:08:14.467705+00:00 | supports | Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records, 57 warnings in 21 records, zero errors; exit 1. Selected target has no reported network warning. Canonical records are unchanged since this run. |
| check-check-network-quality | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src just --no-dotenv check-network-quality; Actual run finished 2026-10-20T07:08:13.673449+00:00 | supports | Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records, 57 warnings in 21 records, zero errors; exit 1. Selected target has no reported network warning. Canonical records are unchanged since this run. |

## Limits And Additional Notes

- The author-uploaded primary text was inspected; separate supplements, PDF figure geometry and raw sequencing/statistical results were not reanalyzed.
- The BioProject is broader than the paper; individual sample-to-experiment mapping remains unverified.
- The source mostly names PCC 7938 but one medium-preparation sentence transposes it to PCC 7398. No new strain ontology mapping is proposed; preserve this source inconsistency when reconciling feedstock identity.
- Community composition varies by inoculum and matrix and is often reported above species rank. Do not construct a single pooled species list or infer partner-resolved flux.
- GTDB candidates remain explicitly ambiguous; passing coherence/domain gates does not resolve a strain mapping.
- All focused checks pass. Required corpus network checks retain their actual warning exits despite no target diagnostic.
- No canonical records, caches, history or generated products changed.
- The initial inspect attempt used a nonexistent TXT suffix and was corrected to the existing Markdown cache after an ignored-inclusive search, before assessment. Successful inspect hashes are the provenance for this review.
- All local input hashes remain unchanged. Browser source-inspection locators and public metadata response hashes are retained.
- Verbatim quotations total 23 words from the paper.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T071859Z-anabaena-digestion-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Anabaena digestion: whole-record review'
started_at: '2026-10-20T07:13:33.822756Z'
finished_at: '2026-10-20T07:18:59.043113Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Target unchanged this session; historical codex curation prevents
    person-level independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: The public primary source supports the study identity and the graph’s measured-versus-inferred
  distinctions. Two major findings concern feedstock encoded as the sole community
  member and overconfident non-graph claims. Four minor findings concern stale source-access
  statements, a missing declared dataset, an outcome stored as a factor and media
  linkage. One informational finding concerns phosphate representation. Focused checks
  pass; corpus warnings remain explicit.
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
  - path: history/records/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium/2026-10-05T084243Z-codex-b65b2f.yaml
    sha256: 74b81a619e6f06ed433552968bbc8f386df76d3943d907611a13182bd1490480
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    sha256: 5cac7e708fb21e2541790ae2b3fd3c33479f9e693537c99d4e8a7dbd49ee6eee
    role: target
  - path: references_cache/PMID_40089033.md
    sha256: a7dc95941ac9d895f089f926e4b487cbe6d6f16811393324766c2865d7d4c5e1
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
- target_id: CommunityMech:000307
  path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  label: Anabaena / MGS-1 Anaerobic-Digestion Methanogen Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
scope:
  description: 'Whole target: one declared taxon, five nodes, both arrows, all evidence,
    source context, cultivation representation, chemical/environment terms, dataset
    provenance and history.'
  selection: Second uncovered record of batch 03 in path order, excluding validated
    baseline and pending batches 01/02.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000307
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml'
  target_ids:
  - CommunityMech:000307
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml\
    \ --out /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv"
  target_ids:
  - CommunityMech:000307
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000307
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000307
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml'
  target_ids:
  - CommunityMech:000307
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: No issues found
  target_ids:
  - CommunityMech:000307
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Command completed without reported issues.
  target_ids:
  - CommunityMech:000307
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: "Validating kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000307
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history; cache-name check is read-only corpus preflight.
    No ontology skips; all inspected cache bytes unchanged.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records,
    57 warnings in 21 records, zero errors; exit 1. Selected target has no reported
    network warning. Canonical records are unchanged since this run.'
  target_ids:
  - CommunityMech:000307
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Corpus-wide warning result, not a scientific pass. Native broad scope
    gives credit to the sole declared taxon despite its feedstock status.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records,
    57 warnings in 21 records, zero errors; exit 1. Selected target has no reported
    network warning. Canonical records are unchanged since this run.'
  target_ids:
  - CommunityMech:000307
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Corpus-wide warning result, not a scientific pass. Native broad scope
    gives credit to the sole declared taxon despite its feedstock status.
- check_id: structured-expression-adapter
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: No named regulatory gene, locus, transcriptomic module or strain expression
    dataset is curated. The cited amplicon project was checked through its public
    metadata; no expression-module claim is made.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - dataset
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  locator: Entire target, including five nodes and both downstream arrows
  summary: The record explicitly describes Anabaena as substrate, yet taxonomy contains
    only that organism with a producer role. Broad community-level nodes consequently
    inherit an inappropriate sole declared participant.
  support: supports
  accessed_at: '2026-10-20T07:18:59.039338Z'
- evidence_id: primary
  kind: primary_source
  reference: PMID:40089033
  locator: https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars;
    author-uploaded article header, Methods 2.1/2.3/2.4.4–2.4.6, Results 3.2.1–3.2.4
    and Outlook/Conclusions
  summary: Public primary text was independently inspected. The study compares separate
    inocula across matrices; it is not one defined consortium. The source supplies
    composition and methodological context beyond the retained abstract.
  support: supports
  accessed_at: '2026-10-20T07:16:15.418113Z'
- evidence_id: feedstock
  kind: primary_source
  reference: PMID:40089033
  locator: https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars;
    Methods 2.1 and 2.3; browser lines 338–412 and 540–749
  summary: The named cyanobacterium supplies biomass; the digesting inocula are distinct.
    The main text gives a strain designation omitted from the abstract-only rationale.
  support: supports
  accessed_at: '2026-10-20T07:16:15.418113Z'
  quote: Anabaena sp. PCC 7938
- evidence_id: guild
  kind: primary_source
  reference: PMID:40089033
  locator: https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars;
    Abstract and Results 3.2.4; lines 1499–1747
  summary: The guild relationship is inferred from taxonomic profiles, not partner-resolved
    transfer measurements.
  support: supports
  accessed_at: '2026-10-20T07:16:15.418113Z'
  quote: taxonomic analysis revealed
- evidence_id: output
  kind: primary_source
  reference: PMID:40089033
  locator: https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars;
    Abstract; Results 3.2.1–3.2.2
  summary: Nutrient and carbon endpoints support an observed processing outcome, without
    identifying the responsible partner pair.
  support: supports
  accessed_at: '2026-10-20T07:16:15.418113Z'
  quote: All communities produced ammonium
- evidence_id: matrix
  kind: primary_source
  reference: PMID:40089033
  locator: https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars;
    Abstract; Results 3.2.2–3.2.3
  summary: The nutrient-recovery observation does not isolate microbial competition
    as its cause.
  support: supports
  accessed_at: '2026-10-20T07:16:15.418113Z'
  quote: reduced the phosphate and ammonium recovery efficiency
- evidence_id: cod
  kind: primary_source
  reference: PMID:40089033
  locator: https://www.researchgate.net/publication/389834004_Anaerobic_digestion_of_cyanobacterial_biomass_for_plant_fertilizer_production_on_mars;
    Methods 2.3.3 and Results 3.2.1; lines 734–742 and 1129–1137
  summary: The matrix constrains which carbon measurement can be claimed.
  support: supports
  accessed_at: '2026-10-20T07:16:15.418113Z'
  quote: simulant interfered with the analysis
- evidence_id: publication
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=40089033&retmode=xml
  locator: PubMed title, DOI and complete abstract
  summary: The DOI and PMID identify the same paper. All 18 target snippets match
    its retrieved abstract after NFKC/whitespace normalization; this is lexical verification,
    not proof of every explanation.
  support: supports
  accessed_at: '2026-10-20T07:15:24.417028Z'
  snapshot_sha256: f2154bd0c65b7dfcedb84dde3e507e8ca7181c2c45b5c144051afbdea67d0793
- evidence_id: dataset
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=bioproject&id=1219353&retmode=json
  locator: BioProject PRJNA1219353 metadata
  summary: The accession cited in Methods 2.4.5 resolves to BioProduction on Mars
    at Bremen. Its project description is broader than this article; project identity
    was verified, but individual sample assignments were not reanalyzed.
  support: supports
  accessed_at: '2026-10-20T07:15:24.417435Z'
  snapshot_sha256: 3f729a756111ffebf61dcae795b8a91e2ba1acb299cfacdf0ec64eea76a4be9b
- evidence_id: ontology
  kind: authority
  reference: OAK local NCBITaxon, ENVO, GO and CHEBI snapshots
  locator: 11 unique curated identifiers
  summary: All ID/label pairs resolve. This does not make feedstock a community member
    or prove pathway activity. Existing GTDB ambiguity is preserved; no new strain
    mapping is proposed.
  support: supports
  accessed_at: '2026-10-20T07:15:41.861660Z'
  snapshot_sha256: 507213257b9dc99891c430603ed6b9e05774fdb67dc8946f588bdaea0a8fab2c
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml; src/communitymech/network/auditor.py
  locator: TaxonomicComposition and broad community-level participation semantics
  summary: Taxonomy denotes organisms present in the community. A broad community-level
    interaction credits declared taxa structurally; a prose exclusion does not remove
    a feedstock entry from that participant set.
  support: supports
  accessed_at: '2026-10-20T07:18:59.039755Z'
- evidence_id: history
  kind: record_content
  reference: history/records/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium
  locator: Whole history event and target row in reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
  summary: Historical graph curation qualified guild claims and retained two arrows.
    It recorded public source availability while excluding non-graph metadata from
    certification; old abstract-only/paywall statements remain elsewhere.
  support: supports
  accessed_at: '2026-10-20T07:18:59.039757Z'
- evidence_id: local-search
  kind: search
  reference: references_cache; history/records; reports/causal_graph_review/decisions;
    kb/taxa
  locator: Ignored-inclusive PMID, accession and slug search
  summary: The retained source is an abstract-only Markdown cache, not a missing TXT
    article. Missing dataset, participant and linkage observations concern the full
    target. External registries were not exhaustively searched for media equivalence.
  support: supports
  accessed_at: '2026-10-20T07:18:59.039955Z'
  search_scope: rg --no-ignore --hidden -l '40089033|1219353|Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium'
    references_cache history/records reports/causal_graph_review/decisions kb/taxa
  snapshot_sha256: cffbfceda34954743200ac773d4c992a993ecdf44c8d1f7d946c33d500b186c8
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  locator: All 18 attached snippets versus current PubMed abstract
  summary: All normalize to exact abstract substrings. The small excerpts do not support
    detailed explanations merely because they match; current full-text context was
    independently checked where material.
  support: supports
  accessed_at: '2026-10-20T07:18:59.040034Z'
  snapshot_sha256: 5913f311304fff278ecfc46bf84b878a790c8b09ee8413181cc87453d80a38e4
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  locator: Actual execution 2026-10-20T07:13:34.927873+00:00 to 2026-10-20T07:13:36.219589+00:00
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml'
  support: supports
  accessed_at: '2026-10-20T07:13:36.219589Z'
  snapshot_sha256: 610a54cd406cd07eb078f81422d66c072c8db5fce7857af004dea68e9bc265c0
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-strict kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv
  locator: Actual execution 2026-10-20T07:13:34.928585+00:00 to 2026-10-20T07:13:38.494027+00:00
  summary: "uv run python scripts/validate_strict.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml\
    \ --out /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv\nValidating\
    \ 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-batch-03/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/batch-03/000307/strict-report.tsv"
  support: supports
  accessed_at: '2026-10-20T07:13:38.494027Z'
  snapshot_sha256: 97c3398926423ddc48d1cd16894d3f9f0650315488c0eabd0a726e24fc20c124
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-terms kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  locator: Actual execution 2026-10-20T07:13:34.936443+00:00 to 2026-10-20T07:13:37.596811+00:00
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-10-20T07:13:37.596811Z'
  snapshot_sha256: 6c07bc722f1d2206ead163385a9b9e91cd1a094d158aa8a67c489608c7f0c256
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  locator: Actual execution 2026-10-20T07:13:36.219994+00:00 to 2026-10-20T07:13:36.364384+00:00
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-10-20T07:13:36.364384Z'
  snapshot_sha256: c350416cc8b5b0cfe34570d1b1cda65363d060cd16174d1cbed6e9ecfeae1c6c
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-gtdb-domain kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  locator: Actual execution 2026-10-20T07:13:36.364745+00:00 to 2026-10-20T07:13:39.172949+00:00
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml'
  support: supports
  accessed_at: '2026-10-20T07:13:39.172949Z'
  snapshot_sha256: bac3341cbfe925c70fd76e4eaf21eb04e29af36df81abc9a6c5f216dcc768c92
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-history history/records/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium
  locator: Actual execution 2026-10-20T07:13:37.597509+00:00 to 2026-10-20T07:13:38.993644+00:00
  summary: No issues found
  support: supports
  accessed_at: '2026-10-20T07:13:38.993644Z'
  snapshot_sha256: 38ce2a6caedfe171429fa640845c4c3304dfaae7a5d24958cd9d7e7f02715e04
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-20T07:13:39.173565+00:00 to 2026-10-20T07:13:39.239610+00:00
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-10-20T07:13:39.239610Z'
  snapshot_sha256: 7e620395ed7ec21ec1d45e977a02d65e525e33cec5a98737ac5b5fc1bbde2baa
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv validate-references-explained kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
  locator: Actual execution 2026-10-20T07:13:39.239885+00:00 to 2026-10-20T07:13:40.770884+00:00
  summary: "Validating kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-10-20T07:13:40.770884Z'
  snapshot_sha256: aa1243f3818757da25dd1a3e2b10bf23da55bda9ee45ed4e67ec3b9027545659
- evidence_id: check-audit-network
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv audit-network
  locator: Actual run finished 2026-10-20T07:08:14.467705+00:00
  summary: 'Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records,
    57 warnings in 21 records, zero errors; exit 1. Selected target has no reported
    network warning. Canonical records are unchanged since this run.'
  support: supports
  accessed_at: '2026-10-20T07:08:14.467705Z'
  snapshot_sha256: e2122e512641be2226ad12ab146b2c8f7d1e153f1211745e4816457834a42667
- evidence_id: check-check-network-quality
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-03/src
    just --no-dotenv check-network-quality
  locator: Actual run finished 2026-10-20T07:08:13.673449+00:00
  summary: 'Actual fresh-base corpus run with this worktree PYTHONPATH: 477 records,
    57 warnings in 21 records, zero errors; exit 1. Selected target has no reported
    network warning. Canonical records are unchanged since this run.'
  support: supports
  accessed_at: '2026-10-20T07:08:13.673449Z'
  snapshot_sha256: b0cb58371a5a771dcbd671952ee68dfe5f26169d08240b66162aa83580fb5229
assessments:
- assessment_id: identity
  area: identity
  topic: Feedstock versus digesting community; experimental strata
  outcome: concern
  summary: The record identifies the intended study, but its machine-readable membership
    contradicts its own feedstock exclusion. Three inocula and their matrix-specific
    outcomes must remain distinguishable during later curation.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - primary
  - feedstock
  - schema
  dimensions:
  - name: source_strain
    value: Anabaena biomass source; digesting inocula are separate
    definition: Feedstock identity is not evidence of living community membership.
    evidence_ids:
    - record
    - feedstock
  - name: community_scope
    value: Three distinct digestion inocula across comparative matrices
    definition: Do not pool source profiles into one experimentally observed consortium.
    evidence_ids:
    - primary
    - record
  - name: experimental_setting
    value: Controlled laboratory comparison motivated by Mars resource use
    definition: Applied extraterrestrial context is distinct from a sampled Martian
      ecosystem.
    evidence_ids:
    - primary
    - ontology
  - name: medium
    value: Alternative assay matrices, not one interchangeable formulation
    definition: The record must keep substrate-production and digestion contexts separate.
    evidence_ids:
    - feedstock
    - record
  - name: evidence_tier
    value: Measured endpoints versus inferred guild links
    definition: Taxonomy and carbon/nutrient measurements have different causal resolution.
    evidence_ids:
    - guild
    - output
    - matrix
    - cod
- assessment_id: taxonomy
  area: grounding
  topic: taxonomy[0] and implicit graph participants
  outcome: concern
  summary: The Anabaena ID/label is valid but is placed in the wrong semantic role.
    Actual digesting-community membership is unrepresented. The source offers composition
    at varying ranks; these should not be promoted to a single pooled species list.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - ontology
  - primary
  - feedstock
  - schema
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Anabaena Biomass Anaerobic Digestion'
  outcome: concern
  summary: The process description and endpoint separation are supported. Participant
    representation is defective because broad scope currently resolves to the feedstock
    organism alone.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - feedstock
  - output
  - schema
  details: 'Participants: separate digestion communities acting on supplied biomass,
    not Anabaena as a live consortium member. Direction: substrate processing toward
    nutrient/carbon outcomes. Source PMID 40089033 Methods 2.3 and Results 3.2; exact
    excerpts/locators in feedstock and output.'
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Fermenter-to-methanogen syntrophy'
  outcome: concern
  summary: The HYPOTHESIZED wording appropriately limits the causal claim. It needs
    corrected community membership, not stronger certainty or an inferred pair of
    species.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - guild
  - schema
  details: 'Participants: candidate fermentative and methanogenic guilds in the minimal-medium
    branch; named partners are not resolved by this review. Direction: proposed donor-to-recipient
    exchange, without partner-resolved flux. Source locator and exact excerpt: guild,
    PMID 40089033 Results 3.2.4. Do not generalize across all matrices.'
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Candidate Sulfate-Reducer Competition in MGS-1
    Regolith'
  outcome: concern
  summary: The node correctly retains competition as a hypothesis and distinguishes
    unsuccessful marker amplification from a measured zero product flux. The same
    participant defect applies.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - guild
  - primary
  - schema
  details: 'Participants: proposed competing guilds, not the cyanobacterial substrate.
    Direction: candidate antagonistic influence, with alternative matrix effects retained.
    Source PMID 40089033 Results 3.2.4, guild locator/quote. This assessment does
    not establish exclusion through a single isolated causal mechanism.'
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Ammonium Production and Organic Carbon Removal'
  outcome: concern
  summary: The outcome node preserves the distinction between soluble and unmeasured
    total-carbon results. Its community scope remains incorrectly linked to the sole
    feedstock taxon.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - output
  - cod
  - schema
  details: 'Participants: digesting communities; direction: processing to measured
    nutrient/carbon outcomes. Exact source locators and excerpts: output and cod,
    PMID 40089033 Results 3.2.1–3.2.2. No specific microbial mediator is established.'
- assessment_id: node-4
  area: graph
  topic: 'ecological_interactions[4]: MGS-1 Nutrient Recovery Penalty'
  outcome: concern
  summary: The PARTIAL description appropriately avoids attributing the recovery penalty
    solely to competition. It shares the participant defect and omits structured phosphate
    representation despite mentioning it in prose.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - matrix
  - schema
  details: 'Participants/context: comparative community assays in the regolith matrix.
    Direction: matrix-associated change in recovered nutrients, not an established
    microbial donor-recipient edge. Source PMID 40089033 Results 3.2.2–3.2.3, exact
    excerpt in matrix.'
- assessment_id: edge-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: supported
  summary: The retained digestion-to-syntrophy arrow is expressly hypothetical and
    context-limited. It must not be treated as measured transfer or as a process performed
    by Anabaena.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - feedstock
  - guild
  - history
  details: 'Source node: biomass digestion. Target node: candidate fermenter/methanogen
    relationship. Direction and mechanism are tentative; participant correction is
    handled in the membership finding. Source PMID 40089033 Results 3.2.4; quote/locator
    in guild.'
- assessment_id: edge-1
  area: graph
  topic: ecological_interactions[0].downstream[1]
  outcome: supported
  summary: The digestion-to-outcome arrow is a process/result relation with the total-COD
    limitation retained. It does not isolate a taxon-specific causal contribution.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - output
  - cod
  - history
  details: 'Source node: digestion; target node: ammonium/carbon endpoints. Direction:
    experimental process to reported outcomes. Exact source excerpts and locators
    in output/cod, PMID 40089033 Results 3.2.1–3.2.2. Other historical arrows remain
    removed.'
- assessment_id: certainty
  area: evidence
  topic: description, environmental_factors[0] and related_ingredients[1]
  outcome: concern
  summary: The graph preserves uncertainty, but summary and ingredient wording present
    inferred exchange, exclusion and methane output more definitively. Cross-field
    certainty should not depend on which part of the record a consumer reads.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - guild
  - primary
  - history
- assessment_id: environment
  area: grounding
  topic: Environment terms, engineering context and metal relevance
  outcome: supported
  summary: The ontology labels fit laboratory/digester context. Mineral constituents
    do not by themselves establish a metal-extraction ecological role, so NOT_APPLICABLE
    is not contradicted by the matrix’s mineral content. The record is an experimental
    comparison rather than a natural community.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - ontology
  - primary
- assessment_id: media
  area: provenance
  topic: growth_media[0] and source-access statements
  outcome: concern
  summary: The medium entry acknowledges alternative matrices, but its paywall rationale
    is stale. Public source access supports revisiting missing provenance and conditions
    while preserving assay distinctions; the supplement was not inspected and no complete
    formulation is certified.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - primary
  - history
  - local-search
- assessment_id: resources
  area: provenance
  topic: Publication, BioProject, snippets and history
  outcome: concern
  summary: Publication identity and all abstract snippets verify. The paper’s declared
    BioProject is missing from associated_datasets despite a resolvable project record.
    Sample-specific identity and raw-data quality were not reanalyzed.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - publication
  - dataset
  - snippets
  - history
- assessment_id: validation
  area: schema
  topic: Focused checks and native network completeness
  outcome: concern
  summary: All eight focused/preflight gates pass and cache bytes remain unchanged.
    Native network integrity is COMPLETE for the encoded taxon set, but broad scope
    gives credit to a substrate organism. That is why scientific membership review
    is needed despite green structural gates.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - schema
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-references-explained
  - check-audit-network
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: concern
  summary: Completeness 85 and capped validation quality 100 are presence/integrity
    calculations; they do not resolve the feedstock-member contradiction or overconfident
    claims.
  target_ids:
  - CommunityMech:000307
  evidence_ids:
  - record
  - schema
  - check-audit-network
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata including roles +5 environment +10 at
      least 3 factors +10 at least 3 nodes +5 external resources +10 media +5 datasets
      +5 node metabolites). 50+5+0+10+5+10+0+5=85; two factors, five nodes, no associated
      dataset. Required-block credit reflects populated fields, not valid ecological
      membership.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50*P1-10*P2-2*P3+20*min(mean node evidence/2,1)+15 if native
      COMPLETE,0,100). P1=0,P2=2,P3=4,P4=1; 7 attached items/5 nodes; broad scope
      credits the sole declared taxon. clamp(100-20-8+14+15)=100.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native target severity count.
  - name: P2
    value: 2
    unit: findings
    definition: Observed native target severity count.
  - name: P3
    value: 4
    unit: findings
    definition: Observed native target severity count.
  - name: P4
    value: 1
    unit: findings
    definition: Observed native target severity count.
  - name: interaction_evidence
    value: 1.4
    unit: evidence items per interaction
    denominator: 5
    definition: Seven attached items across five nodes from one publication, not independent
      replication.
findings:
- finding_id: feedstock-membership
  issue_key: cm-000307-feedstock-membership
  category: representation
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: TaxonomicComposition.community-membership
  status: open
  certainty: confirmed
  title: Feedstock is the sole declared community member
  description: The target explicitly says Anabaena is not a live member but lists
    it as the only taxon with a producer role. Broad community-level nodes therefore
    inherit this substrate organism as their only structured participant, while the
    digesting communities are absent.
  target_ids:
  - CommunityMech:000307
  field_paths:
  - taxonomy[0]
  - ecological_interactions[*].participating_taxa
  evidence_ids:
  - record
  - feedstock
  - schema
  - primary
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
- finding_id: cross-field-certainty
  issue_key: cm-000307-cross-field-certainty
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: CLAUDE.claim-level-evidence
  status: open
  certainty: confirmed
  title: Non-graph fields overstate inferred processes
  description: The description and methane ingredient describe exchange, exclusion
    or product formation more definitively than the graph’s hypothetical/partial wording.
    Taxonomic guild inference and unsuccessful amplification do not establish partner
    flux or a measured gas-production endpoint.
  target_ids:
  - CommunityMech:000307
  field_paths:
  - description
  - environmental_factors[0].description
  - related_ingredients[1].relevance
  - related_ingredients[1].evidence[0]
  evidence_ids:
  - record
  - guild
  - primary
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
- finding_id: stale-source-access
  issue_key: cm-000307-stale-source-access
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded provenance or representation gap; the study
    identity and observed outcomes remain recognizable.'
  rule_id: CLAUDE.claim-level-evidence
  status: open
  certainty: confirmed
  title: Paywall and abstract-only rationales are stale
  description: Several fields say source details cannot be represented because full
    text is paywalled. The public author copy is accessible and was already noted
    in the historical graph decision; its Methods name the biomass strain and assay
    context.
  target_ids:
  - CommunityMech:000307
  field_paths:
  - description
  - taxonomy[0].taxon_term.notes
  - growth_media[0].preparation_notes
  evidence_ids:
  - record
  - primary
  - feedstock
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
- finding_id: dataset-linkage
  issue_key: cm-000307-dataset-linkage
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded provenance or representation gap; the study
    identity and observed outcomes remain recognizable.'
  rule_id: review-checklist.external-resources
  status: open
  certainty: confirmed
  title: Declared sequencing project is not represented
  description: associated_datasets is empty although Methods 2.4.5 cites PRJNA1219353.
    Public metadata resolves it as a broader Bremen Mars-bioproduction project; paper-specific
    sample membership has not been checked.
  target_ids:
  - CommunityMech:000307
  field_paths:
  - associated_datasets
  evidence_ids:
  - record
  - primary
  - dataset
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
- finding_id: output-as-factor
  issue_key: cm-000307-output-as-factor
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded provenance or representation gap; the study
    identity and observed outcomes remain recognizable.'
  rule_id: review-checklist.environment
  status: open
  certainty: confirmed
  title: A process output is stored as an environmental factor
  description: The second environmental_factors entry describes nutrient/carbon outcomes
    already represented by an outcome node. Its label and value describe a result,
    not an independently supplied condition.
  target_ids:
  - CommunityMech:000307
  field_paths:
  - environmental_factors[1]
  evidence_ids:
  - record
  - output
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
- finding_id: media-linkage
  issue_key: cm-000307-media-linkage
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded provenance or representation gap; the study
    identity and observed outcomes remain recognizable.'
  rule_id: P3.1
  status: open
  certainty: confirmed
  title: Alternative assay matrices lack verified resource links
  description: The combined media entry has no CultureMech/MediaIngredientMech linkage.
    A single generic label cannot establish exact equivalence of the alternatives.
  target_ids:
  - CommunityMech:000307
  field_paths:
  - growth_media[0]
  evidence_ids:
  - record
  - primary
  - local-search
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
- finding_id: phosphate-representation
  issue_key: cm-000307-phosphate-representation
  category: completeness
  severity: informational
  native_severity: P4
  normalization_reason: 'P4 informational: the nutrient is retained in prose but lacks
    a structured chemical entry; this is enrichment, not proof of a missing causal
    mechanism.'
  rule_id: P4.2
  status: open
  certainty: confirmed
  title: Phosphate is prose-only in the recovery node
  description: The recovery node mentions phosphate but has only ammonium in its metabolite
    list. Future chemical grounding should preserve the measured entity and the distinction
    between dissolved nutrient recovery and total phosphorus.
  target_ids:
  - CommunityMech:000307
  field_paths:
  - ecological_interactions[4].metabolites
  evidence_ids:
  - record
  - matrix
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
actions:
- action_id: fix-feedstock-membership
  description: Represent feedstock separately from living community membership and
    preserve inoculum/matrix-specific identities at source-supported ranks.
  finding_ids:
  - feedstock-membership
  target_ids:
  - CommunityMech:000307
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - A substrate-only organism is not credited as a live participant in digestion interactions.
  - Distinct experimental communities are not merged into one asserted member list.
  - Unknown participants remain explicit rather than replaced by invented species.
  - Run strict, term and network checks.
- action_id: fix-cross-field-certainty
  description: Carry the graph’s evidence limits consistently into summaries, factors
    and ingredient relevance statements.
  finding_ids:
  - cross-field-certainty
  target_ids:
  - CommunityMech:000307
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Observed endpoints are separated from inferred microbial processes.
  - No gas-production measurement is implied solely by identifying a methanogenic
    guild.
  - No zero-flux claim is inferred from marker-amplification failure.
  - Run reference and strict checks.
- action_id: fix-stale-source-access
  description: Update source-access provenance and distinguish actually inspected
    primary passages from uninspected supplementary material.
  finding_ids:
  - stale-source-access
  target_ids:
  - CommunityMech:000307
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - No categorical paywall assertion remains when a verified public author copy is
    available.
  - Source strain naming remains attached to feedstock, not living digesting members.
  - Do not claim complete supplement/formulation verification.
- action_id: fix-dataset-linkage
  description: Add source-declared project provenance during curation, making the
    broader project scope and any unresolved sample mapping explicit.
  finding_ids:
  - dataset-linkage
  target_ids:
  - CommunityMech:000307
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - The accession resolves and is traceable to the cited paper.
  - Do not claim every project sample belongs to this experiment.
  - No raw sequence reanalysis is implied.
  - Run strict/resource checks.
- action_id: fix-output-as-factor
  description: Keep the outcome at its relevant result assertion instead of duplicating
    it as an environmental condition.
  finding_ids:
  - output-as-factor
  target_ids:
  - CommunityMech:000307
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Conditions and measured outcomes remain distinguishable.
  - The source-supported outcome and evidence are preserved.
  - Run strict and reference checks.
- action_id: fix-media-linkage
  description: Assess exact formulation/resource matches separately when authorized
    curation revisits this field; retain unresolved matches explicitly.
  finding_ids:
  - media-linkage
  target_ids:
  - CommunityMech:000307
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anabaena_MGS1_Anaerobic_Digestion_Methanogen_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - No link is inferred solely from a similar medium name.
  - Alternative matrices remain distinct.
  - Run applicable linkage and strict checks.
limitations:
- The author-uploaded primary text was inspected; separate supplements, PDF figure
  geometry and raw sequencing/statistical results were not reanalyzed.
- The BioProject is broader than the paper; individual sample-to-experiment mapping
  remains unverified.
- The source mostly names PCC 7938 but one medium-preparation sentence transposes
  it to PCC 7398. No new strain ontology mapping is proposed; preserve this source
  inconsistency when reconciling feedstock identity.
- Community composition varies by inoculum and matrix and is often reported above
  species rank. Do not construct a single pooled species list or infer partner-resolved
  flux.
- GTDB candidates remain explicitly ambiguous; passing coherence/domain gates does
  not resolve a strain mapping.
- All focused checks pass. Required corpus network checks retain their actual warning
  exits despite no target diagnostic.
notes:
- No canonical records, caches, history or generated products changed.
- The initial inspect attempt used a nonexistent TXT suffix and was corrected to the
  existing Markdown cache after an ignored-inclusive search, before assessment. Successful
  inspect hashes are the provenance for this review.
- All local input hashes remain unchanged. Browser source-inspection locators and
  public metadata response hashes are retained.
- Verbatim quotations total 23 words from the paper.
tags:
- record-review
- anaerobic-digestion
- batch-03
```
