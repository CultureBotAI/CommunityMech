# Dangl SynComm35 record review

- Review: 20261022T034933Z-dangl-syncomm-35-record-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T03:37:26.412849Z
- Finished UTC: 2026-10-22T03:49:33.469377Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Three major findings address host/member placement, conflated cultivation protocols and unsupported non-graph claims. Two minor findings address GTDB provenance and resource traceability. The four qualified nodes and two arrows remain supported. Eight focused checks pass; five disconnected taxa prevent the network bonus. Literal completeness85 and quality76 are separate from the completed source review.

## Scope And Provenance

Whole maintained record, fresh main article and complete author-hosted SI Methods/text, all five main figures and ten SI figures; current taxonomy, media and declared data/code evidence. Seven separate spreadsheets remain unread.

Selection: Only released CommunityMech:000022 in owned batch14.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e117e3d37c65bfad2e04af53ab34e1325d8d7f98.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000022 | kb/communities/Dangl_SynComm_35.yaml | maintained | Jeff Dangl's SynComm 35 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000022 | Actual native exit0. |
| validate-strict | passed | True | CommunityMech:000022 | Actual native exit0. |
| validate-terms | passed | True | CommunityMech:000022 | Actual native exit0. |
| validate-references-explained | passed | True | CommunityMech:000022 | Actual native exit0. |
| validate-gtdb | passed | True | CommunityMech:000022 | Actual native exit0. |
| validate-gtdb-domain | passed | True | CommunityMech:000022 | Actual native exit0. |
| validate-history | passed | True | CommunityMech:000022 | Actual native exit0. |
| normalize-cache-names-check | passed | True | CommunityMech:000022 | Actual native exit0. |
| audit-network corpus context | failed | False | CommunityMech:000022 | Actual corpus exit1 retained. |
| check-network-quality corpus context | failed | False | CommunityMech:000022 | Actual corpus exit1 retained. |
| Optional structured source adapter | unavailable | False | CommunityMech:000022 | Unavailable in owned runtime. |

## Scientific And Domain Assessments

### Host and source member identity

identity: concern. Targets: CommunityMech:000022.

The host is misplaced as a microbial member and two genus placeholders need source reconciliation.

Retain the 35-member design and explicit DH5alpha control. Figure 3A labels MF360 Mycobacterium rather than Microbacterium; Stenotrophomonas is unsupported by that complete displayed roster. Keep Arabidopsis as an outside-community graph participant. Do not force all 35 stocks into species-level entries from the unread Dataset S1.

### Stage-specific culture and plant assays

evidence: concern. Targets: CommunityMech:000022.

The existing generic TSB/half-MS blocks conflate procedures contradicted by the recovered SI.

Separate bacterial assembly, Johnson germination and chronic treatment, half-MS 16S sampling, acute MS/GUS, smaller-SynCom challenges and cell-free fractions. Plant-free, axenic and cell-free are distinct. Repair temperature, light, medium, shaking and dose by assay, not a global replacement.

### Roles, suppression counts and background ligands

evidence: concern. Targets: CommunityMech:000022.

Metabolic role tags and several non-graph explanations exceed the source context.

Keep assay-specific counts and the source’s 23-versus-24 distinction. Control membership is not cross-feeding, immune facilitation is not syntrophic metabolism, and background chitin/peptidoglycan statements are not direct suppression tests. No environmental metal/REE measurement is established by recipe salts.

### Root flg22 Immune Suppression

graph: supported. Targets: CommunityMech:000022.

Retain community-level suppression and its participant subset; live established community, day12 versus day1 and killed/no-bacteria controls matter. The current SUPPORT/IN_VITRO Abstract evidence remains source-compatible without attributing the whole outcome solely to MF79.

Exact selector ecological_interactions[0]; scope COMMUNITY_LEVEL; interaction_type untyped. Encoded taxa: {"source": null, "target": null, "participants": [{"preferred_term": "Arabidopsis thaliana", "term": {"id": "NCBITaxon:3702", "label": "Arabidopsis thaliana"}}, {"preferred_term": "Dyella japonica MF79", "term": {"id": "NCBITaxon:231455", "label": "Dyella japonica"}}]}. Canonical excerpt bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "2dc66193cd546504b3cd9bedafe661d0574273af20e4702739fb9bd4341ce325", "reference": "PMID:33879573", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 4351280d84327d4291e875b3ab15640ec4650469cf1b63844ab87749c2f9bc94. Source contexts and retained tiers are specified in the linked evidence and summary.

### Root flg22 Immune Suppression → Suppression-Associated Root Colonization Facilitation

graph: supported. Targets: CommunityMech:000022.

Retain the qualified directed link and its conditional experimental scope.

Exact selector ecological_interactions[0].downstream[0]; source node Root flg22 Immune Suppression; target node Suppression-Associated Root Colonization Facilitation. Exact encoded description: Suppression can facilitate nonsuppressor root colonization under the tested conditions. MF79 wild-type retentate, unlike T2SS-mutant material, countered the flg22-associated reduction in Ochrobactrum MF370 colonization. This does not establish universal facilitation by every suppressor or reciprocal benefit.. Description SHA256 4f36927e5108e17b6e00bb05226918aeb7fb99d3f36d4b84a3d1ea88afa1b2ee. Figure 5E and Results s5 paragraph2: MF79 WT retentate, compared with secretion-mutant fractions, conditionally rescues the tested nonsuppressor under flg22. This is not reciprocal fitness or universal suppression-to-colonization causality.

### Community-Associated WRKY Transcript Suppression

graph: supported. Targets: CommunityMech:000022.

Retain community-associated WRKY transcription as a separate readout. The broad Abstract excerpt is correctly PARTIAL/IN_VITRO; full Results and SI Figure S2 supply detail without establishing downstream WRKY mediation.

Exact selector ecological_interactions[1]; scope COMMUNITY_LEVEL; interaction_type untyped. Encoded taxa: {"source": null, "target": null, "participants": [{"preferred_term": "Arabidopsis thaliana", "term": {"id": "NCBITaxon:3702", "label": "Arabidopsis thaliana"}}, {"preferred_term": "Dyella japonica MF79", "term": {"id": "NCBITaxon:231455", "label": "Dyella japonica"}}]}. Canonical excerpt bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "2dc66193cd546504b3cd9bedafe661d0574273af20e4702739fb9bd4341ce325", "reference": "PMID:33879573", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 4351280d84327d4291e875b3ab15640ec4650469cf1b63844ab87749c2f9bc94. Source contexts and retained tiers are specified in the linked evidence and summary.

### MF79 Type II Secretion-Dependent Immune Modulation

graph: supported. Targets: CommunityMech:000022.

Retain the MF79-to-host T2SS-dependent assay and SUPPORT/IN_VITRO evidence. T2SS perturbations and filtrates support this component; the effector remains unknown and the tested T3SS mutants differ.

Exact selector ecological_interactions[2]; scope PAIRWISE; interaction_type untyped. Encoded taxa: {"source": {"preferred_term": "Dyella japonica MF79", "term": {"id": "NCBITaxon:231455", "label": "Dyella japonica"}}, "target": {"preferred_term": "Arabidopsis thaliana", "term": {"id": "NCBITaxon:3702", "label": "Arabidopsis thaliana"}}, "participants": []}. Canonical excerpt bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "f167aa90b194d02705c8b957a2727c24d5640c33ca3ddd40a8ee4910f0aa1bcb", "reference": "PMID:33879573", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 4351280d84327d4291e875b3ab15640ec4650469cf1b63844ab87749c2f9bc94. Source contexts and retained tiers are specified in the linked evidence and summary.

### MF79 Type II Secretion-Dependent Immune Modulation → Root flg22 Immune Suppression

graph: supported. Targets: CommunityMech:000022.

Retain the qualified directed link and its conditional experimental scope.

Exact selector ecological_interactions[2].downstream[0]; source node MF79 Type II Secretion-Dependent Immune Modulation; target node Root flg22 Immune Suppression. Exact encoded description: MF79 T2SS function enables its extracellular suppressive activity in the root reporter assay. This arrow applies to the MF79 component of the suppression node, not necessity of T2SS for the entire SynCom35 phenotype.. Description SHA256 0dcd5a4c5673efaf6a5ca10804d748553f589e76006eb02de796591a361bebf4. Figure 5A–D and Results s5 paragraphs1–2: MF79 secretion perturbation establishes a contributing component, not T2SS necessity for all 35 members or every suppressor.

### Suppression-Associated Root Colonization Facilitation

graph: supported. Targets: CommunityMech:000022.

Retain COLONIZATION_FACILITATION for the tested smaller-SynCom and fraction contexts, with SUPPORT/IN_VITRO Significance evidence. Participating taxa are a subset, not an exhaustive census; no reciprocal nutrient exchange is inferred.

Exact selector ecological_interactions[3]; scope COMMUNITY_LEVEL; interaction_type COLONIZATION_FACILITATION. Encoded taxa: {"source": null, "target": null, "participants": [{"preferred_term": "Arabidopsis thaliana", "term": {"id": "NCBITaxon:3702", "label": "Arabidopsis thaliana"}}, {"preferred_term": "Dyella japonica MF79", "term": {"id": "NCBITaxon:231455", "label": "Dyella japonica"}}, {"preferred_term": "Pseudomonas species", "term": {"id": "NCBITaxon:286", "label": "Pseudomonas"}}]}. Canonical excerpt bindings: [{"selector": "ecological_interactions[3].evidence[0].snippet", "sha256": "1d068bea1ee160ac0852ac1d630d449eabb76ca4f5238d3d3d2d32726724234f", "reference": "doi:10.1073/pnas.2100678118", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Snippet audit SHA256 4351280d84327d4291e875b3ab15640ec4650469cf1b63844ab87749c2f9bc94. Source contexts and retained tiers are specified in the linked evidence and summary.

### Correct labels with bounded mapping provenance

grounding: concern. Targets: CommunityMech:000022.

Twenty ID-label pairs match, but seven mapping_source statements overstate release/build provenance.

Preserve valid GO and chemical identities, source labels and rank routes. Resolve membership before carrying a mapping to a corrected genus. RHIZOSPHERE is source provenance/model context; the assays themselves are gnotobiotic plates or liquid, not soil. COMMON is ordinal rather than a numerical cutoff.

### Study outputs and imported medium links

provenance: concern. Targets: CommunityMech:000022.

Current resource identities are recoverable, but old routes and source-to-resource traceability need repair.

GEO host-transcriptome subseries, 16S colonization libraries and analysis code have separate scopes. Generic CultureMech identity does not establish the experimental recipe; the imported MS record is circular as primary support. No missing scientific dataset is inferred merely from unavailable spreadsheets.

### Maintained YAML and prior curation

ownership: supported. Targets: CommunityMech:000022.

The focal YAML owns the proposed repairs; existing graph qualifications and prior provenance remain intact.

No source/cache/history, issue or Git mutation is part of this review.

### Native checks versus scientific support

schema: supported. Targets: CommunityMech:000022.

Eight focused checks pass. Five target DISCONNECTED warnings and the separate corpus/adapter outcomes remain explicit.

The disconnected taxa are DH5alpha, Flavobacterium, Microbacterium, Stenotrophomonas and Xanthomonadales. Their presence in a diagnostic does not justify invented edges. The graph has four nodes, one typed node, two arrows and four evidence placements.

### Literal completeness and quality

completeness: supported. Targets: CommunityMech:000022.

Completeness85 and quality76, calculated independently of source confidence.

## Findings

### member-identity: Reconcile the host and unsupported member placeholders

major / open / confirmed; issue key: cm-000022-member-identity.

The taxonomy slot includes the plant host, although its schema excludes hosts. Figure 3A identifies MF360 as Mycobacterium rather than the encoded Microbacterium, and its complete 35-row panel does not support Stenotrophomonas. Reconcile these placements while retaining the explicitly included DH5alpha control; do not invent a complete modern stock inventory from unread Dataset S1.

### cultivation: Replace conflated culture conditions with the actual assay stages

major / open / confirmed; issue key: cm-000022-cultivation.

The generic TSB and half-MS recipes, light/temperature/shaking values and inoculum statements conflate stages and conflict with the recovered SI. Primary assembly uses 2xYT and CFU-based dosing; Johnson plant culture, chronic exposure, half-MS 16S, acute MS/GUS and LB/fraction assays are separate. Water1g/L is not a valid solvent-volume recipe, and axenic plants are not plant-free experiments.

### claim-scope: Constrain non-graph roles, counts and ligand explanations

major / open / confirmed; issue key: cm-000022-claim-scope.

The six SYNTROPHIC_PARTNER tags and DH5alpha CROSS_FEEDER tag lack metabolic evidence. The 10+13+11 partition mixes different suppression endpoints; source chronic24/35 and cross-assay23/35 remain distinct. Background chitin/peptidoglycan text does not support the attached experimental suppression explanations, and recipe salts do not support the generic metal/REE measurement claim.

### gtdb-provenance: Use verifiable GTDB snapshot provenance

minor / open / confirmed; issue key: cm-000022-gtdb-provenance.

Seven existing mapping cores reproduce against the current reference snapshot, but latest and built2026-07-25 are not established by its filesystem mtime. Preserve correct rank/name/ID routes and reference-genome scope, subject to resolving membership first.

### resources: Repair resource routes and add scoped study outputs

minor / open / confirmed; issue key: cm-000022-resources.

Five encoded resource URLs are obsolete. Both CultureMech identities resolve at current locations, but the MS import is circular as primary study evidence and current chemical records do not prove legacy MIM numeric identity. The article also declares verified GEO, 16S and code outputs whose distinct scopes can be recorded.

## Recommended Actions And Acceptance Checks

### repair-membership

Reconcile membership against the source and literal schema.

- Remove Arabidopsis from microbial taxonomy while retaining its valid host identity and graph participation. Retain the source-supported DH5alpha control. Distinguish order/genus aggregates from individual stock entries; do not automatically expand the record to 35 species.
- Correct the MF360 Microbacterium placeholder using the source Mycobacterium label and verified genus NCBITaxon:1763; preserve MF360 as a source isolate label without inventing a species/genome assignment. Reconcile Stenotrophomonas with a documented source alias/roster or remove the unsupported placeholder. Dataset S1 remains unread, so do not certify an exhaustive modern stock crosswalk.
- Recheck every affected participant and mapping after membership repair. The existing host and supported MF79/Pseudomonas participant descriptors remain valid; no automatic graph deletion follows.

### repair-cultivation

Encode distinct source protocols with claim-local evidence.

- SI p2 SynCom assembly: 4mL 2xYT in test tubes, tryptone16g/L, yeast extract10g/L, NaCl5g/L; 28°C,250rpm,1–2days. Wash twice in10mM MgCl2. Dose each strain at10^5CFU/mL using the stated OD1≈10^9CFU/mL assumption. The500mL is a medium preparation batch, not a plant vessel capacity. Do not retain unsupported generic TSB pH7.3,180rpm,24h or OD0.001.
- SI p2 Johnson recipe per litre: sucrose5g, KH2PO4 85mg, KNO3 0.6g, Ca(NO3)2·4H2O 0.9g, MgSO4·7H2O 0.2g, KCl3.8mg, H3BO3 1.5mg, MnSO4·H2O0.8mg, ZnSO4·7H2O0.6mg, CuSO4·5H2O0.1mg, H2MoO4 16.1µg, FeSO4·7H2O1.1mg, myo-inositol0.1g and MES0.5g; pH5.6–5.7 and1%agar. Preserve source units/hydration and solvent volume rather than water1g/L. No unsupported new chemical identifier is required.
- Separate seven-day germination16h light/8h dark at21°C day/18°C night from chronic treatment9h light/15h dark at21/18°C, with1µM flg22 and day1/day12 harvests. Retain live,100°C2h heat-killed and no-bacteria arms. Do not treat axenic host plants as plant-free, or invent100µmol light intensity.
- SI p7 half-strength MS with vitamins,pH5.7,1%agar belongs to the16S procedure. SI p10 acute assay has1mL MS with vitamins (strength unspecified),MES0.5g/L,sucrose0.5%,pH5.7 in12-well plates; seven-day seedlings receive single strains atOD0.002 forabout14h, then100nM flg22 for5h. Do not transfer the record’s1%sucrose/0.8%agar/22°C into all stages.
- Keep smaller-SynCom and LB challenge procedures separate: SI pp12–13 uses3mL LB,28°C,250rpm,24h, defined low-OD precolonization/challenge and a48h postchallenge endpoint. SI p16 MF79 filtrates use1xMS,5g/L sucrose,0.1%casamino acids,OD0.02,21°C,250rpm,18h; the MF370 assay exchanges fractions into sucrose-free half-MS. Preserve each source dose/time and controls without implying a single SynCom35 recipe.
- Replace generic evidence with the exact relevant SI Method heading/paragraph and stage. Do not use a generic CultureMech import as independent proof of the paper’s protocol.

### repair-claim-scope

Qualify unsupported non-graph claims while retaining supported ecological effects.

- Remove or qualify optional SYNTROPHIC_PARTNER and DH5alpha CROSS_FEEDER tags unless claim-local metabolic evidence is supplied. Do not replace them with invented mandatory roles. Preserve immune modulation, secretion perturbation and colonization facilitation as supported phenotypes.
- Describe chronic transcription24/35 partial/full suppressors and11 without that effect separately from10 robust cross-assay suppressors and23/35 with any tested activity. Retain the source’s endpoint-sensitive23-versus24 discrepancy; do not silently force a single partition summing to35.
- Keep chitin/peptidoglycan only as correctly labelled background MAMP examples, or supply direct ligand-specific evidence before asserting suppression. Correct the current SUPPORT/IN_VIVO explanations that turn background into a focal result. Remove the unsupported generic metal/REE measurement assertion; medium salts and staining reagents are not environmental measurements.
- Preserve all four qualified nodes and both directed links, their exact source contexts and current evidence tiers. Do not infer reciprocity, universal MF79/T2SS necessity, an identified secreted effector or WRKY mediation of colonization.

### repair-gtdb

Use honest snapshot and mapping-route provenance.

- Replace the seven latest/build-date assertions with actual snapshot SHA256761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd and unknown release when no release evidence exists. Filesystem mtime is not a release/build date.
- Preserve supported cores and routes: Dyella231455 name fallback, two reference genomes; Lysobacterales135614 rank aggregation7047/7047; Pseudomonas17956/25706 with11 total destinations; Flavobacterium859/860 with2; Stenotrophomonas398/404 with2; Microbacterium591/591 with1; DH5alpha668369 exact ID with4/4. These are reference supports, not community abundances or study-stock classifications. Recompute affected mappings after membership corrections, rather than transferring Microbacterium grounding to Mycobacterium.
- Keep source names, current NCBI labels and the name-comparison meaning of is_reclassified separate. Preserve the host’s valid eukaryotic GTDB exclusion wherever its descriptor is retained.

### repair-resources

Restore resolvable links and add scoped study resources.

- Use verified current routes for CultureMech008226 and015433 only where a generic recipe link remains useful after protocol repair. State that the MS record imports CommunityMech000003/000022 and is not independent source support. Do not preserve obsolete MIM URLs merely because water,sucrose and agar have correct chemical identities; currentCHEBI15377/17992/2509 records are candidates, not proof of legacy numeric-ID continuity.
- Add source-declared GEO GSE156426 with subseries GSE156424(MAE666 sample IDs),GSE156425(RST100) andGSE157027(SSC18). The784-ID union is not784 independent biological cultures. Retain study/assay scope and do not promote unread sample or expression matrices to verified results.
- Add PRJNA657936/SRP278111 as the separate16S colonization project,72 paired MiSeq PCR libraries; preserve registry strategyOTHER/sourceMETAGENOMIC versus source amplicon description. Do not call these35 isolate genomes or host RNA-seq.
- Add https://github.com/ncolaian/MAE at inspected commit6dc674a1e23ed0b2128544d86d808472896f1f12 as analysis code. The159-entry tree and666-row design labels do not provide genus-resolved Dataset S1. No raw download, code execution or contact is needed for this repair.

### validate-future-curation

Validate any separately authorized repair.

- Recheck literal schema, ontology labels, exact references, GTDB/domain, history and graph context after source-backed edits. Five disconnected warnings do not authorize invented interactions or forced topology changes.
- Run just gen-html and just check-docs-current after authorized curation. Append appropriate provenance and preserve original cache/history/source bytes. This review changes no canonical record, generated page, issue or Git state.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/Dangl_SynComm_35.yaml; Whole maintained YAML | supports | The record represents the designed SynCom35 and distinguishes community suppression, WRKY transcription, MF79 secretion and conditional colonization facilitation. |
| membership | PMID:33879573; DOI:10.1073/pnas.2100678118; Figure 3A, complete 35-row panel; SI Appendix, Preparation of bacterial synthetic communities (SynComs), first paragraph, printed p2 / physical PDF p12 | supports | The assembly comprises 32 root isolates, two soil isolates and an E. coli DH5alpha control. Figure 3A labels MF360 Mycobacterium; none of its 35 labels is Stenotrophomonas. Arabidopsis is the experimental host. The unread Dataset S1 does not supply a verified modern stock/genome inventory here. |
| membership-figure | PMID:33879573; DOI:10.1073/pnas.2100678118; Figure 3A, all 35 named rows | supports | The figure independently supports the MF360 genus distinction and preserves the explicit E. coli control row. Broad order/genus aggregates are not a 35-stock census. |
| cultivation | PMID:33879573; DOI:10.1073/pnas.2100678118; SI Appendix, Materials and Methods, Preparation of bacterial synthetic communities (SynComs), second paragraph; printed p2 / physical PDF p12 | supports | Assembly preculture uses 4 mL 2xYT (16 g/L tryptone, 10 g/L yeast extract, 5 g/L NaCl) in test tubes, 28°C, 250 rpm and 1–2 days; two washes in 10 mM MgCl2 precede dosing each strain at 10^5 CFU/mL into a 500 mL medium preparation. The source assumes OD1 corresponds to 10^9 CFU/mL. |
| plant-protocol | PMID:33879573; DOI:10.1073/pnas.2100678118; SI Appendix, Preparation of plants for bacteria and flg22 treatments, sole paragraph, p2; Treatment of plants with flg22 in the presence of SynComs, two paragraphs, pp2–3 | supports | Johnson medium has 5 g/L sucrose, 1% agar and pH5.6–5.7. Seven-day germination uses 16 h light/8 h dark at 21°C day/18°C night; chronic SynCom/flg22 treatment uses 9 h light/15 h dark at the same temperatures and harvests at 1 and 12 days. Live, heat-killed and no-bacteria controls are distinct. |
| other-protocols | PMID:33879573; DOI:10.1073/pnas.2100678118; SI Appendix, DNA extraction for 16S sequencing, first paragraph, p7; Evaluation of the root acute response to flg22, sole paragraph, p10; Evaluation of the growth of commensals in the presence of SynComs, pp12–13; Suppression of the flg22 response by D. japonica MF79 cell-free supernatant, p16; Non-suppressor MF370 growth with MF79 10 kDa suppressive fraction, pp16–17; Figures S6–S10 | supports | Half-MS 16S culture, acute MS/GUS assays, smaller-SynCom challenge and MF79 filtrate production have separate media, inocula, doses and exposure schedules. Neither a generic TSB recipe nor one half-MS/light regime describes them all. |
| counts | PMID:33879573; DOI:10.1073/pnas.2100678118; Results, Dissecting the Immunomodulatory Activity of Commensals (s3), whole section and Figures 2–3 | supports | The source distinguishes 24/35 partial or complete chronic-transcription suppressors and 11 without that effect from 10 robust cross-assay suppressors and 23/35 with activity in at least one assay. These statements cannot be collapsed into the current 10+13+11 partition. |
| background | PMID:33879573; DOI:10.1073/pnas.2100678118; Abstract; main introductory MAMP context before Results; Discussion (s6), paragraphs 1–4; SI assay Methods | supports | Chitin and peptidoglycan are background MAMP examples, not demonstrated focal suppression endpoints. Immune modulation and colonization facilitation do not establish syntrophic metabolism or DH5alpha metabolite utilization. Trace-medium salts do not establish environmental metal or REE measurements. |
| suppression | PMID:33879573; DOI:10.1073/pnas.2100678118; Abstract; Results, A Community of Root Commensals Suppresses MTI (s2), paragraphs 2–4; Figure 1B–H | supports | Live established SynCom35 suppresses chronic flg22 transcriptional and growth responses, with day-1/day-12 and heat-killed/no-bacteria controls. MF79 is a studied contributor, not the sole community cause. |
| wrky | PMID:33879573; DOI:10.1073/pnas.2100678118; Results, A Community of Root Commensals Suppresses MTI (s2), paragraph 3 and Figure 1; Discussion (s6), paragraph 2; SI Appendix Figure S2 | supports | Community-associated immune-transcript changes include WRKY-associated responses. This readout does not demonstrate WRKY mediation of every colonization phenotype; the broad current Abstract excerpt remains PARTIAL for this node. |
| secretion | PMID:33879573; DOI:10.1073/pnas.2100678118; Results, Immunomodulatory Strategies in Commensals (s5), paragraphs 1–2; Figure 5A–D; SI Appendix mutant and cell-free-supernatant Methods, pp13–16, Figure S10 | supports | MF79 gspD/gspE perturbations and extracellular fractions support T2SS-dependent modulation, whereas the tested T3SS mutants retain suppression. The responsible secreted molecular identity and a universal mechanism across all suppressors remain unresolved. |
| facilitation | PMID:33879573; DOI:10.1073/pnas.2100678118; Significance; Results, MTI can Control Colonization by Commensals (s4), paragraph 2 and Figure 4A–C; Immunomodulatory Strategies in Commensals (s5), paragraph 2 and Figure 5E; Discussion (s6), paragraph 3 | supports | Defined suppressor precolonization and MF79 fractions conditionally improve tested nonsuppressor colonization. The mutant-fraction comparison supports a specific directed component; it does not establish reciprocal nutrient exchange or community-wide necessity. |
| declared-resources | PMID:33879573; DOI:10.1073/pnas.2100678118; Data Availability (s8), sole paragraph; SI Appendix, Data and code availability, p17 | supports | The source declares GEO GSE156426, BioProject PRJNA657936 and the MAE analysis repository. The SI separately describes seven XLSX datasets, which were not recovered here. |
| ontology | /private/tmp/cm-review-session/batch-14/000022/ontology-authority.json; 20 ID-label definitions/ranks across 29 placements | supports | All current labels match their identifiers. Label validity does not prove membership or source-specific roles. |
| schema | /private/tmp/cm-review-session/batch-14/000022/child-schema-semantics.json; Literal membership, role, interaction and cultivation definitions | supports | Microbial taxonomy excludes its host. SYNTROPHIC_PARTNER denotes syntrophic metabolism and CROSS_FEEDER denotes use of another taxon’s metabolites; neither follows from immune facilitation alone. |
| membership-authority | /private/tmp/cm-review-session/batch-14/000022/child-source-membership-candidate.json; Exact source-name candidate and rank | supports | Mycobacterium NCBITaxon:1763 is a genus candidate for the source label. This is not an MF360 species or genome assignment. |
| gtdb | /private/tmp/cm-review-session/batch-14/000022/child-gtdb-crosswalk.json; Seven current bacterial mappings, routes and snapshot provenance | supports | Encoded mapping cores and reference-genome counts reproduce. Filesystem mtime does not establish the claimed release or build date; correct source membership before transferring classifications. |
| semantics | /private/tmp/cm-review-session/batch-14/000022/ontology-semantic-notes.json; Final membership, roles, graph and cultivation reconciliation | supports | Retain the four qualified nodes and two arrows. Repair membership, non-graph assertions and stage-specific procedures without inventing replacement roles or strain genomes. |
| resources | /private/tmp/cm-review-session/batch-14/000022/dataset-verification.json; Source-declared GEO series, 72 run identities and bounded code inventory | supports | GSE156426 comprises three subseries with 784 sample identifiers in their union; PRJNA657936 is the distinct 16S colonization project. The MAE tree has 159 entries. No raw matrices, sequence reanalysis or 784 independent-culture inference. |
| resource-links | /private/tmp/cm-review-session/batch-14/000022/external-resource-verification.json; Five encoded URLs and exact current record/chemical identities | supports | All five old URLs return404. Both current CultureMech identifiers resolve; the imported MS entry depends on CommunityMech records and is circular as study-method evidence. Retired numeric MIM identifiers have no match in the complete current index; exact chemical identity does not prove identifier continuity. |
| snippets | /private/tmp/cm-review-session/batch-14/000022/snippet-audit.json; All 21 canonical placements and both whole matching paragraphs | supports | All 21 excerpts strictly match fresh source and selected cache: 16 DOI Significance and five PMID Abstract. Matching does not establish entailment of the attached role, medium or ligand claim. |
| provenance | /private/tmp/cm-review-session/batch-14/000022/provenance-audit.json; Sole history, batch29 focal row/adversarial, exact cohort and current issue context | supports | Earlier graph scope repairs remain valid. Current source evidence is reconciled with the prior review; nine issue/PR bodies and eleven comments are support-reviewer scope, not a claim that all reviewers read every issue. |
| inspection | /private/tmp/cm-review-session/batch-14/000022/inspect.json; 32 immutable inputs from ignored-inclusive discovery | supports | Ten focal contexts, 21 applicable authorities and the maintained target were inspected before assessment. |
| assets | /private/tmp/cm-review-session/batch-14/000022/lead-source-assets.json; Fresh article, five figures, complete author-hosted SI and failed linked XLSX routes | supports | Ordinary public fallback recovered the complete article and SI Methods/figures. Seven separate spreadsheet datasets remain unavailable and unread; failed routes are preserved. |
| lead-read | /private/tmp/cm-review-session/batch-14/000022/lead-primary-read-scope.json; Actual whole main/SI and image read scope | supports | Lead read the whole main and all SI text, all five main figures and all ten SI figures. No raw matrices or modern 35-stock reconstruction was performed. |
| locators | /private/tmp/cm-review-session/batch-14/000022/source-locator-verification.json; Direct headings, paragraph counts and PDF page checks | supports | The named HTML sections and SI Method headings/pages were verified. The sole quotation is in the second SynCom preparation paragraph, physical PDF page12. |
| source-scope | /private/tmp/cm-review-session/batch-14/000022/source-audit.json; Final lead scientific findings | supports | Three major findings concern member placement, cultivation and non-graph claim scope. Two minor findings concern mapping provenance and resource traceability. |
| root-source | /private/tmp/cm-review-session/batch-14/000022/root-independent-source-audit.json; Independent source judgment and explicit read scope | supports | Root independently agrees the five findings, graph retention and completed current-claim review with the spreadsheet boundary. |
| root-graph | /private/tmp/cm-review-session/batch-14/000022/root-node-edge-audit.json; Independent node/arrow selectors and hashes | supports | Four nodes and two actual downstream descriptions retain their source- and treatment-specific interpretation. |
| metrics | /private/tmp/cm-review-session/batch-14/000022/support-final-audit.json; Final support, exact rubric and network diagnostic | supports | Completeness85; quality100−30−4+10=76. Five DISCONNECTED warnings prevent the COMPLETE bonus and do not justify fabricated interactions. |
| support-manifest | /private/tmp/cm-review-session/batch-14/000022/support-frozen-manifest.json; Frozen supporting files and pins | supports | Root, lead, child, source, resource and prior evidence were reconciled before rendering. |
| auxiliary | /private/tmp/cm-review-session/batch-14/000022/auxiliary-frozen-manifest.json; Frozen ontology/native artifacts | supports | All 32 official inputs remain unchanged and eight focused native checks pass. |
| final-native | /private/tmp/cm-review-session/batch-14/000022/final-validator-summary.json; Eight actual command/stdout/stderr outcomes | supports | All focused commands return0; source entailment is assessed separately. |
| corpus-context | /private/tmp/cm-review-session/batch-14/000022/child-current-corpus-context.json; Actual batch14 corpus baseline | supports | Both contextual corpus commands returned1 with 44 warnings across 16/477 records and zero errors. |
| adapter | /private/tmp/cm-review-session/batch-14/000022/adapter-check.json; Optional adapter availability | supports | Unavailable in the owned runtime; no adapter from another checkout was executed. |
| check-validate | /private/tmp/cm-review-session/batch-14/000022/validate.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-strict | /private/tmp/cm-review-session/batch-14/000022/validate-strict.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-terms | /private/tmp/cm-review-session/batch-14/000022/validate-terms.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-14/000022/validate-references-explained.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-14/000022/validate-gtdb.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-14/000022/validate-gtdb-domain.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-validate-history | /private/tmp/cm-review-session/batch-14/000022/validate-history.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-14/000022/normalize-cache-names-check.json; Actual current command/stdout/stderr | supports | Native exit0; source entailment assessed separately. |
| context-audit-network | /private/tmp/cm-review-session/batch-14/audit-network.json; Actual batch14 corpus baseline | supports | Exit1,44warnings across16/477records and zero errors. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-14/check-network-quality.json; Actual batch14 corpus baseline | supports | Exit1,44warnings across16/477records and zero errors. |

## Limits And Additional Notes

- The seven separate XLSX datasets were not recovered through the bounded public routes and remain unread. Complete main/SI Methods and figures resolve the current encoded claims; this is not a verified35-stock genome inventory or raw expression/sequence reanalysis.
- Source chronic24/35 and cross-assay23/35 suppression counts retain their named endpoint scopes. SI transcription-analysis day/hour and715/716-gene inconsistencies are not silently harmonized. Distinct100nM and1µM flg22 experiments and germination/treatment light regimes remain separate.
- GEO784 sample IDs and72 16S libraries are registry counts, not independently inspected biological samples or a replicate design reconstruction. Code and design inventory were inspected without executing analysis or reading large matrices.
- Correct ontology labels and reference-genome mappings do not establish membership, individual strain identity or metabolic roles. Five DISCONNECTED warnings are diagnostic context; they do not imply five experimentally missing interactions.
- All32 official input hashes remain unchanged. Canonical excerpt selectors/hashes and the exact two downstream descriptions are bound in the graph assessments.
- Sole source quotation: two words from SI preparation paragraph2, with PDF line-break whitespace normalized. Candidate validation and root save/post-save checks occur afterward; no future result is asserted.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T034933Z-dangl-syncomm-35-record-review
kind: record
repository: CultureBotAI/CommunityMech
title: Dangl SynComm35 record review
started_at: '2026-10-22T03:37:26.412849Z'
finished_at: '2026-10-22T03:49:33.469377Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, support and auxiliary reviewers; no person-level
    independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Three major findings address host/member placement, conflated cultivation
  protocols and unsupported non-graph claims. Two minor findings address GTDB provenance
  and resource traceability. The four qualified nodes and two arrows remain supported.
  Eight focused checks pass; five disconnected taxa prevent the network bonus. Literal
  completeness85 and quality76 are separate from the completed source review.
source:
  git_revision: e117e3d37c65bfad2e04af53ab34e1325d8d7f98
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: d2f94c87b82f59663bc2b0c91ac04a245e56fab52d8c11e6bddb559eb9237c84
    role: context
  - path: .claude/skills/ground-taxa-gtdb/SKILL.md
    sha256: 6358a4324781ce2598554dca18ef952ec03c9d4a9df33f82f5db8ea5e986969b
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
  - path: history/records/Dangl_SynComm_35/2026-10-06T052450Z-codex-4c42b0.yaml
    sha256: dab9ffe4601c981bcf3cd1d84cc96c1e6606989d3faaa958458e091195fe1bd1
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/Dangl_SynComm_35.yaml
    sha256: 9a828b5a59f88ca41699338a0187ebbe4d59da5b05fcc4ef40cf788b2ee9a277
    role: target
  - path: references_cache/PMID_33879573.txt
    sha256: 8e9a737c19f0295881f838aa908d7db935e86b4bca610554a720556d938ec26a
    role: context
  - path: references_cache/doi_10.1073_pnas.2100678118.json
    sha256: 5d541c1d565a0cfb8f30d7a07ef3462864d7f6dd7b83db8159c0c0d4ad3540d8
    role: context
  - path: references_cache/doi_10.1073_pnas.2100678118.md
    sha256: c7509632de060d3081807e1649cae4edec25e8adc2255a73ced6bea14cbbaa0c
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch29.yaml
    sha256: 415dcecde7cce6c3c2a1ca637de252b53d6d0d5ce225ef97dc2c0a8336546a5f
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch29.yaml
    sha256: 6627d37b0aad90ee137572b39e5b4039380bfd01f7e0c16912d7cb10a3c78439
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.md
    sha256: e432615b147787c8d009d96d2f11e5b78a45927bf9c69e45ec0d31123d1fc2e9
    role: context
  - path: reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.yaml
    sha256: 37d089fd55c077793dd20d868b50c47cb1cceab6dae6a82887cc938bee05fa6d
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/frozen_inventory_metrics.tsv
    sha256: d5a47bbcc3745a489ff507680aa7360a6a65ce070ce4ec88f886b70128791313
    role: context
  - path: reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/review_report.md
    sha256: 4e7781aa8cdfc4bb42d896ebe75920719d9dcade92ffc4a0ae07af7481cb37b3
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/gtdb_ground.py
    sha256: 0fc1ba926a56e5be85cdf064db0cf56452aeeee93f15b0ced98e8f11b5296175
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
- target_id: CommunityMech:000022
  path: kb/communities/Dangl_SynComm_35.yaml
  label: Jeff Dangl's SynComm 35
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
scope:
  description: Whole maintained record, fresh main article and complete author-hosted
    SI Methods/text, all five main figures and ten SI figures; current taxonomy, media
    and declared data/code evidence. Seven separate spreadsheets remain unread.
  selection: Only released CommunityMech:000022 in owned batch14.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000022
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000022
  command: just --no-dotenv validate kb/communities/Dangl_SynComm_35.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000022
  command: just --no-dotenv validate-strict kb/communities/Dangl_SynComm_35.yaml --out
    /private/tmp/cm-review-session/batch-14/000022/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000022
  command: just --no-dotenv validate-terms kb/communities/Dangl_SynComm_35.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000022
  command: just --no-dotenv validate-references-explained kb/communities/Dangl_SynComm_35.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000022
  command: just --no-dotenv validate-gtdb kb/communities/Dangl_SynComm_35.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000022
  command: just --no-dotenv validate-gtdb-domain kb/communities/Dangl_SynComm_35.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000022
  command: just --no-dotenv validate-history history/records/Dangl_SynComm_35
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit0.
  target_ids:
  - CommunityMech:000022
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
  scope_note: Focused target/history check; cache-name preflight is corpus-wide.
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit1 retained.
  target_ids:
  - CommunityMech:000022
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
  - corpus-context
  scope_note: Nonrequired corpus context, not wholly attributed to this target.
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit1 retained.
  target_ids:
  - CommunityMech:000022
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-14/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
  - corpus-context
  scope_note: Nonrequired corpus context, not wholly attributed to this target.
- check_id: optional-structured-adapter
  name: Optional structured source adapter
  status: unavailable
  required: false
  summary: Unavailable in owned runtime.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - adapter
  scope_note: No external-checkout adapter execution.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/Dangl_SynComm_35.yaml
  locator: Whole maintained YAML
  summary: The record represents the designed SynCom35 and distinguishes community
    suppression, WRKY transcription, MF79 secretion and conditional colonization facilitation.
  support: supports
  accessed_at: '2026-10-22T03:49:33.433711Z'
- evidence_id: membership
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: Figure 3A, complete 35-row panel; SI Appendix, Preparation of bacterial
    synthetic communities (SynComs), first paragraph, printed p2 / physical PDF p12
  summary: The assembly comprises 32 root isolates, two soil isolates and an E. coli
    DH5alpha control. Figure 3A labels MF360 Mycobacterium; none of its 35 labels
    is Stenotrophomonas. Arabidopsis is the experimental host. The unread Dataset
    S1 does not supply a verified modern stock/genome inventory here.
  support: supports
  accessed_at: '2026-10-22T03:49:33.433792Z'
  snapshot_sha256: f8972d0247d5d2fc7690771c5d5b0569b12cc6107dcd852d444fbeb806c83107
  search_scope: Complete Figure 3A labels and recovered SI preparation paragraph;
    bounded membership check, not absence from every unavailable workbook or current
    classification.
- evidence_id: membership-figure
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: Figure 3A, all 35 named rows
  summary: The figure independently supports the MF360 genus distinction and preserves
    the explicit E. coli control row. Broad order/genus aggregates are not a 35-stock
    census.
  support: supports
  accessed_at: '2026-10-22T03:49:33.446370Z'
  snapshot_sha256: b9fddd69f3146423b5c6bfa2626dcaac6236d773d59db7a8c19a102a64923355
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: SI Appendix, Materials and Methods, Preparation of bacterial synthetic
    communities (SynComs), second paragraph; printed p2 / physical PDF p12
  summary: Assembly preculture uses 4 mL 2xYT (16 g/L tryptone, 10 g/L yeast extract,
    5 g/L NaCl) in test tubes, 28°C, 250 rpm and 1–2 days; two washes in 10 mM MgCl2
    precede dosing each strain at 10^5 CFU/mL into a 500 mL medium preparation. The
    source assumes OD1 corresponds to 10^9 CFU/mL.
  support: supports
  accessed_at: '2026-10-22T03:49:33.446912Z'
  snapshot_sha256: f8972d0247d5d2fc7690771c5d5b0569b12cc6107dcd852d444fbeb806c83107
  quote: single colony
- evidence_id: plant-protocol
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: SI Appendix, Preparation of plants for bacteria and flg22 treatments, sole
    paragraph, p2; Treatment of plants with flg22 in the presence of SynComs, two
    paragraphs, pp2–3
  summary: Johnson medium has 5 g/L sucrose, 1% agar and pH5.6–5.7. Seven-day germination
    uses 16 h light/8 h dark at 21°C day/18°C night; chronic SynCom/flg22 treatment
    uses 9 h light/15 h dark at the same temperatures and harvests at 1 and 12 days.
    Live, heat-killed and no-bacteria controls are distinct.
  support: supports
  accessed_at: '2026-10-22T03:49:33.452104Z'
  snapshot_sha256: f8972d0247d5d2fc7690771c5d5b0569b12cc6107dcd852d444fbeb806c83107
- evidence_id: other-protocols
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: SI Appendix, DNA extraction for 16S sequencing, first paragraph, p7; Evaluation
    of the root acute response to flg22, sole paragraph, p10; Evaluation of the growth
    of commensals in the presence of SynComs, pp12–13; Suppression of the flg22 response
    by D. japonica MF79 cell-free supernatant, p16; Non-suppressor MF370 growth with
    MF79 10 kDa suppressive fraction, pp16–17; Figures S6–S10
  summary: Half-MS 16S culture, acute MS/GUS assays, smaller-SynCom challenge and
    MF79 filtrate production have separate media, inocula, doses and exposure schedules.
    Neither a generic TSB recipe nor one half-MS/light regime describes them all.
  support: supports
  accessed_at: '2026-10-22T03:49:33.457349Z'
  snapshot_sha256: f8972d0247d5d2fc7690771c5d5b0569b12cc6107dcd852d444fbeb806c83107
- evidence_id: counts
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: Results, Dissecting the Immunomodulatory Activity of Commensals (s3), whole
    section and Figures 2–3
  summary: The source distinguishes 24/35 partial or complete chronic-transcription
    suppressors and 11 without that effect from 10 robust cross-assay suppressors
    and 23/35 with activity in at least one assay. These statements cannot be collapsed
    into the current 10+13+11 partition.
  support: supports
  accessed_at: '2026-10-22T03:49:33.462436Z'
  snapshot_sha256: 691a281e7363ab2d32185e6a4c2bc4c0d1beda23fa26bfec116cbb40fa79bd32
- evidence_id: background
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: Abstract; main introductory MAMP context before Results; Discussion (s6),
    paragraphs 1–4; SI assay Methods
  summary: Chitin and peptidoglycan are background MAMP examples, not demonstrated
    focal suppression endpoints. Immune modulation and colonization facilitation do
    not establish syntrophic metabolism or DH5alpha metabolite utilization. Trace-medium
    salts do not establish environmental metal or REE measurements.
  support: supports
  accessed_at: '2026-10-22T03:49:33.462977Z'
  snapshot_sha256: 691a281e7363ab2d32185e6a4c2bc4c0d1beda23fa26bfec116cbb40fa79bd32
- evidence_id: suppression
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: Abstract; Results, A Community of Root Commensals Suppresses MTI (s2),
    paragraphs 2–4; Figure 1B–H
  summary: Live established SynCom35 suppresses chronic flg22 transcriptional and
    growth responses, with day-1/day-12 and heat-killed/no-bacteria controls. MF79
    is a studied contributor, not the sole community cause.
  support: supports
  accessed_at: '2026-10-22T03:49:33.463110Z'
  snapshot_sha256: 691a281e7363ab2d32185e6a4c2bc4c0d1beda23fa26bfec116cbb40fa79bd32
- evidence_id: wrky
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: Results, A Community of Root Commensals Suppresses MTI (s2), paragraph
    3 and Figure 1; Discussion (s6), paragraph 2; SI Appendix Figure S2
  summary: Community-associated immune-transcript changes include WRKY-associated
    responses. This readout does not demonstrate WRKY mediation of every colonization
    phenotype; the broad current Abstract excerpt remains PARTIAL for this node.
  support: supports
  accessed_at: '2026-10-22T03:49:33.463218Z'
  snapshot_sha256: 691a281e7363ab2d32185e6a4c2bc4c0d1beda23fa26bfec116cbb40fa79bd32
- evidence_id: secretion
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: Results, Immunomodulatory Strategies in Commensals (s5), paragraphs 1–2;
    Figure 5A–D; SI Appendix mutant and cell-free-supernatant Methods, pp13–16, Figure
    S10
  summary: MF79 gspD/gspE perturbations and extracellular fractions support T2SS-dependent
    modulation, whereas the tested T3SS mutants retain suppression. The responsible
    secreted molecular identity and a universal mechanism across all suppressors remain
    unresolved.
  support: supports
  accessed_at: '2026-10-22T03:49:33.463320Z'
  snapshot_sha256: 691a281e7363ab2d32185e6a4c2bc4c0d1beda23fa26bfec116cbb40fa79bd32
- evidence_id: facilitation
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: Significance; Results, MTI can Control Colonization by Commensals (s4),
    paragraph 2 and Figure 4A–C; Immunomodulatory Strategies in Commensals (s5), paragraph
    2 and Figure 5E; Discussion (s6), paragraph 3
  summary: Defined suppressor precolonization and MF79 fractions conditionally improve
    tested nonsuppressor colonization. The mutant-fraction comparison supports a specific
    directed component; it does not establish reciprocal nutrient exchange or community-wide
    necessity.
  support: supports
  accessed_at: '2026-10-22T03:49:33.463422Z'
  snapshot_sha256: 691a281e7363ab2d32185e6a4c2bc4c0d1beda23fa26bfec116cbb40fa79bd32
- evidence_id: declared-resources
  kind: primary_source
  reference: PMID:33879573; DOI:10.1073/pnas.2100678118
  locator: Data Availability (s8), sole paragraph; SI Appendix, Data and code availability,
    p17
  summary: The source declares GEO GSE156426, BioProject PRJNA657936 and the MAE analysis
    repository. The SI separately describes seven XLSX datasets, which were not recovered
    here.
  support: supports
  accessed_at: '2026-10-22T03:49:33.463522Z'
  snapshot_sha256: 691a281e7363ab2d32185e6a4c2bc4c0d1beda23fa26bfec116cbb40fa79bd32
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000022/ontology-authority.json
  locator: 20 ID-label definitions/ranks across 29 placements
  summary: All current labels match their identifiers. Label validity does not prove
    membership or source-specific roles.
  support: supports
  accessed_at: '2026-10-22T03:49:33.463630Z'
  snapshot_sha256: 8284d2ebf1661d8f41263fbbc30d1f4e50faefa2946b7b5cff1ebf69f9764f64
- evidence_id: schema
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000022/child-schema-semantics.json
  locator: Literal membership, role, interaction and cultivation definitions
  summary: Microbial taxonomy excludes its host. SYNTROPHIC_PARTNER denotes syntrophic
    metabolism and CROSS_FEEDER denotes use of another taxon’s metabolites; neither
    follows from immune facilitation alone.
  support: supports
  accessed_at: '2026-10-22T03:49:33.463886Z'
  snapshot_sha256: 2200df9de761f2d7de6da303079aa2fef25a2cd6715d9ba4b4c7ec48299662f2
- evidence_id: membership-authority
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000022/child-source-membership-candidate.json
  locator: Exact source-name candidate and rank
  summary: Mycobacterium NCBITaxon:1763 is a genus candidate for the source label.
    This is not an MF360 species or genome assignment.
  support: supports
  accessed_at: '2026-10-22T03:49:33.464064Z'
  snapshot_sha256: 0bf7664f29362b67fa06100ffd9a5fd3a59dc3cdd58965c97e75b222a68ac40d
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000022/child-gtdb-crosswalk.json
  locator: Seven current bacterial mappings, routes and snapshot provenance
  summary: Encoded mapping cores and reference-genome counts reproduce. Filesystem
    mtime does not establish the claimed release or build date; correct source membership
    before transferring classifications.
  support: supports
  accessed_at: '2026-10-22T03:49:33.464214Z'
  snapshot_sha256: c134c21150d3c63ffdd5262bbcc4ae7f5fec804a102a00888cb51d69306a4725
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-14/000022/ontology-semantic-notes.json
  locator: Final membership, roles, graph and cultivation reconciliation
  summary: Retain the four qualified nodes and two arrows. Repair membership, non-graph
    assertions and stage-specific procedures without inventing replacement roles or
    strain genomes.
  support: supports
  accessed_at: '2026-10-22T03:49:33.464372Z'
  snapshot_sha256: c3a99884621c3f05fa8677ee36672b8bfa07b86fa68ec8d9f7fd57f9c7f78d5c
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/dataset-verification.json
  locator: Source-declared GEO series, 72 run identities and bounded code inventory
  summary: GSE156426 comprises three subseries with 784 sample identifiers in their
    union; PRJNA657936 is the distinct 16S colonization project. The MAE tree has
    159 entries. No raw matrices, sequence reanalysis or 784 independent-culture inference.
  support: supports
  accessed_at: '2026-10-22T03:49:33.464520Z'
  snapshot_sha256: e7a430e66261142526ebdb3222e403d29128fe85aff623e9e79ae82c4dc38cae
  search_scope: Source-declared GEO426 and its three subseries, the exact PRJNA657936
    run metadata and complete MAE tree; no broad deposit-absence assertion or raw
    download.
- evidence_id: resource-links
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/external-resource-verification.json
  locator: Five encoded URLs and exact current record/chemical identities
  summary: All five old URLs return404. Both current CultureMech identifiers resolve;
    the imported MS entry depends on CommunityMech records and is circular as study-method
    evidence. Retired numeric MIM identifiers have no match in the complete current
    index; exact chemical identity does not prove identifier continuity.
  support: supports
  accessed_at: '2026-10-22T03:49:33.464743Z'
  snapshot_sha256: 5072f0bd1998a9dbeef36ec64d3fbedf3fe0a857feef498977e8929eeb8f5447
  search_scope: Five encoded routes, current exact CultureMech records and complete
    2953-entry MIM identifier index; no global archive-absence claim.
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/snippet-audit.json
  locator: All 21 canonical placements and both whole matching paragraphs
  summary: 'All 21 excerpts strictly match fresh source and selected cache: 16 DOI
    Significance and five PMID Abstract. Matching does not establish entailment of
    the attached role, medium or ligand claim.'
  support: supports
  accessed_at: '2026-10-22T03:49:33.464902Z'
  snapshot_sha256: 4351280d84327d4291e875b3ab15640ec4650469cf1b63844ab87749c2f9bc94
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-14/000022/provenance-audit.json
  locator: Sole history, batch29 focal row/adversarial, exact cohort and current issue
    context
  summary: Earlier graph scope repairs remain valid. Current source evidence is reconciled
    with the prior review; nine issue/PR bodies and eleven comments are support-reviewer
    scope, not a claim that all reviewers read every issue.
  support: supports
  accessed_at: '2026-10-22T03:49:33.465061Z'
  snapshot_sha256: 5ae4c778d24f317d1907be6876975676547652d72cc2f460047764e4da68e65c
- evidence_id: inspection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/inspect.json
  locator: 32 immutable inputs from ignored-inclusive discovery
  summary: Ten focal contexts, 21 applicable authorities and the maintained target
    were inspected before assessment.
  support: supports
  accessed_at: '2026-10-22T03:49:33.465219Z'
  snapshot_sha256: 534952a0980e90ba999cf24444aecd261f7db58f22a50b2dae65ef147b5c8261
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/lead-source-assets.json
  locator: Fresh article, five figures, complete author-hosted SI and failed linked
    XLSX routes
  summary: Ordinary public fallback recovered the complete article and SI Methods/figures.
    Seven separate spreadsheet datasets remain unavailable and unread; failed routes
    are preserved.
  support: supports
  accessed_at: '2026-10-22T03:49:33.465257Z'
  snapshot_sha256: f75fe7c1e6bad78e01ec7384261a7013b58eb8a9feaff41f496689b3579f64de
- evidence_id: lead-read
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/lead-primary-read-scope.json
  locator: Actual whole main/SI and image read scope
  summary: Lead read the whole main and all SI text, all five main figures and all
    ten SI figures. No raw matrices or modern 35-stock reconstruction was performed.
  support: supports
  accessed_at: '2026-10-22T03:49:33.465408Z'
  snapshot_sha256: f3e9caf80451cff0cbfcc80fe09b62de18e36369815699846a49f83a6827d8c0
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/source-locator-verification.json
  locator: Direct headings, paragraph counts and PDF page checks
  summary: The named HTML sections and SI Method headings/pages were verified. The
    sole quotation is in the second SynCom preparation paragraph, physical PDF page12.
  support: supports
  accessed_at: '2026-10-22T03:49:33.465552Z'
  snapshot_sha256: bef92417c610d889528e3126c60c55a41d9150efaf9a5d139a9851d7abf06d03
- evidence_id: source-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/source-audit.json
  locator: Final lead scientific findings
  summary: Three major findings concern member placement, cultivation and non-graph
    claim scope. Two minor findings concern mapping provenance and resource traceability.
  support: supports
  accessed_at: '2026-10-22T03:49:33.465679Z'
  snapshot_sha256: 07572f073af977f16961f93ab768692440e0ae7cc74dc9be7266599770cb5c7e
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/root-independent-source-audit.json
  locator: Independent source judgment and explicit read scope
  summary: Root independently agrees the five findings, graph retention and completed
    current-claim review with the spreadsheet boundary.
  support: supports
  accessed_at: '2026-10-22T03:49:33.465710Z'
  snapshot_sha256: ecf0c8d8ecc873b89a4dd61335b9073736ffa2f0ddd0df4c2ab375ed535fa34e
- evidence_id: root-graph
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/root-node-edge-audit.json
  locator: Independent node/arrow selectors and hashes
  summary: Four nodes and two actual downstream descriptions retain their source-
    and treatment-specific interpretation.
  support: supports
  accessed_at: '2026-10-22T03:49:33.465850Z'
  snapshot_sha256: bb08b0a22a9c83e5b8aaa4d3574ad9aab1e0891af66118d8617ee9c8e6b284c6
- evidence_id: metrics
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/support-final-audit.json
  locator: Final support, exact rubric and network diagnostic
  summary: Completeness85; quality100−30−4+10=76. Five DISCONNECTED warnings prevent
    the COMPLETE bonus and do not justify fabricated interactions.
  support: supports
  accessed_at: '2026-10-22T03:49:33.466046Z'
  snapshot_sha256: 1944cbe44a7e62c2c99b7e44e79d26d8ced15639254580489e694ab3574b71a9
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/support-frozen-manifest.json
  locator: Frozen supporting files and pins
  summary: Root, lead, child, source, resource and prior evidence were reconciled
    before rendering.
  support: supports
  accessed_at: '2026-10-22T03:49:33.466084Z'
  snapshot_sha256: 97354a0223b09daa51f056915d5406be4aa1793592724a62d4a1a4e77eda5e41
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/auxiliary-frozen-manifest.json
  locator: Frozen ontology/native artifacts
  summary: All 32 official inputs remain unchanged and eight focused native checks
    pass.
  support: supports
  accessed_at: '2026-10-22T03:49:33.466238Z'
  snapshot_sha256: 4710a3a3703745982a00c750ae68212eec405f41dc631b6a1c0a98a3076cab82
- evidence_id: final-native
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/final-validator-summary.json
  locator: Eight actual command/stdout/stderr outcomes
  summary: All focused commands return0; source entailment is assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:49:33.466367Z'
  snapshot_sha256: 15df235de2d5e35aab786e5a3d3ee7819962875a50fbea03efb75924dfdd3f73
- evidence_id: corpus-context
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/child-current-corpus-context.json
  locator: Actual batch14 corpus baseline
  summary: Both contextual corpus commands returned1 with 44 warnings across 16/477
    records and zero errors.
  support: supports
  accessed_at: '2026-10-22T03:49:33.466517Z'
  snapshot_sha256: 15fbf145ab971310b7e392b703e91dad7b0f4b03dcf5978538f9314062812b64
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/adapter-check.json
  locator: Optional adapter availability
  summary: Unavailable in the owned runtime; no adapter from another checkout was
    executed.
  support: supports
  accessed_at: '2026-10-22T03:49:33.466760Z'
  snapshot_sha256: 173981d12e06bf0c0e63005bc02d699ada65c5f1f3630c1d78104b20b5377662
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/validate.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:49:33.467575Z'
  snapshot_sha256: 54d95bffd3a620e5da7867ab52838a45eb5e0d3cc868594b16d91c6125fbef58
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/validate-strict.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:49:33.467767Z'
  snapshot_sha256: 68af09a60e19445cfc1f83c30b45801477c5a12e4281ab829e55c0c510540728
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/validate-terms.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:49:33.467956Z'
  snapshot_sha256: 8a3b25ac0d8cf6caaf1e25637d71011e2a4123743a59a258aa9e81c53647c184
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/validate-references-explained.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:49:33.468144Z'
  snapshot_sha256: b6f1be98563e786acdeac36029bfc5f806c23d2fee1b7b43c8d15fc230398398
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/validate-gtdb.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:49:33.468321Z'
  snapshot_sha256: ee1adc9295a3bed1accd0d13a7670ed16e1ccc6e7b6bee4c6be971d820d20552
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/validate-gtdb-domain.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:49:33.468481Z'
  snapshot_sha256: 24abcc4b57b44b3acd64f03570af57079deedcf0eb783a14aed2b97be55cfa00
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/validate-history.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:49:33.468652Z'
  snapshot_sha256: ce427a7b678b9c88a65f42c8495eec1c93f4dd37cdb7774a0246bf403005a858
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/000022/normalize-cache-names-check.json
  locator: Actual current command/stdout/stderr
  summary: Native exit0; source entailment assessed separately.
  support: supports
  accessed_at: '2026-10-22T03:49:33.468821Z'
  snapshot_sha256: 9c4f686175bac5f5ee271fa5268ae16c4e99efac633fdc18ee5c9e02cebf1b2c
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/audit-network.json
  locator: Actual batch14 corpus baseline
  summary: Exit1,44warnings across16/477records and zero errors.
  support: supports
  accessed_at: '2026-10-22T03:49:33.469156Z'
  snapshot_sha256: 3110e0bb1dbe3ea63b81aea82871ac4adb2915c8fce1d15249422d0f5db266c6
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-14/check-network-quality.json
  locator: Actual batch14 corpus baseline
  summary: Exit1,44warnings across16/477records and zero errors.
  support: supports
  accessed_at: '2026-10-22T03:49:33.469330Z'
  snapshot_sha256: 18896ef4136601b37550cb5612abc06784abcbf982e4778cbf2b9c10368cb66a
assessments:
- assessment_id: identity
  area: identity
  topic: Host and source member identity
  outcome: concern
  summary: The host is misplaced as a microbial member and two genus placeholders
    need source reconciliation.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - membership
  - membership-figure
  - schema
  - membership-authority
  dimensions:
  - name: experimental_scope
    value: 32 root isolates, two soil isolates and one control
    definition: Designed bacterial assembly on an Arabidopsis host, with separate
      smaller SynCom and monoassociation assays.
    evidence_ids:
    - membership
  - name: strain_scope
    value: Source isolate labels, bounded current authority matches
    definition: A genus name or reference-genome mapping is not a verified modern
      experimental-stock assignment.
    evidence_ids:
    - membership
    - membership-authority
    - gtdb
  details: Retain the 35-member design and explicit DH5alpha control. Figure 3A labels
    MF360 Mycobacterium rather than Microbacterium; Stenotrophomonas is unsupported
    by that complete displayed roster. Keep Arabidopsis as an outside-community graph
    participant. Do not force all 35 stocks into species-level entries from the unread
    Dataset S1.
- assessment_id: cultivation
  area: evidence
  topic: Stage-specific culture and plant assays
  outcome: concern
  summary: The existing generic TSB/half-MS blocks conflate procedures contradicted
    by the recovered SI.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - cultivation
  - plant-protocol
  - other-protocols
  - resource-links
  details: Separate bacterial assembly, Johnson germination and chronic treatment,
    half-MS 16S sampling, acute MS/GUS, smaller-SynCom challenges and cell-free fractions.
    Plant-free, axenic and cell-free are distinct. Repair temperature, light, medium,
    shaking and dose by assay, not a global replacement.
- assessment_id: non-graph
  area: evidence
  topic: Roles, suppression counts and background ligands
  outcome: concern
  summary: Metabolic role tags and several non-graph explanations exceed the source
    context.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - counts
  - background
  - schema
  - semantics
  details: Keep assay-specific counts and the source’s 23-versus-24 distinction. Control
    membership is not cross-feeding, immune facilitation is not syntrophic metabolism,
    and background chitin/peptidoglycan statements are not direct suppression tests.
    No environmental metal/REE measurement is established by recipe salts.
- assessment_id: node-0
  area: graph
  topic: Root flg22 Immune Suppression
  outcome: supported
  summary: Retain community-level suppression and its participant subset; live established
    community, day12 versus day1 and killed/no-bacteria controls matter. The current
    SUPPORT/IN_VITRO Abstract evidence remains source-compatible without attributing
    the whole outcome solely to MF79.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - suppression
  - snippets
  - root-graph
  details: 'Exact selector ecological_interactions[0]; scope COMMUNITY_LEVEL; interaction_type
    untyped. Encoded taxa: {"source": null, "target": null, "participants": [{"preferred_term":
    "Arabidopsis thaliana", "term": {"id": "NCBITaxon:3702", "label": "Arabidopsis
    thaliana"}}, {"preferred_term": "Dyella japonica MF79", "term": {"id": "NCBITaxon:231455",
    "label": "Dyella japonica"}}]}. Canonical excerpt bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "2dc66193cd546504b3cd9bedafe661d0574273af20e4702739fb9bd4341ce325",
    "reference": "PMID:33879573", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 4351280d84327d4291e875b3ab15640ec4650469cf1b63844ab87749c2f9bc94.
    Source contexts and retained tiers are specified in the linked evidence and summary.'
- assessment_id: edge-0-0
  area: graph
  topic: Root flg22 Immune Suppression → Suppression-Associated Root Colonization
    Facilitation
  outcome: supported
  summary: Retain the qualified directed link and its conditional experimental scope.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - facilitation
  - root-graph
  details: 'Exact selector ecological_interactions[0].downstream[0]; source node Root
    flg22 Immune Suppression; target node Suppression-Associated Root Colonization
    Facilitation. Exact encoded description: Suppression can facilitate nonsuppressor
    root colonization under the tested conditions. MF79 wild-type retentate, unlike
    T2SS-mutant material, countered the flg22-associated reduction in Ochrobactrum
    MF370 colonization. This does not establish universal facilitation by every suppressor
    or reciprocal benefit.. Description SHA256 4f36927e5108e17b6e00bb05226918aeb7fb99d3f36d4b84a3d1ea88afa1b2ee.
    Figure 5E and Results s5 paragraph2: MF79 WT retentate, compared with secretion-mutant
    fractions, conditionally rescues the tested nonsuppressor under flg22. This is
    not reciprocal fitness or universal suppression-to-colonization causality.'
- assessment_id: node-1
  area: graph
  topic: Community-Associated WRKY Transcript Suppression
  outcome: supported
  summary: Retain community-associated WRKY transcription as a separate readout. The
    broad Abstract excerpt is correctly PARTIAL/IN_VITRO; full Results and SI Figure
    S2 supply detail without establishing downstream WRKY mediation.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - wrky
  - suppression
  - snippets
  - root-graph
  details: 'Exact selector ecological_interactions[1]; scope COMMUNITY_LEVEL; interaction_type
    untyped. Encoded taxa: {"source": null, "target": null, "participants": [{"preferred_term":
    "Arabidopsis thaliana", "term": {"id": "NCBITaxon:3702", "label": "Arabidopsis
    thaliana"}}, {"preferred_term": "Dyella japonica MF79", "term": {"id": "NCBITaxon:231455",
    "label": "Dyella japonica"}}]}. Canonical excerpt bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet",
    "sha256": "2dc66193cd546504b3cd9bedafe661d0574273af20e4702739fb9bd4341ce325",
    "reference": "PMID:33879573", "supports": "PARTIAL", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 4351280d84327d4291e875b3ab15640ec4650469cf1b63844ab87749c2f9bc94.
    Source contexts and retained tiers are specified in the linked evidence and summary.'
- assessment_id: node-2
  area: graph
  topic: MF79 Type II Secretion-Dependent Immune Modulation
  outcome: supported
  summary: Retain the MF79-to-host T2SS-dependent assay and SUPPORT/IN_VITRO evidence.
    T2SS perturbations and filtrates support this component; the effector remains
    unknown and the tested T3SS mutants differ.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - secretion
  - other-protocols
  - snippets
  - root-graph
  details: 'Exact selector ecological_interactions[2]; scope PAIRWISE; interaction_type
    untyped. Encoded taxa: {"source": {"preferred_term": "Dyella japonica MF79", "term":
    {"id": "NCBITaxon:231455", "label": "Dyella japonica"}}, "target": {"preferred_term":
    "Arabidopsis thaliana", "term": {"id": "NCBITaxon:3702", "label": "Arabidopsis
    thaliana"}}, "participants": []}. Canonical excerpt bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet",
    "sha256": "f167aa90b194d02705c8b957a2727c24d5640c33ca3ddd40a8ee4910f0aa1bcb",
    "reference": "PMID:33879573", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Snippet audit SHA256 4351280d84327d4291e875b3ab15640ec4650469cf1b63844ab87749c2f9bc94.
    Source contexts and retained tiers are specified in the linked evidence and summary.'
- assessment_id: edge-2-0
  area: graph
  topic: MF79 Type II Secretion-Dependent Immune Modulation → Root flg22 Immune Suppression
  outcome: supported
  summary: Retain the qualified directed link and its conditional experimental scope.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - secretion
  - root-graph
  details: 'Exact selector ecological_interactions[2].downstream[0]; source node MF79
    Type II Secretion-Dependent Immune Modulation; target node Root flg22 Immune Suppression.
    Exact encoded description: MF79 T2SS function enables its extracellular suppressive
    activity in the root reporter assay. This arrow applies to the MF79 component
    of the suppression node, not necessity of T2SS for the entire SynCom35 phenotype..
    Description SHA256 0dcd5a4c5673efaf6a5ca10804d748553f589e76006eb02de796591a361bebf4.
    Figure 5A–D and Results s5 paragraphs1–2: MF79 secretion perturbation establishes
    a contributing component, not T2SS necessity for all 35 members or every suppressor.'
- assessment_id: node-3
  area: graph
  topic: Suppression-Associated Root Colonization Facilitation
  outcome: supported
  summary: Retain COLONIZATION_FACILITATION for the tested smaller-SynCom and fraction
    contexts, with SUPPORT/IN_VITRO Significance evidence. Participating taxa are
    a subset, not an exhaustive census; no reciprocal nutrient exchange is inferred.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - facilitation
  - other-protocols
  - snippets
  - root-graph
  details: 'Exact selector ecological_interactions[3]; scope COMMUNITY_LEVEL; interaction_type
    COLONIZATION_FACILITATION. Encoded taxa: {"source": null, "target": null, "participants":
    [{"preferred_term": "Arabidopsis thaliana", "term": {"id": "NCBITaxon:3702", "label":
    "Arabidopsis thaliana"}}, {"preferred_term": "Dyella japonica MF79", "term": {"id":
    "NCBITaxon:231455", "label": "Dyella japonica"}}, {"preferred_term": "Pseudomonas
    species", "term": {"id": "NCBITaxon:286", "label": "Pseudomonas"}}]}. Canonical
    excerpt bindings: [{"selector": "ecological_interactions[3].evidence[0].snippet",
    "sha256": "1d068bea1ee160ac0852ac1d630d449eabb76ca4f5238d3d3d2d32726724234f",
    "reference": "doi:10.1073/pnas.2100678118", "supports": "SUPPORT", "evidence_source":
    "IN_VITRO"}]. Snippet audit SHA256 4351280d84327d4291e875b3ab15640ec4650469cf1b63844ab87749c2f9bc94.
    Source contexts and retained tiers are specified in the linked evidence and summary.'
- assessment_id: grounding
  area: grounding
  topic: Correct labels with bounded mapping provenance
  outcome: concern
  summary: Twenty ID-label pairs match, but seven mapping_source statements overstate
    release/build provenance.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - ontology
  - gtdb
  - semantics
  details: Preserve valid GO and chemical identities, source labels and rank routes.
    Resolve membership before carrying a mapping to a corrected genus. RHIZOSPHERE
    is source provenance/model context; the assays themselves are gnotobiotic plates
    or liquid, not soil. COMMON is ordinal rather than a numerical cutoff.
- assessment_id: resources
  area: provenance
  topic: Study outputs and imported medium links
  outcome: concern
  summary: Current resource identities are recoverable, but old routes and source-to-resource
    traceability need repair.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - declared-resources
  - resources
  - resource-links
  details: GEO host-transcriptome subseries, 16S colonization libraries and analysis
    code have separate scopes. Generic CultureMech identity does not establish the
    experimental recipe; the imported MS record is circular as primary support. No
    missing scientific dataset is inferred merely from unavailable spreadsheets.
- assessment_id: ownership
  area: ownership
  topic: Maintained YAML and prior curation
  outcome: supported
  summary: The focal YAML owns the proposed repairs; existing graph qualifications
    and prior provenance remain intact.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - inspection
  - provenance
  details: No source/cache/history, issue or Git mutation is part of this review.
- assessment_id: native
  area: schema
  topic: Native checks versus scientific support
  outcome: supported
  summary: Eight focused checks pass. Five target DISCONNECTED warnings and the separate
    corpus/adapter outcomes remain explicit.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - final-native
  - auxiliary
  - metrics
  - corpus-context
  - adapter
  details: The disconnected taxa are DH5alpha, Flavobacterium, Microbacterium, Stenotrophomonas
    and Xanthomonadales. Their presence in a diagnostic does not justify invented
    edges. The graph has four nodes, one typed node, two arrows and four evidence
    placements.
- assessment_id: metrics
  area: completeness
  topic: Literal completeness and quality
  outcome: supported
  summary: Completeness85 and quality76, calculated independently of source confidence.
  target_ids:
  - CommunityMech:000022
  evidence_ids:
  - metrics
  metrics:
  - name: completeness
    value: 85
    unit: points
    minimum: 0
    maximum: 100
    definition: 50 required fields/roles +5 environment +10 at least three factors
      +10 at least three nodes +10 growth media; no external-resource, dataset or
      node-metabolite award.
  - name: validation_quality
    value: 76
    unit: points
    minimum: 0
    maximum: 100
    definition: 100 -3 major*10 -2 minor*2 +10 evidence bonus (4/4=1 mean) +0 network
      bonus =76. Five DISCONNECTED warnings prevent COMPLETE bonus.
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
- finding_id: member-identity
  issue_key: cm-000022-member-identity
  category: identity
  severity: major
  native_severity: P2
  normalization_reason: Material source or schema mismatch changes biological interpretation
    or experimental reproducibility.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Reconcile the host and unsupported member placeholders
  description: The taxonomy slot includes the plant host, although its schema excludes
    hosts. Figure 3A identifies MF360 as Mycobacterium rather than the encoded Microbacterium,
    and its complete 35-row panel does not support Stenotrophomonas. Reconcile these
    placements while retaining the explicitly included DH5alpha control; do not invent
    a complete modern stock inventory from unread Dataset S1.
  target_ids:
  - CommunityMech:000022
  field_paths:
  - taxonomy[0]
  - taxonomy[5]
  - taxonomy[6]
  evidence_ids:
  - membership
  - membership-figure
  - schema
  - membership-authority
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  ownership_note: Repair the focal maintained YAML in a separate curation step; preserve
    source and historical bytes.
- finding_id: cultivation
  issue_key: cm-000022-cultivation
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material source or schema mismatch changes biological interpretation
    or experimental reproducibility.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Replace conflated culture conditions with the actual assay stages
  description: The generic TSB and half-MS recipes, light/temperature/shaking values
    and inoculum statements conflate stages and conflict with the recovered SI. Primary
    assembly uses 2xYT and CFU-based dosing; Johnson plant culture, chronic exposure,
    half-MS 16S, acute MS/GUS and LB/fraction assays are separate. Water1g/L is not
    a valid solvent-volume recipe, and axenic plants are not plant-free experiments.
  target_ids:
  - CommunityMech:000022
  field_paths:
  - growth_media
  - environmental_factors[0]
  - environmental_factors[1]
  - environmental_factors[2]
  - environmental_factors[3]
  evidence_ids:
  - cultivation
  - plant-protocol
  - other-protocols
  - resource-links
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  ownership_note: Repair the focal maintained YAML in a separate curation step; preserve
    source and historical bytes.
- finding_id: claim-scope
  issue_key: cm-000022-claim-scope
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: Material source or schema mismatch changes biological interpretation
    or experimental reproducibility.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Constrain non-graph roles, counts and ligand explanations
  description: The six SYNTROPHIC_PARTNER tags and DH5alpha CROSS_FEEDER tag lack
    metabolic evidence. The 10+13+11 partition mixes different suppression endpoints;
    source chronic24/35 and cross-assay23/35 remain distinct. Background chitin/peptidoglycan
    text does not support the attached experimental suppression explanations, and
    recipe salts do not support the generic metal/REE measurement claim.
  target_ids:
  - CommunityMech:000022
  field_paths:
  - description
  - taxonomy[1].functional_role
  - taxonomy[2].functional_role
  - taxonomy[3].functional_role
  - taxonomy[4].functional_role
  - taxonomy[5].functional_role
  - taxonomy[6].functional_role
  - taxonomy[7].functional_role
  - environmental_factors[5]
  - related_ingredients[0].evidence[0]
  - related_ingredients[1].evidence[0]
  - metal_notes
  evidence_ids:
  - counts
  - background
  - schema
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  ownership_note: Repair the focal maintained YAML in a separate curation step; preserve
    source and historical bytes.
- finding_id: gtdb-provenance
  issue_key: cm-000022-gtdb-provenance
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Recoverable provenance and traceability gap without invalidating
    supported source outcomes.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Use verifiable GTDB snapshot provenance
  description: Seven existing mapping cores reproduce against the current reference
    snapshot, but latest and built2026-07-25 are not established by its filesystem
    mtime. Preserve correct rank/name/ID routes and reference-genome scope, subject
    to resolving membership first.
  target_ids:
  - CommunityMech:000022
  field_paths:
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  - taxonomy[2].taxon_term.gtdb_classification.mapping_source
  - taxonomy[3].taxon_term.gtdb_classification.mapping_source
  - taxonomy[4].taxon_term.gtdb_classification.mapping_source
  - taxonomy[5].taxon_term.gtdb_classification.mapping_source
  - taxonomy[6].taxon_term.gtdb_classification.mapping_source
  - taxonomy[7].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - gtdb
  - ontology
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  ownership_note: Repair the focal maintained YAML in a separate curation step; preserve
    source and historical bytes.
- finding_id: resources
  issue_key: cm-000022-resources
  category: provenance
  severity: minor
  native_severity: P3
  normalization_reason: Recoverable provenance and traceability gap without invalidating
    supported source outcomes.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Repair resource routes and add scoped study outputs
  description: Five encoded resource URLs are obsolete. Both CultureMech identities
    resolve at current locations, but the MS import is circular as primary study evidence
    and current chemical records do not prove legacy MIM numeric identity. The article
    also declares verified GEO, 16S and code outputs whose distinct scopes can be
    recorded.
  target_ids:
  - CommunityMech:000022
  field_paths:
  - growth_media[0].culturemech_url
  - growth_media[1].culturemech_url
  - growth_media[0].composition[0].media_ingredient_mech_url
  - growth_media[1].composition[1].media_ingredient_mech_url
  - growth_media[1].composition[2].media_ingredient_mech_url
  evidence_ids:
  - declared-resources
  - resources
  - resource-links
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  ownership_note: Repair the focal maintained YAML in a separate curation step; preserve
    source and historical bytes.
actions:
- action_id: repair-membership
  description: Reconcile membership against the source and literal schema.
  finding_ids:
  - member-identity
  target_ids:
  - CommunityMech:000022
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  acceptance_checks:
  - Remove Arabidopsis from microbial taxonomy while retaining its valid host identity
    and graph participation. Retain the source-supported DH5alpha control. Distinguish
    order/genus aggregates from individual stock entries; do not automatically expand
    the record to 35 species.
  - Correct the MF360 Microbacterium placeholder using the source Mycobacterium label
    and verified genus NCBITaxon:1763; preserve MF360 as a source isolate label without
    inventing a species/genome assignment. Reconcile Stenotrophomonas with a documented
    source alias/roster or remove the unsupported placeholder. Dataset S1 remains
    unread, so do not certify an exhaustive modern stock crosswalk.
  - Recheck every affected participant and mapping after membership repair. The existing
    host and supported MF79/Pseudomonas participant descriptors remain valid; no automatic
    graph deletion follows.
- action_id: repair-cultivation
  description: Encode distinct source protocols with claim-local evidence.
  finding_ids:
  - cultivation
  target_ids:
  - CommunityMech:000022
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  acceptance_checks:
  - 'SI p2 SynCom assembly: 4mL 2xYT in test tubes, tryptone16g/L, yeast extract10g/L,
    NaCl5g/L; 28°C,250rpm,1–2days. Wash twice in10mM MgCl2. Dose each strain at10^5CFU/mL
    using the stated OD1≈10^9CFU/mL assumption. The500mL is a medium preparation batch,
    not a plant vessel capacity. Do not retain unsupported generic TSB pH7.3,180rpm,24h
    or OD0.001.'
  - 'SI p2 Johnson recipe per litre: sucrose5g, KH2PO4 85mg, KNO3 0.6g, Ca(NO3)2·4H2O
    0.9g, MgSO4·7H2O 0.2g, KCl3.8mg, H3BO3 1.5mg, MnSO4·H2O0.8mg, ZnSO4·7H2O0.6mg,
    CuSO4·5H2O0.1mg, H2MoO4 16.1µg, FeSO4·7H2O1.1mg, myo-inositol0.1g and MES0.5g;
    pH5.6–5.7 and1%agar. Preserve source units/hydration and solvent volume rather
    than water1g/L. No unsupported new chemical identifier is required.'
  - Separate seven-day germination16h light/8h dark at21°C day/18°C night from chronic
    treatment9h light/15h dark at21/18°C, with1µM flg22 and day1/day12 harvests. Retain
    live,100°C2h heat-killed and no-bacteria arms. Do not treat axenic host plants
    as plant-free, or invent100µmol light intensity.
  - SI p7 half-strength MS with vitamins,pH5.7,1%agar belongs to the16S procedure.
    SI p10 acute assay has1mL MS with vitamins (strength unspecified),MES0.5g/L,sucrose0.5%,pH5.7
    in12-well plates; seven-day seedlings receive single strains atOD0.002 forabout14h,
    then100nM flg22 for5h. Do not transfer the record’s1%sucrose/0.8%agar/22°C into
    all stages.
  - 'Keep smaller-SynCom and LB challenge procedures separate: SI pp12–13 uses3mL
    LB,28°C,250rpm,24h, defined low-OD precolonization/challenge and a48h postchallenge
    endpoint. SI p16 MF79 filtrates use1xMS,5g/L sucrose,0.1%casamino acids,OD0.02,21°C,250rpm,18h;
    the MF370 assay exchanges fractions into sucrose-free half-MS. Preserve each source
    dose/time and controls without implying a single SynCom35 recipe.'
  - Replace generic evidence with the exact relevant SI Method heading/paragraph and
    stage. Do not use a generic CultureMech import as independent proof of the paper’s
    protocol.
- action_id: repair-claim-scope
  description: Qualify unsupported non-graph claims while retaining supported ecological
    effects.
  finding_ids:
  - claim-scope
  target_ids:
  - CommunityMech:000022
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  acceptance_checks:
  - Remove or qualify optional SYNTROPHIC_PARTNER and DH5alpha CROSS_FEEDER tags unless
    claim-local metabolic evidence is supplied. Do not replace them with invented
    mandatory roles. Preserve immune modulation, secretion perturbation and colonization
    facilitation as supported phenotypes.
  - Describe chronic transcription24/35 partial/full suppressors and11 without that
    effect separately from10 robust cross-assay suppressors and23/35 with any tested
    activity. Retain the source’s endpoint-sensitive23-versus24 discrepancy; do not
    silently force a single partition summing to35.
  - Keep chitin/peptidoglycan only as correctly labelled background MAMP examples,
    or supply direct ligand-specific evidence before asserting suppression. Correct
    the current SUPPORT/IN_VIVO explanations that turn background into a focal result.
    Remove the unsupported generic metal/REE measurement assertion; medium salts and
    staining reagents are not environmental measurements.
  - Preserve all four qualified nodes and both directed links, their exact source
    contexts and current evidence tiers. Do not infer reciprocity, universal MF79/T2SS
    necessity, an identified secreted effector or WRKY mediation of colonization.
- action_id: repair-gtdb
  description: Use honest snapshot and mapping-route provenance.
  finding_ids:
  - gtdb-provenance
  target_ids:
  - CommunityMech:000022
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  acceptance_checks:
  - Replace the seven latest/build-date assertions with actual snapshot SHA256761d5537a7edb4b0133e88e7bbc85570cf3cb6f2555b9f9ce6cca3e1056a0ddd
    and unknown release when no release evidence exists. Filesystem mtime is not a
    release/build date.
  - 'Preserve supported cores and routes: Dyella231455 name fallback, two reference
    genomes; Lysobacterales135614 rank aggregation7047/7047; Pseudomonas17956/25706
    with11 total destinations; Flavobacterium859/860 with2; Stenotrophomonas398/404
    with2; Microbacterium591/591 with1; DH5alpha668369 exact ID with4/4. These are
    reference supports, not community abundances or study-stock classifications. Recompute
    affected mappings after membership corrections, rather than transferring Microbacterium
    grounding to Mycobacterium.'
  - Keep source names, current NCBI labels and the name-comparison meaning of is_reclassified
    separate. Preserve the host’s valid eukaryotic GTDB exclusion wherever its descriptor
    is retained.
- action_id: repair-resources
  description: Restore resolvable links and add scoped study resources.
  finding_ids:
  - resources
  target_ids:
  - CommunityMech:000022
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  acceptance_checks:
  - Use verified current routes for CultureMech008226 and015433 only where a generic
    recipe link remains useful after protocol repair. State that the MS record imports
    CommunityMech000003/000022 and is not independent source support. Do not preserve
    obsolete MIM URLs merely because water,sucrose and agar have correct chemical
    identities; currentCHEBI15377/17992/2509 records are candidates, not proof of
    legacy numeric-ID continuity.
  - Add source-declared GEO GSE156426 with subseries GSE156424(MAE666 sample IDs),GSE156425(RST100)
    andGSE157027(SSC18). The784-ID union is not784 independent biological cultures.
    Retain study/assay scope and do not promote unread sample or expression matrices
    to verified results.
  - Add PRJNA657936/SRP278111 as the separate16S colonization project,72 paired MiSeq
    PCR libraries; preserve registry strategyOTHER/sourceMETAGENOMIC versus source
    amplicon description. Do not call these35 isolate genomes or host RNA-seq.
  - Add https://github.com/ncolaian/MAE at inspected commit6dc674a1e23ed0b2128544d86d808472896f1f12
    as analysis code. The159-entry tree and666-row design labels do not provide genus-resolved
    Dataset S1. No raw download, code execution or contact is needed for this repair.
- action_id: validate-future-curation
  description: Validate any separately authorized repair.
  finding_ids:
  - member-identity
  - cultivation
  - claim-scope
  - gtdb-provenance
  - resources
  target_ids:
  - CommunityMech:000022
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Dangl_SynComm_35.yaml
    role: canonical_record
  acceptance_checks:
  - Recheck literal schema, ontology labels, exact references, GTDB/domain, history
    and graph context after source-backed edits. Five disconnected warnings do not
    authorize invented interactions or forced topology changes.
  - Run just gen-html and just check-docs-current after authorized curation. Append
    appropriate provenance and preserve original cache/history/source bytes. This
    review changes no canonical record, generated page, issue or Git state.
limitations:
- The seven separate XLSX datasets were not recovered through the bounded public routes
  and remain unread. Complete main/SI Methods and figures resolve the current encoded
  claims; this is not a verified35-stock genome inventory or raw expression/sequence
  reanalysis.
- Source chronic24/35 and cross-assay23/35 suppression counts retain their named endpoint
  scopes. SI transcription-analysis day/hour and715/716-gene inconsistencies are not
  silently harmonized. Distinct100nM and1µM flg22 experiments and germination/treatment
  light regimes remain separate.
- GEO784 sample IDs and72 16S libraries are registry counts, not independently inspected
  biological samples or a replicate design reconstruction. Code and design inventory
  were inspected without executing analysis or reading large matrices.
- Correct ontology labels and reference-genome mappings do not establish membership,
  individual strain identity or metabolic roles. Five DISCONNECTED warnings are diagnostic
  context; they do not imply five experimentally missing interactions.
notes:
- All32 official input hashes remain unchanged. Canonical excerpt selectors/hashes
  and the exact two downstream descriptions are bound in the graph assessments.
- 'Sole source quotation: two words from SI preparation paragraph2, with PDF line-break
  whitespace normalized. Candidate validation and root save/post-save checks occur
  afterward; no future result is asserted.'
tags:
- record-review
- rhizosphere
- host-immunity
- batch-14
```
