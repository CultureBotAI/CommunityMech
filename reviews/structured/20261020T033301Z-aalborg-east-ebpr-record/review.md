# Aalborg East EBPR: whole-record source and representation review

- Review: 20261020T033301Z-aalborg-east-ebpr-record
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-19T23:42:18.375499Z
- Finished UTC: 2026-10-20T03:33:01.339715Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Plant identity, performance, metagenome accession and qualified four-node/three-arrow graph are supported. One major role-attribution finding and four minor representation/evidence/enrichment findings remain. Focused gates pass; required corpus warnings remain explicit.

## Scope And Provenance

Entire maintained Aalborg East record, all taxonomy, evidence, four nodes and three arrows, culture/operating context and dataset.

Selection: Tenth initially uncovered target in repository path order; one record per saved bundle.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base a4611c913c8da9619673df63a0c2cce3aa206a83.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000139 | kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml | maintained | Aalborg East Full-Scale EBPR Activated Sludge Community |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000139 | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml |
| validate-strict | passed | True | CommunityMech:000139 | uv run python scripts/validate_strict.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml --out /private/tmp/cm-review-session/000139/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/000139/strict-report.tsv |
| validate-terms | passed | True | CommunityMech:000139 | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| validate-gtdb | passed | True | CommunityMech:000139 | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| validate-gtdb-domain | passed | True | CommunityMech:000139 | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml |
| validate-history | passed | True | CommunityMech:000139 | No issues found |
| normalize-cache-names-check | passed | True | CommunityMech:000139 | Command completed without reported issues. |
| validate-references-explained | passed | True | CommunityMech:000139 | Validating kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| audit-network | failed | True | CommunityMech:000139 | Same-session complete corpus recipe exit 1: 462 records, 57 warnings in 21 records, zero errors. No target finding; unchanged base and canonical record bytes verified. This is reused output, not a new focused execution. |
| check-network-quality | failed | True | CommunityMech:000139 | Same-session complete corpus recipe exit 1: 462 records, 57 warnings in 21 records, zero errors. No target finding; unchanged base and canonical record bytes verified. This is reused output, not a new focused execution. |
| Optional expression-module adapter | unavailable | False | CommunityMech:000139 | Optional runner unavailable in isolated runtime; complete public catalog fallback had no matching target organism. |

## Scientific And Domain Assessments

### Community boundary, source strain and experimental setting

identity: supported. Targets: CommunityMech:000139.

One 2009 full-scale plant sample and its operating history are clearly represented. ENGINEERED describes process selection rather than genetic engineering or isolate assembly. The genus-level Accumulibacter descriptor preserves microdiversity; UW-1 remains a comparison genome. No pure strain pair is claimed.

### taxonomy[0..3] rank, source occurrence, abundance and roles

grounding: concern. Targets: CommunityMech:000139.

Accumulibacter genus, Actinomycetota/Bacteroidota phyla and the residual bacterial guild are broad but valid representations of source-covered populations. Actinobacterial 30% must remain a phylum measurement rather than a Tetrasphaera-specific percentage. 4.8% qFISH is supported and DOMINANT is an ordinal catalog designation, not an erroneous percentage conversion. Taxon roles exceed evidence: PAO storage does not imply PRIMARY_DEGRADER, and graph-hypothesized transfer is more cautious than unqualified CROSS_FEEDER/SECONDARY_FERMENTER assignments. NCBI labels and all four GTDB blocks pass native gates; historical mapping counts and six-species/tool-history narrative were not independently reconstructed.

### ecological_interactions[0]: PAO Phosphate Storage Under EBPR Selection

graph: concern. Targets: CommunityMech:000139.

PARTIAL is appropriate. Accumulibacter and Tetrasphaera-related PAOs are conceptual contributors to community storage potential. GO:0006796 is broad enough for the genomic enrichment; no measured niche partitioning or per-member phosphorus flux is asserted. The phosphate charge-state issue is separately bounded.

### ecological_interactions[1]: Flanking-Community Substrate Provision To PAOs

graph: supported. Targets: CommunityMech:000139.

HYPOTHESIZED correctly distinguishes background donor flanking bacteria and recipient Accumulibacter from observed transfer. No specific compound, rate or direct causal experiment is claimed. CROSS_FEEDING is appropriately qualified in this node.

### ecological_interactions[2]: Sludge Floc and Biofilm Formation

graph: supported. Targets: CommunityMech:000139.

PARTIAL is appropriate for community extracellular-polymer and capsule gene enrichment. Bacteroidota and the broad flanking guild are proposed context, not identified causal colonizers. GO:0042710 is suitable as a proposed biofilm process; no organism-specific matrix experiment was measured.

### ecological_interactions[3]: Stable Full-Scale EBPR Phosphorus Removal

graph: concern. Targets: CommunityMech:000139.

Greater than 95% whole-plant removal over preceding years is directly reported. All four descriptors provide community context; their separate contributions were not isolated. Polyphosphate storage is physiological context, while the measured influent/effluent endpoint was phosphorus, not a measured phosphate(3-) concentration.

### ecological_interactions[0].downstream[0] -&gt; Stable Full-Scale EBPR Phosphorus Removal

graph: supported. Targets: CommunityMech:000139.

Positive enabling direction: PAO storage potential to plant phosphorus removal. The arrow is PARTIAL, explicitly does not isolate the quantitative contribution, and is supported only as a plausible connection between genomic potential and observed plant performance.

Natural units are plant-wide observations and inferred community processes. Shared exact primary quotes and section locators are attached to the named evidence entries. All target names resolve.

### ecological_interactions[1].downstream[0] -&gt; PAO Phosphate Storage Under EBPR Selection

graph: supported. Targets: CommunityMech:000139.

Positive substrate-support direction: flanking bacterial fermenters/hydrolyzers to Accumulibacter/PAO storage. The source introduction supplies a background hypothesis; no metabolite transfer was traced. HYPOTHESIZED is appropriate and must remain.

Natural units are plant-wide observations and inferred community processes. Shared exact primary quotes and section locators are attached to the named evidence entries. All target names resolve.

### ecological_interactions[2].downstream[0] -&gt; Stable Full-Scale EBPR Phosphorus Removal

graph: supported. Targets: CommunityMech:000139.

Positive enabling direction: proposed floc/biomass retention to sustained community removal. Author interpretation of genes and settling supplies context, not a perturbation establishing mediation. PARTIAL is appropriate; no partner-specific benefit is asserted.

Natural units are plant-wide observations and inferred community processes. Shared exact primary quotes and section locators are attached to the named evidence entries. All target names resolve.

### engineering_design and environment_term

scope: supported. Targets: CommunityMech:000139.

Process objective, selection by anaerobic/anoxic/oxic operation and observational endpoints fit the study. Activated sludge correctly denotes the actual material sampled from the aeration tank; no hypothetical modeled habitat is substituted. There was no deliberate assembly from isolates or new perturbation performed by this metagenomic study.

### growth_media[0] and cultivation_setup[0]

evidence: supported. Targets: CommunityMech:000139.

Domestic wastewater feed, plant scale and alternating process zones are supported. CONTINUOUS is an operational interpretation of the full-scale treatment context, not a reported experimental dilution rate. The main paper does not supply plant temperature, pH, HRT, SRT or dissolved-oxygen setpoints. The record correctly avoids importing DNA-processing temperatures; supplements and operating records remain uninspected. Variable wastewater should not be assigned a nearby defined-medium identifier merely to fill a field.

### environmental_factors[0..1] and sparse structured context

completeness: concern. Targets: CommunityMech:000139.

Both existing factors are supported. Native non-minimal-community rubric expects at least three; directly reported influent/effluent phosphorus concentrations and sampling context are available for bounded enrichment. No temperature/pH optimum can be inferred.

### related_ingredients and chemical graph copies

grounding: concern. Targets: CommunityMech:000139.

Polyphosphate is appropriate to PAO storage. The phosphate(3-) term is narrower than the source phosphorus-removal and phosphate-metabolism wording; the study does not measure protonation/speciation. Preserve a generic process representation or explicitly qualify the formal chemical proxy.

### associated_datasets[0] accession and deposited scope

provenance: supported. Targets: CommunityMech:000139.

MG-RAST 4463936.3 independently resolves to public WWTP_EBPR_Aalborg_East WGS data. The main paper names the same nonredundant-contig accession. Initial API timeout and default browser failure were resolved using the versioned public API; no broken-accession finding is warranted. Pipeline metadata and original upload files were not reanalyzed.

### All EvidenceItems, methods classifications and quotation fidelity

evidence: concern. Targets: CommunityMech:000139.

All 22 occurrences were inspected. The selected-excerpt cache faithfully signals its restricted scope but has removed citations/punctuation from five passages. These snippets should be made contiguous rather than treated as exact full-text quotes. qFISH measurements are not computational evidence; introductory PAO/flanking physiology is background, not a new in vivo observation in this study. Graph-specific PARTIAL/OTHER labels are better calibrated than some taxon-level evidence.

### Discussions, history, external resources and source limits

provenance: supported. Targets: CommunityMech:000139.

The open discussion correctly asks which inferred transfers drive removal; it does not imply those mechanisms were demonstrated. The prior graph event resolves and is not a whole-record approval. Missing standalone external_resources is partly offset by the verified dataset link; exact exchanged metabolites and dynamics should remain unfilled until supported. No earlier structured finding is closed here.

### Expression-module applicability

evidence: not_applicable. Targets: CommunityMech:000139.

No matching organism/dataset in the inspected catalog. Community phosphate/biofilm potential cannot be supplied by an unrelated expression module; source metagenomics remains the relevant evidence.

### Deterministic gates and source retrieval

schema: supported. Targets: CommunityMech:000139.

Focused gates pass and the selected cache bytes remain unchanged. All four participants occur in the graph and internal names resolve. Required corpus warning failures remain separate; these gate results do not certify source support. Primary HTML and versioned MG-RAST API succeeded after initial failures.

### Native completeness and validation quality

completeness: concern. Targets: CommunityMech:000139.

Completeness is 85. Native validation quality caps at 100 despite one major and four minor findings because of evidence/reference integrity bonuses; it is not scientific approval.

## Findings

### functional-roles: Taxon roles assert functions beyond the qualified graph

major / open / confirmed; issue key: cm-000139-functional-roles.

Accumulibacter and Tetrasphaera-related PAO storage is not evidence for degradation of complex substrates. Flanking-community and PAO cross-feeding/secondary-fermentation roles are stated unconditionally while the source and graph frame transfer as background hypotheses. Bacteroidota hydrolytic context is plausible but does not validate the whole broad guild.

### evidence-fidelity: Evidence categories and edited excerpts need narrower attribution

minor / open / confirmed; issue key: cm-000139-evidence-fidelity.

The qFISH abundance item is marked COMPUTATIONAL; introductory physiological statements are marked IN_VIVO. Five snippets are noncontiguous after source citations/punctuation were silently removed, although recognizable source wording remains. This is a bounded evidence/provenance problem, not fabricated biology.

### phosphate-specificity: Chemical specificity exceeds the reported phosphorus endpoint

minor / open / confirmed; issue key: cm-000139-phosphate-specificity.

CHEBI:18367 denotes phosphate(3-), whereas the source reports phosphate metabolism and whole-plant P removal without charge-state or species measurement. The label resolves, but downstream consumers could mistake the formal representation for a measured ion-specific flux.

### media-linkage: Variable wastewater medium has no verified linkage

minor / open / confirmed; issue key: cm-000139-media-linkage.

The domestic-wastewater medium lacks CultureMech/MediaIngredientMech identifiers under the native linkage rubric. Its variable environmental feed may legitimately have no exact defined-medium match.

### environment-sparse: Only two structured factors capture the non-minimal plant context

minor / open / confirmed; issue key: cm-000139-environment-sparse.

The native rubric expects at least three environmental factors. The source additionally reports influent 10–20 mg P/L and effluent below 0.5 mg P/L; current record factors omit those available quantitative boundary conditions.

## Recommended Actions And Acceptance Checks

### fix-functional-roles

Align each role with a same-population supported function, retaining uncertainty rather than manufacturing complex-substrate degradation or measured transfer.

- Each role satisfies its schema definition and narrow source context.
- Genomic or background potential is not presented as measured metabolism.
- Run focused strict, references-explained and network checks after authorized curation.

### fix-evidence-fidelity

Use short contiguous primary passages and classify evidence at the actual assay or background claim; do not rewrite source text to satisfy matching.

- All retained quotations match contiguous inspected primary text under declared whitespace normalization.
- qFISH, metagenomics and background claims remain distinct.
- Run references-explained and strict gates; manually inspect exact source correspondence.

### fix-phosphate-specificity

Choose a source-compatible chemical abstraction or explicitly document the proxy, retaining total-phosphorus endpoint units separately.

- No ion-specific concentration or removal is inferred from total P.
- Any replacement chemical identifier is independently verified.
- Run term, strict and evidence validation after authorized curation.

### fix-media-linkage

Check exact compatible linkage only; document unmatched environmental feed if appropriate instead of assigning a nearby laboratory recipe.

- Any link resolves to the same material/formulation scope.
- Unmatched variable wastewater is explicitly retained as such.
- Run applicable linkage and strict checks after authorized curation.

### fix-environment-sparse

Add narrowly sourced plant phosphorus-loading or sampling context without inventing missing operational setpoints.

- Separate influent from effluent and retain total-P mass units.
- No PCR temperature or unsupported pH/HRT/SRT is added as cultivation.
- Run strict and references-explained validation after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml; Entire maintained record: four taxonomic entries, four nodes, three arrows, two environmental factors, medium/setup, dataset, discussion and history | supports | Study-specific full-scale EBPR activated sludge, not an isolate assembly. All material fields were read. |
| article | https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/; PMID:22170425; DOI:10.1038/ismej.2011.176; complete main article HTML including Abstract, Sampling, qFISH, assembly, Results and Discussion | supports | The primary paper supports an Aalborg East sample collected 4 August 2009, 18.2 Gb raw sequencing, independent qFISH, genomic potential and long-term plant removal. Source supplements were not independently downloaded. |
| storage | https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/; Abstract and Results: functional potential | supports | Community genomic enrichment supports storage potential, not a measured niche partition or taxon-specific contribution. |
| flanking | https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/; Introduction: flanking community | supports | This is background ecological context and a study motivation; no exchanged substrate was measured. |
| floc | https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/; Results: functional potential of the metagenome | supports | Authors connect extracellular-macromolecule genes to settling/retention selection; no partner-specific intervention was performed. |
| removal | https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/; Materials and methods: Sampling | supports | Whole-plant phosphorus removal was stable for several preceding years, without a partition of each member or mechanism contribution. |
| identity-metadata | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&amp;id=22170425&amp;retmode=xml; PubMed article PMID 22170425, article title, DOI, publication date and PMC identifier | supports | Primary metadata agrees with the full-text identity. Online publication was December 2011 and issue publication June 2012; this is not an identity conflict. |
| taxon-evidence | https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/; Results: Community structure comparison, Figure 1 caption; Similarity of metagenome species; Accumulibacter microdiversity | supports | Accumulibacter is 4.8% by qFISH biomass/probe comparison. Actinobacteria 3% metagenomic versus 30% qFISH is a phylum-level comparison, not a Tetrasphaera species count. The main text independently states high Tetrasphaera qFISH counts and discusses DNA extraction bias. Bacteroidetes assignments are linked cautiously to Saprospiraceae. UW-1 is a reference genome, not the sampled isolate. |
| cultivation | https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/; Materials and methods: Sampling; operating context and date | supports | Domestic wastewater, 100,000 person-equivalent capacity, average 45,000 load, anaerobic plus alternating anoxic/oxic tanks, influent 10–20 mg P/L and effluent below 0.5 mg P/L are stated. The main article supplies no plant pH, temperature, HRT, SRT or dissolved-oxygen setpoint. DNA-extraction/PCR temperatures are not cultivation temperatures. |
| dataset | https://api.mg-rast.org/1/metagenome/mgm4463936.3?verbosity=minimal; Public metagenome response: id, name, WGS sequence type, sample mgs25509 and project mgp259 | supports | The accession resolves to the named Aalborg East WGS dataset. The paper says nonredundant contigs were deposited. The current pipeline flag assembled=no was not interpreted as proof of upload content; files were not downloaded or reassembled. |
| ontology | OAK local SemanticSQL CHEBI/GO/ENVO snapshots; Exact queried labels/definitions retained in /private/tmp/cm-review-session/000139/ontology-authority.json | supports | Canonical terms resolve. GO phosphate-compound metabolism and biofilm formation fit qualified genomic potential. CHEBI:18367 specifically denotes phosphate(3-), while the source reports phosphorus/phosphate metabolism without measuring that ionic species. Activated sludge is a suitable sampled material; absence of a local ENVO textual definition is not an absent class. |
| schema | src/communitymech/schema/communitymech.yaml; FunctionalRoleEnum, AbundanceEnum, EvidenceSourceEnum, cultivation and chemical descriptors | supports | PRIMARY_DEGRADER means complex-substrate degradation; CROSS_FEEDER means utilizing other taxa metabolites. DOMINANT is an ordinal role within the record, not a fixed percentage band. Assay evidence types must follow the represented claim. |
| history | history/records/Aalborg_East_Full_Scale_EBPR_Community/2026-10-05T055200Z-codex-345efd.yaml; Entire history event and matching CommunityMech:000139 row in reports/causal_graph_review/decisions/20261005-seven-records.yaml | supports | Prior graph review explicitly limited causal claims and excluded other metadata certification. Current node and edge caveats and the unresolved discussion retain that distinction. |
| snippets | kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml; All 22 EvidenceItem occurrences checked against independently retrieved main article text | supports | Seventeen snippets match after whitespace/case normalization. Five remove inline citations, taxonomic quotation marks or a Figure 1 parenthesis, so they are not contiguous primary quotations although the surrounding scientific wording is recognizable. Matching the selected-excerpt cache does not expose this editing. |
| local-search | history/records; reports/causal_graph_review; references_cache; kb/taxa; Ignored-inclusive ID/slug/PMID search | supports | The cited cache and history/graph decision were located. No separate reusable taxon match was returned for this bounded record-ID/slug/reference query; this is not a universal taxon-name absence claim. |
| adapter | https://imodulondb.org/api/datasets; Same-session public catalog fallback: all 20 organism keys and 28 datasets | context_only | The isolated runtime lacks the optional adapter runner. The catalog contains no Accumulibacter, Tetrasphaera or source-matched sludge community dataset; unrelated expression modules cannot establish EBPR traits. No module-level query applies. |
| check-validate | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml; Actual execution 2026-10-20T03:28:59.661858+00:00 through 2026-10-20T03:29:00.171187+00:00 | supports | No issues found<br>uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml |
| check-validate-strict | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml --out /private/tmp/cm-review-session/000139/strict-report.tsv; Actual execution 2026-10-20T03:28:59.662006+00:00 through 2026-10-20T03:29:01.309739+00:00 | supports | uv run python scripts/validate_strict.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml --out /private/tmp/cm-review-session/000139/strict-report.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cm-review-session/000139/strict-report.tsv |
| check-validate-terms | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml; Actual execution 2026-10-20T03:28:59.662073+00:00 through 2026-10-20T03:29:01.305014+00:00 | supports | ✅ Validation passed<br>uv run linkml-term-validator validate-data kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml -s src/communitymech/schema/communitymech.yaml --labels |
| check-validate-gtdb | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml; Actual execution 2026-10-20T03:29:00.171422+00:00 through 2026-10-20T03:29:00.235322+00:00 | supports | PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml<br><br>files checked: 1<br>incoherent blocks: 0<br>malformed lineages: 0<br>lineage conflicts: 0 |
| check-validate-gtdb-domain | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml; Actual execution 2026-10-20T03:29:00.235549+00:00 through 2026-10-20T03:29:01.220280+00:00 | supports | files checked: 1<br>contradictory lineages: 0<br>PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml |
| check-validate-history | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-history history/records/Aalborg_East_Full_Scale_EBPR_Community; Actual execution 2026-10-20T03:29:01.220502+00:00 through 2026-10-20T03:29:01.745377+00:00 | supports | No issues found |
| check-normalize-cache-names-check | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check; Actual execution 2026-10-20T03:29:01.745941+00:00 through 2026-10-20T03:29:01.788580+00:00 | supports | Command completed without reported issues. |
| check-validate-references-explained | JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml; Actual execution 2026-10-20T03:29:01.788757+00:00 through 2026-10-20T03:29:02.550618+00:00 | supports | Validating kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml against schema src/communitymech/schema/communitymech.yaml<br>Cache directory: references_cache<br><br>Validation Summary:<br>  Reported validation issues: 0<br>  All validations passed!<br><br>[annotate] This is not a count of checked excerpts (#1469). Native Discussion evidence coverage remains incomplete (#476). |
| check-audit-network | just --no-dotenv audit-network; Executed 2026-10-19T07:30:27.845593+00:00 | supports | Same-session complete corpus recipe exit 1: 462 records, 57 warnings in 21 records, zero errors. No target finding; unchanged base and canonical record bytes verified. This is reused output, not a new focused execution. |
| check-check-network-quality | just --no-dotenv check-network-quality; Executed 2026-10-19T07:30:43.193891+00:00 | supports | Same-session complete corpus recipe exit 1: 462 records, 57 warnings in 21 records, zero errors. No target finding; unchanged base and canonical record bytes verified. This is reused output, not a new focused execution. |

## Limits And Additional Notes

- Full main article inspected through public PMC HTML and primary metadata; supplements and raw sequencing files were not independently analyzed. The committed cache contains selected excerpts only.
- Historical GTDB support counts, six-species statement and prior mapping-tool history were not independently rebuilt; present canonical/coherence/domain checks passed.
- Phosphate charge state was not measured. Operational CONTINUOUS is inferred from the described full-scale plant rather than a reported dilution-rate experiment.
- Initial full-text XML and default MG-RAST requests failed; primary HTML and alternate public API resolved the needed source and accession.
- Optional expression-module adapter unavailable in the isolated runtime; public catalog contains no matching organism. Required network corpus gates fail on unrelated warnings.
- Native scores measure presence and validation features; high scores do not resolve unsupported roles or other findings.
- No record, source cache, history, generated product or scientific-status field changed. Proposed curation needs separate authorization.
- All initial input hashes were checked unchanged. Exact short quotations total at most 25 words for the publication and are shared across node/edge assessments.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T033301Z-aalborg-east-ebpr-record
kind: record
repository: CultureBotAI/CommunityMech
title: 'Aalborg East EBPR: whole-record source and representation review'
started_at: '2026-10-19T23:42:18.375499Z'
finished_at: '2026-10-20T03:33:01.339715Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: No target authored or edited this session; historical graph
    curation used the same codex identity, so person-level independence is unknown.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Plant identity, performance, metagenome accession and qualified four-node/three-arrow
  graph are supported. One major role-attribution finding and four minor representation/evidence/enrichment
  findings remain. Focused gates pass; required corpus warnings remain explicit.
source:
  git_revision: a4611c913c8da9619673df63a0c2cce3aa206a83
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
  - path: history/records/Aalborg_East_Full_Scale_EBPR_Community/2026-10-05T055200Z-codex-345efd.yaml
    sha256: 67a93d0397b82e85d0da933d65e439bcc9939e267ab977bcb9911a41d119c7d1
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    sha256: 8b38b18b0519f17b387ecdd88334ea66438df128cd912a5c56da4f8c1f6d012d
    role: target
  - path: references_cache/PMID_22170425.md
    sha256: 8574fac2bc6d76388aa4af642bb4147cabe8a3f4bd57b848674351670b76a75a
    role: context
  - path: reports/causal_graph_review/decisions/20261005-seven-records.yaml
    sha256: 064f7395bbb54d42023f3a0bceeb31a3dd990221e62094f6a51507fee81eea69
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/communitymech/network/auditor.py
    sha256: fe32aa2eddf9e09c153c47576f943bf08a6019f650bf2575e3ddc8e14675049b
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: e5a87e5367609334ec0d6361f6ddafbe6bc4a1f7d93e5264c64688c28325910f
    role: context
  - path: src/communitymech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: CommunityMech:000139
  path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  label: Aalborg East Full-Scale EBPR Activated Sludge Community
  record_class: MicrobialCommunity
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
scope:
  description: Entire maintained Aalborg East record, all taxonomy, evidence, four
    nodes and three arrows, culture/operating context and dataset.
  selection: Tenth initially uncovered target in repository path order; one record
    per saved bundle.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000139
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml'
  target_ids:
  - CommunityMech:000139
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history, except read-only corpus cache-name preflight.
    No ontology skips; cache unchanged.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: "uv run python scripts/validate_strict.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml\
    \ --out /private/tmp/cm-review-session/000139/strict-report.tsv\nValidating 1\
    \ files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/000139/strict-report.tsv"
  target_ids:
  - CommunityMech:000139
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    --out /private/tmp/cm-review-session/000139/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history, except read-only corpus cache-name preflight.
    No ontology skips; cache unchanged.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  target_ids:
  - CommunityMech:000139
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history, except read-only corpus cache-name preflight.
    No ontology skips; cache unchanged.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  target_ids:
  - CommunityMech:000139
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history, except read-only corpus cache-name preflight.
    No ontology skips; cache unchanged.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml'
  target_ids:
  - CommunityMech:000139
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history, except read-only corpus cache-name preflight.
    No ontology skips; cache unchanged.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: No issues found
  target_ids:
  - CommunityMech:000139
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-history history/records/Aalborg_East_Full_Scale_EBPR_Community
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history, except read-only corpus cache-name preflight.
    No ontology skips; cache unchanged.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Command completed without reported issues.
  target_ids:
  - CommunityMech:000139
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history, except read-only corpus cache-name preflight.
    No ontology skips; cache unchanged.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: "Validating kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  target_ids:
  - CommunityMech:000139
  command: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history, except read-only corpus cache-name preflight.
    No ontology skips; cache unchanged.
- check_id: audit-network
  name: audit-network
  status: failed
  required: true
  summary: 'Same-session complete corpus recipe exit 1: 462 records, 57 warnings in
    21 records, zero errors. No target finding; unchanged base and canonical record
    bytes verified. This is reused output, not a new focused execution.'
  target_ids:
  - CommunityMech:000139
  command: just --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-audit-network
  scope_note: Complete corpus; unrelated warning failures remain explicit.
- check_id: check-network-quality
  name: check-network-quality
  status: failed
  required: true
  summary: 'Same-session complete corpus recipe exit 1: 462 records, 57 warnings in
    21 records, zero errors. No target finding; unchanged base and canonical record
    bytes verified. This is reused output, not a new focused execution.'
  target_ids:
  - CommunityMech:000139
  command: just --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - check-check-network-quality
  scope_note: Complete corpus; unrelated warning failures remain explicit.
- check_id: source-adapter
  name: Optional expression-module adapter
  status: unavailable
  required: false
  summary: Optional runner unavailable in isolated runtime; complete public catalog
    fallback had no matching target organism.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - adapter
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  locator: 'Entire maintained record: four taxonomic entries, four nodes, three arrows,
    two environmental factors, medium/setup, dataset, discussion and history'
  summary: Study-specific full-scale EBPR activated sludge, not an isolate assembly.
    All material fields were read.
  support: supports
  accessed_at: '2026-10-20T03:33:01.334726Z'
- evidence_id: article
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/
  locator: PMID:22170425; DOI:10.1038/ismej.2011.176; complete main article HTML including
    Abstract, Sampling, qFISH, assembly, Results and Discussion
  summary: The primary paper supports an Aalborg East sample collected 4 August 2009,
    18.2 Gb raw sequencing, independent qFISH, genomic potential and long-term plant
    removal. Source supplements were not independently downloaded.
  support: supports
  accessed_at: '2026-10-20T03:29:11.724528Z'
  snapshot_sha256: 2019438b6053c11cf350bc99c2144da00df1fce0d9ecb4c0820b1569efa8b412
- evidence_id: storage
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/
  locator: 'Abstract and Results: functional potential'
  summary: Community genomic enrichment supports storage potential, not a measured
    niche partition or taxon-specific contribution.
  support: supports
  accessed_at: '2026-10-20T03:29:11.724528Z'
  quote: enrichment of genes involved in phosphate metabolism
  snapshot_sha256: 2019438b6053c11cf350bc99c2144da00df1fce0d9ecb4c0820b1569efa8b412
- evidence_id: flanking
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/
  locator: 'Introduction: flanking community'
  summary: This is background ecological context and a study motivation; no exchanged
    substrate was measured.
  support: supports
  accessed_at: '2026-10-20T03:29:11.724528Z'
  quote: bacteria providing substrate to the PAOs
  snapshot_sha256: 2019438b6053c11cf350bc99c2144da00df1fce0d9ecb4c0820b1569efa8b412
- evidence_id: floc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/
  locator: 'Results: functional potential of the metagenome'
  summary: Authors connect extracellular-macromolecule genes to settling/retention
    selection; no partner-specific intervention was performed.
  support: supports
  accessed_at: '2026-10-20T03:29:11.724528Z'
  quote: effective floc/biofilm formation
  snapshot_sha256: 2019438b6053c11cf350bc99c2144da00df1fce0d9ecb4c0820b1569efa8b412
- evidence_id: removal
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/
  locator: 'Materials and methods: Sampling'
  summary: Whole-plant phosphorus removal was stable for several preceding years,
    without a partition of each member or mechanism contribution.
  support: supports
  accessed_at: '2026-10-20T03:29:11.724528Z'
  quote: removing >95% of the incoming P
  snapshot_sha256: 2019438b6053c11cf350bc99c2144da00df1fce0d9ecb4c0820b1569efa8b412
- evidence_id: identity-metadata
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22170425&retmode=xml
  locator: PubMed article PMID 22170425, article title, DOI, publication date and
    PMC identifier
  summary: Primary metadata agrees with the full-text identity. Online publication
    was December 2011 and issue publication June 2012; this is not an identity conflict.
  support: supports
  accessed_at: '2026-10-19T23:42:44.300348Z'
  snapshot_sha256: 80847a6590bca3f9ea4e0e0573a67909abb19ab5995fc0a3d4677da10fab1176
- evidence_id: taxon-evidence
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/
  locator: 'Results: Community structure comparison, Figure 1 caption; Similarity
    of metagenome species; Accumulibacter microdiversity'
  summary: Accumulibacter is 4.8% by qFISH biomass/probe comparison. Actinobacteria
    3% metagenomic versus 30% qFISH is a phylum-level comparison, not a Tetrasphaera
    species count. The main text independently states high Tetrasphaera qFISH counts
    and discusses DNA extraction bias. Bacteroidetes assignments are linked cautiously
    to Saprospiraceae. UW-1 is a reference genome, not the sampled isolate.
  support: supports
  accessed_at: '2026-10-20T03:29:11.724528Z'
- evidence_id: cultivation
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3358022/
  locator: 'Materials and methods: Sampling; operating context and date'
  summary: Domestic wastewater, 100,000 person-equivalent capacity, average 45,000
    load, anaerobic plus alternating anoxic/oxic tanks, influent 10–20 mg P/L and
    effluent below 0.5 mg P/L are stated. The main article supplies no plant pH, temperature,
    HRT, SRT or dissolved-oxygen setpoint. DNA-extraction/PCR temperatures are not
    cultivation temperatures.
  support: supports
  accessed_at: '2026-10-20T03:29:11.724528Z'
- evidence_id: dataset
  kind: database
  reference: https://api.mg-rast.org/1/metagenome/mgm4463936.3?verbosity=minimal
  locator: 'Public metagenome response: id, name, WGS sequence type, sample mgs25509
    and project mgp259'
  summary: The accession resolves to the named Aalborg East WGS dataset. The paper
    says nonredundant contigs were deposited. The current pipeline flag assembled=no
    was not interpreted as proof of upload content; files were not downloaded or reassembled.
  support: supports
  accessed_at: '2026-10-20T03:29:11.724851Z'
  snapshot_sha256: 1c327ff40425add27477dee4b23e56d65e32fe707e2091d58a8270333a00d0b6
- evidence_id: ontology
  kind: authority
  reference: OAK local SemanticSQL CHEBI/GO/ENVO snapshots
  locator: Exact queried labels/definitions retained in /private/tmp/cm-review-session/000139/ontology-authority.json
  summary: Canonical terms resolve. GO phosphate-compound metabolism and biofilm formation
    fit qualified genomic potential. CHEBI:18367 specifically denotes phosphate(3-),
    while the source reports phosphorus/phosphate metabolism without measuring that
    ionic species. Activated sludge is a suitable sampled material; absence of a local
    ENVO textual definition is not an absent class.
  support: supports
  accessed_at: '2026-10-20T03:30:07.213249Z'
  snapshot_sha256: 8cef435de9897cf2fa7395b65349e279ed10904b43ba83823c2f468e1dff6e7c
- evidence_id: schema
  kind: authority
  reference: src/communitymech/schema/communitymech.yaml
  locator: FunctionalRoleEnum, AbundanceEnum, EvidenceSourceEnum, cultivation and
    chemical descriptors
  summary: PRIMARY_DEGRADER means complex-substrate degradation; CROSS_FEEDER means
    utilizing other taxa metabolites. DOMINANT is an ordinal role within the record,
    not a fixed percentage band. Assay evidence types must follow the represented
    claim.
  support: supports
  accessed_at: '2026-10-20T03:33:01.335778Z'
- evidence_id: history
  kind: record_content
  reference: history/records/Aalborg_East_Full_Scale_EBPR_Community/2026-10-05T055200Z-codex-345efd.yaml
  locator: Entire history event and matching CommunityMech:000139 row in reports/causal_graph_review/decisions/20261005-seven-records.yaml
  summary: Prior graph review explicitly limited causal claims and excluded other
    metadata certification. Current node and edge caveats and the unresolved discussion
    retain that distinction.
  support: supports
  accessed_at: '2026-10-20T03:33:01.335780Z'
- evidence_id: snippets
  kind: validation
  reference: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  locator: All 22 EvidenceItem occurrences checked against independently retrieved
    main article text
  summary: Seventeen snippets match after whitespace/case normalization. Five remove
    inline citations, taxonomic quotation marks or a Figure 1 parenthesis, so they
    are not contiguous primary quotations although the surrounding scientific wording
    is recognizable. Matching the selected-excerpt cache does not expose this editing.
  support: supports
  accessed_at: '2026-10-20T03:33:01.335974Z'
  snapshot_sha256: b13b50a3735cbd03b28b6718dc1d90065c19db374231230f2d881d53cae256a5
- evidence_id: local-search
  kind: search
  reference: history/records; reports/causal_graph_review; references_cache; kb/taxa
  locator: Ignored-inclusive ID/slug/PMID search
  summary: The cited cache and history/graph decision were located. No separate reusable
    taxon match was returned for this bounded record-ID/slug/reference query; this
    is not a universal taxon-name absence claim.
  support: supports
  accessed_at: '2026-10-20T03:30:25.011852Z'
  search_scope: rg --no-ignore --hidden -l 'Aalborg_East_Full_Scale_EBPR_Community|CommunityMech:000139|22170425'
    history/records reports/causal_graph_review references_cache kb/taxa
  snapshot_sha256: 9125649b24691a7f24c3409654d53a3671965e6bd33936d3c74def5fa54389e6
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Same-session public catalog fallback: all 20 organism keys and 28 datasets'
  summary: The isolated runtime lacks the optional adapter runner. The catalog contains
    no Accumulibacter, Tetrasphaera or source-matched sludge community dataset; unrelated
    expression modules cannot establish EBPR traits. No module-level query applies.
  support: context_only
  accessed_at: '2026-10-19T23:31:07.726770Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: check-validate
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  locator: Actual execution 2026-10-20T03:28:59.661858+00:00 through 2026-10-20T03:29:00.171187+00:00
  summary: 'No issues found

    uv run linkml-validate -s src/communitymech/schema/communitymech.yaml kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml'
  support: supports
  accessed_at: '2026-10-20T03:29:00.171187Z'
  snapshot_sha256: 2bbb9b73405d47bd79e182b29d2d8471c1411cedfb0ba56e28e88a1d818e954d
- evidence_id: check-validate-strict
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-strict kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    --out /private/tmp/cm-review-session/000139/strict-report.tsv
  locator: Actual execution 2026-10-20T03:28:59.662006+00:00 through 2026-10-20T03:29:01.309739+00:00
  summary: "uv run python scripts/validate_strict.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml\
    \ --out /private/tmp/cm-review-session/000139/strict-report.tsv\nValidating 1\
    \ files with 17 workers; schema=/private/tmp/communitymech-record-reviews-20261019/src/communitymech/schema/communitymech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cm-review-session/000139/strict-report.tsv"
  support: supports
  accessed_at: '2026-10-20T03:29:01.309739Z'
  snapshot_sha256: a34119b9adcb4c51aedbf0cfd6824168a607b0ab828b250c6e23abc192c8a719
- evidence_id: check-validate-terms
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-terms kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  locator: Actual execution 2026-10-20T03:28:59.662073+00:00 through 2026-10-20T03:29:01.305014+00:00
  summary: '✅ Validation passed

    uv run linkml-term-validator validate-data kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    -s src/communitymech/schema/communitymech.yaml --labels'
  support: supports
  accessed_at: '2026-10-20T03:29:01.305014Z'
  snapshot_sha256: 38ce8c2b753100c6f4a55c67fbe8668723c9f01a007d94bd3109e629298423ad
- evidence_id: check-validate-gtdb
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  locator: Actual execution 2026-10-20T03:29:00.171422+00:00 through 2026-10-20T03:29:00.235322+00:00
  summary: 'PYTHONPATH=src uv run python scripts/validate_gtdb_coherence.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml


    files checked: 1

    incoherent blocks: 0

    malformed lineages: 0

    lineage conflicts: 0'
  support: supports
  accessed_at: '2026-10-20T03:29:00.235322Z'
  snapshot_sha256: a06bdf945b8b5e7ceb3c58548f189cbf87c102a15da6942fc8f65c62f723e10e
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-gtdb-domain kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  locator: Actual execution 2026-10-20T03:29:00.235549+00:00 through 2026-10-20T03:29:01.220280+00:00
  summary: 'files checked: 1

    contradictory lineages: 0

    PYTHONPATH=src uv run python scripts/validate_prokaryotic_lineage.py kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml'
  support: supports
  accessed_at: '2026-10-20T03:29:01.220280Z'
  snapshot_sha256: 763c4f24ab850d4960e7ca5d9f2bbfddb7d1bb054a26c4d5a30e934f57a10b96
- evidence_id: check-validate-history
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-history history/records/Aalborg_East_Full_Scale_EBPR_Community
  locator: Actual execution 2026-10-20T03:29:01.220502+00:00 through 2026-10-20T03:29:01.745377+00:00
  summary: No issues found
  support: supports
  accessed_at: '2026-10-20T03:29:01.745377Z'
  snapshot_sha256: 2d5b84313d17d651386323909da1c4d70d4afa09a439e997ddb41a6b50537a3e
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true uv run python scripts/normalize_cache_names.py --check
  locator: Actual execution 2026-10-20T03:29:01.745941+00:00 through 2026-10-20T03:29:01.788580+00:00
  summary: Command completed without reported issues.
  support: supports
  accessed_at: '2026-10-20T03:29:01.788580Z'
  snapshot_sha256: 482f11494fd24fa0ed8f9457f1820c500d2d58b93f92885f611d44b392e919c1
- evidence_id: check-validate-references-explained
  kind: validation
  reference: JUST_NO_DOTENV=true UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1
    UV_OFFLINE=true just --no-dotenv validate-references-explained kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  locator: Actual execution 2026-10-20T03:29:01.788757+00:00 through 2026-10-20T03:29:02.550618+00:00
  summary: "Validating kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml\
    \ against schema src/communitymech/schema/communitymech.yaml\nCache directory:\
    \ references_cache\n\nValidation Summary:\n  Reported validation issues: 0\n \
    \ All validations passed!\n\n[annotate] This is not a count of checked excerpts\
    \ (#1469). Native Discussion evidence coverage remains incomplete (#476)."
  support: supports
  accessed_at: '2026-10-20T03:29:02.550618Z'
  snapshot_sha256: 468e6354619d63528b076e685adde81b92445376f36434526b67f9a08e6922b6
- evidence_id: check-audit-network
  kind: validation
  reference: just --no-dotenv audit-network
  locator: Executed 2026-10-19T07:30:27.845593+00:00
  summary: 'Same-session complete corpus recipe exit 1: 462 records, 57 warnings in
    21 records, zero errors. No target finding; unchanged base and canonical record
    bytes verified. This is reused output, not a new focused execution.'
  support: supports
  accessed_at: '2026-10-19T07:30:27.845593Z'
  snapshot_sha256: bedf3fd18a964bda429f7c6b5feb01b8918e1440b48a4329664501161c80e3f4
- evidence_id: check-check-network-quality
  kind: validation
  reference: just --no-dotenv check-network-quality
  locator: Executed 2026-10-19T07:30:43.193891+00:00
  summary: 'Same-session complete corpus recipe exit 1: 462 records, 57 warnings in
    21 records, zero errors. No target finding; unchanged base and canonical record
    bytes verified. This is reused output, not a new focused execution.'
  support: supports
  accessed_at: '2026-10-19T07:30:43.193891Z'
  snapshot_sha256: 885e62e84ed8d3e69a6e5ef5be43f941ef64d756107c3b062846831f76e081aa
assessments:
- assessment_id: identity
  area: identity
  topic: Community boundary, source strain and experimental setting
  outcome: supported
  summary: One 2009 full-scale plant sample and its operating history are clearly
    represented. ENGINEERED describes process selection rather than genetic engineering
    or isolate assembly. The genus-level Accumulibacter descriptor preserves microdiversity;
    UW-1 remains a comparison genome. No pure strain pair is claimed.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - article
  - identity-metadata
  dimensions:
  - name: source_strain
    value: Environmental plant populations; no sampled isolate strain
    definition: Reference strain UW-1 is distinct from sampled populations.
    evidence_ids:
    - taxon-evidence
  - name: community_scope
    value: Full-scale Aalborg East activated sludge sampled 4 August 2009
    definition: A study-specific complex community with a coarse functional subset
      of its members represented.
    evidence_ids:
    - article
  - name: experimental_setting
    value: Municipal BioDenipho plant; molecular and microscopy assays on sampled
      sludge
    definition: Process conditions are distinct from extraction, PCR and reference-genome
      cultures.
    evidence_ids:
    - cultivation
  - name: medium
    value: Mainly domestic wastewater
    definition: Variable plant feed, not a defined isolate medium.
    evidence_ids:
    - cultivation
  - name: source_category
    value: 'Primary full text: observational process performance, qFISH and comparative
      metagenomics'
    definition: Genomic potential does not demonstrate a transferred metabolite or
      causal perturbation.
    evidence_ids:
    - article
- assessment_id: taxonomy
  area: grounding
  topic: taxonomy[0..3] rank, source occurrence, abundance and roles
  outcome: concern
  summary: 'Accumulibacter genus, Actinomycetota/Bacteroidota phyla and the residual
    bacterial guild are broad but valid representations of source-covered populations.
    Actinobacterial 30% must remain a phylum measurement rather than a Tetrasphaera-specific
    percentage. 4.8% qFISH is supported and DOMINANT is an ordinal catalog designation,
    not an erroneous percentage conversion. Taxon roles exceed evidence: PAO storage
    does not imply PRIMARY_DEGRADER, and graph-hypothesized transfer is more cautious
    than unqualified CROSS_FEEDER/SECONDARY_FERMENTER assignments. NCBI labels and
    all four GTDB blocks pass native gates; historical mapping counts and six-species/tool-history
    narrative were not independently reconstructed.'
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - taxon-evidence
  - schema
  - article
- assessment_id: node-0
  area: graph
  topic: 'ecological_interactions[0]: PAO Phosphate Storage Under EBPR Selection'
  outcome: concern
  summary: PARTIAL is appropriate. Accumulibacter and Tetrasphaera-related PAOs are
    conceptual contributors to community storage potential. GO:0006796 is broad enough
    for the genomic enrichment; no measured niche partitioning or per-member phosphorus
    flux is asserted. The phosphate charge-state issue is separately bounded.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - storage
  - taxon-evidence
  - ontology
- assessment_id: node-1
  area: graph
  topic: 'ecological_interactions[1]: Flanking-Community Substrate Provision To PAOs'
  outcome: supported
  summary: HYPOTHESIZED correctly distinguishes background donor flanking bacteria
    and recipient Accumulibacter from observed transfer. No specific compound, rate
    or direct causal experiment is claimed. CROSS_FEEDING is appropriately qualified
    in this node.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - flanking
  - article
- assessment_id: node-2
  area: graph
  topic: 'ecological_interactions[2]: Sludge Floc and Biofilm Formation'
  outcome: supported
  summary: PARTIAL is appropriate for community extracellular-polymer and capsule
    gene enrichment. Bacteroidota and the broad flanking guild are proposed context,
    not identified causal colonizers. GO:0042710 is suitable as a proposed biofilm
    process; no organism-specific matrix experiment was measured.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - floc
  - article
  - ontology
- assessment_id: node-3
  area: graph
  topic: 'ecological_interactions[3]: Stable Full-Scale EBPR Phosphorus Removal'
  outcome: concern
  summary: Greater than 95% whole-plant removal over preceding years is directly reported.
    All four descriptors provide community context; their separate contributions were
    not isolated. Polyphosphate storage is physiological context, while the measured
    influent/effluent endpoint was phosphorus, not a measured phosphate(3-) concentration.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - removal
  - cultivation
  - ontology
- assessment_id: edge-0
  area: graph
  topic: ecological_interactions[0].downstream[0] -> Stable Full-Scale EBPR Phosphorus
    Removal
  outcome: supported
  summary: 'Positive enabling direction: PAO storage potential to plant phosphorus
    removal. The arrow is PARTIAL, explicitly does not isolate the quantitative contribution,
    and is supported only as a plausible connection between genomic potential and
    observed plant performance.'
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - storage
  - removal
  details: Natural units are plant-wide observations and inferred community processes.
    Shared exact primary quotes and section locators are attached to the named evidence
    entries. All target names resolve.
- assessment_id: edge-1
  area: graph
  topic: ecological_interactions[1].downstream[0] -> PAO Phosphate Storage Under EBPR
    Selection
  outcome: supported
  summary: 'Positive substrate-support direction: flanking bacterial fermenters/hydrolyzers
    to Accumulibacter/PAO storage. The source introduction supplies a background hypothesis;
    no metabolite transfer was traced. HYPOTHESIZED is appropriate and must remain.'
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - flanking
  - storage
  details: Natural units are plant-wide observations and inferred community processes.
    Shared exact primary quotes and section locators are attached to the named evidence
    entries. All target names resolve.
- assessment_id: edge-2
  area: graph
  topic: ecological_interactions[2].downstream[0] -> Stable Full-Scale EBPR Phosphorus
    Removal
  outcome: supported
  summary: 'Positive enabling direction: proposed floc/biomass retention to sustained
    community removal. Author interpretation of genes and settling supplies context,
    not a perturbation establishing mediation. PARTIAL is appropriate; no partner-specific
    benefit is asserted.'
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - floc
  - removal
  details: Natural units are plant-wide observations and inferred community processes.
    Shared exact primary quotes and section locators are attached to the named evidence
    entries. All target names resolve.
- assessment_id: engineering
  area: scope
  topic: engineering_design and environment_term
  outcome: supported
  summary: Process objective, selection by anaerobic/anoxic/oxic operation and observational
    endpoints fit the study. Activated sludge correctly denotes the actual material
    sampled from the aeration tank; no hypothetical modeled habitat is substituted.
    There was no deliberate assembly from isolates or new perturbation performed by
    this metagenomic study.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - cultivation
  - article
- assessment_id: cultivation
  area: evidence
  topic: growth_media[0] and cultivation_setup[0]
  outcome: supported
  summary: Domestic wastewater feed, plant scale and alternating process zones are
    supported. CONTINUOUS is an operational interpretation of the full-scale treatment
    context, not a reported experimental dilution rate. The main paper does not supply
    plant temperature, pH, HRT, SRT or dissolved-oxygen setpoints. The record correctly
    avoids importing DNA-processing temperatures; supplements and operating records
    remain uninspected. Variable wastewater should not be assigned a nearby defined-medium
    identifier merely to fill a field.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - cultivation
  - article
- assessment_id: environment
  area: completeness
  topic: environmental_factors[0..1] and sparse structured context
  outcome: concern
  summary: Both existing factors are supported. Native non-minimal-community rubric
    expects at least three; directly reported influent/effluent phosphorus concentrations
    and sampling context are available for bounded enrichment. No temperature/pH optimum
    can be inferred.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - cultivation
- assessment_id: ingredients
  area: grounding
  topic: related_ingredients and chemical graph copies
  outcome: concern
  summary: Polyphosphate is appropriate to PAO storage. The phosphate(3-) term is
    narrower than the source phosphorus-removal and phosphate-metabolism wording;
    the study does not measure protonation/speciation. Preserve a generic process
    representation or explicitly qualify the formal chemical proxy.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - ontology
  - storage
  - removal
- assessment_id: dataset
  area: provenance
  topic: associated_datasets[0] accession and deposited scope
  outcome: supported
  summary: MG-RAST 4463936.3 independently resolves to public WWTP_EBPR_Aalborg_East
    WGS data. The main paper names the same nonredundant-contig accession. Initial
    API timeout and default browser failure were resolved using the versioned public
    API; no broken-accession finding is warranted. Pipeline metadata and original
    upload files were not reanalyzed.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - dataset
  - article
- assessment_id: evidence
  area: evidence
  topic: All EvidenceItems, methods classifications and quotation fidelity
  outcome: concern
  summary: All 22 occurrences were inspected. The selected-excerpt cache faithfully
    signals its restricted scope but has removed citations/punctuation from five passages.
    These snippets should be made contiguous rather than treated as exact full-text
    quotes. qFISH measurements are not computational evidence; introductory PAO/flanking
    physiology is background, not a new in vivo observation in this study. Graph-specific
    PARTIAL/OTHER labels are better calibrated than some taxon-level evidence.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - snippets
  - article
  - schema
- assessment_id: history
  area: provenance
  topic: Discussions, history, external resources and source limits
  outcome: supported
  summary: The open discussion correctly asks which inferred transfers drive removal;
    it does not imply those mechanisms were demonstrated. The prior graph event resolves
    and is not a whole-record approval. Missing standalone external_resources is partly
    offset by the verified dataset link; exact exchanged metabolites and dynamics
    should remain unfilled until supported. No earlier structured finding is closed
    here.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - history
  - dataset
- assessment_id: structured-source
  area: evidence
  topic: Expression-module applicability
  outcome: not_applicable
  summary: No matching organism/dataset in the inspected catalog. Community phosphate/biofilm
    potential cannot be supplied by an unrelated expression module; source metagenomics
    remains the relevant evidence.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - adapter
- assessment_id: validation
  area: schema
  topic: Deterministic gates and source retrieval
  outcome: supported
  summary: Focused gates pass and the selected cache bytes remain unchanged. All four
    participants occur in the graph and internal names resolve. Required corpus warning
    failures remain separate; these gate results do not certify source support. Primary
    HTML and versioned MG-RAST API succeeded after initial failures.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - check-validate
  - check-validate-strict
  - check-validate-terms
  - check-validate-references-explained
  - check-audit-network
  - dataset
- assessment_id: metrics
  area: completeness
  topic: Native completeness and validation quality
  outcome: concern
  summary: Completeness is 85. Native validation quality caps at 100 despite one major
    and four minor findings because of evidence/reference integrity bonuses; it is
    not scientific approval.
  target_ids:
  - CommunityMech:000139
  evidence_ids:
  - record
  - check-audit-network
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: min(100,50 required metadata with taxonomy roles +5 environment +10
      if at least 3 factors +10 if at least 3 nodes +5 external_resources +10 growth_media
      +5 datasets +5 any node metabolites). Applied 50+5+0+10+0+10+5+5=85. Field presence
      only.
  - name: validation_quality
    value: 100
    unit: points
    minimum: 0
    maximum: 100
    definition: 'clamp(100-50*P1-10*P2-2*P3+20*min(mean evidence/2,1)+15 for COMPLETE
      network,0,100). P1=0,P2=1,P3=4; node evidence 5/4=1.25 gives 12.5 points. All
      four participants and references intact: COMPLETE bonus 15. Raw 100-10-8+12.5+15=109.5,
      capped at 100.'
  - name: P1
    value: 0
    unit: findings
    definition: Target native severity count.
  - name: P2
    value: 1
    unit: findings
    definition: Target native severity count.
  - name: P3
    value: 4
    unit: findings
    definition: Target native severity count.
  - name: interaction_evidence
    value: 1.25
    unit: evidence items per interaction
    denominator: 4
    definition: Five direct EvidenceItems across four nodes, all from one publication;
      not independent replication.
findings:
- finding_id: functional-roles
  issue_key: cm-000139-functional-roles
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: 'P2 major: functional attribution exceeds the supported ecological
    role.'
  rule_id: P2.4
  status: open
  certainty: confirmed
  title: Taxon roles assert functions beyond the qualified graph
  description: Accumulibacter and Tetrasphaera-related PAO storage is not evidence
    for degradation of complex substrates. Flanking-community and PAO cross-feeding/secondary-fermentation
    roles are stated unconditionally while the source and graph frame transfer as
    background hypotheses. Bacteroidota hydrolytic context is plausible but does not
    validate the whole broad guild.
  target_ids:
  - CommunityMech:000139
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  - taxonomy[2].functional_role
  - taxonomy[3].functional_role
  evidence_ids:
  - record
  - schema
  - taxon-evidence
  - flanking
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
- finding_id: evidence-fidelity
  issue_key: cm-000139-evidence-fidelity
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded evidence or structured-context defect;
    the source community and principal outcomes remain identifiable.'
  rule_id: CLAUDE.claim-level-evidence
  status: open
  certainty: confirmed
  title: Evidence categories and edited excerpts need narrower attribution
  description: The qFISH abundance item is marked COMPUTATIONAL; introductory physiological
    statements are marked IN_VIVO. Five snippets are noncontiguous after source citations/punctuation
    were silently removed, although recognizable source wording remains. This is a
    bounded evidence/provenance problem, not fabricated biology.
  target_ids:
  - CommunityMech:000139
  field_paths:
  - taxonomy[0].evidence
  - taxonomy[1].evidence[0]
  - taxonomy[2].evidence[0]
  - taxonomy[3].evidence[0]
  - related_ingredients[1].evidence[0]
  - associated_datasets[0].evidence[0]
  evidence_ids:
  - snippets
  - article
  - schema
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
- finding_id: phosphate-specificity
  issue_key: cm-000139-phosphate-specificity
  category: representation
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded evidence or structured-context defect;
    the source community and principal outcomes remain identifiable.'
  rule_id: review-checklist.grounding
  status: open
  certainty: confirmed
  title: Chemical specificity exceeds the reported phosphorus endpoint
  description: CHEBI:18367 denotes phosphate(3-), whereas the source reports phosphate
    metabolism and whole-plant P removal without charge-state or species measurement.
    The label resolves, but downstream consumers could mistake the formal representation
    for a measured ion-specific flux.
  target_ids:
  - CommunityMech:000139
  field_paths:
  - related_ingredients[0]
  - ecological_interactions[0].metabolites[0]
  - ecological_interactions[3].metabolites[0]
  evidence_ids:
  - ontology
  - storage
  - removal
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
- finding_id: media-linkage
  issue_key: cm-000139-media-linkage
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded evidence or structured-context defect;
    the source community and principal outcomes remain identifiable.'
  rule_id: P3.1
  status: open
  certainty: confirmed
  title: Variable wastewater medium has no verified linkage
  description: The domestic-wastewater medium lacks CultureMech/MediaIngredientMech
    identifiers under the native linkage rubric. Its variable environmental feed may
    legitimately have no exact defined-medium match.
  target_ids:
  - CommunityMech:000139
  field_paths:
  - growth_media[0]
  evidence_ids:
  - record
  - cultivation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
- finding_id: environment-sparse
  issue_key: cm-000139-environment-sparse
  category: completeness
  severity: minor
  native_severity: P3
  normalization_reason: 'P3 minor: bounded evidence or structured-context defect;
    the source community and principal outcomes remain identifiable.'
  rule_id: P3.4
  status: open
  certainty: confirmed
  title: Only two structured factors capture the non-minimal plant context
  description: The native rubric expects at least three environmental factors. The
    source additionally reports influent 10–20 mg P/L and effluent below 0.5 mg P/L;
    current record factors omit those available quantitative boundary conditions.
  target_ids:
  - CommunityMech:000139
  field_paths:
  - environmental_factors
  evidence_ids:
  - record
  - cultivation
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
actions:
- action_id: fix-functional-roles
  description: Align each role with a same-population supported function, retaining
    uncertainty rather than manufacturing complex-substrate degradation or measured
    transfer.
  finding_ids:
  - functional-roles
  target_ids:
  - CommunityMech:000139
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Each role satisfies its schema definition and narrow source context.
  - Genomic or background potential is not presented as measured metabolism.
  - Run focused strict, references-explained and network checks after authorized curation.
- action_id: fix-evidence-fidelity
  description: Use short contiguous primary passages and classify evidence at the
    actual assay or background claim; do not rewrite source text to satisfy matching.
  finding_ids:
  - evidence-fidelity
  target_ids:
  - CommunityMech:000139
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
  acceptance_checks:
  - All retained quotations match contiguous inspected primary text under declared
    whitespace normalization.
  - qFISH, metagenomics and background claims remain distinct.
  - Run references-explained and strict gates; manually inspect exact source correspondence.
- action_id: fix-phosphate-specificity
  description: Choose a source-compatible chemical abstraction or explicitly document
    the proxy, retaining total-phosphorus endpoint units separately.
  finding_ids:
  - phosphate-specificity
  target_ids:
  - CommunityMech:000139
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
  acceptance_checks:
  - No ion-specific concentration or removal is inferred from total P.
  - Any replacement chemical identifier is independently verified.
  - Run term, strict and evidence validation after authorized curation.
- action_id: fix-media-linkage
  description: Check exact compatible linkage only; document unmatched environmental
    feed if appropriate instead of assigning a nearby laboratory recipe.
  finding_ids:
  - media-linkage
  target_ids:
  - CommunityMech:000139
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Any link resolves to the same material/formulation scope.
  - Unmatched variable wastewater is explicitly retained as such.
  - Run applicable linkage and strict checks after authorized curation.
- action_id: fix-environment-sparse
  description: Add narrowly sourced plant phosphorus-loading or sampling context without
    inventing missing operational setpoints.
  finding_ids:
  - environment-sparse
  target_ids:
  - CommunityMech:000139
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    role: canonical_record
  acceptance_checks:
  - Separate influent from effluent and retain total-P mass units.
  - No PCR temperature or unsupported pH/HRT/SRT is added as cultivation.
  - Run strict and references-explained validation after authorized curation.
limitations:
- Full main article inspected through public PMC HTML and primary metadata; supplements
  and raw sequencing files were not independently analyzed. The committed cache contains
  selected excerpts only.
- Historical GTDB support counts, six-species statement and prior mapping-tool history
  were not independently rebuilt; present canonical/coherence/domain checks passed.
- Phosphate charge state was not measured. Operational CONTINUOUS is inferred from
  the described full-scale plant rather than a reported dilution-rate experiment.
- Initial full-text XML and default MG-RAST requests failed; primary HTML and alternate
  public API resolved the needed source and accession.
- Optional expression-module adapter unavailable in the isolated runtime; public catalog
  contains no matching organism. Required network corpus gates fail on unrelated warnings.
- Native scores measure presence and validation features; high scores do not resolve
  unsupported roles or other findings.
notes:
- No record, source cache, history, generated product or scientific-status field changed.
  Proposed curation needs separate authorization.
- All initial input hashes were checked unchanged. Exact short quotations total at
  most 25 words for the publication and are shared across node/edge assessments.
tags:
- record-review
- ebpr
- activated-sludge
- batch-01
```
