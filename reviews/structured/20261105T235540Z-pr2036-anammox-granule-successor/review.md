# Anammox granule community: current-main review successor

- Review: 20261105T235540Z-pr2036-anammox-granule-successor
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-05T23:50:46.514704Z
- Finished UTC: 2026-11-05T23:55:40.767915Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current main adds three ordinal abundance levels and two source-matching evidence items. These additions resolve the narrow missing-field observation already assessed by the later abundance review, without correcting taxonomy. All eight original findings remain open after fresh source review: four major findings concern AMX1 species precision, the CHB clade, exchange certainty and publication-as-dataset representation; four minor findings concern setting, cultivation evidence, background scope and media linkage. Eight focused checks pass; corpus warning exits remain explicit.

## Scope And Provenance

Whole current record: three grouped taxonomic entries, four interaction nodes, three downstream arrows, 17 evidence occurrences, environmental and cultivation claims, dataset representation and three history sidecars. Primary abstract, introduction, Results, Discussion, Methods and Tables 1 and 2 were read; public publication, project and sample metadata were checked.

Selection: PR 2036 stale-target refresh against current main. The parsed diff contains three abundance levels, two evidence items and one embedded history entry; other target data are semantically unchanged. Every original finding was reassessed.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3ee950068e95d2f310643c1a43573fcee872df18.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000146 | kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml | maintained | Anammox Granule Metabolic Interaction Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000146 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml |
| validate-strict | passed | True | CommunityMech:000146 | uv run python scripts/validate_strict.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv<br>Validating 1 files with 17 workers; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv |
| validate-terms | passed | True | CommunityMech:000146 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000146 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000146 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml |
| validate-history | passed | True | CommunityMech:000146 | No issues found |
| normalize-cache-names-check | passed | True | CommunityMech:000146 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000146 | Validating kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000146 | Actual fresh corpus run: 503 records, 44 warnings in 16 records, zero errors; exit 1 retained. The current target has no network issues. No canonical corpus remediation was performed. |
| check-network-quality | failed | True | CommunityMech:000146 | Actual fresh corpus run: 503 records, 44 warnings in 16 records, zero errors; exit 1 retained. The current target has no network issues. No canonical corpus remediation was performed. |
| Structured expression-source applicability | not_applicable | False | CommunityMech:000146 | Native runner unavailable in bounded lookup; public catalog fallback inspected. No exact source-population dataset match was found in the returned catalog. This is not negative evidence for the study's expression claims. |

## Scientific And Domain Assessments

### Community and experiment scope

identity: supported. Targets: CommunityMech:000146.

Publication and record concern the same laboratory anammox granule enrichment. Three grouped entries are not three isolated organisms or an exhaustive census of the 17 recovered genomes.

### taxonomy[0..2] and repeated graph participants

grounding: concern. Targets: CommunityMech:000146.

AMX1 species precision is unsupported; CHB family ancestry contradicts the modern Chlorobiota anchor. Broad flanking Bacteria is a disclosed aggregate. Valid ID-label pairs and GTDB syntax do not repair wrong biological attribution.

### taxonomy abundance values

evidence: supported. Targets: CommunityMech:000146.

The new DOMINANT, ABUNDANT and COMMON levels are consistent qualitative summaries of the source's AMX1, CHB1-associated and moderately represented flanking populations. AMX1 and CHB1 values are DNA/RNA mapping proxies for recovered MAGs; CHB1 percentages must not be assigned to every CHB genome or a modern named clade, and COMMON does not encode a combined guild percentage. The two new snippets match the source exactly after documented normalization.

### ecological_interactions[0]: Anammox Ammonium-Nitrite Conversion

graph: concern. Targets: CommunityMech:000146.

Expression supports the qualified anammox function, but the participant’s sinica identity is unsupported.

AMX1 is encoded as NCBITaxon:795830, but Table 1 supports Brocadia affiliation rather than confirmed sinica identity. Ammonium/nitrite use and expressed anammox potential are supported at the study-MAG level. The linked primary evidence gives exact source locators and brief quotations. No stronger exchange claim is justified.

### ecological_interactions[1]: Heterotrophic Nitrite Loop

graph: concern. Targets: CommunityMech:000146.

The loop is appropriately hypothetical; participant identity and summary wording still need correction.

Participants are aggregated Bacteria and AMX1; proposed direction heterotrophic nitrate reduction to nitrite returning to anammox. Source DOI10.1038/ncomms15416; exact locator and short verbatim snippet in linked evidence. Mechanistic qualification is retained; concerns are attribution, not a request to strengthen causation.

### ecological_interactions[2]: EPS Peptide Scavenging by Chlorobi

graph: concern. Targets: CommunityMech:000146.

Peptide scavenging is explicitly inferred, but Chlorobiota and sinica identifiers misrepresent source population resolution.

Participants AMX1 and CHB populations; proposed direction extracellular protein toward heterotrophic scavengers. Proteolysis is supported as expressed potential. Source DOI10.1038/ncomms15416; exact locator and short verbatim snippet in linked evidence. Mechanistic qualification is retained; concerns are attribution, not a request to strengthen causation.

### ecological_interactions[3]: Detritus and Small-Donor Scavenging

graph: concern. Targets: CommunityMech:000146.

The node preserves unresolved acetate direction and carbon provenance; its AMX1 species identifier remains unsupported.

Participants AMX1 and aggregate flanking bacteria; candidate detritus/small-donor use, not verified secretion and uptake. Source DOI10.1038/ncomms15416; exact locator and short verbatim snippet in linked evidence. Mechanistic qualification is retained; concerns are attribution, not a request to strengthen causation.

### ecological_interactions[0].downstream[0]

graph: concern. Targets: CommunityMech:000146.

The arrow is correctly hypothetical, while its upstream AMX1 species attribution requires correction.

From Anammox Ammonium-Nitrite Conversion to Heterotrophic Nitrite Loop. HYPOTHESIZED - anammox-derived nitrate could supply heterotrophic nitrate reduction and a nitrite-return loop; expression supports potential but not the exchanged flux. Participants AMX1 and the corresponding heterotrophic group. Direction is proposed substrate provision, not measured transfer. Same-study expression supports potential only; source locator/snippet in linked evidence.

### ecological_interactions[0].downstream[1]

graph: concern. Targets: CommunityMech:000146.

The arrow is correctly hypothetical, while its upstream AMX1 species attribution requires correction.

From Anammox Ammonium-Nitrite Conversion to EPS Peptide Scavenging by Chlorobi. HYPOTHESIZED - anammox-associated extracellular material could feed heterotrophic proteolysis; the source of consumed protein and the transfer were not traced in this study. Participants AMX1 and the corresponding heterotrophic group. Direction is proposed substrate provision, not measured transfer. Same-study expression supports potential only; source locator/snippet in linked evidence.

### ecological_interactions[0].downstream[2]

graph: concern. Targets: CommunityMech:000146.

The arrow is correctly hypothetical, while its upstream AMX1 species attribution requires correction.

From Anammox Ammonium-Nitrite Conversion to Detritus and Small-Donor Scavenging. HYPOTHESIZED - biomass turnover or released small substrates could feed heterotrophs; wastewater-derived organic carbon and unresolved pathway directions prevent exclusive attribution to AMX1. Participants AMX1 and the corresponding heterotrophic group. Direction is proposed substrate provision, not measured transfer. Same-study expression supports potential only; source locator/snippet in linked evidence.

### Description and functional roles

evidence: concern. Targets: CommunityMech:000146.

Summary verbs and unqualified cross-feeder roles lose the graph’s uncertainty. Source transfer hypotheses must not become established exchange claims; the broad secondary-fermenter role also overgeneralizes variable capacities where nitrate respiration dominates.

### environment_term and environmental factors

scope: concern. Targets: CommunityMech:000146.

Wastewater treatment plant describes the feedstock setting, not the laboratory reactor itself. Oxygen-diffusion and EPS statements are general introductory context rather than same-study spatial measurements.

### growth_media[0]

evidence: concern. Targets: CommunityMech:000146.

The stated anaerobic reactor context has Methods support, but its attached genome-recovery snippet supports neither atmosphere nor influent identity. Sparse operational detail is not itself a false claim.

### associated_datasets[0]

representation: concern. Targets: CommunityMech:000146.

An article URL and publisher article number are typed as a metatranscriptomics dataset. Verified project/sample accessions should represent data; publication belongs in publication resources.

### History and open discussion

provenance: supported. Targets: CommunityMech:000146.

Three sidecars preserve the earlier snippet and graph repairs plus the November 5 abundance additions. The new event matches the actual parsed diff. The open discussion correctly keeps exchange unresolved; an abundance-field repair does not certify taxonomy, datasets or causal claims.

### Native and independent checks

schema: supported. Targets: CommunityMech:000146.

Eight focused/history/preflight commands pass. All 10 curated ID-label pairs resolve and all 17 evidence placements match the fresh primary XML. Additional family-ancestry inspection confirms identity errors beyond label/syntax gates. The target network audit is empty, while both corpus commands retain their real warning exits.

### Native completeness and validation quality

completeness: concern. Targets: CommunityMech:000146.

Completeness 95 counts populated fields, including the misrepresented dataset; validation quality 79.5 reflects four open major and four open minor findings. Neither score is scientific approval.

### Scope of the later abundance-field remediation

provenance: supported. Targets: CommunityMech:000146.

Current field presence, exact source evidence and the November 5 sidecar support the narrow resolution recorded for c7s4-000146-anammox-granule-abundance-levels. This assessment creates no additional terminal disposition and supersedes no unrelated or grouped review. The eight original findings remain open, especially AMX1 species precision and CHB modern-clade identity.

## Findings

### amx-species: AMX1 is assigned an unsupported species

major / open / confirmed; issue key: cm-000146-amx-species.

The source identifies Brocadia affiliation and proximity to both sinica and fulgida. Closest-representative notes do not justify exact sinica NCBI/GTDB identity propagated through participants.

### chb-clade: Historical Chlorobi was mapped to the wrong modern clade

major / open / confirmed; issue key: cm-000146-chb-clade.

Table 1 assigns CHB1 and CHB2 to families now descending through Ignavibacteriota in the inspected NCBI ancestry, not Chlorobiota (NCBITaxon:1090). The current GTDB Chlorobiia block follows that incorrect anchor. Newly added abundance evidence does not correct taxonomic identity.

### exchange-overstatement: Summary and roles overstate inferred exchanges

major / open / confirmed; issue key: cm-000146-exchange-overstatement.

The description states recycling/scavenging as realized community functions and cross-feeder roles lack the qualification retained in the graph. Fermentation is not established as the shared principal mode of all flanking bacteria.

### article-as-dataset: Publication is represented as a sequencing dataset

major / open / confirmed; issue key: cm-000146-article-as-dataset.

Nature-Communications-15416 is an article locator, not the deposited sequencing accession. The source and NCBI verify actual project and three sample accessions.

### laboratory-setting: Environment points to the source treatment plant

minor / open / confirmed; issue key: cm-000146-laboratory-setting.

The target is a laboratory reactor; appropriate bioreactor/laboratory terms exist. The nearest-validated-term rationale is unsupported.

### cultivation-evidence: Cultivation has an unrelated supporting snippet

minor / open / confirmed; issue key: cm-000146-cultivation-evidence.

The current cultivation evidence duplicates a genome-recovery quotation from engineering_design. It supports genome reconstruction rather than influent identity or anaerobic atmosphere. The source Methods provide directly relevant evidence; resolving the earlier source-verifiability backlog alone would not fix this semantic mismatch.

### background-factor-scope: General granule context is not identified as background

minor / open / confirmed; issue key: cm-000146-background-factor-scope.

Introductory oxygen-diffusion and EPS statements are not measurements of this experiment’s gradients or matrix composition.

### media-links: Media lacks external linkage identifiers

minor / open / confirmed; issue key: cm-000146-media-links.

No CultureMech/MediaIngredientMech links are present. Wastewater filtrate is not interchangeable with a defined synthetic recipe.

## Recommended Actions And Acceptance Checks

### fix-amx-species

Retain source-resolved Brocadia/MAG identity and independently verify any narrower mapping before applying it consistently.

- No exact species is inferred merely from closest related representatives.
- All repeated participant mappings agree.
- Run term,GTDB,strict and network gates.

### fix-chb-clade

Reconcile each source CHB/MAG lineage and re-ground NCBI and GTDB from that identity rather than historical phylum wording.

- Source family placements and modern ancestry agree.
- GTDB mapping is independently recomputed/verified for the corrected anchor.
- Every graph participant is updated consistently.

### fix-exchange-overstatement

Preserve inferred-expression evidence and unresolved transfer/direction in summaries and roles.

- No confirmed partner flux or exclusive AMX1 carbon source is asserted.
- Roles are source-specific or explicitly uncertain.
- Graph qualification is preserved.

### fix-article-as-dataset

Separate publication resources from actual deposited datasets with correct type and provenance.

- Project/sample identifiers resolve to the correct study and data type.
- Article is not mislabeled as a raw sequencing dataset.
- Run strict and reference gates.

### fix-laboratory-setting

Represent actual laboratory setting separately from the feedstock source facility.

- Setting term matches experimental context.
- Feedstock provenance remains intact.
- Run term validation.

### fix-cultivation-evidence

Attach exact Methods evidence to the stated cultivation claims without inventing an influent recipe.

- Attached evidence supports the actual atmosphere/influent claim.
- Do not conflate upstream/downstream reactors.
- Run reference validation.

### fix-background-factor-scope

Identify background versus study-specific evidence and avoid implying measured gradients.

- General context is marked as such.
- No unavailable same-system measurement is claimed.

### fix-media-links

Assess exact applicable resource matches and leave unmatched identities explicit.

- No approximate recipe receives an exact identifier.
- Any accepted link resolves and matches its intended material.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml; Whole current target: three grouped taxa, four nodes, three arrows and all 17 evidence occurrences | supports | Record represents a laboratory granular-sludge enrichment, with broader placeholders for multiple MAGs rather than three isolates. Graph descriptions preserve inferred exchange; exact taxon identifiers and summary require separate assessment. |
| primary | doi:10.1038/ncomms15416; Fresh Europe PMC PMC5460018 XML; abstract, introduction, all Results, Discussion, Methods, Table 1 and Table 2 text. Snapshot and retrieval receipt frozen under .temp/pr2036/146. | supports | The full main article and table text were inspected. The study reconstructs metabolic potential from community DNA/RNA mapping and does not directly trace partner-resolved exchange. Supplementary files and rendered figure geometry were not inspected. |
| amx-identity | doi:10.1038/ncomms15416; Results: Anammox metatranscriptomic insights; Table1 AMX1 row | supports | AMX1 is Brocadia-affiliated and related to both named species, not identified as sinica. Table1 resolves genus only. A nearest representative does not justify exact species identity in the graph. |
| chb-identity | doi:10.1038/ncomms15416; Table1 CHB1 and CHB2 rows | supports | CHB1 belongs to source Ignavibacteria/ Ignavibacteriales/ Melioribacteraceae; CHB2 to Ignavibacteriaceae. Historical Chlorobi wording must be interpreted through these finer source placements. |
| lineage | OAK local ncbitaxon.db; Fresh rdfs:subClassOf ancestry for NCBITaxon:1334117, NCBITaxon:795749 and NCBITaxon:1090 | supports | Melioribacteraceae and Ignavibacteriaceae descend through Ignavibacteria and Ignavibacteriota (NCBITaxon:1134404), not Chlorobiota (NCBITaxon:1090), in the local NCBI authority. These are the families assigned to CHB1 and CHB2 in Table 1. This confirms the clade conflict despite valid labels; the existing GTDB block follows the incorrect anchor and has not been independently re-grounded. |
| ontology | OAK local NCBITaxon,ENVO,CHEBI and GO snapshots; Ten curated ID-label pairs; alternative ENVO setting identifiers checked separately | supports | All ten curated labels match current local OAK authority labels. ENVO:00002123 resolves to bioreactor and ENVO:01001405 to laboratory environment. These provide appropriate setting alternatives; syntax and matching labels cannot establish that the target organism belongs to a mapped taxon. |
| anammox | doi:10.1038/ncomms15416; Results: Anammox metatranscriptomic insights | supports | AMX1 expressed anammox-related genes. Reactor function and expression support active potential; they do not validate the species assignment or downstream partner flux. |
| nitrite | doi:10.1038/ncomms15416; Results: Denitrification gene expression; Discussion | supports | Nitrate-reductase expression supports candidate recycling, with other reduction routes and component-expression caveats. A completed exchange loop is proposed rather than measured. |
| peptides | doi:10.1038/ncomms15416; Results: Amino acid and carbohydrate catabolism; Discussion | supports | Peptidase expression and predicted localization support proposed protein scavenging. Cited tracer evidence comes from other work, not this experiment; substrate origin and intermember transfer were not traced. |
| donors | doi:10.1038/ncomms15416; Results: Carbon and energy metabolism; Discussion | supports | Acetate pathway direction remains unresolved; candidate formate/hydrogen use does not prove AMX1 secretion. Wastewater-derived carbon prevents exclusive attribution of heterotrophic substrates to AMX1. |
| operation | doi:10.1038/ncomms15416; Methods: Bioreactor operation; Table2; introductory granule background | supports | Two-stage wastewater treatment feeds the laboratory anammox reactor with filtrate after nitritation. Anaerobic operation is described directly. The record’s genome-recovery snippet does not support medium/atmosphere. Oxygen diffusion and matrix statements in the introduction are general background, not same-system gradient measurements. |
| abundance | doi:10.1038/ncomms15416; Results: Microbial community abundance and gene expression; Methods: metatranscriptomics | supports | AMX1 is approximately 62% of the source abundance proxy and 54% of its expression proxy; CHB1 is approximately 21% and 26%, respectively. DOMINANT and ABUNDANT are defensible ordinal summaries under AbundanceEnum. The source describes other flanking genomes as moderately abundant, supporting COMMON as a qualitative aggregate descriptor, not a measured percentage for every taxon. These are genome-length-normalized DNA/RNA mapping proxies; DNA covers two collection events while RNA comes from the second. No absolute cell count or combined guild percentage is established. |
| pubmed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=28561030&amp;retmode=xml; Independent metadata retrieval | supports | Publication identity agrees with the primary article. |
| crossref | https://api.crossref.org/works/10.1038/ncomms15416; Independent metadata retrieval | supports | Publication identity agrees with the primary article. |
| bioproject | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=bioproject&amp;id=343219&amp;retmode=json; NCBI BioProject esummary result 343219: accession, title, project description and data type | supports | PRJNA343219 describes a 5 L laboratory anammox sequencing-batch reactor fed with anaerobic digester filtrate after nitritation. It matches the article's study context; the metadata does not itself audit raw sequence content. |
| biosample_metagenome | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&amp;id=SAMN05785375,SAMN05785376,SAMN05785373&amp;retmode=xml; BioSample XML row SAMN05785375: accession, title, sample identifiers and collection date | supports | SAMN05785375 identifies the source-described Illumina HiSeq 2000 metagenome, 2 x 125 bp; collected September 9, 2015; SRA sample SRS1713242. Metadata validates accession and sample type, not every deposited read or inferred MAG. |
| biosample_transcriptome | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&amp;id=SAMN05785375,SAMN05785376,SAMN05785373&amp;retmode=xml; BioSample XML row SAMN05785376: accession, title, sample identifiers and collection date | supports | SAMN05785376 identifies the source-described Illumina HiSeq 2000 metatranscriptome, 2 x 125 bp; collected September 9, 2015; SRA sample SRS1713243. Metadata validates accession and sample type, not every deposited read or inferred MAG. |
| biosample_miseq | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&amp;id=SAMN05785375,SAMN05785376,SAMN05785373&amp;retmode=xml; BioSample XML row SAMN05785373: accession, title, sample identifiers and collection date | supports | SAMN05785373 identifies the source-described Illumina MiSeq metagenome S1, 2 x 300 bp; collected September 4, 2013; SRA sample SRS1713240. Metadata validates accession and sample type, not every deposited read or inferred MAG. |
| snippets | kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml; All 17 current evidence placements, including duplicated cultivation text and two newly added abundance quotations | supports | All 17 snippets match the freshly retrieved primary XML after NFKC and whitespace normalization with inline tags joined. The two new abundance quotations preserve the source wording. Exact text matching does not establish that a genome-recovery fragment supports atmosphere or influent identity. |
| history | reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml; Target graph decision, all three history sidecars and current embedded history | supports | The prior graph decision explicitly qualified exchange and excluded non-graph metadata from certification, including unresolved species identity. The November 5 sidecar accurately describes the three abundance annotations and two added evidence items. Its scope is abundance annotation; it does not certify taxonomic identity or the eight outstanding findings. |
| local-search | references_cache;history;reports/causal_graph_review/decisions;kb/taxa; DOI and target filename search including ignored and hidden files | supports | An ignored-inclusive bounded search located the cache, history and prior decision. No file matching this DOI or exact slug was returned from kb/taxa; this is not an exhaustive search for every taxonomic synonym. Missing linkage observations concern the entire current target, not absence of matches in external registries. |
| predecessor | reviews/structured/20261020T073708Z-anammox-granule-record/review.yaml; All eight findings and their action plans | supports | All eight original findings were reassessed and remain open. Stable issue keys and exact predecessor finding references are retained. |
| target-change | .temp/pr2036/146/target-semantic-diff.json; Parsed comparison against the predecessor's frozen Git target; textual diff separately retained | supports | Only three abundance levels, two evidence objects and one embedded history entry were added. The remaining text diff is serialization, not a biological or claim-level change. |
| abundance-history | history/records/Anammox_Granule_Metabolic_Interaction_Community/2026-11-05T165000Z-antigravity-2120a1.yaml; events[0] and current curation_history[1] | supports | The history description matches the source-backed additions. The narrow missing-abundance-field issue is resolved in the inspected later review; this observation does not retire unrelated taxonomic findings or rewrite prior history. |
| abundance-review-context | reviews/structured/20261105T171000Z-c7s5-remediation-verification/review.yaml; Single-target finding c7s4-000146-anammox-granule-abundance-levels and its referenced Stage 4 occurrences | supports | The later review records a resolved missing-field observation. Current field presence and fresh source inspection substantiate only that narrow repair. This successor does not create another terminal disposition for that key and does not imply corrected AMX1 or CHB taxonomy. |
| abundance-schema | src/communitymech/schema/communitymech.yaml; AbundanceEnum and Taxon.abundance_level | supports | The abundance enum expresses ordinal prominence, explicitly not percentages. It supports a dominant AMX1, major CHB1-associated entry and moderately represented flanking group while retaining the exact proxy and group scope in evidence. |
| alternative-settings | .temp/pr2036/146/alternative-settings.json; Direct OAK lookup of two candidate ENVO settings | supports | Both bioreactor and laboratory environment labels resolve. The appropriate choice is a later curation decision grounded in the laboratory experimental setting. |
| target-network | .temp/pr2036/146/target-network.json; Fresh NetworkIntegrityAuditor.audit_community result | supports | The entire target has no structural network warnings. This does not establish the scientific correctness of participant identifiers or hypothetical transfer edges. |
| adapter-discovery | .temp/pr2036/146/adapter-discovery.json; Executable lookup and two exact expected sibling CLAW paths, including ignored paths | supports | No installed kg-microbe-sources runner was found, and both inspected sibling checkout paths are absent. This is a bounded lookup, not a claim about every filesystem location. |
| expression-catalog | https://imodulondb.org/api/datasets; Complete returned public catalog: 20 organism entries and their dataset keys | supports | No returned catalog organism corresponds to the source Brocadia or Ignavibacteria populations, and no exact AMX1/CHB study dataset is listed. A broad Bacteria placeholder does not establish a strain match to another organism's expression modules. The actual study's metatranscriptomic source and metadata provide the applicable evidence. |
| check-validate | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml; Actual execution 2026-11-05T23:50:58.814331Z to 2026-11-05T23:50:59.369161Z; receipt .temp/pr2036/146/validate.json | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml |
| check-validate-strict | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-strict kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv; Actual execution 2026-11-05T23:50:59.369361Z to 2026-11-05T23:51:01.295299Z; receipt .temp/pr2036/146/validate-strict.json | supports | uv run python scripts/validate_strict.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv<br>Validating 1 files with 17 workers; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv |
| check-validate-terms | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-terms kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml; Actual execution 2026-11-05T23:51:01.295577Z to 2026-11-05T23:51:02.354733Z; receipt .temp/pr2036/146/validate-terms.json | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-gtdb kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml; Actual execution 2026-11-05T23:51:02.354918Z to 2026-11-05T23:51:02.415526Z; receipt .temp/pr2036/146/validate-gtdb.json | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-gtdb-domain kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml; Actual execution 2026-11-05T23:51:02.415782Z to 2026-11-05T23:51:03.346729Z; receipt .temp/pr2036/146/validate-gtdb-domain.json | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml |
| check-validate-history | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-history history/records/Anammox_Granule_Metabolic_Interaction_Community; Actual execution 2026-11-05T23:51:03.346945Z to 2026-11-05T23:51:04.354664Z; receipt .temp/pr2036/146/validate-history.json | supports | No issues found |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-11-05T23:51:04.354864Z to 2026-11-05T23:51:04.393839Z; receipt .temp/pr2036/146/normalize-cache-names-check.json | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv validate-references-explained kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml; Actual execution 2026-11-05T23:51:04.394065Z to 2026-11-05T23:51:05.233774Z; receipt .temp/pr2036/146/validate-references-explained.json | supports | Validating kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv audit-network; Actual execution 2026-11-05T23:51:05.233957Z to 2026-11-05T23:51:09.628218Z; receipt .temp/pr2036/146/audit-network.json | supports | Actual fresh corpus run: 503 records, 44 warnings in 16 records, zero errors; exit 1 retained. The current target has no network issues. No canonical corpus remediation was performed. |
| check-check-network-quality | JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv just --no-dotenv check-network-quality; Actual execution 2026-11-05T23:51:09.628427Z to 2026-11-05T23:51:13.846281Z; receipt .temp/pr2036/146/check-network-quality.json | supports | Actual fresh corpus run: 503 records, 44 warnings in 16 records, zero errors; exit 1 retained. The current target has no network issues. No canonical corpus remediation was performed. |

## Limits And Additional Notes

- Supplementary files, raw reads, accessioned MAG assemblies and rendered figure geometry were not inspected; no independent sequence reconstruction or flux measurement is claimed.
- Fresh local NCBI ancestry confirms the CHB clade conflict. Replacement GTDB grounding and exact accessioned MAG identity require separate curation; coherence gates do not certify the existing biological assignments.
- Abundance and expression values are genome-mapping proxies, not absolute cell counts. Qualitative group annotations must not be interpreted as per-organism measurements or percentages of a modern named clade.
- Required corpus checks retain nonzero warning exits; clean target participation does not verify participant identity or mechanism.
- The native structured-expression runner was unavailable in a bounded lookup. The public catalog fallback had no exact source-population match; primary study text and deposited sample metadata were used, without treating catalog absence as biological evidence.
- Media matching was not searched across external registries. The missing-link finding concerns this target's absent identifiers and does not assert that no exact applicable registry resource exists.
- Original immutable review bytes are preserved. This successor records fresh input hashes, source snapshots and actual check receipts.
- Canonical records, caches, history and generated products were not changed by this author refresh.
- All eight original findings are retained with exact predecessor references; no new scientific curation finding was identified in this refresh.
- Five verified short quotations inherited from the primary paper total 22 words; other source content is paraphrased with locators.
- Independent adversarial review is performed separately from this author pass.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T235540Z-pr2036-anammox-granule-successor
kind: record
repository: CultureBotAI/CommunityMech
title: 'Anammox granule community: current-main review successor'
started_at: '2026-11-05T23:50:46.514704Z'
finished_at: '2026-11-05T23:55:40.767915Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Author refresh of the stale PR 2036 review, with historical
    Codex graph curation. Independent adversarial approval is a separate pass and
    is not claimed here.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Current main adds three ordinal abundance levels and two source-matching
  evidence items. These additions resolve the narrow missing-field observation already
  assessed by the later abundance review, without correcting taxonomy. All eight original
  findings remain open after fresh source review: four major findings concern AMX1
  species precision, the CHB clade, exchange certainty and publication-as-dataset
  representation; four minor findings concern setting, cultivation evidence, background
  scope and media linkage. Eight focused checks pass; corpus warning exits remain
  explicit.'
source:
  git_revision: 3ee950068e95d2f310643c1a43573fcee872df18
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
  - path: .temp/pr2036/146/adapter-discovery.json
    sha256: 6f8de737447babd85c8a656e25df93658e2bf516f614f6a432523e97d40bb049
    role: context
  - path: .temp/pr2036/146/alternative-settings.json
    sha256: fe667cf2b60972714c408fe3a6efbd45f715efad0cbe1b0fbb2e628b939c800d
    role: context
  - path: .temp/pr2036/146/audit-network.json
    sha256: 00e8bc5adeff9be15381903c1bcaa491f1629cfa1091dd73cb0259442ab35c26
    role: context
  - path: .temp/pr2036/146/audit-network.stderr.txt
    sha256: a71fb29e950f3eaf0eb2b834a43c59d4a1b6aa85a2a89473ae99b0e408a27a36
    role: context
  - path: .temp/pr2036/146/audit-network.stdout.txt
    sha256: f5dc190f832300fc5a73fcf3e7e8e3cd53d560ba09b17179ce6c7fcc8aa022e8
    role: context
  - path: .temp/pr2036/146/bioproject.json
    sha256: 34e4e4046e5b05fa94de66b64f1c6c76447a0431318b61e8ed50b66556af8b37
    role: context
  - path: .temp/pr2036/146/biosamples.xml
    sha256: 5d0c91117de7380e060a34eec7e9d8aacc8694941741e73f3af0dc6bb1614b3f
    role: context
  - path: .temp/pr2036/146/check-network-quality.json
    sha256: 31061c9dfacfc1e097e6c16e10d38a4cf9210bf635d8ee7beff96616379b1f0f
    role: context
  - path: .temp/pr2036/146/check-network-quality.stderr.txt
    sha256: f9a8e9fb5a4e4ea545236a809393dbc1ce4325b14579c65a3130bcfe713e798a
    role: context
  - path: .temp/pr2036/146/check-network-quality.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/crossref.json
    sha256: c50626648afbf656a34b1c1e42027b646ee65f010deb2ceaeb4e3ffb5e5cf061
    role: context
  - path: .temp/pr2036/146/fetch-bioproject.json.json
    sha256: 4be7a521f29f8c60cb3ad4758795de9536e7a62c899bc67a6401cc7649ea8f59
    role: context
  - path: .temp/pr2036/146/fetch-bioproject.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/fetch-bioproject.json.stdout.txt
    sha256: 34e4e4046e5b05fa94de66b64f1c6c76447a0431318b61e8ed50b66556af8b37
    role: context
  - path: .temp/pr2036/146/fetch-biosamples.xml.json
    sha256: 294e1aa2f675fe36650da37dcb5bac0f1c427f6d1d4d341347e2d1749cea647b
    role: context
  - path: .temp/pr2036/146/fetch-biosamples.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/fetch-biosamples.xml.stdout.txt
    sha256: 5d0c91117de7380e060a34eec7e9d8aacc8694941741e73f3af0dc6bb1614b3f
    role: context
  - path: .temp/pr2036/146/fetch-crossref.json.json
    sha256: 0cf8a1c2d836002555df54bbb45be082e093c36e450f1e790bb07a11c218d626
    role: context
  - path: .temp/pr2036/146/fetch-crossref.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/fetch-crossref.json.stdout.txt
    sha256: c50626648afbf656a34b1c1e42027b646ee65f010deb2ceaeb4e3ffb5e5cf061
    role: context
  - path: .temp/pr2036/146/fetch-imodulon-catalog.json.json
    sha256: 5ebdb81767a91e4d0943aa5888f4726f97d9e0f8eb1225df4e7f67d8199ba9eb
    role: context
  - path: .temp/pr2036/146/fetch-imodulon-catalog.json.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/fetch-imodulon-catalog.json.stdout.txt
    sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
    role: context
  - path: .temp/pr2036/146/fetch-primary.xml.json
    sha256: 1399294db75bd5744b09bbb50fb2947dadd762e96268dd2c750fcbe59f3055b4
    role: context
  - path: .temp/pr2036/146/fetch-primary.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/fetch-primary.xml.stdout.txt
    sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
    role: context
  - path: .temp/pr2036/146/fetch-publication.xml.json
    sha256: 5d62b3fcf9a96eb5a734f152acbf3f55d10a214b585acdf9c7000477c81540c1
    role: context
  - path: .temp/pr2036/146/fetch-publication.xml.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/fetch-publication.xml.stdout.txt
    sha256: 0ae38e3f8e622ef59a24ce25416a610cb2584d98548bfce28790c4996df70560
    role: context
  - path: .temp/pr2036/146/frozen-target.json
    sha256: 4219ecaf3269d5c7e8e9c783f7b57b989247b8effc47f2e4e3e96c6869d5372f
    role: context
  - path: .temp/pr2036/146/frozen-target.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/frozen-target.stdout.txt
    sha256: cfe33d321709ed3f502b1e4740464b352dbfe08fa226fe2b4c6a79f9c78d9f8a
    role: context
  - path: .temp/pr2036/146/imodulon-catalog.json
    sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
    role: context
  - path: .temp/pr2036/146/inspect.json
    sha256: 318129378d16b9d77127ac7fd1abb645812d689699f2ebfd974c9466f831235c
    role: context
  - path: .temp/pr2036/146/inspect.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/inspect.stdout.txt
    sha256: 34bb45590c36a54d3524163dcc87b04f72a784049440837c044722d79ff3e923
    role: context
  - path: .temp/pr2036/146/inspection.json
    sha256: 34bb45590c36a54d3524163dcc87b04f72a784049440837c044722d79ff3e923
    role: context
  - path: .temp/pr2036/146/lineage.json
    sha256: 46b8c57d076840a2919e9b363caebcdc4119e0f76ef5326fe0fc9ec7448c8365
    role: context
  - path: .temp/pr2036/146/local-search-v2.json
    sha256: 69cd688b80a58727f5147057ad154d0fbdcc9c9f1fab6fe78015838614bf614b
    role: context
  - path: .temp/pr2036/146/local-search-v2.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/local-search-v2.stdout.txt
    sha256: 71b5c5c3c25f07fda13c4ef1a3391085c6bfda6d90bca0f92ee1ae142053a4af
    role: context
  - path: .temp/pr2036/146/local-search.json
    sha256: eb51b6157db7f72ede107949f3cbfc7f5c01794d55d38db86400dd106ec88573
    role: context
  - path: .temp/pr2036/146/local-search.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/local-search.stdout.txt
    sha256: 4f6f633dd38a0d5f9ee99df44d39605f375d76257d2cb48f76b3f5cbcf032cb0
    role: context
  - path: .temp/pr2036/146/normalize-cache-names-check.json
    sha256: c4768609c324d9cc9f530020fdd9f198e6297b525ee879c62e1c119308d683e9
    role: context
  - path: .temp/pr2036/146/normalize-cache-names-check.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/normalize-cache-names-check.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/ontology-authorities.json
    sha256: 25b9a0ab0bc1821fa45fe5b0c2c99ae24f9153c7b969271f4a12704073865a22
    role: context
  - path: .temp/pr2036/146/primary-sections.json
    sha256: 1b594e3743ea40be8cff140267f783d5934e4a946007cb3b10aa88900e4a57b1
    role: context
  - path: .temp/pr2036/146/primary.xml
    sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
    role: context
  - path: .temp/pr2036/146/publication.xml
    sha256: 0ae38e3f8e622ef59a24ce25416a610cb2584d98548bfce28790c4996df70560
    role: context
  - path: .temp/pr2036/146/snippet-replay.json
    sha256: 8249f59081954a5a872bdc4617ddfe731b200351911339a50867d1e17135006d
    role: context
  - path: .temp/pr2036/146/source-family-ancestry.json
    sha256: 9ecc77985eb9a674573866a841236c6d7261c0e1517ea3e87eb0bd1d2ef2789c
    role: context
  - path: .temp/pr2036/146/sources.json
    sha256: 10501a51381a7c3571672af38a863bd998f142c4e531eccf0b19830495db795b
    role: context
  - path: .temp/pr2036/146/strict.tsv
    sha256: b184ed5450b968070bb6c75648407e388f41a1eaf7017890723cf560999fc3f7
    role: context
  - path: .temp/pr2036/146/target-diff.json
    sha256: b1177b588355bb0ec5d06628f908746a5329db52dfd1bc76b3f143a2abe752c5
    role: context
  - path: .temp/pr2036/146/target-diff.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/target-diff.stdout.txt
    sha256: f7e80152f5cc3d46de95ce9902979fb53c3b1837f656594b9f3d3d10e47f4ec4
    role: context
  - path: .temp/pr2036/146/target-network.json
    sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
    role: context
  - path: .temp/pr2036/146/target-semantic-diff.json
    sha256: 31479d3f16726fb7524642ff571f952909094cd0f231146c081b298e1e3bc132
    role: context
  - path: .temp/pr2036/146/targets.json
    sha256: 01df63dce7f32008e56937d06ca4d3f5dde12ed609e2688703d1f6ba99ea58e0
    role: context
  - path: .temp/pr2036/146/validate-gtdb-domain.json
    sha256: 55af40429f5f0adff3476f84ca934bc1d7f26da71f784c651ec5e6b5f991e6aa
    role: context
  - path: .temp/pr2036/146/validate-gtdb-domain.stderr.txt
    sha256: d623fcd592d3d790d50bbb67ab1dd55f5dfdfefd2005cb1e29df2c5b46463683
    role: context
  - path: .temp/pr2036/146/validate-gtdb-domain.stdout.txt
    sha256: ede937293c42cad366f434dce49a485a9a0c56fe86620b52ca243ad10e09ecae
    role: context
  - path: .temp/pr2036/146/validate-gtdb.json
    sha256: 41f3b2ec6a2779586b3701112a117bf55514bd01a26ea617eaefeb260e0159b4
    role: context
  - path: .temp/pr2036/146/validate-gtdb.stderr.txt
    sha256: ca23d5b43ccb8e21b48bdf5fb5f27bc66f2b3abaf9518ba40f9706112c8a5892
    role: context
  - path: .temp/pr2036/146/validate-gtdb.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/validate-history.json
    sha256: 7db945df43fddb7ead0379b043c0ec5bc2c0629814c2c67637e2d51efd0a37ad
    role: context
  - path: .temp/pr2036/146/validate-history.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/validate-history.stdout.txt
    sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
    role: context
  - path: .temp/pr2036/146/validate-references-explained.json
    sha256: ee3bf2aa24153e1255e878b33090241d2fd9ff9c3ebd41c55617cb0c92965a00
    role: context
  - path: .temp/pr2036/146/validate-references-explained.stderr.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/validate-references-explained.stdout.txt
    sha256: 1478636b6e9c6958ffd66ab68f0bad3330d8a01e32e4656b105fb5be1d2470c4
    role: context
  - path: .temp/pr2036/146/validate-strict.json
    sha256: 5af1a3cc7c6b3ea02cfc634b1443b9a90748730878019b6843f8255a0d6a4ba5
    role: context
  - path: .temp/pr2036/146/validate-strict.stderr.txt
    sha256: 828ed8df54725ecf71ebcf1e9acabc89f775b08c1da9b8e52331c5bda2726285
    role: context
  - path: .temp/pr2036/146/validate-strict.stdout.txt
    sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
    role: context
  - path: .temp/pr2036/146/validate-terms.json
    sha256: ae7745bbce018948f2e5ec7e9f6a450ca7d5a3075673b1ff211be4246f585376
    role: context
  - path: .temp/pr2036/146/validate-terms.stderr.txt
    sha256: 9639840217cb76487d73849e011b67272ae2840cee86c87ca2b57dffbe780b6b
    role: context
  - path: .temp/pr2036/146/validate-terms.stdout.txt
    sha256: 23acda1c1d3194d12bc947d897d07de83f4a076a9d93c135148885108530e018
    role: context
  - path: .temp/pr2036/146/validate.json
    sha256: 393355a17a3da7d5df3d5628ed6b3db6872b43012ad8dde430479f37884a428a
    role: context
  - path: .temp/pr2036/146/validate.stderr.txt
    sha256: 6da75c80355a6ae190c79fdcb77d0e8c39650abb296f0d445faa16bba838a4d3
    role: context
  - path: .temp/pr2036/146/validate.stdout.txt
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
  - path: history/README.md
    sha256: 86c0347d77402bcecdec466b01974ad53beddb9cf1bd17cf085674970542a101
    role: context
  - path: history/records/Anammox_Granule_Metabolic_Interaction_Community/2026-08-31T075013Z-claude-code-d590a8.yaml
    sha256: ce6e53602b7729da68827d0a6ec5daf261626a92cbed85b97a2bb279791cf3bd
    role: context
  - path: history/records/Anammox_Granule_Metabolic_Interaction_Community/2026-10-05T084244Z-codex-0dd10f.yaml
    sha256: c6bd4fecc697f4291f022c46b484f5c42b7004638e8b25b125258615acc1ac04
    role: context
  - path: history/records/Anammox_Granule_Metabolic_Interaction_Community/2026-11-05T165000Z-antigravity-2120a1.yaml
    sha256: 57f2e2500f3d08ba62d326a74cec3aeeb63d81d2459ab3c8357c2494c19bc89a
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    sha256: f28da9a5d2087b5d6d329f9dfd746d6e9efa24238d4c47475734392f9c3ec538
    role: target
  - path: references_cache/doi_10.1038_ncomms15416.txt
    sha256: 2349c596e93290d7185340aadc46317fe429a53146d530fab17f256f688c9b4f
    role: context
  - path: reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
    sha256: e21a355f676730e8e7e6de6ea663017c9b09e05a824ff383a272ab9f1399fd70
    role: context
  - path: reviews/structured/20261020T073708Z-anammox-granule-record/review.yaml
    sha256: 84e3dbcc23ce271a33583380f8af0a38e9aa2c0f4162bd8cb52c798e4f1c221a
    role: context
  - path: reviews/structured/20261105T144000Z-c7s4-record-deep-audit/review.yaml
    sha256: fe5de3c3f5c6cb21d935abb7c93452c5ef5a125b3c10163a44e9d712faee3ccd
    role: context
  - path: reviews/structured/20261105T144100Z-c7s4-frozen-cohort-review/review.yaml
    sha256: 6d4bb3018610ed2377507923b3b643e54165c1e645d7fddbad88ce25175a5826
    role: context
  - path: reviews/structured/20261105T171000Z-c7s5-remediation-verification/review.yaml
    sha256: 1e05838838578c4c17bd6e24742b3d38b882600b38a3ed45fff2eadd222c19fa
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/adhoc/pr2036_146_audit.py
    sha256: fa1844efa017767079485f2e76302e831517742c38df239054722241417b4e94
    role: context
  - path: scripts/adhoc/pr2036_146_review.py
    sha256: f18b9a0a88a35bbff80e81a346861e81f074d25af9c9307dfb957d320b5a3252
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
- target_id: CommunityMech:000146
  path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  label: Anammox Granule Metabolic Interaction Community
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
scope:
  description: 'Whole current record: three grouped taxonomic entries, four interaction
    nodes, three downstream arrows, 17 evidence occurrences, environmental and cultivation
    claims, dataset representation and three history sidecars. Primary abstract, introduction,
    Results, Discussion, Methods and Tables 1 and 2 were read; public publication,
    project and sample metadata were checked.'
  selection: PR 2036 stale-target refresh against current main. The parsed diff contains
    three abundance levels, two evidence items and one embedded history entry; other
    target data are semantically unchanged. Every original finding was reassessed.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000146
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml'
  target_ids:
  - CommunityMech:000146
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history checks passed; cache-name preflight was clean.
    All inspected canonical inputs retain their initial hashes. Both corpus warning
    exits remain visible.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml\
    \ --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv\n\
    Validating 1 files with 17 workers; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv"
  target_ids:
  - CommunityMech:000146
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-strict kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history checks passed; cache-name preflight was clean.
    All inspected canonical inputs retain their initial hashes. Both corpus warning
    exits remain visible.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000146
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-terms kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history checks passed; cache-name preflight was clean.
    All inspected canonical inputs retain their initial hashes. Both corpus warning
    exits remain visible.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000146
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-gtdb kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history checks passed; cache-name preflight was clean.
    All inspected canonical inputs retain their initial hashes. Both corpus warning
    exits remain visible.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml'
  target_ids:
  - CommunityMech:000146
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-gtdb-domain kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history checks passed; cache-name preflight was clean.
    All inspected canonical inputs retain their initial hashes. Both corpus warning
    exits remain visible.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: No issues found
  target_ids:
  - CommunityMech:000146
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-history history/records/Anammox_Granule_Metabolic_Interaction_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history checks passed; cache-name preflight was clean.
    All inspected canonical inputs retain their initial hashes. Both corpus warning
    exits remain visible.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Command completed without reported issues.
  target_ids:
  - CommunityMech:000146
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history checks passed; cache-name preflight was clean.
    All inspected canonical inputs retain their initial hashes. Both corpus warning
    exits remain visible.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: "Validating kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000146
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-references-explained kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history checks passed; cache-name preflight was clean.
    All inspected canonical inputs retain their initial hashes. Both corpus warning
    exits remain visible.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Actual fresh corpus run: 503 records, 44 warnings in 16 records, zero
    errors; exit 1 retained. The current target has no network issues. No canonical
    corpus remediation was performed.'
  target_ids:
  - CommunityMech:000146
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Focused target/history checks passed; cache-name preflight was clean.
    All inspected canonical inputs retain their initial hashes. Both corpus warning
    exits remain visible.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Actual fresh corpus run: 503 records, 44 warnings in 16 records, zero
    errors; exit 1 retained. The current target has no network issues. No canonical
    corpus remediation was performed.'
  target_ids:
  - CommunityMech:000146
  command: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Focused target/history checks passed; cache-name preflight was clean.
    All inspected canonical inputs retain their initial hashes. Both corpus warning
    exits remain visible.
- check_id: structured-expression-adapter
  name: Structured expression-source applicability
  status: not_applicable
  required: false
  summary: Native runner unavailable in bounded lookup; public catalog fallback inspected.
    No exact source-population dataset match was found in the returned catalog. This
    is not negative evidence for the study's expression claims.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - adapter-discovery
  - expression-catalog
  - biosample_transcriptome
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  locator: 'Whole current target: three grouped taxa, four nodes, three arrows and
    all 17 evidence occurrences'
  summary: Record represents a laboratory granular-sludge enrichment, with broader
    placeholders for multiple MAGs rather than three isolates. Graph descriptions
    preserve inferred exchange; exact taxon identifiers and summary require separate
    assessment.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: f28da9a5d2087b5d6d329f9dfd746d6e9efa24238d4c47475734392f9c3ec538
- evidence_id: primary
  kind: primary_source
  reference: doi:10.1038/ncomms15416
  locator: Fresh Europe PMC PMC5460018 XML; abstract, introduction, all Results, Discussion,
    Methods, Table 1 and Table 2 text. Snapshot and retrieval receipt frozen under
    .temp/pr2036/146.
  summary: The full main article and table text were inspected. The study reconstructs
    metabolic potential from community DNA/RNA mapping and does not directly trace
    partner-resolved exchange. Supplementary files and rendered figure geometry were
    not inspected.
  support: supports
  accessed_at: '2026-11-05T23:50:59.650341Z'
  snapshot_sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
- evidence_id: amx-identity
  kind: primary_source
  reference: doi:10.1038/ncomms15416
  locator: 'Results: Anammox metatranscriptomic insights; Table1 AMX1 row'
  summary: AMX1 is Brocadia-affiliated and related to both named species, not identified
    as sinica. Table1 resolves genus only. A nearest representative does not justify
    exact species identity in the graph.
  support: supports
  accessed_at: '2026-11-05T23:50:59.650341Z'
  quote: closely related to both
  snapshot_sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
- evidence_id: chb-identity
  kind: primary_source
  reference: doi:10.1038/ncomms15416
  locator: Table1 CHB1 and CHB2 rows
  summary: CHB1 belongs to source Ignavibacteria/ Ignavibacteriales/ Melioribacteraceae;
    CHB2 to Ignavibacteriaceae. Historical Chlorobi wording must be interpreted through
    these finer source placements.
  support: supports
  accessed_at: '2026-11-05T23:50:59.650341Z'
  snapshot_sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
- evidence_id: lineage
  kind: authority
  reference: OAK local ncbitaxon.db
  locator: Fresh rdfs:subClassOf ancestry for NCBITaxon:1334117, NCBITaxon:795749
    and NCBITaxon:1090
  summary: Melioribacteraceae and Ignavibacteriaceae descend through Ignavibacteria
    and Ignavibacteriota (NCBITaxon:1134404), not Chlorobiota (NCBITaxon:1090), in
    the local NCBI authority. These are the families assigned to CHB1 and CHB2 in
    Table 1. This confirms the clade conflict despite valid labels; the existing GTDB
    block follows the incorrect anchor and has not been independently re-grounded.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 9ecc77985eb9a674573866a841236c6d7261c0e1517ea3e87eb0bd1d2ef2789c
- evidence_id: ontology
  kind: authority
  reference: OAK local NCBITaxon,ENVO,CHEBI and GO snapshots
  locator: Ten curated ID-label pairs; alternative ENVO setting identifiers checked
    separately
  summary: All ten curated labels match current local OAK authority labels. ENVO:00002123
    resolves to bioreactor and ENVO:01001405 to laboratory environment. These provide
    appropriate setting alternatives; syntax and matching labels cannot establish
    that the target organism belongs to a mapped taxon.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 25b9a0ab0bc1821fa45fe5b0c2c99ae24f9153c7b969271f4a12704073865a22
- evidence_id: anammox
  kind: primary_source
  reference: doi:10.1038/ncomms15416
  locator: 'Results: Anammox metatranscriptomic insights'
  summary: AMX1 expressed anammox-related genes. Reactor function and expression support
    active potential; they do not validate the species assignment or downstream partner
    flux.
  support: supports
  accessed_at: '2026-11-05T23:50:59.650341Z'
  quote: genes involved in anammox metabolism
  snapshot_sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
- evidence_id: nitrite
  kind: primary_source
  reference: doi:10.1038/ncomms15416
  locator: 'Results: Denitrification gene expression; Discussion'
  summary: Nitrate-reductase expression supports candidate recycling, with other reduction
    routes and component-expression caveats. A completed exchange loop is proposed
    rather than measured.
  support: supports
  accessed_at: '2026-11-05T23:50:59.650341Z'
  quote: could facilitate a nitrite loop
  snapshot_sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
- evidence_id: peptides
  kind: primary_source
  reference: doi:10.1038/ncomms15416
  locator: 'Results: Amino acid and carbohydrate catabolism; Discussion'
  summary: Peptidase expression and predicted localization support proposed protein
    scavenging. Cited tracer evidence comes from other work, not this experiment;
    substrate origin and intermember transfer were not traced.
  support: supports
  accessed_at: '2026-11-05T23:50:59.650341Z'
  quote: may be involved
  snapshot_sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
- evidence_id: donors
  kind: primary_source
  reference: doi:10.1038/ncomms15416
  locator: 'Results: Carbon and energy metabolism; Discussion'
  summary: Acetate pathway direction remains unresolved; candidate formate/hydrogen
    use does not prove AMX1 secretion. Wastewater-derived carbon prevents exclusive
    attribution of heterotrophic substrates to AMX1.
  support: supports
  accessed_at: '2026-11-05T23:50:59.650341Z'
  quote: it is unclear
  snapshot_sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
- evidence_id: operation
  kind: primary_source
  reference: doi:10.1038/ncomms15416
  locator: 'Methods: Bioreactor operation; Table2; introductory granule background'
  summary: Two-stage wastewater treatment feeds the laboratory anammox reactor with
    filtrate after nitritation. Anaerobic operation is described directly. The record’s
    genome-recovery snippet does not support medium/atmosphere. Oxygen diffusion and
    matrix statements in the introduction are general background, not same-system
    gradient measurements.
  support: supports
  accessed_at: '2026-11-05T23:50:59.650341Z'
  snapshot_sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
- evidence_id: abundance
  kind: primary_source
  reference: doi:10.1038/ncomms15416
  locator: 'Results: Microbial community abundance and gene expression; Methods: metatranscriptomics'
  summary: AMX1 is approximately 62% of the source abundance proxy and 54% of its
    expression proxy; CHB1 is approximately 21% and 26%, respectively. DOMINANT and
    ABUNDANT are defensible ordinal summaries under AbundanceEnum. The source describes
    other flanking genomes as moderately abundant, supporting COMMON as a qualitative
    aggregate descriptor, not a measured percentage for every taxon. These are genome-length-normalized
    DNA/RNA mapping proxies; DNA covers two collection events while RNA comes from
    the second. No absolute cell count or combined guild percentage is established.
  support: supports
  accessed_at: '2026-11-05T23:50:59.650341Z'
  snapshot_sha256: 97f447184065af2bd3ac61582bac504aefdf99e13af9d8511806d074bdcf6db3
- evidence_id: pubmed
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=28561030&retmode=xml
  locator: Independent metadata retrieval
  summary: Publication identity agrees with the primary article.
  support: supports
  accessed_at: '2026-11-05T23:51:00.571247Z'
  snapshot_sha256: 0ae38e3f8e622ef59a24ce25416a610cb2584d98548bfce28790c4996df70560
- evidence_id: crossref
  kind: database
  reference: https://api.crossref.org/works/10.1038/ncomms15416
  locator: Independent metadata retrieval
  summary: Publication identity agrees with the primary article.
  support: supports
  accessed_at: '2026-11-05T23:51:01.289363Z'
  snapshot_sha256: c50626648afbf656a34b1c1e42027b646ee65f010deb2ceaeb4e3ffb5e5cf061
- evidence_id: bioproject
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=bioproject&id=343219&retmode=json
  locator: 'NCBI BioProject esummary result 343219: accession, title, project description
    and data type'
  summary: PRJNA343219 describes a 5 L laboratory anammox sequencing-batch reactor
    fed with anaerobic digester filtrate after nitritation. It matches the article's
    study context; the metadata does not itself audit raw sequence content.
  support: supports
  accessed_at: '2026-11-05T23:51:01.800243Z'
  snapshot_sha256: 34e4e4046e5b05fa94de66b64f1c6c76447a0431318b61e8ed50b66556af8b37
- evidence_id: biosample_metagenome
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN05785375,SAMN05785376,SAMN05785373&retmode=xml
  locator: 'BioSample XML row SAMN05785375: accession, title, sample identifiers and
    collection date'
  summary: SAMN05785375 identifies the source-described Illumina HiSeq 2000 metagenome,
    2 x 125 bp; collected September 9, 2015; SRA sample SRS1713242. Metadata validates
    accession and sample type, not every deposited read or inferred MAG.
  support: supports
  accessed_at: '2026-11-05T23:51:02.416145Z'
  snapshot_sha256: 5d0c91117de7380e060a34eec7e9d8aacc8694941741e73f3af0dc6bb1614b3f
- evidence_id: biosample_transcriptome
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN05785375,SAMN05785376,SAMN05785373&retmode=xml
  locator: 'BioSample XML row SAMN05785376: accession, title, sample identifiers and
    collection date'
  summary: SAMN05785376 identifies the source-described Illumina HiSeq 2000 metatranscriptome,
    2 x 125 bp; collected September 9, 2015; SRA sample SRS1713243. Metadata validates
    accession and sample type, not every deposited read or inferred MAG.
  support: supports
  accessed_at: '2026-11-05T23:51:02.416145Z'
  snapshot_sha256: 5d0c91117de7380e060a34eec7e9d8aacc8694941741e73f3af0dc6bb1614b3f
- evidence_id: biosample_miseq
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN05785375,SAMN05785376,SAMN05785373&retmode=xml
  locator: 'BioSample XML row SAMN05785373: accession, title, sample identifiers and
    collection date'
  summary: SAMN05785373 identifies the source-described Illumina MiSeq metagenome
    S1, 2 x 300 bp; collected September 4, 2013; SRA sample SRS1713240. Metadata validates
    accession and sample type, not every deposited read or inferred MAG.
  support: supports
  accessed_at: '2026-11-05T23:51:02.416145Z'
  snapshot_sha256: 5d0c91117de7380e060a34eec7e9d8aacc8694941741e73f3af0dc6bb1614b3f
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  locator: All 17 current evidence placements, including duplicated cultivation text
    and two newly added abundance quotations
  summary: All 17 snippets match the freshly retrieved primary XML after NFKC and
    whitespace normalization with inline tags joined. The two new abundance quotations
    preserve the source wording. Exact text matching does not establish that a genome-recovery
    fragment supports atmosphere or influent identity.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 8249f59081954a5a872bdc4617ddfe731b200351911339a50867d1e17135006d
- evidence_id: history
  kind: record_content
  reference: reports/causal_graph_review/decisions/20261005-twelve-records-batch4.yaml
  locator: Target graph decision, all three history sidecars and current embedded
    history
  summary: The prior graph decision explicitly qualified exchange and excluded non-graph
    metadata from certification, including unresolved species identity. The November
    5 sidecar accurately describes the three abundance annotations and two added evidence
    items. Its scope is abundance annotation; it does not certify taxonomic identity
    or the eight outstanding findings.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
- evidence_id: local-search
  kind: search
  reference: references_cache;history;reports/causal_graph_review/decisions;kb/taxa
  locator: DOI and target filename search including ignored and hidden files
  summary: An ignored-inclusive bounded search located the cache, history and prior
    decision. No file matching this DOI or exact slug was returned from kb/taxa; this
    is not an exhaustive search for every taxonomic synonym. Missing linkage observations
    concern the entire current target, not absence of matches in external registries.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  search_scope: rg --no-ignore --hidden -l 'ncomms15416|Anammox_Granule_Metabolic_Interaction_Community'
    references_cache history reports/causal_graph_review/decisions kb/taxa
  snapshot_sha256: 71b5c5c3c25f07fda13c4ef1a3391085c6bfda6d90bca0f92ee1ae142053a4af
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261020T073708Z-anammox-granule-record/review.yaml
  locator: All eight findings and their action plans
  summary: All eight original findings were reassessed and remain open. Stable issue
    keys and exact predecessor finding references are retained.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 84e3dbcc23ce271a33583380f8af0a38e9aa2c0f4162bd8cb52c798e4f1c221a
- evidence_id: target-change
  kind: record_content
  reference: .temp/pr2036/146/target-semantic-diff.json
  locator: Parsed comparison against the predecessor's frozen Git target; textual
    diff separately retained
  summary: Only three abundance levels, two evidence objects and one embedded history
    entry were added. The remaining text diff is serialization, not a biological or
    claim-level change.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 31479d3f16726fb7524642ff571f952909094cd0f231146c081b298e1e3bc132
- evidence_id: abundance-history
  kind: record_content
  reference: history/records/Anammox_Granule_Metabolic_Interaction_Community/2026-11-05T165000Z-antigravity-2120a1.yaml
  locator: events[0] and current curation_history[1]
  summary: The history description matches the source-backed additions. The narrow
    missing-abundance-field issue is resolved in the inspected later review; this
    observation does not retire unrelated taxonomic findings or rewrite prior history.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 57f2e2500f3d08ba62d326a74cec3aeeb63d81d2459ab3c8357c2494c19bc89a
- evidence_id: abundance-review-context
  kind: prior_review
  reference: reviews/structured/20261105T171000Z-c7s5-remediation-verification/review.yaml
  locator: Single-target finding c7s4-000146-anammox-granule-abundance-levels and
    its referenced Stage 4 occurrences
  summary: The later review records a resolved missing-field observation. Current
    field presence and fresh source inspection substantiate only that narrow repair.
    This successor does not create another terminal disposition for that key and does
    not imply corrected AMX1 or CHB taxonomy.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 1e05838838578c4c17bd6e24742b3d38b882600b38a3ed45fff2eadd222c19fa
- evidence_id: abundance-schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: AbundanceEnum and Taxon.abundance_level
  summary: The abundance enum expresses ordinal prominence, explicitly not percentages.
    It supports a dominant AMX1, major CHB1-associated entry and moderately represented
    flanking group while retaining the exact proxy and group scope in evidence.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
- evidence_id: alternative-settings
  kind: authority
  reference: .temp/pr2036/146/alternative-settings.json
  locator: Direct OAK lookup of two candidate ENVO settings
  summary: Both bioreactor and laboratory environment labels resolve. The appropriate
    choice is a later curation decision grounded in the laboratory experimental setting.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: fe667cf2b60972714c408fe3a6efbd45f715efad0cbe1b0fbb2e628b939c800d
- evidence_id: target-network
  kind: validation
  reference: .temp/pr2036/146/target-network.json
  locator: Fresh NetworkIntegrityAuditor.audit_community result
  summary: The entire target has no structural network warnings. This does not establish
    the scientific correctness of participant identifiers or hypothetical transfer
    edges.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
- evidence_id: adapter-discovery
  kind: search
  reference: .temp/pr2036/146/adapter-discovery.json
  locator: Executable lookup and two exact expected sibling CLAW paths, including
    ignored paths
  summary: No installed kg-microbe-sources runner was found, and both inspected sibling
    checkout paths are absent. This is a bounded lookup, not a claim about every filesystem
    location.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 6f8de737447babd85c8a656e25df93658e2bf516f614f6a432523e97d40bb049
  search_scope: PATH lookup via shutil.which plus exact filesystem existence checks
    of /Users/marcin/Documents/VIMSS/ontology/Mechs/culturebotai-claw and /Users/marcin/Documents/VIMSS/ontology/culturebotai-claw,
    including gitignored paths. No machine-wide absence claim.
- evidence_id: expression-catalog
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Complete returned public catalog: 20 organism entries and their dataset
    keys'
  summary: No returned catalog organism corresponds to the source Brocadia or Ignavibacteria
    populations, and no exact AMX1/CHB study dataset is listed. A broad Bacteria placeholder
    does not establish a strain match to another organism's expression modules. The
    actual study's metatranscriptomic source and metadata provide the applicable evidence.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  locator: Actual execution 2026-11-05T23:50:58.814331Z to 2026-11-05T23:50:59.369161Z;
    receipt .temp/pr2036/146/validate.json
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml'
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 393355a17a3da7d5df3d5628ed6b3db6872b43012ad8dde430479f37884a428a
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-strict kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv
  locator: Actual execution 2026-11-05T23:50:59.369361Z to 2026-11-05T23:51:01.295299Z;
    receipt .temp/pr2036/146/validate-strict.json
  summary: "uv run python scripts/validate_strict.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml\
    \ --out /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv\n\
    Validating 1 files with 17 workers; schema=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/.temp/pr2036/146/strict.tsv"
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 5af1a3cc7c6b3ea02cfc634b1443b9a90748730878019b6843f8255a0d6a4ba5
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-terms kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  locator: Actual execution 2026-11-05T23:51:01.295577Z to 2026-11-05T23:51:02.354733Z;
    receipt .temp/pr2036/146/validate-terms.json
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: ae7745bbce018948f2e5ec7e9f6a450ca7d5a3075673b1ff211be4246f585376
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-gtdb kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  locator: Actual execution 2026-11-05T23:51:02.354918Z to 2026-11-05T23:51:02.415526Z;
    receipt .temp/pr2036/146/validate-gtdb.json
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 41f3b2ec6a2779586b3701112a117bf55514bd01a26ea617eaefeb260e0159b4
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-gtdb-domain kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  locator: Actual execution 2026-11-05T23:51:02.415782Z to 2026-11-05T23:51:03.346729Z;
    receipt .temp/pr2036/146/validate-gtdb-domain.json
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml'
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 55af40429f5f0adff3476f84ca934bc1d7f26da71f784c651ec5e6b5f991e6aa
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-history history/records/Anammox_Granule_Metabolic_Interaction_Community
  locator: Actual execution 2026-11-05T23:51:03.346945Z to 2026-11-05T23:51:04.354664Z;
    receipt .temp/pr2036/146/validate-history.json
  summary: No issues found
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 7db945df43fddb7ead0379b043c0ec5bc2c0629814c2c67637e2d51efd0a37ad
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-11-05T23:51:04.354864Z to 2026-11-05T23:51:04.393839Z;
    receipt .temp/pr2036/146/normalize-cache-names-check.json
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: c4768609c324d9cc9f530020fdd9f198e6297b525ee879c62e1c119308d683e9
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv validate-references-explained kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  locator: Actual execution 2026-11-05T23:51:04.394065Z to 2026-11-05T23:51:05.233774Z;
    receipt .temp/pr2036/146/validate-references-explained.json
  summary: "Validating kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: ee3bf2aa24153e1255e878b33090241d2fd9ff9c3ebd41c55617cb0c92965a00
- evidence_id: check-audit-network
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv audit-network
  locator: Actual execution 2026-11-05T23:51:05.233957Z to 2026-11-05T23:51:09.628218Z;
    receipt .temp/pr2036/146/audit-network.json
  summary: 'Actual fresh corpus run: 503 records, 44 warnings in 16 records, zero
    errors; exit 1 retained. The current target has no network issues. No canonical
    corpus remediation was performed.'
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 00e8bc5adeff9be15381903c1bcaa491f1629cfa1091dd73cb0259442ab35c26
- evidence_id: check-check-network-quality
  kind: validation
  reference: JUST_NO_DOTENV=true PYTHONPATH=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2036-batch03/src
    UV_CACHE_DIR=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.temp/uv-cache
    UV_NO_SYNC=1 UV_OFFLINE=1 UV_PROJECT_ENVIRONMENT=/Users/marcin/Documents/VIMSS/ontology/Mechs/CommunityMech/.temp/pr-2034-canary/.venv
    just --no-dotenv check-network-quality
  locator: Actual execution 2026-11-05T23:51:09.628427Z to 2026-11-05T23:51:13.846281Z;
    receipt .temp/pr2036/146/check-network-quality.json
  summary: 'Actual fresh corpus run: 503 records, 44 warnings in 16 records, zero
    errors; exit 1 retained. The current target has no network issues. No canonical
    corpus remediation was performed.'
  support: supports
  accessed_at: '2026-11-05T23:55:40.767915Z'
  snapshot_sha256: 31061c9dfacfc1e097e6c16e10d38a4cf9210bf635d8ee7beff96616379b1f0f
assessments:
- assessment_id: identity
  area: identity
  topic: Community and experiment scope
  outcome: supported
  summary: Publication and record concern the same laboratory anammox granule enrichment.
    Three grouped entries are not three isolated organisms or an exhaustive census
    of the 17 recovered genomes.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - primary
  - pubmed
  - crossref
  dimensions:
  - name: source_strain
    value: AMX1, CHB1, CHB2 and aggregated flanking MAGs
    definition: Genome bins are not confirmed named-species isolates.
    evidence_ids:
    - amx-identity
    - chb-identity
  - name: community_scope
    value: Laboratory granular-sludge enrichment
    definition: Study-specific community, not a universal wastewater consortium.
    evidence_ids:
    - primary
  - name: experimental_setting
    value: Downstream anammox reactor in two-stage treatment
    definition: Upstream nitritation conditions must not be transferred to this reactor.
    evidence_ids:
    - operation
  - name: medium
    value: Wastewater filtrate after nitritation
    definition: Residual organic carbon prevents exclusive anammox-derived substrate
      attribution.
    evidence_ids:
    - operation
    - donors
  - name: evidence_tier
    value: Metagenomics and metatranscriptomics
    definition: Expression and reconstructed capacity are not resolved exchange flux.
    evidence_ids:
    - primary
    - nitrite
    - peptides
- assessment_id: taxonomy
  area: grounding
  topic: taxonomy[0..2] and repeated graph participants
  outcome: concern
  summary: AMX1 species precision is unsupported; CHB family ancestry contradicts
    the modern Chlorobiota anchor. Broad flanking Bacteria is a disclosed aggregate.
    Valid ID-label pairs and GTDB syntax do not repair wrong biological attribution.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - amx-identity
  - chb-identity
  - lineage
  - ontology
- assessment_id: abundance
  area: evidence
  topic: taxonomy abundance values
  outcome: supported
  summary: The new DOMINANT, ABUNDANT and COMMON levels are consistent qualitative
    summaries of the source's AMX1, CHB1-associated and moderately represented flanking
    populations. AMX1 and CHB1 values are DNA/RNA mapping proxies for recovered MAGs;
    CHB1 percentages must not be assigned to every CHB genome or a modern named clade,
    and COMMON does not encode a combined guild percentage. The two new snippets match
    the source exactly after documented normalization.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - abundance
  - abundance-schema
  - snippets
  - target-change
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: Anammox Ammonium-Nitrite Conversion'
  outcome: concern
  summary: Expression supports the qualified anammox function, but the participant’s
    sinica identity is unsupported.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - anammox
  - amx-identity
  details: AMX1 is encoded as NCBITaxon:795830, but Table 1 supports Brocadia affiliation
    rather than confirmed sinica identity. Ammonium/nitrite use and expressed anammox
    potential are supported at the study-MAG level. The linked primary evidence gives
    exact source locators and brief quotations. No stronger exchange claim is justified.
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Heterotrophic Nitrite Loop'
  outcome: concern
  summary: The loop is appropriately hypothetical; participant identity and summary
    wording still need correction.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - nitrite
  - amx-identity
  details: Participants are aggregated Bacteria and AMX1; proposed direction heterotrophic
    nitrate reduction to nitrite returning to anammox. Source DOI10.1038/ncomms15416;
    exact locator and short verbatim snippet in linked evidence. Mechanistic qualification
    is retained; concerns are attribution, not a request to strengthen causation.
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: EPS Peptide Scavenging by Chlorobi'
  outcome: concern
  summary: Peptide scavenging is explicitly inferred, but Chlorobiota and sinica identifiers
    misrepresent source population resolution.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - peptides
  - amx-identity
  - lineage
  details: Participants AMX1 and CHB populations; proposed direction extracellular
    protein toward heterotrophic scavengers. Proteolysis is supported as expressed
    potential. Source DOI10.1038/ncomms15416; exact locator and short verbatim snippet
    in linked evidence. Mechanistic qualification is retained; concerns are attribution,
    not a request to strengthen causation.
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Detritus and Small-Donor Scavenging'
  outcome: concern
  summary: The node preserves unresolved acetate direction and carbon provenance;
    its AMX1 species identifier remains unsupported.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - donors
  - amx-identity
  details: Participants AMX1 and aggregate flanking bacteria; candidate detritus/small-donor
    use, not verified secretion and uptake. Source DOI10.1038/ncomms15416; exact locator
    and short verbatim snippet in linked evidence. Mechanistic qualification is retained;
    concerns are attribution, not a request to strengthen causation.
- assessment_id: edge-0
  area: graph
  topic: ecological_interactions[0].downstream[0]
  outcome: concern
  summary: The arrow is correctly hypothetical, while its upstream AMX1 species attribution
    requires correction.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - nitrite
  - amx-identity
  details: From Anammox Ammonium-Nitrite Conversion to Heterotrophic Nitrite Loop.
    HYPOTHESIZED - anammox-derived nitrate could supply heterotrophic nitrate reduction
    and a nitrite-return loop; expression supports potential but not the exchanged
    flux. Participants AMX1 and the corresponding heterotrophic group. Direction is
    proposed substrate provision, not measured transfer. Same-study expression supports
    potential only; source locator/snippet in linked evidence.
- assessment_id: edge-1
  area: graph
  topic: ecological_interactions[0].downstream[1]
  outcome: concern
  summary: The arrow is correctly hypothetical, while its upstream AMX1 species attribution
    requires correction.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - peptides
  - amx-identity
  - lineage
  details: From Anammox Ammonium-Nitrite Conversion to EPS Peptide Scavenging by Chlorobi.
    HYPOTHESIZED - anammox-associated extracellular material could feed heterotrophic
    proteolysis; the source of consumed protein and the transfer were not traced in
    this study. Participants AMX1 and the corresponding heterotrophic group. Direction
    is proposed substrate provision, not measured transfer. Same-study expression
    supports potential only; source locator/snippet in linked evidence.
- assessment_id: edge-2
  area: graph
  topic: ecological_interactions[0].downstream[2]
  outcome: concern
  summary: The arrow is correctly hypothetical, while its upstream AMX1 species attribution
    requires correction.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - donors
  - amx-identity
  details: From Anammox Ammonium-Nitrite Conversion to Detritus and Small-Donor Scavenging.
    HYPOTHESIZED - biomass turnover or released small substrates could feed heterotrophs;
    wastewater-derived organic carbon and unresolved pathway directions prevent exclusive
    attribution to AMX1. Participants AMX1 and the corresponding heterotrophic group.
    Direction is proposed substrate provision, not measured transfer. Same-study expression
    supports potential only; source locator/snippet in linked evidence.
- assessment_id: summary
  area: evidence
  topic: Description and functional roles
  outcome: concern
  summary: Summary verbs and unqualified cross-feeder roles lose the graph’s uncertainty.
    Source transfer hypotheses must not become established exchange claims; the broad
    secondary-fermenter role also overgeneralizes variable capacities where nitrate
    respiration dominates.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - primary
  - nitrite
  - peptides
  - donors
- assessment_id: environment
  area: scope
  topic: environment_term and environmental factors
  outcome: concern
  summary: Wastewater treatment plant describes the feedstock setting, not the laboratory
    reactor itself. Oxygen-diffusion and EPS statements are general introductory context
    rather than same-study spatial measurements.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - operation
  - ontology
- assessment_id: cultivation
  area: evidence
  topic: growth_media[0]
  outcome: concern
  summary: The stated anaerobic reactor context has Methods support, but its attached
    genome-recovery snippet supports neither atmosphere nor influent identity. Sparse
    operational detail is not itself a false claim.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - operation
  - snippets
- assessment_id: datasets
  area: representation
  topic: associated_datasets[0]
  outcome: concern
  summary: An article URL and publisher article number are typed as a metatranscriptomics
    dataset. Verified project/sample accessions should represent data; publication
    belongs in publication resources.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - bioproject
  - biosample_metagenome
  - biosample_transcriptome
  - biosample_miseq
- assessment_id: history
  area: provenance
  topic: History and open discussion
  outcome: supported
  summary: Three sidecars preserve the earlier snippet and graph repairs plus the
    November 5 abundance additions. The new event matches the actual parsed diff.
    The open discussion correctly keeps exchange unresolved; an abundance-field repair
    does not certify taxonomy, datasets or causal claims.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - history
  - abundance-history
  - target-change
- assessment_id: validation
  area: schema
  topic: Native and independent checks
  outcome: supported
  summary: Eight focused/history/preflight commands pass. All 10 curated ID-label
    pairs resolve and all 17 evidence placements match the fresh primary XML. Additional
    family-ancestry inspection confirms identity errors beyond label/syntax gates.
    The target network audit is empty, while both corpus commands retain their real
    warning exits.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - ontology
  - lineage
  - snippets
  - check-validate
  - check-validate-strict
  - check-validate-history
  - check-audit-network
  - target-network
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: concern
  summary: Completeness 95 counts populated fields, including the misrepresented dataset;
    validation quality 79.5 reflects four open major and four open minor findings.
    Neither score is scientific approval.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - record
  - check-audit-network
  metrics:
  - name: completeness
    value: 95
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100, 50 required metadata including roles + 5 environment + 10
      for at least 3 factors + 10 for at least 3 nodes + 5 external resources + 10
      media + 5 datasets + 5 node metabolites). 50 + 5 + 10 + 10 + 0 + 10 + 5 + 5
      = 95. The populated dataset counts mechanically despite its representation defect.
  - name: validation_quality
    value: 79.5
    unit: points
    minimum: 0
    maximum: 100
    definition: clamp(100 - 50*P1 - 10*P2 - 2*P3 + 20*min(mean node evidence/2, 1)
      + 15 if native COMPLETE, 0, 100). Open P1=0, P2=4, P3=4, P4=0; 5 evidence items
      / 4 nodes = 1.25; all 3 declared entries participate structurally. 100 - 40
      - 8 + 12.5 + 15 = 79.5.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count for this target review.
  - name: P2
    value: 4
    unit: findings
    definition: Native severity count for this target review.
  - name: P3
    value: 4
    unit: findings
    definition: Native severity count for this target review.
  - name: P4
    value: 0
    unit: findings
    definition: Native severity count for this target review.
- assessment_id: bounded-abundance-repair
  area: provenance
  topic: Scope of the later abundance-field remediation
  outcome: supported
  summary: Current field presence, exact source evidence and the November 5 sidecar
    support the narrow resolution recorded for c7s4-000146-anammox-granule-abundance-levels.
    This assessment creates no additional terminal disposition and supersedes no unrelated
    or grouped review. The eight original findings remain open, especially AMX1 species
    precision and CHB modern-clade identity.
  target_ids:
  - CommunityMech:000146
  evidence_ids:
  - abundance-review-context
  - abundance-history
  - target-change
  - abundance
  - abundance-schema
findings:
- finding_id: amx-species
  issue_key: cm-000146-amx-species
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: review-checklist.taxonomy
  status: open
  certainty: confirmed
  title: AMX1 is assigned an unsupported species
  description: The source identifies Brocadia affiliation and proximity to both sinica
    and fulgida. Closest-representative notes do not justify exact sinica NCBI/GTDB
    identity propagated through participants.
  target_ids:
  - CommunityMech:000146
  field_paths:
  - taxonomy[0].taxon_term
  - ecological_interactions[*].participating_taxa
  evidence_ids:
  - amx-identity
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T073708Z-anammox-granule-record
    finding_id: amx-species
- finding_id: chb-clade
  issue_key: cm-000146-chb-clade
  category: grounding
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: review-checklist.taxonomy
  status: open
  certainty: confirmed
  title: Historical Chlorobi was mapped to the wrong modern clade
  description: Table 1 assigns CHB1 and CHB2 to families now descending through Ignavibacteriota
    in the inspected NCBI ancestry, not Chlorobiota (NCBITaxon:1090). The current
    GTDB Chlorobiia block follows that incorrect anchor. Newly added abundance evidence
    does not correct taxonomic identity.
  target_ids:
  - CommunityMech:000146
  field_paths:
  - taxonomy[1].taxon_term
  - ecological_interactions[2].participating_taxa
  evidence_ids:
  - chb-identity
  - lineage
  - record
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T073708Z-anammox-granule-record
    finding_id: chb-clade
- finding_id: exchange-overstatement
  issue_key: cm-000146-exchange-overstatement
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: review-checklist.causal
  status: open
  certainty: confirmed
  title: Summary and roles overstate inferred exchanges
  description: The description states recycling/scavenging as realized community functions
    and cross-feeder roles lack the qualification retained in the graph. Fermentation
    is not established as the shared principal mode of all flanking bacteria.
  target_ids:
  - CommunityMech:000146
  field_paths:
  - description
  - taxonomy[*].functional_role
  evidence_ids:
  - record
  - nitrite
  - peptides
  - donors
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T073708Z-anammox-granule-record
    finding_id: exchange-overstatement
- finding_id: article-as-dataset
  issue_key: cm-000146-article-as-dataset
  category: representation
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: material experimental, member or evidence attribution
    defect.'
  rule_id: review-checklist.datasets
  status: open
  certainty: confirmed
  title: Publication is represented as a sequencing dataset
  description: Nature-Communications-15416 is an article locator, not the deposited
    sequencing accession. The source and NCBI verify actual project and three sample
    accessions.
  target_ids:
  - CommunityMech:000146
  field_paths:
  - associated_datasets[0]
  evidence_ids:
  - record
  - bioproject
  - biosample_metagenome
  - biosample_transcriptome
  - biosample_miseq
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T073708Z-anammox-granule-record
    finding_id: article-as-dataset
- finding_id: laboratory-setting
  issue_key: cm-000146-laboratory-setting
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded representation/provenance gap; source context
    remains recoverable.'
  rule_id: review-checklist.environment
  status: open
  certainty: confirmed
  title: Environment points to the source treatment plant
  description: The target is a laboratory reactor; appropriate bioreactor/laboratory
    terms exist. The nearest-validated-term rationale is unsupported.
  target_ids:
  - CommunityMech:000146
  field_paths:
  - environment_term
  evidence_ids:
  - record
  - operation
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T073708Z-anammox-granule-record
    finding_id: laboratory-setting
- finding_id: cultivation-evidence
  issue_key: cm-000146-cultivation-evidence
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded representation/provenance gap; source context
    remains recoverable.'
  rule_id: review-checklist.cultivation
  status: open
  certainty: confirmed
  title: Cultivation has an unrelated supporting snippet
  description: The current cultivation evidence duplicates a genome-recovery quotation
    from engineering_design. It supports genome reconstruction rather than influent
    identity or anaerobic atmosphere. The source Methods provide directly relevant
    evidence; resolving the earlier source-verifiability backlog alone would not fix
    this semantic mismatch.
  target_ids:
  - CommunityMech:000146
  field_paths:
  - growth_media[0].evidence
  evidence_ids:
  - record
  - operation
  - snippets
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T073708Z-anammox-granule-record
    finding_id: cultivation-evidence
- finding_id: background-factor-scope
  issue_key: cm-000146-background-factor-scope
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded representation/provenance gap; source context
    remains recoverable.'
  rule_id: review-checklist.environment
  status: open
  certainty: confirmed
  title: General granule context is not identified as background
  description: Introductory oxygen-diffusion and EPS statements are not measurements
    of this experiment’s gradients or matrix composition.
  target_ids:
  - CommunityMech:000146
  field_paths:
  - environmental_factors[0]
  - environmental_factors[1]
  evidence_ids:
  - record
  - operation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T073708Z-anammox-granule-record
    finding_id: background-factor-scope
- finding_id: media-links
  issue_key: cm-000146-media-links
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded representation/provenance gap; source context
    remains recoverable.'
  rule_id: P3.1
  status: open
  certainty: confirmed
  title: Media lacks external linkage identifiers
  description: No CultureMech/MediaIngredientMech links are present. Wastewater filtrate
    is not interchangeable with a defined synthetic recipe.
  target_ids:
  - CommunityMech:000146
  field_paths:
  - growth_media
  evidence_ids:
  - record
  - operation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261020T073708Z-anammox-granule-record
    finding_id: media-links
actions:
- action_id: fix-amx-species
  description: Retain source-resolved Brocadia/MAG identity and independently verify
    any narrower mapping before applying it consistently.
  finding_ids:
  - amx-species
  target_ids:
  - CommunityMech:000146
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  acceptance_checks:
  - No exact species is inferred merely from closest related representatives.
  - All repeated participant mappings agree.
  - Run term,GTDB,strict and network gates.
- action_id: fix-chb-clade
  description: Reconcile each source CHB/MAG lineage and re-ground NCBI and GTDB from
    that identity rather than historical phylum wording.
  finding_ids:
  - chb-clade
  target_ids:
  - CommunityMech:000146
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Source family placements and modern ancestry agree.
  - GTDB mapping is independently recomputed/verified for the corrected anchor.
  - Every graph participant is updated consistently.
- action_id: fix-exchange-overstatement
  description: Preserve inferred-expression evidence and unresolved transfer/direction
    in summaries and roles.
  finding_ids:
  - exchange-overstatement
  target_ids:
  - CommunityMech:000146
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  acceptance_checks:
  - No confirmed partner flux or exclusive AMX1 carbon source is asserted.
  - Roles are source-specific or explicitly uncertain.
  - Graph qualification is preserved.
- action_id: fix-article-as-dataset
  description: Separate publication resources from actual deposited datasets with
    correct type and provenance.
  finding_ids:
  - article-as-dataset
  target_ids:
  - CommunityMech:000146
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Project/sample identifiers resolve to the correct study and data type.
  - Article is not mislabeled as a raw sequencing dataset.
  - Run strict and reference gates.
- action_id: fix-laboratory-setting
  description: Represent actual laboratory setting separately from the feedstock source
    facility.
  finding_ids:
  - laboratory-setting
  target_ids:
  - CommunityMech:000146
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Setting term matches experimental context.
  - Feedstock provenance remains intact.
  - Run term validation.
- action_id: fix-cultivation-evidence
  description: Attach exact Methods evidence to the stated cultivation claims without
    inventing an influent recipe.
  finding_ids:
  - cultivation-evidence
  target_ids:
  - CommunityMech:000146
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Attached evidence supports the actual atmosphere/influent claim.
  - Do not conflate upstream/downstream reactors.
  - Run reference validation.
- action_id: fix-background-factor-scope
  description: Identify background versus study-specific evidence and avoid implying
    measured gradients.
  finding_ids:
  - background-factor-scope
  target_ids:
  - CommunityMech:000146
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  acceptance_checks:
  - General context is marked as such.
  - No unavailable same-system measurement is claimed.
- action_id: fix-media-links
  description: Assess exact applicable resource matches and leave unmatched identities
    explicit.
  finding_ids:
  - media-links
  target_ids:
  - CommunityMech:000146
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  acceptance_checks:
  - No approximate recipe receives an exact identifier.
  - Any accepted link resolves and matches its intended material.
limitations:
- Supplementary files, raw reads, accessioned MAG assemblies and rendered figure geometry
  were not inspected; no independent sequence reconstruction or flux measurement is
  claimed.
- Fresh local NCBI ancestry confirms the CHB clade conflict. Replacement GTDB grounding
  and exact accessioned MAG identity require separate curation; coherence gates do
  not certify the existing biological assignments.
- Abundance and expression values are genome-mapping proxies, not absolute cell counts.
  Qualitative group annotations must not be interpreted as per-organism measurements
  or percentages of a modern named clade.
- Required corpus checks retain nonzero warning exits; clean target participation
  does not verify participant identity or mechanism.
- The native structured-expression runner was unavailable in a bounded lookup. The
  public catalog fallback had no exact source-population match; primary study text
  and deposited sample metadata were used, without treating catalog absence as biological
  evidence.
- Media matching was not searched across external registries. The missing-link finding
  concerns this target's absent identifiers and does not assert that no exact applicable
  registry resource exists.
notes:
- Original immutable review bytes are preserved. This successor records fresh input
  hashes, source snapshots and actual check receipts.
- Canonical records, caches, history and generated products were not changed by this
  author refresh.
- All eight original findings are retained with exact predecessor references; no new
  scientific curation finding was identified in this refresh.
- Five verified short quotations inherited from the primary paper total 22 words;
  other source content is paraphrased with locators.
- Independent adversarial review is performed separately from this author pass.
tags:
- record-review
- anammox
- batch-03
- pr-2036
- staleness-refresh
- successor
```
