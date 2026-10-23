# Bacillales LDSynCom: whole-record review

- Review: 20261021T082337Z-bacillales-ldsyncom-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T08:15:39.537962Z
- Finished UTC: 2026-10-21T08:23:37.303733Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Three minor findings concern dataset stage/assembly level, Figure 5 measurement/statistical precision, and two nonverbatim cached snippets. All eleven source strains resolve; three graph nodes retain appropriate proxy and nonexclusive-mechanism limits, with no arrows. Seven focused gates and cache preflight pass; separate fresh-source quotation failures and corpus network warnings remain explicit.

## Scope And Provenance

Entire record; all eleven strains, three nodes, zero arrows and thirty-one evidence occurrences. Fresh version-1 main text, Table 1, relevant main figures, exact archive identities and immutable GitHub code/selected workbooks were assessed without executing external code or reanalyzing raw data.

Selection: Next uncovered maintained path after CommunityMech:000284 in batch04; one resolved eleven-strain engineered consortium.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base c6e5a9b9af2d05e12eaafb2555a53f3a079268f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000383 | kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml | maintained | Bacillales Lignin-Degrading LDSynCom |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000383 | Target schema validation passed. |
| validate-strict | passed | True | CommunityMech:000383 | Target strict validation passed. |
| validate-terms | passed | True | CommunityMech:000383 | Target term validation passed. |
| validate-gtdb | passed | True | CommunityMech:000383 | Target GTDB syntax/status validation passed. |
| validate-gtdb-domain | passed | True | CommunityMech:000383 | Target GTDB domain validation passed. |
| validate-history | passed | True | CommunityMech:000383 | Target history validation passed. |
| normalize-cache-names-check | passed | True | CommunityMech:000383 | Read-only corpus cache-filename preflight passed. |
| validate-references-explained | passed | True | CommunityMech:000383 | Target native references passed against pinned caches; two fresh-source quotation differences were found separately. |
| audit-network | failed | True | CommunityMech:000383 | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-network-quality | failed | True | CommunityMech:000383 | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| Versioned primary source and full scientific assessment | passed | True | CommunityMech:000383 | Version-1 main text, Table 1 and relevant main figures support a completed review with explicit source ambiguities. |
| Fresh-source snippet fidelity | failed | True | CommunityMech:000383 | Twenty-nine of thirty-one occurrences match fresh sources; two supported claims require verbatim-snippet repairs. |
| Strain, archive and immutable code verification | passed | True | CommunityMech:000383 | All eleven exact archive identities, both projects and pinned GitHub files resolve with stage and assembly-level qualifications. |
| Encoded medium and ingredient-Mech links | not_applicable | False | CommunityMech:000383 | No CultureMech or MediaIngredientMech ID is encoded, and no unique M9 recipe equivalence is certified. |
| Optional structured source adapter | unavailable | False | CommunityMech:000383 | Same-runtime discovery was reused; no strain-module coverage was queried. |

## Scientific And Domain Assessments

### Community, study stage and source strains

identity: supported. Targets: CommunityMech:000383.

The final eleven-strain consortium resolves consistently across version-1 Table 1, Figure 4, immutable code and archive identities.

### All eleven members, roles and abundance

grounding: supported. Targets: CommunityMech:000383.

Source selection and all eleven immutable mappings support membership without uniform functional roles or inferred final abundance.

The nine species anchors cover CEW-AP100, CEW_1W, G6S2, KF24, LY92, MB7_B11, Puebla_S2, MB7_B13, D9_B_56, D9_B_45 and 11B. Each has a distinct encoded assembly. The membership-only abundance text is appropriate; neither equal inoculation nor proteomic contribution establishes cell-count dominance.

### ecological_interactions[0]: LDSynCom lignin-associated phenolic signal

graph: concern. Targets: CommunityMech:000383.

The indirect community phenotype is supported; mean differences from dropout and 11B controls need explicit statistical limits.

Participants are the full eleven-strain consortium versus uninoculated medium, ten-strain dropout and 11B alone in M9 with 0.2% glucose and 0.1% lignin. The measured direction is toward greater day-28 mean A750 signal; only the full-versus-uninoculated contrast is separated by Figure 5C lettering. No structural cleavage, mineralization or downstream causal edge is established.

### ecological_interactions[1]: Paenibacillus 11B contribution to LDSynCom phenolic accumulation

graph: concern. Targets: CommunityMech:000383.

The targeted perturbation supports a contribution interpretation, with AUC and mean-only phenolic contrasts distinguished.

The participant is NCBITaxon:3060965, Paenibacillus sp. 11B, removed from the otherwise ten-member consortium and also grown alone. The reported direction is reduced growth AUC and a lower phenolic mean after removal under the same M9 conditions. The phenolic contrast is not statistically separated; the evidence does not establish exclusive depolymerization or reciprocal benefit to remaining strains.

### ecological_interactions[2]: LDSynCom lignin-particle biofilm formation

graph: supported. Targets: CommunityMech:000383.

SEM supports the surface-associated community phenotype and GO:0042710.

Participants are the inoculated eleven-strain consortium observed on lignin particles after ten days, compared with abiotic lignin. No member-specific donor/recipient or downstream causal direction is encoded. Matrix association does not show that biofilm causes the phenolic signal; pseudocolor and morphology do not identify strains.

### All downstream lists

graph: not_applicable. Targets: CommunityMech:000383.

The current three-node graph contains zero directed arrows; no new mechanistic edge is warranted from the inspected evidence.

### Origin, category, state, factors and metal relevance

scope: supported. Targets: CommunityMech:000383.

ENGINEERED, SYNTHETIC, LIGNOCELLULOSE and the laboratory environment are appropriate, and the two substrate factors have supported values.

The category records the application, not demonstrated cellulose degradation or lignin mineralization. Empty metals/REE and NOT_APPLICABLE describe the absence of a demonstrated metal-processing role; enzyme annotations do not change that classification.

### Medium, setup and related lignin ingredient

scope: supported. Targets: CommunityMech:000383.

The encoded M9 liquid conditions, source substrate and assay-specific notes are supported.

Existing notes separate seven-day proteomics, ten-day SEM and 41-42-day dropout. Glucose prevents treating growth alone as proof of lignin-only carbon utilization. The source general recipe has missing subscripts and inconsistent concentration statements; no inferred correction or unique CultureMech recipe is certified.

### Both BioProjects, assembly links and external code

scope: concern. Targets: CommunityMech:000383.

Identifiers and eleven strain links verify, but assembly-level and selection-stage descriptions require qualification.

The 121 count is source-library scope, not a fresh complete archive inventory. PRJNA1505615 profiles top-down enrichment; immutable source workbooks support proteomic contribution, not cell abundance. No raw PRIDE accession is verified from a placeholder.

### Fresh-source fidelity, caches, history and current issues

provenance: concern. Targets: CommunityMech:000383.

Two source-exact snippet repairs remain despite native cache validation; historical graph repairs remain intact.

Both committed caches contain selected excerpts, not independently complete papers. Table 1 is now available through the fresh PDF, resolving that roster access gap while historical HTTP 429 notes remain historically accurate.

### Native checks, ontology and source fidelity

schema: concern. Targets: CommunityMech:000383.

Seven focused gates and cache preflight pass; all twelve term pairs verify, while the separate fresh-source audit finds two quote defects.

### Native completeness and quality

completeness: supported. Targets: CommunityMech:000383.

Completeness is 40 and capped native quality is 100; neither score overrides the three minor curation findings.

## Findings

### dataset-scope: Dataset descriptions overstate genome completeness and final-community scope

minor / open / confirmed; issue key: cm-000383-dataset-scope.

The genome-project title and description generalize complete genomes, but four encoded current RefSeq assemblies are Contig level. The second dataset title and organism identify final LDSynCom, although project metadata and Methods place the tuf profiling in top-down enrichment of the starting collection. These are attribution limits, not invalid accession findings.

### assay-precision: Growth endpoint and phenolic comparisons need explicit limits

minor / open / confirmed; issue key: cm-000383-assay-precision.

The two signal/contribution nodes correctly preserve indirect chemistry and the reported mean direction, but biomass wording and unqualified reduction language can imply stronger endpoints. Figure 5B is cumulative OD-AUC; Figure 5C does not statistically separate full LDSynCom from dropout or 11B alone.

### fresh-snippets: Two cached quotations are not verbatim fresh-paper spans

minor / open / confirmed; issue key: cm-000383-fresh-snippets.

The environmental lignin snippet changes an article, and the SEM setup snippet replaces the expanded parenthetical subject with an abbreviation. Both match selected cached excerpts, but neither is a contiguous fresh HTML/PDF span; the underlying medium claims are supported.

## Recommended Actions And Acceptance Checks

### fix-dataset-scope

Qualify assembly completeness and distinguish library genomics, enrichment profiling and final consortium assays.

- Identify GCF_030348465.1, GCF_030348595.1, GCF_030348625.1 and GCF_030487755.1 as current Contig assemblies; preserve the other seven Complete Genome records.
- Retain the publication wording as source-attributed rather than treating it as current assembly-level certification.
- Describe PRJNA1505615 as top-down enrichment biofilm profiling, with its actual source method.
- Keep 121 as the reported library size, not an independently enumerated repository inventory.
- Preserve all eleven verified strain links and run strict and reference checks.

### fix-assay-precision

Describe the plotted growth proxy and distinguish phenolic mean differences from statistically supported contrasts.

- Use cumulative OD-AUC for Figure 5B rather than direct biomass mass or final yield.
- State that full/dropout/11B phenolic means share statistical letters; retain the significant full-versus-uninoculated contrast.
- Preserve the numerical mean direction and bounded 11B contribution interpretation without declaring 11B irrelevant.
- Keep indirect chemistry, nonexclusive roles and absence of downstream arrows.
- Run strict, reference and network checks.

### fix-fresh-snippets

Replace the two snippets with source-exact spans and retain versioned fresh-source provenance during a separately authorized curation.

- Use Methods sec-3 and sec-10, corroborated by PDF lines 122-123 and 225-227.
- Do not alter supported lignin concentration or SEM conditions to resolve a quotation defect.
- Keep any refreshed cache provenance distinct from the historical selected-excerpt cache.
- Confirm every repaired snippet against the fresh source as well as native reference validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml; Entire target: eleven strains, three nodes, no arrows, two factors, one medium and two datasets | supports | The final engineered consortium is explicitly distinguished from the 121-strain starting library and four excluded candidates. |
| fulltext | doi:10.64898/2026.08.24.746789; https://www.biorxiv.org/content/10.64898/2026.08.24.746789v1.full.txt | supports | Fresh version-1 HTML supplied the complete main Methods, Results, Discussion and Conclusions. |
| root-biorxiv-pdf | doi:10.64898/2026.08.24.746789; https://www.biorxiv.org/content/10.64898/2026.08.24.746789v1.full.pdf | supports | Fresh version-1 PDF supplied the complete candidate Table 1 and figure legends; Figure 5 was independently inspected visually. |
| crossref | https://api.crossref.org/works/10.64898/2026.08.24.746789; https://api.crossref.org/works/10.64898/2026.08.24.746789 | supports | Fresh DOI/title metadata identifies this work as posted content, dated 2026-08-25. |
| biorxiv-metadata | https://api.biorxiv.org/details/biorxiv/10.64898/2026.08.24.746789; https://api.biorxiv.org/details/biorxiv/10.64898/2026.08.24.746789 | supports | The current bioRxiv response lists version 1 and published NA; no global absence of a journal article is inferred. |
| selection | doi:10.64898/2026.08.24.746789; Methods sec-3, sec-4, sec-6; Results sec-14 to sec-16; PDF Table 1 p.40 and Fig.4A p.44 | supports | The 121-strain collection yields 15 candidates and then eleven retained strains by biofilm formation or dye decolorization; ACCC04323, LY18, YX13 and DX1.1 are excluded. This does not assign every strain the same degradation role. |
| conditions | doi:10.64898/2026.08.24.746789; Methods sec-3, sec-6, sec-10 to sec-12; Results sec-18; Fig.5 legend | supports | Liquid M9 includes 1 g/L lignin and explicit 0.2% glucose. Top-down enrichment uses 10 uL per starting strain; final assays use 100 uL per OD-normalized overnight culture. Thirty degrees Celsius and 200 rpm are reported. SEM lasts ten days, proteomics seven days with four replicates per condition, and dropout growth 41 days in text/42 in the caption. |
| phenolic | doi:10.64898/2026.08.24.746789; Results sec-18, phenolic-assay paragraph; Fig.5C | supports | The full consortium has a greater mean Folin-Ciocalteu signal; the statistically supported contrast with uninoculated medium is distinct from comparisons with 11B alone or dropout. |
| dropout | doi:10.64898/2026.08.24.746789; Results sec-18, growth paragraph; Fig.5B | supports | Removing 11B lowers the reported growth trajectory. The plotted growth endpoint is cumulative OD area under the curve, not a direct biomass-mass assay or final yield. |
| biofilm | doi:10.64898/2026.08.24.746789; Methods sec-10; Results sec-17; Fig.4B-C | supports | SEM shows cells in matrix-associated structures on lignin surfaces after ten days; morphology does not identify individual strains or demonstrate that biofilm causes the chemical signal. |
| figure5 | doi:10.64898/2026.08.24.746789; PDF Fig.5 p.45; legend pp.38-39, lines824-834 | supports | Panel B is AUC in OD-days through day 42. Panel C is day-28 phenolic signal with three replicates: control b, full a, dropout ab and 11B a. Shared letters mean the full/dropout/11B phenolic contrasts are not statistically separated. |
| mechanism | doi:10.64898/2026.08.24.746789; Results sec-19; Discussion sec-20; Conclusions sec-21 | supports | Extracellular proteomics and ring-cleaving annotations nominate functions; the authors retain indirect chemical readouts and nonexclusive roles. They do not establish polymer cleavage, mineralization, exact products, cross-feeding or reciprocal benefits. |
| ontology | Local OAK NCBITaxon, ENVO, GO and CHEBI snapshots; Twelve unique ID/label pairs at nineteen occurrences | supports | All labels match. Nine species-ranked taxon anchors represent eleven strains; GO:0042710 fits surface biofilm formation and CHEBI:6457 is the broad lignin polymer class. |
| schema | src/communitymech/schema/communitymech.yaml; CommunityCategoryEnum; EcologicalStateEnum; FunctionalRoleEnum; taxon and cultivation slots | supports | ENGINEERED/SYNTHETIC and broad LIGNOCELLULOSE category fit the study; absent optional strain roles do not authorize uniform degradation assignments. |
| snippets | kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml; Thirty-one snippet occurrences; snippet-audit.json | supports | All 31 match pinned caches, but only 29 match fresh HTML/code; two scientifically supported cultivation claims have nonverbatim cached snippets. |
| quote-locations | doi:10.64898/2026.08.24.746789; Methods sec-3 and sec-10; PDF lines122-123 and225-227 | supports | The lignin-concentration snippet changes its initial article, and the SEM snippet replaces the expanded parenthetical subject with its abbreviation. Fresh HTML and PDF agree; the stated cultivation values remain supported. |
| assemblies | NCBI Datasets public assembly metadata; assemblies-dataset-report.body: all eleven exact encoded GCF records and their explicit paired GCA accessions | supports | All eleven strain, taxon, BioSample and project links verify, including documented name-spacing variants. Paired GCA records match Table 1. Seven assemblies are Complete Genome; MB7_B13, D9_B_56, D9_B_45 and 11B are Contig level. |
| project-960711 | https://www.ncbi.nlm.nih.gov/bioproject/PRJNA960711; Fresh public BioProject XML | supports | PRJNA960711 identifies the Bacillales genome-sequencing collection; its metadata has no publication field, so the preprint supplies the study linkage. |
| project-1505615 | https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1505615; Fresh public BioProject XML | supports | PRJNA1505615 identifies top-down selection of lignin-enriched biofilm communities; it is not a final eleven-member composition series. |
| datasets | NCBI assembly, BioSample and BioProject metadata; dataset-verification.json: eleven encoded assemblies, paired accessions and both projects | supports | Metadata verifies identities while separating collection size, assembly level and enrichment stage; no reads, genomes or full project inventory were reanalyzed. |
| github | GITHUB:Xinming9606/lignin_SynCom_proteomics/blob/ed208e4d5df80c96100f2113db39698832d7b685/downstream_analysis.py; Immutable commit ed208e4d5df80c96100f2113db39698832d7b685: STRAIN_MAP and selected source workbooks | supports | Fresh code, README and three workbooks match their Git blob hashes. S01-S11 exactly resolve the curated roster; code was read statically and never executed. |
| github-data | https://github.com/Xinming9606/lignin_SynCom_proteomics/tree/ed208e4d5df80c96100f2113db39698832d7b685; github-spreadsheet-audit.json: selected proteomics composition, contribution and ring-cleaving workbooks | supports | Four M9 and four M9-plus-lignin groups and annotated 11B candidates are documented. Workbook Fig5/6 names concern proteomic contribution, not paper Figure 5 growth. README retains a PRIDE placeholder, not a verified raw-data accession. |
| history | history/records/Bacillales_Lignin_Degrading_LDSynCom; reports/causal_graph_review/decisions; Two sidecars; 20261005-eleven-records-batch5.yaml lines377-420 | supports | The prior decision hash matches and certifies graph scope only; unsupported mutualism and a dangling readout edge remain absent. |
| issue-1250 | https://github.com/CultureBotAI/CommunityMech/issues/1250; Fresh public issue body and state | supports | Closed graph-qualification repair; it does not certify dataset fields or source-exact quotations. |
| issue-929 | https://github.com/CultureBotAI/CommunityMech/issues/929; Fresh public issue body and state | supports | Closed unsupported-mutualism repair; current nodes do not assert reciprocal benefits. |
| issue-930 | https://github.com/CultureBotAI/CommunityMech/issues/930; Fresh public issue body and state | supports | Closed citation-placement repair removed the uncached slow-growth rationale; fresh v1 Results sec-16 does report slow DX1.1 growth, so this history is not evidence of source absence. |
| issue-932 | https://github.com/CultureBotAI/CommunityMech/issues/932; Fresh public issue body and state | supports | Closed dangling-readout-edge repair; the current graph has no downstream arrows. |
| search | Owned-worktree kb/taxa, community/isolate records and source IDs; Ignored-inclusive bounded exact-identity lookup | supports | No reusable exact taxon/strain match was found; the source/project lookup returned this target only. |
| adapter | Optional kg-microbe-sources adapter; Explicit same-batch04-runtime discovery reuse | supports | No installed runner/module was available in the recorded runtime; no strain-module coverage was queried and the external-checkout candidate was not executed. |
| native-target | NetworkIntegrityAuditor().audit_community(target); support-audit.json: actual targeted API and native rubric | supports | Native COMPLETE has no issues; three node evidence items across three nodes give mean evidence 1.0. Community-level coverage does not establish each strain mechanism. |
| access-table1 | https://www.biorxiv.org/highwire/markup/5735548/expansion?postprocessors=highwire_tables%2Chighwire_reclass%2Chighwire_figures%2Chighwire_math%2Chighwire_inline_linked_media%2Chighwire_embed&amp;table-expand-inline=1; Recorded HTTP response | supports | HTTP 429 prevented this endpoint; Table 1 was nevertheless read in the fresh PDF and no supplementary quantitative reanalysis is claimed. |
| access-supplement-page | https://www.biorxiv.org/content/10.64898/2026.08.24.746789v1.supplementary-material; Recorded HTTP response | supports | HTTP 429 prevented this endpoint; Table 1 was nevertheless read in the fresh PDF and no supplementary quantitative reanalysis is claimed. |
| independent-source | doi:10.64898/2026.08.24.746789; root-source-audit.json: main PDF, Table 1, main figures and metadata | supports | Independent reading agrees with the three minor findings and preserved mechanism limits. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml; Actual execution 2026-10-21T08:15:56.097794+00:00 to 2026-10-21T08:15:57.006783+00:00 | supports | Target schema validation passed. |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-strict kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml --out /private/tmp/cm-review-session/batch-04/000383/strict-report.tsv; Actual execution 2026-10-21T08:15:56.103986+00:00 to 2026-10-21T08:16:09.741508+00:00 | supports | Target strict validation passed. |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-terms kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml; Actual execution 2026-10-21T08:15:56.107096+00:00 to 2026-10-21T08:15:58.511704+00:00 | supports | Target term validation passed. |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-gtdb kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml; Actual execution 2026-10-21T08:15:57.007068+00:00 to 2026-10-21T08:15:57.140813+00:00 | supports | Target GTDB syntax/status validation passed. |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-gtdb-domain kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml; Actual execution 2026-10-21T08:15:57.141245+00:00 to 2026-10-21T08:15:58.949697+00:00 | supports | Target GTDB domain validation passed. |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-history history/records/Bacillales_Lignin_Degrading_LDSynCom; Actual execution 2026-10-21T08:15:58.512081+00:00 to 2026-10-21T08:15:59.321586+00:00 | supports | Target history validation passed. |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-21T08:16:09.742960+00:00 to 2026-10-21T08:16:09.814658+00:00 | supports | Read-only corpus cache-filename preflight passed. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src just --no-dotenv validate-references-explained kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml; Actual execution 2026-10-21T08:16:09.814906+00:00 to 2026-10-21T08:16:11.015922+00:00 | supports | Target native references passed against pinned caches; two fresh-source quotation differences were found separately. |
| check-audit-network | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv audit-network; Actual execution 2026-10-21T07:06:05.543108+00:00 to 2026-10-21T07:06:16.498440+00:00 | supports | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |
| check-check-network-quality | PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv check-network-quality; Actual execution 2026-10-21T07:06:16.498920+00:00 to 2026-10-21T07:06:23.361213+00:00 | supports | Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records and exit 1; this target has no native network issue. |

## Limits And Additional Notes

- The source is bioRxiv version 1. Current API metadata lists no newer version and published NA; this is not an exhaustive search for later journal publication. Peer review is not implied.
- Complete main text and candidate Table 1 were available. Highwire table and supplement endpoints returned HTTP 429; the PDF resolved Table 1. The root reviewer could not read the rendered supplementary Figure S5 quantitatively, and no supplementary raw measurements were reanalyzed.
- The source general M9 recipe has missing formula subscripts, inconsistent glucose-stock versus explicit liquid percentages, and inconsistent Mg/Ca molarity versus mass values. Retain the explicit supported liquid conditions without silently reconstructing a recipe.
- The publication describes 11B as isolated from a worker termite head, while current BioSample metadata says fresh fungus comb. The record does not encode that origin; retain the discrepancy if origin is later curated rather than treating it as a current record defect.
- Both committed caches contain selected excerpts. Their 31 matches do not establish fresh-source quotation fidelity; two spans require repair while their biological claims remain supported.
- Archive checks cover the eleven encoded assemblies/BioSamples and two projects, not full project enumeration, genome completeness analysis or raw Nanopore reads. The project metadata lacks publication fields; paper linkage is supplied by the primary source.
- Pinned code and three selected workbooks were inspected without execution. Proteomic contributions are not cell abundances, enzyme annotations are candidates, and a PRIDE placeholder is not a verified raw mass-spectrometry accession.
- Historical GTDB crosswalk unavailability was not promoted to a current global absence claim. No mapping was recomputed; optional structured-adapter discovery was reused with its original bounded scope.
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 16 words for the preprint and its supplements combined.
- All source input hashes are inherited from the successful official inspect and rechecked before candidate construction.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082337Z-bacillales-ldsyncom-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Bacillales LDSynCom: whole-record review'
started_at: '2026-10-21T08:15:39.537962Z'
finished_at: '2026-10-21T08:23:37.303733Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Canonical target unchanged; prior codex curation prevents person-level
    independence claims. Separate agents assessed primary text/figures, ontology,
    native checks, archive identities, immutable code, snippets, history and metrics.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Three minor findings concern dataset stage/assembly level, Figure 5 measurement/statistical
  precision, and two nonverbatim cached snippets. All eleven source strains resolve;
  three graph nodes retain appropriate proxy and nonexclusive-mechanism limits, with
  no arrows. Seven focused gates and cache preflight pass; separate fresh-source quotation
  failures and corpus network warnings remain explicit.
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
  - path: history/records/Bacillales_Lignin_Degrading_LDSynCom/2026-10-05T101149Z-codex-93bfc2.yaml
    sha256: c0347e351bc3bbf66e9179560d9edeac525f68ecf45d5a0ce67e87d4829c609b
    role: context
  - path: history/records/Bacillales_Lignin_Degrading_LDSynCom/20260915T075952Z-codex-bacillales-ldsyncom.yaml
    sha256: 3ceb462aa72127e222c918ba19d5ad2a1c0dec597f7f625f3ce81bbfbdb4a3c1
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    sha256: 882c357a014a5814d0b7c792c6f299944e22a8a35f453a1d53ebdf20065d749e
    role: target
  - path: references_cache/GITHUB_Xinming9606_lignin_SynCom_proteomics_blob_ed208e4d5df80c96100f2113db39698832d7b685_downstream_analysis.py.md
    sha256: 39093a705fafca2553e552af4a6c323b1b120eadf3537430e5242163af18f503
    role: context
  - path: references_cache/doi_10.64898_2026.08.24.746789.md
    sha256: 555e4673f5a7909623d1d74d544da5a414c5da56a4d0e1b143fd3cd9c6b31cd2
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
- target_id: CommunityMech:000383
  path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  label: Bacillales Lignin-Degrading LDSynCom
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    role: canonical_record
scope:
  description: Entire record; all eleven strains, three nodes, zero arrows and thirty-one
    evidence occurrences. Fresh version-1 main text, Table 1, relevant main figures,
    exact archive identities and immutable GitHub code/selected workbooks were assessed
    without executing external code or reanalyzing raw data.
  selection: Next uncovered maintained path after CommunityMech:000284 in batch04;
    one resolved eleven-strain engineered consortium.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000383
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Target schema validation passed.
  target_ids:
  - CommunityMech:000383
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Target strict validation passed.
  target_ids:
  - CommunityMech:000383
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-strict kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    --out /private/tmp/cm-review-session/batch-04/000383/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Target term validation passed.
  target_ids:
  - CommunityMech:000383
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-terms kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Target GTDB syntax/status validation passed.
  target_ids:
  - CommunityMech:000383
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Target GTDB domain validation passed.
  target_ids:
  - CommunityMech:000383
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Target history validation passed.
  target_ids:
  - CommunityMech:000383
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-history history/records/Bacillales_Lignin_Degrading_LDSynCom
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Read-only corpus cache-filename preflight passed.
  target_ids:
  - CommunityMech:000383
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Target native references passed against pinned caches; two fresh-source
    quotation differences were found separately.
  target_ids:
  - CommunityMech:000383
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-references-explained kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Seven focused target/history gates plus one corpus cache-filename preflight;
    all pinned inputs unchanged.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000383
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  - native-target
  scope_note: Reused fresh full-corpus batch04 execution; neither a target-specific
    failure nor a pass.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  target_ids:
  - CommunityMech:000383
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  - native-target
  scope_note: Reused fresh full-corpus batch04 execution; neither a target-specific
    failure nor a pass.
- check_id: primary-source
  name: Versioned primary source and full scientific assessment
  status: passed
  required: true
  summary: Version-1 main text, Table 1 and relevant main figures support a completed
    review with explicit source ambiguities.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - fulltext
  - root-biorxiv-pdf
  - crossref
  - biorxiv-metadata
  - independent-source
- check_id: fresh-snippet-audit
  name: Fresh-source snippet fidelity
  status: failed
  required: true
  summary: Twenty-nine of thirty-one occurrences match fresh sources; two supported
    claims require verbatim-snippet repairs.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - snippets
  - quote-locations
- check_id: source-data
  name: Strain, archive and immutable code verification
  status: passed
  required: true
  summary: All eleven exact archive identities, both projects and pinned GitHub files
    resolve with stage and assembly-level qualifications.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - datasets
  - assemblies
  - github
  - github-data
- check_id: cross-mech
  name: Encoded medium and ingredient-Mech links
  status: not_applicable
  required: false
  summary: No CultureMech or MediaIngredientMech ID is encoded, and no unique M9 recipe
    equivalence is certified.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - record
  - conditions
- check_id: structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Same-runtime discovery was reused; no strain-module coverage was queried.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  locator: 'Entire target: eleven strains, three nodes, no arrows, two factors, one
    medium and two datasets'
  summary: The final engineered consortium is explicitly distinguished from the 121-strain
    starting library and four excluded candidates.
  support: supports
  accessed_at: '2026-10-21T08:23:37.292492Z'
- evidence_id: fulltext
  kind: primary_source
  reference: doi:10.64898/2026.08.24.746789
  locator: https://www.biorxiv.org/content/10.64898/2026.08.24.746789v1.full.txt
  summary: Fresh version-1 HTML supplied the complete main Methods, Results, Discussion
    and Conclusions.
  support: supports
  accessed_at: '2026-10-21T08:16:02.425132Z'
  snapshot_sha256: a5e3212b2a1fa66238106e9a01b672fc8e0ad5390b29c88f508558316c29f1b8
- evidence_id: root-biorxiv-pdf
  kind: primary_source
  reference: doi:10.64898/2026.08.24.746789
  locator: https://www.biorxiv.org/content/10.64898/2026.08.24.746789v1.full.pdf
  summary: Fresh version-1 PDF supplied the complete candidate Table 1 and figure
    legends; Figure 5 was independently inspected visually.
  support: supports
  accessed_at: '2026-10-21T08:15:55.866171Z'
  snapshot_sha256: b76077d61e1eb3d2aa79df5d15f1479acecb09665413052a408ab7748c2045ac
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.64898/2026.08.24.746789
  locator: https://api.crossref.org/works/10.64898/2026.08.24.746789
  summary: Fresh DOI/title metadata identifies this work as posted content, dated
    2026-08-25.
  support: supports
  accessed_at: '2026-10-21T08:16:00.728076Z'
  snapshot_sha256: 023140ed8bbcf5eb74bc0b5d8db3ecd4939eb54606fb7ddabb15b104a64ab188
- evidence_id: biorxiv-metadata
  kind: database
  reference: https://api.biorxiv.org/details/biorxiv/10.64898/2026.08.24.746789
  locator: https://api.biorxiv.org/details/biorxiv/10.64898/2026.08.24.746789
  summary: The current bioRxiv response lists version 1 and published NA; no global
    absence of a journal article is inferred.
  support: supports
  accessed_at: '2026-10-21T08:16:00.753993Z'
  snapshot_sha256: 635d66ba953bc8e9149ba4e52c6bc6a1f86ed46f5e7954a5bd9ca76acae62481
- evidence_id: selection
  kind: primary_source
  reference: doi:10.64898/2026.08.24.746789
  locator: Methods sec-3, sec-4, sec-6; Results sec-14 to sec-16; PDF Table 1 p.40
    and Fig.4A p.44
  summary: The 121-strain collection yields 15 candidates and then eleven retained
    strains by biofilm formation or dye decolorization; ACCC04323, LY18, YX13 and
    DX1.1 are excluded. This does not assign every strain the same degradation role.
  support: supports
  accessed_at: '2026-10-21T08:23:37.293785Z'
- evidence_id: conditions
  kind: primary_source
  reference: doi:10.64898/2026.08.24.746789
  locator: Methods sec-3, sec-6, sec-10 to sec-12; Results sec-18; Fig.5 legend
  summary: Liquid M9 includes 1 g/L lignin and explicit 0.2% glucose. Top-down enrichment
    uses 10 uL per starting strain; final assays use 100 uL per OD-normalized overnight
    culture. Thirty degrees Celsius and 200 rpm are reported. SEM lasts ten days,
    proteomics seven days with four replicates per condition, and dropout growth 41
    days in text/42 in the caption.
  support: supports
  accessed_at: '2026-10-21T08:23:37.293787Z'
- evidence_id: phenolic
  kind: primary_source
  reference: doi:10.64898/2026.08.24.746789
  locator: Results sec-18, phenolic-assay paragraph; Fig.5C
  summary: The full consortium has a greater mean Folin-Ciocalteu signal; the statistically
    supported contrast with uninoculated medium is distinct from comparisons with
    11B alone or dropout.
  support: supports
  accessed_at: '2026-10-21T08:23:37.293789Z'
  quote: significantly higher phenolic signals
- evidence_id: dropout
  kind: primary_source
  reference: doi:10.64898/2026.08.24.746789
  locator: Results sec-18, growth paragraph; Fig.5B
  summary: Removing 11B lowers the reported growth trajectory. The plotted growth
    endpoint is cumulative OD area under the curve, not a direct biomass-mass assay
    or final yield.
  support: supports
  accessed_at: '2026-10-21T08:23:37.293791Z'
  quote: reduced the overall growth
- evidence_id: biofilm
  kind: primary_source
  reference: doi:10.64898/2026.08.24.746789
  locator: Methods sec-10; Results sec-17; Fig.4B-C
  summary: SEM shows cells in matrix-associated structures on lignin surfaces after
    ten days; morphology does not identify individual strains or demonstrate that
    biofilm causes the chemical signal.
  support: supports
  accessed_at: '2026-10-21T08:23:37.293792Z'
  quote: well-developed biofilm structures
- evidence_id: figure5
  kind: primary_source
  reference: doi:10.64898/2026.08.24.746789
  locator: PDF Fig.5 p.45; legend pp.38-39, lines824-834
  summary: 'Panel B is AUC in OD-days through day 42. Panel C is day-28 phenolic signal
    with three replicates: control b, full a, dropout ab and 11B a. Shared letters
    mean the full/dropout/11B phenolic contrasts are not statistically separated.'
  support: supports
  accessed_at: '2026-10-21T08:23:37.294460Z'
  quote: groups sharing the same letter
  snapshot_sha256: 4a10911df47e4e0a69819ea6a76812e1fbd38c90e3955fe3a46e295d75dbb41f
- evidence_id: mechanism
  kind: primary_source
  reference: doi:10.64898/2026.08.24.746789
  locator: Results sec-19; Discussion sec-20; Conclusions sec-21
  summary: Extracellular proteomics and ring-cleaving annotations nominate functions;
    the authors retain indirect chemical readouts and nonexclusive roles. They do
    not establish polymer cleavage, mineralization, exact products, cross-feeding
    or reciprocal benefits.
  support: supports
  accessed_at: '2026-10-21T08:23:37.294465Z'
- evidence_id: ontology
  kind: authority
  reference: Local OAK NCBITaxon, ENVO, GO and CHEBI snapshots
  locator: Twelve unique ID/label pairs at nineteen occurrences
  summary: All labels match. Nine species-ranked taxon anchors represent eleven strains;
    GO:0042710 fits surface biofilm formation and CHEBI:6457 is the broad lignin polymer
    class.
  support: supports
  accessed_at: '2026-10-21T08:23:37.295009Z'
  snapshot_sha256: 35c70162f89bb1d13fc6d4b3779db53596101bfa90e7d6cf5986f03dc8feb4c9
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: CommunityCategoryEnum; EcologicalStateEnum; FunctionalRoleEnum; taxon and
    cultivation slots
  summary: ENGINEERED/SYNTHETIC and broad LIGNOCELLULOSE category fit the study; absent
    optional strain roles do not authorize uniform degradation assignments.
  support: supports
  accessed_at: '2026-10-21T08:23:37.295013Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  locator: Thirty-one snippet occurrences; snippet-audit.json
  summary: All 31 match pinned caches, but only 29 match fresh HTML/code; two scientifically
    supported cultivation claims have nonverbatim cached snippets.
  support: supports
  accessed_at: '2026-10-21T08:23:37.295294Z'
  snapshot_sha256: aba011182ceff1bb973ceaee0589d42aa1be349748726ef94c51e554376daef9
- evidence_id: quote-locations
  kind: primary_source
  reference: doi:10.64898/2026.08.24.746789
  locator: Methods sec-3 and sec-10; PDF lines122-123 and225-227
  summary: The lignin-concentration snippet changes its initial article, and the SEM
    snippet replaces the expanded parenthetical subject with its abbreviation. Fresh
    HTML and PDF agree; the stated cultivation values remain supported.
  support: supports
  accessed_at: '2026-10-21T08:23:37.295300Z'
- evidence_id: assemblies
  kind: database
  reference: NCBI Datasets public assembly metadata
  locator: 'assemblies-dataset-report.body: all eleven exact encoded GCF records and
    their explicit paired GCA accessions'
  summary: All eleven strain, taxon, BioSample and project links verify, including
    documented name-spacing variants. Paired GCA records match Table 1. Seven assemblies
    are Complete Genome; MB7_B13, D9_B_56, D9_B_45 and 11B are Contig level.
  support: supports
  accessed_at: '2026-10-21T08:23:37.295597Z'
  snapshot_sha256: eed599c9bcfde716cfb1bce92708fee42c0f750c0baecd096e5b86823d77cc8a
- evidence_id: project-960711
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA960711
  locator: Fresh public BioProject XML
  summary: PRJNA960711 identifies the Bacillales genome-sequencing collection; its
    metadata has no publication field, so the preprint supplies the study linkage.
  support: supports
  accessed_at: '2026-10-21T08:16:16.657706Z'
  snapshot_sha256: 4b3c52dec57fa294d0f636dc8f0c9461ed30063b7151abaed8dd74bf0ce00fc6
- evidence_id: project-1505615
  kind: database
  reference: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA1505615
  locator: Fresh public BioProject XML
  summary: PRJNA1505615 identifies top-down selection of lignin-enriched biofilm communities;
    it is not a final eleven-member composition series.
  support: supports
  accessed_at: '2026-10-21T08:16:16.721336Z'
  snapshot_sha256: 169c0d4c4378870cbc1c26d91f031a688367ff1c82ce168fb34e71b77ba18f2f
- evidence_id: datasets
  kind: validation
  reference: NCBI assembly, BioSample and BioProject metadata
  locator: 'dataset-verification.json: eleven encoded assemblies, paired accessions
    and both projects'
  summary: Metadata verifies identities while separating collection size, assembly
    level and enrichment stage; no reads, genomes or full project inventory were reanalyzed.
  support: supports
  accessed_at: '2026-10-21T08:23:37.296856Z'
  snapshot_sha256: 3da38e9ff2d3b48f9fcf2b2f543350fd139b8cb4070d4f8494f0ee2fdf831d3c
- evidence_id: github
  kind: database
  reference: GITHUB:Xinming9606/lignin_SynCom_proteomics/blob/ed208e4d5df80c96100f2113db39698832d7b685/downstream_analysis.py
  locator: 'Immutable commit ed208e4d5df80c96100f2113db39698832d7b685: STRAIN_MAP
    and selected source workbooks'
  summary: Fresh code, README and three workbooks match their Git blob hashes. S01-S11
    exactly resolve the curated roster; code was read statically and never executed.
  support: supports
  accessed_at: '2026-10-21T08:23:37.297014Z'
  snapshot_sha256: 6c91c09900188fffc9eb0568819dc74ca5cf20997ddf915707dad4ba3a9b4a4d
- evidence_id: github-data
  kind: validation
  reference: https://github.com/Xinming9606/lignin_SynCom_proteomics/tree/ed208e4d5df80c96100f2113db39698832d7b685
  locator: 'github-spreadsheet-audit.json: selected proteomics composition, contribution
    and ring-cleaving workbooks'
  summary: Four M9 and four M9-plus-lignin groups and annotated 11B candidates are
    documented. Workbook Fig5/6 names concern proteomic contribution, not paper Figure
    5 growth. README retains a PRIDE placeholder, not a verified raw-data accession.
  support: supports
  accessed_at: '2026-10-21T08:23:37.297219Z'
  snapshot_sha256: 0318183c17f2223b9aea8678e439a56fd03ff53d3e20f7baed90ebd100c48ec5
- evidence_id: history
  kind: record_content
  reference: history/records/Bacillales_Lignin_Degrading_LDSynCom; reports/causal_graph_review/decisions
  locator: Two sidecars; 20261005-eleven-records-batch5.yaml lines377-420
  summary: The prior decision hash matches and certifies graph scope only; unsupported
    mutualism and a dangling readout edge remain absent.
  support: supports
  accessed_at: '2026-10-21T08:23:37.297393Z'
  snapshot_sha256: 8f852b52d1b92dbdd4a0717cb43babc32b25daec21ed1a851003d0edcaba3405
- evidence_id: issue-1250
  kind: database
  reference: https://github.com/CultureBotAI/CommunityMech/issues/1250
  locator: Fresh public issue body and state
  summary: Closed graph-qualification repair; it does not certify dataset fields or
    source-exact quotations.
  support: supports
  accessed_at: '2026-10-21T08:15:51.679799Z'
  snapshot_sha256: 0d543a02d638c65140c89a475b97dcd986a75f56de5e0c9e6fd4018d811b3b64
- evidence_id: issue-929
  kind: database
  reference: https://github.com/CultureBotAI/CommunityMech/issues/929
  locator: Fresh public issue body and state
  summary: Closed unsupported-mutualism repair; current nodes do not assert reciprocal
    benefits.
  support: supports
  accessed_at: '2026-10-21T08:15:51.683571Z'
  snapshot_sha256: 3cb26c6e5755af8a1ade6d7a8ef06ee21590779d136b52087a4891120cbc7307
- evidence_id: issue-930
  kind: database
  reference: https://github.com/CultureBotAI/CommunityMech/issues/930
  locator: Fresh public issue body and state
  summary: Closed citation-placement repair removed the uncached slow-growth rationale;
    fresh v1 Results sec-16 does report slow DX1.1 growth, so this history is not
    evidence of source absence.
  support: supports
  accessed_at: '2026-10-21T08:15:51.685326Z'
  snapshot_sha256: 04bb4929b355bc6900b6b27a6b3ce2d8dcd5e258376ecd898a1f3841c4b7c9cc
- evidence_id: issue-932
  kind: database
  reference: https://github.com/CultureBotAI/CommunityMech/issues/932
  locator: Fresh public issue body and state
  summary: Closed dangling-readout-edge repair; the current graph has no downstream
    arrows.
  support: supports
  accessed_at: '2026-10-21T08:15:52.340563Z'
  snapshot_sha256: 4324c2be1cc29ff0484523dd2089617ac0edbce97a1a1579ff8ae9b8b437814a
- evidence_id: search
  kind: search
  reference: Owned-worktree kb/taxa, community/isolate records and source IDs
  locator: Ignored-inclusive bounded exact-identity lookup
  summary: No reusable exact taxon/strain match was found; the source/project lookup
    returned this target only.
  support: supports
  accessed_at: '2026-10-21T08:23:37.298913Z'
  snapshot_sha256: abe3d15d0a0eaf10d53af52240fae252c42a068b262711bc84ea024225ae76ed
  search_scope: rg --no-ignore --hidden for the nine exact NCBITaxon IDs, eleven strain
    spellings, source DOI, projects and record ID; no exhaustive synonym claim.
- evidence_id: adapter
  kind: search
  reference: Optional kg-microbe-sources adapter
  locator: Explicit same-batch04-runtime discovery reuse
  summary: No installed runner/module was available in the recorded runtime; no strain-module
    coverage was queried and the external-checkout candidate was not executed.
  support: supports
  accessed_at: '2026-10-21T08:23:37.299050Z'
  snapshot_sha256: 4c023ca26af7566301a2fd7b5a088e6bd31583a876eaca3892ea3d4feab41258
  search_scope: Reused batch04 PATH, virtualenv/module and ignored-inclusive bounded
    discovery with original timestamps.
- evidence_id: native-target
  kind: validation
  reference: NetworkIntegrityAuditor().audit_community(target)
  locator: 'support-audit.json: actual targeted API and native rubric'
  summary: Native COMPLETE has no issues; three node evidence items across three nodes
    give mean evidence 1.0. Community-level coverage does not establish each strain
    mechanism.
  support: supports
  accessed_at: '2026-10-21T08:23:37.299198Z'
  snapshot_sha256: b4476a1bf535f10dab368a07b675c8fbf7f5ae60c3c8dda73c69111005a1425f
- evidence_id: access-table1
  kind: validation
  reference: https://www.biorxiv.org/highwire/markup/5735548/expansion?postprocessors=highwire_tables%2Chighwire_reclass%2Chighwire_figures%2Chighwire_math%2Chighwire_inline_linked_media%2Chighwire_embed&table-expand-inline=1
  locator: Recorded HTTP response
  summary: HTTP 429 prevented this endpoint; Table 1 was nevertheless read in the
    fresh PDF and no supplementary quantitative reanalysis is claimed.
  support: supports
  accessed_at: '2026-10-21T08:16:57.104779Z'
  snapshot_sha256: dda2b901021c367e1b38d4790361de7496429aac4ababa45a2dbb812358c8e99
- evidence_id: access-supplement-page
  kind: validation
  reference: https://www.biorxiv.org/content/10.64898/2026.08.24.746789v1.supplementary-material
  locator: Recorded HTTP response
  summary: HTTP 429 prevented this endpoint; Table 1 was nevertheless read in the
    fresh PDF and no supplementary quantitative reanalysis is claimed.
  support: supports
  accessed_at: '2026-10-21T08:16:57.096713Z'
  snapshot_sha256: 0c20348a90f2e4d40f923c2d8f383f12b32e93140c41f1599ae40d6d3baa3767
- evidence_id: independent-source
  kind: validation
  reference: doi:10.64898/2026.08.24.746789
  locator: 'root-source-audit.json: main PDF, Table 1, main figures and metadata'
  summary: Independent reading agrees with the three minor findings and preserved
    mechanism limits.
  support: supports
  accessed_at: '2026-10-21T08:23:37.299872Z'
  snapshot_sha256: ff87b05e7d0cfccafc0683d81799d2989a093121cef9d5fee50197348df3f43b
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  locator: Actual execution 2026-10-21T08:15:56.097794+00:00 to 2026-10-21T08:15:57.006783+00:00
  summary: Target schema validation passed.
  support: supports
  accessed_at: '2026-10-21T08:15:57.006783Z'
  snapshot_sha256: 500f1e2b0f4406e86eb83c51df29b2fafb0e71c6a220204c13bdedecf526804a
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-strict kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    --out /private/tmp/cm-review-session/batch-04/000383/strict-report.tsv
  locator: Actual execution 2026-10-21T08:15:56.103986+00:00 to 2026-10-21T08:16:09.741508+00:00
  summary: Target strict validation passed.
  support: supports
  accessed_at: '2026-10-21T08:16:09.741508Z'
  snapshot_sha256: 61ee04280c87918ef3dd3ab52f7a8775a9a4052777b17cdd1ae913afed6fde71
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-terms kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  locator: Actual execution 2026-10-21T08:15:56.107096+00:00 to 2026-10-21T08:15:58.511704+00:00
  summary: Target term validation passed.
  support: supports
  accessed_at: '2026-10-21T08:15:58.511704Z'
  snapshot_sha256: 5ca8343ca79d78054a28c405dc283827047cf47298e93f9e90cc2d2db6c55e7b
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  locator: Actual execution 2026-10-21T08:15:57.007068+00:00 to 2026-10-21T08:15:57.140813+00:00
  summary: Target GTDB syntax/status validation passed.
  support: supports
  accessed_at: '2026-10-21T08:15:57.140813Z'
  snapshot_sha256: 5d4b75abac294cb3bdf454d59a35ea4a270fc9b1270bf22dae1e62a14b0361f2
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-gtdb-domain kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  locator: Actual execution 2026-10-21T08:15:57.141245+00:00 to 2026-10-21T08:15:58.949697+00:00
  summary: Target GTDB domain validation passed.
  support: supports
  accessed_at: '2026-10-21T08:15:58.949697Z'
  snapshot_sha256: d88cf2616c6217d6626c77726c080ac58ccd4e334f5d9235561a5ee0d11b71cf
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-history history/records/Bacillales_Lignin_Degrading_LDSynCom
  locator: Actual execution 2026-10-21T08:15:58.512081+00:00 to 2026-10-21T08:15:59.321586+00:00
  summary: Target history validation passed.
  support: supports
  accessed_at: '2026-10-21T08:15:59.321586Z'
  snapshot_sha256: 9d6fc6a43ebe6c35219e21574d11fee2e224bdcbab794fdbf37be95520b53b5a
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-21T08:16:09.742960+00:00 to 2026-10-21T08:16:09.814658+00:00
  summary: Read-only corpus cache-filename preflight passed.
  support: supports
  accessed_at: '2026-10-21T08:16:09.814658Z'
  snapshot_sha256: 7acd69bcb959e08bea6293adda4a846be987c8e837b6584d05b27b7bb84860b3
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src
    just --no-dotenv validate-references-explained kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  locator: Actual execution 2026-10-21T08:16:09.814906+00:00 to 2026-10-21T08:16:11.015922+00:00
  summary: Target native references passed against pinned caches; two fresh-source
    quotation differences were found separately.
  support: supports
  accessed_at: '2026-10-21T08:16:11.015922Z'
  snapshot_sha256: ea54b00971475f745fd809c630d81510c4970b3f6afca60e1899ffcecfc78749
- evidence_id: check-audit-network
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  locator: Actual execution 2026-10-21T07:06:05.543108+00:00 to 2026-10-21T07:06:16.498440+00:00
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  support: supports
  accessed_at: '2026-10-21T07:06:16.498440Z'
  snapshot_sha256: 7e9c998a5a9fe2b1a28c809bd5eb651205b3256dd64666ef7a9ca6fbde7504fa
- evidence_id: check-check-network-quality
  kind: validation
  reference: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-04/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  locator: Actual execution 2026-10-21T07:06:16.498920+00:00 to 2026-10-21T07:06:23.361213+00:00
  summary: Fresh batch04 corpus execution returned 57 warnings across 21 of 477 records
    and exit 1; this target has no native network issue.
  support: supports
  accessed_at: '2026-10-21T07:06:23.361213Z'
  snapshot_sha256: 5ba6a0b7c789574c80df1b60d81f0e54454b66e4f919949ad352cff92dd9744e
assessments:
- assessment_id: identity
  area: identity
  topic: Community, study stage and source strains
  outcome: supported
  summary: The final eleven-strain consortium resolves consistently across version-1
    Table 1, Figure 4, immutable code and archive identities.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - record
  - selection
  - github
  - assemblies
  - ontology
  dimensions:
  - name: community_scope
    value: Eleven-strain engineered Bacillales consortium
    definition: The 121-strain library, fifteen-candidate stage and four excluded
      strains are separate assembly contexts.
    evidence_ids:
    - selection
    - record
  - name: source_strain
    value: Eleven verified assembly/BioSample identities across nine species anchors
    definition: Exact strain designations and documented orthographic variants are
      preserved; shared species IDs do not merge distinct strains.
    evidence_ids:
    - assemblies
    - datasets
    - github
  - name: environment
    value: Controlled aerobic laboratory shake-flask culture
    definition: The laboratory ENVO term fits the assay; source organisms originate
      from diverse environments rather than one natural community.
    evidence_ids:
    - conditions
    - ontology
  - name: medium
    value: M9 with beechwood organosolv lignin and glucose
    definition: Explicit liquid 1 g/L lignin and 0.2% glucose are supported; general
      recipe inconsistencies are not silently corrected.
    evidence_ids:
    - conditions
  - name: experimental_setting
    value: Screening, enrichment, SEM, proteomics and targeted dropout assays
    definition: Different inocula, durations and comparators remain distinct; normalized
      input volumes are not final population abundance measurements.
    evidence_ids:
    - conditions
    - figure5
    - selection
  - name: evidence_tier
    value: Preprint in-vitro phenotypes, indirect chemical assays and proteomic candidates
    definition: Growth AUC and phenolic signal do not directly quantify lignin cleavage
      or identify causal enzymes; SEM establishes attachment.
    evidence_ids:
    - phenolic
    - dropout
    - biofilm
    - mechanism
  - name: grounding_status
    value: Twelve canonical term pairs; GTDB unresolved
    definition: NCBI species labels and strain archives verify, but no GTDB crosswalk
      was recomputed and no current global mapping absence is asserted.
    evidence_ids:
    - ontology
    - assemblies
    - adapter
- assessment_id: taxonomy
  area: grounding
  topic: All eleven members, roles and abundance
  outcome: supported
  summary: Source selection and all eleven immutable mappings support membership without
    uniform functional roles or inferred final abundance.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - selection
  - github
  - assemblies
  - ontology
  details: The nine species anchors cover CEW-AP100, CEW_1W, G6S2, KF24, LY92, MB7_B11,
    Puebla_S2, MB7_B13, D9_B_56, D9_B_45 and 11B. Each has a distinct encoded assembly.
    The membership-only abundance text is appropriate; neither equal inoculation nor
    proteomic contribution establishes cell-count dominance.
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: LDSynCom lignin-associated phenolic signal'
  outcome: concern
  summary: The indirect community phenotype is supported; mean differences from dropout
    and 11B controls need explicit statistical limits.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - record
  - phenolic
  - figure5
  - mechanism
  details: Participants are the full eleven-strain consortium versus uninoculated
    medium, ten-strain dropout and 11B alone in M9 with 0.2% glucose and 0.1% lignin.
    The measured direction is toward greater day-28 mean A750 signal; only the full-versus-uninoculated
    contrast is separated by Figure 5C lettering. No structural cleavage, mineralization
    or downstream causal edge is established.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Paenibacillus 11B contribution to LDSynCom phenolic
    accumulation'
  outcome: concern
  summary: The targeted perturbation supports a contribution interpretation, with
    AUC and mean-only phenolic contrasts distinguished.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - record
  - dropout
  - figure5
  - mechanism
  details: The participant is NCBITaxon:3060965, Paenibacillus sp. 11B, removed from
    the otherwise ten-member consortium and also grown alone. The reported direction
    is reduced growth AUC and a lower phenolic mean after removal under the same M9
    conditions. The phenolic contrast is not statistically separated; the evidence
    does not establish exclusive depolymerization or reciprocal benefit to remaining
    strains.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: LDSynCom lignin-particle biofilm formation'
  outcome: supported
  summary: SEM supports the surface-associated community phenotype and GO:0042710.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - record
  - biofilm
  - ontology
  details: Participants are the inoculated eleven-strain consortium observed on lignin
    particles after ten days, compared with abiotic lignin. No member-specific donor/recipient
    or downstream causal direction is encoded. Matrix association does not show that
    biofilm causes the phenolic signal; pseudocolor and morphology do not identify
    strains.
- assessment_id: arrows
  area: graph
  topic: All downstream lists
  outcome: not_applicable
  summary: The current three-node graph contains zero directed arrows; no new mechanistic
    edge is warranted from the inspected evidence.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - record
  - mechanism
  - history
  - native-target
- assessment_id: environment
  area: scope
  topic: Origin, category, state, factors and metal relevance
  outcome: supported
  summary: ENGINEERED, SYNTHETIC, LIGNOCELLULOSE and the laboratory environment are
    appropriate, and the two substrate factors have supported values.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - record
  - schema
  - conditions
  - ontology
  details: The category records the application, not demonstrated cellulose degradation
    or lignin mineralization. Empty metals/REE and NOT_APPLICABLE describe the absence
    of a demonstrated metal-processing role; enzyme annotations do not change that
    classification.
- assessment_id: cultivation
  area: scope
  topic: Medium, setup and related lignin ingredient
  outcome: supported
  summary: The encoded M9 liquid conditions, source substrate and assay-specific notes
    are supported.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - conditions
  - ontology
  - selection
  details: Existing notes separate seven-day proteomics, ten-day SEM and 41-42-day
    dropout. Glucose prevents treating growth alone as proof of lignin-only carbon
    utilization. The source general recipe has missing subscripts and inconsistent
    concentration statements; no inferred correction or unique CultureMech recipe
    is certified.
- assessment_id: datasets
  area: scope
  topic: Both BioProjects, assembly links and external code
  outcome: concern
  summary: Identifiers and eleven strain links verify, but assembly-level and selection-stage
    descriptions require qualification.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - assemblies
  - project-960711
  - project-1505615
  - datasets
  - github
  - github-data
  details: The 121 count is source-library scope, not a fresh complete archive inventory.
    PRJNA1505615 profiles top-down enrichment; immutable source workbooks support
    proteomic contribution, not cell abundance. No raw PRIDE accession is verified
    from a placeholder.
- assessment_id: provenance
  area: provenance
  topic: Fresh-source fidelity, caches, history and current issues
  outcome: concern
  summary: Two source-exact snippet repairs remain despite native cache validation;
    historical graph repairs remain intact.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - snippets
  - quote-locations
  - history
  - issue-1250
  - issue-929
  - issue-930
  - issue-932
  - search
  details: Both committed caches contain selected excerpts, not independently complete
    papers. Table 1 is now available through the fresh PDF, resolving that roster
    access gap while historical HTTP 429 notes remain historically accurate.
- assessment_id: validation
  area: schema
  topic: Native checks, ontology and source fidelity
  outcome: concern
  summary: Seven focused gates and cache preflight pass; all twelve term pairs verify,
    while the separate fresh-source audit finds two quote defects.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - ontology
  - snippets
  - check-validate
  - check-validate-strict
  - check-audit-network
  - native-target
- assessment_id: metrics
  area: completeness
  topic: Native completeness and quality
  outcome: supported
  summary: Completeness is 40 and capped native quality is 100; neither score overrides
    the three minor curation findings.
  target_ids:
  - CommunityMech:000383
  evidence_ids:
  - record
  - native-target
  metrics:
  - name: completeness
    value: 40
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including every taxon role + 5 environment
      + 10 at least 3 factors + 10 at least 3 nodes + 5 resources + 10 media + 5 datasets
      + 5 node metabolites). 0 + 5 + 0 + 10 + 5 + 10 + 5 + 5 = 40; all eleven optional
      roles are absent, not schema defects.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50P1 - 10P2 - 2P3 + 20 min(mean node evidence / 2, 1)
      + 15 if native COMPLETE, 0, 100). P1=0, P2=0, P3=3, P4=0; 3 items / 3 nodes
      = 1.0; native COMPLETE. 100 - 6 + 10 + 15 = 119 before capping; this is not
      scientific approval.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count for this reviewed target.
  - name: P2
    value: 0
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
- finding_id: dataset-scope
  issue_key: cm-000383-dataset-scope
  category: scope
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded measurement, dataset attribution or quotation
    precision; resolved community identity and qualified graph remain intact.'
  rule_id: review-checklist.datasets
  status: open
  certainty: confirmed
  title: Dataset descriptions overstate genome completeness and final-community scope
  description: The genome-project title and description generalize complete genomes,
    but four encoded current RefSeq assemblies are Contig level. The second dataset
    title and organism identify final LDSynCom, although project metadata and Methods
    place the tuf profiling in top-down enrichment of the starting collection. These
    are attribution limits, not invalid accession findings.
  target_ids:
  - CommunityMech:000383
  field_paths:
  - associated_datasets[0].title
  - associated_datasets[0].description
  - associated_datasets[0].evidence[0].explanation
  - associated_datasets[1].title
  - associated_datasets[1].organism
  - associated_datasets[1].description
  evidence_ids:
  - assemblies
  - project-960711
  - project-1505615
  - datasets
  - selection
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    role: canonical_record
- finding_id: assay-precision
  issue_key: cm-000383-assay-precision
  category: scope
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded measurement, dataset attribution or quotation
    precision; resolved community identity and qualified graph remain intact.'
  rule_id: review-checklist.claim_support
  status: open
  certainty: confirmed
  title: Growth endpoint and phenolic comparisons need explicit limits
  description: The two signal/contribution nodes correctly preserve indirect chemistry
    and the reported mean direction, but biomass wording and unqualified reduction
    language can imply stronger endpoints. Figure 5B is cumulative OD-AUC; Figure
    5C does not statistically separate full LDSynCom from dropout or 11B alone.
  target_ids:
  - CommunityMech:000383
  field_paths:
  - ecological_interactions[0].description
  - ecological_interactions[1].description
  - description
  evidence_ids:
  - phenolic
  - dropout
  - figure5
  - mechanism
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    role: canonical_record
- finding_id: fresh-snippets
  issue_key: cm-000383-fresh-snippets
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded measurement, dataset attribution or quotation
    precision; resolved community identity and qualified graph remain intact.'
  rule_id: review-checklist.snippet_fidelity
  status: open
  certainty: confirmed
  title: Two cached quotations are not verbatim fresh-paper spans
  description: The environmental lignin snippet changes an article, and the SEM setup
    snippet replaces the expanded parenthetical subject with an abbreviation. Both
    match selected cached excerpts, but neither is a contiguous fresh HTML/PDF span;
    the underlying medium claims are supported.
  target_ids:
  - CommunityMech:000383
  field_paths:
  - environmental_factors[0].evidence[0].snippet
  - cultivation_setup[0].evidence[1].snippet
  evidence_ids:
  - snippets
  - quote-locations
  - fulltext
  - root-biorxiv-pdf
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    role: canonical_record
actions:
- action_id: fix-dataset-scope
  description: Qualify assembly completeness and distinguish library genomics, enrichment
    profiling and final consortium assays.
  finding_ids:
  - dataset-scope
  target_ids:
  - CommunityMech:000383
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Identify GCF_030348465.1, GCF_030348595.1, GCF_030348625.1 and GCF_030487755.1
    as current Contig assemblies; preserve the other seven Complete Genome records.
  - Retain the publication wording as source-attributed rather than treating it as
    current assembly-level certification.
  - Describe PRJNA1505615 as top-down enrichment biofilm profiling, with its actual
    source method.
  - Keep 121 as the reported library size, not an independently enumerated repository
    inventory.
  - Preserve all eleven verified strain links and run strict and reference checks.
- action_id: fix-assay-precision
  description: Describe the plotted growth proxy and distinguish phenolic mean differences
    from statistically supported contrasts.
  finding_ids:
  - assay-precision
  target_ids:
  - CommunityMech:000383
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Use cumulative OD-AUC for Figure 5B rather than direct biomass mass or final yield.
  - State that full/dropout/11B phenolic means share statistical letters; retain the
    significant full-versus-uninoculated contrast.
  - Preserve the numerical mean direction and bounded 11B contribution interpretation
    without declaring 11B irrelevant.
  - Keep indirect chemistry, nonexclusive roles and absence of downstream arrows.
  - Run strict, reference and network checks.
- action_id: fix-fresh-snippets
  description: Replace the two snippets with source-exact spans and retain versioned
    fresh-source provenance during a separately authorized curation.
  finding_ids:
  - fresh-snippets
  target_ids:
  - CommunityMech:000383
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    role: canonical_record
  acceptance_checks:
  - Use Methods sec-3 and sec-10, corroborated by PDF lines 122-123 and 225-227.
  - Do not alter supported lignin concentration or SEM conditions to resolve a quotation
    defect.
  - Keep any refreshed cache provenance distinct from the historical selected-excerpt
    cache.
  - Confirm every repaired snippet against the fresh source as well as native reference
    validation.
limitations:
- The source is bioRxiv version 1. Current API metadata lists no newer version and
  published NA; this is not an exhaustive search for later journal publication. Peer
  review is not implied.
- Complete main text and candidate Table 1 were available. Highwire table and supplement
  endpoints returned HTTP 429; the PDF resolved Table 1. The root reviewer could not
  read the rendered supplementary Figure S5 quantitatively, and no supplementary raw
  measurements were reanalyzed.
- The source general M9 recipe has missing formula subscripts, inconsistent glucose-stock
  versus explicit liquid percentages, and inconsistent Mg/Ca molarity versus mass
  values. Retain the explicit supported liquid conditions without silently reconstructing
  a recipe.
- The publication describes 11B as isolated from a worker termite head, while current
  BioSample metadata says fresh fungus comb. The record does not encode that origin;
  retain the discrepancy if origin is later curated rather than treating it as a current
  record defect.
- Both committed caches contain selected excerpts. Their 31 matches do not establish
  fresh-source quotation fidelity; two spans require repair while their biological
  claims remain supported.
- Archive checks cover the eleven encoded assemblies/BioSamples and two projects,
  not full project enumeration, genome completeness analysis or raw Nanopore reads.
  The project metadata lacks publication fields; paper linkage is supplied by the
  primary source.
- Pinned code and three selected workbooks were inspected without execution. Proteomic
  contributions are not cell abundances, enzyme annotations are candidates, and a
  PRIDE placeholder is not a verified raw mass-spectrometry accession.
- Historical GTDB crosswalk unavailability was not promoted to a current global absence
  claim. No mapping was recomputed; optional structured-adapter discovery was reused
  with its original bounded scope.
notes:
- Canonical records, caches, history and generated outputs remain unchanged.
- Direct excerpts total 16 words for the preprint and its supplements combined.
- All source input hashes are inherited from the successful official inspect and rechecked
  before candidate construction.
tags:
- record-review
- synthetic-community
- lignin
- bacillales
- batch-04
```
