# Cycle 2 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward Findings

- Review: 20261025T161500Z-c2s5-remediation-verification
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-25T16:00:00Z
- Finished UTC: 2026-10-25T16:15:00Z
- Reviewer: antigravity-c2s5-remediation-reviewer (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Post-remediation scientific and structural verification review of all 17 finding-bearing community records and 2 reusable taxon records from Cycle 2 Stage 4 (10 community records across 3 actionable open findings grouped into GitHub issues #2072 and #2073, plus 7 source-limited deferred community records tracked in open issues #765, #1467, #1657, #1681, #1699, #1841, and #1847). All 4 BioModels host-associated community models (CommunityMech:000006, 000007, 000008, 000013) now populate top-level environment_term (ENVO:01001002 animal-associated environment) backed by PMID:30254121 and PMID:39738126 (#2072), bringing corpus-wide environment_term coverage to 484/484 (100%). All 4 Geobacter sulfurreducens communities (CommunityMech:000031, 000175, 000176, 000268) and 2 Shewanella oneidensis communities (CommunityMech:000288, 000294) now link their respective TaxonomicComposition entries to CommunityMech:taxon:000002 and CommunityMech:taxon:000001 (#2073), bringing corpus-wide common_taxon linkage for both reusable taxon records to 100% (6/6 and 9/9). All 10 modified records are re-attested in reports/causal_graph_review/decisions/20261025-c2s5-review-remediation.yaml.

## Scope And Provenance

Full post-remediation verification of all 17 community records and 2 reusable taxon records referenced by Cycle 2 Stage 4 findings (10 actionable finding targets + 2 reusable taxon records + 7 carried-forward source-limited targets).

Selection: All 19 records referenced by carry_forward_ids and owner_paths in Cycle 2 Stage 4 evidence.yaml.
Coverage: full; 19 reviewed / 19 in the declared population.
Source: working_tree at Git base 905b058f39f76994eed1ea541dfa1d31eb4d2931.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000006 | kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml | maintained | CommunityMech:000006 (BioModels MODEL1806250003 Spittlebug Sulcia-Sodalis Symbiosis) |
| CommunityMech:000007 | kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml | maintained | CommunityMech:000007 (BioModels MODEL1806250004 Sharpshooter Sulcia-Baumannia Symbiosis) |
| CommunityMech:000008 | kb/communities/BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml | maintained | CommunityMech:000008 (BioModels MODEL1806250005 Cicada Sulcia-Hodgkinia Symbiosis) |
| CommunityMech:000013 | kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml | maintained | CommunityMech:000013 (BioModels MODEL2407300002 Sponge Holobiont Network) |
| CommunityMech:000031 | kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml | maintained | CommunityMech:000031 (Geobacter-Clostridium Interspecies Electron Transfer Coculture) |
| CommunityMech:000048 | kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml | maintained | CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium) |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | CommunityMech:000054 (Phormidium Alkaline Consortium) |
| CommunityMech:000091 | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml | maintained | CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System) |
| CommunityMech:000153 | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml | maintained | CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community) |
| CommunityMech:000175 | kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml | maintained | CommunityMech:000175 (Clostridium cellulolyticum-Geobacter sulfurreducens Cellulose MFC Coculture) |
| CommunityMech:000176 | kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml | maintained | CommunityMech:000176 (ORNL Clostridium-Desulfovibrio-Geobacter Trophic Model Community) |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml | maintained | CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm) |
| CommunityMech:000268 | kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml | maintained | CommunityMech:000268 (Rhodopseudomonas-Geobacter Magnetite Redox Coculture) |
| CommunityMech:000288 | kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml | maintained | CommunityMech:000288 (Shewanella oneidensis + Pseudomonas aeruginosa Fe0-dependent Electro-syntrophic Denitrifying Consortium) |
| CommunityMech:000294 | kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml | maintained | CommunityMech:000294 (Corynebacterium glutamicum + Shewanella oneidensis Succinic-acid Co-culture) |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic Co-culture) |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience) |
| CommunityMech:taxon:000001 | kb/taxa/Shewanella_oneidensis_MR1.yaml | maintained | CommunityMech:taxon:000001 (CommunityMech:taxon:000001) |
| CommunityMech:taxon:000002 | kb/taxa/Geobacter_sulfurreducens.yaml | maintained | CommunityMech:taxon:000002 (CommunityMech:taxon:000002) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema and strict corpus validation on all 19 Cycle 2 Stage 5 target records | passed | True | CommunityMech:000006, CommunityMech:000007, CommunityMech:000008, CommunityMech:000013, CommunityMech:000031, CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000175, CommunityMech:000176, CommunityMech:000222, CommunityMech:000268, CommunityMech:000288, CommunityMech:000294, CommunityMech:000295, CommunityMech:000302, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 17 MicrobialCommunity target records and 2 TaxonRecord target files validate against src/communitymech/schema/communitymech.yaml with 0 errors. |
| Causal review inventory, reusable taxon linkage, and batch regression tests | passed | True | CommunityMech:000006, CommunityMech:000007, CommunityMech:000008, CommunityMech:000013, CommunityMech:000031, CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000175, CommunityMech:000176, CommunityMech:000222, CommunityMech:000268, CommunityMech:000288, CommunityMech:000294, CommunityMech:000295, CommunityMech:000302, CommunityMech:taxon:000001, CommunityMech:taxon:000002 | All 173 pytest checks across test_taxon_records.py, test_causal_review_inventory.py, and test_causal_review_batch{19,24,45,78,91,94,101}.py pass with 0 failures. |

## Scientific And Domain Assessments

### Post-remediation verification of environment_term grounding on BioModels host-associated community models (Issue #2072)

completeness: supported. Targets: CommunityMech:000006, CommunityMech:000007, CommunityMech:000008, CommunityMech:000013.

CommunityMech:000006 (80/100), CommunityMech:000007 (80/100), CommunityMech:000008 (80/100), and CommunityMech:000013 (80/100) now populate environment_term with ENVO:01001002 (animal-associated environment) and source-backed host habitat notes (PMID:30254121 sap-feeding insect bacteriome symbioses and PMID:39738126 Red Sea Stylissa sp. marine sponge holobiont), raising each record's calculate_completeness score from 75/100 to 80/100 (+5 points) and achieving 100% environment_term coverage across all 484 MicrobialCommunity records.

### Post-remediation verification of reusable CommonTaxon linkage for Geobacter sulfurreducens and Shewanella oneidensis (Issue #2073)

grounding: supported. Targets: CommunityMech:000031, CommunityMech:000175, CommunityMech:000176, CommunityMech:000268, CommunityMech:000288, CommunityMech:000294, CommunityMech:taxon:000001, CommunityMech:taxon:000002.

CommunityMech:000031, 000175, 000176, and 000268 now link their Geobacter sulfurreducens (NCBITaxon:35554) TaxonomicComposition entry to CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml, 6/6 communities linked), and CommunityMech:000288 and 000294 now link their Shewanella oneidensis (NCBITaxon:211586 / NCBITaxon:70863) TaxonomicComposition entry to CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml, 9/9 communities linked).

### Verification of abstract-grounded integrity on 7 source-limited deferred community records (#765, #1467, #1657, #1681, #1699, #1841, #1847)

evidence: supported. Targets: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302.

All 7 source-limited records (CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, 000302) remain valid against LinkML and grounded strictly to verbatim abstract claims without fabrication while their full-text/supplementary data gaps remain tracked in open GitHub issues.

## Findings

### c2s4-biomodels-missing-environment-term: Four BioModels community records (CommunityMech:000006, 000007, 000008, 000013) omit environment_term despite explicit host-associated habitat context in cited sources

major / resolved / confirmed; issue key: communitymech-c2s4-biomodels-missing-environment-term.

Out of all 484 MicrobialCommunity records across kb/communities/ (477) and data/isolates/ (7), only 4 records omitted top-level environment_term: CommunityMech:000006 (BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml), CommunityMech:000007 (BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml), CommunityMech:000008 (BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml), and CommunityMech:000013 (BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml). The cited primary sources explicitly establish obligate sap-feeding insect bacteriome symbioses (PMID:30254121 for 000006-000008) and a Stylissa sp. marine sponge holobiont (PMID:39738126 for 000013), supporting ENVO:01001002 (animal-associated environment).

Disposition: Resolved in Issue #2072: populated environment_term with ENVO:01001002 (animal-associated environment) and source-backed host habitat notes on CommunityMech:000006, 000007, 000008 (PMID:30254121) and CommunityMech:000013 (PMID:39738126), regenerated HTML pages, and recorded append-only curation history.

### c2s4-geobacter-common-taxon-linkage-gap: Four Geobacter sulfurreducens community records (CommunityMech:000031, 000175, 000176, 000268) omit common_taxon linkage to CommunityMech:taxon:000002

minor / resolved / confirmed; issue key: communitymech-c2s4-geobacter-common-taxon-linkage-gap.

Four syntrophic/electroactive community records containing Geobacter sulfurreducens (NCBITaxon:35554) — CommunityMech:000031, 000175, 000176, and 000268 — omitted common_taxon: CommunityMech:taxon:000002 linking to kb/taxa/Geobacter_sulfurreducens.yaml.

Disposition: Resolved in Issue #2073: linked Geobacter sulfurreducens (NCBITaxon:35554) TaxonomicComposition entries in CommunityMech:000031, 000175, 000176, and 000268 to common_taxon: CommunityMech:taxon:000002 and recorded append-only curation history.

### c2s4-shewanella-common-taxon-linkage-gap: Two Shewanella oneidensis community records (CommunityMech:000288, 000294) omit common_taxon linkage to CommunityMech:taxon:000001

minor / resolved / confirmed; issue key: communitymech-c2s4-shewanella-common-taxon-linkage-gap.

Two community records containing Shewanella oneidensis (NCBITaxon:211586 / NCBITaxon:70863) — CommunityMech:000288 and 000294 — omitted common_taxon: CommunityMech:taxon:000001 linking to kb/taxa/Shewanella_oneidensis_MR1.yaml.

Disposition: Resolved in Issue #2073: linked Shewanella oneidensis TaxonomicComposition entries in CommunityMech:000288 and 000294 to common_taxon: CommunityMech:taxon:000001 and recorded append-only curation history.

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

### act-defer-source-limited-fulltext-findings-c2s5

Retain source-limited full-text findings under open GitHub issues (#765, #1467, #1657, #1681, #1699, #1841, #1847) until open-access full text or supplementary strain/assay tables become available for CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify full-text or supplementary table availability before expanding abstract-grounded claims on source-limited records.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c2s5-schema-validation | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and TaxonRecord | supports | All 19 Cycle 2 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml with 0 LinkML errors and 100% corpus-wide environment_term coverage (484/484). |
| ev-c2s5-taxon-linkage | tests/test_taxon_records.py; EXPECTED_COMMUNITY_REFS | supports | All 6 Geobacter sulfurreducens community records link to CommunityMech:taxon:000002 (kb/taxa/Geobacter_sulfurreducens.yaml) and all 9 Shewanella oneidensis community records link to CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml) with 0 NCBITaxon ID mismatches. |
| ev-c2s5-causal-inventory | reports/causal_graph_review/decisions/20261025-c2s5-review-remediation.yaml; records[0..9] | supports | Successor causal review ledger 20261025-c2s5-review-remediation.yaml re-attests all 10 modified community records; reports/causal_graph_review/inventory.tsv passes all 32 inventory integrity checks with 0 stale hashes and 0 structural defects. |
| ev-c2s5-primary-sources | references_cache/; PMID:30254121, PMID:39738126, PMID:9501201, PMID:19801417, PMID:26527636, PMID:26668068, PMID:37721157, PMID:41908926 | supports | Primary source abstracts and metadata support ENVO:01001002 (animal-associated environment) on CommunityMech:000006, 000007, 000008 (PMID:30254121) and 000013 (PMID:39738126) (#2072), support common_taxon linkage on CommunityMech:000031, 000175, 000176, 000268, 000288, and 000294 (#2073), and confirm that the 7 deferred records (#765, #1467, #1657, #1681, #1699, #1841, #1847) remain bounded to abstract-verified claims pending paywalled/supplementary full text. |

## Limits And Additional Notes

- Seven source-limited community records (CommunityMech:000048 #1657, 000054 #1699, 000091 #1467, 000153 #765, 000222 #1841, 000295 #1681, 000302 #1847) remain deferred because primary full text or supplementary tables are paywalled or unavailable in references_cache/.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T161500Z-c2s5-remediation-verification
kind: batch
repository: CultureBotAI/CommunityMech
title: Cycle 2 Stage 5 Post-Remediation Verification Review of Actionable and Carried-Forward
  Findings
started_at: '2026-10-25T16:00:00Z'
finished_at: '2026-10-25T16:15:00Z'
reviewer:
  identity: antigravity-c2s5-remediation-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated post-remediation verification review pass over the
    17 Cycle 2 Stage 4 finding-bearing community records and 2 reusable taxon records
    in the working tree.
skill: review-yaml-record
completion: completed
verdict: pass_with_limitations
native_verdict: PASS_WITH_LIMITATIONS (3 actionable Cycle 2 Stage 4 findings resolved
  across 10 updated community records and 2 verified reusable taxon records; 7 source-limited
  findings deferred under open GitHub issues)
scientific_review: true
summary: 'Post-remediation scientific and structural verification review of all 17
  finding-bearing community records and 2 reusable taxon records from Cycle 2 Stage
  4 (10 community records across 3 actionable open findings grouped into GitHub issues
  #2072 and #2073, plus 7 source-limited deferred community records tracked in open
  issues #765, #1467, #1657, #1681, #1699, #1841, and #1847). All 4 BioModels host-associated
  community models (CommunityMech:000006, 000007, 000008, 000013) now populate top-level
  environment_term (ENVO:01001002 animal-associated environment) backed by PMID:30254121
  and PMID:39738126 (#2072), bringing corpus-wide environment_term coverage to 484/484
  (100%). All 4 Geobacter sulfurreducens communities (CommunityMech:000031, 000175,
  000176, 000268) and 2 Shewanella oneidensis communities (CommunityMech:000288, 000294)
  now link their respective TaxonomicComposition entries to CommunityMech:taxon:000002
  and CommunityMech:taxon:000001 (#2073), bringing corpus-wide common_taxon linkage
  for both reusable taxon records to 100% (6/6 and 9/9). All 10 modified records are
  re-attested in reports/causal_graph_review/decisions/20261025-c2s5-review-remediation.yaml.'
source:
  git_revision: 905b058f39f76994eed1ea541dfa1d31eb4d2931
  state: working_tree
  inputs:
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml
    sha256: bb94d58347b0bbc04ebf7c25563d1096efbbd3294a3801e3732e0c95c61e6a24
    role: target
  - path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    sha256: 9cbcf07ed58d956c7b6da920f88893ba96bcad2d481afbda647e56ea7340f9ac
    role: target
  - path: kb/communities/BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml
    sha256: 9f46ee662ca63b493b279b687a38603b5a517160f17b6f3d8ef44ea647318220
    role: target
  - path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    sha256: 2d2c5858211115cc74035f627a0a51376c22703929bfae077ebada161c6924c8
    role: target
  - path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    sha256: e4ccd373cf107383615b6f207ceb0521c83b4c97daf57c6700a441b2392ddda3
    role: target
  - path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    sha256: 20a878c274695f48d5ad4fd8fe4475e576d4210926f3a9cb901ff85001bf3eff
    role: target
  - path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    sha256: 12ec7d94161d772e79598564ae50e6f322c9cfd82e889a2fd5e0fbcde687f8f6
    role: target
  - path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    sha256: 51bf55d56342aa28864c0dd458a172209f9ef1e14e51a0cd210bb46521a17f47
    role: target
  - path: kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml
    sha256: c4d14762f14174fa4f51e7921d8c2c2105f141e12ca78451f39ade949ceabcd7
    role: target
  - path: kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml
    sha256: fdd3d6c6e4fccd5b1416af814ec60609f0353ddc01d5d3e6ec88b4b83da94edc
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
  - path: kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml
    sha256: 143da9f7c6ce3d97701a9de829b13b48eead9113266dbf191c51f1e6f11d0912
    role: target
  - path: kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml
    sha256: 9bdfc9d2f4aa351bf677c6d1b8838738592fe1b7358798860cd13d6bc10472ce
    role: target
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 904cc9646ae53fe0c021c1461a09f3f8d15b763edad42b6c9a43ada91c87597d
    role: target
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: kb/taxa/Geobacter_sulfurreducens.yaml
    sha256: b3e02ec32304b400312e5320a64bbd963b9667c175c019a3cc5bd7bbdb1979a9
    role: target
  - path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    sha256: abc63353af993a7e23f1e676dca15c7012add80ac20cb8827284a32ddbcc95bf
    role: target
  - path: reports/causal_graph_review/decisions/20261025-c2s5-review-remediation.yaml
    sha256: 1296c3021a25078a1a02b3d6554e71e455ba69d157c935c16d6ef6d3c02c348f
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: 4b0feafc41d8cdd53bf8e6513379ac5c81ba1e85aa31bdedce788b0e5fe80194
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Full post-remediation verification of all 17 community records and
    2 reusable taxon records referenced by Cycle 2 Stage 4 findings (10 actionable
    finding targets + 2 reusable taxon records + 7 carried-forward source-limited
    targets).
  selection: All 19 records referenced by carry_forward_ids and owner_paths in Cycle
    2 Stage 4 evidence.yaml.
  coverage: full
  population_size: 19
  reviewed_target_ids:
  - CommunityMech:000006
  - CommunityMech:000007
  - CommunityMech:000008
  - CommunityMech:000013
  - CommunityMech:000031
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000175
  - CommunityMech:000176
  - CommunityMech:000222
  - CommunityMech:000268
  - CommunityMech:000288
  - CommunityMech:000294
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
targets:
- target_id: CommunityMech:000006
  path: kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml
  label: CommunityMech:000006 (BioModels MODEL1806250003 Spittlebug Sulcia-Sodalis
    Symbiosis)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000007
  path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
  label: CommunityMech:000007 (BioModels MODEL1806250004 Sharpshooter Sulcia-Baumannia
    Symbiosis)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000008
  path: kb/communities/BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml
  label: CommunityMech:000008 (BioModels MODEL1806250005 Cicada Sulcia-Hodgkinia Symbiosis)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000013
  path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
  label: CommunityMech:000013 (BioModels MODEL2407300002 Sponge Holobiont Network)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000031
  path: kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml
  label: CommunityMech:000031 (Geobacter-Clostridium Interspecies Electron Transfer
    Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
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
- target_id: CommunityMech:000175
  path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
  label: CommunityMech:000175 (Clostridium cellulolyticum-Geobacter sulfurreducens
    Cellulose MFC Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000176
  path: kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml
  label: CommunityMech:000176 (ORNL Clostridium-Desulfovibrio-Geobacter Trophic Model
    Community)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000222
  path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
  label: CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000268
  path: kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml
  label: CommunityMech:000268 (Rhodopseudomonas-Geobacter Magnetite Redox Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000288
  path: kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml
  label: CommunityMech:000288 (Shewanella oneidensis + Pseudomonas aeruginosa Fe0-dependent
    Electro-syntrophic Denitrifying Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000294
  path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
  label: CommunityMech:000294 (Corynebacterium glutamicum + Shewanella oneidensis
    Succinic-acid Co-culture)
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
- target_id: CommunityMech:taxon:000001
  path: kb/taxa/Shewanella_oneidensis_MR1.yaml
  label: CommunityMech:taxon:000001 (CommunityMech:taxon:000001)
  record_class: TaxonRecord
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:taxon:000002
  path: kb/taxa/Geobacter_sulfurreducens.yaml
  label: CommunityMech:taxon:000002 (CommunityMech:taxon:000002)
  record_class: TaxonRecord
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
checks:
- check_id: chk-linkml-schema-c2s5
  name: LinkML schema and strict corpus validation on all 19 Cycle 2 Stage 5 target
    records
  status: passed
  required: true
  summary: All 17 MicrobialCommunity target records and 2 TaxonRecord target files
    validate against src/communitymech/schema/communitymech.yaml with 0 errors.
  target_ids:
  - CommunityMech:000006
  - CommunityMech:000007
  - CommunityMech:000008
  - CommunityMech:000013
  - CommunityMech:000031
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000175
  - CommunityMech:000176
  - CommunityMech:000222
  - CommunityMech:000268
  - CommunityMech:000288
  - CommunityMech:000294
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  command: PYTHONPATH=src .venv/bin/python scripts/validate_strict.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c2s5-schema-validation
- check_id: chk-causal-and-taxon-tests-c2s5
  name: Causal review inventory, reusable taxon linkage, and batch regression tests
  status: passed
  required: true
  summary: All 173 pytest checks across test_taxon_records.py, test_causal_review_inventory.py,
    and test_causal_review_batch{19,24,45,78,91,94,101}.py pass with 0 failures.
  target_ids:
  - CommunityMech:000006
  - CommunityMech:000007
  - CommunityMech:000008
  - CommunityMech:000013
  - CommunityMech:000031
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000175
  - CommunityMech:000176
  - CommunityMech:000222
  - CommunityMech:000268
  - CommunityMech:000288
  - CommunityMech:000294
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  command: .venv/bin/pytest -o cache_dir=/tmp/pytest_cache tests/test_taxon_records.py
    tests/test_causal_review_inventory.py tests/test_causal_review_batch19.py tests/test_causal_review_batch24.py
    tests/test_causal_review_batch45.py tests/test_causal_review_batch78.py tests/test_causal_review_batch91.py
    tests/test_causal_review_batch94.py tests/test_causal_review_batch101.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-c2s5-taxon-linkage
  - ev-c2s5-causal-inventory
evidence:
- evidence_id: ev-c2s5-schema-validation
  kind: validation
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity and TaxonRecord
  accessed_at: '2026-10-25T16:05:00Z'
  support: supports
  summary: All 19 Cycle 2 Stage 5 target YAML records validate cleanly against src/communitymech/schema/communitymech.yaml
    with 0 LinkML errors and 100% corpus-wide environment_term coverage (484/484).
- evidence_id: ev-c2s5-taxon-linkage
  kind: validation
  reference: tests/test_taxon_records.py
  locator: EXPECTED_COMMUNITY_REFS
  accessed_at: '2026-10-25T16:06:00Z'
  support: supports
  summary: All 6 Geobacter sulfurreducens community records link to CommunityMech:taxon:000002
    (kb/taxa/Geobacter_sulfurreducens.yaml) and all 9 Shewanella oneidensis community
    records link to CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml)
    with 0 NCBITaxon ID mismatches.
- evidence_id: ev-c2s5-causal-inventory
  kind: validation
  reference: reports/causal_graph_review/decisions/20261025-c2s5-review-remediation.yaml
  locator: records[0..9]
  accessed_at: '2026-10-25T16:07:00Z'
  support: supports
  summary: Successor causal review ledger 20261025-c2s5-review-remediation.yaml re-attests
    all 10 modified community records; reports/causal_graph_review/inventory.tsv passes
    all 32 inventory integrity checks with 0 stale hashes and 0 structural defects.
- evidence_id: ev-c2s5-primary-sources
  kind: primary_source
  reference: references_cache/
  locator: PMID:30254121, PMID:39738126, PMID:9501201, PMID:19801417, PMID:26527636,
    PMID:26668068, PMID:37721157, PMID:41908926
  accessed_at: '2026-10-25T16:08:00Z'
  support: supports
  summary: 'Primary source abstracts and metadata support ENVO:01001002 (animal-associated
    environment) on CommunityMech:000006, 000007, 000008 (PMID:30254121) and 000013
    (PMID:39738126) (#2072), support common_taxon linkage on CommunityMech:000031,
    000175, 000176, 000268, 000288, and 000294 (#2073), and confirm that the 7 deferred
    records (#765, #1467, #1657, #1681, #1699, #1841, #1847) remain bounded to abstract-verified
    claims pending paywalled/supplementary full text.'
assessments:
- assessment_id: assess-c2s5-biomodels-environment-term
  area: completeness
  topic: 'Post-remediation verification of environment_term grounding on BioModels
    host-associated community models (Issue #2072)'
  outcome: supported
  summary: CommunityMech:000006 (80/100), CommunityMech:000007 (80/100), CommunityMech:000008
    (80/100), and CommunityMech:000013 (80/100) now populate environment_term with
    ENVO:01001002 (animal-associated environment) and source-backed host habitat notes
    (PMID:30254121 sap-feeding insect bacteriome symbioses and PMID:39738126 Red Sea
    Stylissa sp. marine sponge holobiont), raising each record's calculate_completeness
    score from 75/100 to 80/100 (+5 points) and achieving 100% environment_term coverage
    across all 484 MicrobialCommunity records.
  target_ids:
  - CommunityMech:000006
  - CommunityMech:000007
  - CommunityMech:000008
  - CommunityMech:000013
  evidence_ids:
  - ev-c2s5-schema-validation
  - ev-c2s5-causal-inventory
  - ev-c2s5-primary-sources
  metrics:
  - name: environment_term_coverage_pct
    value: 100.0
    unit: percent
    definition: Percentage of MicrobialCommunity records in CommunityMech with populated
      top-level environment_term (484/484).
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-c2s5-reusable-taxon-linkage
  area: grounding
  topic: 'Post-remediation verification of reusable CommonTaxon linkage for Geobacter
    sulfurreducens and Shewanella oneidensis (Issue #2073)'
  outcome: supported
  summary: CommunityMech:000031, 000175, 000176, and 000268 now link their Geobacter
    sulfurreducens (NCBITaxon:35554) TaxonomicComposition entry to CommunityMech:taxon:000002
    (kb/taxa/Geobacter_sulfurreducens.yaml, 6/6 communities linked), and CommunityMech:000288
    and 000294 now link their Shewanella oneidensis (NCBITaxon:211586 / NCBITaxon:70863)
    TaxonomicComposition entry to CommunityMech:taxon:000001 (kb/taxa/Shewanella_oneidensis_MR1.yaml,
    9/9 communities linked).
  target_ids:
  - CommunityMech:000031
  - CommunityMech:000175
  - CommunityMech:000176
  - CommunityMech:000268
  - CommunityMech:000288
  - CommunityMech:000294
  - CommunityMech:taxon:000001
  - CommunityMech:taxon:000002
  evidence_ids:
  - ev-c2s5-schema-validation
  - ev-c2s5-taxon-linkage
  - ev-c2s5-causal-inventory
  - ev-c2s5-primary-sources
  metrics:
  - name: common_taxon_linkage_coverage_pct
    value: 100.0
    unit: percent
    definition: Percentage of Geobacter sulfurreducens (6/6) and Shewanella oneidensis
      (9/9) community records linked to their canonical reusable TaxonRecord.
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-c2s5-deferred-source-limited-records
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
  - ev-c2s5-schema-validation
  - ev-c2s5-primary-sources
findings:
- finding_id: c2s4-biomodels-missing-environment-term
  issue_key: communitymech-c2s4-biomodels-missing-environment-term
  category: completeness
  severity: major
  status: resolved
  certainty: confirmed
  title: Four BioModels community records (CommunityMech:000006, 000007, 000008, 000013)
    omit environment_term despite explicit host-associated habitat context in cited
    sources
  description: 'Out of all 484 MicrobialCommunity records across kb/communities/ (477)
    and data/isolates/ (7), only 4 records omitted top-level environment_term: CommunityMech:000006
    (BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml), CommunityMech:000007
    (BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml), CommunityMech:000008
    (BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml), and CommunityMech:000013
    (BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml). The cited primary sources
    explicitly establish obligate sap-feeding insect bacteriome symbioses (PMID:30254121
    for 000006-000008) and a Stylissa sp. marine sponge holobiont (PMID:39738126 for
    000013), supporting ENVO:01001002 (animal-associated environment).'
  target_ids:
  - CommunityMech:000006
  - CommunityMech:000007
  - CommunityMech:000008
  - CommunityMech:000013
  field_paths:
  - environment_term
  evidence_ids:
  - ev-c2s5-schema-validation
  - ev-c2s5-causal-inventory
  - ev-c2s5-primary-sources
  rule_id: review-communities:completeness-environment-term
  native_severity: P2
  normalization_reason: CommunityMech P2 (missing core 10-point environment_term grounding
    on 4 host-associated community records) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250004_Sharpshooter_Sulcia_Baumannia.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL1806250005_Cicada_Sulcia_Hodgkinia.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/BioModels_MODEL2407300002_Sponge_Holobiont_Network.yaml
    role: canonical_record
  tags:
  - completeness
  - grounding
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2072: populated environment_term with ENVO:01001002
    (animal-associated environment) and source-backed host habitat notes on CommunityMech:000006,
    000007, 000008 (PMID:30254121) and CommunityMech:000013 (PMID:39738126), regenerated
    HTML pages, and recorded append-only curation history.'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113500Z-c2s4-record-deep-audit
    finding_id: c2s4-biomodels-missing-environment-term
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: c2s4-biomodels-missing-environment-term
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2072
- finding_id: c2s4-geobacter-common-taxon-linkage-gap
  issue_key: communitymech-c2s4-geobacter-common-taxon-linkage-gap
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: Four Geobacter sulfurreducens community records (CommunityMech:000031, 000175,
    000176, 000268) omit common_taxon linkage to CommunityMech:taxon:000002
  description: 'Four syntrophic/electroactive community records containing Geobacter
    sulfurreducens (NCBITaxon:35554) — CommunityMech:000031, 000175, 000176, and 000268
    — omitted common_taxon: CommunityMech:taxon:000002 linking to kb/taxa/Geobacter_sulfurreducens.yaml.'
  target_ids:
  - CommunityMech:000031
  - CommunityMech:000175
  - CommunityMech:000176
  - CommunityMech:000268
  - CommunityMech:taxon:000002
  field_paths:
  - taxonomy[].common_taxon
  evidence_ids:
  - ev-c2s5-schema-validation
  - ev-c2s5-taxon-linkage
  - ev-c2s5-causal-inventory
  rule_id: review-yaml-record:reusable-taxon-linkage
  native_severity: P3
  normalization_reason: CommunityMech P3 (missing optional reusable common_taxon cross-reference
    to kb/taxa/Geobacter_sulfurreducens.yaml) maps to minor.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Geobacter_Clostridium_Interspecies_Electron_Transfer_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Clostridium_Cellulolyticum_Geobacter_Cellulose_MFC_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/ORNL_Clostridium_Desulfovibrio_Geobacter_Trophic_Model.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Rhodopseudomonas_Geobacter_Magnetite_Redox_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/taxa/Geobacter_sulfurreducens.yaml
    role: canonical_record
  tags:
  - grounding
  - taxa-linkage
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2073: linked Geobacter sulfurreducens (NCBITaxon:35554)
    TaxonomicComposition entries in CommunityMech:000031, 000175, 000176, and 000268
    to common_taxon: CommunityMech:taxon:000002 and recorded append-only curation
    history.'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113500Z-c2s4-record-deep-audit
    finding_id: c2s4-geobacter-common-taxon-linkage-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: c2s4-geobacter-common-taxon-linkage-gap
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2073
- finding_id: c2s4-shewanella-common-taxon-linkage-gap
  issue_key: communitymech-c2s4-shewanella-common-taxon-linkage-gap
  category: grounding
  severity: minor
  status: resolved
  certainty: confirmed
  title: Two Shewanella oneidensis community records (CommunityMech:000288, 000294)
    omit common_taxon linkage to CommunityMech:taxon:000001
  description: 'Two community records containing Shewanella oneidensis (NCBITaxon:211586
    / NCBITaxon:70863) — CommunityMech:000288 and 000294 — omitted common_taxon: CommunityMech:taxon:000001
    linking to kb/taxa/Shewanella_oneidensis_MR1.yaml.'
  target_ids:
  - CommunityMech:000288
  - CommunityMech:000294
  - CommunityMech:taxon:000001
  field_paths:
  - taxonomy[].common_taxon
  evidence_ids:
  - ev-c2s5-schema-validation
  - ev-c2s5-taxon-linkage
  - ev-c2s5-causal-inventory
  rule_id: review-yaml-record:reusable-taxon-linkage
  native_severity: P3
  normalization_reason: CommunityMech P3 (missing optional reusable common_taxon cross-reference
    to kb/taxa/Shewanella_oneidensis_MR1.yaml) maps to minor.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Shewanella_Pseudomonas_Fe0_Electrosyntrophic_Denitrifying_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Corynebacterium_glutamicum_Shewanella_oneidensis_Succinic_Acid_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    role: canonical_record
  tags:
  - grounding
  - taxa-linkage
  - stage5-remediation
  disposition_reason: 'Resolved in Issue #2073: linked Shewanella oneidensis TaxonomicComposition
    entries in CommunityMech:000288 and 000294 to common_taxon: CommunityMech:taxon:000001
    and recorded append-only curation history.'
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113500Z-c2s4-record-deep-audit
    finding_id: c2s4-shewanella-common-taxon-linkage-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261025T113600Z-c2s4-frozen-cohort-review
    finding_id: c2s4-shewanella-common-taxon-linkage-gap
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2073
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
  - ev-c2s5-schema-validation
  - ev-c2s5-primary-sources
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
  tags:
  - carried-forward
  - source-limited
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/765
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
  - ev-c2s5-schema-validation
  - ev-c2s5-primary-sources
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
  - ev-c2s5-schema-validation
  - ev-c2s5-primary-sources
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
  - ev-c2s5-schema-validation
  - ev-c2s5-primary-sources
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
  - ev-c2s5-schema-validation
  - ev-c2s5-primary-sources
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
  - ev-c2s5-schema-validation
  - ev-c2s5-primary-sources
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
  tags:
  - carried-forward
  - source-limited
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1657
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
  - ev-c2s5-schema-validation
  - ev-c2s5-primary-sources
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
  tags:
  - carried-forward
  - source-limited
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
actions:
- action_id: act-defer-source-limited-fulltext-findings-c2s5
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
  review_id: 20261025T113500Z-c2s4-record-deep-audit
  relationship: supersedes_stage4_deep_audit
- repository: CultureBotAI/CommunityMech
  review_id: 20261025T113600Z-c2s4-frozen-cohort-review
  relationship: supersedes_stage4_cohort_review
tags:
- cycle2
- stage5
- remediation-verification
- record-review
```
