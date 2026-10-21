# Stage 4 Full-Corpus Frozen Inventory and Cohort Review (479 Records Across 19 Cohorts)

- Review: 20261021T101100Z-stage4-frozen-cohort-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-10-21T09:50:00Z
- Finished UTC: 2026-10-21T10:11:00Z
- Reviewer: antigravity-stage4-cohort-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full-corpus frozen inventory and cohort review of all 479 eligible CommunityMech records (473 kb/communities/*.yaml, 4 data/isolates/*.yaml, 2 kb/taxa/*.yaml) partitioned into 19 disjoint domain cohorts at commit 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b. All 479 records pass LinkML schema validation and EvidenceSourceEnum checks; mean Completeness Score across 477 MicrobialCommunity records is 85.06/100 (median 90/100). Six actionable open findings (3 major/P2, 3 minor/P3) across 12 records and 7 carried-forward source-limited deferred findings are preserved for Stage 5 grouped remediation.

## Scope And Provenance

Exhaustive cohort review of all 19 domain/root cohorts (encompassing all 479 eligible records across kb/communities/*.yaml, data/isolates/*.yaml, and kb/taxa/*.yaml) plus all 19 finding-bearing records.

Selection: All 19 domain/root cohorts (479 records total; full per-record SHA-256 inventory in frozen_inventory_metrics.tsv) and all 19 finding-bearing records at Git commit 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Coverage: full; 38 reviewed / 38 in the declared population.
Source: git_commit at Git base 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000048 | kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml | maintained | CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium) |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | CommunityMech:000054 (Phormidium Alkaline Consortium) |
| CommunityMech:000091 | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml | maintained | CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System) |
| CommunityMech:000153 | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml | maintained | CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community) |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml | maintained | CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm) |
| CommunityMech:000273 | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml | maintained | CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform) |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic Co-culture) |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience) |
| CommunityMech:000321 | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml | maintained | CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model) |
| CommunityMech:000339 | kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml | maintained | CommunityMech:000339 (Space Habitat Seven-Member Stress-Tolerance SynCom) |
| CommunityMech:000347 | kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml | maintained | CommunityMech:000347 (Bacillus siamensis-vallismortis HT Masson Pine SynCom) |
| CommunityMech:000360 | kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml | maintained | CommunityMech:000360 (Wolffia Mankai Endosphere Cobamide Guild) |
| CommunityMech:000364 | kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml | maintained | CommunityMech:000364 (Sclerotinia Sclerotia 12-Strain Biocontrol SynCom) |
| CommunityMech:000373 | kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml | maintained | CommunityMech:000373 (Bacillus G12-Y4-X25 Tobacco Biocontrol SynCom) |
| CommunityMech:000399 | kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml | maintained | CommunityMech:000399 (Pseudomonas aeruginosa Eight-Strain Full-Factorial SynCom) |
| CommunityMech:000415 | kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml | maintained | CommunityMech:000415 (Algal-Methanotroph Biogas Valorization Coculture) |
| CommunityMech:000433 | kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml | maintained | CommunityMech:000433 (Nitrifying Wastewater Ammonia-Oxidizing Consortium) |
| CommunityMech:000434 | kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml | maintained | CommunityMech:000434 (Acidic Nitrification Minimal Consortium) |
| CommunityMech:000447 | kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml | maintained | CommunityMech:000447 (Brocadia Low-Nitrogen Anammox Consortium) |
| cohort:AMD | kb/communities/AMD_Acidophile_Heterotroph_Network.yaml # cohort=AMD;records=7 | snapshot_row | AMD cohort (7 records) |
| cohort:BIOMINING | kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml # cohort=BIOMINING;records=13 | snapshot_row | BIOMINING cohort (13 records) |
| cohort:BIOREMEDIATION | kb/communities/Australian_Lead_Zinc_Polymetallic.yaml # cohort=BIOREMEDIATION;records=80 | snapshot_row | BIOREMEDIATION cohort (80 records) |
| cohort:BIOTECHNOLOGY | kb/communities/BioModels_MODEL2204300001_Kefir_Community_Model.yaml # cohort=BIOTECHNOLOGY;records=94 | snapshot_row | BIOTECHNOLOGY cohort (94 records) |
| cohort:CARBON_SEQUESTRATION | kb/communities/Phormidium_Alkaline_Consortium.yaml # cohort=CARBON_SEQUESTRATION;records=12 | snapshot_row | CARBON_SEQUESTRATION cohort (12 records) |
| cohort:DIET | kb/communities/Geobacter_Methanosaeta_DIET.yaml # cohort=DIET;records=11 | snapshot_row | DIET cohort (11 records) |
| cohort:EXTREME_ENVIRONMENT | kb/communities/Naica_Deep_Subsurface_Thermophilic.yaml # cohort=EXTREME_ENVIRONMENT;records=15 | snapshot_row | EXTREME_ENVIRONMENT cohort (15 records) |
| cohort:ISOLATES:BIOMINING | data/isolates/Aspergillus_Indium_LED_Recovery.yaml # cohort=ISOLATES:BIOMINING;records=2 | snapshot_row | ISOLATES:BIOMINING cohort (2 records) |
| cohort:ISOLATES:BIOTECHNOLOGY | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml # cohort=ISOLATES:BIOTECHNOLOGY;records=2 | snapshot_row | ISOLATES:BIOTECHNOLOGY cohort (2 records) |
| cohort:LIGNOCELLULOSE | kb/communities/MAMC_M48_Lignocellulose.yaml # cohort=LIGNOCELLULOSE;records=37 | snapshot_row | LIGNOCELLULOSE cohort (37 records) |
| cohort:METAL_REDUCTION | kb/communities/Chromium_Sulfur_Reduction_Enrichment.yaml # cohort=METAL_REDUCTION;records=3 | snapshot_row | METAL_REDUCTION cohort (3 records) |
| cohort:METHANOGENESIS | kb/communities/DVM_Triculture.yaml # cohort=METHANOGENESIS;records=17 | snapshot_row | METHANOGENESIS cohort (17 records) |
| cohort:ORAL | kb/communities/Early_Dental_Biofilm_FiveSpecies.yaml # cohort=ORAL;records=5 | snapshot_row | ORAL cohort (5 records) |
| cohort:OTHER | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml # cohort=OTHER;records=44 | snapshot_row | OTHER cohort (44 records) |
| cohort:PHAGE_PREDATION | kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml # cohort=PHAGE_PREDATION;records=2 | snapshot_row | PHAGE_PREDATION cohort (2 records) |
| cohort:PHYTOPLANKTON | kb/communities/Chlamydomonas_Bacterial_H2_Consortium.yaml # cohort=PHYTOPLANKTON;records=19 | snapshot_row | PHYTOPLANKTON cohort (19 records) |
| cohort:RHIZOSPHERE | kb/communities/At_RSPHERE_SynCom.yaml # cohort=RHIZOSPHERE;records=80 | snapshot_row | RHIZOSPHERE cohort (80 records) |
| cohort:SYNTROPHY | kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml # cohort=SYNTROPHY;records=34 | snapshot_row | SYNTROPHY cohort (34 records) |
| cohort:TAXA | kb/taxa/Shewanella_oneidensis_MR1.yaml # cohort=TAXA;records=2 | snapshot_row | TAXA cohort (2 records) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation across all 479 records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000273, CommunityMech:000295, CommunityMech:000302, CommunityMech:000321, CommunityMech:000339, CommunityMech:000347, CommunityMech:000360, CommunityMech:000364, CommunityMech:000373, CommunityMech:000399, CommunityMech:000415, CommunityMech:000433, CommunityMech:000434, CommunityMech:000447, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOTECHNOLOGY, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | All 477 MicrobialCommunity records and 2 TaxonRecord files pass LinkML schema validation with 0 errors and 100% EvidenceItem.evidence_source enum compliance. |
| NetworkIntegrityAuditor check across kb/communities/ | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000273, CommunityMech:000295, CommunityMech:000302, CommunityMech:000321, CommunityMech:000339, CommunityMech:000347, CommunityMech:000360, CommunityMech:000364, CommunityMech:000373, CommunityMech:000399, CommunityMech:000415, CommunityMech:000433, CommunityMech:000434, CommunityMech:000447, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOTECHNOLOGY, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | 452/473 community records have 0 network warnings; 21 records have 57 non-fatal warnings (50 DISCONNECTED_TAXON, 7 UNKNOWN_TARGET, 0 broken downstream references). |
| review-communities Completeness Score rubric across all 479 records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000273, CommunityMech:000295, CommunityMech:000302, CommunityMech:000321, CommunityMech:000339, CommunityMech:000347, CommunityMech:000360, CommunityMech:000364, CommunityMech:000373, CommunityMech:000399, CommunityMech:000415, CommunityMech:000433, CommunityMech:000434, CommunityMech:000447, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOTECHNOLOGY, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | Computed proportional Completeness Score (min 40, median 90, mean 85.06, max 100) and verified causal graph coverage across all 19 cohorts. |

## Scientific And Domain Assessments

### Cohort review of AMD (7 records)

completeness: supported. Targets: cohort:AMD.

Cohort AMD comprises 7 records (34 taxa, 29 ecological interactions, 8 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 87.57/100 (min 86/100).

Reviewed member records (7): CommunityMech:000001, CommunityMech:000002, CommunityMech:000027, CommunityMech:000034, CommunityMech:000059, CommunityMech:000074, CommunityMech:000353.

### Cohort review of BIOMINING (13 records)

completeness: supported. Targets: cohort:BIOMINING.

Cohort BIOMINING comprises 13 records (40 taxa, 48 ecological interactions, 20 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 84.00/100 (min 75/100).

Reviewed member records (13): CommunityMech:000005, CommunityMech:000019, CommunityMech:000026, CommunityMech:000035, CommunityMech:000045, CommunityMech:000049, CommunityMech:000057, CommunityMech:000073, CommunityMech:000217, CommunityMech:000303, CommunityMech:000305, CommunityMech:000385, CommunityMech:000404.

### Cohort review of BIOREMEDIATION (80 records)

completeness: supported. Targets: cohort:BIOREMEDIATION.

Cohort BIOREMEDIATION comprises 80 records (284 taxa, 207 ecological interactions, 85 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 84.69/100 (min 60/100).

Reviewed member records (80): CommunityMech:000004, CommunityMech:000024, CommunityMech:000030, CommunityMech:000038, CommunityMech:000042, CommunityMech:000044, CommunityMech:000051, CommunityMech:000060, CommunityMech:000111, CommunityMech:000112, CommunityMech:000113, CommunityMech:000114, CommunityMech:000115, CommunityMech:000116, CommunityMech:000121, CommunityMech:000132, CommunityMech:000136, CommunityMech:000138, CommunityMech:000163, CommunityMech:000166, CommunityMech:000176, CommunityMech:000181, CommunityMech:000183, CommunityMech:000184, CommunityMech:000199, CommunityMech:000200, CommunityMech:000209, CommunityMech:000238, CommunityMech:000239, CommunityMech:000271, CommunityMech:000285, CommunityMech:000289, CommunityMech:000291, CommunityMech:000292, CommunityMech:000299, CommunityMech:000300, CommunityMech:000301, CommunityMech:000324, CommunityMech:000328, CommunityMech:000331, CommunityMech:000334, CommunityMech:000335, CommunityMech:000340, CommunityMech:000342, CommunityMech:000344, CommunityMech:000352, CommunityMech:000358, CommunityMech:000361, CommunityMech:000362, CommunityMech:000369, CommunityMech:000370, CommunityMech:000371, CommunityMech:000374, CommunityMech:000379, CommunityMech:000384, CommunityMech:000386, CommunityMech:000387, CommunityMech:000388, CommunityMech:000405, CommunityMech:000406, CommunityMech:000410, CommunityMech:000411, CommunityMech:000413, CommunityMech:000420, CommunityMech:000424, CommunityMech:000426, CommunityMech:000437, CommunityMech:000439, CommunityMech:000440, CommunityMech:000442, CommunityMech:000444, CommunityMech:000454, CommunityMech:000461, CommunityMech:000462, CommunityMech:000463, CommunityMech:000470, CommunityMech:000471, CommunityMech:000476, CommunityMech:000479, CommunityMech:000482.

### Cohort review of BIOTECHNOLOGY (94 records)

completeness: concern. Targets: cohort:BIOTECHNOLOGY, CommunityMech:000091, CommunityMech:000153, CommunityMech:000295, CommunityMech:000399, CommunityMech:000415, CommunityMech:000433, CommunityMech:000434, CommunityMech:000447.

Cohort BIOTECHNOLOGY comprises 94 records (300 taxa, 249 ecological interactions, 92 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 83.76/100 (min 55/100).

Reviewed member records (94): CommunityMech:000009, CommunityMech:000029, CommunityMech:000036, CommunityMech:000091, CommunityMech:000092, CommunityMech:000117, CommunityMech:000126, CommunityMech:000139, CommunityMech:000146, CommunityMech:000149, CommunityMech:000151, CommunityMech:000152, CommunityMech:000153, CommunityMech:000154, CommunityMech:000164, CommunityMech:000165, CommunityMech:000167, CommunityMech:000170, CommunityMech:000171, CommunityMech:000172, CommunityMech:000173, CommunityMech:000175, CommunityMech:000177, CommunityMech:000185, CommunityMech:000198, CommunityMech:000202, CommunityMech:000203, CommunityMech:000204, CommunityMech:000207, CommunityMech:000210, CommunityMech:000211, CommunityMech:000213, CommunityMech:000214, CommunityMech:000241, CommunityMech:000244, CommunityMech:000266, CommunityMech:000269, CommunityMech:000278, CommunityMech:000279, CommunityMech:000283, CommunityMech:000284, CommunityMech:000287, CommunityMech:000294, CommunityMech:000295, CommunityMech:000306, CommunityMech:000326, CommunityMech:000329, CommunityMech:000330, CommunityMech:000332, CommunityMech:000333, CommunityMech:000343, CommunityMech:000345, CommunityMech:000354, CommunityMech:000355, CommunityMech:000356, CommunityMech:000357, CommunityMech:000359, CommunityMech:000363, CommunityMech:000365, CommunityMech:000366, CommunityMech:000372, CommunityMech:000378, CommunityMech:000390, CommunityMech:000395, CommunityMech:000397, CommunityMech:000399, CommunityMech:000400, CommunityMech:000402, CommunityMech:000408, CommunityMech:000412, CommunityMech:000415, CommunityMech:000417, CommunityMech:000418, CommunityMech:000422, CommunityMech:000425, CommunityMech:000430, CommunityMech:000431, CommunityMech:000433, CommunityMech:000434, CommunityMech:000435, CommunityMech:000436, CommunityMech:000438, CommunityMech:000445, CommunityMech:000447, CommunityMech:000448, CommunityMech:000449, CommunityMech:000450, CommunityMech:000453, CommunityMech:000455, CommunityMech:000457, CommunityMech:000465, CommunityMech:000478, CommunityMech:000480, CommunityMech:000481.

### Cohort review of CARBON_SEQUESTRATION (12 records)

completeness: concern. Targets: cohort:CARBON_SEQUESTRATION, CommunityMech:000054.

Cohort CARBON_SEQUESTRATION comprises 12 records (37 taxa, 39 ecological interactions, 18 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 86.42/100 (min 75/100).

Reviewed member records (12): CommunityMech:000054, CommunityMech:000137, CommunityMech:000169, CommunityMech:000192, CommunityMech:000197, CommunityMech:000215, CommunityMech:000224, CommunityMech:000227, CommunityMech:000233, CommunityMech:000251, CommunityMech:000261, CommunityMech:000298.

### Cohort review of DIET (11 records)

completeness: supported. Targets: cohort:DIET.

Cohort DIET comprises 11 records (34 taxa, 32 ecological interactions, 12 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 86.09/100 (min 77/100).

Reviewed member records (11): CommunityMech:000032, CommunityMech:000033, CommunityMech:000201, CommunityMech:000281, CommunityMech:000296, CommunityMech:000317, CommunityMech:000349, CommunityMech:000401, CommunityMech:000464, CommunityMech:000466, CommunityMech:000474.

### Cohort review of EXTREME_ENVIRONMENT (15 records)

completeness: concern. Targets: cohort:EXTREME_ENVIRONMENT, CommunityMech:000222, CommunityMech:000339.

Cohort EXTREME_ENVIRONMENT comprises 15 records (54 taxa, 51 ecological interactions, 10 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 85.27/100 (min 75/100).

Reviewed member records (15): CommunityMech:000046, CommunityMech:000062, CommunityMech:000140, CommunityMech:000218, CommunityMech:000222, CommunityMech:000234, CommunityMech:000237, CommunityMech:000242, CommunityMech:000243, CommunityMech:000252, CommunityMech:000260, CommunityMech:000308, CommunityMech:000309, CommunityMech:000319, CommunityMech:000339.

### Cohort review of ISOLATES:BIOMINING (2 records)

completeness: supported. Targets: cohort:ISOLATES:BIOMINING.

Cohort ISOLATES:BIOMINING comprises 2 records (2 taxa, 9 ecological interactions, 6 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 87.50/100 (min 86/100).

Reviewed member records (2): CommunityMech:000320, CommunityMech:000322.

### Cohort review of ISOLATES:BIOTECHNOLOGY (2 records)

completeness: concern. Targets: cohort:ISOLATES:BIOTECHNOLOGY, CommunityMech:000273, CommunityMech:000321.

Cohort ISOLATES:BIOTECHNOLOGY comprises 2 records (2 taxa, 5 ecological interactions, 2 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 83.50/100 (min 80/100).

Reviewed member records (2): CommunityMech:000273, CommunityMech:000321.

### Cohort review of LIGNOCELLULOSE (37 records)

completeness: concern. Targets: cohort:LIGNOCELLULOSE, CommunityMech:000048.

Cohort LIGNOCELLULOSE comprises 37 records (127 taxa, 110 ecological interactions, 54 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 88.03/100 (min 77/100).

Reviewed member records (37): CommunityMech:000041, CommunityMech:000048, CommunityMech:000061, CommunityMech:000075, CommunityMech:000118, CommunityMech:000119, CommunityMech:000120, CommunityMech:000156, CommunityMech:000168, CommunityMech:000178, CommunityMech:000179, CommunityMech:000180, CommunityMech:000193, CommunityMech:000194, CommunityMech:000195, CommunityMech:000196, CommunityMech:000205, CommunityMech:000206, CommunityMech:000208, CommunityMech:000263, CommunityMech:000264, CommunityMech:000265, CommunityMech:000267, CommunityMech:000270, CommunityMech:000275, CommunityMech:000277, CommunityMech:000282, CommunityMech:000286, CommunityMech:000297, CommunityMech:000323, CommunityMech:000338, CommunityMech:000383, CommunityMech:000389, CommunityMech:000398, CommunityMech:000407, CommunityMech:000421, CommunityMech:000473.

### Cohort review of METAL_REDUCTION (3 records)

completeness: supported. Targets: cohort:METAL_REDUCTION.

Cohort METAL_REDUCTION comprises 3 records (8 taxa, 10 ecological interactions, 10 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 86.00/100 (min 85/100).

Reviewed member records (3): CommunityMech:000017, CommunityMech:000262, CommunityMech:000268.

### Cohort review of METHANOGENESIS (17 records)

completeness: supported. Targets: cohort:METHANOGENESIS.

Cohort METHANOGENESIS comprises 17 records (57 taxa, 59 ecological interactions, 22 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 88.88/100 (min 85/100).

Reviewed member records (17): CommunityMech:000021, CommunityMech:000089, CommunityMech:000135, CommunityMech:000174, CommunityMech:000182, CommunityMech:000219, CommunityMech:000226, CommunityMech:000246, CommunityMech:000254, CommunityMech:000255, CommunityMech:000256, CommunityMech:000257, CommunityMech:000258, CommunityMech:000274, CommunityMech:000380, CommunityMech:000394, CommunityMech:000416.

### Cohort review of ORAL (5 records)

completeness: supported. Targets: cohort:ORAL.

Cohort ORAL comprises 5 records (15 taxa, 15 ecological interactions, 6 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 79.00/100 (min 77/100).

Reviewed member records (5): CommunityMech:000081, CommunityMech:000082, CommunityMech:000083, CommunityMech:000084, CommunityMech:000085.

### Cohort review of OTHER (44 records)

completeness: concern. Targets: cohort:OTHER, CommunityMech:000360, CommunityMech:000364.

Cohort OTHER comprises 44 records (192 taxa, 129 ecological interactions, 45 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 83.48/100 (min 55/100).

Reviewed member records (44): CommunityMech:000010, CommunityMech:000011, CommunityMech:000012, CommunityMech:000013, CommunityMech:000037, CommunityMech:000055, CommunityMech:000065, CommunityMech:000066, CommunityMech:000067, CommunityMech:000080, CommunityMech:000086, CommunityMech:000093, CommunityMech:000122, CommunityMech:000123, CommunityMech:000124, CommunityMech:000125, CommunityMech:000127, CommunityMech:000128, CommunityMech:000133, CommunityMech:000144, CommunityMech:000145, CommunityMech:000159, CommunityMech:000160, CommunityMech:000161, CommunityMech:000220, CommunityMech:000223, CommunityMech:000240, CommunityMech:000248, CommunityMech:000249, CommunityMech:000253, CommunityMech:000293, CommunityMech:000315, CommunityMech:000318, CommunityMech:000346, CommunityMech:000351, CommunityMech:000360, CommunityMech:000364, CommunityMech:000377, CommunityMech:000382, CommunityMech:000392, CommunityMech:000396, CommunityMech:000423, CommunityMech:000432, CommunityMech:000443.

### Cohort review of PHAGE_PREDATION (2 records)

completeness: supported. Targets: cohort:PHAGE_PREDATION.

Cohort PHAGE_PREDATION comprises 2 records (11 taxa, 10 ecological interactions, 3 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 77.50/100 (min 77/100).

Reviewed member records (2): CommunityMech:000467, CommunityMech:000468.

### Cohort review of PHYTOPLANKTON (19 records)

completeness: supported. Targets: cohort:PHYTOPLANKTON.

Cohort PHYTOPLANKTON comprises 19 records (60 taxa, 59 ecological interactions, 18 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 88.11/100 (min 80/100).

Reviewed member records (19): CommunityMech:000014, CommunityMech:000015, CommunityMech:000016, CommunityMech:000020, CommunityMech:000056, CommunityMech:000130, CommunityMech:000131, CommunityMech:000143, CommunityMech:000147, CommunityMech:000155, CommunityMech:000162, CommunityMech:000191, CommunityMech:000259, CommunityMech:000325, CommunityMech:000381, CommunityMech:000441, CommunityMech:000446, CommunityMech:000451, CommunityMech:000452.

### Cohort review of RHIZOSPHERE (80 records)

completeness: concern. Targets: cohort:RHIZOSPHERE, CommunityMech:000302, CommunityMech:000347, CommunityMech:000373.

Cohort RHIZOSPHERE comprises 80 records (406 taxa, 254 ecological interactions, 86 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 82.58/100 (min 55/100).

Reviewed member records (80): CommunityMech:000003, CommunityMech:000022, CommunityMech:000025, CommunityMech:000028, CommunityMech:000039, CommunityMech:000040, CommunityMech:000043, CommunityMech:000047, CommunityMech:000050, CommunityMech:000058, CommunityMech:000063, CommunityMech:000064, CommunityMech:000072, CommunityMech:000076, CommunityMech:000077, CommunityMech:000078, CommunityMech:000079, CommunityMech:000087, CommunityMech:000088, CommunityMech:000090, CommunityMech:000094, CommunityMech:000095, CommunityMech:000096, CommunityMech:000097, CommunityMech:000098, CommunityMech:000099, CommunityMech:000100, CommunityMech:000101, CommunityMech:000102, CommunityMech:000103, CommunityMech:000104, CommunityMech:000105, CommunityMech:000106, CommunityMech:000107, CommunityMech:000108, CommunityMech:000109, CommunityMech:000110, CommunityMech:000129, CommunityMech:000216, CommunityMech:000221, CommunityMech:000225, CommunityMech:000235, CommunityMech:000236, CommunityMech:000245, CommunityMech:000247, CommunityMech:000250, CommunityMech:000272, CommunityMech:000280, CommunityMech:000302, CommunityMech:000304, CommunityMech:000310, CommunityMech:000311, CommunityMech:000312, CommunityMech:000313, CommunityMech:000314, CommunityMech:000316, CommunityMech:000341, CommunityMech:000347, CommunityMech:000348, CommunityMech:000367, CommunityMech:000368, CommunityMech:000373, CommunityMech:000375, CommunityMech:000376, CommunityMech:000391, CommunityMech:000393, CommunityMech:000403, CommunityMech:000409, CommunityMech:000414, CommunityMech:000419, CommunityMech:000427, CommunityMech:000428, CommunityMech:000429, CommunityMech:000456, CommunityMech:000458, CommunityMech:000459, CommunityMech:000460, CommunityMech:000472, CommunityMech:000477, CommunityMech:000483.

### Cohort review of SYNTROPHY (34 records)

completeness: supported. Targets: cohort:SYNTROPHY.

Cohort SYNTROPHY comprises 34 records (83 taxa, 113 ecological interactions, 66 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness Score 87.65/100 (min 72/100).

Reviewed member records (34): CommunityMech:000006, CommunityMech:000007, CommunityMech:000008, CommunityMech:000018, CommunityMech:000023, CommunityMech:000031, CommunityMech:000052, CommunityMech:000053, CommunityMech:000068, CommunityMech:000069, CommunityMech:000070, CommunityMech:000071, CommunityMech:000134, CommunityMech:000141, CommunityMech:000142, CommunityMech:000148, CommunityMech:000150, CommunityMech:000157, CommunityMech:000158, CommunityMech:000186, CommunityMech:000187, CommunityMech:000188, CommunityMech:000189, CommunityMech:000190, CommunityMech:000276, CommunityMech:000288, CommunityMech:000290, CommunityMech:000307, CommunityMech:000327, CommunityMech:000336, CommunityMech:000337, CommunityMech:000350, CommunityMech:000469, CommunityMech:000475.

### Cohort review of TAXA (2 records)

completeness: supported. Targets: cohort:TAXA.

Cohort TAXA comprises 2 records (2 taxa, 0 ecological interactions, 0 downstream causal edges, 9 UniProtKB gene annotations) with mean Completeness Score 100.00/100 (min 100/100).

Reviewed member records (2): CommunityMech:taxon:000001, CommunityMech:taxon:000002.

## Findings

### stage4-missing-community-origin-000434: CommunityMech:000434 omits community_origin despite acidic nitrification bioreactor operation in PMID:42762737

major / open / confirmed; issue key: communitymech-stage4-000434-missing-origin.

Acidic_Nitrification_Minimal_Consortium.yaml (CommunityMech:000434) is the only MicrobialCommunity record in the 477-community corpus missing community_origin. The cited abstract (PMID:42762737) describes three acidic nitrification bioreactors operated between pH 2.0 and 5.0 where the pH 2.0 bioreactor hosts a simplified consortium dominated by "Candidatus Nitrosoglobus kelleri" and Mycobacterium species, supporting community_origin: ENGINEERED.

### stage4-missing-ecological-state-000360: CommunityMech:000360 omits ecological_state despite persistent host-filtered endosphere guild maintenance in PMID:42304541

major / open / confirmed; issue key: communitymech-stage4-000360-missing-state.

Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml (CommunityMech:000360) is the only MicrobialCommunity record in the 477-community corpus missing ecological_state. The cited source (PMID:42304541) describes a persistent host-filtered endosphere cobamide-producing guild assembled and maintained in a stable host-mediated niche, supporting ecological_state: STABLE.

### stage4-disconnected-syncom-participants: Five SynCom/consortium records omit co-tested member taxa from COMMUNITY_LEVEL participating_taxa

minor / open / confirmed; issue key: communitymech-stage4-disconnected-syncom-participants.

NetworkIntegrityAuditor flags 14 DISCONNECTED_TAXON warnings across five records (CommunityMech:000339 Space_Habitat_SevenMember_Stress_Tolerance_SynCom [6 disconnected taxa: Sphingomonas paucimobilis, Cupriavidus metallidurans, Ralstonia pickettii, Acinetobacter radioresistens, Burkholderia cepacia, Chryseobacterium gleum], CommunityMech:000399 Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom [5 disconnected strains: H27, F2, F3, W6, M15], CommunityMech:000415 Algal_Methanotroph_Biogas_Valorization_Coculture [1 disconnected cyanobacterial primary producer: Leptolyngbya, NCBITaxon:47251], CommunityMech:000433 Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium [1 disconnected taxon: Legionella MAGs, NCBITaxon:445], and CommunityMech:000447 Brocadia_Low_Nitrogen_Anammox_Consortium [1 disconnected taxon: Candidatus Kuenenia early-acclimation lineage, NCBITaxon:174636]) where COMMUNITY_LEVEL ecological_interactions list only a subset of participating_taxa.

### stage4-external-host-pathogen-targets: Three biocontrol/rhizosphere SynCom records place external non-member hosts or pathogens in target_taxon

minor / open / confirmed; issue key: communitymech-stage4-external-host-pathogen-targets.

NetworkIntegrityAuditor flags all 7 UNKNOWN_TARGET warnings in the corpus across three records (CommunityMech:000347 Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom [3 warnings: Fusarium oxysporum on 1 interaction and Pinus massoniana on 2 interactions], CommunityMech:000364 Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom [2 warnings: Sclerotinia sclerotiorum on 2 interactions], and CommunityMech:000373 Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom [2 warnings: Nicotiana tabacum (tobacco, NCBITaxon:4097) on 2 interactions]) because external host plants and target phytopathogens outside taxonomy[] are modeled in target_taxon on COMMUNITY_LEVEL interactions.

### stage4-isolate-000273-unverified-ore-prose: CommunityMech:000273 retains unverified arsenopyrite ore recovery claims and un-evidenced environmental_factors

major / open / confirmed; issue key: communitymech-stage4-000273-unverified-ore-prose.

Although Stage 2 repaired ecological_interactions on data/isolates/Chromobacterium_Gold_Biocyanidation.yaml (CommunityMech:000273), its top-level description, environment_term.notes, taxonomy[0].taxon_term.notes, and 8 un-evidenced environmental_factors entries (7 ore/cyanide/pulp-density parameters and 1 temperature entry) still assert refractory gold-bearing sulfide ore (arsenopyrite/pyrite) bioleaching, 70-85% gold recovery, 50-200 ppm CN-, and 7-14 day leaching time that do not come from the cited waste-PCB bioleaching source (doi:10.1007/s10163-014-0276-4: Acidithiobacillus ferrooxidans pretreatment removing &gt;80% Cu followed by Chromobacterium violaceum bioleaching reaching 70.6% Au bioleaching efficiency vs 45.5% in direct bioleaching).

### stage4-isolate-000321-missing-functional-role: CommunityMech:000321 omits functional_role and abundance_level on its sole taxon entry

minor / open / confirmed; issue key: communitymech-stage4-000321-missing-role.

data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml (CommunityMech:000321) is the only record in data/isolates/ missing functional_role and abundance_level on taxonomy[0] (Rothia, NCBITaxon:32207, supported by PMID:33398099 and PMID:28963201), reducing its proportional Completeness Score to 80/100.

### cheese-assay-evidence-gap: Full-text-dependent cheese rind assay specifics remain deferred in CommunityMech:000153

minor / deferred / confirmed; issue key: cheese-assay-evidence-gap.

Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153) remains capped at abstract-verified taxa and interactions because strain-specific pairwise assay details in PMID:25043025 require full-text table inspection.

Disposition: Deferred: source-limited until full-text assay tables for PMID:25043025 are ingested.

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

Disposition: Deferred: source-limited because primary full text is paywalled.

### parachlorella-remaining-research: Secondary metabolite exchange specifics in Parachlorella-Saccharomyces co-culture (CommunityMech:000295) require full-text data

minor / deferred / confirmed; issue key: parachlorella-remaining-research.

Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml (CommunityMech:000295) captures the primary abstract-supported algal-yeast mutualism; secondary metabolite exchange kinetics require full-text tables.

Disposition: Deferred: source-limited pending full-text interaction data.

## Recommended Actions And Acceptance Checks

### act-set-community-origin-000434

Set community_origin: ENGINEERED on CommunityMech:000434 (Acidic_Nitrification_Minimal_Consortium.yaml) and append a curation_history entry.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-set-ecological-state-000360

Set ecological_state: STABLE on CommunityMech:000360 (Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml) and append a curation_history entry.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-connect-syncom-participants

Populate full abstract-backed participating_taxa on COMMUNITY_LEVEL ecological_interactions in CommunityMech:000339, 000399, 000415, 000433, and 000447.

- just audit-network
- uv run python scripts/verify_history_Changed_records.py

### act-remove-external-host-pathogen-targets

Replace external non-member host/pathogen target_taxon entries on COMMUNITY_LEVEL interactions in CommunityMech:000347, 000364, and 000373 with member participating_taxa while preserving host/pathogen context in interaction name/description.

- just audit-network
- uv run python scripts/verify_history_Changed_records.py

### act-reconcile-isolate-000273-prose

Align description, environment_term.notes, taxonomy[0].taxon_term.notes, and environmental_factors in data/isolates/Chromobacterium_Gold_Biocyanidation.yaml (CommunityMech:000273) strictly to the cited waste-PCB bioleaching source (doi:10.1007/s10163-014-0276-4).

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-populate-isolate-000321-role

Populate functional_role and abundance_level on taxonomy[0] in data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml (CommunityMech:000321) supported by PMID:33398099 and PMID:28963201.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
- uv run python scripts/verify_history_Changed_records.py

### act-defer-source-limited-fulltext-findings

Retain source-limited full-text findings until open-access full text or supplementary strain/assay tables become available for CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify full-text table availability before modifying abstract-grounded claims on source-limited records.

## Category Boundaries

- split: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000273, CommunityMech:000295, CommunityMech:000302, CommunityMech:000321, CommunityMech:000339, CommunityMech:000347, CommunityMech:000360, CommunityMech:000364, CommunityMech:000373, CommunityMech:000399, CommunityMech:000415, CommunityMech:000433, CommunityMech:000434, CommunityMech:000447, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOTECHNOLOGY, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA. The full 479-record CommunityMech corpus spans 3 record roots (kb/communities/, data/isolates/, kb/taxa/) and 16 ecological categories, which is over-broad for a single unpartitioned cohort. Splitting by root and community_category yields 19 disjoint, ecologically coherent cohorts for comparative rubric evaluation.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and TaxonRecord classes | supports | All 473 kb/communities/*.yaml, 4 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | .claude/skills/review-communities/SKILL.md; Section 5: Completeness Score (0-100) and Validation Quality Score (0-100) | supports | Proportional Completeness Score audit across all 477 MicrobialCommunity records (min 40, median 90, mean 85.06, max 100) identified 2 core metadata omissions (CommunityMech:000434 missing community_origin; CommunityMech:000360 missing ecological_state) and 1 isolate missing functional_role (CommunityMech:000321, Completeness Score 80/100). |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | Network integrity audit across 473 kb/communities records found 452 records with 0 warnings and 21 records with 57 warnings (50 DISCONNECTED_TAXON, 7 UNKNOWN_TARGET across 44 issue categories), of which 5 SynCom/guild records have 14 remediable disconnected member taxa and 3 biocontrol records place external hosts/pathogens in target_taxon across 7 interaction entries. |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-478 | supports | Corpus-wide causal graph inventory covers all 477 MicrobialCommunity records (423 reviewed with evidence-backed causal structure, 54 needs_research source-limited, 0 unreviewed). |
| ev-000434-pmid42762737 | PMID:42762737; references_cache/PMID_42762737.txt | supports | Cached PubMed abstract PMID:42762737 describes operating acidic nitrification bioreactors between pH 2.0 and 5.0, with the pH 2.0 bioreactor hosting a strongly simplified community dominated by "Candidatus Nitrosoglobus kelleri" and Mycobacterium species. |
| ev-000360-pmid42304541 | PMID:42304541; references_cache/PMID_42304541.txt | supports | Cached PubMed abstract PMID:42304541 describes a persistent host-filtered endosphere cobamide-producing bacterial guild assembled and maintained in a stable host-mediated niche within Wolffia globosa Mankai. |
| ev-isolate-000273-audit | data/isolates/Chromobacterium_Gold_Biocyanidation.yaml; description, environment_term.notes, taxonomy[0].taxon_term.notes, environmental_factors | refutes | Non-graph prose and 8 un-evidenced environmental_factors (7 ore/cyanide/pulp-density parameters and 1 temperature entry) in CommunityMech:000273 still claim refractory arsenopyrite ore bioleaching (70-85% Au recovery, 50-200 ppm CN-, 7-14 days) rather than the two-step waste-PCB bioleaching reported by doi:10.1007/s10163-014-0276-4 (Acidithiobacillus ferrooxidans pretreatment removing &gt;80% Cu followed by Chromobacterium violaceum bioleaching reaching 70.6% Au bioleaching efficiency vs 45.5% in direct bioleaching). |
| ev-isolate-000321-audit | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml; taxonomy[0] | supports | CommunityMech:000321 is a valid single-species GSMM baseline record for Rothia (PMID:33398099, PMID:28963201; Completeness Score 80/100) but omits functional_role and abundance_level on taxonomy[0]. |
| ev-prior-structured-reviews | reviews/structured; 40 retained structured review bundles through 20261016T091936Z | context_only | Lineage inspection of all 40 prior structured reviews identified 7 record-scoped source-limited findings that remain unresolved at commit 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b and are carried forward as deferred. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- 54 records in reports/causal_graph_review/inventory.tsv remain source-limited (needs_research) because cached abstracts do not provide multi-step causal chains or full-text assay tables.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101100Z-stage4-frozen-cohort-review
kind: category
repository: CultureBotAI/CommunityMech
title: Stage 4 Full-Corpus Frozen Inventory and Cohort Review (479 Records Across
  19 Cohorts)
started_at: '2026-10-21T09:50:00Z'
finished_at: '2026-10-21T10:11:00Z'
reviewer:
  identity: antigravity-stage4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated Stage 4 full-corpus read-only review pass over frozen
    commit 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b without record mutation.
skill: review-yaml-category
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION (460/479 records pass without unresolved findings;
  6 new actionable open findings across 12 records and 7 carried-forward source-limited
  deferred findings across 7 records)
scientific_review: true
summary: Full-corpus frozen inventory and cohort review of all 479 eligible CommunityMech
  records (473 kb/communities/*.yaml, 4 data/isolates/*.yaml, 2 kb/taxa/*.yaml) partitioned
  into 19 disjoint domain cohorts at commit 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
  All 479 records pass LinkML schema validation and EvidenceSourceEnum checks; mean
  Completeness Score across 477 MicrobialCommunity records is 85.06/100 (median 90/100).
  Six actionable open findings (3 major/P2, 3 minor/P3) across 12 records and 7 carried-forward
  source-limited deferred findings are preserved for Stage 5 grouped remediation.
source:
  git_revision: 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b
  state: git_commit
  inputs:
  - path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
    sha256: c9ebc23ad2748751ae6a42fbc2340c5f7524a7aa38185bcad4602b7e56734d9d
    role: target
  - path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    sha256: b73ac6cd532c8fb20c7d1fa70979b2a220238069f0ce78c7b6c9d66af2524ab8
    role: target
  - path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    sha256: 6f859fe8ba028743e55e8b77565c2ee747df5b436e7d3741728af6e037850fa2
    role: target
  - path: docs/record-review-profile.md
    sha256: 285f79747999f83edbe63e5efde349a5cc063e9e486ce1a748b47b76c6631f31
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: kb/communities/AMD_Acidophile_Heterotroph_Network.yaml
    sha256: 81fe29292038349e959041675b876ef4e351cdfb6884796989540185c6797834
    role: target
  - path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
    sha256: 376423d5910b761cc88aa6d9afe44204a7c275ed3e8873fef1a56c4def1e19c9
    role: target
  - path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    sha256: 3e009885b98b2aa6b6763fb5386ab60f764367d5436db204e0aede39dc6e3331
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
  - path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    sha256: e0126b602878c9abada427f906334f6a059784e07b29c33b709c9a9549f0689f
    role: target
  - path: kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
    sha256: c0cb1ddb17e22f1fba3db44ecdb5cf8cc8a3412d23be6910a043851f23ce51d6
    role: target
  - path: kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml
    sha256: 655ff223cc2775123bf63fe23caa3445c1775988dd1d292a7a9edf79c4959a3f
    role: target
  - path: kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml
    sha256: f29ece197fbf2088caa649cbf78c0c2d0054d1434369353b29e7f6efdd05a848
    role: target
  - path: kb/communities/BioModels_MODEL2204300001_Kefir_Community_Model.yaml
    sha256: b2e55eea689446b15484d0b01ce6f0da687b66ddd2b5b6507e1677216b2619ea
    role: target
  - path: kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml
    sha256: 45ea96efd71094d61fc28d38e2ce107358b785f173e2982e48c87edf69ca73d6
    role: target
  - path: kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
    sha256: 227362963f3008129281c29d08829d1bf49aa57230b126cc7986e592c6cd9a96
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
  - path: kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
    sha256: 61a0b16fc00db138fa35884e8f9f170bda3b2cc9092008a9d5098b3600ad920a
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
  - path: kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml
    sha256: 5771a8a97beb8ccb19b6cccad32062d896b09747ce0670788686060481cf68b9
    role: target
  - path: kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml
    sha256: b76f915e08d08faf1516698a67c53bb6e25f912bd8d4803dfe55412f1a100a3e
    role: target
  - path: kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml
    sha256: 0304999156eeec1556a337ff0138a6bfce205c38b9d5a8010051d864949a2a7f
    role: target
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 904cc9646ae53fe0c021c1461a09f3f8d15b763edad42b6c9a43ada91c87597d
    role: target
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
    sha256: 829d29dcebcb9ba30483df9d1ec71eafb945a6a3bf966539ee6a16d9abd9077d
    role: target
  - path: kb/taxa/Shewanella_oneidensis_MR1.yaml
    sha256: abc63353af993a7e23f1e676dca15c7012add80ac20cb8827284a32ddbcc95bf
    role: target
  - path: reports/causal_graph_review/inventory.tsv
    sha256: cc95d8ac0dbf12aa50a3afd2a59fae72fbe5df1b89a636296f5b0e97cfe19fd0
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: d38c4ddc359b6987209ce5d12d5af119e6b64da51ee40d568fe4f8d382bcd56c
    role: context
  - path: src/communitymech/schema/communitymech.yaml
    sha256: c41630d09def826256ddb6678c1ce31fa71e3b074219bb9d217d98035a5324ee
    role: context
  - path: src/communitymech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
scope:
  description: Exhaustive cohort review of all 19 domain/root cohorts (encompassing
    all 479 eligible records across kb/communities/*.yaml, data/isolates/*.yaml, and
    kb/taxa/*.yaml) plus all 19 finding-bearing records.
  selection: All 19 domain/root cohorts (479 records total; full per-record SHA-256
    inventory in frozen_inventory_metrics.tsv) and all 19 finding-bearing records
    at Git commit 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b.
  coverage: full
  population_size: 38
  reviewed_target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000273
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000321
  - CommunityMech:000339
  - CommunityMech:000347
  - CommunityMech:000360
  - CommunityMech:000364
  - CommunityMech:000373
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000434
  - CommunityMech:000447
  - cohort:AMD
  - cohort:BIOMINING
  - cohort:BIOREMEDIATION
  - cohort:BIOTECHNOLOGY
  - cohort:CARBON_SEQUESTRATION
  - cohort:DIET
  - cohort:EXTREME_ENVIRONMENT
  - cohort:ISOLATES:BIOMINING
  - cohort:ISOLATES:BIOTECHNOLOGY
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
- target_id: CommunityMech:000273
  path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
  label: CommunityMech:000273 (Chromobacterium Gold Biocyanidation Platform)
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
- target_id: CommunityMech:000321
  path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  label: CommunityMech:000321 (BioModels MODEL2204300002 Kefir Rothia Model)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000339
  path: kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml
  label: CommunityMech:000339 (Space Habitat Seven-Member Stress-Tolerance SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000347
  path: kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
  label: CommunityMech:000347 (Bacillus siamensis-vallismortis HT Masson Pine SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000360
  path: kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
  label: CommunityMech:000360 (Wolffia Mankai Endosphere Cobamide Guild)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000364
  path: kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml
  label: CommunityMech:000364 (Sclerotinia Sclerotia 12-Strain Biocontrol SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000373
  path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
  label: CommunityMech:000373 (Bacillus G12-Y4-X25 Tobacco Biocontrol SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000399
  path: kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml
  label: CommunityMech:000399 (Pseudomonas aeruginosa Eight-Strain Full-Factorial
    SynCom)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000415
  path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
  label: CommunityMech:000415 (Algal-Methanotroph Biogas Valorization Coculture)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000433
  path: kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
  label: CommunityMech:000433 (Nitrifying Wastewater Ammonia-Oxidizing Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000434
  path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
  label: CommunityMech:000434 (Acidic Nitrification Minimal Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000447
  path: kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
  label: CommunityMech:000447 (Brocadia Low-Nitrogen Anammox Consortium)
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
  selector: cohort=BIOMINING;records=13
  label: BIOMINING cohort (13 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 13 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:BIOREMEDIATION
  path: kb/communities/Australian_Lead_Zinc_Polymetallic.yaml
  selector: cohort=BIOREMEDIATION;records=80
  label: BIOREMEDIATION cohort (80 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 80 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:BIOTECHNOLOGY
  path: kb/communities/BioModels_MODEL2204300001_Kefir_Community_Model.yaml
  selector: cohort=BIOTECHNOLOGY;records=94
  label: BIOTECHNOLOGY cohort (94 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 94 canonical records in CultureBotAI/CommunityMech (per-record
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
  selector: cohort=EXTREME_ENVIRONMENT;records=15
  label: EXTREME_ENVIRONMENT cohort (15 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 15 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ISOLATES:BIOMINING
  path: data/isolates/Aspergillus_Indium_LED_Recovery.yaml
  selector: cohort=ISOLATES:BIOMINING;records=2
  label: ISOLATES:BIOMINING cohort (2 records)
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
  selector: cohort=RHIZOSPHERE;records=80
  label: RHIZOSPHERE cohort (80 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 80 canonical records in CultureBotAI/CommunityMech (per-record
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
- check_id: chk-linkml-schema-all-479
  name: LinkML schema validation across all 479 records
  status: passed
  required: true
  summary: All 477 MicrobialCommunity records and 2 TaxonRecord files pass LinkML
    schema validation with 0 errors and 100% EvidenceItem.evidence_source enum compliance.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000273
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000321
  - CommunityMech:000339
  - CommunityMech:000347
  - CommunityMech:000360
  - CommunityMech:000364
  - CommunityMech:000373
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000434
  - CommunityMech:000447
  - cohort:AMD
  - cohort:BIOMINING
  - cohort:BIOREMEDIATION
  - cohort:BIOTECHNOLOGY
  - cohort:CARBON_SEQUESTRATION
  - cohort:DIET
  - cohort:EXTREME_ENVIRONMENT
  - cohort:ISOLATES:BIOMINING
  - cohort:ISOLATES:BIOTECHNOLOGY
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
  command: .venv/bin/python -c 'validate all 479 records against src/communitymech/schema/communitymech.yaml'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-schema-validation-gate
- check_id: chk-network-integrity-all
  name: NetworkIntegrityAuditor check across kb/communities/
  status: passed
  required: true
  summary: 452/473 community records have 0 network warnings; 21 records have 57 non-fatal
    warnings (50 DISCONNECTED_TAXON, 7 UNKNOWN_TARGET, 0 broken downstream references).
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000273
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000321
  - CommunityMech:000339
  - CommunityMech:000347
  - CommunityMech:000360
  - CommunityMech:000364
  - CommunityMech:000373
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000434
  - CommunityMech:000447
  - cohort:AMD
  - cohort:BIOMINING
  - cohort:BIOREMEDIATION
  - cohort:BIOTECHNOLOGY
  - cohort:CARBON_SEQUESTRATION
  - cohort:DIET
  - cohort:EXTREME_ENVIRONMENT
  - cohort:ISOLATES:BIOMINING
  - cohort:ISOLATES:BIOTECHNOLOGY
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
- check_id: chk-completeness-rubric-all
  name: review-communities Completeness Score rubric across all 479 records
  status: passed
  required: true
  summary: Computed proportional Completeness Score (min 40, median 90, mean 85.06,
    max 100) and verified causal graph coverage across all 19 cohorts.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000273
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000321
  - CommunityMech:000339
  - CommunityMech:000347
  - CommunityMech:000360
  - CommunityMech:000364
  - CommunityMech:000373
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000434
  - CommunityMech:000447
  - cohort:AMD
  - cohort:BIOMINING
  - cohort:BIOREMEDIATION
  - cohort:BIOTECHNOLOGY
  - cohort:CARBON_SEQUESTRATION
  - cohort:DIET
  - cohort:EXTREME_ENVIRONMENT
  - cohort:ISOLATES:BIOMINING
  - cohort:ISOLATES:BIOTECHNOLOGY
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
  command: .venv/bin/python -c 'compute proportional Completeness Score across all
    479 records'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-completeness-audit
  - ev-causal-inventory
evidence:
- evidence_id: ev-schema-validation-gate
  kind: validation
  reference: src/communitymech/schema/communitymech.yaml
  locator: MicrobialCommunity and TaxonRecord classes
  accessed_at: '2026-10-21T10:05:00Z'
  support: supports
  summary: All 473 kb/communities/*.yaml, 4 data/isolates/*.yaml, and 2 kb/taxa/*.yaml
    records pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum
    compliance.
- evidence_id: ev-completeness-audit
  kind: validation
  reference: .claude/skills/review-communities/SKILL.md
  locator: 'Section 5: Completeness Score (0-100) and Validation Quality Score (0-100)'
  accessed_at: '2026-10-21T10:06:00Z'
  support: supports
  summary: Proportional Completeness Score audit across all 477 MicrobialCommunity
    records (min 40, median 90, mean 85.06, max 100) identified 2 core metadata omissions
    (CommunityMech:000434 missing community_origin; CommunityMech:000360 missing ecological_state)
    and 1 isolate missing functional_role (CommunityMech:000321, Completeness Score
    80/100).
- evidence_id: ev-network-integrity-audit
  kind: validation
  reference: src/communitymech/network/auditor.py
  locator: NetworkIntegrityAuditor.audit_all()
  accessed_at: '2026-10-21T10:06:30Z'
  support: supports
  summary: Network integrity audit across 473 kb/communities records found 452 records
    with 0 warnings and 21 records with 57 warnings (50 DISCONNECTED_TAXON, 7 UNKNOWN_TARGET
    across 44 issue categories), of which 5 SynCom/guild records have 14 remediable
    disconnected member taxa and 3 biocontrol records place external hosts/pathogens
    in target_taxon across 7 interaction entries.
- evidence_id: ev-causal-inventory
  kind: record_content
  reference: reports/causal_graph_review/inventory.tsv
  locator: rows 1-478
  accessed_at: '2026-10-21T10:07:00Z'
  support: supports
  summary: Corpus-wide causal graph inventory covers all 477 MicrobialCommunity records
    (423 reviewed with evidence-backed causal structure, 54 needs_research source-limited,
    0 unreviewed).
- evidence_id: ev-000434-pmid42762737
  kind: primary_source
  reference: PMID:42762737
  locator: references_cache/PMID_42762737.txt
  accessed_at: '2026-10-21T10:07:30Z'
  support: supports
  summary: Cached PubMed abstract PMID:42762737 describes operating acidic nitrification
    bioreactors between pH 2.0 and 5.0, with the pH 2.0 bioreactor hosting a strongly
    simplified community dominated by "Candidatus Nitrosoglobus kelleri" and Mycobacterium
    species.
  quote: To address this gap, three acidic nitrification bioreactors were operated
    between pH 2.0 and 5.0. All systems achieved stable ammonia oxidation (34.4-51.8
    mg N L-1 d-1), despite pH 2.0 bioreactor hosting a strongly simplified community
    dominated by "Candidatus Nitrosoglobus kelleri" and Mycobacterium species.
- evidence_id: ev-000360-pmid42304541
  kind: primary_source
  reference: PMID:42304541
  locator: references_cache/PMID_42304541.txt
  accessed_at: '2026-10-21T10:07:45Z'
  support: supports
  summary: Cached PubMed abstract PMID:42304541 describes a persistent host-filtered
    endosphere cobamide-producing bacterial guild assembled and maintained in a stable
    host-mediated niche within Wolffia globosa Mankai.
- evidence_id: ev-isolate-000273-audit
  kind: record_content
  reference: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
  locator: description, environment_term.notes, taxonomy[0].taxon_term.notes, environmental_factors
  accessed_at: '2026-10-21T10:08:00Z'
  support: refutes
  summary: Non-graph prose and 8 un-evidenced environmental_factors (7 ore/cyanide/pulp-density
    parameters and 1 temperature entry) in CommunityMech:000273 still claim refractory
    arsenopyrite ore bioleaching (70-85% Au recovery, 50-200 ppm CN-, 7-14 days) rather
    than the two-step waste-PCB bioleaching reported by doi:10.1007/s10163-014-0276-4
    (Acidithiobacillus ferrooxidans pretreatment removing >80% Cu followed by Chromobacterium
    violaceum bioleaching reaching 70.6% Au bioleaching efficiency vs 45.5% in direct
    bioleaching).
- evidence_id: ev-isolate-000321-audit
  kind: record_content
  reference: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  locator: taxonomy[0]
  accessed_at: '2026-10-21T10:08:15Z'
  support: supports
  summary: CommunityMech:000321 is a valid single-species GSMM baseline record for
    Rothia (PMID:33398099, PMID:28963201; Completeness Score 80/100) but omits functional_role
    and abundance_level on taxonomy[0].
- evidence_id: ev-prior-structured-reviews
  kind: prior_review
  reference: reviews/structured
  locator: 40 retained structured review bundles through 20261016T091936Z
  accessed_at: '2026-10-21T10:08:30Z'
  support: context_only
  summary: Lineage inspection of all 40 prior structured reviews identified 7 record-scoped
    source-limited findings that remain unresolved at commit 00a4a35e57d262d57b5f1a66fc3b5bdc03ae715b
    and are carried forward as deferred.
assessments:
- assessment_id: assess-cohort-amd
  area: completeness
  topic: Cohort review of AMD (7 records)
  outcome: supported
  summary: Cohort AMD comprises 7 records (34 taxa, 29 ecological interactions, 8
    downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 87.57/100 (min 86/100).
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
  metrics:
  - name: mean_completeness_score
    value: 87.57
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 7
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 86.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 7
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-biomining
  area: completeness
  topic: Cohort review of BIOMINING (13 records)
  outcome: supported
  summary: Cohort BIOMINING comprises 13 records (40 taxa, 48 ecological interactions,
    20 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 84.00/100 (min 75/100).
  details: 'Reviewed member records (13): CommunityMech:000005, CommunityMech:000019,
    CommunityMech:000026, CommunityMech:000035, CommunityMech:000045, CommunityMech:000049,
    CommunityMech:000057, CommunityMech:000073, CommunityMech:000217, CommunityMech:000303,
    CommunityMech:000305, CommunityMech:000385, CommunityMech:000404.'
  target_ids:
  - cohort:BIOMINING
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 84.0
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 13
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 75.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 13
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-bioremediation
  area: completeness
  topic: Cohort review of BIOREMEDIATION (80 records)
  outcome: supported
  summary: Cohort BIOREMEDIATION comprises 80 records (284 taxa, 207 ecological interactions,
    85 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 84.69/100 (min 60/100).
  details: 'Reviewed member records (80): CommunityMech:000004, CommunityMech:000024,
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
    CommunityMech:000479, CommunityMech:000482.'
  target_ids:
  - cohort:BIOREMEDIATION
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 84.69
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 80
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 60.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 80
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-biotechnology
  area: completeness
  topic: Cohort review of BIOTECHNOLOGY (94 records)
  outcome: concern
  summary: Cohort BIOTECHNOLOGY comprises 94 records (300 taxa, 249 ecological interactions,
    92 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 83.76/100 (min 55/100).
  details: 'Reviewed member records (94): CommunityMech:000009, CommunityMech:000029,
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
    CommunityMech:000465, CommunityMech:000478, CommunityMech:000480, CommunityMech:000481.'
  target_ids:
  - cohort:BIOTECHNOLOGY
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000295
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000434
  - CommunityMech:000447
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 83.76
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 94
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 55.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 94
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-carbon-sequestration
  area: completeness
  topic: Cohort review of CARBON_SEQUESTRATION (12 records)
  outcome: concern
  summary: Cohort CARBON_SEQUESTRATION comprises 12 records (37 taxa, 39 ecological
    interactions, 18 downstream causal edges, 0 UniProtKB gene annotations) with mean
    Completeness Score 86.42/100 (min 75/100).
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
  metrics:
  - name: mean_completeness_score
    value: 86.42
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 12
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 75.0
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
    12 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 86.09/100 (min 77/100).
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
  metrics:
  - name: mean_completeness_score
    value: 86.09
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 11
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 77.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 11
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-extreme-environment
  area: completeness
  topic: Cohort review of EXTREME_ENVIRONMENT (15 records)
  outcome: concern
  summary: Cohort EXTREME_ENVIRONMENT comprises 15 records (54 taxa, 51 ecological
    interactions, 10 downstream causal edges, 0 UniProtKB gene annotations) with mean
    Completeness Score 85.27/100 (min 75/100).
  details: 'Reviewed member records (15): CommunityMech:000046, CommunityMech:000062,
    CommunityMech:000140, CommunityMech:000218, CommunityMech:000222, CommunityMech:000234,
    CommunityMech:000237, CommunityMech:000242, CommunityMech:000243, CommunityMech:000252,
    CommunityMech:000260, CommunityMech:000308, CommunityMech:000309, CommunityMech:000319,
    CommunityMech:000339.'
  target_ids:
  - cohort:EXTREME_ENVIRONMENT
  - CommunityMech:000222
  - CommunityMech:000339
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 85.27
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 15
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 75.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 15
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-isolates-biomining
  area: completeness
  topic: Cohort review of ISOLATES:BIOMINING (2 records)
  outcome: supported
  summary: Cohort ISOLATES:BIOMINING comprises 2 records (2 taxa, 9 ecological interactions,
    6 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 87.50/100 (min 86/100).
  details: 'Reviewed member records (2): CommunityMech:000320, CommunityMech:000322.'
  target_ids:
  - cohort:ISOLATES:BIOMINING
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 87.5
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 86.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-isolates-biotechnology
  area: completeness
  topic: Cohort review of ISOLATES:BIOTECHNOLOGY (2 records)
  outcome: concern
  summary: Cohort ISOLATES:BIOTECHNOLOGY comprises 2 records (2 taxa, 5 ecological
    interactions, 2 downstream causal edges, 0 UniProtKB gene annotations) with mean
    Completeness Score 83.50/100 (min 80/100).
  details: 'Reviewed member records (2): CommunityMech:000273, CommunityMech:000321.'
  target_ids:
  - cohort:ISOLATES:BIOTECHNOLOGY
  - CommunityMech:000273
  - CommunityMech:000321
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 83.5
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 80.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-lignocellulose
  area: completeness
  topic: Cohort review of LIGNOCELLULOSE (37 records)
  outcome: concern
  summary: Cohort LIGNOCELLULOSE comprises 37 records (127 taxa, 110 ecological interactions,
    54 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 88.03/100 (min 77/100).
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
  metrics:
  - name: mean_completeness_score
    value: 88.03
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 37
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 77.0
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
    10 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 86.00/100 (min 85/100).
  details: 'Reviewed member records (3): CommunityMech:000017, CommunityMech:000262,
    CommunityMech:000268.'
  target_ids:
  - cohort:METAL_REDUCTION
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 86.0
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 3
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 85.0
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
    22 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 88.88/100 (min 85/100).
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
  metrics:
  - name: mean_completeness_score
    value: 88.88
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 17
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 85.0
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
    downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 79.00/100 (min 77/100).
  details: 'Reviewed member records (5): CommunityMech:000081, CommunityMech:000082,
    CommunityMech:000083, CommunityMech:000084, CommunityMech:000085.'
  target_ids:
  - cohort:ORAL
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 79.0
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 5
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 77.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 5
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-other
  area: completeness
  topic: Cohort review of OTHER (44 records)
  outcome: concern
  summary: Cohort OTHER comprises 44 records (192 taxa, 129 ecological interactions,
    45 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 83.48/100 (min 55/100).
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
  - CommunityMech:000360
  - CommunityMech:000364
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 83.48
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
    3 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 77.50/100 (min 77/100).
  details: 'Reviewed member records (2): CommunityMech:000467, CommunityMech:000468.'
  target_ids:
  - cohort:PHAGE_PREDATION
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 77.5
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 2
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 77.0
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
    18 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 88.11/100 (min 80/100).
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
  metrics:
  - name: mean_completeness_score
    value: 88.11
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 19
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 80.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 19
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-rhizosphere
  area: completeness
  topic: Cohort review of RHIZOSPHERE (80 records)
  outcome: concern
  summary: Cohort RHIZOSPHERE comprises 80 records (406 taxa, 254 ecological interactions,
    86 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 82.58/100 (min 55/100).
  details: 'Reviewed member records (80): CommunityMech:000003, CommunityMech:000022,
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
    CommunityMech:000477, CommunityMech:000483.'
  target_ids:
  - cohort:RHIZOSPHERE
  - CommunityMech:000302
  - CommunityMech:000347
  - CommunityMech:000373
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  metrics:
  - name: mean_completeness_score
    value: 82.58
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 80
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 55.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 80
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-syntrophy
  area: completeness
  topic: Cohort review of SYNTROPHY (34 records)
  outcome: supported
  summary: Cohort SYNTROPHY comprises 34 records (83 taxa, 113 ecological interactions,
    66 downstream causal edges, 0 UniProtKB gene annotations) with mean Completeness
    Score 87.65/100 (min 72/100).
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
  metrics:
  - name: mean_completeness_score
    value: 87.65
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 34
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 72.0
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
    causal edges, 9 UniProtKB gene annotations) with mean Completeness Score 100.00/100
    (min 100/100).
  details: 'Reviewed member records (2): CommunityMech:taxon:000001, CommunityMech:taxon:000002.'
  target_ids:
  - cohort:TAXA
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
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
- finding_id: stage4-missing-community-origin-000434
  issue_key: communitymech-stage4-000434-missing-origin
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: CommunityMech:000434 omits community_origin despite acidic nitrification
    bioreactor operation in PMID:42762737
  description: 'Acidic_Nitrification_Minimal_Consortium.yaml (CommunityMech:000434)
    is the only MicrobialCommunity record in the 477-community corpus missing community_origin.
    The cited abstract (PMID:42762737) describes three acidic nitrification bioreactors
    operated between pH 2.0 and 5.0 where the pH 2.0 bioreactor hosts a simplified
    consortium dominated by "Candidatus Nitrosoglobus kelleri" and Mycobacterium species,
    supporting community_origin: ENGINEERED.'
  target_ids:
  - CommunityMech:000434
  field_paths:
  - community_origin
  evidence_ids:
  - ev-completeness-audit
  - ev-000434-pmid42762737
  rule_id: review-communities:completeness-core-metadata
  native_severity: P2
  normalization_reason: CommunityMech P2 (record-completeness metadata omission with
    direct primary-source resolution) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
    role: canonical_record
  tags:
  - completeness
  - metadata
  - stage5-remediation
- finding_id: stage4-missing-ecological-state-000360
  issue_key: communitymech-stage4-000360-missing-state
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: CommunityMech:000360 omits ecological_state despite persistent host-filtered
    endosphere guild maintenance in PMID:42304541
  description: 'Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml (CommunityMech:000360)
    is the only MicrobialCommunity record in the 477-community corpus missing ecological_state.
    The cited source (PMID:42304541) describes a persistent host-filtered endosphere
    cobamide-producing guild assembled and maintained in a stable host-mediated niche,
    supporting ecological_state: STABLE.'
  target_ids:
  - CommunityMech:000360
  field_paths:
  - ecological_state
  evidence_ids:
  - ev-completeness-audit
  - ev-000360-pmid42304541
  rule_id: review-communities:completeness-core-metadata
  native_severity: P2
  normalization_reason: CommunityMech P2 (record-completeness metadata omission with
    direct primary-source resolution) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
    role: canonical_record
  tags:
  - completeness
  - metadata
  - stage5-remediation
- finding_id: stage4-disconnected-syncom-participants
  issue_key: communitymech-stage4-disconnected-syncom-participants
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Five SynCom/consortium records omit co-tested member taxa from COMMUNITY_LEVEL
    participating_taxa
  description: 'NetworkIntegrityAuditor flags 14 DISCONNECTED_TAXON warnings across
    five records (CommunityMech:000339 Space_Habitat_SevenMember_Stress_Tolerance_SynCom
    [6 disconnected taxa: Sphingomonas paucimobilis, Cupriavidus metallidurans, Ralstonia
    pickettii, Acinetobacter radioresistens, Burkholderia cepacia, Chryseobacterium
    gleum], CommunityMech:000399 Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom
    [5 disconnected strains: H27, F2, F3, W6, M15], CommunityMech:000415 Algal_Methanotroph_Biogas_Valorization_Coculture
    [1 disconnected cyanobacterial primary producer: Leptolyngbya, NCBITaxon:47251],
    CommunityMech:000433 Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium [1 disconnected
    taxon: Legionella MAGs, NCBITaxon:445], and CommunityMech:000447 Brocadia_Low_Nitrogen_Anammox_Consortium
    [1 disconnected taxon: Candidatus Kuenenia early-acclimation lineage, NCBITaxon:174636])
    where COMMUNITY_LEVEL ecological_interactions list only a subset of participating_taxa.'
  target_ids:
  - CommunityMech:000339
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000447
  field_paths:
  - ecological_interactions[].participating_taxa
  evidence_ids:
  - ev-network-integrity-audit
  rule_id: review-communities:network-integrity-disconnected-taxon
  native_severity: P3
  normalization_reason: CommunityMech P3 (network-integrity participant list completeness
    on COMMUNITY_LEVEL nodes) maps to minor.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
    role: canonical_record
  tags:
  - graph
  - participating_taxa
  - stage5-remediation
- finding_id: stage4-external-host-pathogen-targets
  issue_key: communitymech-stage4-external-host-pathogen-targets
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Three biocontrol/rhizosphere SynCom records place external non-member hosts
    or pathogens in target_taxon
  description: 'NetworkIntegrityAuditor flags all 7 UNKNOWN_TARGET warnings in the
    corpus across three records (CommunityMech:000347 Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom
    [3 warnings: Fusarium oxysporum on 1 interaction and Pinus massoniana on 2 interactions],
    CommunityMech:000364 Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom [2 warnings:
    Sclerotinia sclerotiorum on 2 interactions], and CommunityMech:000373 Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom
    [2 warnings: Nicotiana tabacum (tobacco, NCBITaxon:4097) on 2 interactions]) because
    external host plants and target phytopathogens outside taxonomy[] are modeled
    in target_taxon on COMMUNITY_LEVEL interactions.'
  target_ids:
  - CommunityMech:000347
  - CommunityMech:000364
  - CommunityMech:000373
  field_paths:
  - ecological_interactions[].target_taxon
  - ecological_interactions[].participating_taxa
  evidence_ids:
  - ev-network-integrity-audit
  rule_id: review-communities:network-integrity-unknown-target
  native_severity: P3
  normalization_reason: CommunityMech P3 (host/pathogen boundary modeling in COMMUNITY_LEVEL
    interactions) maps to minor.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  tags:
  - scope
  - boundary
  - network-integrity
  - stage5-remediation
- finding_id: stage4-isolate-000273-unverified-ore-prose
  issue_key: communitymech-stage4-000273-unverified-ore-prose
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: CommunityMech:000273 retains unverified arsenopyrite ore recovery claims
    and un-evidenced environmental_factors
  description: 'Although Stage 2 repaired ecological_interactions on data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    (CommunityMech:000273), its top-level description, environment_term.notes, taxonomy[0].taxon_term.notes,
    and 8 un-evidenced environmental_factors entries (7 ore/cyanide/pulp-density parameters
    and 1 temperature entry) still assert refractory gold-bearing sulfide ore (arsenopyrite/pyrite)
    bioleaching, 70-85% gold recovery, 50-200 ppm CN-, and 7-14 day leaching time
    that do not come from the cited waste-PCB bioleaching source (doi:10.1007/s10163-014-0276-4:
    Acidithiobacillus ferrooxidans pretreatment removing >80% Cu followed by Chromobacterium
    violaceum bioleaching reaching 70.6% Au bioleaching efficiency vs 45.5% in direct
    bioleaching).'
  target_ids:
  - CommunityMech:000273
  field_paths:
  - description
  - environment_term.notes
  - taxonomy[0].taxon_term.notes
  - environmental_factors
  evidence_ids:
  - ev-isolate-000273-audit
  rule_id: review-yaml-record:evidence-claim-alignment
  native_severity: P2
  normalization_reason: CommunityMech P2 (unverified numeric/substrate prose not supported
    by cited primary source) maps to major.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    role: canonical_record
  tags:
  - evidence
  - isolates
  - stage5-remediation
- finding_id: stage4-isolate-000321-missing-functional-role
  issue_key: communitymech-stage4-000321-missing-role
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: CommunityMech:000321 omits functional_role and abundance_level on its sole
    taxon entry
  description: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml (CommunityMech:000321)
    is the only record in data/isolates/ missing functional_role and abundance_level
    on taxonomy[0] (Rothia, NCBITaxon:32207, supported by PMID:33398099 and PMID:28963201),
    reducing its proportional Completeness Score to 80/100.
  target_ids:
  - CommunityMech:000321
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[0].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-isolate-000321-audit
  rule_id: review-communities:completeness-functional-roles
  native_severity: P3
  normalization_reason: CommunityMech P3 (missing optional functional_role annotation
    on isolate taxon) maps to minor.
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  tags:
  - completeness
  - isolates
  - stage5-remediation
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
  - ev-prior-structured-reviews
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text assay detail gap preserved as minor.
  disposition_reason: 'Deferred: source-limited until full-text assay tables for PMID:25043025
    are ingested.'
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
  - ev-prior-structured-reviews
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
  - ev-prior-structured-reviews
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
  disposition_reason: 'Deferred: source-limited because primary full text is paywalled.'
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
  disposition_reason: 'Deferred: source-limited pending full-text interaction data.'
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
  tags:
  - carried-forward
  - source-limited
actions:
- action_id: act-set-community-origin-000434
  description: 'Set community_origin: ENGINEERED on CommunityMech:000434 (Acidic_Nitrification_Minimal_Consortium.yaml)
    and append a curation_history entry.'
  finding_ids:
  - stage4-missing-community-origin-000434
  target_ids:
  - CommunityMech:000434
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Acidic_Nitrification_Minimal_Consortium.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-set-ecological-state-000360
  description: 'Set ecological_state: STABLE on CommunityMech:000360 (Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml)
    and append a curation_history entry.'
  finding_ids:
  - stage4-missing-ecological-state-000360
  target_ids:
  - CommunityMech:000360
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Wolffia_Mankai_Endosphere_Cobamide_Guild.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-connect-syncom-participants
  description: Populate full abstract-backed participating_taxa on COMMUNITY_LEVEL
    ecological_interactions in CommunityMech:000339, 000399, 000415, 000433, and 000447.
  finding_ids:
  - stage4-disconnected-syncom-participants
  target_ids:
  - CommunityMech:000339
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000447
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Space_Habitat_SevenMember_Stress_Tolerance_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Pseudomonas_Aeruginosa_EightStrain_Full_Factorial_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Algal_Methanotroph_Biogas_Valorization_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Nitrifying_Wastewater_Ammonia_Oxidizing_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Brocadia_Low_Nitrogen_Anammox_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - just audit-network
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-remove-external-host-pathogen-targets
  description: Replace external non-member host/pathogen target_taxon entries on COMMUNITY_LEVEL
    interactions in CommunityMech:000347, 000364, and 000373 with member participating_taxa
    while preserving host/pathogen context in interaction name/description.
  finding_ids:
  - stage4-external-host-pathogen-targets
  target_ids:
  - CommunityMech:000347
  - CommunityMech:000364
  - CommunityMech:000373
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_siamensis_vallismortis_HT_Masson_Pine_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Bacillus_G12_Y4_X25_Tobacco_Biocontrol_SynCom.yaml
    role: canonical_record
  acceptance_checks:
  - just audit-network
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-reconcile-isolate-000273-prose
  description: Align description, environment_term.notes, taxonomy[0].taxon_term.notes,
    and environmental_factors in data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    (CommunityMech:000273) strictly to the cited waste-PCB bioleaching source (doi:10.1007/s10163-014-0276-4).
  finding_ids:
  - stage4-isolate-000273-unverified-ore-prose
  target_ids:
  - CommunityMech:000273
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity data/isolates/Chromobacterium_Gold_Biocyanidation.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-populate-isolate-000321-role
  description: Populate functional_role and abundance_level on taxonomy[0] in data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    (CommunityMech:000321) supported by PMID:33398099 and PMID:28963201.
  finding_ids:
  - stage4-isolate-000321-missing-functional-role
  target_ids:
  - CommunityMech:000321
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
  - uv run python scripts/verify_history_Changed_records.py
- action_id: act-defer-source-limited-fulltext-findings
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
  - CommunityMech:000273
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000321
  - CommunityMech:000339
  - CommunityMech:000347
  - CommunityMech:000360
  - CommunityMech:000364
  - CommunityMech:000373
  - CommunityMech:000399
  - CommunityMech:000415
  - CommunityMech:000433
  - CommunityMech:000434
  - CommunityMech:000447
  - cohort:AMD
  - cohort:BIOMINING
  - cohort:BIOREMEDIATION
  - cohort:BIOTECHNOLOGY
  - cohort:CARBON_SEQUESTRATION
  - cohort:DIET
  - cohort:EXTREME_ENVIRONMENT
  - cohort:ISOLATES:BIOMINING
  - cohort:ISOLATES:BIOTECHNOLOGY
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
  rationale: The full 479-record CommunityMech corpus spans 3 record roots (kb/communities/,
    data/isolates/, kb/taxa/) and 16 ecological categories, which is over-broad for
    a single unpartitioned cohort. Splitting by root and community_category yields
    19 disjoint, ecologically coherent cohorts for comparative rubric evaluation.
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
  - label: BIOREMEDIATION
    target_ids:
    - cohort:BIOREMEDIATION
  - label: BIOTECHNOLOGY
    target_ids:
    - cohort:BIOTECHNOLOGY
    - CommunityMech:000091
    - CommunityMech:000153
    - CommunityMech:000295
    - CommunityMech:000399
    - CommunityMech:000415
    - CommunityMech:000433
    - CommunityMech:000434
    - CommunityMech:000447
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
    - CommunityMech:000339
  - label: ISOLATES:BIOMINING
    target_ids:
    - cohort:ISOLATES:BIOMINING
  - label: ISOLATES:BIOTECHNOLOGY
    target_ids:
    - cohort:ISOLATES:BIOTECHNOLOGY
    - CommunityMech:000273
    - CommunityMech:000321
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
    - CommunityMech:000360
    - CommunityMech:000364
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
    - CommunityMech:000347
    - CommunityMech:000373
  - label: SYNTROPHY
    target_ids:
    - cohort:SYNTROPHY
  - label: TAXA
    target_ids:
    - cohort:TAXA
related_reviews:
- repository: CultureBotAI/CommunityMech
  review_id: 20261021T101000Z-stage4-record-deep-audit
  relationship: companion_per_record_deep_audit
limitations:
- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- 54 records in reports/causal_graph_review/inventory.tsv remain source-limited (needs_research)
  because cached abstracts do not provide multi-step causal chains or full-text assay
  tables.
tags:
- stage4
- cohort-review
- full-corpus
```
