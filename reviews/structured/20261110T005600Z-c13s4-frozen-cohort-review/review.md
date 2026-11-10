# Cycle 13 Stage 4 Full-Corpus Frozen Inventory and Cohort Review (537 Records Across 23 Cohorts)

- Review: 20261110T005600Z-c13s4-frozen-cohort-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-10T00:50:00Z
- Finished UTC: 2026-11-10T00:56:00Z
- Reviewer: antigravity-c13s4-cohort-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full-corpus frozen inventory and cohort review of all 537 eligible CommunityMech records (512 kb/communities/*.yaml, 23 data/isolates/*.yaml, 2 kb/taxa/*.yaml) partitioned into 23 disjoint domain cohorts at commit acd658dac45d0d64d5903cd8289e72925b8ffa13. All 537 records pass LinkML schema validation, ontology ID-label verification, and verbatim snippet checks; mean Completeness Score across 535 MicrobialCommunity records is 91.32/100 (median 94/100), with 100% top-level environment_term coverage (535/535) and 100% reusable CommonTaxon linkage (22/22 matching Shewanella oneidensis and Geobacter sulfurreducens occurrences across 21 MicrobialCommunity records: 20 kb/communities/*.yaml records and 1 data/isolates/*.yaml record, linked to 5 reusable EET genes / 42 EvidenceItems on CommunityMech:taxon:000001 and 4 reusable EET genes / 33 EvidenceItems on CommunityMech:taxon:000002). Two actionable open P2 findings across 2 records (CommunityMech:000424 and 000438), 3 carried-forward FunctionalRoleEnum vocabulary-blocked deferred findings across 3 records (CommunityMech:000374, 000533, 000534 under #2194), and 7 carried-forward source-limited deferred findings are preserved for Cycle 13 Stage 5 grouped remediation.

## Scope And Provenance

Exhaustive cohort review of all 23 domain/root cohorts (encompassing all 537 eligible records across kb/communities/*.yaml, data/isolates/*.yaml, and kb/taxa/*.yaml) plus all 12 finding-bearing records.

Selection: All 23 domain/root cohorts (537 records total; full per-record SHA-256 inventory in frozen_inventory_metrics.tsv) and all 12 finding-bearing records at Git commit acd658dac45d0d64d5903cd8289e72925b8ffa13.
Coverage: full; 35 reviewed / 35 in the declared population.
Source: git_commit at Git base acd658dac45d0d64d5903cd8289e72925b8ffa13.
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
| CommunityMech:000424 | kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml | maintained | CommunityMech:000424 (QY2-S1 Dehalogenimonas-Rich Brominated-Flame-Retardant Consortium) |
| CommunityMech:000438 | kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml | maintained | CommunityMech:000438 (Wine Yeast Three-Species Contact Consortium) |
| CommunityMech:000533 | data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml | maintained | CommunityMech:000533 (Achromobacter sp. SL8 Cadmium Immobilization Isolate Baseline) |
| CommunityMech:000534 | data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml | maintained | CommunityMech:000534 (Enterobacter sp. SL12 Cadmium Immobilization Isolate Baseline) |
| cohort:AMD | kb/communities/AMD_Acidophile_Heterotroph_Network.yaml # cohort=AMD;records=7 | snapshot_row | AMD cohort (7 records) |
| cohort:BIOMINING | kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml # cohort=BIOMINING;records=23 | snapshot_row | BIOMINING cohort (23 records) |
| cohort:BIOREMEDIATION | kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml # cohort=BIOREMEDIATION;records=93 | snapshot_row | BIOREMEDIATION cohort (93 records) |
| cohort:BIOTECHNOLOGY | kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml # cohort=BIOTECHNOLOGY;records=99 | snapshot_row | BIOTECHNOLOGY cohort (99 records) |
| cohort:CARBON_SEQUESTRATION | kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml # cohort=CARBON_SEQUESTRATION;records=12 | snapshot_row | CARBON_SEQUESTRATION cohort (12 records) |
| cohort:DIET | kb/communities/Bacteroides_Desulfovibrio_Carrageenan_H2S_Coculture.yaml # cohort=DIET;records=11 | snapshot_row | DIET cohort (11 records) |
| cohort:EXTREME_ENVIRONMENT | kb/communities/Angelarchaeales_Thermoplasmata_CuMMO_Soil_Sediment_Community.yaml # cohort=EXTREME_ENVIRONMENT;records=16 | snapshot_row | EXTREME_ENVIRONMENT cohort (16 records) |
| cohort:ISOLATES:BIOMINING | data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml # cohort=ISOLATES:BIOMINING;records=8 | snapshot_row | ISOLATES:BIOMINING cohort (8 records) |
| cohort:ISOLATES:BIOREMEDIATION | data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml # cohort=ISOLATES:BIOREMEDIATION;records=9 | snapshot_row | ISOLATES:BIOREMEDIATION cohort (9 records) |
| cohort:ISOLATES:BIOTECHNOLOGY | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml # cohort=ISOLATES:BIOTECHNOLOGY;records=2 | snapshot_row | ISOLATES:BIOTECHNOLOGY cohort (2 records) |
| cohort:ISOLATES:EXTREME_ENVIRONMENT | data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml # cohort=ISOLATES:EXTREME_ENVIRONMENT;records=1 | snapshot_row | ISOLATES:EXTREME_ENVIRONMENT cohort (1 records) |
| cohort:ISOLATES:RHIZOSPHERE | data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml # cohort=ISOLATES:RHIZOSPHERE;records=1 | snapshot_row | ISOLATES:RHIZOSPHERE cohort (1 records) |
| cohort:ISOLATES:SYNTROPHY | data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml # cohort=ISOLATES:SYNTROPHY;records=2 | snapshot_row | ISOLATES:SYNTROPHY cohort (2 records) |
| cohort:LIGNOCELLULOSE | kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml # cohort=LIGNOCELLULOSE;records=37 | snapshot_row | LIGNOCELLULOSE cohort (37 records) |
| cohort:METAL_REDUCTION | kb/communities/Alaska_Tundra_Permafrost_Iron_Redox_Community.yaml # cohort=METAL_REDUCTION;records=3 | snapshot_row | METAL_REDUCTION cohort (3 records) |
| cohort:METHANOGENESIS | kb/communities/Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml # cohort=METHANOGENESIS;records=17 | snapshot_row | METHANOGENESIS cohort (17 records) |
| cohort:ORAL | kb/communities/Defined_Multispecies_Enamel_Caries_Model.yaml # cohort=ORAL;records=5 | snapshot_row | ORAL cohort (5 records) |
| cohort:OTHER | kb/communities/Altered_Schaedler_Flora_Gnotobiotic_Mouse_Community.yaml # cohort=OTHER;records=45 | snapshot_row | OTHER cohort (45 records) |
| cohort:PHAGE_PREDATION | kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml # cohort=PHAGE_PREDATION;records=2 | snapshot_row | PHAGE_PREDATION cohort (2 records) |
| cohort:PHYTOPLANKTON | kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml # cohort=PHYTOPLANKTON;records=19 | snapshot_row | PHYTOPLANKTON cohort (19 records) |
| cohort:RHIZOSPHERE | kb/communities/Alfalfa_Stress_Adapted_Bacterial_SynCom.yaml # cohort=RHIZOSPHERE;records=85 | snapshot_row | RHIZOSPHERE cohort (85 records) |
| cohort:SYNTROPHY | kb/communities/ANME_SRB_Anaerobic_Methanotrophic_Syntrophic_Consortia.yaml # cohort=SYNTROPHY;records=38 | snapshot_row | SYNTROPHY cohort (38 records) |
| cohort:TAXA | kb/taxa/Geobacter_sulfurreducens.yaml # cohort=TAXA;records=2 | snapshot_row | TAXA cohort (2 records) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation across all 537 records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000424, CommunityMech:000438, CommunityMech:000533, CommunityMech:000534, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:ISOLATES:RHIZOSPHERE, cohort:ISOLATES:SYNTROPHY, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | All 535 MicrobialCommunity records and 2 CommonTaxon files pass LinkML schema validation with 0 errors and 100% EvidenceItem.evidence_source enum compliance. |
| NetworkIntegrityAuditor check across kb/communities/ and data/isolates/ | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000424, CommunityMech:000438, CommunityMech:000533, CommunityMech:000534, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:ISOLATES:RHIZOSPHERE, cohort:ISOLATES:SYNTROPHY, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | 495/512 community records and 23/23 isolate records have 0 network warnings; 17 community records have 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| review-communities Completeness Score rubric across all 537 records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000424, CommunityMech:000438, CommunityMech:000533, CommunityMech:000534, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:ISOLATES:RHIZOSPHERE, cohort:ISOLATES:SYNTROPHY, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | Computed proportional 100-point review-communities Completeness Score (min 50, median 94, mean 91.32, max 100 across 535 MicrobialCommunity records; 100/100 across 2 CommonTaxon files; 000424=95/100 [s_ab=0/5], 000438=83/100 [s_ab=0/5], 000374=90/100 [s_fr=0/10], 000533=85/100 [s_fr=0/10, external_resources=0/5], 000534=85/100 [s_fr=0/10, external_resources=0/5]; scripts/audit_completeness.py scores 90, 85, 40, 25, and 25) and verified causal graph and reusable taxon coverage across all 23 cohorts. |

## Scientific And Domain Assessments

### Cohort review of AMD (7 records)

completeness: supported. Targets: cohort:AMD.

Cohort AMD comprises 7 records (34 taxa, 29 ecological interactions, 8 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 94.00/100 (min 91/100).

Reviewed member records (7): CommunityMech:000001, CommunityMech:000002, CommunityMech:000027, CommunityMech:000034, CommunityMech:000059, CommunityMech:000074, CommunityMech:000353.

### Cohort review of BIOMINING (23 records)

completeness: supported. Targets: cohort:BIOMINING.

Cohort BIOMINING comprises 23 records (66 taxa, 70 ecological interactions, 32 downstream causal edges, 0 inline UniProtKB gene annotations, 7 reusable CommonTaxon links) with mean Completeness Score 93.61/100 (min 75/100).

Reviewed member records (23): CommunityMech:000005, CommunityMech:000019, CommunityMech:000026, CommunityMech:000035, CommunityMech:000045, CommunityMech:000049, CommunityMech:000057, CommunityMech:000073, CommunityMech:000217, CommunityMech:000303, CommunityMech:000305, CommunityMech:000385, CommunityMech:000404, CommunityMech:000485, CommunityMech:000486, CommunityMech:000487, CommunityMech:000491, CommunityMech:000519, CommunityMech:000520, CommunityMech:000523, CommunityMech:000526, CommunityMech:000527, CommunityMech:000528.

### Cohort review of BIOREMEDIATION (93 records)

completeness: concern. Targets: cohort:BIOREMEDIATION, CommunityMech:000374, CommunityMech:000424.

Cohort BIOREMEDIATION comprises 93 records (329 taxa, 230 ecological interactions, 89 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon links) with mean Completeness Score 91.95/100 (min 60/100).

Reviewed member records (93): CommunityMech:000004, CommunityMech:000024, CommunityMech:000030, CommunityMech:000038, CommunityMech:000042, CommunityMech:000044, CommunityMech:000051, CommunityMech:000060, CommunityMech:000111, CommunityMech:000112, CommunityMech:000113, CommunityMech:000114, CommunityMech:000115, CommunityMech:000116, CommunityMech:000121, CommunityMech:000132, CommunityMech:000136, CommunityMech:000138, CommunityMech:000163, CommunityMech:000166, CommunityMech:000176, CommunityMech:000181, CommunityMech:000183, CommunityMech:000184, CommunityMech:000199, CommunityMech:000200, CommunityMech:000209, CommunityMech:000238, CommunityMech:000239, CommunityMech:000271, CommunityMech:000285, CommunityMech:000289, CommunityMech:000291, CommunityMech:000292, CommunityMech:000299, CommunityMech:000300, CommunityMech:000301, CommunityMech:000324, CommunityMech:000328, CommunityMech:000331, CommunityMech:000334, CommunityMech:000335, CommunityMech:000340, CommunityMech:000342, CommunityMech:000344, CommunityMech:000352, CommunityMech:000358, CommunityMech:000361, CommunityMech:000362, CommunityMech:000369, CommunityMech:000370, CommunityMech:000371, CommunityMech:000374, CommunityMech:000379, CommunityMech:000384, CommunityMech:000386, CommunityMech:000387, CommunityMech:000388, CommunityMech:000405, CommunityMech:000406, CommunityMech:000410, CommunityMech:000411, CommunityMech:000413, CommunityMech:000420, CommunityMech:000424, CommunityMech:000426, CommunityMech:000437, CommunityMech:000439, CommunityMech:000440, CommunityMech:000442, CommunityMech:000444, CommunityMech:000454, CommunityMech:000461, CommunityMech:000462, CommunityMech:000463, CommunityMech:000470, CommunityMech:000471, CommunityMech:000476, CommunityMech:000479, CommunityMech:000482, CommunityMech:000484, CommunityMech:000493, CommunityMech:000498, CommunityMech:000499, CommunityMech:000500, CommunityMech:000502, CommunityMech:000503, CommunityMech:000504, CommunityMech:000505, CommunityMech:000506, CommunityMech:000507, CommunityMech:000508, CommunityMech:000509.

### Cohort review of BIOTECHNOLOGY (99 records)

completeness: concern. Targets: cohort:BIOTECHNOLOGY, CommunityMech:000091, CommunityMech:000153, CommunityMech:000295, CommunityMech:000438.

Cohort BIOTECHNOLOGY comprises 99 records (312 taxa, 264 ecological interactions, 96 downstream causal edges, 0 inline UniProtKB gene annotations, 8 reusable CommonTaxon links) with mean Completeness Score 89.91/100 (min 50/100).

Reviewed member records (99): CommunityMech:000009, CommunityMech:000029, CommunityMech:000036, CommunityMech:000091, CommunityMech:000092, CommunityMech:000117, CommunityMech:000126, CommunityMech:000139, CommunityMech:000146, CommunityMech:000149, CommunityMech:000151, CommunityMech:000152, CommunityMech:000153, CommunityMech:000154, CommunityMech:000164, CommunityMech:000165, CommunityMech:000167, CommunityMech:000170, CommunityMech:000171, CommunityMech:000172, CommunityMech:000173, CommunityMech:000175, CommunityMech:000177, CommunityMech:000185, CommunityMech:000198, CommunityMech:000202, CommunityMech:000203, CommunityMech:000204, CommunityMech:000207, CommunityMech:000210, CommunityMech:000211, CommunityMech:000213, CommunityMech:000214, CommunityMech:000241, CommunityMech:000244, CommunityMech:000266, CommunityMech:000269, CommunityMech:000278, CommunityMech:000279, CommunityMech:000283, CommunityMech:000284, CommunityMech:000287, CommunityMech:000294, CommunityMech:000295, CommunityMech:000306, CommunityMech:000326, CommunityMech:000329, CommunityMech:000330, CommunityMech:000332, CommunityMech:000333, CommunityMech:000343, CommunityMech:000345, CommunityMech:000354, CommunityMech:000355, CommunityMech:000356, CommunityMech:000357, CommunityMech:000359, CommunityMech:000363, CommunityMech:000365, CommunityMech:000366, CommunityMech:000372, CommunityMech:000378, CommunityMech:000390, CommunityMech:000395, CommunityMech:000397, CommunityMech:000399, CommunityMech:000400, CommunityMech:000402, CommunityMech:000408, CommunityMech:000412, CommunityMech:000415, CommunityMech:000417, CommunityMech:000418, CommunityMech:000422, CommunityMech:000425, CommunityMech:000430, CommunityMech:000431, CommunityMech:000433, CommunityMech:000434, CommunityMech:000435, CommunityMech:000436, CommunityMech:000438, CommunityMech:000445, CommunityMech:000447, CommunityMech:000448, CommunityMech:000449, CommunityMech:000450, CommunityMech:000453, CommunityMech:000455, CommunityMech:000457, CommunityMech:000465, CommunityMech:000478, CommunityMech:000480, CommunityMech:000481, CommunityMech:000496, CommunityMech:000497, CommunityMech:000517, CommunityMech:000522, CommunityMech:000535.

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

### Cohort review of ISOLATES:BIOMINING (8 records)

completeness: supported. Targets: cohort:ISOLATES:BIOMINING.

Cohort ISOLATES:BIOMINING comprises 8 records (8 taxa, 21 ecological interactions, 9 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon links) with mean Completeness Score 94.38/100 (min 91/100).

Reviewed member records (8): CommunityMech:000320, CommunityMech:000322, CommunityMech:000489, CommunityMech:000490, CommunityMech:000524, CommunityMech:000525, CommunityMech:000529, CommunityMech:000530.

### Cohort review of ISOLATES:BIOREMEDIATION (9 records)

completeness: concern. Targets: cohort:ISOLATES:BIOREMEDIATION, CommunityMech:000533, CommunityMech:000534.

Cohort ISOLATES:BIOREMEDIATION comprises 9 records (9 taxa, 12 ecological interactions, 3 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 92.78/100 (min 85/100).

Reviewed member records (9): CommunityMech:000488, CommunityMech:000492, CommunityMech:000531, CommunityMech:000532, CommunityMech:000533, CommunityMech:000534, CommunityMech:000536, CommunityMech:000537, CommunityMech:000538.

### Cohort review of ISOLATES:BIOTECHNOLOGY (2 records)

completeness: supported. Targets: cohort:ISOLATES:BIOTECHNOLOGY.

Cohort ISOLATES:BIOTECHNOLOGY comprises 2 records (2 taxa, 5 ecological interactions, 2 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 93.00/100 (min 91/100).

Reviewed member records (2): CommunityMech:000273, CommunityMech:000321.

### Cohort review of ISOLATES:EXTREME_ENVIRONMENT (1 records)

completeness: supported. Targets: cohort:ISOLATES:EXTREME_ENVIRONMENT.

Cohort ISOLATES:EXTREME_ENVIRONMENT comprises 1 records (1 taxa, 3 ecological interactions, 2 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 92.00/100 (min 92/100).

Reviewed member records (1): CommunityMech:000495.

### Cohort review of ISOLATES:RHIZOSPHERE (1 records)

completeness: supported. Targets: cohort:ISOLATES:RHIZOSPHERE.

Cohort ISOLATES:RHIZOSPHERE comprises 1 records (1 taxa, 3 ecological interactions, 0 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 94.00/100 (min 94/100).

Reviewed member records (1): CommunityMech:000521.

### Cohort review of ISOLATES:SYNTROPHY (2 records)

completeness: supported. Targets: cohort:ISOLATES:SYNTROPHY.

Cohort ISOLATES:SYNTROPHY comprises 2 records (2 taxa, 2 ecological interactions, 0 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 95.00/100 (min 95/100).

Reviewed member records (2): CommunityMech:000539, CommunityMech:000540.

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

### Cohort review of OTHER (45 records)

completeness: supported. Targets: cohort:OTHER.

Cohort OTHER comprises 45 records (198 taxa, 131 ecological interactions, 45 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 87.80/100 (min 55/100).

Reviewed member records (45): CommunityMech:000010, CommunityMech:000011, CommunityMech:000012, CommunityMech:000013, CommunityMech:000037, CommunityMech:000055, CommunityMech:000065, CommunityMech:000066, CommunityMech:000067, CommunityMech:000080, CommunityMech:000086, CommunityMech:000093, CommunityMech:000122, CommunityMech:000123, CommunityMech:000124, CommunityMech:000125, CommunityMech:000127, CommunityMech:000128, CommunityMech:000133, CommunityMech:000144, CommunityMech:000145, CommunityMech:000159, CommunityMech:000160, CommunityMech:000161, CommunityMech:000220, CommunityMech:000223, CommunityMech:000240, CommunityMech:000248, CommunityMech:000249, CommunityMech:000253, CommunityMech:000293, CommunityMech:000315, CommunityMech:000318, CommunityMech:000346, CommunityMech:000351, CommunityMech:000360, CommunityMech:000364, CommunityMech:000377, CommunityMech:000382, CommunityMech:000392, CommunityMech:000396, CommunityMech:000423, CommunityMech:000432, CommunityMech:000443, CommunityMech:000515.

### Cohort review of PHAGE_PREDATION (2 records)

completeness: supported. Targets: cohort:PHAGE_PREDATION.

Cohort PHAGE_PREDATION comprises 2 records (11 taxa, 10 ecological interactions, 3 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 83.00/100 (min 83/100).

Reviewed member records (2): CommunityMech:000467, CommunityMech:000468.

### Cohort review of PHYTOPLANKTON (19 records)

completeness: supported. Targets: cohort:PHYTOPLANKTON.

Cohort PHYTOPLANKTON comprises 19 records (60 taxa, 59 ecological interactions, 18 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 95.00/100 (min 84/100).

Reviewed member records (19): CommunityMech:000014, CommunityMech:000015, CommunityMech:000016, CommunityMech:000020, CommunityMech:000056, CommunityMech:000130, CommunityMech:000131, CommunityMech:000143, CommunityMech:000147, CommunityMech:000155, CommunityMech:000162, CommunityMech:000191, CommunityMech:000259, CommunityMech:000325, CommunityMech:000381, CommunityMech:000441, CommunityMech:000446, CommunityMech:000451, CommunityMech:000452.

### Cohort review of RHIZOSPHERE (85 records)

completeness: concern. Targets: cohort:RHIZOSPHERE, CommunityMech:000302.

Cohort RHIZOSPHERE comprises 85 records (454 taxa, 269 ecological interactions, 86 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 87.15/100 (min 55/100).

Reviewed member records (85): CommunityMech:000003, CommunityMech:000022, CommunityMech:000025, CommunityMech:000028, CommunityMech:000039, CommunityMech:000040, CommunityMech:000043, CommunityMech:000047, CommunityMech:000050, CommunityMech:000058, CommunityMech:000063, CommunityMech:000064, CommunityMech:000072, CommunityMech:000076, CommunityMech:000077, CommunityMech:000078, CommunityMech:000079, CommunityMech:000087, CommunityMech:000088, CommunityMech:000090, CommunityMech:000094, CommunityMech:000095, CommunityMech:000096, CommunityMech:000097, CommunityMech:000098, CommunityMech:000099, CommunityMech:000100, CommunityMech:000101, CommunityMech:000102, CommunityMech:000103, CommunityMech:000104, CommunityMech:000105, CommunityMech:000106, CommunityMech:000107, CommunityMech:000108, CommunityMech:000109, CommunityMech:000110, CommunityMech:000129, CommunityMech:000216, CommunityMech:000221, CommunityMech:000225, CommunityMech:000235, CommunityMech:000236, CommunityMech:000245, CommunityMech:000247, CommunityMech:000250, CommunityMech:000272, CommunityMech:000280, CommunityMech:000302, CommunityMech:000304, CommunityMech:000310, CommunityMech:000311, CommunityMech:000312, CommunityMech:000313, CommunityMech:000314, CommunityMech:000316, CommunityMech:000341, CommunityMech:000347, CommunityMech:000348, CommunityMech:000367, CommunityMech:000368, CommunityMech:000373, CommunityMech:000375, CommunityMech:000376, CommunityMech:000391, CommunityMech:000393, CommunityMech:000403, CommunityMech:000409, CommunityMech:000414, CommunityMech:000419, CommunityMech:000427, CommunityMech:000428, CommunityMech:000429, CommunityMech:000456, CommunityMech:000458, CommunityMech:000459, CommunityMech:000460, CommunityMech:000472, CommunityMech:000477, CommunityMech:000483, CommunityMech:000501, CommunityMech:000513, CommunityMech:000514, CommunityMech:000516, CommunityMech:000518.

### Cohort review of SYNTROPHY (38 records)

completeness: supported. Targets: cohort:SYNTROPHY.

Cohort SYNTROPHY comprises 38 records (93 taxa, 119 ecological interactions, 68 downstream causal edges, 0 inline UniProtKB gene annotations, 2 reusable CommonTaxon links) with mean Completeness Score 96.24/100 (min 84/100).

Reviewed member records (38): CommunityMech:000006, CommunityMech:000007, CommunityMech:000008, CommunityMech:000018, CommunityMech:000023, CommunityMech:000031, CommunityMech:000052, CommunityMech:000053, CommunityMech:000068, CommunityMech:000069, CommunityMech:000070, CommunityMech:000071, CommunityMech:000134, CommunityMech:000141, CommunityMech:000142, CommunityMech:000148, CommunityMech:000150, CommunityMech:000157, CommunityMech:000158, CommunityMech:000186, CommunityMech:000187, CommunityMech:000188, CommunityMech:000189, CommunityMech:000190, CommunityMech:000276, CommunityMech:000288, CommunityMech:000290, CommunityMech:000307, CommunityMech:000327, CommunityMech:000336, CommunityMech:000337, CommunityMech:000350, CommunityMech:000469, CommunityMech:000475, CommunityMech:000510, CommunityMech:000511, CommunityMech:000512, CommunityMech:000541.

### Cohort review of TAXA (2 records)

completeness: supported. Targets: cohort:TAXA.

Cohort TAXA comprises 2 records (2 taxa, 0 ecological interactions, 0 downstream causal edges, 9 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 100.00/100 (min 100/100).

Reviewed member records (2): CommunityMech:taxon:000001, CommunityMech:taxon:000002.

## Findings

### c13s4-000424-qy2s1-bfr-consortium-abundance-levels: All four reductive-dehalogenation consortium members in QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium (CommunityMech:000424) populate free-text abundance_value but omit controlled abundance_level despite explicit phylum and genus dominance in PMID:42511722

major / open / confirmed; issue key: c13s4-000424-qy2s1-bfr-consortium-abundance-levels.

In kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml (CommunityMech:000424), Dehalogenimonas (taxonomy[0], NCBITaxon:670486, functional_role: [PRIMARY_DEGRADER, SYNTROPHIC_PARTNER]), Clostridium (taxonomy[1], NCBITaxon:1485, functional_role: [SECONDARY_FERMENTER, SYNTROPHIC_PARTNER]), Sedimentibacter (taxonomy[2], NCBITaxon:190972, functional_role: [SECONDARY_FERMENTER, SYNTROPHIC_PARTNER]), and Methanoculleus (taxonomy[3], NCBITaxon:45989, functional_role: [SYNTROPHIC_PARTNER, ELECTRON_ACCEPTOR]) all populate free-text abundance_value strings but omit the controlled abundance_level enum. The cited open-access study (PMID:42511722, doi:10.3390/ijms27146379) explicitly establishes that 'More detailed analysis revealed a consistent microbial community composition among different systems, predominantly composed of the phyla Bacillota (formerly Firmicutes; 43.84 ± 3.76%~54.15 ± 7.28%), Chloroflexota (19.70 ± 4.90%~29.33 ± 5.27%), and Halobacteriota (11.72 ± 4.57%~27.33 ± 9.08%). At the genus level, these phyla were mainly represented by Clostridium and Sedimentibacter (class Clostridia) as the dominant fermenters, along with Dehalogenimonas (class Dehalococcoidia) as the key functional OHRB, and Methanoculleus (class Methanomicrobia) as the primary methanogens.' Setting abundance_level: DOMINANT on taxonomy[0..3] raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/4 -&gt; 4/4 taxa with abundance_level; proportional Completeness Score 95/100 -&gt; 100/100; scripts/audit_completeness.py score 90/100).

### c13s4-000438-wine-yeast-contact-consortium-abundance-levels: All three defined wine-yeast consortium members in Wine_Yeast_ThreeSpecies_Contact_Consortium (CommunityMech:000438) omit abundance_level despite explicit equimolar inoculation and 12-h population measurements in PMID:42176030

major / open / confirmed; issue key: c13s4-000438-wine-yeast-contact-consortium-abundance-levels.

In kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml (CommunityMech:000438), Saccharomyces cerevisiae VIN13 (taxonomy[0], NCBITaxon:4932, functional_role: [SECONDARY_FERMENTER]), Lachancea thermotolerans IWBT Y1240 (taxonomy[1], NCBITaxon:381046, functional_role: [SECONDARY_FERMENTER]), and Torulaspora delbrueckii LO544 (taxonomy[2], NCBITaxon:4950, functional_role: [SECONDARY_FERMENTER]) all omit abundance_level. The cited open-access study (PMID:42176030, doi:10.1007/s00253-026-13856-4) explicitly establishes that each species was inoculated at ca. 5 × 10^6 cells/mL (total 1.6 × 10^7 cells/mL) and that in direct physical contact at 12 h 'S. cerevisiae reached maximum cell numbers of 3.7 × 107 cells/mL, while both non-Saccharomyces species reached ca. 2.5 × 107 cells/mL (Fig. 3 b)', establishing sole numerical dominance of S. cerevisiae in the direct-contact consortium (whereas in indirect contact, T. delbrueckii showed rapid growth and early numerical dominance before T. delbrueckii and S. cerevisiae both reached ca. 3 × 10^7 cells/mL compared to ca. 1 × 10^7 cells/mL for L. thermotolerans). Setting abundance_level: DOMINANT on taxonomy[0] (anchored to the direct physical contact consortium where S. cerevisiae is the sole numerical majority at 3.7 × 10^7 cells/mL, p &lt; 0.05) and abundance_level: COMMON (or DOMINANT) on taxonomy[1] and taxonomy[2] raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/3 -&gt; 3/3 taxa with abundance_level; proportional Completeness Score 83/100 -&gt; 88/100; scripts/audit_completeness.py score 85/100).

### c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles: Both cadmium-immobilizing coculture members in Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture (CommunityMech:000374) omit functional_role despite direct Cd-detoxification support in PMID:42307251

minor / deferred / confirmed; issue key: c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles.

In kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml (CommunityMech:000374), both Achromobacter sp. SL8 (taxonomy[0], NCBITaxon:222, abundance_level: DOMINANT) and Enterobacter sp. SL12 (taxonomy[1], NCBITaxon:547, abundance_level: DOMINANT) omit functional_role, despite direct Cd-detoxification and Cd-immobilization support in the cited open-access study (PMID:42307251, doi:10.1128/spectrum.01081-26: 'After a 7-day incubation period, RE-Cd values reached 82.6% and 69.55% for SL8, 63.4% and 70.8% for SL12, and 82.6% and 80.9% for the co-cultured strains at initial Cd concentrations of 50 mg/L and 100 mg/L, respectively.'). Setting functional_role: [PRIMARY_DEGRADER] on both taxonomy[0] and taxonomy[1] raises the review-communities s_fr functional_role rubric component from 0/10 to 10/10 (Completeness Score 90/100 -&gt; 100/100) and raises scripts/audit_completeness.py:calculate_completeness() from 40/100 to 90/100.

Disposition: Deferred under existing open GitHub issue #2194 (and schema policy #301): FunctionalRoleEnum.PRIMARY_DEGRADER is defined in src/communitymech/schema/communitymech.yaml as 'Degrades complex substrates' and must not be forced onto inorganic Cd2+ immobilization via CdS bioprecipitation, intracellular Cd accumulation, and N-H / amide C=O surface coordination (PMID:42307251). Preserved as an explicit vocabulary gap until FunctionalRoleEnum adds a heavy-metal-immobilizer / metal-detoxifier value.

### c12s4-000533-achromobacter-sl8-isolate-functional-role: Achromobacter sp. SL8 monoculture isolate baseline Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline (CommunityMech:000533) omits functional_role on taxonomy[0] despite direct Cd-immobilization support in PMID:42307251

minor / deferred / confirmed; issue key: c12s4-000533-achromobacter-sl8-isolate-functional-role.

In data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml (CommunityMech:000533), Achromobacter sp. SL8 (taxonomy[0], NCBITaxon:222, abundance_level: DOMINANT) omits functional_role despite direct monoculture cadmium-detoxification and Cd-immobilization support in PMID:42307251 (doi:10.1128/spectrum.01081-26: 'After a 7-day incubation period, RE-Cd values reached 82.6% and 69.55% for SL8, 63.4% and 70.8% for SL12, and 82.6% and 80.9% for the co-cultured strains at initial Cd concentrations of 50 mg/L and 100 mg/L, respectively.'). Setting functional_role: [PRIMARY_DEGRADER] on taxonomy[0] raises the review-communities s_fr functional_role rubric component from 0/10 to 10/10 (Completeness Score 85/100 -&gt; 95/100) and raises scripts/audit_completeness.py:calculate_completeness() from 25/100 to 75/100.

Disposition: Deferred under existing open GitHub issue #2194 (and schema policy #301): FunctionalRoleEnum.PRIMARY_DEGRADER is defined in src/communitymech/schema/communitymech.yaml as 'Degrades complex substrates' and must not be forced onto inorganic Cd2+ immobilization via CdS bioprecipitation, intracellular Cd accumulation, and N-H / amide C=O surface coordination (PMID:42307251). Preserved as an explicit vocabulary gap until FunctionalRoleEnum adds a heavy-metal-immobilizer / metal-detoxifier value.

### c12s4-000534-enterobacter-sl12-isolate-functional-role: Enterobacter sp. SL12 monoculture isolate baseline Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline (CommunityMech:000534) omits functional_role on taxonomy[0] despite direct Cd-immobilization support in PMID:42307251

minor / deferred / confirmed; issue key: c12s4-000534-enterobacter-sl12-isolate-functional-role.

In data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml (CommunityMech:000534), Enterobacter sp. SL12 (taxonomy[0], NCBITaxon:547, abundance_level: DOMINANT) omits functional_role despite direct monoculture cadmium-detoxification and Cd-immobilization support in PMID:42307251 (doi:10.1128/spectrum.01081-26: 'After a 7-day incubation period, RE-Cd values reached 82.6% and 69.55% for SL8, 63.4% and 70.8% for SL12, and 82.6% and 80.9% for the co-cultured strains at initial Cd concentrations of 50 mg/L and 100 mg/L, respectively.'). Setting functional_role: [PRIMARY_DEGRADER] on taxonomy[0] raises the review-communities s_fr functional_role rubric component from 0/10 to 10/10 (Completeness Score 85/100 -&gt; 95/100) and raises scripts/audit_completeness.py:calculate_completeness() from 25/100 to 75/100.

Disposition: Deferred under existing open GitHub issue #2194 (and schema policy #301): FunctionalRoleEnum.PRIMARY_DEGRADER is defined in src/communitymech/schema/communitymech.yaml as 'Degrades complex substrates' and must not be forced onto inorganic Cd2+ immobilization via CdS bioprecipitation, intracellular Cd accumulation, and N-H / amide C=O surface coordination (PMID:42307251). Preserved as an explicit vocabulary gap until FunctionalRoleEnum adds a heavy-metal-immobilizer / metal-detoxifier value.

### cheese-assay-evidence-gap: Pairwise cheese-rind competition and cross-feeding assay details require full-text tables beyond cached PMID:25043025 abstract

minor / deferred / confirmed; issue key: cheese-assay-evidence-gap.

Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153) is grounded to the cached PMID:25043025 abstract; strain-pair competition and cross-feeding assay specifics remain deferred until full-text supplementary tables are available (#765).

Disposition: Deferred: source-limited until full-text assay tables for PMID:25043025 are ingested (#765).

### communitymech-1467-source-discrepancy-and-extension: GLBRC Transwell exometabolite SynCom (CommunityMech:000091) full 18-species campaign details require full-text tables

minor / deferred / confirmed; issue key: communitymech-1467-source-discrepancy-and-extension.

GLBRC_Exometabolite_Transwell_SynCom.yaml (CommunityMech:000091) captures the cached abstract-supported five-member model; broader 18-species campaign details and strain-table reconciliation require full-text tables (#1467).

Disposition: Deferred: tracked in GitHub issue #1467 pending full-text table reconciliation.

### communitymech-1699-coverage: Full heterotrophic isolate inventory for Phormidium alkaline consortium (CommunityMech:000054) requires full-text tables

minor / deferred / confirmed; issue key: communitymech-1699-coverage.

Phormidium_Alkaline_Consortium.yaml (CommunityMech:000054) records the abstract-supported cyanobacterial host and glyoxylate-consuming heterotrophic partner; additional co-isolated heterotrophs require full-text table verification (#1699).

Disposition: Deferred: tracked in GitHub issue #1699 pending full-text isolate table verification.

### communitymech-1841: Lower-rank isolate resolution for Sulfide_Spring_Autotrophic_CPR_Biofilm (CommunityMech:000222) requires full-text strain tables

minor / deferred / confirmed; issue key: communitymech-1841.

Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml (CommunityMech:000222) grounds parent-rank taxa from the abstract; resolving lower-rank MAG/isolate assignments requires full-text supplementary tables (#1841).

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

### act-populate-qy2s1-bfr-consortium-abundance-levels

Add abundance_level: DOMINANT to Dehalogenimonas (taxonomy[0], NCBITaxon:670486), Clostridium (taxonomy[1], NCBITaxon:1485), Sedimentibacter (taxonomy[2], NCBITaxon:190972), and Methanoculleus (taxonomy[3], NCBITaxon:45989) backed by PMID:42511722 (doi:10.3390/ijms27146379) on CommunityMech:000424, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml
- just validate-history history

### act-populate-wine-yeast-contact-consortium-abundance-levels

Add abundance_level: DOMINANT to Saccharomyces cerevisiae VIN13 (taxonomy[0], NCBITaxon:4932) and abundance_level: COMMON (or DOMINANT) to Lachancea thermotolerans IWBT Y1240 (taxonomy[1], NCBITaxon:381046) and Torulaspora delbrueckii LO544 (taxonomy[2], NCBITaxon:4950) backed by PMID:42176030 (doi:10.1007/s00253-026-13856-4) on CommunityMech:000438, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml
- just validate-history history

### act-defer-vocabulary-and-source-limited-findings-c13s4

Retain 3 vocabulary-blocked FunctionalRoleEnum findings (#2194) on CommunityMech:000374, 000533, and 000534 and 7 source-limited full-text findings (#765, #1467, #1657, #1681, #1699, #1841, #1847) on CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify FunctionalRoleEnum vocabulary expansion (#2194) or full-text table availability before modifying deferred claims.

## Category Boundaries

- split: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000374, CommunityMech:000424, CommunityMech:000438, CommunityMech:000533, CommunityMech:000534, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:ISOLATES:RHIZOSPHERE, cohort:ISOLATES:SYNTROPHY, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA. The full 537-record CommunityMech corpus spans 3 record roots (kb/communities/, data/isolates/, kb/taxa/) and 16 ecological categories, which is over-broad for a single unpartitioned cohort. Splitting by root and community_category yields 23 disjoint, ecologically coherent cohorts (16 community cohorts, 6 isolate cohorts, and 1 TAXA cohort) for comparative rubric evaluation.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and CommonTaxon classes | supports | All 512 kb/communities/*.yaml, 23 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records (537 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | scripts/audit_completeness.py; 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness() across all 537 records | supports | Proportional 100-point review-communities Completeness Score audit across all 535 MicrobialCommunity records (min 50, median 94, mean 91.32, max 100; CommunityMech:000424 = 95/100 [s_ab = 0/5], CommunityMech:000438 = 83/100 [s_ab = 0/5], CommunityMech:000374 = 90/100 [s_fr = 0/10], CommunityMech:000533 = 85/100 [s_fr = 0/10, external_resources = 0/5], CommunityMech:000534 = 85/100 [s_fr = 0/10, external_resources = 0/5]) and 2 CommonTaxon files (100/100) confirmed 100% core metadata presence and 100% top-level environment_term coverage (535/535), while scripts/audit_completeness.py:calculate_completeness() scores 000424 at 90/100, 000438 at 85/100, 000374 at 40/100, 000533 at 25/100, and 000534 at 25/100. |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | NetworkIntegrityAuditor across 512 kb/communities and 23 data/isolates records found 495/512 communities and 23/23 isolates with 0 warnings (including all 30/30 MicrobialCommunity records in the 32-record deep audit) and 17 community records with 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-536 | supports | Corpus-wide causal graph inventory covers all 535 MicrobialCommunity records (512 kb/communities/*.yaml and 23 data/isolates/*.yaml) through CommunityMech:000541 with 100% SHA-256 attestation in verify_causal_graph_reviews.py after Cycle 13 Stage 2 (#2744). |
| ev-common-taxon-linkage-audit | kb/taxa/Shewanella_oneidensis_MR1.yaml; TaxonomicComposition.common_taxon cross-references and kb/taxa/*.yaml EvidenceItem entries | supports | Corpus-wide audit of reusable taxon cross-references confirmed 22 TaxonomicComposition.common_taxon links across 21 MicrobialCommunity records (20 kb/communities/*.yaml records and 1 data/isolates/*.yaml record: 6 Geobacter sulfurreducens communities linked to CommunityMech:taxon:000002 [4 reusable UniProt EET genes with 33 verified EvidenceItems] and 15 Shewanella oneidensis communities plus isolate baseline CommunityMech:000524 linked to CommunityMech:taxon:000001 [5 reusable UniProt EET genes with 42 verified EvidenceItems], with CommunityMech:000177 linking to both) after Cycle 13 Stage 3 (#2745). |
| ev-qy2s1-bfr-consortium-pmid42511722 | PMID:42511722; kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml | supports | PMID:42511722 (doi:10.3390/ijms27146379) establishes that the QY2S1 reductive dehalogenation consortium is predominantly composed of Bacillota (43.84 ± 3.76%~54.15 ± 7.28%, represented by Clostridium and Sedimentibacter as dominant fermenters), Chloroflexota (19.70 ± 4.90%~29.33 ± 5.27%, represented by Dehalogenimonas as the key functional OHRB), and Halobacteriota (11.72 ± 4.57%~27.33 ± 9.08%, represented by Methanoculleus as the primary methanogens). |
| ev-wine-yeast-contact-consortium-pmid42176030 | PMID:42176030; kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml | supports | PMID:42176030 (doi:10.1007/s00253-026-13856-4) establishes that Saccharomyces cerevisiae VIN13 (NCBITaxon:4932), Lachancea thermotolerans IWBT Y1240 (NCBITaxon:381046), and Torulaspora delbrueckii LO544 (NCBITaxon:4950) were co-inoculated at equal initial cell densities (ca. 5 × 10^6 cells/mL each; total 1.6 × 10^7 cells/mL), with S. cerevisiae establishing sole numerical dominance in direct physical contact (reaching 3.7 × 10^7 cells/mL at 12 h while both non-Saccharomyces species reached ca. 2.5 × 10^7 cells/mL). |
| ev-achromobacter-enterobacter-sl8-sl12-pmid42307251 | PMID:42307251; kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml, data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml, data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml | supports | PMID:42307251 (doi:10.1128/spectrum.01081-26) establishes that Achromobacter sp. SL8 (NCBITaxon:222) and Enterobacter sp. SL12 (NCBITaxon:547) are primary cadmium-detoxifying and cadmium-immobilizing bacteria in both the defined SL8-SL12 coculture (CommunityMech:000374) and the single-strain monoculture isolate baselines (CommunityMech:000533 and CommunityMech:000534); inorganic Cd2+ immobilization remains deferred under open issue #2194 (#301) until FunctionalRoleEnum adds a metal-immobilizer / metal-detoxifier value. |
| ev-prior-structured-reviews | reviews/structured; 271 retained structured review bundles through 20261109T080500Z-c12s5-remediation-verification | context_only | Lineage inspection of all 271 prior structured reviews and Cycle 12 Stage 5 evidence.yaml confirmed that both Cycle 12 Stage 4 abundance_level findings across CommunityMech:000115 and 000116 were resolved in Cycle 12 Stage 5 (#2740, PR #2741), 3 FunctionalRoleEnum vocabulary-gap findings across CommunityMech:000374, 000533, and 000534 remain deferred under #2194, and 7 record-scoped source-limited findings remain deferred at commit acd658dac45d0d64d5903cd8289e72925b8ffa13. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Three cadmium-immobilization records (CommunityMech:000374, 000533, 000534) remain deferred under open GitHub issue #2194 (#301) until FunctionalRoleEnum adds a heavy-metal-immobilizer / metal-detoxifier value.
- Seven carried-forward community records remain source-limited because cached abstracts do not provide full-text assay or strain tables (#765, #1467, #1657, #1681, #1699, #1841, #1847).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261110T005600Z-c13s4-frozen-cohort-review
kind: category
repository: CultureBotAI/CommunityMech
title: Cycle 13 Stage 4 Full-Corpus Frozen Inventory and Cohort Review (537 Records
  Across 23 Cohorts)
started_at: '2026-11-10T00:50:00Z'
finished_at: '2026-11-10T00:56:00Z'
reviewer:
  identity: antigravity-c13s4-cohort-reviewer
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Dedicated Cycle 13 Stage 4 full-corpus read-only review pass
    over frozen commit acd658dac45d0d64d5903cd8289e72925b8ffa13 without record mutation.
skill: review-yaml-category
completion: completed
verdict: needs_curation
native_verdict: 'NEEDS_CURATION (525/537 records pass without unresolved findings;
  2 new actionable open findings across 2 records, 3 carried-forward vocabulary-blocked
  deferred findings across 3 records under #2194, and 7 carried-forward source-limited
  deferred findings across 7 records)'
scientific_review: true
summary: 'Full-corpus frozen inventory and cohort review of all 537 eligible CommunityMech
  records (512 kb/communities/*.yaml, 23 data/isolates/*.yaml, 2 kb/taxa/*.yaml) partitioned
  into 23 disjoint domain cohorts at commit acd658dac45d0d64d5903cd8289e72925b8ffa13.
  All 537 records pass LinkML schema validation, ontology ID-label verification, and
  verbatim snippet checks; mean Completeness Score across 535 MicrobialCommunity records
  is 91.32/100 (median 94/100), with 100% top-level environment_term coverage (535/535)
  and 100% reusable CommonTaxon linkage (22/22 matching Shewanella oneidensis and
  Geobacter sulfurreducens occurrences across 21 MicrobialCommunity records: 20 kb/communities/*.yaml
  records and 1 data/isolates/*.yaml record, linked to 5 reusable EET genes / 42 EvidenceItems
  on CommunityMech:taxon:000001 and 4 reusable EET genes / 33 EvidenceItems on CommunityMech:taxon:000002).
  Two actionable open P2 findings across 2 records (CommunityMech:000424 and 000438),
  3 carried-forward FunctionalRoleEnum vocabulary-blocked deferred findings across
  3 records (CommunityMech:000374, 000533, 000534 under #2194), and 7 carried-forward
  source-limited deferred findings are preserved for Cycle 13 Stage 5 grouped remediation.'
source:
  git_revision: acd658dac45d0d64d5903cd8289e72925b8ffa13
  state: git_commit
  inputs:
  - path: data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml
    sha256: 0680fbc0c1ee94f3a79ce13d9c6b3d8b91317022addca4c095195a37974b6d0e
    role: target
  - path: data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml
    sha256: 1183e9ac2b3567f395e7f19cceb575ac15227bc4ce1323736c042d1fbd43fb4b
    role: target
  - path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
    sha256: 3f3fe69bc250a439ff851305a95d485ad1deee50602335de11b36601542e04d4
    role: target
  - path: data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml
    sha256: 68a2f6ea9b523e7db0eacf6ef1a87af5227cd3f6c7e93be14facffc265232796
    role: target
  - path: data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml
    sha256: 991e85326303854835a6a7481d1599e068f4d67411856fbb8092620953919b18
    role: target
  - path: data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml
    sha256: cc05785add2613ee69f29971820f913e038de75e44d584a3d8ec22015377c0f1
    role: target
  - path: data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml
    sha256: 64b3114cddeee0140d34709e04dd0510dbc62710da0a73810629133c72147f71
    role: target
  - path: kb/communities/AMD_Acidophile_Heterotroph_Network.yaml
    sha256: 81fe29292038349e959041675b876ef4e351cdfb6884796989540185c6797834
    role: target
  - path: kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
    sha256: f3a69684e81df00ca791bfc61832141ad9048270f4b3ed476328b772d07604d2
    role: target
  - path: kb/communities/ANME_SRB_Anaerobic_Methanotrophic_Syntrophic_Consortia.yaml
    sha256: 33b202bc07eceb38a47c560434734e8b21f1b251bf20433964af97aef3568b6b
    role: target
  - path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
    sha256: 8b38b18b0519f17b387ecdd88334ea66438df128cd912a5c56da4f8c1f6d012d
    role: target
  - path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    sha256: eeef4a3c72f6660c2263fe91ec7858610797c19fa513bf641e2a6234ff4414d4
    role: target
  - path: kb/communities/Alaska_Tundra_Permafrost_Iron_Redox_Community.yaml
    sha256: f6995f5d0e91799be24fe9cda290def69b08cb30c1c5f939b4f58d7e7888dfee
    role: target
  - path: kb/communities/Alfalfa_Stress_Adapted_Bacterial_SynCom.yaml
    sha256: ff5a241eec381f83352135c004e32f39407dc4d82fb4f2bbba2c2bbb299a71d9
    role: target
  - path: kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml
    sha256: cef1f3c47035ef336cb809456b25a185e0397bb9f0a16c492becdb5b371529f5
    role: target
  - path: kb/communities/Altered_Schaedler_Flora_Gnotobiotic_Mouse_Community.yaml
    sha256: be4b61b43e7901960e96c485a8c234f87375fd9c16cc07c08a969ca75bc21aa9
    role: target
  - path: kb/communities/Angelarchaeales_Thermoplasmata_CuMMO_Soil_Sediment_Community.yaml
    sha256: 2db6b0937bb7b4158fe6dec8e82d98a5ad9359ede221315a22cd8cf110739b3c
    role: target
  - path: kb/communities/Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml
    sha256: 90510230f2053bb53ef0f2020d0bf60b557586fa250312df1c6bdb56ade99a23
    role: target
  - path: kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml
    sha256: 46b0aef3dfa908dafade954d7aecef895465874f2121772e7e3f6cf1982fdcb1
    role: target
  - path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
    sha256: 882c357a014a5814d0b7c792c6f299944e22a8a35f453a1d53ebdf20065d749e
    role: target
  - path: kb/communities/Bacteroides_Desulfovibrio_Carrageenan_H2S_Coculture.yaml
    sha256: e44ebc56b370c51d94e86c411f50203f53284105a7771fbd3836a8447271f873
    role: target
  - path: kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml
    sha256: 655ff223cc2775123bf63fe23caa3445c1775988dd1d292a7a9edf79c4959a3f
    role: target
  - path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
    sha256: 7d75f820906ff9d78b5b0af28c3f11f89399f0f7b80c28df6438d9f19b3b368d
    role: target
  - path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    sha256: e4ccd373cf107383615b6f207ceb0521c83b4c97daf57c6700a441b2392ddda3
    role: target
  - path: kb/communities/Defined_Multispecies_Enamel_Caries_Model.yaml
    sha256: 320691301cf3e2d94ca9bf69873471e12309ce32271eecc02c3b222a08e6b9d6
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
  - path: kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml
    sha256: a634e28075ce72c27b0bb6348b68bde7ece13d970a0457281aacb8f48710ae3c
    role: target
  - path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    sha256: 904cc9646ae53fe0c021c1461a09f3f8d15b763edad42b6c9a43ada91c87597d
    role: target
  - path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    sha256: 75f43d8ae7e953f895bf8b2e13cd26de63c288cf9200c2476fd60750ba87afcd
    role: target
  - path: kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml
    sha256: ba42e79fb1133d49ce6280562566ffedd6bcf37306ce42b97473e7cfdc1b017f
    role: target
  - path: kb/taxa/Geobacter_sulfurreducens.yaml
    sha256: 413329d881e1bcfcf692ffcd76a3839d183e9abd64952703233f6e786b918d7e
    role: target
  - path: src/communitymech/schema/communitymech.yaml
    sha256: 7355e14f0f17c5d3b875abd33af6474ddc1aad08cc3305313686fede337e259a
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
    sha256: c63a8201286ecbb38938be4d896691f36422258719c2afeb69519a67985dc69b
    role: context
  - path: reports/causal_graph_review/summary.json
    sha256: 50f84c73a4faebeb94d88b85251fd1c518292e469f3efe6367d576f18730f801
    role: context
scope:
  description: Exhaustive cohort review of all 23 domain/root cohorts (encompassing
    all 537 eligible records across kb/communities/*.yaml, data/isolates/*.yaml, and
    kb/taxa/*.yaml) plus all 12 finding-bearing records.
  selection: All 23 domain/root cohorts (537 records total; full per-record SHA-256
    inventory in frozen_inventory_metrics.tsv) and all 12 finding-bearing records
    at Git commit acd658dac45d0d64d5903cd8289e72925b8ffa13.
  coverage: full
  population_size: 35
  reviewed_target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000424
  - CommunityMech:000438
  - CommunityMech:000533
  - CommunityMech:000534
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
  - cohort:ISOLATES:RHIZOSPHERE
  - cohort:ISOLATES:SYNTROPHY
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
- target_id: CommunityMech:000424
  path: kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml
  label: CommunityMech:000424 (QY2-S1 Dehalogenimonas-Rich Brominated-Flame-Retardant
    Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000438
  path: kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml
  label: CommunityMech:000438 (Wine Yeast Three-Species Contact Consortium)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000533
  path: data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml
  label: CommunityMech:000533 (Achromobacter sp. SL8 Cadmium Immobilization Isolate
    Baseline)
  record_class: MicrobialCommunity
  kind: maintained
  ownership_note: Canonical record and history/records/ sidecar maintained in CultureBotAI/CommunityMech.
- target_id: CommunityMech:000534
  path: data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml
  label: CommunityMech:000534 (Enterobacter sp. SL12 Cadmium Immobilization Isolate
    Baseline)
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
  selector: cohort=BIOMINING;records=23
  label: BIOMINING cohort (23 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 23 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:BIOREMEDIATION
  path: kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml
  selector: cohort=BIOREMEDIATION;records=93
  label: BIOREMEDIATION cohort (93 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 93 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:BIOTECHNOLOGY
  path: kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml
  selector: cohort=BIOTECHNOLOGY;records=99
  label: BIOTECHNOLOGY cohort (99 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 99 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:CARBON_SEQUESTRATION
  path: kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml
  selector: cohort=CARBON_SEQUESTRATION;records=12
  label: CARBON_SEQUESTRATION cohort (12 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 12 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:DIET
  path: kb/communities/Bacteroides_Desulfovibrio_Carrageenan_H2S_Coculture.yaml
  selector: cohort=DIET;records=11
  label: DIET cohort (11 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 11 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:EXTREME_ENVIRONMENT
  path: kb/communities/Angelarchaeales_Thermoplasmata_CuMMO_Soil_Sediment_Community.yaml
  selector: cohort=EXTREME_ENVIRONMENT;records=16
  label: EXTREME_ENVIRONMENT cohort (16 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 16 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ISOLATES:BIOMINING
  path: data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml
  selector: cohort=ISOLATES:BIOMINING;records=8
  label: ISOLATES:BIOMINING cohort (8 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 8 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ISOLATES:BIOREMEDIATION
  path: data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml
  selector: cohort=ISOLATES:BIOREMEDIATION;records=9
  label: ISOLATES:BIOREMEDIATION cohort (9 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 9 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ISOLATES:BIOTECHNOLOGY
  path: data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml
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
- target_id: cohort:ISOLATES:RHIZOSPHERE
  path: data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml
  selector: cohort=ISOLATES:RHIZOSPHERE;records=1
  label: ISOLATES:RHIZOSPHERE cohort (1 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 1 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ISOLATES:SYNTROPHY
  path: data/isolates/Escherichia_Coli_PFM2_Anaerobic_Monoculture_Baseline.yaml
  selector: cohort=ISOLATES:SYNTROPHY;records=2
  label: ISOLATES:SYNTROPHY cohort (2 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 2 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:LIGNOCELLULOSE
  path: kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml
  selector: cohort=LIGNOCELLULOSE;records=37
  label: LIGNOCELLULOSE cohort (37 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 37 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:METAL_REDUCTION
  path: kb/communities/Alaska_Tundra_Permafrost_Iron_Redox_Community.yaml
  selector: cohort=METAL_REDUCTION;records=3
  label: METAL_REDUCTION cohort (3 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 3 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:METHANOGENESIS
  path: kb/communities/Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml
  selector: cohort=METHANOGENESIS;records=17
  label: METHANOGENESIS cohort (17 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 17 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:ORAL
  path: kb/communities/Defined_Multispecies_Enamel_Caries_Model.yaml
  selector: cohort=ORAL;records=5
  label: ORAL cohort (5 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 5 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:OTHER
  path: kb/communities/Altered_Schaedler_Flora_Gnotobiotic_Mouse_Community.yaml
  selector: cohort=OTHER;records=45
  label: OTHER cohort (45 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 45 canonical records in CultureBotAI/CommunityMech (per-record
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
  path: kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml
  selector: cohort=PHYTOPLANKTON;records=19
  label: PHYTOPLANKTON cohort (19 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 19 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:RHIZOSPHERE
  path: kb/communities/Alfalfa_Stress_Adapted_Bacterial_SynCom.yaml
  selector: cohort=RHIZOSPHERE;records=85
  label: RHIZOSPHERE cohort (85 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 85 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:SYNTROPHY
  path: kb/communities/ANME_SRB_Anaerobic_Methanotrophic_Syntrophic_Consortia.yaml
  selector: cohort=SYNTROPHY;records=38
  label: SYNTROPHY cohort (38 records)
  record_class: MicrobialCommunity
  kind: snapshot_row
  ownership_note: Cohort of 38 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
- target_id: cohort:TAXA
  path: kb/taxa/Geobacter_sulfurreducens.yaml
  selector: cohort=TAXA;records=2
  label: TAXA cohort (2 records)
  record_class: CommonTaxon
  kind: snapshot_row
  ownership_note: Cohort of 2 canonical records in CultureBotAI/CommunityMech (per-record
    SHA-256 digests in frozen_inventory_metrics.tsv).
checks:
- check_id: chk-linkml-schema-all-537
  name: LinkML schema validation across all 537 records
  status: passed
  required: true
  summary: All 535 MicrobialCommunity records and 2 CommonTaxon files pass LinkML
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
  - CommunityMech:000424
  - CommunityMech:000438
  - CommunityMech:000533
  - CommunityMech:000534
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
  - cohort:ISOLATES:RHIZOSPHERE
  - cohort:ISOLATES:SYNTROPHY
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
  command: .venv/bin/python -c 'validate all 537 records against src/communitymech/schema/communitymech.yaml'
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev-schema-validation-gate
- check_id: chk-network-integrity-all-c13s4
  name: NetworkIntegrityAuditor check across kb/communities/ and data/isolates/
  status: passed
  required: true
  summary: 495/512 community records and 23/23 isolate records have 0 network warnings;
    17 community records have 48 non-fatal warnings (46 DISCONNECTED across 16 records
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
  - CommunityMech:000424
  - CommunityMech:000438
  - CommunityMech:000533
  - CommunityMech:000534
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
  - cohort:ISOLATES:RHIZOSPHERE
  - cohort:ISOLATES:SYNTROPHY
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
- check_id: chk-completeness-rubric-all-c13s4
  name: review-communities Completeness Score rubric across all 537 records
  status: passed
  required: true
  summary: Computed proportional 100-point review-communities Completeness Score (min
    50, median 94, mean 91.32, max 100 across 535 MicrobialCommunity records; 100/100
    across 2 CommonTaxon files; 000424=95/100 [s_ab=0/5], 000438=83/100 [s_ab=0/5],
    000374=90/100 [s_fr=0/10], 000533=85/100 [s_fr=0/10, external_resources=0/5],
    000534=85/100 [s_fr=0/10, external_resources=0/5]; scripts/audit_completeness.py
    scores 90, 85, 40, 25, and 25) and verified causal graph and reusable taxon coverage
    across all 23 cohorts.
  target_ids:
  - CommunityMech:000048
  - CommunityMech:000054
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000222
  - CommunityMech:000295
  - CommunityMech:000302
  - CommunityMech:000374
  - CommunityMech:000424
  - CommunityMech:000438
  - CommunityMech:000533
  - CommunityMech:000534
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
  - cohort:ISOLATES:RHIZOSPHERE
  - cohort:ISOLATES:SYNTROPHY
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
  locator: MicrobialCommunity and CommonTaxon classes
  accessed_at: '2026-11-10T00:51:00Z'
  support: supports
  summary: All 512 kb/communities/*.yaml, 23 data/isolates/*.yaml, and 2 kb/taxa/*.yaml
    records (537 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum
    compliance.
- evidence_id: ev-completeness-audit
  kind: validation
  reference: scripts/audit_completeness.py
  locator: 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness()
    across all 537 records
  accessed_at: '2026-11-10T00:52:00Z'
  support: supports
  summary: Proportional 100-point review-communities Completeness Score audit across
    all 535 MicrobialCommunity records (min 50, median 94, mean 91.32, max 100; CommunityMech:000424
    = 95/100 [s_ab = 0/5], CommunityMech:000438 = 83/100 [s_ab = 0/5], CommunityMech:000374
    = 90/100 [s_fr = 0/10], CommunityMech:000533 = 85/100 [s_fr = 0/10, external_resources
    = 0/5], CommunityMech:000534 = 85/100 [s_fr = 0/10, external_resources = 0/5])
    and 2 CommonTaxon files (100/100) confirmed 100% core metadata presence and 100%
    top-level environment_term coverage (535/535), while scripts/audit_completeness.py:calculate_completeness()
    scores 000424 at 90/100, 000438 at 85/100, 000374 at 40/100, 000533 at 25/100,
    and 000534 at 25/100.
- evidence_id: ev-network-integrity-audit
  kind: validation
  reference: src/communitymech/network/auditor.py
  locator: NetworkIntegrityAuditor.audit_all()
  accessed_at: '2026-11-10T00:52:30Z'
  support: supports
  summary: NetworkIntegrityAuditor across 512 kb/communities and 23 data/isolates
    records found 495/512 communities and 23/23 isolates with 0 warnings (including
    all 30/30 MicrobialCommunity records in the 32-record deep audit) and 17 community
    records with 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL
    UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0
    error-severity issues, 0 broken downstream references).
- evidence_id: ev-causal-inventory
  kind: record_content
  reference: reports/causal_graph_review/inventory.tsv
  locator: rows 1-536
  accessed_at: '2026-11-10T00:53:00Z'
  support: supports
  summary: Corpus-wide causal graph inventory covers all 535 MicrobialCommunity records
    (512 kb/communities/*.yaml and 23 data/isolates/*.yaml) through CommunityMech:000541
    with 100% SHA-256 attestation in verify_causal_graph_reviews.py after Cycle 13
    Stage 2 (#2744).
- evidence_id: ev-common-taxon-linkage-audit
  kind: record_content
  reference: kb/taxa/Shewanella_oneidensis_MR1.yaml
  locator: TaxonomicComposition.common_taxon cross-references and kb/taxa/*.yaml EvidenceItem
    entries
  accessed_at: '2026-11-10T00:53:30Z'
  support: supports
  summary: 'Corpus-wide audit of reusable taxon cross-references confirmed 22 TaxonomicComposition.common_taxon
    links across 21 MicrobialCommunity records (20 kb/communities/*.yaml records and
    1 data/isolates/*.yaml record: 6 Geobacter sulfurreducens communities linked to
    CommunityMech:taxon:000002 [4 reusable UniProt EET genes with 33 verified EvidenceItems]
    and 15 Shewanella oneidensis communities plus isolate baseline CommunityMech:000524
    linked to CommunityMech:taxon:000001 [5 reusable UniProt EET genes with 42 verified
    EvidenceItems], with CommunityMech:000177 linking to both) after Cycle 13 Stage
    3 (#2745).'
- evidence_id: ev-qy2s1-bfr-consortium-pmid42511722
  kind: primary_source
  reference: PMID:42511722
  locator: kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml
  accessed_at: '2026-11-10T00:54:00Z'
  support: supports
  summary: PMID:42511722 (doi:10.3390/ijms27146379) establishes that the QY2S1 reductive
    dehalogenation consortium is predominantly composed of Bacillota (43.84 ± 3.76%~54.15
    ± 7.28%, represented by Clostridium and Sedimentibacter as dominant fermenters),
    Chloroflexota (19.70 ± 4.90%~29.33 ± 5.27%, represented by Dehalogenimonas as
    the key functional OHRB), and Halobacteriota (11.72 ± 4.57%~27.33 ± 9.08%, represented
    by Methanoculleus as the primary methanogens).
  quote: More detailed analysis revealed a consistent microbial community composition
    among different systems, predominantly composed of the phyla Bacillota (formerly
    Firmicutes; 43.84 ± 3.76%~54.15 ± 7.28%), Chloroflexota (19.70 ± 4.90%~29.33 ±
    5.27%), and Halobacteriota (11.72 ± 4.57%~27.33 ± 9.08%). At the genus level,
    these phyla were mainly represented by Clostridium and Sedimentibacter (class
    Clostridia) as the dominant fermenters, along with Dehalogenimonas (class Dehalococcoidia)
    as the key functional OHRB, and Methanoculleus (class Methanomicrobia) as the
    primary methanogens.
- evidence_id: ev-wine-yeast-contact-consortium-pmid42176030
  kind: primary_source
  reference: PMID:42176030
  locator: kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml
  accessed_at: '2026-11-10T00:54:15Z'
  support: supports
  summary: PMID:42176030 (doi:10.1007/s00253-026-13856-4) establishes that Saccharomyces
    cerevisiae VIN13 (NCBITaxon:4932), Lachancea thermotolerans IWBT Y1240 (NCBITaxon:381046),
    and Torulaspora delbrueckii LO544 (NCBITaxon:4950) were co-inoculated at equal
    initial cell densities (ca. 5 × 10^6 cells/mL each; total 1.6 × 10^7 cells/mL),
    with S. cerevisiae establishing sole numerical dominance in direct physical contact
    (reaching 3.7 × 10^7 cells/mL at 12 h while both non-Saccharomyces species reached
    ca. 2.5 × 10^7 cells/mL).
  quote: S. cerevisiae reached maximum cell numbers of 3.7 × 107 cells/mL, while both
    non-Saccharomyces species reached ca. 2.5 × 107 cells/mL (Fig. 3 b).
- evidence_id: ev-achromobacter-enterobacter-sl8-sl12-pmid42307251
  kind: primary_source
  reference: PMID:42307251
  locator: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml,
    data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml,
    data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml
  accessed_at: '2026-11-10T00:54:30Z'
  support: supports
  summary: 'PMID:42307251 (doi:10.1128/spectrum.01081-26) establishes that Achromobacter
    sp. SL8 (NCBITaxon:222) and Enterobacter sp. SL12 (NCBITaxon:547) are primary
    cadmium-detoxifying and cadmium-immobilizing bacteria in both the defined SL8-SL12
    coculture (CommunityMech:000374) and the single-strain monoculture isolate baselines
    (CommunityMech:000533 and CommunityMech:000534); inorganic Cd2+ immobilization
    remains deferred under open issue #2194 (#301) until FunctionalRoleEnum adds a
    metal-immobilizer / metal-detoxifier value.'
  quote: After a 7-day incubation period, RE-Cd values reached 82.6% and 69.55% for
    SL8, 63.4% and 70.8% for SL12, and 82.6% and 80.9% for the co-cultured strains
    at initial Cd concentrations of 50 mg/L and 100 mg/L, respectively.
- evidence_id: ev-prior-structured-reviews
  kind: prior_review
  reference: reviews/structured
  locator: 271 retained structured review bundles through 20261109T080500Z-c12s5-remediation-verification
  accessed_at: '2026-11-10T00:54:45Z'
  support: context_only
  summary: 'Lineage inspection of all 271 prior structured reviews and Cycle 12 Stage
    5 evidence.yaml confirmed that both Cycle 12 Stage 4 abundance_level findings
    across CommunityMech:000115 and 000116 were resolved in Cycle 12 Stage 5 (#2740,
    PR #2741), 3 FunctionalRoleEnum vocabulary-gap findings across CommunityMech:000374,
    000533, and 000534 remain deferred under #2194, and 7 record-scoped source-limited
    findings remain deferred at commit acd658dac45d0d64d5903cd8289e72925b8ffa13.'
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
    value: 94
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
  topic: Cohort review of BIOMINING (23 records)
  outcome: supported
  summary: Cohort BIOMINING comprises 23 records (66 taxa, 70 ecological interactions,
    32 downstream causal edges, 0 inline UniProtKB gene annotations, 7 reusable CommonTaxon
    links) with mean Completeness Score 93.61/100 (min 75/100).
  details: 'Reviewed member records (23): CommunityMech:000005, CommunityMech:000019,
    CommunityMech:000026, CommunityMech:000035, CommunityMech:000045, CommunityMech:000049,
    CommunityMech:000057, CommunityMech:000073, CommunityMech:000217, CommunityMech:000303,
    CommunityMech:000305, CommunityMech:000385, CommunityMech:000404, CommunityMech:000485,
    CommunityMech:000486, CommunityMech:000487, CommunityMech:000491, CommunityMech:000519,
    CommunityMech:000520, CommunityMech:000523, CommunityMech:000526, CommunityMech:000527,
    CommunityMech:000528.'
  target_ids:
  - cohort:BIOMINING
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 93.61
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 23
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 75.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 23
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-bioremediation
  area: completeness
  topic: Cohort review of BIOREMEDIATION (93 records)
  outcome: concern
  summary: Cohort BIOREMEDIATION comprises 93 records (329 taxa, 230 ecological interactions,
    89 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon
    links) with mean Completeness Score 91.95/100 (min 60/100).
  details: 'Reviewed member records (93): CommunityMech:000004, CommunityMech:000024,
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
    CommunityMech:000503, CommunityMech:000504, CommunityMech:000505, CommunityMech:000506,
    CommunityMech:000507, CommunityMech:000508, CommunityMech:000509.'
  target_ids:
  - cohort:BIOREMEDIATION
  - CommunityMech:000374
  - CommunityMech:000424
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 91.95
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 93
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 60.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 93
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-biotechnology
  area: completeness
  topic: Cohort review of BIOTECHNOLOGY (99 records)
  outcome: concern
  summary: Cohort BIOTECHNOLOGY comprises 99 records (312 taxa, 264 ecological interactions,
    96 downstream causal edges, 0 inline UniProtKB gene annotations, 8 reusable CommonTaxon
    links) with mean Completeness Score 89.91/100 (min 50/100).
  details: 'Reviewed member records (99): CommunityMech:000009, CommunityMech:000029,
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
    CommunityMech:000496, CommunityMech:000497, CommunityMech:000517, CommunityMech:000522,
    CommunityMech:000535.'
  target_ids:
  - cohort:BIOTECHNOLOGY
  - CommunityMech:000091
  - CommunityMech:000153
  - CommunityMech:000295
  - CommunityMech:000438
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 89.91
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 99
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 50.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 99
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
  topic: Cohort review of ISOLATES:BIOMINING (8 records)
  outcome: supported
  summary: Cohort ISOLATES:BIOMINING comprises 8 records (8 taxa, 21 ecological interactions,
    9 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon
    links) with mean Completeness Score 94.38/100 (min 91/100).
  details: 'Reviewed member records (8): CommunityMech:000320, CommunityMech:000322,
    CommunityMech:000489, CommunityMech:000490, CommunityMech:000524, CommunityMech:000525,
    CommunityMech:000529, CommunityMech:000530.'
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
    value: 94.38
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 8
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 91.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 8
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-isolates-bioremediation
  area: completeness
  topic: Cohort review of ISOLATES:BIOREMEDIATION (9 records)
  outcome: concern
  summary: Cohort ISOLATES:BIOREMEDIATION comprises 9 records (9 taxa, 12 ecological
    interactions, 3 downstream causal edges, 0 inline UniProtKB gene annotations,
    0 reusable CommonTaxon links) with mean Completeness Score 92.78/100 (min 85/100).
  details: 'Reviewed member records (9): CommunityMech:000488, CommunityMech:000492,
    CommunityMech:000531, CommunityMech:000532, CommunityMech:000533, CommunityMech:000534,
    CommunityMech:000536, CommunityMech:000537, CommunityMech:000538.'
  target_ids:
  - cohort:ISOLATES:BIOREMEDIATION
  - CommunityMech:000533
  - CommunityMech:000534
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 92.78
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 9
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 85.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 9
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
    value: 93
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
    value: 92
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
- assessment_id: assess-cohort-isolates-rhizosphere
  area: completeness
  topic: Cohort review of ISOLATES:RHIZOSPHERE (1 records)
  outcome: supported
  summary: Cohort ISOLATES:RHIZOSPHERE comprises 1 records (1 taxa, 3 ecological interactions,
    0 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 94.00/100 (min 94/100).
  details: 'Reviewed member records (1): CommunityMech:000521.'
  target_ids:
  - cohort:ISOLATES:RHIZOSPHERE
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 94
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 1
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 94.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 1
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-isolates-syntrophy
  area: completeness
  topic: Cohort review of ISOLATES:SYNTROPHY (2 records)
  outcome: supported
  summary: Cohort ISOLATES:SYNTROPHY comprises 2 records (2 taxa, 2 ecological interactions,
    0 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 95.00/100 (min 95/100).
  details: 'Reviewed member records (2): CommunityMech:000539, CommunityMech:000540.'
  target_ids:
  - cohort:ISOLATES:SYNTROPHY
  evidence_ids:
  - ev-schema-validation-gate
  - ev-completeness-audit
  - ev-network-integrity-audit
  - ev-causal-inventory
  - ev-common-taxon-linkage-audit
  metrics:
  - name: mean_completeness_score
    value: 95
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
  topic: Cohort review of OTHER (45 records)
  outcome: supported
  summary: Cohort OTHER comprises 45 records (198 taxa, 131 ecological interactions,
    45 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 87.80/100 (min 55/100).
  details: 'Reviewed member records (45): CommunityMech:000010, CommunityMech:000011,
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
    CommunityMech:000432, CommunityMech:000443, CommunityMech:000515.'
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
    value: 87.8
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 45
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 55.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 45
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
    value: 83
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
    value: 95
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
  topic: Cohort review of RHIZOSPHERE (85 records)
  outcome: concern
  summary: Cohort RHIZOSPHERE comprises 85 records (454 taxa, 269 ecological interactions,
    86 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon
    links) with mean Completeness Score 87.15/100 (min 55/100).
  details: 'Reviewed member records (85): CommunityMech:000003, CommunityMech:000022,
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
    CommunityMech:000477, CommunityMech:000483, CommunityMech:000501, CommunityMech:000513,
    CommunityMech:000514, CommunityMech:000516, CommunityMech:000518.'
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
    value: 87.15
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 85
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 55.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 85
    minimum: 0.0
    maximum: 100.0
- assessment_id: assess-cohort-syntrophy
  area: completeness
  topic: Cohort review of SYNTROPHY (38 records)
  outcome: supported
  summary: Cohort SYNTROPHY comprises 38 records (93 taxa, 119 ecological interactions,
    68 downstream causal edges, 0 inline UniProtKB gene annotations, 2 reusable CommonTaxon
    links) with mean Completeness Score 96.24/100 (min 84/100).
  details: 'Reviewed member records (38): CommunityMech:000006, CommunityMech:000007,
    CommunityMech:000008, CommunityMech:000018, CommunityMech:000023, CommunityMech:000031,
    CommunityMech:000052, CommunityMech:000053, CommunityMech:000068, CommunityMech:000069,
    CommunityMech:000070, CommunityMech:000071, CommunityMech:000134, CommunityMech:000141,
    CommunityMech:000142, CommunityMech:000148, CommunityMech:000150, CommunityMech:000157,
    CommunityMech:000158, CommunityMech:000186, CommunityMech:000187, CommunityMech:000188,
    CommunityMech:000189, CommunityMech:000190, CommunityMech:000276, CommunityMech:000288,
    CommunityMech:000290, CommunityMech:000307, CommunityMech:000327, CommunityMech:000336,
    CommunityMech:000337, CommunityMech:000350, CommunityMech:000469, CommunityMech:000475,
    CommunityMech:000510, CommunityMech:000511, CommunityMech:000512, CommunityMech:000541.'
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
    value: 96.24
    unit: points
    definition: Mean proportional Completeness Score (0-100) across cohort records.
    denominator: 38
    minimum: 0.0
    maximum: 100.0
  - name: min_completeness_score
    value: 84.0
    unit: points
    definition: Minimum proportional Completeness Score (0-100) across cohort records.
    denominator: 38
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
    value: 100
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
- finding_id: c13s4-000424-qy2s1-bfr-consortium-abundance-levels
  issue_key: c13s4-000424-qy2s1-bfr-consortium-abundance-levels
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: All four reductive-dehalogenation consortium members in QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium
    (CommunityMech:000424) populate free-text abundance_value but omit controlled
    abundance_level despite explicit phylum and genus dominance in PMID:42511722
  description: 'In kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml
    (CommunityMech:000424), Dehalogenimonas (taxonomy[0], NCBITaxon:670486, functional_role:
    [PRIMARY_DEGRADER, SYNTROPHIC_PARTNER]), Clostridium (taxonomy[1], NCBITaxon:1485,
    functional_role: [SECONDARY_FERMENTER, SYNTROPHIC_PARTNER]), Sedimentibacter (taxonomy[2],
    NCBITaxon:190972, functional_role: [SECONDARY_FERMENTER, SYNTROPHIC_PARTNER]),
    and Methanoculleus (taxonomy[3], NCBITaxon:45989, functional_role: [SYNTROPHIC_PARTNER,
    ELECTRON_ACCEPTOR]) all populate free-text abundance_value strings but omit the
    controlled abundance_level enum. The cited open-access study (PMID:42511722, doi:10.3390/ijms27146379)
    explicitly establishes that ''More detailed analysis revealed a consistent microbial
    community composition among different systems, predominantly composed of the phyla
    Bacillota (formerly Firmicutes; 43.84 ± 3.76%~54.15 ± 7.28%), Chloroflexota (19.70
    ± 4.90%~29.33 ± 5.27%), and Halobacteriota (11.72 ± 4.57%~27.33 ± 9.08%). At the
    genus level, these phyla were mainly represented by Clostridium and Sedimentibacter
    (class Clostridia) as the dominant fermenters, along with Dehalogenimonas (class
    Dehalococcoidia) as the key functional OHRB, and Methanoculleus (class Methanomicrobia)
    as the primary methanogens.'' Setting abundance_level: DOMINANT on taxonomy[0..3]
    raises the review-communities s_ab abundance_level rubric component from 0/5 to
    5/5 (0/4 -> 4/4 taxa with abundance_level; proportional Completeness Score 95/100
    -> 100/100; scripts/audit_completeness.py score 90/100).'
  target_ids:
  - CommunityMech:000424
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  - taxonomy[2].abundance_level
  - taxonomy[3].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-qy2s1-bfr-consortium-pmid42511722
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing controlled abundance_level on all four core QY2S1
    reductive-dehalogenation consortium genera leaves the review-communities s_ab
    rubric component at 0/5 (Completeness Score 95/100; scripts/audit_completeness.py
    score 90/100) and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005500Z-c13s4-record-deep-audit
    finding_id: c13s4-000424-qy2s1-bfr-consortium-abundance-levels
- finding_id: c13s4-000438-wine-yeast-contact-consortium-abundance-levels
  issue_key: c13s4-000438-wine-yeast-contact-consortium-abundance-levels
  category: completeness
  severity: major
  status: open
  certainty: confirmed
  title: All three defined wine-yeast consortium members in Wine_Yeast_ThreeSpecies_Contact_Consortium
    (CommunityMech:000438) omit abundance_level despite explicit equimolar inoculation
    and 12-h population measurements in PMID:42176030
  description: 'In kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml
    (CommunityMech:000438), Saccharomyces cerevisiae VIN13 (taxonomy[0], NCBITaxon:4932,
    functional_role: [SECONDARY_FERMENTER]), Lachancea thermotolerans IWBT Y1240 (taxonomy[1],
    NCBITaxon:381046, functional_role: [SECONDARY_FERMENTER]), and Torulaspora delbrueckii
    LO544 (taxonomy[2], NCBITaxon:4950, functional_role: [SECONDARY_FERMENTER]) all
    omit abundance_level. The cited open-access study (PMID:42176030, doi:10.1007/s00253-026-13856-4)
    explicitly establishes that each species was inoculated at ca. 5 × 10^6 cells/mL
    (total 1.6 × 10^7 cells/mL) and that in direct physical contact at 12 h ''S. cerevisiae
    reached maximum cell numbers of 3.7 × 107 cells/mL, while both non-Saccharomyces
    species reached ca. 2.5 × 107 cells/mL (Fig. 3 b)'', establishing sole numerical
    dominance of S. cerevisiae in the direct-contact consortium (whereas in indirect
    contact, T. delbrueckii showed rapid growth and early numerical dominance before
    T. delbrueckii and S. cerevisiae both reached ca. 3 × 10^7 cells/mL compared to
    ca. 1 × 10^7 cells/mL for L. thermotolerans). Setting abundance_level: DOMINANT
    on taxonomy[0] (anchored to the direct physical contact consortium where S. cerevisiae
    is the sole numerical majority at 3.7 × 10^7 cells/mL, p < 0.05) and abundance_level:
    COMMON (or DOMINANT) on taxonomy[1] and taxonomy[2] raises the review-communities
    s_ab abundance_level rubric component from 0/5 to 5/5 (0/3 -> 3/3 taxa with abundance_level;
    proportional Completeness Score 83/100 -> 88/100; scripts/audit_completeness.py
    score 85/100).'
  target_ids:
  - CommunityMech:000438
  field_paths:
  - taxonomy[0].abundance_level
  - taxonomy[1].abundance_level
  - taxonomy[2].abundance_level
  evidence_ids:
  - ev-completeness-audit
  - ev-wine-yeast-contact-consortium-pmid42176030
  rule_id: review-yaml-record:taxonomy-abundance-level-completeness
  native_severity: P2
  normalization_reason: Missing source-backed abundance_level on all three defined
    wine-yeast consortium members leaves the review-communities s_ab rubric component
    at 0/5 (Completeness Score 83/100; scripts/audit_completeness.py score 85/100)
    and maps to major (P2).
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - abundance-level
  - completeness
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005500Z-c13s4-record-deep-audit
    finding_id: c13s4-000438-wine-yeast-contact-consortium-abundance-levels
- finding_id: c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
  issue_key: c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
  category: completeness
  severity: minor
  status: deferred
  certainty: confirmed
  title: Both cadmium-immobilizing coculture members in Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture
    (CommunityMech:000374) omit functional_role despite direct Cd-detoxification support
    in PMID:42307251
  description: 'In kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    (CommunityMech:000374), both Achromobacter sp. SL8 (taxonomy[0], NCBITaxon:222,
    abundance_level: DOMINANT) and Enterobacter sp. SL12 (taxonomy[1], NCBITaxon:547,
    abundance_level: DOMINANT) omit functional_role, despite direct Cd-detoxification
    and Cd-immobilization support in the cited open-access study (PMID:42307251, doi:10.1128/spectrum.01081-26:
    ''After a 7-day incubation period, RE-Cd values reached 82.6% and 69.55% for SL8,
    63.4% and 70.8% for SL12, and 82.6% and 80.9% for the co-cultured strains at initial
    Cd concentrations of 50 mg/L and 100 mg/L, respectively.''). Setting functional_role:
    [PRIMARY_DEGRADER] on both taxonomy[0] and taxonomy[1] raises the review-communities
    s_fr functional_role rubric component from 0/10 to 10/10 (Completeness Score 90/100
    -> 100/100) and raises scripts/audit_completeness.py:calculate_completeness()
    from 40/100 to 90/100.'
  target_ids:
  - CommunityMech:000374
  field_paths:
  - taxonomy[0].functional_role
  - taxonomy[1].functional_role
  evidence_ids:
  - ev-completeness-audit
  - ev-achromobacter-enterobacter-sl8-sl12-pmid42307251
  - ev-prior-structured-reviews
  rule_id: review-yaml-record:taxonomy-functional-role-completeness
  native_severity: P3
  normalization_reason: 'P3 minor under #2194 and schema policy #301: missing structured
    FunctionalRoleEnum value because PRIMARY_DEGRADER (''Degrades complex substrates'')
    does not match inorganic Cd2+ immobilization; schema permits omitting functional_role
    while abundance_value and ecological_interactions retain the supported heavy-metal
    immobilization process.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - functional-role
  - completeness
  disposition_reason: 'Deferred under existing open GitHub issue #2194 (and schema
    policy #301): FunctionalRoleEnum.PRIMARY_DEGRADER is defined in src/communitymech/schema/communitymech.yaml
    as ''Degrades complex substrates'' and must not be forced onto inorganic Cd2+
    immobilization via CdS bioprecipitation, intracellular Cd accumulation, and N-H
    / amide C=O surface coordination (PMID:42307251). Preserved as an explicit vocabulary
    gap until FunctionalRoleEnum adds a heavy-metal-immobilizer / metal-detoxifier
    value.'
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2194
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051500Z-c12s4-record-deep-audit
    finding_id: c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005500Z-c13s4-record-deep-audit
    finding_id: c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
- finding_id: c12s4-000533-achromobacter-sl8-isolate-functional-role
  issue_key: c12s4-000533-achromobacter-sl8-isolate-functional-role
  category: completeness
  severity: minor
  status: deferred
  certainty: confirmed
  title: Achromobacter sp. SL8 monoculture isolate baseline Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline
    (CommunityMech:000533) omits functional_role on taxonomy[0] despite direct Cd-immobilization
    support in PMID:42307251
  description: 'In data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml
    (CommunityMech:000533), Achromobacter sp. SL8 (taxonomy[0], NCBITaxon:222, abundance_level:
    DOMINANT) omits functional_role despite direct monoculture cadmium-detoxification
    and Cd-immobilization support in PMID:42307251 (doi:10.1128/spectrum.01081-26:
    ''After a 7-day incubation period, RE-Cd values reached 82.6% and 69.55% for SL8,
    63.4% and 70.8% for SL12, and 82.6% and 80.9% for the co-cultured strains at initial
    Cd concentrations of 50 mg/L and 100 mg/L, respectively.''). Setting functional_role:
    [PRIMARY_DEGRADER] on taxonomy[0] raises the review-communities s_fr functional_role
    rubric component from 0/10 to 10/10 (Completeness Score 85/100 -> 95/100) and
    raises scripts/audit_completeness.py:calculate_completeness() from 25/100 to 75/100.'
  target_ids:
  - CommunityMech:000533
  field_paths:
  - taxonomy[0].functional_role
  evidence_ids:
  - ev-completeness-audit
  - ev-achromobacter-enterobacter-sl8-sl12-pmid42307251
  - ev-prior-structured-reviews
  rule_id: review-yaml-record:taxonomy-functional-role-completeness
  native_severity: P3
  normalization_reason: 'P3 minor under #2194 and schema policy #301: missing structured
    FunctionalRoleEnum value because PRIMARY_DEGRADER (''Degrades complex substrates'')
    does not match inorganic Cd2+ immobilization; schema permits omitting functional_role
    while abundance_value and ecological_interactions retain the supported heavy-metal
    immobilization process.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - functional-role
  - completeness
  disposition_reason: 'Deferred under existing open GitHub issue #2194 (and schema
    policy #301): FunctionalRoleEnum.PRIMARY_DEGRADER is defined in src/communitymech/schema/communitymech.yaml
    as ''Degrades complex substrates'' and must not be forced onto inorganic Cd2+
    immobilization via CdS bioprecipitation, intracellular Cd accumulation, and N-H
    / amide C=O surface coordination (PMID:42307251). Preserved as an explicit vocabulary
    gap until FunctionalRoleEnum adds a heavy-metal-immobilizer / metal-detoxifier
    value.'
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2194
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051500Z-c12s4-record-deep-audit
    finding_id: c12s4-000533-achromobacter-sl8-isolate-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: c12s4-000533-achromobacter-sl8-isolate-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: c12s4-000533-achromobacter-sl8-isolate-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005500Z-c13s4-record-deep-audit
    finding_id: c12s4-000533-achromobacter-sl8-isolate-functional-role
- finding_id: c12s4-000534-enterobacter-sl12-isolate-functional-role
  issue_key: c12s4-000534-enterobacter-sl12-isolate-functional-role
  category: completeness
  severity: minor
  status: deferred
  certainty: confirmed
  title: Enterobacter sp. SL12 monoculture isolate baseline Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline
    (CommunityMech:000534) omits functional_role on taxonomy[0] despite direct Cd-immobilization
    support in PMID:42307251
  description: 'In data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml
    (CommunityMech:000534), Enterobacter sp. SL12 (taxonomy[0], NCBITaxon:547, abundance_level:
    DOMINANT) omits functional_role despite direct monoculture cadmium-detoxification
    and Cd-immobilization support in PMID:42307251 (doi:10.1128/spectrum.01081-26:
    ''After a 7-day incubation period, RE-Cd values reached 82.6% and 69.55% for SL8,
    63.4% and 70.8% for SL12, and 82.6% and 80.9% for the co-cultured strains at initial
    Cd concentrations of 50 mg/L and 100 mg/L, respectively.''). Setting functional_role:
    [PRIMARY_DEGRADER] on taxonomy[0] raises the review-communities s_fr functional_role
    rubric component from 0/10 to 10/10 (Completeness Score 85/100 -> 95/100) and
    raises scripts/audit_completeness.py:calculate_completeness() from 25/100 to 75/100.'
  target_ids:
  - CommunityMech:000534
  field_paths:
  - taxonomy[0].functional_role
  evidence_ids:
  - ev-completeness-audit
  - ev-achromobacter-enterobacter-sl8-sl12-pmid42307251
  - ev-prior-structured-reviews
  rule_id: review-yaml-record:taxonomy-functional-role-completeness
  native_severity: P3
  normalization_reason: 'P3 minor under #2194 and schema policy #301: missing structured
    FunctionalRoleEnum value because PRIMARY_DEGRADER (''Degrades complex substrates'')
    does not match inorganic Cd2+ immobilization; schema permits omitting functional_role
    while abundance_value and ecological_interactions retain the supported heavy-metal
    immobilization process.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml
    role: canonical_record
  tags:
  - actionable
  - stage5-candidate
  - functional-role
  - completeness
  disposition_reason: 'Deferred under existing open GitHub issue #2194 (and schema
    policy #301): FunctionalRoleEnum.PRIMARY_DEGRADER is defined in src/communitymech/schema/communitymech.yaml
    as ''Degrades complex substrates'' and must not be forced onto inorganic Cd2+
    immobilization via CdS bioprecipitation, intracellular Cd accumulation, and N-H
    / amide C=O surface coordination (PMID:42307251). Preserved as an explicit vocabulary
    gap until FunctionalRoleEnum adds a heavy-metal-immobilizer / metal-detoxifier
    value.'
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/2194
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051500Z-c12s4-record-deep-audit
    finding_id: c12s4-000534-enterobacter-sl12-isolate-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: c12s4-000534-enterobacter-sl12-isolate-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: c12s4-000534-enterobacter-sl12-isolate-functional-role
  - repository: CultureBotAI/CommunityMech
    review_id: 20261110T005500Z-c13s4-record-deep-audit
    finding_id: c12s4-000534-enterobacter-sl12-isolate-functional-role
- finding_id: cheese-assay-evidence-gap
  issue_key: cheese-assay-evidence-gap
  category: evidence
  severity: minor
  status: deferred
  certainty: confirmed
  title: Pairwise cheese-rind competition and cross-feeding assay details require
    full-text tables beyond cached PMID:25043025 abstract
  description: Cheese_Rind_InSitu_InVitro_Model_Community.yaml (CommunityMech:000153)
    is grounded to the cached PMID:25043025 abstract; strain-pair competition and
    cross-feeding assay specifics remain deferred until full-text supplementary tables
    are available (#765).
  target_ids:
  - CommunityMech:000153
  field_paths:
  - ecological_interactions
  evidence_ids:
  - ev-prior-structured-reviews
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text evidence gap preserved as minor.
  disposition_reason: 'Deferred: source-limited until full-text assay tables for PMID:25043025
    are ingested (#765).'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T071900Z-cheese-rind-audit
    finding_id: assay-evidence-gap
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: cheese-assay-evidence-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
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
  title: GLBRC Transwell exometabolite SynCom (CommunityMech:000091) full 18-species
    campaign details require full-text tables
  description: GLBRC_Exometabolite_Transwell_SynCom.yaml (CommunityMech:000091) captures
    the cached abstract-supported five-member model; broader 18-species campaign details
    and strain-table reconciliation require full-text tables (#1467).
  target_ids:
  - CommunityMech:000091
  field_paths:
  - taxonomy
  - ecological_interactions
  evidence_ids:
  - ev-prior-structured-reviews
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text extension gap preserved as minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1467 pending full-text table
    reconciliation.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T223718Z-glbrc-before
    finding_id: source-discrepancy
  - repository: CultureBotAI/CommunityMech
    review_id: 20261014T231926Z-glbrc-after
    finding_id: source-discrepancy
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: communitymech-1467-source-discrepancy-and-extension
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
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
  title: Full heterotrophic isolate inventory for Phormidium alkaline consortium (CommunityMech:000054)
    requires full-text tables
  description: Phormidium_Alkaline_Consortium.yaml (CommunityMech:000054) records
    the abstract-supported cyanobacterial host and glyoxylate-consuming heterotrophic
    partner; additional co-isolated heterotrophs require full-text table verification
    (#1699).
  target_ids:
  - CommunityMech:000054
  field_paths:
  - taxonomy
  evidence_ids:
  - ev-prior-structured-reviews
  rule_id: review-yaml-record:source-limited-gap
  native_severity: P3
  normalization_reason: Source-limited full-text taxonomic coverage gap preserved
    as minor.
  disposition_reason: 'Deferred: tracked in GitHub issue #1699 pending full-text isolate
    table verification.'
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical_record
  previous_occurrences:
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T052328Z-phormidium-before
    finding_id: coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261015T052748Z-phormidium-after
    finding_id: coverage
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: communitymech-1699-coverage
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
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
  title: Lower-rank isolate resolution for Sulfide_Spring_Autotrophic_CPR_Biofilm
    (CommunityMech:000222) requires full-text strain tables
  description: Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml (CommunityMech:000222)
    grounds parent-rank taxa from the abstract; resolving lower-rank MAG/isolate assignments
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: communitymech-1841
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: communitymech-1841
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: communitymech-1847-metg2-membership
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: okeke-fulltext-assay-gap
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T180100Z-c6s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261104T203000Z-c6s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261105T144100Z-c7s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
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
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T052000Z-c9s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T062000Z-c9s5-remediation-verification-r2
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T174500Z-c10s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T193500Z-c10s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261107T202000Z-c10s5-remediation-verification-r2
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T121500Z-c11s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261108T150500Z-c11s5-remediation-verification
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T051600Z-c12s4-frozen-cohort-review
    finding_id: parachlorella-remaining-research
  - repository: CultureBotAI/CommunityMech
    review_id: 20261109T080500Z-c12s5-remediation-verification
    finding_id: parachlorella-remaining-research
  external_issues:
  - https://github.com/CultureBotAI/CommunityMech/issues/1681
  tags:
  - carried-forward
  - source-limited
actions:
- action_id: act-populate-qy2s1-bfr-consortium-abundance-levels
  description: 'Add abundance_level: DOMINANT to Dehalogenimonas (taxonomy[0], NCBITaxon:670486),
    Clostridium (taxonomy[1], NCBITaxon:1485), Sedimentibacter (taxonomy[2], NCBITaxon:190972),
    and Methanoculleus (taxonomy[3], NCBITaxon:45989) backed by PMID:42511722 (doi:10.3390/ijms27146379)
    on CommunityMech:000424, and append curation_history.'
  finding_ids:
  - c13s4-000424-qy2s1-bfr-consortium-abundance-levels
  target_ids:
  - CommunityMech:000424
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/QY2S1_Dehalogenimonas_BFR_Bioremediation_Consortium.yaml
  - just validate-history history
- action_id: act-populate-wine-yeast-contact-consortium-abundance-levels
  description: 'Add abundance_level: DOMINANT to Saccharomyces cerevisiae VIN13 (taxonomy[0],
    NCBITaxon:4932) and abundance_level: COMMON (or DOMINANT) to Lachancea thermotolerans
    IWBT Y1240 (taxonomy[1], NCBITaxon:381046) and Torulaspora delbrueckii LO544 (taxonomy[2],
    NCBITaxon:4950) backed by PMID:42176030 (doi:10.1007/s00253-026-13856-4) on CommunityMech:000438,
    and append curation_history.'
  finding_ids:
  - c13s4-000438-wine-yeast-contact-consortium-abundance-levels
  target_ids:
  - CommunityMech:000438
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml
    role: canonical_record
  acceptance_checks:
  - uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class
    MicrobialCommunity kb/communities/Wine_Yeast_ThreeSpecies_Contact_Consortium.yaml
  - just validate-history history
- action_id: act-defer-vocabulary-and-source-limited-findings-c13s4
  description: 'Retain 3 vocabulary-blocked FunctionalRoleEnum findings (#2194) on
    CommunityMech:000374, 000533, and 000534 and 7 source-limited full-text findings
    (#765, #1467, #1657, #1681, #1699, #1841, #1847) on CommunityMech:000048, 000054,
    000091, 000153, 000222, 000295, and 000302.'
  finding_ids:
  - c12s4-000374-achromobacter-enterobacter-sl8-sl12-functional-roles
  - c12s4-000533-achromobacter-sl8-isolate-functional-role
  - c12s4-000534-enterobacter-sl12-isolate-functional-role
  - cheese-assay-evidence-gap
  - communitymech-1467-source-discrepancy-and-extension
  - communitymech-1699-coverage
  - communitymech-1841
  - communitymech-1847-metg2-membership
  - okeke-fulltext-assay-gap
  - parachlorella-remaining-research
  target_ids:
  - CommunityMech:000374
  - CommunityMech:000533
  - CommunityMech:000534
  - CommunityMech:000153
  - CommunityMech:000091
  - CommunityMech:000054
  - CommunityMech:000222
  - CommunityMech:000302
  - CommunityMech:000048
  - CommunityMech:000295
  owner_paths:
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Achromobacter_Enterobacter_SL8_SL12_Cadmium_Immobilization_Coculture.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Achromobacter_SL8_Cadmium_Immobilization_Isolate_Baseline.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: data/isolates/Enterobacter_SL12_Cadmium_Immobilization_Isolate_Baseline.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Phormidium_Alkaline_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml
    role: canonical_record
  - repository: CultureBotAI/CommunityMech
    path: kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml
    role: canonical_record
  acceptance_checks:
  - Verify FunctionalRoleEnum vocabulary expansion (#2194) or full-text table availability
    before modifying deferred claims.
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
  - CommunityMech:000424
  - CommunityMech:000438
  - CommunityMech:000533
  - CommunityMech:000534
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
  - cohort:ISOLATES:RHIZOSPHERE
  - cohort:ISOLATES:SYNTROPHY
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
  rationale: The full 537-record CommunityMech corpus spans 3 record roots (kb/communities/,
    data/isolates/, kb/taxa/) and 16 ecological categories, which is over-broad for
    a single unpartitioned cohort. Splitting by root and community_category yields
    23 disjoint, ecologically coherent cohorts (16 community cohorts, 6 isolate cohorts,
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
  - label: BIOREMEDIATION
    target_ids:
    - cohort:BIOREMEDIATION
    - CommunityMech:000374
    - CommunityMech:000424
  - label: BIOTECHNOLOGY
    target_ids:
    - cohort:BIOTECHNOLOGY
    - CommunityMech:000091
    - CommunityMech:000153
    - CommunityMech:000295
    - CommunityMech:000438
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
    - CommunityMech:000533
    - CommunityMech:000534
  - label: ISOLATES:BIOTECHNOLOGY
    target_ids:
    - cohort:ISOLATES:BIOTECHNOLOGY
  - label: ISOLATES:EXTREME_ENVIRONMENT
    target_ids:
    - cohort:ISOLATES:EXTREME_ENVIRONMENT
  - label: ISOLATES:RHIZOSPHERE
    target_ids:
    - cohort:ISOLATES:RHIZOSPHERE
  - label: ISOLATES:SYNTROPHY
    target_ids:
    - cohort:ISOLATES:SYNTROPHY
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
  review_id: 20261110T005500Z-c13s4-record-deep-audit
  relationship: companion_per_record_deep_audit
- repository: CultureBotAI/CommunityMech
  review_id: 20261109T051600Z-c12s4-frozen-cohort-review
  relationship: prior_cycle_stage4_cohort_review
- repository: CultureBotAI/CommunityMech
  review_id: 20261109T080500Z-c12s5-remediation-verification
  relationship: prior_cycle_stage5_remediation_review
limitations:
- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- 'Three cadmium-immobilization records (CommunityMech:000374, 000533, 000534) remain
  deferred under open GitHub issue #2194 (#301) until FunctionalRoleEnum adds a heavy-metal-immobilizer
  / metal-detoxifier value.'
- 'Seven carried-forward community records remain source-limited because cached abstracts
  do not provide full-text assay or strain tables (#765, #1467, #1657, #1681, #1699,
  #1841, #1847).'
tags:
- cycle13
- stage4
- cohort-review
- full-corpus
```
