# EcoFAB ring trial SynCom17 record review

- Review: 20261022T094134Z-ecofab-ring-trial-record-review-v2
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-22T09:22:45.700136Z
- Finished UTC: 2026-10-22T09:41:34.672711Z
- Reviewer: codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two major findings concern causal/evidence scope and pooled study conditions; two minor findings concern taxon/map provenance and genome identifiers. Retain five nodes and four qualified arrows. Eight required checks pass; completeness45 and quality100 (raw103).

## Scope And Provenance

Whole record, both cited scientific texts, principal main/SI figures, relevant tables, protocol and bounded resource/authority checks.

Selection: Sole released CommunityMech:000025 in owned batch16.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base cb7a782c8ba80299dca8761ad0a2c90bccd8a117.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000025 | kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml | maintained | EcoFAB 2.0 Root Microbiome Ring Trial SynCom17 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| validate | passed | True | CommunityMech:000025 | Actual native exit 0. |
| validate-strict | passed | True | CommunityMech:000025 | Actual native exit 0. |
| validate-terms | passed | True | CommunityMech:000025 | Actual native exit 0. |
| validate-references-explained | passed | True | CommunityMech:000025 | Actual native exit 0. |
| validate-gtdb | passed | True | CommunityMech:000025 | Actual native exit 0. |
| validate-gtdb-domain | passed | True | CommunityMech:000025 | Actual native exit 0. |
| validate-history | passed | True | CommunityMech:000025 | Actual native exit 0. |
| normalize-cache-names-check | passed | True | CommunityMech:000025 | Actual native exit 0. |
| audit-network corpus context | failed | False | CommunityMech:000025 | Actual corpus exit 1; 44 warnings and no errors across 16 of 477 records. |
| check-network-quality corpus context | failed | False | CommunityMech:000025 | Actual corpus exit 1; 44 warnings and no errors across 16 of 477 records. |
| Source-specific structured adapter | unavailable | False | CommunityMech:000025 | Optional runner unavailable in owned runtime. |

## Scientific And Domain Assessments

### Defined isolates and host system

identity: supported. Targets: CommunityMech:000025.

The record identifies the intended ring trial.

Seventeen named stocks form the microbial roster; Brachypodium distachyon is the host. DSM200000SY is a collection, not a strain identifier. Retain synthetic origin, engineered state and rhizosphere category.

### Mechanism, optional roles and attribution

evidence: concern. Targets: CommunityMech:000025.

Non-graph claims exceed the experiments.

Relative dominance does not demonstrate competitive exclusion or absolute extinction. Bulk spent-medium profiles do not identify OAS925-specific amino-acid uptake. Plant effects belong to the whole SynCom17 treatment. Three PRIMARY_DEGRADER tags and Methylobacterium CROSS_FEEDER need member-local support; general membership or exudate associations do not suffice. Preserve positive genomic potential and measured phenotypes without assigning untested flux or trait necessity.

### SynCom17 EcoFAB Ring-Trial Perturbation

graph: supported. Targets: CommunityMech:000025.

Retain the qualified claim; align evidence tiers with assay context.

Exact selector ecological_interactions[0]. Participants: {"participating_taxa": [{"preferred_term": "Paraburkholderia sp. OAS925", "term": {"id": "NCBITaxon:1822464", "label": "Paraburkholderia"}}, {"preferred_term": "Rhodococcus sp. OAS809", "term": {"id": "NCBITaxon:1827", "label": "Rhodococcus &lt;high G+C Gram-positive bacteria&gt;"}}, {"preferred_term": "Mycobacterium sp. OAE908", "term": {"id": "NCBITaxon:1763", "label": "Mycobacterium"}}, {"preferred_term": "Methylobacterium sp. OAE515", "term": {"id": "NCBITaxon:407", "label": "Methylobacterium"}}, {"preferred_term": "Variovorax sp. OAS795", "term": {"id": "NCBITaxon:34072", "label": "Variovorax"}}, {"preferred_term": "Rhizobium sp. OAE497", "term": {"id": "NCBITaxon:379", "label": "Rhizobium"}}, {"preferred_term": "Bosea sp. OAE506", "term": {"id": "NCBITaxon:85413", "label": "Allobosea"}}, {"preferred_term": "Bradyrhizobium sp. OAE829", "term": {"id": "NCBITaxon:374", "label": "Bradyrhizobium"}}, {"preferred_term": "Lysobacter sp. OAE881", "term": {"id": "NCBITaxon:68", "label": "Lysobacter"}}, {"preferred_term": "Arthrobacter sp. OAP107", "term": {"id": "NCBITaxon:1667", "label": "Arthrobacter sp."}}, {"preferred_term": "Marmoricola sp. OAE513", "term": {"id": "NCBITaxon:86795", "label": "Marmoricola"}}, {"preferred_term": "Chitinophaga sp. OAE865", "term": {"id": "NCBITaxon:79328", "label": "Chitinophaga"}}, {"preferred_term": "Mucilaginibacter sp. OAE612", "term": {"id": "NCBITaxon:423349", "label": "Mucilaginibacter"}}, {"preferred_term": "Niastella sp. OAS944", "term": {"id": "NCBITaxon:354354", "label": "Niastella"}}, {"preferred_term": "Gottfriedia sp. OAE603", "term": {"id": "NCBITaxon:2837503", "label": "Gottfriedia"}}, {"preferred_term": "Brevibacillus sp. OAP136", "term": {"id": "NCBITaxon:55080", "label": "Brevibacillus"}}, {"preferred_term": "Paenibacillus sp. OAE614", "term": {"id": "NCBITaxon:44249", "label": "Paenibacillus"}}]}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet", "sha256": "063a3aeac44f41c5a36ee645a51138fdfbd64be3bd40de1acea1c7c8b30724af", "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.1/2.4 and Methods 4.1–4.2; Figures 1/3. Retain the whole-community inoculation and its experimental contrasts; this is not a generic microbiome effect. Scope: COMMUNITY_LEVEL.

### Paraburkholderia Acid-Tolerant Root Colonization Traits

graph: supported. Targets: CommunityMech:000025.

Retain the qualified claim; align evidence tiers with assay context.

Exact selector ecological_interactions[1]. Participants: {"source_taxon": {"preferred_term": "Paraburkholderia sp. OAS925", "term": {"id": "NCBITaxon:1822464", "label": "Paraburkholderia"}}}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[1].evidence[0].snippet", "sha256": "0c573b7488e6cc047517640cadfa82d519993074869f37181f4ecb5985373160", "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"}, {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "e64fa9506c4a47618fab5b997d0431751f475f5631d498048bef96012a3a0e41", "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.7 and Methods 4.8–4.10; SI8–11 and selected S9 rows. Retain source-only PAIRWISE scope for OAS925 properties. T3SS is a genomic annotation; acid-tolerant motility was measured separately. Individual acid-resistance genes also occur in other isolates, so qualify uniqueness as the combined profile or surveyed T3SS module. No selective gene intervention establishes necessity.

### Paraburkholderia-Dominated SynCom17 Root Assembly

graph: supported. Targets: CommunityMech:000025.

Retain the qualified claim; align evidence tiers with assay context.

Exact selector ecological_interactions[2]. Participants: {"participating_taxa": [{"preferred_term": "Paraburkholderia sp. OAS925", "term": {"id": "NCBITaxon:1822464", "label": "Paraburkholderia"}}, {"preferred_term": "Rhodococcus sp. OAS809", "term": {"id": "NCBITaxon:1827", "label": "Rhodococcus &lt;high G+C Gram-positive bacteria&gt;"}}, {"preferred_term": "Mycobacterium sp. OAE908", "term": {"id": "NCBITaxon:1763", "label": "Mycobacterium"}}, {"preferred_term": "Methylobacterium sp. OAE515", "term": {"id": "NCBITaxon:407", "label": "Methylobacterium"}}, {"preferred_term": "Variovorax sp. OAS795", "term": {"id": "NCBITaxon:34072", "label": "Variovorax"}}, {"preferred_term": "Rhizobium sp. OAE497", "term": {"id": "NCBITaxon:379", "label": "Rhizobium"}}, {"preferred_term": "Bosea sp. OAE506", "term": {"id": "NCBITaxon:85413", "label": "Allobosea"}}, {"preferred_term": "Bradyrhizobium sp. OAE829", "term": {"id": "NCBITaxon:374", "label": "Bradyrhizobium"}}, {"preferred_term": "Lysobacter sp. OAE881", "term": {"id": "NCBITaxon:68", "label": "Lysobacter"}}, {"preferred_term": "Arthrobacter sp. OAP107", "term": {"id": "NCBITaxon:1667", "label": "Arthrobacter sp."}}, {"preferred_term": "Marmoricola sp. OAE513", "term": {"id": "NCBITaxon:86795", "label": "Marmoricola"}}, {"preferred_term": "Chitinophaga sp. OAE865", "term": {"id": "NCBITaxon:79328", "label": "Chitinophaga"}}, {"preferred_term": "Mucilaginibacter sp. OAE612", "term": {"id": "NCBITaxon:423349", "label": "Mucilaginibacter"}}, {"preferred_term": "Niastella sp. OAS944", "term": {"id": "NCBITaxon:354354", "label": "Niastella"}}, {"preferred_term": "Gottfriedia sp. OAE603", "term": {"id": "NCBITaxon:2837503", "label": "Gottfriedia"}}, {"preferred_term": "Brevibacillus sp. OAP136", "term": {"id": "NCBITaxon:55080", "label": "Brevibacillus"}}, {"preferred_term": "Paenibacillus sp. OAE614", "term": {"id": "NCBITaxon:44249", "label": "Paenibacillus"}}]}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet", "sha256": "6a1b117f4ef0431908bbb8ad2d22cba0ac4edd413ce946b52b4c4a582f75720b", "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.4; Figure 3. Retain OAS925 relative-read dominance and its contrast with SynCom16. Approximately 98% reads do not establish absolute exclusion, extinction or uniform participant abundance. Scope: COMMUNITY_LEVEL.

### Treatment-Structured Rhizosphere Exometabolites

graph: supported. Targets: CommunityMech:000025.

Retain the qualified claim; align evidence tiers with assay context.

Exact selector ecological_interactions[3]. Participants: {"participating_taxa": [{"preferred_term": "Paraburkholderia sp. OAS925", "term": {"id": "NCBITaxon:1822464", "label": "Paraburkholderia"}}, {"preferred_term": "Rhodococcus sp. OAS809", "term": {"id": "NCBITaxon:1827", "label": "Rhodococcus &lt;high G+C Gram-positive bacteria&gt;"}}, {"preferred_term": "Mycobacterium sp. OAE908", "term": {"id": "NCBITaxon:1763", "label": "Mycobacterium"}}, {"preferred_term": "Methylobacterium sp. OAE515", "term": {"id": "NCBITaxon:407", "label": "Methylobacterium"}}, {"preferred_term": "Variovorax sp. OAS795", "term": {"id": "NCBITaxon:34072", "label": "Variovorax"}}, {"preferred_term": "Rhizobium sp. OAE497", "term": {"id": "NCBITaxon:379", "label": "Rhizobium"}}, {"preferred_term": "Bosea sp. OAE506", "term": {"id": "NCBITaxon:85413", "label": "Allobosea"}}, {"preferred_term": "Bradyrhizobium sp. OAE829", "term": {"id": "NCBITaxon:374", "label": "Bradyrhizobium"}}, {"preferred_term": "Lysobacter sp. OAE881", "term": {"id": "NCBITaxon:68", "label": "Lysobacter"}}, {"preferred_term": "Arthrobacter sp. OAP107", "term": {"id": "NCBITaxon:1667", "label": "Arthrobacter sp."}}, {"preferred_term": "Marmoricola sp. OAE513", "term": {"id": "NCBITaxon:86795", "label": "Marmoricola"}}, {"preferred_term": "Chitinophaga sp. OAE865", "term": {"id": "NCBITaxon:79328", "label": "Chitinophaga"}}, {"preferred_term": "Mucilaginibacter sp. OAE612", "term": {"id": "NCBITaxon:423349", "label": "Mucilaginibacter"}}, {"preferred_term": "Niastella sp. OAS944", "term": {"id": "NCBITaxon:354354", "label": "Niastella"}}, {"preferred_term": "Gottfriedia sp. OAE603", "term": {"id": "NCBITaxon:2837503", "label": "Gottfriedia"}}, {"preferred_term": "Brevibacillus sp. OAP136", "term": {"id": "NCBITaxon:55080", "label": "Brevibacillus"}}, {"preferred_term": "Paenibacillus sp. OAE614", "term": {"id": "NCBITaxon:44249", "label": "Paenibacillus"}}]}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[3].evidence[0].snippet", "sha256": "f294df6ddcee0f73f3b016e90b0426c81b8beb6115c3e55ba8107e77fe815e4a", "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.5; Figure 4. Retain whole-treatment net bulk extracellular changes. They combine uptake, secretion, transformation and host effects; no taxon-specific exchange or consumption rate is identified. Scope: COMMUNITY_LEVEL.

### SynCom17 Plant Biomass and Root Development Decrease

graph: supported. Targets: CommunityMech:000025.

Retain the qualified claim; align evidence tiers with assay context.

Exact selector ecological_interactions[4]. Participants: {"participating_taxa": [{"preferred_term": "Paraburkholderia sp. OAS925", "term": {"id": "NCBITaxon:1822464", "label": "Paraburkholderia"}}, {"preferred_term": "Rhodococcus sp. OAS809", "term": {"id": "NCBITaxon:1827", "label": "Rhodococcus &lt;high G+C Gram-positive bacteria&gt;"}}, {"preferred_term": "Mycobacterium sp. OAE908", "term": {"id": "NCBITaxon:1763", "label": "Mycobacterium"}}, {"preferred_term": "Methylobacterium sp. OAE515", "term": {"id": "NCBITaxon:407", "label": "Methylobacterium"}}, {"preferred_term": "Variovorax sp. OAS795", "term": {"id": "NCBITaxon:34072", "label": "Variovorax"}}, {"preferred_term": "Rhizobium sp. OAE497", "term": {"id": "NCBITaxon:379", "label": "Rhizobium"}}, {"preferred_term": "Bosea sp. OAE506", "term": {"id": "NCBITaxon:85413", "label": "Allobosea"}}, {"preferred_term": "Bradyrhizobium sp. OAE829", "term": {"id": "NCBITaxon:374", "label": "Bradyrhizobium"}}, {"preferred_term": "Lysobacter sp. OAE881", "term": {"id": "NCBITaxon:68", "label": "Lysobacter"}}, {"preferred_term": "Arthrobacter sp. OAP107", "term": {"id": "NCBITaxon:1667", "label": "Arthrobacter sp."}}, {"preferred_term": "Marmoricola sp. OAE513", "term": {"id": "NCBITaxon:86795", "label": "Marmoricola"}}, {"preferred_term": "Chitinophaga sp. OAE865", "term": {"id": "NCBITaxon:79328", "label": "Chitinophaga"}}, {"preferred_term": "Mucilaginibacter sp. OAE612", "term": {"id": "NCBITaxon:423349", "label": "Mucilaginibacter"}}, {"preferred_term": "Niastella sp. OAS944", "term": {"id": "NCBITaxon:354354", "label": "Niastella"}}, {"preferred_term": "Gottfriedia sp. OAE603", "term": {"id": "NCBITaxon:2837503", "label": "Gottfriedia"}}, {"preferred_term": "Brevibacillus sp. OAP136", "term": {"id": "NCBITaxon:55080", "label": "Brevibacillus"}}, {"preferred_term": "Paenibacillus sp. OAE614", "term": {"id": "NCBITaxon:44249", "label": "Paenibacillus"}}]}. Exact canonical snippet bindings: [{"selector": "ecological_interactions[4].evidence[0].snippet", "sha256": "0a532645bb2a9f4036a42d2bd7510f27db541dd0b9fbda963f14170c67306277", "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}]. Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.3–2.4; Figure 2. Retain whole-SynCom17 plant biomass and root effects. Neither OAS925 alone nor a specific trait was isolated as the cause. Scope: COMMUNITY_LEVEL.

### Node 0 → node 2

graph: supported. Targets: CommunityMech:000025.

Retain the bounded direction.

Exact selector ecological_interactions[0].downstream[0]. Source node 0: SynCom17 EcoFAB Ring-Trial Perturbation. Target node 2: Paraburkholderia-Dominated SynCom17 Root Assembly. Exact canonical edge: {"target": "Paraburkholderia-Dominated SynCom17 Root Assembly", "description": "SynCom17 inoculation supplied the 17-member community from which the OAS925-dominated root profile developed by 22 DAI. The SynCom16 omission comparison supports an inoculum-composition effect, not identification of the molecular mechanism or absolute loss of the other members."}. Edge description SHA256: 995b477467d8d731c00a72f52e9403fd8990ba6879811f3cd3d489b83a364ba2. Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.4; Figure 3. The directed effect is the whole inoculation-treatment contrast; it does not identify a single-member mediator.

### Node 0 → node 3

graph: supported. Targets: CommunityMech:000025.

Retain the bounded direction.

Exact selector ecological_interactions[0].downstream[1]. Source node 0: SynCom17 EcoFAB Ring-Trial Perturbation. Target node 3: Treatment-Structured Rhizosphere Exometabolites. Exact canonical edge: {"target": "Treatment-Structured Rhizosphere Exometabolites", "description": "SynCom17 inoculation altered the plant-microbe system and thereby changed the measured bulk spent-medium metabolite profile relative to the control treatments. This is a treatment-level effect; microbial versus plant production, uptake and extracellular enzyme activity were not separated."}. Edge description SHA256: 5cb971ec57720a05c47781b2985c83d973e2251f0b60a389308ff6c4f53bc370. Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.5; Figure 4. The directed effect is the whole inoculation-treatment contrast; it does not identify a single-member mediator.

### Node 0 → node 4

graph: supported. Targets: CommunityMech:000025.

Retain the bounded direction.

Exact selector ecological_interactions[0].downstream[2]. Source node 0: SynCom17 EcoFAB Ring-Trial Perturbation. Target node 4: SynCom17 Plant Biomass and Root Development Decrease. Exact canonical edge: {"target": "SynCom17 Plant Biomass and Root Development Decrease", "description": "The SynCom17 inoculation treatment reduced shoot biomass in the combined-laboratory comparison with axenic plants and reduced root development from 14 DAI onward. The experiment establishes a whole-treatment response, not OAS925-only toxicity, competition for a specific nutrient or one necessary member."}. Edge description SHA256: 33581f51519a7d23e12d1479bc890a7e127dee3dd5d94c473f1a27f5c35dcbec. Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.3–2.4; Figure 2. The directed effect is the whole inoculation-treatment contrast; it does not identify a single-member mediator.

### Node 1 → node 2

graph: supported. Targets: CommunityMech:000025.

Retain the bounded direction.

Exact selector ecological_interactions[1].downstream[0]. Source node 1: Paraburkholderia Acid-Tolerant Root Colonization Traits. Target node 2: Paraburkholderia-Dominated SynCom17 Root Assembly. Exact canonical edge: {"target": "Paraburkholderia-Dominated SynCom17 Root Assembly", "description": "HYPOTHESIZED - acid-tolerant motility, colonization traits and associated genomic modules may help OAS925 establish and expand on roots, contributing to its relative dominance. Separate isolate assays and gene annotation support candidate mechanisms, but none was selectively disrupted or rescued in the 17-member community."}. Edge description SHA256: 05a729400915c693bfa62c4570c3c8e9c9e6db08bbbd3682247e9ba2be8b49e7. Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.4; Figure 3 and Results 2.7; SI8–11. Trait contribution remains HYPOTHESIZED, without a necessity test.

### Five nodes and four directed claims

graph: supported. Targets: CommunityMech:000025.

No topology repair is required.

Four COMMUNITY_LEVEL nodes and one source-only PAIRWISE node have no interaction_type. Three arrows originate at node 0 and one HYPOTHESIZED arrow at node 1. Retain the explicit limits and current discussion.

### Study, preparation and host-growth separation

scope: concern. Targets: CommunityMech:000025.

Current conditions mix distinct experiments.

Ring-trial seedlings had three days stratification, three days germination and four days in EcoFAB before inoculation. The 27 C, 200 rpm reporter preparation and three-day seedling assay are separate; motility precultures also used 200 rpm at 27 C. The earlier sterile nitrogen experiment is not a SynCom17 nitrogen/light intervention.

### Rank refinement and reproducible GTDB provenance

grounding: concern. Targets: CommunityMech:000025.

Grounding cores are reproducible; OAP107 rank and release wording need bounded repair.

Encoded NCBITaxon:1667 is an explicitly unresolved unnamed-species placeholder. Source-linked OAP107 metadata supports genus NCBITaxon:1663, without resolving its species or strain-level GTDB. Fifteen mapping cores reproduce, including curated Allobosea to legacy Bosea 34/34. Preserve Paenibacillus ambiguity. A filesystem date does not establish a GTDB release or build date.

### Exact excerpts and assay-local tiers

evidence: concern. Targets: CommunityMech:000025.

All 30 snippets match, but several placements are broader than their source support.

Use S2 and Methods 4.8 for exact stock identities rather than repeating a generic membership abstract. Living-host colonization and plant outcomes need IN_VIVO scope; genomic annotations need COMPUTATIONAL, and separate isolate phenotype assays remain IN_VITRO. Exact lexical matches do not prove stronger causal interpretations.

### Actual study resources and genome identifiers

evidence: concern. Targets: CommunityMech:000025.

Five encoded study resources resolve; the genome pseudo-range is incomplete.

PRJNA1151037, GNPS task, MSV000095476, NMDC study and Figshare collection identify the ring trial. Gp0588949-Gp0589682 is not the exact 17-project set and excludes Mycobacterium Gp0440934. Keep IMG taxon identifiers distinct from NCBITaxon; metadata is not functional validation.

### Source access and prior context

scope: supported. Targets: CommunityMech:000025.

The main claims have complete scientific assessment with bounded SI scope.

Lead read both main scientific texts, all principal main/SI figures, all related main figures and selected S1/S2/S9 cells. Root independently read the protocol and complete Markdown caches; support read the complete third PMC cache. Videos, bulk numerical matrices and raw omics were not reanalyzed. Current issue 1424 is closed; 1427 remains open; the historical Allobosea repair is retained.

### Native checks and actual limits

schema: supported. Targets: CommunityMech:000025.

Eight required checks passed; no native failure.

Deterministic success does not certify causal support. Optional adapter unavailability, a truncated package and auxiliary extraction/writer errors are preserved separately from native checks.

### Two literal review scores

completeness: supported. Targets: CommunityMech:000025.

Completeness 45; quality 100 after capping raw 103.

## Findings

### causal-role-evidence: Separate treatment outcomes from member-level mechanisms

major / open / confirmed; issue key: cm-000025-causal-role-evidence.

Competitive exclusion, OAS925-specific uptake/plant harm and optional member roles exceed the demonstrated claims; evidence tiers mix host, isolate and genomic contexts.

### study-stage-scope: Separate ring-trial conditions from related studies and assays

major / open / confirmed; issue key: cm-000025-study-stage-scope.

Nitrogen/light interventions and reporter preparation conditions are pooled with the ring trial.

### grounding-provenance: Refine OAP107 rank and mapping provenance

minor / open / confirmed; issue key: cm-000025-grounding-provenance.

The unresolved OAP107 placeholder can be refined using source-linked genus metadata; latest/build assertions exceed file provenance.

### genome-identifiers: Replace the genome pseudo-range with exact identifiers

minor / open / confirmed; issue key: cm-000025-genome-identifiers.

The range omits Gp0440934 and does not enumerate all 17 source projects.

## Recommended Actions And Acceptance Checks

### repair-causal-scope

Align member claims and evidence with actual assays.

- Qualify competitive exclusion and member-specific uptake as hypotheses; attribute plant effects to SynCom17 treatment. Preserve relative abundance and net extracellular measurements without assigning absolute exclusion or taxon-specific flux.
- Omit unsupported optional PRIMARY_DEGRADER/CROSS_FEEDER tags or attach isolate-local support with the correct predicted versus demonstrated scope. Preserve positive genomic capabilities; do not impose a polymer-only definition or infer physiological inability.
- Use exact stock evidence from S2/Methods 4.8. Correct host-associated evidence to IN_VIVO, genomic annotation to COMPUTATIONAL and separate isolate assays to IN_VITRO where applicable.
- Retain five nodes and four arrows; retain HYPOTHESIZED trait mediation. Distinguish the combined acid-resistance profile from uniqueness of individual genes or T3SS signature; do not assert trait necessity or uniquely highest OAS925 biomass.

### repair-study-stages

Represent each protocol and perturbation in its own study context.

- Remove nitrogen/light factorial claims from the ring-trial design. Retain the earlier sterile nitrogen study only as separately attributed context.
- Separate S2 stock preparation, genomic DNA culture, RFP-isolate microscopy, motility precultures and host cultivation. Preserve stock-specific media and distinct shaking/temperature values.
- Use ten-day ring-trial seedlings, 9 mL half-MS plus 1 mL inoculum, default 14 h/10 h light-dark and laboratory C deviation, and 22 DAI harvest; preserve the source theoretical inoculum and freeze-thaw assumptions. Keep protocol pH5.7 versus main5.5–6.0 appropriately attributed.

### repair-grounding-provenance

Use bounded source-linked rank and reproducible map provenance.

- Use verified Arthrobacter genus NCBITaxon:1663 for OAP107 at taxonomy[9] and its four participant placements if applying the source-linked refinement. Preserve stock code and species uncertainty; re-evaluate GTDB status without selecting one of eleven genus candidates arbitrarily.
- Retain the fifteen valid numerical cores, curated Allobosea85413/Bosea34-of-34 mapping and Paenibacillus ambiguity. Replace unsupported latest/build wording with mapping file identity, hash and method; filesystem mtime is not release metadata.

### repair-genome-identifiers

Represent exact source genome identifiers and verify the curated record.

- Replace the pseudo-range with the source genome collection and/or all 17 explicit strain-to-IMG/GOLD pairs from Methods 4.8/S2, including OAE908 Gp0440934. Preserve namespaces and actual assembly scope.
- After separately authorized curation, rerun schema, strict, ontology, reference, GTDB, domain and history checks; recheck graph participants. Regenerate HTML with just gen-html and run just check-docs-current.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml; Whole canonical record | supports | Defined 17-isolate plant-associated community, five nodes and four arrows. |
| design | PMID:40920748; DOI:10.1371/journal.pbio.3003358; Results 2.1, sec003, both paragraphs; 2.4, sec006, sole paragraph; Figures 1 and 3 | supports | Five laboratories compared axenic, SynCom16, SynCom17 and plant-free treatments; each treatment had seven replicates per laboratory. |
| cultivation | PMID:40920748; DOI:10.1371/journal.pbio.3003358; Methods 4.1 Preparation of synthetic bacterial communities, sec012, first direct paragraph | supports | Isolate preparation and equal-cell stock assembly are separate from host inoculation and isolate phenotype assays. |
| host | PMID:40920748; DOI:10.1371/journal.pbio.3003358; Methods 4.2 Experimental setup and plant growth conditions, sec013, sole paragraph; 4.4, sec015 | supports | The ring trial used ten-day-old seedlings, laboratory-specific light conditions and harvest at 22 days after inoculation. |
| outcomes | PMID:40920748; DOI:10.1371/journal.pbio.3003358; Results 2.3–2.5, sec005–sec007; Figures 2–4 | supports | Whole-treatment plant effects, relative community profiles and net bulk spent-medium changes were measured. |
| traits | PMID:40920748; DOI:10.1371/journal.pbio.3003358; Results 2.7, sec009, all four paragraphs; Discussion, sec010; Methods 4.7–4.10 | supports | Genome annotations and separate growth, biofilm, reporter and motility assays support candidate traits, not isolated causal mediation. |
| genomes | PMID:40920748; DOI:10.1371/journal.pbio.3003358; Methods 4.8 Genomic analysis of bacterial isolates, sec019, first paragraph; S2 Table | supports | Seventeen specific strain-to-IMG/GOLD pairs include Mycobacterium OAE908 Gp0440934. |
| data | PMID:40920748; DOI:10.1371/journal.pbio.3003358; Data Availability, notes1, sole paragraph | supports | The source declares sequencing, metabolomics, analysis and genome-collection resources. |
| nitrogen | PMID:38170767; DOI:10.1126/sciadv.adg7888; Results and Methods: plant growth/nitrogen treatments and individual bacterial growth on selected exudates; Figures 1 and 5 | supports | The earlier sterile-plant nitrogen experiment and individual bacterial assays are not SynCom17 nitrogen or light perturbations. |
| stock-table | PMID:40920748; DOI:10.1371/journal.pbio.3003358; S2 Table; All 18 rows of S2 Table, including header | supports | Exact stocks, preferred preparation media and genome identifiers. |
| trait-table | PMID:40920748; DOI:10.1371/journal.pbio.3003358; S9 Table; Selected rows documented in workbook-selected-read.json; T3SS signature row 2 | supports | OAS925 has the uniquely detected surveyed T3SS signature; other pathway annotations remain predicted potential. |
| protocol | DOI:10.17504/protocols.io.kxygxyydkl8j/v1; Protocol PDF pages 4–5, 8 and 12; independently read by root | supports | Timeline, half-MS preparation at pH 5.7 and inoculum dilution support separation of the ring trial from related assays. |
| ontology | /private/tmp/cm-review-session/batch-16/000025/ontology-authority.json; Receipt with explicit underlying read scope | supports | Twenty ID/label pairs match across 90 placements. |
| semantics | /private/tmp/cm-review-session/batch-16/000025/semantic-review-notes.json; Receipt with explicit underlying read scope | supports | Source-specific roles, evidence tiers and grounding assessed. |
| rank | /private/tmp/cm-review-session/batch-16/000025/child-source-linked-rank-scope.json; Receipt with explicit underlying read scope | supports | Source-linked OAP107 metadata supports genus Arthrobacter 1663; no exact species assignment. |
| gtdb | /private/tmp/cm-review-session/batch-16/000025/child-gtdb-crosswalk.json; Receipt with explicit underlying read scope | supports | Fifteen current numeric mapping cores reproduce; aggregate votes do not identify study strains. |
| adapter | /private/tmp/cm-review-session/batch-16/000025/child-structured-adapter-applicability.json; Receipt with explicit underlying read scope | supports | T3SS, acid-resistance and motility annotation scope checked; optional structured runner unavailable. |
| snippets | /private/tmp/cm-review-session/batch-16/000025/snippet-audit.json; Receipt with explicit underlying read scope | supports | Thirty strict source/cache matches: 22 MED Abstract and eight JATS placements. |
| resources | /private/tmp/cm-review-session/batch-16/000025/dataset-verification.json; Receipt with explicit underlying read scope | supports | Six resource identities verified; genome pseudo-range omits a source-listed member. |
| provenance | /private/tmp/cm-review-session/batch-16/000025/provenance-audit.json; Receipt with explicit underlying read scope | supports | Focal histories, prior decision, cohort and current issue context checked. |
| assets | /private/tmp/cm-review-session/batch-16/000025/lead-source-assets.json; Receipt with explicit underlying read scope | supports | Declared source inventory and positive/failed retrieval classifications. |
| read-scope | /private/tmp/cm-review-session/batch-16/000025/lead-primary-read-scope.json; Receipt with explicit underlying read scope | supports | Whole scientific texts, main figures and relevant SI assessed with explicit unread boundaries. |
| locators | /private/tmp/cm-review-session/batch-16/000025/source-locator-verification.json; Receipt with explicit underlying read scope | supports | Exact source contexts and two-word cultivation quote verified. |
| source-audit | /private/tmp/cm-review-session/batch-16/000025/source-audit.json; Receipt with explicit underlying read scope | supports | Two major and two minor findings; graph topology retained. |
| root-source | /private/tmp/cm-review-session/batch-16/000025/root-independent-source-audit.json; Receipt with explicit underlying read scope | supports | Independent source assessment agrees. |
| collection | /private/tmp/cm-review-session/batch-16/000025/root-protocol-collection-audit.json; Receipt with explicit underlying read scope | supports | Protocol and collection identity verified; individual DSM113627 is distinct from DSM200000SY. |
| support | /private/tmp/cm-review-session/batch-16/000025/support-final-audit.json; Receipt with explicit underlying read scope | supports | Final provenance, snippets, resources and metrics reconciled. |
| support-manifest | /private/tmp/cm-review-session/batch-16/000025/support-frozen-manifest.json; Receipt with explicit underlying read scope | supports | Supporting artifacts frozen. |
| auxiliary | /private/tmp/cm-review-session/batch-16/000025/auxiliary-frozen-manifest.json; Receipt with explicit underlying read scope | supports | Eight native checks and source-specific authority work frozen. |
| check-validate | /private/tmp/cm-review-session/batch-16/000025/validate.json; Actual command and complete output | supports | Required native exit 0. |
| check-validate-strict | /private/tmp/cm-review-session/batch-16/000025/validate-strict.json; Actual command and complete output | supports | Required native exit 0. |
| check-validate-terms | /private/tmp/cm-review-session/batch-16/000025/validate-terms.json; Actual command and complete output | supports | Required native exit 0. |
| check-validate-references-explained | /private/tmp/cm-review-session/batch-16/000025/validate-references-explained.json; Actual command and complete output | supports | Required native exit 0. |
| check-validate-gtdb | /private/tmp/cm-review-session/batch-16/000025/validate-gtdb.json; Actual command and complete output | supports | Required native exit 0. |
| check-validate-gtdb-domain | /private/tmp/cm-review-session/batch-16/000025/validate-gtdb-domain.json; Actual command and complete output | supports | Required native exit 0. |
| check-validate-history | /private/tmp/cm-review-session/batch-16/000025/validate-history.json; Actual command and complete output | supports | Required native exit 0. |
| check-normalize-cache-names-check | /private/tmp/cm-review-session/batch-16/000025/normalize-cache-names-check.json; Actual command and complete output | supports | Required native exit 0. |
| context-audit-network | /private/tmp/cm-review-session/batch-16/audit-network.json; Fresh batch16 corpus baseline | supports | Corpus context is distinct from the target network. |
| context-check-network-quality | /private/tmp/cm-review-session/batch-16/check-network-quality.json; Fresh batch16 corpus baseline | supports | Corpus context is distinct from the target network. |

## Limits And Additional Notes

- Relative reads, bulk metabolite profiles, isolate phenotypes and genome annotations do not establish member-specific flux or trait necessity.
- Source laboratory/timing differences remain explicit. S1 laboratory E logger date and endpoint labels are not silently harmonized.
- Principal videos, settings and response files were inventoried but not inspected; other numerical workbooks were not exhaustively read. Related nitrogen SI text was read only through character8000, with no SI pixel claim.
- No raw genome, sequencing, metabolomic or video reanalysis. The timed-out principal package is a failed retrieval; genuine direct publisher assets supplied the assessed figures and tables.
- Optional structured runner unavailable; this is not negative gene evidence or an unavailable required check. Auxiliary construction/extraction failures are distinct from zero native failures.
- Exact inspection source/target arrays and actual command types preserved. Thirty strict snippet matches, six node bindings, four exact edge-description hashes and eight evidence-linked dimensions.
- This review proposes curation only; no canonical, cache, history or Git change.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T094134Z-ecofab-ring-trial-record-review-v2
kind: record
repository: CultureBotAI/CommunityMech
title: EcoFAB ring trial SynCom17 record review
started_at: '2026-10-22T09:22:45.700136Z'
finished_at: '2026-10-22T09:41:34.672711Z'
reviewer:
  identity: codex
  kind: agent
  independence: unknown
  independence_basis: Separate lead, root, auxiliary and support assessments; no person-level
    independence claim.
skill: review-yaml-record
completion: completed
verdict: needs_curation
scientific_review: true
summary: Two major findings concern causal/evidence scope and pooled study conditions;
  two minor findings concern taxon/map provenance and genome identifiers. Retain five
  nodes and four qualified arrows. Eight required checks pass; completeness45 and
  quality100 (raw103).
source:
  git_revision: cb7a782c8ba80299dca8761ad0a2c90bccd8a117
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
  - path: history/records/EcoFAB_Ring_Trial_SynCom17/2026-10-02T054932Z-codex-ecf17a.yaml
    sha256: 265fc37c2ef65720e26261c78ae6bbe627933d1bfac6703b0f13f1160ada0bfa
    role: context
  - path: history/records/EcoFAB_Ring_Trial_SynCom17/2026-10-06T082610Z-codex-00f1fc.yaml
    sha256: 74b79275ed965c83ebc9da67a25f604a0c707af6f69fa6fcf47c43a9326d91e1
    role: context
  - path: justfile
    sha256: 4c8551e51dbc69a0331c0c8461414ea710275d43cc83b86e07e00b3749081453
    role: context
  - path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    sha256: 2e0f6da3387904e4f33283c5117df14ab55c80a1ec7d7290fe00343f69569f1d
    role: target
  - path: references_cache/PMID_40920748.md
    sha256: 9835902fb578c079d6b11fd84cff8498d55d43fd931713cd77e40c411d571b07
    role: context
  - path: references_cache/doi_10.1126_sciadv.adg7888.md
    sha256: 18499621c38705107707711cf65fd933886be3525c8b0c03ed3675c5d4ec8317
    role: context
  - path: references_cache/pmc_full_pmid_40920748.txt
    sha256: 5ada098f595961565eaac5d2420a8fb29a6e7a324f35a41f284e49ae6db7e5e3
    role: context
  - path: reports/causal_graph_review/adversarial-review-20261006-batch36.yaml
    sha256: 411a075ced01f0daaf59db828b6bfc2163a00d6d040ecae1328b5aee70b5452e
    role: context
  - path: reports/causal_graph_review/decisions/20261006-three-records-batch36.yaml
    sha256: 1b57537e06001eaf8d91b2ef58bf176281a616c4a21158cf4679fb969ce010e8
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
- target_id: CommunityMech:000025
  path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
  label: EcoFAB 2.0 Root Microbiome Ring Trial SynCom17
  kind: maintained
  record_class: MicrobialCommunity
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    role: canonical_record
scope:
  description: Whole record, both cited scientific texts, principal main/SI figures,
    relevant tables, protocol and bounded resource/authority checks.
  selection: Sole released CommunityMech:000025 in owned batch16.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - CommunityMech:000025
checks:
- check_id: validate
  name: validate
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000025
  command: just --no-dotenv validate kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate
- check_id: validate-strict
  name: validate-strict
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000025
  command: just --no-dotenv validate-strict kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    --out /private/tmp/cm-review-session/batch-16/000025/strict-report.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-strict
- check_id: validate-terms
  name: validate-terms
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000025
  command: just --no-dotenv validate-terms kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-terms
- check_id: validate-references-explained
  name: validate-references-explained
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000025
  command: just --no-dotenv validate-references-explained kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-references-explained
- check_id: validate-gtdb
  name: validate-gtdb
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000025
  command: just --no-dotenv validate-gtdb kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb
- check_id: validate-gtdb-domain
  name: validate-gtdb-domain
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000025
  command: just --no-dotenv validate-gtdb-domain kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-gtdb-domain
- check_id: validate-history
  name: validate-history
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000025
  command: just --no-dotenv validate-history history/records/EcoFAB_Ring_Trial_SynCom17
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-validate-history
- check_id: normalize-cache-names-check
  name: normalize-cache-names-check
  status: passed
  required: true
  summary: Actual native exit 0.
  target_ids:
  - CommunityMech:000025
  command: uv run python scripts/normalize_cache_names.py --check
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - check-normalize-cache-names-check
- check_id: context-audit-network
  name: audit-network corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1; 44 warnings and no errors across 16 of 477 records.
  target_ids:
  - CommunityMech:000025
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv audit-network
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-audit-network
- check_id: context-check-network-quality
  name: check-network-quality corpus context
  status: failed
  required: false
  summary: Actual corpus exit 1; 44 warnings and no errors across 16 of 477 records.
  target_ids:
  - CommunityMech:000025
  command: PYTHONPATH=/private/tmp/communitymech-record-reviews-batch-16/src JUST_NO_DOTENV=true
    UV_CACHE_DIR=/private/tmp/cm-review-uv-cache UV_NO_SYNC=1 UV_OFFLINE=true just
    --no-dotenv check-network-quality
  exit_code: 1
  expected_exit_code: 0
  evidence_ids:
  - context-check-network-quality
- check_id: structured-adapter
  name: Source-specific structured adapter
  status: unavailable
  required: false
  summary: Optional runner unavailable in owned runtime.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - adapter
  scope_note: No provider query or absence-of-function inference; source-based assessment
    remains complete.
evidence:
- evidence_id: record
  kind: record_content
  reference: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
  locator: Whole canonical record
  summary: Defined 17-isolate plant-associated community, five nodes and four arrows.
  support: supports
  accessed_at: '2026-10-22T09:37:34.899723Z'
- evidence_id: design
  kind: primary_source
  reference: PMID:40920748; DOI:10.1371/journal.pbio.3003358
  locator: Results 2.1, sec003, both paragraphs; 2.4, sec006, sole paragraph; Figures
    1 and 3
  summary: Five laboratories compared axenic, SynCom16, SynCom17 and plant-free treatments;
    each treatment had seven replicates per laboratory.
  support: supports
  accessed_at: '2026-10-22T09:37:34.899797Z'
  snapshot_sha256: a24f3cb202adc56ab293852bfc6af6ba2cd7275960368b261cb51a75693b82f3
- evidence_id: cultivation
  kind: primary_source
  reference: PMID:40920748; DOI:10.1371/journal.pbio.3003358
  locator: Methods 4.1 Preparation of synthetic bacterial communities, sec012, first
    direct paragraph
  summary: Isolate preparation and equal-cell stock assembly are separate from host
    inoculation and isolate phenotype assays.
  support: supports
  accessed_at: '2026-10-22T09:37:34.900231Z'
  snapshot_sha256: a24f3cb202adc56ab293852bfc6af6ba2cd7275960368b261cb51a75693b82f3
  quote: equal numbers
- evidence_id: host
  kind: primary_source
  reference: PMID:40920748; DOI:10.1371/journal.pbio.3003358
  locator: Methods 4.2 Experimental setup and plant growth conditions, sec013, sole
    paragraph; 4.4, sec015
  summary: The ring trial used ten-day-old seedlings, laboratory-specific light conditions
    and harvest at 22 days after inoculation.
  support: supports
  accessed_at: '2026-10-22T09:37:34.900352Z'
  snapshot_sha256: a24f3cb202adc56ab293852bfc6af6ba2cd7275960368b261cb51a75693b82f3
- evidence_id: outcomes
  kind: primary_source
  reference: PMID:40920748; DOI:10.1371/journal.pbio.3003358
  locator: Results 2.3–2.5, sec005–sec007; Figures 2–4
  summary: Whole-treatment plant effects, relative community profiles and net bulk
    spent-medium changes were measured.
  support: supports
  accessed_at: '2026-10-22T09:37:34.900451Z'
  snapshot_sha256: a24f3cb202adc56ab293852bfc6af6ba2cd7275960368b261cb51a75693b82f3
- evidence_id: traits
  kind: primary_source
  reference: PMID:40920748; DOI:10.1371/journal.pbio.3003358
  locator: Results 2.7, sec009, all four paragraphs; Discussion, sec010; Methods 4.7–4.10
  summary: Genome annotations and separate growth, biofilm, reporter and motility
    assays support candidate traits, not isolated causal mediation.
  support: supports
  accessed_at: '2026-10-22T09:37:34.900544Z'
  snapshot_sha256: a24f3cb202adc56ab293852bfc6af6ba2cd7275960368b261cb51a75693b82f3
- evidence_id: genomes
  kind: primary_source
  reference: PMID:40920748; DOI:10.1371/journal.pbio.3003358
  locator: Methods 4.8 Genomic analysis of bacterial isolates, sec019, first paragraph;
    S2 Table
  summary: Seventeen specific strain-to-IMG/GOLD pairs include Mycobacterium OAE908
    Gp0440934.
  support: supports
  accessed_at: '2026-10-22T09:37:34.900637Z'
  snapshot_sha256: a24f3cb202adc56ab293852bfc6af6ba2cd7275960368b261cb51a75693b82f3
- evidence_id: data
  kind: primary_source
  reference: PMID:40920748; DOI:10.1371/journal.pbio.3003358
  locator: Data Availability, notes1, sole paragraph
  summary: The source declares sequencing, metabolomics, analysis and genome-collection
    resources.
  support: supports
  accessed_at: '2026-10-22T09:37:34.900728Z'
  snapshot_sha256: a24f3cb202adc56ab293852bfc6af6ba2cd7275960368b261cb51a75693b82f3
- evidence_id: nitrogen
  kind: primary_source
  reference: PMID:38170767; DOI:10.1126/sciadv.adg7888
  locator: 'Results and Methods: plant growth/nitrogen treatments and individual bacterial
    growth on selected exudates; Figures 1 and 5'
  summary: The earlier sterile-plant nitrogen experiment and individual bacterial
    assays are not SynCom17 nitrogen or light perturbations.
  support: supports
  accessed_at: '2026-10-22T09:37:34.900818Z'
  snapshot_sha256: 4404957d6903f95867787162e8af0de118d59ffdf55cf2942ebea13df9876197
- evidence_id: stock-table
  kind: primary_source
  reference: PMID:40920748; DOI:10.1371/journal.pbio.3003358; S2 Table
  locator: All 18 rows of S2 Table, including header
  summary: Exact stocks, preferred preparation media and genome identifiers.
  support: supports
  accessed_at: '2026-10-22T09:37:34.901083Z'
  snapshot_sha256: fd7882e673f62498ce2ac8c1215ece003edb7369fa780c106bfaa6db4b80e147
- evidence_id: trait-table
  kind: primary_source
  reference: PMID:40920748; DOI:10.1371/journal.pbio.3003358; S9 Table
  locator: Selected rows documented in workbook-selected-read.json; T3SS signature
    row 2
  summary: OAS925 has the uniquely detected surveyed T3SS signature; other pathway
    annotations remain predicted potential.
  support: supports
  accessed_at: '2026-10-22T09:37:34.901253Z'
  snapshot_sha256: 83dea79fe391fff1fee305bd04db6731fd108505b21d25e73abb54040ef5c4f2
- evidence_id: protocol
  kind: primary_source
  reference: DOI:10.17504/protocols.io.kxygxyydkl8j/v1
  locator: Protocol PDF pages 4–5, 8 and 12; independently read by root
  summary: Timeline, half-MS preparation at pH 5.7 and inoculum dilution support separation
    of the ring trial from related assays.
  support: supports
  accessed_at: '2026-10-22T09:37:34.901427Z'
  snapshot_sha256: c6ba43539a7e4fa8ac48f8bc7e2b36372370bc243fa3be29f8d7a9d2b115270f
- evidence_id: ontology
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000025/ontology-authority.json
  locator: Receipt with explicit underlying read scope
  summary: Twenty ID/label pairs match across 90 placements.
  support: supports
  accessed_at: '2026-10-22T09:37:34.902840Z'
  snapshot_sha256: 74f60a2e419da11b96dd14a9097234b5dbce39054a9a4939465d9ef144055f4d
- evidence_id: semantics
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000025/semantic-review-notes.json
  locator: Receipt with explicit underlying read scope
  summary: Source-specific roles, evidence tiers and grounding assessed.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903011Z'
  snapshot_sha256: e94722525c1069f113565f728d63e4e6d6552bd1288a493f4f1c7db96e759cc9
- evidence_id: rank
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000025/child-source-linked-rank-scope.json
  locator: Receipt with explicit underlying read scope
  summary: Source-linked OAP107 metadata supports genus Arthrobacter 1663; no exact
    species assignment.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903059Z'
  snapshot_sha256: 607696060ba3659cf6b06f4c8657c668df8b9aef48af19e2e62b2b8207689648
- evidence_id: gtdb
  kind: authority
  reference: /private/tmp/cm-review-session/batch-16/000025/child-gtdb-crosswalk.json
  locator: Receipt with explicit underlying read scope
  summary: Fifteen current numeric mapping cores reproduce; aggregate votes do not
    identify study strains.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903095Z'
  snapshot_sha256: 68d30d9f80ccaf4eaf7cd7735dc4c5f33a8acea9e3e68751a81724433bee6ebe
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/child-structured-adapter-applicability.json
  locator: Receipt with explicit underlying read scope
  summary: T3SS, acid-resistance and motility annotation scope checked; optional structured
    runner unavailable.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903128Z'
  snapshot_sha256: 25458c0be6fbb95a3ed90b3fbf4b0e0d354b152d960bdd4d3834843953407a7e
- evidence_id: snippets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/snippet-audit.json
  locator: Receipt with explicit underlying read scope
  summary: 'Thirty strict source/cache matches: 22 MED Abstract and eight JATS placements.'
  support: supports
  accessed_at: '2026-10-22T09:37:34.903156Z'
  snapshot_sha256: d54f70979568249ebbd5ddbe9250ce5639c9d441e61da506fb80e6e9d5631327
- evidence_id: resources
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/dataset-verification.json
  locator: Receipt with explicit underlying read scope
  summary: Six resource identities verified; genome pseudo-range omits a source-listed
    member.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903194Z'
  snapshot_sha256: 40cf61da718aee8ee29c5941ab8c9c576c2f491ace2a3209b224df656120275d
- evidence_id: provenance
  kind: prior_review
  reference: /private/tmp/cm-review-session/batch-16/000025/provenance-audit.json
  locator: Receipt with explicit underlying read scope
  summary: Focal histories, prior decision, cohort and current issue context checked.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903223Z'
  snapshot_sha256: b82c65677a2b72803d4acbacbb6032baee9b5145caedccfa2947bb4bcb1eef3c
- evidence_id: assets
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/lead-source-assets.json
  locator: Receipt with explicit underlying read scope
  summary: Declared source inventory and positive/failed retrieval classifications.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903257Z'
  snapshot_sha256: 1346c96fd1305b582b24ee2d18ebf8f5c043dd98c4773f4121b2e694a0e3e8a2
- evidence_id: read-scope
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/lead-primary-read-scope.json
  locator: Receipt with explicit underlying read scope
  summary: Whole scientific texts, main figures and relevant SI assessed with explicit
    unread boundaries.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903293Z'
  snapshot_sha256: 1b9c98b7520120957a4447f0eefdabc933933637bdefa21783ca5ca48d5d7966
- evidence_id: locators
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/source-locator-verification.json
  locator: Receipt with explicit underlying read scope
  summary: Exact source contexts and two-word cultivation quote verified.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903321Z'
  snapshot_sha256: 2bfc4a6b96ad20be14911d22941752d6a3481ec07a92484488a8b56008b017ad
- evidence_id: source-audit
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/source-audit.json
  locator: Receipt with explicit underlying read scope
  summary: Two major and two minor findings; graph topology retained.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903393Z'
  snapshot_sha256: b3873f0f20bb58566a65a9b07fbf77c57f8ad6d7a3ce8c30b129b88dd5e72704
- evidence_id: root-source
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/root-independent-source-audit.json
  locator: Receipt with explicit underlying read scope
  summary: Independent source assessment agrees.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903443Z'
  snapshot_sha256: e113d500fa0db3efc64ca6634b6dee723b49f4cd1a0fe35bfdb8fcf5c70a9aac
- evidence_id: collection
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/root-protocol-collection-audit.json
  locator: Receipt with explicit underlying read scope
  summary: Protocol and collection identity verified; individual DSM113627 is distinct
    from DSM200000SY.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903487Z'
  snapshot_sha256: f850b1822386e39a4651227574bcc75edcc7db490c7c095fa4ba517cb4935ac7
- evidence_id: support
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/support-final-audit.json
  locator: Receipt with explicit underlying read scope
  summary: Final provenance, snippets, resources and metrics reconciled.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903520Z'
  snapshot_sha256: c9362e6d30464e2f8d8e95f67df3afc0d4a3b91fd76d8b894fe0f759884e3664
- evidence_id: support-manifest
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/support-frozen-manifest.json
  locator: Receipt with explicit underlying read scope
  summary: Supporting artifacts frozen.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903553Z'
  snapshot_sha256: 49f0d83f0807233f14679d14086234349ce1d28fddaa726ef25476a69007a0dd
- evidence_id: auxiliary
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/auxiliary-frozen-manifest.json
  locator: Receipt with explicit underlying read scope
  summary: Eight native checks and source-specific authority work frozen.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903584Z'
  snapshot_sha256: d25e04555d54171567d8fa5464b32f2508093f23c836a1e2e32bc3da3f793e08
- evidence_id: check-validate
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/validate.json
  locator: Actual command and complete output
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903672Z'
  snapshot_sha256: 8621da791f257a539d534a701bba7db48f7de9387c1fc8c83f26b9208e64fbc0
- evidence_id: check-validate-strict
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/validate-strict.json
  locator: Actual command and complete output
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903729Z'
  snapshot_sha256: 279f5a585b641cc50b3f46f4e46fd83054ad6f119e018a0f36cd2dc4d538b738
- evidence_id: check-validate-terms
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/validate-terms.json
  locator: Actual command and complete output
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903779Z'
  snapshot_sha256: 86de26c76949da5a77d5c5f9dbcdf17ddb125a0a73d852e8f94dd901868ce8ff
- evidence_id: check-validate-references-explained
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/validate-references-explained.json
  locator: Actual command and complete output
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903829Z'
  snapshot_sha256: 469a3dfaba63ec33bba965d1e5f4e086a099035a5d4f798dee86df57cf4371bd
- evidence_id: check-validate-gtdb
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/validate-gtdb.json
  locator: Actual command and complete output
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903874Z'
  snapshot_sha256: 6389ff3bbb1bf813102865050358019d3dde4f2a543a7e6a3ba00f43b900ea42
- evidence_id: check-validate-gtdb-domain
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/validate-gtdb-domain.json
  locator: Actual command and complete output
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903919Z'
  snapshot_sha256: 0e3b80786ddfadb7741d080f80376897c492e427d49da4eaa71fbc201467a596
- evidence_id: check-validate-history
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/validate-history.json
  locator: Actual command and complete output
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T09:37:34.903964Z'
  snapshot_sha256: d9e0ad166add85ce0bfd1b1190c473f16897581e419355accb6827654d306b9d
- evidence_id: check-normalize-cache-names-check
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/000025/normalize-cache-names-check.json
  locator: Actual command and complete output
  summary: Required native exit 0.
  support: supports
  accessed_at: '2026-10-22T09:37:34.904011Z'
  snapshot_sha256: 217f838caae373b870c71ffb974b7d830fa614ca9dbd4ca95df0076dabc33467
- evidence_id: context-audit-network
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/audit-network.json
  locator: Fresh batch16 corpus baseline
  summary: Corpus context is distinct from the target network.
  support: supports
  accessed_at: '2026-10-22T09:37:34.904196Z'
  snapshot_sha256: f4809c6a349f1496dbfe0243fb5ce661f469f7235f2aa00e6294ee3aa04f3123
- evidence_id: context-check-network-quality
  kind: validation
  reference: /private/tmp/cm-review-session/batch-16/check-network-quality.json
  locator: Fresh batch16 corpus baseline
  summary: Corpus context is distinct from the target network.
  support: supports
  accessed_at: '2026-10-22T09:37:34.904354Z'
  snapshot_sha256: 759ba13f2cda067251275491bbafc401d0be8bddf7907c7f962eb4369f61688f
assessments:
- assessment_id: identity
  area: identity
  topic: Defined isolates and host system
  outcome: supported
  summary: The record identifies the intended ring trial.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - design
  - stock-table
  - collection
  details: Seventeen named stocks form the microbial roster; Brachypodium distachyon
    is the host. DSM200000SY is a collection, not a strain identifier. Retain synthetic
    origin, engineered state and rhizosphere category.
  dimensions:
  - name: stable_id
    value: CommunityMech:000025; PMID:40920748; PMC12416739; DOI:10.1371/journal.pbio.3003358
    definition: Exact record and principal study identity.
    evidence_ids:
    - record
    - design
  - name: source_strains
    value: Seventeen stock codes in S2 and Methods 4.8; OAS925 DSM113627; collection
      DSM200000SY
    definition: Preserve stock identity independently of genus and collection names.
    evidence_ids:
    - stock-table
    - genomes
    - collection
  - name: community_scope
    value: Five-laboratory Brachypodium EcoFAB ring trial; SynCom17 versus SynCom16,
      axenic and plant-free controls
    definition: Defined inoculum, final relative community and separate single-isolate
      assays are different experimental units.
    evidence_ids:
    - design
    - outcomes
- assessment_id: nongraph
  area: evidence
  topic: Mechanism, optional roles and attribution
  outcome: concern
  summary: Non-graph claims exceed the experiments.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - outcomes
  - traits
  - trait-table
  - semantics
  details: Relative dominance does not demonstrate competitive exclusion or absolute
    extinction. Bulk spent-medium profiles do not identify OAS925-specific amino-acid
    uptake. Plant effects belong to the whole SynCom17 treatment. Three PRIMARY_DEGRADER
    tags and Methylobacterium CROSS_FEEDER need member-local support; general membership
    or exudate associations do not suffice. Preserve positive genomic potential and
    measured phenotypes without assigning untested flux or trait necessity.
- assessment_id: node-0
  area: graph
  topic: SynCom17 EcoFAB Ring-Trial Perturbation
  outcome: supported
  summary: Retain the qualified claim; align evidence tiers with assay context.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - snippets
  - design
  - cultivation
  - host
  details: 'Exact selector ecological_interactions[0]. Participants: {"participating_taxa":
    [{"preferred_term": "Paraburkholderia sp. OAS925", "term": {"id": "NCBITaxon:1822464",
    "label": "Paraburkholderia"}}, {"preferred_term": "Rhodococcus sp. OAS809", "term":
    {"id": "NCBITaxon:1827", "label": "Rhodococcus <high G+C Gram-positive bacteria>"}},
    {"preferred_term": "Mycobacterium sp. OAE908", "term": {"id": "NCBITaxon:1763",
    "label": "Mycobacterium"}}, {"preferred_term": "Methylobacterium sp. OAE515",
    "term": {"id": "NCBITaxon:407", "label": "Methylobacterium"}}, {"preferred_term":
    "Variovorax sp. OAS795", "term": {"id": "NCBITaxon:34072", "label": "Variovorax"}},
    {"preferred_term": "Rhizobium sp. OAE497", "term": {"id": "NCBITaxon:379", "label":
    "Rhizobium"}}, {"preferred_term": "Bosea sp. OAE506", "term": {"id": "NCBITaxon:85413",
    "label": "Allobosea"}}, {"preferred_term": "Bradyrhizobium sp. OAE829", "term":
    {"id": "NCBITaxon:374", "label": "Bradyrhizobium"}}, {"preferred_term": "Lysobacter
    sp. OAE881", "term": {"id": "NCBITaxon:68", "label": "Lysobacter"}}, {"preferred_term":
    "Arthrobacter sp. OAP107", "term": {"id": "NCBITaxon:1667", "label": "Arthrobacter
    sp."}}, {"preferred_term": "Marmoricola sp. OAE513", "term": {"id": "NCBITaxon:86795",
    "label": "Marmoricola"}}, {"preferred_term": "Chitinophaga sp. OAE865", "term":
    {"id": "NCBITaxon:79328", "label": "Chitinophaga"}}, {"preferred_term": "Mucilaginibacter
    sp. OAE612", "term": {"id": "NCBITaxon:423349", "label": "Mucilaginibacter"}},
    {"preferred_term": "Niastella sp. OAS944", "term": {"id": "NCBITaxon:354354",
    "label": "Niastella"}}, {"preferred_term": "Gottfriedia sp. OAE603", "term": {"id":
    "NCBITaxon:2837503", "label": "Gottfriedia"}}, {"preferred_term": "Brevibacillus
    sp. OAP136", "term": {"id": "NCBITaxon:55080", "label": "Brevibacillus"}}, {"preferred_term":
    "Paenibacillus sp. OAE614", "term": {"id": "NCBITaxon:44249", "label": "Paenibacillus"}}]}.
    Exact canonical snippet bindings: [{"selector": "ecological_interactions[0].evidence[0].snippet",
    "sha256": "063a3aeac44f41c5a36ee645a51138fdfbd64be3bd40de1acea1c7c8b30724af",
    "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.1/2.4
    and Methods 4.1–4.2; Figures 1/3. Retain the whole-community inoculation and its
    experimental contrasts; this is not a generic microbiome effect. Scope: COMMUNITY_LEVEL.'
- assessment_id: node-1
  area: graph
  topic: Paraburkholderia Acid-Tolerant Root Colonization Traits
  outcome: supported
  summary: Retain the qualified claim; align evidence tiers with assay context.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - snippets
  - traits
  - trait-table
  details: 'Exact selector ecological_interactions[1]. Participants: {"source_taxon":
    {"preferred_term": "Paraburkholderia sp. OAS925", "term": {"id": "NCBITaxon:1822464",
    "label": "Paraburkholderia"}}}. Exact canonical snippet bindings: [{"selector":
    "ecological_interactions[1].evidence[0].snippet", "sha256": "0c573b7488e6cc047517640cadfa82d519993074869f37181f4ecb5985373160",
    "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "COMPUTATIONAL"},
    {"selector": "ecological_interactions[1].evidence[1].snippet", "sha256": "e64fa9506c4a47618fab5b997d0431751f475f5631d498048bef96012a3a0e41",
    "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.7
    and Methods 4.8–4.10; SI8–11 and selected S9 rows. Retain source-only PAIRWISE
    scope for OAS925 properties. T3SS is a genomic annotation; acid-tolerant motility
    was measured separately. Individual acid-resistance genes also occur in other
    isolates, so qualify uniqueness as the combined profile or surveyed T3SS module.
    No selective gene intervention establishes necessity.'
- assessment_id: node-2
  area: graph
  topic: Paraburkholderia-Dominated SynCom17 Root Assembly
  outcome: supported
  summary: Retain the qualified claim; align evidence tiers with assay context.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - snippets
  - design
  - outcomes
  details: 'Exact selector ecological_interactions[2]. Participants: {"participating_taxa":
    [{"preferred_term": "Paraburkholderia sp. OAS925", "term": {"id": "NCBITaxon:1822464",
    "label": "Paraburkholderia"}}, {"preferred_term": "Rhodococcus sp. OAS809", "term":
    {"id": "NCBITaxon:1827", "label": "Rhodococcus <high G+C Gram-positive bacteria>"}},
    {"preferred_term": "Mycobacterium sp. OAE908", "term": {"id": "NCBITaxon:1763",
    "label": "Mycobacterium"}}, {"preferred_term": "Methylobacterium sp. OAE515",
    "term": {"id": "NCBITaxon:407", "label": "Methylobacterium"}}, {"preferred_term":
    "Variovorax sp. OAS795", "term": {"id": "NCBITaxon:34072", "label": "Variovorax"}},
    {"preferred_term": "Rhizobium sp. OAE497", "term": {"id": "NCBITaxon:379", "label":
    "Rhizobium"}}, {"preferred_term": "Bosea sp. OAE506", "term": {"id": "NCBITaxon:85413",
    "label": "Allobosea"}}, {"preferred_term": "Bradyrhizobium sp. OAE829", "term":
    {"id": "NCBITaxon:374", "label": "Bradyrhizobium"}}, {"preferred_term": "Lysobacter
    sp. OAE881", "term": {"id": "NCBITaxon:68", "label": "Lysobacter"}}, {"preferred_term":
    "Arthrobacter sp. OAP107", "term": {"id": "NCBITaxon:1667", "label": "Arthrobacter
    sp."}}, {"preferred_term": "Marmoricola sp. OAE513", "term": {"id": "NCBITaxon:86795",
    "label": "Marmoricola"}}, {"preferred_term": "Chitinophaga sp. OAE865", "term":
    {"id": "NCBITaxon:79328", "label": "Chitinophaga"}}, {"preferred_term": "Mucilaginibacter
    sp. OAE612", "term": {"id": "NCBITaxon:423349", "label": "Mucilaginibacter"}},
    {"preferred_term": "Niastella sp. OAS944", "term": {"id": "NCBITaxon:354354",
    "label": "Niastella"}}, {"preferred_term": "Gottfriedia sp. OAE603", "term": {"id":
    "NCBITaxon:2837503", "label": "Gottfriedia"}}, {"preferred_term": "Brevibacillus
    sp. OAP136", "term": {"id": "NCBITaxon:55080", "label": "Brevibacillus"}}, {"preferred_term":
    "Paenibacillus sp. OAE614", "term": {"id": "NCBITaxon:44249", "label": "Paenibacillus"}}]}.
    Exact canonical snippet bindings: [{"selector": "ecological_interactions[2].evidence[0].snippet",
    "sha256": "6a1b117f4ef0431908bbb8ad2d22cba0ac4edd413ce946b52b4c4a582f75720b",
    "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.4;
    Figure 3. Retain OAS925 relative-read dominance and its contrast with SynCom16.
    Approximately 98% reads do not establish absolute exclusion, extinction or uniform
    participant abundance. Scope: COMMUNITY_LEVEL.'
- assessment_id: node-3
  area: graph
  topic: Treatment-Structured Rhizosphere Exometabolites
  outcome: supported
  summary: Retain the qualified claim; align evidence tiers with assay context.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - snippets
  - outcomes
  details: 'Exact selector ecological_interactions[3]. Participants: {"participating_taxa":
    [{"preferred_term": "Paraburkholderia sp. OAS925", "term": {"id": "NCBITaxon:1822464",
    "label": "Paraburkholderia"}}, {"preferred_term": "Rhodococcus sp. OAS809", "term":
    {"id": "NCBITaxon:1827", "label": "Rhodococcus <high G+C Gram-positive bacteria>"}},
    {"preferred_term": "Mycobacterium sp. OAE908", "term": {"id": "NCBITaxon:1763",
    "label": "Mycobacterium"}}, {"preferred_term": "Methylobacterium sp. OAE515",
    "term": {"id": "NCBITaxon:407", "label": "Methylobacterium"}}, {"preferred_term":
    "Variovorax sp. OAS795", "term": {"id": "NCBITaxon:34072", "label": "Variovorax"}},
    {"preferred_term": "Rhizobium sp. OAE497", "term": {"id": "NCBITaxon:379", "label":
    "Rhizobium"}}, {"preferred_term": "Bosea sp. OAE506", "term": {"id": "NCBITaxon:85413",
    "label": "Allobosea"}}, {"preferred_term": "Bradyrhizobium sp. OAE829", "term":
    {"id": "NCBITaxon:374", "label": "Bradyrhizobium"}}, {"preferred_term": "Lysobacter
    sp. OAE881", "term": {"id": "NCBITaxon:68", "label": "Lysobacter"}}, {"preferred_term":
    "Arthrobacter sp. OAP107", "term": {"id": "NCBITaxon:1667", "label": "Arthrobacter
    sp."}}, {"preferred_term": "Marmoricola sp. OAE513", "term": {"id": "NCBITaxon:86795",
    "label": "Marmoricola"}}, {"preferred_term": "Chitinophaga sp. OAE865", "term":
    {"id": "NCBITaxon:79328", "label": "Chitinophaga"}}, {"preferred_term": "Mucilaginibacter
    sp. OAE612", "term": {"id": "NCBITaxon:423349", "label": "Mucilaginibacter"}},
    {"preferred_term": "Niastella sp. OAS944", "term": {"id": "NCBITaxon:354354",
    "label": "Niastella"}}, {"preferred_term": "Gottfriedia sp. OAE603", "term": {"id":
    "NCBITaxon:2837503", "label": "Gottfriedia"}}, {"preferred_term": "Brevibacillus
    sp. OAP136", "term": {"id": "NCBITaxon:55080", "label": "Brevibacillus"}}, {"preferred_term":
    "Paenibacillus sp. OAE614", "term": {"id": "NCBITaxon:44249", "label": "Paenibacillus"}}]}.
    Exact canonical snippet bindings: [{"selector": "ecological_interactions[3].evidence[0].snippet",
    "sha256": "f294df6ddcee0f73f3b016e90b0426c81b8beb6115c3e55ba8107e77fe815e4a",
    "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.5;
    Figure 4. Retain whole-treatment net bulk extracellular changes. They combine
    uptake, secretion, transformation and host effects; no taxon-specific exchange
    or consumption rate is identified. Scope: COMMUNITY_LEVEL.'
- assessment_id: node-4
  area: graph
  topic: SynCom17 Plant Biomass and Root Development Decrease
  outcome: supported
  summary: Retain the qualified claim; align evidence tiers with assay context.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - snippets
  - outcomes
  details: 'Exact selector ecological_interactions[4]. Participants: {"participating_taxa":
    [{"preferred_term": "Paraburkholderia sp. OAS925", "term": {"id": "NCBITaxon:1822464",
    "label": "Paraburkholderia"}}, {"preferred_term": "Rhodococcus sp. OAS809", "term":
    {"id": "NCBITaxon:1827", "label": "Rhodococcus <high G+C Gram-positive bacteria>"}},
    {"preferred_term": "Mycobacterium sp. OAE908", "term": {"id": "NCBITaxon:1763",
    "label": "Mycobacterium"}}, {"preferred_term": "Methylobacterium sp. OAE515",
    "term": {"id": "NCBITaxon:407", "label": "Methylobacterium"}}, {"preferred_term":
    "Variovorax sp. OAS795", "term": {"id": "NCBITaxon:34072", "label": "Variovorax"}},
    {"preferred_term": "Rhizobium sp. OAE497", "term": {"id": "NCBITaxon:379", "label":
    "Rhizobium"}}, {"preferred_term": "Bosea sp. OAE506", "term": {"id": "NCBITaxon:85413",
    "label": "Allobosea"}}, {"preferred_term": "Bradyrhizobium sp. OAE829", "term":
    {"id": "NCBITaxon:374", "label": "Bradyrhizobium"}}, {"preferred_term": "Lysobacter
    sp. OAE881", "term": {"id": "NCBITaxon:68", "label": "Lysobacter"}}, {"preferred_term":
    "Arthrobacter sp. OAP107", "term": {"id": "NCBITaxon:1667", "label": "Arthrobacter
    sp."}}, {"preferred_term": "Marmoricola sp. OAE513", "term": {"id": "NCBITaxon:86795",
    "label": "Marmoricola"}}, {"preferred_term": "Chitinophaga sp. OAE865", "term":
    {"id": "NCBITaxon:79328", "label": "Chitinophaga"}}, {"preferred_term": "Mucilaginibacter
    sp. OAE612", "term": {"id": "NCBITaxon:423349", "label": "Mucilaginibacter"}},
    {"preferred_term": "Niastella sp. OAS944", "term": {"id": "NCBITaxon:354354",
    "label": "Niastella"}}, {"preferred_term": "Gottfriedia sp. OAE603", "term": {"id":
    "NCBITaxon:2837503", "label": "Gottfriedia"}}, {"preferred_term": "Brevibacillus
    sp. OAP136", "term": {"id": "NCBITaxon:55080", "label": "Brevibacillus"}}, {"preferred_term":
    "Paenibacillus sp. OAE614", "term": {"id": "NCBITaxon:44249", "label": "Paenibacillus"}}]}.
    Exact canonical snippet bindings: [{"selector": "ecological_interactions[4].evidence[0].snippet",
    "sha256": "0a532645bb2a9f4036a42d2bd7510f27db541dd0b9fbda963f14170c67306277",
    "reference": "PMID:40920748", "supports": "SUPPORT", "evidence_source": "IN_VITRO"}].
    Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.3–2.4;
    Figure 2. Retain whole-SynCom17 plant biomass and root effects. Neither OAS925
    alone nor a specific trait was isolated as the cause. Scope: COMMUNITY_LEVEL.'
- assessment_id: edge-0-0
  area: graph
  topic: Node 0 → node 2
  outcome: supported
  summary: Retain the bounded direction.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - design
  - outcomes
  details: 'Exact selector ecological_interactions[0].downstream[0]. Source node 0:
    SynCom17 EcoFAB Ring-Trial Perturbation. Target node 2: Paraburkholderia-Dominated
    SynCom17 Root Assembly. Exact canonical edge: {"target": "Paraburkholderia-Dominated
    SynCom17 Root Assembly", "description": "SynCom17 inoculation supplied the 17-member
    community from which the OAS925-dominated root profile developed by 22 DAI. The
    SynCom16 omission comparison supports an inoculum-composition effect, not identification
    of the molecular mechanism or absolute loss of the other members."}. Edge description
    SHA256: 995b477467d8d731c00a72f52e9403fd8990ba6879811f3cd3d489b83a364ba2. Source:
    PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.4; Figure
    3. The directed effect is the whole inoculation-treatment contrast; it does not
    identify a single-member mediator.'
- assessment_id: edge-0-1
  area: graph
  topic: Node 0 → node 3
  outcome: supported
  summary: Retain the bounded direction.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - design
  - outcomes
  details: 'Exact selector ecological_interactions[0].downstream[1]. Source node 0:
    SynCom17 EcoFAB Ring-Trial Perturbation. Target node 3: Treatment-Structured Rhizosphere
    Exometabolites. Exact canonical edge: {"target": "Treatment-Structured Rhizosphere
    Exometabolites", "description": "SynCom17 inoculation altered the plant-microbe
    system and thereby changed the measured bulk spent-medium metabolite profile relative
    to the control treatments. This is a treatment-level effect; microbial versus
    plant production, uptake and extracellular enzyme activity were not separated."}.
    Edge description SHA256: 5cb971ec57720a05c47781b2985c83d973e2251f0b60a389308ff6c4f53bc370.
    Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.5;
    Figure 4. The directed effect is the whole inoculation-treatment contrast; it
    does not identify a single-member mediator.'
- assessment_id: edge-0-2
  area: graph
  topic: Node 0 → node 4
  outcome: supported
  summary: Retain the bounded direction.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - design
  - outcomes
  details: 'Exact selector ecological_interactions[0].downstream[2]. Source node 0:
    SynCom17 EcoFAB Ring-Trial Perturbation. Target node 4: SynCom17 Plant Biomass
    and Root Development Decrease. Exact canonical edge: {"target": "SynCom17 Plant
    Biomass and Root Development Decrease", "description": "The SynCom17 inoculation
    treatment reduced shoot biomass in the combined-laboratory comparison with axenic
    plants and reduced root development from 14 DAI onward. The experiment establishes
    a whole-treatment response, not OAS925-only toxicity, competition for a specific
    nutrient or one necessary member."}. Edge description SHA256: 33581f51519a7d23e12d1479bc890a7e127dee3dd5d94c473f1a27f5c35dcbec.
    Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.3–2.4;
    Figure 2. The directed effect is the whole inoculation-treatment contrast; it
    does not identify a single-member mediator.'
- assessment_id: edge-1-0
  area: graph
  topic: Node 1 → node 2
  outcome: supported
  summary: Retain the bounded direction.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - traits
  - outcomes
  details: 'Exact selector ecological_interactions[1].downstream[0]. Source node 1:
    Paraburkholderia Acid-Tolerant Root Colonization Traits. Target node 2: Paraburkholderia-Dominated
    SynCom17 Root Assembly. Exact canonical edge: {"target": "Paraburkholderia-Dominated
    SynCom17 Root Assembly", "description": "HYPOTHESIZED - acid-tolerant motility,
    colonization traits and associated genomic modules may help OAS925 establish and
    expand on roots, contributing to its relative dominance. Separate isolate assays
    and gene annotation support candidate mechanisms, but none was selectively disrupted
    or rescued in the 17-member community."}. Edge description SHA256: 05a729400915c693bfa62c4570c3c8e9c9e6db08bbbd3682247e9ba2be8b49e7.
    Source: PMID:40920748; DOI:10.1371/journal.pbio.3003358. Locator: Results 2.4;
    Figure 3 and Results 2.7; SI8–11. Trait contribution remains HYPOTHESIZED, without
    a necessity test.'
- assessment_id: graph-topology
  area: graph
  topic: Five nodes and four directed claims
  outcome: supported
  summary: No topology repair is required.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - record
  - support
  - source-audit
  details: Four COMMUNITY_LEVEL nodes and one source-only PAIRWISE node have no interaction_type.
    Three arrows originate at node 0 and one HYPOTHESIZED arrow at node 1. Retain
    the explicit limits and current discussion.
- assessment_id: cultivation
  area: scope
  topic: Study, preparation and host-growth separation
  outcome: concern
  summary: Current conditions mix distinct experiments.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - cultivation
  - host
  - stock-table
  - protocol
  - nitrogen
  details: Ring-trial seedlings had three days stratification, three days germination
    and four days in EcoFAB before inoculation. The 27 C, 200 rpm reporter preparation
    and three-day seedling assay are separate; motility precultures also used 200
    rpm at 27 C. The earlier sterile nitrogen experiment is not a SynCom17 nitrogen/light
    intervention.
  dimensions:
  - name: environment
    value: ENVO:01001405 laboratory environment; Brachypodium root-associated culture
    definition: Broad environment is valid; laboratory deviations must remain explicit.
    evidence_ids:
    - host
    - ontology
  - name: medium
    value: Half-MS host medium; stock-specific R2A, 1/10 R2A or LB before washing
    definition: S2 lists Rhizobium, Bradyrhizobium, Mycobacterium and Niastella in
      1/10 R2A, Gottfriedia in LB; other stocks use R2A. Protocol half-MS is 2.165
      g/L, pH 5.7.
    evidence_ids:
    - stock-table
    - cultivation
    - protocol
  - name: experimental_setting
    value: EcoFAB 2.0; 9 mL half-MS plus 1 mL diluted inoculum; harvest 22 DAI
    definition: Default 14 h light at 26 C/10 h dark at 20 C, laboratory C 16 h light;
      PPFD 110–140 and humidity 70% only if tunable. Preparation, genomic-DNA and
      reporter assays remain separate.
    evidence_ids:
    - host
    - protocol
- assessment_id: grounding
  area: grounding
  topic: Rank refinement and reproducible GTDB provenance
  outcome: concern
  summary: Grounding cores are reproducible; OAP107 rank and release wording need
    bounded repair.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - ontology
  - rank
  - gtdb
  - semantics
  details: Encoded NCBITaxon:1667 is an explicitly unresolved unnamed-species placeholder.
    Source-linked OAP107 metadata supports genus NCBITaxon:1663, without resolving
    its species or strain-level GTDB. Fifteen mapping cores reproduce, including curated
    Allobosea to legacy Bosea 34/34. Preserve Paenibacillus ambiguity. A filesystem
    date does not establish a GTDB release or build date.
  dimensions:
  - name: taxon_grounding
    value: 'Seventeen NCBI entries: sixteen genus-level names plus unresolved Arthrobacter
      sp. 1667; host NCBITaxon:15368'
    definition: OAP107 genus candidate 1663 is source-linked; genus votes do not identify
      isolates. Retain verified Allobosea 85413 and unresolved/ambiguous boundaries.
    evidence_ids:
    - record
    - ontology
    - rank
    - gtdb
- assessment_id: evidence
  area: evidence
  topic: Exact excerpts and assay-local tiers
  outcome: concern
  summary: All 30 snippets match, but several placements are broader than their source
    support.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - snippets
  - cultivation
  - outcomes
  - traits
  - nitrogen
  details: Use S2 and Methods 4.8 for exact stock identities rather than repeating
    a generic membership abstract. Living-host colonization and plant outcomes need
    IN_VIVO scope; genomic annotations need COMPUTATIONAL, and separate isolate phenotype
    assays remain IN_VITRO. Exact lexical matches do not prove stronger causal interpretations.
  dimensions:
  - name: evidence_tier
    value: Host experiments, separate isolate assays and genomic predictions
    definition: Retain IN_VIVO, IN_VITRO and COMPUTATIONAL distinctions at the narrowest
      claim; no blanket tier replacement.
    evidence_ids:
    - semantics
    - outcomes
    - traits
- assessment_id: resources
  area: evidence
  topic: Actual study resources and genome identifiers
  outcome: concern
  summary: Five encoded study resources resolve; the genome pseudo-range is incomplete.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - resources
  - data
  - genomes
  - stock-table
  details: PRJNA1151037, GNPS task, MSV000095476, NMDC study and Figshare collection
    identify the ring trial. Gp0588949-Gp0589682 is not the exact 17-project set and
    excludes Mycobacterium Gp0440934. Keep IMG taxon identifiers distinct from NCBITaxon;
    metadata is not functional validation.
- assessment_id: coverage
  area: scope
  topic: Source access and prior context
  outcome: supported
  summary: The main claims have complete scientific assessment with bounded SI scope.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - assets
  - read-scope
  - provenance
  - root-source
  - support
  details: Lead read both main scientific texts, all principal main/SI figures, all
    related main figures and selected S1/S2/S9 cells. Root independently read the
    protocol and complete Markdown caches; support read the complete third PMC cache.
    Videos, bulk numerical matrices and raw omics were not reanalyzed. Current issue
    1424 is closed; 1427 remains open; the historical Allobosea repair is retained.
- assessment_id: validation
  area: schema
  topic: Native checks and actual limits
  outcome: supported
  summary: Eight required checks passed; no native failure.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - auxiliary
  - support
  - adapter
  details: Deterministic success does not certify causal support. Optional adapter
    unavailability, a truncated package and auxiliary extraction/writer errors are
    preserved separately from native checks.
- assessment_id: metrics
  area: completeness
  topic: Two literal review scores
  outcome: supported
  summary: Completeness 45; quality 100 after capping raw 103.
  target_ids:
  - CommunityMech:000025
  evidence_ids:
  - support
  metrics:
  - name: completeness
    value: 45
    minimum: 0
    maximum: 100
    unit: points
    definition: 0 required-fields-and-all-roles +5 environment +10 factors +10 nodes
      +0 external resources +10 medium +5 datasets +5 node metabolites =45. Only four
      of seventeen taxa have roles; do not invent roles for scoring.
  - name: validation_quality
    value: 100
    minimum: 0
    maximum: 100
    unit: points
    definition: 100 -10*2 -2*2 +20*min((6/5)/2,1) +15 =103, capped at100. Six excerpts
      across five nodes; evidence bonus12 and COMPLETE structural bonus15.
  - name: P1
    value: 0
    unit: findings
    definition: Native severity count.
  - name: P2
    value: 2
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
- finding_id: causal-role-evidence
  issue_key: cm-000025-causal-role-evidence
  category: evidence
  severity: major
  native_severity: P2
  normalization_reason: These assertions change biological mechanism and experimental
    meaning, despite the correctly qualified graph.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Separate treatment outcomes from member-level mechanisms
  description: Competitive exclusion, OAS925-specific uptake/plant harm and optional
    member roles exceed the demonstrated claims; evidence tiers mix host, isolate
    and genomic contexts.
  target_ids:
  - CommunityMech:000025
  field_paths:
  - description
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  - taxonomy[2].functional_role
  - taxonomy[3].functional_role
  - taxonomy[0].taxon_term.notes
  - engineering_design.measurement_endpoints
  - engineering_design.evidence[0]
  - related_ingredients[0].relevance
  - ecological_interactions[0].evidence[0].evidence_source
  - ecological_interactions[1].evidence[1].evidence_source
  - ecological_interactions[2].evidence[0].evidence_source
  - ecological_interactions[3].evidence[0].evidence_source
  - ecological_interactions[4].evidence[0].evidence_source
  evidence_ids:
  - outcomes
  - traits
  - stock-table
  - trait-table
  - nitrogen
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    role: canonical_record
- finding_id: study-stage-scope
  issue_key: cm-000025-study-stage-scope
  category: scope
  severity: major
  native_severity: P2
  normalization_reason: The pooled fields misdescribe the experimental design and
    conditions needed to reproduce it.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Separate ring-trial conditions from related studies and assays
  description: Nitrogen/light interventions and reporter preparation conditions are
    pooled with the ring trial.
  target_ids:
  - CommunityMech:000025
  field_paths:
  - engineering_design.perturbation_design
  - engineering_design.notes
  - environment_term.notes
  - environmental_factors[0]
  - environmental_factors[1]
  - growth_media[0]
  evidence_ids:
  - cultivation
  - host
  - protocol
  - stock-table
  - nitrogen
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    role: canonical_record
- finding_id: grounding-provenance
  issue_key: cm-000025-grounding-provenance
  category: grounding
  severity: minor
  native_severity: P3
  normalization_reason: Stock identity is explicit and other mapping cores reproduce,
    so this is a bounded metadata correction.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Refine OAP107 rank and mapping provenance
  description: The unresolved OAP107 placeholder can be refined using source-linked
    genus metadata; latest/build assertions exceed file provenance.
  target_ids:
  - CommunityMech:000025
  field_paths:
  - taxonomy[9].taxon_term
  - ecological_interactions[0].participating_taxa[9].term
  - ecological_interactions[2].participating_taxa[9].term
  - ecological_interactions[3].participating_taxa[9].term
  - ecological_interactions[4].participating_taxa[9].term
  - taxonomy[0].taxon_term.gtdb_classification.mapping_source
  - taxonomy[1].taxon_term.gtdb_classification.mapping_source
  - taxonomy[2].taxon_term.gtdb_classification.mapping_source
  - taxonomy[3].taxon_term.gtdb_classification.mapping_source
  - taxonomy[4].taxon_term.gtdb_classification.mapping_source
  - taxonomy[5].taxon_term.gtdb_classification.mapping_source
  - taxonomy[6].taxon_term.gtdb_classification.mapping_source
  - taxonomy[7].taxon_term.gtdb_classification.mapping_source
  - taxonomy[8].taxon_term.gtdb_classification.mapping_source
  - taxonomy[10].taxon_term.gtdb_classification.mapping_source
  - taxonomy[11].taxon_term.gtdb_classification.mapping_source
  - taxonomy[12].taxon_term.gtdb_classification.mapping_source
  - taxonomy[13].taxon_term.gtdb_classification.mapping_source
  - taxonomy[14].taxon_term.gtdb_classification.mapping_source
  - taxonomy[15].taxon_term.gtdb_classification.mapping_source
  evidence_ids:
  - rank
  - gtdb
  - semantics
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    role: canonical_record
- finding_id: genome-identifiers
  issue_key: cm-000025-genome-identifiers
  category: evidence
  severity: minor
  native_severity: P3
  normalization_reason: Public collection identity and data availability are recoverable;
    no wrong-study or raw-data finding is implied.
  rule_id: review-checklist.claim-specific-support-and-context
  status: open
  certainty: confirmed
  title: Replace the genome pseudo-range with exact identifiers
  description: The range omits Gp0440934 and does not enumerate all 17 source projects.
  target_ids:
  - CommunityMech:000025
  field_paths:
  - associated_datasets[5]
  evidence_ids:
  - resources
  - genomes
  - stock-table
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    role: canonical_record
actions:
- action_id: repair-causal-scope
  description: Align member claims and evidence with actual assays.
  finding_ids:
  - causal-role-evidence
  target_ids:
  - CommunityMech:000025
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    role: canonical_record
  acceptance_checks:
  - Qualify competitive exclusion and member-specific uptake as hypotheses; attribute
    plant effects to SynCom17 treatment. Preserve relative abundance and net extracellular
    measurements without assigning absolute exclusion or taxon-specific flux.
  - Omit unsupported optional PRIMARY_DEGRADER/CROSS_FEEDER tags or attach isolate-local
    support with the correct predicted versus demonstrated scope. Preserve positive
    genomic capabilities; do not impose a polymer-only definition or infer physiological
    inability.
  - Use exact stock evidence from S2/Methods 4.8. Correct host-associated evidence
    to IN_VIVO, genomic annotation to COMPUTATIONAL and separate isolate assays to
    IN_VITRO where applicable.
  - Retain five nodes and four arrows; retain HYPOTHESIZED trait mediation. Distinguish
    the combined acid-resistance profile from uniqueness of individual genes or T3SS
    signature; do not assert trait necessity or uniquely highest OAS925 biomass.
- action_id: repair-study-stages
  description: Represent each protocol and perturbation in its own study context.
  finding_ids:
  - study-stage-scope
  target_ids:
  - CommunityMech:000025
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    role: canonical_record
  acceptance_checks:
  - Remove nitrogen/light factorial claims from the ring-trial design. Retain the
    earlier sterile nitrogen study only as separately attributed context.
  - Separate S2 stock preparation, genomic DNA culture, RFP-isolate microscopy, motility
    precultures and host cultivation. Preserve stock-specific media and distinct shaking/temperature
    values.
  - Use ten-day ring-trial seedlings, 9 mL half-MS plus 1 mL inoculum, default 14
    h/10 h light-dark and laboratory C deviation, and 22 DAI harvest; preserve the
    source theoretical inoculum and freeze-thaw assumptions. Keep protocol pH5.7 versus
    main5.5–6.0 appropriately attributed.
- action_id: repair-grounding-provenance
  description: Use bounded source-linked rank and reproducible map provenance.
  finding_ids:
  - grounding-provenance
  target_ids:
  - CommunityMech:000025
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    role: canonical_record
  acceptance_checks:
  - Use verified Arthrobacter genus NCBITaxon:1663 for OAP107 at taxonomy[9] and its
    four participant placements if applying the source-linked refinement. Preserve
    stock code and species uncertainty; re-evaluate GTDB status without selecting
    one of eleven genus candidates arbitrarily.
  - Retain the fifteen valid numerical cores, curated Allobosea85413/Bosea34-of-34
    mapping and Paenibacillus ambiguity. Replace unsupported latest/build wording
    with mapping file identity, hash and method; filesystem mtime is not release metadata.
- action_id: repair-genome-identifiers
  description: Represent exact source genome identifiers and verify the curated record.
  finding_ids:
  - genome-identifiers
  target_ids:
  - CommunityMech:000025
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/EcoFAB_Ring_Trial_SynCom17.yaml
    role: canonical_record
  acceptance_checks:
  - Replace the pseudo-range with the source genome collection and/or all 17 explicit
    strain-to-IMG/GOLD pairs from Methods 4.8/S2, including OAE908 Gp0440934. Preserve
    namespaces and actual assembly scope.
  - After separately authorized curation, rerun schema, strict, ontology, reference,
    GTDB, domain and history checks; recheck graph participants. Regenerate HTML with
    just gen-html and run just check-docs-current.
limitations:
- Relative reads, bulk metabolite profiles, isolate phenotypes and genome annotations
  do not establish member-specific flux or trait necessity.
- Source laboratory/timing differences remain explicit. S1 laboratory E logger date
  and endpoint labels are not silently harmonized.
- Principal videos, settings and response files were inventoried but not inspected;
  other numerical workbooks were not exhaustively read. Related nitrogen SI text was
  read only through character8000, with no SI pixel claim.
- No raw genome, sequencing, metabolomic or video reanalysis. The timed-out principal
  package is a failed retrieval; genuine direct publisher assets supplied the assessed
  figures and tables.
- Optional structured runner unavailable; this is not negative gene evidence or an
  unavailable required check. Auxiliary construction/extraction failures are distinct
  from zero native failures.
notes:
- Exact inspection source/target arrays and actual command types preserved. Thirty
  strict snippet matches, six node bindings, four exact edge-description hashes and
  eight evidence-linked dimensions.
- This review proposes curation only; no canonical, cache, history or Git change.
tags:
- record-review
- ecofab
- rhizosphere
- batch-16
```
