# Cycle 5 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward Findings

- Review: 20261104T060000Z-c5s5-remediation-verification
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-04T05:50:00Z
- Finished UTC: 2026-11-04T06:00:00Z
- Reviewer: antigravity-c5s5-remediation-reviewer (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Post-remediation scientific and structural verification review of all 10 finding-bearing community records from Cycle 5 Stage 4 (3 community records across 3 actionable open findings grouped into GitHub issue #2105, plus 7 source-limited deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699, #1841, and #1847). CommunityMech:000084 (SMutans_SSputigena_ECC_Pathobiont.yaml) now populates functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: ABUNDANT on Streptococcus mutans (NCBITaxon:1309), functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] on Selenomonas sputigena (NCBITaxon:69823), and environmental_factors for 1% (w/v) sucrose supplementation in BHIS medium (value: 1% (w/v)) per PMID:37217495 (doi:10.1038/s41467-023-38346-3), raising proportional Completeness Score from 80 to 95/100 (and scripts/audit_completeness.py score from 15 to 80/100). CommunityMech:000085 (SMutans_VParvula_ASC_Biofilm.yaml) now populates functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: ABUNDANT on Streptococcus mutans (NCBITaxon:1309), functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] on Veillonella parvula (NCBITaxon:29466, retaining pre-existing abundance_level: DOMINANT), and environmental_factors for 1% (w/v) sucrose supplementation in BHI broth (value: 1% (w/v)) per PMID:39345197, raising proportional Completeness Score from 80 to 95/100 (and scripts/audit_completeness.py score from 15 to 80/100). CommunityMech:000385 (SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml) now populates functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] on engineered ethanol-detoxifying and riboflavin-synthesizing Bacillus subtilis 168 BS3 (NCBITaxon:1423, Bacillus subtilis, retaining pre-existing abundance_level: ABUNDANT alongside Shewanella oneidensis MR-1 SO3, NCBITaxon:70863) per PMID:42733304 (doi:10.1002/advs.77699), raising proportional Completeness Score from 90 to 98/100 (and scripts/audit_completeness.py score from 20 to 70/100). All 3 modified records are re-attested in reports/causal_graph_review/decisions/20261104-c5s5-review-remediation.yaml.

## Scope And Provenance

Full post-remediation verification of all 10 community records referenced by Cycle 5 Stage 4 findings (3 actionable finding targets + 7 carried-forward source-limited targets).

Selection: All 10 records referenced by carry_forward_ids and owner_paths in Cycle 5 Stage 4 evidence.yaml.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base bedd8140895e43ae3aa7765664db6b6e7f1995ff.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000048 | kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml | maintained | CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium) |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | CommunityMech:000054 (Phormidium Alkaline Consortium) |
| CommunityMech:000084 | kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml | maintained | CommunityMech:000084 (Streptococcus mutans - Selenomonas sputigena ECC Pathobiont Model) |
| CommunityMech:000085 | kb/communities/SMutans_VParvula_ASC_Biofilm.yaml | maintained | CommunityMech:000085 (Streptococcus mutans - Veillonella parvula ASC Biofilm Co-culture) |
| CommunityMech:000091 | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml | maintained | CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System) |
| CommunityMech:000153 | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml | maintained | CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community) |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml | maintained | CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm) |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic Co-culture) |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience) |
| CommunityMech:000385 | kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml | maintained | CommunityMech:000385 (SO3-BS3 Lithium-Ion Battery Bioleaching Consortium) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema and strict corpus validation on all 10 Cycle 5 Stage 5 target records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000084, CommunityMech:000085, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000385 | All 10 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| Causal review inventory, participating_taxa integrity, and batch regression tests | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000084, CommunityMech:000085, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000385 | All pytest checks across test_participating_taxa.py, test_causal_review_inventory.py, and test_causal_review_batch97.py pass with 0 failures. |

## Scientific And Domain Assessments

### Post-remediation verification of functional_role, abundance_level, and environmental_factors on CommunityMech:000084, 000085, and 000385 (Issue #2105)

completeness: supported. Targets: CommunityMech:000084, CommunityMech:000085, CommunityMech:000385.

CommunityMech:000084 (proportional Completeness Score 80 -&gt; 95/100; scripts/audit_completeness.py score 15 -&gt; 80/100), CommunityMech:000085 (proportional Completeness Score 80 -&gt; 95/100; scripts/audit_completeness.py score 15 -&gt; 80/100), and CommunityMech:000385 (proportional Completeness Score 90 -&gt; 98/100; scripts/audit_completeness.py score 20 -&gt; 70/100) now populate source-backed functional_role on all 6/6 TaxonomicComposition entries (and source-backed abundance_level on all 5/6 entries where categorical abundance is supported by the source), plus source-backed environmental_factors on all 3 records.

### Verification of abstract-grounded integrity on 7 source-limited deferred community records (#765, #1467, #1657, #1681, #1699, #1841, #1847)

evidence: supported. Targets: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302.

All 7 source-limited records (CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, 000302) remain valid against LinkML and grounded strictly to verbatim abstract claims without fabrication while their full-text/supplementary data gaps remain tracked in open GitHub issues.

## Findings

### c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose: Streptococcus mutans - Selenomonas sputigena ECC Pathobiont Model (CommunityMech:000084) omits source-backed functional_role and ABUNDANT abundance_level on Streptococcus mutans, functional_role on Selenomonas sputigena, and environmental_factors for 1% (w/v) sucrose supplementation in BHIS medium

major / resolved / confirmed; issue key: communitymech-c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose.

CommunityMech:000084 (kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml, proportional Completeness Score 80/100; scripts/audit_completeness.py score 15/100) models the two-species cariogenic dental biofilm of Streptococcus mutans (NCBITaxon:1309) and Selenomonas sputigena (NCBITaxon:69823) in early childhood caries (PMID:37217495, doi:10.1038/s41467-023-38346-3). In taxonomy, Streptococcus mutans omits functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: ABUNDANT, and Selenomonas sputigena omits functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER], despite verbatim support in PMID:37217495 showing that the biofilm core near the centroid consists predominantly of S. mutans while S. sputigena becomes trapped in streptococcal exoglucans and engages in a co-metabolic relationship that increases acid production rate. In addition, environmental_factors is absent despite PMID:37217495 establishing 1% (w/v) sucrose supplementation in BHIS medium (107 CFU/mL for the new species and/or 105 CFU/mL S. mutans).

Disposition: Resolved in Issue #2105: populated functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: ABUNDANT on Streptococcus mutans (NCBITaxon:1309), functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] on Selenomonas sputigena (NCBITaxon:69823), and environmental_factors for 1% (w/v) sucrose supplementation in BHIS medium (value: 1% (w/v)) per PMID:37217495 (doi:10.1038/s41467-023-38346-3).

### c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose: Streptococcus mutans - Veillonella parvula ASC Biofilm Co-culture (CommunityMech:000085) omits source-backed functional_role and ABUNDANT abundance_level on Streptococcus mutans, functional_role on Veillonella parvula, and environmental_factors for 1% (w/v) sucrose supplementation in BHI broth

major / resolved / confirmed; issue key: communitymech-c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose.

CommunityMech:000085 (kb/communities/SMutans_VParvula_ASC_Biofilm.yaml, proportional Completeness Score 80/100; scripts/audit_completeness.py score 15/100) models the dual-species cariogenic biofilm of Streptococcus mutans (NCBITaxon:1309) and Veillonella parvula (NCBITaxon:29466) associated with active secondary caries (PMID:39345197). In taxonomy, Streptococcus mutans omits functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: ABUNDANT, and Veillonella parvula omits functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] (while carrying abundance_level: DOMINANT), despite verbatim support in PMID:39345197 showing S. mutans GTF-mediated sucrose metabolism into water-insoluble glucan EPS, significantly increased relative abundance among the 30 most predominant species in the HC group, and V. parvula promotion of S. mutans mature biofilm formation with enhanced acid resistance and hydrogen peroxide detoxicity. In addition, environmental_factors is absent despite PMID:39345197 establishing 1% (w/v) sucrose supplementation in BHI broth for mono- and dual-species biofilms grown on saliva-coated hydroxyapatite slides at 37 °C for 24 h.

Disposition: Resolved in Issue #2105: populated functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: ABUNDANT on Streptococcus mutans (NCBITaxon:1309), functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] on Veillonella parvula (NCBITaxon:29466), and environmental_factors for 1% (w/v) sucrose supplementation in BHI broth (value: 1% (w/v)) per PMID:39345197.

### c5s4-000385-so3-bs3-bsubtilis-functional-role: SO3-BS3 Lithium-Ion Battery Bioleaching Consortium (CommunityMech:000385) omits source-backed functional_role on engineered ethanol-detoxifying and riboflavin-synthesizing Bacillus subtilis 168 BS3

major / resolved / confirmed; issue key: communitymech-c5s4-000385-so3-bs3-bsubtilis-functional-role.

CommunityMech:000385 (kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml, proportional Completeness Score 90/100; scripts/audit_completeness.py score 20/100) models the engineered two-species consortium of Shewanella oneidensis MR-1 SO3 (NCBITaxon:70863, Shewanella oneidensis) and Bacillus subtilis 168 BS3 (NCBITaxon:1423, Bacillus subtilis) in Moutai brewing wastewater for reductive bioleaching of spent LiNi1/3Co1/3Mn1/3O2 (NCM) lithium-ion battery cathodes (PMID:42733304, doi:10.1002/advs.77699). While Shewanella oneidensis MR-1 SO3 (taxonomy[0]) carries functional_role: [ELECTROGEN, ELECTRON_DONOR] and abundance_level: ABUNDANT, Bacillus subtilis 168 BS3 (taxonomy[1], carrying abundance_level: ABUNDANT) omits functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] despite verbatim support in PMID:42733304 showing that strain BS3 eliminates ethanol inhibition on S. oneidensis EET by converting residual ethanol into acetate via the Adh-AldH dual enzyme cascade and synthesizes riboflavin as an electron shuttle promoting S. oneidensis EET.

Disposition: Resolved in Issue #2105: populated functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] on Bacillus subtilis 168 BS3 (NCBITaxon:1423, Bacillus subtilis, taxonomy[1]) with verbatim IN_VITRO evidence from PMID:42733304 (doi:10.1002/advs.77699).

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

### act-defer-source-limited-fulltext-findings-c5s5

Retain source-limited full-text findings under open GitHub issues (#765, #1467, #1657, #1681, #1699, #1841, #1847) until open-access full text or supplementary strain/assay tables become available for CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify full-text or supplementary table availability before expanding abstract-grounded claims on source-limited records.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c5s5-schema-validation | src/communitymech/schema/communitymech.yaml; MicrobialCommunity | supports | All 10 Cycle 5 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml with 0 LinkML errors, 0 GTDB coherence errors, 0 scalar errors, and 0 ontology term label errors. |
| ev-c5s5-causal-inventory | reports/causal_graph_review/decisions/20261104-c5s5-review-remediation.yaml; records[0..2] | supports | Successor causal review ledger 20261104-c5s5-review-remediation.yaml re-attests all 3 modified community records (CommunityMech:000084, 000085, 000385); reports/causal_graph_review/inventory.tsv passes all 32 inventory integrity checks (436 reviewed, 54 needs_research, 0 stale hashes, 0 structural defects). |
| ev-c5s5-primary-sources | references_cache/; PMID:37217495, PMID:39345197, PMID:42733304 | supports | Primary source caches in references_cache/ support PRIMARY_DEGRADER/CROSS_FEEDER and ABUNDANT on Streptococcus mutans (NCBITaxon:1309), SYNTROPHIC_PARTNER/CROSS_FEEDER on Selenomonas sputigena (NCBITaxon:69823), and 1% (w/v) sucrose supplementation in BHIS medium on CommunityMech:000084 (PMID:37217495, doi:10.1038/s41467-023-38346-3); PRIMARY_DEGRADER/CROSS_FEEDER and ABUNDANT on Streptococcus mutans (NCBITaxon:1309), SYNTROPHIC_PARTNER/CROSS_FEEDER on Veillonella parvula (NCBITaxon:29466), and 1% (w/v) sucrose supplementation in BHI broth on CommunityMech:000085 (PMID:39345197); and SYNTROPHIC_PARTNER/CROSS_FEEDER on Bacillus subtilis 168 BS3 (NCBITaxon:1423, Bacillus subtilis) on CommunityMech:000385 (PMID:42733304, doi:10.1002/advs.77699) (#2105), while confirming that the 7 deferred records (#765, #1467, #1657, #1681, #1699, #1841, #1847) remain bounded to abstract-verified claims. |

## Limits And Additional Notes

- Seven source-limited community records (CommunityMech:000048 #1657, 000054 #1699, 000091 #1467, 000153 #765, 000222 #1841, 000295 #1681, 000302 #1847) remain deferred because primary full text or supplementary tables are paywalled or unavailable in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T060000Z-c5s5-remediation-verification
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 5 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward
  Findings
started_at: '2026-11-04T05:50:00Z'
finished_at: '2026-11-04T06:00:00Z'
reviewer:
  identity: antigravity-c5s5-remediation-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated post-remediation verification review pass over the
    10 Cycle 5 Stage 4 finding-bearing community records in the working tree.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
native_verdict: 'PASS_WITH_LIMITATIONS (3 actionable Cycle 5 Stage 4 findings resolved
  across 3 updated community records in #2105; 7 source-limited findings deferred
  under open GitHub issues)'
scientific_review: true
summary: 'Post-remediation scientific and structural verification review of all 10
  finding-bearing community records from Cycle 5 Stage 4 (3 community records across
  3 actionable open findings grouped into GitHub issue #2105, plus 7 source-limited
  deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699,
  #1841, and #1847). CommunityMech:000084 (SMutans_SSputigena_ECC_Pathobiont.yaml)
  now populates functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level:
  ABUNDANT on Streptococcus mutans (NCBITaxon:1309), functional_role: [SYNTROPHIC_PARTNER,
  CROSS_FEEDER] on Selenomonas sputigena (NCBITaxon:69823), and environmental_factors
  for 1% (w/v) sucrose supplementation in BHIS medium (value: 1% (w/v)) per PMID:37217495
  (doi:10.1038/s41467-023-38346-3), raising proportional Completeness Score from 80
  to 95/100 (and scripts/audit_completeness.py score from 15 to 80/100). CommunityMech:000085
  (SMutans_VParvula_ASC_Biofilm.yaml) now populates functional_role: [PRIMARY_DEGRADER,
  CROSS_FEEDER] and abundance_level: ABUNDANT on Streptococcus mutans (NCBITaxon:1309),
  functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] on Veillonella parvula (NCBITaxon:29466,
  retaining pre-existing abundance_level: DOMINANT), and environmental_factors for
  1% (w/v) sucrose supplementation in BHI broth (value: 1% (w/v)) per PMID:39345197,
  raising proportional Completeness Score from 80 to 95/100 (and scripts/audit_completeness.py
  score from 15 to 80/100). CommunityMech:000385 (SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml)
  now populates functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] on engineered
  ethanol-detoxifying and riboflavin-synthesizing Bacillus subtilis 168 BS3 (NCBITaxon:1423,
  Bacillus subtilis, retaining pre-existing abundance_level: ABUNDANT alongside Shewanella
  oneidensis MR-1 SO3, NCBITaxon:70863) per PMID:42733304 (doi:10.1002/advs.77699),
  raising proportional Completeness Score from 90 to 98/100 (and scripts/audit_completeness.py
  score from 20 to 70/100). All 3 modified records are re-attested in reports/causal_graph_review/decisions/20261104-c5s5-review-remediation.yaml.'
source:
  git_revision: bedd8140895e43ae3aa7765664db6b6e7f1995ff
  state: working_tree
  inputs:
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
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
  - path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    sha256: 0f03389e79ddcf2e97ebb0f32bd51a776b6bcbaea3ddad52c21ada8feca2939b
    role: target
  - path: kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
    sha256: 04ab8c93316524a7316f27651a9cf1b29cd83f6495e558c9a4c190c216301516
    role: target
  - path: kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
    sha256: 05bdd8b0222ec8e14e7b5b63b6be37e9f73bd8de356023cf52c0b6c47bb182d6
    role: target
  - path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
    sha256: bc1fb667da9be21480d7f27961b01fc547c45dc3cef1ca63b58fe01584104076
    role: target
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 904cc9646ae53fe0c021c1461a09f3f8d15b763edad42b6c9a43ada91c87597d
    role: target
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: reports/causal_graph_review/decisions/20261104-c5s5-review-remediation.yaml
    sha256: 62a47d9ca83ac959e10f7934732bb43f0686648ebcf146f7a33164d4c175568e
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: 5e0dd104785787c98e6bcb9268fb61d27d33fdfef62c9e421285e379dd7fb179
    role: context
  - path: reviews/structured/20261104T034000Z-c5s4-record-deep-audit/review.yaml
    sha256: 47b83251ea42a654fe539b006b8afef9b7f80194351ccefd838ba66054d0488e
    role: context
  - path: reviews/structured/20261104T034100Z-c5s4-frozen-cohort-review/review.yaml
    sha256: 2d02703e40b1172ccaddca7b9319a5898cda75662a34275c12f6d50eccb1fe23
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Full post-remediation verification of all 10 community records referenced
    by Cycle 5 Stage 4 findings (3 actionable finding targets + 7 carried-forward
    source-limited targets).
  selection: All 10 records referenced by carry_forward_ids and owner_paths in Cycle
    5 Stage 4 evidence.yaml.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000084
  - CommunityMech:000085
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000385
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
- target_id: CommunityMech:000084
  path: kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
  label: CommunityMech:000084 (Streptococcus mutans - Selenomonas sputigena ECC Pathobiont
    Model)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000085
  path: kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
  label: CommunityMech:000085 (Streptococcus mutans - Veillonella parvula ASC Biofilm
    Co-culture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000091
  path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
  label: CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000153
  path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
  label: CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community)
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
- target_id: CommunityMech:000385
  path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
  label: CommunityMech:000385 (SO3-BS3 Lithium-Ion Battery Bioleaching Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
checks:
- check_id: chk-linkml-schema-c5s5
  name: LinkML schema and strict corpus validation on all 10 Cycle 5 Stage 5 target
    records
  status: passed
  required: true
  summary: All 10 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml
    with 0 errors.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000084
  - CommunityMech:000085
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000385
  command: PYTHONPATH=src .venv/bin/python scripts/validate_strict.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c5s5-schema-validation
- check_id: chk-causal-and-participants-tests-c5s5
  name: Causal review inventory, participating_taxa integrity, and batch regression
    tests
  status: passed
  required: true
  summary: All pytest checks across test_participating_taxa.py, test_causal_review_inventory.py,
    and test_causal_review_batch97.py pass with 0 failures.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000084
  - CommunityMech:000085
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000385
  command: .venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_participating_taxa.py
    tests/test_causal_review_inventory.py tests/test_causal_review_batch97.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c5s5-causal-inventory
evidence:
- evidence_id: ev-c5s5-schema-validation
  kind: validation
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity
  accessed_at: '2026-11-04T05:55:00Z'
  support: supports
  summary: All 10 Cycle 5 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml
    with 0 LinkML errors, 0 GTDB coherence errors, 0 scalar errors, and 0 ontology
    term label errors.
- evidence_id: ev-c5s5-causal-inventory
  kind: validation
  reference: reports/causal_graph_review/decisions/20261104-c5s5-review-remediation.yaml
  locator: records[0..2]
  accessed_at: '2026-11-04T05:56:00Z'
  support: supports
  summary: Successor causal review ledger 20261104-c5s5-review-remediation.yaml re-attests
    all 3 modified community records (CommunityMech:000084, 000085, 000385); reports/causal_graph_review/inventory.tsv
    passes all 32 inventory integrity checks (436 reviewed, 54 needs_research, 0 stale
    hashes, 0 structural defects).
- evidence_id: ev-c5s5-primary-sources
  kind: primary_source
  reference: references_cache/
  locator: PMID:37217495, PMID:39345197, PMID:42733304
  accessed_at: '2026-11-04T05:57:00Z'
  support: supports
  summary: 'Primary source caches in references_cache/ support PRIMARY_DEGRADER/CROSS_FEEDER
    and ABUNDANT on Streptococcus mutans (NCBITaxon:1309), SYNTROPHIC_PARTNER/CROSS_FEEDER
    on Selenomonas sputigena (NCBITaxon:69823), and 1% (w/v) sucrose supplementation
    in BHIS medium on CommunityMech:000084 (PMID:37217495, doi:10.1038/s41467-023-38346-3);
    PRIMARY_DEGRADER/CROSS_FEEDER and ABUNDANT on Streptococcus mutans (NCBITaxon:1309),
    SYNTROPHIC_PARTNER/CROSS_FEEDER on Veillonella parvula (NCBITaxon:29466), and
    1% (w/v) sucrose supplementation in BHI broth on CommunityMech:000085 (PMID:39345197);
    and SYNTROPHIC_PARTNER/CROSS_FEEDER on Bacillus subtilis 168 BS3 (NCBITaxon:1423,
    Bacillus subtilis) on CommunityMech:000385 (PMID:42733304, doi:10.1002/advs.77699)
    (#2105), while confirming that the 7 deferred records (#765, #1467, #1657, #1681,
    #1699, #1841, #1847) remain bounded to abstract-verified claims.'
assessments:
- assessment_id: assess-c5s5-functional-roles-and-completeness
  area: completeness
  topic: 'Post-remediation verification of functional_role, abundance_level, and environmental_factors
    on CommunityMech:000084, 000085, and 000385 (Issue #2105)'
  outcome: supported
  summary: CommunityMech:000084 (proportional Completeness Score 80 -> 95/100; scripts/audit_completeness.py
    score 15 -> 80/100), CommunityMech:000085 (proportional Completeness Score 80
    -> 95/100; scripts/audit_completeness.py score 15 -> 80/100), and CommunityMech:000385
    (proportional Completeness Score 90 -> 98/100; scripts/audit_completeness.py score
    20 -> 70/100) now populate source-backed functional_role on all 6/6 TaxonomicComposition
    entries (and source-backed abundance_level on all 5/6 entries where categorical
    abundance is supported by the source), plus source-backed environmental_factors
    on all 3 records.
  target_ids:
  - CommunityMech:000084
  - CommunityMech:000085
  - CommunityMech:000385
  evidence_ids:
  - ev-c5s5-schema-validation
  - ev-c5s5-causal-inventory
  - ev-c5s5-primary-sources
  metrics:
  - name: remediated_record_taxon_functional_role_pct
    value: 100.0
    unit: percent
    definition: Percentage of TaxonomicComposition entries across the 3 remediated
      MicrobialCommunity records carrying populated functional_role (6/6).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-c5s5-deferred-source-limited-records
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
  - ev-c5s5-schema-validation
  - ev-c5s5-primary-sources
findings:
- finding_id: c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose
  issue_key: communitymech-c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Streptococcus mutans - Selenomonas sputigena ECC Pathobiont Model (CommunityMech:000084)
    omits source-backed functional_role and ABUNDANT abundance_level on Streptococcus
    mutans, functional_role on Selenomonas sputigena, and environmental_factors for
    1% (w/v) sucrose supplementation in BHIS medium
  description: 'CommunityMech:000084 (kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml,
    proportional Completeness Score 80/100; scripts/audit_completeness.py score 15/100)
    models the two-species cariogenic dental biofilm of Streptococcus mutans (NCBITaxon:1309)
    and Selenomonas sputigena (NCBITaxon:69823) in early childhood caries (PMID:37217495,
    doi:10.1038/s41467-023-38346-3). In taxonomy, Streptococcus mutans omits functional_role:
    [PRIMARY_DEGRADER, CROSS_FEEDER] and abundance_level: ABUNDANT, and Selenomonas
    sputigena omits functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER], despite verbatim
    support in PMID:37217495 showing that the biofilm core near the centroid consists
    predominantly of S. mutans while S. sputigena becomes trapped in streptococcal
    exoglucans and engages in a co-metabolic relationship that increases acid production
    rate. In addition, environmental_factors is absent despite PMID:37217495 establishing
    1% (w/v) sucrose supplementation in BHIS medium (107 CFU/mL for the new species
    and/or 105 CFU/mL S. mutans).'
  target_ids:
  - CommunityMech:000084
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - environmental_factors
  evidence_ids:
  - ev-c5s5-schema-validation
  - ev-c5s5-causal-inventory
  - ev-c5s5-primary-sources
  rule_id: review-communities:completeness-functional-roles-and-environment
  native_severity: P2
  normalization_reason: CommunityMech P2 (missing source-backed functional_role, abundance_level,
    and environmental_factors on an active two-species cariogenic biofilm record)
    maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SMutans_SSputigena_ECC_Pathobiont.yaml
    role: canonical_record
  tags:
  - completeness
  - grounding
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2105: populated functional_role: [PRIMARY_DEGRADER,
    CROSS_FEEDER] and abundance_level: ABUNDANT on Streptococcus mutans (NCBITaxon:1309),
    functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] on Selenomonas sputigena (NCBITaxon:69823),
    and environmental_factors for 1% (w/v) sucrose supplementation in BHIS medium
    (value: 1% (w/v)) per PMID:37217495 (doi:10.1038/s41467-023-38346-3).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034000Z-c5s4-record-deep-audit
    finding_id: c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: c5s4-000084-smutans-ssputigena-roles-abundance-and-sucrose
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2105
- finding_id: c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose
  issue_key: communitymech-c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Streptococcus mutans - Veillonella parvula ASC Biofilm Co-culture (CommunityMech:000085)
    omits source-backed functional_role and ABUNDANT abundance_level on Streptococcus
    mutans, functional_role on Veillonella parvula, and environmental_factors for
    1% (w/v) sucrose supplementation in BHI broth
  description: 'CommunityMech:000085 (kb/communities/SMutans_VParvula_ASC_Biofilm.yaml,
    proportional Completeness Score 80/100; scripts/audit_completeness.py score 15/100)
    models the dual-species cariogenic biofilm of Streptococcus mutans (NCBITaxon:1309)
    and Veillonella parvula (NCBITaxon:29466) associated with active secondary caries
    (PMID:39345197). In taxonomy, Streptococcus mutans omits functional_role: [PRIMARY_DEGRADER,
    CROSS_FEEDER] and abundance_level: ABUNDANT, and Veillonella parvula omits functional_role:
    [SYNTROPHIC_PARTNER, CROSS_FEEDER] (while carrying abundance_level: DOMINANT),
    despite verbatim support in PMID:39345197 showing S. mutans GTF-mediated sucrose
    metabolism into water-insoluble glucan EPS, significantly increased relative abundance
    among the 30 most predominant species in the HC group, and V. parvula promotion
    of S. mutans mature biofilm formation with enhanced acid resistance and hydrogen
    peroxide detoxicity. In addition, environmental_factors is absent despite PMID:39345197
    establishing 1% (w/v) sucrose supplementation in BHI broth for mono- and dual-species
    biofilms grown on saliva-coated hydroxyapatite slides at 37 °C for 24 h.'
  target_ids:
  - CommunityMech:000085
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - environmental_factors
  evidence_ids:
  - ev-c5s5-schema-validation
  - ev-c5s5-causal-inventory
  - ev-c5s5-primary-sources
  rule_id: review-communities:completeness-functional-roles-and-environment
  native_severity: P2
  normalization_reason: CommunityMech P2 (missing source-backed functional_role, abundance_level,
    and environmental_factors on an active dual-species cariogenic biofilm record)
    maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SMutans_VParvula_ASC_Biofilm.yaml
    role: canonical_record
  tags:
  - completeness
  - grounding
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2105: populated functional_role: [PRIMARY_DEGRADER,
    CROSS_FEEDER] and abundance_level: ABUNDANT on Streptococcus mutans (NCBITaxon:1309),
    functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] on Veillonella parvula (NCBITaxon:29466),
    and environmental_factors for 1% (w/v) sucrose supplementation in BHI broth (value:
    1% (w/v)) per PMID:39345197.'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034000Z-c5s4-record-deep-audit
    finding_id: c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: c5s4-000085-smutans-vparvula-roles-abundance-and-sucrose
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2105
- finding_id: c5s4-000385-so3-bs3-bsubtilis-functional-role
  issue_key: communitymech-c5s4-000385-so3-bs3-bsubtilis-functional-role
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: SO3-BS3 Lithium-Ion Battery Bioleaching Consortium (CommunityMech:000385)
    omits source-backed functional_role on engineered ethanol-detoxifying and riboflavin-synthesizing
    Bacillus subtilis 168 BS3
  description: 'CommunityMech:000385 (kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml,
    proportional Completeness Score 90/100; scripts/audit_completeness.py score 20/100)
    models the engineered two-species consortium of Shewanella oneidensis MR-1 SO3
    (NCBITaxon:70863, Shewanella oneidensis) and Bacillus subtilis 168 BS3 (NCBITaxon:1423,
    Bacillus subtilis) in Moutai brewing wastewater for reductive bioleaching of spent
    LiNi1/3Co1/3Mn1/3O2 (NCM) lithium-ion battery cathodes (PMID:42733304, doi:10.1002/advs.77699).
    While Shewanella oneidensis MR-1 SO3 (taxonomy[0]) carries functional_role: [ELECTROGEN,
    ELECTRON_DONOR] and abundance_level: ABUNDANT, Bacillus subtilis 168 BS3 (taxonomy[1],
    carrying abundance_level: ABUNDANT) omits functional_role: [SYNTROPHIC_PARTNER,
    CROSS_FEEDER] despite verbatim support in PMID:42733304 showing that strain BS3
    eliminates ethanol inhibition on S. oneidensis EET by converting residual ethanol
    into acetate via the Adh-AldH dual enzyme cascade and synthesizes riboflavin as
    an electron shuttle promoting S. oneidensis EET.'
  target_ids:
  - CommunityMech:000385
  field_paths:
  - taxonomy[1].functional_role
  evidence_ids:
  - ev-c5s5-schema-validation
  - ev-c5s5-causal-inventory
  - ev-c5s5-primary-sources
  rule_id: review-communities:completeness-functional-roles-and-environment
  native_severity: P2
  normalization_reason: CommunityMech P2 (missing source-backed functional_role on
    the engineered syntrophic/cross-feeding partner taxon in a two-member bioleaching
    consortium) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SO3_BS3_Lithium_Battery_Bioleaching_Consortium.yaml
    role: canonical_record
  tags:
  - completeness
  - grounding
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2105: populated functional_role: [SYNTROPHIC_PARTNER,
    CROSS_FEEDER] on Bacillus subtilis 168 BS3 (NCBITaxon:1423, Bacillus subtilis,
    taxonomy[1]) with verbatim IN_VITRO evidence from PMID:42733304 (doi:10.1002/advs.77699).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034000Z-c5s4-record-deep-audit
    finding_id: c5s4-000385-so3-bs3-bsubtilis-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
    finding_id: c5s4-000385-so3-bs3-bsubtilis-functional-role
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2105
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
  - ev-c5s5-schema-validation
  - ev-c5s5-primary-sources
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
    finding_id: evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T092604Z-cheese-after
    finding_id: evidence-gap
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
  - ev-c5s5-schema-validation
  - ev-c5s5-primary-sources
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
    finding_id: remaining
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T063739Z-transwell-after
    finding_id: remaining
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
  - ev-c5s5-schema-validation
  - ev-c5s5-primary-sources
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
    review_id: 20261014T235318Z-causal-prompt-phormidium-after
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
  - ev-c5s5-schema-validation
  - ev-c5s5-primary-sources
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
  - ev-c5s5-schema-validation
  - ev-c5s5-primary-sources
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
  - ev-c5s5-schema-validation
  - ev-c5s5-primary-sources
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
  - ev-c5s5-schema-validation
  - ev-c5s5-primary-sources
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
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
  tags:
  - carried-forward
  - source-limited
actions:
- action_id: act-defer-source-limited-fulltext-findings-c5s5
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
  review_id: 20261104T034000Z-c5s4-record-deep-audit
  relationship: supersedes_stage4_deep_audit
- repository: CultureBotAI/CommunityMech
  review_id: 20261104T034100Z-c5s4-frozen-cohort-review
  relationship: supersedes_stage4_cohort_review
tags:
- cycle5
- stage5
- remediation-verification
- record-review
```
