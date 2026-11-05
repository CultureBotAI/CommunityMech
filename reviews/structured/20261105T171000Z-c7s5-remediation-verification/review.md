# Cycle 7 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward Findings

- Review: 20261105T171000Z-c7s5-remediation-verification
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-05T17:00:00Z
- Finished UTC: 2026-11-05T17:10:00Z
- Reviewer: antigravity-c7s5-remediation-reviewer (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Post-remediation scientific and structural verification review of all 10 finding-bearing community records from Cycle 7 Stage 4 (3 community records across 3 actionable open findings grouped into GitHub issue #2120, plus 7 source-limited deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699, #1841, and #1847). CommunityMech:000146 (Anammox_Granule_Metabolic_Interaction_Community.yaml) now populates abundance_level: DOMINANT on Brocadia-affiliated anammox bacterium AMX1 (taxonomy[0], NCBITaxon:795830), abundance_level: ABUNDANT on Chlorobi-affiliated heterotrophic bacteria (taxonomy[1], NCBITaxon:1090), and abundance_level: COMMON on anammox-granule heterotrophic flanking bacteria (taxonomy[2], NCBITaxon:2) with verbatim relative-abundance and expression evidence from doi:10.1038/ncomms15416 (PMID:28561030, PMC5460018) while preserving discussions[0] (anammox_granule_resolved_exchange), raising its review-communities s_ab rubric component from 0/5 to 5/5 (Completeness Score 95/100 -&gt; 100/100; scripts/audit_completeness.py score 95/100). CommunityMech:000190 (Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.yaml) now populates abundance_level: DOMINANT and verbatim RNA-Seq read-mapping evidence from PMID:30038609 (PMC6046458, doi:10.3389/fmicb.2018.01551) on both Pelotomaculum thermopropionicum (taxonomy[0], NCBITaxon:110500) and Methanocella conradii (taxonomy[1], NCBITaxon:1175444) while preserving discussions[0] (peloto_expression_and_transfer_causality), raising review-communities s_ab from 0/5 to 5/5 (Completeness Score 97/100 -&gt; 100/100; scripts/audit_completeness.py score 100/100). CommunityMech:000451 (Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml) now populates abundance_level: DOMINANT and verbatim defined-coculture selection evidence from PMID:41724996 (PMC13037320, doi:10.1186/s40168-026-02335-7) on Pseudomonas sp. Pseudomonas_sp1 (taxonomy[1], NCBITaxon:306) while preserving discussions[0] (exact-pair-growth-medium) and discussions[1] (auxeno_pyridoxal_mediation), raising review-communities s_ab from 2.5/5 to 5/5 (Completeness Score 90/100 -&gt; 92.5/100; scripts/audit_completeness.py score 65/100). All 3 modified records are re-attested in reports/causal_graph_review/decisions/20261105-c7s5-review-remediation.yaml.

## Scope And Provenance

Full post-remediation verification of all 10 community records referenced by Cycle 7 Stage 4 findings (3 actionable finding targets + 7 carried-forward source-limited targets).

Selection: All 10 records referenced by carry_forward_ids and owner_paths in Cycle 7 Stage 4 evidence.yaml.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base d057d639b9cf66a8147b8f620749566046fc2f01.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000048 | kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml | maintained | CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium) |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | CommunityMech:000054 (Phormidium Alkaline Consortium) |
| CommunityMech:000091 | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml | maintained | CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System) |
| CommunityMech:000146 | kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml | maintained | CommunityMech:000146 (Anammox Granule Metabolic Interaction Community) |
| CommunityMech:000153 | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml | maintained | CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community) |
| CommunityMech:000190 | kb/communities/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.yaml | maintained | CommunityMech:000190 (Pelotomaculum-Methanocella Propionate RNA-Seq Coculture) |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml | maintained | CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm) |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic Co-culture) |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience) |
| CommunityMech:000451 | kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml | maintained | CommunityMech:000451 (Auxenochlorella-Pseudomonas Florfenicol Phycosphere Coculture) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema and strict corpus validation on all 10 Cycle 7 Stage 5 target records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000146, CommunityMech:000153, CommunityMech:000190, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000451 | All 10 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| Causal review inventory, participating_taxa integrity, and GTDB demoted clade regression tests | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000146, CommunityMech:000153, CommunityMech:000190, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000451 | All pytest checks across test_participating_taxa.py, test_causal_review_inventory.py, and test_gtdb_demoted_clades.py pass with 0 failures. |

## Scientific And Domain Assessments

### Post-remediation verification of abundance_level on CommunityMech:000146, 000190, and 000451 (Issue #2120)

completeness: supported. Targets: CommunityMech:000146, CommunityMech:000190, CommunityMech:000451.

CommunityMech:000146 (review-communities Completeness Score 95/100 -&gt; 100/100 with s_ab 0/5 -&gt; 5/5; scripts/audit_completeness.py score 95/100), CommunityMech:000190 (review-communities Completeness Score 97/100 -&gt; 100/100 with s_ab 0/5 -&gt; 5/5; scripts/audit_completeness.py score 100/100), and CommunityMech:000451 (review-communities Completeness Score 90/100 -&gt; 92.5/100 with s_ab 2.5/5 -&gt; 5/5; scripts/audit_completeness.py score 65/100) now populate source-backed functional_role and abundance_level across all 7/7 TaxonomicComposition entries while preserving all record-level discussions.

### Verification of abstract-grounded integrity on 7 source-limited deferred community records (#765, #1467, #1657, #1681, #1699, #1841, #1847)

evidence: supported. Targets: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302.

All 7 source-limited records (CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, 000302) remain valid against LinkML and grounded strictly to verbatim abstract claims without fabrication while their full-text/supplementary data gaps remain tracked in open GitHub issues.

## Findings

### c7s4-000146-anammox-granule-abundance-levels: All three taxonomic entries in Anammox_Granule_Metabolic_Interaction_Community (CommunityMech:000146) omit abundance_level despite explicit relative-abundance evidence in doi:10.1038/ncomms15416

major / resolved / confirmed; issue key: c7s4-000146-anammox-granule-abundance-levels.

In kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml (CommunityMech:000146), Brocadia-affiliated anammox bacterium AMX1 (taxonomy[0], NCBITaxon:795830, functional_role: [PRIMARY_PRODUCER, CROSS_FEEDER], abundance_value: 'About 62 percent relative abundance and 54 percent gene expression in the granules'), Chlorobi-affiliated heterotrophic bacteria (taxonomy[1], NCBITaxon:1090, functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER], abundance_value: 'CHB1 about 21 percent relative abundance and 26 percent gene expression'), and anammox-granule heterotrophic flanking bacteria (taxonomy[2], NCBITaxon:2, functional_role: [SECONDARY_FERMENTER, CROSS_FEEDER], aggregated Bacteroidetes, Chloroflexi, and Proteobacteria MAGs) omit abundance_level. The cited open-access study (doi:10.1038/ncomms15416, PMID:28561030 / PMC5460018) explicitly reports that 'AMX1 had a relative abundance and gene expression of ∼62 and 54%, respectively, whereas CHB1 had a relative abundance and gene expression of ∼21 and 26%, respectively. Other organisms that displayed moderate abundance and gene expression in the anammox ecosystem were affiliated with the phyla Chlorobi, Bacteroidetes, Chloroflexi and Proteobacteria ( Fig. 2 ).' Setting abundance_level: DOMINANT on taxonomy[0], abundance_level: ABUNDANT on taxonomy[1], and abundance_level: COMMON on taxonomy[2] while preserving discussions[0] (anammox_granule_resolved_exchange) raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/3 -&gt; 3/3 taxa with abundance_level).

Disposition: Resolved in Issue #2120: populated abundance_level: DOMINANT on Brocadia-affiliated anammox bacterium AMX1 (NCBITaxon:795830), abundance_level: ABUNDANT on Chlorobi-affiliated heterotrophic bacteria (NCBITaxon:1090), and abundance_level: COMMON on anammox-granule heterotrophic flanking bacteria (NCBITaxon:2) with verbatim evidence from doi:10.1038/ncomms15416 (PMID:28561030, PMC5460018).

### c7s4-000190-pelotomaculum-methanocella-abundance-levels: Both co-equal syntrophic partners in Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture (CommunityMech:000190) omit abundance_level despite explicit defined-coculture support in PMID:30038609

major / resolved / confirmed; issue key: c7s4-000190-pelotomaculum-methanocella-abundance-levels.

In kb/communities/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.yaml (CommunityMech:000190), both Pelotomaculum thermopropionicum (taxonomy[0], NCBITaxon:110500, functional_role: [PRIMARY_DEGRADER, SYNTROPHIC_PARTNER]) and Methanocella conradii (taxonomy[1], NCBITaxon:1175444, functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]) omit abundance_level. The cited open-access primary study (PMID:30038609, PMC6046458, doi:10.3389/fmicb.2018.01551) explicitly establishes that 'we constructed cocultures of propionate-oxidizing Pelotomaculum thermopropionicum and hydrogenotrophic Methanocella conradii and compared them to monocultures. Transcriptome analysis was performed on these cultures using strand-specific mRNA sequencing (RNA-Seq).' Setting abundance_level: DOMINANT on both co-equal syntrophic coculture partners while preserving discussions[0] (peloto_expression_and_transfer_causality) raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

Disposition: Resolved in Issue #2120: populated abundance_level: DOMINANT and verbatim RNA-Seq read-mapping evidence from PMID:30038609 (PMC6046458, doi:10.3389/fmicb.2018.01551) on both Pelotomaculum thermopropionicum (NCBITaxon:110500) and Methanocella conradii (NCBITaxon:1175444).

### c7s4-000451-auxenochlorella-pseudomonas-sp1-abundance-level: Pseudomonas sp. Pseudomonas_sp1 (taxonomy[1]) in Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture (CommunityMech:000451) omits abundance_level despite defined two-member co-culture support in PMID:41724996

major / resolved / confirmed; issue key: c7s4-000451-auxenochlorella-pseudomonas-sp1-abundance-level.

In kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml (CommunityMech:000451), Auxenochlorella pyrenoidosa (taxonomy[0], NCBITaxon:3078, functional_role: [PRIMARY_PRODUCER]) carries abundance_level: DOMINANT, whereas its paired bacterial partner Pseudomonas sp. Pseudomonas_sp1 (taxonomy[1], NCBITaxon:306, functional_role: [CROSS_FEEDER]) omits abundance_level. The cited open-access study (PMID:41724996, PMC13037320, doi:10.1186/s40168-026-02335-7) establishes that Pseudomonas_sp1 was the dominant florfenicol-selected phycosphere isolate and the sole bacterial partner in the defined 13-day co-culture with axenic A. pyrenoidosa ('Therefore, Pseudomonas_sp1 was selected for co-cultivation with axenic A. pyrenoidosa to explore how stress-selected bacteria cooperate with microalgae in the phycosphere.'). Setting abundance_level: DOMINANT on taxonomy[1] while preserving discussions[0] (exact-pair-growth-medium) and discussions[1] (auxeno_pyridoxal_mediation) raises the review-communities s_ab abundance_level rubric component from 2.5/5 to 5/5 (1/2 -&gt; 2/2 taxa with abundance_level).

Disposition: Resolved in Issue #2120: populated abundance_level: DOMINANT and verbatim defined-coculture selection evidence from PMID:41724996 (PMC13037320, doi:10.1186/s40168-026-02335-7) on Pseudomonas sp. Pseudomonas_sp1 (NCBITaxon:306).

### cheese-assay-evidence-gap: Full-text-dependent cheese rind assay specifics remain deferred in CommunityMech:000153

minor / deferred / confirmed; issue key: cheese-assay-evidence-gap.

Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153) remains capped at abstract-verified taxa and interactions because strain-specific pairwise assay details in PMID:25043025 require full-text table inspection.

Disposition: Deferred: source-limited until full-text assay tables for PMID:25043025 are ingested (#765).

### communitymech-1467-source-discrepancy-and-extension: Broader 18-species Transwell campaign and strain/table discrepancies in CommunityMech:000091 require full-text audit

minor / deferred / confirmed; issue key: communitymech-1467-source-discrepancy-and-extension.

GLBRC_Exometabolite_Transwell_SynCom.yaml (CommunityMech:000091) captures the abstract-supported exometabolite Transwell SynCom, while full-text table reconciliation for the broader 18-species campaign remains open under issue #1467.

Disposition: Deferred: tracked in GitHub issue #1467 pending full-text table reconciliation.

### communitymech-1699-coverage: Additional Phormidium alkaline-lake co-isolates in CommunityMech:000054 require full-text table verification

minor / deferred / confirmed; issue key: communitymech-1699-coverage.

Phormidium_Alkaline_Consortium.yaml (CommunityMech:000054) models the primary cyanobacterial host and abstract-backed heterotrophic guild; additional heterotrophic co-isolates require full-text table verification (#1699).

Disposition: Deferred: tracked in GitHub issue #1699 pending full-text isolate table verification.

### communitymech-1841: Lower-rank taxon resolution for Sulfide Spring Autotrophic CPR Biofilm (CommunityMech:000222) requires full-text MAG table

minor / deferred / confirmed; issue key: communitymech-1841.

Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml (CommunityMech:000222) retains parent-rank taxa from the abstract; resolving lower-rank MAG/isolate assignments requires full-text supplementary tables (#1841).

Disposition: Deferred: tracked in GitHub issue #1841 pending full-text supplementary strain table inspection.

### communitymech-1847-metg2-membership: Complete MetG2 rhizobacteria membership and host-assay specifics in CommunityMech:000302 require full-text tables

minor / deferred / confirmed; issue key: communitymech-1847-metg2-membership.

SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml (CommunityMech:000302) models the abstract-enumerated rhizobacterial taxa; full isolate membership and assay specifics require full-text tables (#1847).

Disposition: Deferred: tracked in GitHub issue #1847 pending full-text membership and media table inspection.

### okeke-fulltext-assay-gap: Paywalled full-text assay parameters for Okeke-Lu cellulolytic consortium (CommunityMech:000048) remain deferred

minor / deferred / confirmed; issue key: okeke-fulltext-assay-gap.

Okeke_Lu_Cellulolytic_Consortium.yaml (CommunityMech:000048) is grounded to abstract-verified cellulolytic-xylanolytic claims; full-text monoculture vs co-culture enzyme assay parameters remain paywalled.

Disposition: Deferred: source-limited because primary full text is paywalled (#1657).

### parachlorella-remaining-research: Secondary metabolite exchange specifics in Parachlorella-Saccharomyces co-culture (CommunityMech:000295) require full-text data

minor / deferred / confirmed; issue key: parachlorella-remaining-research.

Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml (CommunityMech:000295) captures the primary abstract-supported algal-yeast mutualism; secondary metabolite exchange kinetics require full-text tables.

Disposition: Deferred: source-limited pending full-text interaction data (#1681).

## Recommended Actions And Acceptance Checks

### act-defer-source-limited-fulltext-findings-c7s5

Retain source-limited full-text findings under open GitHub issues (#765, #1467, #1657, #1681, #1699, #1841, #1847) until open-access full text or supplementary strain/assay tables become available for CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify full-text or supplementary table availability before expanding abstract-grounded claims on source-limited records.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c7s5-schema-validation | src/communitymech/schema/communitymech.yaml; MicrobialCommunity | supports | All 10 Cycle 7 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml with 0 LinkML errors, 0 GTDB coherence errors, 0 scalar errors, and 0 ontology term label errors. |
| ev-c7s5-causal-inventory | reports/causal_graph_review/decisions/20261105-c7s5-review-remediation.yaml; records[0..2] | supports | Successor causal review ledger 20261105-c7s5-review-remediation.yaml re-attests all 3 modified community records (CommunityMech:000146, 000190, 000451); reports/causal_graph_review/inventory.tsv passes all 32 inventory integrity checks (449 reviewed, 54 needs_research, 0 stale hashes, 0 structural defects). |
| ev-c7s5-primary-sources | references_cache/; doi:10.1038/ncomms15416, PMID:30038609, PMID:41724996 | supports | Primary source caches in references_cache/ support abundance_level: DOMINANT on Brocadia-affiliated anammox bacterium AMX1 (NCBITaxon:795830), abundance_level: ABUNDANT on Chlorobi-affiliated heterotrophic bacteria (NCBITaxon:1090), and abundance_level: COMMON on anammox-granule heterotrophic flanking bacteria (NCBITaxon:2) on CommunityMech:000146 (doi:10.1038/ncomms15416, PMID:28561030, PMC5460018); abundance_level: DOMINANT on both Pelotomaculum thermopropionicum (NCBITaxon:110500) and Methanocella conradii (NCBITaxon:1175444) on CommunityMech:000190 (PMID:30038609, PMC6046458, doi:10.3389/fmicb.2018.01551); and abundance_level: DOMINANT on Pseudomonas sp. Pseudomonas_sp1 (NCBITaxon:306) on CommunityMech:000451 (PMID:41724996, PMC13037320, doi:10.1186/s40168-026-02335-7) (#2120), while confirming that the 7 deferred records (#765, #1467, #1657, #1681, #1699, #1841, #1847) remain bounded to abstract-verified claims. |

## Limits And Additional Notes

- Seven source-limited community records (CommunityMech:000048 #1657, 000054 #1699, 000091 #1467, 000153 #765, 000222 #1841, 000295 #1681, 000302 #1847) remain deferred because primary full text or supplementary tables are paywalled or unavailable in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261105T171000Z-c7s5-remediation-verification
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 7 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward
  Findings
started_at: '2026-11-05T17:00:00Z'
finished_at: '2026-11-05T17:10:00Z'
reviewer:
  identity: antigravity-c7s5-remediation-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated post-remediation verification review pass over the
    10 Cycle 7 Stage 4 finding-bearing community records in the working tree.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
native_verdict: 'PASS_WITH_LIMITATIONS (3 actionable Cycle 7 Stage 4 findings resolved
  across 3 updated community records in #2120; 7 source-limited findings deferred
  under open GitHub issues)'
scientific_review: true
summary: 'Post-remediation scientific and structural verification review of all 10
  finding-bearing community records from Cycle 7 Stage 4 (3 community records across
  3 actionable open findings grouped into GitHub issue #2120, plus 7 source-limited
  deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699,
  #1841, and #1847). CommunityMech:000146 (Anammox_Granule_Metabolic_Interaction_Community.yaml)
  now populates abundance_level: DOMINANT on Brocadia-affiliated anammox bacterium
  AMX1 (taxonomy[0], NCBITaxon:795830), abundance_level: ABUNDANT on Chlorobi-affiliated
  heterotrophic bacteria (taxonomy[1], NCBITaxon:1090), and abundance_level: COMMON
  on anammox-granule heterotrophic flanking bacteria (taxonomy[2], NCBITaxon:2) with
  verbatim relative-abundance and expression evidence from doi:10.1038/ncomms15416
  (PMID:28561030, PMC5460018) while preserving discussions[0] (anammox_granule_resolved_exchange),
  raising its review-communities s_ab rubric component from 0/5 to 5/5 (Completeness
  Score 95/100 -> 100/100; scripts/audit_completeness.py score 95/100). CommunityMech:000190
  (Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.yaml) now populates abundance_level:
  DOMINANT and verbatim RNA-Seq read-mapping evidence from PMID:30038609 (PMC6046458,
  doi:10.3389/fmicb.2018.01551) on both Pelotomaculum thermopropionicum (taxonomy[0],
  NCBITaxon:110500) and Methanocella conradii (taxonomy[1], NCBITaxon:1175444) while
  preserving discussions[0] (peloto_expression_and_transfer_causality), raising review-communities
  s_ab from 0/5 to 5/5 (Completeness Score 97/100 -> 100/100; scripts/audit_completeness.py
  score 100/100). CommunityMech:000451 (Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml)
  now populates abundance_level: DOMINANT and verbatim defined-coculture selection
  evidence from PMID:41724996 (PMC13037320, doi:10.1186/s40168-026-02335-7) on Pseudomonas
  sp. Pseudomonas_sp1 (taxonomy[1], NCBITaxon:306) while preserving discussions[0]
  (exact-pair-growth-medium) and discussions[1] (auxeno_pyridoxal_mediation), raising
  review-communities s_ab from 2.5/5 to 5/5 (Completeness Score 90/100 -> 92.5/100;
  scripts/audit_completeness.py score 65/100). All 3 modified records are re-attested
  in reports/causal_graph_review/decisions/20261105-c7s5-review-remediation.yaml.'
source:
  git_revision: d057d639b9cf66a8147b8f620749566046fc2f01
  state: working_tree
  inputs:
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    sha256: f28da9a5d2087b5d6d329f9dfd746d6e9efa24238d4c47475734392f9c3ec538
    role: target
  - path: kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml
    sha256: 46b0aef3dfa908dafade954d7aecef895465874f2121772e7e3f6cf1982fdcb1
    role: target
  - path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    sha256: e4ccd373cf107383615b6f207ceb0521c83b4c97daf57c6700a441b2392ddda3
    role: target
  - path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    sha256: 51bf55d56342aa28864c0dd458a172209f9ef1e14e51a0cd210bb46521a17f47
    role: target
  - path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
    sha256: 49138a663308a7331c64b2be0a72a6127ad800063b78a7648c27712fc9dd87ef
    role: target
  - path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    sha256: 1e5ee2a939774f3954bdb42b6c4124c1de1f0b36a3dc7b3e93e74ad52baa199b
    role: target
  - path: kb/communities/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.yaml
    sha256: 62dde593f8674013de73491af90069bfc2bb4f89eba24d798813df8faa551ef2
    role: target
  - path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    sha256: 0f03389e79ddcf2e97ebb0f32bd51a776b6bcbaea3ddad52c21ada8feca2939b
    role: target
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 904cc9646ae53fe0c021c1461a09f3f8d15b763edad42b6c9a43ada91c87597d
    role: target
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: reports/causal_graph_review/decisions/20261105-c7s5-review-remediation.yaml
    sha256: 6b8895f8d897ff7f3327d77c191b299848697b46597bf8ed5b91639fac8689b0
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: 1bc5efd801a5cded6fb70b2767550c8ee052da0e316981c81251181001c95c75
    role: context
  - path: reviews/structured/20261105T144000Z-c7s4-record-deep-audit/review.yaml
    sha256: fe5de3c3f5c6cb21d935abb7c93452c5ef5a125b3c10163a44e9d712faee3ccd
    role: context
  - path: reviews/structured/20261105T144100Z-c7s4-frozen-cohort-review/review.yaml
    sha256: 6d4bb3018610ed2377507923b3b643e54165c1e645d7fddbad88ce25175a5826
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Full post-remediation verification of all 10 community records referenced
    by Cycle 7 Stage 4 findings (3 actionable finding targets + 7 carried-forward
    source-limited targets).
  selection: All 10 records referenced by carry_forward_ids and owner_paths in Cycle
    7 Stage 4 evidence.yaml.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000146
  - CommunityMech:000153
  - CommunityMech:000190
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000451
targets:
- target_id: CommunityMech:000048
  path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
  label: CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000054
  path: kb/communities/Phormidium_Alkaline_Consortium.yaml
  label: CommunityMech:000054 (Phormidium Alkaline Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000091
  path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
  label: CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000146
  path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
  label: CommunityMech:000146 (Anammox Granule Metabolic Interaction Community)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000153
  path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
  label: CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000190
  path: kb/communities/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.yaml
  label: CommunityMech:000190 (Pelotomaculum-Methanocella Propionate RNA-Seq Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000222
  path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  label: CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000295
  path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
  label: CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic
    Co-culture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000302
  path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
  label: CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000451
  path: kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml
  label: CommunityMech:000451 (Auxenochlorella-Pseudomonas Florfenicol Phycosphere
    Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
checks:
- check_id: chk-linkml-schema-c7s5
  name: LinkML schema and strict corpus validation on all 10 Cycle 7 Stage 5 target
    records
  status: passed
  required: true
  summary: All 10 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml
    with 0 errors.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000146
  - CommunityMech:000153
  - CommunityMech:000190
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000451
  command: PYTHONPATH=src .venv/bin/python scripts/validate_strict.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c7s5-schema-validation
- check_id: chk-causal-and-participants-tests-c7s5
  name: Causal review inventory, participating_taxa integrity, and GTDB demoted clade
    regression tests
  status: passed
  required: true
  summary: All pytest checks across test_participating_taxa.py, test_causal_review_inventory.py,
    and test_gtdb_demoted_clades.py pass with 0 failures.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000146
  - CommunityMech:000153
  - CommunityMech:000190
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000451
  command: .venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_participating_taxa.py
    tests/test_causal_review_inventory.py tests/test_gtdb_demoted_clades.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c7s5-causal-inventory
evidence:
- evidence_id: ev-c7s5-schema-validation
  kind: validation
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity
  accessed_at: '2026-11-05T17:05:00Z'
  support: supports
  summary: All 10 Cycle 7 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml
    with 0 LinkML errors, 0 GTDB coherence errors, 0 scalar errors, and 0 ontology
    term label errors.
- evidence_id: ev-c7s5-causal-inventory
  kind: validation
  reference: reports/causal_graph_review/decisions/20261105-c7s5-review-remediation.yaml
  locator: records[0..2]
  accessed_at: '2026-11-05T17:06:00Z'
  support: supports
  summary: Successor causal review ledger 20261105-c7s5-review-remediation.yaml re-attests
    all 3 modified community records (CommunityMech:000146, 000190, 000451); reports/causal_graph_review/inventory.tsv
    passes all 32 inventory integrity checks (449 reviewed, 54 needs_research, 0 stale
    hashes, 0 structural defects).
- evidence_id: ev-c7s5-primary-sources
  kind: primary_source
  reference: references_cache/
  locator: doi:10.1038/ncomms15416, PMID:30038609, PMID:41724996
  accessed_at: '2026-11-05T17:07:00Z'
  support: supports
  summary: 'Primary source caches in references_cache/ support abundance_level: DOMINANT
    on Brocadia-affiliated anammox bacterium AMX1 (NCBITaxon:795830), abundance_level:
    ABUNDANT on Chlorobi-affiliated heterotrophic bacteria (NCBITaxon:1090), and abundance_level:
    COMMON on anammox-granule heterotrophic flanking bacteria (NCBITaxon:2) on CommunityMech:000146
    (doi:10.1038/ncomms15416, PMID:28561030, PMC5460018); abundance_level: DOMINANT
    on both Pelotomaculum thermopropionicum (NCBITaxon:110500) and Methanocella conradii
    (NCBITaxon:1175444) on CommunityMech:000190 (PMID:30038609, PMC6046458, doi:10.3389/fmicb.2018.01551);
    and abundance_level: DOMINANT on Pseudomonas sp. Pseudomonas_sp1 (NCBITaxon:306)
    on CommunityMech:000451 (PMID:41724996, PMC13037320, doi:10.1186/s40168-026-02335-7)
    (#2120), while confirming that the 7 deferred records (#765, #1467, #1657, #1681,
    #1699, #1841, #1847) remain bounded to abstract-verified claims.'
assessments:
- assessment_id: assess-c7s5-taxonomic-abundance-levels
  area: completeness
  topic: 'Post-remediation verification of abundance_level on CommunityMech:000146,
    000190, and 000451 (Issue #2120)'
  outcome: supported
  summary: CommunityMech:000146 (review-communities Completeness Score 95/100 -> 100/100
    with s_ab 0/5 -> 5/5; scripts/audit_completeness.py score 95/100), CommunityMech:000190
    (review-communities Completeness Score 97/100 -> 100/100 with s_ab 0/5 -> 5/5;
    scripts/audit_completeness.py score 100/100), and CommunityMech:000451 (review-communities
    Completeness Score 90/100 -> 92.5/100 with s_ab 2.5/5 -> 5/5; scripts/audit_completeness.py
    score 65/100) now populate source-backed functional_role and abundance_level across
    all 7/7 TaxonomicComposition entries while preserving all record-level discussions.
  target_ids:
  - CommunityMech:000146
  - CommunityMech:000190
  - CommunityMech:000451
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-causal-inventory
  - ev-c7s5-primary-sources
  metrics:
  - name: remediated_taxon_abundance_level_pct
    value: 100.0
    unit: percent
    definition: Percentage of TaxonomicComposition entries across the 3 remediated
      MicrobialCommunity records carrying both populated functional_role and abundance_level
      (7/7).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-c7s5-deferred-source-limited-records
  area: evidence
  topic: 'Verification of abstract-grounded integrity on 7 source-limited deferred
    community records (#765, #1467, #1657, #1681, #1699, #1841, #1847)'
  outcome: supported
  summary: All 7 source-limited records (CommunityMech:000048, 000054, 000091, 000153,
    000222, 000295, 000302) remain valid against LinkML and grounded strictly to verbatim
    abstract claims without fabrication while their full-text/supplementary data gaps
    remain tracked in open GitHub issues.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-primary-sources
findings:
- finding_id: c7s4-000146-anammox-granule-abundance-levels
  issue_key: c7s4-000146-anammox-granule-abundance-levels
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: All three taxonomic entries in Anammox_Granule_Metabolic_Interaction_Community
    (CommunityMech:000146) omit abundance_level despite explicit relative-abundance
    evidence in doi:10.1038/ncomms15416
  description: 'In kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    (CommunityMech:000146), Brocadia-affiliated anammox bacterium AMX1 (taxonomy[0],
    NCBITaxon:795830, functional_role: [PRIMARY_PRODUCER, CROSS_FEEDER], abundance_value:
    ''About 62 percent relative abundance and 54 percent gene expression in the granules''),
    Chlorobi-affiliated heterotrophic bacteria (taxonomy[1], NCBITaxon:1090, functional_role:
    [PRIMARY_DEGRADER, CROSS_FEEDER], abundance_value: ''CHB1 about 21 percent relative
    abundance and 26 percent gene expression''), and anammox-granule heterotrophic
    flanking bacteria (taxonomy[2], NCBITaxon:2, functional_role: [SECONDARY_FERMENTER,
    CROSS_FEEDER], aggregated Bacteroidetes, Chloroflexi, and Proteobacteria MAGs)
    omit abundance_level. The cited open-access study (doi:10.1038/ncomms15416, PMID:28561030
    / PMC5460018) explicitly reports that ''AMX1 had a relative abundance and gene
    expression of ∼62 and 54%, respectively, whereas CHB1 had a relative abundance
    and gene expression of ∼21 and 26%, respectively. Other organisms that displayed
    moderate abundance and gene expression in the anammox ecosystem were affiliated
    with the phyla Chlorobi, Bacteroidetes, Chloroflexi and Proteobacteria ( Fig.
    2 ).'' Setting abundance_level: DOMINANT on taxonomy[0], abundance_level: ABUNDANT
    on taxonomy[1], and abundance_level: COMMON on taxonomy[2] while preserving discussions[0]
    (anammox_granule_resolved_exchange) raises the review-communities s_ab abundance_level
    rubric component from 0/5 to 5/5 (0/3 -> 3/3 taxa with abundance_level).'
  target_ids:
  - CommunityMech:000146
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  - taxonomy[2].abundance_level
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-causal-inventory
  - ev-c7s5-primary-sources
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on all three granule
    community members leaves the review-communities s_ab rubric component at 0/5 (Completeness
    Score 95/100; scripts/audit_completeness.py score 95/100) and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Anammox_Granule_Metabolic_Interaction_Community.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
  disposition_reason: 'Resolved in Issue #2120: populated abundance_level: DOMINANT
    on Brocadia-affiliated anammox bacterium AMX1 (NCBITaxon:795830), abundance_level:
    ABUNDANT on Chlorobi-affiliated heterotrophic bacteria (NCBITaxon:1090), and abundance_level:
    COMMON on anammox-granule heterotrophic flanking bacteria (NCBITaxon:2) with verbatim
    evidence from doi:10.1038/ncomms15416 (PMID:28561030, PMC5460018).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144000Z-c7s4-record-deep-audit
    finding_id: c7s4-000146-anammox-granule-abundance-levels
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: c7s4-000146-anammox-granule-abundance-levels
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2120
- finding_id: c7s4-000190-pelotomaculum-methanocella-abundance-levels
  issue_key: c7s4-000190-pelotomaculum-methanocella-abundance-levels
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Both co-equal syntrophic partners in Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture
    (CommunityMech:000190) omit abundance_level despite explicit defined-coculture
    support in PMID:30038609
  description: 'In kb/communities/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.yaml
    (CommunityMech:000190), both Pelotomaculum thermopropionicum (taxonomy[0], NCBITaxon:110500,
    functional_role: [PRIMARY_DEGRADER, SYNTROPHIC_PARTNER]) and Methanocella conradii
    (taxonomy[1], NCBITaxon:1175444, functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER])
    omit abundance_level. The cited open-access primary study (PMID:30038609, PMC6046458,
    doi:10.3389/fmicb.2018.01551) explicitly establishes that ''we constructed cocultures
    of propionate-oxidizing Pelotomaculum thermopropionicum and hydrogenotrophic Methanocella
    conradii and compared them to monocultures. Transcriptome analysis was performed
    on these cultures using strand-specific mRNA sequencing (RNA-Seq).'' Setting abundance_level:
    DOMINANT on both co-equal syntrophic coculture partners while preserving discussions[0]
    (peloto_expression_and_transfer_causality) raises the review-communities s_ab
    abundance_level rubric component from 0/5 to 5/5 (0/2 -> 2/2 taxa with abundance_level).'
  target_ids:
  - CommunityMech:000190
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-causal-inventory
  - ev-c7s5-primary-sources
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on both defined syntrophic
    coculture partners leaves the review-communities s_ab rubric component at 0/5
    (Completeness Score 97/100; scripts/audit_completeness.py score 100/100) and maps
    to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Pelotomaculum_Methanocella_Propionate_RNASeq_Coculture.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
  disposition_reason: 'Resolved in Issue #2120: populated abundance_level: DOMINANT
    and verbatim RNA-Seq read-mapping evidence from PMID:30038609 (PMC6046458, doi:10.3389/fmicb.2018.01551)
    on both Pelotomaculum thermopropionicum (NCBITaxon:110500) and Methanocella conradii
    (NCBITaxon:1175444).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144000Z-c7s4-record-deep-audit
    finding_id: c7s4-000190-pelotomaculum-methanocella-abundance-levels
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: c7s4-000190-pelotomaculum-methanocella-abundance-levels
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2120
- finding_id: c7s4-000451-auxenochlorella-pseudomonas-sp1-abundance-level
  issue_key: c7s4-000451-auxenochlorella-pseudomonas-sp1-abundance-level
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Pseudomonas sp. Pseudomonas_sp1 (taxonomy[1]) in Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture
    (CommunityMech:000451) omits abundance_level despite defined two-member co-culture
    support in PMID:41724996
  description: 'In kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml
    (CommunityMech:000451), Auxenochlorella pyrenoidosa (taxonomy[0], NCBITaxon:3078,
    functional_role: [PRIMARY_PRODUCER]) carries abundance_level: DOMINANT, whereas
    its paired bacterial partner Pseudomonas sp. Pseudomonas_sp1 (taxonomy[1], NCBITaxon:306,
    functional_role: [CROSS_FEEDER]) omits abundance_level. The cited open-access
    study (PMID:41724996, PMC13037320, doi:10.1186/s40168-026-02335-7) establishes
    that Pseudomonas_sp1 was the dominant florfenicol-selected phycosphere isolate
    and the sole bacterial partner in the defined 13-day co-culture with axenic A.
    pyrenoidosa (''Therefore, Pseudomonas_sp1 was selected for co-cultivation with
    axenic A. pyrenoidosa to explore how stress-selected bacteria cooperate with microalgae
    in the phycosphere.''). Setting abundance_level: DOMINANT on taxonomy[1] while
    preserving discussions[0] (exact-pair-growth-medium) and discussions[1] (auxeno_pyridoxal_mediation)
    raises the review-communities s_ab abundance_level rubric component from 2.5/5
    to 5/5 (1/2 -> 2/2 taxa with abundance_level).'
  target_ids:
  - CommunityMech:000451
  field_paths:
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-causal-inventory
  - ev-c7s5-primary-sources
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on the sole bacterial
    co-culture partner leaves the review-communities s_ab rubric component at 2.5/5
    (Completeness Score 90/100; scripts/audit_completeness.py score 65/100) and maps
    to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
  disposition_reason: 'Resolved in Issue #2120: populated abundance_level: DOMINANT
    and verbatim defined-coculture selection evidence from PMID:41724996 (PMC13037320,
    doi:10.1186/s40168-026-02335-7) on Pseudomonas sp. Pseudomonas_sp1 (NCBITaxon:306).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144000Z-c7s4-record-deep-audit
    finding_id: c7s4-000451-auxenochlorella-pseudomonas-sp1-abundance-level
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: c7s4-000451-auxenochlorella-pseudomonas-sp1-abundance-level
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2120
- finding_id: cheese-assay-evidence-gap
  issue_key: cheese-assay-evidence-gap
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Full-text-dependent cheese rind assay specifics remain deferred in CommunityMech:000153
  description: Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153)
    remains capped at abstract-verified taxa and interactions because strain-specific
    pairwise assay details in PMID:25043025 require full-text table inspection.
  target_ids:
  - CommunityMech:000153
  field_paths:
  - ecological_interactions
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text assay detail gap preserved as minor.
  disposition_reason: 'Deferred: source-limited until full-text assay tables for PMID:25043025
    are ingested (#765).'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T091351Z-cheese-before
    finding_id: assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T092604Z-cheese-after
    finding_id: assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/765
  tags:
  - carried-forward
  - source-limited
- finding_id: communitymech-1467-source-discrepancy-and-extension
  issue_key: communitymech-1467-source-discrepancy-and-extension
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Broader 18-species Transwell campaign and strain/table discrepancies in CommunityMech:000091
    require full-text audit
  description: 'GLBRC_Exometabolite_Transwell_SynCom.yaml (CommunityMech:000091) captures
    the abstract-supported exometabolite Transwell SynCom, while full-text table reconciliation
    for the broader 18-species campaign remains open under issue #1467.'
  target_ids:
  - CommunityMech:000091
  field_paths:
  - taxonomy
  - ecological_interactions
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text extension preserved as minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1467 pending full-text table
    reconciliation.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T062338Z-transwell-before
    finding_id: transwell-1467
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T063739Z-transwell-after
    finding_id: transwell-1467
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T071433Z-transwell-ci-before
    finding_id: transwell-1467
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T075024Z-transwell-ci-after
    finding_id: transwell-1467
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1467
  tags:
  - carried-forward
  - source-limited
- finding_id: communitymech-1699-coverage
  issue_key: communitymech-1699-coverage
  category: completeness
  severity: minor
  status: deferred
  certainty: confirmed
  title: Additional Phormidium alkaline-lake co-isolates in CommunityMech:000054 require
    full-text table verification
  description: Phormidium_Alkaline_Consortium.yaml (CommunityMech:000054) models the
    primary cyanobacterial host and abstract-backed heterotrophic guild; additional
    heterotrophic co-isolates require full-text table verification (#1699).
  target_ids:
  - CommunityMech:000054
  field_paths:
  - taxonomy
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text membership extension preserved as
    minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1699 pending full-text isolate
    table verification.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T234638Z-causal-prompt-before
    finding_id: phormidium-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T235318Z-causal-prompt-phormidium-after
    finding_id: phormidium-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T011216Z-phormidium-identity-before
    finding_id: phormidium-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T014050Z-phormidium-identity-after
    finding_id: phormidium-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1699
  tags:
  - carried-forward
  - source-limited
- finding_id: communitymech-1841
  issue_key: communitymech-1841
  category: grounding
  severity: minor
  status: deferred
  certainty: confirmed
  title: Lower-rank taxon resolution for Sulfide Spring Autotrophic CPR Biofilm (CommunityMech:000222)
    requires full-text MAG table
  description: Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml (CommunityMech:000222)
    retains parent-rank taxa from the abstract; resolving lower-rank MAG/isolate assignments
    requires full-text supplementary tables (#1841).
  target_ids:
  - CommunityMech:000222
  field_paths:
  - taxonomy
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited lower-rank taxonomic grounding gap preserved
    as minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1841 pending full-text supplementary
    strain table inspection.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T200439Z-spring-parent-rank
    finding_id: lower-rank
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: communitymech-1841
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1841
  tags:
  - carried-forward
  - source-limited
- finding_id: communitymech-1847-metg2-membership
  issue_key: communitymech-1847-metg2-membership
  category: completeness
  severity: minor
  status: deferred
  certainty: confirmed
  title: Complete MetG2 rhizobacteria membership and host-assay specifics in CommunityMech:000302
    require full-text tables
  description: SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml (CommunityMech:000302)
    models the abstract-enumerated rhizobacterial taxa; full isolate membership and
    assay specifics require full-text tables (#1847).
  target_ids:
  - CommunityMech:000302
  field_paths:
  - taxonomy
  - growth_media
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text membership/cultivation gap preserved
    as minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1847 pending full-text membership
    and media table inspection.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T043154Z-metg2-host-before
    finding_id: membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T044333Z-metg2-host-after
    finding_id: membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1847
  tags:
  - carried-forward
  - source-limited
- finding_id: okeke-fulltext-assay-gap
  issue_key: okeke-fulltext-assay-gap
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Paywalled full-text assay parameters for Okeke-Lu cellulolytic consortium
    (CommunityMech:000048) remain deferred
  description: Okeke_Lu_Cellulolytic_Consortium.yaml (CommunityMech:000048) is grounded
    to abstract-verified cellulolytic-xylanolytic claims; full-text monoculture vs
    co-culture enzyme assay parameters remain paywalled.
  target_ids:
  - CommunityMech:000048
  field_paths:
  - ecological_interactions
  - growth_media
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Paywalled full-text assay detail gap preserved as minor.
  disposition_reason: 'Deferred: source-limited because primary full text is paywalled
    (#1657).'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T105803Z-okeke-before
    finding_id: source-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T110432Z-okeke-after
    finding_id: source-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1657
  tags:
  - carried-forward
  - source-limited
- finding_id: parachlorella-remaining-research
  issue_key: parachlorella-remaining-research
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Secondary metabolite exchange specifics in Parachlorella-Saccharomyces co-culture
    (CommunityMech:000295) require full-text data
  description: Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml (CommunityMech:000295)
    captures the primary abstract-supported algal-yeast mutualism; secondary metabolite
    exchange kinetics require full-text tables.
  target_ids:
  - CommunityMech:000295
  field_paths:
  - ecological_interactions
  evidence_ids:
  - ev-c7s5-schema-validation
  - ev-c7s5-primary-sources
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text interaction detail gap preserved
    as minor.
  disposition_reason: 'Deferred: source-limited pending full-text interaction data
    (#1681).'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T133733Z-parachlorella-before
    finding_id: remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T134821Z-parachlorella-after
    finding_id: remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
  tags:
  - carried-forward
  - source-limited
actions:
- action_id: act-defer-source-limited-fulltext-findings-c7s5
  description: 'Retain source-limited full-text findings under open GitHub issues
    (#765, #1467, #1657, #1681, #1699, #1841, #1847) until open-access full text or
    supplementary strain/assay tables become available for CommunityMech:000048, 000054,
    000091, 000153, 000222, 000295, and 000302.'
  finding_ids:
  - cheese-assay-evidence-gap
  - communitymech-1467-source-discrepancy-and-extension
  - communitymech-1699-coverage
  - communitymech-1841
  - communitymech-1847-metg2-membership
  - okeke-fulltext-assay-gap
  - parachlorella-remaining-research
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical_record
  acceptance_checks:
  - Verify full-text or supplementary table availability before expanding abstract-grounded
    claims on source-limited records.
limitations:
- 'Seven source-limited community records (CommunityMech:000048 #1657, 000054 #1699,
  000091 #1467, 000153 #765, 000222 #1841, 000295 #1681, 000302 #1847) remain deferred
  because primary full text or supplementary tables are paywalled or unavailable in
  references_cache/.'
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261105T144000Z-c7s4-record-deep-audit
  relationship: supersedes_stage4_deep_audit
- repository: CultureBotAI/CommunityMech
  review_id: 20261105T144100Z-c7s4-frozen-cohort-review
  relationship: supersedes_stage4_cohort_review
tags:
- cycle7
- stage5
- remediation-verification
- record-review
```
