# Galveston Bacillus-Pseudomonas PET consortium: record review

- Review: 20261021T091534Z-galveston-pet-consortium-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T09:09:37.086879Z
- Finished UTC: 2026-10-21T09:15:34.725120Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Completed scientific review: the five-isolate identity and qualified one-node model are supported. Four minor findings address taxon-role evidence, medium/quotation precision, unsupported equilibrium state and BioSample terminology; verified more-specific Pseudomonas taxids are optional refinements. Native checks pass, and no causal arrows are required.

## Scope And Provenance

Entire record, all five taxa, one interaction and zero arrows assessed against the published main source, relevant supplements, archive metadata, actual schema and native/OAK checks. Source and inference scopes remain explicit.

Selection: Next assigned maintained path after CommunityMech:000483 in batch05; the source community is uniquely resolved.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c6e5a9b9af2d05e12eaafb2555a53f3a079268f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000370 | kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml | maintained | Bacillus-Pseudomonas Galveston PET Consortium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000370 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000370 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000370 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000370 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000370 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000370 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000370 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000370 | Target reference validation passed against the selected-passage cache. |
| audit-network | failed | True | CommunityMech:000370 | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-network-quality | failed | True | CommunityMech:000370 | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| Publication identifiers and source version | passed | True | CommunityMech:000370 | Fresh metadata and final published XML agree; no preprint evidence was substituted. |
| Whole main source and relevant supplementary evidence | passed | True | CommunityMech:000370 | Complete main text and relevant supplementary figures/tables support a completed scientific assessment. |
| Project and five BioSample identities | passed | True | CommunityMech:000370 | Project and all five sample identities resolve with explicit study-subset and assembly-accession boundaries. |
| Encoded medium/ingredient-Mech links | not_applicable | False | CommunityMech:000370 | No CultureMech or MediaIngredientMech ID is encoded; recipe equivalence was not inferred. |
| Optional structured source adapter | unavailable | False | CommunityMech:000370 | Same-runtime batch05 discovery is reused; no external runner or strain-module query was executed. |

## Scientific And Domain Assessments

### Five-isolate PET consortium and source scope

identity: supported. Targets: CommunityMech:000370.

The study and five-member roster resolve; operational grouping of 10/13.2 does not erase their separate identities.

### All five member identities, roles and abundance descriptions

grounding: concern. Targets: CommunityMech:000370.

Membership resolves, but local role evidence should distinguish observed activity from proposed cross-feeding.

Both Bacillus PRIMARY_DEGRADER roles are compatible with source hydrolytic evidence; their membership-only snippets should be supplemented. All three Pseudomonas CROSS_FEEDER roles need an explicit inference qualifier and role-specific source support. One-of-five wording describes membership, not measured abundance; no percentage-based defect is asserted.

### ecological_interactions[0]: Bacillus-Pseudomonas PET division of labor

graph: supported. Targets: CommunityMech:000370.

Retain the COMMUNITY_LEVEL, PARTIAL niche-specialization model and its explicit uncertainty.

Participants are the five-isolate consortium, with Bacillus/Pseudomonas activities overlapping and 10/13.2 unresolved analytically. The proposal places extracellular polymer processing before downstream intermediate handling, but no directed edge or member-resolved transfer is encoded. NICHE_PARTITIONING remains a proposed model: competition reduction is explicitly unmeasured. Full-consortium PET-associated transformation, MHET comparison limits, tentative MMHET identity and absence of matched monoculture proteomes are accurately distinguished. Zero arrows require no invented connectivity.

### Media, environmental factors and cultivation context

completeness: concern. Targets: CommunityMech:000370.

Most conditions are source-supported; clarify carbon terminology and recover the bounded trace-stock recipe.

PET 1%, MHET 0.2% and final OD600 0.01 match Methods. The PET and MHET entries retain distinct durations/modes. Do not assign seed-culture temperature to substrate assays; the source does not provide a separate PET/MHET temperature in the inspected cultivation passage. Trace-metal nutrient salts do not establish metal-processing activity; NOT_APPLICABLE for processing is reasonable.

### Natural origin versus ecological equilibrium

identity: concern. Targets: CommunityMech:000370.

NATURAL origin is supported, while unqualified STABLE exceeds the inspected equilibrium evidence.

Co-isolation, continued survival and source discussion of ecological adaptation are not measurements of equilibrium composition. Do not substitute another state solely from laboratory assembly or incubation duration.

### Dataset, sample identifiers and chemical scope

completeness: concern. Targets: CommunityMech:000370.

Project/sample links verify; sample identifiers should not be described as genome assembly accessions.

The source supports hybrid sequencing, while archive metadata verifies identities rather than sequencing quality or completeness. The project publication is the earlier PMID 31221643; the current article independently links the project. Five denotes this study subset. PET and TPA are correctly grounded; tentative MMHET should not become a confirmed exchanged metabolite. No extra dataset accession follows from the generic data-within-article statement.

### Final publication, cache boundary and historical review

evidence: supported. Targets: CommunityMech:000370.

Fresh main text resolves the selected cache boundary; existing qualified graph repairs remain supported.

The cache sentinel overstates coverage but the prior decision already disclosed selected excerpts. Three SupportingReference full_text values are schema-valid. One degree-symbol omission needs exact quotation repair; it does not undermine the LB condition. Published evidence is kept separate from the discovered, unused preprint.

### Native gates and semantic review

schema: supported. Targets: CommunityMech:000370.

Seven focused native checks and cache preflight pass; target network integrity is complete.

Corpus warnings retain actual failing exit codes and are not assigned to this target. Reference-cache success does not independently establish fresh quote fidelity or biological interpretation.

### Native completeness and validation quality

completeness: supported. Targets: CommunityMech:000370.

Completeness is 90 and capped quality 100; four minor findings remain despite the high diagnostic score.

## Findings

### role-evidence-scope: Qualify taxon roles with claim-level source evidence

minor / open / confirmed; issue key: cm-000370-role-evidence-scope.

Taxon-local snippets identify membership and BioSamples, not functions. The three CROSS_FEEDER assignments present the proposed handoff without the graph's inference limits; published chemistry and protein associations do not establish member-resolved uptake of another member's products.

### medium-and-quotation: Clarify LCFBM composition and restore source-exact cultivation evidence

minor / open / confirmed; issue key: cm-000370-medium-and-quotation.

The description calls the medium carbon-free although the encoded and published formulation contains yeast extract. The trace stock remains unspecified locally despite a recoverable recipe, and the LB quote drops the degree symbol. These are bounded wording/completeness issues, not evidence that PET transformation was absent.

### equilibrium-state: Qualify the unsupported equilibrium state

minor / open / confirmed; issue key: cm-000370-equilibrium-state.

STABLE asserts equilibrium, but co-enrichment, bounded growth and inferred ecological persistence do not establish equilibrium composition in the reviewed source.

### sample-accession-scope: Distinguish BioSample identifiers from genome assembly accessions

minor / open / confirmed; issue key: cm-000370-sample-accession-scope.

Three taxon notes call their BioSamples strain-level genome accessions. The verified identifiers describe biological samples; no assembly identity was verified from those notes. More specific current NCBI strain placeholders are available as optional refinements.

## Recommended Actions And Acceptance Checks

### repair-role-evidence-scope

Qualify taxon roles with claim-level source evidence.

- Attach role-specific primary evidence to both Bacillus degradation roles; retain incomplete-transformation scope.
- Qualify Pseudomonas cross-feeding as the source-proposed model with PARTIAL evidence or remove an unqualified role if the representation cannot retain that uncertainty.
- Do not infer transferred carbon from externally supplied MHET consumption, protein presence, or the conceptual Fig. 9 alone.
- Preserve the current PARTIAL community node, zero arrows, overlapping functions and unresolved 10/13.2 contributions.

### repair-medium-and-quotation

Clarify LCFBM composition and restore source-exact cultivation evidence.

- Describe LCFBM as the source-named medium containing 0.05% wt/vol yeast extract; avoid implying literal carbon absence or demonstrated sole-carbon growth.
- Document the stock separately from its 1% vol/vol addition: FeSO4·7H2O and MgSO4·7H2O each 0.1% wt/vol; CuSO4·5H2O, MnSO4·5H2O and ZnSO4·7H2O each 0.01% wt/vol.
- Restore the primary-source degree symbol in the LB snippet and retain explicit historical cache provenance rather than silently claiming the cache was exact.
- Keep 37°C attached to overnight LB seed culture; retain separate static seven-week PET and aerobic 21-day MHET conditions.
- Resolve the MHET base by explicit reference to the same formulation without inventing a CultureMech recipe ID or substrate-assay temperature.

### repair-equilibrium-state

Qualify the unsupported equilibrium state.

- Supply direct source evidence of equilibrium if retaining STABLE; otherwise use a schema-supported uncertainty representation or explain the unresolved state.
- Preserve NATURAL origin and the laboratory assay context; do not automatically replace the state with TRANSIENT or ENGINEERED.

### repair-sample-accession-scope

Distinguish BioSample identifiers from genome assembly accessions.

- Call SAMN41232459, SAMN41232460 and SAMN41232462 BioSample accessions, and retain their verified source-strain/project mappings.
- If refining NCBI grounding, use verified canonical pairs 3144666 Pseudomonas sp. 9.2(2024), 3144667 Pseudomonas sp. 10(2024), and 3144665 Pseudomonas sp. 13.2 while preserving reported strain names and candidate provenance.
- Do not call current generic NCBITaxon:306 wrong, infer a new named biological species, or collapse separate samples 10 and 13.2.
- Keep sample_count 5 scoped to the reviewed set; do not claim it is the total project size or infer assembly completeness, GTDB placement or raw sequencing validation.

### validate-curation

After separately authorized corrections, rerun native checks and document the precise source-backed changes.

- Preserve the existing qualified interaction and zero-arrow graph while repairing non-graph claims.
- Use source-exact evidence and a new history event; rerun schema, strict, term, reference, history and network checks.
- Refresh historical source-access discussion to reflect inspected figures/supplement scope without claiming independent raw-data reproduction.
- Do not close broader issue 1256 solely because this target is corrected; its other records remain outside scope.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml; Entire target: five strains, one node and no arrows | supports | The record separates laboratory assays from original contaminated soil and retains a qualified proposed functional-partition model; non-graph fields need four bounded clarifications. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42627158&amp;retmode=xml; https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=42627158&amp;retmode=xml | supports | Article-level PubMed identifiers verify PMID 42627158, PMC13595931, DOI 10.1128/msystems.00829-26, title and abstract. |
| crossref | https://api.crossref.org/works/10.1128/msystems.00829-26; https://api.crossref.org/works/10.1128/msystems.00829-26 | supports | Crossref DOI and title metadata identify the published mSystems article. |
| epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42627158&amp;format=json&amp;resultType=core; https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42627158&amp;format=json&amp;resultType=core | supports | Europe PMC metadata identifies the same published article and supplies its full-text XML route. |
| fulltext | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13595931/fullTextXML; https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13595931/fullTextXML | supports | Fresh published XML contains the complete main article, tables, captions, data statement and supplement links. |
| membership | PMID:42627158; Materials and Methods, s2-1: Bacterial strains and bioinformatics | supports | Five named isolates and their BioSamples are explicit. Strains 10 and 13.2 are combined for comparative analysis because of source-reported near-complete genomic identity; both remain distinct deposited samples. |
| medium | PMID:42627158; Materials and Methods, s2-3: Bacterial growth and biodegradation assays | supports | LCFBM contains yeast extract. LB seed preparation, static seven-week PET growth and aerobic 21-day MHET assays are distinct contexts; the trace-element stock is explicitly formulated. |
| model | PMID:42627158; Results and Discussion, s3-3 and s3-5; Fig. 9 caption | supports | The source proposes overlapping hydrolysis and downstream-processing strengths; the schematic does not trace member-to-member substrate transfer or measure reduced competition. |
| chemistry | PMID:42627158; Results and Discussion, s3-4; Fig. 8 caption | supports | Full-consortium MHET depletion is not statistically distinguished from Pseudomonas treatments. Product peaks support transformation, not complete mineralization or balanced carbon flux. |
| proteomics | PMID:42627158; Results and Discussion, s3-3; Tables 3-4 and Figs. 6-7 | supports | PET-associated protein patterns support proposed functions; matched PET monoculture proteomes were not generated, so induction and selective member contributions are unestablished. |
| supplement | PMID:42627158; Published supplement S6: Figs. S3-S4 and Table S3; main s3-4/s3-5 | supports | Chromatography and mass assignment support a tentative methylated-MHET product. Detoxification or partner benefit was not directly tested. |
| supplement-retrieval | Published EPMC supplementary ZIP; root-supplementary-zip.json and root-supplement-manifest.json | context_only | The public ZIP supplies five annotation workbooks and the figures/tables DOCX; file retrieval is distinct from complete annotation reanalysis. |
| stability | PMID:42627158; Materials and Methods s2-3; Results and Discussion s3-5; supplement S6 | partial | Co-enrichment and bounded growth assays do not establish equilibrium of the five-member community; the inspected source supplies no compositional-equilibrium assessment. |
| hgt | PMID:42627158; Results and Discussion s3-1/s3-2/s3-5; Tables 1-2 | supports | HGT and genomic-island analyses remain predictions with unresolved transfer direction and PET specificity; the record already preserves these limits. |
| ontology | Local OAK NCBITaxon, ENVO, CHEBI and GO snapshots; Eight unique ID/label pairs across ten occurrences | supports | All current labels match; generic NCBITaxon:306 is species-ranked but does not uniquely identify the three named strains. PET, TPA and xenobiotic-process terms are compatible with the qualified phenotype. |
| schema | src/communitymech/schema/communitymech.yaml; EcologicalStateEnum.STABLE; FunctionalRoleEnum.PRIMARY_DEGRADER/CROSS_FEEDER; InteractionTypeEnum.NICHE_PARTITIONING | supports | STABLE denotes equilibrium. CROSS_FEEDER consumes other taxa's metabolites; complex-substrate degradation need not imply mineralization. Niche partitioning includes reduced competition, which this graph explicitly leaves unmeasured. |
| datasets | NCBI BioProject PRJNA517285 and BioSamples SAMN41232458-SAMN41232462; dataset-verification.json: project and five individual sample records | supports | All five sample-to-strain/project links verify. BioSamples identify samples, not assembly accessions; the project also lists older samples, so sample_count 5 is the reviewed study subset. |
| grounding-candidates | Local OAK plus verified NCBI BioSample mappings; pseudomonas-grounding-candidates.json | supports | Source strains 9.2, 10 and 13.2 map respectively to NCBITaxon:3144666, 3144667 and 3144665, with canonical labels and lineage under Pseudomonas verified; these are optional refinements, not proof current 306 is erroneous. |
| snippets | kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml; snippet-audit.json: all 27 evidence occurrences | supports | All snippets match the selected-passage cache; 26 match fresh XML exactly after NFKC/whitespace normalization, while the LB snippet omits the source degree symbol without changing its supported condition. |
| history | Three target sidecars; 20261005-eleven-records-batch6.yaml; Target decision lines 368-403; provenance-audit.json | supports | Prior hash matches and graph repairs remain. Fresh issues 872, 873 and 1255 are closed; issue 1256 remains open for non-graph source follow-up, including this medium wording. |
| search | Owned community, isolate and reusable-taxon roots; Ignored-inclusive bounded source/strain/taxon search | supports | No exact reusable identity was found in the named roots; shared generic taxa elsewhere cannot supply missing strain-level evidence. |
| adapter | Optional kg-microbe-sources runner; Same batch05 runtime discovery reused from 000120 at 08:47:38Z | supports | No callable owned-runtime adapter was available; no external runner or source/module query was executed. |
| native-target | NetworkIntegrityAuditor().audit_community(target); support-audit.json: target audit and native metric components | supports | Native network status is COMPLETE with no issues; four evidence items on one node give mean 4, without certifying measured cooperation. |
| independent-source | PMID:42627158; root-independent-source-audit.json: full main, key figure and supplement scope | supports | Independent review read complete main text, main Figs. 6-9 pixels and all S6 captions/tables/figures; workbook inspection was structural and selective, not omics reanalysis. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml; Actual execution 2026-10-21T09:09:47.832608+00:00 to 2026-10-21T09:09:49.056174+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-strict kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml --out /private/tmp/cm-review-session/batch-05/000370/strict-report.tsv; Actual execution 2026-10-21T09:09:47.833497+00:00 to 2026-10-21T09:09:59.853605+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-terms kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml; Actual execution 2026-10-21T09:09:47.833609+00:00 to 2026-10-21T09:09:50.786647+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-gtdb kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml; Actual execution 2026-10-21T09:09:49.059242+00:00 to 2026-10-21T09:09:49.226206+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml; Actual execution 2026-10-21T09:09:49.226630+00:00 to 2026-10-21T09:09:51.676640+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-history history/records/Bacillus_Pseudomonas_Galveston_PET_Consortium; Actual execution 2026-10-21T09:09:50.786983+00:00 to 2026-10-21T09:09:51.970613+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T09:09:59.854564+00:00 to 2026-10-21T09:09:59.957849+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src just --no-dotenv validate-references-explained kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml; Actual execution 2026-10-21T09:09:59.958111+00:00 to 2026-10-21T09:10:01.480859+00:00 | supports | Target reference validation passed against the selected-passage cache. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T08:44:47.720127+00:00 to 2026-10-21T08:45:04.195128+00:00 | supports | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T08:44:47.737345+00:00 to 2026-10-21T08:45:04.925187+00:00 | supports | Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |

## Limits And Additional Notes

- Final published XML is primary evidence. The discovered preprint was not used; publisher PDF access failed while EPMC main XML and relevant supplements were available.
- Complete main text, tables and captions were read; independent visual review covers main Figs. 6-9 and all S6 figures, not main Fig. 1-5 pixels. Five workbooks were inventoried and selectively inspected; no genome, proteome, HGT or chromatographic analysis was reproduced.
- Proposed inter-member handoff, ecological persistence and MMHET function remain interpretations; no equilibrium composition, member-resolved carbon transfer, complete mineralization or direct detoxification result is certified.
- Five BioSamples and their project link verify identity, not assembly completeness or sequencing quality. The project also lists older samples; current sample_count denotes the reviewed set. The source combined 10/13.2 analytically, without collapsing their distinct sample identities.
- Specific Pseudomonas taxids are archive-backed optional refinements; GTDB candidate lists were not recomputed, and proteomic reference matches do not reidentify the source strains.
- The committed cache contains selected excerpts despite its full-text sentinel; 26 of 27 snippets match fresh XML, with one degree-symbol omission. No cache, canonical record or historical artifact was changed.
- Same-runtime adapter discovery and fresh full-corpus network receipts are explicitly reused. The corpus failures are not target-specific graph defects.
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 9 words across the publication and its supplement.
- All 25 repository inputs were pinned before assessment and rechecked; quality 100 is capped from 127 and does not remove the four minor findings.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091534Z-galveston-pet-consortium-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Galveston Bacillus-Pseudomonas PET consortium: record review'
started_at: '2026-10-21T09:09:37.086879Z'
finished_at: '2026-10-21T09:15:34.725120Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Canonical inputs unchanged; separate agents assessed main sources
    and figures, ontology, native gates, snippets, history and archive metadata. No
    person-level independence beyond task roles is claimed.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Completed scientific review: the five-isolate identity and qualified one-node
  model are supported. Four minor findings address taxon-role evidence, medium/quotation
  precision, unsupported equilibrium state and BioSample terminology; verified more-specific
  Pseudomonas taxids are optional refinements. Native checks pass, and no causal arrows
  are required.'
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
  - path: history/records/Bacillus_Pseudomonas_Galveston_PET_Consortium/2026-09-14T001933Z-codex-4a2e06.yaml
    sha256: d5d4beb8758771f2234958a9e6ce43e3b85a7fb1d9532f4763e7a5fa0dedfa26
    role: context
  - path: history/records/Bacillus_Pseudomonas_Galveston_PET_Consortium/2026-09-14T002656Z-codex-d4e872.yaml
    sha256: 5b163b085855c4ad0d395d2166368fa02d8e4e4b15b41e0ae8acc362c289c528
    role: context
  - path: history/records/Bacillus_Pseudomonas_Galveston_PET_Consortium/2026-10-05T112951Z-codex-eb801f.yaml
    sha256: f46f238b26f90a19e40affb39eb7bd9d682dd9a3924f98cbdb1e1b0f38678ffd
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    sha256: 2ddcc9012e3cb0045be8bd35993136dbdf780557535f3d0db053980694d5d2d7
    role: target
  - path: references_cache/PMID_42627158.txt
    sha256: 5431289316c7fea4b95b7cd524d468e35db1b37c17b5b2096de8e0f426962734
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
- target_id: CommunityMech:000370
  path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
  label: Bacillus-Pseudomonas Galveston PET Consortium
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    role: canonical_record
scope:
  description: Entire record, all five taxa, one interaction and zero arrows assessed
    against the published main source, relevant supplements, archive metadata, actual
    schema and native/OAK checks. Source and inference scopes remain explicit.
  selection: Next assigned maintained path after CommunityMech:000483 in batch05;
    the source community is uniquely resolved.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000370
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000370
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
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
  - CommunityMech:000370
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-strict kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-05/000370/strict-report.tsv
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
  - CommunityMech:000370
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-terms kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
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
  - CommunityMech:000370
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
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
  - CommunityMech:000370
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
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
  - CommunityMech:000370
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-history history/records/Bacillus_Pseudomonas_Galveston_PET_Consortium
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
  - CommunityMech:000370
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
  summary: Target reference validation passed against the selected-passage cache.
  target_ids:
  - CommunityMech:000370
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-references-explained kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
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
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000370
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Reused fresh full-corpus batch05 execution, not a target-specific pass
    or scientific certification.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000370
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Reused fresh full-corpus batch05 execution, not a target-specific pass
    or scientific certification.
- check_id: publication-identity
  name: Publication identifiers and source version
  status: passed
  required: true
  summary: Fresh metadata and final published XML agree; no preprint evidence was
    substituted.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - fulltext
- check_id: full-primary-source
  name: Whole main source and relevant supplementary evidence
  status: passed
  required: true
  summary: Complete main text and relevant supplementary figures/tables support a
    completed scientific assessment.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - fulltext
  - supplement
  - independent-source
  scope_note: All main text/tables/captions assessed; main Figs. 6-9 and S6 figures
    independently viewed; no raw omics reanalysis or claim to have viewed main Fig.
    1-5 pixels.
- check_id: source-data
  name: Project and five BioSample identities
  status: passed
  required: true
  summary: Project and all five sample identities resolve with explicit study-subset
    and assembly-accession boundaries.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - datasets
  - grounding-candidates
- check_id: cross-mech
  name: Encoded medium/ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech ID is encoded; recipe equivalence
    was not inferred.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - record
  - medium
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Same-runtime batch05 discovery is reused; no external runner or strain-module
    query was executed.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
  locator: 'Entire target: five strains, one node and no arrows'
  summary: The record separates laboratory assays from original contaminated soil
    and retains a qualified proposed functional-partition model; non-graph fields
    need four bounded clarifications.
  support: supports
  accessed_at: '2026-10-21T09:15:34.701126Z'
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42627158&retmode=xml
  locator: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=42627158&retmode=xml
  summary: Article-level PubMed identifiers verify PMID 42627158, PMC13595931, DOI
    10.1128/msystems.00829-26, title and abstract.
  support: supports
  accessed_at: '2026-10-21T09:09:54.143107Z'
  snapshot_sha256: ad531bf0463794db08fb3d029fe14252b4f157527043f4d74251a1cbe4faae21
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1128/msystems.00829-26
  locator: https://api.crossref.org/works/10.1128/msystems.00829-26
  summary: Crossref DOI and title metadata identify the published mSystems article.
  support: supports
  accessed_at: '2026-10-21T09:09:54.120482Z'
  snapshot_sha256: 92860b2928c8209bde60fdfef334562627631b5aa4caccafce537c89a9c88119
- evidence_id: epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42627158&format=json&resultType=core
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42627158&format=json&resultType=core
  summary: Europe PMC metadata identifies the same published article and supplies
    its full-text XML route.
  support: supports
  accessed_at: '2026-10-21T09:09:54.688179Z'
  snapshot_sha256: aef24c470913a0976a9275612762ca83f3fb10e094d75044e0bc36ce977f3e71
- evidence_id: fulltext
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13595931/fullTextXML
  locator: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC13595931/fullTextXML
  summary: Fresh published XML contains the complete main article, tables, captions,
    data statement and supplement links.
  support: supports
  accessed_at: '2026-10-21T09:09:55.794050Z'
  snapshot_sha256: 6e1b0e7f4818e707a8cd38ab3af74e7b5e148bd16909065fd8862afbbbf2c1b9
- evidence_id: membership
  kind: primary_source
  reference: PMID:42627158
  locator: 'Materials and Methods, s2-1: Bacterial strains and bioinformatics'
  summary: Five named isolates and their BioSamples are explicit. Strains 10 and 13.2
    are combined for comparative analysis because of source-reported near-complete
    genomic identity; both remain distinct deposited samples.
  support: supports
  accessed_at: '2026-10-21T09:15:34.706129Z'
  snapshot_sha256: 6e1b0e7f4818e707a8cd38ab3af74e7b5e148bd16909065fd8862afbbbf2c1b9
- evidence_id: medium
  kind: primary_source
  reference: PMID:42627158
  locator: 'Materials and Methods, s2-3: Bacterial growth and biodegradation assays'
  summary: LCFBM contains yeast extract. LB seed preparation, static seven-week PET
    growth and aerobic 21-day MHET assays are distinct contexts; the trace-element
    stock is explicitly formulated.
  support: supports
  accessed_at: '2026-10-21T09:15:34.707140Z'
  quote: 0.05% (wt/vol) yeast extract
  snapshot_sha256: 6e1b0e7f4818e707a8cd38ab3af74e7b5e148bd16909065fd8862afbbbf2c1b9
- evidence_id: model
  kind: primary_source
  reference: PMID:42627158
  locator: Results and Discussion, s3-3 and s3-5; Fig. 9 caption
  summary: The source proposes overlapping hydrolysis and downstream-processing strengths;
    the schematic does not trace member-to-member substrate transfer or measure reduced
    competition.
  support: supports
  accessed_at: '2026-10-21T09:15:34.707297Z'
  quote: Proposed division of labor pathways
  snapshot_sha256: 6e1b0e7f4818e707a8cd38ab3af74e7b5e148bd16909065fd8862afbbbf2c1b9
- evidence_id: chemistry
  kind: primary_source
  reference: PMID:42627158
  locator: Results and Discussion, s3-4; Fig. 8 caption
  summary: Full-consortium MHET depletion is not statistically distinguished from
    Pseudomonas treatments. Product peaks support transformation, not complete mineralization
    or balanced carbon flux.
  support: supports
  accessed_at: '2026-10-21T09:15:34.707404Z'
  snapshot_sha256: 6e1b0e7f4818e707a8cd38ab3af74e7b5e148bd16909065fd8862afbbbf2c1b9
- evidence_id: proteomics
  kind: primary_source
  reference: PMID:42627158
  locator: Results and Discussion, s3-3; Tables 3-4 and Figs. 6-7
  summary: PET-associated protein patterns support proposed functions; matched PET
    monoculture proteomes were not generated, so induction and selective member contributions
    are unestablished.
  support: supports
  accessed_at: '2026-10-21T09:15:34.707530Z'
  snapshot_sha256: 6e1b0e7f4818e707a8cd38ab3af74e7b5e148bd16909065fd8862afbbbf2c1b9
- evidence_id: supplement
  kind: primary_source
  reference: PMID:42627158
  locator: 'Published supplement S6: Figs. S3-S4 and Table S3; main s3-4/s3-5'
  summary: Chromatography and mass assignment support a tentative methylated-MHET
    product. Detoxification or partner benefit was not directly tested.
  support: supports
  accessed_at: '2026-10-21T09:15:34.708226Z'
  snapshot_sha256: 7932685511c454579304048d4d50df4c1736699276f3a24855e0b6ad3c24cf00
- evidence_id: supplement-retrieval
  kind: validation
  reference: Published EPMC supplementary ZIP
  locator: root-supplementary-zip.json and root-supplement-manifest.json
  summary: The public ZIP supplies five annotation workbooks and the figures/tables
    DOCX; file retrieval is distinct from complete annotation reanalysis.
  support: context_only
  accessed_at: '2026-10-21T09:15:34.708623Z'
  snapshot_sha256: b853416579a89236e9d892be44a15bc7a44d9b90bc1f23b7c9962accffcf49c4
- evidence_id: stability
  kind: primary_source
  reference: PMID:42627158
  locator: Materials and Methods s2-3; Results and Discussion s3-5; supplement S6
  summary: Co-enrichment and bounded growth assays do not establish equilibrium of
    the five-member community; the inspected source supplies no compositional-equilibrium
    assessment.
  support: partial
  accessed_at: '2026-10-21T09:15:34.708761Z'
  snapshot_sha256: 6e1b0e7f4818e707a8cd38ab3af74e7b5e148bd16909065fd8862afbbbf2c1b9
- evidence_id: hgt
  kind: primary_source
  reference: PMID:42627158
  locator: Results and Discussion s3-1/s3-2/s3-5; Tables 1-2
  summary: HGT and genomic-island analyses remain predictions with unresolved transfer
    direction and PET specificity; the record already preserves these limits.
  support: supports
  accessed_at: '2026-10-21T09:15:34.709204Z'
  snapshot_sha256: 6e1b0e7f4818e707a8cd38ab3af74e7b5e148bd16909065fd8862afbbbf2c1b9
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, CHEBI and GO snapshots
  locator: Eight unique ID/label pairs across ten occurrences
  summary: All current labels match; generic NCBITaxon:306 is species-ranked but does
    not uniquely identify the three named strains. PET, TPA and xenobiotic-process
    terms are compatible with the qualified phenotype.
  support: supports
  accessed_at: '2026-10-21T09:15:34.709555Z'
  snapshot_sha256: ca55235e8fb58a62e162d26e04c5349d1f406008d12baf148e855a5c1902d141
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: EcologicalStateEnum.STABLE; FunctionalRoleEnum.PRIMARY_DEGRADER/CROSS_FEEDER;
    InteractionTypeEnum.NICHE_PARTITIONING
  summary: STABLE denotes equilibrium. CROSS_FEEDER consumes other taxa's metabolites;
    complex-substrate degradation need not imply mineralization. Niche partitioning
    includes reduced competition, which this graph explicitly leaves unmeasured.
  support: supports
  accessed_at: '2026-10-21T09:15:34.709560Z'
- evidence_id: datasets
  kind: database
  reference: NCBI BioProject PRJNA517285 and BioSamples SAMN41232458-SAMN41232462
  locator: 'dataset-verification.json: project and five individual sample records'
  summary: All five sample-to-strain/project links verify. BioSamples identify samples,
    not assembly accessions; the project also lists older samples, so sample_count
    5 is the reviewed study subset.
  support: supports
  accessed_at: '2026-10-21T09:15:34.709810Z'
  snapshot_sha256: 7ba0db4d668f013b3c426e8f4de5ad9962835a0ab0c81e7a32a28454c15dd429
- evidence_id: grounding-candidates
  kind: authority
  reference: Local OAK plus verified NCBI BioSample mappings
  locator: pseudomonas-grounding-candidates.json
  summary: Source strains 9.2, 10 and 13.2 map respectively to NCBITaxon:3144666,
    3144667 and 3144665, with canonical labels and lineage under Pseudomonas verified;
    these are optional refinements, not proof current 306 is erroneous.
  support: supports
  accessed_at: '2026-10-21T09:15:34.710754Z'
  snapshot_sha256: 7cb315d6802498d7557e21fd7f6db5f5e93d20cd8a1762bced9b7dd18e6cab9f
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
  locator: 'snippet-audit.json: all 27 evidence occurrences'
  summary: All snippets match the selected-passage cache; 26 match fresh XML exactly
    after NFKC/whitespace normalization, while the LB snippet omits the source degree
    symbol without changing its supported condition.
  support: supports
  accessed_at: '2026-10-21T09:15:34.711223Z'
  snapshot_sha256: a60caace5d4300dd3221deb74725fafdf7f9c384bcf55edc759efc1d4ca27f80
- evidence_id: history
  kind: record_content
  reference: Three target sidecars; 20261005-eleven-records-batch6.yaml
  locator: Target decision lines 368-403; provenance-audit.json
  summary: Prior hash matches and graph repairs remain. Fresh issues 872, 873 and
    1255 are closed; issue 1256 remains open for non-graph source follow-up, including
    this medium wording.
  support: supports
  accessed_at: '2026-10-21T09:15:34.711628Z'
  snapshot_sha256: 869d4b0cae8290be24cd5ed1d1e990e21a43e47d1633b2363aaa872565dfdf30
- evidence_id: search
  kind: search
  reference: Owned community, isolate and reusable-taxon roots
  locator: Ignored-inclusive bounded source/strain/taxon search
  summary: No exact reusable identity was found in the named roots; shared generic
    taxa elsewhere cannot supply missing strain-level evidence.
  support: supports
  accessed_at: '2026-10-21T09:15:34.712003Z'
  snapshot_sha256: e40acb756fc7b5c15d249777a39a872d6fa7f2f0283aad27f2bba1bf5a61f9b8
  search_scope: Stored rg --no-ignore --hidden searches of maintained roots; bounded
    exact identifiers/names, not an exhaustive synonym or global absence search.
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources runner
  locator: Same batch05 runtime discovery reused from 000120 at 08:47:38Z
  summary: No callable owned-runtime adapter was available; no external runner or
    source/module query was executed.
  support: supports
  accessed_at: '2026-10-21T09:15:34.713420Z'
  snapshot_sha256: 64eaa590a290edb968f18c634c2750bc5967c5e3bda5ada033dd40e7645f1f64
  search_scope: Original batch05 PATH/venv/module and ignored-inclusive owned-path
    discovery retained with its timestamp and checkout boundary.
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: 'support-audit.json: target audit and native metric components'
  summary: Native network status is COMPLETE with no issues; four evidence items on
    one node give mean 4, without certifying measured cooperation.
  support: supports
  accessed_at: '2026-10-21T09:15:34.713808Z'
  snapshot_sha256: 707a0e7e5c9d530cf1a41720288f9b619f79bd0a2d06da277fb63f064ad12f45
- evidence_id: independent-source
  kind: validation
  reference: PMID:42627158
  locator: 'root-independent-source-audit.json: full main, key figure and supplement
    scope'
  summary: Independent review read complete main text, main Figs. 6-9 pixels and all
    S6 captions/tables/figures; workbook inspection was structural and selective,
    not omics reanalysis.
  support: supports
  accessed_at: '2026-10-21T09:15:34.714043Z'
  snapshot_sha256: ee4224017e9122dd15c5c21721b0ef85533e295fa14f57959c9f1f1381fe5291
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
  locator: Actual execution 2026-10-21T09:09:47.832608+00:00 to 2026-10-21T09:09:49.056174+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T09:09:49.056174Z'
  snapshot_sha256: d94ce4a95c6cb671ec535bbe165fb1777da89bfaccd4bea73ddb3eb7c6bfcd8e
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-strict kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    --out /private/tmp/cm-review-session/batch-05/000370/strict-report.tsv
  locator: Actual execution 2026-10-21T09:09:47.833497+00:00 to 2026-10-21T09:09:59.853605+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T09:09:59.853605Z'
  snapshot_sha256: 753776c30ceb2a873d5e3cba130243401fb419e0c9a95eaac6a80c16cb3b8c3b
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-terms kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
  locator: Actual execution 2026-10-21T09:09:47.833609+00:00 to 2026-10-21T09:09:50.786647+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T09:09:50.786647Z'
  snapshot_sha256: a03bd9792b1bb07d5310836cd58b744158738ea78402d0e529696eb39636e7aa
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
  locator: Actual execution 2026-10-21T09:09:49.059242+00:00 to 2026-10-21T09:09:49.226206+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T09:09:49.226206Z'
  snapshot_sha256: de8dd773a8549053be0428f00d70b199bd02862f6a5d435370111f9c6b746458
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
  locator: Actual execution 2026-10-21T09:09:49.226630+00:00 to 2026-10-21T09:09:51.676640+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T09:09:51.676640Z'
  snapshot_sha256: 6211c54eb091b7a13e2b027a1a9d6012805855024f1b6909eb184876953aab5f
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-history history/records/Bacillus_Pseudomonas_Galveston_PET_Consortium
  locator: Actual execution 2026-10-21T09:09:50.786983+00:00 to 2026-10-21T09:09:51.970613+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T09:09:51.970613Z'
  snapshot_sha256: d542e40c9a98a74b3410d0c1903b79046359a48790835f3952243d16e5c4d5c2
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T09:09:59.854564+00:00 to 2026-10-21T09:09:59.957849+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T09:09:59.957849Z'
  snapshot_sha256: 4a8f2c034d5d0c105d55010b80642c556a16a2da389232487fd33e0151b5e4ce
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src
    just --no-dotenv validate-references-explained kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
  locator: Actual execution 2026-10-21T09:09:59.958111+00:00 to 2026-10-21T09:10:01.480859+00:00
  summary: Target reference validation passed against the selected-passage cache.
  support: supports
  accessed_at: '2026-10-21T09:10:01.480859Z'
  snapshot_sha256: 8bcb5e13f723c10a59a17dfa102d2fb340323260bcf4bae88646d154d1e99c3d
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-05/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T08:44:47.720127+00:00 to 2026-10-21T08:45:04.195128+00:00
  summary: Fresh batch05 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
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
    and exit 1; this target has no native network issue.
  support: supports
  accessed_at: '2026-10-21T08:45:04.925187Z'
  snapshot_sha256: 8128f67a5d762dda726f1e6a0c0775a825d030d316c46765c08a359e6b621edb
assessments:
- assessment_id: identity
  area: identity
  topic: Five-isolate PET consortium and source scope
  outcome: supported
  summary: The study and five-member roster resolve; operational grouping of 10/13.2
    does not erase their separate identities.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - membership
  - datasets
  - record
  - ontology
  dimensions:
  - name: community_scope
    value: Environmental consortium examined in laboratory cultures
    definition: Natural co-enrichment provenance and laboratory reconstruction are
      distinguished; BIOREMEDIATION is compatible with PET transformation.
    evidence_ids:
    - membership
    - model
    - record
  - name: source_strain
    value: B. thuringiensis 9.1; B. cereus 13.1; Pseudomonas 9.2, 10, 13.2
    definition: Five sample identities verify; near-identical 10/13.2 are a combined
      comparative unit, not a demonstrated single organism.
    evidence_ids:
    - membership
    - datasets
  - name: environment
    value: Laboratory culture with contaminated coastal-soil provenance
    definition: Current laboratory ENVO and modeled contaminated-soil ENVO encode
      distinct contexts; geographic provenance is source-reported, not supplied by
      missing archive location metadata.
    evidence_ids:
    - membership
    - ontology
    - datasets
  - name: medium
    value: LCFBM with yeast extract plus PET or MHET
    definition: The source medium name does not prove absence of organic carbon; the
      stock recipe and substrate-specific incubation remain separable.
    evidence_ids:
    - medium
  - name: experimental_setting
    value: Seven-week static PET growth and 21-day aerobic MHET transformation
    definition: Final consortium OD600 0.01; PET cultures use 5 mL in 1.5-cm tubes
      in triplicate; 37°C applies to overnight LB seed cultures.
    evidence_ids:
    - medium
  - name: evidence_tier
    value: In-vitro chemistry plus comparative genomic/proteomic inference
    definition: Measured substrate/product signals and proposed partner roles have
      different evidential strength; no member-resolved transfer, complete mineralization
      or detoxification test is claimed.
    evidence_ids:
    - chemistry
    - proteomics
    - model
    - supplement
  - name: grounding_status
    value: Eight matched pairs; three verified optional strain-specific NCBI candidates
    definition: GTDB ambiguity/status is retained without recomputing historical candidate
      sets; no specific GTDB assignment follows from reference-proteome labels.
    evidence_ids:
    - ontology
    - grounding-candidates
    - adapter
- assessment_id: taxonomy
  area: grounding
  topic: All five member identities, roles and abundance descriptions
  outcome: concern
  summary: Membership resolves, but local role evidence should distinguish observed
    activity from proposed cross-feeding.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - membership
  - datasets
  - model
  - proteomics
  - schema
  details: Both Bacillus PRIMARY_DEGRADER roles are compatible with source hydrolytic
    evidence; their membership-only snippets should be supplemented. All three Pseudomonas
    CROSS_FEEDER roles need an explicit inference qualifier and role-specific source
    support. One-of-five wording describes membership, not measured abundance; no
    percentage-based defect is asserted.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Bacillus-Pseudomonas PET division of labor'
  outcome: supported
  summary: Retain the COMMUNITY_LEVEL, PARTIAL niche-specialization model and its
    explicit uncertainty.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - model
  - chemistry
  - proteomics
  - supplement
  - schema
  - ontology
  details: 'Participants are the five-isolate consortium, with Bacillus/Pseudomonas
    activities overlapping and 10/13.2 unresolved analytically. The proposal places
    extracellular polymer processing before downstream intermediate handling, but
    no directed edge or member-resolved transfer is encoded. NICHE_PARTITIONING remains
    a proposed model: competition reduction is explicitly unmeasured. Full-consortium
    PET-associated transformation, MHET comparison limits, tentative MMHET identity
    and absence of matched monoculture proteomes are accurately distinguished. Zero
    arrows require no invented connectivity.'
- assessment_id: conditions
  area: completeness
  topic: Media, environmental factors and cultivation context
  outcome: concern
  summary: Most conditions are source-supported; clarify carbon terminology and recover
    the bounded trace-stock recipe.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - medium
  - snippets
  - record
  details: PET 1%, MHET 0.2% and final OD600 0.01 match Methods. The PET and MHET
    entries retain distinct durations/modes. Do not assign seed-culture temperature
    to substrate assays; the source does not provide a separate PET/MHET temperature
    in the inspected cultivation passage. Trace-metal nutrient salts do not establish
    metal-processing activity; NOT_APPLICABLE for processing is reasonable.
- assessment_id: state
  area: identity
  topic: Natural origin versus ecological equilibrium
  outcome: concern
  summary: NATURAL origin is supported, while unqualified STABLE exceeds the inspected
    equilibrium evidence.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - membership
  - stability
  - schema
  details: Co-isolation, continued survival and source discussion of ecological adaptation
    are not measurements of equilibrium composition. Do not substitute another state
    solely from laboratory assembly or incubation duration.
- assessment_id: resources
  area: completeness
  topic: Dataset, sample identifiers and chemical scope
  outcome: concern
  summary: Project/sample links verify; sample identifiers should not be described
    as genome assembly accessions.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - datasets
  - grounding-candidates
  - ontology
  - supplement
  details: The source supports hybrid sequencing, while archive metadata verifies
    identities rather than sequencing quality or completeness. The project publication
    is the earlier PMID 31221643; the current article independently links the project.
    Five denotes this study subset. PET and TPA are correctly grounded; tentative
    MMHET should not become a confirmed exchanged metabolite. No extra dataset accession
    follows from the generic data-within-article statement.
- assessment_id: provenance
  area: evidence
  topic: Final publication, cache boundary and historical review
  outcome: supported
  summary: Fresh main text resolves the selected cache boundary; existing qualified
    graph repairs remain supported.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - pubmed
  - crossref
  - epmc
  - fulltext
  - snippets
  - history
  - hgt
  - independent-source
  details: The cache sentinel overstates coverage but the prior decision already disclosed
    selected excerpts. Three SupportingReference full_text values are schema-valid.
    One degree-symbol omission needs exact quotation repair; it does not undermine
    the LB condition. Published evidence is kept separate from the discovered, unused
    preprint.
- assessment_id: validation
  area: schema
  topic: Native gates and semantic review
  outcome: supported
  summary: Seven focused native checks and cache preflight pass; target network integrity
    is complete.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - ontology
  - snippets
  - check-validate
  - check-validate-strict
  - native-target
  details: Corpus warnings retain actual failing exit codes and are not assigned to
    this target. Reference-cache success does not independently establish fresh quote
    fidelity or biological interpretation.
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: supported
  summary: Completeness is 90 and capped quality 100; four minor findings remain despite
    the high diagnostic score.
  target_ids:
  - CommunityMech:000370
  evidence_ids:
  - record
  - native-target
  metrics:
  - name: completeness
    value: 90
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including all taxon roles + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). 50 + 5 + 10 + 0 + 5 + 10 + 5 + 5 = 90.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1=0, P2=0, P3=4, P4=0; 4 items / 1 node =
      4; native COMPLETE. 100 - 8 + 20 + 15 = 127 before capping.
  - name: P1
    value: 0
    unit: findings
    definition: Observed native severity count within this complete record review.
  - name: P2
    value: 0
    unit: findings
    definition: Observed native severity count within this complete record review.
  - name: P3
    value: 4
    unit: findings
    definition: Observed native severity count within this complete record review.
  - name: P4
    value: 0
    unit: findings
    definition: Observed native severity count within this complete record review.
findings:
- finding_id: role-evidence-scope
  issue_key: cm-000370-role-evidence-scope
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded metadata or evidence qualification is needed
    without invalidating the resolved roster or already qualified interaction model.'
  rule_id: review-checklist.claim-level-evidence
  status: open
  certainty: confirmed
  title: Qualify taxon roles with claim-level source evidence
  description: Taxon-local snippets identify membership and BioSamples, not functions.
    The three CROSS_FEEDER assignments present the proposed handoff without the graph's
    inference limits; published chemistry and protein associations do not establish
    member-resolved uptake of another member's products.
  target_ids:
  - CommunityMech:000370
  field_paths:
  - taxonomy[0].evidence
  - taxonomy[1].evidence
  - taxonomy[2].evidence
  - taxonomy[3].evidence
  - taxonomy[4].evidence
  - taxonomy[2].functional_role
  - taxonomy[3].functional_role
  - taxonomy[4].functional_role
  evidence_ids:
  - membership
  - model
  - chemistry
  - proteomics
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    role: canonical_record
- finding_id: medium-and-quotation
  issue_key: cm-000370-medium-and-quotation
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded metadata or evidence qualification is needed
    without invalidating the resolved roster or already qualified interaction model.'
  rule_id: review-checklist.cultivation
  status: open
  certainty: confirmed
  title: Clarify LCFBM composition and restore source-exact cultivation evidence
  description: The description calls the medium carbon-free although the encoded and
    published formulation contains yeast extract. The trace stock remains unspecified
    locally despite a recoverable recipe, and the LB quote drops the degree symbol.
    These are bounded wording/completeness issues, not evidence that PET transformation
    was absent.
  target_ids:
  - CommunityMech:000370
  field_paths:
  - description
  - growth_media[0].composition[3]
  - growth_media[0].evidence[0].snippet
  - growth_media[1].composition[0]
  evidence_ids:
  - medium
  - snippets
  - history
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    role: canonical_record
- finding_id: equilibrium-state
  issue_key: cm-000370-equilibrium-state
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded metadata or evidence qualification is needed
    without invalidating the resolved roster or already qualified interaction model.'
  rule_id: review-checklist.community-scope
  status: open
  certainty: confirmed
  title: Qualify the unsupported equilibrium state
  description: STABLE asserts equilibrium, but co-enrichment, bounded growth and inferred
    ecological persistence do not establish equilibrium composition in the reviewed
    source.
  target_ids:
  - CommunityMech:000370
  field_paths:
  - ecological_state
  evidence_ids:
  - stability
  - schema
  - membership
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    role: canonical_record
- finding_id: sample-accession-scope
  issue_key: cm-000370-sample-accession-scope
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded metadata or evidence qualification is needed
    without invalidating the resolved roster or already qualified interaction model.'
  rule_id: review-checklist.identifier-resolution
  status: open
  certainty: confirmed
  title: Distinguish BioSample identifiers from genome assembly accessions
  description: Three taxon notes call their BioSamples strain-level genome accessions.
    The verified identifiers describe biological samples; no assembly identity was
    verified from those notes. More specific current NCBI strain placeholders are
    available as optional refinements.
  target_ids:
  - CommunityMech:000370
  field_paths:
  - taxonomy[2].taxon_term.notes
  - taxonomy[3].taxon_term.notes
  - taxonomy[4].taxon_term.notes
  evidence_ids:
  - datasets
  - grounding-candidates
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    role: canonical_record
actions:
- action_id: repair-role-evidence-scope
  description: Qualify taxon roles with claim-level source evidence.
  finding_ids:
  - role-evidence-scope
  target_ids:
  - CommunityMech:000370
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Attach role-specific primary evidence to both Bacillus degradation roles; retain
    incomplete-transformation scope.
  - Qualify Pseudomonas cross-feeding as the source-proposed model with PARTIAL evidence
    or remove an unqualified role if the representation cannot retain that uncertainty.
  - Do not infer transferred carbon from externally supplied MHET consumption, protein
    presence, or the conceptual Fig. 9 alone.
  - Preserve the current PARTIAL community node, zero arrows, overlapping functions
    and unresolved 10/13.2 contributions.
- action_id: repair-medium-and-quotation
  description: Clarify LCFBM composition and restore source-exact cultivation evidence.
  finding_ids:
  - medium-and-quotation
  target_ids:
  - CommunityMech:000370
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Describe LCFBM as the source-named medium containing 0.05% wt/vol yeast extract;
    avoid implying literal carbon absence or demonstrated sole-carbon growth.
  - 'Document the stock separately from its 1% vol/vol addition: FeSO4·7H2O and MgSO4·7H2O
    each 0.1% wt/vol; CuSO4·5H2O, MnSO4·5H2O and ZnSO4·7H2O each 0.01% wt/vol.'
  - Restore the primary-source degree symbol in the LB snippet and retain explicit
    historical cache provenance rather than silently claiming the cache was exact.
  - Keep 37°C attached to overnight LB seed culture; retain separate static seven-week
    PET and aerobic 21-day MHET conditions.
  - Resolve the MHET base by explicit reference to the same formulation without inventing
    a CultureMech recipe ID or substrate-assay temperature.
- action_id: repair-equilibrium-state
  description: Qualify the unsupported equilibrium state.
  finding_ids:
  - equilibrium-state
  target_ids:
  - CommunityMech:000370
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Supply direct source evidence of equilibrium if retaining STABLE; otherwise use
    a schema-supported uncertainty representation or explain the unresolved state.
  - Preserve NATURAL origin and the laboratory assay context; do not automatically
    replace the state with TRANSIENT or ENGINEERED.
- action_id: repair-sample-accession-scope
  description: Distinguish BioSample identifiers from genome assembly accessions.
  finding_ids:
  - sample-accession-scope
  target_ids:
  - CommunityMech:000370
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Call SAMN41232459, SAMN41232460 and SAMN41232462 BioSample accessions, and retain
    their verified source-strain/project mappings.
  - If refining NCBI grounding, use verified canonical pairs 3144666 Pseudomonas sp.
    9.2(2024), 3144667 Pseudomonas sp. 10(2024), and 3144665 Pseudomonas sp. 13.2
    while preserving reported strain names and candidate provenance.
  - Do not call current generic NCBITaxon:306 wrong, infer a new named biological
    species, or collapse separate samples 10 and 13.2.
  - Keep sample_count 5 scoped to the reviewed set; do not claim it is the total project
    size or infer assembly completeness, GTDB placement or raw sequencing validation.
- action_id: validate-curation
  description: After separately authorized corrections, rerun native checks and document
    the precise source-backed changes.
  finding_ids:
  - role-evidence-scope
  - medium-and-quotation
  - equilibrium-state
  - sample-accession-scope
  target_ids:
  - CommunityMech:000370
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_Pseudomonas_Galveston_PET_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - Preserve the existing qualified interaction and zero-arrow graph while repairing
    non-graph claims.
  - Use source-exact evidence and a new history event; rerun schema, strict, term,
    reference, history and network checks.
  - Refresh historical source-access discussion to reflect inspected figures/supplement
    scope without claiming independent raw-data reproduction.
  - Do not close broader issue 1256 solely because this target is corrected; its other
    records remain outside scope.
limitations:
- Final published XML is primary evidence. The discovered preprint was not used; publisher
  PDF access failed while EPMC main XML and relevant supplements were available.
- Complete main text, tables and captions were read; independent visual review covers
  main Figs. 6-9 and all S6 figures, not main Fig. 1-5 pixels. Five workbooks were
  inventoried and selectively inspected; no genome, proteome, HGT or chromatographic
  analysis was reproduced.
- Proposed inter-member handoff, ecological persistence and MMHET function remain
  interpretations; no equilibrium composition, member-resolved carbon transfer, complete
  mineralization or direct detoxification result is certified.
- Five BioSamples and their project link verify identity, not assembly completeness
  or sequencing quality. The project also lists older samples; current sample_count
  denotes the reviewed set. The source combined 10/13.2 analytically, without collapsing
  their distinct sample identities.
- Specific Pseudomonas taxids are archive-backed optional refinements; GTDB candidate
  lists were not recomputed, and proteomic reference matches do not reidentify the
  source strains.
- The committed cache contains selected excerpts despite its full-text sentinel; 26
  of 27 snippets match fresh XML, with one degree-symbol omission. No cache, canonical
  record or historical artifact was changed.
- Same-runtime adapter discovery and fresh full-corpus network receipts are explicitly
  reused. The corpus failures are not target-specific graph defects.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 9 words across the publication and its supplement.
- All 25 repository inputs were pinned before assessment and rechecked; quality 100
  is capped from 127 and does not remove the four minor findings.
tags:
- record-review
- completed
- pet-degradation
- batch-05
```
