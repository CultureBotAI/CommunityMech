# Cycle 6 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward Findings

- Review: 20261104T203000Z-c6s5-remediation-verification
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-04T20:20:00Z
- Finished UTC: 2026-11-04T20:30:00Z
- Reviewer: antigravity-c6s5-remediation-reviewer (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Post-remediation scientific and structural verification review of all 10 finding-bearing community records from Cycle 6 Stage 4 (3 community records across 3 actionable open findings grouped into GitHub issue #2113, plus 7 source-limited deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699, #1841, and #1847). CommunityMech:000401 (Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml) now populates abundance_level: DOMINANT and verbatim abundance-shift evidence from PMID:42655156 (PMC13515949, doi:10.3390/microorganisms14081812) on both Bifidobacterium bifidum JCM1254 (NCBITaxon:1681) and Faecalibacterium prausnitzii A2-165 (NCBITaxon:853), raising its review-communities s_ab rubric component from 0/5 to 5/5 (Completeness Score 100/100; scripts/audit_completeness.py score 75/100). CommunityMech:000402 (Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml) now populates functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT on Delta nrfA Shewanella oneidensis MR-1 (NCBITaxon:211586) and functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] and abundance_level: DOMINANT on Candidatus Brocadia anammox bacteria (NCBITaxon:203682) with verbatim evidence from PMID:42655905 (PMC13519132, doi:10.1002/wer.70526) while preserving taxonomy[2] (endogenous activated-sludge heterotrophic bacteria, NCBITaxon:2) under discussions[0] (shewanella_anammox_sludge_membership_and_flux_unresolved), raising review-communities Completeness Score from 90 to 95/100 (scripts/audit_completeness.py score 25/100). CommunityMech:000404 (Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml) now populates functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT on Ramichloridium apiculatum CMS-1 (NCBITaxon:470080) and functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: DOMINANT on Talaromyces pseudofuniculosus hzt-3' (NCBITaxon:2015341) with verbatim evidence from PMID:42478817 (PMC13488302, doi:10.1128/aem.02519-25), raising review-communities Completeness Score from 90 to 98/100 (and scripts/audit_completeness.py score from 40 to 90/100). All 3 modified records are re-attested in reports/causal_graph_review/decisions/20261104-c6s5-review-remediation.yaml.

## Scope And Provenance

Full post-remediation verification of all 10 community records referenced by Cycle 6 Stage 4 findings (3 actionable finding targets + 7 carried-forward source-limited targets).

Selection: All 10 records referenced by carry_forward_ids and owner_paths in Cycle 6 Stage 4 evidence.yaml.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 8abeafc9364252290709f261b3d1f60cad450ea7.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000048 | kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml | maintained | CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium) |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | CommunityMech:000054 (Phormidium Alkaline Consortium) |
| CommunityMech:000091 | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml | maintained | CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System) |
| CommunityMech:000153 | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml | maintained | CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community) |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml | maintained | CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm) |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic Co-culture) |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience) |
| CommunityMech:000401 | kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml | maintained | CommunityMech:000401 (Bifidobacterium bifidum-Faecalibacterium prausnitzii 2'-FL/FOS Butyrate Co-Culture) |
| CommunityMech:000402 | kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml | maintained | CommunityMech:000402 (Delta nrfA Shewanella oneidensis-Anammox Nitrite-Coupled Consortium) |
| CommunityMech:000404 | kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml | maintained | CommunityMech:000404 (Ramichloridium apiculatum-Talaromyces pseudofuniculosus Wollastonite-Dissolving Fungal Consortium) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema and strict corpus validation on all 10 Cycle 6 Stage 5 target records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000401, CommunityMech:000402, CommunityMech:000404 | All 10 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| Causal review inventory, participating_taxa integrity, and batch regression tests | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000401, CommunityMech:000402, CommunityMech:000404 | All pytest checks across test_participating_taxa.py, test_causal_review_inventory.py, test_causal_review_batch100.py, and test_causal_review_batch123.py pass with 0 failures. |

## Scientific And Domain Assessments

### Post-remediation verification of functional_role and abundance_level on CommunityMech:000401, 000402, and 000404 (Issue #2113)

completeness: supported. Targets: CommunityMech:000401, CommunityMech:000402, CommunityMech:000404.

CommunityMech:000401 (review-communities Completeness Score 100/100 with s_ab 0/5 -&gt; 5/5; scripts/audit_completeness.py score 75/100), CommunityMech:000402 (review-communities Completeness Score 90 -&gt; 95/100; scripts/audit_completeness.py score 25/100), and CommunityMech:000404 (review-communities Completeness Score 90 -&gt; 98/100; scripts/audit_completeness.py score 40 -&gt; 90/100) now populate source-backed functional_role and abundance_level across all 6/6 focal TaxonomicComposition entries (while preserving the broad endogenous sludge background grouping taxonomy[2] on CommunityMech:000402 per shewanella_anammox_sludge_membership_and_flux_unresolved).

### Verification of abstract-grounded integrity on 7 source-limited deferred community records (#765, #1467, #1657, #1681, #1699, #1841, #1847)

evidence: supported. Targets: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302.

All 7 source-limited records (CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, 000302) remain valid against LinkML and grounded strictly to verbatim abstract claims without fabrication while their full-text/supplementary data gaps remain tracked in open GitHub issues.

## Findings

### c6s4-000401-bifido-faecali-abundance-levels: Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture (CommunityMech:000401) omits abundance_level on both co-equal OD600-standardized coculture members

major / resolved / confirmed; issue key: c6s4-000401-bifido-faecali-abundance-levels.

In kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml (CommunityMech:000401), both taxonomy[0] (Bifidobacterium bifidum JCM1254, NCBITaxon:1681, label: Bifidobacterium bifidum) and taxonomy[1] (Faecalibacterium prausnitzii A2-165, NCBITaxon:853, label: Faecalibacterium prausnitzii) record abundance_value: 'One of two OD600-standardized co-culture members' and functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER], but both omit abundance_level. The cited open-access source PMID:42655156 (PMC13515949, doi:10.3390/microorganisms14081812) establishes that both strains were co-inoculated as equal 8 uL aliquots of OD600 = 1.0 suspensions into 800 uL YCFA- medium and alternated in dominance across the 2'-FL/FOS substrate ratio series (with F. prausnitzii accounting for ~60% under FOS-only conditions and B. bifidum reaching up to 95% under 2'-FL-rich conditions), supporting abundance_level: DOMINANT on both co-equal coculture members while preserving discussions[0] (bifido_faecali_2fl_fos_flux_unresolved) regarding unmeasured pH, residual substrate, and metabolic flux.

Disposition: Resolved in Issue #2113: populated abundance_level: DOMINANT and verbatim abundance-shift evidence from PMID:42655156 (PMC13515949, doi:10.3390/microorganisms14081812) on both Bifidobacterium bifidum JCM1254 (NCBITaxon:1681) and Faecalibacterium prausnitzii A2-165 (NCBITaxon:853).

### c6s4-000402-shewanella-anammox-roles-and-abundance: Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium (CommunityMech:000402) omits functional_role and abundance_level on Delta nrfA Shewanella oneidensis MR-1 and Candidatus Brocadia anammox bacteria

major / resolved / confirmed; issue key: c6s4-000402-shewanella-anammox-roles-and-abundance.

In kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml (CommunityMech:000402), taxonomy[0] (Delta nrfA Shewanella oneidensis MR-1, NCBITaxon:211586, label: Shewanella oneidensis MR-1) and taxonomy[1] (Candidatus Brocadia anammox bacteria, NCBITaxon:203682, label: Planctomycetota) omit both functional_role and abundance_level. The cited open-access source PMID:42655905 (PMC13519132, doi:10.1002/wer.70526) establishes that Delta nrfA S. oneidensis MR-1 accumulates nitrite (NO2--N) by blocking the nrfA DNRA pathway and supplies nitrite to anammox bacteria in a stable synergistic interaction (functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER]; abundance_level: ABUNDANT, co-inoculated as 5 mL bacterial suspension with 25 mL anammox sludge in 500 mL DeltaB1 reactors), while Candidatus Brocadia (7%~10% relative abundance within Planctomycetota at 15%~21%) emerged as the dominant genus and only detected anammox bacterium (functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]; abundance_level: DOMINANT). In accordance with discussions[0] (shewanella_anammox_sludge_membership_and_flux_unresolved), taxonomy[2] (endogenous activated-sludge heterotrophic bacteria, NCBITaxon:2) remains scoped as an unresolved broad background sludge grouping whose pathway flux partitioning between anammox, denitrification, and DNRA was not quantified by isotope labeling.

Disposition: Resolved in Issue #2113: populated functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT on Delta nrfA Shewanella oneidensis MR-1 (NCBITaxon:211586) and functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] and abundance_level: DOMINANT on Candidatus Brocadia anammox bacteria (NCBITaxon:203682) with verbatim evidence from PMID:42655905 (PMC13519132, doi:10.1002/wer.70526).

### c6s4-000404-wollastonite-cms1-role-and-abundance: Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium (CommunityMech:000404) omits functional_role on Ramichloridium apiculatum CMS-1 and abundance_level on both fungal members

major / resolved / confirmed; issue key: c6s4-000404-wollastonite-cms1-role-and-abundance.

In kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml (CommunityMech:000404), taxonomy[0] (Ramichloridium apiculatum CMS-1, NCBITaxon:470080, label: Ramichloridium apiculatum) omits both functional_role and abundance_level, while taxonomy[1] (Talaromyces pseudofuniculosus hzt-3', NCBITaxon:2015341, label: Talaromyces pseudofuniculosus) records functional_role: [CROSS_FEEDER] but omits abundance_level. The cited open-access source PMID:42478817 (PMC13488302, doi:10.1128/aem.02519-25) establishes that in the optimal 20% CMS-1 + 80% hzt-3' mixed fungal consortium, R. apiculatum CMS-1 produces oxalic acid (0.66 +- 0.033 mg/mL in monoculture), L-glutamic acid, and extracellular polysaccharides and proteins utilized in the mixed culture (functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER]; abundance_level: ABUNDANT at 20% initial spore-suspension inoculum share), while T. pseudofuniculosus hzt-3' is inoculated at 80% initial spore-suspension share and explicitly identified as playing the dominant role in the mixed culture (functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER, SYNTROPHIC_PARTNER]; abundance_level: DOMINANT), preserving discussions[0] (woll_causal_scope_batch123) that cross-feeding directionality from CMS-1 to hzt-3' is proposed from bulk monoculture vs mixed-culture metabolomics.

Disposition: Resolved in Issue #2113: populated functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT on Ramichloridium apiculatum CMS-1 (NCBITaxon:470080) and functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: DOMINANT on Talaromyces pseudofuniculosus hzt-3' (NCBITaxon:2015341) with verbatim evidence from PMID:42478817 (PMC13488302, doi:10.1128/aem.02519-25).

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

### act-defer-source-limited-fulltext-findings-c6s5

Retain source-limited full-text findings under open GitHub issues (#765, #1467, #1657, #1681, #1699, #1841, #1847) until open-access full text or supplementary strain/assay tables become available for CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify full-text or supplementary table availability before expanding abstract-grounded claims on source-limited records.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c6s5-schema-validation | src/communitymech/schema/communitymech.yaml; MicrobialCommunity | supports | All 10 Cycle 6 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml with 0 LinkML errors, 0 GTDB coherence errors, 0 scalar errors, and 0 ontology term label errors. |
| ev-c6s5-causal-inventory | reports/causal_graph_review/decisions/20261104-c6s5-review-remediation.yaml; records[0..2] | supports | Successor causal review ledger 20261104-c6s5-review-remediation.yaml re-attests all 3 modified community records (CommunityMech:000401, 000402, 000404); reports/causal_graph_review/inventory.tsv passes all 32 inventory integrity checks (444 reviewed, 54 needs_research, 0 stale hashes, 0 structural defects). |
| ev-c6s5-primary-sources | references_cache/; PMID:42655156, PMID:42655905, PMID:42478817 | supports | Primary source caches in references_cache/ support abundance_level: DOMINANT on both Bifidobacterium bifidum JCM1254 (NCBITaxon:1681) and Faecalibacterium prausnitzii A2-165 (NCBITaxon:853) on CommunityMech:000401 (PMID:42655156, PMC13515949, doi:10.3390/microorganisms14081812); functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT on Delta nrfA Shewanella oneidensis MR-1 (NCBITaxon:211586) and functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] and abundance_level: DOMINANT on Candidatus Brocadia anammox bacteria (NCBITaxon:203682) on CommunityMech:000402 (PMID:42655905, PMC13519132, doi:10.1002/wer.70526); and functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT on Ramichloridium apiculatum CMS-1 (NCBITaxon:470080) and functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: DOMINANT on Talaromyces pseudofuniculosus hzt-3' (NCBITaxon:2015341) on CommunityMech:000404 (PMID:42478817, PMC13488302, doi:10.1128/aem.02519-25) (#2113), while confirming that the 7 deferred records (#765, #1467, #1657, #1681, #1699, #1841, #1847) remain bounded to abstract-verified claims. |

## Limits And Additional Notes

- Seven source-limited community records (CommunityMech:000048 #1657, 000054 #1699, 000091 #1467, 000153 #765, 000222 #1841, 000295 #1681, 000302 #1847) remain deferred because primary full text or supplementary tables are paywalled or unavailable in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T203000Z-c6s5-remediation-verification
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 6 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward
  Findings
started_at: '2026-11-04T20:20:00Z'
finished_at: '2026-11-04T20:30:00Z'
reviewer:
  identity: antigravity-c6s5-remediation-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated post-remediation verification review pass over the
    10 Cycle 6 Stage 4 finding-bearing community records in the working tree.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
native_verdict: 'PASS_WITH_LIMITATIONS (3 actionable Cycle 6 Stage 4 findings resolved
  across 3 updated community records in #2113; 7 source-limited findings deferred
  under open GitHub issues)'
scientific_review: true
summary: 'Post-remediation scientific and structural verification review of all 10
  finding-bearing community records from Cycle 6 Stage 4 (3 community records across
  3 actionable open findings grouped into GitHub issue #2113, plus 7 source-limited
  deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699,
  #1841, and #1847). CommunityMech:000401 (Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml)
  now populates abundance_level: DOMINANT and verbatim abundance-shift evidence from
  PMID:42655156 (PMC13515949, doi:10.3390/microorganisms14081812) on both Bifidobacterium
  bifidum JCM1254 (NCBITaxon:1681) and Faecalibacterium prausnitzii A2-165 (NCBITaxon:853),
  raising its review-communities s_ab rubric component from 0/5 to 5/5 (Completeness
  Score 100/100; scripts/audit_completeness.py score 75/100). CommunityMech:000402
  (Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml) now populates functional_role:
  [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT on Delta nrfA Shewanella
  oneidensis MR-1 (NCBITaxon:211586) and functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]
  and abundance_level: DOMINANT on Candidatus Brocadia anammox bacteria (NCBITaxon:203682)
  with verbatim evidence from PMID:42655905 (PMC13519132, doi:10.1002/wer.70526) while
  preserving taxonomy[2] (endogenous activated-sludge heterotrophic bacteria, NCBITaxon:2)
  under discussions[0] (shewanella_anammox_sludge_membership_and_flux_unresolved),
  raising review-communities Completeness Score from 90 to 95/100 (scripts/audit_completeness.py
  score 25/100). CommunityMech:000404 (Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml)
  now populates functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level:
  ABUNDANT on Ramichloridium apiculatum CMS-1 (NCBITaxon:470080) and functional_role:
  [PRIMARY_DEGRADER, CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: DOMINANT
  on Talaromyces pseudofuniculosus hzt-3'' (NCBITaxon:2015341) with verbatim evidence
  from PMID:42478817 (PMC13488302, doi:10.1128/aem.02519-25), raising review-communities
  Completeness Score from 90 to 98/100 (and scripts/audit_completeness.py score from
  40 to 90/100). All 3 modified records are re-attested in reports/causal_graph_review/decisions/20261104-c6s5-review-remediation.yaml.'
source:
  git_revision: 8abeafc9364252290709f261b3d1f60cad450ea7
  state: working_tree
  inputs:
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    sha256: c751d65f77ac054c5c8686bb6fd9d0ecf503fe729c1bb5c1d2409bbfe781169e
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
  - path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    sha256: 0f03389e79ddcf2e97ebb0f32bd51a776b6bcbaea3ddad52c21ada8feca2939b
    role: target
  - path: kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
    sha256: 703558d694853b4262cb56256d65bcd314d432ba376fea5639ea4d5b5fd286f2
    role: target
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 904cc9646ae53fe0c021c1461a09f3f8d15b763edad42b6c9a43ada91c87597d
    role: target
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
    sha256: cc6165ecc72e89e7945cd433d963ce1105ccc8a08078de656f5485a098ccd49d
    role: target
  - path: reports/causal_graph_review/decisions/20261104-c6s5-review-remediation.yaml
    sha256: 66e9447171a3a8fe64dc01cea5fecbe01785236b19a2fa21842ad439a7cb22f0
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: 2ffddeef6e2b6843ff5ecf037b85edcc0281d1f4bb82d2de1e818030c4569903
    role: context
  - path: reviews/structured/20261104T180000Z-c6s4-record-deep-audit/review.yaml
    sha256: 47976319669248c26320528ed574b6da77b38aa592f3c0c9b1f76aaf6e0dc208
    role: context
  - path: reviews/structured/20261104T180100Z-c6s4-frozen-cohort-review/review.yaml
    sha256: 60d9ce7de9da126368e0db1407f3403509ba4766df437feeed2f220dc66ef575
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Full post-remediation verification of all 10 community records referenced
    by Cycle 6 Stage 4 findings (3 actionable finding targets + 7 carried-forward
    source-limited targets).
  selection: All 10 records referenced by carry_forward_ids and owner_paths in Cycle
    6 Stage 4 evidence.yaml.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000401
  - CommunityMech:000402
  - CommunityMech:000404
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
- target_id: CommunityMech:000401
  path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
  label: CommunityMech:000401 (Bifidobacterium bifidum-Faecalibacterium prausnitzii
    2'-FL/FOS Butyrate Co-Culture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000402
  path: kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
  label: CommunityMech:000402 (Delta nrfA Shewanella oneidensis-Anammox Nitrite-Coupled
    Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000404
  path: kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
  label: CommunityMech:000404 (Ramichloridium apiculatum-Talaromyces pseudofuniculosus
    Wollastonite-Dissolving Fungal Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
checks:
- check_id: chk-linkml-schema-c6s5
  name: LinkML schema and strict corpus validation on all 10 Cycle 6 Stage 5 target
    records
  status: passed
  required: true
  summary: All 10 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml
    with 0 errors.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000401
  - CommunityMech:000402
  - CommunityMech:000404
  command: PYTHONPATH=src .venv/bin/python scripts/validate_strict.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c6s5-schema-validation
- check_id: chk-causal-and-participants-tests-c6s5
  name: Causal review inventory, participating_taxa integrity, and batch regression
    tests
  status: passed
  required: true
  summary: All pytest checks across test_participating_taxa.py, test_causal_review_inventory.py,
    test_causal_review_batch100.py, and test_causal_review_batch123.py pass with 0
    failures.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000401
  - CommunityMech:000402
  - CommunityMech:000404
  command: .venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_participating_taxa.py
    tests/test_causal_review_inventory.py tests/test_causal_review_batch100.py tests/test_causal_review_batch123.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c6s5-causal-inventory
evidence:
- evidence_id: ev-c6s5-schema-validation
  kind: validation
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity
  accessed_at: '2026-11-04T20:25:00Z'
  support: supports
  summary: All 10 Cycle 6 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml
    with 0 LinkML errors, 0 GTDB coherence errors, 0 scalar errors, and 0 ontology
    term label errors.
- evidence_id: ev-c6s5-causal-inventory
  kind: validation
  reference: reports/causal_graph_review/decisions/20261104-c6s5-review-remediation.yaml
  locator: records[0..2]
  accessed_at: '2026-11-04T20:26:00Z'
  support: supports
  summary: Successor causal review ledger 20261104-c6s5-review-remediation.yaml re-attests
    all 3 modified community records (CommunityMech:000401, 000402, 000404); reports/causal_graph_review/inventory.tsv
    passes all 32 inventory integrity checks (444 reviewed, 54 needs_research, 0 stale
    hashes, 0 structural defects).
- evidence_id: ev-c6s5-primary-sources
  kind: primary_source
  reference: references_cache/
  locator: PMID:42655156, PMID:42655905, PMID:42478817
  accessed_at: '2026-11-04T20:27:00Z'
  support: supports
  summary: 'Primary source caches in references_cache/ support abundance_level: DOMINANT
    on both Bifidobacterium bifidum JCM1254 (NCBITaxon:1681) and Faecalibacterium
    prausnitzii A2-165 (NCBITaxon:853) on CommunityMech:000401 (PMID:42655156, PMC13515949,
    doi:10.3390/microorganisms14081812); functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER]
    and abundance_level: ABUNDANT on Delta nrfA Shewanella oneidensis MR-1 (NCBITaxon:211586)
    and functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] and abundance_level: DOMINANT
    on Candidatus Brocadia anammox bacteria (NCBITaxon:203682) on CommunityMech:000402
    (PMID:42655905, PMC13519132, doi:10.1002/wer.70526); and functional_role: [CROSS_FEEDER,
    SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT on Ramichloridium apiculatum
    CMS-1 (NCBITaxon:470080) and functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER,
    SYNTROPHIC_PARTNER] and abundance_level: DOMINANT on Talaromyces pseudofuniculosus
    hzt-3'' (NCBITaxon:2015341) on CommunityMech:000404 (PMID:42478817, PMC13488302,
    doi:10.1128/aem.02519-25) (#2113), while confirming that the 7 deferred records
    (#765, #1467, #1657, #1681, #1699, #1841, #1847) remain bounded to abstract-verified
    claims.'
assessments:
- assessment_id: assess-c6s5-functional-roles-and-abundance
  area: completeness
  topic: 'Post-remediation verification of functional_role and abundance_level on
    CommunityMech:000401, 000402, and 000404 (Issue #2113)'
  outcome: supported
  summary: CommunityMech:000401 (review-communities Completeness Score 100/100 with
    s_ab 0/5 -> 5/5; scripts/audit_completeness.py score 75/100), CommunityMech:000402
    (review-communities Completeness Score 90 -> 95/100; scripts/audit_completeness.py
    score 25/100), and CommunityMech:000404 (review-communities Completeness Score
    90 -> 98/100; scripts/audit_completeness.py score 40 -> 90/100) now populate source-backed
    functional_role and abundance_level across all 6/6 focal TaxonomicComposition
    entries (while preserving the broad endogenous sludge background grouping taxonomy[2]
    on CommunityMech:000402 per shewanella_anammox_sludge_membership_and_flux_unresolved).
  target_ids:
  - CommunityMech:000401
  - CommunityMech:000402
  - CommunityMech:000404
  evidence_ids:
  - ev-c6s5-schema-validation
  - ev-c6s5-causal-inventory
  - ev-c6s5-primary-sources
  metrics:
  - name: remediated_focal_taxon_functional_role_and_abundance_pct
    value: 100.0
    unit: percent
    definition: Percentage of focal TaxonomicComposition entries across the 3 remediated
      MicrobialCommunity records carrying both populated functional_role and abundance_level
      (6/6).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-c6s5-deferred-source-limited-records
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
  - ev-c6s5-schema-validation
  - ev-c6s5-primary-sources
findings:
- finding_id: c6s4-000401-bifido-faecali-abundance-levels
  issue_key: c6s4-000401-bifido-faecali-abundance-levels
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture (CommunityMech:000401)
    omits abundance_level on both co-equal OD600-standardized coculture members
  description: 'In kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    (CommunityMech:000401), both taxonomy[0] (Bifidobacterium bifidum JCM1254, NCBITaxon:1681,
    label: Bifidobacterium bifidum) and taxonomy[1] (Faecalibacterium prausnitzii
    A2-165, NCBITaxon:853, label: Faecalibacterium prausnitzii) record abundance_value:
    ''One of two OD600-standardized co-culture members'' and functional_role: [PRIMARY_DEGRADER,
    CROSS_FEEDER], but both omit abundance_level. The cited open-access source PMID:42655156
    (PMC13515949, doi:10.3390/microorganisms14081812) establishes that both strains
    were co-inoculated as equal 8 uL aliquots of OD600 = 1.0 suspensions into 800
    uL YCFA- medium and alternated in dominance across the 2''-FL/FOS substrate ratio
    series (with F. prausnitzii accounting for ~60% under FOS-only conditions and
    B. bifidum reaching up to 95% under 2''-FL-rich conditions), supporting abundance_level:
    DOMINANT on both co-equal coculture members while preserving discussions[0] (bifido_faecali_2fl_fos_flux_unresolved)
    regarding unmeasured pH, residual substrate, and metabolic flux.'
  target_ids:
  - CommunityMech:000401
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-c6s5-schema-validation
  - ev-c6s5-causal-inventory
  - ev-c6s5-primary-sources
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on both co-equal members
    of a two-strain gut coculture leaves the review-communities s_ab rubric component
    at 0/5 (Completeness Score 100/100; scripts/audit_completeness.py score 75/100)
    and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bifidobacterium_Faecalibacterium_2FL_FOS_Butyrate_Coculture.yaml
    role: canonical_record
  tags:
  - actionable-stage5
  - diet-cohort
  - completeness
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2113: populated abundance_level: DOMINANT
    and verbatim abundance-shift evidence from PMID:42655156 (PMC13515949, doi:10.3390/microorganisms14081812)
    on both Bifidobacterium bifidum JCM1254 (NCBITaxon:1681) and Faecalibacterium
    prausnitzii A2-165 (NCBITaxon:853).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180000Z-c6s4-record-deep-audit
    finding_id: c6s4-000401-bifido-faecali-abundance-levels
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: c6s4-000401-bifido-faecali-abundance-levels
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2113
- finding_id: c6s4-000402-shewanella-anammox-roles-and-abundance
  issue_key: c6s4-000402-shewanella-anammox-roles-and-abundance
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium (CommunityMech:000402)
    omits functional_role and abundance_level on Delta nrfA Shewanella oneidensis
    MR-1 and Candidatus Brocadia anammox bacteria
  description: 'In kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
    (CommunityMech:000402), taxonomy[0] (Delta nrfA Shewanella oneidensis MR-1, NCBITaxon:211586,
    label: Shewanella oneidensis MR-1) and taxonomy[1] (Candidatus Brocadia anammox
    bacteria, NCBITaxon:203682, label: Planctomycetota) omit both functional_role
    and abundance_level. The cited open-access source PMID:42655905 (PMC13519132,
    doi:10.1002/wer.70526) establishes that Delta nrfA S. oneidensis MR-1 accumulates
    nitrite (NO2--N) by blocking the nrfA DNRA pathway and supplies nitrite to anammox
    bacteria in a stable synergistic interaction (functional_role: [CROSS_FEEDER,
    SYNTROPHIC_PARTNER]; abundance_level: ABUNDANT, co-inoculated as 5 mL bacterial
    suspension with 25 mL anammox sludge in 500 mL DeltaB1 reactors), while Candidatus
    Brocadia (7%~10% relative abundance within Planctomycetota at 15%~21%) emerged
    as the dominant genus and only detected anammox bacterium (functional_role: [SYNTROPHIC_PARTNER,
    CROSS_FEEDER]; abundance_level: DOMINANT). In accordance with discussions[0] (shewanella_anammox_sludge_membership_and_flux_unresolved),
    taxonomy[2] (endogenous activated-sludge heterotrophic bacteria, NCBITaxon:2)
    remains scoped as an unresolved broad background sludge grouping whose pathway
    flux partitioning between anammox, denitrification, and DNRA was not quantified
    by isotope labeling.'
  target_ids:
  - CommunityMech:000402
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-c6s5-schema-validation
  - ev-c6s5-causal-inventory
  - ev-c6s5-primary-sources
  rule_id: review-yaml-record:taxonomy-functional-role-completeness
  native_severity: P2
  normalization_reason: Missing source-backed functional_role and abundance_level
    on the two focal guilds (Delta nrfA S. oneidensis MR-1 and Candidatus Brocadia)
    of an engineered nitrite-coupled anammox consortium reduces the review-communities
    Completeness Score to 90/100 (scripts/audit_completeness.py score 25/100) and
    maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
    role: canonical_record
  tags:
  - actionable-stage5
  - biotechnology-cohort
  - completeness
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2113: populated functional_role: [CROSS_FEEDER,
    SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT on Delta nrfA Shewanella oneidensis
    MR-1 (NCBITaxon:211586) and functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]
    and abundance_level: DOMINANT on Candidatus Brocadia anammox bacteria (NCBITaxon:203682)
    with verbatim evidence from PMID:42655905 (PMC13519132, doi:10.1002/wer.70526).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180000Z-c6s4-record-deep-audit
    finding_id: c6s4-000402-shewanella-anammox-roles-and-abundance
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: c6s4-000402-shewanella-anammox-roles-and-abundance
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2113
- finding_id: c6s4-000404-wollastonite-cms1-role-and-abundance
  issue_key: c6s4-000404-wollastonite-cms1-role-and-abundance
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium (CommunityMech:000404)
    omits functional_role on Ramichloridium apiculatum CMS-1 and abundance_level on
    both fungal members
  description: 'In kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
    (CommunityMech:000404), taxonomy[0] (Ramichloridium apiculatum CMS-1, NCBITaxon:470080,
    label: Ramichloridium apiculatum) omits both functional_role and abundance_level,
    while taxonomy[1] (Talaromyces pseudofuniculosus hzt-3'', NCBITaxon:2015341, label:
    Talaromyces pseudofuniculosus) records functional_role: [CROSS_FEEDER] but omits
    abundance_level. The cited open-access source PMID:42478817 (PMC13488302, doi:10.1128/aem.02519-25)
    establishes that in the optimal 20% CMS-1 + 80% hzt-3'' mixed fungal consortium,
    R. apiculatum CMS-1 produces oxalic acid (0.66 +- 0.033 mg/mL in monoculture),
    L-glutamic acid, and extracellular polysaccharides and proteins utilized in the
    mixed culture (functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER]; abundance_level:
    ABUNDANT at 20% initial spore-suspension inoculum share), while T. pseudofuniculosus
    hzt-3'' is inoculated at 80% initial spore-suspension share and explicitly identified
    as playing the dominant role in the mixed culture (functional_role: [PRIMARY_DEGRADER,
    CROSS_FEEDER, SYNTROPHIC_PARTNER]; abundance_level: DOMINANT), preserving discussions[0]
    (woll_causal_scope_batch123) that cross-feeding directionality from CMS-1 to hzt-3''
    is proposed from bulk monoculture vs mixed-culture metabolomics.'
  target_ids:
  - CommunityMech:000404
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-c6s5-schema-validation
  - ev-c6s5-causal-inventory
  - ev-c6s5-primary-sources
  rule_id: review-yaml-record:taxonomy-functional-role-completeness
  native_severity: P2
  normalization_reason: Missing source-backed functional_role on Ramichloridium apiculatum
    CMS-1 and abundance_level on both 20%:80% fungal consortium members reduces the
    review-communities Completeness Score to 90/100 and causes scripts/audit_completeness.py
    required-block failure (40/100), mapping to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
    role: canonical_record
  tags:
  - actionable-stage5
  - biomining-cohort
  - completeness
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2113: populated functional_role: [CROSS_FEEDER,
    SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT on Ramichloridium apiculatum
    CMS-1 (NCBITaxon:470080) and functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER,
    SYNTROPHIC_PARTNER] and abundance_level: DOMINANT on Talaromyces pseudofuniculosus
    hzt-3'' (NCBITaxon:2015341) with verbatim evidence from PMID:42478817 (PMC13488302,
    doi:10.1128/aem.02519-25).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180000Z-c6s4-record-deep-audit
    finding_id: c6s4-000404-wollastonite-cms1-role-and-abundance
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: c6s4-000404-wollastonite-cms1-role-and-abundance
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2113
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
  - ev-c6s5-schema-validation
  - ev-c6s5-primary-sources
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
  - ev-c6s5-schema-validation
  - ev-c6s5-primary-sources
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
  - ev-c6s5-schema-validation
  - ev-c6s5-primary-sources
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
  - ev-c6s5-schema-validation
  - ev-c6s5-primary-sources
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
  - ev-c6s5-schema-validation
  - ev-c6s5-primary-sources
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
  - ev-c6s5-schema-validation
  - ev-c6s5-primary-sources
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
  - ev-c6s5-schema-validation
  - ev-c6s5-primary-sources
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
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
  tags:
  - carried-forward
  - source-limited
actions:
- action_id: act-defer-source-limited-fulltext-findings-c6s5
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
  review_id: 20261104T180000Z-c6s4-record-deep-audit
  relationship: supersedes_stage4_deep_audit
- repository: CultureBotAI/CommunityMech
  review_id: 20261104T180100Z-c6s4-frozen-cohort-review
  relationship: supersedes_stage4_cohort_review
tags:
- cycle6
- stage5
- remediation-verification
- record-review
```
