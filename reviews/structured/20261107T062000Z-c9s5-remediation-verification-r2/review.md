# Cycle 9 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward Findings (Revision 2)

- Review: 20261107T062000Z-c9s5-remediation-verification-r2
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-07T06:18:00Z
- Finished UTC: 2026-11-07T06:20:00Z
- Reviewer: antigravity-c9s5-remediation-reviewer (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Post-remediation scientific and structural verification review of all 10 finding-bearing community records from Cycle 9 Stage 4 (3 community records across 3 actionable open findings grouped into GitHub issue #2713, plus 7 source-limited deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699, #1841, and #1847). CommunityMech:000331 (Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml) now populates abundance_level: DOMINANT and verbatim two-strain synthetic consortium evidence from PMID:42269294 (doi:10.1016/j.jhazmat.2026.142626) on both Pseudomonas aeruginosa PA (taxonomy[0], NCBITaxon:287) and Paracoccus pantotrophus PP (taxonomy[1], NCBITaxon:82367) while preserving discussions[0] (bifenthrin-removal-versus-assimilation), raising its review-communities s_ab rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level; Completeness Score 83/100 -&gt; 88/100; scripts/audit_completeness.py score 65/100). CommunityMech:000455 (Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml) now populates abundance_level: DOMINANT and bracket-free verbatim two-strain obligate mutualistic coculture evidence from PMID:42592155 (PMC13463769, doi:10.1093/nsr/nwag357) on both Escherichia coli K-12 MG1655 ΔargA-ΔmetJ (taxonomy[0], NCBITaxon:511145) and Escherichia coli K-12 MG1655 ΔmetA-ΔargR (taxonomy[1], NCBITaxon:511145) while preserving discussions[0..2], raising review-communities s_ab from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level; Completeness Score 83/100 -&gt; 88/100; scripts/audit_completeness.py score 65/100). CommunityMech:000461 (Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml) now populates abundance_level: DOMINANT on Pseudomonas sp. RF (taxonomy[0], NCBITaxon:286) and abundance_level: ABUNDANT on Acidovorax sp. PH (taxonomy[1], NCBITaxon:12916) with verbatim 3:1 inoculation-ratio evidence from PMID:41900437 (PMC13029111, doi:10.3390/microorganisms14030678) while preserving discussions[0..1], raising review-communities s_ab from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level; Completeness Score 73/100 -&gt; 78/100; scripts/audit_completeness.py score 55/100). All 3 modified records are re-attested in reports/causal_graph_review/decisions/20261107-c9s5-review-remediation.yaml.

## Scope And Provenance

Full post-remediation verification of all 10 community records referenced by Cycle 9 Stage 4 findings (3 actionable finding targets + 7 carried-forward source-limited targets).

Selection: All 10 records referenced by carry_forward_ids and owner_paths in Cycle 9 Stage 4 evidence.yaml.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base 336c2543d5c7c265e240aa695f53ce34dca59207.
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
| CommunityMech:000331 | kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml | maintained | CommunityMech:000331 (Pseudomonas-Paracoccus Bifenthrin-Degrading Consortium) |
| CommunityMech:000455 | kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml | maintained | CommunityMech:000455 (E. coli K-12 MG1655 Arg-Met Cross-Feeding Coculture) |
| CommunityMech:000461 | kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml | maintained | CommunityMech:000461 (Pseudomonas-Acidovorax Aniline-Degradation SynCom) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema and strict corpus validation on all 10 Cycle 9 Stage 5 target records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000331, CommunityMech:000455, CommunityMech:000461 | All 10 MicrobialCommunity target records validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| Causal review inventory, participating_taxa integrity, and GTDB demoted clade regression tests | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000331, CommunityMech:000455, CommunityMech:000461 | All pytest checks across test_participating_taxa.py, test_causal_review_inventory.py, and test_gtdb_demoted_clades.py pass with 0 failures. |

## Scientific And Domain Assessments

### Post-remediation verification of abundance_level on CommunityMech:000331, 000455, and 000461 (Issue #2713)

completeness: supported. Targets: CommunityMech:000331, CommunityMech:000455, CommunityMech:000461.

CommunityMech:000331 (review-communities s_ab 0/5 -&gt; 5/5, Completeness Score 83/100 -&gt; 88/100; scripts/audit_completeness.py score 65/100), CommunityMech:000455 (review-communities s_ab 0/5 -&gt; 5/5, Completeness Score 83/100 -&gt; 88/100; scripts/audit_completeness.py score 65/100), and CommunityMech:000461 (review-communities s_ab 0/5 -&gt; 5/5, Completeness Score 73/100 -&gt; 78/100; scripts/audit_completeness.py score 55/100) now populate source-backed functional_role and abundance_level across all 6/6 TaxonomicComposition entries while preserving all record-level discussions.

### Verification of abstract-grounded integrity on 7 source-limited deferred community records (#765, #1467, #1657, #1681, #1699, #1841, #1847)

evidence: supported. Targets: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302.

All 7 source-limited records (CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, 000302) remain valid against LinkML and grounded strictly to verbatim abstract claims without fabrication while their full-text/supplementary data gaps remain tracked in open GitHub issues.

## Findings

### c9s4-000331-pseudomonas-paracoccus-abundance-levels: Both synthetic consortium members in Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium (CommunityMech:000331) omit abundance_level despite defined two-strain consortium support in PMID:42269294

major / resolved / confirmed; issue key: c9s4-000331-pseudomonas-paracoccus-abundance-levels.

In kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml (CommunityMech:000331), both Pseudomonas aeruginosa PA (taxonomy[0], NCBITaxon:287, functional_role: [PRIMARY_DEGRADER]) and Paracoccus pantotrophus PP (taxonomy[1], NCBITaxon:82367, functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER]) omit abundance_level. The cited study (PMID:42269294, doi:10.1016/j.jhazmat.2026.142626) explicitly reports that 'Pseudomonas aeruginosa strain PA (PA) and Paracoccus pantotrophus strain PP (PP) were isolated from contaminated soil and constructed into a synthetic consortium (PA+PP), which synergistically enhanced bifenthrin degradation.' Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1] while preserving discussions[0] (bifenthrin-removal-versus-assimilation) raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

Disposition: Resolved in Issue #2713: populated abundance_level: DOMINANT and verbatim two-strain synthetic consortium evidence from PMID:42269294 (doi:10.1016/j.jhazmat.2026.142626) on both Pseudomonas aeruginosa PA (NCBITaxon:287) and Paracoccus pantotrophus PP (NCBITaxon:82367).

### c9s4-000455-ecoli-arg-met-abundance-levels: Both engineered auxotrophic partners in Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture (CommunityMech:000455) omit abundance_level despite defined two-strain mutualistic coculture support in PMID:42592155

major / resolved / confirmed; issue key: c9s4-000455-ecoli-arg-met-abundance-levels.

In kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml (CommunityMech:000455), both Escherichia coli K-12 MG1655 ΔargA-ΔmetJ (taxonomy[0], NCBITaxon:511145, functional_role: [CROSS_FEEDER]) and Escherichia coli K-12 MG1655 ΔmetA-ΔargR (taxonomy[1], NCBITaxon:511145, functional_role: [CROSS_FEEDER]) omit abundance_level. The cited open-access study (PMID:42592155, PMC13463769, doi:10.1093/nsr/nwag357) explicitly reports that 'we constructed a metabolic cross-feeding system consisting of two genetically engineered double-mutant strains of E. coli, ΔargA-ΔmetJ and ΔmetA-ΔargR [ 17 , 27 , 28 ].' Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1] while preserving discussions[0] (arg_met_supplementary_protocol_details), discussions[1] (additional_pair_and_environmental_isolate_scope), and discussions[2] (argmet_noise_mechanism_expansion) raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

Disposition: Resolved in Issue #2713: populated abundance_level: DOMINANT and verbatim two-strain obligate mutualistic coculture evidence from PMID:42592155 (PMC13463769, doi:10.1093/nsr/nwag357) on both Escherichia coli K-12 MG1655 ΔargA-ΔmetJ and ΔmetA-ΔargR (NCBITaxon:511145).

### c9s4-000461-pseudomonas-acidovorax-abundance-levels: Both synthetic consortium strains in Pseudomonas_Acidovorax_Aniline_Degradation_SynCom (CommunityMech:000461) omit abundance_level despite explicit 3:1 inoculation-ratio support in PMID:41900437

major / resolved / confirmed; issue key: c9s4-000461-pseudomonas-acidovorax-abundance-levels.

In kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml (CommunityMech:000461), both Pseudomonas sp. RF (taxonomy[0], NCBITaxon:286, functional_role: [PRIMARY_DEGRADER]) and Acidovorax sp. PH (taxonomy[1], NCBITaxon:12916, functional_role: [PRIMARY_DEGRADER]) omit abundance_level. The cited open-access study (PMID:41900437, PMC13029111, doi:10.3390/microorganisms14030678) explicitly reports that 'Through orthogonal experiments to optimize the inoculation ratio, a synthetic consortium, RF-PH, composed of the two strains at a 3:1 ratio, was constructed.' Setting abundance_level: DOMINANT on taxonomy[0] (Pseudomonas sp. RF, 3:1 majority partner) and abundance_level: ABUNDANT on taxonomy[1] (Acidovorax sp. PH, 1:3 partner) while preserving discussions[0] (rf_ph_aniline_pairwise_mechanism) and discussions[1] (rf-ph-removal-versus-mineralization) raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

Disposition: Resolved in Issue #2713: populated abundance_level: DOMINANT on Pseudomonas sp. RF (NCBITaxon:286) and abundance_level: ABUNDANT on Acidovorax sp. PH (NCBITaxon:12916) with verbatim 3:1 inoculation-ratio evidence from PMID:41900437 (PMC13029111, doi:10.3390/microorganisms14030678).

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

### act-defer-source-limited-fulltext-findings-c9s5

Retain source-limited full-text findings under open GitHub issues (#765, #1467, #1657, #1681, #1699, #1841, #1847) until open-access full text or supplementary strain/assay tables become available for CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify full-text or supplementary table availability before expanding abstract-grounded claims on source-limited records.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c9s5-schema-validation | src/communitymech/schema/communitymech.yaml; MicrobialCommunity | supports | All 10 Cycle 9 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml with 0 LinkML errors, 0 GTDB coherence errors, 0 scalar errors, and 0 ontology term label errors. |
| ev-c9s5-causal-inventory | reports/causal_graph_review/decisions/20261107-c9s5-review-remediation.yaml; records[0..2] | supports | Successor causal review ledger 20261107-c9s5-review-remediation.yaml re-attests all 3 modified community records (CommunityMech:000331, 000455, 000461); reports/causal_graph_review/inventory.tsv passes all 32 inventory integrity checks (515 records, 461 reviewed, 54 needs_research, 0 stale hashes, 0 structural defects). |
| ev-c9s5-primary-sources | references_cache/; PMID:42269294, PMID:42592155, PMID:41900437 | supports | Primary source caches in references_cache/ support abundance_level: DOMINANT on both Pseudomonas aeruginosa PA (NCBITaxon:287) and Paracoccus pantotrophus PP (NCBITaxon:82367) on CommunityMech:000331 (PMID:42269294, doi:10.1016/j.jhazmat.2026.142626); abundance_level: DOMINANT on both Escherichia coli K-12 MG1655 ΔargA-ΔmetJ and ΔmetA-ΔargR (NCBITaxon:511145) on CommunityMech:000455 (PMID:42592155, PMC13463769, doi:10.1093/nsr/nwag357); and abundance_level: DOMINANT on Pseudomonas sp. RF (NCBITaxon:286) and abundance_level: ABUNDANT on Acidovorax sp. PH (NCBITaxon:12916) on CommunityMech:000461 (PMID:41900437, PMC13029111, doi:10.3390/microorganisms14030678) (#2713), while confirming that the 7 deferred records (#765, #1467, #1657, #1681, #1699, #1841, #1847) remain bounded to abstract-verified claims. |

## Limits And Additional Notes

- Seven source-limited community records (CommunityMech:000048 #1657, 000054 #1699, 000091 #1467, 000153 #765, 000222 #1841, 000295 #1681, 000302 #1847) remain deferred because primary full text or supplementary tables are paywalled or unavailable in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261107T062000Z-c9s5-remediation-verification-r2
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 9 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward
  Findings (Revision 2)
started_at: '2026-11-07T06:18:00Z'
finished_at: '2026-11-07T06:20:00Z'
reviewer:
  identity: antigravity-c9s5-remediation-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated post-remediation verification review pass over the
    10 Cycle 9 Stage 4 finding-bearing community records in the working tree.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
native_verdict: 'PASS_WITH_LIMITATIONS (3 actionable Cycle 9 Stage 4 findings resolved
  across 3 updated community records in #2713; 7 source-limited findings deferred
  under open GitHub issues)'
scientific_review: true
summary: 'Post-remediation scientific and structural verification review of all 10
  finding-bearing community records from Cycle 9 Stage 4 (3 community records across
  3 actionable open findings grouped into GitHub issue #2713, plus 7 source-limited
  deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699,
  #1841, and #1847). CommunityMech:000331 (Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml)
  now populates abundance_level: DOMINANT and verbatim two-strain synthetic consortium
  evidence from PMID:42269294 (doi:10.1016/j.jhazmat.2026.142626) on both Pseudomonas
  aeruginosa PA (taxonomy[0], NCBITaxon:287) and Paracoccus pantotrophus PP (taxonomy[1],
  NCBITaxon:82367) while preserving discussions[0] (bifenthrin-removal-versus-assimilation),
  raising its review-communities s_ab rubric component from 0/5 to 5/5 (0/2 -> 2/2
  taxa with abundance_level; Completeness Score 83/100 -> 88/100; scripts/audit_completeness.py
  score 65/100). CommunityMech:000455 (Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml)
  now populates abundance_level: DOMINANT and bracket-free verbatim two-strain obligate
  mutualistic coculture evidence from PMID:42592155 (PMC13463769, doi:10.1093/nsr/nwag357)
  on both Escherichia coli K-12 MG1655 ΔargA-ΔmetJ (taxonomy[0], NCBITaxon:511145)
  and Escherichia coli K-12 MG1655 ΔmetA-ΔargR (taxonomy[1], NCBITaxon:511145) while
  preserving discussions[0..2], raising review-communities s_ab from 0/5 to 5/5 (0/2
  -> 2/2 taxa with abundance_level; Completeness Score 83/100 -> 88/100; scripts/audit_completeness.py
  score 65/100). CommunityMech:000461 (Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml)
  now populates abundance_level: DOMINANT on Pseudomonas sp. RF (taxonomy[0], NCBITaxon:286)
  and abundance_level: ABUNDANT on Acidovorax sp. PH (taxonomy[1], NCBITaxon:12916)
  with verbatim 3:1 inoculation-ratio evidence from PMID:41900437 (PMC13029111, doi:10.3390/microorganisms14030678)
  while preserving discussions[0..1], raising review-communities s_ab from 0/5 to
  5/5 (0/2 -> 2/2 taxa with abundance_level; Completeness Score 73/100 -> 78/100;
  scripts/audit_completeness.py score 55/100). All 3 modified records are re-attested
  in reports/causal_graph_review/decisions/20261107-c9s5-review-remediation.yaml.'
source:
  git_revision: 336c2543d5c7c265e240aa695f53ce34dca59207
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
  - path: kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml
    sha256: 3097670257aa374e7bf38197c0c1528cfd4f2e0f7c6b1acbb8c33abf431500a4
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
  - path: kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml
    sha256: 1b43d889efac75c21e02af27ab2f1c94979448a7cc4c2e15cbff1ad1f6f71b68
    role: target
  - path: kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml
    sha256: f3ac3ff51d02bb342a6f48d80fa4549b22ef17b3ee7052d4694a44e84dd159f5
    role: target
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 904cc9646ae53fe0c021c1461a09f3f8d15b763edad42b6c9a43ada91c87597d
    role: target
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: reports/causal_graph_review/decisions/20261107-c9s5-review-remediation.yaml
    sha256: 1b137d9817b8018a8b9c107411d5c9ba569bde163f0f52a67270646cfecc4fe4
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: f54ad04da89342a9e272ef60e9fc3a8f307f25edc63deb0599c4b896c08e2fea
    role: context
  - path: reviews/structured/20261107T030000Z-c9s4-record-deep-audit/review.yaml
    sha256: 702a2832996d21e63f4a494d538faad935fb2c138ecdf975a3af2a03bb0232d4
    role: context
  - path: reviews/structured/20261107T030100Z-c9s4-frozen-cohort-review/review.yaml
    sha256: 1d58b7bc242788958cb34821d6cfa1d4f0cd243d1544e7f01501fe35ec73839f
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Full post-remediation verification of all 10 community records referenced
    by Cycle 9 Stage 4 findings (3 actionable finding targets + 7 carried-forward
    source-limited targets).
  selection: All 10 records referenced by carry_forward_ids and owner_paths in Cycle
    9 Stage 4 evidence.yaml.
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
  - CommunityMech:000331
  - CommunityMech:000455
  - CommunityMech:000461
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
- target_id: CommunityMech:000331
  path: kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml
  label: CommunityMech:000331 (Pseudomonas-Paracoccus Bifenthrin-Degrading Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000455
  path: kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml
  label: CommunityMech:000455 (E. coli K-12 MG1655 Arg-Met Cross-Feeding Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000461
  path: kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml
  label: CommunityMech:000461 (Pseudomonas-Acidovorax Aniline-Degradation SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
checks:
- check_id: chk-linkml-schema-c9s5
  name: LinkML schema and strict corpus validation on all 10 Cycle 9 Stage 5 target
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
  - CommunityMech:000331
  - CommunityMech:000455
  - CommunityMech:000461
  command: PYTHONPATH=src .venv/bin/python scripts/validate_strict.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c9s5-schema-validation
- check_id: chk-causal-and-participants-tests-c9s5
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
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000331
  - CommunityMech:000455
  - CommunityMech:000461
  command: .venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_participating_taxa.py
    tests/test_causal_review_inventory.py tests/test_gtdb_demoted_clades.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c9s5-causal-inventory
evidence:
- evidence_id: ev-c9s5-schema-validation
  kind: validation
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity
  accessed_at: '2026-11-07T05:18:00Z'
  support: supports
  summary: All 10 Cycle 9 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml
    with 0 LinkML errors, 0 GTDB coherence errors, 0 scalar errors, and 0 ontology
    term label errors.
- evidence_id: ev-c9s5-causal-inventory
  kind: validation
  reference: reports/causal_graph_review/decisions/20261107-c9s5-review-remediation.yaml
  locator: records[0..2]
  accessed_at: '2026-11-07T05:19:00Z'
  support: supports
  summary: Successor causal review ledger 20261107-c9s5-review-remediation.yaml re-attests
    all 3 modified community records (CommunityMech:000331, 000455, 000461); reports/causal_graph_review/inventory.tsv
    passes all 32 inventory integrity checks (515 records, 461 reviewed, 54 needs_research,
    0 stale hashes, 0 structural defects).
- evidence_id: ev-c9s5-primary-sources
  kind: primary_source
  reference: references_cache/
  locator: PMID:42269294, PMID:42592155, PMID:41900437
  accessed_at: '2026-11-07T05:19:30Z'
  support: supports
  summary: 'Primary source caches in references_cache/ support abundance_level: DOMINANT
    on both Pseudomonas aeruginosa PA (NCBITaxon:287) and Paracoccus pantotrophus
    PP (NCBITaxon:82367) on CommunityMech:000331 (PMID:42269294, doi:10.1016/j.jhazmat.2026.142626);
    abundance_level: DOMINANT on both Escherichia coli K-12 MG1655 ΔargA-ΔmetJ and
    ΔmetA-ΔargR (NCBITaxon:511145) on CommunityMech:000455 (PMID:42592155, PMC13463769,
    doi:10.1093/nsr/nwag357); and abundance_level: DOMINANT on Pseudomonas sp. RF
    (NCBITaxon:286) and abundance_level: ABUNDANT on Acidovorax sp. PH (NCBITaxon:12916)
    on CommunityMech:000461 (PMID:41900437, PMC13029111, doi:10.3390/microorganisms14030678)
    (#2713), while confirming that the 7 deferred records (#765, #1467, #1657, #1681,
    #1699, #1841, #1847) remain bounded to abstract-verified claims.'
assessments:
- assessment_id: assess-c9s5-taxonomic-abundance-levels
  area: completeness
  topic: 'Post-remediation verification of abundance_level on CommunityMech:000331,
    000455, and 000461 (Issue #2713)'
  outcome: supported
  summary: CommunityMech:000331 (review-communities s_ab 0/5 -> 5/5, Completeness
    Score 83/100 -> 88/100; scripts/audit_completeness.py score 65/100), CommunityMech:000455
    (review-communities s_ab 0/5 -> 5/5, Completeness Score 83/100 -> 88/100; scripts/audit_completeness.py
    score 65/100), and CommunityMech:000461 (review-communities s_ab 0/5 -> 5/5, Completeness
    Score 73/100 -> 78/100; scripts/audit_completeness.py score 55/100) now populate
    source-backed functional_role and abundance_level across all 6/6 TaxonomicComposition
    entries while preserving all record-level discussions.
  target_ids:
  - CommunityMech:000331
  - CommunityMech:000455
  - CommunityMech:000461
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-causal-inventory
  - ev-c9s5-primary-sources
  metrics:
  - name: remediated_taxon_abundance_level_pct
    value: 100.0
    unit: percent
    definition: Percentage of TaxonomicComposition entries across the 3 remediated
      MicrobialCommunity records carrying both populated functional_role and abundance_level
      (6/6).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-c9s5-deferred-source-limited-records
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
  - ev-c9s5-schema-validation
  - ev-c9s5-primary-sources
findings:
- finding_id: c9s4-000331-pseudomonas-paracoccus-abundance-levels
  issue_key: c9s4-000331-pseudomonas-paracoccus-abundance-levels
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Both synthetic consortium members in Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium
    (CommunityMech:000331) omit abundance_level despite defined two-strain consortium
    support in PMID:42269294
  description: 'In kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml
    (CommunityMech:000331), both Pseudomonas aeruginosa PA (taxonomy[0], NCBITaxon:287,
    functional_role: [PRIMARY_DEGRADER]) and Paracoccus pantotrophus PP (taxonomy[1],
    NCBITaxon:82367, functional_role: [PRIMARY_DEGRADER, CROSS_FEEDER]) omit abundance_level.
    The cited study (PMID:42269294, doi:10.1016/j.jhazmat.2026.142626) explicitly
    reports that ''Pseudomonas aeruginosa strain PA (PA) and Paracoccus pantotrophus
    strain PP (PP) were isolated from contaminated soil and constructed into a synthetic
    consortium (PA+PP), which synergistically enhanced bifenthrin degradation.'' Setting
    abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1] while preserving
    discussions[0] (bifenthrin-removal-versus-assimilation) raises the review-communities
    s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -> 2/2 taxa with abundance_level).'
  target_ids:
  - CommunityMech:000331
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-causal-inventory
  - ev-c9s5-primary-sources
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on both defined two-strain
    consortium members leaves the review-communities s_ab rubric component at 0/5
    (Completeness Score 83/100 -> 88/100; scripts/audit_completeness.py score 65/100)
    and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Pseudomonas_Paracoccus_Bifenthrin_Degradation_Consortium.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
  disposition_reason: 'Resolved in Issue #2713: populated abundance_level: DOMINANT
    and verbatim two-strain synthetic consortium evidence from PMID:42269294 (doi:10.1016/j.jhazmat.2026.142626)
    on both Pseudomonas aeruginosa PA (NCBITaxon:287) and Paracoccus pantotrophus
    PP (NCBITaxon:82367).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030000Z-c9s4-record-deep-audit
    finding_id: c9s4-000331-pseudomonas-paracoccus-abundance-levels
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: c9s4-000331-pseudomonas-paracoccus-abundance-levels
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2713
- finding_id: c9s4-000455-ecoli-arg-met-abundance-levels
  issue_key: c9s4-000455-ecoli-arg-met-abundance-levels
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Both engineered auxotrophic partners in Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture
    (CommunityMech:000455) omit abundance_level despite defined two-strain mutualistic
    coculture support in PMID:42592155
  description: 'In kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml
    (CommunityMech:000455), both Escherichia coli K-12 MG1655 ΔargA-ΔmetJ (taxonomy[0],
    NCBITaxon:511145, functional_role: [CROSS_FEEDER]) and Escherichia coli K-12 MG1655
    ΔmetA-ΔargR (taxonomy[1], NCBITaxon:511145, functional_role: [CROSS_FEEDER]) omit
    abundance_level. The cited open-access study (PMID:42592155, PMC13463769, doi:10.1093/nsr/nwag357)
    explicitly reports that ''we constructed a metabolic cross-feeding system consisting
    of two genetically engineered double-mutant strains of E. coli, ΔargA-ΔmetJ and
    ΔmetA-ΔargR [ 17 , 27 , 28 ].'' Setting abundance_level: DOMINANT on both taxonomy[0]
    and taxonomy[1] while preserving discussions[0] (arg_met_supplementary_protocol_details),
    discussions[1] (additional_pair_and_environmental_isolate_scope), and discussions[2]
    (argmet_noise_mechanism_expansion) raises the review-communities s_ab abundance_level
    rubric component from 0/5 to 5/5 (0/2 -> 2/2 taxa with abundance_level).'
  target_ids:
  - CommunityMech:000455
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-causal-inventory
  - ev-c9s5-primary-sources
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on both obligate mutualist
    coculture strains leaves the review-communities s_ab rubric component at 0/5 (Completeness
    Score 83/100 -> 88/100; scripts/audit_completeness.py score 65/100) and maps to
    major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Ecoli_K12_MG1655_Arg_Met_CrossFeeding_Coculture.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
  disposition_reason: 'Resolved in Issue #2713: populated abundance_level: DOMINANT
    and verbatim two-strain obligate mutualistic coculture evidence from PMID:42592155
    (PMC13463769, doi:10.1093/nsr/nwag357) on both Escherichia coli K-12 MG1655 ΔargA-ΔmetJ
    and ΔmetA-ΔargR (NCBITaxon:511145).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030000Z-c9s4-record-deep-audit
    finding_id: c9s4-000455-ecoli-arg-met-abundance-levels
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: c9s4-000455-ecoli-arg-met-abundance-levels
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2713
- finding_id: c9s4-000461-pseudomonas-acidovorax-abundance-levels
  issue_key: c9s4-000461-pseudomonas-acidovorax-abundance-levels
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Both synthetic consortium strains in Pseudomonas_Acidovorax_Aniline_Degradation_SynCom
    (CommunityMech:000461) omit abundance_level despite explicit 3:1 inoculation-ratio
    support in PMID:41900437
  description: 'In kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml
    (CommunityMech:000461), both Pseudomonas sp. RF (taxonomy[0], NCBITaxon:286, functional_role:
    [PRIMARY_DEGRADER]) and Acidovorax sp. PH (taxonomy[1], NCBITaxon:12916, functional_role:
    [PRIMARY_DEGRADER]) omit abundance_level. The cited open-access study (PMID:41900437,
    PMC13029111, doi:10.3390/microorganisms14030678) explicitly reports that ''Through
    orthogonal experiments to optimize the inoculation ratio, a synthetic consortium,
    RF-PH, composed of the two strains at a 3:1 ratio, was constructed.'' Setting
    abundance_level: DOMINANT on taxonomy[0] (Pseudomonas sp. RF, 3:1 majority partner)
    and abundance_level: ABUNDANT on taxonomy[1] (Acidovorax sp. PH, 1:3 partner)
    while preserving discussions[0] (rf_ph_aniline_pairwise_mechanism) and discussions[1]
    (rf-ph-removal-versus-mineralization) raises the review-communities s_ab abundance_level
    rubric component from 0/5 to 5/5 (0/2 -> 2/2 taxa with abundance_level).'
  target_ids:
  - CommunityMech:000461
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-causal-inventory
  - ev-c9s5-primary-sources
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on both defined RF-PH
    consortium members leaves the review-communities s_ab rubric component at 0/5
    (Completeness Score 73/100 -> 78/100; scripts/audit_completeness.py score 55/100)
    and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Pseudomonas_Acidovorax_Aniline_Degradation_SynCom.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
  disposition_reason: 'Resolved in Issue #2713: populated abundance_level: DOMINANT
    on Pseudomonas sp. RF (NCBITaxon:286) and abundance_level: ABUNDANT on Acidovorax
    sp. PH (NCBITaxon:12916) with verbatim 3:1 inoculation-ratio evidence from PMID:41900437
    (PMC13029111, doi:10.3390/microorganisms14030678).'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030000Z-c9s4-record-deep-audit
    finding_id: c9s4-000461-pseudomonas-acidovorax-abundance-levels
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: c9s4-000461-pseudomonas-acidovorax-abundance-levels
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2713
- category: evidence
  certainty: confirmed
  description: Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153)
    remains capped at abstract-verified taxa and interactions because strain-specific
    pairwise assay details in PMID:25043025 require full-text table inspection.
  disposition_reason: 'Deferred: source-limited until full-text assay tables for PMID:25043025
    are ingested (#765).'
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-primary-sources
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/765
  field_paths:
  - ecological_interactions
  finding_id: cheese-assay-evidence-gap
  issue_key: cheese-assay-evidence-gap
  native_severity: P3
  normalization_reason: Source-limited full-text assay detail gap preserved as minor.
  owner_paths:
  - path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  previous_occurrences:
  - finding_id: assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T091351Z-cheese-before
  - finding_id: assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T092604Z-cheese-after
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
  - finding_id: cheese-assay-evidence-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  rule_id: review-yaml-record:source-limited-gap
  severity: minor
  status: deferred
  tags:
  - carried-forward
  - source-limited
  target_ids:
  - CommunityMech:000153
  title: Full-text-dependent cheese rind assay specifics remain deferred in CommunityMech:000153
- category: evidence
  certainty: confirmed
  description: 'GLBRC_Exometabolite_Transwell_SynCom.yaml (CommunityMech:000091) captures
    the abstract-supported exometabolite Transwell SynCom, while full-text table reconciliation
    for the broader 18-species campaign remains open under issue #1467.'
  disposition_reason: 'Deferred: tracked in GitHub issue #1467 pending full-text table
    reconciliation.'
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-primary-sources
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1467
  field_paths:
  - taxonomy
  - ecological_interactions
  finding_id: communitymech-1467-source-discrepancy-and-extension
  issue_key: communitymech-1467-source-discrepancy-and-extension
  native_severity: P3
  normalization_reason: Source-limited full-text extension preserved as minor.
  owner_paths:
  - path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  previous_occurrences:
  - finding_id: transwell-1467
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T062338Z-transwell-before
  - finding_id: transwell-1467
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T063739Z-transwell-after
  - finding_id: transwell-1467
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T071433Z-transwell-ci-before
  - finding_id: transwell-1467
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T075024Z-transwell-ci-after
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
  - finding_id: communitymech-1467-source-discrepancy-and-extension
    repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  rule_id: review-yaml-record:source-limited-gap
  severity: minor
  status: deferred
  tags:
  - carried-forward
  - source-limited
  target_ids:
  - CommunityMech:000091
  title: Broader 18-species Transwell campaign and strain/table discrepancies in CommunityMech:000091
    require full-text audit
- category: completeness
  certainty: confirmed
  description: Phormidium_Alkaline_Consortium.yaml (CommunityMech:000054) models the
    primary cyanobacterial host and abstract-backed heterotrophic guild; additional
    heterotrophic co-isolates require full-text table verification (#1699).
  disposition_reason: 'Deferred: tracked in GitHub issue #1699 pending full-text isolate
    table verification.'
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-primary-sources
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1699
  field_paths:
  - taxonomy
  finding_id: communitymech-1699-coverage
  issue_key: communitymech-1699-coverage
  native_severity: P3
  normalization_reason: Source-limited full-text membership extension preserved as
    minor.
  owner_paths:
  - path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  previous_occurrences:
  - finding_id: phormidium-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261014T234638Z-causal-prompt-before
  - finding_id: phormidium-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261014T235318Z-causal-prompt-phormidium-after
  - finding_id: phormidium-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T011216Z-phormidium-identity-before
  - finding_id: phormidium-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T014050Z-phormidium-identity-after
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
  - finding_id: communitymech-1699-coverage
    repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  rule_id: review-yaml-record:source-limited-gap
  severity: minor
  status: deferred
  tags:
  - carried-forward
  - source-limited
  target_ids:
  - CommunityMech:000054
  title: Additional Phormidium alkaline-lake co-isolates in CommunityMech:000054 require
    full-text table verification
- category: grounding
  certainty: confirmed
  description: Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml (CommunityMech:000222)
    retains parent-rank taxa from the abstract; resolving lower-rank MAG/isolate assignments
    requires full-text supplementary tables (#1841).
  disposition_reason: 'Deferred: tracked in GitHub issue #1841 pending full-text supplementary
    strain table inspection.'
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-primary-sources
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1841
  field_paths:
  - taxonomy
  finding_id: communitymech-1841
  issue_key: communitymech-1841
  native_severity: P3
  normalization_reason: Source-limited lower-rank taxonomic grounding gap preserved
    as minor.
  owner_paths:
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  previous_occurrences:
  - finding_id: lower-rank
    repository: CultureBotAI/CommunityMech
    review_id: 20261014T200439Z-spring-parent-rank
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
  - finding_id: communitymech-1841
    repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: communitymech-1841
  rule_id: review-yaml-record:source-limited-gap
  severity: minor
  status: deferred
  tags:
  - carried-forward
  - source-limited
  target_ids:
  - CommunityMech:000222
  title: Lower-rank taxon resolution for Sulfide Spring Autotrophic CPR Biofilm (CommunityMech:000222)
    requires full-text MAG table
- category: completeness
  certainty: confirmed
  description: SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml (CommunityMech:000302)
    models the abstract-enumerated rhizobacterial taxa; full isolate membership and
    assay specifics require full-text tables (#1847).
  disposition_reason: 'Deferred: tracked in GitHub issue #1847 pending full-text membership
    and media table inspection.'
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-primary-sources
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1847
  field_paths:
  - taxonomy
  - growth_media
  finding_id: communitymech-1847-metg2-membership
  issue_key: communitymech-1847-metg2-membership
  native_severity: P3
  normalization_reason: Source-limited full-text membership/cultivation gap preserved
    as minor.
  owner_paths:
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  previous_occurrences:
  - finding_id: membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T043154Z-metg2-host-before
  - finding_id: membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T044333Z-metg2-host-after
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
  - finding_id: communitymech-1847-metg2-membership
    repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  rule_id: review-yaml-record:source-limited-gap
  severity: minor
  status: deferred
  tags:
  - carried-forward
  - source-limited
  target_ids:
  - CommunityMech:000302
  title: Complete MetG2 rhizobacteria membership and host-assay specifics in CommunityMech:000302
    require full-text tables
- category: evidence
  certainty: confirmed
  description: Okeke_Lu_Cellulolytic_Consortium.yaml (CommunityMech:000048) is grounded
    to abstract-verified cellulolytic-xylanolytic claims; full-text monoculture vs
    co-culture enzyme assay parameters remain paywalled.
  disposition_reason: 'Deferred: source-limited because primary full text is paywalled
    (#1657).'
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-primary-sources
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1657
  field_paths:
  - ecological_interactions
  - growth_media
  finding_id: okeke-fulltext-assay-gap
  issue_key: okeke-fulltext-assay-gap
  native_severity: P3
  normalization_reason: Paywalled full-text assay detail gap preserved as minor.
  owner_paths:
  - path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  previous_occurrences:
  - finding_id: source-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T105803Z-okeke-before
  - finding_id: source-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T110432Z-okeke-after
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
  - finding_id: okeke-fulltext-assay-gap
    repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  rule_id: review-yaml-record:source-limited-gap
  severity: minor
  status: deferred
  tags:
  - carried-forward
  - source-limited
  target_ids:
  - CommunityMech:000048
  title: Paywalled full-text assay parameters for Okeke-Lu cellulolytic consortium
    (CommunityMech:000048) remain deferred
- category: evidence
  certainty: confirmed
  description: Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml (CommunityMech:000295)
    captures the primary abstract-supported algal-yeast mutualism; secondary metabolite
    exchange kinetics require full-text tables.
  disposition_reason: 'Deferred: source-limited pending full-text interaction data
    (#1681).'
  evidence_ids:
  - ev-c9s5-schema-validation
  - ev-c9s5-primary-sources
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
  field_paths:
  - ecological_interactions
  finding_id: parachlorella-remaining-research
  issue_key: parachlorella-remaining-research
  native_severity: P3
  normalization_reason: Source-limited full-text interaction detail gap preserved
    as minor.
  owner_paths:
  - path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    repository: CultureBotAI/CommunityMech
    role: canonical_record
  previous_occurrences:
  - finding_id: remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T133733Z-parachlorella-before
  - finding_id: remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261015T134821Z-parachlorella-after
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T101100Z-stage4-frozen-cohort-review
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261021T193000Z-stage5-remediation-verification
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261025T161500Z-c2s5-remediation-verification
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261026T063100Z-c3s4-frozen-cohort-review
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T081500Z-c3s5-remediation-verification
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T200100Z-c4s4-frozen-cohort-review
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261031T235500Z-c4s5-remediation-verification
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T034100Z-c5s4-frozen-cohort-review
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T060000Z-c5s5-remediation-verification
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
  - finding_id: parachlorella-remaining-research
    repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T171000Z-c7s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T094100Z-c8s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261106T114000Z-c8s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T030100Z-c9s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  rule_id: review-yaml-record:source-limited-gap
  severity: minor
  status: deferred
  tags:
  - carried-forward
  - source-limited
  target_ids:
  - CommunityMech:000295
  title: Secondary metabolite exchange specifics in Parachlorella-Saccharomyces co-culture
    (CommunityMech:000295) require full-text data
actions:
- action_id: act-defer-source-limited-fulltext-findings-c9s5
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
  review_id: 20261107T030000Z-c9s4-record-deep-audit
  relationship: supersedes_stage4_deep_audit
- repository: CultureBotAI/CommunityMech
  review_id: 20261107T030100Z-c9s4-frozen-cohort-review
  relationship: supersedes_stage4_cohort_review
- repository: CultureBotAI/CommunityMech
  review_id: 20261107T052000Z-c9s5-remediation-verification
  relationship: supersedes_stage5_revision1_review
tags:
- cycle9
- stage5
- remediation-verification
- record-review
```
