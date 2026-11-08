# Cycle 11 Stage 4 Full-Corpus Frozen Inventory and Cohort Review (526 Records Across 22 Cohorts)

- Review: 20261108T121500Z-c11s4-frozen-cohort-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-08T12:08:00Z
- Finished UTC: 2026-11-08T12:15:00Z
- Reviewer: antigravity-c11s4-cohort-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full-corpus frozen inventory and cohort review of all 526 eligible CommunityMech records (510 kb/communities/*.yaml, 14 data/isolates/*.yaml, 2 kb/taxa/*.yaml) partitioned into 22 disjoint domain cohorts at commit e9ada20c23b553a0328f8d0601b46ab8fcb906f3. All 526 records pass LinkML schema validation, ontology ID-label verification, and verbatim snippet checks; mean Completeness Score across 524 MicrobialCommunity records is 91.3/100 (median 93/100), with 100% top-level environment_term coverage (524/524) and 100% reusable CommonTaxon linkage (22/22 matching Shewanella oneidensis and Geobacter sulfurreducens occurrences across 21 MicrobialCommunity records: 20 kb/communities/*.yaml records and 1 data/isolates/*.yaml record). Three actionable open P2 findings across 3 community records (CommunityMech:000069, 000181, 000213) and 7 carried-forward source-limited deferred findings are preserved for Cycle 11 Stage 5 grouped remediation.

## Scope And Provenance

Exhaustive cohort review of all 22 domain/root cohorts (encompassing all 526 eligible records across kb/communities/*.yaml, data/isolates/*.yaml, and kb/taxa/*.yaml) plus all 10 finding-bearing records.

Selection: All 22 domain/root cohorts (526 records total; full per-record SHA-256 inventory in frozen_inventory_metrics.tsv) and all 10 finding-bearing records at Git commit e9ada20c23b553a0328f8d0601b46ab8fcb906f3.
Coverage: full; 32 reviewed / 32 in the declared population.
Source: git_commit at Git base e9ada20c23b553a0328f8d0601b46ab8fcb906f3.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000048 | kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml | maintained | CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium) |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | CommunityMech:000054 (Phormidium Alkaline Consortium) |
| CommunityMech:000069 | kb/communities/Syntrophobacter_Methanospirillum_Syntrophy.yaml | maintained | CommunityMech:000069 (Syntrophobacter-Methanospirillum Syntrophic Consortium) |
| CommunityMech:000091 | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml | maintained | CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System) |
| CommunityMech:000153 | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml | maintained | CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community) |
| CommunityMech:000181 | kb/communities/Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture.yaml | maintained | CommunityMech:000181 (Pseudomonas-Rhodococcus Chloronitrobenzene Coculture) |
| CommunityMech:000213 | kb/communities/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm.yaml | maintained | CommunityMech:000213 (Variovorax-Cryptococcus Vitamin Cross-Feeding Microcosm) |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml | maintained | CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm) |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic Co-culture) |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience) |
| cohort:AMD | kb/communities/AMD_Acidophile_Heterotroph_Network.yaml # cohort=AMD;records=7 | snapshot_row | AMD cohort (7 records) |
| cohort:BIOMINING | kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml # cohort=BIOMINING;records=23 | snapshot_row | BIOMINING cohort (23 records) |
| cohort:BIOREMEDIATION | kb/communities/AM_AB_Chlorella_MLSS_Wastewater_Consortium.yaml # cohort=BIOREMEDIATION;records=93 | snapshot_row | BIOREMEDIATION cohort (93 records) |
| cohort:BIOTECHNOLOGY | kb/communities/Aalborg_East_Full_Scale_EBPR_Community.yaml # cohort=BIOTECHNOLOGY;records=98 | snapshot_row | BIOTECHNOLOGY cohort (98 records) |
| cohort:CARBON_SEQUESTRATION | kb/communities/California_Grassland_Precipitation_Legacy_Soil_Community.yaml # cohort=CARBON_SEQUESTRATION;records=12 | snapshot_row | CARBON_SEQUESTRATION cohort (12 records) |
| cohort:DIET | kb/communities/Bacteroides_Desulfovibrio_Carrageenan_H2S_Coculture.yaml # cohort=DIET;records=11 | snapshot_row | DIET cohort (11 records) |
| cohort:EXTREME_ENVIRONMENT | kb/communities/Angelarchaeales_Thermoplasmata_CuMMO_Soil_Sediment_Community.yaml # cohort=EXTREME_ENVIRONMENT;records=16 | snapshot_row | EXTREME_ENVIRONMENT cohort (16 records) |
| cohort:ISOLATES:BIOMINING | data/isolates/Acidithiobacillus_LED_Metal_Bioleaching.yaml # cohort=ISOLATES:BIOMINING;records=8 | snapshot_row | ISOLATES:BIOMINING cohort (8 records) |
| cohort:ISOLATES:BIOREMEDIATION | data/isolates/Bacillus_licheniformis_Chromate_Biosorption.yaml # cohort=ISOLATES:BIOREMEDIATION;records=2 | snapshot_row | ISOLATES:BIOREMEDIATION cohort (2 records) |
| cohort:ISOLATES:BIOTECHNOLOGY | data/isolates/BioModels_MODEL2204300002_Kefir_Rothia_Model.yaml # cohort=ISOLATES:BIOTECHNOLOGY;records=2 | snapshot_row | ISOLATES:BIOTECHNOLOGY cohort (2 records) |
| cohort:ISOLATES:EXTREME_ENVIRONMENT | data/isolates/Ferroplasma_Acidiphilum_ZJ_AMD_Genomic_Island_Adaptation.yaml # cohort=ISOLATES:EXTREME_ENVIRONMENT;records=1 | snapshot_row | ISOLATES:EXTREME_ENVIRONMENT cohort (1 records) |
| cohort:ISOLATES:RHIZOSPHERE | data/isolates/Pseudomonas_Protegens_E1BL2_Jala_Maize_Isolate_Baseline.yaml # cohort=ISOLATES:RHIZOSPHERE;records=1 | snapshot_row | ISOLATES:RHIZOSPHERE cohort (1 records) |
| cohort:LIGNOCELLULOSE | kb/communities/Bacillales_Lignin_Degrading_LDSynCom.yaml # cohort=LIGNOCELLULOSE;records=37 | snapshot_row | LIGNOCELLULOSE cohort (37 records) |
| cohort:METAL_REDUCTION | kb/communities/Alaska_Tundra_Permafrost_Iron_Redox_Community.yaml # cohort=METAL_REDUCTION;records=3 | snapshot_row | METAL_REDUCTION cohort (3 records) |
| cohort:METHANOGENESIS | kb/communities/Asgard_Wetland_Soil_Methanogenesis_Substrate_Community.yaml # cohort=METHANOGENESIS;records=17 | snapshot_row | METHANOGENESIS cohort (17 records) |
| cohort:ORAL | kb/communities/Defined_Multispecies_Enamel_Caries_Model.yaml # cohort=ORAL;records=5 | snapshot_row | ORAL cohort (5 records) |
| cohort:OTHER | kb/communities/Altered_Schaedler_Flora_Gnotobiotic_Mouse_Community.yaml # cohort=OTHER;records=45 | snapshot_row | OTHER cohort (45 records) |
| cohort:PHAGE_PREDATION | kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml # cohort=PHAGE_PREDATION;records=2 | snapshot_row | PHAGE_PREDATION cohort (2 records) |
| cohort:PHYTOPLANKTON | kb/communities/Auxenochlorella_Pseudomonas_Florfenicol_Phycosphere_Coculture.yaml # cohort=PHYTOPLANKTON;records=19 | snapshot_row | PHYTOPLANKTON cohort (19 records) |
| cohort:RHIZOSPHERE | kb/communities/Alfalfa_Stress_Adapted_Bacterial_SynCom.yaml # cohort=RHIZOSPHERE;records=85 | snapshot_row | RHIZOSPHERE cohort (85 records) |
| cohort:SYNTROPHY | kb/communities/ANME_SRB_Anaerobic_Methanotrophic_Syntrophic_Consortia.yaml # cohort=SYNTROPHY;records=37 | snapshot_row | SYNTROPHY cohort (37 records) |
| cohort:TAXA | kb/taxa/Geobacter_sulfurreducens.yaml # cohort=TAXA;records=2 | snapshot_row | TAXA cohort (2 records) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation across all 526 records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000069, CommunityMech:000091, CommunityMech:000153, CommunityMech:000181, CommunityMech:000213, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:ISOLATES:RHIZOSPHERE, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | All 524 MicrobialCommunity records and 2 CommonTaxon files pass LinkML schema validation with 0 errors and 100% EvidenceItem.evidence_source enum compliance. |
| NetworkIntegrityAuditor check across kb/communities/ and data/isolates/ | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000069, CommunityMech:000091, CommunityMech:000153, CommunityMech:000181, CommunityMech:000213, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:ISOLATES:RHIZOSPHERE, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | 493/510 community records and 14/14 isolate records have 0 network warnings; 17 community records have 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| review-communities Completeness Score rubric across all 526 records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000069, CommunityMech:000091, CommunityMech:000153, CommunityMech:000181, CommunityMech:000213, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:ISOLATES:RHIZOSPHERE, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | Computed proportional 100-point review-communities Completeness Score (min 50, median 93, mean 91.3, max 100 across 524 MicrobialCommunity records; 100/100 across 2 CommonTaxon files; 000069=100/100, 000181=96/100, 000213=100/100; scripts/audit_completeness.py scores 90, 95, and 85; review-communities s_ab abundance_level rubric component is 0/5 on 000069, 000181, and 000213 due to missing taxon abundance_level) and verified causal graph and reusable taxon coverage across all 22 cohorts. |

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

completeness: concern. Targets: cohort:BIOREMEDIATION, CommunityMech:000181.

Cohort BIOREMEDIATION comprises 93 records (329 taxa, 230 ecological interactions, 89 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon links) with mean Completeness Score 91.99/100 (min 60/100).

Reviewed member records (93): CommunityMech:000004, CommunityMech:000024, CommunityMech:000030, CommunityMech:000038, CommunityMech:000042, CommunityMech:000044, CommunityMech:000051, CommunityMech:000060, CommunityMech:000111, CommunityMech:000112, CommunityMech:000113, CommunityMech:000114, CommunityMech:000115, CommunityMech:000116, CommunityMech:000121, CommunityMech:000132, CommunityMech:000136, CommunityMech:000138, CommunityMech:000163, CommunityMech:000166, CommunityMech:000176, CommunityMech:000181, CommunityMech:000183, CommunityMech:000184, CommunityMech:000199, CommunityMech:000200, CommunityMech:000209, CommunityMech:000238, CommunityMech:000239, CommunityMech:000271, CommunityMech:000285, CommunityMech:000289, CommunityMech:000291, CommunityMech:000292, CommunityMech:000299, CommunityMech:000300, CommunityMech:000301, CommunityMech:000324, CommunityMech:000328, CommunityMech:000331, CommunityMech:000334, CommunityMech:000335, CommunityMech:000340, CommunityMech:000342, CommunityMech:000344, CommunityMech:000352, CommunityMech:000358, CommunityMech:000361, CommunityMech:000362, CommunityMech:000369, CommunityMech:000370, CommunityMech:000371, CommunityMech:000374, CommunityMech:000379, CommunityMech:000384, CommunityMech:000386, CommunityMech:000387, CommunityMech:000388, CommunityMech:000405, CommunityMech:000406, CommunityMech:000410, CommunityMech:000411, CommunityMech:000413, CommunityMech:000420, CommunityMech:000424, CommunityMech:000426, CommunityMech:000437, CommunityMech:000439, CommunityMech:000440, CommunityMech:000442, CommunityMech:000444, CommunityMech:000454, CommunityMech:000461, CommunityMech:000462, CommunityMech:000463, CommunityMech:000470, CommunityMech:000471, CommunityMech:000476, CommunityMech:000479, CommunityMech:000482, CommunityMech:000484, CommunityMech:000493, CommunityMech:000498, CommunityMech:000499, CommunityMech:000500, CommunityMech:000502, CommunityMech:000503, CommunityMech:000504, CommunityMech:000505, CommunityMech:000506, CommunityMech:000507, CommunityMech:000508, CommunityMech:000509.

### Cohort review of BIOTECHNOLOGY (98 records)

completeness: concern. Targets: cohort:BIOTECHNOLOGY, CommunityMech:000091, CommunityMech:000153, CommunityMech:000213, CommunityMech:000295.

Cohort BIOTECHNOLOGY comprises 98 records (310 taxa, 263 ecological interactions, 96 downstream causal edges, 0 inline UniProtKB gene annotations, 8 reusable CommonTaxon links) with mean Completeness Score 89.91/100 (min 50/100).

Reviewed member records (98): CommunityMech:000009, CommunityMech:000029, CommunityMech:000036, CommunityMech:000091, CommunityMech:000092, CommunityMech:000117, CommunityMech:000126, CommunityMech:000139, CommunityMech:000146, CommunityMech:000149, CommunityMech:000151, CommunityMech:000152, CommunityMech:000153, CommunityMech:000154, CommunityMech:000164, CommunityMech:000165, CommunityMech:000167, CommunityMech:000170, CommunityMech:000171, CommunityMech:000172, CommunityMech:000173, CommunityMech:000175, CommunityMech:000177, CommunityMech:000185, CommunityMech:000198, CommunityMech:000202, CommunityMech:000203, CommunityMech:000204, CommunityMech:000207, CommunityMech:000210, CommunityMech:000211, CommunityMech:000213, CommunityMech:000214, CommunityMech:000241, CommunityMech:000244, CommunityMech:000266, CommunityMech:000269, CommunityMech:000278, CommunityMech:000279, CommunityMech:000283, CommunityMech:000284, CommunityMech:000287, CommunityMech:000294, CommunityMech:000295, CommunityMech:000306, CommunityMech:000326, CommunityMech:000329, CommunityMech:000330, CommunityMech:000332, CommunityMech:000333, CommunityMech:000343, CommunityMech:000345, CommunityMech:000354, CommunityMech:000355, CommunityMech:000356, CommunityMech:000357, CommunityMech:000359, CommunityMech:000363, CommunityMech:000365, CommunityMech:000366, CommunityMech:000372, CommunityMech:000378, CommunityMech:000390, CommunityMech:000395, CommunityMech:000397, CommunityMech:000399, CommunityMech:000400, CommunityMech:000402, CommunityMech:000408, CommunityMech:000412, CommunityMech:000415, CommunityMech:000417, CommunityMech:000418, CommunityMech:000422, CommunityMech:000425, CommunityMech:000430, CommunityMech:000431, CommunityMech:000433, CommunityMech:000434, CommunityMech:000435, CommunityMech:000436, CommunityMech:000438, CommunityMech:000445, CommunityMech:000447, CommunityMech:000448, CommunityMech:000449, CommunityMech:000450, CommunityMech:000453, CommunityMech:000455, CommunityMech:000457, CommunityMech:000465, CommunityMech:000478, CommunityMech:000480, CommunityMech:000481, CommunityMech:000496, CommunityMech:000497, CommunityMech:000517, CommunityMech:000522.

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

### Cohort review of ISOLATES:RHIZOSPHERE (1 records)

completeness: supported. Targets: cohort:ISOLATES:RHIZOSPHERE.

Cohort ISOLATES:RHIZOSPHERE comprises 1 records (1 taxa, 3 ecological interactions, 0 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 94.00/100 (min 94/100).

Reviewed member records (1): CommunityMech:000521.

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

### Cohort review of SYNTROPHY (37 records)

completeness: concern. Targets: cohort:SYNTROPHY, CommunityMech:000069.

Cohort SYNTROPHY comprises 37 records (90 taxa, 117 ecological interactions, 67 downstream causal edges, 0 inline UniProtKB gene annotations, 2 reusable CommonTaxon links) with mean Completeness Score 96.27/100 (min 84/100).

Reviewed member records (37): CommunityMech:000006, CommunityMech:000007, CommunityMech:000008, CommunityMech:000018, CommunityMech:000023, CommunityMech:000031, CommunityMech:000052, CommunityMech:000053, CommunityMech:000068, CommunityMech:000069, CommunityMech:000070, CommunityMech:000071, CommunityMech:000134, CommunityMech:000141, CommunityMech:000142, CommunityMech:000148, CommunityMech:000150, CommunityMech:000157, CommunityMech:000158, CommunityMech:000186, CommunityMech:000187, CommunityMech:000188, CommunityMech:000189, CommunityMech:000190, CommunityMech:000276, CommunityMech:000288, CommunityMech:000290, CommunityMech:000307, CommunityMech:000327, CommunityMech:000336, CommunityMech:000337, CommunityMech:000350, CommunityMech:000469, CommunityMech:000475, CommunityMech:000510, CommunityMech:000511, CommunityMech:000512.

### Cohort review of TAXA (2 records)

completeness: supported. Targets: cohort:TAXA.

Cohort TAXA comprises 2 records (2 taxa, 0 ecological interactions, 0 downstream causal edges, 9 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 100.00/100 (min 100/100).

Reviewed member records (2): CommunityMech:taxon:000001, CommunityMech:taxon:000002.

## Findings

### c11s4-000069-syntrophobacter-methanospirillum-abundance-levels: Both obligate syntrophic coculture partners in Syntrophobacter_Methanospirillum_Syntrophy (CommunityMech:000069) omit abundance_level despite defined two-member coculture support in PMID:9828440

major / open / confirmed; issue key: c11s4-000069-syntrophobacter-methanospirillum-abundance-levels.

In kb/communities/Syntrophobacter_Methanospirillum_Syntrophy.yaml (CommunityMech:000069), both Syntrophobacter fumaroxidans (taxonomy[0], NCBITaxon:119484, functional_role: [PRIMARY_DEGRADER, SYNTROPHIC_PARTNER]) and Methanospirillum hungatei (taxonomy[1], NCBITaxon:2203, functional_role: [SYNTROPHIC_PARTNER]) omit abundance_level. The cited primary study (PMID:9828440, doi:10.1099/00207713-48-4-1383) explicitly establishes that 'It oxidized propionate syntrophically in co-culture with the hydrogen- and formate-utilizing Methanospirillum hungateii, and was able to oxidize propionate and other organic compounds in pure culture with sulfate or fumarate as the electron acceptor.' Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1] raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

### c11s4-000181-pseudomonas-rhodococcus-abundance-levels: Both chloronitrobenzene-degrading coculture partners in Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture (CommunityMech:000181) omit abundance_level despite defined two-strain coculture support in PMID:10049867

major / open / confirmed; issue key: c11s4-000181-pseudomonas-rhodococcus-abundance-levels.

In kb/communities/Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture.yaml (CommunityMech:000181), both Pseudomonas putida HS12 (taxonomy[0], NCBITaxon:303, functional_role: [PRIMARY_DEGRADER]) and Rhodococcus sp. strain HS51 (taxonomy[1], NCBITaxon:1827, functional_role: [CROSS_FEEDER, PRIMARY_DEGRADER]) omit abundance_level. The cited primary study (PMID:10049867, doi:10.1128/AEM.65.3.1083-1091.1999) explicitly establishes that 'For the degradation of CNBs, Rhodococcus sp. strain HS51, which degrades 4- and 5-chloro-2-hydroxyacetanilides, was isolated and combined with P. putida HS12 to give a coculture. This coculture was confirmed to mineralize 3- and 4-CNBs in the presence of an additional carbon source.' Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1] raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

### c11s4-000213-variovorax-cryptococcus-abundance-levels: Both vitamin cross-feeding mutualism partners in Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm (CommunityMech:000213) omit abundance_level despite defined two-member coculture support in PMID:37553333

major / open / confirmed; issue key: c11s4-000213-variovorax-cryptococcus-abundance-levels.

In kb/communities/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm.yaml (CommunityMech:000213), both Variovorax species (taxonomy[0], NCBITaxon:34072, functional_role: [CROSS_FEEDER, PRIMARY_PRODUCER]) and Cryptococcus yeast (taxonomy[1], NCBITaxon:5206, functional_role: [CROSS_FEEDER, PRIMARY_PRODUCER]) omit abundance_level. The cited primary study (PMID:37553333, doi:10.1038/s41467-023-40360-4) explicitly establishes that 'predict that a Variovorax species is a hub as an important source of thiamine. Quantification of thiamine during the growth of Variovorax in minimal media show high levels of thiamine production, up to 100 mg/L. A few of the correlated thiamine auxotrophs are predicted to produce pantothenate, which we show is required for growth of Variovorax, supporting that a subset of vitamin-dependent interactions are mutualistic. A Cryptococcus yeast produces the B-vitamin pantothenate, and co-culturing with Variovorax leads to a 90-130-fold fitness increase for both organisms.' Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1] raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

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

### act-populate-syntrophobacter-methanospirillum-abundance-levels

Add abundance_level: DOMINANT to both Syntrophobacter fumaroxidans (taxonomy[0], NCBITaxon:119484) and Methanospirillum hungatei (taxonomy[1], NCBITaxon:2203) backed by PMID:9828440 (doi:10.1099/00207713-48-4-1383) on CommunityMech:000069, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Syntrophobacter_Methanospirillum_Syntrophy.yaml
- just validate-history history

### act-populate-pseudomonas-rhodococcus-abundance-levels

Add abundance_level: DOMINANT to both Pseudomonas putida HS12 (taxonomy[0], NCBITaxon:303) and Rhodococcus sp. strain HS51 (taxonomy[1], NCBITaxon:1827) backed by PMID:10049867 (doi:10.1128/AEM.65.3.1083-1091.1999) on CommunityMech:000181, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture.yaml
- just validate-history history

### act-populate-variovorax-cryptococcus-abundance-levels

Add abundance_level: DOMINANT to both Variovorax species (taxonomy[0], NCBITaxon:34072) and Cryptococcus yeast (taxonomy[1], NCBITaxon:5206) backed by PMID:37553333 (doi:10.1038/s41467-023-40360-4) on CommunityMech:000213, and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm.yaml
- just validate-history history

### act-defer-source-limited-fulltext-findings-c11s4

Retain source-limited full-text findings until open-access full text or supplementary strain/assay tables become available for CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify full-text table availability before modifying abstract-grounded claims on source-limited records.

## Category Boundaries

- split: CommunityMech:000048, CommunityMech:000054, CommunityMech:000069, CommunityMech:000091, CommunityMech:000153, CommunityMech:000181, CommunityMech:000213, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:ISOLATES:RHIZOSPHERE, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA. The full 526-record CommunityMech corpus spans 3 record roots (kb/communities/, data/isolates/, kb/taxa/) and 16 ecological categories, which is over-broad for a single unpartitioned cohort. Splitting by root and community_category yields 22 disjoint, ecologically coherent cohorts (16 community cohorts, 5 isolate cohorts, and 1 TAXA cohort) for comparative rubric evaluation.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and CommonTaxon classes | supports | All 510 kb/communities/*.yaml, 14 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records (526 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | scripts/audit_completeness.py; 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness() across all 526 records | supports | Proportional 100-point review-communities Completeness Score audit across all 524 MicrobialCommunity records (min 50, median 93, mean 91.3, max 100; CommunityMech:000069 = 100/100, CommunityMech:000181 = 96/100, CommunityMech:000213 = 100/100) and 2 CommonTaxon files (100/100) confirmed 100% core metadata presence and 100% top-level environment_term coverage (524/524), while scripts/audit_completeness.py:calculate_completeness() scores 000069 at 90/100, 000181 at 95/100, and 000213 at 85/100. |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | NetworkIntegrityAuditor across 510 kb/communities and 14 data/isolates records found 493/510 communities and 14/14 isolates with 0 warnings (including all 24/24 MicrobialCommunity records in the 26-record deep audit) and 17 community records with 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-525 | supports | Corpus-wide causal graph inventory covers all 524 MicrobialCommunity records (510 kb/communities/*.yaml and 14 data/isolates/*.yaml) through CommunityMech:000530 with 100% SHA-256 attestation in verify_causal_graph_reviews.py after Cycle 11 Stage 2 (#2729). |
| ev-common-taxon-linkage-audit | kb/taxa/Shewanella_oneidensis_MR1.yaml; TaxonomicComposition.common_taxon cross-references and kb/taxa/*.yaml EvidenceItem entries | supports | Corpus-wide audit of reusable taxon cross-references confirmed 22 TaxonomicComposition.common_taxon links across 21 MicrobialCommunity records (20 kb/communities/*.yaml records and 1 data/isolates/*.yaml record: 6 Geobacter sulfurreducens communities linked to CommunityMech:taxon:000002 [4 reusable UniProt EET genes with 27 verified EvidenceItems] and 15 Shewanella oneidensis communities plus isolate baseline CommunityMech:000524 linked to CommunityMech:taxon:000001 [5 reusable UniProt EET genes with 34 verified EvidenceItems], with CommunityMech:000177 linking to both) after Cycle 11 Stage 3 (#2730). |
| ev-syntrophobacter-methanospirillum-pmid9828440 | PMID:9828440; kb/communities/Syntrophobacter_Methanospirillum_Syntrophy.yaml | supports | PMID:9828440 (doi:10.1099/00207713-48-4-1383) establishes that Syntrophobacter fumaroxidans (NCBITaxon:119484) and Methanospirillum hungatei (NCBITaxon:2203) form a defined two-member syntrophic propionate-oxidizing co-culture. |
| ev-pseudomonas-rhodococcus-pmid10049867 | PMID:10049867; kb/communities/Pseudomonas_Rhodococcus_Chloronitrobenzene_Coculture.yaml | supports | PMID:10049867 (doi:10.1128/AEM.65.3.1083-1091.1999) establishes that Pseudomonas putida HS12 (NCBITaxon:303) and Rhodococcus sp. strain HS51 (NCBITaxon:1827) form a defined two-strain coculture that mineralizes 3- and 4-chloronitrobenzene. |
| ev-variovorax-cryptococcus-pmid37553333 | PMID:37553333; kb/communities/Variovorax_Cryptococcus_Vitamin_Mutualism_Microcosm.yaml | supports | PMID:37553333 (doi:10.1038/s41467-023-40360-4) establishes that thiamine-producing, pantothenate-requiring Variovorax species (NCBITaxon:34072) and pantothenate-producing, thiamine-auxotrophic Cryptococcus yeast (NCBITaxon:5206) form a defined two-member vitamin cross-feeding mutualism. |
| ev-prior-structured-reviews | reviews/structured; 265 retained structured review bundles through 20261107T202000Z-c10s5-remediation-verification-r2 | context_only | Lineage inspection of all 265 prior structured reviews and Cycle 10 Stage 5 evidence.yaml confirmed that all 3 Cycle 10 Stage 4 open findings across CommunityMech:000052, 000092, and 000162 were resolved in Cycle 10 Stage 5 (#2723, PR #2724) and 7 record-scoped source-limited findings remain deferred at commit e9ada20c23b553a0328f8d0601b46ab8fcb906f3. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Seven carried-forward community records remain source-limited because cached abstracts do not provide full-text assay or strain tables (#765, #1467, #1657, #1681, #1699, #1841, #1847).

## Structured Review Bundles And Machine-Readable Artifacts

- Full-corpus cohort review bundle: `reviews/structured/20261108T121500Z-c11s4-frozen-cohort-review/review.yaml`
- Per-record deep audit bundle: `reviews/structured/20261108T121400Z-c11s4-record-deep-audit/review.yaml`
- Workflow findings manifest: `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/review_findings.yaml`
- Frozen 526-record inventory metrics and SHA-256 digests: `reviews/workflow/mech-goal-sequence-20261019/cycle-000011/stage-04/revision-0001/frozen_inventory_metrics.tsv`
