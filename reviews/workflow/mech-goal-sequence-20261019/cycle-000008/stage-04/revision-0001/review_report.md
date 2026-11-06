# Cycle 8 Stage 4 Full-Corpus Frozen Inventory and Cohort Review (512 Records Across 21 Cohorts)

- Review: 20261106T094100Z-c8s4-frozen-cohort-review
- Repository: CultureBotAI/CommunityMech
- Started UTC: 2026-11-06T09:32:00Z
- Finished UTC: 2026-11-06T09:41:00Z
- Reviewer: antigravity-c8s4-cohort-reviewer (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full-corpus frozen inventory and cohort review of all 512 eligible CommunityMech records (501 kb/communities/*.yaml, 9 data/isolates/*.yaml, 2 kb/taxa/*.yaml) partitioned into 21 disjoint domain cohorts at commit 36fdbffc2427cfb3291b442cbaeda47a312ba55b. All 512 records pass LinkML schema validation, ontology ID-label verification, and verbatim snippet checks; mean Completeness Score across 510 MicrobialCommunity records is 91.23/100 (median 90/100), with 100% top-level environment_term coverage (510/510) and 100% reusable CommonTaxon linkage (15/15 matching Shewanella oneidensis and Geobacter sulfurreducens occurrences). Three actionable open P2 findings across 3 community records (CommunityMech:000210, 000359, 000454) and 7 carried-forward source-limited deferred findings are preserved for Cycle 8 Stage 5 grouped remediation.

## Scope And Provenance

Exhaustive cohort review of all 21 domain/root cohorts (encompassing all 512 eligible records across kb/communities/*.yaml, data/isolates/*.yaml, and kb/taxa/*.yaml) plus all 10 finding-bearing records.

Selection: All 21 domain/root cohorts (512 records total; full per-record SHA-256 inventory in frozen_inventory_metrics.tsv) and all 10 finding-bearing records at Git commit 36fdbffc2427cfb3291b442cbaeda47a312ba55b.
Coverage: full; 31 reviewed / 31 in the declared population.
Source: git_commit at Git base 36fdbffc2427cfb3291b442cbaeda47a312ba55b.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| CommunityMech:000048 | kb/communities/Okeke_Lu_Cellulolytic_Consortium.yaml | maintained | CommunityMech:000048 (Okeke-Lu Cellulolytic-Xylanolytic Consortium) |
| CommunityMech:000054 | kb/communities/Phormidium_Alkaline_Consortium.yaml | maintained | CommunityMech:000054 (Phormidium Alkaline Consortium) |
| CommunityMech:000091 | kb/communities/GLBRC_Exometabolite_Transwell_SynCom.yaml | maintained | CommunityMech:000091 (GLBRC Exometabolite Transwell SynCom System) |
| CommunityMech:000153 | kb/communities/Cheese_Rind_InSitu_InVitro_Model_Community.yaml | maintained | CommunityMech:000153 (Cheese Rind In Situ-In Vitro Model Community) |
| CommunityMech:000210 | kb/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml | maintained | CommunityMech:000210 (Zymomonas-E. coli Exometabolomics-Designed Obligate Mutualism) |
| CommunityMech:000222 | kb/communities/Sulfide_Spring_Autotrophic_CPR_Biofilm.yaml | maintained | CommunityMech:000222 (Sulfide Spring Autotrophic CPR-Hosting Biofilm) |
| CommunityMech:000295 | kb/communities/Parachlorella_Saccharomyces_Mutualistic_Coculture.yaml | maintained | CommunityMech:000295 (Parachlorella kessleri + Saccharomyces cerevisiae Mutualistic Co-culture) |
| CommunityMech:000302 | kb/communities/SynCom_MetG2_Rhizobacteria_Sugarcane_Stress_Resilience.yaml | maintained | CommunityMech:000302 (SynCom MetG2 Rhizobacteria Sugarcane Stress Resilience) |
| CommunityMech:000359 | kb/communities/PPHET_Hybrid_Photosynthetic_PHB_Microbiome.yaml | maintained | CommunityMech:000359 (PPHET Hybrid Photosynthetic PHB Microbiome) |
| CommunityMech:000454 | kb/communities/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture.yaml | maintained | CommunityMech:000454 (Thermoleptolyngbya-Chelatococcus Arsenic Detoxification Coculture) |
| cohort:AMD | kb/communities/AMD_Acidophile_Heterotroph_Network.yaml # cohort=AMD;records=7 | snapshot_row | AMD cohort (7 records) |
| cohort:BIOMINING | kb/communities/Bayan_Obo_REE_Tailings_Consortium.yaml # cohort=BIOMINING;records=17 | snapshot_row | BIOMINING cohort (17 records) |
| cohort:BIOREMEDIATION | kb/communities/Australian_Lead_Zinc_Polymetallic.yaml # cohort=BIOREMEDIATION;records=93 | snapshot_row | BIOREMEDIATION cohort (93 records) |
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
| cohort:OTHER | kb/communities/BioModels_MODEL2209060002_DPigrum_SAureus_Community.yaml # cohort=OTHER;records=45 | snapshot_row | OTHER cohort (45 records) |
| cohort:PHAGE_PREDATION | kb/communities/Alseth_FourSpecies_Pathogen_Phage_Community.yaml # cohort=PHAGE_PREDATION;records=2 | snapshot_row | PHAGE_PREDATION cohort (2 records) |
| cohort:PHYTOPLANKTON | kb/communities/Chlamydomonas_Bacterial_H2_Consortium.yaml # cohort=PHYTOPLANKTON;records=19 | snapshot_row | PHYTOPLANKTON cohort (19 records) |
| cohort:RHIZOSPHERE | kb/communities/At_RSPHERE_SynCom.yaml # cohort=RHIZOSPHERE;records=84 | snapshot_row | RHIZOSPHERE cohort (84 records) |
| cohort:SYNTROPHY | kb/communities/BioModels_MODEL1806250003_Spittlebug_Sulcia_Sodalis.yaml # cohort=SYNTROPHY;records=37 | snapshot_row | SYNTROPHY cohort (37 records) |
| cohort:TAXA | kb/taxa/Shewanella_oneidensis_MR1.yaml # cohort=TAXA;records=2 | snapshot_row | TAXA cohort (2 records) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation across all 512 records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000210, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000359, CommunityMech:000454, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | All 510 MicrobialCommunity records and 2 CommonTaxon files pass LinkML schema validation with 0 errors and 100% EvidenceItem.evidence_source enum compliance. |
| NetworkIntegrityAuditor check across kb/communities/ and data/isolates/ | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000210, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000359, CommunityMech:000454, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | 484/501 community records and 9/9 isolate records have 0 network warnings; 17 community records have 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| review-communities Completeness Score rubric across all 512 records | passed | True | CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000210, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000359, CommunityMech:000454, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA | Computed proportional 100-point review-communities Completeness Score (min 40, median 90, mean 91.23, max 100 across 510 MicrobialCommunity records; 100/100 across 2 CommonTaxon files; 000210=98/100, 000359=94/100, 000454=90/100; scripts/audit_completeness.py scores 85, 90, and 60; review-communities s_ab abundance_level rubric component is 0/5 on 000210 and 2.5/5 on 000359 and 000454 due to missing taxon abundance_level) and verified causal graph and reusable taxon coverage across all 21 cohorts. |

## Scientific And Domain Assessments

### Cohort review of AMD (7 records)

completeness: supported. Targets: cohort:AMD.

Cohort AMD comprises 7 records (34 taxa, 29 ecological interactions, 8 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 94.00/100 (min 91/100).

Reviewed member records (7): CommunityMech:000001, CommunityMech:000002, CommunityMech:000027, CommunityMech:000034, CommunityMech:000059, CommunityMech:000074, CommunityMech:000353.

### Cohort review of BIOMINING (17 records)

completeness: supported. Targets: cohort:BIOMINING.

Cohort BIOMINING comprises 17 records (54 taxa, 58 ecological interactions, 26 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon links) with mean Completeness Score 92.53/100 (min 75/100).

Reviewed member records (17): CommunityMech:000005, CommunityMech:000019, CommunityMech:000026, CommunityMech:000035, CommunityMech:000045, CommunityMech:000049, CommunityMech:000057, CommunityMech:000073, CommunityMech:000217, CommunityMech:000303, CommunityMech:000305, CommunityMech:000385, CommunityMech:000404, CommunityMech:000485, CommunityMech:000486, CommunityMech:000487, CommunityMech:000491.

### Cohort review of BIOREMEDIATION (93 records)

completeness: concern. Targets: cohort:BIOREMEDIATION, CommunityMech:000454.

Cohort BIOREMEDIATION comprises 93 records (329 taxa, 230 ecological interactions, 89 downstream causal edges, 0 inline UniProtKB gene annotations, 1 reusable CommonTaxon links) with mean Completeness Score 91.99/100 (min 60/100).

Reviewed member records (93): CommunityMech:000004, CommunityMech:000024, CommunityMech:000030, CommunityMech:000038, CommunityMech:000042, CommunityMech:000044, CommunityMech:000051, CommunityMech:000060, CommunityMech:000111, CommunityMech:000112, CommunityMech:000113, CommunityMech:000114, CommunityMech:000115, CommunityMech:000116, CommunityMech:000121, CommunityMech:000132, CommunityMech:000136, CommunityMech:000138, CommunityMech:000163, CommunityMech:000166, CommunityMech:000176, CommunityMech:000181, CommunityMech:000183, CommunityMech:000184, CommunityMech:000199, CommunityMech:000200, CommunityMech:000209, CommunityMech:000238, CommunityMech:000239, CommunityMech:000271, CommunityMech:000285, CommunityMech:000289, CommunityMech:000291, CommunityMech:000292, CommunityMech:000299, CommunityMech:000300, CommunityMech:000301, CommunityMech:000324, CommunityMech:000328, CommunityMech:000331, CommunityMech:000334, CommunityMech:000335, CommunityMech:000340, CommunityMech:000342, CommunityMech:000344, CommunityMech:000352, CommunityMech:000358, CommunityMech:000361, CommunityMech:000362, CommunityMech:000369, CommunityMech:000370, CommunityMech:000371, CommunityMech:000374, CommunityMech:000379, CommunityMech:000384, CommunityMech:000386, CommunityMech:000387, CommunityMech:000388, CommunityMech:000405, CommunityMech:000406, CommunityMech:000410, CommunityMech:000411, CommunityMech:000413, CommunityMech:000420, CommunityMech:000424, CommunityMech:000426, CommunityMech:000437, CommunityMech:000439, CommunityMech:000440, CommunityMech:000442, CommunityMech:000444, CommunityMech:000454, CommunityMech:000461, CommunityMech:000462, CommunityMech:000463, CommunityMech:000470, CommunityMech:000471, CommunityMech:000476, CommunityMech:000479, CommunityMech:000482, CommunityMech:000484, CommunityMech:000493, CommunityMech:000498, CommunityMech:000499, CommunityMech:000500, CommunityMech:000502, CommunityMech:000503, CommunityMech:000504, CommunityMech:000505, CommunityMech:000506, CommunityMech:000507, CommunityMech:000508, CommunityMech:000509.

### Cohort review of BIOTECHNOLOGY (96 records)

completeness: concern. Targets: cohort:BIOTECHNOLOGY, CommunityMech:000091, CommunityMech:000153, CommunityMech:000210, CommunityMech:000295, CommunityMech:000359.

Cohort BIOTECHNOLOGY comprises 96 records (304 taxa, 255 ecological interactions, 96 downstream causal edges, 0 inline UniProtKB gene annotations, 8 reusable CommonTaxon links) with mean Completeness Score 90.01/100 (min 50/100).

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

### Cohort review of RHIZOSPHERE (84 records)

completeness: concern. Targets: cohort:RHIZOSPHERE, CommunityMech:000302.

Cohort RHIZOSPHERE comprises 84 records (447 taxa, 266 ecological interactions, 86 downstream causal edges, 0 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 87.17/100 (min 55/100).

Reviewed member records (84): CommunityMech:000003, CommunityMech:000022, CommunityMech:000025, CommunityMech:000028, CommunityMech:000039, CommunityMech:000040, CommunityMech:000043, CommunityMech:000047, CommunityMech:000050, CommunityMech:000058, CommunityMech:000063, CommunityMech:000064, CommunityMech:000072, CommunityMech:000076, CommunityMech:000077, CommunityMech:000078, CommunityMech:000079, CommunityMech:000087, CommunityMech:000088, CommunityMech:000090, CommunityMech:000094, CommunityMech:000095, CommunityMech:000096, CommunityMech:000097, CommunityMech:000098, CommunityMech:000099, CommunityMech:000100, CommunityMech:000101, CommunityMech:000102, CommunityMech:000103, CommunityMech:000104, CommunityMech:000105, CommunityMech:000106, CommunityMech:000107, CommunityMech:000108, CommunityMech:000109, CommunityMech:000110, CommunityMech:000129, CommunityMech:000216, CommunityMech:000221, CommunityMech:000225, CommunityMech:000235, CommunityMech:000236, CommunityMech:000245, CommunityMech:000247, CommunityMech:000250, CommunityMech:000272, CommunityMech:000280, CommunityMech:000302, CommunityMech:000304, CommunityMech:000310, CommunityMech:000311, CommunityMech:000312, CommunityMech:000313, CommunityMech:000314, CommunityMech:000316, CommunityMech:000341, CommunityMech:000347, CommunityMech:000348, CommunityMech:000367, CommunityMech:000368, CommunityMech:000373, CommunityMech:000375, CommunityMech:000376, CommunityMech:000391, CommunityMech:000393, CommunityMech:000403, CommunityMech:000409, CommunityMech:000414, CommunityMech:000419, CommunityMech:000427, CommunityMech:000428, CommunityMech:000429, CommunityMech:000456, CommunityMech:000458, CommunityMech:000459, CommunityMech:000460, CommunityMech:000472, CommunityMech:000477, CommunityMech:000483, CommunityMech:000501, CommunityMech:000513, CommunityMech:000514, CommunityMech:000516.

### Cohort review of SYNTROPHY (37 records)

completeness: supported. Targets: cohort:SYNTROPHY.

Cohort SYNTROPHY comprises 37 records (90 taxa, 117 ecological interactions, 67 downstream causal edges, 0 inline UniProtKB gene annotations, 2 reusable CommonTaxon links) with mean Completeness Score 96.27/100 (min 84/100).

Reviewed member records (37): CommunityMech:000006, CommunityMech:000007, CommunityMech:000008, CommunityMech:000018, CommunityMech:000023, CommunityMech:000031, CommunityMech:000052, CommunityMech:000053, CommunityMech:000068, CommunityMech:000069, CommunityMech:000070, CommunityMech:000071, CommunityMech:000134, CommunityMech:000141, CommunityMech:000142, CommunityMech:000148, CommunityMech:000150, CommunityMech:000157, CommunityMech:000158, CommunityMech:000186, CommunityMech:000187, CommunityMech:000188, CommunityMech:000189, CommunityMech:000190, CommunityMech:000276, CommunityMech:000288, CommunityMech:000290, CommunityMech:000307, CommunityMech:000327, CommunityMech:000336, CommunityMech:000337, CommunityMech:000350, CommunityMech:000469, CommunityMech:000475, CommunityMech:000510, CommunityMech:000511, CommunityMech:000512.

### Cohort review of TAXA (2 records)

completeness: supported. Targets: cohort:TAXA.

Cohort TAXA comprises 2 records (2 taxa, 0 ecological interactions, 0 downstream causal edges, 9 inline UniProtKB gene annotations, 0 reusable CommonTaxon links) with mean Completeness Score 100.00/100 (min 100/100).

Reviewed member records (2): CommunityMech:taxon:000001, CommunityMech:taxon:000002.

## Findings

### c8s4-000210-zymomonas-ecoli-abundance-levels: Both obligate mutualist partners in Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism (CommunityMech:000210) omit abundance_level despite defined two-member coculture support in PMID:26885935

major / open / confirmed; issue key: c8s4-000210-zymomonas-ecoli-abundance-levels.

In kb/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml (CommunityMech:000210), both Zymomonas mobilis (taxonomy[0], NCBITaxon:542, strain ZM4 ZMO0748 cysteine synthase mutant, functional_role: [CROSS_FEEDER]) and Escherichia coli (taxonomy[1], NCBITaxon:562, strain BW25113 Keio amino-acid auxotrophs proA, pheA, and ilvA, functional_role: [CROSS_FEEDER]) omit abundance_level. The cited study (PMID:26885935, doi:10.1021/acssynbio.5b00236) explicitly reports that 'Three sets of cocultures between the Z. mobilis auxotroph and each of the three E. coli auxotrophs were monitored by optical density for growth and analyzed by flow cytometry to confirm high cell counts for each species.' Setting abundance_level: DOMINANT on both taxonomy[0] and taxonomy[1] while preserving discussions[0] (zymomonas_sulfur_identity_and_release_routes) raises the review-communities s_ab abundance_level rubric component from 0/5 to 5/5 (0/2 -&gt; 2/2 taxa with abundance_level).

### c8s4-000359-pphet-heterotroph-abundance-level: Non-cyanobacterial WCRM heterotrophs (taxonomy[1]) in PPHET_Hybrid_Photosynthetic_PHB_Microbiome (CommunityMech:000359) omit abundance_level despite 16S community-composition support in PMID:41559821

major / open / confirmed; issue key: c8s4-000359-pphet-heterotroph-abundance-level.

In kb/communities/PPHET_Hybrid_Photosynthetic_PHB_Microbiome.yaml (CommunityMech:000359), Synechocystis sp. PCC 6803 PPT1 (taxonomy[0], NCBITaxon:1148, functional_role: [PRIMARY_PRODUCER]) carries abundance_level: DOMINANT, whereas its co-cultivated heterotrophic partner fraction non-cyanobacterial WCRM heterotrophs (taxonomy[1], NCBITaxon:2, functional_role: [CROSS_FEEDER]) omits abundance_level. The cited open-access study (PMID:41559821, PMC12819161, doi:10.1111/1751-7915.70302) explicitly reports that 'At the phylum level, both were dominated by Cyanobacteria, Proteobacteria, and Bacteroidota, with Cyanobacteria representing ~70% of the total community (Figure  2a ).' Setting abundance_level: ABUNDANT on taxonomy[1] (~30% non-cyanobacterial Proteobacteria/Bacteroidota heterotrophic fraction) while preserving discussions[0] (DISCUSSION-PPHET-OXYGEN-SCAVENGING) and discussions[1] (phb-production-assay-boundaries) raises the review-communities s_ab abundance_level rubric component from 2.5/5 to 5/5 (1/2 -&gt; 2/2 taxa with abundance_level).

### c8s4-000454-thermoleptolyngbya-chelatococcus-abundance-level: Chelatococcus sp. XZ-Ab1 (taxonomy[1]) in Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture (CommunityMech:000454) omits abundance_level despite defined two-member co-culture support in PMID:42468699

major / open / confirmed; issue key: c8s4-000454-thermoleptolyngbya-chelatococcus-abundance-level.

In kb/communities/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture.yaml (CommunityMech:000454), Thermoleptolyngbya sichuanensis XZ-Cy5 (taxonomy[0], NCBITaxon:3031812, functional_role: [PRIMARY_PRODUCER]) carries abundance_level: DOMINANT, whereas its paired arsenite-oxidizing mutualistic partner Chelatococcus sp. XZ-Ab1 (taxonomy[1], NCBITaxon:3034027, functional_role: [CROSS_FEEDER]) omits abundance_level. The cited study (PMID:42468699, doi:10.1016/j.biortech.2026.135440) explicitly establishes the two-strain mutualistic co-culture ('A co-culture system demonstrated mutualistic interactions where "T. sichuanensis" XZ-Cy5 secreted organic carbon to facilitate heterotrophic growth of Chelatococcus sp. XZ-Ab1, while Chelatococcus sp. XZ-Ab1 promoted growth of "T. sichuanensis" XZ-Cy5 by oxidizing toxic As(Ⅲ) to the less toxic arsenate.'). Setting abundance_level: DOMINANT on taxonomy[1] while preserving discussions[0] (thermoleptolyngbya_chelatococcus_exact_culture_conditions) and discussions[1] (arsenic_causal_scope_batch120) raises the review-communities s_ab abundance_level rubric component from 2.5/5 to 5/5 (1/2 -&gt; 2/2 taxa with abundance_level).

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

### act-populate-zymomonas-ecoli-abundance-levels

Add abundance_level: DOMINANT to both Zymomonas mobilis (taxonomy[0], NCBITaxon:542) and Escherichia coli (taxonomy[1], NCBITaxon:562) backed by PMID:26885935 (doi:10.1021/acssynbio.5b00236) on CommunityMech:000210 while preserving discussions[0] (zymomonas_sulfur_identity_and_release_routes), and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml
- just validate-history history

### act-populate-pphet-heterotroph-abundance-level

Add abundance_level: ABUNDANT to non-cyanobacterial WCRM heterotrophs (taxonomy[1], NCBITaxon:2) backed by PMID:41559821 (PMC12819161, doi:10.1111/1751-7915.70302) on CommunityMech:000359 while preserving discussions[0] (DISCUSSION-PPHET-OXYGEN-SCAVENGING) and discussions[1] (phb-production-assay-boundaries), and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/PPHET_Hybrid_Photosynthetic_PHB_Microbiome.yaml
- just validate-history history

### act-populate-thermoleptolyngbya-chelatococcus-abundance-level

Add abundance_level: DOMINANT to Chelatococcus sp. XZ-Ab1 (taxonomy[1], NCBITaxon:3034027) backed by PMID:42468699 (doi:10.1016/j.biortech.2026.135440) on CommunityMech:000454 while preserving discussions[0] (thermoleptolyngbya_chelatococcus_exact_culture_conditions) and discussions[1] (arsenic_causal_scope_batch120), and append curation_history.

- uv run linkml-validate --schema src/communitymech/schema/communitymech.yaml --target-class MicrobialCommunity kb/communities/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture.yaml
- just validate-history history

### act-defer-source-limited-fulltext-findings-c8s4

Retain source-limited full-text findings until open-access full text or supplementary strain/assay tables become available for CommunityMech:000048, 000054, 000091, 000153, 000222, 000295, and 000302.

- Verify full-text table availability before modifying abstract-grounded claims on source-limited records.

## Category Boundaries

- split: CommunityMech:000048, CommunityMech:000054, CommunityMech:000091, CommunityMech:000153, CommunityMech:000210, CommunityMech:000222, CommunityMech:000295, CommunityMech:000302, CommunityMech:000359, CommunityMech:000454, cohort:AMD, cohort:BIOMINING, cohort:BIOREMEDIATION, cohort:BIOTECHNOLOGY, cohort:CARBON_SEQUESTRATION, cohort:DIET, cohort:EXTREME_ENVIRONMENT, cohort:ISOLATES:BIOMINING, cohort:ISOLATES:BIOREMEDIATION, cohort:ISOLATES:BIOTECHNOLOGY, cohort:ISOLATES:EXTREME_ENVIRONMENT, cohort:LIGNOCELLULOSE, cohort:METAL_REDUCTION, cohort:METHANOGENESIS, cohort:ORAL, cohort:OTHER, cohort:PHAGE_PREDATION, cohort:PHYTOPLANKTON, cohort:RHIZOSPHERE, cohort:SYNTROPHY, cohort:TAXA. The full 512-record CommunityMech corpus spans 3 record roots (kb/communities/, data/isolates/, kb/taxa/) and 16 ecological categories, which is over-broad for a single unpartitioned cohort. Splitting by root and community_category yields 21 disjoint, ecologically coherent cohorts (16 community cohorts, 4 isolate cohorts, and 1 TAXA cohort) for comparative rubric evaluation.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-schema-validation-gate | src/communitymech/schema/communitymech.yaml; MicrobialCommunity and CommonTaxon classes | supports | All 501 kb/communities/*.yaml, 9 data/isolates/*.yaml, and 2 kb/taxa/*.yaml records (512 total) pass LinkML schema validation with 0 errors and 100% EvidenceSourceEnum compliance. |
| ev-completeness-audit | scripts/audit_completeness.py; 100-point proportional review-communities rubric and scripts/audit_completeness.py:calculate_completeness() across all 512 records | supports | Proportional 100-point review-communities Completeness Score audit across all 510 MicrobialCommunity records (min 40, median 90, mean 91.23, max 100; CommunityMech:000210 = 98/100, CommunityMech:000359 = 94/100, CommunityMech:000454 = 90/100) and 2 CommonTaxon files (100/100) confirmed 100% core metadata presence and 100% top-level environment_term coverage (510/510), while scripts/audit_completeness.py:calculate_completeness() scores 000210 at 85/100, 000359 at 90/100, and 000454 at 60/100. |
| ev-network-integrity-audit | src/communitymech/network/auditor.py; NetworkIntegrityAuditor.audit_all() | supports | NetworkIntegrityAuditor across 501 kb/communities and 9 data/isolates records found 484/501 communities and 9/9 isolates with 0 warnings (including all 24/24 MicrobialCommunity records in the 26-record deep audit) and 17 community records with 48 non-fatal warnings (46 DISCONNECTED across 16 records and 2 COMMUNITY_LEVEL UNKNOWN_TARGET warnings on Sclerotinia_Sclerotia_12Strain_Biocontrol_SynCom; 0 error-severity issues, 0 broken downstream references). |
| ev-causal-inventory | reports/causal_graph_review/inventory.tsv; rows 1-509 | supports | Corpus-wide causal graph inventory covers 508 MicrobialCommunity records through CommunityMech:000514 with 100% SHA-256 attestation in verify_causal_graph_reviews.py; the 2 subsequently merged biocontrol SynCom records (CommunityMech:000515 and 000516, PR #2425) pass schema and NetworkIntegrityAuditor checks with 0 warnings. |
| ev-common-taxon-linkage-audit | kb/taxa/Geobacter_sulfurreducens.yaml; TaxonomicComposition.common_taxon cross-references and kb/taxa/*.yaml EvidenceItem entries | supports | Corpus-wide audit of reusable taxon cross-references confirmed 15 TaxonomicComposition.common_taxon links across kb/communities/*.yaml (6 Geobacter sulfurreducens communities linked to CommunityMech:taxon:000002 [4 reusable UniProt EET genes with 21 verified EvidenceItems plus inline macA/Q749P2] and 9 Shewanella oneidensis communities linked to CommunityMech:taxon:000001 [5 reusable UniProt EET genes with 26 verified EvidenceItems plus inline fccA/Q8EKT2]) after Cycle 8 Stage 3 (#2431). |
| ev-zymomonas-ecoli-pmid26885935 | PMID:26885935; kb/communities/Zymomonas_Ecoli_Exometabolomics_Obligate_Mutualism.yaml | supports | PMID:26885935 (doi:10.1021/acssynbio.5b00236) establishes that Zymomonas mobilis (NCBITaxon:542) and Escherichia coli (NCBITaxon:562) auxotrophs were co-cultivated as a defined two-member obligate mutualism and confirmed by flow cytometry to reach high cell counts for each species. |
| ev-pphet-hybrid-pmid41559821 | PMID:41559821; kb/communities/PPHET_Hybrid_Photosynthetic_PHB_Microbiome.yaml | supports | PMID:41559821 (PMC12819161, doi:10.1111/1751-7915.70302) establishes by 16S rRNA amplicon sequencing that the PPHET hybrid microbiome is dominated by Cyanobacteria (~70%, Synechocystis sp. PCC 6803 PPT1) alongside an abundant (~30%) Proteobacteria and Bacteroidota non-cyanobacterial heterotrophic fraction. |
| ev-thermoleptolyngbya-chelatococcus-pmid42468699 | PMID:42468699; kb/communities/Thermoleptolyngbya_Chelatococcus_Arsenic_Detoxification_Coculture.yaml | supports | PMID:42468699 (doi:10.1016/j.biortech.2026.135440) establishes that Thermoleptolyngbya sichuanensis XZ-Cy5 (NCBITaxon:3031812) and Chelatococcus sp. XZ-Ab1 (NCBITaxon:3034027) form a defined two-member mutualistic arsenic-detoxifying co-culture. |
| ev-prior-structured-reviews | reviews/structured; 150 retained structured review bundles through 20261106T062035Z-pr2043-kefir-state-action-correction | context_only | Lineage inspection of all 150 prior structured reviews and Cycle 7 Stage 5 evidence.yaml confirmed that all 3 Cycle 7 Stage 4 open findings across CommunityMech:000146, 000190, and 000451 were resolved in Cycle 7 Stage 5 (#2120, PR #2121) and 7 record-scoped source-limited findings remain deferred at commit 36fdbffc2427cfb3291b442cbaeda47a312ba55b. |

## Limits And Additional Notes

- Read-only Stage 4 record review; no record YAML files were modified in this stage.
- Seven carried-forward community records remain source-limited because cached abstracts do not provide full-text assay or strain tables (#765, #1467, #1657, #1681, #1699, #1841, #1847).

## Structured Review Bundles And Machine-Readable Artifacts

- Full-corpus cohort review bundle: `reviews/structured/20261106T094100Z-c8s4-frozen-cohort-review/review.yaml`
- Per-record deep audit bundle: `reviews/structured/20261106T094000Z-c8s4-record-deep-audit/review.yaml`
- Workflow findings manifest: `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/review_findings.yaml`
- Frozen 512-record inventory metrics and SHA-256 digests: `reviews/workflow/mech-goal-sequence-20261019/cycle-000008/stage-04/revision-0001/frozen_inventory_metrics.tsv`
