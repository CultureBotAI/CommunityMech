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

## Structured Review Bundles And Machine-Readable Artifacts

- Full-corpus cohort review bundle: `reviews/structured/20261021T101100Z-stage4-frozen-cohort-review/review.yaml`
- Per-record deep audit bundle: `reviews/structured/20261021T101000Z-stage4-record-deep-audit/review.yaml`
- Workflow findings manifest: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/review_findings.yaml`
- Frozen 479-record inventory metrics and SHA-256 digests: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/frozen_inventory_metrics.tsv`
