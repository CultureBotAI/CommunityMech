# Algal–methanotroph biogas coculture: current-main review successor

- Review: 20261105T223023Z-pr2035-algal-methanotroph-successor
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-05T22:26:12.602813Z
- Finished UTC: 2026-11-05T22:30:23.327619Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current record adds Leptolyngbya to the qualified community-level oxygen-support node, resolving the predecessor's disconnected-member observation. Four prior curation findings remain. New findings identify an incorrect append-only history event and explicitly track omitted source-supported assay conditions. Two major, three minor and one informational findings remain open. Eight focused/preflight gates pass; corpus network warnings retain their actual nonzero exits.

## Scope And Provenance

Whole target: six selected taxa, two nodes, no arrows, evidence, engineering, environment, cultivation, publication/dataset metadata and history.

Selection: PR2035 staleness refresh: current origin/main target differs from the predecessor only by Leptolyngbya participation and embedded history. All six taxa, both nodes, no arrows, source claims and five history files were reassessed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 5719f60dc7e98a3329326e4e53bd54c06f8d1ab7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000415 | kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml | maintained | Algal-Methanotroph Biogas Valorization Coculture |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000415 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml |
| validate-strict | passed | True | CommunityMech:000415 | uv run python scripts/validate_strict.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv<br>Validating 1 files with 17 workers; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv |
| validate-terms | passed | True | CommunityMech:000415 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000415 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000415 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml |
| validate-history | passed | True | CommunityMech:000415 | No issues found |
| normalize-cache-names-check | passed | True | CommunityMech:000415 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000415 | Validating kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000415 | Actual fresh corpus run:503 records,44 warnings in16 records,0 errors; exit1 retained. This target has no warnings. No corpus remediation is authorized by this review. |
| check-network-quality | failed | True | CommunityMech:000415 | Actual fresh corpus run:503 records,44 warnings in16 records,0 errors; exit1 retained. This target has no warnings. No corpus remediation is authorized by this review. |
| Structured expression-source applicability | not_applicable | False | CommunityMech:000415 | No strain-specific regulatory assertion is curated; no adapter execution or current catalog absence is claimed. |

## Scientific And Domain Assessments

### Mixed enrichment identity and provenance

identity: supported. Targets: CommunityMech:000415.

The source, publication IDs and BioProject denote the same engineered laboratory coculture. The record preserves non-axenic enrichment origins and should not be read as six isolated strains or a natural ecosystem.

### taxonomy[0..5], abundance and roles

grounding: concern. Targets: CommunityMech:000415.

All six identities verify at the curated ranks. Abundance statements retain the appropriate guild-level denominators in their explanations; the total methanotroph percentage is not assigned solely to one genus. Roles require more care: complex-substrate degradation is not methane oxidation, and unqualified CROSS_FEEDER tags exceed the explicitly hypothetical exchange node.

### ecological_interactions[0]: Photosynthetic O2 Support for Methane Oxidation

graph: supported. Targets: CommunityMech:000415.

The PARTIAL node correctly distinguishes observed gas dynamics from inferred oxygen support after startup supplementation. It does not assert partner-resolved transfer or reciprocal fitness.

Participants are Chlorella vulgaris, Dunaliella viridis, Leptolyngbya and Methylotuvimicrobium. Source sections2.3/2.3.1 support detected phototrophic membership; the PARTIAL node retains community-scale inferred oxygen support. No donor-resolved oxygen flux, reciprocal fitness or new causal arrow is established.

### ecological_interactions[1]: Methane-Linked Methylotroph Cross-Feeding

graph: supported. Targets: CommunityMech:000415.

The HYPOTHESIZED node accurately limits the proposed one-carbon exchange. Source physiology and taxon abundance support plausibility, not measured methanol transfer or detoxification.

Participants: Methylotuvimicrobium as candidate donor, Methylophaga and Methylonatrum as candidate recipients, within a community-level node. Mechanism: proposed methanol/other one-carbon use; no direct flux or reciprocal benefit established. Source PMID 41745484 section 2.3.1, exact short quote in exchange. Gene abundance is not pathway activity.

### ecological_interactions[*].downstream

graph: not_applicable. Targets: CommunityMech:000415.

No downstream arrows occur in the complete target. Bulk gas removal, product accumulation and proposed exchange do not establish an ordered causal chain between the two nodes.

### Environment, engineering design, factors and metal relevance

scope: supported. Targets: CommunityMech:000415.

Laboratory environment, engineered origin and biotechnology category fit the source. The main assay and comparator design are correctly distinguished from source enrichments. The metal designation concerns the absence of a metal-processing ecological role, not absence of mineral medium constituents.

### growth_media and cultivation_setup

provenance: concern. Targets: CommunityMech:000415.

The represented assay details match Methods/Table 1. The illumination evidence locator comes from inoculum preparation despite a matching final-assay value in Table 1. Exact external medium links remain absent; no verified formulation match is assumed. Additional reported conditions could be represented in later curation, without treating absence as an invalid experiment.

### description, related_ingredients[2] and functional roles

evidence: concern. Targets: CommunityMech:000415.

The graph and discussion correctly qualify exchange, but the summary/oxygen-ingredient wording sounds more certain and the methylotroph role tags have no hypothesis qualifier. The source itself proposes the mechanism; consistency requires carrying its evidential limits beyond graph prose.

### Publication, dataset, snippets and history

provenance: concern. Targets: CommunityMech:000415.

Publication and BioProject identities resolve;35of36 snippets match normalized primaryXML and the DOI-labelled36th is in the bibliographic cache header. Five history files validate structurally, but the October21event's scientific identity is incorrect. Historical graph decisions and stage5 terminal status do not certify that event or this whole record.

### Structured expression-source applicability

evidence: not_applicable. Targets: CommunityMech:000415.

The target contains no strain-specific gene or regulatory assertion requiring an expression-module lookup. Source metagenomic attribution does not become a validated functional transfer through an unrelated expression dataset.

### Focused gates and native network completeness

schema: concern. Targets: CommunityMech:000415.

Eight focused/preflight gates pass and inspected canonical bytes remain unchanged. Both required corpus commands return1 for44warnings/16of503records,0errors. This target has no network issues after the Leptolyngbya participation addition; this is structural completeness, not proof of exchange.

### Native completeness and validation quality

completeness: concern. Targets: CommunityMech:000415.

Completeness90 and capped validation quality100 are rubric values, not scientific approval. Two major, three minor and one informational findings remain open; the original informational disconnected-member finding is resolved.

### Bounded correction to Stage 5's CommunityMech:000415 identity clause

provenance: concern. Targets: CommunityMech:000415.

The description of finding stage4-disconnected-syncom-participants in review 20261021T193000Z-stage5-remediation-verification incorrectly identifies the missing member of CommunityMech:000415 as Parachlorella kessleri NIES-2152, NCBITaxon:3074. The current record, original Stage 4 descriptions and primary source sections 2.3/2.3.1 instead identify Leptolyngbya, NCBITaxon:47251. This append-only correction applies only to that 000415 identity clause. The other four targets and all grouped resolved dispositions are NOT reassessed; the multi-target issue key and occurrence lineage are not superseded.

## Findings

### functional-roles: Functional-role tags exceed their support

major / open / confirmed; issue key: cm-000415-functional-roles.

Methylotuvimicrobium is tagged PRIMARY_DEGRADER, whose schema definition concerns complex substrates, while the source concerns methane oxidation. Methylophaga and Methylonatrum are tagged CROSS_FEEDER without carrying the explicit hypothesis qualification already present in their interaction node.

### oxygen-qualification: Oxygen-support certainty differs across fields

minor / open / confirmed; issue key: cm-000415-oxygen-qualification.

The description and oxygen ingredient state photosynthetic supply as established, while the carefully curated node correctly states community-level inference. This is a bounded wording inconsistency; the gas-removal endpoint itself is supported.

### light-evidence-context: Illumination evidence points to the inoculum stage

minor / open / confirmed; issue key: cm-000415-light-evidence-context.

The attached illumination quotation is from section 3.1 inoculum growth, while the explanation claims final coculture assays. Table 1 independently supports the curated assay intensity, so this is evidence placement rather than a wrong value.

### media-linkage: Medium lacks verified registry linkage

minor / open / confirmed; issue key: cm-000415-media-linkage.

The medium and gas components have CHEBI grounding where represented but no CultureMech or MediaIngredientMech link. A similarly named medium is not proof of formulation equivalence.

### unconnected-member: Leptolyngbya has no curated interaction participation

informational / resolved / confirmed; issue key: cm-000415-unconnected-member.

The predecessor observed Leptolyngbya missing from both participant lists. Current main explicitly includes Leptolyngbya47251 in the PARTIAL community-level oxygen-support node. Source sections2.3/2.3.1 report its detection and phototrophic community context. This supports bounded participation without a taxon-resolved transfer or new edge.

Disposition: Direct current-record inspection, exact target diff, source sections2.3/2.3.1 and a fresh empty target-network audit resolve this specific single-target omission. Neither the erroneous October21 external history prose nor the unrelated taxa in stage5 review prose are used as proof.

### history-provenance: October21 history event describes different taxa and record

major / open / confirmed; issue key: cm-000415-history-provenance.

The history file targets the000415slug but its event names000446, Methylocystis hirsuta, Desmodesmus abundans and a lipid-valorization node. The actual change adds Leptolyngbya47251 to000415's oxygen-support node. Schema validation does not establish history accuracy.

### assay-conditions: Track omitted final-assay cultivation conditions

informational / open / confirmed; issue key: cm-000415-assay-conditions.

The predecessor requested later cultivation enrichment without a tracked action. Methods3.2 give25degreesC and200rpm magnetic stirring; Table1 gives56days for the co-culture; Methods3.1 gives initial prepared-medium pH9. These conditions are absent from the entire current target. Later curation must distinguish initialpH from maintainedpH and final-assay magnetic stirring from150rpm orbital inoculum growth.

## Recommended Actions And Acceptance Checks

### fix-functional-roles

Use only role terms compatible with the source and schema; preserve unresolved exchange in the role evidence rather than asserting a confirmed donor-recipient function.

- No complex-substrate degradation is inferred from methane oxidation.
- Role evidence distinguishes candidate methylotrophy from demonstrated interspecies transfer.
- Run strict, reference and network checks.

### fix-oxygen-qualification

Carry the same inferential qualification into summary and ingredient statements.

- Measured gas removal remains distinct from inferred oxygen transfer.
- No taxon-resolved flux or reciprocal fitness is asserted.
- Run strict and reference checks.

### fix-light-evidence-context

Cite the final-assay table for the existing condition, preserving distinct inoculum and reactor stages.

- The evidence locator and explanation concern the same assay.
- Do not derive other assay conditions from inoculum preparation.
- Run reference and strict checks.

### fix-media-linkage

Assess exact registry compatibility in later authorized curation; leave uncertain matches unresolved.

- Any identifier resolves to the same formulation/context.
- Do not substitute a convenient differently formulated medium.
- Run relevant linkage and strict checks.

### correct-history-append-only

Create a new append-only history correction that identifies the erroneous prior event and documents the actual Leptolyngbya addition to000415; preserve the old entry unchanged.

- Correction matches the actual Git diff, source scope and embedded history.
- No historical event is rewritten.
- Run history and strict validators.

### curate-assay-conditions

Represent supported final-assay temperature, stirring and duration, and initial medium pH with exact source evidence and experimental-stage qualifiers.

- 25degreesC/200rpm magnetic stirring/56days are scoped to final co-culture assay.
- pH9 is initial prepared-medium pH, not a claimed controlled trajectory.
- Do not import150rpm orbital inoculum conditions; run strict/reference validation and append history.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml; Entire target: six taxa, two nodes, no arrows, all metadata and evidence | supports | Mixed enrichment assembled from non-axenic algal and methanotrophic inocula; six selected taxa are not an exhaustive or axenic six-member synthetic community. |
| primary | PMID:41745484; Fresh Europe PMC XML: PMID41745484/PMC12941554/doi10.3390/md24020081; Results2.1–2.3 and Methods3.1–3.4, Table1 read in full; public XML retrieval receipt and bytes frozen. | supports | Read full Results/Discussion and Methods from retrieved primary XML, including reactor comparisons, gas dynamics, product measurements, metagenomic attribution and BioProject statement. The measured community endpoints do not trace exchange between individual taxa. |
| gas | PMID:41745484; Section 2.1, coculture gas dynamics | supports | Community methane consumption followed startup oxygen additions. The authors infer ongoing photosynthetic support; taxon-resolved oxygen transfer and reciprocal fitness were not measured. |
| exchange | PMID:41745484; Section 2.3.1, methylotrophic guild | supports | The paper proposes exchange from metagenomic composition and established physiology, with a literature citation. It does not quantify donor-to-recipient methanol flux or demonstrate detoxification in this culture. |
| methods | PMID:41745484; Section 3.4, composition and functional attribution | supports | Taxon composition and gene/pathway associations are sequencing-based. They should not be confused with direct functional measurements on each named organism. |
| publication | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=41745484&amp;retmode=xml; Retrieved public identity metadata | supports | PubMed returns the matching title, PMID 41745484, PMCID PMC12941554 and DOI 10.3390/md24020081. |
| dataset | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=bioproject&amp;id=1369521&amp;retmode=json; Retrieved public identity metadata | supports | NCBI resolves PRJNA1369521 as the extremophile methanotrophic-algal coculture metagenome project for biogas valorization. Metadata agrees with the primary paper; raw sequences were not downloaded or reanalyzed. |
| composition | PMID:41745484; Sections 2.3 and 2.3.1; taxonomic abundance denominators | supports | Chlorella and Dunaliella percentages refer to Chlorophyta, Leptolyngbya to the bacterial fraction, and the two methylotroph percentages to the methylotroph fraction. The 9.1% value describes the whole methanotroph guild, not Methylotuvimicrobium alone; the record explanation correctly says so. Its coarse abundance classes must not be treated as absolute cell fractions. |
| cultivation | PMID:41745484; Sections 3.1–3.2, Table 1, and section 2.1 | supports | The mixed-inoculum reactor design, initial gas feed and startup intervention match the record. Table 1 is the appropriate light-intensity evidence for the coculture assay; the quoted light sentence currently attached to it is from inoculum preparation. The primary Methods also give additional structured conditions absent from the record. Final assays used25 degrees C and200rpm magnetic stirring; Table1 reports56days; the prepared MSM was adjusted to initialpH9. These are distinct from150rpm orbital inoculum growth. |
| ontology | OAK local NCBITaxon, ENVO, GO and CHEBI snapshots; 13 unique identifiers, including six taxa | supports | Every curated identifier and canonical label resolves. Eukaryotic algae correctly declare no GTDB equivalent; bacterial genus mappings remain explicitly unresolved. Process terms fit broad photosynthesis/methane metabolism without proving organism-specific activity. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum and EvidenceSourceEnum | supports | PRIMARY_DEGRADER denotes degradation of complex substrates, while methane is a one-carbon substrate. CROSS_FEEDER denotes use of another taxon’s metabolites. IN_VITRO includes bioreactor experiments; it is not by itself a claim that all taxon functions were directly measured. |
| snippets | kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml; All 36 EvidenceItem occurrences | supports | 35 snippets match the primary XML after NFKC/whitespace normalization with inline XML tags concatenated. The DOI-labelled snippet is present in the PubMed-formatted cache header; the identifier independently verifies in PubMed and article metadata. No substantive quote mismatch was established. |
| history | history/records/Algal_Methanotroph_Biogas_Valorization_Coculture; Five append-only history files plus embedded history and the prior graph decision | supports | The four older entries describe creation and gas/light, dangling-edge and uncertainty repairs. The October21 external event is misattributed: it names record000446, Methylocystis/Desmodesmus and a lipid node, while the actual current target change adds Leptolyngbya to 000415's oxygen-support node. Embedded history matches the actual change. Do not use the erroneous external prose to certify the target. |
| local-search | references_cache; history/records; reports/causal_graph_review/decisions; kb/taxa; Ignored-inclusive PMID, accession and slug search | supports | Located source cache, history and decision. Missing medium identifiers are absent from the entire target; no claim is made that a matching external registry record does not exist. |
| adapter | kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml; All taxon and interaction assertions; applicability assessment only | context_only | No strain-specific regulatory assertion or expression-module claim is curated. An expression-source lookup is not required for the actual community gas, metagenomic abundance and inferred exchange assertions; no current catalog search or dataset absence is claimed. |
| predecessor | reviews/structured/20261020T065737Z-algal-methanotroph-record/review.yaml; All five prior findings, four actions, whole-record assessments and frozen target | supports | Every predecessor finding is rechecked. Stable issue keys and exact finding occurrence references are retained; only the single-target disconnected-member observation is resolved. |
| target-diff | .temp/pr2035/415/target-diff.stdout.txt; Exact target diff from predecessor base to current HEAD | supports | Only Leptolyngbya47251 participation in node0 and the embedded October21 event changed. The previously flagged role, wording, evidence-locator and media-linkage fields are unchanged. |
| target-network | .temp/pr2035/415/target-network.json; NetworkIntegrityAuditor.audit_community on the current entire target | supports | No target network issues. Every curated member occurs in a community-level participant list; this structural result does not demonstrate partner-specific exchange. |
| history-mismatch | history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-21T190000Z-claude-2048.yaml; events[0].summary and events[0].details versus target path, current diff and embedded history | supports | The external event claims two different taxa, CommunityMech000446 and a different node, while the exact diff shows Leptolyngbya in record000415. It needs an append-only correction, not rewriting the old event. |
| stage5-context | reviews/structured/20261021T193000Z-stage5-remediation-verification/review.yaml; finding stage4-disconnected-syncom-participants description; context only | context_only | The preexisting multi-target finding describes000415 using Parachlorella kessleri NIES-2152/3074, inconsistent with both current target and primary source Leptolyngbya47251. Its terminal status is not used as scientific proof. This one-target successor does not retire or adjudicate that multi-target issue key. |
| check-validate | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml; Actual execution 2026-11-05T22:26:35.529934Z to 2026-11-05T22:26:36.245306Z; receipt .temp/pr2035/415/validate.json | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml |
| check-validate-strict | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-strict kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv; Actual execution 2026-11-05T22:26:36.245520Z to 2026-11-05T22:26:41.100782Z; receipt .temp/pr2035/415/validate-strict.json | supports | uv run python scripts/validate_strict.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv<br>Validating 1 files with 17 workers; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv |
| check-validate-terms | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-terms kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml; Actual execution 2026-11-05T22:26:41.100960Z to 2026-11-05T22:26:42.404514Z; receipt .temp/pr2035/415/validate-terms.json | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-gtdb kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml; Actual execution 2026-11-05T22:26:42.404732Z to 2026-11-05T22:26:42.472103Z; receipt .temp/pr2035/415/validate-gtdb.json | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-gtdb-domain kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml; Actual execution 2026-11-05T22:26:42.472268Z to 2026-11-05T22:26:43.470743Z; receipt .temp/pr2035/415/validate-gtdb-domain.json | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml |
| check-validate-history | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-history history/records/Algal_Methanotroph_Biogas_Valorization_Coculture; Actual execution 2026-11-05T22:26:43.470915Z to 2026-11-05T22:26:44.055841Z; receipt .temp/pr2035/415/validate-history.json | supports | No issues found |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-11-05T22:26:44.056017Z to 2026-11-05T22:26:44.095805Z; receipt .temp/pr2035/415/normalize-cache-names-check.json | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-references-explained kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml; Actual execution 2026-11-05T22:26:44.096040Z to 2026-11-05T22:26:45.656006Z; receipt .temp/pr2035/415/validate-references-explained.json | supports | Validating kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv audit-network; Actual execution 2026-11-05T22:26:45.656204Z to 2026-11-05T22:26:50.632106Z; receipt .temp/pr2035/415/audit-network.json | supports | Actual fresh corpus run:503 records,44 warnings in16 records,0 errors; exit1 retained. This target has no warnings. No corpus remediation is authorized by this review. |
| check-check-network-quality | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv check-network-quality; Actual execution 2026-11-05T22:26:50.632341Z to 2026-11-05T22:26:55.290119Z; receipt .temp/pr2035/415/check-network-quality.json | supports | Actual fresh corpus run:503 records,44 warnings in16 records,0 errors; exit1 retained. This target has no warnings. No corpus remediation is authorized by this review. |

## Limits And Additional Notes

- Primary Results/Discussion and Methods were freshly read from XML; separate supplements and raw metagenomic data were not reanalyzed.
- Shotgun taxonomic/gene attribution is not a direct measurement of taxon-resolved transfer, pathway activity or reciprocal fitness.
- BioProject metadata verifies project identity, not every sample accession or sequencing result.
- Bacterial GTDB assignments remain explicitly unresolved; coherence gates do not establish new mappings.
- Current reference validator coverage does not certify every assertion's source scope; direct36snippet replay complements it.
- Corpus network warning failures are retained explicitly. No out-of-scope canonical remediation was performed.
- The preexisting stage5 multi-target review misidentifies000415's member; this one-target successor explicitly excludes that prose from its scientific proof and does not adjudicate its multi-target lineage.
- Immutable successor to the stale PR2035review; original review bytes retained.
- Current record changed only in participant membership and embedded history; frozen input hashes and new receipts reflect current main.
- Scientific source scope and all five original findings were independently reconsidered by the author; independent adversarial approval remains a separate pass.
- No canonical records, source caches, history entries or generated products were changed by this refresh.
- Three brief source quotes inherited after fresh verification total fewer than25words; new claims are paraphrased with section locators.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T223023Z-pr2035-algal-methanotroph-successor
kind: record
repository: CultureBotAI/CommunityMech
title: 'Algal–methanotroph biogas coculture: current-main review successor'
started_at: '2026-11-05T22:26:12.602813Z'
finished_at: '2026-11-05T22:30:23.327619Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Author refresh of the stale PR2035 bundle; independent adversarial
    approval is a separate pass. Historical Codex curation prevents person-level independence
    claims.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Current record adds Leptolyngbya to the qualified community-level oxygen-support
  node, resolving the predecessor's disconnected-member observation. Four prior curation
  findings remain. New findings identify an incorrect append-only history event and
  explicitly track omitted source-supported assay conditions. Two major, three minor
  and one informational findings remain open. Eight focused/preflight gates pass;
  corpus network warnings retain their actual nonzero exits.
source:
  git_revision: 5719f60dc7e98a3329326e4e53bd54c06f8d1ab7
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
  - path: .temp/pr2035/415/audit-network.json
    sha256: 6aaf209f549963162edf13cf188eaf3b5c0694a08dca9f9f0890568f795d6871
    role: context
  - path: .temp/pr2035/415/audit-network.stderr.txt
    sha256: a71fb29e950f3eaf0eb2b834a43c59d4a1b6aa85a2a89473ae99b0e408a27a36
    role: context
  - path: .temp/pr2035/415/audit-network.stdout.txt
    sha256: f5dc190f832300fc5a73fcf3e7e8e3cd53d560ba09b17179ce6c7fcc8aa022e8
    role: context
  - path: .temp/pr2035/415/bioproject.json
    sha256: 5f3b7a667ac6a974b37755b99bc8901efdb8e916f4af2103bf4358677a664a55
    role: context
  - path: .temp/pr2035/415/check-network-quality.json
    sha256: c27ea52c3936e32a9d5fce4650e09e5e91291d7966051d022c8654fec8d22d2f
    role: context
  - path: .temp/pr2035/415/check-network-quality.stderr.txt
    sha256: f9a8e9fb5a4e4ea545236a809393dbc1ce4325b14579c65a3130bcfe713e798a
    role: context
  - path: .temp/pr2035/415/check-network-quality.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/fetch-bioproject.json.json
    sha256: 1cb37af68825f571e3cac9dae38beb50e6cb6949f9b26d2e063cec785bb9f5e0
    role: context
  - path: .temp/pr2035/415/fetch-bioproject.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/fetch-bioproject.json.stdout.txt
    sha256: 5f3b7a667ac6a974b37755b99bc8901efdb8e916f4af2103bf4358677a664a55
    role: context
  - path: .temp/pr2035/415/fetch-primary.xml.json
    sha256: d20304d9dc6b5296fb765bf4c9a2a3071b359dfc12e8d47ced078c03f87b8907
    role: context
  - path: .temp/pr2035/415/fetch-primary.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/fetch-primary.xml.stdout.txt
    sha256: 614c2550f02285471c58610c17bb9d6c44a2e08dc1ece608d7b0c0314a5d9f57
    role: context
  - path: .temp/pr2035/415/fetch-publication.xml.json
    sha256: d0f3f8ac0f97dabc6057dac5198103cbe2b993d03a0f06b9787d22683427c944
    role: context
  - path: .temp/pr2035/415/fetch-publication.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/fetch-publication.xml.stdout.txt
    sha256: c5d6bbe116fcb9bac874c6cc14dc07c270bba0652cfeb95bf662da3241c1ea0d
    role: context
  - path: .temp/pr2035/415/inspect.json
    sha256: 895717241df27a8c2b845c51a93d8e21718908e087196bb6769a0daf0e9cedbb
    role: context
  - path: .temp/pr2035/415/inspect.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/inspect.stdout.txt
    sha256: 18355a3c8d910441b8c47fe074c21930da20635a8e22ede15762bb7e4939a27f
    role: context
  - path: .temp/pr2035/415/inspection.json
    sha256: 18355a3c8d910441b8c47fe074c21930da20635a8e22ede15762bb7e4939a27f
    role: context
  - path: .temp/pr2035/415/lineage.json
    sha256: 12eef7bb6071c86dadd905531a9d5988665701c365b9f56a8d60fc7640ebc3c0
    role: context
  - path: .temp/pr2035/415/local-search-v2.json
    sha256: 4ec1ca3d9fb056a0d218e4398deeba45681e68470f1034c68b19cf147a6936b0
    role: context
  - path: .temp/pr2035/415/local-search-v2.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/local-search-v2.stdout.txt
    sha256: a2347ddff47ada167c08ac2b672c1f386acd2e0d163ab2f1fcada53361132d6e
    role: context
  - path: .temp/pr2035/415/local-search.json
    sha256: e408f904949b2405d5483e2b905042602600d3f72ee5e70cd58bae9f4aee16bd
    role: context
  - path: .temp/pr2035/415/local-search.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/local-search.stdout.txt
    sha256: a9e2dc933f596c4f480bb0134bfef68e5a43dd68afb9f091234f13e9a691ea34
    role: context
  - path: .temp/pr2035/415/normalize-cache-names-check.json
    sha256: f4d856187e6a791aa896ba00524fce6065e0f12cfed01c418c4e67022035c5e7
    role: context
  - path: .temp/pr2035/415/normalize-cache-names-check.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/normalize-cache-names-check.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/ontology-authorities.json
    sha256: cff704b485c2e94ce29ea7727ff65142bc0f1b6de96126c6dcc4fe093b891500
    role: context
  - path: .temp/pr2035/415/primary-sections.json
    sha256: a1372b53819059fec54cd438e8b46a27f307f5cb3cc0b1ccd36bbe680e137cdf
    role: context
  - path: .temp/pr2035/415/primary.xml
    sha256: 614c2550f02285471c58610c17bb9d6c44a2e08dc1ece608d7b0c0314a5d9f57
    role: context
  - path: .temp/pr2035/415/publication.xml
    sha256: c5d6bbe116fcb9bac874c6cc14dc07c270bba0652cfeb95bf662da3241c1ea0d
    role: context
  - path: .temp/pr2035/415/snippet-replay.json
    sha256: 37a102b0e1b11e8020920917cdc0c20e48c6261c21cf770fa9f6b969e03e7af8
    role: context
  - path: .temp/pr2035/415/sources.json
    sha256: 84c0d81d0a1f07381550d28d7fe6556dc3b151c342fe7cfd5dd0b59dbe8c464b
    role: context
  - path: .temp/pr2035/415/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/pr2035/415/target-diff.json
    sha256: 2806258158c13ee86b1ab6514c9a945ae4c14de32bbac024e4d6e93d20c47f83
    role: context
  - path: .temp/pr2035/415/target-diff.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/target-diff.stdout.txt
    sha256: f068f118edd9b19db5e3f667cb83f587943b8d8984355001cc8fef43f114783a
    role: context
  - path: .temp/pr2035/415/target-network.json
    sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
    role: context
  - path: .temp/pr2035/415/targets.json
    sha256: 95baed3e9532ac3a472c8c01b7456b2f3753926d569084448f5a3b5ce91d3c78
    role: context
  - path: .temp/pr2035/415/validate-gtdb-domain.json
    sha256: 4ec79efbe04e635a6ce924c7b13da6fe80a8bc235755830e6d5595a8a9b210da
    role: context
  - path: .temp/pr2035/415/validate-gtdb-domain.stderr.txt
    sha256: 64c03576f70ddabf12f780b4b46432bf626b3dd8022444be04c07d16512f782e
    role: context
  - path: .temp/pr2035/415/validate-gtdb-domain.stdout.txt
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2035/415/validate-gtdb.json
    sha256: ba2db006c22d68b1baff4d5700719714c53ecea659f689563a88b16f212ab9bf
    role: context
  - path: .temp/pr2035/415/validate-gtdb.stderr.txt
    sha256: af0ff24b2bb94a57a126eb213ed3c9f89de66d409220f237100377dcc8c6db0f
    role: context
  - path: .temp/pr2035/415/validate-gtdb.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/validate-history.json
    sha256: e0a36b624183ba924b3a20f0b8abf31ea010e6de34bb56bdce2bce381695ab9c
    role: context
  - path: .temp/pr2035/415/validate-history.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/validate-history.stdout.txt
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2035/415/validate-references-explained.json
    sha256: ce51a52add0029b0a148a5539db987e53e0a51fb8032e9eef0c4de9719b203aa
    role: context
  - path: .temp/pr2035/415/validate-references-explained.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/validate-references-explained.stdout.txt
    sha256: 10e1a2d376d17d3c71b961c658007a8a6f88e872365111f8781e07c8ec3ac80e
    role: context
  - path: .temp/pr2035/415/validate-strict.json
    sha256: ccefc261b60722b6e97645c655c164afcd09528fb1af16b74ece7c9884cb10c9
    role: context
  - path: .temp/pr2035/415/validate-strict.stderr.txt
    sha256: 6ac056580ede0f44a6757ecf93365493f1db2ba149e300afb813318ebac71797
    role: context
  - path: .temp/pr2035/415/validate-strict.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2035/415/validate-terms.json
    sha256: c7eac3f25a8ce0cf93fbf4114d519f88af7e1cbe223d1553881f5e089b671856
    role: context
  - path: .temp/pr2035/415/validate-terms.stderr.txt
    sha256: 87d6373fc14d7c25d87e55a7464a6ef6e120258eb28fc3f32a292cea2b219184
    role: context
  - path: .temp/pr2035/415/validate-terms.stdout.txt
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2035/415/validate.json
    sha256: 0a055dc029fd57373f2c1b8fd0b9a37d0a95dd9e0ebbcb7628a6dce41dc26d57
    role: context
  - path: .temp/pr2035/415/validate.stderr.txt
    sha256: ef781ea131bd356760c4b5250b41648d6f0516af41fa357a5828e533f7450a2c
    role: context
  - path: .temp/pr2035/415/validate.stdout.txt
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: AGENTS.md
    sha256: 8f23dcad7ed9c9873f00058995d1219cca8810c27ed5d787cb9b66a8abf96728
    role: context
  - path: conf/record_review.yaml
    sha256: c4ad25505a87a040c57eb93f1ee9673a09389a474c6d4e1136781456ff190fc8
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
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-09-22T021817Z-codex-f1f2c6.yaml
    sha256: 9bfc08ee8935ee656496cef83e96ea5fc7ee6ade7edaa4cb863f561e24fd6f43
    role: context
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-09-22T022344Z-codex-42bb96.yaml
    sha256: 87094b42b79ea0b6824dbbba9a93238c5fe8ddceb4c92ff75a9fd87ecce4f9cc
    role: context
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-09-22T023024Z-codex-7b6bb4.yaml
    sha256: 5144011707902c422b278db5147111dd9a9fbe2ad4bd9ca817e0557407bc5e7b
    role: context
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-05T084241Z-codex-0a0de5.yaml
    sha256: 986118826596e140971dbae607a5d01293023f3f0120eb6752a3f8e6740584b1
    role: context
  - path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-21T190000Z-claude-2048.yaml
    sha256: 6daeecaecb30693d966d470d6d1324726d1bcc32d45e232157cc27b68d0c4b46
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    sha256: d317416542deab471a12785f688c23d08ed5a7eea2894dbde489f40c0df80806
    role: target
  - path: references_cache/PMID_41745484.txt
    sha256: ad543c6e92b26ff25763f25f499719f0075bdfe85af9d006b20ae5865f50b9ae
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
    sha256: e21a355f676730e8e7e6de6ea663017c9b09e05a824ff383a272ab9f1399fd70
    role: context
  - path: reviews/structured/20261020T065737Z-algal-methanotroph-record/review.yaml
    sha256: 455dbf1ddc34124a9f5f995f2b115e6a07eb85dda6c9b40ac7f1255a1842419f
    role: context
  - path: reviews/structured/20261021T101000Z-stage4-record-deep-audit/review.yaml
    sha256: f32db16fda535e46adee4bd7d8d2de5c3f206dc7fdb892d137e1fe00e3346b59
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.yaml
    sha256: 37d089fd55c077793dd20d868b50c47cb1cceab6dae6a82887cc938bee05fa6d
    role: context
  - path: reviews/structured/20261021T193000Z-stage5-remediation-verification/review.yaml
    sha256: 8f8f980813203a0336e27f0bc0a3c3b6e68bb68c2f2a7d71460183f4fe3bbc09
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/pr2035_415_audit.py
    sha256: d9d5fb1c688c53c76d29dbc71f6a3235c63d93032870a0451e2eecb492a46184
    role: context
  - path: scripts/adhoc/pr2035_415_review.py
    sha256: b99e4e36b89864d1a9c4074bc154b5663c1d44f316f59d9fb01e0d54982ada1b
    role: context
  - path: scripts/record_review.py
    sha256: 95a4ec41e38ec47ba3578e76838c46a0adbf47e49ad3636524735d08cfcb1c4d
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/ontology_adapters.py
    sha256: bb3803581ac2946b2ca8e14278e36cd660faf12db9237f9688a6cef577fa9016
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000415
  path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  label: Algal-Methanotroph Biogas Valorization Coculture
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
scope:
  description: 'Whole target: six selected taxa, two nodes, no arrows, evidence, engineering,
    environment, cultivation, publication/dataset metadata and history.'
  selection: 'PR2035 staleness refresh: current origin/main target differs from the
    predecessor only by Leptolyngbya participation and embedded history. All six taxa,
    both nodes, no arrows, source claims and five history files were reassessed.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000415
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml'
  target_ids:
  - CommunityMech:000415
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Corpus-level existing warnings retained; focused target gates have no
    failures. Reference validation followed clean cache-name preflight and all inspected
    canonical input bytes remain unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml\
    \ --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv\n\
    Validating 1 files with 17 workers; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv"
  target_ids:
  - CommunityMech:000415
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-strict kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Corpus-level existing warnings retained; focused target gates have no
    failures. Reference validation followed clean cache-name preflight and all inspected
    canonical input bytes remain unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000415
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-terms kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Corpus-level existing warnings retained; focused target gates have no
    failures. Reference validation followed clean cache-name preflight and all inspected
    canonical input bytes remain unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000415
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-gtdb kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Corpus-level existing warnings retained; focused target gates have no
    failures. Reference validation followed clean cache-name preflight and all inspected
    canonical input bytes remain unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml'
  target_ids:
  - CommunityMech:000415
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-gtdb-domain kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Corpus-level existing warnings retained; focused target gates have no
    failures. Reference validation followed clean cache-name preflight and all inspected
    canonical input bytes remain unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: No issues found
  target_ids:
  - CommunityMech:000415
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-history history/records/Algal_Methanotroph_Biogas_Valorization_Coculture
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Corpus-level existing warnings retained; focused target gates have no
    failures. Reference validation followed clean cache-name preflight and all inspected
    canonical input bytes remain unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Command completed without reported issues.
  target_ids:
  - CommunityMech:000415
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Corpus-level existing warnings retained; focused target gates have no
    failures. Reference validation followed clean cache-name preflight and all inspected
    canonical input bytes remain unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: "Validating kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000415
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-references-explained kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Corpus-level existing warnings retained; focused target gates have no
    failures. Reference validation followed clean cache-name preflight and all inspected
    canonical input bytes remain unchanged.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: Actual fresh corpus run:503 records,44 warnings in16 records,0 errors;
    exit1 retained. This target has no warnings. No corpus remediation is authorized
    by this review.
  target_ids:
  - CommunityMech:000415
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Corpus-level existing warnings retained; focused target gates have no
    failures. Reference validation followed clean cache-name preflight and all inspected
    canonical input bytes remain unchanged.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: Actual fresh corpus run:503 records,44 warnings in16 records,0 errors;
    exit1 retained. This target has no warnings. No corpus remediation is authorized
    by this review.
  target_ids:
  - CommunityMech:000415
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Corpus-level existing warnings retained; focused target gates have no
    failures. Reference validation followed clean cache-name preflight and all inspected
    canonical input bytes remain unchanged.
- check_id: optional-adapter
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: No strain-specific regulatory assertion is curated; no adapter execution
    or current catalog absence is claimed.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  locator: 'Entire target: six taxa, two nodes, no arrows, all metadata and evidence'
  summary: Mixed enrichment assembled from non-axenic algal and methanotrophic inocula;
    six selected taxa are not an exhaustive or axenic six-member synthetic community.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: d317416542deab471a12785f688c23d08ed5a7eea2894dbde489f40c0df80806
- evidence_id: primary
  kind: primary_source
  reference: PMID:41745484
  locator: 'Fresh Europe PMC XML: PMID41745484/PMC12941554/doi10.3390/md24020081;
    Results2.1–2.3 and Methods3.1–3.4, Table1 read in full; public XML retrieval receipt
    and bytes frozen.'
  summary: Read full Results/Discussion and Methods from retrieved primary XML, including
    reactor comparisons, gas dynamics, product measurements, metagenomic attribution
    and BioProject statement. The measured community endpoints do not trace exchange
    between individual taxa.
  support: supports
  accessed_at: '2026-11-05T22:26:22.631360Z'
  snapshot_sha256: 614c2550f02285471c58610c17bb9d6c44a2e08dc1ece608d7b0c0314a5d9f57
- evidence_id: gas
  kind: primary_source
  reference: PMID:41745484
  locator: Section 2.1, coculture gas dynamics
  summary: Community methane consumption followed startup oxygen additions. The authors
    infer ongoing photosynthetic support; taxon-resolved oxygen transfer and reciprocal
    fitness were not measured.
  support: supports
  accessed_at: '2026-11-05T22:26:22.631360Z'
  quote: functionally self-sustaining state
  snapshot_sha256: 614c2550f02285471c58610c17bb9d6c44a2e08dc1ece608d7b0c0314a5d9f57
- evidence_id: exchange
  kind: primary_source
  reference: PMID:41745484
  locator: Section 2.3.1, methylotrophic guild
  summary: The paper proposes exchange from metagenomic composition and established
    physiology, with a literature citation. It does not quantify donor-to-recipient
    methanol flux or demonstrate detoxification in this culture.
  support: supports
  accessed_at: '2026-11-05T22:26:22.631360Z'
  quote: suggesting a tightly coupled metabolic interaction
  snapshot_sha256: 614c2550f02285471c58610c17bb9d6c44a2e08dc1ece608d7b0c0314a5d9f57
- evidence_id: methods
  kind: primary_source
  reference: PMID:41745484
  locator: Section 3.4, composition and functional attribution
  summary: Taxon composition and gene/pathway associations are sequencing-based. They
    should not be confused with direct functional measurements on each named organism.
  support: supports
  accessed_at: '2026-11-05T22:26:22.631360Z'
  quote: Shotgun metagenomics analysis
  snapshot_sha256: 614c2550f02285471c58610c17bb9d6c44a2e08dc1ece608d7b0c0314a5d9f57
- evidence_id: publication
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=41745484&retmode=xml
  locator: Retrieved public identity metadata
  summary: PubMed returns the matching title, PMID 41745484, PMCID PMC12941554 and
    DOI 10.3390/md24020081.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: c5d6bbe116fcb9bac874c6cc14dc07c270bba0652cfeb95bf662da3241c1ea0d
- evidence_id: dataset
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=bioproject&id=1369521&retmode=json
  locator: Retrieved public identity metadata
  summary: NCBI resolves PRJNA1369521 as the extremophile methanotrophic-algal coculture
    metagenome project for biogas valorization. Metadata agrees with the primary paper;
    raw sequences were not downloaded or reanalyzed.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: 5f3b7a667ac6a974b37755b99bc8901efdb8e916f4af2103bf4358677a664a55
- evidence_id: composition
  kind: primary_source
  reference: PMID:41745484
  locator: Sections 2.3 and 2.3.1; taxonomic abundance denominators
  summary: Chlorella and Dunaliella percentages refer to Chlorophyta, Leptolyngbya
    to the bacterial fraction, and the two methylotroph percentages to the methylotroph
    fraction. The 9.1% value describes the whole methanotroph guild, not Methylotuvimicrobium
    alone; the record explanation correctly says so. Its coarse abundance classes
    must not be treated as absolute cell fractions.
  support: supports
  accessed_at: '2026-11-05T22:26:22.631360Z'
  snapshot_sha256: 614c2550f02285471c58610c17bb9d6c44a2e08dc1ece608d7b0c0314a5d9f57
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:41745484
  locator: Sections 3.1–3.2, Table 1, and section 2.1
  summary: The mixed-inoculum reactor design, initial gas feed and startup intervention
    match the record. Table 1 is the appropriate light-intensity evidence for the
    coculture assay; the quoted light sentence currently attached to it is from inoculum
    preparation. The primary Methods also give additional structured conditions absent
    from the record. Final assays used25 degrees C and200rpm magnetic stirring; Table1
    reports56days; the prepared MSM was adjusted to initialpH9. These are distinct
    from150rpm orbital inoculum growth.
  support: supports
  accessed_at: '2026-11-05T22:26:22.631360Z'
  snapshot_sha256: 614c2550f02285471c58610c17bb9d6c44a2e08dc1ece608d7b0c0314a5d9f57
- evidence_id: ontology
  kind: authority
  reference: OAK local NCBITaxon, ENVO, GO and CHEBI snapshots
  locator: 13 unique identifiers, including six taxa
  summary: Every curated identifier and canonical label resolves. Eukaryotic algae
    correctly declare no GTDB equivalent; bacterial genus mappings remain explicitly
    unresolved. Process terms fit broad photosynthesis/methane metabolism without
    proving organism-specific activity.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: cff704b485c2e94ce29ea7727ff65142bc0f1b6de96126c6dcc4fe093b891500
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum and EvidenceSourceEnum
  summary: PRIMARY_DEGRADER denotes degradation of complex substrates, while methane
    is a one-carbon substrate. CROSS_FEEDER denotes use of another taxon’s metabolites.
    IN_VITRO includes bioreactor experiments; it is not by itself a claim that all
    taxon functions were directly measured.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  locator: All 36 EvidenceItem occurrences
  summary: 35 snippets match the primary XML after NFKC/whitespace normalization with
    inline XML tags concatenated. The DOI-labelled snippet is present in the PubMed-formatted
    cache header; the identifier independently verifies in PubMed and article metadata.
    No substantive quote mismatch was established.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: 37a102b0e1b11e8020920917cdc0c20e48c6261c21cf770fa9f6b969e03e7af8
- evidence_id: history
  kind: record_content
  reference: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture
  locator: Five append-only history files plus embedded history and the prior graph
    decision
  summary: 'The four older entries describe creation and gas/light, dangling-edge
    and uncertainty repairs. The October21 external event is misattributed: it names
    record000446, Methylocystis/Desmodesmus and a lipid node, while the actual current
    target change adds Leptolyngbya to 000415''s oxygen-support node. Embedded history
    matches the actual change. Do not use the erroneous external prose to certify
    the target.'
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
- evidence_id: local-search
  kind: search
  reference: references_cache; history/records; reports/causal_graph_review/decisions;
    kb/taxa
  locator: Ignored-inclusive PMID, accession and slug search
  summary: Located source cache, history and decision. Missing medium identifiers
    are absent from the entire target; no claim is made that a matching external registry
    record does not exist.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  search_scope: rg --no-ignore --hidden -n '41745484|1369521|Algal_Methanotroph_Biogas_Valorization_Coculture'
    references_cache history/records reports/causal_graph_review/decisions kb/taxa
  snapshot_sha256: a2347ddff47ada167c08ac2b672c1f386acd2e0d163ab2f1fcada53361132d6e
- evidence_id: adapter
  kind: record_content
  reference: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  locator: All taxon and interaction assertions; applicability assessment only
  summary: No strain-specific regulatory assertion or expression-module claim is curated.
    An expression-source lookup is not required for the actual community gas, metagenomic
    abundance and inferred exchange assertions; no current catalog search or dataset
    absence is claimed.
  support: context_only
  accessed_at: '2026-11-05T22:30:23.327619Z'
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261020T065737Z-algal-methanotroph-record/review.yaml
  locator: All five prior findings, four actions, whole-record assessments and frozen
    target
  summary: Every predecessor finding is rechecked. Stable issue keys and exact finding
    occurrence references are retained; only the single-target disconnected-member
    observation is resolved.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: 455dbf1ddc34124a9f5f995f2b115e6a07eb85dda6c9b40ac7f1255a1842419f
- evidence_id: target-diff
  kind: record_content
  reference: .temp/pr2035/415/target-diff.stdout.txt
  locator: Exact target diff from predecessor base to current HEAD
  summary: Only Leptolyngbya47251 participation in node0 and the embedded October21
    event changed. The previously flagged role, wording, evidence-locator and media-linkage
    fields are unchanged.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: f068f118edd9b19db5e3f667cb83f587943b8d8984355001cc8fef43f114783a
- evidence_id: target-network
  kind: validation
  reference: .temp/pr2035/415/target-network.json
  locator: NetworkIntegrityAuditor.audit_community on the current entire target
  summary: No target network issues. Every curated member occurs in a community-level
    participant list; this structural result does not demonstrate partner-specific
    exchange.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: history-mismatch
  kind: record_content
  reference: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-21T190000Z-claude-2048.yaml
  locator: events[0].summary and events[0].details versus target path, current diff
    and embedded history
  summary: The external event claims two different taxa, CommunityMech000446 and a
    different node, while the exact diff shows Leptolyngbya in record000415. It needs
    an append-only correction, not rewriting the old event.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: 6daeecaecb30693d966d470d6d1324726d1bcc32d45e232157cc27b68d0c4b46
- evidence_id: stage5-context
  kind: prior_review
  reference: reviews/structured/20261021T193000Z-stage5-remediation-verification/review.yaml
  locator: finding stage4-disconnected-syncom-participants description; context only
  summary: The preexisting multi-target finding describes000415 using Parachlorella
    kessleri NIES-2152/3074, inconsistent with both current target and primary source
    Leptolyngbya47251. Its terminal status is not used as scientific proof. This one-target
    successor does not retire or adjudicate that multi-target issue key.
  support: context_only
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: 8f8f980813203a0336e27f0bc0a3c3b6e68bb68c2f2a7d71460183f4fe3bbc09
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  locator: Actual execution 2026-11-05T22:26:35.529934Z to 2026-11-05T22:26:36.245306Z;
    receipt .temp/pr2035/415/validate.json
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml'
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: 0a055dc029fd57373f2c1b8fd0b9a37d0a95dd9e0ebbcb7628a6dce41dc26d57
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-strict kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv
  locator: Actual execution 2026-11-05T22:26:36.245520Z to 2026-11-05T22:26:41.100782Z;
    receipt .temp/pr2035/415/validate-strict.json
  summary: "uv run python scripts/validate_strict.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml\
    \ --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv\n\
    Validating 1 files with 17 workers; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/.temp/pr2035/415/strict.tsv"
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: ccefc261b60722b6e97645c655c164afcd09528fb1af16b74ece7c9884cb10c9
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-terms kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  locator: Actual execution 2026-11-05T22:26:41.100960Z to 2026-11-05T22:26:42.404514Z;
    receipt .temp/pr2035/415/validate-terms.json
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: c7eac3f25a8ce0cf93fbf4114d519f88af7e1cbe223d1553881f5e089b671856
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-gtdb kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  locator: Actual execution 2026-11-05T22:26:42.404732Z to 2026-11-05T22:26:42.472103Z;
    receipt .temp/pr2035/415/validate-gtdb.json
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: ba2db006c22d68b1baff4d5700719714c53ecea659f689563a88b16f212ab9bf
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-gtdb-domain kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  locator: Actual execution 2026-11-05T22:26:42.472268Z to 2026-11-05T22:26:43.470743Z;
    receipt .temp/pr2035/415/validate-gtdb-domain.json
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml'
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: 4ec79efbe04e635a6ce924c7b13da6fe80a8bc235755830e6d5595a8a9b210da
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-history history/records/Algal_Methanotroph_Biogas_Valorization_Coculture
  locator: Actual execution 2026-11-05T22:26:43.470915Z to 2026-11-05T22:26:44.055841Z;
    receipt .temp/pr2035/415/validate-history.json
  summary: No issues found
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: e0a36b624183ba924b3a20f0b8abf31ea010e6de34bb56bdce2bce381695ab9c
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-11-05T22:26:44.056017Z to 2026-11-05T22:26:44.095805Z;
    receipt .temp/pr2035/415/normalize-cache-names-check.json
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: f4d856187e6a791aa896ba00524fce6065e0f12cfed01c418c4e67022035c5e7
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-references-explained kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  locator: Actual execution 2026-11-05T22:26:44.096040Z to 2026-11-05T22:26:45.656006Z;
    receipt .temp/pr2035/415/validate-references-explained.json
  summary: "Validating kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: ce51a52add0029b0a148a5539db987e53e0a51fb8032e9eef0c4de9719b203aa
- evidence_id: check-audit-network
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv audit-network
  locator: Actual execution 2026-11-05T22:26:45.656204Z to 2026-11-05T22:26:50.632106Z;
    receipt .temp/pr2035/415/audit-network.json
  summary: Actual fresh corpus run:503 records,44 warnings in16 records,0 errors;
    exit1 retained. This target has no warnings. No corpus remediation is authorized
    by this review.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: 6aaf209f549963162edf13cf188eaf3b5c0694a08dca9f9f0890568f795d6871
- evidence_id: check-check-network-quality
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2035-batch02/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv check-network-quality
  locator: Actual execution 2026-11-05T22:26:50.632341Z to 2026-11-05T22:26:55.290119Z;
    receipt .temp/pr2035/415/check-network-quality.json
  summary: Actual fresh corpus run:503 records,44 warnings in16 records,0 errors;
    exit1 retained. This target has no warnings. No corpus remediation is authorized
    by this review.
  support: supports
  accessed_at: '2026-11-05T22:30:23.327619Z'
  snapshot_sha256: c27ea52c3936e32a9d5fce4650e09e5e91291d7966051d022c8654fec8d22d2f
assessments:
- assessment_id: identity
  area: identity
  topic: Mixed enrichment identity and provenance
  outcome: supported
  summary: The source, publication IDs and BioProject denote the same engineered laboratory
    coculture. The record preserves non-axenic enrichment origins and should not be
    read as six isolated strains or a natural ecosystem.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - record
  - primary
  - publication
  - dataset
  dimensions:
  - name: source_strain
    value: Mixed enrichments; no strain-resolved six-member assembly
    definition: Taxonomic representatives were inferred by shotgun profiling, not
      assembled as six purified isolates.
    evidence_ids:
    - composition
    - methods
  - name: community_scope
    value: Engineered algal–methanotrophic enrichment
    definition: The curated taxa are selected representatives of a more diverse microbiome.
    evidence_ids:
    - primary
    - record
  - name: experimental_setting
    value: Laboratory reactor comparisons with community gas/product measurements
    definition: Reactor-level phenotypes differ from partner-resolved metabolic transfer.
    evidence_ids:
    - gas
    - cultivation
  - name: medium
    value: Saline mineral medium and gas headspace
    definition: Inoculum preparation and final assay are separate experimental contexts.
    evidence_ids:
    - cultivation
  - name: evidence_tier
    value: Measured bulk endpoints; genomic composition; inferred exchange
    definition: Different claims in the same laboratory study have different mechanistic
      resolution.
    evidence_ids:
    - gas
    - methods
    - exchange
- assessment_id: taxonomy
  area: grounding
  topic: taxonomy[0..5], abundance and roles
  outcome: concern
  summary: 'All six identities verify at the curated ranks. Abundance statements retain
    the appropriate guild-level denominators in their explanations; the total methanotroph
    percentage is not assigned solely to one genus. Roles require more care: complex-substrate
    degradation is not methane oxidation, and unqualified CROSS_FEEDER tags exceed
    the explicitly hypothetical exchange node.'
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - record
  - ontology
  - schema
  - composition
  - exchange
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Photosynthetic O2 Support for Methane Oxidation'
  outcome: supported
  summary: The PARTIAL node correctly distinguishes observed gas dynamics from inferred
    oxygen support after startup supplementation. It does not assert partner-resolved
    transfer or reciprocal fitness.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - record
  - primary
  - gas
  details: Participants are Chlorella vulgaris, Dunaliella viridis, Leptolyngbya and
    Methylotuvimicrobium. Source sections2.3/2.3.1 support detected phototrophic membership;
    the PARTIAL node retains community-scale inferred oxygen support. No donor-resolved
    oxygen flux, reciprocal fitness or new causal arrow is established.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Methane-Linked Methylotroph Cross-Feeding'
  outcome: supported
  summary: The HYPOTHESIZED node accurately limits the proposed one-carbon exchange.
    Source physiology and taxon abundance support plausibility, not measured methanol
    transfer or detoxification.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - record
  - exchange
  - methods
  - composition
  details: 'Participants: Methylotuvimicrobium as candidate donor, Methylophaga and
    Methylonatrum as candidate recipients, within a community-level node. Mechanism:
    proposed methanol/other one-carbon use; no direct flux or reciprocal benefit established.
    Source PMID 41745484 section 2.3.1, exact short quote in exchange. Gene abundance
    is not pathway activity.'
- assessment_id: edges
  area: graph
  topic: ecological_interactions[*].downstream
  outcome: not_applicable
  summary: No downstream arrows occur in the complete target. Bulk gas removal, product
    accumulation and proposed exchange do not establish an ordered causal chain between
    the two nodes.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - record
  - history
  - primary
- assessment_id: environment
  area: scope
  topic: Environment, engineering design, factors and metal relevance
  outcome: supported
  summary: Laboratory environment, engineered origin and biotechnology category fit
    the source. The main assay and comparator design are correctly distinguished from
    source enrichments. The metal designation concerns the absence of a metal-processing
    ecological role, not absence of mineral medium constituents.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - record
  - cultivation
  - ontology
- assessment_id: cultivation
  area: provenance
  topic: growth_media and cultivation_setup
  outcome: concern
  summary: The represented assay details match Methods/Table 1. The illumination evidence
    locator comes from inoculum preparation despite a matching final-assay value in
    Table 1. Exact external medium links remain absent; no verified formulation match
    is assumed. Additional reported conditions could be represented in later curation,
    without treating absence as an invalid experiment.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - record
  - cultivation
  - snippets
- assessment_id: qualifiers
  area: evidence
  topic: description, related_ingredients[2] and functional roles
  outcome: concern
  summary: The graph and discussion correctly qualify exchange, but the summary/oxygen-ingredient
    wording sounds more certain and the methylotroph role tags have no hypothesis
    qualifier. The source itself proposes the mechanism; consistency requires carrying
    its evidential limits beyond graph prose.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - record
  - gas
  - exchange
  - schema
- assessment_id: resources
  area: provenance
  topic: Publication, dataset, snippets and history
  outcome: concern
  summary: Publication and BioProject identities resolve;35of36 snippets match normalized
    primaryXML and the DOI-labelled36th is in the bibliographic cache header. Five
    history files validate structurally, but the October21event's scientific identity
    is incorrect. Historical graph decisions and stage5 terminal status do not certify
    that event or this whole record.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - publication
  - dataset
  - snippets
  - history
  - methods
  - history-mismatch
  - stage5-context
  - target-diff
- assessment_id: adapter
  area: evidence
  topic: Structured expression-source applicability
  outcome: not_applicable
  summary: The target contains no strain-specific gene or regulatory assertion requiring
    an expression-module lookup. Source metagenomic attribution does not become a
    validated functional transfer through an unrelated expression dataset.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - adapter
  - methods
- assessment_id: validation
  area: schema
  topic: Focused gates and native network completeness
  outcome: concern
  summary: Eight focused/preflight gates pass and inspected canonical bytes remain
    unchanged. Both required corpus commands return1 for44warnings/16of503records,0errors.
    This target has no network issues after the Leptolyngbya participation addition;
    this is structural completeness, not proof of exchange.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - record
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-references-explained
  - check-audit-network
  - target-network
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: concern
  summary: Completeness90 and capped validation quality100 are rubric values, not
    scientific approval. Two major, three minor and one informational findings remain
    open; the original informational disconnected-member finding is resolved.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - record
  - schema
  - check-audit-network
  metrics:
  - name: completeness
    value: 90
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata including all roles +5 environment +10
      at least 3 factors +10 at least 3 nodes +5 external resources +10 media +5 datasets
      +5 node metabolites). 50+5+10+0+5+10+5+5=90; presence-only formula does not
      certify role correctness.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100-50*P1-10*P2-2*P3+20*min(mean node evidence/2,1)+15 if native
      COMPLETE,0,100). Open P1=0,P2=2,P3=3,P4=1;5evidence/2nodes; target network empty.
      clamp(100-20-6+20+15)=100.
  - name: P1
    value: 0
    unit: findings
    definition: Open native-severity finding count; resolved predecessor omission
      excluded.
  - name: P2
    value: 2
    unit: findings
    definition: Open native-severity finding count; resolved predecessor omission
      excluded.
  - name: P3
    value: 3
    unit: findings
    definition: Open native-severity finding count; resolved predecessor omission
      excluded.
  - name: P4
    value: 1
    unit: findings
    definition: Open native-severity finding count; resolved predecessor omission
      excluded.
  - name: interaction_evidence
    value: 2.5
    unit: evidence items per interaction
    denominator: 2
    definition: Five attached snippets across two nodes from one source, not five
      independent studies.
- assessment_id: stage5-identity-correction
  area: provenance
  topic: Bounded correction to Stage 5's CommunityMech:000415 identity clause
  outcome: concern
  summary: The description of finding stage4-disconnected-syncom-participants in review
    20261021T193000Z-stage5-remediation-verification incorrectly identifies the missing
    member of CommunityMech:000415 as Parachlorella kessleri NIES-2152, NCBITaxon:3074.
    The current record, original Stage 4 descriptions and primary source sections
    2.3/2.3.1 instead identify Leptolyngbya, NCBITaxon:47251. This append-only correction
    applies only to that 000415 identity clause. The other four targets and all grouped
    resolved dispositions are NOT reassessed; the multi-target issue key and occurrence
    lineage are not superseded.
  target_ids:
  - CommunityMech:000415
  evidence_ids:
  - stage5-context
  - record
  - composition
  - target-diff
findings:
- finding_id: functional-roles
  issue_key: cm-000415-functional-roles
  category: representation
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: P2.4
  status: open
  certainty: confirmed
  title: Functional-role tags exceed their support
  description: Methylotuvimicrobium is tagged PRIMARY_DEGRADER, whose schema definition
    concerns complex substrates, while the source concerns methane oxidation. Methylophaga
    and Methylonatrum are tagged CROSS_FEEDER without carrying the explicit hypothesis
    qualification already present in their interaction node.
  target_ids:
  - CommunityMech:000415
  field_paths:
  - taxonomy[3].functional_role
  - taxonomy[4].functional_role
  - taxonomy[5].functional_role
  evidence_ids:
  - record
  - schema
  - exchange
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T065737Z-algal-methanotroph-record
    finding_id: functional-roles
- finding_id: oxygen-qualification
  issue_key: cm-000415-oxygen-qualification
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded evidence-placement, wording or resource-linkage
    limitation; source identity and measured community endpoints remain supported.'
  rule_id: CLAUDE.claim-level-evidence
  status: open
  certainty: confirmed
  title: Oxygen-support certainty differs across fields
  description: The description and oxygen ingredient state photosynthetic supply as
    established, while the carefully curated node correctly states community-level
    inference. This is a bounded wording inconsistency; the gas-removal endpoint itself
    is supported.
  target_ids:
  - CommunityMech:000415
  field_paths:
  - description
  - related_ingredients[2].relevance
  - related_ingredients[2].evidence[0]
  evidence_ids:
  - record
  - gas
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T065737Z-algal-methanotroph-record
    finding_id: oxygen-qualification
- finding_id: light-evidence-context
  issue_key: cm-000415-light-evidence-context
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded evidence-placement, wording or resource-linkage
    limitation; source identity and measured community endpoints remain supported.'
  rule_id: CLAUDE.claim-level-evidence
  status: open
  certainty: confirmed
  title: Illumination evidence points to the inoculum stage
  description: The attached illumination quotation is from section 3.1 inoculum growth,
    while the explanation claims final coculture assays. Table 1 independently supports
    the curated assay intensity, so this is evidence placement rather than a wrong
    value.
  target_ids:
  - CommunityMech:000415
  field_paths:
  - growth_media[0].evidence[3]
  evidence_ids:
  - cultivation
  - snippets
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T065737Z-algal-methanotroph-record
    finding_id: light-evidence-context
- finding_id: media-linkage
  issue_key: cm-000415-media-linkage
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded evidence-placement, wording or resource-linkage
    limitation; source identity and measured community endpoints remain supported.'
  rule_id: P3.1
  status: open
  certainty: confirmed
  title: Medium lacks verified registry linkage
  description: The medium and gas components have CHEBI grounding where represented
    but no CultureMech or MediaIngredientMech link. A similarly named medium is not
    proof of formulation equivalence.
  target_ids:
  - CommunityMech:000415
  field_paths:
  - growth_media[0]
  evidence_ids:
  - record
  - cultivation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T065737Z-algal-methanotroph-record
    finding_id: media-linkage
- finding_id: unconnected-member
  issue_key: cm-000415-unconnected-member
  category: completeness
  severity: informational
  native_severity: P4
  normalization_reason: 'P4 informational: the native auditor explicitly treats disconnected
    taxa as incomplete knowledge, not inconsistent data.'
  rule_id: network.DISCONNECTED
  status: resolved
  certainty: confirmed
  title: Leptolyngbya has no curated interaction participation
  description: The predecessor observed Leptolyngbya missing from both participant
    lists. Current main explicitly includes Leptolyngbya47251 in the PARTIAL community-level
    oxygen-support node. Source sections2.3/2.3.1 report its detection and phototrophic
    community context. This supports bounded participation without a taxon-resolved
    transfer or new edge.
  target_ids:
  - CommunityMech:000415
  field_paths:
  - taxonomy[2]
  - ecological_interactions[*].participating_taxa
  evidence_ids:
  - record
  - target-diff
  - composition
  - gas
  - target-network
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T065737Z-algal-methanotroph-record
    finding_id: unconnected-member
  disposition_reason: Direct current-record inspection, exact target diff, source
    sections2.3/2.3.1 and a fresh empty target-network audit resolve this specific
    single-target omission. Neither the erroneous October21 external history prose
    nor the unrelated taxa in stage5 review prose are used as proof.
- finding_id: history-provenance
  issue_key: cm-000415-history-provenance
  category: provenance
  severity: major
  native_severity: P2
  normalization_reason: 'P2: materially misidentifies the record, taxa and interaction
    whose curation it claims to document.'
  rule_id: AGENTS.append-only-history
  status: open
  certainty: confirmed
  title: October21 history event describes different taxa and record
  description: The history file targets the000415slug but its event names000446, Methylocystis
    hirsuta, Desmodesmus abundans and a lipid-valorization node. The actual change
    adds Leptolyngbya47251 to000415's oxygen-support node. Schema validation does
    not establish history accuracy.
  target_ids:
  - CommunityMech:000415
  field_paths:
  - history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-21T190000Z-claude-2048.yaml:events[0].summary
  - history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-21T190000Z-claude-2048.yaml:events[0].details
  evidence_ids:
  - history-mismatch
  - target-diff
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-21T190000Z-claude-2048.yaml
    role: curation_history
- finding_id: assay-conditions
  issue_key: cm-000415-assay-conditions
  category: completeness
  severity: informational
  native_severity: P4
  normalization_reason: 'P4: optional source-supported cultivation enrichment; the
    existing assay is not invalidated.'
  rule_id: review-yaml-record.completeness
  status: open
  certainty: confirmed
  title: Track omitted final-assay cultivation conditions
  description: The predecessor requested later cultivation enrichment without a tracked
    action. Methods3.2 give25degreesC and200rpm magnetic stirring; Table1 gives56days
    for the co-culture; Methods3.1 gives initial prepared-medium pH9. These conditions
    are absent from the entire current target. Later curation must distinguish initialpH
    from maintainedpH and final-assay magnetic stirring from150rpm orbital inoculum
    growth.
  target_ids:
  - CommunityMech:000415
  field_paths:
  - growth_media[0]
  - cultivation_setup[0]
  evidence_ids:
  - cultivation
  - record
  - predecessor
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
actions:
- action_id: fix-functional-roles
  description: Use only role terms compatible with the source and schema; preserve
    unresolved exchange in the role evidence rather than asserting a confirmed donor-recipient
    function.
  finding_ids:
  - functional-roles
  target_ids:
  - CommunityMech:000415
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - No complex-substrate degradation is inferred from methane oxidation.
  - Role evidence distinguishes candidate methylotrophy from demonstrated interspecies
    transfer.
  - Run strict, reference and network checks.
- action_id: fix-oxygen-qualification
  description: Carry the same inferential qualification into summary and ingredient
    statements.
  finding_ids:
  - oxygen-qualification
  target_ids:
  - CommunityMech:000415
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Measured gas removal remains distinct from inferred oxygen transfer.
  - No taxon-resolved flux or reciprocal fitness is asserted.
  - Run strict and reference checks.
- action_id: fix-light-evidence-context
  description: Cite the final-assay table for the existing condition, preserving distinct
    inoculum and reactor stages.
  finding_ids:
  - light-evidence-context
  target_ids:
  - CommunityMech:000415
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - The evidence locator and explanation concern the same assay.
  - Do not derive other assay conditions from inoculum preparation.
  - Run reference and strict checks.
- action_id: fix-media-linkage
  description: Assess exact registry compatibility in later authorized curation; leave
    uncertain matches unresolved.
  finding_ids:
  - media-linkage
  target_ids:
  - CommunityMech:000415
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Any identifier resolves to the same formulation/context.
  - Do not substitute a convenient differently formulated medium.
  - Run relevant linkage and strict checks.
- action_id: correct-history-append-only
  description: Create a new append-only history correction that identifies the erroneous
    prior event and documents the actual Leptolyngbya addition to000415; preserve
    the old entry unchanged.
  finding_ids:
  - history-provenance
  target_ids:
  - CommunityMech:000415
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: history/records/Algal_Methanotroph_Biogas_Valorization_Coculture/2026-10-21T190000Z-claude-2048.yaml
    role: curation_history
  acceptance_checks:
  - Correction matches the actual Git diff, source scope and embedded history.
  - No historical event is rewritten.
  - Run history and strict validators.
- action_id: curate-assay-conditions
  description: Represent supported final-assay temperature, stirring and duration,
    and initial medium pH with exact source evidence and experimental-stage qualifiers.
  finding_ids:
  - assay-conditions
  target_ids:
  - CommunityMech:000415
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - 25degreesC/200rpm magnetic stirring/56days are scoped to final co-culture assay.
  - pH9 is initial prepared-medium pH, not a claimed controlled trajectory.
  - Do not import150rpm orbital inoculum conditions; run strict/reference validation
    and append history.
limitations:
- Primary Results/Discussion and Methods were freshly read from XML; separate supplements
  and raw metagenomic data were not reanalyzed.
- Shotgun taxonomic/gene attribution is not a direct measurement of taxon-resolved
  transfer, pathway activity or reciprocal fitness.
- BioProject metadata verifies project identity, not every sample accession or sequencing
  result.
- Bacterial GTDB assignments remain explicitly unresolved; coherence gates do not
  establish new mappings.
- Current reference validator coverage does not certify every assertion's source scope;
  direct36snippet replay complements it.
- Corpus network warning failures are retained explicitly. No out-of-scope canonical
  remediation was performed.
- The preexisting stage5 multi-target review misidentifies000415's member; this one-target
  successor explicitly excludes that prose from its scientific proof and does not
  adjudicate its multi-target lineage.
notes:
- Immutable successor to the stale PR2035review; original review bytes retained.
- Current record changed only in participant membership and embedded history; frozen
  input hashes and new receipts reflect current main.
- Scientific source scope and all five original findings were independently reconsidered
  by the author; independent adversarial approval remains a separate pass.
- No canonical records, source caches, history entries or generated products were
  changed by this refresh.
- Three brief source quotes inherited after fresh verification total fewer than25words;
  new claims are paraphrased with section locators.
tags:
- record-review
- biogas
- batch-02
- pr-2035
- staleness-refresh
- successor
```
