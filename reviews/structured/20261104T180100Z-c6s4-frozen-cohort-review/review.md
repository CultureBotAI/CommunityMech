# Cycle 6 Stage 4 Full-Corpus Frozen Inventory and Cohort Review (500 Records Across 21 Cohorts)

- Review: 20261104T180100Z-c6s4-frozen-cohort-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-04T17:52:00Z
- Finished UTC: 2026-11-04T18:01:00Z
- Reviewer: antigravity-c6s4-cohort-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full-corpus frozen inventory and cohort review of all 500 eligible CommunityMech records (489 kb/communities/*.yaml, 9 data/isolates/*.yaml, 2 kb/taxa/*.yaml) partitioned into 21 disjoint domain cohorts at commit 634cae02f33fd755d0c2dd38a6c03fd7d10041c1. All 500 records pass LinkML schema validation, ontology ID-label verification, and verbatim snippet checks; mean Completeness Score across 498 MicrobialCommunity records is 91.19/100 (median 90/100), with 100% top-level environment_term coverage (498/498) and 100% reusable CommonTaxon linkage (15/15 matching Shewanella oneidensis and Geobacter sulfurreducens occurrences). Three actionable open P2 findings across 3 community records (CommunityMech:000374, 000402, 000404) and 7 carried-forward source-limited deferred findings are preserved for Cycle 6 Stage 5 grouped remediation.

## Scope And Provenance

Exhaustive cohort review of all 21 domain/root cohorts (encompassing all 500 eligible records across kb/communities/*.yaml, data/isolates/*.yaml, and kb/taxa/*.yaml) plus all 10 finding-bearing records.

Selection: All 21 domain/root cohorts (500 records total; full per-record SHA-256 inventory in frozen_inventory_metrics.tsv) and all 10 finding-bearing records at Git commit 634cae02f33fd755d0c2dd38a6c03fd7d10041c1.
Coverage: full; 31 reviewed / 31 in the declared population.
Source: git_commit at Git base 634cae02f33fd755d0c2dd38a6c03fd7d10041c1.
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
| CommunityMech:000374 | kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml | maintained | CommunityMech:000374 (Achromobacter-Enterobacter SL8-SL12 Cadmium Immobilization Coculture) |
| CommunityMech:000402 | kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml | maintained | CommunityMech:000402 (Delta nrfA Shewanella-Anammox Nitrite Coupled Consortium) |
| CommunityMech:000404 | kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml | maintained | CommunityMech:000404 (Wollastonite Ramichloridium-Talaromyces Fungal Consortium) |
| cohort:AMD | kb/communities/AMD_Acidophile_Heterotroph_Network.yaml # cohort=AMD;records=7 | snapshot_row | AMD cohort (7 records) |
| cohort:BIOMINING | kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml # cohort=BIOMINING;records=17 | snapshot_row | BIOMINING cohort (17 records) |
| cohort:BIOREMEDIATION | kb/communities/Australian_Lead_Zinc_Polymetallic.yaml # cohort=BIOREMEDIATION;records=88 | snapshot_row | BIOREMEDIATION cohort (88 records) |
| cohort:BIOTECHNOLOGY | kb/communities/BioModels_MODEL2204300001_Kefir_Community_Model.yaml # cohort=BIOTECHNOLOGY;records=96 | snapshot_row | BIOTECHNOLOGY cohort (96 records) |
| cohort:CARBON_SEQUESTRATION | kb/communities/Phormidium_Alkaline_Consortium.yaml # cohort=CARBON_SEQUESTRATION;records=12 | snapshot_row | CARBON_SEQUESTRATION cohort (12 records) |
| cohort:DIET | kb/communities/Geobacter_Methanosaeta_DIET.yaml # cohort=DIET;records=11 | snapshot_row | DIET cohort (11 records) |
| cohort:EXTREME_ENVIRONMENT | kb/communities/Naica_Deep_Subsurface_Thermophilic.yaml # cohort=EXTREME_ENVIRONMENT;records=16 | snapshot_row | EXTREME_ENVIRONMENT cohort (16 records) |
| cohort:ISOLATES:BIOMINING | data/isolates/Aspergillus_Indium_LED_Recovery.yaml # cohort=ISOLATES:BIOMINING;records=4 | snapshot_row | ISOLATES:BIOMINING cohort (4 records) |
| cohort:ISOLATES:BIOREMEDIATION | data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml # cohort=ISOLATES:BIOREMEDIATION;records=2 | snapshot_row | ISOLATES:BIOREMEDIATION cohort (2 records) |
| cohort:ISOLATES:BIOTECHNOLOGY | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml # cohort=ISOLATES:BIOTECHNOLOGY;records=2 | snapshot_row | ISOLATES:BIOTECHNOLOGY cohort (2 records) |
| cohort:ISOLATES:EXTREME_ENVIRONMENT | data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml # cohort=ISOLATES:EXTREME_ENVIRONMENT;records=1 | snapshot_row | ISOLATES:EXTREME_ENVIRONMENT cohort (1 records) |
| cohort:LIGNOCELLULOSE | kb/communities/MAMC_M48_Lignocellulose.yaml # cohort=LIGNOCELLULOSE;records=37 | snapshot_row | LIGNOCELLULOSE cohort (37 records) |
| cohort:METAL_REDUCTION | kb/communities/Chromium_Sulfur_Reduction_Enrichment.yaml # cohort=METAL_REDUCTION;records=3 | snapshot_row | METAL_REDUCTION cohort (3 records) |
| cohort:METHANOGENESIS | kb/communities/DVM_Triculture.yaml # cohort=METHANOGENESIS;records=17 | snapshot_row | METHANOGENESIS cohort (17 records) |
| cohort:ORAL | kb/communities/Early_Dental_Biofilm_FiveSpecies.yaml # cohort=ORAL;records=5 | snapshot_row | ORAL cohort (5 records) |
| cohort:OTHER | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml # cohort=OTHER;records=44 | snapshot_row | OTHER cohort (44 records) |
| cohort:PHAGE_PREDATION | kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml # cohort=PHAGE_PREDATION;records=2 | snapshot_row | PHAGE_PREDATION cohort (2 records) |
| cohort:PHYTOPLANKTON | kb/communities/Chlamydomonas_Bacterial_H2_Consortium.yaml # cohort=PHYTOPLANKTON;records=19 | snapshot_row | PHYTOPLANKTON cohort (19 records) |
| cohort:RHIZOSPHERE | kb/communities/At_RSPHERE_SynCom.yaml # cohort=RHIZOSPHERE;records=81 | snapshot_row | RHIZOSPHERE cohort (81 records) |
| cohort:SYNTROPHY | kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml # cohort=SYNTROPHY;records=34 | snapshot_row | SYNTROPHY cohort (34 records) |
| cohort:TAXA | kb/taxa/Shewanella_oneidensis_MR1.yaml # cohort=TAXA;records=2 | snapshot_row | TAXA cohort (2 records) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation across all 500 records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000402, CommunityMech:000404, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | All 498 MicrobialCommunity records and 2 TaxonRecord files pass LinkML schema validation with 0 errors and 100% EvidenceItem.evidence_source enum compliance. |
| NetworkIntegrityAuditor check across kb/communities/ and data/isolates/ | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000402, CommunityMech:000404, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | 473/489 community records and 9/9 isolate records have 0 network warnings; 16 community records have 44 non-fatal warnings (42 DISCONNECTED across 15 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| review-communities Completeness Score rubric across all 500 records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000402, CommunityMech:000404, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | Computed proportional 100-point review-communities Completeness Score (min 40, median 90, mean 91.19, max 100 across 498 MicrobialCommunity records; 100/100 across 2 TaxonRecord files; 000374=90/100, 000402=90/100, 000404=90/100; scripts/audit_completeness.py scores 40, 25, and 40 due to missing taxon functional_role) and verified causal graph and reusable taxon coverage across all 21 cohorts. |

## Scientific And Domain Assessments

### Cohort review of AMD (7 records)

completeness: supported. Targets: cohort:AMD.

Cohort AMD comprises 7 records (34 taxa, 29 ecological interactions, 8 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 94.00/100 (min 91/100).

Reviewed member records (7): CommunityMech:000001, CommunityMech:000002, CommunityMech:000027, CommunityMech:000034, CommunityMech:000059, CommunityMech:000074, CommunityMech:000353.

### Cohort review of BIOMINING (17 records)

completeness: concern. Targets: cohort:BIOMINING, CommunityMech:000404.

Cohort BIOMINING comprises 17 records (54 taxa, 58 ecological interactions, 26 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon links) with mean Completeness Score 92.24/100 (min 75/100).

Reviewed member records (17): CommunityMech:000005, CommunityMech:000019, CommunityMech:000026, CommunityMech:000035, CommunityMech:000045, CommunityMech:000049, CommunityMech:000057, CommunityMech:000073, CommunityMech:000217, CommunityMech:000303, CommunityMech:000305, CommunityMech:000385, CommunityMech:000404, CommunityMech:000485, CommunityMech:000486, CommunityMech:000487, CommunityMech:000491.

### Cohort review of BIOREMEDIATION (88 records)

completeness: concern. Targets: cohort:BIOREMEDIATION, CommunityMech:000374.

Cohort BIOREMEDIATION comprises 88 records (313 taxa, 225 ecological interactions, 89 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon links) with mean Completeness Score 92.10/100 (min 60/100).

Reviewed member records (88): CommunityMech:000004, CommunityMech:000024, CommunityMech:000030, CommunityMech:000038, CommunityMech:000042, CommunityMech:000044, CommunityMech:000051, CommunityMech:000060, CommunityMech:000111, CommunityMech:000112, CommunityMech:000113, CommunityMech:000114, CommunityMech:000115, CommunityMech:000116, CommunityMech:000121, CommunityMech:000132, CommunityMech:000136, CommunityMech:000138, CommunityMech:000163, CommunityMech:000166, CommunityMech:000176, CommunityMech:000181, CommunityMech:000183, CommunityMech:000184, CommunityMech:000199, CommunityMech:000200, CommunityMech:000209, CommunityMech:000238, CommunityMech:000239, CommunityMech:000271, CommunityMech:000285, CommunityMech:000289, CommunityMech:000291, CommunityMech:000292, CommunityMech:000299, CommunityMech:000300, CommunityMech:000301, CommunityMech:000324, CommunityMech:000328, CommunityMech:000331, CommunityMech:000334, CommunityMech:000335, CommunityMech:000340, CommunityMech:000342, CommunityMech:000344, CommunityMech:000352, CommunityMech:000358, CommunityMech:000361, CommunityMech:000362, CommunityMech:000369, CommunityMech:000370, CommunityMech:000371, CommunityMech:000374, CommunityMech:000379, CommunityMech:000384, CommunityMech:000386, CommunityMech:000387, CommunityMech:000388, CommunityMech:000405, CommunityMech:000406, CommunityMech:000410, CommunityMech:000411, CommunityMech:000413, CommunityMech:000420, CommunityMech:000424, CommunityMech:000426, CommunityMech:000437, CommunityMech:000439, CommunityMech:000440, CommunityMech:000442, CommunityMech:000444, CommunityMech:000454, CommunityMech:000461, CommunityMech:000462, CommunityMech:000463, CommunityMech:000470, CommunityMech:000471, CommunityMech:000476, CommunityMech:000479, CommunityMech:000482, CommunityMech:000484, CommunityMech:000493, CommunityMech:000498, CommunityMech:000499, CommunityMech:000500, CommunityMech:000502, CommunityMech:000503, CommunityMech:000504.

### Cohort review of BIOTECHNOLOGY (96 records)

completeness: concern. Targets: cohort:BIOTECHNOLOGY, CommunityMech:000091, CommunityMech:000153, CommunityMech:000295, CommunityMech:000402.

Cohort BIOTECHNOLOGY comprises 96 records (304 taxa, 255 ecological interactions, 96 downstream causal edges, 0 inline UniProtKB gene annotations, 8 reusable CommonTaxon links) with mean Completeness Score 89.94/100 (min 50/100).

Reviewed member records (96): CommunityMech:000009, CommunityMech:000029, CommunityMech:000036, CommunityMech:000091, CommunityMech:000092, CommunityMech:000117, CommunityMech:000126, CommunityMech:000139, CommunityMech:000146, CommunityMech:000149, CommunityMech:000151, CommunityMech:000152, CommunityMech:000153, CommunityMech:000154, CommunityMech:000164, CommunityMech:000165, CommunityMech:000167, CommunityMech:000170, CommunityMech:000171, CommunityMech:000172, CommunityMech:000173, CommunityMech:000175, CommunityMech:000177, CommunityMech:000185, CommunityMech:000198, CommunityMech:000202, CommunityMech:000203, CommunityMech:000204, CommunityMech:000207, CommunityMech:000210, CommunityMech:000211, CommunityMech:000213, CommunityMech:000214, CommunityMech:000241, CommunityMech:000244, CommunityMech:000266, CommunityMech:000269, CommunityMech:000278, CommunityMech:000279, CommunityMech:000283, CommunityMech:000284, CommunityMech:000287, CommunityMech:000294, CommunityMech:000295, CommunityMech:000306, CommunityMech:000326, CommunityMech:000329, CommunityMech:000330, CommunityMech:000332, CommunityMech:000333, CommunityMech:000343, CommunityMech:000345, CommunityMech:000354, CommunityMech:000355, CommunityMech:000356, CommunityMech:000357, CommunityMech:000359, CommunityMech:000363, CommunityMech:000365, CommunityMech:000366, CommunityMech:000372, CommunityMech:000378, CommunityMech:000390, CommunityMech:000395, CommunityMech:000397, CommunityMech:000399, CommunityMech:000400, CommunityMech:000402, CommunityMech:000408, CommunityMech:000412, CommunityMech:000415, CommunityMech:000417, CommunityMech:000418, CommunityMech:000422, CommunityMech:000425, CommunityMech:000430, CommunityMech:000431, CommunityMech:000433, CommunityMech:000434, CommunityMech:000435, CommunityMech:000436, CommunityMech:000438, CommunityMech:000445, CommunityMech:000447, CommunityMech:000448, CommunityMech:000449, CommunityMech:000450, CommunityMech:000453, CommunityMech:000455, CommunityMech:000457, CommunityMech:000465, CommunityMech:000478, CommunityMech:000480, CommunityMech:000481, CommunityMech:000496, CommunityMech:000497.

### Cohort review of CARBON_SEQUESTRATION (12 records)

completeness: concern. Targets: cohort:CARBON_SEQUESTRATION, CommunityMech:000054.

Cohort CARBON_SEQUESTRATION comprises 12 records (37 taxa, 39 ecological interactions, 18 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon links) with mean Completeness Score 92.17/100 (min 80/100).

Reviewed member records (12): CommunityMech:000054, CommunityMech:000137, CommunityMech:000169, CommunityMech:000192, CommunityMech:000197, CommunityMech:000215, CommunityMech:000224, CommunityMech:000227, CommunityMech:000233, CommunityMech:000251, CommunityMech:000261, CommunityMech:000298.

### Cohort review of DIET (11 records)

completeness: supported. Targets: cohort:DIET.

Cohort DIET comprises 11 records (34 taxa, 32 ecological interactions, 12 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon links) with mean Completeness Score 92.73/100 (min 85/100).

Reviewed member records (11): CommunityMech:000032, CommunityMech:000033, CommunityMech:000201, CommunityMech:000281, CommunityMech:000296, CommunityMech:000317, CommunityMech:000349, CommunityMech:000401, CommunityMech:000464, CommunityMech:000466, CommunityMech:000474.

### Cohort review of EXTREME_ENVIRONMENT (16 records)

completeness: concern. Targets: cohort:EXTREME_ENVIRONMENT, CommunityMech:000222.

Cohort EXTREME_ENVIRONMENT comprises 16 records (61 taxa, 53 ecological interactions, 11 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 89.19/100 (min 80/100).

Reviewed member records (16): CommunityMech:000046, CommunityMech:000062, CommunityMech:000140, CommunityMech:000218, CommunityMech:000222, CommunityMech:000234, CommunityMech:000237, CommunityMech:000242, CommunityMech:000243, CommunityMech:000252, CommunityMech:000260, CommunityMech:000308, CommunityMech:000309, CommunityMech:000319, CommunityMech:000339, CommunityMech:000494.

### Cohort review of ISOLATES:BIOMINING (4 records)

completeness: supported. Targets: cohort:ISOLATES:BIOMINING.

Cohort ISOLATES:BIOMINING comprises 4 records (4 taxa, 14 ecological interactions, 9 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 93.75/100 (min 91/100).

Reviewed member records (4): CommunityMech:000320, CommunityMech:000322, CommunityMech:000489, CommunityMech:000490.

### Cohort review of ISOLATES:BIOREMEDIATION (2 records)

completeness: supported. Targets: cohort:ISOLATES:BIOREMEDIATION.

Cohort ISOLATES:BIOREMEDIATION comprises 2 records (2 taxa, 5 ecological interactions, 3 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 95.00/100 (min 95/100).

Reviewed member records (2): CommunityMech:000488, CommunityMech:000492.

### Cohort review of ISOLATES:BIOTECHNOLOGY (2 records)

completeness: supported. Targets: cohort:ISOLATES:BIOTECHNOLOGY.

Cohort ISOLATES:BIOTECHNOLOGY comprises 2 records (2 taxa, 5 ecological interactions, 2 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 93.00/100 (min 91/100).

Reviewed member records (2): CommunityMech:000273, CommunityMech:000321.

### Cohort review of ISOLATES:EXTREME_ENVIRONMENT (1 records)

completeness: supported. Targets: cohort:ISOLATES:EXTREME_ENVIRONMENT.

Cohort ISOLATES:EXTREME_ENVIRONMENT comprises 1 records (1 taxa, 3 ecological interactions, 2 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 92.00/100 (min 92/100).

Reviewed member records (1): CommunityMech:000495.

### Cohort review of LIGNOCELLULOSE (37 records)

completeness: concern. Targets: cohort:LIGNOCELLULOSE, CommunityMech:000048.

Cohort LIGNOCELLULOSE comprises 37 records (127 taxa, 110 ecological interactions, 54 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 94.97/100 (min 85/100).

Reviewed member records (37): CommunityMech:000041, CommunityMech:000048, CommunityMech:000061, CommunityMech:000075, CommunityMech:000118, CommunityMech:000119, CommunityMech:000120, CommunityMech:000156, CommunityMech:000168, CommunityMech:000178, CommunityMech:000179, CommunityMech:000180, CommunityMech:000193, CommunityMech:000194, CommunityMech:000195, CommunityMech:000196, CommunityMech:000205, CommunityMech:000206, CommunityMech:000208, CommunityMech:000263, CommunityMech:000264, CommunityMech:000265, CommunityMech:000267, CommunityMech:000270, CommunityMech:000275, CommunityMech:000277, CommunityMech:000282, CommunityMech:000286, CommunityMech:000297, CommunityMech:000323, CommunityMech:000338, CommunityMech:000383, CommunityMech:000389, CommunityMech:000398, CommunityMech:000407, CommunityMech:000421, CommunityMech:000473.

### Cohort review of METAL_REDUCTION (3 records)

completeness: supported. Targets: cohort:METAL_REDUCTION.

Cohort METAL_REDUCTION comprises 3 records (8 taxa, 10 ecological interactions, 10 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon links) with mean Completeness Score 94.33/100 (min 90/100).

Reviewed member records (3): CommunityMech:000017, CommunityMech:000262, CommunityMech:000268.

### Cohort review of METHANOGENESIS (17 records)

completeness: supported. Targets: cohort:METHANOGENESIS.

Cohort METHANOGENESIS comprises 17 records (57 taxa, 59 ecological interactions, 22 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 96.53/100 (min 90/100).

Reviewed member records (17): CommunityMech:000021, CommunityMech:000089, CommunityMech:000135, CommunityMech:000174, CommunityMech:000182, CommunityMech:000219, CommunityMech:000226, CommunityMech:000246, CommunityMech:000254, CommunityMech:000255, CommunityMech:000256, CommunityMech:000257, CommunityMech:000258, CommunityMech:000274, CommunityMech:000380, CommunityMech:000394, CommunityMech:000416.

### Cohort review of ORAL (5 records)

completeness: supported. Targets: cohort:ORAL.

Cohort ORAL comprises 5 records (15 taxa, 15 ecological interactions, 6 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 92.40/100 (min 84/100).

Reviewed member records (5): CommunityMech:000081, CommunityMech:000082, CommunityMech:000083, CommunityMech:000084, CommunityMech:000085.

### Cohort review of OTHER (44 records)

completeness: supported. Targets: cohort:OTHER.

Cohort OTHER comprises 44 records (192 taxa, 129 ecological interactions, 45 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 87.98/100 (min 55/100).

Reviewed member records (44): CommunityMech:000010, CommunityMech:000011, CommunityMech:000012, CommunityMech:000013, CommunityMech:000037, CommunityMech:000055, CommunityMech:000065, CommunityMech:000066, CommunityMech:000067, CommunityMech:000080, CommunityMech:000086, CommunityMech:000093, CommunityMech:000122, CommunityMech:000123, CommunityMech:000124, CommunityMech:000125, CommunityMech:000127, CommunityMech:000128, CommunityMech:000133, CommunityMech:000144, CommunityMech:000145, CommunityMech:000159, CommunityMech:000160, CommunityMech:000161, CommunityMech:000220, CommunityMech:000223, CommunityMech:000240, CommunityMech:000248, CommunityMech:000249, CommunityMech:000253, CommunityMech:000293, CommunityMech:000315, CommunityMech:000318, CommunityMech:000346, CommunityMech:000351, CommunityMech:000360, CommunityMech:000364, CommunityMech:000377, CommunityMech:000382, CommunityMech:000392, CommunityMech:000396, CommunityMech:000423, CommunityMech:000432, CommunityMech:000443.

### Cohort review of PHAGE_PREDATION (2 records)

completeness: supported. Targets: cohort:PHAGE_PREDATION.

Cohort PHAGE_PREDATION comprises 2 records (11 taxa, 10 ecological interactions, 3 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 83.00/100 (min 83/100).

Reviewed member records (2): CommunityMech:000467, CommunityMech:000468.

### Cohort review of PHYTOPLANKTON (19 records)

completeness: supported. Targets: cohort:PHYTOPLANKTON.

Cohort PHYTOPLANKTON comprises 19 records (60 taxa, 59 ecological interactions, 18 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 95.00/100 (min 84/100).

Reviewed member records (19): CommunityMech:000014, CommunityMech:000015, CommunityMech:000016, CommunityMech:000020, CommunityMech:000056, CommunityMech:000130, CommunityMech:000131, CommunityMech:000143, CommunityMech:000147, CommunityMech:000155, CommunityMech:000162, CommunityMech:000191, CommunityMech:000259, CommunityMech:000325, CommunityMech:000381, CommunityMech:000441, CommunityMech:000446, CommunityMech:000451, CommunityMech:000452.

### Cohort review of RHIZOSPHERE (81 records)

completeness: concern. Targets: cohort:RHIZOSPHERE, CommunityMech:000302.

Cohort RHIZOSPHERE comprises 81 records (411 taxa, 257 ecological interactions, 86 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 87.01/100 (min 55/100).

Reviewed member records (81): CommunityMech:000003, CommunityMech:000022, CommunityMech:000025, CommunityMech:000028, CommunityMech:000039, CommunityMech:000040, CommunityMech:000043, CommunityMech:000047, CommunityMech:000050, CommunityMech:000058, CommunityMech:000063, CommunityMech:000064, CommunityMech:000072, CommunityMech:000076, CommunityMech:000077, CommunityMech:000078, CommunityMech:000079, CommunityMech:000087, CommunityMech:000088, CommunityMech:000090, CommunityMech:000094, CommunityMech:000095, CommunityMech:000096, CommunityMech:000097, CommunityMech:000098, CommunityMech:000099, CommunityMech:000100, CommunityMech:000101, CommunityMech:000102, CommunityMech:000103, CommunityMech:000104, CommunityMech:000105, CommunityMech:000106, CommunityMech:000107, CommunityMech:000108, CommunityMech:000109, CommunityMech:000110, CommunityMech:000129, CommunityMech:000216, CommunityMech:000221, CommunityMech:000225, CommunityMech:000235, CommunityMech:000236, CommunityMech:000245, CommunityMech:000247, CommunityMech:000250, CommunityMech:000272, CommunityMech:000280, CommunityMech:000302, CommunityMech:000304, CommunityMech:000310, CommunityMech:000311, CommunityMech:000312, CommunityMech:000313, CommunityMech:000314, CommunityMech:000316, CommunityMech:000341, CommunityMech:000347, CommunityMech:000348, CommunityMech:000367, CommunityMech:000368, CommunityMech:000373, CommunityMech:000375, CommunityMech:000376, CommunityMech:000391, CommunityMech:000393, CommunityMech:000403, CommunityMech:000409, CommunityMech:000414, CommunityMech:000419, CommunityMech:000427, CommunityMech:000428, CommunityMech:000429, CommunityMech:000456, CommunityMech:000458, CommunityMech:000459, CommunityMech:000460, CommunityMech:000472, CommunityMech:000477, CommunityMech:000483, CommunityMech:000501.

### Cohort review of SYNTROPHY (34 records)

completeness: supported. Targets: cohort:SYNTROPHY.

Cohort SYNTROPHY comprises 34 records (83 taxa, 113 ecological interactions, 66 downstream causal edges, 0 inline UniProtKB gene annotations, 2 reusable CommonTaxon links) with mean Completeness Score 95.94/100 (min 84/100).

Reviewed member records (34): CommunityMech:000006, CommunityMech:000007, CommunityMech:000008, CommunityMech:000018, CommunityMech:000023, CommunityMech:000031, CommunityMech:000052, CommunityMech:000053, CommunityMech:000068, CommunityMech:000069, CommunityMech:000070, CommunityMech:000071, CommunityMech:000134, CommunityMech:000141, CommunityMech:000142, CommunityMech:000148, CommunityMech:000150, CommunityMech:000157, CommunityMech:000158, CommunityMech:000186, CommunityMech:000187, CommunityMech:000188, CommunityMech:000189, CommunityMech:000190, CommunityMech:000276, CommunityMech:000288, CommunityMech:000290, CommunityMech:000307, CommunityMech:000327, CommunityMech:000336, CommunityMech:000337, CommunityMech:000350, CommunityMech:000469, CommunityMech:000475.

### Cohort review of TAXA (2 records)

completeness: supported. Targets: cohort:TAXA.

Cohort TAXA comprises 2 records (2 taxa, 0 ecological interactions, 0 downstream causal edges, 9 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 100.00/100 (min 100/100).

Reviewed member records (2): CommunityMech:taxon:000001, CommunityMech:taxon:000002.

## Findings

### c6s4-000374-sl8-sl12-functional-roles: Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture (CommunityMech:000374) omits functional_role on both Achromobacter sp. SL8 and Enterobacter sp. SL12

major / open / confirmed; issue key: c6s4-000374-sl8-sl12-functional-roles.

In kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml (CommunityMech:000374), both taxonomy[0] (Achromobacter sp. SL8, NCBITaxon:222) and taxonomy[1] (Enterobacter sp. SL12, NCBITaxon:547) record abundance_level: ABUNDANT at a 1:1 (v/v) co-inoculation ratio, but both omit functional_role. The cited open-access source PMID:42307251 (PMC13340288, doi:10.3390/microorganisms14061493) explicitly establishes that Achromobacter sp. SL8 and Enterobacter sp. SL12 act as synergistic extracellular-polymeric-substance (EPS)-producing and CdS-precipitating partners (functional_role: [SYNTROPHIC_PARTNER, BIOFILM_FORMER]) whose co-culture stimulates polysaccharide and protein secretion, cell aggregation, and up-regulation of cysteine biosynthesis (cysK) and sulfate transport to immobilize Cd2+.

### c6s4-000402-shewanella-anammox-roles-and-abundance: Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium (CommunityMech:000402) omits functional_role and abundance_level across all three taxonomy entries

major / open / confirmed; issue key: c6s4-000402-shewanella-anammox-roles-and-abundance.

In kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml (CommunityMech:000402), taxonomy[0] (Delta nrfA Shewanella oneidensis MR-1, NCBITaxon:211586), taxonomy[1] (Candidatus Brocadia anammox bacteria, NCBITaxon:380240), and taxonomy[2] (endogenous activated-sludge heterotrophic bacteria, NCBITaxon:2) all omit functional_role and abundance_level. The cited open-access source PMID:42655905 (PMC13519132, doi:10.1002/advs.77600) establishes Delta nrfA S. oneidensis MR-1 as the engineered partial-denitrifying nitrite-supplying cross-feeder and syntrophic partner (functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER]; abundance_level: ABUNDANT), Candidatus Brocadia as the dominant anammox syntrophic partner (functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER]; abundance_level: DOMINANT, enriched to 7%~10% of community abundance), and endogenous activated-sludge heterotrophic bacteria as the organic-matter-fermenting syntrophic guild providing volatile fatty acids and amino acids to Delta nrfA S. oneidensis (functional_role: [SYNTROPHIC_PARTNER, SECONDARY_FERMENTER]; abundance_level: ABUNDANT).

### c6s4-000404-wollastonite-cms1-role-and-abundance: Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium (CommunityMech:000404) omits functional_role on Ramichloridium apiculatum CMS-1 and abundance_level on both fungal members

major / open / confirmed; issue key: c6s4-000404-wollastonite-cms1-role-and-abundance.

In kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml (CommunityMech:000404), taxonomy[0] (Ramichloridium apiculatum CMS-1, NCBITaxon:222813) omits both functional_role and abundance_level, while taxonomy[1] (Talaromyces pseudofuniculosus hzt-3', NCBITaxon:28568) records functional_role: [CROSS_FEEDER] but omits abundance_level. The cited open-access source PMID:42478817 (PMC13488302, doi:10.3390/jof12070581) establishes that at the optimal CMS-1 : hzt-3' = 1:4 inoculum ratio (20% CMS-1, 80% hzt-3'), R. apiculatum CMS-1 acts as the carbonic-anhydrase- and cellulase-producing syntrophic cross-feeder (functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER]; abundance_level: ABUNDANT) and T. pseudofuniculosus hzt-3' is the dominant organic-acid-secreting wollastonite-dissolving partner (functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER]; abundance_level: DOMINANT).

### cheese-assay-evidence-gap: Pairwise in-vitro assay evidence in Cheese Rind Model Community (CommunityMech:000153) remains abstract-limited

minor / deferred / confirmed; issue key: cheese-assay-evidence-gap.

Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153) cites PMID:25043025 abstract for community-wide moisture and pH interactions; specific pairwise bacterial-fungal assay details reside in full-text figures/tables not present in the abstract cache.

Disposition: Deferred: source-limited until full-text assay tables for PMID:25043025 are ingested (#765).

### communitymech-1467-source-discrepancy-and-extension: GLBRC Transwell SynCom (CommunityMech:000091) broader 18-species campaign and strain-detail extension remains source-limited

minor / deferred / confirmed; issue key: communitymech-1467-source-discrepancy-and-extension.

GLBRC_Exometabolite_Transwell_SynCom.yaml (CommunityMech:000091) captures the abstract-supported five-member model system; broader 18-species screening campaign and strain-level table details require full-text tables tracked in #1467.

Disposition: Deferred: tracked in GitHub issue #1467 pending full-text table reconciliation.

### communitymech-1699-coverage: Additional heterotrophic co-isolates in Phormidium Alkaline Consortium (CommunityMech:000054) require full-text tables

minor / deferred / confirmed; issue key: communitymech-1699-coverage.

Phormidium_Alkaline_Consortium.yaml (CommunityMech:000054) curates the primary cyanobacterial-heterotroph interactions supported by cached abstracts; full heterotrophic member enumeration requires full-text tables (#1699).

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

### act-populate-sl8-sl12-functional-roles

Add functional_role: [SYNTROPHIC_PARTNER, BIOFILM_FORMER] to both Achromobacter sp. SL8 (taxonomy[0]) and Enterobacter sp. SL12 (taxonomy[1]) backed by PMID:42307251 (PMC13340288) on CommunityMech:000374, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
- just validate-history history

### act-populate-shewanella-anammox-roles-and-abundance

Add functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT to Delta nrfA Shewanella oneidensis MR-1 (taxonomy[0]), add functional_role: [SYNTROPHIC_PARTNER, CROSS_FEEDER] and abundance_level: DOMINANT to Candidatus Brocadia anammox bacteria (taxonomy[1]), add functional_role: [SYNTROPHIC_PARTNER, SECONDARY_FERMENTER] and abundance_level: ABUNDANT to endogenous activated-sludge heterotrophic bacteria (taxonomy[2]) backed by PMID:42655905 (PMC13519132) on CommunityMech:000402, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
- just validate-history history

### act-populate-wollastonite-cms1-role-and-abundance

Add functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level: ABUNDANT to Ramichloridium apiculatum CMS-1 (taxonomy[0]), and add abundance_level: DOMINANT and SYNTROPHIC_PARTNER to Talaromyces pseudofuniculosus hzt-3' (taxonomy[1]) backed by PMID:42478817 (PMC13488302) on CommunityMech:000404, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
- just validate-history history

### act-defer-source-limited-fulltext-findings-c6s4

Retain source-limited full-text findings until open-access full text or supplementary strain/assay tables become available for CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify full-text table availability before modifying abstract-grounded claims on source-limited records.

## Category Boundaries

- split: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000402, CommunityMech:000404, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA. The full 500-record CommunityMech corpus spans 3 record roots (kb/communities/, data/isolates/, kb/taxa/) and 16 ecological categories, which is over-broad for a single unpartitioned cohort. Splitting by root and community_category yields 21 disjoint, ecologically coherent cohorts (16 community cohorts, 4 isolate cohorts, and 1 TAXA cohort) for comparative rubric evaluation.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and TaxonRecord classes | supports | All 489 kb/communities/*.yaml, 9 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records (500 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | scripts/audit_completeness.py; 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness() across all 500 records | supports | Proportional 100-point review-communities Completeness Score audit across all 498 MicrobialCommunity records (min 40, median 90, mean 91.19, max 100; CommunityMech:000374 = 90/100, CommunityMech:000402 = 90/100, CommunityMech:000404 = 90/100) and 2 TaxonRecord files (100/100) confirmed 100% core metadata presence and 100% top-level environment_term coverage (498/498), while scripts/audit_completeness.py:calculate_completeness() (which requires every taxon to have functional_role for its 50-point required block) scores 000374 at 40/100, 000402 at 25/100, and 000404 at 40/100. |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | NetworkIntegrityAuditor across 489 kb/communities and 9 data/isolates records found 473/489 communities and 9/9 isolates with 0 warnings (including all 19/19 MicrobialCommunity records in the 21-record deep audit) and 16 community records with 44 non-fatal warnings (42 DISCONNECTED across 15 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-499 | supports | Corpus-wide causal graph inventory covers all 498 MicrobialCommunity records with 100% SHA-256 attestation in verify_causal_graph_reviews.py (0 unreviewed records). |
| ev-common-taxon-linkage-audit | kb/taxa/Geobacter_sulfurreducens.yaml; TaxonomicComposition.common_taxon cross-references and inline UniProtKB genes across kb/communities/*.yaml | supports | Corpus-wide audit of reusable taxon cross-references confirmed 15 TaxonomicComposition.common_taxon links across kb/communities/*.yaml (6 Geobacter sulfurreducens communities linked to CommunityMech:taxon:000002 [4 reusable UniProt EET genes plus inline macA/Q749P2] and 9 Shewanella oneidensis communities linked to CommunityMech:taxon:000001 [5 reusable UniProt EET genes plus inline fccA/Q8EKT2]) and 25 new verified inline UniProtKB gene annotations across CommunityMech:000501-000504 after Cycle 6 Stage 3 (#2111). |
| ev-sl8-sl12-pmid42307251 | PMID:42307251; kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml | supports | PMID:42307251 (PMC13340288, doi:10.3390/microorganisms14061493) establishes that Achromobacter sp. SL8 and Enterobacter sp. SL12 act as synergistic extracellular-polymeric-substance (EPS)-producing and CdS-bioprecipitating partners at a 1:1 co-inoculation ratio. |
| ev-shewanella-anammox-pmid42655905 | PMID:42655905; kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml | supports | PMID:42655905 (PMC13519132, doi:10.1002/advs.77600) establishes Delta nrfA Shewanella oneidensis MR-1 as the engineered nitrite-supplying cross-feeder, Candidatus Brocadia as the dominant anammox partner (enriched to 7%~10% relative abundance), and endogenous activated-sludge heterotrophic bacteria as the organic-matter-fermenting syntrophic guild supplying volatile fatty acids and amino acids. |
| ev-wollastonite-pmid42478817 | PMID:42478817; kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml | supports | PMID:42478817 (PMC13488302, doi:10.3390/jof12070581) establishes that at the optimal CMS-1 : hzt-3' = 1:4 inoculum ratio (20% CMS-1, 80% hzt-3'), Ramichloridium apiculatum CMS-1 acts as the carbonic-anhydrase- and cellulase-producing syntrophic cross-feeder and Talaromyces pseudofuniculosus hzt-3' is the dominant organic-acid-producing mineral-weathering partner. |
| ev-prior-structured-reviews | reviews/structured; 55 retained structured review bundles through 20261104T060000Z-c5s5-remediation-verification | context_only | Lineage inspection of all 55 prior structured reviews and Cycle 5 Stage 5 evidence.yaml confirmed that all 3 Cycle 5 Stage 4 open findings across CommunityMech:000084, 000085, and 000385 were resolved in Cycle 5 Stage 5 (#2105, PR #2106) and 7 record-scoped source-limited findings remain deferred at commit 634cae02f33fd755d0c2dd38a6c03fd7d10041c1. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Seven carried-forward community records remain source-limited because cached abstracts do not provide full-text assay or strain tables (#765, #1467, #1657, #1681, #1699, #1841, #1847).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261104T180100Z-c6s4-frozen-cohort-review
kind: category
repository: CultureBotAI/CommunityMech
title: Cycle 6 Stage 4 Full-Corpus Frozen Inventory and Cohort Review (500 Records
  Across 21 Cohorts)
started_at: '2026-11-04T17:52:00Z'
finished_at: '2026-11-04T18:01:00Z'
reviewer:
  identity: antigravity-c6s4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated Cycle 6 Stage 4 full-corpus read-only review pass
    over frozen commit 634cae02f33fd755d0c2dd38a6c03fd7d10041c1 without record mutation.
skill: review-yaml-category
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION (490/500 records pass without unresolved findings;
  3 new actionable open findings across 3 records and 7 carried-forward source-limited
  deferred findings across 7 records)
scientific_review: true
summary: Full-corpus frozen inventory and cohort review of all 500 eligible CommunityMech
  records (489 kb/communities/*.yaml, 9 data/isolates/*.yaml, 2 kb/taxa/*.yaml) partitioned
  into 21 disjoint domain cohorts at commit 634cae02f33fd755d0c2dd38a6c03fd7d10041c1.
  All 500 records pass LinkML schema validation, ontology ID-label verification, and
  verbatim snippet checks; mean Completeness Score across 498 MicrobialCommunity records
  is 91.19/100 (median 90/100), with 100% top-level environment_term coverage (498/498)
  and 100% reusable CommonTaxon linkage (15/15 matching Shewanella oneidensis and
  Geobacter sulfurreducens occurrences). Three actionable open P2 findings across
  3 community records (CommunityMech:000374, 000402, 000404) and 7 carried-forward
  source-limited deferred findings are preserved for Cycle 6 Stage 5 grouped remediation.
source:
  git_revision: 634cae02f33fd755d0c2dd38a6c03fd7d10041c1
  state: git_commit
  inputs:
  - path: kb/communities/AMD_Acidophile_Heterotroph_Network.yaml
    sha256: 81fe29292038349e959041675b876ef4e351cdfb6884796989540185c6797834
    role: target
  - path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    sha256: eeef4a3c72f6660c2263fe91ec7858610797c19fa513bf641e2a6234ff4414d4
    role: target
  - path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    sha256: cef1f3c47035ef336cb809456b25a185e0397bb9f0a16c492becdb5b371529f5
    role: target
  - path: kb/communities/At_RSPHERE_SynCom.yaml
    sha256: b615c84fa2415eecbf9eb3964ee830fdb3bc573508fbc42ce601fb340f3500c0
    role: target
  - path: kb/communities/Australian_Lead_Zinc_Polymetallic.yaml
    sha256: 6caa95c7d95905e4ae235578c54a75a73908c698bbf8f5d0ad6b3339595caf63
    role: target
  - path: kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml
    sha256: 655ff223cc2775123bf63fe23caa3445c1775988dd1d292a7a9edf79c4959a3f
    role: target
  - path: kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml
    sha256: bb94d58347b0bbc04ebf7c25563d1096efbbd3294a3801e3732e0c95c61e6a24
    role: target
  - path: kb/communities/BioModels_MODEL2204300001_Kefir_Community_Model.yaml
    sha256: b2e55eea689446b15484d0b01ce6f0da687b66ddd2b5b6507e1677216b2619ea
    role: target
  - path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    sha256: 45ea96efd71094d61fc28d38e2ce107358b785f173e2982e48c87edf69ca73d6
    role: target
  - path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    sha256: e4ccd373cf107383615b6f207ceb0521c83b4c97daf57c6700a441b2392ddda3
    role: target
  - path: kb/communities/Chlamydomonas_Bacterial_H2_Consortium.yaml
    sha256: 5abfc7e315eabcec04b7d57d557f6935e0f6fb9ba9f944dcc80628477fef5bb3
    role: target
  - path: kb/communities/Chromium_Sulfur_Reduction_Enrichment.yaml
    sha256: 5be48eb0c799123a45f64ec1a3dc2e07d3fcd614110fa95c383edbdcd4ed4a87
    role: target
  - path: kb/communities/DVM_Triculture.yaml
    sha256: a35537c075a8b201555340df6b43a65be0409250e87e476fb4dac682201e6f36
    role: target
  - path: kb/communities/Early_Dental_Biofilm_FiveSpecies.yaml
    sha256: 5f765b58c46852bbb55161479525a0b8f6bcc3249c385ca296978ef580a62c75
    role: target
  - path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    sha256: 51bf55d56342aa28864c0dd458a172209f9ef1e14e51a0cd210bb46521a17f47
    role: target
  - path: kb/communities/Geobacter_Methanosaeta_DIET.yaml
    sha256: 8e194a9177b013c6db3e2dd9b4ed9744f06ca0379116f41a0f4ed62cf1d4fde1
    role: target
  - path: kb/communities/MAMC_M48_Lignocellulose.yaml
    sha256: d877e443187162745cbfa2adba246854e6b2667793da22f8837fd64d08925176
    role: target
  - path: kb/communities/Naica_Deep_Subsurface_Thermophilic.yaml
    sha256: 18f4bc69aff646a74cd4f402b36be2a789d02e69a04efcd9c43a94e2c15dc8e9
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
    sha256: f300a08a92756ce174019800b7a50cec74b8d9a6be17a56accd8e2daa8aa6cf3
    role: target
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 904cc9646ae53fe0c021c1461a09f3f8d15b763edad42b6c9a43ada91c87597d
    role: target
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
    sha256: 06d15492c6e358b75deffe722b5299d7b5f86bf15090276db87fda690c6e639e
    role: target
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    sha256: c9ebc23ad2748751ae6a42fbc2340c5f7524a7aa38185bcad4602b7e56734d9d
    role: target
  - path: data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml
    sha256: 7ad94b96c56469311346da8af429fb922eaa122a96464121697282771c45120e
    role: target
  - path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    sha256: 4eb42a867f2b2b1489c4ef4fa95e408d241a54d0e2bfb1cf9474dd407d036b86
    role: target
  - path: data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml
    sha256: cc05785add2613ee69f29971820f913e038de75e44d584a3d8ec22015377c0f1
    role: target
  - path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    sha256: 2fcc32b1e409beb3b69c850a7ca22ac562a47bc9cf3a028e31eb1d7e85c92671
    role: target
  - path: src/communitymech/schema/communitymech.yaml
    sha256: a00434e0d75020b2926c9f755d625c09cc78b6f88135805991fcb0ecd4230c83
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: reports/causal_graph_review/inventory.tsv
    sha256: f4e5ce30b80926136e0ad374b98b1ae1d5c89b3c461e6ddd96ffe32c6eb6fad7
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: 6a9c9e68e27f2b6ec8ff0de5dcee17137967527b9ec42848d8525a5369f89fd2
    role: context
scope:
  description: Exhaustive cohort review of all 21 domain/root cohorts (encompassing
    all 500 eligible records across kb/communities/*.yaml, data/isolates/*.yaml, and
    kb/taxa/*.yaml) plus all 10 finding-bearing records.
  selection: All 21 domain/root cohorts (500 records total; full per-record SHA-256
    inventory in frozen_inventory_metrics.tsv) and all 10 finding-bearing records
    at Git commit 634cae02f33fd755d0c2dd38a6c03fd7d10041c1.
  coverage: full
  population_size: 31
  reviewed_target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000402
  - CommunityMech:000404
  - cohort:AMD
  - cohort:BIOMINING
  - cohort:BIOREMEDIATION
  - cohort:BIOTECHNOLOGY
  - cohort:CARBON_SEQUESTRATION
  - cohort:DIET
  - cohort:EXTREME_ENVIRONMENT
  - cohort:ISOLATES:BIOMINING
  - cohort:ISOLATES:BIOREMEDIATION
  - cohort:ISOLATES:BIOTECHNOLOGY
  - cohort:ISOLATES:EXTREME_ENVIRONMENT
  - cohort:LIGNOCELLULOSE
  - cohort:METAL_REDUCTION
  - cohort:METHANOGENESIS
  - cohort:ORAL
  - cohort:OTHER
  - cohort:PHAGE_PREDATION
  - cohort:PHYTOPLANKTON
  - cohort:RHIZOSPHERE
  - cohort:SYNTROPHY
  - cohort:TAXA
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
- target_id: CommunityMech:000374
  path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  label: CommunityMech:000374 (Achromobacter-Enterobacter SL8-SL12 Cadmium Immobilization
    Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000402
  path: kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
  label: CommunityMech:000402 (Delta nrfA Shewanella-Anammox Nitrite Coupled Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000404
  path: kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
  label: CommunityMech:000404 (Wollastonite Ramichloridium-Talaromyces Fungal Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: cohort:AMD
  path: kb/communities/AMD_Acidophile_Heterotroph_Network.yaml
  selector: cohort=AMD;records=7
  label: AMD cohort (7 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 7 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:BIOMINING
  path: kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml
  selector: cohort=BIOMINING;records=17
  label: BIOMINING cohort (17 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 17 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:BIOREMEDIATION
  path: kb/communities/Australian_Lead_Zinc_Polymetallic.yaml
  selector: cohort=BIOREMEDIATION;records=88
  label: BIOREMEDIATION cohort (88 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 88 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:BIOTECHNOLOGY
  path: kb/communities/BioModels_MODEL2204300001_Kefir_Community_Model.yaml
  selector: cohort=BIOTECHNOLOGY;records=96
  label: BIOTECHNOLOGY cohort (96 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 96 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:CARBON_SEQUESTRATION
  path: kb/communities/Phormidium_Alkaline_Consortium.yaml
  selector: cohort=CARBON_SEQUESTRATION;records=12
  label: CARBON_SEQUESTRATION cohort (12 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 12 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:DIET
  path: kb/communities/Geobacter_Methanosaeta_DIET.yaml
  selector: cohort=DIET;records=11
  label: DIET cohort (11 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 11 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:EXTREME_ENVIRONMENT
  path: kb/communities/Naica_Deep_Subsurface_Thermophilic.yaml
  selector: cohort=EXTREME_ENVIRONMENT;records=16
  label: EXTREME_ENVIRONMENT cohort (16 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 16 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ISOLATES:BIOMINING
  path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  selector: cohort=ISOLATES:BIOMINING;records=4
  label: ISOLATES:BIOMINING cohort (4 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 4 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ISOLATES:BIOREMEDIATION
  path: data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml
  selector: cohort=ISOLATES:BIOREMEDIATION;records=2
  label: ISOLATES:BIOREMEDIATION cohort (2 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 2 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ISOLATES:BIOTECHNOLOGY
  path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
  selector: cohort=ISOLATES:BIOTECHNOLOGY;records=2
  label: ISOLATES:BIOTECHNOLOGY cohort (2 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 2 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ISOLATES:EXTREME_ENVIRONMENT
  path: data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml
  selector: cohort=ISOLATES:EXTREME_ENVIRONMENT;records=1
  label: ISOLATES:EXTREME_ENVIRONMENT cohort (1 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 1 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:LIGNOCELLULOSE
  path: kb/communities/MAMC_M48_Lignocellulose.yaml
  selector: cohort=LIGNOCELLULOSE;records=37
  label: LIGNOCELLULOSE cohort (37 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 37 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:METAL_REDUCTION
  path: kb/communities/Chromium_Sulfur_Reduction_Enrichment.yaml
  selector: cohort=METAL_REDUCTION;records=3
  label: METAL_REDUCTION cohort (3 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 3 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:METHANOGENESIS
  path: kb/communities/DVM_Triculture.yaml
  selector: cohort=METHANOGENESIS;records=17
  label: METHANOGENESIS cohort (17 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 17 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ORAL
  path: kb/communities/Early_Dental_Biofilm_FiveSpecies.yaml
  selector: cohort=ORAL;records=5
  label: ORAL cohort (5 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 5 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:OTHER
  path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
  selector: cohort=OTHER;records=44
  label: OTHER cohort (44 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 44 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:PHAGE_PREDATION
  path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
  selector: cohort=PHAGE_PREDATION;records=2
  label: PHAGE_PREDATION cohort (2 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 2 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:PHYTOPLANKTON
  path: kb/communities/Chlamydomonas_Bacterial_H2_Consortium.yaml
  selector: cohort=PHYTOPLANKTON;records=19
  label: PHYTOPLANKTON cohort (19 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 19 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:RHIZOSPHERE
  path: kb/communities/At_RSPHERE_SynCom.yaml
  selector: cohort=RHIZOSPHERE;records=81
  label: RHIZOSPHERE cohort (81 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 81 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:SYNTROPHY
  path: kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml
  selector: cohort=SYNTROPHY;records=34
  label: SYNTROPHY cohort (34 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 34 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:TAXA
  path: kb/taxa/Shewanella_oneidensis_MR1.yaml
  selector: cohort=TAXA;records=2
  label: TAXA cohort (2 records)
  record_class: TaxonRecord
  kind: snapshot_row
  ownership_note: Cohort of 2 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
checks:
- check_id: chk-linkml-schema-all-500
  name: LinkML schema validation across all 500 records
  status: passed
  required: true
  summary: All 498 MicrobialCommunity records and 2 TaxonRecord files pass LinkML
    schema validation with 0 errors and 100% EvidenceItem.evidence_source enum compliance.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000402
  - CommunityMech:000404
  - cohort:AMD
  - cohort:BIOMINING
  - cohort:BIOREMEDIATION
  - cohort:BIOTECHNOLOGY
  - cohort:CARBON_SEQUESTRATION
  - cohort:DIET
  - cohort:EXTREME_ENVIRONMENT
  - cohort:ISOLATES:BIOMINING
  - cohort:ISOLATES:BIOREMEDIATION
  - cohort:ISOLATES:BIOTECHNOLOGY
  - cohort:ISOLATES:EXTREME_ENVIRONMENT
  - cohort:LIGNOCELLULOSE
  - cohort:METAL_REDUCTION
  - cohort:METHANOGENESIS
  - cohort:ORAL
  - cohort:OTHER
  - cohort:PHAGE_PREDATION
  - cohort:PHYTOPLANKTON
  - cohort:RHIZOSPHERE
  - cohort:SYNTROPHY
  - cohort:TAXA
  command: .venv/bin/python -c 'validate all 500 records against src/communitymech/schema/communitymech.yaml'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-schema-validation-gate
- check_id: chk-network-integrity-all-c6s4
  name: NetworkIntegrityAuditor check across kb/communities/ and data/isolates/
  status: passed
  required: true
  summary: 473/489 community records and 9/9 isolate records have 0 network warnings;
    16 community records have 44 non-fatal warnings (42 DISCONNECTED across 15 records
    and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom;
    0 error-severity issues, 0 broken downstream references).
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000402
  - CommunityMech:000404
  - cohort:AMD
  - cohort:BIOMINING
  - cohort:BIOREMEDIATION
  - cohort:BIOTECHNOLOGY
  - cohort:CARBON_SEQUESTRATION
  - cohort:DIET
  - cohort:EXTREME_ENVIRONMENT
  - cohort:ISOLATES:BIOMINING
  - cohort:ISOLATES:BIOREMEDIATION
  - cohort:ISOLATES:BIOTECHNOLOGY
  - cohort:ISOLATES:EXTREME_ENVIRONMENT
  - cohort:LIGNOCELLULOSE
  - cohort:METAL_REDUCTION
  - cohort:METHANOGENESIS
  - cohort:ORAL
  - cohort:OTHER
  - cohort:PHAGE_PREDATION
  - cohort:PHYTOPLANKTON
  - cohort:RHIZOSPHERE
  - cohort:SYNTROPHY
  - cohort:TAXA
  command: .venv/bin/python -m communitymech.cli audit-network
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-network-integrity-audit
- check_id: chk-completeness-rubric-all-c6s4
  name: review-communities Completeness Score rubric across all 500 records
  status: passed
  required: true
  summary: Computed proportional 100-point review-communities Completeness Score (min
    40, median 90, mean 91.19, max 100 across 498 MicrobialCommunity records; 100/100
    across 2 TaxonRecord files; 000374=90/100, 000402=90/100, 000404=90/100; scripts/audit_completeness.py
    scores 40, 25, and 40 due to missing taxon functional_role) and verified causal
    graph and reusable taxon coverage across all 21 cohorts.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000402
  - CommunityMech:000404
  - cohort:AMD
  - cohort:BIOMINING
  - cohort:BIOREMEDIATION
  - cohort:BIOTECHNOLOGY
  - cohort:CARBON_SEQUESTRATION
  - cohort:DIET
  - cohort:EXTREME_ENVIRONMENT
  - cohort:ISOLATES:BIOMINING
  - cohort:ISOLATES:BIOREMEDIATION
  - cohort:ISOLATES:BIOTECHNOLOGY
  - cohort:ISOLATES:EXTREME_ENVIRONMENT
  - cohort:LIGNOCELLULOSE
  - cohort:METAL_REDUCTION
  - cohort:METHANOGENESIS
  - cohort:ORAL
  - cohort:OTHER
  - cohort:PHAGE_PREDATION
  - cohort:PHYTOPLANKTON
  - cohort:RHIZOSPHERE
  - cohort:SYNTROPHY
  - cohort:TAXA
  command: .venv/bin/python scripts/audit_completeness.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-completeness-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
evidence:
- evidence_id: ev-schema-validation-gate
  kind: validation
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity and TaxonRecord classes
  accessed_at: '2026-11-04T17:55:00Z'
  support: supports
  summary: All 489 kb/communities/*.yaml, 9 data/isolates/*.yaml, and 2 kb/taxa/*.yaml
    records (500 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum
    compliance.
- evidence_id: ev-completeness-audit
  kind: validation
  reference: scripts/audit_completeness.py
  locator: 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness()
    across all 500 records
  accessed_at: '2026-11-04T17:56:00Z'
  support: supports
  summary: Proportional 100-point review-communities Completeness Score audit across
    all 498 MicrobialCommunity records (min 40, median 90, mean 91.19, max 100; CommunityMech:000374
    = 90/100, CommunityMech:000402 = 90/100, CommunityMech:000404 = 90/100) and 2
    TaxonRecord files (100/100) confirmed 100% core metadata presence and 100% top-level
    environment_term coverage (498/498), while scripts/audit_completeness.py:calculate_completeness()
    (which requires every taxon to have functional_role for its 50-point required
    block) scores 000374 at 40/100, 000402 at 25/100, and 000404 at 40/100.
- evidence_id: ev-network-integrity-audit
  kind: validation
  reference: src/communitymech/network/auditor.py
  locator: NetworkIntegrityAuditor.audit_all()
  accessed_at: '2026-11-04T17:57:00Z'
  support: supports
  summary: NetworkIntegrityAuditor across 489 kb/communities and 9 data/isolates records
    found 473/489 communities and 9/9 isolates with 0 warnings (including all 19/19
    MicrobialCommunity records in the 21-record deep audit) and 16 community records
    with 44 non-fatal warnings (42 DISCONNECTED across 15 records and 2 COMMUNITY_LEVEL
    UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0
    error-severity issues, 0 broken downstream references).
- evidence_id: ev-causal-inventory
  kind: record_content
  reference: reports/causal_graph_review/inventory.tsv
  locator: rows 1-499
  accessed_at: '2026-11-04T17:57:30Z'
  support: supports
  summary: Corpus-wide causal graph inventory covers all 498 MicrobialCommunity records
    with 100% SHA-256 attestation in verify_causal_graph_reviews.py (0 unreviewed
    records).
- evidence_id: ev-common-taxon-linkage-audit
  kind: record_content
  reference: kb/taxa/Geobacter_sulfurreducens.yaml
  locator: TaxonomicComposition.common_taxon cross-references and inline UniProtKB
    genes across kb/communities/*.yaml
  accessed_at: '2026-11-04T17:58:00Z'
  support: supports
  summary: Corpus-wide audit of reusable taxon cross-references confirmed 15 TaxonomicComposition.common_taxon
    links across kb/communities/*.yaml (6 Geobacter sulfurreducens communities linked
    to CommunityMech:taxon:000002 [4 reusable UniProt EET genes plus inline macA/Q749P2]
    and 9 Shewanella oneidensis communities linked to CommunityMech:taxon:000001 [5
    reusable UniProt EET genes plus inline fccA/Q8EKT2]) and 25 new verified inline
    UniProtKB gene annotations across CommunityMech:000501-000504 after Cycle 6 Stage
    3 (#2111).
- evidence_id: ev-sl8-sl12-pmid42307251
  kind: primary_source
  reference: PMID:42307251
  locator: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  accessed_at: '2026-11-04T17:58:30Z'
  support: supports
  summary: PMID:42307251 (PMC13340288, doi:10.3390/microorganisms14061493) establishes
    that Achromobacter sp. SL8 and Enterobacter sp. SL12 act as synergistic extracellular-polymeric-substance
    (EPS)-producing and CdS-bioprecipitating partners at a 1:1 co-inoculation ratio.
  quote: The bacterial consortium SL8+SL12 promoted EPS secretion (specifically polysaccharides
    and proteins), increased the variety of functional groups, and stimulated cell
    aggregation, leading to enhanced extracellular immobilization of Cd2+.
- evidence_id: ev-shewanella-anammox-pmid42655905
  kind: primary_source
  reference: PMID:42655905
  locator: kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
  accessed_at: '2026-11-04T17:59:00Z'
  support: supports
  summary: PMID:42655905 (PMC13519132, doi:10.1002/advs.77600) establishes Delta nrfA
    Shewanella oneidensis MR-1 as the engineered nitrite-supplying cross-feeder, Candidatus
    Brocadia as the dominant anammox partner (enriched to 7%~10% relative abundance),
    and endogenous activated-sludge heterotrophic bacteria as the organic-matter-fermenting
    syntrophic guild supplying volatile fatty acids and amino acids.
  quote: Metagenomic sequencing and isotope tracing analyses revealed that the deletion
    of the nrfA gene eliminated the ability of S. oneidensis to reduce NO2−‐N to NH4+‐N,
    resulting in a redirect of nitrite flux toward AnAOB and a significant increase
    in the relative abundance of Candidatus Brocadia (7%~10%).
- evidence_id: ev-wollastonite-pmid42478817
  kind: primary_source
  reference: PMID:42478817
  locator: kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
  accessed_at: '2026-11-04T17:59:20Z'
  support: supports
  summary: 'PMID:42478817 (PMC13488302, doi:10.3390/jof12070581) establishes that
    at the optimal CMS-1 : hzt-3'' = 1:4 inoculum ratio (20% CMS-1, 80% hzt-3''),
    Ramichloridium apiculatum CMS-1 acts as the carbonic-anhydrase- and cellulase-producing
    syntrophic cross-feeder and Talaromyces pseudofuniculosus hzt-3'' is the dominant
    organic-acid-producing mineral-weathering partner.'
  quote: Among the tested fungal consortia, the composite with an inoculation ratio
    of CMS-1 to hzt-3′ at 1:4 demonstrated the most pronounced weathered effect on
    wollastonite, significantly outperforming monocultures.
- evidence_id: ev-prior-structured-reviews
  kind: prior_review
  reference: reviews/structured
  locator: 55 retained structured review bundles through 20261104T060000Z-c5s5-remediation-verification
  accessed_at: '2026-11-04T17:59:45Z'
  support: context_only
  summary: 'Lineage inspection of all 55 prior structured reviews and Cycle 5 Stage
    5 evidence.yaml confirmed that all 3 Cycle 5 Stage 4 open findings across CommunityMech:000084,
    000085, and 000385 were resolved in Cycle 5 Stage 5 (#2105, PR #2106) and 7 record-scoped
    source-limited findings remain deferred at commit 634cae02f33fd755d0c2dd38a6c03fd7d10041c1.'
assessments:
- assessment_id: assess-cohort-amd
  area: completeness
  topic: Cohort review of AMD (7 records)
  outcome: supported
  summary: Cohort AMD comprises 7 records (34 taxa, 29 ecological interactions, 8
    downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 94.00/100 (min 91/100).
  details: 'Reviewed member records (7): CommunityMech:000001, CommunityMech:000002,
    CommunityMech:000027, CommunityMech:000034, CommunityMech:000059, CommunityMech:000074,
    CommunityMech:000353.'
  target_ids:
  - cohort:AMD
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 94.0
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 7
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 91.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 7
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-biomining
  area: completeness
  topic: Cohort review of BIOMINING (17 records)
  outcome: concern
  summary: Cohort BIOMINING comprises 17 records (54 taxa, 58 ecological interactions,
    26 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon
    links) with mean Completeness Score 92.24/100 (min 75/100).
  details: 'Reviewed member records (17): CommunityMech:000005, CommunityMech:000019,
    CommunityMech:000026, CommunityMech:000035, CommunityMech:000045, CommunityMech:000049,
    CommunityMech:000057, CommunityMech:000073, CommunityMech:000217, CommunityMech:000303,
    CommunityMech:000305, CommunityMech:000385, CommunityMech:000404, CommunityMech:000485,
    CommunityMech:000486, CommunityMech:000487, CommunityMech:000491.'
  target_ids:
  - cohort:BIOMINING
  - CommunityMech:000404
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 92.24
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 17
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 75.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 17
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-bioremediation
  area: completeness
  topic: Cohort review of BIOREMEDIATION (88 records)
  outcome: concern
  summary: Cohort BIOREMEDIATION comprises 88 records (313 taxa, 225 ecological interactions,
    89 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon
    links) with mean Completeness Score 92.10/100 (min 60/100).
  details: 'Reviewed member records (88): CommunityMech:000004, CommunityMech:000024,
    CommunityMech:000030, CommunityMech:000038, CommunityMech:000042, CommunityMech:000044,
    CommunityMech:000051, CommunityMech:000060, CommunityMech:000111, CommunityMech:000112,
    CommunityMech:000113, CommunityMech:000114, CommunityMech:000115, CommunityMech:000116,
    CommunityMech:000121, CommunityMech:000132, CommunityMech:000136, CommunityMech:000138,
    CommunityMech:000163, CommunityMech:000166, CommunityMech:000176, CommunityMech:000181,
    CommunityMech:000183, CommunityMech:000184, CommunityMech:000199, CommunityMech:000200,
    CommunityMech:000209, CommunityMech:000238, CommunityMech:000239, CommunityMech:000271,
    CommunityMech:000285, CommunityMech:000289, CommunityMech:000291, CommunityMech:000292,
    CommunityMech:000299, CommunityMech:000300, CommunityMech:000301, CommunityMech:000324,
    CommunityMech:000328, CommunityMech:000331, CommunityMech:000334, CommunityMech:000335,
    CommunityMech:000340, CommunityMech:000342, CommunityMech:000344, CommunityMech:000352,
    CommunityMech:000358, CommunityMech:000361, CommunityMech:000362, CommunityMech:000369,
    CommunityMech:000370, CommunityMech:000371, CommunityMech:000374, CommunityMech:000379,
    CommunityMech:000384, CommunityMech:000386, CommunityMech:000387, CommunityMech:000388,
    CommunityMech:000405, CommunityMech:000406, CommunityMech:000410, CommunityMech:000411,
    CommunityMech:000413, CommunityMech:000420, CommunityMech:000424, CommunityMech:000426,
    CommunityMech:000437, CommunityMech:000439, CommunityMech:000440, CommunityMech:000442,
    CommunityMech:000444, CommunityMech:000454, CommunityMech:000461, CommunityMech:000462,
    CommunityMech:000463, CommunityMech:000470, CommunityMech:000471, CommunityMech:000476,
    CommunityMech:000479, CommunityMech:000482, CommunityMech:000484, CommunityMech:000493,
    CommunityMech:000498, CommunityMech:000499, CommunityMech:000500, CommunityMech:000502,
    CommunityMech:000503, CommunityMech:000504.'
  target_ids:
  - cohort:BIOREMEDIATION
  - CommunityMech:000374
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 92.1
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 88
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 60.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 88
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-biotechnology
  area: completeness
  topic: Cohort review of BIOTECHNOLOGY (96 records)
  outcome: concern
  summary: Cohort BIOTECHNOLOGY comprises 96 records (304 taxa, 255 ecological interactions,
    96 downstream causal edges, 0 inline UniProtKB gene annotations, 8 reusable CommonTaxon
    links) with mean Completeness Score 89.94/100 (min 50/100).
  details: 'Reviewed member records (96): CommunityMech:000009, CommunityMech:000029,
    CommunityMech:000036, CommunityMech:000091, CommunityMech:000092, CommunityMech:000117,
    CommunityMech:000126, CommunityMech:000139, CommunityMech:000146, CommunityMech:000149,
    CommunityMech:000151, CommunityMech:000152, CommunityMech:000153, CommunityMech:000154,
    CommunityMech:000164, CommunityMech:000165, CommunityMech:000167, CommunityMech:000170,
    CommunityMech:000171, CommunityMech:000172, CommunityMech:000173, CommunityMech:000175,
    CommunityMech:000177, CommunityMech:000185, CommunityMech:000198, CommunityMech:000202,
    CommunityMech:000203, CommunityMech:000204, CommunityMech:000207, CommunityMech:000210,
    CommunityMech:000211, CommunityMech:000213, CommunityMech:000214, CommunityMech:000241,
    CommunityMech:000244, CommunityMech:000266, CommunityMech:000269, CommunityMech:000278,
    CommunityMech:000279, CommunityMech:000283, CommunityMech:000284, CommunityMech:000287,
    CommunityMech:000294, CommunityMech:000295, CommunityMech:000306, CommunityMech:000326,
    CommunityMech:000329, CommunityMech:000330, CommunityMech:000332, CommunityMech:000333,
    CommunityMech:000343, CommunityMech:000345, CommunityMech:000354, CommunityMech:000355,
    CommunityMech:000356, CommunityMech:000357, CommunityMech:000359, CommunityMech:000363,
    CommunityMech:000365, CommunityMech:000366, CommunityMech:000372, CommunityMech:000378,
    CommunityMech:000390, CommunityMech:000395, CommunityMech:000397, CommunityMech:000399,
    CommunityMech:000400, CommunityMech:000402, CommunityMech:000408, CommunityMech:000412,
    CommunityMech:000415, CommunityMech:000417, CommunityMech:000418, CommunityMech:000422,
    CommunityMech:000425, CommunityMech:000430, CommunityMech:000431, CommunityMech:000433,
    CommunityMech:000434, CommunityMech:000435, CommunityMech:000436, CommunityMech:000438,
    CommunityMech:000445, CommunityMech:000447, CommunityMech:000448, CommunityMech:000449,
    CommunityMech:000450, CommunityMech:000453, CommunityMech:000455, CommunityMech:000457,
    CommunityMech:000465, CommunityMech:000478, CommunityMech:000480, CommunityMech:000481,
    CommunityMech:000496, CommunityMech:000497.'
  target_ids:
  - cohort:BIOTECHNOLOGY
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000295
  - CommunityMech:000402
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 89.94
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 96
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 50.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 96
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-carbon-sequestration
  area: completeness
  topic: Cohort review of CARBON_SEQUESTRATION (12 records)
  outcome: concern
  summary: Cohort CARBON_SEQUESTRATION comprises 12 records (37 taxa, 39 ecological
    interactions, 18 downstream causal edges, 0 inline UniProtKB gene annotations,
    1 reusable CommonTaxon links) with mean Completeness Score 92.17/100 (min 80/100).
  details: 'Reviewed member records (12): CommunityMech:000054, CommunityMech:000137,
    CommunityMech:000169, CommunityMech:000192, CommunityMech:000197, CommunityMech:000215,
    CommunityMech:000224, CommunityMech:000227, CommunityMech:000233, CommunityMech:000251,
    CommunityMech:000261, CommunityMech:000298.'
  target_ids:
  - cohort:CARBON_SEQUESTRATION
  - CommunityMech:000054
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 92.17
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 12
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 80.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 12
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-diet
  area: completeness
  topic: Cohort review of DIET (11 records)
  outcome: supported
  summary: Cohort DIET comprises 11 records (34 taxa, 32 ecological interactions,
    12 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon
    links) with mean Completeness Score 92.73/100 (min 85/100).
  details: 'Reviewed member records (11): CommunityMech:000032, CommunityMech:000033,
    CommunityMech:000201, CommunityMech:000281, CommunityMech:000296, CommunityMech:000317,
    CommunityMech:000349, CommunityMech:000401, CommunityMech:000464, CommunityMech:000466,
    CommunityMech:000474.'
  target_ids:
  - cohort:DIET
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 92.73
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 11
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 85.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 11
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-extreme-environment
  area: completeness
  topic: Cohort review of EXTREME_ENVIRONMENT (16 records)
  outcome: concern
  summary: Cohort EXTREME_ENVIRONMENT comprises 16 records (61 taxa, 53 ecological
    interactions, 11 downstream causal edges, 0 inline UniProtKB gene annotations,
    0 reusable CommonTaxon links) with mean Completeness Score 89.19/100 (min 80/100).
  details: 'Reviewed member records (16): CommunityMech:000046, CommunityMech:000062,
    CommunityMech:000140, CommunityMech:000218, CommunityMech:000222, CommunityMech:000234,
    CommunityMech:000237, CommunityMech:000242, CommunityMech:000243, CommunityMech:000252,
    CommunityMech:000260, CommunityMech:000308, CommunityMech:000309, CommunityMech:000319,
    CommunityMech:000339, CommunityMech:000494.'
  target_ids:
  - cohort:EXTREME_ENVIRONMENT
  - CommunityMech:000222
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 89.19
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 16
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 80.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 16
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-isolates-biomining
  area: completeness
  topic: Cohort review of ISOLATES:BIOMINING (4 records)
  outcome: supported
  summary: Cohort ISOLATES:BIOMINING comprises 4 records (4 taxa, 14 ecological interactions,
    9 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 93.75/100 (min 91/100).
  details: 'Reviewed member records (4): CommunityMech:000320, CommunityMech:000322,
    CommunityMech:000489, CommunityMech:000490.'
  target_ids:
  - cohort:ISOLATES:BIOMINING
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 93.75
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 4
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 91.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 4
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-isolates-bioremediation
  area: completeness
  topic: Cohort review of ISOLATES:BIOREMEDIATION (2 records)
  outcome: supported
  summary: Cohort ISOLATES:BIOREMEDIATION comprises 2 records (2 taxa, 5 ecological
    interactions, 3 downstream causal edges, 0 inline UniProtKB gene annotations,
    0 reusable CommonTaxon links) with mean Completeness Score 95.00/100 (min 95/100).
  details: 'Reviewed member records (2): CommunityMech:000488, CommunityMech:000492.'
  target_ids:
  - cohort:ISOLATES:BIOREMEDIATION
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 95.0
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 95.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-isolates-biotechnology
  area: completeness
  topic: Cohort review of ISOLATES:BIOTECHNOLOGY (2 records)
  outcome: supported
  summary: Cohort ISOLATES:BIOTECHNOLOGY comprises 2 records (2 taxa, 5 ecological
    interactions, 2 downstream causal edges, 0 inline UniProtKB gene annotations,
    0 reusable CommonTaxon links) with mean Completeness Score 93.00/100 (min 91/100).
  details: 'Reviewed member records (2): CommunityMech:000273, CommunityMech:000321.'
  target_ids:
  - cohort:ISOLATES:BIOTECHNOLOGY
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 93.0
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 91.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-isolates-extreme-environment
  area: completeness
  topic: Cohort review of ISOLATES:EXTREME_ENVIRONMENT (1 records)
  outcome: supported
  summary: Cohort ISOLATES:EXTREME_ENVIRONMENT comprises 1 records (1 taxa, 3 ecological
    interactions, 2 downstream causal edges, 0 inline UniProtKB gene annotations,
    0 reusable CommonTaxon links) with mean Completeness Score 92.00/100 (min 92/100).
  details: 'Reviewed member records (1): CommunityMech:000495.'
  target_ids:
  - cohort:ISOLATES:EXTREME_ENVIRONMENT
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 92.0
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 1
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 92.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 1
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-lignocellulose
  area: completeness
  topic: Cohort review of LIGNOCELLULOSE (37 records)
  outcome: concern
  summary: Cohort LIGNOCELLULOSE comprises 37 records (127 taxa, 110 ecological interactions,
    54 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 94.97/100 (min 85/100).
  details: 'Reviewed member records (37): CommunityMech:000041, CommunityMech:000048,
    CommunityMech:000061, CommunityMech:000075, CommunityMech:000118, CommunityMech:000119,
    CommunityMech:000120, CommunityMech:000156, CommunityMech:000168, CommunityMech:000178,
    CommunityMech:000179, CommunityMech:000180, CommunityMech:000193, CommunityMech:000194,
    CommunityMech:000195, CommunityMech:000196, CommunityMech:000205, CommunityMech:000206,
    CommunityMech:000208, CommunityMech:000263, CommunityMech:000264, CommunityMech:000265,
    CommunityMech:000267, CommunityMech:000270, CommunityMech:000275, CommunityMech:000277,
    CommunityMech:000282, CommunityMech:000286, CommunityMech:000297, CommunityMech:000323,
    CommunityMech:000338, CommunityMech:000383, CommunityMech:000389, CommunityMech:000398,
    CommunityMech:000407, CommunityMech:000421, CommunityMech:000473.'
  target_ids:
  - cohort:LIGNOCELLULOSE
  - CommunityMech:000048
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 94.97
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 37
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 85.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 37
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-metal-reduction
  area: completeness
  topic: Cohort review of METAL_REDUCTION (3 records)
  outcome: supported
  summary: Cohort METAL_REDUCTION comprises 3 records (8 taxa, 10 ecological interactions,
    10 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon
    links) with mean Completeness Score 94.33/100 (min 90/100).
  details: 'Reviewed member records (3): CommunityMech:000017, CommunityMech:000262,
    CommunityMech:000268.'
  target_ids:
  - cohort:METAL_REDUCTION
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 94.33
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 3
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 90.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 3
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-methanogenesis
  area: completeness
  topic: Cohort review of METHANOGENESIS (17 records)
  outcome: supported
  summary: Cohort METHANOGENESIS comprises 17 records (57 taxa, 59 ecological interactions,
    22 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 96.53/100 (min 90/100).
  details: 'Reviewed member records (17): CommunityMech:000021, CommunityMech:000089,
    CommunityMech:000135, CommunityMech:000174, CommunityMech:000182, CommunityMech:000219,
    CommunityMech:000226, CommunityMech:000246, CommunityMech:000254, CommunityMech:000255,
    CommunityMech:000256, CommunityMech:000257, CommunityMech:000258, CommunityMech:000274,
    CommunityMech:000380, CommunityMech:000394, CommunityMech:000416.'
  target_ids:
  - cohort:METHANOGENESIS
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 96.53
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 17
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 90.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 17
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-oral
  area: completeness
  topic: Cohort review of ORAL (5 records)
  outcome: supported
  summary: Cohort ORAL comprises 5 records (15 taxa, 15 ecological interactions, 6
    downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 92.40/100 (min 84/100).
  details: 'Reviewed member records (5): CommunityMech:000081, CommunityMech:000082,
    CommunityMech:000083, CommunityMech:000084, CommunityMech:000085.'
  target_ids:
  - cohort:ORAL
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 92.4
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 5
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 84.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 5
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-other
  area: completeness
  topic: Cohort review of OTHER (44 records)
  outcome: supported
  summary: Cohort OTHER comprises 44 records (192 taxa, 129 ecological interactions,
    45 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 87.98/100 (min 55/100).
  details: 'Reviewed member records (44): CommunityMech:000010, CommunityMech:000011,
    CommunityMech:000012, CommunityMech:000013, CommunityMech:000037, CommunityMech:000055,
    CommunityMech:000065, CommunityMech:000066, CommunityMech:000067, CommunityMech:000080,
    CommunityMech:000086, CommunityMech:000093, CommunityMech:000122, CommunityMech:000123,
    CommunityMech:000124, CommunityMech:000125, CommunityMech:000127, CommunityMech:000128,
    CommunityMech:000133, CommunityMech:000144, CommunityMech:000145, CommunityMech:000159,
    CommunityMech:000160, CommunityMech:000161, CommunityMech:000220, CommunityMech:000223,
    CommunityMech:000240, CommunityMech:000248, CommunityMech:000249, CommunityMech:000253,
    CommunityMech:000293, CommunityMech:000315, CommunityMech:000318, CommunityMech:000346,
    CommunityMech:000351, CommunityMech:000360, CommunityMech:000364, CommunityMech:000377,
    CommunityMech:000382, CommunityMech:000392, CommunityMech:000396, CommunityMech:000423,
    CommunityMech:000432, CommunityMech:000443.'
  target_ids:
  - cohort:OTHER
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 87.98
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 44
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 55.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 44
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-phage-predation
  area: completeness
  topic: Cohort review of PHAGE_PREDATION (2 records)
  outcome: supported
  summary: Cohort PHAGE_PREDATION comprises 2 records (11 taxa, 10 ecological interactions,
    3 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 83.00/100 (min 83/100).
  details: 'Reviewed member records (2): CommunityMech:000467, CommunityMech:000468.'
  target_ids:
  - cohort:PHAGE_PREDATION
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 83.0
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 83.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-phytoplankton
  area: completeness
  topic: Cohort review of PHYTOPLANKTON (19 records)
  outcome: supported
  summary: Cohort PHYTOPLANKTON comprises 19 records (60 taxa, 59 ecological interactions,
    18 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 95.00/100 (min 84/100).
  details: 'Reviewed member records (19): CommunityMech:000014, CommunityMech:000015,
    CommunityMech:000016, CommunityMech:000020, CommunityMech:000056, CommunityMech:000130,
    CommunityMech:000131, CommunityMech:000143, CommunityMech:000147, CommunityMech:000155,
    CommunityMech:000162, CommunityMech:000191, CommunityMech:000259, CommunityMech:000325,
    CommunityMech:000381, CommunityMech:000441, CommunityMech:000446, CommunityMech:000451,
    CommunityMech:000452.'
  target_ids:
  - cohort:PHYTOPLANKTON
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 95.0
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 19
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 84.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 19
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-rhizosphere
  area: completeness
  topic: Cohort review of RHIZOSPHERE (81 records)
  outcome: concern
  summary: Cohort RHIZOSPHERE comprises 81 records (411 taxa, 257 ecological interactions,
    86 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 87.01/100 (min 55/100).
  details: 'Reviewed member records (81): CommunityMech:000003, CommunityMech:000022,
    CommunityMech:000025, CommunityMech:000028, CommunityMech:000039, CommunityMech:000040,
    CommunityMech:000043, CommunityMech:000047, CommunityMech:000050, CommunityMech:000058,
    CommunityMech:000063, CommunityMech:000064, CommunityMech:000072, CommunityMech:000076,
    CommunityMech:000077, CommunityMech:000078, CommunityMech:000079, CommunityMech:000087,
    CommunityMech:000088, CommunityMech:000090, CommunityMech:000094, CommunityMech:000095,
    CommunityMech:000096, CommunityMech:000097, CommunityMech:000098, CommunityMech:000099,
    CommunityMech:000100, CommunityMech:000101, CommunityMech:000102, CommunityMech:000103,
    CommunityMech:000104, CommunityMech:000105, CommunityMech:000106, CommunityMech:000107,
    CommunityMech:000108, CommunityMech:000109, CommunityMech:000110, CommunityMech:000129,
    CommunityMech:000216, CommunityMech:000221, CommunityMech:000225, CommunityMech:000235,
    CommunityMech:000236, CommunityMech:000245, CommunityMech:000247, CommunityMech:000250,
    CommunityMech:000272, CommunityMech:000280, CommunityMech:000302, CommunityMech:000304,
    CommunityMech:000310, CommunityMech:000311, CommunityMech:000312, CommunityMech:000313,
    CommunityMech:000314, CommunityMech:000316, CommunityMech:000341, CommunityMech:000347,
    CommunityMech:000348, CommunityMech:000367, CommunityMech:000368, CommunityMech:000373,
    CommunityMech:000375, CommunityMech:000376, CommunityMech:000391, CommunityMech:000393,
    CommunityMech:000403, CommunityMech:000409, CommunityMech:000414, CommunityMech:000419,
    CommunityMech:000427, CommunityMech:000428, CommunityMech:000429, CommunityMech:000456,
    CommunityMech:000458, CommunityMech:000459, CommunityMech:000460, CommunityMech:000472,
    CommunityMech:000477, CommunityMech:000483, CommunityMech:000501.'
  target_ids:
  - cohort:RHIZOSPHERE
  - CommunityMech:000302
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 87.01
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 81
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 55.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 81
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-syntrophy
  area: completeness
  topic: Cohort review of SYNTROPHY (34 records)
  outcome: supported
  summary: Cohort SYNTROPHY comprises 34 records (83 taxa, 113 ecological interactions,
    66 downstream causal edges, 0 inline UniProtKB gene annotations, 2 reusable CommonTaxon
    links) with mean Completeness Score 95.94/100 (min 84/100).
  details: 'Reviewed member records (34): CommunityMech:000006, CommunityMech:000007,
    CommunityMech:000008, CommunityMech:000018, CommunityMech:000023, CommunityMech:000031,
    CommunityMech:000052, CommunityMech:000053, CommunityMech:000068, CommunityMech:000069,
    CommunityMech:000070, CommunityMech:000071, CommunityMech:000134, CommunityMech:000141,
    CommunityMech:000142, CommunityMech:000148, CommunityMech:000150, CommunityMech:000157,
    CommunityMech:000158, CommunityMech:000186, CommunityMech:000187, CommunityMech:000188,
    CommunityMech:000189, CommunityMech:000190, CommunityMech:000276, CommunityMech:000288,
    CommunityMech:000290, CommunityMech:000307, CommunityMech:000327, CommunityMech:000336,
    CommunityMech:000337, CommunityMech:000350, CommunityMech:000469, CommunityMech:000475.'
  target_ids:
  - cohort:SYNTROPHY
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 95.94
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 34
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 84.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 34
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-taxa
  area: completeness
  topic: Cohort review of TAXA (2 records)
  outcome: supported
  summary: Cohort TAXA comprises 2 records (2 taxa, 0 ecological interactions, 0 downstream
    causal edges, 9 inline UniProtKB gene annotations, 0 reusable CommonTaxon links)
    with mean Completeness Score 100.00/100 (min 100/100).
  details: 'Reviewed member records (2): CommunityMech:taxon:000001, CommunityMech:taxon:000002.'
  target_ids:
  - cohort:TAXA
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 100.0
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 100.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
findings:
- finding_id: c6s4-000374-sl8-sl12-functional-roles
  issue_key: c6s4-000374-sl8-sl12-functional-roles
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture (CommunityMech:000374)
    omits functional_role on both Achromobacter sp. SL8 and Enterobacter sp. SL12
  description: 'In kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    (CommunityMech:000374), both taxonomy[0] (Achromobacter sp. SL8, NCBITaxon:222)
    and taxonomy[1] (Enterobacter sp. SL12, NCBITaxon:547) record abundance_level:
    ABUNDANT at a 1:1 (v/v) co-inoculation ratio, but both omit functional_role. The
    cited open-access source PMID:42307251 (PMC13340288, doi:10.3390/microorganisms14061493)
    explicitly establishes that Achromobacter sp. SL8 and Enterobacter sp. SL12 act
    as synergistic extracellular-polymeric-substance (EPS)-producing and CdS-precipitating
    partners (functional_role: [SYNTROPHIC_PARTNER, BIOFILM_FORMER]) whose co-culture
    stimulates polysaccharide and protein secretion, cell aggregation, and up-regulation
    of cysteine biosynthesis (cysK) and sulfate transport to immobilize Cd2+.'
  target_ids:
  - CommunityMech:000374
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  evidence_ids:
  - ev-completeness-audit
  - ev-sl8-sl12-pmid42307251
  rule_id: review-yaml-record:taxonomy-functional-role-completeness
  native_severity: P2
  normalization_reason: Missing source-backed functional_role on both members of a
    two-strain cadmium-immobilizing co-culture causes scripts/audit_completeness.py
    required-block failure (25/100) and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
  tags:
  - actionable-stage5
  - bioremediation-cohort
  - completeness
- finding_id: c6s4-000402-shewanella-anammox-roles-and-abundance
  issue_key: c6s4-000402-shewanella-anammox-roles-and-abundance
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium (CommunityMech:000402)
    omits functional_role and abundance_level across all three taxonomy entries
  description: 'In kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
    (CommunityMech:000402), taxonomy[0] (Delta nrfA Shewanella oneidensis MR-1, NCBITaxon:211586),
    taxonomy[1] (Candidatus Brocadia anammox bacteria, NCBITaxon:380240), and taxonomy[2]
    (endogenous activated-sludge heterotrophic bacteria, NCBITaxon:2) all omit functional_role
    and abundance_level. The cited open-access source PMID:42655905 (PMC13519132,
    doi:10.1002/advs.77600) establishes Delta nrfA S. oneidensis MR-1 as the engineered
    partial-denitrifying nitrite-supplying cross-feeder and syntrophic partner (functional_role:
    [CROSS_FEEDER, SYNTROPHIC_PARTNER]; abundance_level: ABUNDANT), Candidatus Brocadia
    as the dominant anammox syntrophic partner (functional_role: [SYNTROPHIC_PARTNER,
    CROSS_FEEDER]; abundance_level: DOMINANT, enriched to 7%~10% of community abundance),
    and endogenous activated-sludge heterotrophic bacteria as the organic-matter-fermenting
    syntrophic guild providing volatile fatty acids and amino acids to Delta nrfA
    S. oneidensis (functional_role: [SYNTROPHIC_PARTNER, SECONDARY_FERMENTER]; abundance_level:
    ABUNDANT).'
  target_ids:
  - CommunityMech:000402
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - taxonomy[1].abundance_level
  - taxonomy[2].functional_role
  - taxonomy[2].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-shewanella-anammox-pmid42655905
  rule_id: review-yaml-record:taxonomy-functional-role-completeness
  native_severity: P2
  normalization_reason: Missing source-backed functional_role and abundance_level
    across all three guilds of an engineered partial-denitrification-anammox consortium
    causes scripts/audit_completeness.py required-block failure (25/100) and maps
    to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
    role: canonical_record
  tags:
  - actionable-stage5
  - biotechnology-cohort
  - completeness
- finding_id: c6s4-000404-wollastonite-cms1-role-and-abundance
  issue_key: c6s4-000404-wollastonite-cms1-role-and-abundance
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium (CommunityMech:000404)
    omits functional_role on Ramichloridium apiculatum CMS-1 and abundance_level on
    both fungal members
  description: 'In kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
    (CommunityMech:000404), taxonomy[0] (Ramichloridium apiculatum CMS-1, NCBITaxon:222813)
    omits both functional_role and abundance_level, while taxonomy[1] (Talaromyces
    pseudofuniculosus hzt-3'', NCBITaxon:28568) records functional_role: [CROSS_FEEDER]
    but omits abundance_level. The cited open-access source PMID:42478817 (PMC13488302,
    doi:10.3390/jof12070581) establishes that at the optimal CMS-1 : hzt-3'' = 1:4
    inoculum ratio (20% CMS-1, 80% hzt-3''), R. apiculatum CMS-1 acts as the carbonic-anhydrase-
    and cellulase-producing syntrophic cross-feeder (functional_role: [CROSS_FEEDER,
    SYNTROPHIC_PARTNER]; abundance_level: ABUNDANT) and T. pseudofuniculosus hzt-3''
    is the dominant organic-acid-secreting wollastonite-dissolving partner (functional_role:
    [CROSS_FEEDER, SYNTROPHIC_PARTNER]; abundance_level: DOMINANT).'
  target_ids:
  - CommunityMech:000404
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  - taxonomy[1].functional_role
  - taxonomy[1].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-wollastonite-pmid42478817
  rule_id: review-yaml-record:taxonomy-functional-role-completeness
  native_severity: P2
  normalization_reason: Missing source-backed functional_role on Ramichloridium apiculatum
    CMS-1 and abundance_level on both 1:4 fungal consortium members causes scripts/audit_completeness.py
    required-block failure (25/100) and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
    role: canonical_record
  tags:
  - actionable-stage5
  - biomining-cohort
  - completeness
- finding_id: cheese-assay-evidence-gap
  issue_key: cheese-assay-evidence-gap
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Pairwise in-vitro assay evidence in Cheese Rind Model Community (CommunityMech:000153)
    remains abstract-limited
  description: Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153)
    cites PMID:25043025 abstract for community-wide moisture and pH interactions;
    specific pairwise bacterial-fungal assay details reside in full-text figures/tables
    not present in the abstract cache.
  target_ids:
  - CommunityMech:000153
  field_paths:
  - ecological_interactions
  evidence_ids:
  - ev-prior-structured-reviews
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
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/765
  tags:
  - carried-forward
  - source-limited
- finding_id: communitymech-1467-source-discrepancy-and-extension
  issue_key: communitymech-1467-source-discrepancy-and-extension
  category: completeness
  severity: minor
  status: deferred
  certainty: confirmed
  title: GLBRC Transwell SynCom (CommunityMech:000091) broader 18-species campaign
    and strain-detail extension remains source-limited
  description: 'GLBRC_Exometabolite_Transwell_SynCom.yaml (CommunityMech:000091) captures
    the abstract-supported five-member model system; broader 18-species screening
    campaign and strain-level table details require full-text tables tracked in #1467.'
  target_ids:
  - CommunityMech:000091
  field_paths:
  - taxonomy
  - ecological_interactions
  evidence_ids:
  - ev-prior-structured-reviews
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: 'Source-limited extension tracked in open issue #1467 maps
    to minor.'
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
  title: Additional heterotrophic co-isolates in Phormidium Alkaline Consortium (CommunityMech:000054)
    require full-text tables
  description: Phormidium_Alkaline_Consortium.yaml (CommunityMech:000054) curates
    the primary cyanobacterial-heterotroph interactions supported by cached abstracts;
    full heterotrophic member enumeration requires full-text tables (#1699).
  target_ids:
  - CommunityMech:000054
  field_paths:
  - taxonomy
  evidence_ids:
  - ev-prior-structured-reviews
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text co-isolate enumeration gap preserved
    as minor.
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
  - ev-prior-structured-reviews
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
  - ev-prior-structured-reviews
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
  - ev-prior-structured-reviews
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
  - ev-prior-structured-reviews
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
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
  tags:
  - carried-forward
  - source-limited
actions:
- action_id: act-populate-sl8-sl12-functional-roles
  description: 'Add functional_role: [SYNTROPHIC_PARTNER, BIOFILM_FORMER] to both
    Achromobacter sp. SL8 (taxonomy[0]) and Enterobacter sp. SL12 (taxonomy[1]) backed
    by PMID:42307251 (PMC13340288) on CommunityMech:000374, and append curation_history.'
  finding_ids:
  - c6s4-000374-sl8-sl12-functional-roles
  target_ids:
  - CommunityMech:000374
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
  - just validate-history history
- action_id: act-populate-shewanella-anammox-roles-and-abundance
  description: 'Add functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level:
    ABUNDANT to Delta nrfA Shewanella oneidensis MR-1 (taxonomy[0]), add functional_role:
    [SYNTROPHIC_PARTNER, CROSS_FEEDER] and abundance_level: DOMINANT to Candidatus
    Brocadia anammox bacteria (taxonomy[1]), add functional_role: [SYNTROPHIC_PARTNER,
    SECONDARY_FERMENTER] and abundance_level: ABUNDANT to endogenous activated-sludge
    heterotrophic bacteria (taxonomy[2]) backed by PMID:42655905 (PMC13519132) on
    CommunityMech:000402, and append curation_history.'
  finding_ids:
  - c6s4-000402-shewanella-anammox-roles-and-abundance
  target_ids:
  - CommunityMech:000402
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Shewanella_Anammox_Delta_nrfA_Nitrite_Coupled_Consortium.yaml
  - just validate-history history
- action_id: act-populate-wollastonite-cms1-role-and-abundance
  description: 'Add functional_role: [CROSS_FEEDER, SYNTROPHIC_PARTNER] and abundance_level:
    ABUNDANT to Ramichloridium apiculatum CMS-1 (taxonomy[0]), and add abundance_level:
    DOMINANT and SYNTROPHIC_PARTNER to Talaromyces pseudofuniculosus hzt-3'' (taxonomy[1])
    backed by PMID:42478817 (PMC13488302) on CommunityMech:000404, and append curation_history.'
  finding_ids:
  - c6s4-000404-wollastonite-cms1-role-and-abundance
  target_ids:
  - CommunityMech:000404
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Wollastonite_Ramichloridium_Talaromyces_Fungal_Consortium.yaml
  - just validate-history history
- action_id: act-defer-source-limited-fulltext-findings-c6s4
  description: Retain source-limited full-text findings until open-access full text
    or supplementary strain/assay tables become available for CommunityMech:000048,
    000054, 000091, 000153, 000222, 000295, and 000302.
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
  - Verify full-text table availability before modifying abstract-grounded claims
    on source-limited records.
boundary_decisions:
- action: split
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000402
  - CommunityMech:000404
  - cohort:AMD
  - cohort:BIOMINING
  - cohort:BIOREMEDIATION
  - cohort:BIOTECHNOLOGY
  - cohort:CARBON_SEQUESTRATION
  - cohort:DIET
  - cohort:EXTREME_ENVIRONMENT
  - cohort:ISOLATES:BIOMINING
  - cohort:ISOLATES:BIOREMEDIATION
  - cohort:ISOLATES:BIOTECHNOLOGY
  - cohort:ISOLATES:EXTREME_ENVIRONMENT
  - cohort:LIGNOCELLULOSE
  - cohort:METAL_REDUCTION
  - cohort:METHANOGENESIS
  - cohort:ORAL
  - cohort:OTHER
  - cohort:PHAGE_PREDATION
  - cohort:PHYTOPLANKTON
  - cohort:RHIZOSPHERE
  - cohort:SYNTROPHY
  - cohort:TAXA
  rationale: The full 500-record CommunityMech corpus spans 3 record roots (kb/communities/,
    data/isolates/, kb/taxa/) and 16 ecological categories, which is over-broad for
    a single unpartitioned cohort. Splitting by root and community_category yields
    21 disjoint, ecologically coherent cohorts (16 community cohorts, 4 isolate cohorts,
    and 1 TAXA cohort) for comparative rubric evaluation.
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  proposed_groups:
  - label: AMD
    target_ids:
    - cohort:AMD
  - label: BIOMINING
    target_ids:
    - cohort:BIOMINING
    - CommunityMech:000404
  - label: BIOREMEDIATION
    target_ids:
    - cohort:BIOREMEDIATION
    - CommunityMech:000374
  - label: BIOTECHNOLOGY
    target_ids:
    - cohort:BIOTECHNOLOGY
    - CommunityMech:000091
    - CommunityMech:000153
    - CommunityMech:000295
    - CommunityMech:000402
  - label: CARBON_SEQUESTRATION
    target_ids:
    - cohort:CARBON_SEQUESTRATION
    - CommunityMech:000054
  - label: DIET
    target_ids:
    - cohort:DIET
  - label: EXTREME_ENVIRONMENT
    target_ids:
    - cohort:EXTREME_ENVIRONMENT
    - CommunityMech:000222
  - label: ISOLATES:BIOMINING
    target_ids:
    - cohort:ISOLATES:BIOMINING
  - label: ISOLATES:BIOREMEDIATION
    target_ids:
    - cohort:ISOLATES:BIOREMEDIATION
  - label: ISOLATES:BIOTECHNOLOGY
    target_ids:
    - cohort:ISOLATES:BIOTECHNOLOGY
  - label: ISOLATES:EXTREME_ENVIRONMENT
    target_ids:
    - cohort:ISOLATES:EXTREME_ENVIRONMENT
  - label: LIGNOCELLULOSE
    target_ids:
    - cohort:LIGNOCELLULOSE
    - CommunityMech:000048
  - label: METAL_REDUCTION
    target_ids:
    - cohort:METAL_REDUCTION
  - label: METHANOGENESIS
    target_ids:
    - cohort:METHANOGENESIS
  - label: ORAL
    target_ids:
    - cohort:ORAL
  - label: OTHER
    target_ids:
    - cohort:OTHER
  - label: PHAGE_PREDATION
    target_ids:
    - cohort:PHAGE_PREDATION
  - label: PHYTOPLANKTON
    target_ids:
    - cohort:PHYTOPLANKTON
  - label: RHIZOSPHERE
    target_ids:
    - cohort:RHIZOSPHERE
    - CommunityMech:000302
  - label: SYNTROPHY
    target_ids:
    - cohort:SYNTROPHY
  - label: TAXA
    target_ids:
    - cohort:TAXA
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261104T180000Z-c6s4-record-deep-audit
  relationship: companion_per_record_deep_audit
- repository: CultureBotAI/CommunityMech
  review_id: 20261104T034100Z-c5s4-frozen-cohort-review
  relationship: prior_cycle_stage4_cohort_review
- repository: CultureBotAI/CommunityMech
  review_id: 20261104T060000Z-c5s5-remediation-verification
  relationship: prior_cycle_stage5_remediation_review
limitations:
- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- 'Seven carried-forward community records remain source-limited because cached abstracts
  do not provide full-text assay or strain tables (#765, #1467, #1657, #1681, #1699,
  #1841, #1847).'
tags:
- cycle6
- stage4
- cohort-review
- full-corpus
```
